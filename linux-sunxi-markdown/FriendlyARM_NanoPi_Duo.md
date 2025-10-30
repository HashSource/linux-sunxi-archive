# FriendlyARM NanoPi Duo
FriendlyARM NanoPi Duo  
---  
[![Device front.jpg][20291]][20292]  
Manufacturer |  [FriendlyARM][20293]  
Dimensions |  25.4 _mm_ x 50 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][20294]  
Specifications   
SoC |  [H2+][20295] @ XGhz   
DRAM |  512MiB/1GiB/2GiB DDR3 @ xxxMHz   
NAND |  optional SPI NOR   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][20296])   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][20297]), 10/100/1000Mbps Ethernet ([Manufacturer device][20298])   
Storage |  µSD, SATA   
USB |  2x USB2.0 pin header, 1x OTG µUSB   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][20299]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][20300] and the [New Device Page guide][20301].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][20302]
  * [2 Sunxi support][20303]
    * [2.1 Current status][20304]
    * [2.2 Images][20305]
    * [2.3 HW-Pack][20306]
    * [2.4 BSP][20307]
    * [2.5 Manual build][20308]
      * [2.5.1 U-Boot][20309]
        * [2.5.1.1 Sunxi/Legacy U-Boot][20310]
        * [2.5.1.2 Mainline U-Boot][20311]
      * [2.5.2 Linux Kernel][20312]
        * [2.5.2.1 Sunxi/Legacy Kernel][20313]
        * [2.5.2.2 Mainline kernel][20314]
  * [3 Tips, Tricks, Caveats][20315]
    * [3.1 FEL mode][20316]
    * [3.2 Device specific topic][20317]
    * [3.3 ...][20318]
  * [4 Adding a serial port (**voids warranty**)][20319]
    * [4.1 Device disassembly][20320]
    * [4.2 Locating the UART][20321]
  * [5 Pictures][20322]
  * [6 Also known as][20323]
  * [7 See also][20324]
    * [7.1 Manufacturer images][20325]

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
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][20324]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][20326] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][20327] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][20328]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][20329]][20330]
[][20331]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][20332]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][20333].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][20332].
# Pictures
Take some pictures of your device, [ upload them][20334], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][20335]][20292]
  * [![Device back.jpg][20336]][20337]
  * [![Device buttons 1.jpg][20338]][20339]
  * [![Device buttons 2.jpg][20340]][20341]
  * [![Device board front.jpg][20342]][20343]
  * [![Device board back.jpg][20344]][20345]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
