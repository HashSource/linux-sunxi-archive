# Databyte.ch a13-som
Databyte.ch a13-som  
---  
[![A13som.PNG][16352]][16353]  
Manufacturer |  [http://databyte.ch][16354]  
Dimensions |  67.6 _mm_ x 38 _mm_ x ~4 _mm_  
Release Date |  01 2020   
Website |  [http://databyte.ch][16354]  
Specifications   
SoC |  [A13][16355] @ 1GHz   
DRAM |  512MiB DDR3 @ 403MHz   
NAND |  none on-board   
Power |  DC 3.3V @ 1A (t.b.d)   
Features   
LCD |  none   
Touchscreen |  touchcontroller through SO-DIMM conenctor   
Video |  yes, on SO-DIMM connector, RGB, LCD   
Audio |  yes, on SO-DIMM connector   
Network |  yes, MII on SO-DIMM connector   
Storage |  µSD on-board   
USB |  yes, on SO-DIMM connector   
Camera |  yes, CSI on SO-DIMM connector   
Other |  Accelerometer ([Manufacturer device][16356]), GPS, IRDA   
Headers |  JTAG (2x5x1.27mm)   
This page needs to be properly filled according to the [New Device Howto][16357] and the [New Device Page guide][16358].
The A13-SOM is yet an other System on Module. Comparable to a RaspberryPi Compute Module and is also partially pin compatible. 
## Contents
  * [1 Identification][16359]
  * [2 Sunxi support][16360]
    * [2.1 Current status][16361]
    * [2.2 Images][16362]
    * [2.3 HW-Pack][16363]
    * [2.4 BSP][16364]
    * [2.5 Manual build][16365]
      * [2.5.1 U-Boot][16366]
        * [2.5.1.1 Mainline U-Boot][16367]
      * [2.5.2 Linux Kernel][16368]
        * [2.5.2.1 Mainline kernel][16369]
  * [3 Tips, Tricks, Caveats][16370]
    * [3.1 FEL mode][16371]
    * [3.2 Device specific topic][16372]
    * [3.3 ...][16373]
  * [4 Adding a serial port (**voids warranty**)][16374]
    * [4.1 Device disassembly][16375]
    * [4.2 Locating the UART][16376]
  * [5 Pictures][16377]
  * [6 Also known as][16378]
  * [7 See also][16379]
    * [7.1 Manufacturer images][16380]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    DATABYTE.CH
    ED1912-011-A
    A13-SOM
[/code]
The PCB has the following silkscreened on it: 
[code] 
    A13-SOM
[/code]
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. Sunxi mainline is fully supported. U-Boot as also linux. 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][16379]. If no sunxi based images are available, this section can be removed.
You can find the latest images here: <http://databyte.ch/A13-SOM>
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][16381] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
All Pins are connected to the 200-Pin header. Read the A13-Manual for further information's about activating the FEL-Mode 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][16382]][16383]
[][16384]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][16385]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][16386].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][16385].
# Pictures
Take some pictures of your device, [ upload them][16387], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][16388]][16389]
  * [![Device back.jpg][16390]][16391]
  * [![Device buttons 1.jpg][16392]][16393]
  * [![Device buttons 2.jpg][16394]][16395]
  * [![Device board front.jpg][16396]][16397]
  * [![Device board back.jpg][16398]][16399]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
