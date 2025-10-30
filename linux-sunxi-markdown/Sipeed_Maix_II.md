# Sipeed Maix II
Sipeed Maix II  
---  
[![Device front.jpg][50950]][50951]  
Manufacturer |  [Sipeed][50952]  
Dimensions |  48.9 _mm_ x 33.9 _mm_ x 36.1 _mm_ (full Kit)   
Release Date |  January 2021   
Website |  [Device Product Page][50953]  
Specifications   
SoC |  [V831][50954] @ 800Mhz   
DRAM |  64MiB DDR2   
Power |  USB Female (Type-C)   
Features   
LCD |  1.3" 240x240 optional   
Audio |  optional analog electret microphone, optional 8Ω1W speaker   
Network |  WiFi 802.11 b/g/n ([RTL8189FTV][50955])   
Storage |  µSD   
USB |  1x USB (Type-C) OTG   
Camera |  2MP (1080p30) Omnivision SP2305 optional   
Other |  Accelerometer ([MSA301][50956])   
## Contents
  * [1 Identification][50957]
  * [2 Sunxi support][50958]
    * [2.1 Current status][50959]
    * [2.2 Images][50960]
    * [2.3 HW-Pack][50961]
    * [2.4 BSP][50962]
    * [2.5 Manual build][50963]
      * [2.5.1 U-Boot][50964]
        * [2.5.1.1 Sunxi/Legacy U-Boot][50965]
        * [2.5.1.2 Mainline U-Boot][50966]
      * [2.5.2 Linux Kernel][50967]
        * [2.5.2.1 Sunxi/Legacy Kernel][50968]
        * [2.5.2.2 Mainline kernel][50969]
  * [3 Tips, Tricks, Caveats][50970]
    * [3.1 FEL mode][50971]
    * [3.2 Device specific topic][50972]
    * [3.3 ...][50973]
  * [4 Adding a serial port (**voids warranty**)][50974]
    * [4.1 Device disassembly][50975]
    * [4.2 Locating the UART][50976]
  * [5 Pictures][50977]
  * [6 Schematic][50978]
  * [7 Also known as][50979]
  * [8 See also][50980]
    * [8.1 Manufacturer images][50981]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Maix-II Version:3100
[/code]
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][50980]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][50982] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][50983] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][50984]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][50985]][50986]
[][50987]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][50988]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][50989].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][50988].
# Pictures
Take some pictures of your device, [ upload them][50990], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][50991]][50951]
  * [![Device back.jpg][50992]][50993]
  * [![Device buttons 1.jpg][50994]][50995]
  * [![Device buttons 2.jpg][50996]][50997]
  * [![Device board front.jpg][50998]][50999]
  * [![Device board back.jpg][51000]][51001]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
