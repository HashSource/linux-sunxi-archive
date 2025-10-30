# PengPod 1000
PengPod 1000  
---  
[![CherryM1007Android.jpg][44152]][44153]  
Manufacturer |  FIXME  
Dimensions |  267mm x 164mm x 14mm   
Release Date |  Month year  
Website |  Out of print   
Specifications   
SoC |  [A10][44154] @ 1Ghz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ 3A, 6000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (10" 10:6)   
Touchscreen |  5-finger capacitive (2x Focaltech FT5x)   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek 8192CU][44155]), in later models ([Realtek 8188EU][44155])   
Storage |  µSD, also an internal filled mmc slot   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][44156])   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][44157] and the [New Device Page guide][44158].
  
This device was [imported and rebranded][44159] under the PengPod 1000 name by Peacock Imports, who was secretive about where they had bought them. 
Although it comes in the same case as [Inet_1][44160], the board differs slightly. 
  

## Contents
  * [1 Identification][44161]
  * [2 Sunxi support][44162]
    * [2.1 Current status][44163]
    * [2.2 Images][44164]
    * [2.3 HW-Pack][44165]
    * [2.4 BSP][44166]
    * [2.5 Manual build][44167]
    * [2.6 Mainline U-Boot][44168]
    * [2.7 Mainline kernel][44169]
  * [3 Tips, Tricks, Caveats][44170]
    * [3.1 FEL mode][44171]
  * [4 Adding a serial port (**voids warranty**)][44172]
    * [4.1 Device disassembly][44173]
    * [4.2 Locating the UART][44174]
  * [5 Pictures][44175]
  * [6 Also known as][44176]
  * [7 See also][44177]
    * [7.1 Manufacturer images][44178]

# Identification
Apart from the names and symbols explaining the buttons, the back of the device is blank. It came with a small sticker proclaiming "N500c", indicating that it _may_ have been a Wayestar device. 
The following is silkscreened on the underside of the PCB: 
[code] 
    USEN
    1252.040 (or some other numbers) 
    YONESTOPTECH-1077
    2012/05/05
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: BC1077
  * Kernel Version: 3.0.8+ jackie@ubuntu #50 Mon Nov5 09:51:29 CST 2012
  * Build Number: crane_bc1077-eng 4.0.4 IMM76D 20121108 test-keys

# Sunxi support
## Current status
pengpod1000 can be found in [boards.cfg][44179], but not much else. However, it is (as mentioned earlier) very similiar to the [Point of View Protab 2 XXL][44160]
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][44177]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
## BSP
## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can (not yet) be found in sunxi-boards
  * It can be found at [this temporary location][44180]

Everything else is the same as the [manual build howto][44181]. 
## Mainline U-Boot
## Mainline kernel
# Tips, Tricks, Caveats
It may need the same changes to fully support FT5X as mentioned on the [Inet_1][44160] page. 
## FEL mode
There is a button between power connector and Mini USB connector which supposedly triggers [ FEL mode][44182]. 
  

# Adding a serial port (**voids warranty**)
[![][44183]][44184]
[][44185]
DEVICE UART pads
  

## Device disassembly
By removing the two screws on the connector side, the device is trivially opened. 
## Locating the UART
There are some marked UART pads in a corner of the board, near the type-A usb socket, where you'd need to solder on some wires according to our [UART howto][44186]. 
# Pictures
  * [![CherryM1007Android.jpg][44187]][44153]
  * [![PP1k back.jpg][44188]][44189]
  * [![PP1k buttons.jpg][44190]][44191]
  * [![][44192]][44193]
PCB front side 
  * [![][44194]][44195]
PCB back side 
  * [![][44196]][44197]
Connector side with two screws 

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
