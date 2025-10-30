# Sencor Element 7 V3
Sencor Element 7 V3  
---  
[![SE7V3 front.jpg][49156]][49157]  
Manufacturer |  [Sencor][49158]  
Dimensions |  182 _mm_ x 121 _mm_ x 11 _mm_  
Release Date |  April 2013   
Website |  [Device Product Page][49159]  
Specifications   
SoC |  [A13][49160] @ 1Ghz   
DRAM |  512MiB DDR3 @ 384MHz ([Elpida J2108BCSE-DJ-F][49161])   
NAND |  4GB   
Power |  DC 5V @ 1.5A, 3250mAh 3.7V Li-Pol battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][49162])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Ralink RT5370N][49163])   
Storage |  µSD   
USB |  USB2.0 OTG   
Camera |  0.3MPx (640x480) front   
Other |  Accelerometer ([Freescale MMA7660][49164])   
Headers |  UART   
_Sencor Element 7 version 3_ is a standard [Q8 format][49165], [A13][49160] based tablet. 
## Contents
  * [1 Identification][49166]
  * [2 Sunxi support][49167]
    * [2.1 Current status][49168]
    * [2.2 Manual build][49169]
      * [2.2.1 U-Boot][49170]
        * [2.2.1.1 Sunxi/Legacy U-Boot][49171]
        * [2.2.1.2 Mainline U-Boot][49172]
      * [2.2.2 Linux Kernel][49173]
        * [2.2.2.1 Sunxi/Legacy Kernel][49174]
        * [2.2.2.2 Mainline kernel][49175]
  * [3 Tips, Tricks, Caveats][49176]
    * [3.1 FEL mode][49177]
    * [3.2 Hardware problems][49178]
  * [4 Adding a serial port (**voids warranty**)][49179]
    * [4.1 Device disassembly][49180]
    * [4.2 Locating the UART][49181]
  * [5 Pictures][49182]
  * [6 Also known as][49183]
  * [7 See also][49184]
    * [7.1 Manufacturer images][49185]

# Identification
On the back of the device, the following is printed: 
[code] 
    element 7
    version 3
    
    SENCOR®
    Internet Tablet with 7" Capacitive display
    and 4GB Memory
[/code]
The PCB has the following silkscreened on it: 
[code] 
    SAQ8-A13 V1.2
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _ELEMENT 7V3_
  * Build Number: _nuclear_evb-eng 4.0.4 GC0308_5370_1680_7660_MSM_

# Sunxi support
## Current status
Supported, but lacks [ mainline kernel support][49175] and likely some driver support in [ sunxi kernel][49174]. 
## Manual build
You can build things for yourself by following our [ Manual build howto][49186] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _q8_a13_tablet_ build target. 
#### Mainline U-Boot
Use the _q8_a13_tablet_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_sencor_element7v3.fex_][49187] file. 
#### Mainline kernel
Use the _sun5i-a13-sencor-element7v3.dts_ device-tree binary.
# Tips, Tricks, Caveats
## FEL mode
Either **Vol+** or **Vol-** button triggers [ FEL mode][49188]. Simply hold the button and then connect to the USB port. 
No success entering Boot1 for me, but [./fel version][49189], [LiveSuit/PhoenixSuit flashing][49190] and [booting over USB][49191] works fine. 
## Hardware problems
The device is of typical cheap chinese quality, so if you happen to be already inside it playing god, it may be worthwhile to [check for hardware problems][49192]. 
# Adding a serial port (**voids warranty**)
[![][49193]][49194]
[][49195]
Element7's UART pads
## Device disassembly
Identical with [Q8 Format disassembly][49196]. To access the PCB backside, unplug the three flex cables and unscrew the three PH0 screws. Turn the board over on the battery, then remove the plastic cover glued to the backside. 
## Locating the UART
UART solder pads are in the middle on the back-side of the PCB. Device's TX is the one closer to the USB port. 
Note 1: I am receiving no output during boot or Boot0 FEL mode; only [serial_noise][49197] seems to work for me. It maps to /dev/ttyS1 (so it needs editing the [script.bin][49198] or the kernel arguments). 
Note 2: The diagnostic pads are easily torn off from the PCB (maybe not suitable for soldering to). 
If despite those caveats you decide to try for yourself, here's how: [UART howto][49199]. 
# Pictures
  * [![SE7V3 front.jpg][49200]][49157]
  * [![SE7V3 back.jpg][49201]][49202]
  * [![SE7V3 buttons.jpg][49203]][49204]
  * [![SE7V3 board front.jpg][49205]][49206]
  * [![SE7V3 board back.jpg][49207]][49208]

# Also known as
# See also
  * [Other Q8 format A13 based tablets.][49209]

## Manufacturer images
  * [Stock ROM (tested ok, but unknown source!)][49210]
