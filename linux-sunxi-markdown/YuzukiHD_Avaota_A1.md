# YuzukiHD Avaota A1
YuzukiHD Avaota A1  
---  
[![Avaota a1 top.jpg][63862]][63863]  
Manufacturer |  [YuzukiHD Open Hardware][63864]  
Dimensions |  100 _mm_ x 75 _mm_ x 24 _mm_  
Release Date |  2024   
Website |  [Device Product Page][63865]  
Specifications   
SoC |  [T527][63866] @ 1.8Ghz   
DRAM |  1GiB/2GiB/4GiB LPDDR4 @ 1200MHz   
NAND |  16/32/64/128 GiB eMMC   
Power |  DC 12V @ 3A   
Features   
LCD |  240x135 (1.14" 16:9)   
Video |  HDMI (Type A - full), DP   
Audio |  3.5mm headphone plug, HDMI   
Network |  WiFi 6 2.4+5GHz ([Manufacturer device][63867]), 2 * 10/100/1000Mbps Ethernet ([Realtek RTL8211F][63868])   
Storage |  µSD, eMMC   
USB |  1 USB2.0 Host, 1 USB2.0 Type-C OTG, 1 USB 3.0 OTG   
Headers |  40pin GPIO, CAN, fan, MIPI-CSI, LCD   
This page needs to be properly filled according to the [New Device Howto][63869] and the [New Device Page guide][63870].
Open Hardware router board with two Gigabit Ethernet interfaces, WiFi 6, one USB 3.0 port and a small LCD screen for status messages. 
## Contents
  * [1 Identification][63871]
  * [2 Sunxi support][63872]
    * [2.1 Current status][63873]
    * [2.2 Manual build][63874]
      * [2.2.1 Mainline U-Boot][63875]
      * [2.2.2 Mainline Linux Kernel][63876]
  * [3 Tips, Tricks, Caveats][63877]
    * [3.1 FEL mode][63878]
    * [3.2 Device specific topic][63879]
    * [3.3 ...][63880]
  * [4 Accessing the serial port][63881]
  * [5 Pictures][63882]
  * [6 Schematic][63883]
  * [7 Also known as][63884]
  * [8 See also][63885]
    * [8.1 Manufacturer images][63886]

# Identification
The PCB features the "Avaota A1" name prominently in the middle, above the Avaota logo. On the underside, on the bottom left corner, close to the Ethernet jacks, it shows the hardware version number. 
The latest version so far is v1.7. 
# Sunxi support
## Current status
Supported for basic headless use cases in mainline Linux and U-Boot, development closely follows the A523/T527 upstreaming progress. USB3.0 and support for the second Ethernet port are work in progress, with patches being on the list already. 
## Manual build
You can build things for yourself by following our [ Manual build howto][63887] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _avaota-a1_defconfig_ build target. Supported since v2025.10-rc1. 
There is also [Syterkit][63888], an Open Source project for an alternative bootloader, using a binary blob to do the critical DRAM initialisation. That could be used to load a mainline U-Boot proper build or Linux kernels directly as well. 
### Mainline Linux Kernel
Basic headless support is working since v6.15, with the DT being merged in v6.16. 
Use the _sun55i-t527-avaota-a1.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The FEL button triggers [ FEL mode][63889]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Accessing the serial port
[![][63890]][63891]
[][63892]
DEVICE UART pads
The boot console is connected to pins on the 40pin GPIO header connector, in the same location as on the Raspberry Pi 2: pin 6 for TX, pin 8 for TX, pin 4 for GND. It's the usual 3.3V TTL level, refer to the [UART howto][63893] for more details. 
# Pictures
  * [![Avaota a1 top.jpg][63894]][63863]
  * [![Avaota a1 bottom.jpg][63895]][63896]
  * [![Avaota a1 bottom flash.jpg][63897]][63898]
  * [![Avaota a1 top chips.jpg][63899]][63900]
  * [![Avaota a1 top edge.jpg][63901]][63902]
  * [![Avaota a1 top connectors.jpg][63903]][63904]

# Schematic
[v1.7 schematics][63905]
[hardware info (gerber, layout, BOM, schematics][63906] for all versions. 
# Also known as
Pine64 also produces and [sells the board][63907], using the original name. 
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Official [AvaotaOS releases][63908], based on the BSP kernel.
