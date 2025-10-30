# Inet U70B
Inet U70B  
---  
[![Device front.jpg][27189]][27190]  
Manufacturer |  [iNet][27191]  
Dimensions |  193 _mm_ x 110 _mm_ x 11 _mm_  
Specifications   
SoC |  [A33][27192] @ 1.2Ghz   
DRAM |  512MiB DDR3 @ 480MHz   
NAND |  8GB   
Power |  DC 5V @ 3A, 2000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 7"   
Touchscreen |  Multi-finger capacitive ([Silead GSL1686][27193])   
Audio |  3.5mm headphone/microphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek 8723CS][27194])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  Header (unpopulated in device on hand)   
Other |  Accelerometer ([Bosch BMA250][27195])   
This page needs to be properly filled according to the [New Device Howto][27196] and the [New Device Page guide][27197].
## Contents
  * [1 Identification][27198]
  * [2 Sunxi support][27199]
    * [2.1 Current status][27200]
    * [2.2 Manual build][27201]
      * [2.2.1 U-Boot][27202]
        * [2.2.1.1 Mainline U-Boot][27203]
      * [2.2.2 Linux Kernel][27204]
        * [2.2.2.1 Mainline kernel][27205]
  * [3 Tips, Tricks, Caveats][27206]
  * [4 Adding a serial port (**voids warranty**)][27207]
    * [4.1 Device disassembly][27208]
    * [4.2 Locating the UART][27209]
  * [5 Pictures][27210]
  * [6 Schematic][27211]
  * [7 Also known as][27212]
  * [8 See also][27213]

# Identification
This white-label board may appear in tablets by other brands. One tablet using this board is the "Nimbus 17 V1". On the back of the tablet, the following is printed: 
[code] 
    cm2
    NIMBUS performance
    2AM4S-NIMBUS17V1
    [serial number sticker]
    
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INET-U70B-REV01
    Zeng-gc 2016-11-30
    
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _Nimbus 17 V1_
  * Build Number: _Nimbus_20171110_V001_

More android build info: 
[code] 
    [ro.build.characteristics]: [tablet]
    [ro.build.date.utc]: [1510293882]
    [ro.build.date]: [Fri Nov 10 14:04:42 CST 2017]
    [ro.build.description]: [astar_ibt_8723bs-eng 4.4.2 KVT49L 20171110 test-keys]
    [ro.build.display.id]: [Nimbus_20171110_V001]
    [ro.build.fingerprint]: [iNet/astar_ibt_8723bs/astar-ibt-8723bs:4.4.2/KVT49L/20171110:eng/test-keys]
    [ro.build.host]: [inet-server01]
    [ro.build.id]: [KVT49L]
    [ro.build.product]: [astar-ibt-8723bs]
    [ro.build.tags]: [test-keys]
    [ro.build.type]: [eng]
    [ro.build.user]: [inet-soft03]
    [ro.build.version.codename]: [REL]
    [ro.build.version.incremental]: [20171110]
    [ro.build.version.release]: [4.4.2]
    [ro.build.version.sdk]: [19]
    [ro.product.board]: [exdroid]
    [ro.product.brand]: [Nimbus]
    [ro.product.device]: [astar-ibt-8723bs]
    [ro.product.firmware]: [2.1_20160317]
    [ro.product.manufacturer]: [unknown]
    [ro.product.model]: [Nimbus 17 V1]
    [ro.product.model_mtp]: [Nimbus_17_V1]
    [ro.product.name]: [astar_ibt_8723bs]
    [ro.reversion.aw_sdk_tag]: [exdroid4.4.2_r2-a33-v2.1]
    [ro.rock.gota.brand]: [unknown]
    [ro.rock.gota.model]: [Nimbus 17 V1]
    [ro.rock.gota.model_mtp]: [Nimbus_17_V1]
    [ro.rock.gota.version]: [Nimbus_20171110_V001_1510293882]
    
[/code]
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Manual build
You can build things for yourself by following our [ Manual build howto][27214] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
# Adding a serial port (**voids warranty**)
[![][27215]][27216]
[][27217]
DEVICE UART pads
See the [UART howto][27218]. A microSD breakout board is recommended for UART access. This does not require disassembly. 
## Device disassembly
Pop off the back cover by releasing the clips around the edges. The speaker is loosely glued to the back cover, so you will need to gently remove it before fully removing the back cover. 
## Locating the UART
There are UART TX and RX pads near the SD card slot. You can solder wires onto these pads, but since they are the same pins (PF2 and PF4) used for the microSD card, there is no advantage over using a microSD breakout board to access them. 
# Pictures
Take some pictures of your device, [ upload them][27219], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][27220]][27190]
  * [![Device back.jpg][27221]][27222]
  * [![Device buttons 1.jpg][27223]][27224]
  * [![Device buttons 2.jpg][27225]][27226]
  * [![Device board front.jpg][27227]][27228]
  * [![Device board back.jpg][27229]][27230]

# Schematic
No schematic is available, but here is some hardware info gathered from the stock android build: 
**GPIO mapping:**
[code] 
    GPIOs 0-383, platform/sunxi-pinctrl, sunxi-pinctrl:
     gpio-36  (cd                  ) in  lo
     gpio-225 (?                   ) out lo
     gpio-232 (otg_id              ) in  hi
     gpio-233 (?                   ) out lo
    
[/code]
**I2C mapping:**
[code] 
    root@astar-ibt-8723bs:/ # grep . /sys/bus/i2c/devices/*-0*/name
    /sys/bus/i2c/devices/0-0040/name:gslX680
    /sys/bus/i2c/devices/1-0018/name:bma250
    
[/code]
**Pinctrl mapping:**
[code] 
    root@astar-ibt-8723bs:/ # cat /sys/kernel/debug/pinctrl/pinctrl-handles
    Requested pin control handlers their pinmux maps:
    device: sunxi-pinctrl current state: none
    device: axp-pinctrl current state: none
    device: twi0 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PH2 (103) function: twi0 (26)
        type: MUX_GROUP controller sunxi-pinctrl group: PH3 (104) function: twi0 (26)
    device: twi1 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PH4 (105) function: twi1 (27)
        type: MUX_GROUP controller sunxi-pinctrl group: PH5 (106) function: twi1 (27)
    device: twi2 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PE12 (75) function: twi2 (20)
        type: MUX_GROUP controller sunxi-pinctrl group: PE13 (76) function: twi2 (20)
    device: uart0 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PF2 (83) function: uart0 (8)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PF2 (83) 00010002
        type: MUX_GROUP controller sunxi-pinctrl group: PF4 (85) function: uart0 (8)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PF4 (85) 00010002
    device: uart1 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PG6 (93) function: uart1 (17)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PG6 (93) 00010002
        type: MUX_GROUP controller sunxi-pinctrl group: PG7 (94) function: uart1 (17)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PG7 (94) 00010002
        type: MUX_GROUP controller sunxi-pinctrl group: PG8 (95) function: uart1 (17)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PG8 (95) 00010002
        type: MUX_GROUP controller sunxi-pinctrl group: PG9 (96) function: uart1 (17)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PG9 (96) 00010002
    
[/code]
**PWM mapping:**
[code] 
    root@astar-ibt-8723bs:/ # cat /sys/kernel/debug/pwm
    platform/sunxi_pwm, 2 PWM devices
     pwm-0   (lcd                 ): requested
     pwm-1   ((null)              ):
    
[/code]
**U-Boot log:**
[code] 
    U-Boot 2011.09-rc1-00024-g36bb972 (Jun 26 2017 - 09:39:25) Allwinner Technology
    
    [      0.271]version: 2.1.0
    [      0.360]pmbus:   ready
    [      0.362]PMU: AXP221
    [      0.364]PMU: AXP22x found
    [      0.368]PMU: dcdc3 1200
    [      0.371]PMU: pll1 1008 Mhz,PLL6=600 Mhz
    AXI=336 Mhz,AHB=200 Mhz, APB1=100 Mhz
    set power on vol to default
    dcdc1_vol = 3000
    dcdc2_vol = 1100
    dcdc3_vol = 1200
    dcdc4_vol = 0
    dcdc5_vol = 1500
    aldo2_vol = 2500
    aldo3_vol = 3000
    find power_sply to end
    vbus pc exist, limit to pc
    fel key old mode
    run key detect
    no key found
    no key input
    dram_para_set start
    dram_para_set end
    [      0.496]DRAM:  512 MiB
    relocation Offset is: 15aee000
    smcl's set manager is NULL
    OSAL_Power_Enable:<axp22, dc1sw>
    workmode = 0
    [      0.702]NAND: NAND_UbootInit
    NAND_UbootInit start
    NB1 : enter NAND_LogicInit
    uboot:nand version: 2 32 20170220 1103
    nand : get id_number_ctl from script, 2
    uboot:nand info: ab14dead ffff4a42 318c 60704 6
    nand : get sorting_flag fail, a
    nand : get CapacityLevel fail, 5fb7fc70
    not burn nand partition table!
    NB1 : nftl num: 2
     init nftl: 0
    NB1 : NAND_LogicInit ok, result = 0x0
    [      1.237]sunxi flash init ok
    sunxi secure storage is not supported
    find key burned flag
    In:    serial
    Out:   serial
    Err:   serial
    --------fastboot partitions--------
    -total partitions:12-
    -name-        -start-       -size-
    bootloader  : 1000000       2000000
    env         : 3000000       1000000
    boot        : 4000000       1000000
    system      : 5000000       30000000
    misc        : 35000000      1000000
    recovery    : 36000000      2000000
    cache       : 38000000      20000000
    metadata    : 58000000      1000000
    private     : 59000000      1000000
    klog        : 5a000000      1000000
    alog        : 5b000000      4000000
    UDISK       : 5f000000      0
    -----------------------------------
    base bootcmd=run setargs_nand boot_normal
    bootcmd set setargs_nand
    key 0
    recovery key high 100, low 2
    cant find fstbt value
    misc partition found
    misc_message->command = 0
    to be run cmd=run setargs_nand boot_normal
    mount part name bootloader
    cant open script.bin, maybe it is not exist
    WORK_MODE_BOOT
    board_status_probe
    [      1.351]pre sys mode
    sunxi_bmp_logo_display
    screen_id =0, screen_width =1024, screen_height =600
    [      1.474]Hit any key to stop autoboot:  0
    read boot or recovery all
    [      1.953]sunxi flash read :offset 4000000, 12626790 bytes OK
    no signature
    [      1.962]ready to boot
    para err in disp_ioctl, cmd = 0xa,screen id = 1
    [      1.969][mmc]: MMC Device 2 not found
    [      1.973][mmc]:  mmc  not find,so not exit
    NAND_UbootExit
    NB1 : NAND_LogicExit
    nand release dma:0
    [      1.977]
    Starting kernel ...
    
[/code]
**PMIC info from dmesg** : 
[code] 
    [    0.520045] axp22_board axp22_board: AXP (CHIP ID: 0x06) detected
    [    0.522136] axp22_dcdc1: 1600 <--> 3400 mV at 3000 mV
    [    0.522136] axp22_dcdc2: 600 <--> 1540 mV at 1100 mV
    [    0.522136] axp22_dcdc3: 600 <--> 1860 mV at 1200 mV
    [    0.522136] axp22_dcdc4: 600 <--> 1540 mV at 1100 mV
    [    0.522136] axp22_dcdc5: 1000 <--> 2550 mV at 1500 mV
    [    0.522136] axp22_rtc: 3000 mV
    [    0.522136] axp22_aldo1: 700 <--> 3300 mV at 3000 mV
    [    0.522136] axp22_aldo2: 700 <--> 3300 mV at 2500 mV
    [    0.522136] axp22_aldo3: 700 <--> 3300 mV at 3000 mV
    [    0.522136] axp22_dldo1: 700 <--> 3300 mV at 700 mV
    [    0.522136] axp22_dldo2: 700 <--> 3300 mV at 700 mV
    [    0.522136] axp22_dldo3: 700 <--> 3300 mV at 700 mV
    [    0.522136] axp22_dldo4: 700 <--> 3300 mV at 700 mV
    [    0.522136] axp22_eldo1: 700 <--> 3300 mV at 700 mV
    [    0.522136] axp22_eldo1: supplied by axp22_dcdc1
    [    0.522136] axp22_eldo2: 700 <--> 3300 mV at 700 mV
    [    0.522136] axp22_eldo2: supplied by axp22_dcdc1
    [    0.522136] axp22_eldo3: 700 <--> 3300 mV at 700 mV
    [    0.522136] axp22_eldo3: supplied by axp22_dcdc1
    [    0.522136] axp22_dc5ldo: 700 <--> 1400 mV at 1100 mV
    [    0.522136] axp22_ldoio0: 700 <--> 3300 mV at 3800 mV
    [    0.522136] axp22_ldoio1: 700 <--> 3300 mV at 3800 mV
    [    0.530071] axp22_dc1sw: at 700 mV
    [    0.530071] axp22_dc1sw: supplied by axp22_dcdc1
    [    0.565902] no usbc(0) det_vbus gpio and try to axp det_pin
    [    0.669659] [rtl8723bs]: module power name axp22_dldo1
    [    0.669673] [rtl8723bs]: module power ext1 name axp22_dldo2
    [    0.669849] [rtl8723bs]: rtl8723bs module power set by axp.
    [   12.940521] lcd_power0:axp22_dc1sw
    [   14.590835] [sw_device]:get_power_para: power_ldo = axp22_ldoio1,power_ldo_vol = 3300,power_io = 0,reset_pin = 225
    
[/code]
**More info from dmesg:**
[code] 
    [   24.900024] ctp_wakeup gpio number is 225
    [   24.904473] ctp_irq gpio number is 37
    
    
[/code]
# Also known as
  * Nimbus 17 V1

# See also
  * <https://fccid.io/2AM4S-NIMBUS17V1> (FCC registration)
