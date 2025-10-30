# MXQ-4K
MXQ-4K  
---  
[![MXQ-4K-above.jpg][33520]][33521]  
Manufacturer |  [Manufacturer][33522]  
Dimensions |  118 _mm_ x 118 _mm_ x 26 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][33523]  
Specifications   
SoC |  [H3][33524] @ 1.5 Ghz   
DRAM |  2GiB DDR3 @ 667MHz   
NAND |  16GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A), CVBS   
Audio |  3.5mm headphone plug, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n (XR819), 10/100 Ethernet (H1102NL)   
Storage |  SD   
USB |  4 X USB2.0 Host   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][33525] and the [New Device Page guide][33526].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][33527]
  * [2 Sunxi support][33528]
    * [2.1 Current status][33529]
    * [2.2 Manual build][33530]
      * [2.2.1 U-Boot][33531]
        * [2.2.1.1 Sunxi/Legacy U-Boot][33532]
        * [2.2.1.2 Mainline U-Boot][33533]
      * [2.2.2 Linux Kernel][33534]
        * [2.2.2.1 Sunxi/Legacy Kernel][33535]
        * [2.2.2.2 Mainline kernel][33536]
  * [3 Tips, Tricks, Caveats][33537]
    * [3.1 FEL mode][33538]
  * [4 Adding a serial port (**voids warranty**)][33539]
    * [4.1 Device disassembly][33540]
    * [4.2 Locating the UART][33541]
  * [5 Pictures][33542]
  * [6 Also known as][33543]
  * [7 See also][33544]
    * [7.1 Manufacturer images][33545]

# Identification
"MXQ-4K" logo embossed on top cover of the device. 
The PCB has the following silkscreened on it: 
[code] 
    MXQ_8X4_DDR3_V1.0
    2018-05-09
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _TVBOX_
  * Version: _7.1.2_
  * Kernel Version: _4.4.55 linux@linux-PowerEdge-R730 #1_
  * Build Number: _1.1.4_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Manual build
You can build things for yourself by following our [ Manual build howto][33546] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][33547] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The button on the top of the PCB triggers [ FEL mode][33548] mode (to be confirmed). It is reachable through the CVBS connector. 
# Adding a serial port (**voids warranty**)
[![][33549]][33550]
[][33551]
UART pads
## Device disassembly
To open up the case, remove the rubber feet to expose the screws. 
## Locating the UART
A labelled solder point for the UART can be found between USB-4 and the SPDIF connector. 
# Pictures
  * [![MXQ-4K-front.jpg][33552]][33553]
  * [![MXQ-4K-top.jpg][33554]][33555]
  * [![MXQ-4K-base.jpg][33556]][33557]
  * [![MXQ-4K-back.jpg][33558]][33559]
  * [![MXQ-4K-rightside.jpg][33560]][33561]
  * [![MXQ-4K-pcbtop.jpg][33562]][33563]
  * [![MXQ-4K-pcbbottom.jpg][33564]][33565]
  * [![MXQ-4K-heatsink removed.jpg][33566]][33567]
  * [![MXQ-4K-box.jpg][33568]][33569]

# Also known as
List rebadged devices here.
# See also
  * [MXQ-4K on 'wikidevi'][33570]

## Manufacturer images
Optional. Add non-sunxi images in this section.
