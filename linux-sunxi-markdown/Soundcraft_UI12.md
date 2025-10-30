# Soundcraft UI12
Soundcraft UI12  
---  
[![Device front.jpg][51257]][51258]  
Manufacturer |  [[1]][51259]  
Dimensions |  90 _mm_ x 90 _mm_ x TODO _mm_  
Release Date |  [Template:May 2015][51260]  
Website |  [Soundcraft UI12 Product Page][51261]  
Specifications   
SoC |  [A20][51262] @ ?Ghz   
DRAM |  512MiB DDR3 @ ?MHz SKHynix H5TQ4G63CFR   
NAND |  4GB <https://www.alldatasheet.com/view.jsp?Searchword=SDIN7DP2-4G>  
Power |  DC 5V @ ?A, battery n/a (18V to the entire box)   
Features   
LCD |  n/a   
Touchscreen |  n/a   
Video |  n/a   
Audio |  on board? on extension board: 8XLR in, 4 XLR out   
Network |  WiFi 802.11 b/g/n ([TODO manufacturer device][51263]), 10/100Mbps Ethernet ([[RTL8201CP][51264]])   
Storage |  n/a except for nand (and possibly some unexposed headers?)   
USB |  3 USB2.0 Host   
Camera |  n/a   
Other |  Analog devices ADSP 21489 KSWZ-4B 4112246-1B.02#1802   
Headers |  UART, JTAG, LCD, VGA, ...   
This is a first step. This page needs to be properly filled according to the [New Device Howto][51265] and the [New Device Page guide][51266].
This is a digital mixer. We found out binwalking the firmware update it actually has a sun7i under its cooling fin... 
## Contents
  * [1 Identification][51267]
  * [2 Sunxi support][51268]
    * [2.1 Current status][51269]
    * [2.2 Images][51270]
    * [2.3 HW-Pack][51271]
    * [2.4 BSP][51272]
    * [2.5 Manual build][51273]
      * [2.5.1 U-Boot][51274]
        * [2.5.1.1 Sunxi/Legacy U-Boot][51275]
        * [2.5.1.2 Mainline U-Boot][51276]
      * [2.5.2 Linux Kernel][51277]
        * [2.5.2.1 Sunxi/Legacy Kernel][51278]
        * [2.5.2.2 Mainline kernel][51279]
  * [3 Tips, Tricks, Caveats][51280]
    * [3.1 FEL mode][51281]
    * [3.2 Device specific topic][51282]
    * [3.3 ...][51283]
  * [4 Adding a serial port (**voids warranty**)][51284]
    * [4.1 Device disassembly][51285]
    * [4.2 Locating the UART][51286]
  * [5 Pictures][51287]
  * [6 Also known as][51288]
  * [7 See also][51289]
    * [7.1 Manufacturer images][51290]

# Identification
The audio PCB has the following silkscreened on it: 
[code] 
    IPS6_Ui12 NSM_2015_MP3
    1970-01-01
[/code]
This is not an android device. 
# Sunxi support
## Current status
n/a. We've just got 99% certainty that this is an A20 board. Firmware image suggests it's running a 3.4.106 sun7i kernel. As far as I could find, it has at least ffmpeg and mpv on board without anything mentioned in terms of licensing information whatsoever. 
## Images
No full image recovered yet. The NAND is too fiddly small to clip on legs and read firmware :-( 
## HW-Pack
n/a 
## BSP
n/a 
## Manual build
You can build things for yourself by following our [ Manual build howto][51291] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][51292] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The SW2 button looks like it would trigger [ FEL mode][51293]. We were warned not to use that in order not to confuse the NAND, at least not until we have more info (u-boot version, linux kernel version, ...) and a proper firmware image to investigate. 
## Device specific topic
The thing runs a telnetd. No username or password guessed yet. Firmware updates seem to be mostly signed, with no /etc/passwd file to brute force at first sight. 
## ...
# Adding a serial port (**voids warranty**)
[![][51294]][51295]
[][51296]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][51297]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
Just unscrew the 8 screw keeping the metal lid on. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][51297].
# Pictures
  * [![Soundcraftui12 1.jpg][51298]][51299]
  * [![IMG 6212.JPG][51300]][51301]
  * [![Soundcraftui12 2.jpg][51302]][51303]
  * [![IMG 6214.JPG][51304]][51305]
  * [![IMG 6215.JPG][51306]][51307]
  * [![Soundcraftui12 4.jpg][51308]][51309]
  * [![Soundcraftui12 5.jpg][51310]][51311]
  * [![IMG 6218.JPG][51312]][51313]
  * [![IMG 6219.JPG][51314]][51315]
  * [![IMG 6220.JPG][51316]][51317]
  * [![IMG 6221.JPG][51318]][51319]
  * [![IMG 6222.JPG][51320]][51321]
  * [![IMG 6223.JPG][51322]][51323]
  * [![IMG 6224.JPG][51324]][51325]
  * [![IMG 6225.JPG][51326]][51327]
  * [![IMG 6226.JPG][51328]][51329]
  * [![IMG 6227.JPG][51330]][51331]
  * [![IMG 6228.JPG][51332]][51333]
  * [![IMG 6229.JPG][51334]][51335]
  * [![IMG 6230.JPG][51336]][51337]

# Also known as
This thing has a brother, the Soundcraft Ui16, that uses the exact same sunxi hardware. 
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
