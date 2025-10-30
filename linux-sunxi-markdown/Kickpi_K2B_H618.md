# Kickpi K2B H618
Kickpi K2B H618  
---  
[![Kickpi K2B H618.jpg][29546]][29547]  
Manufacturer |  Kickpi   
Dimensions |  80 _mm_ x 56 _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][29548]  
Specifications   
SoC |  [H618][29549] @ 1.5 Ghz   
DRAM |  1GiB/2GiB/4GiB LPDDR4 @ xxxMHz   
NAND |  8/16/32GB eMMC   
Power |  DC 5V @ 4A   
Features   
Video |  HDMI (full)   
Audio |  3.5mm headphone plug, HDMI   
Network |  WiFi 802.11 b/g/n ([Allwinner AW859A][29550]), 10/100/1000Mbps Ethernet ([Realtek RTL8211F][29551])   
Storage |  µSD, eMMC   
USB |  2 USB2.0 Host, 1 USB2.0 OTG, 1 USB2.0 on header   
Headers |  20 pin header   
This page needs to be properly filled according to the [New Device Howto][29552] and the [New Device Page guide][29553].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][29554]
  * [2 Sunxi support][29555]
    * [2.1 Current status][29556]
    * [2.2 Images][29557]
    * [2.3 Manual build][29558]
      * [2.3.1 Mainline U-Boot][29559]
      * [2.3.2 Mainline Linux Kernel][29560]
  * [3 Tips, Tricks, Caveats][29561]
    * [3.1 FEL mode][29562]
    * [3.2 Device specific topic][29563]
    * [3.3 ...][29564]
  * [4 Adding a serial port][29565]
  * [5 Pictures][29566]
  * [6 Schematic][29567]
  * [7 Also known as][29568]
  * [8 See also][29569]
    * [8.1 Manufacturer images][29570]

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
Not currently supported due to DT missing, but schematic available. 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][29569]. If no sunxi based images are available, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][29571] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Mainline Linux Kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][29572]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port
[![Kickpi K2B H618 pinout.png.png][29573]][29574]
# Pictures
Take some pictures of your device, [ upload them][29575], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][29576]][29577]
  * [![Device back.jpg][29578]][29579]
  * [![Device buttons 1.jpg][29580]][29581]
  * [![Device buttons 2.jpg][29582]][29583]
  * [![Device board front.jpg][29584]][29585]
  * [![Device board back.jpg][29586]][29587]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
  * <https://e.tb.cn/h.6TH0uupCMWTWcLx?tk=dTB9eA7olv5> / <https://www.cssbuy.com/item-856255894386.html>

## Manufacturer images
Optional. Add non-sunxi images in this section.
