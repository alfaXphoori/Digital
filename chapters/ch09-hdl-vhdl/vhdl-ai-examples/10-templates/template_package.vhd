library ieee;
use ieee.std_logic_1164.all;

package my_package is
  constant DATA_WIDTH : positive := 32;
  type     bus_t       is record
    valid : std_logic;
    data  : std_logic_vector(DATA_WIDTH-1 downto 0);
  end record;
  function bit_count(v : std_logic_vector) return natural;
end package;

package body my_package is
  function bit_count(v : std_logic_vector) return natural is
    variable n : natural := 0;
  begin
    for i in v'range loop
      if v(i) = '1' then n := n + 1; end if;
    end loop;
    return n;
  end function;
end package body;
