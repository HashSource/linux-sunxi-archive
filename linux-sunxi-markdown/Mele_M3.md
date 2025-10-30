# Mele M3
Mele M3  
---  
[![Mele-m3-front.jpg][37088]][37089]  
Manufacturer |  [Mele][37090]  
Dimensions |  140 _mm_ x 105 _mm_ x 40 _mm_  
Release Date |  September 2013   
Website |  [Device Product Page][37091] (see page#14)   
Specifications   
SoC |  [A20][37092] @ 1Ghz   
DRAM |  1GiB DDR3 @ 384MHz ([H5TQ2G83EFR-PBC][37093])   
NAND |  4GB (H27UBG8T2BTR-BC)   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI 1.4 (Type A - full), Composite, VGA   
Audio |  Left/Right RCA connectors, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][37094]), 10/100Mbps Ethernet ([Realtek RTL8201CP][37095])   
Storage |  SD   
USB |  3 USB2.0 Host   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][37096] and the [New Device Page guide][37097].
The Mele M3 is an [A20][37092] based HTPC housed in the case of the original [Mele A2000][37098]. 
## Contents
  * [1 Identification][37099]
  * [2 Sunxi support][37100]
    * [2.1 Current status][37101]
    * [2.2 Manual build][37102]
      * [2.2.1 U-Boot][37103]
        * [2.2.1.1 Sunxi/Legacy U-Boot][37104]
        * [2.2.1.2 Mainline U-Boot][37105]
      * [2.2.2 Linux Kernel][37106]
        * [2.2.2.1 Sunxi/Legacy Kernel][37107]
        * [2.2.2.2 Mainline kernel][37108]
  * [3 Tips, Tricks, Caveats][37109]
    * [3.1 FEL mode][37110]
  * [4 Adding a serial port (**voids warranty**)][37111]
    * [4.1 Device disassembly][37112]
    * [4.2 Locating the UART][37113]
  * [5 Pictures][37114]
  * [6 Also known as][37115]
  * [7 See also][37116]

# Identification
Device has only "Mele" but no "M3" printed on the case, but you can find "Mele M3" on the carton. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: _SoftwinerEvb_
  * Build Number: _v1.1.1_

# Sunxi support
## Current status
Supported 
## Manual build
You can build things for yourself by following our [ Manual build howto][37117] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Not supported 
  * u-boot-sunxi is deprecated, use mainline u-boot as delineated below.

#### Mainline U-Boot
For [ building mainline u-boot][37118], use the _Mele_M3_defconfig_ target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
The .fex file can be found in sunxi-boards as [Mele_M3.fex][37119]
#### Mainline kernel
Use the _sun7i-a20-m3.dtb_ device-tree file for the [mainline kernel][37120]. 
# Tips, Tricks, Caveats
## FEL mode
The Mele A1000 can be put into FEL mode by shorting jumper 11K1. This has not been verified to work on the M3. 
# Adding a serial port (**voids warranty**)
[![][37121]][37122]
[][37123]
Mele M3 UART pads
## Device disassembly
When you remove 2 screws at top corners of the back side, you can simply take off the plastic cover. 
## Locating the UART
The Mele M3 has a 4 pin 2.0 pitch JST-PH connector available for its UART0 port (same as [Mele A1000][37124]). This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. More information is available at [our UART howto][37125]. 
# Pictures
Take some pictures of your device, [ upload them][37126], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Mele-m3-front.jpg][37127]][37089]
  * [![Mele-m3-back.jpg][37128]][37129]
  * [![Mele-m3-rc.jpg][37130]][37131]
  * [![Device buttons 1.jpg][37132]][37133]
  * [![Device buttons 2.jpg][37134]][37135]
  * [![Mele-m3-board-top.jpg][37136]][37137]
  * [![Device board back.jpg][37138]][37139]

# Also known as
  * Mele A100/A20
  * Mele A100 dual core

# See also
  * [Mele M5][37140]
