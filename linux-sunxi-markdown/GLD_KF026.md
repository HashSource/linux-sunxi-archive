# GLD KF026
GLD KF026  
---  
[![Kf026 front.JPG][21532]][21533]  
Manufacturer |  Softwinners   
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Specifications   
SoC |  [A13][21534] @ 1.2Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ ?A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (9" 16:9)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][21535] FIXME)   
Audio |  3.5mm headphone/microphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][21536] FIXME)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([manufacturer device][21537] FIXME)   
This page needs to be properly filled according to the [New Device Howto][21538] and the [New Device Page guide][21539].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurp.
## Contents
  * [1 Identification][21540]
  * [2 Sunxi support][21541]
    * [2.1 Current status][21542]
    * [2.2 Images][21543]
    * [2.3 HW-Pack][21544]
    * [2.4 BSP][21545]
    * [2.5 Manual build][21546]
  * [3 Tips, Tricks, Caveats][21547]
    * [3.1 FEL mode][21548]
    * [3.2 Recovery mode][21549]
    * [3.3 Device specific topic][21550]
    * [3.4 ...][21551]
  * [4 Adding a serial port (**voids warranty**)][21552]
    * [4.1 Device disassembly][21553]
    * [4.2 Locating the UART][21554]
  * [5 Pictures][21555]
  * [6 Also known as][21556]
  * [7 See also][21557]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: MID
  * Build Number: GLD-HJDZ_V2.0.6_20130603_40LK_0308-0309-121d_a489_2628a00

Or: 
  * Model Number: Softwinerkf026
  * Build Number: kf026_V2.0.6_20130603_a489_2628a00

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
  * For building u-boot, use the "softwinners_kf026" target.
  * The .fex file can be found in sunxi-boards as [gld_kf026.fex][21558]

Everything else is the same as the [manual build howto][21559]. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The BACK + POWER button triggers [ FEL mode][21560]. 
## Recovery mode
The VOLUP + POWER button triggers recovery mode. 
## Device specific topic
## ...
# Adding a serial port (**voids warranty**)
[![][21561]][21562]
[][21563]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][21564]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
Remove screws from the right side, then pull off the back cover. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][21564].
# Pictures
  * [![Kf026 front.JPG][21565]][21533]
  * [![Kf026 back.JPG][21566]][21567]
  * [![Kf026 buttons top.JPG][21568]][21569]
  * [![Kf026 button right.JPG][21570]][21571]
  * [![Kf026 board front.JPG][21572]][21573]
  * [![Kf026 board back.JPG][21574]][21575]
  * [![Kf026 board back naked.JPG][21576]][21577]

# Also known as
Lingxiu T21 
# See also
Add some nice to have links here. This includes related devices, and external links.
