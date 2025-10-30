# Inet D71b
Inet D71b  
---  
[![Device front.jpg][26995]][26996]  
Manufacturer |  [Manufacturer][26997]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][26998]  
Specifications   
SoC |  [AXX][26999] @ XGhz   
DRAM |  512MiB/1GiB/2GiB DDR3 @ xxxMHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][27000])   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][27001]), 10/100/1000Mbps Ethernet ([Manufacturer device][27002])   
Storage |  µSD, SATA   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][27003]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][27004] and the [New Device Page guide][27005].
## Contents
  * [1 Identification][27006]
  * [2 Sunxi support][27007]
    * [2.1 Current status][27008]
    * [2.2 Images][27009]
    * [2.3 HW-Pack][27010]
    * [2.4 BSP][27011]
    * [2.5 Manual build][27012]
      * [2.5.1 U-Boot][27013]
        * [2.5.1.1 Sunxi/Legacy U-Boot][27014]
        * [2.5.1.2 Mainline U-Boot][27015]
      * [2.5.2 Linux Kernel][27016]
        * [2.5.2.1 Sunxi/Legacy Kernel][27017]
        * [2.5.2.2 Mainline kernel][27018]
  * [3 Tips, Tricks, Caveats][27019]
    * [3.1 FEL mode][27020]
    * [3.2 Device specific topic][27021]
    * [3.3 ...][27022]
  * [4 Adding a serial port (**voids warranty**)][27023]
    * [4.1 Device disassembly][27024]
    * [4.2 Locating the UART][27025]
  * [5 Pictures][27026]
  * [6 Also known as][27027]
  * [7 See also][27028]
    * [7.1 Manufacturer images][27029]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Pendo Pad
    PENDHD7
[/code]
The PCB has the following silkscreened on it: 
[code] 
    Inet D71B-Rev02 Zeng-gc 2014-11-06
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][27028]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][27030] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][27031] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][27032]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][27033]][27034]
[][27035]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][27036]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][27037].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][27036]. See [UART howto][27036]. Easiest way to find the signals is to remove the 5 screws and the touch sense flatflex and fold the board up. They are marked on the underside of the board. 
# Pictures
Take some pictures of your device, [ upload them][27038], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][27039]][26996]
  * [![Device back.jpg][27040]][27041]
  * [![Device buttons 1.jpg][27042]][27043]
  * [![Device buttons 2.jpg][27044]][27045]
  * [![PendoPadHD7 opened.jpeg][27046]][27047]
  * [![PendoPadHD7 uart.jpeg][27048]][27049]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
