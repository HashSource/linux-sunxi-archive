# Jepower T508A
Jepower T508A  
---  
[![Device front.jpg][28907]][28908]  
Manufacturer |  [Jepower][28909]  
Dimensions |  350 _mm_ x 185 _mm_ x 145 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][28910]  
Specifications   
SoC |  [A10][28911] @ 1Ghz   
DRAM |  1GB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 12V @ 5A, 4400mAh ?V Li-Ion battery   
Features   
LCD |  1024x720 (9.7")   
Touchscreen |  5-finger capacitive/resistive ([Manufacturer device][28912])   
Video |  HDMI (mini)   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, miniHDMI, internal stereo speakers   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188CUS), 10/100/1000Mbps Ethernet (Realtek RTL8150)   
Storage |  µSD   
USB |  3 USB2.0 Host, 1 USB2.0 OTG   
Camera |  2MP front (optional)   
Other |  10-digit LED, NFC, RFID, Magnetic stripe reader (optional), RJ11, Fingerprint reader (optional), Thermal printer   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][28913] and the [New Device Page guide][28914].
## Contents
  * [1 Identification][28915]
  * [2 Sunxi support][28916]
    * [2.1 Current status][28917]
    * [2.2 Images][28918]
    * [2.3 HW-Pack][28919]
    * [2.4 BSP][28920]
    * [2.5 Manual build][28921]
    * [2.6 Mainline U-Boot][28922]
    * [2.7 Mainline kernel][28923]
  * [3 Tips, Tricks, Caveats][28924]
    * [3.1 FEL mode][28925]
    * [3.2 Device specific topic][28926]
    * [3.3 ...][28927]
  * [4 Adding a serial port (**voids warranty**)][28928]
    * [4.1 Device disassembly][28929]
    * [4.2 Locating the UART][28930]
  * [5 Pictures][28931]
  * [6 See also][28932]
    * [6.1 Manufacturer images][28933]

# Identification
On the back of the device, the following is printed: 
[code] 
    Android Multi-function Intelligent Terminal
    
    Input: 12V5A DC
    Model: T508
    S/N  : <sticker>
    
[/code]
The PCB has the following silkscreened on it: 
[/code]
[code] 
In android, under Settings->About Tablet, you will find: 
  * Model Number: _363LB POS v1_
  * Build Number: _crane_m1003h6-eng 4.1.1 JRO03C 20130108 test-keys_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either U-Boot or kernel, mention this too, but add the extra sections below. A10 (sun4i) 
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][28932]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][28934]

Everything else is the same as the [manual build howto][28935]. 
## Mainline U-Boot
If there is mainline U-Boot support, add this section.
For [ building mainline U-Boot][28936], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][28937]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][28938]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][28939]][28940]
[][28941]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][28942]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][28943].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][28942].
# Pictures
Take some pictures of your device, [ upload them][28944], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][28945]][28908]
  * [![Device back.jpg][28946]][28947]
  * [![Device buttons 1.jpg][28948]][28949]
  * [![Device buttons 2.jpg][28950]][28951]
  * [![Device board front.jpg][28952]][28953]
  * [![Device board back.jpg][28954]][28955]

# See also
## Manufacturer images
  * [[1]][28956]
  * [[2]][28957]
  * [[3]][28958]
  * [[4]][28959]
  * [[5]][28960]
