# MangoPi R3
MangoPi R3  
---  
[![180px-MangoPi-R3 Top.jpeg][35158]][35159]  
Manufacturer |  [MangoPi][35160]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  August 2021   
Website |  [Product Support Page][35161]  
Specifications   
SoC |  [F1C200s][35162] @ 420Mhz   
DRAM |  64MiB DDR @ 420MHz (SIP)   
NAND |  128MB   
Power |  MicroUSB   
Features   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Headers |  DVP Camera, microphone, amplifier, RGB LCD FPC, SPI, I2C, SDIO   
This page needs to be properly filled according to the [New Device Howto][35163] and the [New Device Page guide][35164].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][35165]
  * [2 Sunxi support][35166]
    * [2.1 Current status][35167]
    * [2.2 Images][35168]
    * [2.3 HW-Pack][35169]
    * [2.4 BSP][35170]
    * [2.5 Manual build][35171]
      * [2.5.1 U-Boot][35172]
        * [2.5.1.1 Mainline U-Boot][35173]
      * [2.5.2 Linux Kernel][35174]
        * [2.5.2.1 Mainline kernel][35175]
  * [3 Tips, Tricks, Caveats][35176]
    * [3.1 FEL mode][35177]
    * [3.2 GPIO][35178]
    * [3.3 Locating the UART][35179]
  * [4 Pictures][35180]
  * [5 Schematic][35181]
  * [6 Also known as][35182]
  * [7 See also][35183]
    * [7.1 Manufacturer images][35184]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    MangoPi-R3 Ver:C
    MANGOPI
    20211031
[/code]
# Sunxi support
## Current status
No sunxi support now 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][35183]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][35185] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The boot button and rst button triggers [ FEL mode][35186]. 
## GPIO
If there are no further device specific topics to add, remove these sections.
## Locating the UART
Serial console is available via the USB Female Micro-B marked TTL. See the [UART howto][35187] for more details. 
# Pictures
Take some pictures of your device, [ upload them][35188], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![MangoPi-R3 Top.jpeg][35189]][35190]
  * [![MangoPi-R3 Bottom.jpeg][35191]][35192]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
[Camera Firmware][35193] [SPI Firmware][35194]
