# Olimex A64-OLinuXino
Olimex A64-OLinuXino  
---  
[![Olimex-a64-olinuxino-rev c-id.jpg][41249]][41250]  
Manufacturer |  [Olimex][41251]  
Release Date |  2017-06   
Website |  [Product Page][41252]  
Specifications   
SoC |  [A64][41253] @ 1.2GHz   
DRAM |  1GiB DDR3L @ 672MHz   
NAND |  4GB eMMC (optional)   
Power |  DC 5V (2.1/5.5mm barrel plug, centre positive), 3.7V Li-Po battery   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug, 3.5mm microphone plug   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8732BS][41254])   
Storage |  µSD, optional SPI NOR Flash on board   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Other |  UART, JTAG, battery connector, LCD, UEXT, 1x 40-pin GPIO header drills   
This page needs to be properly filled according to the [New Device Howto][41255] and the [New Device Page guide][41256].
## Contents
  * [1 Identification][41257]
  * [2 Sunxi support][41258]
  * [3 Tips, Tricks, Caveats][41259]
    * [3.1 FEL mode][41260]
    * [3.2 SPI NOR flash][41261]
    * [3.3 Thermal issues][41262]
  * [4 Adding a serial port][41263]
  * [5 Pictures][41264]
  * [6 Variants][41265]
  * [7 See also][41266]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    A64-OLinuXino
    Rev.D (c) 2017
    
[/code]
# Sunxi support
Device is supported by mainline u-boot/linux: 
  * u-boot - use the **a64-olinuxino_defconfig** build target (supported since v2017.09)
  * linux - use the **sun50i-a64-olinuxino{,-emmc}** device-tree binary.

# Tips, Tricks, Caveats
## FEL mode
The board will automatically fallback to [ FEL mode][41267] when there is no SPL header present on neither eMMC nor the SPI NOR flash and when there is no SD card present. 
## SPI NOR flash
The A64 OLinuXino board does have a footprint to solder a SPI NOR flash package on. The W25Q128FVSIG is a 128 Mbit SPI NOR Flash chip that is cheap, easy to source and the correct package for this footprint on the PCB. Soldering it on should be relatively easy. First clean the footprint with solder wick to make it flat. However, the A64 OLinuXino board may already come with a SPI NOR Flash. For instance, one of the sample boards came with an Eon EN25Q64 as shown below: 
[code] 
    => sf probe
    SF: Detected en25q64 with page size 256 Bytes, erase size 4 KiB, total 8 MiB
    
[/code]
When using [apritzel's sunxi64-beta branch][41268] with the [SPI driver patches][41269] applied, it is possible to build a u-boot binary with support for reading/writing/erasing the SPI NOR flash. 
  

## Thermal issues
Device is quite prone to overheating, causing hang/reboot, so in case of CPU-hungry workloads, use at least heatsink. 
# Adding a serial port
[![][41270]][41271]
[][41272]
UART connector (from left to right: TX, RX, GND)
There already is a clearly marked UART0 connector that can be identified by the "DBG_UART1" text next to it. All you have to do is attach some leads according to our [UART howto][41273]. 
# Pictures
  * [![Olimex-a64-olinuxino-rev c-top.jpg][41274]][41275]
  * [![Olimex-a64-olinuxino-rev c-side.jpg][41276]][41277]

# Variants
  * A64-OLinuXino-1G with 1GB RAM, no Flash, no WiFi/BLE
  * A64-OLinuXino-1Ge16GW with 1GB RAM, 16GB eMMC and WiFi/BLE
  * A64-OLinuXino-1Ge4GW with 1GB RAM, 4GB eMMC and WiFi/BLE
  * A64-OLinuXino-1Gs16M with 1GB RAM, 16MB SPI flash, no eMMC or WiFi/BLE
  * A64-OLinuXino-2Ge8G-IND with 2GB RAM, 8GB eMMC with industrial grade components (-40 to +85°C temperature range)

# See also
  * [A64-OLinuXino schematics & CAD files][41278]
