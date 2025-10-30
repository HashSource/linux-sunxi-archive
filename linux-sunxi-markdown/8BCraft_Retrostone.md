# 8BCraft Retrostone
Work in Progress. Please contribute and join discord to discuss <https://discord.gg/G5yxVPp>
  

8BCraft Retrostone  
---  
[![Rsfront.jpg][128]][129]  
Manufacturer |  [8BCraft][130]  
Dimensions |  _90mm_ x _25mm_ x _130mm_  
Release Date |  07/2018   
Website |  [8BCraft Retrostone][131]  
Specifications   
SoC |  [H3][132] @ 1.2Ghz   
DRAM |  1GiB DDR3 @ xxxMHz   
Power |  DC 5V @ 3A, 3000mAh 3.7V Li-Ion battery, energysquare   
Features   
LCD |  WidthxHeight (3.5" X:Y)   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker   
Network |  100Mbps Ethernet ([Manufacturer device][133])   
Storage |  µSD   
USB |  4x USB2.0 Host   
Other |  Built-in game controller, D-Pad and buttons   
Headers |  UART, JTAG, LCD, VGA   
This page needs to be properly filled according to the [New Device Howto][134] and the [New Device Page guide][135].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][136]
  * [2 Sunxi support][137]
    * [2.1 Current status][138]
    * [2.2 Manual build][139]
      * [2.2.1 U-Boot][140]
        * [2.2.1.1 Sunxi/Legacy U-Boot][141]
        * [2.2.1.2 Mainline U-Boot][142]
      * [2.2.2 Linux Kernel][143]
        * [2.2.2.1 Sunxi/Legacy Kernel][144]
        * [2.2.2.2 Mainline kernel][145]
  * [3 Tips, Tricks, Caveats][146]
    * [3.1 FEL mode][147]
    * [3.2 Device specific topic][148]
    * [3.3 ...][149]
  * [4 Adding a serial port (**voids warranty**)][150]
    * [4.1 Device disassembly][151]
    * [4.2 Locating the UART][152]
  * [5 Pictures][153]
  * [6 Also known as][154]
  * [7 See also][155]
    * [7.1 Manufacturer images][156]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    RSN-001
[/code]
The PCB has the following silkscreened on it: 
[code] 
    RetroStone Pi v.13
[/code]
# Sunxi support
## Current status
Retrostone currently uses stock H3 u-boot and FEX 
## Manual build
You can build things for yourself by following our [ Manual build howto][157] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][158] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][159]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][160]][161]
[][162]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][163]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][164].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][163].
# Pictures
Take some pictures of your device, [ upload them][165], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Rsfront.jpg][166]][129]
  * [![RSback.jpg][167]][168]
  * [![RStop.jpg][169]][170]
  * [![RSbottom.jpg][171]][172]
  * [![RSleft.jpg][173]][174]
  * [![RSright.jpg][175]][176]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
