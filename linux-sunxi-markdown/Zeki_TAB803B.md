# Zeki TAB803B
Zeki TAB803B  
---  
[![TAB803B front.JPG][64087]][64088]  
Manufacturer |  [Zeki][64089]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  2013  
Website |  [Device Product Page][64090]  
Specifications   
SoC |  [A10][64091] @ 1Ghz   
DRAM |  1GiB DDR3   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
LCD |  none   
Touchscreen |  none   
Video |  HDMI (Type A - full), 3.5mm AV video output   
Audio |  3.5mm headphone plug   
Network |  WiFi 802.11 b/g/n ([Realtek 8188eus][64092]), 10/100/1000Mbps Ethernet ([Realtek device][64093])   
Storage |  µSD, SATA   
USB |  2 USB2.0 Host   
Camera |  none   
Other |  none   
Headers |  UART, JTAG, SATA   
This page needs to be properly filled according to the [New Device Howto][64094] and the [New Device Page guide][64095].
## Contents
  * [1 Identification][64096]
  * [2 Sunxi support][64097]
    * [2.1 Current status][64098]
    * [2.2 Manual build][64099]
      * [2.2.1 U-Boot][64100]
        * [2.2.1.1 Sunxi/Legacy U-Boot][64101]
        * [2.2.1.2 Mainline U-Boot][64102]
      * [2.2.2 Linux Kernel][64103]
        * [2.2.2.1 Sunxi/Legacy Kernel][64104]
        * [2.2.2.2 Mainline kernel][64105]
  * [3 Tips, Tricks, Caveats][64106]
    * [3.1 FEL mode][64107]
    * [3.2 Device specific topic][64108]
    * [3.3 ...][64109]
  * [4 Pictures][64110]
  * [5 Also known as][64111]
  * [6 See also][64112]
    * [6.1 Manufacturer images][64113]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
It is also known as a Zeki Streaming Media Box 
In android, under Settings->About Device, you will find: 
  * Model Number: _TAB803_
  * Build Number: _IMM76D_

# Sunxi support
## Current status
Currently the easiest way to get another OS running is by installing [Berryboot][64114] from Android. The wifi is broken on the Berryboot kernel however 
## Manual build
You can build things for yourself by following our [ Manual build howto][64115] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][64116] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][64117]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Pictures
Take some pictures of your device, [ upload them][64118], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][64119]][64120]
  * [![TAB803B rear.JPG][64121]][64122]
  * [![Device buttons 1.jpg][64123]][64124]
  * [![Device buttons 2.jpg][64125]][64126]
  * [![Device board front.jpg][64127]][64128]
  * [![Device board back.jpg][64129]][64130]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
