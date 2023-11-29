--???????????? ????????????? ? ???????? ???????.
--???????? ?????????? ?????? ????? ??? ???????? ????? (addr, ????????), ??????
--?????????????? ????? (din, ??????) ? ???? ?????????????? ????? (dout, ?????????).

library ieee; 
use ieee.STD_LOGIC_1164.ALL; 

entity lab_3_1 is 
    port ( 
        din : in std_logic_vector (3 downto 0); 
        addr : in std_logic_vector (1 downto 0);     
        dout : out std_logic
    ); 
end entity; 


architecture impl of lab_3_1 is 
begin 
    pro: process(addr, din) 
    begin 
        case addr is 
            when "00" => dout <= din(0); 
            when "01" => dout <= din(1); 
            when "10" => dout <= din(2); 
            when "11" => dout <= din(3); 
        end case; 
    end process; 
end architecture;
------------------------------------------------------------------------------------------------------------------------------------------------------------------

--???????????? ??????????????? ? ???????? ????????.
--???????? ?????????? ?????? ????? ??? ???????? ????? (????????), ???? ?????????????? ????
--(??????) ? ?????? ?????????????? ?????? (??????????).

--library ieee; 
--use ieee.STD_LOGIC_1164.ALL;
 
--entity lab_3_2 is 
--    port ( 
--        din : in std_logic; 
--        addr : in std_logic_vector (1 downto 0); 
--        dout : out std_logic_vector (3 downto 0)
--    ); 
--end entity; 

--architecture impl of lab_3_2 is 
--begin 
--    pro : process(din, addr) 
--    begin 
--        dout <= "0000"; 
--        case addr is 
--            when "00" => dout(0) <= din; 
--            when "01" => dout(1) <= din; 
--            when "10" => dout(2) <= din; 
--            when "11" => dout(3) <= din; 
--        end case; 
--    end process; 
--end architecture;
------------------------------------------------------------------------------------------------------------------------------------------------------------------

--???????? ???? ??????????????? ????????????? ?????.
--???????? ?????????? ?????? ????? ??? ????????????? ????? (????????) ? ?????? ??????
--(??????????). ??? ?????????? ???????? ????????, ?????????? ????????????? ???????????
--???????????? ???????????. ??? ????? - ????????? ????? ???????? ? ????????? ?? 1.

--library ieee; 
--use ieee.STD_LOGIC_1164.all; 
--use ieee.std_logic_arith.all; 

--entity lab_4_1 is 
--    port ( 
--        x1: in std_logic_vector (2 downto 0); 
--        x2: in std_logic_vector (2 downto 0); 
--        y: out std_logic_vector (3 downto 0)
--    ); 
--end entity; 	

--architecture impl of lab_4_1 is 
--    signal x1_p: std_logic_vector:="0000"; 
--    signal x2_p: std_logic_vector:="0000"; 
--begin 
--    x1_p <= "0" & x1; 
--    x2_p <= "0" & x2; 
--    y <= unsigned(x1_p) + unsigned(x2_p); 
--end architecture;
------------------------------------------------------------------------------------------------------------------------------------------------------------------

--???????? ????????? ?????????????? ????? ? ????????? (cnst = 3).
--???????? ?????????? ?????? ????? ???? 7-????????? ???? ? ??? ??????? ???????? ?????
--(????????) ? ???? 8-????????? ????? y (??????????). ???????? ?????? ??????????? ? ??????
--?????, ?.?. ??????? ?????? ??????? ?????????? ? ????? - ????????. ??????????? ????? ?????????
--?????????? ????????? ?? 8 ??? ?????????? ???????? ????????, ?????? ?????????? ???????????
--?????? ???? ????????? ? ?????? ?????.
--??????? ???????? ??? ?????????????? ??????, ????????? ????????????? ??? ??????

--library ieee; 
--use ieee.STD_LOGIC_1164.all; 
--use ieee.std_logic_arith.all; 

--entity lab_4_2 is 
--    port ( 
--        x: in std_logic_vector (6 downto 0); 
--        y: out std_logic_vector (7 downto 0)
--    ); 
--end entity; 

--architecture impl of lab_4_2 is 
--    constant cnst: std_logic_vector(7 downto 0) := X"03"; 
--begin 
--    y <= signed(x(6) & x) + signed(cnst);  
--end architecture;
------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ????, ??????????? ??????????? ????? ????????????????? ????? ????? ?? ??? ???????.
--???????? ?????????? ?????? ????? ???? ???????????????? ???? ??? ??????? ???????? ?????
--(????????) ? ??? ???????????????? ?????? (??????????). ?????? ????? - ??? ???????????
--????????? ?????, ? ?????? - ??? ??????????? ?????????? ???????????? ?????? ?? ??? ???????
--?????. ???????? ????? ?????? ?????????? ? ??????? ???????? ????????? ???????.

library ieee; 
use ieee.STD_LOGIC_1164.all; 

entity lab_4_3 is 
    port (
        x: in std_logic_vector(3 downto 0); 
        y: out std_logic_vector(7 downto 0)
    ); 
end entity; 

architecture impl of lab_4_3 is 
begin 
    y(3 downto 0) <= x; 
    y(4) <= x(2); 
    y(5) <= x(3); 
    y(6) <= x(0); 
    y(7) <= x(1); 
end architecture;
------------------------------------------------------------------------------------------------------------------------------------------------------------------

--?????????? ???? ??????????????? ????????????? ?????.
--???????? ?????????? ?????? ????? ??? ????????????? ????? ??? ??????? ??????? ?????
--(????????) ? ???? ????????????? ????? (?????????????? ?????????) ??? ???????????
--?????????? ?????????

library ieee; 
use ieee.STD_LOGIC_1164.all; 
use ieee.std_logic_arith.all; 

entity lab_4_4 is 
    port ( 
        x1: in std_logic_vector (1 downto 0); 
        x2 : in std_logic_vector (1 downto 0); 
        an : out std_logic_vector (3 downto 0); 
        y: out std_logic_vector (6 downto 0)
    ); 
end entity; 

architecture impl of lab_4_4 is 
    signal din : std_logic_vector (3 downto 0); 
begin 
    an <= "1110"; 
    
    process (x1,x2) is 
    begin 
        din <= (unsigned(x1)* unsigned(x2)); 
    end process; 

    y <= not "0111111" when din = X"0" else 
         not "0000110" when din = X"1" else 
         not "1011011" when din = X"2" else 
         not "1001111" when din = X"3" else 
         not "1100110" when din = X"4" else 
         not "1101101" when din = X"5" else 
         not "1111101" when din = X"6" else 
         not "0000111" when din = X"7" else 
         not "1111111" when din = X"8" else 
         not "1101111" when din = X"9" else 
         not "1110111" when din = X"A" else 
         not "1111100" when din = X"B" else 
         not "0111001" when din = X"C" else 
         not "0111110" when din = X"D" else 
         not "1111001" when din = X"E" else 
         not "1110001" when din = X"F"; 
end architecture;
------------------------------------------------------------------------------------------------------------------------------------------------------------------