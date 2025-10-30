# TrimUI Model S
TrimUI Model S  
---  
[![Trimui model s front.jpg][55726]][55727]  
Manufacturer |  [TrimUI][55728]  
Dimensions |  105 _mm_ x 55 _mm_ x 9.5 _mm_  
Release Date |  2020   
Website |  [Device Product Page][55728]  
Specifications   
SoC |  [F1C200s][55729] @ XGhz   
DRAM |  64MiB DDR1 @ xxxMHz   
NAND |  128MB   
Power |  DC 5V @ 500mA, 600mAh 3.7V Li-Ion battery   
Features   
LCD |  320x240 (2.0" 3:4)   
Audio |  internal speaker   
Storage |  µSD   
USB |  1 USB2.0 Type-C OTG   
This page needs to be properly filled according to the [New Device Howto][55730] and the [New Device Page guide][55731].
A small portable game console, designed to run retro game emulators (NES, Gameboy, etc). 
## Contents
  * [1 Identification][55732]
  * [2 Sunxi support][55733]
    * [2.1 Current status][55734]
    * [2.2 Images][55735]
    * [2.3 HW-Pack][55736]
    * [2.4 BSP][55737]
    * [2.5 Manual build][55738]
      * [2.5.1 U-Boot][55739]
        * [2.5.1.1 Sunxi/Legacy U-Boot][55740]
        * [2.5.1.2 Mainline U-Boot][55741]
      * [2.5.2 Linux Kernel][55742]
        * [2.5.2.1 Sunxi/Legacy Kernel][55743]
        * [2.5.2.2 Mainline kernel][55744]
  * [3 Tips, Tricks, Caveats][55745]
    * [3.1 FEL mode][55746]
    * [3.2 Device specific topic][55747]
    * [3.3 ...][55748]
  * [4 Adding a serial port (**voids warranty**)][55749]
    * [4.1 Device disassembly][55750]
    * [4.2 Locating the UART][55751]
  * [5 Pictures][55752]
  * [6 Schematic][55753]
  * [7 Also known as][55754]
  * [8 See also][55755]
    * [8.1 Manufacturer images][55756]

# Identification
"TRIMUI MODEL S" is printed on the back of the device as well as the front of the PCB (visible through the clear front casing) 
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][55755]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][55757] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][55758] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
Turn off the device, remove the uSD card. The uSD card **must** be removed, otherwise the device will boot normally. Hold the "L" and "R" shoulder buttons while turning the device on. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][55759]][55760]
[][55761]
TrimUI Model S UART pads
There are UART test pads inside the device. You will need to solder jumper wires to access them, see [UART howto][55762] for details. 
## Device disassembly
Unscrew the four self-tapping Torx T6 screws from the back of the device. Remove the aluminum back panel and the plastic spacer. 
## Locating the UART
The UART test pads are near the NAND flash chip, labeled U1_RX, U1_TX, and GND. 
# Pictures
Take some pictures of your device, [ upload them][55763], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][55764]][55765]
  * [![Device back.jpg][55766]][55767]
  * [![Device buttons 1.jpg][55768]][55769]
  * [![Device buttons 2.jpg][55770]][55771]
  * [![Device board front.jpg][55772]][55773]
  * [![Device board back.jpg][55774]][55775]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
PowKiddy A66 
# See also
Unofficial wiki: <https://github.com/tiduscrying/trimui-model-s-wiki>
## Manufacturer images
<http://trimui.com/page.php?id=2>
