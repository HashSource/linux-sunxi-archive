# Mele M5
Mele M5  
---  
[![Mele M5 front.jpg][37181]][37182]  
Manufacturer |  [Mele][37183]  
Dimensions |  175 _mm_ x 110 _mm_ x 47 _mm_  
Release Date |  August 2013   
Website |  [Product Catalog][37184]  
Specifications   
SoC |  [A20][37185] @ 1 GHz   
DRAM |  1GiB DDR3 @ 384 MHz   
NAND |  8 GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full), Composite   
Audio |  R/L Cinch, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][37186]), 10/100Mbps Ethernet ([Realtek RTL8201CP][37187])   
Storage |  SD, SATA   
USB |  3 USB 2.0 Host   
Headers |  UART   
The Mele M5 is an [A20][37185] based upgrade to the [Mele A1000][37188] family of set-top-boxes. The Mele M5 shares the same case as the [Mele A1000][37188], but uses the same motherboard as the A3700, however with an [A20][37185] SoC. 
## Contents
  * [1 Identification][37189]
  * [2 Sunxi support][37190]
    * [2.1 Current status][37191]
    * [2.2 Images][37192]
    * [2.3 HW-Pack][37193]
    * [2.4 BSP][37194]
    * [2.5 Manual build][37195]
  * [3 Tips, Tricks, Caveats][37196]
    * [3.1 FEL mode][37197]
  * [4 Adding a serial port][37198]
    * [4.1 Device disassembly][37199]
    * [4.2 Locating the UART][37200]
  * [5 Pictures][37201]
  * [6 Also known as][37202]
  * [7 GPIO][37203]
  * [8 See also][37204]

# Identification
The manufacturer name and model-number are clearly printed on a label on the bottom of the device. 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Mele_M5" target.
  * The .fex file can be found in sunxi-boards as [mele_m5.fex][37205]

Everything else is the same as the [manual build howto][37206]. 
# Tips, Tricks, Caveats
## FEL mode
The Mele A1000 can be put into FEL mode by shorting jumper 11K1. This has not been verified to work on the M5. 
# Adding a serial port
[![][37207]][37208]
[][37209]
Mele M5 UART Connector
## Device disassembly
Trivially unscrew 4 screws. 
## Locating the UART
The Mele has a 4 pin 2.0 pitch JST-PH connector available for its UART0 port. This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. More information is available at [our UART howto][37210]. 
# Pictures
  * [![Mele M5 front.jpg][37211]][37182]
  * [![Mele M5 back.jpg][37212]][37213]
  * [![Mele M5 left side.jpg][37214]][37215]
  * [![Mele M5 right side.jpg][37216]][37217]
  * [![Mele M5 bottom.JPG][37218]][37219]
  * [![Mele M5 case open.jpg][37220]][37221]
  * [![Mele M5 mb top.jpg][37222]][37223]
  * [![Mele M5 mb bottom.jpg][37224]][37225]
  * [![Gpios mele m5 hi res.jpg][37226]][37227]
  * [![Mele M5 gpios bottom hi res.jpg][37228]][37229]

# Also known as
Like the Mele A1000 family, the Mele M5 appears to have two [A20][37185] based siblings: the [Mele M3][37230] and [Mele M6][37231]. 
# GPIO
There are approximately 30 GPIO pins available on the top side 
[![Gpios mele m5 hi res.jpg][37232]][37227]
[][37233]
and at least 4 GPIO pins accessible on the bottom face of the board. 
[![Mele M5 gpios bottom hi res.jpg][37234]][37229]
[][37235]
  
To access to all of them you need to disable some features of the motherboard in the script.bin file. For example to access the pins used for flash memory that is present on the motherboard you must before desolder the flash memory and change the file script.bin properly. 
The following file File: [File:Script.fex.30gpios.pdf][37236] offers access to at least 31 GPIO pins. 
# See also
  * [Mele A1000][37188]: The original [A10][37237] based Mele
  * [Mele A1000G Quad][37238]: A quad-core [A31][37239] based Mele
