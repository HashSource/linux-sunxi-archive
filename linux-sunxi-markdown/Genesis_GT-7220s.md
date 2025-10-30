# Genesis GT-7220s
Genesis GT-7220s  
---  
[![Device front.jpg][21914]][21915]  
Manufacturer |  Genesis/[Skyworth][21916]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Circa 2012   
Website |  Non-existant   
Specifications   
SoC |  [A10][21917] @ Ghz   
DRAM |  1GiB DDR3 @ 800MHz   
NAND |  8GB   
Power |  DC 5V @ 3A, 4000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7")   
Touchscreen |  5-finger capacitive ([Goodix GT811][21918])   
Video |  HDMI (mini)   
Audio |  3.5mm headphone plug, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek 8188CUS][21919])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Headers |  LCD   
This page needs to be properly filled according to the [New Device Howto][21920] and the [New Device Page guide][21921].
The Genesis GT-7220s is a cheap Chinese A10 tablet that used to be sold in Brazil circa 2012. I can't find more information about it in the Internet because most of its community was found in the Genesis Series forums, which have been since taken down. 
## Contents
  * [1 Identification][21922]
  * [2 Sunxi support][21923]
    * [2.1 Current status][21924]
    * [2.2 Manual build][21925]
      * [2.2.1 U-Boot][21926]
        * [2.2.1.1 Sunxi/Legacy U-Boot][21927]
        * [2.2.1.2 Mainline U-Boot][21928]
      * [2.2.2 Linux Kernel][21929]
        * [2.2.2.1 Sunxi/Legacy Kernel][21930]
        * [2.2.2.2 Mainline kernel][21931]
  * [3 Tips, Tricks, Caveats][21932]
    * [3.1 FEL mode][21933]
    * [3.2 Device specific topic][21934]
    * [3.3 ...][21935]
  * [4 Adding a serial port (**voids warranty**)][21936]
    * [4.1 Device disassembly][21937]
    * [4.2 Locating the UART][21938]
  * [5 Pictures][21939]
  * [6 Also known as][21940]
  * [7 See also][21941]
    * [7.1 Manufacturer images][21942]

# Identification
On the back of the device, the following is printed: 
[code] 
    Skyworth
    GT-7220S
[/code]
The PCB has the following silkscreened on it: 
[code] 
    A702_MB_V1.6
    2012.06.19
[/code]
My sample of the device had a custom ROM spoofing it as a Samsung tablet before I started researching it, so I can't provide correct Android identification strings. 
# Sunxi support
## Current status
This device is not currently supported by the project. I am working on porting both mainline U-Boot and Linux to it. 
## Manual build
You can build things for yourself by following our [ Manual build howto][21943] and by choosing from the configurations available below. 
Please note that, since this device is in the process of being supported, the patches containing the settings below probably won't be upstreamed yet. 
### U-Boot
#### Sunxi/Legacy U-Boot
n/a 
#### Mainline U-Boot
Use the _Genesis_GT7220s_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_genesis_gt7220.fex_][21944] file. 
#### Mainline kernel
Use the _sun4i-a10-genesis-gt7220s.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][21945]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][21946]][21947]
[][21948]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][21949]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][21950].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][21949].
# Pictures
Take some pictures of your device, [ upload them][21951], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][21952]][21915]
  * [![Device back.jpg][21953]][21954]
  * [![Device buttons 1.jpg][21955]][21956]
  * [![Device buttons 2.jpg][21957]][21958]
  * [![Device board front.jpg][21959]][21960]
  * [![Device board back.jpg][21961]][21962]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
