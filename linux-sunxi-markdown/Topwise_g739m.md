# Topwise g739m
Topwise g739m  
---  
[![Topwise-g739m-0000.jpg][55441]][55442]  
Manufacturer |  [Topwise Communication Co. Ltd.][55443]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][55444]  
Specifications   
SoC |  [A23][55445] @ XGhz   
DRAM |  512MiB/1GiB/2GiB DDR3 @ xxxMHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ 2A, 2100mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  Multi-finger capacitive/resistive ([Manufacturer device][55446])   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][55447]), 10/100/1000Mbps Ethernet ([Manufacturer device][55448])   
Storage |  µSD, SATA   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][55449]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][55450] and the [New Device Page guide][55451].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][55452]
  * [2 Sunxi support][55453]
    * [2.1 Current status][55454]
    * [2.2 Images][55455]
    * [2.3 HW-Pack][55456]
    * [2.4 BSP][55457]
    * [2.5 Manual build][55458]
    * [2.6 Mainline U-Boot][55459]
    * [2.7 Mainline kernel][55460]
  * [3 Tips, Tricks, Caveats][55461]
    * [3.1 FEL mode][55462]
    * [3.2 Device specific topic][55463]
    * [3.3 ...][55464]
  * [4 Adding a serial port (**voids warranty**)][55465]
    * [4.1 Device disassembly][55466]
    * [4.2 Locating the UART][55467]
  * [5 Pictures][55468]
  * [6 Also known as][55469]
  * [7 See also][55470]
    * [7.1 Manufacturer images][55471]

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
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either U-Boot or kernel, mention this too, but add the extra sections below.
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][55470]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][55472]

Everything else is the same as the [manual build howto][55473]. 
## Mainline U-Boot
If there is mainline U-Boot support, add this section.
For [ building mainline U-Boot][55474], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][55475]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][55476]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][55477]][55478]
[][55479]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][55480]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][55481].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][55480].
# Pictures
Take some pictures of your device, [ upload them][55482], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Topwise-g739m-0000.jpg][55483]][55442]
  * [![Topwise-g739m-0001.jpg][55484]][55485]
  * [![Topwise-g739m-0002.jpg][55486]][55487]
  * [![Topwise-g739m-0003.jpg][55488]][55489]
  * [![Topwise-g739m-0004.jpg][55490]][55491]
  * [![Topwise-g739m-0005.jpg][55492]][55493]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
