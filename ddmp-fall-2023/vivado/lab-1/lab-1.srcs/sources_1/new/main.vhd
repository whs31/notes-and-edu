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

architecture rtl of lab_1 is
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
end rtl;
