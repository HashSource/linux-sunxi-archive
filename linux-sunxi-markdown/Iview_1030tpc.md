# Iview 1030tpc
Iview 1030tpc  
---  
[![Iview-1030tpc-front.jpg][28584]][28585]  
Manufacturer |  [Iview][28586]  
Dimensions |  260 _mm_ x 159 _mm_ x 13 _mm_  
Release Date |  April 2013   
Website |  [Product Page][28587]  
Specifications   
SoC |  [A10][28588] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  8 GB   
Power |  DC 5V @ 3A, 6500mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (10" 4:3)   
Touchscreen |  5-Finger capacitive ([Goodix GT828][28589])   
Video |  HDMI (Type C, mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CTV][28590])   
Storage |  µSD   
USB |  1 x USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2MP (1600x1200) rear   
Other |  UART, I2C   
This page needs to be properly filled according to the [New Device Howto][28591] and the [New Device Page guide][28592].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurp.
## Contents
  * [1 Identification][28593]
  * [2 Sunxi support][28594]
    * [2.1 Current status][28595]
    * [2.2 Images][28596]
    * [2.3 HW-Pack][28597]
    * [2.4 BSP][28598]
    * [2.5 Manual build][28599]
    * [2.6 Mainline U-Boot][28600]
    * [2.7 Mainline kernel][28601]
  * [3 Tips, Tricks, Caveats][28602]
    * [3.1 FEL mode][28603]
    * [3.2 Device specific topic][28604]
    * [3.3 ...][28605]
  * [4 Adding a serial port (**voids warranty**)][28606]
    * [4.1 Device disassembly][28607]
    * [4.2 Locating the UART][28608]
  * [5 Pictures][28609]
  * [6 Also known as][28610]
  * [7 See also][28611]
    * [7.1 Manufacturer images][28612]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: 1030TPC
  * Build Number: 1030TPC20130111

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either u-boot or kernel, mention this too, but add the extra sections below.
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][28611]
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here.
## BSP
Add MANUFACTURER DEVICE BSP specifics here.
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][28613]

Everything else is the same as the [manual build howto][28614]. 
## Mainline U-Boot
If there is mainline u-boot support, add this section.
For [ building mainline u-boot][28615], use the "MANUFACTURER_DEVICE" target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the FAMILY-CHIP-DEVICE.dtb device-tree file for the [mainline kernel][28616]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][28617]. 
## Device specific topic
## ...
# Adding a serial port (**voids warranty**)
[![][28618]][28619]
[][28620]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][28621]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][28622].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][28621].
# Pictures
  * [![Iview-1030tpc-front.jpg][28623]][28585]
  * [![Iview-1030tpc-back.jpg][28624]][28625]
  * [![Iview-1030tpc-buttons.jpg][28626]][28627]
  * [![Iview-1030tpc-slots.jpg][28628]][28629]
  * [![Iview-1030tpc-pcb.jpg][28630]][28631]
  * [![Iview-1030tpc-i2c.jpg][28632]][28633]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
