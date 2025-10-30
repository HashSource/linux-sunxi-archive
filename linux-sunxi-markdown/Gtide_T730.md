# Gtide T730
Gtide T730  
---  
[![Device front.jpg][22283]][22284]  
Manufacturer |  [Manufacturer][22285]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][22286]  
Specifications   
SoC |  [A13][22287] @ 1.008Ghz   
DRAM |  512MiB DDR3 @ 60MHz   
NAND |  4GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][22288])   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][22289]), 10/100/1000Mbps Ethernet ([Manufacturer device][22290])   
Storage |  µSD, SATA   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][22291]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][22292] and the [New Device Page guide][22293].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][22294]
  * [2 Sunxi support][22295]
    * [2.1 Current status][22296]
    * [2.2 Images][22297]
    * [2.3 HW-Pack][22298]
    * [2.4 BSP][22299]
    * [2.5 Manual build][22300]
      * [2.5.1 U-Boot][22301]
        * [2.5.1.1 Sunxi/Legacy U-Boot][22302]
        * [2.5.1.2 Mainline U-Boot][22303]
      * [2.5.2 Linux Kernel][22304]
        * [2.5.2.1 Sunxi/Legacy Kernel][22305]
        * [2.5.2.2 Mainline kernel][22306]
  * [3 Tips, Tricks, Caveats][22307]
    * [3.1 FEL mode][22308]
    * [3.2 Device specific topic][22309]
    * [3.3 ...][22310]
  * [4 Adding a serial port (**voids warranty**)][22311]
    * [4.1 Device disassembly][22312]
    * [4.2 Locating the UART][22313]
  * [5 Pictures][22314]
  * [6 Also known as][22315]
  * [7 See also][22316]
    * [7.1 Manufacturer images][22317]

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
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][22316]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][22318] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][22319] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][22320]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][22321]][22322]
[][22323]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][22324]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][22325].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][22324].
# Pictures
Take some pictures of your device, [ upload them][22326], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][22327]][22284]
  * [![Device back.jpg][22328]][22329]
  * [![Device buttons 1.jpg][22330]][22331]
  * [![Device buttons 2.jpg][22332]][22333]
  * [![Device board front.jpg][22334]][22335]
  * [![Device board back.jpg][22336]][22337]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
