library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity my_entity is
  port (
    clk : in  std_logic;
    rst : in  std_logic;
    d   : in  std_logic_vector(7 downto 0);
    q   : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of my_entity is
begin
  process (clk, rst)
  begin
    if rst = '1' then
      q <= (others => '0');
    elsif rising_edge(clk) then
      q <= d;
    end if;
  end process;
end architecture;
