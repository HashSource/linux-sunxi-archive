# CherryPi PC V3S
CherryPi PC V3S  
---  
[![CherryPi PC V3S Top.jpeg][12473]][12474]  
Manufacturer |  [Shenzhen LC Technology][12475]  
Dimensions |  85 _mm_ x 56 _mm_  
Release Date |  January 2021   
Website |  [LcTech Pi V3s Product Page][12476]  
Specifications   
SoC |  [V3s][12477] @ 1.2Ghz   
DRAM |  64MiB DDR2 Integrated @ 360MHz   
NAND |  128MB   
Power |  via 5V Type-C USB or via 5V microB OTG   
Features   
LCD |  optional   
Audio |  3.5mm headphone plug, on-board microphone   
Network |  WiFi 802.11 b/g/n ([Espressif ESP8089][12478]), 10/100 Ethernet   
Storage |  µSD   
USB |  1x USB2.0 OTG   
Camera |  MIPI CSI   
Headers |  16-pin GPIO   
This page needs to be properly filled according to the [New Device Howto][12479] and the [New Device Page guide][12480].
## Contents
  * [1 Identification][12481]
  * [2 Sunxi support][12482]
    * [2.1 Current status][12483]
    * [2.2 Images][12484]
    * [2.3 HW-Pack][12485]
    * [2.4 BSP][12486]
    * [2.5 Manual build][12487]
      * [2.5.1 U-Boot][12488]
        * [2.5.1.1 Sunxi/Legacy U-Boot][12489]
        * [2.5.1.2 Mainline U-Boot][12490]
      * [2.5.2 Linux Kernel][12491]
        * [2.5.2.1 Sunxi/Legacy Kernel][12492]
        * [2.5.2.2 Mainline kernel][12493]
  * [3 Tips, Tricks, Caveats][12494]
    * [3.1 FEL mode][12495]
    * [3.2 Device specific topic][12496]
    * [3.3 ...][12497]
    * [3.4 Locating the UART][12498]
  * [4 Pictures][12499]
  * [5 Schematic][12500]
  * [6 Also known as][12501]
  * [7 See also][12502]
    * [7.1 Manufacturer images][12503]

# Identification
CherryPi PC V3s is a development board by Shenzhen LC Technology Co., Ltd. based on Allwinner V3s with a standard Raspberry Pi 3/4 board size. At some point name was changed to Lctech Pi V3s 
The PCB has the following silkscreened on the bottom: 
[code] 
    CherryPi-PC_V3S_V1.2
    www.lctech-inc.com
[/code]
  

In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][12502]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][12504] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][12505] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][12506]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][12507].
# Pictures
  * [![CherryPi PC V3S Top.jpeg][12508]][12474]
  * [![CherryPi PC V3S Bottom.jpeg][12509]][12510]

# Schematic
[CherryPi-PC-V3S_V1.1.pdf][12511]
# Also known as
Lctech Pi H3 V7 
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
