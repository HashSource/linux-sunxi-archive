# Justop MPA040BKT
Justop MPA040BKT  
---  
[![Justop MPA040BKT.png][29242]][29243]  
Manufacturer |  [Justop][29244]  
Dimensions |  120 _mm_ x 90 _mm_ x 30 _mm_  
Release Date |  11/2012   
Website |  <http://www.justop.com> Device Product Page]   
Specifications   
SoC |  [A10][29245] @ 1.0Ghz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ 1A, *3.3V coin cell battery needs 16mm socket soldered to the PCB pads   
Features   
LCD |  No   
Touchscreen |  No   
Video |  HDMI (Type A - full), Composite 3.5mm plug   
Audio |  3.5mm plug, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CTV][29246]), 10/100/1000Mbps Ethernet ([Realtek RTL8201CP][29247])   
Storage |  SD   
USB |  1 X USB2.0 Host, 1 X USB2.0 OTG/FEL   
Camera |  No   
Other |  IRDA   
Headers |  UART, JTAG   
This page needs to be properly filled according to the [New Device Howto][29248] and the [New Device Page guide][29249].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][29250]
  * [2 Sunxi support][29251]
    * [2.1 Current status][29252]
    * [2.2 Images][29253]
    * [2.3 HW-Pack][29254]
    * [2.4 BSP][29255]
    * [2.5 Manual build][29256]
      * [2.5.1 U-Boot][29257]
        * [2.5.1.1 Sunxi/Legacy U-Boot][29258]
        * [2.5.1.2 Mainline U-Boot][29259]
      * [2.5.2 Linux Kernel][29260]
        * [2.5.2.1 Sunxi/Legacy Kernel][29261]
        * [2.5.2.2 Mainline kernel][29262]
  * [3 Tips, Tricks, Caveats][29263]
    * [3.1 FEL mode][29264]
    * [3.2 Device specific topic][29265]
    * [3.3 ...][29266]
  * [4 Adding a serial port][29267]
    * [4.1 Device disassembly][29268]
    * [4.2 Locating the UART][29269]
  * [5 Pictures][29270]
  * [6 Also known as][29271]
  * [7 See also][29272]
    * [7.1 Manufacturer images][29273]

# Identification
This was sold in two versions with the main difference being the functionality of the remote IR controller. Very similar to Miniand Hackberry (1GB RAM version) and the images for the Hackberry work on this unit as well. Supplied with Android 4.0 that could be updated with various versions released by Justop (by the administrator Justin) on their old forums with the latest being "JUSTOP_A054_V1.8.1_20130809_ytb_fix_old_remote" or "new remote", depending on the hardware version). The forums are active again on <https://www.tapatalk.com/groups/justop/> (as of July 2020) but all the old messages are gone. 
Manual 
[File:Justop MPA040BKT V2 Manual.pdf][29274]
[Original][29275]
There's nothing printed on the back. 
The PCB has the following silkscreened on it: 
[code] 
    RSH-A9-MAIN V1.5
    2012-08-12
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _RSH_PUB_APOLLO_
  * Build Number: _apollo_rshhost-eng4.0.4_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][29272]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][29276] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][29277] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The FEL mode can be triggered by shorting the two pads on the button K9 marked as FEL (see adding a serial port section below) or by sending number 2 over serial after powering on the device. Both trigger FEL but the second method provides initialization of the PIO according to "script.bin". 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port
[![][29278]][29279]
[][29280]
UART pads
[UART howto][29281]
The picture shows the serial port at the bottom. Pins left to right are: 
\- GND 
\- GND 
\- 3.3V 
\- RX 
\- TX 
  

## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][29282].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][29281].
# Pictures
Take some pictures of your device, [ upload them][29283], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Justop MPA040BKT pcb top.jpg][29284]][29279]
  * [![Justop MPA040BKT pcb bottom.jpg][29285]][29286]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
