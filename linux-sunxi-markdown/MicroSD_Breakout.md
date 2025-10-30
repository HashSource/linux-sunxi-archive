# MicroSD Breakout
[![][37884]][37885]
[][37886]
GND, GND, VDD, RX, TX
[![JTAG MicroSD UART-back.jpeg][37887]][37888]
[][37889]
[![JTAG MicroSD UART-side.jpeg][37890]][37891]
[][37892]
The cubieboard MicroSD breakout board provides JTAG and UART over the SD-Card connector. The UART connector is a 5 pin JST-XH. 
## Contents
  * [1 Mapping][37893]
  * [2 U-Boot output to sdcard UART][37894]
    * [2.1 Mainline U-Boot][37895]
    * [2.2 legacy u-boot-sunxi][37896]
  * [3 Linux kernel output to SD-Card UART][37897]
    * [3.1 mainline kernel][37898]
    * [3.2 Legacy sunxi-3.4 kernel][37899]
  * [4 Breakout boards][37900]
  * [5 See also][37901]
  * [6 Buy][37902]

## Mapping
Pin | [MicroSD][37903] | [JTAG][37904] Connection | 14-pin ARM [JTAG][37904] Header | [UART][37905] Connection | 5-pin [UART][37905] Header   
---|---|---|---|---|---  
1 | Data2 | TCK | 9 | _nc_ | _nc_  
2 | CD/Data3 | _nc_ | _nc_ | RX | 2   
3 | Cmd | TDO | 11 | _nc_ | _nc_  
4 | VDD | VTG | 1,13 | VDD | 3   
5 | CLK | _nc_ | _nc_ | TX | 1   
6 | VSS | GND |  2,4,6,8,10,14 | GND | 4, 5   
7 | Data0 | TDI | 5 | _nc_ | _nc_  
8 | Data1 | TMS | 7 | _nc_ | _nc_  
_nc_ | _nc_ | nTRST | 3 | _nc_ | _nc_  
_nc_ | _nc_ | nRESET | 12 | _nc_ | _nc_  
## U-Boot output to sdcard UART
For booting, apply the [FEL/USBBoot][37906] procedure. 
### Mainline U-Boot
First, to setup u-boot for FEL mode, use _< board>_felconfig_ instead of the usual _< board>_defconfig_. 
Then, set in both 
  * .config
  * spl/.conf

[code] 
    CONFIG_UART0_PORT_F=y
    
[/code]
Alternatively, you can set the variables via menuconfig, but again you have to do this twice: 
  * make menuconfig
  * make spl/menuconfig

[code] 
    ARM architecture  --->
    [*] SPL/FEL mode support
    [*]  UART0 on MicroSD breakout board
    
[/code]
Compile as usual. 
### legacy u-boot-sunxi
Add 'UART0_PORT_F' to the option of the *_FEL line of your board in _boards.cfg_. Make sure it also contains 'SPL_FEL' instead of 'SPL'. 
## Linux kernel output to SD-Card UART
### mainline kernel
It is necessary to delete the mmc0 entry from the dts file and also move uart0 pins from "PB22 and "PB23" to "PF2" and "PF4". This may look like adding something like this to the dts file (not the cleanest option): 
[code] 
    	pio: pinctrl@01c20800 {
    		uart0_pins_a: uart0@0 {
    			allwinner,pins = "PF2", "PF4";
    			allwinner,function = "uart0";
    			allwinner,drive = <0>;
    			allwinner,pull = <0>;
    		};
    	};
    
[/code]
### Legacy sunxi-3.4 kernel
Sunxi-3.4 kernel branch is deprecated and unsupported, information is here is stored for historical reasons. 
Some FEX modifications are needed. An example for A13: 
[code] 
    @@ -31,13 +31,13 @@ sdc_d2 = port:PF05<2><1><default><default>
     twi_port = 0
     twi_scl = port:PB00<2><1><default><default>
     twi_sda = port:PB01<2><1><default><default>
     
     [uart_para]
    -uart_debug_port = 1
    -uart_debug_tx = port:PG03<4><1><default><default>
    -uart_debug_rx = port:PG04<4><1><default><default>
    +uart_debug_port = 0
    +uart_debug_tx = port:PF02<4><1><default><default>
    +uart_debug_rx = port:PF04<4><1><default><default>
     
     [jtag_para]
     jtag_enable = 0
     jtag_ms = port:PF00<4><1><default><default>
     jtag_ck = port:PF05<4><1><default><default>
    @@ -112,15 +112,15 @@ twi1_sda = port:PB16<2><default><default><default>
     twi2_used = 1
     twi2_scl = port:PB17<2><default><default><default>
     twi2_sda = port:PB18<2><default><default><default>
     
     [uart_para0]
    -uart_used = 0
    +uart_used = 1
     uart_port = 0
     uart_type = 2
    -uart_tx = port:PB19<2><1><default><default>
    -uart_rx = port:PB20<2><1><default><default>
    +uart_tx = port:PF02<4><1><default><default>
    +uart_rx = port:PF04<4><1><default><default>
     
     [uart_para1]
     uart_used = 1
     uart_port = 1
     uart_type = 2
    @@ -351,11 +351,11 @@ csi_power_en_b =
     csi_stby_b =
     csi_flash_b =
     csi_af_en_b =
     
     [mmc0_para]
    -sdc_used = 1
    +sdc_used = 0
     sdc_detmode = 1
     bus_width = 4
     sdc_d1 = port:PF00<2><1><2><default>
     sdc_d0 = port:PF01<2><1><2><default>
     sdc_clk = port:PF02<2><1><2><default>
    
[/code]
## Breakout boards
  * [microSD Sniffer][37907] (@sparkfun.com) - header needs to be soldered.

## See also
  * [JTAG][37904]
  * [UART][37905]

## Buy
<https://www.sparkfun.com/products/9419> \- SparkFun microSD sniffer.
