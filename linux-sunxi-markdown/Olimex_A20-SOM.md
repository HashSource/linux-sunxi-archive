# Olimex A20-SOM
Olimex A20-SOM  
---  
[![A20-SOM-1.JPG][41046]][41047]  
Manufacturer |  [Olimex][41048]  
Dimensions |  85 _mm_ x 54 _mm_ x 5 _mm_  
Release Date |  May 2014   
Website |  [Product page][41049]  
Specifications   
SoC |  [A20][41050] @ 1 Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  4GB (optional)   
Power |  DC 6-16V @ 3A   
Features   
Video |  HDMI (Type A)   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI   
Network |  10/100Mbps Ethernet ([Realtek RTL8201CP][41051])   
Storage |  µSD, SD, SATA   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  2KiB EEPROM   
Headers |  UART, ...   
Olimex A20-SOM is an [A20][41050] based development board from our friends at [Olimex][41052]. 
## Contents
  * [1 Identification][41053]
  * [2 Sunxi support][41054]
    * [2.1 Current status][41055]
    * [2.2 Images][41056]
    * [2.3 HW-Pack][41057]
    * [2.4 BSP][41058]
    * [2.5 Manual build][41059]
  * [3 Tips, Tricks, Caveats][41060]
    * [3.1 FEL mode][41061]
    * [3.2 LCD Modules][41062]
    * [3.3 Expansion Ports][41063]
    * [3.4 LDO3 (Port E / CSI0 Power Supply) Problem][41064]
  * [4 Adding a serial port][41065]
    * [4.1 Pictures][41066]
  * [5 Also known as][41067]
  * [6 See also][41068]

# Identification
The board helpfully reads "A20-SOM". 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _Olimex_A20-SOM_ target.
  * The .fex file can be found in sunxi-boards as [olimex_a20_som_evb.fex][41069]

Everything else is the same as the [manual build howto][41070]. 
# Tips, Tricks, Caveats
## FEL mode
The _Recovery_ button triggers [ FEL mode][41071]. 
## LCD Modules
## Expansion Ports
## LDO3 (Port E / CSI0 Power Supply) Problem
When the A20-SOM is connected to the A20-SOM-EVB base board sold by Olimex and the LDO3 of the AXP209 chip is initially switched off by uboot (which newer uboot versions do by default), **LDO3 should never be re-enabled**. Doing so leads to immediate shut down of the AXP209 resulting in a crash of the board. The reason seems to be too much capacitance on the lines connected to the LDO3 output and non-effective voltage rate control on the AXP209 for LDO3, leading to excessive inrush currents and triggering the overcurrent-protection of the AXP. See this thread on the mailing list for more details: <https://groups.google.com/d/topic/linux-sunxi/EDvEsbHHqQI/discussion>
# Adding a serial port
[![][41072]][41073]
[][41074]
UART connector
A nicely labeled UART connector is available, all you have to do is attach some leads according to our [UART howto][41075]. 
## Pictures
  * [![A20-SOM-1.JPG][41076]][41047]
  * [![A20-SOM-2.JPG][41077]][41078]

# Also known as
This type of device does not get rebadged. 
# See also
  * [Our local Olimex page][41052] showing all other Olimex products.
  * [Original announcement on Olimex's blog.][41079]
  * [Schematics and various docs][41080]
