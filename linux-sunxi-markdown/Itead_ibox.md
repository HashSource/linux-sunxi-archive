# Itead ibox
Itead ibox  
---  
[![IBOX.jpg][28418]][28419]  
Manufacturer |  [Itead Studio][28420]  
Dimensions |  95 _mm_ x 145 _mm_ x 27 _mm_  
Release Date |  April 2014   
Website |  [Indiegogo Product Page][28421]  
Specifications   
SoC |  [A20][28422] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz   
NAND |  4GB   
Power |  DC 9V @ 2A   
Features   
Video |  HDMI   
Audio |  HDMI, TOSLINK S/PDIF   
Network |  10/100Mbps Ethernet (Realtek RTL8201CP)   
Storage |  µSD   
USB |  3 USB2.0 Host (GL850G hub), 1 USB2.0 OTG (port 4)   
Headers |  32pin expansion header   
The Itead IBOX is a variation of the [Iteaduino Plus A20][28423]. It uses the same mainboard module, but a different baseboard, and it comes with a nice case as well. 
## Contents
  * [1 Identification][28424]
  * [2 Sunxi support][28425]
    * [2.1 Current status][28426]
    * [2.2 Images][28427]
    * [2.3 Manual build][28428]
      * [2.3.1 U-Boot][28429]
        * [2.3.1.1 Mainline U-Boot][28430]
        * [2.3.1.2 Sunxi/Legacy U-Boot][28431]
      * [2.3.2 Linux Kernel][28432]
        * [2.3.2.1 Sunxi/Legacy Kernel][28433]
        * [2.3.2.2 Mainline Kernel][28434]
  * [3 Tips, Tricks, Caveats][28435]
    * [3.1 FEL mode][28436]
    * [3.2 USB][28437]
    * [3.3 Power][28438]
    * [3.4 LED/IRDA][28439]
    * [3.5 Expansion Header][28440]
  * [4 Serial port][28441]
    * [4.1 Device disassembly][28442]
    * [4.2 Locating the UART][28443]
  * [5 Pictures][28444]
  * [6 Also known as][28445]
  * [7 See also][28446]

# Identification
The IBOX is easily identifiable by the "IBOX" branding on the side, the aluminium case and high-gloss finish on the top of the case. 
# Sunxi support
## Current status
The IBOX is very similar to the [Cubieboard2][28447] and boots most images build for the Cubieboard2 without issues. Images which Itead Studio themselves suggest actually have Cubieboard2 as the board type in u-boot. Thus, support is on-par with the Cubieboard2. 
## Images
Cubieboard2 images will work for this board. Itead lists some images [here][28448]
## Manual build
You can build things for yourself by following our [ Manual build howto][28449] and by choosing from the configurations available below. 
Because this device is highly compatible with the [Cubieboard2][28447], you should also be able to get away with using the [Cubieboard2 manual build instructions][28450]. 
### U-Boot
#### Mainline U-Boot
Use the _Cubieboard2_defconfig_ build target unless _Itead_Ibox_A20_defconfig_ is available. 
#### Sunxi/Legacy U-Boot
Use the _Cubieboard2_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_iteaduino_plus_a20.fex_][28451] file. 
#### Mainline Kernel
Use the _sun7i-a20-itead-ibox.dtb_ device-tree file for the [mainline kernel][28452].file. 
# Tips, Tricks, Caveats
## FEL mode
The **Uboot** button, left of the USB ports, triggers [ FEL mode][28453]. Hold the button in while plugging in power. 
## USB
3 of the 4 USB ports are connected to the outputs of the USB hub IC. However, USB 4 is connected directly to the port and supports USB OTG. Pins 1 and 2 of the expansion header export the same USB OTG port. 
## Power
Power is supplied by an MP2307 switching regulator. Theoretically, you should be able to power this board with 12V (which is more convenient than 9) without issues. The regulator provides a maximum of 3A @ 5V. 
The device will also run if powered over the USB OTG port, which means you can run it from a 5V supply. Be careful as this is not intended operation and there is no protection for over-current, reverse polarity etc. That being said, I've measured a peak draw of about 700-800mA over 5V so a 1A supply should work well. Try this at your own risk - it is a hack. 
## LED/IRDA
The IBOX also has a dual-colour LED (red/green) and in infrared receiver connected to PB4 of the A20. 
## Expansion Header
The 32pin expansion header provides access to 
  * VGA
  * Stereo analogue input/output
  * SATA
  * SPI
  * I2C
  * 4 UARTs (2 dedicated, 2 shared by SPI pins)
  * Duplication of USB port 4
  * Power

# Serial port
[![][28454]][28455]
[][28456]
Ibox UART pins
## Device disassembly
Board can be disassembled by removing the 4 screws on the bottom of the box. It is intended to be a development platform in a consumer package, so they have not made it difficult. 
## Locating the UART
The UART can be found on pins 9 (TX) and 10 (RX) with ground on pin 29 on the expansion header. Read the [UART howto][28457] for more information. 
# Pictures
  * [![IBOX Front.jpg][28458]][28459]
  * [![IBOX Rear.jpg][28460]][28461]
  * [![IBOX Header.jpg][28462]][28463]
  * [![IBOX BaseboardBottom.jpg][28464]][28465]
  * [![IBOX BaseboardTop.jpg][28466]][28467]
  * [![IBOX MainboardTop.jpg][28468]][28469]
  * [![IBOX MainboardBottom.jpg][28470]][28471]

# Also known as
The IBOX shares the core board with the [Iteaduino Plus A20][28472]. 
# See also
  * [Iteaduino Plus A20][28423]: The same mainboard module supplied with a different baseboard.
  * [Source design file of IBOX baseboard][28473]
  * [Schematic of IBOX baseboard][28474]
  * [Schematic of ITEAD A20 CORE][28475]
