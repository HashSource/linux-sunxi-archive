# Device Page example
Device Page example  
---  
[![Device front.jpg][16530]][16531]  
Manufacturer |  [Manufacturer][16532]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][16533]  
Specifications   
SoC |  [AXX][16534] @ XGhz   
DRAM |  512MiB/1GiB/2GiB DDR3 @ xxxMHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][16535])   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][16536]), 10/100/1000Mbps Ethernet ([Manufacturer device][16537])   
Storage |  µSD, SATA   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][16538]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][16539] and the [New Device Page guide][16540].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][16541]
  * [2 Sunxi support][16542]
    * [2.1 Current status][16543]
    * [2.2 Images][16544]
    * [2.3 HW-Pack][16545]
    * [2.4 BSP][16546]
    * [2.5 Manual build][16547]
      * [2.5.1 U-Boot][16548]
        * [2.5.1.1 Sunxi/Legacy U-Boot][16549]
        * [2.5.1.2 Mainline U-Boot][16550]
      * [2.5.2 Linux Kernel][16551]
        * [2.5.2.1 Sunxi/Legacy Kernel][16552]
        * [2.5.2.2 Mainline kernel][16553]
  * [3 Tips, Tricks, Caveats][16554]
    * [3.1 FEL mode][16555]
    * [3.2 Device specific topic][16556]
    * [3.3 ...][16557]
  * [4 Adding a serial port (**voids warranty**)][16558]
    * [4.1 Device disassembly][16559]
    * [4.2 Locating the UART][16560]
  * [5 Pictures][16561]
  * [6 Schematic][16562]
  * [7 Also known as][16563]
  * [8 See also][16564]
    * [8.1 Manufacturer images][16565]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Manufacturer Marketing Name
    ModelNumber
[/code]
The PCB has the following silkscreened on it: 
[code] 
    LIA-BB-V6.66
    1970-01-01
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][16564]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][16566] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][16567] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][16568]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][16569]][16570]
[][16571]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][16572]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][16573].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][16572].
# Pictures
Take some pictures of your device, [ upload them][16574], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][16575]][16531]
  * [![Device back.jpg][16576]][16577]
  * [![Device buttons 1.jpg][16578]][16579]
  * [![Device buttons 2.jpg][16580]][16581]
  * [![Device board front.jpg][16582]][16583]
  * [![Device board back.jpg][16584]][16585]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
