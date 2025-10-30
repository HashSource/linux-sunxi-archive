# SDK build howto
Allwinner usually provides device manufacturers with a complete SDK that includes the matching u-boot and kernel sources (with some odd binaries), Android packages, buildroot, build scripts and a matching Linaro toolchain. 
Development board vendors share the SDK with hardware owners to customize. This howto assumes you have such an SDK. This document is based on the A23 and A80 SDKs. If you have one for an earlier SoC, some names may vary. 
## Contents
  * [1 Warning][48010]
  * [2 Contents of the SDK][48011]
  * [3 Basic Full Build][48012]
    * [3.1 Configuring the Build][48013]
    * [3.2 Running the Build][48014]
      * [3.2.1 Linux Build Specifics][48015]
      * [3.2.2 Android Build Specifics][48016]
    * [3.3 Packing the Image][48017]
  * [4 Manual Build of Separate Components][48018]
    * [4.1 boot0][48019]
    * [4.2 U-Boot][48020]
      * [4.2.1 Fixing update_uboot][48021]
  * [5 Installing onto Storage][48022]
    * [5.1 SD card][48023]

# Warning
**This howto is not complete.**
# Contents of the SDK
The SDK is split into several parts, but the build scripts requires them to be complete. 
  * `android-4.4`
  * `lichee`
    * `build.sh` \-- main build script
    * `buildroot` \-- rootfs, toolchain, and build scripts
    * `linux-3.4` \-- linux kernel
    * `brandy` \-- boot related stuff 
      * `build.sh` \-- simple build script for u-boot
      * `u-boot-2011.09` \-- Allwinner's port of u-Boot
    * `out` \-- build intermediaries and results. toolchain is also in here
    * `tools`
      * `tools_win` \-- LiveSuit/PhoenixSuit tools and drivers
      * `pack` \-- tools and configuration related to firmware packing 
        * `chips` \-- chip specific files (boot0/u-boot binaries, fex files)
        * `common` \-- common config files and tools
        * `out` \-- work directory for firmware packing
        * `pack` \-- firmware packing script

# Basic Full Build
Once you have unpacked the SDK (the _lichee_ directory in particular), you can go in a do a straight full build, which results in a [LiveSuite][48024] image. 
## Configuring the Build
The SDK can build android or linux flavor images, and may target different boards. 
[code] 
    lichee$ ./build.sh config
    
    Welcome to mkscript setup progress
    All available chips:
       0. sun9iw1p1
    Choice: 0
    All available platforms:
       0. android
       1. dragonboard
       2. linux
    Choice: 0
    All available kernel:
       0. linux-3.4
    Choice: 0
    All available boards:
       0. optimus
       1. p1
       2. perf
       3. perf5
       4. perf-lpddr3
    Choice: 0
    
[/code]
## Running the Build
Running _build.sh_ will produce binaries and images under _out/ <platform>/{linux,android}_. These will be used to generate the firmware image in the next step. 
[code] 
    lichee$ ./build.sh
    
[/code]
This will prepare the toolchain (or build buildroot if you're building for Linux), the kernel, and the rootfs (if not Android). 
### Linux Build Specifics
Building the Linux platform will build the whole buildroot tree. As the buildroot version bundled in the SDK is rather old, errors are bound to happen. Please use an older host toolchain. 
### Android Build Specifics
(This section requires additional work.) The Android image is built from the android directory in the SDK. 
## Packing the Image
Run the following command to pack the final [LiveSuit][48025] image. 
[code] 
    lichee$ ./build.sh pack
    
[/code]
  

# Manual Build of Separate Components
The following section explains how to build the various components from the SDK, so you can use them on your system. 
## boot0
Most SDKs only ship a binary version of boot0. This is a pristine version, and needs to be seeded with information such as the debug UART, DRAM clock rates, NAND/MMC ports. Normally this is done during the packing process. This section goes through the process manually. 
The boot0 binary can be found under 
[code] 
    lichee/tools/pack/chips/CHIP/bin/
    
[/code]
Replace **CHIP** with whatever chip you have. 
There are 2 flavors of boot0: 1 for NAND, and 1 for SD/MMC. One will not work with the other, as boot0 loads the next stage bootloader (U-Boot) from the respective supported storage. Also, there is a special boot0 for FEL mode. 
The following is a series of commands to properly prepare boot0 for usage. 
[code] 
    # Using sun9iw1p1 A80 Optimus Board as an example
    # Under lichee/tools/pack
    
    # Copy fex file
    cp -fv chips/sun9iw1p1/configs/optimus/sys_config.fex out/sys_config.fex
    
    # Copy boot0
    cp -fv chips/sun9iw1p1/bin/boot0_nand_sun9iw1p1.bin out/boot0_nand.fex
    cp -fv chips/sun9iw1p1/bin/boot0_sdcard_sun9iw1p1.bin out/boot0_sdcard.fex
    cp -fv chips/sun9iw1p1/bin/fes1_sun9iw1p1.bin out/fes1.fex
    
    # Fex file compiler requires fex file in CRLF format
    unix2dos out/sys_config.fex
    
    # Compile fex file
    pctools/linux/mod_update/script out/sys_config.fex
    
    # Patch sdcard boot0
    pctools/linux/mod_update/update_boot0 out/boot0_sdcard.fex out/sys_config.bin SDMMC_CARD
    
    # Patch nand boot0
    pctools/linux/mod_update/update_boot0 out/boot0_nand.fex out/sys_config.bin NAND
    
    # Patch FEL boot0
    pctools/linux/mod_update/update_fes1 out/fes1.fex out/sys_config.bin
    
[/code]
You can then dd the boot0 image onto an SD card, or load the FEL mode boot0 over usb. 
## U-Boot
Building U-Boot is fairly straightforward. 
First build the U-Boot binary: 
[code] 
    lichee$ cd brandy/u-boot-2011.09
    
    u-boot-2011.09$ make sun9iw1p1_config # replace sun9iw1p1 with whatever platform you have
    
    u-boot-2011.09$ make
    [...]
    arm-linux-gnueabi-objcopy --gap-fill=0xff -O binary u-boot u-boot.bin
    'u-boot-sun9iw1p1.bin' -> '../../tools/pack/chips/sun9iw1p1/bin/u-boot-sun9iw1p1.bin'
    
[/code]
The last line shows the U-Boot binary being copied to the packing directory. This is because the binary still needs to be seeded with information from the fex file. 
The following is an example to manually patch u-boot: 
[code] 
    # Using sun9iw1p1 A80 Optimus Board as an example
    # Under lichee/tools/pack
    
    # Copy fex file
    cp -fv chips/sun9iw1p1/configs/optimus/sys_config.fex out/sys_config.fex
    
    # Copy U-Boot
    cp -fv chips/sun9iw1p1/bin/u-boot-sun9iw1p1.bin out/u-boot.fex
    
    # Fex file compiler requires fex file in CRLF format
    unix2dos out/sys_config.fex
    
    # Compile fex file
    pctools/linux/mod_update/script out/sys_config.fex
    
    # Patch U-Boot
    pctools/linux/mod_update/update_uboot out/u-boot.fex out/sys_config.bin
    
[/code]
### Fixing update_uboot
If you get memory corruption when using _update_uboot_ , use the following to build a working one. You will only hit this bug when trying to update an u-boot.fex that stores a _source_length_ equal to a multiple of _align_size_ inside the original u-boot header. 
[code] 
    git clone https://github.com/longsleep/sunxi-pack-tools
    cd sunxi-pack-tools
    unix2dos <<EOF | patch --binary -l -p1 && make
    diff --git a/update_uboot/check.c b/update_uboot/check.c
    index 4dae372..4987f14 100644
    --- a/update_uboot/check.c
    +++ b/update_uboot/check.c
    @@ -27,6 +27,7 @@
     *
     ************************************************************************************************************************
     */
    +#include <string.h>
     #include "check.h"
     #include "spare_head.h"
     
    diff --git a/update_uboot/check.h b/update_uboot/check.h
    index ff1ac42..35e0291 100644
    --- a/update_uboot/check.h
    +++ b/update_uboot/check.h
    @@ -36,6 +36,7 @@
     #define CHECK_IS_CORRECT           0
     
     
    +__s32 check_magic( __u32 *mem_base, const char *magic );
     extern __s32 check_file   ( __u32 *mem_base, __u32 size, const char *magic );
     extern __s32 gen_check_sum( void *boot_buf );
     
    diff --git a/update_uboot/update_uboot.c b/update_uboot/update_uboot.c
    index 2bb929f..cd5ccc7 100644
    --- a/update_uboot/update_uboot.c
    +++ b/update_uboot/update_uboot.c
    @@ -10,7 +10,7 @@
     #include <ctype.h>
     #include <unistd.h>
     
    -#define  MAX_PATH             (260)
    +#define  MAX_PATH             (1024)
     
     
     int  script_length;
    @@ -19,6 +19,7 @@ int  align_size;
     void *script_file_decode(char *script_name);
     int merge_uboot(char *source_uboot_name, char *script_name);
     
    +int align_uboot(char *source_uboot_name);
     int update_for_uboot(char *uboot_name);
     //------------------------------------------------------------------------------------------------------------
     //
    @@ -685,6 +686,7 @@ int merge_uboot(char *source_uboot_name, char *script_file_name)
            {
                    total_length = (total_length + align_size) & (~(align_size - 1));
            }
    +       printf("u-boot+script total length = %d\n", total_length);
     
            pbuf_source = (char *)malloc(total_length);
            if(!pbuf_source)
    @@ -753,14 +755,15 @@ int align_uboot(char *source_uboot_name)
            rewind(uboot_file);
     
            head = (struct spare_boot_ctrl_head *)buffer;
    -       source_length = head->uboot_length;
    +       total_length = source_length = head->uboot_length;
            align_size = head->align_size;
            if(source_length & (align_size - 1))
            {
                    total_length = (source_length + align_size) & (~(align_size - 1));
            }
    -       //printf("source length = %d\n", source_length);
    -       //printf("total length = %d\n", total_length);
    +       printf("u-boot align size = %d\n", align_size);
    +       printf("u-boot source length = %d\n", source_length);
    +       printf("u-boot total length = %d\n", total_length);
            uboot_buf = (char *)malloc(total_length);
            if(!uboot_buf)
            {
    EOF
    
[/code]
# Installing onto Storage
## SD card
Allwinner SoCs have a specific boot process, as described in the [ boot loader][48026] page. The on-chip [BROM][48027] loads boot0 starting from sector 16, or 8 KiB. boot0 then loads boot1 starting from sector 38192, or 19096 KiB. boot1 then loads u-boot from the first partiion (FAT). If the SoC SDK has done away with boot1, then u-boot is loaded from boot1's original place. 
Each of these binaries have a specific header, which includes a magic string and a checksum. Both must be correct for the binary to be accepted and executed by the previous stage. 
The following shows the process of installing boot0 and u-boot built from the A80 SDK to an SD card in /dev/mmcblk0. Note you must leave enough unused space before the first partition, or u-boot may be overwritten by filesystem usage. 
[code] 
    # write boot0
    dd if=boot0_sdcard.fex of=/dev/mmcblk0 bs=1k seek=8
    
    # write u-boot
    dd if=u-boot.fex of=/dev/mmcblk0 bs=1k seek=19096
    
[/code]
The SDK default config for u-boot only supports FAT filesystems, so you will need have a small FAT boot partition to store your kernel and other boot files.
