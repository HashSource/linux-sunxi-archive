# Navon iQ7 2018
Navon iQ7 2018  
---  
[![Navon iQ7 2018 front.jpg][39061]][39062]  
Manufacturer |  [Navon][39063]  
Dimensions |  115 _mm_ x 10 _mm_ x 190 _mm_  
Release Date |  2018   
Specifications   
SoC |  [A64][39064] @ 1.152Ghz   
DRAM |  1GiB LPDDR2 @ 533(?)MHz   
NAND |  8GB   
Power |  microUSB, 2500mAh 3.7V Li-Ion battery   
Features   
LCD |  600x1024 (7" ~17∶10)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][39065])   
Audio |  3.5mm TRRS headphone and microphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8703BS][39066])   
Storage |  µSD   
USB |  1x USB 2.0 OTG   
Camera |  0.3MP (640x480) front (GalaxyCore GC0312), 2MP (1600x1200) rear (GalaxyCore GC2145)   
Other |  Accelerometer ([Manufacturer device][39067]), GPS, IRDA   
Headers |  UART, JTAG, LCD, ...   
This page needs to be properly filled according to the [New Device Howto][39068] and the [New Device Page guide][39069].
## Contents
  * [1 Identification][39070]
  * [2 Sunxi support][39071]
    * [2.1 Current status][39072]
    * [2.2 Images][39073]
    * [2.3 HW-Pack][39074]
    * [2.4 BSP][39075]
    * [2.5 Manual build][39076]
      * [2.5.1 U-Boot][39077]
        * [2.5.1.1 Mainline U-Boot][39078]
      * [2.5.2 Linux Kernel][39079]
        * [2.5.2.1 Mainline kernel][39080]
  * [3 Tips, Tricks, Caveats][39081]
    * [3.1 FEL mode][39082]
  * [4 Adding a serial port (**voids warranty**)][39083]
    * [4.1 Device disassembly][39084]
    * [4.2 Locating the UART][39085]
  * [5 Pictures][39086]
  * [6 Also known as][39087]
  * [7 See also][39088]
    * [7.1 Manufacturer images][39089]

# Identification
On the back of the device, the following is printed: 
[code] 
    Navon
    iQ7 2018
[/code]
The PCB has the following silkscreened on it: 
[code] 
    AL-A64-86VH-V1.0
    22DB_20180730
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _iQ7_2018_
  * Build Number: _Navon_V1.0_20180114_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][39088]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][39090] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
It is possible to enter [FEL mode][39091] using the Volume Down button with [this method][39092] or through the [special SD card image][39093]. 
# Adding a serial port (**voids warranty**)
[![][39094]][39095]
[][39096]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][39097]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
  1. Unscrew the two screws at the top of the device (the side with all the ports and buttons)
  2. Use a [Plastic tool][39098] to unclip the back cover

## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][39097].
# Pictures
  * [![Navon iQ7 2018 front.jpg][39099]][39062]
  * [![Navon iQ7 2018 back.jpg][39100]][39101]
  * [![Navon iQ7 2018 top.jpg][39102]][39103]
  * [![Navon iQ7 2018 back removed.jpg][39104]][39105]
  * [![Navon iQ7 2018 board front.jpeg][39106]][39107]
  * [![Navon iQ7 2018 board back.jpg][39108]][39109]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
