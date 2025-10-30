# TZX-723Qa4
TZX-723Qa4  
---  
Manufacturer |  Haehne?   
Dimensions |  196.3 _mm_ x 120.8 _mm_ x 9 _mm_  
Website |  Missing product page.   
Specifications   
SoC |  [A33][53739] @ 1.6Ghz   
DRAM |  512MiB DDR3   
NAND |  16GB   
Power |  DC 5V @ 1.5A, 200mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][53740])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([RDA Microelectronics RDA5991][53741]),   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3 MP front, 2 MP rear   
Other |  Accelerometer ([Manufacturer device][53742])   
This page needs to be properly filled according to the [New Device Howto][53743] and the [New Device Page guide][53744].
A [Q8 style][53745] cheap tablet, but with an [A33][53739] SoC. 
## Contents
  * [1 Identification][53746]
  * [2 Sunxi support][53747]
    * [2.1 Current status][53748]
    * [2.2 Images][53749]
    * [2.3 HW-Pack][53750]
    * [2.4 BSP][53751]
    * [2.5 Fex file][53752]
    * [2.6 Manual build][53753]
    * [2.7 Mainline U-Boot][53754]
    * [2.8 Mainline kernel][53755]
  * [3 Tips, Tricks, Caveats][53756]
    * [3.1 Retrieving script.bin][53757]
  * [4 Adding a serial port (**voids warranty**)][53758]
    * [4.1 Device disassembly][53759]
  * [5 Pictures][53760]
  * [6 See also][53761]

# Identification
On the back of the device, the following is printed: 
[code] 
    The PCB has the following written on it:
    TZX-723Qa4
    
[/code]
  

# Sunxi support
## Current status
Following devices are unsupported: 
  * Wifi RDA5991
  * GSL1680 touch input
  * Accelometer Dmard09 or bma150?

## Images
## HW-Pack
## BSP
## Fex file
## Manual build
  * For building u-boot, use the _q8_a33_tablet_1024x600_defconfig_ target.
  * The .fex file can be found in sunxi-boards as [TZX-723Qa4.fex][53762]

## Mainline U-Boot
Supported in the [mainline u-boot git 'master' branch][53763]. 
## Mainline kernel
Use the _sun8i-a33-q8-tablet.dts_ device-tree file for the [mainline kernel][53764]. 
# Tips, Tricks, Caveats
## Retrieving script.bin
Unlike, other allwinner devices,Script.bin is not present in the vfat partition(nanda) as file. 
Instead, It is located 0x43000000, it's size is 0x00020000. script.bin can be extracted from /dev/mem using mmap(). 
# Adding a serial port (**voids warranty**)
[![][53765]][53766]
[][53767]
Serial connected to board
## Device disassembly
# Pictures
# See also
  * [Other Q8 format A33 based tablets.][53768]
