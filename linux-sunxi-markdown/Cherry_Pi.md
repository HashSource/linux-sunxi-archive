# Cherry Pi
Cherry Pi  
---  
[![Cherry Pi.jpg][12616]][12617]  
Manufacturer |  [Manufacturer][12618]  
Dimensions |  50 _mm_ x 20 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][12619]  
Specifications   
SoC |  [H3][12620] @ 1Ghz   
DRAM |  64MiB DDR2 Integrated @ 360MHz   
NAND |  2/4/8/16GB  
Power |  via GPIO pins or USB jack   
Features   
Audio |  none   
Network |  10/100Mbps Ethernet (via USB OTG)   
Storage |  8 GB (SPI NAND)   
USB |  1 USB2.0 OTG   
Camera |  none   
Headers |  13x GPIO pins   
This page needs to be properly filled according to the [New Device Howto][12621] and the [New Device Page guide][12622].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][12623]
  * [2 Sunxi support][12624]
    * [2.1 Current status][12625]
    * [2.2 Images][12626]
    * [2.3 HW-Pack][12627]
    * [2.4 BSP][12628]
    * [2.5 Manual build][12629]
      * [2.5.1 U-Boot][12630]
        * [2.5.1.1 Sunxi/Legacy U-Boot][12631]
        * [2.5.1.2 Mainline U-Boot][12632]
      * [2.5.2 Linux Kernel][12633]
        * [2.5.2.1 Sunxi/Legacy Kernel][12634]
        * [2.5.2.2 Mainline kernel][12635]
  * [3 Tips, Tricks, Caveats][12636]
    * [3.1 FEL mode][12637]
    * [3.2 Device specific topic][12638]
    * [3.3 ...][12639]
  * [4 Adding a serial port (**voids warranty**)][12640]
    * [4.1 Device disassembly][12641]
    * [4.2 Locating the UART][12642]
  * [5 Pictures][12643]
  * [6 Also known as][12644]
  * [7 See also][12645]
    * [7.1 Manufacturer images][12646]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Manufacturer Marketing Name
    ModelNumber
[/code]
The PCB has the following silkscreened on it: 
[code] 
    Cherry v1.0.6
[/code]
[code] 
    SUNXI
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][12645]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][12647] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][12648] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][12649]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][12650]][12651]
[][12652]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][12653]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][12654].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][12653].
# Pictures
Take some pictures of your device, [ upload them][12655], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][12656]][12657]
  * [![Device back.jpg][12658]][12659]
  * [![Device buttons 1.jpg][12660]][12661]
  * [![Device buttons 2.jpg][12662]][12663]
  * [![Device board front.jpg][12664]][12665]
  * [![Device board back.jpg][12666]][12667]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
  * [Bash Bunny][12668]

## Manufacturer images
Optional. Add non-sunxi images in this section.
