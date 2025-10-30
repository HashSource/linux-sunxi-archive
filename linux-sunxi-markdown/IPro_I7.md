# IPro I7
IPro I7  
---  
[![Device front.jpg][24997]][24998]  
Manufacturer |  [IPro (Facebook page)][24999]  
Dimensions |  182 _mm_ x 121 _mm_ x 7 _mm_  
Release Date |  2012   
Website |  [Device announcement (no official page)][25000]  
Specifications   
SoC |  [A10][25001] @ 1GHz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  4GB (Samsung K9GBG08U0A)   
Power |  DC 5V @ 1.5A, xxxmAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Goodix GT811][25002])   
Video |  HDMI (mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][25003])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][25004])   
This page needs to be properly filled according to the [New Device Howto][25005] and the [New Device Page guide][25006].
This device uses the [Q8][25007] casing, but it uses Allwinner [A10][25001] processor instead of [A13][25008]. 
## Contents
  * [1 Identification][25009]
  * [2 Sunxi support][25010]
    * [2.1 Current status][25011]
    * [2.2 Images][25012]
    * [2.3 Manual build][25013]
      * [2.3.1 U-Boot][25014]
        * [2.3.1.1 Sunxi/Legacy U-Boot][25015]
        * [2.3.1.2 Mainline U-Boot][25016]
      * [2.3.2 Linux Kernel][25017]
        * [2.3.2.1 Sunxi/Legacy Kernel][25018]
        * [2.3.2.2 Mainline kernel][25019]
  * [3 Tips, Tricks, Caveats][25020]
    * [3.1 FEL mode][25021]
    * [3.2 Device specific topic][25022]
    * [3.3 ...][25023]
  * [4 Adding a serial port (**voids warranty**)][25024]
    * [4.1 Device disassembly][25025]
    * [4.2 Locating the UART][25026]
  * [5 Pictures][25027]
  * [6 Schematic][25028]
  * [7 Also known as][25029]
  * [8 See also][25030]
    * [8.1 Manufacturer images][25031]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Manufacturer Marketing Name
    ModelNumber
[/code]
The PCB has the following silkscreened on it: 
[code] 
    LIA-BB-V6.66
    1970-01-01
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][25030]. If no sunxi based images are available, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][25032] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][25033] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][25034]. AFAIK, no combination of buttons can trigger FEL. 
Another way is spamming '2' on serial console during BOOT1 startup. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][25035]][25036]
[][25037]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][25038]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
Case is held by plastic tabs all around the border. Back cover can be detached without worry because everything is glued to the back of the LCD. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][25038].
# Pictures
Take some pictures of your device, [ upload them][25039], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][25040]][24998]
  * [![Device back.jpg][25041]][25042]
  * [![Device buttons 1.jpg][25043]][25044]
  * [![Device buttons 2.jpg][25045]][25046]
  * [![Device board front.jpg][25047]][25048]
  * [![Device board back.jpg][25049]][25050]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
