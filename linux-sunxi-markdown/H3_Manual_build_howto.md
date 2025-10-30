# H3 Manual build howto
This is currently a placeholder for an H3 specific rework of the [Manual build howto][22884].
  

[![MBOX icon important.png][22885]][22886] | This page provides instructions for the legacy unmaintained Allwinner BSP. It is only here for historical reasons. Please follow the [Mainline U-Boot][22887] / [Mainline Kernel Howto][22888].   
---|---  
This page describes the process to combine Allwinners binary boot0, an SDK U-Boot, an SDK linux kernel and other bits together to create a useful SD-card from scratch, the basis for further hacking. 
This page is only suited for [H3][22889] based devices, please look under [See also][22890] for other manual build howtos. 
We of course do not build a whole distribution, we only build U-Boot, the kernel and a handful of tools, and then use an existing rootfs to get a useful system. Depending on the rootfs size, you might want to use a 2GB or larger SD Card. SD-card partitioning and formatting will be taken care of later. 
## Contents
  * [1 Getting a cross toolchain][22891]
  * [2 Installing boot0][22892]
  * [3 Building u-boot][22893]
  * [4 Installing onto Storage][22894]
    * [4.1 SD card][22895]
  * [5 Building the kernel][22896]
  * [6 Setting up the boot partition][22897]
  * [7 Setting up the rootfs][22898]
  * [8 Boot!][22899]
  * [9 See also][22890]

# Getting a cross toolchain
For this part, you need to refer to our [ toolchain page][22900]. 
# Installing boot0
[![MBOX icon important.png][22885]][22886] | This page provides instructions for the legacy unmaintained Allwinner BSP. It is only here for historical reasons. Please follow the [Mainline U-Boot][22887] / [Mainline Kernel Howto][22888].   
---|---  
SDKs only ship a binary version of boot0. This is a pristine version, and needs to be seeded with information such as the debug UART, DRAM clock rates, NAND/MMC ports. Normally this is done during the packing process. This section goes through the process manually. There are 2 flavors of boot0: 1 for NAND, and 1 for SD/MMC. One will not work with the other, as boot0 loads the next stage bootloader (U-Boot) from the respective supported storage. The boot0 binary can be found under 
[code] 
    lichee/tools/pack/chips/sun8iw7p1/bin/
    
[/code]
The following is a series of commands (ELF 64-bit) to properly prepare boot0 for usage. 
[code] 
    # Using sun8iw7p1 "dolphin-p1" Board as an example
    # Under lichee/tools/pack
    
    # Copy fex file
    cp -fv chips/sun8iw7p1/configs/dolphin-p1/sys_config.fex out/sys_config.fex
    
    # Copy boot0
    cp -fv chips/sun8iw7p1/bin/boot0_sdcard_sun8iw7p1.bin out/boot0_sdcard.fex
    
    # Fex file compiler requires fex file in CRLF format
    unix2dos out/sys_config.fex
    
    # Compile fex file
    pctools/linux/mod_update/script out/sys_config.fex
    
    
[/code]
For compiling The fex file it's preferable to use fex2bin (fexc) from [sunxi-tools][22901]
[code] 
    # Compile fex file with fex2bin (sunxi-tools)
    fex2bin out/sys_config.fex out/sys_config.bin
    
[/code]
This will give you some errors, but they are simple to fix. 
Continue with commands from SDK: 
[code] 
    # Patch sdcard boot0
    pctools/linux/mod_update/update_boot0 out/boot0_sdcard.fex out/sys_config.bin SDMMC_CARD
    
[/code]
You can then dd the boot0 image onto an SD card. See below for instructions. 
# Building u-boot
[![MBOX icon important.png][22885]][22886] | This page provides instructions for the legacy unmaintained Allwinner BSP. It is only here for historical reasons. Please follow the [Mainline U-Boot][22887] / [Mainline Kernel Howto][22888].   
---|---  
Building U-Boot is fairly straightforward. But before building check env settings in: brandy/u-boot-2011.09/include/configs/sun8iw7p1.h -> #define CONFIG_EXTRA_ENV_SETTINGS 
Then build the U-Boot binary: 
[code] 
    lichee$ cd brandy/u-boot-2011.09
    
    u-boot-2011.09$ make sun8iw7p1_config
    
    u-boot-2011.09$ make
    [...]
    arm-linux-gnueabi-objcopy --gap-fill=0xff -O binary u-boot u-boot.bin
    'u-boot-sun8iw7p1.bin' -> '../../tools/pack/chips/sun8iw7p1/bin/u-boot-sun8iw7p1.bin'
    
[/code]
The last line shows the U-Boot binary being copied to the packing directory. This is because the binary still needs to be seeded with information from the fex file. 
The following is an example to manually patch u-boot with sys_config.bin. See the boot0 section how to prepare it: 
[code] 
    # Under lichee/tools/pack
    
    # Copy U-Boot
    cp -fv chips/sun8iw7p1/bin/u-boot-sun8iw7p1.bin out/u-boot.fex
    
    # Patch U-Boot
    pctools/linux/mod_update/update_uboot out/u-boot.fex out/sys_config.bin
    
[/code]
You can then dd the updated u-boot.fex (u-boot.bin) image onto an SD card. See below for instructions. 
# Installing onto Storage
## SD card
Allwinner SoCs have a specific boot process, as described in the [ boot loader][22902] page. The on-chip [BROM][22903] loads boot0 starting from sector 16, or 8 KiB. boot0 then loads u-boot starting from sector 32800, or 16400 KiB. 
Each of these binaries have a specific header, which includes a magic string and a checksum. Both must be correct for the binary to be accepted and executed by the previous stage. 
The following shows the process of installing boot0 and u-boot built from the H3 SDK to an SD card in /dev/mmcblk0. Note you must leave enough unused space before the first partition (40960), or u-boot may be overwritten by filesystem usage. 
[code] 
    # write boot0
    dd if=boot0_sdcard.fex of=/dev/sdX bs=1k seek=8
    
    # write u-boot
    dd if=u-boot.fex of=/dev/sdX bs=1k seek=16400
    
[/code]
The SDK default config for u-boot only supports FAT filesystems, so you will need have a small FAT boot partition to store your kernel and other boot files. 
# Building the kernel
[![MBOX icon important.png][22885]][22886] | This page provides instructions for the legacy unmaintained Allwinner BSP. It is only here for historical reasons. Please follow the [Mainline U-Boot][22887] / [Mainline Kernel Howto][22888].   
---|---  
This is an example of how to build a minimal kernel using the internal (ELF 32-bit) 4.6.3 linaro toolchain (needs lib32-gcc-libs and lib32-zlib on a 64-bit system) : 
[code] 
    export PATH="$PATH":/your_path_to_the_SDK/lichee/brandy/gcc-linaro/bin
    export C_INCLUDE_PATH=/usr/include
    cd lichee/linux-3.4
    mkdir output
    cp rootfs.cpio.gz output/
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- sun8iw7p1smp_min_defconfig
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- uImage modules
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- INSTALL_MOD_PATH=output modules_install
    
[/code]
Now you can copy the generated uImage and modules to your SD card. 
# Setting up the boot partition
This section should refer to the [Manual_build_howto#Setting_up_the_boot_partition][22904] as much as possible.
# Setting up the rootfs
Please refer to [Bootable_SD_card#Rootfs][22905]
As a last step you need to copy the kernel modules into the newly created rootfs. Change into the top level directory of the newly created rootfs and run: 
[code] 
    mount ${cardroot} /mnt
    mkdir -p /mnt/lib/modules
    rm -rf /mnt/lib/modules/
    cp -r <PATH_TO_KERNEL_TREE>/output/lib /mnt/
    umount /mnt
    
[/code]
(Replace <PATH_TO_KERNEL_TREE> with the directory you have built your kernel in as described [above][22896].) 
# Boot!
Now you should be able to unmount your SDCard filesystems, and you should be able to boot your brand new installation. 
# See also
We have Manual build howtos for all SoCs: 
[H3 Manual build howto][22906]
[Manual build howto][22884]
