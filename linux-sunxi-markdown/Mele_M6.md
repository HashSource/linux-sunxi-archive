# Mele M6
Mele M6  
---  
[![Mele M6 front.jpg][37277]][37278]  
Manufacturer |  [Mele][37279]  
Website |  [Device Product Page][37280]  
Specifications   
SoC |  [A20][37281]  
DRAM |  512MiB   
NAND |  4GB   
Power |  DC 5V @ 1A   
Features   
Video |  HDMI (Type A - full), Composite A/V   
Audio |  3.5mm headphone plug, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n (Manufacturer Device), 10/100Mbps Ethernet (Realtek RTL8201CP)   
Storage |  SD   
USB |  2 USB2.0 Host   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][37282] and the [New Device Page guide][37283].
The Mele M6 is a heavily reduced version of the [Mele M3][37284] and [Mele M5][37285], with a different motherboard layout, allowing for a more compact design and a cheaper price tag. 
## Contents
  * [1 Identification][37286]
  * [2 Sunxi support][37287]
    * [2.1 Current status][37288]
    * [2.2 Images][37289]
    * [2.3 HW-Pack][37290]
    * [2.4 BSP][37291]
    * [2.5 Manual build][37292]
  * [3 Tips, Tricks, Caveats][37293]
    * [3.1 FEL mode][37294]
    * [3.2 Device specific topic][37295]
    * [3.3 ...][37296]
  * [4 Adding a serial port (**voids warranty**)][37297]
    * [4.1 Device disassembly][37298]
    * [4.2 Locating the UART][37299]
  * [5 Pictures][37300]
  * [6 Also known as][37301]
  * [7 See also][37302]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

# Sunxi support
## Current status
There is no support yet for this device. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][37303]

Everything else is the same as the [manual build howto][37304]. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][37305]. 
## Device specific topic
## ...
# Adding a serial port (**voids warranty**)
[![][37306]][37307]
[][37308]
DEVICE UART pads
## Device disassembly
Three hidden screws can be found under the device. Once the screws are removed, the plastic case can be pried open. 
The board itself is secured by three other screws; the device's LED cover is secured by two extra screws, which do not need to be removed to extract the board. 
## Locating the UART
The Mele has a 4 pin 2.0 pitch JST-PH connector available for its UART0 port, near the SD card slot. This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. More information is available at [our UART howto][37309]. 
# Pictures
  * [![Mele M6 front.jpg][37310]][37278]
  * [![Mele M6 Screws.jpg][37311]][37312]
  * [![Device buttons 1.jpg][37313]][37314]
  * [![Device buttons 2.jpg][37315]][37316]
  * [![Mele M6 Inside.jpg][37317]][37318]
  * [![Mele M6 Board.jpg][37319]][37320]
  * [![Mele M6 Board Back.jpg][37321]][37322]
  * [![Mele M6 UART.jpg][37323]][37324]

# Also known as
There are no known rebadgers for this device. 
# See also
  * [Mele A1000][37325]: The original [A10][37326] based Mele
  * [Mele M5][37285]: Different board, but also based on the A20.
