# InFocus F1
InFocus F1  
---  
[![Device front.jpg][25817]][25818]  
Manufacturer |  [Manufacturer][25819]  
Dimensions |  267mm x 170mm x 9.7mm   
Release Date |  February 2014   
Website |  [Device Product Page][25820]  
Specifications   
SoC |  [A31][25821] @ 1Ghz   
DRAM |  2GiB DDR3   
NAND |  16GB   
Power |  7000mAh Li-Ion battery, Standard USB charger   
Features   
LCD |  1280x800 (10.1" 8.5":5.3")   
Touchscreen |  2-finger capacitive ([Manufacturer device][25822])   
Video |  Built in display   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][25823])   
Storage |  unknown   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  5MP (2592x1944) front, 2MP (1600x1200) rear   
Other |  Accelerometer ([Manufacturer device][25824]), GPS, gyro   
Headers |  unknown   
This page needs to be properly filled according to the [New Device Howto][25825] and the [New Device Page guide][25826].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][25827]
  * [2 Sunxi support][25828]
    * [2.1 Current status][25829]
    * [2.2 Images][25830]
    * [2.3 HW-Pack][25831]
    * [2.4 BSP][25832]
    * [2.5 Manual build][25833]
      * [2.5.1 U-Boot][25834]
        * [2.5.1.1 Sunxi/Legacy U-Boot][25835]
        * [2.5.1.2 Mainline U-Boot][25836]
      * [2.5.2 Linux Kernel][25837]
        * [2.5.2.1 Sunxi/Legacy Kernel][25838]
        * [2.5.2.2 Mainline kernel][25839]
  * [3 Tips, Tricks, Caveats][25840]
    * [3.1 FEL mode][25841]
    * [3.2 Device specific topic][25842]
    * [3.3 ...][25843]
  * [4 Adding a serial port (**voids warranty**)][25844]
    * [4.1 Device disassembly][25845]
    * [4.2 Locating the UART][25846]
  * [5 Pictures][25847]
  * [6 Also known as][25848]
  * [7 See also][25849]
    * [7.1 Manufacturer images][25850]

# Identification
This tablet is distributed to selected participants of Firefox OS tablet contribution program, it runs Firefox tablet OS (now discontinued). The device is not available in retail. Its codename is flatfish. 
On the back of the device, the following is printed: 
[code] 
    InFocus
[/code]
In Firefox OS Settings -> Device Information the following appears: 
  * Model: Flatfish
  * Build Number: 20150225

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][25849]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][25851] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [infocus_f1_flatfish.fex][25852] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
Hold Volume+ button and pressing Power button for a few seconds triggers [ FEL mode][25853]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][25854]][25855]
[][25856]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][25857]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][25858].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][25857].
# Pictures
Take some pictures of your device, [ upload them][25859], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][25860]][25818]
  * [![Device back.jpg][25861]][25862]
  * [![Device buttons 1.jpg][25863]][25864]
  * [![Device buttons 2.jpg][25865]][25866]
  * [![Device board front.jpg][25867]][25868]
  * [![Device board back.jpg][25869]][25870]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
