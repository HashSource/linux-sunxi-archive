# Inet 86vw
Inet 86vw  
---  
[![Device front.jpg][26561]][26562]  
Manufacturer |  [iNet][26563]  
Dimensions |  191 _mm_ x 116 _mm_ x 12 _mm_  
Release Date |  June 2013   
Website |  [Device Product Page][26564]  
Specifications   
SoC |  [A13][26565] @ 1.2 Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  4 GB   
Power |  DC 5V @ 2A, 2800mAh 3.7V LiFe battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Manufacturer device][26566] FIXME)   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8723AS][26567])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  1.3MP (1280x960) front, 1.3MP (1280x960) rear   
Other |  Accelerometer ([MEMSIC MXC622X][26568]), Reset button   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][26569] and the [New Device Page guide][26570].
A low-budget, A13 tablet device, running Android 4.0.4 Ice-Cream Sandwich. 
## Contents
  * [1 Identification][26571]
    * [1.1 PowerFast][26572]
    * [1.2 PCB][26573]
  * [2 Sunxi support][26574]
    * [2.1 Current status][26575]
    * [2.2 Manual build][26576]
    * [2.3 Mainline U-Boot][26577]
    * [2.4 FEL mode][26578]
    * [2.5 Device disassembly][26579]
    * [2.6 Locating the UART][26580]
  * [3 Also known as][26581]
  * [4 See also][26582]

# Identification
## PowerFast
On the back of the device, the following is printed: 
[code] 
    PowerFast TCTB-7106DC3g-Plus (South America/Brazil)
[/code]
## PCB
The PCB has the following silkscreened on it: 
[code] 
    INET-86VW-REV06 Zeng-gc 2013-06-21
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _TCTB-7106DC3g (can vary from country to country)_
  * Build Number: _A13_86VWBC_M705BC_1306135.20130724_

# Sunxi support
## Current status
WORK IN PROGRESS 
## Manual build
  * For building u-boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][26583]

Everything else is the same as the [manual build howto][26584]. 
## Mainline U-Boot
For [ building mainline u-boot][26585], use the _MANUFACTURER_DEVICE_ target. 
## FEL mode
The _Volume +_ button triggers [ FEL mode][26586]. 
## Device disassembly
Carefully insert a small, plastic spatula in the groove, in the opposite side from the _Volume_ buttons. Take care to not damage the case, nor the speaker cables inside. 
## Locating the UART
[File:Product Board.jpg][26587]
UART pads
This one looks straight-forward. _Rx_ and _Tx_ pads are between the processor's enclosure and the mmc/SIM card slot. The _GND_ is just on top of the board, between back camera and board's identification silk screen. Just solder the wires and have a go for it. 
(NOTE: Also has an _Ub001_ pad, don't mess with it!) 
# Also known as
TCTB-7106DC3G 
# See also
[Inet 86vs][26588] [Inet 86vz][26589]
