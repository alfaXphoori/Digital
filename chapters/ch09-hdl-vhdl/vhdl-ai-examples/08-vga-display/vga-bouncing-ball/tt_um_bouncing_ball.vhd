library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- TinyTapeout-pinout VGA bouncing-ball demo.
-- A 32x32 white square bounces around the 640x480 visible area, updating
-- position once per frame.
--
-- ui_in[0]   : pause animation
-- ui_in[3:1] : ball colour (R, G, B bit each)
--
-- Inspired by the classic 'first VGA sprite' pattern from FPGA tutorials
-- (Mike Field, Nandland). Original implementation for VHDLive.
entity tt_um_bouncing_ball is
  port (
    clk    : in  std_logic;
    rst_n  : in  std_logic;
    ui_in  : in  std_logic_vector(7 downto 0);
    uo_out : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of tt_um_bouncing_ball is
  constant H_ACT : natural := 640;
  constant V_ACT : natural := 480;
  constant BALL  : natural := 32;

  signal hpos : unsigned(9 downto 0) := (others => '0');
  signal vpos : unsigned(9 downto 0) := (others => '0');
  signal hsync, vsync, vis : std_logic;

  -- Ball top-left position in active-area coords
  signal bx : unsigned(9 downto 0) := to_unsigned(320 - BALL/2, 10);
  signal by : unsigned(9 downto 0) := to_unsigned(240 - BALL/2, 10);
  -- Velocity sign: '0' = moving right/down, '1' = moving left/up
  signal vx_sign : std_logic := '0';
  signal vy_sign : std_logic := '0';
  signal last_vsync : std_logic := '1';

  signal r, g, b : unsigned(1 downto 0);
begin
  -- ── VGA pixel counter ────────────────────────────────────────────────────
  process(clk, rst_n) is
  begin
    if rst_n = '0' then
      hpos <= (others => '0');
      vpos <= (others => '0');
    elsif rising_edge(clk) then
      if hpos = 799 then
        hpos <= (others => '0');
        if vpos = 524 then vpos <= (others => '0');
        else               vpos <= vpos + 1;
        end if;
      else hpos <= hpos + 1;
      end if;
    end if;
  end process;

  hsync <= '0' when hpos < 96 else '1';
  vsync <= '0' when vpos < 2  else '1';
  vis   <= '1' when hpos >= 144 and hpos < 784 and vpos >= 35 and vpos < 515 else '0';

  -- ── Ball physics: advance once per frame on vsync falling edge ───────────
  process(clk, rst_n) is
  begin
    if rst_n = '0' then
      bx <= to_unsigned(320 - BALL/2, 10);
      by <= to_unsigned(240 - BALL/2, 10);
      vx_sign <= '0';
      vy_sign <= '0';
      last_vsync <= '1';
    elsif rising_edge(clk) then
      last_vsync <= vsync;
      if last_vsync = '1' and vsync = '0' and ui_in(0) = '0' then
        -- Horizontal step
        if vx_sign = '0' then       -- moving right
          if bx + BALL >= H_ACT - 1 then
            vx_sign <= '1';
            bx <= bx - 1;
          else
            bx <= bx + 1;
          end if;
        else                         -- moving left
          if bx = 0 then
            vx_sign <= '0';
            bx <= bx + 1;
          else
            bx <= bx - 1;
          end if;
        end if;
        -- Vertical step
        if vy_sign = '0' then       -- moving down
          if by + BALL >= V_ACT - 1 then
            vy_sign <= '1';
            by <= by - 1;
          else
            by <= by + 1;
          end if;
        else                         -- moving up
          if by = 0 then
            vy_sign <= '0';
            by <= by + 1;
          else
            by <= by - 1;
          end if;
        end if;
      end if;
    end if;
  end process;

  -- ── Pixel colour ─────────────────────────────────────────────────────────
  process(vis, hpos, vpos, bx, by, ui_in) is
    variable px : unsigned(9 downto 0);
    variable py : unsigned(9 downto 0);
    variable in_ball : boolean;
  begin
    r <= "00"; g <= "00"; b <= "00";
    if vis = '1' then
      px := hpos - 144;
      py := vpos - 35;
      in_ball := (px >= bx) and (px < bx + BALL) and (py >= by) and (py < by + BALL);
      if in_ball then
        r <= ui_in(1) & ui_in(1);
        g <= ui_in(2) & ui_in(2);
        b <= ui_in(3) & ui_in(3);
      else
        b <= "01";  -- dark blue background
      end if;
    end if;
  end process;

  uo_out <= hsync & b(0) & g(0) & r(0) & vsync & b(1) & g(1) & r(1);
end architecture;
