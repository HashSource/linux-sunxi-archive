# Mele A210
Mele A210  
---  
[![Mele A210 overview.jpg][36772]][36773]  
Manufacturer |  [Mele][36774]  
Dimensions |  99 _mm_ x 99 _mm_ x 28 _mm_  
Release Date |  January 2013   
Website |  Missing product page.   
Specifications   
SoC |  [A10s][36775] @ 1 GHz   
DRAM |  512 MiB DDR3 @ 432 MHz   
NAND |  4 GB   
Power |  DC 5 V @ 2 A   
Features   
Video |  HDMI (Type A - full)   
Audio |  HDMI   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][36776]), 10/100 Mbps Ethernet ([Realtek RTL8201CP][36777])   
Storage |  SD   
USB |  2 x USB 2.0 Host   
Other |  IRDA   
Headers |  UART   
The Mele A210 is a cheap [A10s][36775] based TV puck. 
## Contents
  * [1 Identification][36778]
  * [2 Sunxi support][36779]
    * [2.1 Current status][36780]
    * [2.2 Images][36781]
    * [2.3 HW-Pack][36782]
    * [2.4 BSP][36783]
    * [2.5 Manual build][36784]
  * [3 Tips, Tricks, Caveats][36785]
    * [3.1 FEL mode][36786]
  * [4 Adding a serial port][36787]
    * [4.1 Device disassembly][36788]
    * [4.2 Locating the UART][36789]
  * [5 Pictures][36790]
  * [6 Also known as][36791]
  * [7 See also][36792]
    * [7.1 Manufacturer images][36793]

# Identification
The device has a sticker on the bottom of the exterior where it is clearly marked as _MELE_ and _(Model): A210_. 
The board is marked as:
[code]
    AB10S-G41A-V1.40-0
    WLBM:831-2454140-90
    2012-11-06
[/code]
MELE A200 single core version's board (with a LAN port) has exactly the same mark. 
In android, under Settings->SYSTEM->About device, you will find: 
  * Model Number: Mele HTPC
  * Build Number: Mele HTPC 121219 Version 1.3

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Mele_A210" target.
  * The .fex file can be found in sunxi-boards as [mele_a210.fex][36794]
  * extra Linux kernel patch [[1]][36795] is needed

Everything else is the same as the [manual build howto][36796]. 
# Tips, Tricks, Caveats
## FEL mode
While you could use the UART to trigger [ FEL mode][36797], there is little point in it as you'd probably first need to solder on a port to get USB OTG out of this device. 
# Adding a serial port
[![][36798]][36799]
[][36800]
UART Connector
## Device disassembly
There are four screws underneath the rubber feet at the bottom. Remove them, and your device will open. 
## Locating the UART
The Mele A210 has a 4 pin 2.0 pitch JST-PH connector for its UART. This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. Wire things up according to our [UART howto][36801]. 
# Pictures
  * [![Mele A210 top.jpg][36802]][36803]
  * [![Mele A210 bottom.jpg][36804]][36805]
  * [![Mele A210 front.jpg][36806]][36807]
  * [![Mele A210 back.jpg][36808]][36809]
  * [![Mele A210 internal.jpg][36810]][36811]
  * [![Mele A210 board front.jpg][36812]][36813]
  * [![Mele A210 board back.jpg][36814]][36815]

# Also known as
# See also
## Manufacturer images
