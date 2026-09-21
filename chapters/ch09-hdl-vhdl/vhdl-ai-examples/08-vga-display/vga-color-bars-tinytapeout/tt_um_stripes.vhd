library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- TinyTapeout-pinout VGA stripes demo.
-- Generates a 640x480 60Hz signal with vertical color bars.
-- Pinout: uo_out = { hsync, B(0), G(0), R(0), vsync, B(1), G(1), R(1) }
entity tt_um_stripes is
  port (
    clk    : in  std_logic;
    rst_n  : in  std_logic;
    ui_in  : in  std_logic_vector(7 downto 0);
    uo_out : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of tt_um_stripes is
  -- VGA 640x480 @ 60Hz timing, 25.175 MHz pixel clock
  -- H: 96 sync + 48 back + 640 active + 16 front = 800
  -- V: 2 sync + 33 back + 480 active + 10 front = 525
  signal hpos  : unsigned(9 downto 0) := (others => '0');
  signal vpos  : unsigned(9 downto 0) := (others => '0');
  signal hsync : std_logic;
  signal vsync : std_logic;
  signal vis   : std_logic;
  signal r, g, b : unsigned(1 downto 0);
begin
  process(clk, rst_n)
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
      else
        hpos <= hpos + 1;
      end if;
    end if;
  end process;

  hsync <= '0' when hpos < 96 else '1';
  vsync <= '0' when vpos < 2  else '1';
  vis   <= '1' when (hpos >= 144 and hpos < 784 and vpos >= 35 and vpos < 515) else '0';

  -- Vertical color bars: 8 bars of 80 px each across 640 active pixels.
  -- Pick R/G/B per band based on bits of (hpos-144)/80 = active_col bits 4..6.
  process(vis, hpos, vpos, ui_in)
    variable band : unsigned(2 downto 0);
    variable ac   : unsigned(9 downto 0);
  begin
    r <= "00"; g <= "00"; b <= "00";
    if vis = '1' then
      ac   := hpos - 144;
      band := ac(6 downto 4) xor unsigned(ui_in(2 downto 0));
      r <= band(2) & band(2);
      g <= band(1) & band(1);
      b <= band(0) & band(0);
    end if;
  end process;

  uo_out <= hsync & b(0) & g(0) & r(0) & vsync & b(1) & g(1) & r(1);
end architecture;
