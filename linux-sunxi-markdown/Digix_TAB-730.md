# Digix TAB-730
Digix TAB-730  
---  
[![Tab730-front.jpeg][16746]][16747]  
Manufacturer |  Digix (defunct)   
Dimensions |  125.9 _mm_ x 198.8 _mm_ x 10.9 _mm_  
Release Date |  November 2011   
Website |  (defunct)   
Specifications   
SoC |  [A10][16748] @ 1.2Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 5:3)   
Touchscreen |  5-finger capacitive ([Focaltech ft5x][16749])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8192cu][16750]), 10/100/1000Mbps Ethernet ([Manufacturer device][16751])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([MMA7660][16752])   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][16753] and the [New Device Page guide][16754].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][16755]
  * [2 Sunxi support][16756]
    * [2.1 Current status][16757]
    * [2.2 Images][16758]
    * [2.3 HW-Pack][16759]
    * [2.4 BSP][16760]
    * [2.5 Manual build][16761]
      * [2.5.1 U-Boot][16762]
        * [2.5.1.1 Sunxi/Legacy U-Boot][16763]
        * [2.5.1.2 Mainline U-Boot][16764]
      * [2.5.2 Linux Kernel][16765]
        * [2.5.2.1 Sunxi/Legacy Kernel][16766]
        * [2.5.2.2 Mainline kernel][16767]
  * [3 Tips, Tricks, Caveats][16768]
    * [3.1 FEL mode][16769]
  * [4 Adding a serial port (**voids warranty**)][16770]
    * [4.1 Device disassembly][16771]
    * [4.2 Locating the UART][16772]
  * [5 Pictures][16773]
  * [6 Schematic][16774]
  * [7 Also known as][16775]
  * [8 See also][16776]
    * [8.1 Manufacturer images][16777]

# Identification
On the back of the device, the following is printed: 
[code] 
    DIGIX
    Model: TAB-730
    FCC ID: YAPTAB730
[/code]
The PCB has the following silkscreened on it: 
[code] 
    ST-02 94V-0
    E310229
[/code]
[code] 
    TAB730MA1X30
    20120814
    Contel
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _TAB-730_

There is no build number. 
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][16776]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][16778] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][16779] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
To trigger [ FEL mode][16780] unplug USB, turn it off, hold down the Volume Down button, plug in USB, quickly press the Power button ten times, and release the Power and Volume Down buttons. 
# Adding a serial port (**voids warranty**)
[![][16781]][16782]
[][16783]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][16784]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
Remove the screw next to the USB port and slide the back cover away. Make sure to not break the thin speaker wires. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][16784].
# Pictures
  * [![Tab730-front.jpeg][16785]][16747]
  * [![Tab730-back.jpeg][16786]][16787]
  * [![Tab730-buttons.jpeg][16788]][16789]
  * [![Tab730-inside.jpeg][16790]][16791]
  * [![Device board back.jpg][16792]][16793]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
Sophix TAB-730g 
# See also
  * [FCC application documents][16794]
  * [iFixit page][16795]

## Manufacturer images
Optional. Add non-sunxi images in this section.
