----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/15/2023 01:42:10 PM
-- Design Name: 
-- Module Name: main - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity lab_1 is
    port(
        a: in std_logic;
        b: in std_logic;
        out_and: out std_logic;
        out_or: out std_logic;
        out_xor: out std_logic;
        out_not: out std_logic;
        out_nand: out std_logic;
        out_nor: out std_logic;
        out_xnor: out std_logic
    );
end lab_1;

architecture impl of lab_1 is
    signal and_gate: std_logic;
    signal or_gate: std_logic;
    signal xor_gate: std_logic;
    signal not_gate: std_logic;
    signal nand_gate: std_logic;
    signal nor_gate: std_logic;
    signal xnor_gate: std_logic;
begin
    and_gate <= a and b;  
    or_gate <= a or b;
    xor_gate <= a xor b;
    not_gate <= not a;
    nand_gate <= a nand b;
    nor_gate <= a nor b;
    xnor_gate <= a xnor b;
    
    out_and <= and_gate;
    out_or <= or_gate;
    out_xor <= xor_gate;
    out_not <= not_gate;
    out_nand <= nand_gate;
    out_nor <= nor_gate;
    out_xnor <= xnor_gate;
end impl;

-- -- lab 2 part 1
-- library ieee; 
-- use ieee.std_logic_1164.all; 

-- entity lab_2_1 is 
--     port (
--         din: in std_logic_vector(2 downto 0);
--         dout: out std_logic_vector(7 downto 0)
--     );
-- end lab2_1

-- architecture impl of lab_2_1 is 
-- begin
--     with din select dout <=
--         "00000001" when "000",
--         "00000010" when "001",
--         "00000100" when "010",
--         "00001000" when "011",
--         "00010000" when "100",
--         "00100000" when "101",
--         "01000000" when "110",
--         "10000000" when others;
-- end impl;

-- -- lab 2 part 2 
-- library IEEE;
-- use IEEE.STD_LOGIC_1164.ALL;

-- entity lab_2_2 is 
--     port (
--         din: in std_logic_vector(7 downto 0);
--         dout: out std_logic_vector(3 downto 0)
--     );
-- end lab_2_2;

-- architecture impl of lab_2_2 is 
-- begin
--     with din select dout <= 
--         "0001" when "00000010", 
--         "0010" when "00000100", 
--         "0011" when "00001000", 
--         "0100" when "00010000", 
--         "0101" when "00100000", 
--         "0110" when "01000000", 
--         "0111" when "10000000", 
--         "1000" when others;
-- end impl;
