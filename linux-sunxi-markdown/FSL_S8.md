# FSL S8
FSL S8  
---  
[![Device front.jpg][19159]][19160]  
Manufacturer |  [FSL][19161]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [[1]][19162]  
Specifications   
SoC |  [A31S][19163] @ 1.2Ghz   
DRAM |  512MiB/1GiB DDR3 @ xxxMHz   
NAND |  8/16GB   
Power |  DC 5V @ 2A, 4000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (8" 4:3)   
Touchscreen |  5-finger capacitive (TODO: [Manufacturer device][19164])   
Video |  HDMI (Type A/B/C - full/mini/micro)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (TODO: [Realtek device, USB Id: 0bda:8179][19165])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer (TODO: [manufacturer device][19166])   
This page needs to be properly filled according to the [New Device Howto][19167] and the [New Device Page guide][19168].
## Contents
  * [1 Identification][19169]
  * [2 Sunxi support][19170]
    * [2.1 Current status][19171]
    * [2.2 Images][19172]
    * [2.3 HW-Pack][19173]
    * [2.4 BSP][19174]
    * [2.5 Manual build][19175]
    * [2.6 Mainline U-Boot][19176]
    * [2.7 Mainline kernel][19177]
  * [3 Tips, Tricks, Caveats][19178]
    * [3.1 FEL mode][19179]
    * [3.2 Device specific topic][19180]
    * [3.3 ...][19181]
  * [4 Adding a serial port (**voids warranty**)][19182]
    * [4.1 Device disassembly][19183]
    * [4.2 Locating the UART][19184]
  * [5 Pictures][19185]
  * [6 Also known as][19186]
  * [7 See also][19187]
    * [7.1 Manufacturer images][19188]

# Identification
On the back of the device, the following is printed: 
[code] 
    FSL S8
    Produced by Shenzen FSL Technology Co., Ltd.
    http://www.fslkj.com
[/code]
The PCB has the following silkscreened on it: 
[code] 
    TODO
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _ALFAR8040_
  * Build Number: _fiber_m9-eng 4.2.2 JDQ39 20130722 test-key_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either u-boot or kernel, mention this too, but add the extra sections below.
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][19187]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building u-boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][19189]

Everything else is the same as the [manual build howto][19190]. 
## Mainline U-Boot
If there is mainline u-boot support, add this section.
For [ building mainline u-boot][19191], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][19192]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][19193]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][19194]][19195]
[][19196]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][19197]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][19198].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][19197].
# Pictures
Take some pictures of your device, [ upload them][19199], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][19200]][19160]
  * [![Device back.jpg][19201]][19202]
  * [![Device buttons 1.jpg][19203]][19204]
  * [![Device buttons 2.jpg][19205]][19206]
  * [![Device board front.jpg][19207]][19208]
  * [![Device board back.jpg][19209]][19210]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
