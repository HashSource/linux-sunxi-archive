# MangoPi MQ-Quad
MangoPi MQ-Quad  
---  
[![MangoPi MQ Quad Top.jpeg][34974]][34975]  
Manufacturer |  [MangoPi][34976]  
Dimensions |  65 _mm_ x 30 _mm_  
Release Date |  August 2022   
Website |  [Home Page][34977]  
Specifications   
SoC |  [H616][34978] @ 1.5Ghz   
DRAM |  1GiB DDR3L   
Power |  DC 5V @ 2A (via OTG Type-C connector, GPIO header or pogo pins)   
Features   
Video |  HDMI (Type C - Mini)   
Audio |  HDMI, I2S   
Network |  Trolink TL8723DS Wi-Fi+BT   
Storage |  µSD, optional SPI flash (bottom)   
USB |  1 USB Type-C OTG, 1 USB Type-C USB host   
Other |  RMII/RGMII flex connector   
Headers |  1x 40-pin connector   
This page needs to be properly filled according to the [New Device Howto][34979] and the [New Device Page guide][34980].
MangoPi MQ-Quad is a [H616][34978] based board in the Pi Zero form factor, so it fits in cases made for the Pi Zero. 
It is even pin compatible, allowing for using various gadgets made for Pi Zero boards with it, e.g., [Ethernet / USB HUB HAT][34981]. See the pictures for examples. 
## Contents
  * [1 Identification][34982]
    * [1.1 PCB revisions][34983]
  * [2 Sunxi support][34984]
    * [2.1 Current status][34985]
    * [2.2 Images][34986]
    * [2.3 HW-Pack][34987]
    * [2.4 BSP][34988]
    * [2.5 Manual build][34989]
      * [2.5.1 U-Boot][34990]
        * [2.5.1.1 Sunxi/Legacy U-Boot][34991]
        * [2.5.1.2 Mainline U-Boot][34992]
      * [2.5.2 Linux Kernel][34993]
        * [2.5.2.1 Mainline kernel][34994]
    * [2.6 Locating the UART][34995]
  * [3 Pictures][34996]
  * [4 Schematic][34997]
  * [5 See also][34998]
    * [5.1 Manufacturer images][34999]

# Identification
The PCB has the following silkscreened on the bottom: 
[code] 
    Your tiny-tiny-tiny
    Card Computer
    MangoPi.CC
    20220810 V1.1
[/code]
## PCB revisions
There are several PCB revisions, indicated on the back side of the board. 
Revision | Date | PCB color | Details   
---|---|---|---  
v1.0 | 2022.07.13 | Black | first release   
v1.1 | 2022.08.10 | Black | new audio pad locations   
v1.2 | 2022.09.04 | Black/Pink | FEL/RST pads on front side   
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][34998]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][35000] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
  

## Locating the UART
UART is available via the 40 pin GPIO connector and corresponds to the same pins (6 - GND, 8 - RX, 10 - TX) used on Raspberry Pi Zero. This means that the [Adafruit PiUART][35001], [Solderless Serial to USB adapter for RPi][35002] or similar devices can be used. 
# Pictures
  * [![][35003]][34975]
top view 
  * [![][35004]][35005]
bottom view 
  * [![][35006]][35007]
mounted on WaveShare Ethernet/USB Hub Hat 

# Schematic
  * [V1.1 Schematic][35008]
  * [V1.2 Schematic][35009]
  * [BOM][35010]
  * [CAD][35011]

# See also
[MangoPi_MQ-Pro][35012] \- Similar device from same manufacturer using RISC-V D1 processor. 
## Manufacturer images
See <https://mangopi.org/mqquad>
