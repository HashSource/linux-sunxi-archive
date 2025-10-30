# Forlinx OKA40i-C
Forlinx OKA40i-C  
---  
[![Oka40i-front.jpg][19682]][19683] [][19684]  
Manufacturer |  [Forlinx][19685]  
Dimensions |  190 _mm_ x 130 _mm_  
Release Date |  2019   
Website |  [OKA40i-C Product Page][19686]  
Specifications   
SoC |  [A40i][19687] @ 1.2Ghz   
DRAM |  1GiB/2GiB DDR3 @ 576MHz   
eMMC |  8GB   
Power |  DC 5V @ 2A, battery   
Features   
Video |  HDMI (Type A - full), TV out, LVDS   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI   
Network |  WiFi 802.11 b/g/n ([RL-UM02WBS-8723BU-V1.2][19688]), 10/100Mbps Ethernet ([Manufacturer device][19689])   
Storage |  µSD, fullsize SD, eMMC, SATA   
USB |  3 x USB2.0 Host (2 via hub, 1 native), 1 x USB2.0 OTG (micro-B)   
Other |  SPI flash, 4G modem slot   
Headers |  countless headers exposing almost every peripheral   
This page needs to be properly filled according to the [New Device Howto][19690] and the [New Device Page guide][19691].
This is a development board built around Forlinx's "automotive" FETA40i-C system-on-module based on the [A40i][19687] chip. 
## Contents
  * [1 Identification][19692]
  * [2 Sunxi support][19693]
    * [2.1 Current status][19694]
    * [2.2 Images][19695]
    * [2.3 Manual build][19696]
      * [2.3.1 U-Boot][19697]
      * [2.3.2 Linux Kernel][19698]
  * [3 Tips, Tricks, Caveats][19699]
    * [3.1 FEL mode][19700]
    * [3.2 Device specific topic][19701]
  * [4 Adding a serial port][19702]
  * [5 Pictures][19703]
  * [6 Also known as][19704]
  * [7 See also][19705]
    * [7.1 Manufacturer images][19706]

# Identification
The SOM has "FETA40i-C" silkscreened on it in the upper left corner; The carrier devboard has "OKA40i-C [version]" near the fullsize SD card slot. 
# Sunxi support
## Current status
Manufacturer-provided images/sources available (kernel 3.10). 
Experimental support with mainline U-Boot. Mainline Linux (Armbian) has been made to run on this board. 
Currently working code available at <https://github.com/flashcactus/u-boot/tree/sunxi-feta40i-config-rb>. 
## Images
Apparently provided by the board/SoM manufacturer to customers only. Contains Allwinner BSP based images, SDKs, schematics and other information, with the usual complete ignorance towards mainline work. 
## Manual build
No mainline support yet. Experiments should start off the other [R40/A40i][19707] boards. DRAM is apparently dual-rank, which is not yet supported by mainline U-Boot (but you can try to make it work anyway if you really want). 
You can build things for yourself by following our [ Manual build howto][19708] and by choosing from the configurations available below. 
### U-Boot
Use the repository at <https://github.com/flashcactus/u-boot/tree/sunxi-feta40i-config-rb>, using the _OKA40i_ build target. 
### Linux Kernel
The mainline kernel runs on this board without any additional modification. For now, compile the _sun8i-r40-OKA40i-C_ device tree from the U-Boot repository listed above. 
# Tips, Tricks, Caveats
  * The full-size SD card slot is bootable; the micro-SD is for storage only.
  * The red DIP switch near the SoM socket changes the BROM boot priority: eMMC is tried first when the switch is in the "On" position, and the SD card first when it is off.

## FEL mode
The "Boot" button next to the reset button triggers [ FEL mode][19709]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
# Adding a serial port
Standard DB9 serial connector gives access to the debug UART. 
# Pictures
  * [![Oka40i-front.jpg][19710]][19683]
  * [![Device back.jpg][19711]][19712]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
