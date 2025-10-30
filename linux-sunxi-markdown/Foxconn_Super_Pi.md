# Foxconn Super Pi
Foxconn Super Pi  
---  
[![Foxconn SuperPI.JPG][19883]][19884]  
Manufacturer |  [Foxconn][19885]  
Dimensions |  91.5 mm x 60 mm   
Release Date |  unknown   
Website |  [Super Pi Product Page(Currently broken)][19886]  
Specifications   
SoC |  [A20][19887] @ 1 GHz   
DRAM |  1 GiB DDR3 @ 432 MHz   
NAND |  no (onboard) NAND available   
Power |  DC 5 V @ 2 A (micro USB)   
Features   
Video |  HDMI (Type A - full), CVBS, LVDS   
Audio |  3.5 mm headphone plug, HDMI, internal microphone   
Network |  10/100/1000 Mbps Ethernet ([Realtek RTL8211E][19888])   
Storage |  SD, SATA (with power connector: JST XH 2.5mm header, providing +5V)   
USB |  2 x USB 2.0 Host, 1 x USB 2.0 OTG   
Other |  IR receiver   
Headers |  2 pin UART, 8 pin UART (including power source), LCD/ LVDS, CSI, 26 pin GPIO   
This page needs to be properly filled according to the [New Device Howto][19889] and the [New Device Page guide][19890].
The Foxconn Super Pi is essentially a Foxconn redesigned [Banana Pi][19891]. The overall design shows clear relationship with the [Banana Pi][19891] but the PCB layout and onboard connector positions are mostly different. 
## Contents
  * [1 Identification][19892]
  * [2 Sunxi support][19893]
    * [2.1 Current status][19894]
    * [2.2 Manual build][19895]
      * [2.2.1 Mainline U-Boot][19896]
      * [2.2.2 Sunxi/Legacy Kernel][19897]
      * [2.2.3 Mainline kernel][19898]
  * [3 Tips, Tricks, Caveats][19899]
    * [3.1 FEL mode][19900]
    * [3.2 Powering the board][19901]
  * [4 Adding a serial port][19902]
    * [4.1 Locating the UART][19903]
  * [5 Pictures][19904]
  * [6 Manufacturer images][19905]
  * [7 See also][19906]

# Identification
The board has "Super Pi REV:1.0" printed between the DSI connector and Ethernet port. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: Super Pi
  * Build Number: abd_super1-eng 4.2.2 10SB 20141122
  * Firmware version: 2.1
  * Kernel Version: 3.4.39+ root@alice-desktop #3 Sat Nov 22 03:20:27 EST 2014

  

# Sunxi support
## Current status
_Patches awaiting inclusion in the sunxi repos._
## Manual build
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][19907] file. 
#### Mainline kernel
Use the _MANUFACTURER_DEVICE_ device-tree file, and follow the [Mainline Kernel Howto][19908]. 
# Tips, Tricks, Caveats
## FEL mode
The _UBOOT_ button, located behind the Ethernet port, triggers [ FEL mode][19909]. 
## Powering the board
This board has severe UART backpower problem. While connected to another computer through a [UART-USB dongle][19910], the current leaked through RXD keeps the board in an slightly "working" state, preventing the board from properly powering up. To normally power cycle the device it is often needed to disconnect RXD temporarily. 
# Adding a serial port
[![][19911]][19912]
[][19913]
Super Pi UART pads
## Locating the UART
The UART pins are located in the upper right corner of the board (connector J11 and J12), and the relative positions among the pins are the same as the [Banana Pi][19891]. Just attach some leads according to our [UART Howto][19914]. 
# Pictures
  * [![Foxconn SuperPI.JPG][19915]][19884]
  * [![Foxconn SuperPI top.JPG][19916]][19917]
  * [![Foxconn SuperPI bot.JPG][19918]][19919]
  * [![Foxconn SuperPI side1.JPG][19920]][19921]
  * [![Foxconn SuperPI side2.JPG][19922]][19923]
  * [![Foxconn SuperPI side3.JPG][19924]][19925]
  * [![Foxconn SuperPI side4.JPG][19926]][19927]

  

# Manufacturer images
  * [Manufacturer provided Android image][19928]

# See also
[LeMaker Banana Pi][19891]
