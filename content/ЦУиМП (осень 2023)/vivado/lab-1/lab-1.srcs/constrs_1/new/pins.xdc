set_property PACKAGE_PIN V17 [get_ports {j}]
set_property IOSTANDARD LVCMOS33 [get_ports {j}]
set_property PACKAGE_PIN V16 [get_ports {k}]
set_property IOSTANDARD LVCMOS33 [get_ports {k}]
set_property PACKAGE_PIN W16 [get_ports {preset}]
set_property IOSTANDARD LVCMOS33 [get_ports {preset}]
##Buttons
set_property PACKAGE_PIN U18 [get_ports e]
set_property IOSTANDARD LVCMOS33 [get_ports e]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets e_IBUF]
set_property PACKAGE_PIN T18 [get_ports clear]
set_property IOSTANDARD LVCMOS33 [get_ports clear]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets clear_IBUF]
set_property PACKAGE_PIN W19 [get_ports preset]
set_property IOSTANDARD LVCMOS33 [get_ports preset]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets preset_IBUF]
## 
set_property PACKAGE_PIN W5 [get_ports clk]
set_property IOSTANDARD LVCMOS33 [get_ports clk]
create_clock -add -name sys_clk_pin -period 10.00 -waveform {0 5}
[get_ports clk]
# LEDs
set_property PACKAGE_PIN U16 [get_ports {jk_out}]
set_property IOSTANDARD LVCMOS33 [get_ports {jk_out}]
