# MID-KLIPAD HC-913
MID-KLIPAD HC-913  
---  
[![Device front.jpg][32980]][32981]  
Manufacturer |  [Klipad][32982]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  Not anymore   
Specifications   
SoC |  [A13][32983] @ 1.3Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  4 GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (9" X:Y)   
Touchscreen |  x-finger capacitive ([Silead GSL3680][32984])   
Video |  None   
Audio |  3.5mm headphone plug, internal speaker   
Network |  WiFi 802.11 b/g/n ([MediaTek MT7601UN][32985])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front   
Other |  Accelerometer ([Manufacturer device][32986])   
This page needs to be properly filled according to the [New Device Howto][32987] and the [New Device Page guide][32988].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][32989]
  * [2 Sunxi support][32990]
    * [2.1 Current status][32991]
    * [2.2 Images][32992]
    * [2.3 HW-Pack][32993]
    * [2.4 BSP][32994]
    * [2.5 Manual build][32995]
    * [2.6 Mainline U-Boot][32996]
    * [2.7 Mainline kernel][32997]
  * [3 Tips, Tricks, Caveats][32998]
    * [3.1 FEL mode][32999]
    * [3.2 Device specific topic][33000]
    * [3.3 ...][33001]
  * [4 Adding a serial port (**voids warranty**)][33002]
    * [4.1 Device disassembly][33003]
    * [4.2 Locating the UART][33004]
  * [5 Pictures][33005]
  * [6 Also known as][33006]
  * [7 See also][33007]
    * [7.1 Manufacturer images][33008]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    MID-KLIPAD HC-913
[/code]
The PCB has the following silkscreened on it: 
[code] 
    A91-V05
    2013-04-12
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Work on 3.4.103+ kernel, but for : \- wifi : not supported t'ill 4.2+ kernel \- touchscreen (I'm currently testing it). 
Not tested : \- camera \- axis detector 
## Images
[Uboot, kernel and "naked" Gentoo rootfs][33009]
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building the full BSP, use the _a13_mid_ target.
  * The .fex file can be found in [my github repo][33010]

Everything else is the same as the [manual build howto][33011]. 
## Mainline U-Boot
If there is mainline U-Boot support, add this section.
For [ building mainline U-Boot][33012], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][33013]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][33014]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][33015]][33016]
[][33017]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][33018]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][33019].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][33018].
# Pictures
  * [![HC-913 - Battery and motherboard.jpeg][33020]][33021]
  * [![HC-913 - Motherboard.jpeg][33022]][33023]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
