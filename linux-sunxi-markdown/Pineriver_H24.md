# Pineriver H24
Pineriver H24  
---  
[![Pineriver h24 front.jpg][44947]][44948]  
Manufacturer |  [Pineriver][44949]  
Dimensions |  60 _mm_ x 60 _mm_ x 13 _mm_  
Release Date |  July 2012   
Website |  [H24 Product page][44950]  
Specifications   
SoC |  [A10][44951] @ 1Ghz   
DRAM |  512MiB/1GiB DDR3 @ 360MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A), Composite (3.5mm AV connector)   
Audio |  HDMI, 3.5mm AV connector   
Network |  WiFi 802.11 b/g/n (Manufacturer device)   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG (full size)   
Other |  IRDA   
The Pineriver H24 was most commonly sold as the Mini-X, and earlier versions came with 512MB RAM while later ones came with 1GB. This version was prone to overheating, and the case was redesigned, and then sold as the Mini XPlus. 
There have been many clones with different internals. Some with also an [A10][44951] inside (sometimes called MK805 or G1-TV), but some come with [A10s][44952] (G1-TV-A10s or [Semitime_g1_a10s][44953]) or [A20][44954]. When these hit our community, they should be documented separately. There's even a Jesurun device called MT Box which has a Rockchip in it. 
There is also a company called Minix. There is no relationship with pineriver and the devices are a different formfactor. 
## Contents
  * [1 Identification][44955]
  * [2 Sunxi support][44956]
    * [2.1 Current status][44957]
    * [2.2 Images][44958]
    * [2.3 HW-Pack][44959]
    * [2.4 BSP][44960]
    * [2.5 Manual build][44961]
      * [2.5.1 512MiB][44962]
      * [2.5.2 1GiB][44963]
    * [2.6 Mainline kernel][44964]
  * [3 Tips, Tricks, Caveats][44965]
    * [3.1 FEL mode][44966]
    * [3.2 AV connector][44967]
  * [4 Adding a serial port (**voids warranty**)][44968]
    * [4.1 Device disassembly][44969]
    * [4.2 Locating the UART][44970]
  * [5 Pictures][44971]
  * [6 Also known as][44972]
  * [7 See also][44973]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: H24
  * Build Number: Add build number

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
### 512MiB
  * For building u-boot, use the "Mini-X" target.
  * The .fex file can be found in sunxi-boards as [mini-x.fex][44974]

Everything else is the same as the [manual build howto][44975]. 
### 1GiB
  * For building u-boot, use the "Mini-X-1Gb" target.
  * The .fex file can be found in sunxi-boards as [mini-x-1gb.fex][44976]

Everything else is the same as the [manual build howto][44975]. 
## Mainline kernel
Use the _sun4i-a10-mini-xplus.dts_ device-tree file for the [mainline kernel][44977]. 
[![][44978]][44979]
[][44980]
AV connector pinout
# Tips, Tricks, Caveats
## FEL mode
Pads for a button are present, but is not populated. You will have to trigger [ FEL mode][44981] through serial. 
## AV connector
You will need a special cable for the AV-connector. 
# Adding a serial port (**voids warranty**)
[![][44982]][44983]
[][44984]
UART pads
## Device disassembly
Remove the two screws at the back, and the board should slide out easily. 
## Locating the UART
There are two pads right next to the SoC, just swap your lines until you have identified RX and TX, as described in the [UART howto][44985]. 
# Pictures
  * Mini-X

  * [![Pineriver h24 front.jpg][44986]][44948]
  * [![Pineriver h24 board front.jpg][44987]][44988]
  * [![Pineriver h24 board back.jpg][44989]][44990]

# Also known as
  * Miniand Mini X
  * Miniand Mini XPlus
  * Jesurun Mini X

# See also
[Pineriver_H25][44991]
