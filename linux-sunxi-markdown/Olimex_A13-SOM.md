# Olimex A13-SOM
Olimex A13-SOM  
---  
[![Olimex a13 som front.jpg][40639]][40640]  
Manufacturer |  [Olimex][40641]  
Dimensions |  61 _mm_ x 32 _mm_ x 9.8 _mm_  
Release Date |  June 2014   
Website |  [Olimex A13 SOM][40642]  
Specifications   
SoC |  [A13][40643] @ 1Ghz   
DRAM |  256MiB / 512MiB DDR3 @ 408 MHz   
NAND |  4GB (optional)   
Power |  DC 5V @ 2A   
Features   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CU][40644])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Headers |  UART, LCD, GPIO   
Olimex A13-SOM is an [A13][40643] based, very small System on Module from the friendly company [Olimex][40645]. Two versions are available, one with 256 MB and one with 512 MB RAM. 
## Contents
  * [1 Identification][40646]
  * [2 Sunxi support][40647]
    * [2.1 Current status][40648]
    * [2.2 Manual build][40649]
    * [2.3 Mainline U-Boot][40650]
    * [2.4 Mainline kernel][40651]
    * [2.5 FEL mode][40652]
  * [3 Adding a serial port][40653]
    * [3.1 Locating the UART][40654]
  * [4 Pictures][40655]
  * [5 Also known as][40656]
  * [6 See also][40657]

# Identification
The name "A13-SOM" is printed on left border of the board (side with sdcard slot). 
# Sunxi support
## Current status
Supported by sunxi kernel 3.4 and sunxi U-Boot. 
## Manual build
  * For building u-boot, use the _OLIMEX-A13-SOM_ target.
  * The .fex file can be found in sunxi-boards as [olimex_a13_som.fex][40658]

Everything else is the same as the [manual build howto][40659]. 
## Mainline U-Boot
No mainline U-Boot support available. 
## Mainline kernel
Generic A13 support available, but no Device Tree file for the A13-SOM 
## FEL mode
The UBOOT/HOME button triggers [ FEL mode][40660]. 
# Adding a serial port
[![][40661]][40662]
[][40663]
UART connector
The UART Header is easy accessable. 
## Locating the UART
The UART connector is labeled just connect wires according to [UART howto][40664]. 
# Pictures
  * [![Olimex a13 som front.jpg][40665]][40640]
  * [![Olimex a13 som back.jpg][40666]][40667]
  * [![Olimex a13 som wifi front.jpg][40668]][40669]
  * [![Olimex a13 som wifi back.jpg][40670]][40671]

# Also known as
No rebadged devices. 
# See also
  * [Our local Olimex page][40645] showing all other Olimex products.
  * [Users Manual][40672]
  * [Schematics and various docs][40673]
