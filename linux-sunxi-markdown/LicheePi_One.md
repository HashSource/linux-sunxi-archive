# LicheePi One
LicheePi One  
---  
[![LicheePi One Front.jpg][30890]][30891]  
Manufacturer |  [Zepan][30892]  
Dimensions |  72 _mm_ x 54 _mm_  
Release Date |  Nov. 2016   
Website |  [[1]][30893]  
Specifications   
SoC |  [A13][30894] @ 1.0Ghz   
DRAM |  256MiB/512MiB DDR3 @ 408MHz   
Power |  DC 5V via USB jack, USB OTG power   
Features   
LCD |  optional   
Touchscreen |  optional   
Video |  TV Composite (optional)   
Audio |  3.5mm headphone plug with Mic (default) / TV (optional)   
Network |  WiFi 802.11 b/g/n ([RTL8723BU][30895]) (optional)   
Storage |  µSD * 2   
USB |  1 USB2.0 HOST, 1 USB2.0 OTG   
Camera |  optional   
Headers |  2 Custom GPIO Headers, CSI, RGB LCD   
## Contents
  * [1 Identification][30896]
  * [2 Sunxi support][30897]
    * [2.1 Current status][30898]
    * [2.2 Manual build][30899]
      * [2.2.1 U-Boot][30900]
        * [2.2.1.1 Sunxi/Legacy U-Boot][30901]
        * [2.2.1.2 Mainline U-Boot][30902]
      * [2.2.2 Linux Kernel][30903]
        * [2.2.2.1 Sunxi/Legacy Kernel][30904]
        * [2.2.2.2 Mainline kernel][30905]
  * [3 Tips, Tricks, Caveats][30906]
    * [3.1 FEL mode][30907]
    * [3.2 About the two Micro-USB ports][30908]
  * [4 Adding a serial port][30909]
    * [4.1 Locating the UART][30910]
  * [5 Pictures][30911]
  * [6 See also][30912]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Lichee Pi
[/code]
# Sunxi support
## Current status
Not support, but there's officiallly supported FEX and defconfig for it at the git repo. 
## Manual build
You can build things for yourself by following our [ Manual build howto][30913] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the defconfig [here][30914]
#### Mainline U-Boot
Not supported yet. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [official fex file][30915]. 
#### Mainline kernel
Use the _sun5i-a13-licheepi-one.dtsb_ device-tree tree binary. 
# Tips, Tricks, Caveats
## FEL mode
Just removing all SD Cards triggers FEL mode. 
The HOME key also works as FEL key. 
## About the two Micro-USB ports
The port tagged J5 is the real USB OTG port. 
The port tagged J10 is only a jack for DCIN in the Micro USB form. 
# Adding a serial port
[![][30916]][30917]
[][30918]
UART connection
The picture is the UART connection, with the green cable as the board's TX (cable's RX), white cable as the board's RX (cable's TX), and the black cable as GND. 
The USB2TTL cable used in the picture is the cable described in [Cubieboard/TTL][30919]. 
## Locating the UART
The debugging UART is the UART1, located at the top-right corner, silked with RX and TX. 
GND is available at the bottom-right corner. 
Both needs soldering to work. 
# Pictures
  * [![LicheePi One byZepan.jpg][30920]][30921]

# See also
