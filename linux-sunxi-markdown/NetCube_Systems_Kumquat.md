# NetCube Systems Kumquat
NetCube Systems Kumquat  
---  
[![Kumquat front.png][39332]][39333]  
Manufacturer |  [NetCube Systems Austria][39334]  
Dimensions |  106 _mm_ x 86 _mm_ x 43 _mm_  
Release Date |  May 2024   
Website |  [Device Product Page][39335]  
Specifications   
SoC |  [V3s][39336] @ 1.2Ghz   
DRAM |  64MB DDR2 @ 400MHz   
Power |  DC 12/24V @ 3A   
Features   
Audio |  3.5mm stereo output plug, 3.5mm microphone plug   
Network |  WiFi 802.11 b/g/n ([Espressif ESP32][39337]), 10/100Mbps Ethernet   
Storage |  µSD/eMMC, on-board SPI NOR Flash   
USB |  1 USB2.0 Type-C OTG   
Other |  CAN-FD Controller, EEPROM   
Headers |  SDIO, I2C, RTC-Backup   
## Contents
  * [1 Identification][39338]
  * [2 Sunxi support][39339]
    * [2.1 Current status][39340]
    * [2.2 Manual build][39341]
      * [2.2.1 U-Boot][39342]
        * [2.2.1.1 Mainline U-Boot][39343]
      * [2.2.2 Linux Kernel][39344]
        * [2.2.2.1 Mainline kernel][39345]
  * [3 Tips, Tricks, Caveats][39346]
    * [3.1 FEL mode][39347]
  * [4 Adding a serial port][39348]
  * [5 Pictures][39349]
  * [6 See also][39350]
    * [6.1 Manufacturer images][39351]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Kumquat Embedded
    (C) 2024 NetCube Systems Austria
[/code]
# Sunxi support
## Current status
Supported. 
  * Mainline kernel patches posted to linux-sunxi mailing list 2025-01-02
  * Mainline u-boot patches posted to u-boot mailing list 2025-06-07

## Manual build
You can build things for yourself by following our [ Manual build howto][39352] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _sun8i_v3s_netcube_kumquat_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _sun8i-v3s-netcube-kumquat.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
If not eMMC or SD-Card is connected, shorting pins 4 and 6 on the SPI-NOR chip triggers [ FEL mode][39353]. 
# Adding a serial port
[![][39354]][39355]
[][39356]
Console connector
There is a secondary USB-C connector located on the right half of the device,  
connected to an CH340 USB-Serial converted which is then connected to UART0.  
Connect a USB cable to it and your computer and then the UART can be access as described in [UART howto][39357]. 
# Pictures
  * [![Kumquat complete.jpg][39358]][39359]
  * [![Kuqmuat used.jpg][39360]][39361]
  * [![Kumquat front.png][39362]][39333]

# See also
  * [ReadTheDocs][39363]
  * [Kumquat on Tindie][39335]
  * [Kumquat Buildroot Git][39364]
  * [Alpine Linux Git][39365]

## Manufacturer images
  * [Buildroot Image][39366]
  * [Alpine Linux Image][39367]
