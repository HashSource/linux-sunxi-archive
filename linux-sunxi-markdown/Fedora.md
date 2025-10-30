# Fedora
## Contents
  * [1 Installation][19286]
  * [2 Fedora 22 officially supported boards][19287]
  * [3 Not supported boards][19288]
  * [4 Caveats][19289]

# Installation
Fedora now have official support for ARM devices, the different images are [here][19290] and the installation instructions [here][19291]. 
Note that [RPM Fusion][19292] repositories are also available for ARM. 
# Fedora 22 officially supported boards
[Olimex_A10-OLinuXino-Lime][19293]  
[Olimex_A20-OLinuXino-Lime][19294]  
[Olimex_A20-OLinuXino-Lime2][19295]  
[Olimex A20-OLinuXino-Micro][19296]  
[LeMaker_Banana_Pi][19297]  
[LeMaker_Banana_Pro][19298]  
[Cubietech_Cubieboard][19299]  
[Cubietech_Cubieboard2][19300]  
[Cubietech_Cubietruck][19301]  
[Mele A1000][19302]  

# Not supported boards
If your board isn't supported, you can anyway install Fedora if it is supported by u-boot and you have the corresponding device tree file. 
  1. Copy Fedora image on your SD card with [this instructions][19303].
  2. Compile u-boot [following this instructions][19304].
  3. Install u-boot on your SD card: 
[code]sudo dd if=/Some Path/uboot/u-boot-sunxi-with-spl.bin of=/dev/YOURSDCARD bs=1024 seek=8 conv=fsync,notrunc 
[/code]
  4. Copy dtb to your SD card boot partition in each kernel dtb folder, for example with 4.0.4-301: 
[code]sudo cp /Some Path/uboot/arch/arm/dts/YOUR_DTB_FILE.dtb /YOUR_SDCARD_BOOT_PARTITION/dtb-4.0.4-301.fc22.armv7hl/ 
[/code]

You will have to copy your dtb file in the new kernel folder after each kernel update, unless if somebody have a better solution? 
# Caveats
Don't try to install the Workstation or the kde image on Allwinner devices due to the poor graphical performance it won't work.
