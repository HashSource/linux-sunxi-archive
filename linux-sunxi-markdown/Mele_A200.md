# Mele A200
Mele A200  
---  
[![Device front.jpg][36415]][36416]  
Manufacturer |  [Mele][36417]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][36418]  
Specifications   
SoC |  [A10s][36419] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  4GB   
Power |  DC 5V @ 1A   
Features   
LCD |  N.A.   
Touchscreen |  N.A.   
Video |  HDMI (Type A Female)   
Audio |  N.A.   
Network |  WiFi 802.11 b/g ([RTL8188eu][36420]), 100Mbps Ethernet ([Realtek_RTL8201CP][36421])   
Storage |  SD   
USB |  2 USB2.0 Host   
Camera |  N.A.   
Other |  N.A.   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][36422] and the [New Device Page guide][36423].
Mele A200 is a cheap A10s Set-Top-Box. There is an early version without Ethernet, and later version with dual core A20. This page is written based on the A10s version device with an Ethernet. 
## Contents
  * [1 Identification][36424]
  * [2 Sunxi support][36425]
    * [2.1 Current status][36426]
    * [2.2 Images][36427]
    * [2.3 HW-Pack][36428]
    * [2.4 BSP][36429]
    * [2.5 Manual build][36430]
    * [2.6 Mainline U-Boot][36431]
    * [2.7 Mainline kernel][36432]
  * [3 Tips, Tricks, Caveats][36433]
    * [3.1 FEL mode][36434]
    * [3.2 Device specific topic][36435]
    * [3.3 ...][36436]
  * [4 Adding a serial port (**voids warranty**)][36437]
    * [4.1 Device disassembly][36438]
    * [4.2 Locating the UART][36439]
  * [5 Pictures][36440]
  * [6 Also known as][36441]
  * [7 See also][36442]
    * [7.1 Manufacturer images][36443]

# Identification
On the back of the device, the following is printed: 
[code] 
    MELE迈乐
    型号(MODEL):A200
[/code]
The PCB has the following silkscreened on it: 
[code] 
    AB10S-G41A-V1.40-0
    WLBM:831-2454140-90
    2012-11-06
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

Please note, there are several version of A200, the information here is based on single core (A10s) version with LAN port. 
# Sunxi support
## Current status
sunxi-linux-3.4 works fine (as headless server). 
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][36442]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building u-boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][36444]

Everything else is the same as the [manual build howto][36445]. 
## Mainline U-Boot
For generic upstream u-boot, follow the Google groups post here: [https://groups.google.com/forum/#!searchin/linux-sunxi/upstream$20uboot/linux-sunxi/z2kby8B38o8/rU2YUi55bTkJ][36446]
Here is instruction that works for Mele A200, after setting up cross compiler. ` `
`
  1. export PATH="/path/to/cross/compiler/bin:$PATH"
  2. make -j2 CROSS_COMPILE=arm-linux-gnueabihf- A10s-OlinuXino-M_defconfig
  3. make -j2 CROSS_COMPILE=arm-linux-gnueabihf-
  4. dd if=u-boot-sunxi-with-spl.bin of=/dev/your_mmc_card bs=1024 seek=8

```
`` Mele A200 has some difference from A10s-OlinuXino-M, will try to address it later (TODO). mmc works, HDMI works, USB keyboard works (storage seems work), network works. 
For [ building mainline u-boot][36447], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
Most of components are supported by mainline kernel. Use this [Wip dts patch ][36448] for preliminary device-tree file. The configuration file is for Debian Jessie. 
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][36449]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
[code] 
    --------fastboot partitions--------
    -total partitions:11-
    -name-        -start-       -size-      
    bootloader  : 1000000       1000000     
    env         : 2000000       1000000     
    boot        : 3000000       2000000     
    system      : 5000000       20000000    
    data        : 25000000      60000000    
    misc        : 85000000      1000000     
    recovery    : 86000000      2000000     
    cache       : 88000000      8000000     
    private     : 90000000      1000000     
    sysrecovery : 91000000      20000000    
    UDISK       : b1000000      3b000000    
    -----------------------------------
[/code]
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][36450]. 
##  Device specific topic
[Install to Nand][36451]
Although the forum post is about A10 Olimex-lime, it is tested works on A200, using sunxi-3.4 kernel and Debian Wheezy. 
## ...
# Adding a serial port (**voids warranty**)
[![][36452]][36453]
[][36454]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][36455]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
The CPU is marked as "A10s", RTL8201cp LAN chip, RTL8188eus WIFI chip, AXP152 power chip. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][36455].
# Pictures
Take some pictures of your device, [ upload them][36456], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Screen.JPG][36457]][36458]
  * [![Device front.jpg][36459]][36416]
  * [![Device back.jpg][36460]][36461]
  * [![Device buttons 1.jpg][36462]][36463]
  * [![Device buttons 2.jpg][36464]][36465]
  * [![Device board front.jpg][36466]][36467]
  * [![Device board back.jpg][36468]][36469]

# Also known as
List rebadged devices here.
# See also
[Mele_A210][36470]
[Olimex_A10s-OLinuXino-Micro][36471]
## Manufacturer images
Optional. Add non-sunxi images in this section.
