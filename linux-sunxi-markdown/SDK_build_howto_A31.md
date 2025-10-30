# SDK build howto A31
Allwinner usually provides device manufacturers with a complete SDK that includes the matching u-boot and kernel sources (with some odd binaries), Android packages, buildroot, build scripts and a matching Linaro toolchain. 
Development board vendors share the SDK with hardware owners to customize. This howto assumes you have such an SDK. This document is based on the A31 SDKs. 
## Contents
  * [1 Warning][48060]
  * [2 Contents of the SDK][48061]
  * [3 Android Build][48062]
    * [3.1 Configuring the Build][48063]
    * [3.2 Building Android][48064]
    * [3.3 Packing the Image][48065]

# Warning
**This howto is not complete and the intention is to merge it into the[original SDK how to][48066].**
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

# Android Build
Once you have unpacked the SDK (the _lichee_ directory in particular), you can go in a do a straight full build, which results in a [LiveSuite][48067] image. 
## Configuring the Build
The SDK can build android or linux flavor images, and may target different boards. Running ./build.sh will list the options. 
[code] 
    lichee$ ./build.sh -p sun6i_fiber
    
[/code]
I found that this failed silently when generating the rootfs(see gen_rootfs_log.txt). The reason for this was that the treat warning as errors flag was set in makedevs.mk. By removing this then everything worked as expected. Running _build.sh_ will produce binaries and images under _out/ <platform>/{linux,android}_. 
## Building Android
[code] 
    android4.4$ source build/envsetup.sh
    including device/asus/tilapia/vendorsetup.sh
    including device/asus/deb/vendorsetup.sh
    including device/asus/grouper/vendorsetup.sh
    including device/asus/flo/vendorsetup.sh
    including device/lge/mako/vendorsetup.sh
    including device/lge/hammerhead/vendorsetup.sh
    including device/softwinner/fiber-a31stm/vendorsetup.sh
    including device/softwinner/fiber-3g/vendorsetup.sh
    including device/softwinner/fiber-a31st512m/vendorsetup.sh
    including device/softwinner/fiber-w02/vendorsetup.sh
    including device/softwinner/fiber-common/vendorsetup.sh
    including device/softwinner/fiber-a31st/vendorsetup.sh
    including device/generic/x86/vendorsetup.sh
    including device/generic/armv7-a-neon/vendorsetup.sh
    including device/generic/mips/vendorsetup.sh
    including device/samsung/manta/vendorsetup.sh
    including sdk/bash_completion/adb.bash
    
    android4.4$ lunch
    
    You're building on Linux
    
    Lunch menu... pick a combo:
         1. aosp_arm-eng
         2. aosp_x86-eng
         3. aosp_mips-eng
         4. vbox_x86-eng
         5. aosp_tilapia-userdebug
         6. aosp_deb-userdebug
         7. aosp_grouper-userdebug
         8. aosp_flo-userdebug
         9. aosp_mako-userdebug
         10. aosp_hammerhead-userdebug
         11. fiber_a31stm-eng
         12. fiber_a31stm-user
         13. fiber_3g-eng
         14. fiber_a31st512m-eng
         15. fiber_a31st512m-user
         16. fiber_w02-eng
         17. fiber_w02-user
         18. fiber_a31st-eng
         19. fiber_a31st-user
         20. mini_x86-userdebug
         21. mini_armv7a_neon-userdebug
         22. mini_mips-userdebug
         23. aosp_manta-userdebug
    
    Which would you like? [aosp_arm-eng] 13
    
    ============================================
    PLATFORM_VERSION_CODENAME=REL
    PLATFORM_VERSION=4.4.2
    TARGET_PRODUCT=fiber_3g
    TARGET_BUILD_VARIANT=eng
    TARGET_BUILD_TYPE=release
    TARGET_BUILD_APPS=
    TARGET_ARCH=arm
    TARGET_ARCH_VARIANT=armv7-a-neon
    TARGET_CPU_VARIANT=cortex-a7
    HOST_ARCH=x86
    HOST_OS=linux
    HOST_OS_EXTRA=Linux-3.2.0-68-generic-x86_64-with-Ubuntu-12.04-precise
    HOST_BUILD_TYPE=release
    BUILD_ID=KOT49H
    OUT_DIR=out
    ============================================
    
    
    android4.4$make
    
[/code]
This should create the image files that are needed for packing. 
## Packing the Image
Run the following command to pack the final [LiveSuit][48068] image. 
[code] 
    lichee$ ./build.sh pack
    
[/code]
I found that the packing script was looking for the CRANE_IMAGE_OUT variable to be set. I know this is done by vendorsetup.sh in android4.4/device/softwinner/fibercommon but I haven't worked out what calls that. In the end I added this line to lichee/tools/pack_brandy/pack 
[code] 
    CRANE_IMAGE_OUT=../../../../android4.4/out/target/product/fiber-3g
    
[/code]
The resulting file that can flashed using [LiveSuit][48068] can be found lichee/tools/pack_brandy. In this case it's called sun6i_android_fiber-3g.img
