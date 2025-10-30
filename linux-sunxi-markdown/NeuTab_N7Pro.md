# NeuTab N7Pro
NeuTab N7Pro  
---  
[![N7pro-tablet.jpg][39509]][39510]  
Manufacturer |  [[1]][39511]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  February 2015  
Website |  [[2]][39512]  
Specifications   
SoC |  [A33][39513] @ XGhz   
DRAM |  512MiB DDR3 @ 456MHz   
NAND |  8GB   
Power |  DC 5V @ 2A, 2500mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7 " 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][39514])   
Video |  none   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek Semiconductor RTL8703AS][39515]), Bluetooth (Realtek Semiconductor RTL8703AS)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][39516])   
Headers |  none   
This page needs to be properly filled according to the [New Device Howto][39517] and the [New Device Page guide][39518].
## Contents
  * [1 Identification][39519]
  * [2 Sunxi support][39520]
    * [2.1 Current status][39521]
    * [2.2 Images][39522]
    * [2.3 HW-Pack][39523]
    * [2.4 BSP][39524]
    * [2.5 Manual build][39525]
    * [2.6 Mainline U-Boot][39526]
    * [2.7 Mainline kernel][39527]
  * [3 Tips, Tricks, Caveats][39528]
    * [3.1 FEL mode][39529]
      * [3.1.1 Through serial console][39530]
      * [3.1.2 FEL version example][39531]
    * [3.2 ADB][39532]
    * [3.3 Recovery mode][39533]
    * [3.4 Boot log from serial port][39534]
  * [4 Adding a serial port (**voids warranty**)][39535]
    * [4.1 Device disassembly][39536]
  * [5 Pictures][39537]
  * [6 Also known as][39538]
  * [7 See also][39539]
    * [7.1 Manufacturer images][39540]

# Identification
On the back of the device, the following is printed: 
[code] 
    NeuTab Model: N7 Pro
[/code]
The PCB has the following silkscreened on it: 
[code] 
    TZX-723QB6
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _N7Pro_
  * Build Number: _723Q6.A33.KK44.V2.31.150610.wsvga.rtl87x3xsvq0_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either U-Boot or kernel, mention this too, but add the extra sections below.
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][39539]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][39541]

Everything else is the same as the [manual build howto][39542]. 
## Mainline U-Boot
If there is mainline U-Boot support, add this section.
For [ building mainline U-Boot][39543], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][39544]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
### Through serial console
This method will NOT initialize boot1. For more information on the various ways to enter FEL mode, see the [ FEL][39545] page. 
  1. Power off the device
  2. Start a serial terminal program (`screen /dev/ttyUSB0 115200` for instance)
  3. In the serial terminal, hold down the 2 key
  4. Power on the device

The device should eventually print out the following over serial: 
[code] 
    HELLO! BOOT0 is starting!
    boot0 version : 3.1.0
    reg_addr 0x01f00100 =0x00000000
    reg_addr 0x01f00104 =0x00000000
    reg_addr 0x01f00108 =0x00000000
    reg_addr 0x01f0010c =0x00000000
    reg_addr 0x01f00110 =0x00000000
    reg_addr 0x01f00114 =0x00000000
    eraly jump fel
    
[/code]
### FEL version example
[code] 
    $ ./fel version
    AWUSBFEX soc=00001667(A33) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
    
[/code]
## ADB
This device has root access enabled by default. This means that dumping things like `script.bin` from NAND is as easy as: 
  1. Install `adb` on a PC, enable USB debugging on the tablet, and connect the tablet to the PC via USB
  2. Run `adb pull /dev/block/nanda ./nanda.img` from the PC to dump an image of `nanda` to the PC's working directory

## Recovery mode
  1. Power off the device
  2. Hold down the vol+ button
  3. Power on the device
  4. Release the vol+ button when recovery starts

## Boot log from serial port
NOTE: this log is from a device that has had its battery removed. 
[code] 
    HELLO! BOOT0 is starting!
    boot0 version : 3.1.0
    reg_addr 0x01f00100 =0x00000000
    reg_addr 0x01f00104 =0x000000cf
    reg_addr 0x01f00108 =0x00000000
    reg_addr 0x01f0010c =0xf1f18000
    reg_addr 0x01f00110 =0x00000000
    reg_addr 0x01f00114 =0x00000000
    DRAM DRIVE INFO: V1.4
    DRAM CLK =456 MHZ
    DRAM simple test OK.
    dram size =512
    sum=0xe1d09ca5
    src_sum=0xe1d09ca5
    Ready to disable icache.
    Jump to secend Boot.
    [      0.220]
    
    U-Boot 2011.09-rc1 (Nov 26 2014 - 15:14:37) Allwinner Technology 
    
    [      0.228]version: 2.1.0
    [      0.304]pmbus:   ready
    [      0.307]PMU: AXP221
    [      0.309]PMU: AXP22x found
    [      0.313]PMU: dcdc3 1200
    [      0.316]PMU: pll1 1008 Mhz,PLL6=600 Mhz
    AXI=336 Mhz,AHB=200 Mhz, APB1=100 Mhz 
    set power on vol to default
    dcdc1_vol = 3000
    dcdc2_vol = 1260
    dcdc3_vol = 1200
    dcdc4_vol = 0
    dcdc5_vol = 1600
    aldo2_vol = 2500
    aldo3_vol = 3000
    find power_sply to end
    no battery, limit to dc
    fel key old mode
    run key detect
    no key found
    no key input
    dram_para_set start
    dram_para_set end
    [      0.364]DRAM:  512 MiB
    relocation Offset is: 15b11000
    smcl's set manager is NULL
    workmode = 0
    [      0.563]NAND: NAND_UbootInit
    NAND_UbootInit start
    NB1 : enter NAND_LogicInit
    uboot:physical version: 2 1b 20140616 1640 
    nand io drivering: 2863311530
    nand : get id_number_ctl fail, 1
    uboot:nand info: a714dead ffff4a42 318c 40704 5 
    nand : get CapacityLevel fail, 5fb9cec5
    not burn nand partition table!
    NB1 : nftl num: 2 
     init nftl: 0 
    NB1 : NAND_LogicInit ok, result = 0x0 
    [      0.872]sunxi flash init ok
    out of usb burn from boot: not enough energy
    In:    serial
    Out:   serial
    Err:   serial
    --------fastboot partitions--------
    -total partitions:10-
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
    UDISK       : 5a000000      0           
    -----------------------------------
    base bootcmd=run setargs_nand boot_normal
    bootcmd set setargs_nand
    key 0
    recovery key high 5, low 3
    cant find fstbt value
    misc partition found
    misc_message->command = 0 
    to be run cmd=run setargs_nand boot_normal
    mount part name bootloader
    cant open script.bin, maybe it is not exist
    WORK_MODE_BOOT
    board_status_probe
    [      0.979]key trigger
    sunxi_bmp_logo_display
    screen_id =0, screen_width =1024, screen_height =600
    [      1.109]Hit any key to stop autoboot:  0 
    read boot or recovery all
    [      1.605]sunxi flash read :offset 4000000, 12891315 bytes OK
    no signature
    [      1.614]ready to boot
    para err in disp_ioctl, cmd = 0xa,screen id = 1
    [      1.621][mmc]: MMC Device 2 not found
    [      1.625][mmc]:  mmc  not find,so not exit
    NAND_UbootExit
    NB1 : NAND_LogicExit
    nand release dma:0
    [      1.629]
    Starting kernel ...
    
    <4
    
[/code]
# Adding a serial port (**voids warranty**)
[![][39546]][39547]
[][39548]
N7 Pro UART pads
The non-chip/connector side of the board has a number of test pads on it. Solder headers or wires to the pins below the large ground pad on the right side of the board (as seen with the USB port, power port, and power button facing upwards). For more information, please reference the [UART howto][39549]. Note: the UART pins are shared with the µSD (MicroSD) card pins, so please do not have a MicroSD card inserted when attempting to debug this device with a UART. 
## Device disassembly
See [the Q8 tablet format disassembly page][39550]. 
# Pictures
  * [![N7pro-front.jpg][39551]][39552]
  * [![N7pro-tablet-rear.jpg][39553]][39554]
  * [![N7pro-board-chipside.jpg][39555]][39556]
  * [![N7pro-board-chipside-noribbons.jpg][39557]][39558]
  * [![N7pro-chip-next-to-dram.jpg][39559]][39560]
  * [![N7pro-board-padside-uart-solered.jpg][39561]][39562]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
