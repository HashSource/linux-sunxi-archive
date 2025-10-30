# Linux Kernel
[![MBOX icon important.png][31960]][31961] | This page provides information about the legacy linux-sunxi kernels, which are based on the vendor code drops. It is only useful when accelerated 3D graphics and multimedia support is strictly necessary.   
But the [Mainline Kernel][31962] is already a much better choice for a headless server. And also the mainline kernel works fine even for a basic Linux desktop system running on top of a simple framebuffer, which may be good enough for the users who do not need fancy 3D graphics or video playback acceleration.   
---|---  
This page describes how to get the sunxi specific linux kernel built for your device. 
## Contents
  * [1 History][31963]
  * [2 Repository][31964]
  * [3 Kernel versions][31965]
    * [3.1 Active branches][31966]
    * [3.2 Stale/ archived branches][31967]
  * [4 Compilation][31968]
    * [4.1 Get a toolchain][31969]
    * [4.2 Clone the repository][31970]
    * [4.3 Set default config][31971]
      * [4.3.1 A10][31972]
      * [4.3.2 A13][31973]
      * [4.3.3 A10s][31974]
      * [4.3.4 A20][31975]
    * [4.4 Tweak config][31976]
    * [4.5 Build][31977]
    * [4.6 Install][31978]
    * [4.7 U-boot setup][31979]
      * [4.7.1 Mainline U-boot][31980]
  * [5 Upstream code][31981]
  * [6 External links][31982]
  * [7 References][31983]

# History
Public [Linux Kernel][31984] support for the sunxi family (Allwinner [A10][31985], [A13][31986], ...) started with a source drop of `2.6.36` made by [Ainol][31987], followed by an official release of 2.6.36[[1]][31988] sources by [Allwinner][31989]. Developement jumped forward after a source release of 3.0.8 made by [Qware][31990][[2]][31991]
Initially living in [amery's github][31992] now our [community driven sunxi kernel][31993] repo is located in the [linux-sunxi's github][31994]. 
# Repository
The main sunxi kernel repository is available at [our projects' github][31994]. 
You can clone the entire (huge) repository by installing the git package and running: 
[code] 
    git clone https://github.com/linux-sunxi/linux-sunxi.git
[/code]
but if you just want to build our kernel, then follow [ the guide below][31968]. 
# Kernel versions
Parts of the sunxi SoC are already supported by [mainline kernel][31995] 3.8 and onwards. 
In case you need support for e.g. display, 3D, hardware accelerated video decoding and audio support (for A10/A20), you should can check out the **sunxi-3.4** or **stage/sunxi-3.4** branch as this will get the most out of your hardware quickly. But beware that this is already obsolete and unmaintained. 
## Active branches
Name | State | Description   
---|---|---  
`[sunxi-3.4][31996]` | **stable** | sunxi support forward ported from `sunxi-3.0` and keeping `reference-3.4` as it's mainline reference. **[PREFERRED]**  
`[stage/sunxi-3.4][31997]` | **testing** | fork of sunxi-3.4 with patches waiting to be accepted in stable sunxi-3.4   
`[sunxi-next][31998]` | **next mainline** | fork of mainline kernel including all patches, that are already accepted or merged for the next stable release   
If unsure, use the **sunxi-3.4** branch. 
## Stale/ archived branches
Name | State | Description   
---|---|---  
`sunxi-3.0` | **stable** | sunxi support initially based on `lichee3-3.0.8` and keeping `reference-3.0` as it's mainline reference.   
`experimental/sunxi-3.10` | **scheduled for removal. DO NOT USE.** | sunxi support forward ported from `sunxi-3.4`, backporting from `mainline` and keeping `reference-3.10` as it's mainline reference.   
`experimental/sunxi-3.14` | **highly experimental** | fix me   
`sunxi-2.6.36` | legacy  | sunxi support based on the official 2.6.36 release.   
`reference-3.0` | reference  | merge of `mirror/android-3.0` and the latest `v3.0.x` mainline stable tag. Used to see what of `sunxi-3.0` is **sunxi** specific.   
`reference-3.4` | reference  | merge of `mirror/android-3.4` and the latest `v3.4.x` mainline stable tag. Used to see what of `sunxi-3.4` is **sunxi** specific.   
`reference-3.10` | reference  | merge of `mirror/android-3.10` and the latest `v3.10.x` mainline stable tag. Used to see what of `sunxi-3.10` is **sunxi** specific.   
`mirror/allwinner-2.6.36` | mirror | mirror of allwinner's official 2.6.36 tree (aka [lichee2][31999])   
`mirror/android-2.6.36` | mirror | mirror of Android's kernel-common for Android 2.3 (_Gingerbread_)   
`mirror/android-3.0` | mirror | mirror of Android's kernel-common for Android 4.0 (_Ice Cream Sandwich_), 4.1 (_Jelly Bean_)   
`mirror/android-3.4` | mirror | mirror of Android's 3.4 kernel branch.   
`mirror/android-3.10` | mirror | mirror of Android's 3.10 kernel branch.   
`mirror/master` | mirror | mirror of Linus Torvalds' master.   
`lichee-3.0.8-sun4i` | compat | based on [Qware][32000]'s source release, kept only to let people drop-in new modules into a GPL-violating [lichee3][31999]/[A10][31985] based install.   
`wip/*` | WIP | experimental and very likely to 1) be rebased, 2) be seriously broken   
# Compilation
## Get a toolchain
If you haven't done so before, get a suitable [toolchain][32001] installed and added to your PATH. 
## Clone the repository
This command will clone the sunxi-3.4 branch: 
[code] 
    git clone -b sunxi-3.4 https://github.com/linux-sunxi/linux-sunxi.git
[/code]
If you just want a quick build and do not wish to download a big git repository, then run: 
[code] 
    git clone -b sunxi-3.4 --depth 1 https://github.com/linux-sunxi/linux-sunxi.git
[/code]
This will create a so-called shallow clone (still a 500MB download), which does not allow for much in the way of development or changes. Downloading a branch as a zip is recommended as the entire branch is compressed into 160MBs (unpacks into 500MB+). Recommended for users with slow or metered internet. 
## Set default config
[![MBOX icon important.png][31960]][31961] | This page provides information about the legacy linux-sunxi kernels, which are based on the vendor code drops. It is only useful when accelerated 3D graphics and multimedia support is strictly necessary.   
But the [Mainline Kernel][31962] is already a much better choice for a headless server. And also the mainline kernel works fine even for a basic Linux desktop system running on top of a simple framebuffer, which may be good enough for the users who do not need fancy 3D graphics or video playback acceleration.   
---|---  
### A10
For [A10][31985] use: 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- sun4i_defconfig
[/code]
### A13
For [A13][31986] use: 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- sun5i_defconfig
[/code]
### A10s
For [A10s][32002] use: 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- sun5i_defconfig
[/code]
But to get a booting system, you need to set: 
[code] 
    CONFIG_SW_DEBUG_UART=1
[/code]
to: 
[code] 
    CONFIG_SW_DEBUG_UART=0
[/code]
in `.config`. 
Through menuconfig, you need to dig through: 
[code] 
    System Type --->
[/code]
Then: 
[code] 
    Allwinner's sunxi options  --->
[/code]
And then set this to _0_ : 
[code] 
    (1) UART to use for low-level debug
[/code]
### A20
For [A20][32003] use: 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- sun7i_defconfig
[/code]
## Tweak config
After you have set a default configuration, you can fine-tune your kernel configuration. 
For this you will need ncurses development code installed. So for example, on a system that uses the apt package manager, run the following: 
[code] 
    apt-get install libncurses5-dev
[/code]
Now you can run menuconfig, and edit your configuration: 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig
[/code]
Note that the sunxi kernel is based on an obsolete kernel version with vendor hacks thrown in to support the sunxi hardware. As a result some configurations that are possible to select will not build or work. 
In particular some sunxi-specific drivers were not fixed to work both as built-in and as module and IPv6 only works as built-in. 
If you plan on using a [rootfs][32004] with _systemd_ or _upstart_ (e.g. Ubuntu) you should set CONFIG_FHANDLE=y in the kernel configuration. By default, .config reads "# CONFIG_FHANDLE is not set" The option can be found in General Setup, Open by fhandle syscalls. 
## Build
Make sure you have the package _u-boot-tools_ installed, then: 
[code] 
    make -j$(nproc) ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- uImage modules
[/code]
As a final step, create the full module tree: 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=output modules_install
[/code]
The INSTALL_MOD_PATH option specifies the directory where the full module tree will be made available, in this example, it will be the output directory under the kernel build directory itself. 
## Install
Now you have the following sitting in your kernel tree: 
[code] 
        arch/arm/boot/uImage
        output/lib/modules/3.4.XXX/
    
[/code]
The **uImage** file (the kernel minus the modules) needs to be started by U-Boot, so it is usually copied to a boot partition where U-Boot will find it, load it in RAM and then transfer control to it (U-Boot can also pass parameters to the kernel). The modules subdirectory needs to be copied to **/lib/modules** on the target root file system. 
## U-boot setup
### Mainline U-boot
A basic boot.cmd for the **deprecated sunxi-3.4 kernel** would be: 
[code] 
     setenv bootm_boot_mode sec
     setenv bootargs console=ttyS0,115200 root=/dev/mmcblk0p2 rootwait panic=10
     load mmc 0:1 0x43000000 script.bin || load mmc 0:1 0x43000000 boot/script.bin
     load mmc 0:1 0x42000000 uImage || load mmc 0:1 0x42000000 boot/uImage
     bootm 0x42000000
[/code]
_boot.cmd_ isn't used directly, but needs to be wrapped with uboot header with the command: 
[code] 
    mkimage -C none -A arm -T script -d boot.cmd boot.scr
[/code]
# Upstream code
Although it depends on the SoC, the status of [ mainline kernel][31962] is now almost suitable for normal use. 
# External links
  * [Official linux-sunxi git repository][31993]

Alternative 3.4 kernels are maintained and provided by 
  * Daniel Andersen: <https://github.com/dan-and/linux-sunxi> (also maintains an experimental U-Boot tree)
  * Armbian (<https://www.armbian.com>) maintains a patch set for default sunxi 3.4: <https://github.com/igorpecovnik/lib/tree/master/patch/kernel/sun7i-default>

# References
  1. [↑][32005] <https://github.com/allwinner/linux-2.6.36/>
  2. [↑][32006] [Qware (dutch redistributor of Ployer Momo tablets) released the Android 4.0.3 (AOSP + kernel) code][32007]
