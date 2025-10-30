# Xiaomi-RoboRock-V1
Xiaomi-RoboRock-V1  
---  
[![Device front.jpg][60099]][60100]  
Manufacturer |  [Manufacturer][60101]  
Release Date |  Month year  
Website |  [Device Product Page][60102]  
Specifications   
SoC |  [A33][60103] @ XGhz   
DRAM |  512MiB DDR3 @ 600MHz   
NAND |  4GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
Audio |  internal speaker   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][60104])   
Storage |  eMMC   
USB |  1 USB2.0 Host(OTG)   
Other |  A lot of sensors   
This page needs to be properly filled according to the [New Device Howto][60105] and the [New Device Page guide][60106].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
Device is special, because its a vacuum cleaner :) 
## Contents
  * [1 Identification][60107]
  * [2 Sunxi support][60108]
    * [2.1 Current status][60109]
    * [2.2 Images][60110]
    * [2.3 Manual build][60111]
      * [2.3.1 U-Boot][60112]
        * [2.3.1.1 Mainline U-Boot][60113]
      * [2.3.2 Linux Kernel][60114]
        * [2.3.2.1 Mainline kernel][60115]
  * [3 Tips, Tricks, Caveats][60116]
    * [3.1 FEL mode][60117]
    * [3.2 ...][60118]
  * [4 Adding a serial port (**voids warranty**)][60119]
    * [4.1 Device disassembly][60120]
  * [5 See also][60121]
    * [5.1 Manufacturer images][60122]

# Identification
# Sunxi support
WIP 
## Current status
Mainline U-Boot is working, Kernel needs some finetuning(24.3.2019) 
  

## Images
## Manual build
You can build things for yourself by following our [ Manual build howto][60123] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _Xiaomi_RockRobo_V1_defconfig_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _sun8i-r16-xiaomi-roborock-v1.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Attention: Device uses a special FEL-Configuration. You can find the FEL-File here: <https://github.com/dgiese/dustcloud-documentation/blob/master/rockrobo.vacuum.v1/script.bin.txt>
The configuration is special, because it has a disabled MMC0. MMC2 is the main storage. 
## FEL mode
You will need to solder UART-Headers to access FEL-Mode. 
  

## ...
# Adding a serial port (**voids warranty**)
Can be found here: <https://github.com/dgiese/dustcloud-documentation/blob/master/rockrobo.vacuum.v1/photos/UART-soldered-hack/IMG_20170813_220256a.jpg>
Explanation is here: <https://github.com/dgiese/dustcloud-documentation/blob/master/rockrobo.vacuum.v1/techinfo.pdf>
## Device disassembly
Can be found here: <https://github.com/dgiese/dustcloud-documentation/blob/master/rockrobo.vacuum.v1/techinfo.pdf>
  

# See also
## Manufacturer images
Optional. Add non-sunxi images in this section.
