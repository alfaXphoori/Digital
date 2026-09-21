library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- TinyTapeout-pinout VGA "XOR texture" — the classic
--     pixel(x, y) = (x XOR y) bit pattern
-- that shows up in graphics tutorials as a stunning result of one of the
-- simplest possible expressions. A frame counter slowly drifts the pattern.
--
-- ui_in[0]   : enable animation
-- ui_in[3:1] : colour permutation
--
-- Credit: this pattern is a folklore demoscene staple. Discussed e.g. in
-- Hugo Elias's "tiny demo" page and countless Shadertoy variants. Pure-VHDL
-- TinyTapeout port is original to VHDLive.
entity tt_um_xor_pattern is
  port (
    clk    : in  std_logic;
    rst_n  : in  std_logic;
    ui_in  : in  std_logic_vector(7 downto 0);
    uo_out : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of tt_um_xor_pattern is
  signal hpos : unsigned(9 downto 0) := (others => '0');
  signal vpos : unsigned(9 downto 0) := (others => '0');
  signal hsync, vsync, vis : std_logic;
  signal frame_ctr : unsigned(7 downto 0) := (others => '0');
  signal r, g, b : unsigned(1 downto 0);
begin
  process(clk, rst_n) is
  begin
    if rst_n = '0' then
      hpos <= (others => '0');
      vpos <= (others => '0');
      frame_ctr <= (others => '0');
    elsif rising_edge(clk) then
      if hpos = 799 then
        hpos <= (others => '0');
        if vpos = 524 then
          vpos <= (others => '0');
          if ui_in(0) = '1' then
            frame_ctr <= frame_ctr + 1;
          end if;
        else
          vpos <= vpos + 1;
        end if;
      else
        hpos <= hpos + 1;
      end if;
    end if;
  end process;

  hsync <= '0' when hpos < 96 else '1';
  vsync <= '0' when vpos < 2  else '1';
  vis   <= '1' when hpos >= 144 and hpos < 784 and vpos >= 35 and vpos < 515 else '0';

  process(vis, hpos, vpos, frame_ctr, ui_in) is
    variable px  : unsigned(9 downto 0);
    variable py  : unsigned(9 downto 0);
    variable val : unsigned(7 downto 0);
    variable rv, gv, bv : unsigned(1 downto 0);
  begin
    rv := "00"; gv := "00"; bv := "00";
    if vis = '1' then
      px := hpos - 144;
      py := vpos - 35;
      val := (px(7 downto 0) + frame_ctr) xor py(7 downto 0);
      -- Spread the 8-bit XOR result across R, G, B 2-bit channels
      case ui_in(3 downto 1) is
        when "001"  => rv := val(7 downto 6); gv := val(3 downto 2); bv := val(5 downto 4);
        when "010"  => rv := val(3 downto 2); gv := val(7 downto 6); bv := val(5 downto 4);
        when "011"  => rv := val(5 downto 4); gv := val(3 downto 2); bv := val(7 downto 6);
        when "100"  => rv := val(3 downto 2); gv := val(5 downto 4); bv := val(7 downto 6);
        when "101"  => rv := val(5 downto 4); gv := val(7 downto 6); bv := val(3 downto 2);
        when others => rv := val(7 downto 6); gv := val(5 downto 4); bv := val(3 downto 2);
      end case;
    end if;
    r <= rv;
    g <= gv;
    b <= bv;
  end process;

  uo_out <= hsync & b(0) & g(0) & r(0) & vsync & b(1) & g(1) & r(1);
end architecture;
