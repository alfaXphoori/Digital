library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- TinyTapeout-pinout VGA checkerboard demo.
-- A clean intro to VGA: just hsync/vsync timing and a 1-bit pattern from
-- two position bits XOR-ed together.
--
-- ui_in[2:0] : sets the dark-square colour (RGB bits)
-- ui_in[5:4] : square size: 00=32px, 01=64px, 10=128px, 11=16px
--
-- Inspired by the classic "your first VGA design" pattern from fpga4fun
-- and Nandland's VGA tutorial.
entity tt_um_checker is
  port (
    clk    : in  std_logic;
    rst_n  : in  std_logic;
    ui_in  : in  std_logic_vector(7 downto 0);
    uo_out : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of tt_um_checker is
  signal hpos : unsigned(9 downto 0) := (others => '0');
  signal vpos : unsigned(9 downto 0) := (others => '0');
  signal hsync, vsync, vis : std_logic;
  signal cell : std_logic;
  signal r, g, b : unsigned(1 downto 0);
begin
  process(clk, rst_n) is
  begin
    if rst_n = '0' then
      hpos <= (others => '0');
      vpos <= (others => '0');
    elsif rising_edge(clk) then
      if hpos = 799 then
        hpos <= (others => '0');
        if vpos = 524 then vpos <= (others => '0');
        else vpos <= vpos + 1;
        end if;
      else hpos <= hpos + 1;
      end if;
    end if;
  end process;

  hsync <= '0' when hpos < 96 else '1';
  vsync <= '0' when vpos < 2  else '1';
  vis   <= '1' when hpos >= 144 and hpos < 784 and vpos >= 35 and vpos < 515 else '0';

  -- Select which position-bit determines the cell sign (i.e., square size).
  process(hpos, vpos, ui_in)
  begin
    case ui_in(5 downto 4) is
      when "00"   => cell <= hpos(5) xor vpos(5);  -- 32 px
      when "01"   => cell <= hpos(6) xor vpos(6);  -- 64 px
      when "10"   => cell <= hpos(7) xor vpos(7);  -- 128 px
      when others => cell <= hpos(4) xor vpos(4);  -- 16 px
    end case;
  end process;

  process(vis, cell, ui_in) is
  begin
    r <= "00"; g <= "00"; b <= "00";
    if vis = '1' then
      if cell = '1' then
        r <= "11"; g <= "11"; b <= "11";       -- light squares: white
      else
        r <= ui_in(0) & ui_in(0);              -- dark squares: ui_in[2:0]
        g <= ui_in(1) & ui_in(1);
        b <= ui_in(2) & ui_in(2);
      end if;
    end if;
  end process;

  uo_out <= hsync & b(0) & g(0) & r(0) & vsync & b(1) & g(1) & r(1);
end architecture;
