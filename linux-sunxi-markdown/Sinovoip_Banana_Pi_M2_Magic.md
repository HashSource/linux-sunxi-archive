# Sinovoip Banana Pi M2 Magic
Sinovoip Banana Pi M2 Magic  
---  
[![BPi M2M top.jpg][50205]][50206]  
Manufacturer |  [Sinovoip][50207]  
Dimensions |  51 _mm_ x 51 _mm_ x 12 _mm_  
Release Date |  2017?   
Website |  [Device Product Page][50208]  
Specifications   
SoC |  [R16][50209] @ XGhz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  8GB eMMC   
Power |  DC 5V @ 2A via barrel plug, battery connector   
Features   
Video |  MIPI DSI LCD connector   
Audio |  onboard microphone, two-pin speaker connector   
Network |  WiFi 802.11 b/g/n ([Ampak AP6212][50210])   
Storage |  µSD, eMMC   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  CSI connector   
Headers |  3pin UART, 40pin GPIO, 2pin speaker   
This page needs to be properly filled according to the [New Device Howto][50211] and the [New Device Page guide][50212].
Compact development board with the R16 (aka. A33) SoC. No Ethernet or HDMI (as both are not supported by the SoC). 
## Contents
  * [1 Identification][50213]
  * [2 Sunxi support][50214]
    * [2.1 Current status][50215]
    * [2.2 Manual build][50216]
      * [2.2.1 U-Boot][50217]
      * [2.2.2 Linux Kernel][50218]
  * [3 Tips, Tricks, Caveats][50219]
    * [3.1 FEL mode][50220]
    * [3.2 Device specific topic][50221]
    * [3.3 ...][50222]
  * [4 Adding a serial port (**voids warranty**)][50223]
    * [4.1 Device disassembly][50224]
    * [4.2 Locating the UART][50225]
  * [5 Pictures][50226]
  * [6 Also known as][50227]
  * [7 See also][50228]
    * [7.1 Manufacturer images][50229]

# Identification
On the top of the board the BananaPi logo is silkscreened, and next to it: 
[code] 
    BPI_M2M_V1.2
[/code]
There are pictures of a v1.0 PCB version, with small differences, for instance a missing SPI flash footprint. 
# Sunxi support
## Current status
Supported in mainline Linux and U-Boot. 
## Manual build
You can build things for yourself by following our [ Manual build howto][50230] and by choosing from the configurations available below. 
### U-Boot
Use the _Bananapi_m2m_defconfig_ build target. 
### Linux Kernel
Use the _sun8i-r16-bananapi-m2m.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][50231]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][50232]][50233]
[][50234]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][50235]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][50236].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][50235].
# Pictures
  * [![BPi M2M bottom.jpg][50237]][50238]
  * [![BPi M2M side.jpg][50239]][50240]

# Also known as
  * Banana Pi BPI-M2M

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
