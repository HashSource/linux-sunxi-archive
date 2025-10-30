# Xunlong Orange Pi Zero2W
Xunlong Orange Pi Zero2W  
---  
[![Opi zero2w.jpg][62847]][62848]  
Manufacturer |  [Xunlong][62849]  
Dimensions |  65 _mm_ x 30 _mm_ x 1.2 _mm_  
Release Date |  September 2023   
Website |  [Device Product Page][62850]  
Specifications   
SoC |  [H618][62851] @ 1.5 GHz   
DRAM |  1GiB/1.5GiB/2GiB/4GiB LPDDR4 @ 792MHz   
Power |  DC 5V @ 2A via USB-C or GPIO   
Features   
Video |  mini HDMI, TV-Out on expansion board   
Audio |  HDMI, line out on expansion board   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][62852]), 10/100Mbps Ethernet (internal PHY) on expansion board   
Storage |  µSD, 16 MiB SPI flash   
USB |  1 x USB2.0 OTG (Type-C), 1 x USB2.0 host (Type-C), 2 x USB2.0 host (Type-A) on expansion board   
Headers |  UART, 40pin GPIO, 24pin expansion port   
This page needs to be properly filled according to the [New Device Howto][62853] and the [New Device Page guide][62854].
Small and minimal development board with the [H618][62851] SoC. There is an optional expansion board, which connects via an FPC connector, and provides two more USB host ports, an 100MBit/s Ethernet jack, an audio out port, buttons and LEDs. 
## Contents
  * [1 Identification][62855]
  * [2 Sunxi support][62856]
    * [2.1 Current status][62857]
    * [2.2 Images][62858]
    * [2.3 Manual build][62859]
      * [2.3.1 Mainline U-Boot][62860]
      * [2.3.2 Mainline Linux Kernel][62861]
  * [3 Tips, Tricks, Caveats][62862]
    * [3.1 FEL mode][62863]
    * [3.2 Expansion board][62864]
  * [4 Adding a serial port][62865]
  * [5 Pictures][62866]
  * [6 Schematic][62867]
  * [7 See also][62868]
    * [7.1 Manufacturer images][62869]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange pi
    ZERO 2W V1.1.1
[/code]
# Sunxi support
## Current status
DT in kernel tree since Linux v6.8. The expansion board overlay is still missing, and the 100 Mbit/s Ethernet port relies on the still missing internal PHY support. 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][62868]. If no sunxi based images are available, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][62870] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _orangepi_zero2w_defconfig_ build target. 
### Mainline Linux Kernel
Use the _sun50i-h618-orangepi-zero2w.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
There is no FEL button, and out of the box there is some bootable image on the SPI flash, which prevents [ FEL mode][62871] when booting without an SD card. 
You can either disable SPI booting by overwriting the first few bytes of the SPI flash, or boot from an SD card with fel-sdboot.sunxi on it. 
## Expansion board
# Adding a serial port
[![][62872]][62873]
[][62874]
DEVICE UART pads
There are no dedicated [UART][62875] pins, but UART0 is connected to the GPIO header pins, at the same location as on Raspberry Pi boards (pins 8 & 10). 
# Pictures
  * [![Opi zero2w top.jpg][62876]][62877]
  * [![Opi zero2w bottom.jpg][62878]][62879]
  * [![Opi zero2w.jpg][62880]][62848]

# Schematic
List schematics, board layout, cad files, etc here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
