# Ippo gt90h
Ippo gt90h  
---  
[![Device front.jpg][28060]][28061]  
Manufacturer |  [Manufacturer][28062]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][28063]  
Specifications   
SoC |  [AXX][28064] @ XGhz   
DRAM |  512MiB/1GiB/2GiB DDR3 @ xxxMHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][28065])   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][28066]), 10/100/1000Mbps Ethernet ([Manufacturer device][28067])   
Storage |  µSD, NAND   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][28068]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][28069] and the [New Device Page guide][28070].
  

## Contents
  * [1 Identification][28071]
  * [2 Sunxi support][28072]
    * [2.1 Current status][28073]
    * [2.2 Images][28074]
    * [2.3 HW-Pack][28075]
    * [2.4 BSP][28076]
    * [2.5 Manual build][28077]
      * [2.5.1 U-Boot][28078]
        * [2.5.1.1 Sunxi/Legacy U-Boot][28079]
        * [2.5.1.2 Mainline U-Boot][28080]
      * [2.5.2 Linux Kernel][28081]
        * [2.5.2.1 Sunxi/Legacy Kernel][28082]
        * [2.5.2.2 Mainline kernel][28083]
  * [3 Tips, Tricks, Caveats][28084]
    * [3.1 FEL mode][28085]
    * [3.2 Device specific topic][28086]
    * [3.3 ...][28087]
  * [4 Adding a serial port (**voids warranty**)][28088]
    * [4.1 Device disassembly][28089]
    * [4.2 Locating the UART][28090]
  * [5 Pictures][28091]
  * [6 Schematic][28092]
  * [7 Also known as][28093]
  * [8 See also][28094]
    * [8.1 Manufacturer images][28095]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: none 
The PCB has the following silkscreened on it: 
[code] 
    to_be_done
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][28094]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][28096] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][28097] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][28098]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][28099]][28100]
[][28101]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][28102]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][28103].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][28102].
# Pictures
Take some pictures of your device, [ upload them][28104], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][28105]][28061]
  * [![Device back.jpg][28106]][28107]
  * [![Device buttons 1.jpg][28108]][28109]
  * [![Device buttons 2.jpg][28110]][28111]
  * [![Device board front.jpg][28112]][28113]
  * [![Device board back.jpg][28114]][28115]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
