# Jesurun Q5
Jesurun Q5  
---  
[![Jesurun Q5 Device front.jpg][29074]][29075]  
Manufacturer |  [Jesurun][29076]  
Dimensions |  100 _mm_ x 100 _mm_ x 24 _mm_  
Release Date |  August 2013   
Website |  Unknown   
Specifications   
SoC |  [A10][29077] @ 1Ghz   
DRAM |  1GiB DDR3 @ 312MHz (4x [PE918-15E][29078])   
NAND |  8GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full, female)   
Audio |  3.5mm headphone plug, HDMI, SPDIF   
Network |  WiFi 802.11 g ([Realtek RTL8188CTV][29079]), 10/100Mbps Ethernet ([Realtek RTL8201CP][29080])   
Storage |  µSD   
USB |  2X USB2.0 Host   
Headers |  UART, IRDA   
This page needs to be properly filled according to the [New Device Howto][29081] and the [New Device Page guide][29082].
The Jesurun Q5 is a cheap [A10][29077] based media puck, with a distinctive case with the top and bottom panels consisting almost entirely of ventilation holes. 
## Contents
  * [1 Identification][29083]
  * [2 Sunxi support][29084]
    * [2.1 Current status][29085]
    * [2.2 Images][29086]
    * [2.3 HW-Pack][29087]
    * [2.4 BSP][29088]
    * [2.5 Manual build][29089]
    * [2.6 Mainline U-Boot][29090]
    * [2.7 Mainline kernel][29091]
  * [3 Tips, Tricks, Caveats][29092]
    * [3.1 FEL mode][29093]
    * [3.2 Mainline U-Boot: HDMI hotplug detection does not work][29094]
  * [4 Adding a serial port (**voids warranty**)][29095]
    * [4.1 Device disassembly][29096]
    * [4.2 Locating the UART][29097]
  * [5 Pictures][29098]
  * [6 Also known as][29099]
  * [7 See also][29100]
    * [7.1 Manufacturer images][29101]

# Identification
Apart from a _Jesurun_ sticker, there are no external markings. 
The PCB has the following silkscreened on it: 
[code] 
    AVM STV301 MB V1.1
    2012.07.16
[/code]
Find out the strings as reported under settings.
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
U-boot-sunxi and linux-sunxi are supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _jesurun_q5_defconfig_ target.
  * The .fex file can be found in sunxi-boards as [sys_config/a10/jesurun-q5.fex][29102]

Everything else is the same as the [manual build howto][29103]. 
## Mainline U-Boot
For [ building mainline u-boot][29104], use the _jesurun_q5_defconfig_ target. 
## Mainline kernel
Use the _sun4i-a10-jesurun-q5.dts_ device-tree file for the [mainline kernel][29105]. 
**NOTE** : submitting patch is WIP (2015-02-26) 
# Tips, Tricks, Caveats
## FEL mode
There is a solder mask for a button on the board that might trigger [ FEL mode][29106], but it is not populated. 
## Mainline U-Boot: HDMI hotplug detection does not work
Workaround: 
  * Manually set video mode and disable hot-plug detection

[code] 
    sunxi# setenv video-mode sunxi:1280x720-24@60,hpd=0
[/code]
  * Make env variable persistent:

[code] 
    sunxi# saveenv
[/code]
Verify: Check video-mode env variable: 
[code] 
    sunxi# printenv video-mode
       video-mode=sunxi:1280x720-24@60,hpd=0
[/code]
# Adding a serial port (**voids warranty**)
[![][29107]][29108]
[][29109]
UART pads
## Device disassembly
This casing is trivially disassembled by removing 4 Philips screws on the bottom. 
## Locating the UART
The UART pads are clearly marked on the top of the board. You can solder in a 2.54mm pitch header as shown in the picture, or you can solder on wires directly. For more information read our [UART howto][29110]. 
# Pictures
  * [![Jesurun Q5 Device front.jpg][29111]][29075]
  * [![Jesurun Q5 Device back.jpg][29112]][29113]
  * [![Jesurun Q5 Device side 1.jpg][29114]][29115]
  * [![Jesurun Q5 Device side 2.jpg][29116]][29117]
  * [![Jesurun Q5 Device board front.jpg][29118]][29119]
  * [![Jesurun Q5 Device board back.jpg][29120]][29121]

# Also known as
# See also
## Manufacturer images
