# Transpeed 8K618-T
Transpeed 8K618-T  
---  
[![Transpeed 8k front.jpg][55653]][55654]  
Manufacturer |  Transpeed?   
Dimensions |  100 _mm_ x 100 _mm_ x 22 _mm_  
Release Date |  2023   
Website |  _unknown_  
Specifications   
SoC |  [H618][55655] @ 1.5 Ghz   
DRAM |  2GiB/4GiB DDR3L-1600 @ 648 MHz (8 * Micron MT41K1G4RH-125:E)   
eMMC |  16/32/64/128 GiB eMMC 5.1   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full), CVBS   
Audio |  3.5mm headphone plug, HDMI   
Network |  WiFi (HK2735M), 100Mbps Ethernet (integrated H616 PHY)   
Storage |  µSD, eMMC   
USB |  2 X USB2.0 Host   
Headers |  UART header pads   
Cheap TV box, an example of various very similar devices, shipped under different names. 
## Contents
  * [1 Identification][55656]
  * [2 Sunxi support][55657]
    * [2.1 Current status][55658]
    * [2.2 Manual build][55659]
      * [2.2.1 Mainline U-Boot][55660]
      * [2.2.2 Mainline Linux Kernel][55661]
  * [3 Tips, Tricks, Caveats][55662]
    * [3.1 FEL mode][55663]
  * [4 Adding a serial port (**voids warranty**)][55664]
    * [4.1 Device disassembly][55665]
    * [4.2 Locating the UART][55666]
  * [5 Pictures][55667]
  * [6 Also known as][55668]
  * [7 See also][55669]
    * [7.1 Manufacturer images][55670]

# Identification
On the back of the device, the following is printed: 
[code] 
    Transpeed
    MODEL: 8K618-T    RAM: 4GB
    DC IN: 5V         ROM: 64GB
[/code]
The PCB has the following silkscreened on it: 
[code] 
    Fx-H618-D4-V10
    2023-03-21
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _8K618-T_
  * Android TV OS version: _12_
  * Android TV OS build: _SP1A.211105.004_

# Sunxi support
## Current status
Many features are already supported by the mainline kernel (eMMC, SD card, USB, WiFi), though video, audio and Ethernet (PHY) are missing, for the [H616/H618][55671] in general. Just needs the DTB to run on mainline builds since Linux v6.5 (required for the AXP313a PMIC support). 
## Manual build
You can build things for yourself by following our [ Manual build howto][55672] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _transpeed-8k618-t_defconfig_ build target. Available since v2024.04-rc1. 
### Mainline Linux Kernel
Use the _sun50i-h618-transpeed-8k618-t.dtb_ devicetree binary from a mainline kernel, available since v6.8-rc1. Requires at least v6.5 for the AXP PMIC support. 
# Tips, Tricks, Caveats
## FEL mode
There is a FEL button on the PCB (behind the AV socket), it can be reached by a non-conductive tool like a toothpick through the AV socket. Alternatively, enter FEL mode with the fel-sdboot.sunxi image written to an SD card. 
The USB socket next to the SD card is connected to USB controller 0, a non-standard USB A-to-A cable can be used to connect using FEL. 
# Adding a serial port (**voids warranty**)
[![][55673]][55674]
[][55675]
Transpeed 8K618-T UART pads
## Device disassembly
Use a [Plastic tool][55676] to move around the lid on the top, to pop open three brackets at the front and the back of the device. 
## Locating the UART
The UART pins are clearly marked with RX, TX, GND on three easy to solder pins on the PCB. 
# Pictures
  * [![Transpeed 8k front.jpg][55677]][55654]
  * [![Transpeed 8k bottom.jpg][55678]][55679]
  * [![Transpeed 8k side.jpg][55680]][55681]
  * [![Transpeed 8k top.jpg][55682]][55683]
  * [![Transpeed 8k rear.jpg][55684]][55685]
  * [![Transpeed 8k pcb top.jpg][55686]][55687]
  * [![Transpeed 8k pcb bottom.jpg][55688]][55689]
  * [![Transpeed 8k pcb dram.jpg][55690]][55691]
  * [![Transpeed 8k pcb wifi emmc.jpg][55692]][55693]

# Also known as
Probably very similar, if not identical to other H618 TV boxes, especially those with a display at the front, the two USB sockets on the side, and no SPDIF socket. 
With the H618 being designed for TV boxes, there are not many variations to come up with for a cheap design. The AXP313 PMIC used in those boxes (with the H618 SoC) has really little wiggle room for customisation, so all rails need to be enabled all the time, and the voltages are pretty fixed, for practical purposes. There could be variations in the WiFi chip, and in the DRAM chips used, although cost pressure probably leads to DDR3 DRAM chips being used. 
# See also
## Manufacturer images
