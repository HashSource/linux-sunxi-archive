# Pineriver H25
Pineriver H25  
---  
[![Jesurun Xplus H25 Front.JPG][45027]][45028]  
Manufacturer |  [pineriver][45029]  
Dimensions |  102 _mm_ x 35 _mm_ x 15 _mm_  
Release Date |  December 2012   
Website |  [Device Product Page][45030]  
Specifications   
SoC |  [A10s][45031] @ 1008Mhz   
DRAM |  1GiB DDR3 @ 408MHz   
NAND |  4GB   
Power |  DC 5V @ 0.5A   
Features   
Video |  HDMI (Type A - full)   
Audio |  HDMI   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8189ES][45032])   
Storage |  µSD   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART, JTAG   
This page needs to be properly filled according to the [New Device Howto][45033] and the [New Device Page guide][45034].
## Contents
  * [1 Identification][45035]
  * [2 Sunxi support][45036]
    * [2.1 Current status][45037]
    * [2.2 HW-Pack][45038]
    * [2.3 BSP][45039]
    * [2.4 Manual build][45040]
  * [3 Tips, Tricks, Caveats][45041]
    * [3.1 FEL mode][45042]
  * [4 Adding a serial port (**voids warranty**)][45043]
    * [4.1 Device disassembly][45044]
    * [4.2 Locating the UART][45045]
  * [5 Pictures][45046]
  * [6 Also known as][45047]
  * [7 See also][45048]
    * [7.1 Manufacturer images][45049]

# Identification
The mainboard reads _H25_01_MAIN_V3.0_. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: h25
  * Build Number: elite_h25-eng 4.0.4 IMM76D

# Sunxi support
## Current status
Supported. 
## HW-Pack
Add link so people know what to do with this information. from the BSP using pineriver_h25 
## BSP
Add link so people know what to do with this information. configure the BSP using pineriver_h25 
## Manual build
  * For building u-boot, use the "pineriver_h25" target.
  * The .fex file can be found in sunxi-boards as [pineriver_h25.fex][45050]

Everything else is the same as the [manual build howto][45051]. 
# Tips, Tricks, Caveats
## FEL mode
The reset Where??? button triggers [ FEL mode][45052]. 
# Adding a serial port (**voids warranty**)
[![][45053]][45054]
[][45055]
UART pads
## Device disassembly
The case has 2 screws which should be removed first. Then use your [Plastic tool][45056] to gently push the back cover outwards to pop the remaining clips. 
## Locating the UART
The UART can be found between the A10s and one of the memory chips. There are 2 sets of pads, one with 4 pins, one with 3. The 3 pins is the UART, with RX, TX and GND from left to right, when the A10s text is best readable. See the [UART howto][45057] for more info. 
# Pictures
Add pictures from the sides so people can use that to further identify this device.
  * [![Jesurun Xplus H25 Front.JPG][45058]][45028]
  * [![Jesurun Xplus H25 Back.JPG][45059]][45060]
  * Jesurun Xplus H25 Side1.JPG
  * Jesurun Xplus H25 Side2.JPG
  * [![Pineriver elite-h25 PCB front.JPG][45061]][45062]
  * [![Pineriver elite-h25 PCB back.JPG][45063]][45064]

# Also known as
  * [Mini Xplus H25][45065]
  * Jesurun Xplus H25

# See also
  * [Pineriver H24][45066]: An A10 based HTPC from the same manufacturer.

## Manufacturer images
  * [h25_v1.2_1222.img][45067]
