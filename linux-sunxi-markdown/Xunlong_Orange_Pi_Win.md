# Xunlong Orange Pi Win
Xunlong Orange Pi Win  
---  
[![Device front.jpg][62519]][62520]  
Manufacturer |  [OrangePi][62521]  
Dimensions |  93 _mm_ x 60 _mm_  
Release Date |  March 2017 (Plus version in April 2017)   
Website |  [[1]][62522]  
Specifications   
SoC |  [A64][62523] @ 1.2 GHz   
DRAM |  1GiB/2GiB DDR3L   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive)  
or via µUSB or via Li-battery header pins   
Features   
Video |  HDMI (HDCP, CEC), CVBS   
Audio |  3.5 mm Jack, HDMI, Microphone   
Network |  BT4.0/WiFi 802.11 b/g/n ([Ampak AP6212][62524]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][62525])   
Storage |  µSD, 16Mbit NOR Flash on board   
USB |  4 USB 2.0 Host (shared, internal hub), 1 USB 2.0 OTG   
Other |  [CIR][62526]  
Headers |  3 pin UART, CSI, 40 pin GPIO   
_Orange Pi Win_ and _Orange Pi Win Plus_ are [A64][62523] based development board produced by [Xunlong][62527]. The Win model comes with 1 GiB of RAM and the Win Plus model is bundled with 2 GiB RAM. 
This page needs to be properly filled according to the [New Device Howto][62528] and the [New Device Page guide][62529].
## Contents
  * [1 Identification][62530]
  * [2 Sunxi support][62531]
    * [2.1 Current status][62532]
    * [2.2 Images][62533]
    * [2.3 HW-Pack][62534]
    * [2.4 BSP][62535]
    * [2.5 Manual build][62536]
      * [2.5.1 U-Boot][62537]
        * [2.5.1.1 Sunxi/Legacy U-Boot][62538]
        * [2.5.1.2 Mainline U-Boot][62539]
      * [2.5.2 Linux Kernel][62540]
        * [2.5.2.1 Sunxi/Legacy Kernel][62541]
        * [2.5.2.2 Mainline kernel][62542]
  * [3 Tips, Tricks, Caveats][62543]
    * [3.1 FEL mode][62544]
    * [3.2 Device specific topic][62545]
    * [3.3 Locating the UART][62546]
  * [4 Pictures][62547]
  * [5 Variants][62548]
    * [5.1 Xunlong Orange Pi Win Plus][62549]
  * [6 See also][62550]
    * [6.1 Manufacturer images][62551]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange pi Win v1.1
[/code]
# Sunxi support
## Current status
The board is supported by both mainline U-Boot and kernels. 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][62550]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][62552] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
#### Mainline U-Boot
Use the **orangepi_win_defconfig** build target (supported since v2017.07). 
### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
Use the **sun50i-a64-orangepi-win.dtb** device-tree tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The SW3(unsoldered) button triggers [ FEL mode][62553] (untested). 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## Locating the UART
[![][62554]][62555]
[][62556]
DEVICE UART pads
The UART pins are located between microusb and power jack of the board. On some boards they are marked as TX, RX and GND on the PCB (simplified layout: ..DC-IN.. [GND][RX][TX] ..microusb..). Just attach some leads according to our [UART howto][62557]. 
# Pictures
Take some pictures of your device, [ upload them][62558], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][62559]][62520]
  * [![Device back.jpg][62560]][62561]
  * [![Device buttons 1.jpg][62562]][62563]
  * [![Device buttons 2.jpg][62564]][62565]
  * [![Device board front.jpg][62566]][62567]
  * [![Device board back.jpg][62568]][62569]

# Variants
## Xunlong Orange Pi Win Plus
  * There is a variant called Xunlong Orange Pi Win Plus with 2 GB of DDR3 instead of the 1 GB in the original version. The Win Plus PCB is also black compared to the original blue. Otherwise the board seems identical.

# See also
  * [Orange Pi Win Plus schematics v1.3][62570]

## Manufacturer images
  * [User Manual][62571]
  * [Android source][62572]
  * [Linux kernel source][62573]
