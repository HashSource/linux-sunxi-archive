# Hipstreet Aurora
Hipstreet Aurora  
---  
[![Device front.jpg][24027]][24028]  
Manufacturer |  [Manufacturer][24029]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][24030]  
Specifications   
SoC |  [AXX][24031] @ XGhz   
DRAM |  512MiB/1GiB/2GiB DDR3 @ xxxMHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][24032])   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][24033]), 10/100/1000Mbps Ethernet ([Manufacturer device][24034])   
Storage |  µSD, SATA   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][24035]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][24036] and the [New Device Page guide][24037].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][24038]
  * [2 Sunxi support][24039]
    * [2.1 Current status][24040]
    * [2.2 Images][24041]
    * [2.3 HW-Pack][24042]
    * [2.4 BSP][24043]
    * [2.5 Manual build][24044]
      * [2.5.1 U-Boot][24045]
        * [2.5.1.1 Sunxi/Legacy U-Boot][24046]
        * [2.5.1.2 Mainline U-Boot][24047]
      * [2.5.2 Linux Kernel][24048]
        * [2.5.2.1 Sunxi/Legacy Kernel][24049]
        * [2.5.2.2 Mainline kernel][24050]
  * [3 Tips, Tricks, Caveats][24051]
    * [3.1 FEL mode][24052]
    * [3.2 Device specific topic][24053]
    * [3.3 ...][24054]
  * [4 Adding a serial port (**voids warranty**)][24055]
    * [4.1 Device disassembly][24056]
    * [4.2 Locating the UART][24057]
  * [5 Pictures][24058]
  * [6 Also known as][24059]
  * [7 See also][24060]
    * [7.1 Manufacturer images][24061]

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
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][24060]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][24062] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][24063] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][24064]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][24065]][24066]
[][24067]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][24068]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][24069].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][24068].
# Pictures
Take some pictures of your device, [ upload them][24070], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][24071]][24028]
  * [![Device back.jpg][24072]][24073]
  * [![Device buttons 1.jpg][24074]][24075]
  * [![Device buttons 2.jpg][24076]][24077]
  * [![Device board front.jpg][24078]][24079]
  * [![Device board back.jpg][24080]][24081]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
