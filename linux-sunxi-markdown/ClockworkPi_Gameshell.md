# ClockworkPi Gameshell
ClockworkPi Gameshell  
---  
Manufacturer |  [Clockwork Tech LLC][12915]  
Dimensions |  82 _mm_ x 135 _mm_ x 21 _mm_  
Release Date |  August 2019   
Website |  [Device Product Page][12915]  
Specifications   
SoC |  [A33][12916] [R16][12917] @ 1.2Ghz   
DRAM |  1G DDR3   
Power |  DC 5V @ 2A, 1200mAh 3.7V Li-Ion battery   
Features   
LCD |  320x240 2.7 inch TFT RGB@60fps Screen   
Video |  Mali400 MP2 GPU, micro-HDMI   
Audio |  3.5mm headphone plug, internal mono speaker   
Storage |  µSD   
USB |  1 USB Host   
Other |  17 GPIO Buttons, 1 Charging LED, 1 Power LED , PMIC [AXP223][12918]  
Headers |  TFT, Battery, Speaker   
## Contents
  * [1 Identification][12919]
  * [2 Sunxi support][12920]
    * [2.1 Current status][12921]
    * [2.2 Images][12922]
    * [2.3 HW-Pack][12923]
    * [2.4 BSP][12924]
    * [2.5 Manual build][12925]
      * [2.5.1 U-Boot][12926]
        * [2.5.1.1 Sunxi/Legacy U-Boot][12927]
        * [2.5.1.2 Mainline U-Boot][12928]
      * [2.5.2 Linux Kernel][12929]
        * [2.5.2.1 Sunxi/Legacy Kernel][12930]
        * [2.5.2.2 Mainline kernel][12931]
    * [2.6 FEL mode][12932]
    * [2.7 Device specific topic][12933]
    * [2.8 ...][12934]
  * [3 Using a serial port][12935]
    * [3.1 Device disassembly][12936]
    * [3.2 Locating the UART][12937]
  * [4 Pictures][12938]
  * [5 Schematic][12939]
  * [6 Also known as][12940]
  * [7 See also][12941]
    * [7.1 Manufacturer images][12942]

# Identification
On the front of the device, the following is printed: 
[code] 
    clockwork
    GameSH>
    Modular Portable Game Console
[/code]
The PCB has the following silkscreened on it: 
[code] 
    CP13.1
[/code]
  

[code] 
    uname -a
    Linux clockworkpi  5.7.0-clockworkpi-cpi3-g5c715d2cd-dirty #1 SMP Sun Jul 12 20:21:02 CEST 2020 armv7l GNU/Linux
[/code]
# Sunxi support
## Current status
Building and running your own build of u-boot and Linux is currently unsupported. The device seems to be running a custom build of u-boot and Linux version 5.7.0. 
## Images
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][12943] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][12944] file. 
#### Mainline kernel
Use the patches from <https://github.com/clockworkpi/Kernel> or <https://github.com/wolfallein/clockworkpi-debian/>
_FAMILY-CHIP-DEVICE.dtb_ device-tree binary. <https://github.com/wolfallein/clockworkpi-debian/blob/master/bin/kernel/5.7/sun8i-r16-clockworkpi-cpi3.dtb> & <https://github.com/wolfallein/clockworkpi-debian/blob/master/bin/kernel/5.7/sun8i-r16-clockworkpi-cpi3-hdmi.dtb>
## FEL mode
The something button triggers [ FEL mode][12945]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Using a serial port
[![][12946]][12947]
[][12948]
ClockworkPi UART pads
To use the UART, you can use the pins on the side of the board, follow [Stuarts's guide][12949] or [the post on the forum][12950]. See [UART howto][12951] for generic UART instructions. 
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][12952].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][12951].
# Pictures
Take some pictures of your device, [ upload them][12953], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][12954]][12955]
  * [![Device back.jpg][12956]][12957]
  * [![Device buttons 1.jpg][12958]][12959]
  * [![Device buttons 2.jpg][12960]][12961]
  * [![Device board front.jpg][12962]][12963]
  * [![Device board back.jpg][12964]][12965]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
