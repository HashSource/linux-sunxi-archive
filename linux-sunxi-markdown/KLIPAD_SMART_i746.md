# KLIPAD SMART i746
KLIPAD SMART i746  
---  
[![KLIPAD I746 FRONT.jpeg][29320]][29321]  
Manufacturer |  Klipad [[1]][29322]  
Dimensions |  width _189mm_ x length _119mm_ x height _11mm_  
Release Date |  2018  
Website |  klipad.fr [[2]][29323]  
Specifications   
SoC |  [A64][29324] @ 1.152Ghz   
DRAM |  1GiB DDR3   
NAND |  8GB   
Power |  DC 5V @ 1.5A, 2500mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (7" X:Y)   
Touchscreen |  X-finger capacitive ([Manufacturer device][29325])   
Video |  None   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n and Bluetooth ([RTL8703BS][29326])   
Storage |  µSD   
USB |  1 x USB2.0 OTG   
Camera |  2MP GC2035 front, 0.3MP rear   
Other |  Accelerometer ([Manufacturer device][29327])   
This page needs to be properly filled according to the [New Device Howto][29328] and the [New Device Page guide][29329].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][29330]
  * [2 Sunxi support][29331]
    * [2.1 Current status][29332]
    * [2.2 Images][29333]
    * [2.3 Manual build][29334]
      * [2.3.1 U-Boot][29335]
        * [2.3.1.1 Sunxi/Legacy U-Boot][29336]
        * [2.3.1.2 Mainline U-Boot][29337]
      * [2.3.2 Linux Kernel][29338]
        * [2.3.2.1 Sunxi/Legacy Kernel][29339]
        * [2.3.2.2 Mainline kernel][29340]
  * [3 Tips, Tricks, Caveats][29341]
    * [3.1 FEL mode][29342]
    * [3.2 Device specific topic][29343]
    * [3.3 ...][29344]
  * [4 Adding a serial port (**voids warranty**)][29345]
    * [4.1 Device disassembly][29346]
    * [4.2 Locating the UART][29347]
  * [5 Pictures][29348]
  * [6 Also known as][29349]
  * [7 See also][29350]
    * [7.1 Manufacturer images][29351]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    - KLIVER -
    Model: KL3839/I746
[/code]
The PCB has the following silkscreened on it: 
[code] 
    YA7001B R600
    2018-02-06
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Nothing yet 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][29350]. If no sunxi based images are available, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][29352] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][29353] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The Volume+ and Power buttons trigger [ FEL mode][29354]. Press and hold `Volume+` Press and hold `Power` for about 2 seconds Release `Power` and press it again 3 times immediately 
## Device specific topic
If there are no further device specific topics to add, remove these sections. Delivered with a keyboard 
## ...
# Adding a serial port (**voids warranty**)
[![][29355]][29356]
[][29357]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][29358]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning. Not found how to add a serial port on this device. 
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][29359]. Warning, plastic is not great. Almost every pins were broken after disassembly. Disassemble by pressing a pry tool between the screen and the back of the tablet. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][29358]. Not found 
# Pictures
Take some pictures of your device, [ upload them][29360], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![KLIPAD I746 FRONT.jpeg][29361]][29321]
  * [![KLIPAD I746 BACK.jpg][29362]][29363]
  * [![Device buttons 1.jpg][29364]][29365]
  * [![Device buttons 2.jpg][29366]][29367]
  * [![KLIPAD SMART I746 INSIDE.jpg][29368]][29369]
  * [![Device board back.jpg][29370]][29371]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
