# Tanix TX1
Tanix TX1  
---  
[![Tanix tx1.jpg][54256]][54257]  
Manufacturer |  [Tanix][54258]  
Dimensions |  58 _mm_ x 58 _mm_ x 25 _mm_  
Release Date |  November 2023   
Website |  [Tanix TX1][54259]  
Specifications   
SoC |  [H313][54260] @ 1.3Ghz   
DRAM |  1GiB/2GiB LPDDR3 @ 720MHz   
eMMC |  8/16GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug, HDMI   
Network |  WiFi 802.11 b/g/n ([SCI S9082H][54261])   
Storage |  eMMC, **NO** SD card!   
USB |  1 USB2.0 Host   
Other |  infrared   
Headers |  UART pads   
This page needs to be properly filled according to the [New Device Howto][54262] and the [New Device Page guide][54263].
Tiny TV box (about 70% of a credit card), without SD card and Ethernet. AXP313 PMIC. 
## Contents
  * [1 Identification][54264]
  * [2 Sunxi support][54265]
    * [2.1 Current status][54266]
    * [2.2 Manual build][54267]
      * [2.2.1 Mainline U-Boot][54268]
      * [2.2.2 Mainline Linux Kernel][54269]
  * [3 Tips, Tricks, Caveats][54270]
    * [3.1 FEL mode][54271]
  * [4 Adding a serial port (**voids warranty**)][54272]
    * [4.1 Device disassembly][54273]
    * [4.2 Locating the UART][54274]
  * [5 Pictures][54275]
  * [6 Also known as][54276]
  * [7 See also][54277]
    * [7.1 Manufacturer images][54278]

# Identification
On the top of the device, it shows the Tanix logo. On the bottom of the device, there is nothing really device specific, it just shows a sticker with the serial number and MAC address, below some compliance logos, and "DC = 5V/2A MADE IN CHINA". 
The PCB has the following silkscreened on it: 
[code] 
    CS_H313_TX1_EMCP_V1.1
    DATE:2023-09-21
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _TX1_
  * Build Number: '****

#  Sunxi support
## Current status
Supported in both mainline kernel and U-Boot. 
## Manual build
You can build things for yourself by following our [ Manual build howto][54279] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _tanix_tx1_defconfig_ build target. Available since v2024.10-rc3. 
### Mainline Linux Kernel
Use the _sun50i-h313-tanix-tx1.dtb_ devicetree binary from a mainline kernel, available since v6.10. Older kernels with decent H616 support will work as well, as long as you give it the right DTB, for instance the one used in U-Boot (`$fdtcontroladdr`). 
# Tips, Tricks, Caveats
## FEL mode
Use a toothpick or any other non-conductive stick to push the button inside the A/V connector when powering up the box. Connect a USB-A/USB-A cable to the only USB port and a host PC. 
# Adding a serial port (**voids warranty**)
[![][54280]][54281]
[][54282]
Tanix TX1 UART pads
## Device disassembly
Insert some spudger tool into the small gap around the top of the device, and gently pry the lid off by moving the tool around the entire lid. There is some sticky heat dispensing material glued to the lid, which presses on top of the PCB heat spreader, but that comes off easily. A similar sticky pad holds the PCB on the bottom shell, so just use some tool to lever and pull the PCB out off the device, its not secured with any screws. 
## Locating the UART
The UART pads are on the underside of the PCB, there are four circular solder pads just underneath the USB connector. The silk screen label above them describes them as "VCC, RX, TX, GND", as usual just use the lower three to connect some cable and ignore the VCC pin. Also see the [UART howto][54283]. 
# Pictures
  * [![Tanix tx1.jpg][54284]][54257]
  * [![Tanix tx1 ports.jpg][54285]][54286]
  * [![Tanix tx1 rear.jpg][54287]][54288]
  * [![Tanix tx1 bottom.jpg][54289]][54290]
  * [![Tanix tx1 shells.jpg][54291]][54292]
  * [![Tanix tx1 pcb.jpg][54293]][54294]
  * [![Tanix tx1 pcb bottom.jpg][54295]][54296]
  * [![Tanix tx1 pcb pmic.jpg][54297]][54298]
  * [![Wudung-W01-top.jpg][54299]][54300]
  * [![Wudung W01 pcb bottom.jpg][54301]][54302]

  

# Also known as
  * Wudung W01

[![][54303]][54300]
[][54304]
Wudung W01 PCB front
[![][54305]][54302]
[][54306]
Wudung W01 PCB bottom
  * Vontar QTV Q1

  

# See also
## Manufacturer images
No known images available for download (yet?).
