# DongshanPi Nezha STU
DongshanPi Nezha STU  
---  
[![Dongshanpi-nezha-stu-diy.jpg][17126]][17127]  
Manufacturer |  [DongshanPi][17128]  
Dimensions |  ?_mm_ x ?_mm_  
Release Date |  ?   
Website |  [Home Page in Chinese][17129]  
Specifications   
SoC |  [D1][17130] @ 1.0Ghz   
DRAM |  512MiB DDR3 @ 792MHz, 1×[H5TQ4G63EFR][17131]  
Power |  DC 5V @ 2A (via OTG Type-C connector)   
Features   
Video |  HDMI (Type A - full)   
Audio |  audio, HDMI, I2S   
Network |  ethernet   
Storage |  µSD, optional SPI flash   
USB |  1 USB Type-C OTG, 1 USB Type-C USB serial   
Other |  Power LED, system LED, OK & FEL buttons   
This page needs to be properly filled according to the [New Device Howto][17132] and the [New Device Page guide][17133].
There is a carrier board named "DIY" with three 2x20 GPIO connector headers of varying pin assignments. 
At the bottom are solder pads for a SPI flash, NAND or NOR. A white dot in the top left marks pin 1 (CS). You can order a variant that includes a NAND flash. 
  * [stock firmware boot log][17134]
  * [schematic][17135]

## Software Support
Linux and U-Boot upstreaming are in progress. See [Allwinner_Nezha#Manual_build][17136] for build instructions. For U-Boot, use the `dongshan_nezha_stu_defconfig` configuration.
