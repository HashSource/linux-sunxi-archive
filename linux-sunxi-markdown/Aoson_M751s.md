# Aoson M751s
Aoson M751s  
---  
[![Aoson M751S Front.jpg][7837]][7838]  
Manufacturer |  [Aoson][7839]  
Dimensions |  8.6 _mm_ x 190 _mm_ x 130 _mm_  
Release Date |  Dec 2015   
Website |  N/A (There's no device page on the manufacturer's website)   
Specifications   
SoC |  [A33][7840] @ 1.34Ghz   
DRAM |  512MiB DDR3 @ 360MHz   
NAND |  8GB   
Power |  DC 5V @ 2A, 2200mAh 3.7V Li-Ion battery, Micro USB   
Features   
LCD |  800x480 (7" 5:3)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][7841])   
Video |  N/A   
Audio |  3.5mm headphone plug, internal speaker   
Network |  WiFi 802.11 b/g/n ([ExpressIf ESP8089][7842]))   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  30.0MP (640x480) front, 30.0MP (640x480) rear   
Other |  Accelerometer ([Mma8652][7843])   
Headers |  LCD   
## Contents
  * [1 Identification][7844]
  * [2 Sunxi support][7845]
    * [2.1 Current status][7846]
    * [2.2 Manual build][7847]
      * [2.2.1 U-Boot][7848]
        * [2.2.1.1 Mainline U-Boot][7849]
      * [2.2.2 Linux Kernel][7850]
        * [2.2.2.1 Mainline kernel][7851]
        * [2.2.2.2 Customized kernel based on Allwinner official SDK][7852]
        * [2.2.2.3 BSP Kernel][7853]
  * [3 Tips, Tricks, Caveats][7854]
    * [3.1 FEL mode][7855]
    * [3.2 Device disassembly][7856]
    * [3.3 UART][7857]
    * [3.4 Interesting things][7858]
    * [3.5 Note about the accessories][7859]
  * [4 Pictures][7860]
  * [5 Also known as][7861]
  * [6 See also][7862]
    * [6.1 Manufacturer images][7863]

# Identification
On the back of the device, the following is printed: 
[code] 
    aoson
[/code]
The PCB has the following silkscreened on it: 
[code] 
    AL-AX3-751B-V1.0
    2015.03.26
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _M751S-B_
  * Build Number: _aster_ococci-eng 4.4.2 KVT49L 20151008_

It has a Q8-like design, but its buttons are at the same side (left, in the default orientation). 
# Sunxi support
## Current status
None currently, A33 is not supported yet. 
## Manual build
You can build things for yourself by following our [ Manual build howto][7864] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
  * For building u-boot, use the _q8_a33_tablet_800x480_defconfig_ target.

### Linux Kernel
#### Mainline kernel
Use the sun8i-a33-q8-tablet.dtb device-tree binary. 
#### Customized kernel based on Allwinner official SDK
[[1]][7865] includes a customized sdk kernel for m751s along with its config. It requires AOSC OS and its cross-compile toolchain. 
#### BSP Kernel
Use the [aoson_m751s.fex][7866] file. 
# Tips, Tricks, Caveats
## FEL mode
The Vol+ button triggers [ FEL mode][7867]. 
## Device disassembly
It's disassembly is just like Q8 devices. Look for [Format_Q8#Disassembly][7868] for reference. 
Note: Do not start from the side of the screen, otherwise you may break the touchscreen! 
## UART
It seems that no UART pads are available. 
## Interesting things
This pad is claimed to have different SoCs on different websites in China, from RK3288 to A33, and when it's disassembled, the A33 SoC and AXP223 PMIC is covered by stickers. 
## Note about the accessories
The USB-OTG Cable in the device box is too unstable for data transmission. If possible, use another one to replace it. 
# Pictures
  * [![Aoson M751S Front.jpg][7869]][7838]
  * [![Aoson M751S Back.jpg][7870]][7871]
  * [![Aoson M751S Buttons.jpg][7872]][7873]
  * [![Aoson M751S PCB.jpg][7874]][7875]

# Also known as
# See also
[A33][7840]
## Manufacturer images
[PhoenixSuit image][7876]
