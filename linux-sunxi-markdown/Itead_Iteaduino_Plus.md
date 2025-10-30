# Itead Iteaduino Plus
Itead Iteaduino Plus  
---  
[![Iteaduino plus top.jpg][28338]][28339]  
Manufacturer |  [Itead][28340]  
Dimensions |  109.2 _mm_ x 76.2 _mm_ x ? _mm_  
Release Date |  August 2013   
Website |  [Product page][28341]  
Specifications   
SoC |  [A10][28342]/[A20][28343] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz   
Power |  micro-USB   
Features   
Video |  HDMI (Type A - full)   
Audio |  HDMI, 3.5mm headphone plug, 3.5mm microphone plug   
Network |  10/100 Ethernet (Realtek RTL8201CP)   
Storage |  µSD, SATA   
USB |  2x USB2.0 Host, 1x USB2.0 OTG   
Headers |  2 x 2x36pin (2.54mm) headers   
This page needs to be properly filled according to the [New Device Howto][28344] and the [New Device Page guide][28345].
The Iteaduino Plus is an arduino compatible baseboard, which can take [A10][28342] and [A20][28343] "core"-boards. The result is called either an Iteaduino Plus A10 or an Iteaduino Plus A20. 
The baseboard is OSHW ([design files are here][28346]), while the core board has schematics available. Sadly, this board was designed with [Cadence Allegro][28347], which limits these files usefulness. Itead studios [claimed to intend to switch to KiCAD][28348] for future designs, but this does not seem to have happened. 
## Contents
  * [1 Sunxi support][28349]
    * [1.1 Current status][28350]
    * [1.2 Images][28351]
    * [1.3 HW-Pack][28352]
    * [1.4 BSP][28353]
    * [1.5 Manual build][28354]
      * [1.5.1 For the A10 core board][28355]
      * [1.5.2 For the A20 core board][28356]
  * [2 Tips, Tricks, Caveats][28357]
  * [3 Adding a serial port][28358]
  * [4 Pictures][28359]
  * [5 Also known as][28360]
  * [6 See also][28361]

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
### For the A10 core board
  * For building u-boot, use the "Iteaduino_Plus_A10" target.
  * The .fex file can be found in sunxi-boards as [iteaduino_plus_a10.fex][28362]

Everything else is the same as the [manual build howto][28363]. 
### For the A20 core board
  * For building u-boot, use the "Iteaduino_Plus_A20" target.
  * The .fex file can be found in sunxi-boards as [iteaduino_plus_a20.fex][28364]

Everything else is the same as the [manual build howto][28363]. 
# Tips, Tricks, Caveats
There is no button to enter FEL mode on the iTeaduino Core or iTeaduino Plus baseboard. You must short the uBoot pin to ground using a jumper wire to enter FEL mode (pin 102 on the Core, pin 139 on the Plus baseboard). 
# Adding a serial port
[![][28365]][28366]
[][28367]
DEVICE UART pads
There is a nice 2.54mm female pin header under the MicroSD slot, at the bottom side of the board. All you have to do is connect male jumper wires according to our [UART howto][28368]. 
**Do not connect Vcc as that might damage your board.**
# Pictures
  * [![][28369]][28339]
Top view of Iteaduino Plus with Core 
  * [![][28370]][28371]
Top view of Iteaduino Plus without Core 
  * [![][28372]][28373]
Bottom view of Iteaduino Plus 
  * [![][28374]][28375]
Top view of Iteaduino Core 
  * [![][28376]][28377]
Bottom view of Iteaduino Core 

# Also known as
This type of device knows no rebadgers. 
# See also
  * [Itead ibox][28378]: A HTPC based on the A20 core board and a different base board.
  * [Iteaduino Plus base board schematic][28379]
  * [Iteaduino A10 Core schematic][28380]
