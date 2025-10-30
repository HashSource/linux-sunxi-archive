# Pine64-LTS
Pine64-LTS  
---  
[![Pine64-LTS-top.jpg][44352]][44353]  
Manufacturer |  [Pine64][44354]  
Dimensions |  133 _mm_ x 80 _mm_ x 19 _mm_  
Release Date |  Mid 2017   
Website |  [Pine64-LTS Product Page][44355]  
Specifications   
SoC |  [R18][44356] @ 1152 MHz   
DRAM |  2GiB LPDDR3 @ 552 MHz   
NAND |  eMMC module socket   
Power |  DC 5V @ 2A (3.5mm/1.35mm barrel plug), Li-Ion battery connector, header pins   
Features   
Video |  HDMI (Type A - full), DSI LCD connector   
Audio |  3.5mm headphone+mic plug, HDMI, SPDIF on headers   
Network |  optional WiFi module socket ([Realtek 8723BS][44357]), 10/100/1000Mbps Ethernet ([Realtek 8211E][44358])   
Storage |  µSD, 128Mbit (16MiB) SPI flash, optional eMMC module   
USB |  2 X USB2.0 Host   
Other |  2 LEDs, power and reset button   
Headers |  2 x 20 pin RPi2 header, 2 x 17 pin Euler header, 2 x 5 pin EXP header, LCD DSI connector, touchscreen connector, CSI camera connector, RTC battery connector, 3-pin battery connector   
The successor of the original [PineA64+][44359], in the same form factor, but with different DRAM (2GB LPDDR3), 16MiB SPI flash and an eMMC socket. It also replaces the microUSB power-only connector with a barrel plug. As the name LTS suggests, this model is available for a longer period, at least until 2022. The usage of LPDDR3 DRAM makes normal firmware images incompatible with the original Pine64(+). 
## Contents
  * [1 Identification][44360]
  * [2 Sunxi support][44361]
    * [2.1 Current status][44362]
    * [2.2 Images][44363]
    * [2.3 BSP][44364]
    * [2.4 Manual build][44365]
      * [2.4.1 U-Boot][44366]
      * [2.4.2 Linux Kernel][44367]
  * [3 Tips, Tricks, Caveats][44368]
    * [3.1 FEL mode][44369]
    * [3.2 Device specific topic][44370]
  * [4 Serial port / UART][44371]
  * [5 Pictures][44372]
  * [6 See also][44373]
    * [6.1 Manufacturer images][44374]

# Identification
Has the Pine64 pine cone logo on the bottom right corner, also states "PINE64-R18-V1_x" along with a date just under the RPi2 style GPIO header. 
On the back of the device, the following is printed: 
[code] 
    Designed in Silicon Valley, California.
    Built in Silicon Delta, China
[/code]
The PCB has the following silkscreened on it: 
[code] 
    PINE64-R18-V1_1
    2017-08-03
[/code]
(early version) 
# Sunxi support
## Current status
Well supported by mainline U-Boot, Trusted Firmware and the Linux kernel, also FreeBSD. 
## Images
Various ready-to-use images, created by various parties, are provided on the Pine64 [Software Software Release Wiki page][44375]. 
## BSP
A Linux kernel v4.9 based [BSP SDK][44376] was provided by Allwinner. 
## Manual build
You can build things for yourself by following our [ Manual build howto][44377] and by choosing from the configurations available below. 
### U-Boot
Use the _pine64-lts_defconfig_ build target. 
### Linux Kernel
Use the _sun50i-a64-pine64-lts.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The board has no dedicated FEL button. Out of the box with no SD card inserted the board will go into FEL mode. A bootable image on the SPI flash or on the eMMC module will prevent that. An SD card image with a magic FEL image will force FEL mode, regardless of eMMC or SPI flash content. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
# Serial port / UART
[![][44378]][44379]
[][44380]
Pine64 UART pads
The debug UART 0 is exposed both on the 10-pin EXP connector as well as on the 34-pin Euler connector. Refer to the picture on the right to find the pins. The location is the same as on the [ Pine64 board][44381]. 
# Pictures
  * [![Pine64-LTS-top.jpg][44382]][44353]
  * [![EMMC-Pine64-LTS.jpg][44383]][44384]

# See also
[Pine64][44359] predecessor board 
[Official Pine64-LTS wiki page][44385]
## Manufacturer images
[Software Pine64-LTS Software Release Wiki page][44375]
