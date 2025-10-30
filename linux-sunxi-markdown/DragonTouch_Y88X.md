# DragonTouch Y88X
DragonTouch Y88X  
---  
[![Front.jpg][17171]][17172]  
Manufacturer |  [TabletExpress][17173]  
Dimensions |  188 _mm_ x 121 _mm_ x 11 _mm_  
Release Date |  Month year  
Website |  [Dragon Touch Y88X][17174]  
Specifications   
SoC |  [A33][17175] @ XGhz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][17176])   
Video |  no video export   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][17177])   
Storage |  no external ports   
USB |  1x USB2.0 Host (microusb port)   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer   
Headers |  none   
This page needs to be properly filled according to the [New Device Howto][17178] and the [New Device Page guide][17179].
The Dragon Touch is a widely available low cost tablet. 
This is the second model in the Dragon Touch tablet line. The previous model is the [Dragon Touch Y88][17180] and it was succeeded by the [Dragon Touch Y88X Plus][17181]. 
## Contents
  * [1 Identification][17182]
  * [2 Sunxi support][17183]
    * [2.1 Current status][17184]
    * [2.2 Images][17185]
    * [2.3 HW-Pack][17186]
    * [2.4 BSP][17187]
    * [2.5 Manual build][17188]
    * [2.6 Mainline U-Boot][17189]
    * [2.7 Mainline kernel][17190]
  * [3 Tips, Tricks, Caveats][17191]
    * [3.1 FEL mode][17192]
    * [3.2 Device specific topic][17193]
    * [3.3 ...][17194]
  * [4 Adding a serial port (**voids warranty**)][17195]
    * [4.1 Device disassembly][17196]
    * [4.2 Locating the UART][17197]
  * [5 Pictures][17198]
  * [6 Also known as][17199]
  * [7 See also][17200]
    * [7.1 Manufacturer images][17201]

# Identification
On the back of the device, the following is printed: 
[code] 
    Dragon Touch
    Y88X
[/code]
The PCB has the following silkscreened on it: 
[code] 
    LIA-BB-V6.66
    1970-01-01
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _Dragon Touch-Y88X_
  * Build Number: _astar_chiphd-eng 4.4.2 KVT49L 20150128 test-keys_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either U-Boot or kernel, mention this too, but add the extra sections below.
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][17200]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][17202]

Everything else is the same as the [manual build howto][17203]. 
## Mainline U-Boot
If there is mainline U-Boot support, add this section.
For [ building mainline U-Boot][17204], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][17205]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
Connect your tablet to a Linux PC using the USB cable. In order to trigger [ FEL mode][17206] first make sure the tablet is completely switched off. You may have to hold down the power button for ~ 10s to make sure it is really off. Then hold down the volume up button and simultaneously press the power button for ~ 5s. While still pressing the volume up button release the power button and press it again 3 times in an interval of ~ 1s. Then release both buttons.  

_lsusb_ will show a line:  

Bus 001 Device 007: ID 1f3a:efe8 Onda (unverified) V972 tablet in flashing mode  

sunxi-fel shows:  

AWUSBFEX soc=00001667(A33) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000  

You may have to add   

SUBSYSTEM=="usb", ATTR{idVendor}=="1f3a", MODE="0666", GROUP="plugdev"  

to /etc/udev/rules/51-android.rules and restart udev in order to allow the sunxi-fel command for normal users 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][17207]][17208]
[][17209]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][17210]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][17211].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][17210].
# Pictures
Take some pictures of your device, [ upload them][17212], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Front.jpg][17213]][17172]
  * [![Back.jpg][17214]][17215]
  * [![Buttons.jpg][17216]][17217]
  * [![Device buttons 2.jpg][17218]][17219]
  * [![Device board front.jpg][17220]][17221]
  * [![Device board back.jpg][17222]][17223]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
  * [Manufacturer firmware links][17224]

## Manufacturer images
Optional. Add non-sunxi images in this section.
