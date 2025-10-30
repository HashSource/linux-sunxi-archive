# Pentagram P5355
Pentagram P5355  
---  
[![Device front.jpg][44231]][44232]  
Manufacturer |  [Pentagram][44233]  
Release Date |  2013  
Website |  [Quadra 9.7][44234]  
Specifications   
SoC |  [A31][44235] @ 1 Ghz   
DRAM |  2 GiB DDR3 @ 624 MHz (SK Hynix H5TQ2G83EFR-PBC)   
NAND |  16 GB (Hynix H27UCG8T2MYR-BC)   
Features   
LCD |  2048×1536 (9.7” 4:3)   
Touchscreen |  10-finger capacitive ([Silead gslX680][44236])   
Video |  HDMI (Type C — mini)   
Audio |  3.5 mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][44237])   
Storage |  µSD   
USB |  1 µUSB 2.0 OTG   
Camera |  1.92 MPx (1600×1200) front, 1.92 MPx (1600×1200) rear   
This page needs to be properly filled according to the [New Device Howto][44238] and the [New Device Page guide][44239].
  

## Contents
  * [1 Identification][44240]
  * [2 Sunxi support][44241]
    * [2.1 Current status][44242]
    * [2.2 Images][44243]
    * [2.3 HW-Pack][44244]
    * [2.4 BSP][44245]
    * [2.5 Manual build][44246]
      * [2.5.1 U-Boot][44247]
        * [2.5.1.1 Mainline U-Boot][44248]
      * [2.5.2 Linux Kernel][44249]
        * [2.5.2.1 Mainline kernel][44250]
  * [3 Tips, Tricks, Caveats][44251]
    * [3.1 FEL mode][44252]
    * [3.2 Locating the UART][44253]
  * [4 Pictures][44254]
  * [5 Also known as][44255]
  * [6 See also][44256]
    * [6.1 Manufacturer images][44257]

# Identification
On the back of the device, the following is printed: 
[code] 
    PENTAGRAM
    TAB Quadra 9
[/code]
The PCB has the following silkscreened on it: 
[code] 
    M977QG9_MB_V13_130309
[/code]
In Android, under Settings→About Tablet, you will find: 
  * Model Number: _PENTAGRAM TAB Quadra 9.7_
  * Build Number: _fiber_pentagram977q9-eng 4.2.2 JDQ39 20130813 test-keys_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][44256]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][44258] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
### Linux Kernel
#### Mainline kernel
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The Home button triggers [ FEL mode][44259]. It’s possible to run “sunxi-fel version” successfully, but e.g. “sunxi-fel read 0x42400000 0x82d0 boot1.header” fails with “usb_bulk_send() ERROR -7: Operation timed out”. 
Sending 1 over UART during device startup results in boot0, then boot1. It is possible to mount nanda and internal storage over USB. 
Sending 2 over UART during device startup results in boot0, then boot1, then boot0/FEL. It’s possible to run “sunxi-fel version” successfully, but e.g. “sunxi-fel read 0x42400000 0x82d0 boot1.header” fails with “usb_bulk_send() ERROR -7: Operation timed out”. 
  

## Locating the UART
The UART pads (RX and TX) are on the left of the SoC. The upper pad is tablet’s TX, the lower one is RX. The pads aren’t pretinned. Follow the [UART howto][44260]. 
# Pictures
  * [![Pentagram P5355 back.jpg][44261]][44262]

# Also known as
  * Modecom Freetab 9704
  * [Onda V972][44263]
  * sQuad 9.72

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
