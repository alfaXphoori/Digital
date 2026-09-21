library ieee;
use ieee.std_logic_1164.all;

entity my_fsm is
  port (
    clk    : in  std_logic;
    rst    : in  std_logic;
    start  : in  std_logic;
    done   : out std_logic
  );
end entity;

architecture rtl of my_fsm is
  type state_t is (IDLE, RUN, FINISH);
  signal s, s_next : state_t := IDLE;
begin
  process (clk, rst)
  begin
    if rst = '1' then s <= IDLE;
    elsif rising_edge(clk) then s <= s_next;
    end if;
  end process;

  process (s, start)
  begin
    s_next <= s;
    done   <= '0';
    case s is
      when IDLE   => if start = '1' then s_next <= RUN; end if;
      when RUN    => s_next <= FINISH;
      when FINISH => done <= '1'; s_next <= IDLE;
    end case;
  end process;
end architecture;
