# Langcent h6s
Langcent h6s  
---  
[![H6SB-hd12-a20-front.jpg][30237]][30238]  
Manufacturer |  [Langcent][30239]  
Dimensions |  150 _mm_ x 93 _mm_ x 23 _mm_  
Release Date |  October 2013   
Website |  [H6S product page][30240]  
Specifications   
SoC |  [A20][30241] @ 1Ghz   
DRAM |  512MiB DDR3 @ 360MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A), 3.5mm AV connector   
Audio |  3.5mm AV connector, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][30242]), 10/100Mbps Ethernet ([Realtek RTL8201CP][30243])   
Storage |  SD   
USB |  3 USB2.0 Host   
Headers |  IRDA, UART, JTAG   
This page needs to be properly filled according to the [New Device Howto][30244] and the [New Device Page guide][30245].
## Contents
  * [1 Identification][30246]
  * [2 Sunxi support][30247]
    * [2.1 Current status][30248]
    * [2.2 Images][30249]
    * [2.3 HW-Pack][30250]
    * [2.4 BSP][30251]
    * [2.5 Manual build][30252]
  * [3 Tips, Tricks, Caveats][30253]
    * [3.1 FEL mode][30254]
  * [4 Adding a serial port (**voids warranty**)][30255]
    * [4.1 Device disassembly][30256]
    * [4.2 Locating the UART][30257]
  * [5 Pictures][30258]
  * [6 Also known as][30259]
  * [7 See also][30260]

# Identification
Find out the strings as reported under settings.
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Langcent_H6S_config" target.
  * The .fex file can be found in sunxi-boards as [hd12-a20-v1.fex][30261]

Everything else is the same as the [manual build howto][30262]. 
# Tips, Tricks, Caveats
## FEL mode
VERIFY ME: There is a button between DC-IN and SPDIF connectors that might trigger [ FEL mode][30263].
# Adding a serial port (**voids warranty**)
[![][30264]][30265]
[][30266]
UART and JTAG pads
## Device disassembly
There are no screws, only clips. Just turn the device upside down and push your [plastic tool][30267] between bottom and top cover. 
## Locating the UART
There are RX and TX pads between the flash chip and the SoC. Just solder on some wires according to the [UART howto][30268]. 
# Pictures
  * [![H6SB-hd12-a20-front.jpg][30269]][30238]
  * [![H6SB-hd12-a20-back.jpg][30270]][30271]
  * [![H6SB-hd12-a20-bottom.jpg][30272]][30273]
  * [![H6SB-hd12-a20-pcb-top.jpg][30274]][30275]
  * [![H6SB-hd12-a20-pcb-bottom.jpg][30276]][30277]

# Also known as
# See also
