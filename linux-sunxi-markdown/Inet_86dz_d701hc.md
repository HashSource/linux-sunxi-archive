# Inet 86dz d701hc
Inet 86dz d701hc  
---  
[![Digma optima 7.6-front.png][26383]][26384]  
Manufacturer |  [Digma][26385]  
Dimensions |  193mm x 118.8mm x 10.5mm   
Release Date |  March 2014   
Website |  [Product Page ][26386]  
Specifications   
SoC |  [A23][26387] @ 1Ghz   
DRAM |  512MiB DDR3 @ 552MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" 128:75)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][26388])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (TODO: [Manufacturer device][26389])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front (GC0329), 0.3MP (640x480) rear (GC0308)   
Other |  Accelerometer ([Bosch BMA250][26390])   
This page needs to be properly filled according to the [New Device Howto][26391] and the [New Device Page guide][26392].
This is a dual-camera higher resolution version of the [Inet 86dz d701c][26393]. 
## Contents
  * [1 Identification][26394]
  * [2 Sunxi support][26395]
    * [2.1 Current status][26396]
    * [2.2 Images][26397]
    * [2.3 HW-Pack][26398]
    * [2.4 BSP][26399]
    * [2.5 Manual build][26400]
  * [3 Tips, Tricks, Caveats][26401]
    * [3.1 FEL mode][26402]
    * [3.2 Device specific topic][26403]
    * [3.3 ...][26404]
  * [4 Adding a serial port (**voids warranty**)][26405]
    * [4.1 Device disassembly][26406]
    * [4.2 Locating the UART][26407]
  * [5 Pictures][26408]
  * [6 Also known as][26409]
  * [7 See also][26410]

# Identification
In android, under _Settings_ ->_About Tablet_ : 
  * Kernel Version: 3.4.39 inet_xzy@supperFAE #6 Tue Feb 18 14:16:27 CST 2014
  * Model Number: TT7026MW
  * Build Number: A23_86DZ_D701HC_1402033.20140319

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here.
## BSP
Add MANUFACTURER DEVICE BSP specifics here.
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][26411]

Everything else is the same as the [manual build howto][26412]. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The '+' button triggers [ FEL mode][26413]. 
## Device specific topic
## ...
# Adding a serial port (**voids warranty**)
[![][26414]][26415]
[][26416]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][26417]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][26418].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][26417].
# Pictures
Take some pictures of your device, [ upload them][26419], and add them here.
  * [![Digma optima 7.6-front.png][26420]][26384]
  * [![Digma optima 7.6-back.png][26421]][26422]
  * [![Digma optima 7.6-side.png][26423]][26424]
  * [![Device buttons 2.jpg][26425]][26426]
  * [![Device board front.jpg][26427]][26428]
  * [![Device board back.jpg][26429]][26430]

# Also known as
Digma Optima 7.6 (Android 4.2)  
Digma Optima 7.8 (Android 4.4) 
# See also
  * [Inet 86dz d701c][26393] The same mainboard in a single camera 800x480 7" tablet.
