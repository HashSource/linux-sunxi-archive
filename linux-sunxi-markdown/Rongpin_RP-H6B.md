# Rongpin RP-H6B
Rongpin RP-H6B  
---  
[![RP-H6B Front.jpg][47641]][47642]  
Manufacturer |  [Shenzhen Rongpin Electronic Technology Co., Ltd.][47643]  
Dimensions |  160 _mm_ x 90 _mm_ x 17 _mm_  
Release Date |  April 2018   
Website |  [Device Product Page][47644]  
Specifications   
SoC |  [H6][47645] @ 1.5 Ghz   
DRAM |  1GiB LPDDR3 @ xxxMHz   
NAND |  8GiB eMMC   
Power |  DC 12V @ xxxA (Max36W)   
Features   
Video |  HDMI 2.0a, CVBS OUT   
Audio |  HDMI, PHONE OUT   
Network |  10/100Mbps Ethernet @ RJ45   
Storage |  micro SD   
USB |  4 HOST USB 2.0, 1 HOST USB 3.0   
Other |  UART0(Debug)   
This page needs to be properly filled according to the [New Device Howto][47646] and the [New Device Page guide][47647].
Rongpin RP-H6B is H6 based development board produced by Rongpin. 
## Contents
  * [1 Identification][47648]
  * [2 Sunxi support][47649]
    * [2.1 Current status][47650]
    * [2.2 Images][47651]
    * [2.3 HW-Pack][47652]
    * [2.4 BSP][47653]
    * [2.5 Manual build][47654]
      * [2.5.1 U-Boot][47655]
        * [2.5.1.1 Sunxi/Legacy U-Boot][47656]
        * [2.5.1.2 Mainline U-Boot][47657]
      * [2.5.2 Linux Kernel][47658]
        * [2.5.2.1 Sunxi/Legacy Kernel][47659]
        * [2.5.2.2 Mainline kernel][47660]
  * [3 Tips, Tricks, Caveats][47661]
    * [3.1 FEL mode][47662]
    * [3.2 Device specific topic][47663]
    * [3.3 ...][47664]
  * [4 Adding a serial port (**voids warranty**)][47665]
    * [4.1 Locating the UART][47666]
  * [5 Pictures][47667]
  * [6 Also known as][47668]
  * [7 See also][47669]
    * [7.1 Manufacturer images][47670]

# Identification
On the back of the device, the following is printed: 
[code] 
    RP-H6B
[/code]
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][47669]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][47671] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][47672] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][47673]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][47674]][47675]
[][47676]
Rongpin RP-H6B UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][47677]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][47677].
# Pictures
Take some pictures of your device, [ upload them][47678], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![RP-H6B Front.jpg][47679]][47642]
  * [![RP-H6B Back.jpg][47680]][47681]
  * [![Device buttons 1.jpg][47682]][47683]
  * [![Device buttons 2.jpg][47684]][47685]
  * [![Device board front.jpg][47686]][47687]
  * [![Device board back.jpg][47688]][47689]

# Also known as
List rebadged devices here.
# See also
[File:RP-H6C-20180316 Schematics.pdf][47690] [File:RP-H6B-20180423 Schematics.pdf][47691]
## Manufacturer images
Optional. Add non-sunxi images in this section.
