# Users:Danielt3/PandorasBox3
Users:Danielt3/PandorasBox3  
---  
[![Device front.jpg][57630]][57631]  
Manufacturer |  [3A-Game Electronic Technology][57632]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  2015   
Website |  [Device Product Page][57633]  
Specifications   
SoC |  [A13][57634] @ 1Ghz   
DRAM |  256MB DDR3 @ 533MHz   
Power |  DC +5V, DC +12V   
Features   
Video |  VGA output   
Audio |  arcade speakers   
Storage |  µSD   
Other |  JAMMA connector   
Headers |  UART, JAMMA, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][57635] and the [New Device Page guide][57636].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][57637]
  * [2 Sunxi support][57638]
    * [2.1 Current status][57639]
    * [2.2 Images][57640]
    * [2.3 HW-Pack][57641]
    * [2.4 BSP][57642]
    * [2.5 Manual build][57643]
      * [2.5.1 U-Boot][57644]
        * [2.5.1.1 Sunxi/Legacy U-Boot][57645]
        * [2.5.1.2 Mainline U-Boot][57646]
      * [2.5.2 Linux Kernel][57647]
        * [2.5.2.1 Sunxi/Legacy Kernel][57648]
        * [2.5.2.2 Mainline kernel][57649]
  * [3 Tips, Tricks, Caveats][57650]
    * [3.1 FEL mode][57651]
    * [3.2 Device specific topic][57652]
    * [3.3 ...][57653]
  * [4 Adding a serial port (**voids warranty**)][57654]
    * [4.1 Device disassembly][57655]
    * [4.2 Locating the UART][57656]
  * [5 Pictures][57657]
  * [6 Also known as][57658]
  * [7 See also][57659]
    * [7.1 Datasheets][57660]
    * [7.2 Manufacturer images][57661]

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
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][57659]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][57662] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][57663] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][57664]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][57665]][57666]
[][57667]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][57668]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][57669].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][57668].
# Pictures
Here are some pictures of the PCB. 
  * [![PandorasBox3 A13 detail.JPG][57670]][57671]
  * [![PandorasBox3 AudioOutput.JPG][57672]][57673]
  * [![PandorasBox3 PCB overview.jpg][57674]][57675]
  * [![PandorasBox3 PCB overview2.jpg][57676]][57677]
  * [![PandorasBox3 PCB overview3.JPG][57678]][57679]
  * [![PandorasBox3 PowerSupply.jpg][57680]][57681]

# Also known as
List rebadged devices here.
# See also
## Datasheets
  * SK hynix 2GB DDR3 RAM [datasheet][57682]

## Manufacturer images
Optional. Add non-sunxi images in this section.
