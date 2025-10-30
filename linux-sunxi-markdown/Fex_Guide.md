# Fex Guide
## Contents
  * [1 FEX Description][19336]
  * [2 Port Definitions][19337]
  * [3 application][19338]
    * [3.1 [product]][19339]
  * [4 system configuration][19340]
    * [4.1 [target]][19341]
    * [4.2 [card_burn_para]][19342]
    * [4.3 [card_boot]][19343]
    * [4.4 [card_boot0_para]][19344]
    * [4.5 [card_boot2_para]][19345]
    * [4.6 [twi_para]][19346]
    * [4.7 [uart_para]][19347]
    * [4.8 [jtag_para]][19348]
    * [4.9 [system]][19349]
    * [4.10 [gpio_para]][19350]
    * [4.11 [gpio_init]][19351]
  * [5 SDRAM][19352]
    * [5.1 [dram_para]][19353]
  * [6 mali configuration][19354]
    * [6.1 [mali_para]][19355]
    * [6.2 [g2d_para]][19356]
  * [7 ethernet MAC configuration][19357]
    * [7.1 [emac_para]][19358]
  * [8 i2c configuration][19359]
    * [8.1 [twi0_para]][19360]
    * [8.2 [twi1_para]][19361]
    * [8.3 [twi2_para]][19362]
  * [9 uart configuration][19363]
    * [9.1 [uart_para0]][19364]
    * [9.2 [uart_para1]][19365]
    * [9.3 [uart_para2]][19366]
    * [9.4 [uart_para3]][19367]
    * [9.5 [uart_para4]][19368]
    * [9.6 [uart_para5]][19369]
    * [9.7 [uart_para6]][19370]
    * [9.8 [uart_para7]][19371]
  * [10 spi configuration][19372]
    * [10.1 [spi0_para]][19373]
    * [10.2 [spi1_para]][19374]
    * [10.3 [spi2_para]][19375]
    * [10.4 [spi3_para]][19376]
  * [11 external spi device configuration][19377]
    * [11.1 [spi_devices]][19378]
    * [11.2 [spi_board0]][19379]
  * [12 resistive touch panel configuration][19380]
    * [12.1 [rtp_para]][19381]
  * [13 capacitive touch panel configuration][19382]
    * [13.1 [ctp_para]][19383]
  * [14 touch key configuration][19384]
    * [14.1 [tkey_para]][19385]
  * [15 microphone configuration][19386]
    * [15.1 [micphone_para]][19387]
  * [16 tablet key configuration][19388]
    * [16.1 [tabletkeys_para]][19389]
  * [17 motor configuration][19390]
    * [17.1 [motor_para]][19391]
  * [18 lock configuration][19392]
    * [18.1 [locks_para]][19393]
  * [19 nand flash configuration][19394]
    * [19.1 [nand_para]][19395]
  * [20 boot disp configuration][19396]
    * [20.1 [boot_disp]][19397]
  * [21 disp init configuration][19398]
    * [21.1 [disp_init]][19399]
  * [22 lcd[0/1] configuration][19400]
    * [22.1 [lcd0_para]][19401]
    * [22.2 [lcd1_para]][19402]
  * [23 tv out dac configuration][19403]
    * [23.1 [tv_out_dac_para]][19404]
  * [24 csi gpio configuration][19405]
    * [24.1 [csi0_para]][19406]
    * [24.2 [csi1_para]][19407]
  * [25 tv configuration][19408]
    * [25.1 [tvout_para]][19409]
    * [25.2 [tvin_para]][19410]
  * [26 sata configuration][19411]
    * [26.1 [sata_para]][19412]
  * [27 sdmmc configuration][19413]
    * [27.1 [mmc0_para]][19414]
    * [27.2 [mmc1_para]][19415]
    * [27.3 [mmc2_para]][19416]
    * [27.4 [mmc3_para]][19417]
  * [28 memory stick configuration][19418]
    * [28.1 [ms_para]][19419]
  * [29 sim card configuration][19420]
    * [29.1 [smc_para]][19421]
  * [30 ps2 configuration][19422]
    * [30.1 [ps2_0_para]][19423]
    * [30.2 [ps2_1_para]][19424]
  * [31 can bus configuration][19425]
    * [31.1 [can_para]][19426]
  * [32 matrix keyboard][19427]
  * [33 23.1 [keypad_para]][19428]
  * [34 USB control flags][19429]
    * [34.1 [usbc0]][19430]
    * [34.2 [usbc1]][19431]
    * [34.3 [usbc2]][19432]
  * [35 USB Device][19433]
    * [35.1 [usb_feature]][19434]
    * [35.2 [msc_feature]][19435]
  * [36 G Sensor configuration][19436]
    * [36.1 [gsensor_para]][19437]
  * [37 gps gpio configuration][19438]
    * [37.1 [gps_para]][19439]
  * [38 sdio wifi configuration][19440]
    * [38.1 [sdio_wifi_para]][19441]
  * [39 us wifi configuration][19442]
    * [39.1 [usb_wifi_para]][19443]
  * [40 3G configuration][19444]
    * [40.1 [3g_para]][19445]
  * [41 gyroscope][19446]
    * [41.1 [gy_para]][19447]
  * [42 light sensor][19448]
    * [42.1 [ls_para]][19449]
  * [43 compass][19450]
    * [43.1 [compass_para]][19451]
  * [44 blue tooth][19452]
    * [44.1 [bt_para]][19453]
  * [45 i2s configuration][19454]
    * [45.1 [i2s_para]][19455]
  * [46 spdif configuration][19456]
    * [46.1 [spdif_para]][19457]
  * [47 audio configuration][19458]
    * [47.1 [audio_para]][19459]
  * [48 infrared remote configuration][19460]
    * [48.1 [ir_para]][19461]
  * [49 pmu configuration][19462]
    * [49.1 [pmu_para]][19463]
  * [50 recovery key configuration][19464]
    * [50.1 [recovery_key]][19465]
  * [51 dvfs voltage-frequency table configuration][19466]
    * [51.1 [dvfs_table]][19467]
  * [52 led configuration][19468]
    * [52.1 [leds_para]][19469]
    * [52.2 external leds][19470]
  * [53 dynamic configuration][19471]
    * [53.1 [dynamic]][19472]

## FEX Description
A FEX file defines various aspects of how the SoC works. It configures the GPIO pins and sets up DRAM, Display, etc parameters. It is Allwinners predecessor for the devicetree. 
Each line consists of a **key** = **value** pair combination under a **[sectionheader]**. All three, **[sectionheader]** , **key** and **value** are case-sensitive. For comments a semi-colon (**;**) is used and everything following a semi-colon is ignored. The chip does not parse a textual version of a fex file, it gets cleaned and compiled by a fex-compiler. A reverse engineered open source version exists in the [sunxi-tools repository][19473]. Also a de-compiler which takes a binary _script.bin_ and creates a textual _script.fex_. Usually, _script.bin_ can be found on the nanda boot partition on A10 devices. 
[![Sticky-note-pin.png][19474]][19475] _Note:_ The [mainline][19476] Linux kernel makes no use of FEX / [script.bin][19477], and relies on the [device tree][19478] model instead (_.dtb_ files). 
## Port Definitions
Description of the GPIO configuration in the form: 
    port:<port><mux feature><pullup/down><drive capability><output level>
where: 
    **< port>** is the port to configure (ie. PH15)
    **< mux feature>** is the function to configure the port for, mux 0 is as input, mux 1 as output and for 2-7 see [A10/PIO][19479], [A13/PIO][19480], or [A20/PIO][19481] for details.
    **< pullup/down>** is 0 = disabled; 1 = pullup enabled; 2 = pulldown enabled (only valid when port is an input)
    **< drive capability>** defines the output drive in mA, values are 0-3 corresponding to 10mA, 20mA, 30mA and 40mA.
    **< output level>** sets the initial output level for the port; 0 = low; 1 = high (only valid for outputs)
The **< pullup/down>** <drive capability> and <output level> can be set to <default> which means don't change. Any trailing <default> options can be omitted. 
This can also be used to specify various pins on the AXP PMIC. The syntax is "power:portN". 
Port | AXP20x | AXP22x / AXP8xx |   
---|---|---|---  
0 | GPIO0 | GPIO0   
1 | GPIO1 | GPIO1   
2 | GPIO2 | DC1SW   
3 | GPIO3 | CHGLED   
4 |  | N_VBUSEN   
5 |  | WAKEUP (slave PMIC)   
6 |  | SWOUT (slave PMIC)   
## application
### [product]
Product version and description. It seems all fex files at this moment are at version 1.0 and use the default evaluation board name. It doesn't appear to be used internally, but requires further investigation. 
  * **version** : string indicating fex file version.
  * **machine** : string indicating the board name. _"A10-EVB-V1.2"_ appears to be a common one, seemingly to refer to the A10 Evaluation board v1.2.

[code] 
    [product]
    version = "1.0"
    machine = "A10-EVB-V1.2"
    
[/code]
## system configuration
### [target]
[![Sticky-note-pin.png][19474]][19475] _Note:_ blue module chip pin configuration, the black module internal control configuration 
Configuration items to configure the meaning of 
  * **boot_clock** : Initial boot frequency in MHz.
  * **dcdc2_vol** : Dcdc2 output voltage in mV.
  * **dcdc3_vol** : Dcdc3 output voltage in mV.
  * **ldo2_vol** : Ldo2 output voltage in mV.
  * **ldo3_vol** : Ldo3 output voltage in mV.
  * **ldo4_vol** : Ldo4 output voltage in mV.
  * **power_start** : 0 or 1.
  * **storage_type** : 0 = nand, 1 = SDCard, 2 = SPI-nor

Configuration example: 
[code] 
    [target]
    boot_clock = 1008
    dcdc2_vol = 1400
    dcdc3_vol = 1250
    ldo2_vol = 3000
    ldo3_vol = 2800
    ldo4_vol = 2800
    pll4_freq = 960
    pll6_freq = 960
    power_start = 1
    storage_type = 0
    
[/code]
### [card_burn_para]
Configuration example: 
[code] 
    [card_burn_para]
    card_no = 0
    card_line = 4
    card_mode = 0
    sdc_d1 = port:PF00<2><1><default><default>
    sdc_d0 = port:PF01<2><1><default><default>
    sdc_clk = port:PF02<2><1><default><default>
    sdc_cmd = port:PF03<2><1><default><default>
    sdc_d3 = port:PF04<2><1><default><default>
    sdc_d2 = port:PF05<2><1><default><default>
    
[/code]
### [card_boot]
  * **logical_start** : logical starting address when booting from SD-Card.
  * **sprite_gpio0** :

Configuration example: 
[code] 
    [Card_boot]
    logical_start = 40960
    sprite_gpio0 =
    
[/code]
### [card_boot0_para]
  * **card_ctrl** : card controller to be used
  * **card_high_speed** : 0 for low speed, 1 for high-speed
  * **card_line** : Number of card data lines
  * **sdc_ cmd** : SD-Card command signals GPIO configuration
  * **sdc_ clk** : SD-Card clock signal GPIO configuration
  * **sdc_ d0** : SD-Card data 0 line signal GPIO configuration
  * **sdc_ d1** : SD-Card data 1 line signal GPIO configuration
  * **sdc_d2** : SD-Card data 2 line signal GPIO configuration
  * **sdc_d3** : SD-Card data 3 line signal GPIO configuration

Configuration example: 
[code] 
    [card_boot0_para]
    card_ctrl = 0
    card_high_speed = 1
    card_line = 4
    sdc_d1 = port:PF00<2><1><default><default>
    sdc_d0 = port:PF01<2><1><default><default>
    sdc_clk = port:PF02<2><1><default><default>
    sdc_cmd = port:PF03<2><1><default><default>
    sdc_d3 = port:PF04<2><1><default><default>
    sdc_d2 = port:PF05<2><1><default><default>
    
[/code]
### [card_boot2_para]
  * **card_ctrl** : card controller to be used
  * **card_high_speed** : 0 for low speed, 1 for high-speed
  * **card_line** : number of card data lines
  * **sdc_ cmd** : SD-Card command signals GPIO configuration
  * **sdc_ clk** : SD-Card clock signal GPIO configuration
  * **sdc_ d0** : SD-Card data 0 line signal GPIO configuration
  * **sdc_ d1** : SD-Card data 1 line signal GPIO configuration
  * **sdc_d2** : SD-Card data 2 line signal GPIO configuration
  * **sdc_d3** : SD-Card data 3 line signal GPIO configuration

Configuration example: 
[code] 
    [card_boot2_para]
    card_ctrl = 2
    card_high_speed = 1
    card_line = 4
    sdc_cmd = port:PC06<3><1><default><default>
    sdc_clk = port:PC07<3><1><default><default>
    sdc_d0 = port:PC08<3><1><default><default>
    sdc_d1 = port:PC09<3><1><default><default>
    sdc_d2 = port:PC10<3><1><default><default>
    sdc_d3 = port:PC11<3><1><default><default>
    
[/code]
### [twi_para]
twi controller to enable during/for boot. 
  * **twi_port** : twi controller to configure
  * **twi_scl** : twi Serial CLock line GPIO configuration
  * **twi_sda** : = twi Serial DAta line GPIO configuration

Configuration example: 
[code] 
    [twi_para]
    twi_port = 0
    twi_scl = port:PB00<2><default><default><default>
    twi_sda = port:PB01<2><default><default><default>
    
[/code]
### [uart_para]
Serial port to be enabled during/for boot. 
  * **uart_debug_port** : serial controller number
  * **uart_debug_tx** : serial port TX line GPIO configuration
  * **uart_debug_rx** : serial port RX line GPIO configuration

Configuration example: 
[code] 
    [uart_para]
    uart_debug_port = 0
    uart_debug_tx = port:PB22<2>
    uart_debug_rx = port:PB23<2>
    
[/code]
### [jtag_para]
JTAG port to be enabled during/for boot. 
  * **jtag_enable** : 0 to disable JTAG, 1 to enable JTAG
  * **jtag_ms** : JTAG Test Mode Select (TMS) GPIO configuration
  * **jtag_ck** : JTAG Test Clock (TCK) GPIO configuration
  * **jtag_do** : JTAG Test Data Output (TDO) GPIO configuration
  * **jtag_di** : JTAG Test Data Input (TDI) GPIO configuration

Configuration example: 
[code] 
    [jtag_para]
    jtag_enable = 1
    jtag_ms = port:PB14<3><default><default><default>
    jtag_ck = port:PB15<3>default><default><default>
    jtag_do = port:PB16<3>default><default><default>
    jtag_di = port:PB17<3>default><default><default>
    
[/code]
### [system]
  * **recovery_key** : recovery key GPIO configuration

Configuration example: 
[code] 
    recovery_key = port:PH16<0><1><default><default>
    
[/code]
### [gpio_para]
  * **gpio_used** : 0 to disable; 1 to enable
  * **gpio_num** : number mapped GPIO's
  * **gpio_pin_1** : first GPIO pin

Configuration example: 
[code] 
    gpio_used = 0
    gpio_num = 4
    gpio_pin_1 = port:PH10<1><default><default><0>
    gpio_pin_2 = port:PH20<1><default><default><0>
    gpio_pin_3 = port:PB03<0><default><default><default>
    gpio_pin_4 = port:PH22<1><default><default><0>
    
[/code]
### [gpio_init]
  * **pin_1** : Initial pin 1 GPIO configuration

Configuration example: 
[code] 
    pin_1 = port:PH10<1><default><default><0>
    pin_2 = port:PH20<1><default><default><0>
    
[/code]
## SDRAM
### [dram_para]
SD-Ram is usually configured via livesuit when flashing. Livesuit probes the hardware or knows about the hardware and its configuration and configures the SoC accordingly. This luxury is not available from Linux and thus sdram parameters have to be set up by hand. 
  * **dram_baseaddr** : DRAM physical start address, fixed at 0x40000000
  * **dram_clk** : DRAM clock frequency in MHz; it must be an integer multiple of 24, minimally 120, maximally 480 MHz
  * **dram_type** : DRAM type; Set to 2 for DDR2; 3 for DDR3
  * **dram_rank_num** : DRAM chip select; 1 is a chip select; 2 election for two tablets
  * **dram_chip_density** : monolithic DRAM capacity in Mbit
  * **dram_io_width** : monolithic DRAM bus width in bits
  * **dram_bus_width** : DRAM bus width in bits, such as two 16-bit DRAM banks make up a 32 bit bus width
  * **dram_cas** : DRAM CAS latency
  * **dram_zq** : DRAM controller internal parameters
  * **dram_odt_en** : ODT 0 to disable; 1 to enable
  * **dram_size** : DRAM total capacity in MB
  * **dram_tpr0** : DRAM controller internal parameter
  * **dram_tpr1** : DRAM controller internal parameter
  * **dram_tpr2** : DRAM controller internal parameter
  * **dram_tpr3** : DRAM controller internal parameter
  * **dram_tpr4** : DRAM controller internal parameter
  * **dram_tpr5** : DRAM controller internal parameter
  * **dram_emr1** : DRAM controller internal parameter
  * **dram_emr2** : DRAM controller internal parameter
  * **dram_emr3** : DRAM controller internal parameter

Configuration example: 
[code] 
    [dram_para]
    dram_baseaddr = 0x40000000
    dram_clk = 360
    dram_type = 3
    dram_rank_num = 1
    dram_chip_density = 2048
    dram_io_width = 16
    dram_bus_width = 32
    dram_cas = 6
    dram_zq = 0x7b
    dram_odt_en = 0
    dram_size = 512
    dram_tpr0 = 0x30926692
    dram_tpr1 = 0x1090
    dram_tpr2 = 0x1a0c8
    dram_tpr3 = 0x0
    dram_tpr4 = 0x0
    dram_tpr5 = 0x0
    dram_emr1 = 0x0
    dram_emr2 = 0x0
    dram_emr3 = 0x0
    
[/code]
## mali configuration
[Mali][19482] is the name of the GPU on the A10, A10s, A13, A20, A23, and A33 SoC's 
### [mali_para]
  * **mali_used** : 0 to disable; 1 to enable Mali module
  * **mali_clkdiv** : Mali clock divisor. Clock is obtained by devising PLL4 with _mali_clkdiv_

Configuration example: 
[code] 
    [mali_para]
    mali_used = 1
    mali_clkdiv = 3
    
[/code]
### [g2d_para]
G2D is the 2D graphic display engine on the Allwinner SoC 
  * **g2d_used** : 0 to disable; 1 to enable the g2d module
  * **g2d_size** : memory size for g2d

[code] 
    g2d_used = 1
    g2d_size = 0x1000000
    
[/code]
## ethernet MAC configuration
### [emac_para]
Ethernet configuration for the integrated ethernet IP. It still requires an external PHY 
  * **emac_used** : 0 to disable; 1 to enable the ethernet MAC
  * **emac_rxd0** : RX data line 0 GPIO configuration
  * **emac_rxd1** : RX data line 1 GPIO configuration
  * **emac_rxd2** : RX data line 2 GPIO configuration
  * **emac_rxd3** : RX data line 3 GPIO configuration
  * **emac_txd0** : TX data line 0 GPIO configuration
  * **emac_txd1** : TX data line 1 GPIO configuration
  * **emac_txd2** : TX data line 2 GPIO configuration
  * **emac_txd3** : TX data line 3 GPIO configuration
  * **emac_rxclk** : RX clock GPIO configuration
  * **emac_rxerr** : RX error GPIO configuration
  * **emac_rxdV** : RX enabled GPIO configuration
  * **emac_mdc** : MII clock GPIO configuration
  * **emac_mdio** : MII data I/O GPIO configuration
  * **emac_txen** : TX enabled GPIO configuration
  * **emac_txclk** : TX clock GPIO configuration
  * **emac_crs** : Carrier Status of GPIO configuration
  * **emac_col** : Collision Detection GPIO configuration
  * **emac_reset** : PHY reset signal GPIO configuration
  * **emac_power** :
  * **emac_link** :

Configuration example: 
[code] 
    [Emac_para]
    emac_used = 1
    emac_rxd3 = port:PA00<2><default><default><default>
    emac_rxd2 = port:PA01<2><default><default><default>
    emac_rxd1 = port:PA02<2><default><default><default>
    emac_rxd0 = port:PA03<2><default><default><default>
    emac_txd3 = port:PA04<2><default><default><default>
    emac_txd2 = port:PA05<2><default><default><default>
    emac_txd1 = port:PA06<2><default><default><default>
    emac_txd0 = port:PA07<2><default><default><default>
    emac_rxclk = port:PA08<2><default><default><default>
    emac_rxerr = port:PA09<2><default><default><default>
    emac_rxdV = port:PA10<2><default><default><default>
    emac_mdc = port:PA11<2><default><default><default>
    emac_mdio = port:PA12<2><default><default><default>
    emac_txen = port:PA13<2><default><default><default>
    emac_txclk = port:PA14<2><default><default><default>
    emac_crs = port:PA15<2><default><default><default>
    emac_col = port:PA16<2><default><default><default>
    emac_reset = port:PA17<1><default><default><default>
    
[/code]
## i2c configuration
### [twi0_para]
Two Wire Interface (i²c) configuration for TWI port 0 
  * **twi0_used** : 0 to disable; 1 to enable
  * **twi0_scl** : TWI Serial CLock GPIO configuration
  * **twi0_sda** : TWI Serial Data GPIO configuration

Configuration example: 
[code] 
    [twi0_para]
    twi0_used = 1
    twi0_scl = port:PB00<2><default><default><default>
    twi0_sda = port:PB01<2><default><default><default>
    
[/code]
### [twi1_para]
Two Wire Interface (i²c) configuration for TWI port 1 
  * **twi1_used** : 0 to disable; 1 to enable
  * **twi1_scl** : TWI Serial CLock GPIO configuration
  * **twi1_sda** : TWI Serial Data GPIO configuration

Configuration example: 
[code] 
    [tw1_para]
    twi1_used = 1
    twi1_scl = port:PB18<2><default><default><default>
    twi1_sda = port:PB19<2><default><default><default>
    
[/code]
### [twi2_para]
Two Wire Interface (i²c) configuration for TWI port 2 
  * **twi2_used** : 0 to disable; 1 to enable
  * **twi2_scl** : TWI Serial CLock GPIO configuration
  * **twi2_sda** : TWI Serial Data GPIO configuration

Configuration example: 
[code] 
    [twi2_para]
    twi2_used = 1
    twi2_scl = port:PB20<2><default><default><default>
    twi2_sda = port:PB21<2><default><default><default>
    
[/code]
## uart configuration
Any of the 8 UART ports can be configured to be either 2 (Only TX/RX) wires, 4 wires (TX, RX, RTS and CTS) or 8 (Full function) ports. 
  * **uart_used** : 0 to disable; 1 to enable
  * **uart_port** : UART port number
  * **uart_type** : UART type, 2, 4 or 8 wires
  * **uart_tx** : UART TX data line GPIO configuration
  * **uart_rx** : UART RX data line GPIO configuration
  * **uart_rts** : UART Ready to Send line GPIO configuration, only for 4 and 8 wire modes
  * **uart_cts** : UART Clear to Send line GPIO configuration, only for 4 and 8 wire modes
  * **uart_dtr** : UART Data Terminal Ready GPIO configuration, only for 8 wire modes
  * **uart_dsr** : UART Data Set Ready GPIO configuration, only for 8 wire modes
  * **uart_dcd** : UART Data Carrier Detect GPIO configuration, only for 8 wire modes
  * **uart_ring** : UART Ring Indicator GPIO configuration, only for 8 wire modes

### [uart_para0]
Configuration example: 
[code] 
    [uart_para0]
    uart_used = 1
    uart_port = 0
    uart_tx = port:PB22<2><1><default><default>
    uart_rx = port:PB23<2><1><default><default>
    
[/code]
### [uart_para1]
Configuration example: 
[code] 
    [uart_para1]
    uart_used = 0
    uart_port = 1
    uart_type = 8
    uart_tx = port:PA10<4><1><default><default>
    uart_rx = port:PA11<4><1><default><default>
    uart_rts = port:PA12<4><1><default><default>
    uart_cts = port:PA13<4><1><default><default>
    uart_dtr = port:PA14<4><1><default><default>
    uart_dsr = port:PA15<4><1><default><default>
    uart_dcd = port:PA16<4><1><default><default>
    uart_ring = port:PA17<4><1><default><default>
    
[/code]
### [uart_para2]
Configuration example: 
[code] 
    [uart_para2]
    uart_used = 0
    uart_port = 2
    uart_type = 4
    uart_tx = port:PI18<3><1><default><default>
    uart_rx = port:PI19<3><1><default><default>
    uart_rts = port:PI16<3><1><default><default>
    uart_cts = port:PI17<3><1><default><default>
    
[/code]
### [uart_para3]
Configuration example: 
[code] 
    [uart_para3]
    uart_used = 0
    uart_port = 3
    uart_type = 4
    uart_tx = port:PH00<4><1><default><default>
    uart_rx = port:PH01<4><1><default><default>
    uart_rts = port:PH02<4><1><default><default>
    uart_cts = port:PH03<4><1><default><default>
    
[/code]
### [uart_para4]
Configuration example: 
[code] 
    [Uart_para4]
    uart_used = 0
    uart_port = 4
    uart_type = 2
    uart_tx = port:PH04<4><1><default><default>
    uart_rx = port:PH05<4><1><default><default>
    
[/code]
### [uart_para5]
Configuration example: 
[code] 
    [uart_para5]
    uart_used = 0
    uart_port = 5
    uart_type = 2
    uart_tx = port: PH06<4><1><default><default>
    uart_rx = port: PH07<4><1><default><default>
    
[/code]
### [uart_para6]
Configuration example: 
[code] 
    [uart_para6]
    uart_used = 0
    uart_port = 6
    uart_type = 2
    uart_tx = port:PA12<4><1><default><default>
    uart_rx = port:PA13<4><1><default><default>
    
[/code]
### [uart_para7]
Configuration example: 
[code] 
    [uart_para7]
    uart_used = 0
    uart_port = 7
    uart_type = 2
    uart_tx = port:PA14<4><1><default><default>
    uart_rx = port:PA15<4><1><default><default>
    
[/code]
## spi configuration
  * **spi_used** : 0 to disable; 1 to enable
  * **spi_cs_bitmap** : 1 use cs0, 2 use cs1, 3 use cs0 & cs1
  * **spi_cs0** : Chip Select bit 0 GPIO configuration
  * **spi_cs1** : Chip Select bit 1 GPIO configuration
  * **spi_sclk** : clock GPIO configuration
  * **spi_mosi** : MOSI GPIO configuration
  * **spi_miso** : MISO GPIO configuration

[![Sticky-note-pin.png][19474]][19475] _Note:_ Not all spi chip select bits are required to be set 
### [spi0_para]
Configuration example 1: 
[code] 
    [spi0_para]
    spi_used = 0
    spi_cs_bitmap = 1
    spi_cs0 = port:PI10<3><default><default><default>
    spi_sclk = port:PI11<3><default><default><default>
    spi_mosi = port:PI12<3><default><default><default>
    spi_miso = port:PI13<3><default><default><default>
    spi_cs1 = port:PI14<3><default><default><default>
    
[/code]
Configuration example 2: 
[code] 
    [spi0_para]
    spi_used = 0
    spi_cs_bitmap = 1
    spi_mosi = port:PC00<3><default><default><default>
    spi_miso = port:PC01<3><default><default><default>
    spi_sclk = port:PC02<3><default><default><default>
    spi_cs0 = port:PC23<3><default><default><default>
    
[/code]
### [spi1_para]
Configuration example 1: 
[code] 
    [spi1_para]
    spi_used = 0
    spi_cs_bitmap = 1
    spi_cs0 = port:PA00<3><default><default><default>
    spi_sclk = port:PA01<3><default><default><default>
    spi_mosi = port:PA02<3><default><default><default>
    spi_miso = port:PA03<3><default><default><default>
    spi_cs1 = port:PA04<3><default><default><default>
    
[/code]
Configuration example 2: 
[code] 
    [spi1_para]
    spi_used = 0
    spi_cs_bitmap = 1
    spi_cs1 = port:PI15<2><default><default><default>
    spi_cs0 = port:PI16<2><default><default><default>
    spi_sclk = port:PI17<2><default><default><default>
    spi_mosi = port:PI18<2><default><default><default>
    spi_miso = port:PI19<2><default><default><default>
    
[/code]
### [spi2_para]
Configuration example 1: 
[code] 
    [spi2_para]
    spi_used = 0
    spi_cs_bitmap = 1
    spi_cs1 = port:PB13<3><default><default><default>
    spi_cs0 = port:PB14<3><default><default><default>
    spi_sclk = port:PB15<3><default><default><default>
    spi_mosi = port:PB16<3><default><default><default>
    spi_miso = port:PB17<3><default><default><default>
    
[/code]
Configuration example 2: 
[code] 
    [spi2_para]
    spi_used = 0
    spi_cs_bitmap = 1
    spi_cs0 = port:PC19<3><default><default><default>
    spi_sclk = port:PC20<3><default><default><default>
    spi_mosi = port:PC21<3><default><default><default>
    spi_miso = port:PC23<3><default><default><default>
    
[/code]
### [spi3_para]
Configuration example: 
[code] 
    [spi3_para]
    spi_used = 0
    spi_cs_bitmap = 1
    spi_cs0 = port:PA05<3><default><default><default>
    spi_sclk = port:PA06<3><default><default><default>
    spi_mosi = port:PA07<3><default><default><default>
    spi_miso = port:PA08<3><default><default><default>
    spi_cs1 = port:PA09<3><default><default><default>
    
[/code]
## external spi device configuration
### [spi_devices]
  * **spi_dev_num** : number of external SPI devices connected to the SoC. For each external SPI device N, a board define _[spi_boardM]_ with M = N - 1 needs to be created

### [spi_board0]
  * **modalias** : Alias
  * **max_speed_hz: Maximum speed in Hz**
  * **bus_num** : Bus number of SPI controller
  * **mode** : SPI mode, bitfield defined in [spi.h][19483]
  * **full_duplex** : 0 for half-duplex; 1 for full-duplex mode
  * **manual_cs** : manually control Chip Select level (unsupported for now)
  * **irq_gpio** : Some SPI boards should need a IRQ to work properly and register the irq handler inside the device driver

Configuration example: 
[code] 
    [spi_board0]
    modalias = "External SPI connection"
    max_speed_hz = 12000000
    bus_num = 1
    chip_select = 0
    mode = 3
    full_duplex = 0
    manual_cs = 0
    irq_gpio = 1
    
    [gpio_para]
    gpio_used = 1
    gpio_num = 1
    gpio_pin_1 = port:PB04<6><default><default><default> 
    
[/code]
## resistive touch panel configuration
### [rtp_para]
  * **rtp_used** : 0 to disable; 1 to enable
  * **rtp_screen_size** : diagonal screen size rounded to full inches
  * **rtp_regidity_level** : touchscreen regidty in 10 ms units
  * **rtp_press_threshold_enable** : 0 to disable; 1 to enable
  * **rtp_press_threshold** : defines the press-threshold sensitivity; (0x0 is least sensitive, 0xffffff is most sensitive) using TP Pressure Management threshold control (PRE_MEA_THRE_CNT register in [A20 User Manual][19484])
  * **rtp_sensitive_level** : defines the sensitivity (0x0 is least sensitive, 0xf is most sensitive) using internal pull-up resistor control (TP_SENSITIVE_ADJUST register in [A20 User Manual][19484])
  * **rtp_exchange_x_y_flag** : 0 for normal operation; 1 to flip X and Y coordinates

Configuration example: 
[code] 
    rtp_used = 0
    rtp_screen_size = 7
    rtp_regidity_level = 7
    rtp_press_threshold_enable = 0
    rtp_press_threshold = 0x1f40
    rtp_sensitive_level = 0xf
    rtp_exchange_x_y_flag = 0
    
[/code]
## capacitive touch panel configuration
### [ctp_para]
Several touch panel's can be configured. Their name must match to the linux ctp-driver! 
  * **ctp_used** : 0 to disable; 1 to enable
  * **ctp_name** : Name of the touch panel driver to use
  * **ctp_twi_id** : twi controller to use
  * **ctp_twi_addr** : hardware specfic twi address in hex
  * **ctp_screen_rotate** : 0 for normal operation; 1 for 180° rotation
  * **ctp_screen_max_x** : Maximum X screen resolution
  * **ctp_screen_max_y** : Maximum Y screen resolution
  * **ctp_revert_x_flag** : 0 for normal operation; 1 to flip the X axis
  * **ctp_revert_y_flag** : 0 for normal operation; 1 to flip the Y axis
  * **ctp_havekey** : 0 for normal operation; 1 if the touch panel also has touch-_keys_.
  * **ctp_int_port** : interrupt line GPIO configuration
  * **ctp_wakeup** : screen wake up GPIO configuration
  * **ctp_io_port** : I/O port GPIO configuration

Configuration example: 
[code] 
    [ctp_para]
    ctp_used = 1
    ctp_twi_id = 2
    ctp_name = "ft5x_ts"
    ctp_twi_addr = 0x38
    
    ctp1_used = 1
    ctp1_name = "Goodix-TS"
    ctp1_twi_addr = 0x55
    
    ctp2_used = 1
    ctp2_name = "ssd253x-ts"
    ctp2_twi_addr = 0x48
    
    ctp3_used = 1
    ctp3_name = "novatek-ts"
    ctp3_twi_addr = 0x09
    
    ctp4_used = 1
    ctp4_name = "zet622x-ts"
    ctp4_twi_addr = 0x76
    
    ctp5_used = 1
    ctp5_name = "byd693x-ts"
    ctp5_twi_addr = 0x52
    
    ctp6_used = 0
    ctp6_name = "gt82x"
    ctp6_twi_addr = 0x5d
    
    ctp7_used = 0
    ctp7_name = "px811"
    ctp7_twi_addr = 0x5c
    
    ctp_screen_rotate = 0
    ctp_screen_max_x = 800
    ctp_screen_max_y = 480
    ctp_revert_x_flag = 0
    ctp_revert_y_flag = 0
    ctp_exchange_x_y_flag = 0
    ctp_havekey = 0
    ctp_int_port = port: PH21<6><default><default><default>
    ctp_wakeup = port: PB13<1><default><default><1>
    ctp_io_port = port: PH21<0><default><default><default>
    
[/code]
## touch key configuration
### [tkey_para]
Touch 'key', only for "hv_keypad" for now 
  * **tkey_used** : 0 to disable; 1 to enable
  * **tkey_name** : driver name, must match linux driver name
  * **tkey_twi_id** : twi controller to use
  * **tkey_twi_addr** : hardware specfic twi address in hex
  * **tkey_int** : interrupt line GPIO configuration

Configuration example: 
[code] 
    [tkey_para]
    tkey_used = 0
    tkey_name = "hv_keypad"
    tkey_twi_id = 2
    tkey_twi_addr = 0x62
    tkey_int = port: PI13<6><default><default><default>
    
[/code]
## microphone configuration
### [micphone_para]
  * **micphone_used** : 0 to disable; 1 to enable
  * **micphone_name** : driver name, must match linux driver name
  * **mic_port** : mic GPIO port
  * **headset_port** : headset GPIO port
  * **audio_pa_ctrl** : External Amp shutdown GPIO configuration

Configuration example: 
[code] 
    [micphone_para]
    micphone_used = 1
    micphone_name = "micphone_keypad"
    mic_port = port:PH20<0><default><default><default>
    headset_port = port:PH16<0><default><default><default>
    audio_pa_ctrl = port:PH15<1><default><default><0>
    
[/code]
## tablet key configuration
Configures tablet physical buttons - usually Vol+ and Vol-, may have Home, Back and others. 
Power key is usually handled by the AXP PMU. Buttons like reset and FEL are special and should work without a driver. 
### [tabletkeys_para]
  * **tabletkeys_used** : 0 to disable; 1 to enable
  * **keyN_code** : numeric keycode - easily found with evtest. N seems to be 0-4 by default.

Configuration example: 
[code] 
    [tabletkeys_para]
    tabletkeys_used=1
    key0_code = 114
    key1_code = 115
    
[/code]
## motor configuration
### [motor_para]
  * **motor_used** : 0 to disable; 1 to enable
  * **motor_shake** : motor control pin GPIO configuration

Configuration example: 
[code] 
    [motor_para]
    motor_used = 0
    motor_shake = port:PB03<1><default><default><1>
    
[/code]
## lock configuration
Locks are either very new or really old as nothing can be found in any fex file in git. It seems reasonable to believe that this would be a screen lock 'button'. 
### [locks_para]
  * **locks_used** : 0 to disable; 1 to enable
  * **locks_gpio** : switch GPIO configuration

Configuration example: 
[code] 
    [locks_para]
    locks_used = 0
    locks_gpio = port:PH00<0><default><default><0>
    
[/code]
## nand flash configuration
### [nand_para]
  * **nand_used** : 0 to disable; 1 to enable
  * **nand_we** : Write Enable GPIO configuration
  * **nand_ale** : Address Latch Enable GPIO configuration
  * **nand_cle** : Command Latch Enable GPIO configuration
  * **nand_ce0** : Chip sElect bit 0 GPIO configuration
  * **nand_ce1** : Chip sElect bit 1 GPIO configuration
  * **nand_ce2** : Chip sElect bit 2 GPIO configuration
  * **nand_ce3** : Chip sElect bit 3 GPIO configuration
  * **nand_ce4** : Chip sElect bit 4 GPIO configuration
  * **nand_ce5** : Chip sElect bit 5 GPIO configuration
  * **nand_ce6** : Chip sElect bit 6 GPIO configuration
  * **nand_ce7** : Chip sElect bit 7 GPIO configuration
  * **nand_nre** : Nand Read Enable GPIO configuration
  * **nand_rb0** : Read / Busy bit 0 GPIO configuration
  * **nand_rb1** : Read / Busy bit 1 GPIO configuration
  * **nand_d0** : data bus bit 0 GPIO configuration
  * **nand_d1** : data bus bit 1 GPIO configuration
  * **nand_d2** : data bus bit 2 GPIO configuration
  * **nand_d3** : data bus bit 3 GPIO configuration
  * **nand_d4** : data bus bit 4 GPIO configuration
  * **nand_d5** : data bus bit 5 GPIO configuration
  * **nand_d6** : data bus bit 6 GPIO configuration
  * **nand_d7** : data bus bit 7 GPIO configuration
  * **nand_wp** : Write Protect GPIO configuration
  * **nand_spi** : SPI data line GPIO configuration
  * **nand_ndqs** : nand ddr clock signal GPIO configuration

Configuration example: 
[code] 
    [Nand_para]
    nand_used = 1
    nand_we = port:PC00<2><default><default><default>
    nand_ale = port:PC01<2><default><default><default>
    nand_cle = port:PC02<2><default><default><default>
    nand_ce1 = port:PC03<2><default><default><default>
    nand_ce0 = port:PC04<2><default><default><default>
    nand_nre = port:PC05<2><default><default><default>
    nand_rb0 = port:PC06<2><default><default><default>
    nand_rb1 = port:PC07<2><default><default><default>
    nand_d0 = port:PC08<2><default><default><default>
    nand_d1 = port:PC09<2><default><default><default>
    nand_d2 = port:PC10<2><default><default><default>
    nand_d3 = port:PC11<2><default><default><default>
    nand_d4 = port:PC12<2><default><default><default>
    nand_d5 = port:PC13<2><default><default><default>
    nand_d6 = port:PC14<2><default><default><default>
    nand_d7 = port:PC15<2><default><default><default>
    nand_wp = port:PC16<2><default><default><default>
    nand_ce2 = port:PC17<2><default><default><default>
    nand_ce3 = port:PC18<2><default><default><default>
    nand_ce4 = port:PC19<2><default><default><default>
    nand_ce5 = port:PC20<2><default><default><default>
    nand_ce6 = port:PC21<2><default><default><default>
    nand_ce7 = port:PC22<2><default><default><default>
    nand_spi = port:PC23<3><default><default><default>
    nand_ndqs = port:PC24<2><default><default><default>
    
[/code]
## boot disp configuration
### [boot_disp]
This section can be found in vendor fex files for H3 devices and is only used by Allwinner's BSP u-boot (eg. to display a boot logo which might require [further patches][19485]) 
## disp init configuration
### [disp_init]
  * **disp_init_enable** : 0 to disable; 1 to enable
  * **disp_mode** : Display mode to use:

    
    
     mode  | display mode   
---|---  
0  | screen0(screen0, fb0)   
1  | screen1(screen1, fb0)   
2  | dualhead(screen0, screen1, fb0, fb1) (2 screens, 2 framebuffers)   
3  | xinerama(screen0, screen1, fb0) (2 screens, one big framebuffer)   
4  | clone(screen0, screen1, fb0) (2 screens, one standard framebuffer)   
  * **screen0_out_color_range** : Output color range for HDMI (applies to both screen0/screen1 - there is no screen1_out_color_range):

    
    
     type  | output color range   
---|---  
0  | 16-255 Limited Range (Default)   
1  | 0-255 Full Range - PC Level   
2  | 16-235 Limited Range - Video Level   
  * **screen0_output_type** : Output type for screen0:
  * **screen1_output_type** : Output type for screen1:

    
    
     type  | Output type   
---|---  
0  | NONE   
1  | LCD   
2  | TV   
3  | HDMI   
4  | VGA   
  * **screen0_output_mode** : Output mode for screen0:
  * **screen1_output_mode** : Output mode for screen1:

    
    
     mode  | used for tv/hdmi output  | used for vga output   
---|---|---  
0  | 480i  | 1680*1050   
1  | 576i  | 1440*900   
2  | 480p  | 1360*768   
3  | 576p  | 1280*1024   
4  | 720p50  | 1024*768   
5  | 720p60  | 800*600   
6  | 1080i50  | 640*480   
7  | 1080i60  |   
8  | 1080p24  |   
9  | 1080p50  |   
10  | 1080p60  | 1920*1080   
11  | pal  | 1280*720   
14  | ntsc  |   
  * **fb0_framebuffer_num** : fb0 buffer number, use _2_ for double buffering
  * **fb1_framebuffer_num** : fb1 buffer number, use _2_ for double buffering
  * **fb0_format** : pixel format for fb0:
  * **fb1_format** : pixel format for fb1:

    
    
     format  | fb0_format   
---|---  
4  | RGB655   
5  | RGB565   
6  | RGB556   
7  | ARGB1555   
8  | RGBA5551   
9  | RGB888   
10  | ARGB8888   
12  | ARGB4444   
  * **fb0_pixel_sequence** : fb0 pixel sequence (0 generally for linux, 2 for android):
  * **fb1_pixel_sequence** : fb1 pixel sequence (0 generally for linux, 2 for android):

    
    
     sequence  | fb0_pixel_sequence   
---|---  
0  | ARGB   
2  | BGRA   
  * **fb0_scaler_mode_enable** : 0 to disable; 1 to enable
  * **fb1_scaler_mode_enable** : 0 to disable; 1 to enable
  * **lcd0_backlight** : value to 240 sets PWM rate on selected PWM gpio
  * **lcd1_backlight** : value to 240 sets PWM rate on selected PWM gpio

  
Configuration example for LCD: 
[code] 
    [disp_init]
    disp_init_enable = 1
    disp_mode = 0
    
    screen0_output_type = 1
    screen0_output_mode = 4
    
    screen1_output_type = 1
    screen1_output_mode = 4
    
    fb0_framebuffer_num = 2
    fb0_format = 10
    fb0_pixel_sequence = 0
    fb0_scaler_mode_enable = 0
    
    fb1_framebuffer_num = 2
    fb1_format = 10
    fb1_pixel_sequence = 0
    fb1_scaler_mode_enable = 0
    
[/code]
Configuration example for VGA: 
[code] 
    [disp_init]
    disp_init_enable = 1
    disp_mode = 0
    
    screen0_output_type = 4
    screen0_output_mode = 4
    
    screen1_output_type = 2
    screen1_output_mode = 14
    
    fb0_framebuffer_num = 2
    fb0_format = 10
    fb0_pixel_sequence = 0
    fb0_scaler_mode_enable = 1
    
    fb1_framebuffer_num = 2
    fb1_format = 10
    fb1_pixel_sequence = 0
    fb1_scaler_mode_enable = 1
    
[/code]
Configuration example for Composite TV on an old TV (PAL mode): 
[code] 
    [disp_init]
    disp_init_enable = 1
    disp_mode = 0
    
    screen0_output_type = 2
    screen0_output_mode = 11
    
    screen1_output_type = 2
    screen1_output_mode = 11
    
    fb0_framebuffer_num = 2
    fb0_format = 10
    fb0_pixel_sequence = 0
    fb0_scaler_mode_enable = 1
    
    fb1_framebuffer_num = 2
    fb1_format = 10
    fb1_pixel_sequence = 0
    fb1_scaler_mode_enable = 1
    
[/code]
## lcd[0/1] configuration
lcd0 is used when lcd output is selected by display screen0, lcd1 by display screen1. 
  * **lcd_used** : 0 to disable; 1 to enable
  * **lcd_pwm_not_used** : 0 to enable PWM; 1 to disable
  * **lcd_pwm_ch** : PWM channel
  * **lcd_pwm_freq** : PWM frequency in Hz
  * **lcd_pwm_pol** : PWM polarity; 0 is pulse LOW for lcd[0|1]_backlight periods, 1 is pulse HIGH.
  * **lcd_x** : X-axis active width
  * **lcd_y** : Y-axis active height
  * **lcd_dclk_freq** : pixel clock frequency in MHz
  * **lcd_if** : lcd interface:

    
    
     interface  | lcd_interface   
---|---  
0  | hv (sync + de)   
1  | 8080   
2  | ttl   
3  | lvds   
4  | dsi (on [A20][19486] it means the use of [SSD2828][19487] bridge chip, on [A31][19488] it might really mean native DSI)   
5  | edp   
6  | external dsi (the use of [SSD2828][19487] bridge chip on [A31][19488] and onwards)   
  * **lcd_hbp** : hsync back porch
  * **lcd_ht** : hsync total cycle
  * **lcd_vbp** : vsync back porch
  * **lcd_vt** : vsync total cycle * 2
  * **lcd_hv_if** : 0 for parallel hv interface; 1: for serial hv interface
  * **lcd_hv_smode** : 0 for RGB888 serial interface mode; 1 for CCIR656
  * **lcd_hv_s888_if** : serial RGB format
  * **lcd_hv_syuv_if** : serial YUV format
  * **lcd_hv_vspw** : vysnc pulse width
  * **lcd_hv_hspw** : hsync pulse width
  * **lcd_hv_lde_used** : 0 to disable; 1 to enable
  * **lcd_hv_lde_iovalue** : HV LDE iovalue
  * **lcd_lvds_ch** : 0 for single channel; 1 for dual channel
  * **lcd_lvds_mode** : 0 for NS mode; 1 for JEIDA mode
  * **lcd_lvds_bitwidth** : 0 for 24 bit; 1 for 18 bit
  * **lcd_io_cfg0** : lcd IO configuration
  * **lcd_lvds_io_cross** : 0 for normal; 1 for pn cross
  * **lcd_cpu_if** : cpu if mode:

    
    
     mode  | cpu_if   
---|---  
0  | 18 bit   
1  | 16 bit mode0   
2  | 16 bit mode1   
3  | 16 bit mode2   
4  | 16 bit mode3   
5  | 9 bit   
6  | 8 bit, 256k   
7  | 8 bit, 65k   
  * **lcd_gamma_correction_en** : 0 to disable; 1 to enable
  * **lcd_gamma_tbl_[0-255]** : Gamma table 0 through 255
  * **lcd_frm** : 0 to disable dither; 1 to enable enable rgb666 dither; 2 to enable rgb656 dither
  * **lcd_io_cfg0** : lcd io inv
  * **lcd_bl_en_used** : 0 to disable; 1 to enable
  * **lcd_bl_en** : LCD BackLight GPIO configuration
  * **lcd_power_used** : 0 to disable; 1 to enable
  * **lcd_power** : LCD_VCC Voltage control GPIO configuration
  * **lcd_pwm_used** : 0 to disable; 1 to enable
  * **lcd_pwm** : lcd PWM, GPIO configuration (PWM0 fixed using the PB02 PWM1 fixed PI03 without user modification)
  * **lcd_gpio_0** : 2/3-wire SCL GPIO configuration
  * **lcd_gpio_1** : 2/3-wire SDA GPIO configuration
  * **lcd_gpio_2** : 2/3-wire SCEN GPIO configuration
  * **lcd_gpio_3** : LCD module RESET GPIO configuration
  * **lcdd0** : data bit 0 GPIO configuration
  * **lcdd1** : data bit 1 GPIO configuration
  * **lcdd2** : data bit 2 GPIO configuration
  * **lcdd3** : data bit 3 GPIO configuration
  * **lcdd4** : data bit 4 GPIO configuration
  * **lcdd5** : data bit 5 GPIO configuration
  * **lcdd6** : data bit 6 GPIO configuration
  * **lcdd7** : data bit 7 GPIO configuration
  * **lcdd8** : data bit 8 GPIO configuration
  * **lcdd9** : data bit 9 GPIO configuration
  * **lcdd10** : data bit 10 GPIO configuration
  * **lcdd11** : data bit 11 GPIO configuration
  * **lcdd12** : data bit 12 GPIO configuration
  * **lcdd13** : data bit 13 GPIO configuration
  * **lcdd14** : data bit 14 GPIO configuration
  * **lcdd15** : data bit 15 GPIO configuration
  * **lcdd16** : data bit 16 GPIO configuration
  * **lcdd17** : data bit 17 GPIO configuration
  * **lcdd18** : data bit 18 GPIO configuration
  * **lcdd19** : data bit 19 GPIO configuration
  * **lcdd20** : data bit 20 GPIO configuration
  * **lcdd21** : data bit 21 GPIO configuration
  * **lcdd22** : data bit 22 GPIO configuration
  * **lcdd23** : data bit 23 GPIO configuration
  * **lcdclk** : LCD Clock GPIO configuration
  * **lcdde** : LCD _de_ GPIO configuration
  * **lcdhsync** : H sync GPIO configuration
  * **lcdvsync** : V sync GPIO configuration

### [lcd0_para]
Configuration example: 
[code] 
    [lcd0_para]
    lcd_used = 1
    lcd_x = 800
    lcd_y = 480
    lcd_dclk_freq = 33
    lcd_pwm_freq = 1000
    lcd_pwm_pol = 0
    lcd_swap = 0
    lcd_if = 0
    lcd_hbp = 215
    lcd_ht = 1055
    lcd_vbp = 34
    lcd_vt = 1050
    lcd_hv_if = 0
    lcd_hv_smode = 0
    lcd_hv_s888_if = 0
    lcd_hv_syuv_if = 0
    lcd_hv_vspw = 0
    lcd_hv_hspw = 0
    lcd_hv_lde_used = 0
    lcd_hv_lde_iovalue = 0
    lcd_lvds_ch = 0
    lcd_lvds_mode = 0
    lcd_lvds_bitwidth = 0
    lcd_lvds_io_cross = 0
    lcd_cpu_if = 0
    lcd_cpu_da = 0
    lcd_frm = 0
    lcd_io_cfg0 = 0x10000000
    lcd_io_cfg1 = 0
    lcd_io_strength = 0
    lcd_bl_en_used = 1
    lcd_bl_en = port: PH07<1><0><default><1>
    lcd_power_used = 1
    lcd_power = port: PH08<1><0><default><1>
    lcd_pwm_used = 1
    lcd_pwm = port:PB02<2><default><default><default>
    lcd_gpio_0 =
    lcd_gpio_1 =
    lcd_gpio_2 =
    lcd_gpio_3 =
    lcdd0 = port:PD00<2><default><default><default>
    lcdd1 = port:PD01<2><default><default><default>
    lcdd2 = port:PD02<2><default><default><default>
    lcdd3 = port:PD03<2><default><default><default>
    lcdd4 = port:PD04<2><default><default><default>
    lcdd5 = port:PD05<2><default><default><default>
    lcdd6 = port:PD06<2><default><default><default>
    lcdd7 = port:PD07<2><default><default><default>
    lcdd8 = port:PD08<2><default><default><default>
    lcdd9 = port:PD09<2><default><default><default>
    lcdd10 = port:PD10<2><default><default><default>
    lcdd11 = port:PD11<2><default><default><default>
    lcdd12 = port:PD12<2><default><default><default>
    lcdd13 = port:PD13<2><default><default><default>
    lcdd14 = port:PD14<2><default><default><default>
    lcdd15 = port:PD15<2><default><default><default>
    lcdd16 = port:PD16<2><default><default><default>
    lcdd17 = port:PD17<2><default><default><default>
    lcdd18 = port:PD18<2><default><default><default>
    lcdd19 = port:PD19<2><default><default><default>
    lcdd20 = port:PD20<2><default><default><default>
    lcdd21 = port:PD21<2><default><default><default>
    lcdd22 = port:PD22<2><default><default><default>
    lcdd23 = port:PD23<2><default><default><default>
    lcdclk = port:PD24<2><default><default><default>
    lcdde = port:PD25<2><default><default><default>
    lcdhsync = port:PD26<2><default><default><default>
    lcdvsync = port:PD27<2><default><default><default>
    
[/code]
Other configuration examples for certain panels: 
[code] 
    ;lvds 640x480   module name: SG0570EDG
    lcd_x                    = 640
    lcd_y                    = 480
    lcd_dclk_freq            = 25
    lcd_if                   = 3
    lcd_hbp                  = 114
    lcd_ht                   = 800
    lcd_vt                   = 1050
    lcd_vbp                  = 34
    lcd_pwm_freq             = 20000
    lcd_lvds_bitwidth        = 1
    lcd_pwm_used             = 1
    lcd_pwm                  = port:PB02<2><0><default><default>
    lcd_pwm_pol              = 0
    
    ;RGB 800x480	module name: H-B070D-15C
    lcd_x                    = 800
    lcd_y                    = 480
    lcd_dclk_freq            = 33
    lcd_if                   = 0
    lcd_hbp                  = 46
    lcd_ht                   = 1055
    lcd_vbp                  = 23
    lcd_vt                   = 1050
    
    ;RGB 800x600    module name: H-B080D-24F
    lcd_x                    = 800
    lcd_y                    = 600
    lcd_dclk_freq            = 40
    lcd_if                   = 0
    lcd_hbp                  = 46
    lcd_ht                   = 1056
    lcd_vbp                  = 23
    lcd_vt                   = 1270
    
    
    ;RGB 480x272    module name: KD43G18-40NB-A11
    lcd_x                    = 480
    lcd_y                    = 272
    lcd_dclk_freq            = 9
    lcd_if                   = 0
    lcd_hbp                  = 2
    lcd_ht                   = 525
    lcd_vbp                  = 2
    lcd_vt                   = 572
    
    ;lvds 1024x600   module name: CLAP101NC01CW�
    lcd_x                    = 1024
    lcd_y                    = 600
    lcd_dclk_freq            = 52
    lcd_if                   = 3
    lcd_hbp                  = 33
    lcd_ht                   = 1344
    lcd_vbp                  = 23
    lcd_vt                   = 1270
    
    ;lvds 1024x768   module name: KD080D3-40NA-A2
    lcd_x                    = 1024
    lcd_y                    = 768
    lcd_dclk_freq            = 65
    lcd_if                   = 3
    lcd_hbp                  = 160
    lcd_ht                   = 1344
    lcd_vbp                  = 23
    lcd_vt                   = 1612
    
    ;lvds 1024x768   module name: LG-LP097X02
    lcd_x                    = 1024
    lcd_y                    = 768
    lcd_dclk_freq            = 100
    lcd_if                   = 3
    lcd_hbp                  = 480
    lcd_ht                   = 2084
    lcd_vbp                  = 6
    lcd_vt                   = 1600
    lcd_lvds_bitwidth        = 1
    lcd_io_cfg0              = 0x04000000
    lcd_frm                  = 1
    
    lcd_io_cfg0              = 0x10000000
    lcd_gamma_correction_en  = 0
    lcd_gamma_tbl_0          = 0x00000000
    lcd_gamma_tbl_1          = 0x00010101
    ;........
    lcd_gamma_tbl_255        = 0x00ffffff
    
[/code]
### [lcd1_para]
Configuration example: 
[code] 
    [lcd1_para]
    lcd_used                 = 0
    
    lcd_x                    = 0
    lcd_y                    = 0
    lcd_dclk_freq            = 0
    lcd_pwm_not_used         = 0
    lcd_pwm_ch               = 0
    lcd_pwm_freq             = 0
    lcd_pwm_pol              = 0
    lcd_if                   = 0
    lcd_hbp                  = 0
    lcd_ht                   = 0
    lcd_vbp                  = 0
    lcd_vt                   = 0
    lcd_hv_if                = 0
    lcd_hv_smode             = 0
    lcd_hv_s888_if           = 0
    lcd_hv_syuv_if           = 0
    lcd_hv_vspw              = 0
    lcd_hv_hspw              = 0
    lcd_lvds_ch              = 0
    lcd_lvds_mode            = 0
    lcd_lvds_bitwidth        = 0
    lcd_lvds_io_cross        = 0
    lcd_cpu_if               = 0
    lcd_frm                  = 0
    lcd_io_cfg0              = 0
    lcd_gamma_correction_en  = 0
    lcd_gamma_tbl_0          = 0x00000000
    lcd_gamma_tbl_1          = 0x00010101
    ;........
    lcd_gamma_tbl_255        = 0x00ffffff
    
    lcd_bl_en_used           = 0
    lcd_bl_en                =
    
    lcd_power_used           = 0
    lcd_power                = 
    
    lcd_pwm_used             = 0
    lcd_pwm                  = port:PI03<2><0><default><default>
    
    lcd_gpio_0               = 
    lcd_gpio_1               = 
    lcd_gpio_2               = 
    lcd_gpio_3               = 
    
    lcdd0                    = port:PH00<2><0><default><default>
    lcdd1                    = port:PH01<2><0><default><default>
    lcdd2                    = port:PH02<2><0><default><default>
    lcdd3                    = port:PH03<2><0><default><default>
    lcdd4                    = port:PH04<2><0><default><default>
    lcdd5                    = port:PH05<2><0><default><default>
    lcdd6                    = port:PH06<2><0><default><default>
    lcdd7                    = port:PH07<2><0><default><default>
    lcdd8                    = port:PH08<2><0><default><default>
    lcdd9                    = port:PH09<2><0><default><default>
    lcdd10                   = port:PH10<2><0><default><default>
    lcdd11                   = port:PH11<2><0><default><default>
    lcdd12                   = port:PH12<2><0><default><default>
    lcdd13                   = port:PH13<2><0><default><default>
    lcdd14                   = port:PH14<2><0><default><default>
    lcdd15                   = port:PH15<2><0><default><default>
    lcdd16                   = port:PH16<2><0><default><default>
    lcdd17                   = port:PH17<2><0><default><default>
    lcdd18                   = port:PH18<2><0><default><default>
    lcdd19                   = port:PH19<2><0><default><default>
    lcdd20                   = port:PH20<2><0><default><default>
    lcdd21                   = port:PH21<2><0><default><default>
    lcdd22                   = port:PH22<2><0><default><default>
    lcdd23                   = port:PH23<2><0><default><default>
    lcdclk                   = port:PH24<2><0><default><default>
    lcdde                    = port:PH25<2><0><default><default>
    lcdhsync                 = port:PH26<2><0><default><default>
    lcdvsync                 = port:PH27<2><0><default><default>
    
[/code]
## tv out dac configuration
The TV-Out Digital Analog Converter (DAC) modules the framebuffer to a signal suitable for a TV 
### [tv_out_dac_para]
  * **dac_used** : 0 to disable; 1 to enable
  * **dac0_src** : Output source for the DAC:
  * **dac1_src** : Output source for the DAC:
  * **dac2_src** : Output source for the DAC:
  * **dac3_src** : Output source for the DAC:

    
    
     dac  | Output source   
---|---  
0  | Composite   
1  | Luma   
2  | Chroma   
3  |   
4  | Y   
5  | Pb   
6  | Pr   
7  | None   
Configuration example: 
[code] 
    [tv_out_dac_para]
    dac_used = 1
    dac0_src = 4
    dac1_src = 5
    dac2_src = 6
    dac3_src = 0
    
[/code]
## csi gpio configuration
  * **csi_used** : 0 to enable; 1 to disable
  * **csi_mode** : 0 to sample one csi to one buffer; 1 to sample two csi to one buffer
  * **csi_dev_qty** : Quantity of devices linked to the csi interface
  * **csi_twi_id** : TWI controller to use
  * **csi_twi_id_b** : TWI controller to use for second device
  * **csi_mname** : Module name to match the csi device; currently known to work:
  * **csi_mname_b** : Module name to match the second csi device; currently known to work:

    
    
    
  * ov7670
  * gc0308
  * gt2005
  * hi704
  * hi253

  * **csi_twi_addr** : TWI address for the used camera
  * **csi_twi_addr_b** : TWI address for the used camera for second device
  * **csi_if** : interface:
  * **csi_if_b** : interface for second device:

    
    
     if  | csi interface   
---|---  
0  | hv_8bit   
1  | hv_16bit   
2  | hv_24bit   
3  | bt656 1ch   
4  | bt656 2ch   
5  | bt656 4ch   
  * **csi_pck** : _p_ clock GPIO configuration
  * **csi_ck** : clock GPIO configuration
  * **csi_hsync** : H-sync GPIO configuration
  * **csi_vsync** : V-sync GPIO configuration
  * **csi_hflip** : Horizontal frame flip
  * **csi_hflip_b** : Horizontal frame flip for second device
  * **csi_vflip** : Vertical frame flip
  * **csi_vflip_b** : Vertical frame flip for second device
  * **csi_d0** : data bit 0 GPIO configuration
  * **csi_d1** : data bit 1 GPIO configuration
  * **csi_d2** : data bit 2 GPIO configuration
  * **csi_d3** : data bit 3 GPIO configuration
  * **csi_d4** : data bit 4 GPIO configuration
  * **csi_d5** : data bit 5 GPIO configuration
  * **csi_d6** : data bit 6 GPIO configuration
  * **csi_d7** : data bit 7 GPIO configuration
  * **csi_d8** : data bit 8 GPIO configuration
  * **csi_d9** : data bit 9 GPIO configuration
  * **csi_d10** : data bit 10 GPIO configuration
  * **csi_d11** : data bit 11 GPIO configuration
  * **csi_d12** : data bit 12 GPIO configuration
  * **csi_d13** : data bit 13 GPIO configuration
  * **csi_d14** : data bit 14 GPIO configuration
  * **csi_d15** : data bit 15 GPIO configuration
  * **csi_reset** : Camera reset; the default value, high or low ,depends on the module
  * **csi_power_en** : Power enable GPIO configuration
  * **csi_stby** : Camera standby GPIO configuration; the default value, high or low ,depends on the module
  * **csi_stby_b** : Camera standby GPIO configuration for second device; the default value, high or low ,depends on the module
  * **csi_stby_mode** : 0 to not shutdown power at standby; 1 shutdown power at standby
  * **csi_facing** : Tells the device if the camera is facing or otherwise. 0 for the back, 1 for the front camera.
  * **csi_facing_b** : Same as above.
  * **csi_vflip** : Vertical flip; 0: disabled, 1: enabled
  * **csi_hflip** : Horizontal flip; 0: disabled, 1: enabled
  * **csi_flash** : Camera Flash GPIO configuration
  * **csi_flash_b** : Camera Flash GPIO configuration for second device
  * **csi_flash_pol** : Flash polarity of flash light; 0 for active low; 1 for active high
  * **csi_flash_pol_b** : Flash polarity of flash light for second device; 0 for active low; 1 for active high
  * **csi_af_en** : Autofocus enable GPIO configuration
  * **csi_iovdd** : Camera module IO power, PMU power supply
  * **csi_iovdd_b** : Camera module IO power, PMU power supply for second device
  * **csi_avdd** : Camera analog power, PMU power supply
  * **csi_avdd_b** : Camera analog power, PMU power supply for second device
  * **csi_dvdd** : Camera digital power, PMU power supply
  * **csi_dvdd_b** : Camera digital power, PMU power supply for second device
  * **pmu_ldo3** : "axp20_pll" or leave empty empty when not using any PMU power supply
  * **pmu_ldo4** : "axp20_hdmi" or empty when not using any PMU power supply

### [csi0_para]
Configuration example: 
[code] 
    [csi0_para]
    csi_used = 1
    csi_mode = 0
    csi_dev_qty = 1
    csi_stby_mode = 1
    
    csi_mname = "gc0308"
    csi_twi_id = 1
    csi_twi_addr =0x42
    csi_if = 0
    csi_vflip = 0
    csi_hflip = 1
    csi_iovdd = ""
    csi_avdd = ""
    csi_dvdd  = ""
    csi_flash_pol = 1
    
    csi_mname_b = "gt2005"
    csi_twi_id_b = 1
    csi_twi_addr_b = 0x78
    csi_if_b = 0
    csi_vflip_b = 0
    csi_hflip_b = 0
    csi_iovdd_b = ""
    csi_avdd_b = ""
    csi_dvdd_b = ""
    csi_flash_pol_b = 1
    
    csi_pck = port:PE00<3><default><default><default>
    csi_ck = port:PE01<3><default><default><default>
    csi_hsync = port:PE02<3><default><default><default>
    csi_vsync= port:PE03<3><default><default><default>
    csi_d0 = port:PE04<3><default><default><default>
    csi_d1 = port:PE05<3><default><default><default>
    csi_d2 = port:PE06<3><default><default><default>
    csi_d3 = port:PE07<3><default><default><default>
    csi_d4 = port:PE08<3><default><default><default>
    csi_d5 = port:PE09<3><default><default><default>
    csi_d6 = port:PE10<3><default><default><default>
    csi_d7 = port:PE11<3><default><default><default>
    csi_d8 = port:PG04<5><default><default><default>
    csi_d9 = port:PG05<5><default><default><default>
    csi_d10 = port:PG06<5><default><default><default>
    csi_d11 = port:PG07<5><default><default><default>
    csi_d12 = port:PG08<5><default><default><default>
    csi_d13 = port:PG09<5><default><default><default>
    csi_d14 = port:PG10<5><default><default><default>
    csi_d15 = port:PG11<5><default><default><default>
    csi_reset = port:PH13<1><default><default><0>
    csi_power_en = port:PH16<1><default><default><0>
    csi_stby = port:PH18<1><default><default><0>
    csi_flash = 
    csi_af_en = 
    csi_reset_b = port:PH13<1><default><default><0>
    csi_power_en_b = port:PH16<1><default><default><0>
    csi_stby_b = port:PH19<1><default><default><0>
    csi_flash_b = 
    csi_af_en_b = 
    
[/code]
### [csi1_para]
Configuration example: 
[code] 
    [csi1_para]
    csi_used = 1
    csi_mode = 0
    csi_dev_qty = 1
    csi_stby_mode = 1
    
    csi_mname = "gc0308"
    csi_twi_id = 1
    csi_twi_addr =0x42
    csi_if = 0
    csi_vflip = 0
    csi_hflip = 1
    csi_iovdd = ""
    csi_avdd = ""
    csi_dvdd  = ""
    csi_flash_pol = 1
    
    csi_mname_b = "gt2005"
    csi_twi_id_b = 1
    csi_twi_addr_b = 0x78
    csi_if_b = 0
    csi_vflip_b = 0
    csi_hflip_b = 0
    csi_iovdd_b = ""
    csi_avdd_b = ""
    csi_dvdd_b = ""
    csi_flash_pol_b = 1
    
    csi_pck = port:PG00<3><default><default><default>
    csi_ck = port:PG01<3><default><default><default>
    csi_d0 = port:PH00<7><default><default><default>
    csi_d1 = port:PH01<7><default><default><default>
    csi_d2 = port:PH02<7><default><default><default>
    csi_d3 = port:PH03<7><default><default><default>
    csi_d4 = port:PH04<7><default><default><default>
    csi_d5 = port:PH05<7><default><default><default>
    csi_d6 = port:PH06<7><default><default><default>
    csi_d7 = port:PH07<7><default><default><default>
    csi_d8 = port:PH08<7><default><default><default>
    csi_d9 = port:PH09<7><default><default><default>
    csi_d10 = port:PH10<7><default><default><default>
    csi_d11 = port:PH11<7><default><default><default>
    csi_d12 = port:PH12<7><default><default><default>
    csi_d13 = port:PH13<7><default><default><default>
    csi_d14 = port:PH14<7><default><default><default>
    csi_d15 = port:PH15<7><default><default><default>
    csi_d16 = port:PH16<7><default><default><default>
    csi_d17 = port:PH17<7><default><default><default>
    csi_d18 = port:PH18<7><default><default><default>
    csi_d19 = port:PH19<7><default><default><default>
    csi_d20 = port:PH20<7><default><default><default>
    csi_d21 = port:PH21<7><default><default><default>
    csi_d22 = port:PH22<7><default><default><default>
    csi_d23 = port:PH23<7><default><default><default>
    csi_hsync = port:PH26<7><default><default><default>
    csi_vsync= port:PH27<7><default><default><default>
    csi_reset = port:PG13<1><default><default><0>
    csi_power_en = port:PG16<1><default><default><0>
    csi_stby = port:PG18<1><default><default><0>
    csi_flash = 
    csi_af_en = 
    csi_reset_b = port:PG13<1><default><default><0>
    csi_power_en_b = port:PG16<1><default><default><0>
    csi_stby_b = port:PG19<1><default><default><0>
    csi_flash_b = 
    csi_af_en_b =
    
[/code]
## tv configuration
### [tvout_para]
  * **tvout_used** : 0 to disable; 1 to enable
  * **tvout_channel_num** : Channel number
  * **tv_en** : TV encoder GPIO configuration

Configuration example: 
[code] 
    tvout_used = 1
    tvout_channel_num = 1
    tv_en = port:PI12<1><default><default><0>
    
[/code]
### [tvin_para]
  * **tvin_used** : 0 to disable; 1 to enable
  * **tvin_channel_num** : channel number

Configuration example: 
[code] 
    tvin_used = 1
    tvin_channel_num = 4
    
[/code]
## sata configuration
### [sata_para]
  * **sata_used** : 0 to disable; 1 to enable
  * **sata_power_en** : Sata power enable GPIO configuration

Configuration example: 
[code] 
    sata_used = 1
    sata_power_en = port:PB08<1><default><default><0>
    
[/code]
## sdmmc configuration
There are several things to notice when configuring the sdmmc controller. 
  * **sdc_used** : 0 to disable; 1 to enable;（0=不使用，1=使用）
  * **sdc_detmode** : detection mode （卡检测模式）:

    
    
     mode  | detection mode  | note   
---|---|---  
0  |  |   
1  | GPIO detection  | Also configure **sdc_det** to map to a GPIO （GPIO检测模式，需在sdc_det配置一个GPIO口）   
2  | sdc_d3 detection  | **sdc_d3** must be configured as HiZ GPIO and have an external 1 MΩ pull-down resistor （SD卡D3数据口检测模式，需配置GPIO口为高阻，并使用1M欧下拉）   
3  | polling (card cannot be swapped)  | 不检测，卡常在   
4  | manually (via the proc file system node)  |   
  * **bus_width** : 1 for 1bit; 4 for 4bit (may also be called sdc_bwid?!? verify please)
  * **sdc_d0** : data line 0 GPIO configuration
  * **sdc_d1** : data line 1 GPIO configuration
  * **sdc_d2** : data line 2 GPIO configuration
  * **sdc_d3** : data line 3 GPIO configuration
  * **sdc_clk** : CLK GPIO configuration
  * **sdc_cmd** : CMD GPIO configuration
  * **sdc_det** : DET GPIO configuration
  * **sdc_use_wp** : 0 is normal operation; 1 is write protect
  * **sdc_wp** : Write Protect the GPIO configuration

### [mmc0_para]
Configuration example: 
[code] 
    [mmc0_para]
    sdc_used = 1
    sdc_detmode = 1
    bus_width = 4
    sdc_d1 = port:PF00<2><1><default><default>
    sdc_d0 = port:PF01<2><1><default><default>
    sdc_clk = port:PF02<2><1><default><default>
    sdc_cmd = port:PF03<2><1><default><default>
    sdc_d3 = port:PF04<2><1><default><default>
    sdc_d2 = port:PF05<2><1><default><default>
    sdc_det = port:PH01<0><1><default><default>
    sdc_use_wp = 0
    sdc_wp =
    
[/code]
### [mmc1_para]
Configuration example: 
[code] 
    [mmc1_para]              
    sdc_used = 1
    sdc_detmode = 1
    bus_width = 4
    sdc_cmd = port:PH22<5><1><2><default>
    sdc_clk = port:PH23<5><1><2><default>
    sdc_d0 = port:PH24<5><1><2><default>
    sdc_d1 = port:PH25<5><1><2><default>
    sdc_d2 = port:PH26<5><1><2><default>
    sdc_d3 = port:PH27<5><1><2><default>
    sdc_det = port:PH2<0><1><default><default>
    sdc_use_wp = 0
    sdc_wp =
    
[/code]
### [mmc2_para]
Configuration example: 
[code] 
    [mmc2_para]              
    sdc_used = 0
    
[/code]
### [mmc3_para]
Configuration example: 
[code] 
                             
    [mmc3_para]              
    sdc_used = 1
    sdc_detmode = 4
    bus_width = 4
    sdc_cmd = port:PI04<2><1><2><default>
    sdc_clk = port:PI05<2><1><2><default>
    sdc_d0 = port:PI06<2><1><2><default>
    sdc_d1 = port:PI07<2><1><2><default>
    sdc_d2 = port:PI08<2><1><2><default>
    sdc_d3 = port:PI09<2><1><2><default>
    sdc_det = 
    sdc_use_wp = 0
    sdc_wp =
    
[/code]
## memory stick configuration
### [ms_para]
  * **ms_used** : 0 to disable; 1 to enable
  * **ms_bs** : Bus State signal GPIO configuration
  * **ms_clk** : Clock GPIO configuration
  * **ms_d0** : Data line 0 GPIO Configuration
  * **ms_d1** : Data line 1 GPIO Configuration
  * **ms_d2** : Data line 2 GPIO Configuration
  * **ms_d3** : Data line 3 GPIO Configuration
  * **ms_det** : Stick detection GPIO Configuration

Configuration example: 
[code] 
    [ms_para]
    ms_used = 1
    ms_bs = port:PH06<5><default><default><default>
    ms_clk = port:PH07<5><default><default><default>
    ms_d0 = port:PH08<5><default><default><default>
    ms_d1 = port:PH09<5><default><default><default>
    ms_d2 = port:PH10<5><default><default><default>
    ms_d3 = port:PH11<5><default><default><default>
    ms_det = port:PH2<0><1><default><default>
    
[/code]
## sim card configuration
### [smc_para]
  * **smc_used** : 0 to disable; 1 to enable
  * **smc_rst** : Reset GPIO configuration
  * **smc_vppen** : VPP enable GPIO configuration
  * **smc_vppp** : Programming VPP GPIO configuration
  * **smc_det** : SIM Card detect GPIO configuration
  * **smc_vccen** : VCC enable GPIO configuration
  * **smc_sck** : Serial clock GPIO configuration
  * **smc_sda** : Serial data GPIO configurion

Configuration example: 
[code] 
    [smc_para]
    smc_used = 1
    smc_rst = port:PH13<5><default><default><default>
    smc_vppen = port:PH14<5><default><default><default>
    smc_vppp = port:PH15<5><default><default><default>
    smc_det = port:PH16<5><default><default><default>
    smc_vccen = port:PH17<5><default><default><default>
    smc_sck = port:PH18<5><default><default><default>
    smc_sda = port:PH19<5><default><default><default>
    
[/code]
## ps2 configuration
### [ps2_0_para]
  * **ps2_used** : 0 to disable; 1 to enable
  * **ps2_scl** : Serial clock GPIO configuration
  * **ps2_sda** : Serial data GPIO configuration

Configuration example: 
[code] 
    [ps2_0_para]
    ps2_used = 1
    ps2_scl = port:PI20<2><1><default><default>
    ps2_sda = port:PI21<2><1><default><default>
    
[/code]
### [ps2_1_para]
  * **ps2_used** : 0 to disable; 1 to enable
  * **ps2_scl** : Serial clock GPIO configuration
  * **ps2_sda** : Serial data GPIO configuration

Configuration example: 
[code] 
    [ps2_1_para]
    ps2_used = 1
    ps2_scl = port:PI20<2><1><default><default>
    ps2_sda = port:PI21<2><1><default><default>
    
[/code]
## can bus configuration
### [can_para]
  * **can_used** : 0 to disable; 1 to enable it
  * **can_tx** : transmit GPIO Configuration
  * **can_rx** : receive GPIO configuration

Configuration example: 
[code] 
    [Can_para]
    can_used = 1
    can_tx = port:PA16<3><default><default><default>
    can_rx = port:PA17<3><default><default><default>
    
[/code]
## matrix keyboard
## 23.1 [keypad_para]
  * **kp_used** : 0 to disable; 1 to enable
  * **kp_in_size** : column width
  * **kp_out_size** : row width
  * **kp_in0** : column 0 GPIO Configuration
  * **kp_in1** : column 1 GPIO Configuration
  * **kp_in2** : column 2 GPIO Configuration
  * **kp_in3** : column 3 GPIO Configuration
  * **kp_in4** : column 4 GPIO configuration
  * **kp_in5** : column 5 GPIO configuration
  * **kp_in6** : column 6 GPIO Configuration
  * **kp_in7** : column 7 GPIO configuration
  * **kp_out0** : row 0 GPIO Configuration
  * **kp_out1** : row 1 GPIO Configuration
  * **kp_out2** : row 2 GPIO Configuration
  * **kp_out3** : row 3 GPIO Configuration
  * **kp_out4** : row 4 GPIO configuration
  * **kp_out5** : row 5 GPIO configuration
  * **kp_out6** : row 6 GPIO Configuration
  * **kp_out7** : row 7 GPIO configuration

Configuration example: 
[code] 
    [Keypad_para]
    kp_used = 1
    kp_in_size = 8
    kp_out_size = 8
    kp_in0 = port:PH08<4><1><default><default>
    kp_in1 = port:PH09<4><1><default><default>
    kp_in2 = port:PH10<4><1><default><default>
    kp_in3 = port:PH11<4><1><default><default>
    kp_in4 = port:PH14<4><1><default><default>
    kp_in5 = port:PH15<4><1><default><default>
    kp_in6 = port:PH16<4><1><default><default>
    kp_in7 = port:PH17<4><1><default><default>
    kp_out0 = port:PH18<4><1><default><default>
    kp_out1 = port:PH19<4><1><default><default>
    kp_out2 = port:PH22<4><1><default><default>
    kp_out3 = port:PH23<4><1><default><default>
    kp_out4 = port:PH24<4><1><default><default>
    kp_out5 = port:PH25<4><1><default><default>
    kp_out6 = port:PH26<4><1><default><default>
    kp_out7 = port:PH27<4><1><default><default>
    
[/code]
## USB control flags
  * **usb_used** : 0 to disable; 1 to enable
  * **usb_port_type** : USB port type:

    
    
     type  | usb port type   
---|---  
0  | device only   
1  | host only   
2  | OTG   
  * **usb_detect_type** : 0 = no checking; 1 = VBus / id check
  * **usb_controller_type** : USB controller type:

    
    
     type  | usb controller type   
---|---  
0  | Unknown   
1  | EHCI   
2  | OHCI   
  * **usb_id_gpio** :USB ID pin GPIO configuration
  * **usb_det_vbus_gpio** : USB detect VBus pin GPIO configuration (VBus is USB speak for the +5V line)
  * **usb_drv_vbus_gpio** : USB drive VBus pin GPIO configuration
  * **usb_restrict_gpio** :
  * **usb_host_init_state** : In host only mode, host port initialization state; 0 do not initialize; 1 initializatie USB
  * **usb_restric_flag** :

### [usbc0]
Configuration example: 
[code] 
    [usbc0]
    usb_used = 1
    usb_port_type = 2
    usb_detect_type = 1
    usb_id_gpio = port:PH04<0><1><default><default>
    usb_det_vbus_gpio = port:PH05<0><0><default><default>
    usb_drv_vbus_gpio = port:PB09<1><0><default><0>
    usb_host_init_state = 0
    
[/code]
### [usbc1]
Configuration example: 
[code] 
    [usbc1]
    usb_used = 1
    usb_port_type = 1
    usb_detect_type = 0
    usb_id_gpio =
    usb_det_vbus_gpio =
    usb_drv_vbus_gpio = port:PH06<1><0><default><0>
    usb_host_init_state = 1
    
[/code]
### [usbc2]
Configuration example: 
[code] 
    [usbc2]
    usb_used = 1
    usb_port_type = 1
    usb_detect_type = 0
    usb_id_gpio =
    usb_det_vbus_gpio =
    usb_drv_vbus_gpio = port:PH03<1><0><default><0>
    usb_host_init_state = 1
    
[/code]
## USB Device
### [usb_feature]
  * **vendor_id** : vendor ID
  * **mass_storage_id** : mass storage ID
  * **adb_id** : android debug bridge ID
  * **manufacturer_name** : vendor name
  * **product_name** : = product name
  * **serial_number** : = serial number

Configuration example: 
[code] 
    [usb_feature]
    vendor_id = 0x18d1
    mass_storage_id = 0x0001
    adb_id = 0x0002
    manufacturer_name = "USB Developer"
    product_name = "Android"
    serial_number = "20080411"
    
[/code]
### [msc_feature]
  * **vendor_name** : vendor name
  * **product_name** : product name
  * **release** : release version
  * **luns** : number of logical units

Configuration example: 
[code] 
    [msc_feature]
    vendor_name = "USB 2.0"
    product_name = "USB Flash Driver"
    release = 100
    luns = 2
    
[/code]
## G Sensor configuration
### [gsensor_para]
  * **gsensor_used** : 0 to disable; 1 to enable
  * **gsensor_name** : linux kernel module name to match configuration
  * **gsensor_twi_id** : TWI bus ID
  * **gsensor_twi_addr** : TWI address
  * **gsensor_int1** : interrupt 1 GPIO configuration
  * **gsensor_int2** : interrupt 2 GPIO configuration
  * **gsensor_revert_x_flag** : (untested)
  * **gsensor_revert_y_flag** : (untested)
  * **gsensor_revert_z_flag** : (untested)
  * **gsensor_exchange_x_y_flag** : (untested)

Configuration example 1: 
[code] 
    [Gsensor_para]
    gsensor_used = 1
    gsenser_name = "bma250"
    gsensor_twi_id = 1
    gsensor_twi_addr = 0x18
    gsensor_int1 = port:PH00<6><1><default><default>
    gsensor_int2 = port:PI10<6><1><default><default>
    
[/code]
Configuration example 2: 
[code] 
    [Gsensor_para]
    gsensor_used = 1
    gsenser_name = "bma222"
    gsensor_twi_id = 1
    gsensor_twi_addr = 0x08
    gsensor_int1 = port:PH00<6><1><default><default>
    gsensor_int2 = port:PI10<6><1><default><default>
    
[/code]
Configuration example 3: 
[code] 
    [Gsensor_para]
    gsensor_used = 1
    gsenser_name = "mma7660"
    gsensor_twi_id = 1
    gsensor_twi_addr = 0x4c
    gsensor_int1 = port:PH00<6><1><default><default>
    gsensor_int2 = port:PI10<6><1><default><default>
    
[/code]
## gps gpio configuration
### [gps_para]
  * **gps_used** : 0 to disable; 1 to enable
  * **gps_spi_id** : SPI controller; 0 - 2 for SPI0, SPI1 or SPI2; 15 if no SPI is used
  * **gps_spi_cs_num** : chip select SPI controller; 0 = SPI0, 1 = SPI1
  * **gps_lradc** : 0 or 1 for Low Rate ADC Format; 2 for no Low Rate ADC Format
  * **gps_clk** : Clock GPIO configuration
  * **gps_sign** : GPS sign GPIO configuration
  * **gps_mag** : GPS Magnitude GPIO configuration
  * **gps_vcc_en** : GPS VCC enable GPIO configuration
  * **gps_osc_en** : GPS Oscillator enable GPIO configuration
  * **gps_rx_en** : GPS receive enable GPIO configuration

Configuration example: 
[code] 
    [gps_para]
    gps_used = 0
    gps_spi_id = 2
    gps_spi_cs_num = 0
    gps_lradc = 1
    gps_clk = port:PI00<2><default><default><default>
    gps_sign = port:PI01<2><default><default><default>
    gps_mag = port:PI02<2><default><default><default>
    gps_vcc_en = port:PC22<1><default><default><0>
    gps_osc_en = port:PI14<1><default><default><0>
    gps_rx_en = port:PI15<1><default><default><0>
    
[/code]
## sdio wifi configuration
### [sdio_wifi_para]
  * **sdio_wifi_used** : 0 to disable; 1 to enable
  * **sdio_wifi_sdc_id** : SD controller ID to use
  * **sdio_wifi_mod_sel** : SDI module selection (see [mmc_pm.c][19489] ):

    
    
     mode  | wifi selection mode  | note   
---|---|---  
0  | none  |   
1  | swl-n20  | WiFi   
2  | usi bm-01  | WiFi - Bluetooth - FM radio   
3  | ar6302qfn  |   
4  | apm6xxx  |   
5  | swb b23  | WiFi - Bluetooth - FM radio   
6  | hw-mw269x  | Huawei wifi driver   
7  | bcm40181   
8  | bcm40183  | BCM40183(BCM4330)   
9  | rtl8723as  | RTL8723AS(RF-SM02B)   
10  | rtl8189es  | RTL8189ES(SM89E00)   
  * **sdio_wifi_shdn** : SHDN GPIO configuration
  * **sdio_wifi_host_wakeup** : WiFi wakeup GPIO Configuration
  * **sdio_wifi_vdd_en** : VDD enable GPIO configuration
  * **sdio_wifi_vcc_en** : VCC enable GPIO configuration

Configuration example: 
[code] 
    [Sdio_wifi_para]
    sdio_wifi_used = 1
    sdio_wifi_sdc_id = 3
    sdio_wifi_mod_sel = 1
    
    sdio_wifi_shdn = port:PH09<1><default><default><0>
    sdio_wifi_host_wakeup = port:PH10<1><default><default><1>
    sdio_wifi_vdd_en = port:PH11<1><default><default><0>
    sdio_wifi_vcc_en = port:PH12<1><default><default><0>
    
[/code]
Optionally the following parameters can be used when other/multiple transceivers are installed. 
[code] 
    ; 1 - samsung swl-n20 sdio wifi gpio config
    swl_n20_shdn            = port:PH09<1><default><default><0>
    swl_n20_host_wakeup     = port:PH10<1><default><default><1>
    swl_n20_vdd_en          = port:PH11<1><default><default><0>
    swl_n20_vcc_en          = port:PH12<1><default><default><0>
    
    ; 2 - usi bm01a sdio wifi gpio config
    usi_bm01a_wl_pwr        = port:PH12<1><default><default><0>
    usi_bm01a_wlbt_regon    = port:PI11<1><default><default><0>
    usi_bm01a_wl_rst        = port:PI10<1><default><default><0>
    usi_bm01a_wl_wake       = port:PI12<1><default><default><0>
    usi_bm01a_bt_rst        = port:PB05<1><default><default><0>
    usi_bm01a_bt_wake       = port:PI20<1><default><default><0>
    usi_bm01a_bt_hostwake   = port:PI21<0><default><default><0>
    
    ; 3 - ar6302qfn sdio wifi gpio config
    ar6302_qfn_pwr          = port:PH12<1><default><default><0>
    ar6302_qfn_shdn_n       = port:PH09<1><default><default><0>
    
    ; 4 - apm sdio wifi gpio config
    apm_6981_vcc_en         = port:PA09<1><default><default><0>
    apm_6981_vdd_en         = port:PA10<1><default><default><0>
    apm_6981_wakeup         = port:PA11<1><default><default><0>
    apm_6981_rst_n          = port:PA12<1><default><default><0>
    apm_6981_pwd_n          = port:PA13<1><default><default><0>
    
    ; 6 - huawei mw269x(v1/v2) sdio wifi gpio config
    hw_mw269x_wl_pwr        = port:PH12<1><default><default><0>
    hw_mw269x_wl_enb        = port:PH11<1><default><default><0>
    hw_mw269x_wl_hostwake   = port:PH10<0><default><default><0>
    hw_mw269x_wl_wake       = port:PH09<1><default><default><0>
    hw_mw269x_bt_enb        = port:PB05<1><default><default><0>
    hw_mw269x_bt_wake       = port:PI20<1><default><default><0>
    hw_mw269x_bt_hostwake   = port:PI21<0><default><default><0>
    
[/code]
## us wifi configuration
### [usb_wifi_para]
  * **usb_wifi_used** : 0 to disable; 1 to enable
  * **usb_wifi_usbc_num** : USB controller to which USB wifi module is connected
  * **usb_host_init_state** : used together, such as xx = 2. Then usbc2 the usb_host_init_state 0

Configuration example: 
[code] 
    [usb_wifi_para]
    usb_wifi_used = 0
    usb_wifi_usbc_num = 2
    
[/code]
## 3G configuration
### [3g_para]
  * **3g_used** : 0 to disable; 1 to enable
  * **3g_usbc_num** : USB controller to which the 3G module is connected
  * **3g_uart_num** : UART controller to which the 3G module is connected
  * **3g_pwr** : power enable GPIO configuration
  * **3g_wakeup** : wakeup GPIO configuration
  * **3g_int** : interrupt GPIO configuration

Configuration example: 
[code] 
    3g_used = 1
    3g_usbc_num = 2
    3g_uart_num = 0
    3g_pwr = port:PH09<1><default><default><1>
    3g_wakeup = port:PH10<1><default><default><1>
    3g_int = port:PH11<1><default><default><1>
    
[/code]
## gyroscope
### [gy_para]
  * **gy_used** : 0 to disable; 1 to enable
  * **gy_twi_id** : TWI controller to use
  * **gy_twi_addr** : TWI address to use
  * **gy_int1** : interrupt 1 GPIO configuration
  * **gy_int2** : interrupt 2 GPIO configuration

Configuration example: 
[code] 
    [gy_para]
    gy_used = 1
    gy_twi_id = 1
    gy_twi_addr = 0x0a
    gy_int1 = port:PH18<6><1><default><default>
    gy_int2 = port:PH19<6><1><default><default>
    
[/code]
## light sensor
### [ls_para]
  * **ls_used** : 0 to disable; 1 to enable
  * **ls_twi_id** : TWI controller to use
  * **ls_twi_addr** : TWI address
  * **ls_int** : interrupt GPIO configuration

Configuration example: 
[code] 
    [ls_para]
    ls_used = 1
    ls_twi_id = 1
    ls_twi_addr = 0x0c
    ls_int = port:PH20<6><1><default><default>
    
[/code]
## compass
### [compass_para]
  * **compass_used** : 0 to disable; 1 to enable
  * **compass_twi_id** : TWI controller to use
  * **compass_twi_addr** : TWI address to use
  * **compass_int** : interrupt GPIO configuration

Configuration example: 
[code] 
    [compass_para]
    compass_used = 0
    compass_twi_id = 1
    compass_twi_addr = 0x0d
    compass_int = port:PI13<6><1><default><default>
    
[/code]
## blue tooth
### [bt_para]
  * **bt_used** : 0 to disable; 1 to enable
  * **bt_uart_id** : UART controller to use
  * **bt_wakeup** : wakeup GPIO configuration
  * **bt_gpio** : optional bluetooth pin GPIO configuration
  * **bt_rst** : = reset GPIO configuration

Configuration example: 
[code] 
    [Bt_para]
    bt_used = 1
    bt_uart_id = 2
    bt_wakeup = port:PI20<1><default><default><default>
    bt_gpio = port:PI21<1><default><default><default>
    bt_rst = port:PB05<1><default><default><default>
    
[/code]
## i2s configuration
### [i2s_para]
  * **i2s_used** : 0 to disable; 1 to enable
  * **i2s_channel** : channel control; 1 for one, 2 for two channels
  * **i2s_mclk** : master clock signal GPIO configuration
  * **i2s_bclk** : bit clock signal GPIO configuration
  * **i2s_lrclk** : word clock (left/right) signal GPIO configuration
  * **i2s_dout0** : digital out 0 GPIO configuration
  * **i2s_dout1** : (optional) digital out 1 GPIO configuration
  * **i2s_dout2** : (optional) digital out 2 GPIO configuration
  * **i2s_dout3** : (optional) digital out 3 GPIO configuration
  * **i2s_din** : multiplexed in signal GPIO configuration

Configuration example: 
[code] 
    [i2s_para]
    i2s_used = 1
    i2s_channel = 2
    i2s_mclk = port:PB05<2><1><default><default>
    i2s_bclk = port:PB06<2><1><default><default>
    i2s_lrclk = port:PB07<2><1><default><default>
    i2s_dout0 = port:PB08<2><1><default><default>
    i2s_dout1 =
    i2s_dout2 =
    i2s_dout3 =
    i2s_din = port:PB12<2><1><default><default>
    
[/code]
## spdif configuration
### [spdif_para]
  * **spdif_used** : 0 to disable; 1 to enable
  * **spdif_mclk** : optional master clock GPIO configuration
  * **spdif_dout** : digital out GPIO configuration
  * **spdif_din** : digital in GPIO configuration

Configuration example: 
[code] 
    [spdif_para]
    spdif_used = 1
    spdif_mclk =
    spdif_dout = port:PB13<4><1><default><default>
    spdif_din =
    
[/code]
## audio configuration
### [audio_para]
  * **audio_used** : 0 to disable; 1 to enable
  * **audio_pa_ctrl** : External Amp shutdown GPIO configuration
  * **audio_lr_change** : 0 for normal operation; 1 to swap left and right channels
  * **playback_used** : 0 to disable; 1 to enable _**This is a linux-sunxi specific extention**_
  * **capture_used** : 0 to dissable; 1 to enable _**This is a linux-sunxi specific extention**_

Some extra settings were introduced with the A31: 
  * **audio_mute_ctrl** : External Amp mute GPIO configuration
  * **cap_vol** : ???
  * **headphone_vol** : Internal headphone amp volume (0 ~ 0x3f: 0 .. -62 dB)
  * **headphone_direct_used** : 1 for headphone DC direct drive (no coupling capacitors)
  * **headset_mic_vol** : Headset microphone boost gain (0 ~ 0x7: 0 dB, 24 .. 42 dB)
  * **main_mic_vol** : Main microphone boost gain (0 ~ 0x7: 0 dB, 24 .. 42 dB)
  * **pa_double_used** : 0 for mono differential output; 1 for stereo output
  * **pa_double_vol** : Line out volume for _**Stereo**_ output mode
  * **pa_single_vol** : Line out volume for _**Mono differential**_ output mode

Configuration example: 
[code] 
    [audio_para]
    audio_used = 1
    audio_pa_ctrl = port:PH15<1><default><default><0>
    audio_lr_change = 0
    playback_used = 1
    capture_used = 1
    
[/code]
## infrared remote configuration
### [ir_para]
  * **ir_used** : 0 to disable; 1 to enable
  * **ir0_rx** : receiver GPIO configuration
  * **ir0_tx** : transmitter GPIO configuration
  * **ir1_rx** : receiver GPIO configuration
  * **ir1_tx** : transmitter GPIO configuration

Configuration example: 
[code] 
    ir_used = 1
    ir0_tx = port:PB03<2>default<default><default>
    ir0_rx = port:PB04<2>default<default><default>
    
    ir1_tx = port:PB22<2>default<default><default>
    ir1_rx = port:PB23<2>default<default><default>
    
[/code]
## pmu configuration
### [pmu_para]
  * **pmu_used** : 0 to disable; 1 to enable
  * **pmu_used2** : 0 to disable; 1 to enable secondary PMU
  * **pmu_twi_id** : TWI controller to use
  * **pmu_twi_addr** : TWI address to use
  * **pmu_irq_id** : interrupt to use; 0 = NMI; 1 - 15 = interrupt 1 to 15
  * **pmu_battery_rdc** : battery internal resistance in mΩ
  * **pmu_battery_cap** : battery capacity in mAh
  * **pmu_init_chgcur** : initial charging current in mA; 300, 400 ... 1800
  * **pmu_init_chgcur2** : initial charging current in mA for secondary PMU; 300, 400 ... 1800
  * **pmu_earlysuspend_chgcur2** early suspend charging current in mA; 300, 400 ... 1800
  * **pmu_suspend_chgcur** : suspended charging current in mA; 300, 400 ... 1800
  * **pmu_suspend_chgcur2** : suspended charging current in mA for secondary PMU; 300, 400 ... 1800
  * **pmu_resume_chgcur** : normal charging current in mA; 300, 400 ... 1800
  * **pmu_resume_chgcur2** : normal charging current in mA for secondary PMU; 300, 400 ... 1800
  * **pmu_shutdown_chgcur** : powered down charge current in mA; 300, 400 ... 1800
  * **pmu_shutdown_chgcur2** : powered down charge current in mA for secondary PMU; 300, 400 ... 1800
  * **pmu_init_chgvol** : initial charging target voltage in mV; 4100/4150/4200/4360
  * **pmu_init_chgend_rate** : initial charging current ratio in %; 10, 15
  * **pmu_init_chg_enabled** : 0 to disable; 1 to enable
  * **pmu_init_adc_freq** : initial ADC sampling rate in Hz; 25/50/100/200
  * **pmu_init_adc_freqc** : initial ADC coulomb meter sampling rate in Hz; 25/50/100/200
  * **pmu_init_chg_pretime** : initial precharge timeout in minutes; 40/50/60/70
  * **pmu_init_chg_csttime** : initial constant charging current timeout in minutes; 360/480/600/720
  * **pmu_bat_para1** : = battery charge LUT in %
  * **pmu_bat_para2** : = battery charge LUT in %
  * **pmu_bat_para3** : = battery charge LUT in %
  * **pmu_bat_para4** : = battery charge LUT in %
  * **pmu_bat_para5** : = battery charge LUT in %
  * **pmu_bat_para6** : = battery charge LUT in %
  * **pmu_bat_para7** : = battery charge LUT in %
  * **pmu_bat_para8** : = battery charge LUT in %
  * **pmu_bat_para9** : = battery charge LUT in %
  * **pmu_bat_para10** : = battery charge LUT in %
  * **pmu_bat_para11** : = battery charge LUT in %
  * **pmu_bat_para12** : = battery charge LUT in %
  * **pmu_bat_para13** : = battery charge LUT in %
  * **pmu_bat_para14** : = battery charge LUT in %
  * **pmu_bat_para15** : = battery charge LUT in %
  * **pmu_bat_para16** : = battery charge LUT in %; should always be 100
  * **pmu_usbvol_limit** : 0 no USB voltage limiter; 1 = limit USB voltage
  * **pmu_usbvol** : USB voltage limit in mV; 4000, 4100 ... 4700
  * **pmu_usbcur_limit** : 0 no USB current limiter; 1 = limit USB current
  * **pmu_usbcur** : USB current limit in mA; 100/500/900
  * **pmu_pwroff_vol** : boot hardware protection voltage in mV; 2600, 2700 ... 3300
  * **pmu_pwron_vol** : running hardware protection voltage in mV; 2600, 2700 ... 3300
  * **pmu_pekoff_time** : Power Enable Key, short power button off delay in ms; 4000, 6000, 8000, 10000
  * **pmu_pekoff_en** : 0 to disable; 1 to enable power button power off
  * **pmu_peklong_time** : long power off button delay in ms; 1000, 1500, 2000, 2500
  * **pmu_pekon_time** : power on button delay in ms; 128, 1000, 2000, 3000
  * **pmu_pwrok_time** : power 'ok' delay in ms; 8, 64
  * **pmu_pwrnoe_time** : n_oe from low to high shutdown delay time in ms; 128, 1000, 2000, 3000
  * **pmu_intotp_en** : 0 to disable; 1 to enable over temperature protection
  * **pmu_suspendpwroff_vol** : shutdown voltage when suspended and battery is low
  * **pmu_batdeten** : Battery detection enabled
  * **pmu_adpdet** : adapter detect GPIO configuration
  * **pmu_backupen** : 1 to enable RTC/backup battery charging

Configuration example: 
[code] 
    [pmu_para]
    pmu_used = 1
    pmu_twi_addr = 0x34
    pmu_twi_id = 0
    pmu_irq_id = 0
    pmu_battery_rdc = 200
    pmu_battery_cap = 2600
    pmu_init_chgcur = 300
    pmu_suspend_chgcur = 1000
    pmu_resume_chgcur = 300
    pmu_shutdown_chgcur = 1000
    pmu_init_chgvol = 4200
    pmu_init_chgend_rate = 15
    pmu_init_chg_enabled = 1
    pmu_init_adc_freq = 100
    pmu_init_adc_freqc = 100
    pmu_init_chg_pretime = 50
    pmu_init_chg_csttime = 720
    pmu_bat_para1 = 0
    pmu_bat_para2 = 0
    pmu_bat_para3 = 1
    pmu_bat_para4 = 5
    pmu_bat_para5 = 7
    pmu_bat_para6 = 13
    pmu_bat_para7 = 16
    pmu_bat_para8 = 26
    pmu_bat_para9 = 36
    pmu_bat_para10 = 46
    pmu_bat_para11 = 53
    pmu_bat_para12 = 61
    pmu_bat_para13 = 73
    pmu_bat_para14 = 84
    pmu_bat_para15 = 92
    pmu_bat_para16 = 100
    pmu_usbvol_limit = 1
    pmu_usbvol = 4400
    pmu_usbcur_limit = 1
    pmu_usbcur = 900
    pmu_pwroff_vol = 3300
    pmu_pwron_vol = 2900
    pmu_pekoff_time = 6000
    pmu_pekoff_en = 1
    pmu_peklong_time = 1500
    pmu_pekon_time = 1000
    pmu_pwrok_time = 64
    pmu_pwrnoe_time = 2000
    pmu_intotp_en = 1
    pmu_adpdet = port:PH02<0><default><default><default>
    pmu_batdeten = 1
    pmu_suspendpwroff_vol = 3500
    
    pmu_used2 = 0
    pmu_init_chgcur2 = 400
    pmu_suspend_chgcur2 = 1200
    pmu_resume_chgcur2 = 400
    pmu_shutdown_chgcur2 = 1200
    
[/code]
## recovery key configuration
### [recovery_key]
  * **key_min** : minimal length for the key to be depressed in seconds
  * **key_max** : maximal length for the key to be depressed in seconds

Example configuration: 
[code] 
    key_min	= 4
    key_max	= 32
    
[/code]
## dvfs voltage-frequency table configuration
Define at which frequency what voltage should be set. Recommended defaults: 
voltage  | frequency range   
---|---  
1.50 v  | 1008 MHz - 1056 MHz   
1.40 v  | 912 MHz - 1008 MHz   
1.35 v  | 864 MHz - 912 MHz   
1.30 v  | 624 MHz - 864 MHz   
1.25 v  | 60 MHz - 624 MHz   
### [dvfs_table]
  * **max_freq** : cpu maximum frequency in Hz; can not be more than 1008 MHz
  * **min_freq** : cpu minimum frequency in Hz; can not be less than 60 MHz
  * **lv_count** : number of lv_freq/lv_volt pairs; must be < 16
  * **lv1_freq** : state 1 frequency
  * **lv1_volt** : state 1 voltage

[code] 
    [dvfs_table]
    max_freq = 1008000000
    min_freq = 60000000
    lv_count = 5
    
    lv1_freq = 1056000000
    lv1_volt = 1500
    
    lv2_freq = 1008000000
    lv2_volt = 1400
    
    lv3_freq = 912000000
    lv3_volt = 1350
    
    lv4_freq = 864000000
    lv4_volt = 1300
    
    lv5_freq = 624000000
    lv5_volt = 1250
    
[/code]
## led configuration
LEDs are accessible via sys-fs; for example on the cubietruck you can find the following directory: /sys/class/leds/blue\:ph21\:led1 `cat` the file trigger to see the triggers that can be set in .fex files. Currently these are 
  * none (kinda defeats the purpose of setting a trigger)
  * rfkill0
  * battery-charging-or-full
  * battery-charging
  * battery-full
  * battery-charging-blink-full-solid
  * ac-online
  * usb-online
  * mmc0
  * mmc1
  * timer
  * heartbeat
  * cpu0
  * cpu1
  * default-on
  * rfkill1
  * rfkill2

How much they make sense - experiment. I'd be especially curious about the effects of rfkill settings. 
Please note that depending on the trigger in question the sysfs will be populated with even more pseudo files. When you choose timer for example then you get a constant blinking led and two more files: delay_on and delay_off with which you can specify how many milliseconds will the LED stay in on/off state. Very convenient to indicate eg. disk usage or average load with higher blinking frequency and stuff like that. 
### [leds_para]
Configuration example: 
[code] 
    [leds_para]
    leds_used = 1
    leds_num = 3
    leds_pin_1 = port:PH20<1><default><default><0>
    leds_name_1 = "ph20:green:led1"
    leds_trigger_1 = "heartbeat"
    leds_pin_2 = port:PH21<1><default><default><0>
    leds_name_2 = "ph21:blue:led2"
    leds_trigger_2 = "cpu0"
    leds_pin_3 = port:PI12<1><default><default><0>
    leds_name_3 = "red:pi12:led3"
    leds_trigger_3 = "cpu1"
    
[/code]
### external leds
External LEDs that are connected to one of the GPIO pins (don't forget to add a resistor!) can also be defined in the fex file and used like internal ones afterwards. You have to check which GPIO pin is connected to which SoC pin and use this in the definition. As an example a 3rd led on a Banana Pro connected to GPIO pin 19 (PI12) in the config above. This will lead to a sysfs entry /sys/class/leds/red:pi12:led3 where everything works just like with internal leds. 
## dynamic configuration
### [dynamic]
Configuration example: 
[code] 
    [dynamic]
    MAC = "000000000000"
    
[/code]
