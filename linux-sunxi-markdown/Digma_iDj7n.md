# Digma iDj7n
Digma iDj7n  
---  
[img][16831]  
Manufacturer |  [Digma]   
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][16832]  
Specifications   
SoC |  [A13][16833] @ XGhz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  4 Gb   
Power |  DC 5V @ 3A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (7" 800:480)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][16834])   
Video |  \--   
Audio |  3.5mm headphone plug,internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][16835])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer (manufacturer device), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...1   
This page needs to be properly filled according to the [New Device Howto][16836] and the [New Device Page guide][16837].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][16838]
  * [2 Sunxi support][16839]
    * [2.1 Current status][16840]
    * [2.2 Images][16841]
    * [2.3 HW-Pack][16842]
    * [2.4 BSP][16843]
    * [2.5 Manual build][16844]
    * [2.6 Mainline U-Boot][16845]
    * [2.7 Mainline kernel][16846]
  * [3 Tips, Tricks, Caveats][16847]
    * [3.1 FEL mode][16848]
    * [3.2 Device specific topic][16849]
    * [3.3 ...][16850]
  * [4 Adding a serial port (**voids warranty**)][16851]
    * [4.1 Device disassembly][16852]
    * [4.2 Locating the UART][16853]
  * [5 Pictures][16854]
  * [6 Also known as][16855]
  * [7 See also][16856]
    * [7.1 Manufacturer images][16857]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Digma
    Digma iDj7n
[/code]
The PCB has the following silkscreened on it: 
[code] 
    --
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: iDj7n
  * Build Number: A13_86VS_M758C1_*number* (I have non-official firmware)

# Sunxi support
## Current status
20-11-2014 WIP; have a bootable prototype 
05-05-2015 Ponies ^_____^ [unfreezing a project] 
20-11-2017 [unfreezing a project] (still in pony-mode) 
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][16856]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building u-boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][16858]

Everything else is the same as the [manual build howto][16859]. 
## Mainline U-Boot
If there is mainline u-boot support, add this section.
For [ building mainline u-boot][16860], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][16861]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The volume+ button triggers [ FEL mode][16862]. Press VOL+, PWR, wait 2-3 sec, press PWR 3-5 times again, release VOL+. 
FEL SD image don't work. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][16863]][16864]
[][16865]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][16866]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][16867].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][16866].
# Pictures
Take some pictures of your device, [ upload them][16868], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][16869]][16870]
  * [![Device back.jpg][16871]][16872]
  * [![Device buttons 1.jpg][16873]][16874]
  * [![Device buttons 2.jpg][16875]][16876]
  * [![Device board front.jpg][16877]][16878]
  * [![Device board back.jpg][16879]][16880]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
