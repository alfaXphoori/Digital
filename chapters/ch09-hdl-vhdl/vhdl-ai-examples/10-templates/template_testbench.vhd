library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity my_testbench is
end entity;

architecture sim of my_testbench is
  constant CLK_PERIOD : time := 10 ns;
  signal clk : std_logic := '0';
  signal rst : std_logic := '1';
begin
  clk <= not clk after CLK_PERIOD / 2;
  rst <= '1', '0' after 30 ns;

  process
  begin
    wait for 200 ns;
    report "Simulation finished" severity note;
    wait;
  end process;
end architecture;
