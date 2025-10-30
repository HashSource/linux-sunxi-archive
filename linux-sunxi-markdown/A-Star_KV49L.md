# A-Star KV49L
A-Star KV49L  
---  
[![A-Star KVT49L Front.jpg][209]][210]  
Manufacturer |  [A-Star]   
Dimensions |  200 _mm_ x 100 _mm_ x 10 _mm_  
Release Date |  July 2014   
Website |  Missing device product page.   
Specifications   
SoC |  [A33][211] @ 1.5Ghz   
DRAM |  1024 MiB DDR3 @ xxxMHz   
NAND |  8 GiB   
Power |  DC 5V @ 3A, 5500mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (8" 10:6)   
Touchscreen |  X-finger capacitive ([Silead GSL1680][212])   
Video |  N/A   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([ExpressIf ESP8089][213]))   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) (gc0308) front,2.0MP (1600x1200) (GC2035) rear   
Other |  Accelerometer ([Sensortek STK8312][214])   
Headers |  N/A   
This page needs to be properly filled according to the [New Device Howto][215] and the [New Device Page guide][216].
## Contents
  * [1 Identification][217]
  * [2 Sunxi support][218]
    * [2.1 Current status][219]
    * [2.2 Manual build][220]
      * [2.2.1 U-Boot][221]
        * [2.2.1.1 Sunxi/Legacy U-Boot][222]
        * [2.2.1.2 Mainline U-Boot][223]
      * [2.2.2 Linux Kernel][224]
        * [2.2.2.1 Sunxi/Legacy Kernel][225]
        * [2.2.2.2 Mainline kernel][226]
  * [3 Tips, Tricks, Caveats][227]
    * [3.1 FEL mode][228]
    * [3.2 Retrieving script.bin][229]
  * [4 Adding a serial port (**voids warranty**)][230]
    * [4.1 Device disassembly][231]
    * [4.2 Locating the UART][232]
  * [5 Pictures][233]
  * [6 Also known as][234]
  * [7 See also][235]
    * [7.1 Manufacturer images][236]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    M102_MB V1.0
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _QUAD-CORE A33 y3_
  * Build Number: _astar-y3-eng 4.4.2 KVT49L_

# Sunxi support
## Current status
None currently, [A33][211] is not supported yet. 
## Manual build
You can build things for yourself by following our [ Manual build howto][237] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][238]file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][239]. 
## Retrieving script.bin
Unlike older Allwinner devices, this device only has some basic images on the nanda partition. This means that u-boot and script.bin are living elsewhere. 
# Adding a serial port (**voids warranty**)
[![][240]][241]
[][242]
DEVICE UART pads
## Device disassembly
The device has no screws, the cover is 'clicked' on the screen. A suction cup and a little wiggling with the soft back shell quickly and easily removes the rear cover. You might want to use a [Plastic tool][243] as well. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][244].
# Pictures
  * [![A-Star KVT49L Front.jpg][245]][210]
  * [![A-Star KVT49L Inside.jpg][246]][247]
  * [![A-Star KVT49L PCB top.jpg][248]][249]
  * [![A-Star KVT49L PCB bottom.jpg][250]][251]
  * [![A-Star KVT49L PCB top left.jpg][252]][253]
  * [![A-Star KVT49L PCB top right.jpg][254]][255]
  * [![A-Star KVT49L PCB bottom left.jpg][256]][257]
  * [![A-Star KVT49L PCB bottom right.jpg][258]][259]

# Also known as
Takara MID 109 
iDeaPLAY DF1002 
# See also
## Manufacturer images
