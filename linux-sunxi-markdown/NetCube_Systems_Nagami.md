# NetCube Systems Nagami
NetCube Systems Nagami  
---  
[![Nagami-front.jpg][39404]][39405]  
Manufacturer |  [NetCube Systems Austria][39406]  
Dimensions |  30 _mm_ x 50.96 _mm_ x 4 _mm_  
Release Date |  July 2025   
Website |  [Device Product Page][39407]  
Specifications   
SoC |  [T113-s3][39408] @ 1.2Ghz   
DRAM |  128MB/256MB DDR3   
NAND |  4GB eMMC   
Power |  DC 3.3V @ 1.2A   
Features   
Audio |  I2S, PCM, SPDIF, DMIC   
Network |  WiFi 802.11 b/g/n ([Espressif ESP32][39409]), 10/100Mbps Ethernet ([Microchip LAN8720A][39410])   
Storage |  eMMC   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Other |  EEPROM   
Headers |  UART, JTAG, USB, I2C, CAN, I2S, SPDIF, SDIO, ...   
## Contents
  * [1 Identification][39411]
    * [1.1 Current status][39412]
    * [1.2 Manual build][39413]
      * [1.2.1 U-Boot][39414]
        * [1.2.1.1 Mainline U-Boot][39415]
      * [1.2.2 Linux Kernel][39416]
        * [1.2.2.1 Mainline kernel][39417]
  * [2 Tips, Tricks, Caveats][39418]
    * [2.1 FEL mode][39419]
  * [3 Adding a serial port][39420]
  * [4 Pictures][39421]
  * [5 See also][39422]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Nagami SoM
    (C) 2025 NetCube Systems Austria
[/code]
## Current status
Supported. 
  * Mainline kernel patches posted to linux-sunxi mailing list 2025-06-07
  * Mainline u-boot patches posted to u-boot mailing list 2025-09-14

## Manual build
You can build things for yourself by following our [ Manual build howto][39423] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _netcube_nagami_basic_carrier_defconfig_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _sun8i-t113s-netcube-nagami-basic-carrier.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
On boards with revision b or later [ FEL mode][39424] is disabled in hardware. 
# Adding a serial port
The serial port is brought out on the Card-Edge connector on pins 17 (TX) and 19 (RX)  
The UART can be access as described in [UART howto][39425]. 
# Pictures
  * [![Nagami-front.jpg][39426]][39405]

# See also
  * [ReadTheDocs][39427]
  * [Product Brief][39428]
  * [Datasheet][39429]
  * [Nagami Buildroot Git][39430]
  * [Alpine Linux Git][39431]
