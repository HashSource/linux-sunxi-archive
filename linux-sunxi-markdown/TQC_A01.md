# TQC A01
TQC A01  
---  
[![TQC A01 front.jpg][53439]][53440]  
Manufacturer |  [TaiqiGame][53441]  
Dimensions |  96 _mm_ x 96 _mm_ x 17 _mm_  
Release Date |  early 2018 year  
Website |  [TQC][53442]  
Specifications   
SoC |  [H6][53443] @ 1.8Ghz   
DRAM |  1GiB DDR3 @ 1600MHz   
NAND |  8GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full)   
Audio |  HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([AP6212][53444]), 10/100Mbps Ethernet ([embedded AC200][53445])   
Storage |  µSD, eMMC   
USB |  1 USB3.0 Host, 1 USB2.0 Host, 1 USB2.0 OTG   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][53446] and the [New Device Page guide][53447].
Inexpensive TV box with the H6 SoC and some general specifications (1GiB RAM, 8GiB eMMC), but missing GBit Ethernet. What is special is that it has a circular shape, including the PCB and the casing. 
official description of TQC-A01: 
_TQC娱乐云终端是一台可以共享计算能力，同时赚取积分的新一代智能娱乐云设备，是一款基于区块链技术的私人娱乐终端。通过收集用户闲置算力的方式，解决游戏行业中数据分析遇到的问题。作为回报，泰奇互动将根据用户的贡献回馈用户TQC积分，该积分可用于泰奇互动的全系产品并享有额外的增值服务。_
_TQC Entertainment Cloud Terminal is a new generation smart entertainment cloud device that allows users to share computing power and earn points. It is a private entertainment terminal based on blockchain technology. By collecting idle computing power from users, it solves the problems encountered in data analysis in the gaming industry. As a reward, TQ Interactive will give back TQC points to users based on their contributions. These points can be used for all products of TQ Interactive and enjoy additional value-added services. (translated by ChatGPT)_
It was launched in early 2018 and ceased its business operations in Q2 2023. 
## Contents
  * [1 Identification][53448]
  * [2 Sunxi support][53449]
    * [2.1 Current status][53450]
    * [2.2 Manual build][53451]
      * [2.2.1 U-Boot][53452]
        * [2.2.1.1 Mainline U-Boot][53453]
      * [2.2.2 Linux Kernel][53454]
        * [2.2.2.1 Mainline kernel][53455]
  * [3 Tips, Tricks, Caveats][53456]
    * [3.1 FEL mode][53457]
    * [3.2 Device specific topic][53458]
    * [3.3 ...][53459]
  * [4 Adding a serial port (**voids warranty**)][53460]
    * [4.1 Device disassembly][53461]
    * [4.2 Locating the UART][53462]
  * [5 Pictures][53463]
  * [6 Schematic][53464]
  * [7 Also known as][53465]
  * [8 See also][53466]
    * [8.1 Manufacturer images][53467]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
     产品型号(Model): TQC-A01
[/code]
The PCB has the following silkscreened on it: 
[code] 
    AZW-KT02
    Ver: 2.0
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _TQC_
  * Build Number: _106N0_
  * Kernel Version: _3.10.65_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Manual build
You can build things for yourself by following our [ Manual build howto][53468] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The UPGRADE button triggers [ FEL mode][53469]. It is between the USB 3.0 port and the DC 5V port. 
[![][53470]][53471]
[][53472]
TQC A01 UPGRADE button
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][53473]][53474]
[][53475]
TQC-A01 UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][53476]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][53477].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][53476].
# Pictures
  * [![TQC A01 top.jpg][53478]][53479]
  * [![TQC A01 base.jpg][53480]][53481]
  * [![TQC A01 pcb top.jpg][53482]][53483]
  * [![TQC A01 pcb bottom.jpg][53484]][53485]
  * [![TQC A01 back side 1.jpg][53486]][53487]
  * [![TQC A01 back side 2.jpg][53488]][53489]
  * [![TQC A01 box top.jpg][53490]][53491]
  * [![TQC A01 box bottom.jpg][53492]][53493]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
  * [Similar Device: Eachlink H6 Mini][53494]
  * [AZW OEM official websize][53495]
  * [TaiqiGame(rebadged) official websize][53441]

## Manufacturer images
Optional. Add non-sunxi images in this section.
