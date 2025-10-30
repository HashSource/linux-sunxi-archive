# Onda V972
Onda V972  
---  
[![Device front.jpg][41561]][41562]  
Manufacturer |  [Onda][41563]  
Dimensions |  242.0 _mm_ x 187.5 _mm_ x 9.8 _mm_  
Release Date |  5 December 2012   
Website |  [V972 Product page][41564]  
Specifications   
SoC |  [A31][41565] @ 1.0Ghz   
DRAM |  Hynix H5TQ2G43CFR-PBC 256MiB DDR3 SDRAM x8 (2GiB) @ xxxMHz   
NAND |  Hynix H27UCG8T2MYR 8GiB NAND x2 (16GiB)   
Power |  DC 5V @ xA, 8000mAh 3.7V Li-Poly battery   
Features   
LCD |  2048x1536 (9.7" 4:3 IPS retina-class 264ppi)   
Touchscreen |  10-finger capacitive ([Manufacturer device][41566])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  Realtek RTL811EUS IEEE 802.11 b/g/n ([Manufacturer device][41567])   
Storage |  µSD   
USB |  1 µUSB OTG   
Camera |  2.0MP (?x?) front, 5.0MP (?x?) rear   
Other |  Accelerometer ([Manufacturer device][41568])   
This page needs to be properly filled according to the [New Device Howto][41569] and the [New Device Page guide][41570].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][41571]
  * [2 Sunxi support][41572]
    * [2.1 Current status][41573]
    * [2.2 Images][41574]
    * [2.3 HW-Pack][41575]
    * [2.4 BSP][41576]
    * [2.5 Manual build][41577]
      * [2.5.1 U-Boot][41578]
        * [2.5.1.1 Sunxi/Legacy U-Boot][41579]
        * [2.5.1.2 Mainline U-Boot][41580]
      * [2.5.2 Linux Kernel][41581]
        * [2.5.2.1 Sunxi/Legacy Kernel][41582]
        * [2.5.2.2 Mainline kernel][41583]
  * [3 Tips, Tricks, Caveats][41584]
    * [3.1 FEL mode][41585]
    * [3.2 Device specific topic][41586]
    * [3.3 ...][41587]
  * [4 Adding a serial port (**voids warranty**)][41588]
    * [4.1 Device disassembly][41589]
    * [4.2 Locating the UART][41590]
  * [5 Pictures][41591]
  * [6 Also known as][41592]
  * [7 Variants/clones][41593]
  * [8 See also][41594]
    * [8.1 Manufacturer images][41595]
    * [8.2 User made images][41596]
    * [8.3 Categories][41597]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    ONDA
    Model: V972 四核版 (Translation: Quad-core version) Made in China
    SN:[SN] 
[/code]
The PCB has the following silkscreened on it: 
[code] 
    LIA-BB-V6.66
    1970-01-01
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _V972 Core4_
  * Android Version: _v4.2.2_
  * Kernel Version: _3.3.0 lgm@SzExdroid5 #28 Tue May21 11:51:35 CST 2013_
  * Build Number: _fiber_onda978q9-eng 4.2.2 JDQ29 20130522 test-keys_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][41594]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
[SDK_build_howto_A31][41598] \- SDK build howto (generic) 
## Manual build
You can build things for yourself by following our [ Manual build howto][41599] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][41600] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][41601]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][41602]][41603]
[][41604]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][41605]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
To open remove 4 tiny screws on the bezel and lift alu backplate. There are some plastic tabs keeping it in place, [Plastic tool howto][41606] might come handy. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][41605].
# Pictures
Take some pictures of your device, [ upload them][41607], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][41608]][41562]
  * [![Device back.jpg][41609]][41610]
  * [![Device buttons 1.jpg][41611]][41612]
  * [![Device buttons 2.jpg][41613]][41614]
  * [![Onda v972-inside.jpg][41615]][41616]
  * [![Device board back.jpg][41617]][41618]

# Also known as
List rebadged devices here.
# Variants/clones
  * V972 comes in 3 versions differing with at least touchscreen (have V1/V2/V3 in model number)
  * Modecom Freetab 9704 IPS2-X4 (pcb ver 1.4 = v1, 1.6 = v2)
  * Archos 97 Platinum HD
  * Texet TM-9751HD

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
[v3.2.1 firmware][41619]
## User made images
[omni rom][41620] \- user build of 4.4.4 with compatibility packages for many a31 tablets 
## Categories
