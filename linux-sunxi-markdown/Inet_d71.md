# Inet d71
Inet d71  
---  
[![Device front.jpg][27354]][27355]  
Manufacturer |  [Manufacturer][27356]  
Dimensions |  188 _mm_ x 117 _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][27357]  
Specifications   
SoC |  [A23][27358] @ 1.5Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  DC 5V @ 2A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Manufacturer device][27359])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][27360])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][27361])   
Headers |  UART?   
This page needs to be properly filled according to the [New Device Howto][27362] and the [New Device Page guide][27363].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][27364]
  * [2 Sunxi support][27365]
    * [2.1 Current status][27366]
    * [2.2 Images][27367]
    * [2.3 HW-Pack][27368]
    * [2.4 BSP][27369]
    * [2.5 Manual build][27370]
    * [2.6 Mainline U-Boot][27371]
    * [2.7 Mainline kernel][27372]
  * [3 Tips, Tricks, Caveats][27373]
    * [3.1 FEL mode][27374]
    * [3.2 Device specific topic][27375]
    * [3.3 ...][27376]
  * [4 Adding a serial port (**voids warranty**)][27377]
    * [4.1 Device disassembly][27378]
    * [4.2 Locating the UART][27379]
  * [5 Pictures][27380]
  * [6 Also known as][27381]
  * [7 See also][27382]
    * [7.1 Manufacturer images][27383]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Azpen
    A728
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INET-D71-REV01 Zeng-gc 2013-10-31
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: A728
  * Build Number: A23_D71_D711C_PG_1401072.20140616

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either U-Boot or kernel, mention this too, but add the extra sections below.
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][27382]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][27384]

Everything else is the same as the [manual build howto][27385]. 
## Mainline U-Boot
If there is mainline U-Boot support, add this section.
For [ building mainline U-Boot][27386], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][27387]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The VOL+ button triggers [ FEL mode][27388]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][27389]][27390]
[][27391]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][27392]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][27393].
  1. Insert a [plastic tool][27393] (I used my fingernail) into the seam between the display bezel and the back cover.
  2. Slide the tool around all four sides
  3. When all clips are released, the back cover should lift off. Be careful of the speaker taped to the back.

## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][27392].
# Pictures
Take some pictures of your device, [ upload them][27394], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][27395]][27355]
  * [![Device back.jpg][27396]][27397]
  * [![Device buttons 1.jpg][27398]][27399]
  * [![Device buttons 2.jpg][27400]][27401]
  * [![Device board front.jpg][27402]][27403]
  * [![Device board back.jpg][27404]][27405]

# Also known as
3GO 7003 EQC 
Azpen A72 
Danew Dslide 750 7.85" 
Pixor Tiny One 
Serioux Surya Antares 7" Slim SMO72 
Serioux Surya Antares 7" Slim SMO9VDC 
# See also
Add some nice to have links here. This includes related devices, and external links. [Inet_86dz_d701c][27406] [Inet_d70][27407]
## Manufacturer images
Optional. Add non-sunxi images in this section.
