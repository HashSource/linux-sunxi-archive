# Mele M9
Mele M9  
---  
[![IMG 5636 klein.jpg][37362]][37363]  
Manufacturer |  [Mele][37364]  
Dimensions |  175 _mm_ x 120 _mm_ x 45 _mm_  
Release Date |  Month 2013   
Website |  [Device Product Page][37365]  
Specifications   
SoC |  [A31][37366] @ 1Ghz   
DRAM |  2GiB DDR3 @ xxxMHz   
NAND |  16GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI 1.4   
Audio |  3.5mm headphone plug, HDMI, S/PDIF   
Network |  WiFi 802.11 b/g/n (RTL8188EUS), 10/100 Mbps Ethernet ([RealTek RTL8201CP][37367])   
Storage |  SD, on A1000G an USB-to-SATA bridge   
USB |  3 USB2.0 Host, 1 USB2.0 OTG, internal GL850G hub   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][37368] and the [New Device Page guide][37369].
The M9 is an A31 based HTPC which was sold in two versions. Namely, the reduced functionality M9, and the A1000G Quad. The latter has two UART connectors, a very slightly different motherboard layout, and a SATA connector (using a GL830 USB-to-SATA bridge (that is [SAT][37370] capable, therefore querying [S.M.A.R.T.][37371] data and triggering selftests works) 
## Contents
  * [1 Identification][37372]
  * [2 Sunxi support][37373]
    * [2.1 Current status][37374]
    * [2.2 Images][37375]
    * [2.3 HW-Pack][37376]
    * [2.4 BSP][37377]
    * [2.5 Manual build][37378]
    * [2.6 Mainline kernel][37379]
  * [3 Tips, Tricks, Caveats][37380]
    * [3.1 FEL mode][37381]
    * [3.2 Device disassembly][37382]
    * [3.3 Connecting a SATA disk][37383]
    * [3.4 Locating the UART][37384]
  * [4 Pictures][37385]
  * [5 Also known as][37386]
  * [6 See also][37387]
    * [6.1 Manufacturer images][37388]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

# Sunxi support
## Current status
Like any [A31][37366] device, there is little community interest and little support. 
## Images
  * [M9 V3.4.2 official release][37389]

## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][37390]

Everything else is the same as the [manual build howto][37391]. 
## Mainline kernel
Use the _sun6i-a31-m9.dts_ device-tree file for the [mainline kernel][37392]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][37393]. 
## Device disassembly
The device can be opened easily after removing 4 Phillips screws. 
## Connecting a SATA disk
On the A1000G's mainboard there is a SATA port (connected to a Genesys Logic USB-to-SATA bridge) and a SATA power JST header. They're connected to a standardized SATA data+power connector on the case's top (normally hidden by a closed lid). By opening the lid standard 2.5" disks can be inserted into the slot. The connector is advertised as being compatible to the [SATA Universal Storage Module (USM)][37394] standard. 
## Locating the UART
[![][37395]][37396]
[][37397]
Mele A1000G Quad UART Connector
The Mele has a 4 pin 2.0 pitch JST-PH connector available for its UART0 port. This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. More information is available at [our UART howto][37398]. 
# Pictures
  * Mele M9:

  * [![Mele m9 inside top.jpg][37399]][37400]

  * Mele A1000G Quad:

  * [![IMG 5636.JPG][37401]][37402]
  * [![Mele A1000G quad.jpg][37403]][37404]
  * [![IMG 5644.JPG][37405]][37406]
  * [![IMG 5646.JPG][37407]][37408]

# Also known as
List rebadged devices here.
# See also
  * [Mele I7][37409]: A 1GiB RAM 8GiB ROM HTPC from the same company using the same SOC. Comes in the same case as the Mele A1000G Quad.

  * [A31 enabled u-boot][37410]
  * [A31 enabled upstream kernel][37411]

## Manufacturer images
  * [Firmware for M9 - V3.1.4][37412]
  * [Firmware for A1000G Quad - V3.1.7][37413]
