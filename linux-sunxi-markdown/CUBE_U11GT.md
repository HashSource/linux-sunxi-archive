# CUBE U11GT
CUBE U11GT  
---  
[![CUBE U11GT Front.jpg][11337]][11338]  
Manufacturer |  [CUBE][11339]  
Dimensions |  194 _mm_ x 119 _mm_ x 11 _mm_  
Release Date |  December 2011   
Specifications   
SoC |  [A10][11340] @ 1Ghz   
DRAM |  512MiB DDR3 @ 360MHz   
NAND |  8GB   
Power |  DC 5V @ 2A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 15:9)   
Touchscreen |  5-finger capacitive ([Goodix GT801][11341])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][11342])   
Storage |  µSD   
USB |  0 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Freescale MMA7660][11343])   
This page needs to be properly filled according to the [New Device Howto][11344] and the [New Device Page guide][11345].
It has a Home Button on its front side. 
## Contents
  * [1 Identification][11346]
  * [2 Sunxi support][11347]
    * [2.1 Current status][11348]
    * [2.2 Manual build][11349]
      * [2.2.1 U-Boot][11350]
        * [2.2.1.1 Sunxi/Legacy U-Boot][11351]
        * [2.2.1.2 Mainline U-Boot][11352]
      * [2.2.2 Linux Kernel][11353]
        * [2.2.2.1 Sunxi/Legacy Kernel][11354]
        * [2.2.2.2 Mainline kernel][11355]
  * [3 Tips, Tricks, Caveats][11356]
    * [3.1 FEL mode][11357]
    * [3.2 Adding USB Host port][11358]
    * [3.3 ...][11359]
  * [4 Adding a serial port (**voids warranty**)][11360]
    * [4.1 Device disassembly][11361]
    * [4.2 Locating the UART][11362]
  * [5 Pictures][11363]
  * [6 Also known as][11364]
  * [7 See also][11365]
    * [7.1 Manufacturer images][11366]

# Identification
On the back of the device, the following is printed: 
[code] 
    酷比魔方
    CUBE U11GT Made in China
[/code]
The PCB has the following silkscreened on it: 
[code] 
    U11GT V0.3
    2011-11-04
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _U11GT_

# Sunxi support
## Current status
Not supported. 
## Manual build
You can build things for yourself by following our [ Manual build howto][11367] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][11368] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The ESC button triggers [ FEL mode][11369]. 
## Adding USB Host port
This device has an empty USB Host pad. A guy tried soldering it. Link (in Chinese): [[1]][11370]
## ...
# Adding a serial port (**voids warranty**)
[![][11371]][11372]
[][11373]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][11374]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
This tablet only uses clips to hold its back, so be cautious and follow [Plastic tool howto][11375]. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][11374].
# Pictures
  * [![CUBE U11GT Front.jpg][11376]][11338]
  * [![CUBE U11GT Back.jpg][11377]][11378]
  * [![CUBE U11GT Buttons.jpg][11379]][11380]
  * [![CUBE U11GT Ports.jpg][11381]][11382]
  * [![CUBE U11GT Inside.jpg][11383]][11384]
  * [![CUBE U11GT PCB 1.jpg][11385]][11386]
  * [![CUBE U11GT PCB 2.jpg][11387]][11388]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
[v1.05 (android 2.3)][11389]
[v1.06 (android 4.0.3)][11390]
