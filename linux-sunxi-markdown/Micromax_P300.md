# Micromax P300
Micromax P300  
---  
[![Device front.jpg][37940]][37941]  
Manufacturer |  [Micromax][37942]  
Dimensions |  192 _mm_ x 122 _mm_ x 10.50 _mm_  
Release Date |  April 2012   
Website |  [Micromax P300(funbook)][37943]  
Specifications   
SoC |  [A10][37944] @ 1Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ ?A, 2800mAh 4.2V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  X-finger capacitive (TODO: [Manufacturer device][37945])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (Manufacturer device)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([manufacturer device][37946] FIXME)   
Headers |  UART, JTAG  
## Contents
  * [1 Identification][37947]
  * [2 Sunxi support][37948]
    * [2.1 Current status][37949]
    * [2.2 Images][37950]
    * [2.3 HW-Pack][37951]
    * [2.4 BSP][37952]
    * [2.5 Manual build][37953]
  * [3 Tips, Tricks, Caveats][37954]
    * [3.1 FEL mode][37955]
    * [3.2 Device specific topic][37956]
    * [3.3 ...][37957]
  * [4 Adding a serial port (**voids warranty**)][37958]
    * [4.1 Device disassembly][37959]
    * [4.2 Locating the UART][37960]
  * [5 Pictures][37961]
  * [6 Also known as][37962]
  * [7 See also][37963]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: P300(Funbook)
  * Build Number: 97F1-D1-H2-H01-MMX.20120914

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
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][37964]

Everything else is the same as the [manual build howto][37965]. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][37966]. 
## Device specific topic
## ...
# Adding a serial port (**voids warranty**)
[![][37967]][37968]
[][37969]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][37970]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][37971].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][37970].
# Pictures
Take some pictures of your device, [ upload them][37972], and add them here.
  * [![Device front.jpg][37973]][37941]
  * [![Device back.jpg][37974]][37975]
  * [![Device buttons 1.jpg][37976]][37977]
  * [![Device buttons 2.jpg][37978]][37979]
  * [![Device board front.jpg][37980]][37981]
  * [![Device board back.jpg][37982]][37983]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
