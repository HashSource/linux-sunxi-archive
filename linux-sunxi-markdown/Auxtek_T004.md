# Auxtek T004
Auxtek T004  
---  
[![Device front.jpg][8066]][8067]  
Manufacturer |  Auxtek (link missing)   
Dimensions |  90 _mm_ x 29 _mm_ x 16 _mm_  
Release Date |  September 2012   
Website |  Missing   
Specifications   
SoC |  [A10s][8068] @ 1Ghz   
DRAM |  512MB DDR3 @ 432MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI   
Audio |  HDMI   
Network |  WiFi 802.11 b/g/n ([Unknown module][8069])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
This page needs to be properly filled according to the [New Device Howto][8070] and the [New Device Page guide][8071].
## Contents
  * [1 Identification][8072]
  * [2 Sunxi support][8073]
    * [2.1 Current status][8074]
    * [2.2 Images][8075]
    * [2.3 HW-Pack][8076]
    * [2.4 BSP][8077]
    * [2.5 Manual build][8078]
    * [2.6 Mainline kernel][8079]
  * [3 Tips, Tricks, Caveats][8080]
    * [3.1 FEL mode][8081]
    * [3.2 Wifi][8082]
    * [3.3 Debugging help][8083]
  * [4 Adding a serial port (**voids warranty**)][8084]
    * [4.1 Device disassembly][8085]
    * [4.2 Locating the UART][8086]
  * [5 Pictures][8087]
  * [6 Also known as][8088]
  * [7 See also][8089]

# Identification
On the back of the board, _XW-MINIPC-I9_ is printed. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: I9
  * Kernel Version 3.0.8+ hzj@Exdroid #9 Thu Dec 13 12:07:24 CST 2012
  * Build Number: elite_evb-eng 4.0.4 IMM76D 20121213 test-keys

# Sunxi support
## Current status
Supported, apart from the unidentified wifi. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Auxtek-T004" target.
  * The .fex file can be found in sunxi-boards as [auxtek-t004.fex][8090]

Everything else is the same as the [manual build howto][8091]. 
## Mainline kernel
Use the _sun5i-a10s-auxtek-t004.dts_ device-tree file for the [mainline kernel][8092]. 
  

# Tips, Tricks, Caveats
## FEL mode
The button marked _uboot_ , right next to the serial port, triggers [ FEL mode][8093]. 
[![][8094]][8095]
[][8096]
Unidentified Wifi module
## Wifi
The wifi chip, marked _W01_ _TOC9002_ _1237_ still is a bit of a puzzler. Perhaps powering the USB bus and then running lsusb will reveal what's in there. 
## Debugging help
For building the kernel set the options: 
  * EARLY_PRINTK enabled
  * SW_DEBUG_UART configured to 0

Pass earlyprintk on your bootargs. 
# Adding a serial port (**voids warranty**)
[![][8097]][8098]
[][8099]
T004 UART pads
## Device disassembly
With a [plastic tool][8100] it is very easy to remove the top lid How exactly?. 
## Locating the UART
There are two pads between the SoC and the u-boot button. Just solder on some wires according to our [UART howto][8101]. 
# Pictures
  * [![Device front.jpg][8102]][8067]
  * [![Device back.jpg][8103]][8104]
  * [![Device buttons 1.jpg][8105]][8106]
  * [![Device buttons 2.jpg][8107]][8108]
  * [![Auxtek t004 - board back.jpg][8109]][8110]
  * [![Auxtek t004 - board front.jpg][8111]][8112]
  * [![Auxtek t004 - cover back.jpg][8113]][8114]
  * [![Auxtek t004 - cover front.jpg][8115]][8116]

# Also known as
# See also
