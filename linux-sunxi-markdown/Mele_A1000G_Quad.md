# Mele M9
(Redirected from [Mele A1000G Quad][36251])
 
Mele M9  
---  
[![IMG 5636 klein.jpg][36254]][36255]  
Manufacturer |  [Mele][36256]  
Dimensions |  175 _mm_ x 120 _mm_ x 45 _mm_  
Release Date |  Month 2013   
Website |  [Device Product Page][36257]  
Specifications   
SoC |  [A31][36258] @ 1Ghz   
DRAM |  2GiB DDR3 @ xxxMHz   
NAND |  16GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI 1.4   
Audio |  3.5mm headphone plug, HDMI, S/PDIF   
Network |  WiFi 802.11 b/g/n (RTL8188EUS), 10/100 Mbps Ethernet ([RealTek RTL8201CP][36259])   
Storage |  SD, on A1000G an USB-to-SATA bridge   
USB |  3 USB2.0 Host, 1 USB2.0 OTG, internal GL850G hub   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][36260] and the [New Device Page guide][36261].
The M9 is an A31 based HTPC which was sold in two versions. Namely, the reduced functionality M9, and the A1000G Quad. The latter has two UART connectors, a very slightly different motherboard layout, and a SATA connector (using a GL830 USB-to-SATA bridge (that is [SAT][36262] capable, therefore querying [S.M.A.R.T.][36263] data and triggering selftests works) 
## Contents
  * [1 Identification][36264]
  * [2 Sunxi support][36265]
    * [2.1 Current status][36266]
    * [2.2 Images][36267]
    * [2.3 HW-Pack][36268]
    * [2.4 BSP][36269]
    * [2.5 Manual build][36270]
    * [2.6 Mainline kernel][36271]
  * [3 Tips, Tricks, Caveats][36272]
    * [3.1 FEL mode][36273]
    * [3.2 Device disassembly][36274]
    * [3.3 Connecting a SATA disk][36275]
    * [3.4 Locating the UART][36276]
  * [4 Pictures][36277]
  * [5 Also known as][36278]
  * [6 See also][36279]
    * [6.1 Manufacturer images][36280]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

# Sunxi support
## Current status
Like any [A31][36258] device, there is little community interest and little support. 
## Images
  * [M9 V3.4.2 official release][36281]

## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][36282]

Everything else is the same as the [manual build howto][36283]. 
## Mainline kernel
Use the _sun6i-a31-m9.dts_ device-tree file for the [mainline kernel][36284]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][36285]. 
## Device disassembly
The device can be opened easily after removing 4 Phillips screws. 
## Connecting a SATA disk
On the A1000G's mainboard there is a SATA port (connected to a Genesys Logic USB-to-SATA bridge) and a SATA power JST header. They're connected to a standardized SATA data+power connector on the case's top (normally hidden by a closed lid). By opening the lid standard 2.5" disks can be inserted into the slot. The connector is advertised as being compatible to the [SATA Universal Storage Module (USM)][36286] standard. 
## Locating the UART
[![][36287]][36288]
[][36289]
Mele A1000G Quad UART Connector
The Mele has a 4 pin 2.0 pitch JST-PH connector available for its UART0 port. This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. More information is available at [our UART howto][36290]. 
# Pictures
  * Mele M9:

  * [![Mele m9 inside top.jpg][36291]][36292]

  * Mele A1000G Quad:

  * [![IMG 5636.JPG][36293]][36294]
  * [![Mele A1000G quad.jpg][36295]][36296]
  * [![IMG 5644.JPG][36297]][36298]
  * [![IMG 5646.JPG][36299]][36300]

# Also known as
List rebadged devices here.
# See also
  * [Mele I7][36301]: A 1GiB RAM 8GiB ROM HTPC from the same company using the same SOC. Comes in the same case as the Mele A1000G Quad.

  * [A31 enabled u-boot][36302]
  * [A31 enabled upstream kernel][36303]

## Manufacturer images
  * [Firmware for M9 - V3.1.4][36304]
  * [Firmware for A1000G Quad - V3.1.7][36305]
