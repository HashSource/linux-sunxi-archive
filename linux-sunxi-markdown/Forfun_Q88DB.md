# Forfun Q88DB
Forfun Q88DB  
---  
[![Forfun q88db - front.jpg][19596]][19597]  
Manufacturer |  [Unknown Manufacturer][19598]  
Dimensions |  182 _mm_ x 121 _mm_ x 7 _mm_  
Release Date |  May 2013   
Website |  [Missing Device Product Page][19599]  
Specifications   
SoC |  [A13][19600] @ 1Ghz   
DRAM |  512MiB DDR3 @384MHz (2x [N2CB2G80GN-CG][19601] or 2x [256X8DDR3 HL 1320][19602])   
NAND |  4GB   
Power |  DC 5V @ 2A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([ZEITEC zet6221][19603])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][19604])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Memsic MXC622X][19605]), RTC   
Headers |  UART   
A standard [Q8 format][19606], [A13][19600] based tablet, but with separate [UART][19607] pads. 
## Contents
  * [1 Identification][19608]
  * [2 Sunxi support][19609]
    * [2.1 Current status][19610]
    * [2.2 Images][19611]
    * [2.3 HW-Pack][19612]
    * [2.4 BSP][19613]
    * [2.5 Manual build][19614]
    * [2.6 Mainline U-Boot][19615]
  * [3 Tips, Tricks, Caveats][19616]
    * [3.1 FEL mode][19617]
  * [4 Adding a serial port (**voids warranty**)][19618]
    * [4.1 Device disassembly][19619]
    * [4.2 Locating the UART][19620]
  * [5 Pictures][19621]
  * [6 Also known as][19622]
  * [7 See also][19623]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: A13-MID
  * Build Number: nuclear_pfdq88d-eng 4.0.4 IMM76D 20130531

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Forfun_Q88DB" target.
  * The .fex file can be found in sunxi-boards as [forfun_q88db.fex][19624]

Everything else is the same as the [manual build howto][19625]. 
## Mainline U-Boot
Supported in the [mainline u-boot git 'master' branch][19626] and scheduled for the [v2015.04][19627] release. 
For [ building mainline u-boot][19628], use the _forfun_q88db_ board name. 
# Tips, Tricks, Caveats
## FEL mode
The VOL+ button triggers [ boot0 FEL mode][19629]. 
# Adding a serial port (**voids warranty**)
[![][19630]][19631]
[][19632]
Q88DB UART pads
## Device disassembly
See [the Q8 tablet format disassembly page][19633]. 
## Locating the UART
There are two pads to the left of the SoC, just solder on some wires according to our [UART howto][19607]. These pads are not multiplexed with the SD card. 
# Pictures
  * [![Forfun q88db - front.jpg][19634]][19597]
  * [![Forfun q88db - back.jpg][19635]][19636]
  * [![Forfun q88db - buttons 1.jpg][19637]][19638]
  * [![Forfun q88db - buttons 2.jpg][19639]][19640]
  * [![Forfun q88db - internal.jpg][19641]][19642]
  * [![Forfun q88db - board.jpg][19643]][19644]

# Also known as
Probably has many rebadgers. 
  * Most commonly found as Forfun Q88DB

# See also
  * [Other Q8 format A13 based tablets.][19645]
  * [More PCB pictures posted in some Internet forum][19646]
