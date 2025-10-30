# U-Boot
(Redirected from [Mainline U-Boot][33994])
 
This page describes how to build and use [upstream U-Boot][33997] for 32bit (armv7/armhf) sunxi devices. 
Differences for ARM64 are only mentioned in the [Compile U-Boot][33998] section. For more info see directly board/sunxi/README.sunxi64 in uboot sources. 
We have a separate page for [the deprecated legacy sunxi branch of U-Boot][33999]. 
## Contents
  * [1 Status Matrix][34000]
  * [2 Device support][34001]
  * [3 Changelog (outdated)][34002]
  * [4 Compile U-Boot][33998]
    * [4.1 Get a toolchain][34003]
    * [4.2 Get swig][34004]
    * [4.3 Get python3-dev][34005]
    * [4.4 Get dtc][34006]
    * [4.5 Get Trusted Firmware-A (aarch64)][34007]
    * [4.6 Clone the repository][34008]
    * [4.7 Determine build target][34009]
    * [4.8 Build][34010]
      * [4.8.1 armhf][34011]
      * [4.8.2 arm64][34012]
  * [5 Configure U-Boot][34013]
    * [5.1 Boot][34014]
      * [5.1.1 Booting with boot.cmd][34015]
      * [5.1.2 Booting with extlinux.conf][34016]
      * [5.1.3 Boot menu support][34017]
    * [5.2 Setting u-boot environment variables][34018]
    * [5.3 NAND][34019]
    * [5.4 NFS][34020]
    * [5.5 FB console][34021]
    * [5.6 LCD Settings][34022]
  * [6 Install U-Boot][34023]
  * [7 Troubleshooting][34024]
    * [7.1 USB 1.x, USB keyboards (U-Boot < v2015.07)][34025]
    * [7.2 U-Boot 2015.07+ won't start][34026]
    * [7.3 Legacy kernel won't start][34027]
    * [7.4 Unrecognized/unsupported machine ID][34028]
    * [7.5 ImportError: No module named _libfdt][34029]
  * [8 Adding a new device to upstream U-Boot][34030]
    * [8.1 DRAM Settings][34031]
      * [8.1.1 Extract boot0 parameters][34032]
      * [8.1.2 Failsafe DRAM settings for old (pre 2014) devices, based on standard JEDEC timings][34033]
      * [8.1.3 The settings from old (pre 2014) Android firmware][34034]
      * [8.1.4 Performance optimized DRAM settings][34035]
  * [9 See also][34036]

# Status Matrix
SoC  | Basic support | SD-Card/eMMC boot | USB | Ethernet boot | HDMI display | LCD display  
---|---|---|---|---|---|---  
[F1C-100s][34037] | v2022.04 | v2022.07 | v2023.10 | N/A | N/A | Unknown  
[A10][34038] | v2014.10 | v2014.10 | v2014.10 | v2014.10 | v2015.01 | v2015.04  
[A10s][34039] | v2014.10 | v2014.10 | v2014.10 | v2014.10 | v2015.01 | v2015.04  
[A13][34040] | v2014.10 | v2014.10 | v2014.10 | v2014.10 | N/A | v2015.04  
[A20][34041] | v2014.07 | v2014.07 | v2014.10 | v2014.07 | v2015.01 | v2015.04  
[A23][34042] | v2015.01 | v2015.04 | v2015.04 | N/A | N/A | v2015.04  
[A31][34043] | v2015.01 | v2015.01 | v2015.01 | v2015.01 | v2015.01 | v2015.04  
[A33][34044] | v2015.07 | v2015.07 | v2015.07 | N/A | N/A | v2015.07  
[A64][34045] | v2016.05 | v2016.05 | v2016.11 | v2016.09 | v2017.07 | v2017.07  
[A80][34046] | v2015.07 | v2015.07 | TODO | TODO | TODO | TODO  
[A83T][34047] | v2016.01 | v2016.01 | v2016.01 | v2016.01 | TODO | TODO  
[H3][34048] | v2016.01 | v2016.01 | v2016.03 | v2016.09 | v2017.07 | N/A  
[H5][34049] | v2017.05 | v2017.05 | v2017.05 | v2017.05 | v2017.07 | N/A  
[H6][34050] | v2018.09 | v2018.09 | v2019.10 | v2020.07 | TODO | TODO  
[R40][34051] | v2017.05 | v2017.05 | v2020.04 | v2020.04 | TODO | TODO  
[V3][34052] / [V3s][34053] / [S3L][34054] | v2017.05 | v2017.05 | v2017.05 | WIP | TODO | TODO  
[H616][34055] | v2021.04 | v2021.04 | v2023.10 | v2021.04 | TODO | TODO  
[T113-s3][34056] | v2024.01 | v2024.01 | v2024.01 | Unknown | N/A | TODO  
[D1][34057] / [D1s][34058] | Unknown | Unknown | Unknown | Unknown | TODO | TODO  
[A133][34059] | v2025.10 | v2025.10 | v2025.10 | WIP | TODO | TODO  
[A523][34060] | v2025.10 | v2025.10 | v2025.10 | WIP | TODO | TODO  
[A733][34061] | WIP | WIP | WIP | WIP | TODO | TODO  
# Device support
To know if your device is supported in U-Boot, check out [the respective device page.][34062]
Here is [the list of all devices supporting mainline U-Boot.][34063]
# Changelog (outdated)
A sunxi specific changelog for upstream [ is available here][34064]. It has only been kept up to date until 2019. 
# Compile U-Boot
## Get a toolchain
Our [ toolchain page][34065] explains everything you need to know about installing a toolchain. 
## Get swig
Install the swig compiler. 
[code] 
    apt-get install swig
[/code]
## Get python3-dev
If you experience: 
[code] 
    fatal error: Python.h: No such file or directory
[/code]
Then install the development package for python-3: 
[code] 
    apt-get install python3-dev
[/code]
## Get dtc
The device tree compiler, dtc, needs to be available to successfully build u-boot. 
[code] 
    apt-get install device-tree-compiler
[/code]
## Get Trusted Firmware-A (aarch64)
If you are building U-Boot for an arm64/aarch64 device, you need to include Trusted Firmware-A (TF-A, formerly known as ATF). 
You can get this from: 
[code] 
    git clone https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git
[/code]
To build this, run: 
[code] 
    make CROSS_COMPILE=aarch64-linux-gnu- PLAT=<platform> DEBUG=1 bl31
[/code]
Change _< platform>_ to your needs. _sun50i_a64_ for example is suitable for H5 and A64 devices. 
See [docs/plat/allwinner.rst][34066] in the TF-A source or [doc/board/allwinner/sunxi.rst][34067] in the U-Boot source for more information. 
## Clone the repository
You can clone the u-boot repository by running: 
[code] 
    git clone git://git.denx.de/u-boot.git
[/code]
You might want to use the latest release instead of the newest development code. To get a list of available releases, which are tags, run: 
[code] 
    git tag -l
[/code]
Check out your preferred release: 
[code] 
    git checkout v2024.01
[/code]
## Determine build target
Every [device page][34068] should list the device specific u-boot config under the section _Mainline U-Boot_. 
This config usually follows the _< device>_defconfig_ schema. For instance, if your device is the [Cubieboard2][34069] then your build target is _Cubieboard2_defconfig_. 
You should be able to find this file in the u-boot tree under _configs/_
## Build
The commands below include a menuconfig step, this allows you to change some build-time settings, but can normally be skipped. 
When the build has completed, there will be _u-boot-sunxi-with-spl.bin_ available at the top level of your u-boot repository. Follow the u-boot installation step of the respective howto you are following for your preferred installation medium. 
### armhf
[code] 
    make CROSS_COMPILE=arm-linux-gnueabihf- <board_name>_defconfig
    make CROSS_COMPILE=arm-linux-gnueabihf- menuconfig
    make CROSS_COMPILE=arm-linux-gnueabihf-
[/code]
### arm64
[code] 
    make CROSS_COMPILE=aarch64-linux-gnu- BL31=<path_to_arm-trusted-firmware>/build/sun50i_a64/debug/bl31.bin  <board_name>_defconfig
    make CROSS_COMPILE=aarch64-linux-gnu- BL31=<path_to_arm-trusted-firmware>/build/sun50i_a64/debug/bl31.bin menuconfig
    make CROSS_COMPILE=aarch64-linux-gnu- BL31=<path_to_arm-trusted-firmware>/build/sun50i_a64/debug/bl31.bin
[/code]
# Configure U-Boot
This article provides a collection of various scenarios for booting with U-Boot. 
## Boot
For getting these bits loaded onto the hardware, please refer to the respective howto: 
  * [ SD Card][34070]
  * [NAND][34071]
  * [ SPI NOR Flash][34072]
  * [ USB OTG][34073]
  * [ Ethernet][34074]
  * [Fastboot][34075]

### Booting with boot.cmd
For booting from SD with mainline U-Boot, the recommended way is by using a _boot.cmd_ on the boot partition. 
A basic boot.cmd would be: 
[code] 
    setenv bootargs console=ttyS0,115200 root=/dev/mmcblk0p2 rootwait panic=10
    load mmc 0:1 0x43000000 sunXi-board.dtb || load mmc 0:1 0x43000000 boot/sunXi-board.dtb
    load mmc 0:1 0x42000000 zImage || load mmc 0:1 0x42000000 boot/zImage
    bootz 0x42000000 - 0x43000000
[/code]
If you are using a **uImage** for the kernel image, then substitute _zImage_ with _uImage_ , and use **bootm** instead of _bootz_. If you are on a **arm64** or **riscv** kernel, you are using **Image** , and you have to load it with **booti**. 
If you also want to use an initramfs, please refer to the [Initial Ramdisk][34076] article for details. 
On kernels before 3.14 (from 2013) setting **bootm_boot_mode** might be necessary, more info is on the [ PSCI page][34077]. 
_boot.cmd_ isn't used directly, but needs to be wrapped with uboot header with the command: 
[code] 
    mkimage -C none -A arm -T script -d boot.cmd boot.scr
[/code]
### Booting with extlinux.conf
Mainline U-Boot also use syslinux/extlinux as payload. 
You need to install the boot configuration file extlinux.conf in an ext2/3/4 partition of SD card and U-Boot will find and execute it. This is conceptually identical to creating a GRUB configuration file on a desktop PC. 
Example extlinux.conf: 
[code] 
    TIMEOUT 100
    DEFAULT default
    MENU TITLE Boot menu
    
    LABEL default
    	MENU LABEL Default
            LINUX /zImage
            FDT /sun4i-a10-marsboard.dtb
            APPEND root=/dev/sda1 rootwait console=tty0 console=ttyS0,115200n8
    
    LABEL exit
    	MENU LABEL Local boot script (boot.scr)
            LOCALBOOT 1
    
[/code]
### Boot menu support
There are two ways to show boot menu in U-Boot: 
  * Specify multiple _LABEL_ s in extlinux.conf

  * Use _bootmenu_ command in boot.cmd and convert boot.cmd to boot.scr

Make sure that CONFIG_CMD_BOOTMENU is enabled before compiling U-Boot. Then create boot.cmd with the usual booting commands set as the content of the env variable named _bootmenu_NUM_ , followed by _bootmenu DELAYS_. Examples are as follows: 
[code] 
    setenv bootmenu_0 Kernel and rootfs on USB disk="setenv bootargs console=ttyS0,115200 console=tty0 root=PARTLABEL=USB-Root rw rootwait; led orangepi:red:status on; load usb 0:1 ${fdt_addr_r} board.dtb; load usb 0:1 ${kernel_addr_r} zImage; bootz ${kernel_addr_r} - ${fdt_addr_r}"
    
    setenv bootmenu_1 Kernel and rootfs on SD card="setenv bootargs console=ttyS0,115200 console=tty0 root=/dev/mmcblk0p2 rw rootwait; led orangepi:red:status on; load mmc 0:1 ${fdt_addr_r} board.dtb; load mmc 0:1 ${kernel_addr_r} zImage; bootz ${kernel_addr_r} - ${fdt_addr_r}"
    
    bootmenu 1
    
[/code]
For more info, see doc/usage/cmd/bootmenu.rst in U-Boot source tree. 
## Setting u-boot environment variables
There is a difference in setting environment variables between the boot script and the U-Boot shell. 
Inside the shell you would set, for instance: 
[code] 
    setenv root /dev/sda1
[/code]
But in the script you would use: 
[code] 
    root=/dev/sda1
[/code]
## NAND
Example U-Boot environment, as found in `uEnv.txt` from a stock android U-Boot environment partition 
[code] 
    bootdelay=0
    bootcmd=run setargs boot_normal
    console=ttyS0,115200
    nand_root=/dev/nandc
    mmc_root=/dev/mmcblk0p4
    init=/init
    loglevel=8
    setargs=setenv bootargs console=${console} root=${nand_root} init=${init} loglevel=${loglevel}
    boot_normal=nand read 40007800 boot;boota 40007800
    boot_recovery=nand read 40007800 recovery;boota 40007800
    boot_fastboot=fastboot
[/code]
## NFS
Recent version of U-Boot are able to boot from NFS as well as TFTP, but you have to get rid of the automatic setup of FTP. Check [ Ethernet][34074] for more information. 
[![Sticky-note-pin.png][34078]][34079] _Note:_ on the A20 based cubieboards, this only seems to work on the stable kernel, not on stage. 
## FB console
To get U-Boot output shown on the built-in framebuffer driver (currently, HDMI only at 1024x768), add the following to your boot.cmd: 
[code] 
    setenv stdout=serial,vga
    setenv stderr=serial,vga
[/code]
The default environment has these values set as well. 
## LCD Settings
There is a [separate wiki page about configuring LCD][34080] in U-Boot. 
# Install U-Boot
  * One way to automatically load a specific kernel, with specific command line options, is to create a boot script with the respective U-Boot commands. Convert the _boot.cmd_ to _boot.scr_ using [mkimage][34081]:

[code] 
     mkimage -C none -A arm -T script -d boot.cmd boot.scr
    
[/code]
  * Copy the bootloader to the installation media

[code] 
     dd if=u-boot-sunxi-with-spl.bin of=/dev/sdX bs=1024 seek=8
    
[/code]
For a more elaborate list of possible targets to install U-Boot, and instructions on how to best install U-Boot there, check the [U-Boot documentation][34082]. 
  * copy kernel files to the first partition 
    * For a 3.4 kernel you need _uImage_ (linux kernel) and _script.bin_ (binary representation of [FEX][34083]).
    * For a device tree based kernel ("mainline", 4.x) you need the kernel image (_uImage_ , _zImage_ or _Image_) and the device-specific _.dtb_ file (the one referenced in the _${fdtfile}_ above) that is generated as part of your kernel compilation.

Look at [Manual build howto][34084] for more details. 
# Troubleshooting
## USB 1.x, USB keyboards (U-Boot < v2015.07)
**U-Boot v2015.07 and later shouldn't have problems supporting mixed USB 1.x/2.0 devices.** OHCI and EHCI no longer conflict with each other (after the switch to device model). 
Previous U-Boot versions (v2015.04 and older) have a problem supporting both USB 1.x (OHCI) and USB 2.0 (EHCI) at the same time - the latter includes the _SUNXI_EHCI_ driver for Allwinner boards. 
    Unfortunately, this also affects many **USB HID / keyboard** devices which would not be detected properly by U-Boot. The typical message in this case is "_cannot reset port N!?_ ", where _N_ is whichever USB port those devices were attached to.
[![Information.png][34085]][34086] A possible workaround is to place an external USB 2.0 hub between your board and these USB devices. 
See: <http://lists.denx.de/pipermail/u-boot/2015-January/200162.html>. 
## U-Boot 2015.07+ won't start
If you're using a recent (device model based) U-Boot, and the SPL just hangs after initializing the DRAM (`CPU: 912000000Hz, AXI/AHB/APB: 3/2/2` or something similar), chances are that your main U-Boot binary may be missing DTB information / a proper [device tree][34087]. Depending on the (possibly outdated) instructions you followed: double-check that you're not incorrectly using _u-boot.bin_ instead of _u-boot**-dtb**.bin_, or _u-boot.img_ instead of _u-boot**-dtb**.img_. 
## Legacy kernel won't start
  * If your 3.4.x kernel refuses to boot / gets stuck right after _"Starting kernel ..."_ : 
    * Double-check that **bootm_boot_mode** is set to "**sec** "! (see [above][34014])
    * For U-Boot 2018.09-rc1 or later, set CONFIG_ARMV7_LPAE=n in .config or apply <https://patchwork.ozlabs.org/patch/1058338/>
  * If you don't have a serial console and only use VGA/HDMI/LCD, then it might be also the case of "Unrecognized/unsupported machine ID" (see [below][34028]).

## Unrecognized/unsupported machine ID
The sunxi-3.4 kernel may fail to boot with one of the following error messages on the serial console (but this message is not visible on a HDMI monitor or a LCD display!): 
[code] 
    Error: unrecognized/unsupported machine ID (r1 = 0x10001008).
    Error: unrecognized/unsupported machine ID (r1 = 0x1000102a).
    Error: unrecognized/unsupported machine ID (r1 = 0x100010bb).
    
[/code]
In this case either upgrade to a recent _stage/sunxi-3.4_ kernel ([github branch][34088]) - or try to **"Enable workarounds for booting old kernels"** in U-Boot: 
    `make menuconfig` or `make CROSS_COMPILE=arm-linux-gnueabihf- menuconfig`, the option is located under "ARM architecture". (Make sure to rebuild your U-Boot after changing it.)
If upgrading to _stage/sunxi-3.4_ is not an option (i.e. using some old and very much diverged sunxi-3.4 fork is really necessary), then the following patches can be cherry-picked (= selectively merged _as a set_): 
[code] 
    wget https://github.com/linux-sunxi/linux-sunxi/commit/5052b83aa44dc16d6662d8d9d936166c139ad8c5.patch
    wget https://github.com/linux-sunxi/linux-sunxi/commit/9a1cd034181af628d4145202289e1993c1687db6.patch
    wget https://github.com/linux-sunxi/linux-sunxi/commit/c4c4664ed1a2f35e54a33ae4e65f517721ff43b5.patch
    wget https://github.com/linux-sunxi/linux-sunxi/commit/ade08aa6e5249a9e75a97393e86c250b2bcb3ec8.patch
    wget https://github.com/linux-sunxi/linux-sunxi/commit/16b25a95327f45a995f6efcf3e9d83a414231af9.patch
    wget https://github.com/linux-sunxi/linux-sunxi/commit/dea62f21deb177053b84b15a519dff6c74d061d9.patch
    wget https://github.com/linux-sunxi/linux-sunxi/commit/d47d367036be38c5180632ec8a3ad169a4593a88.patch
    git am 5052b83aa44dc16d6662d8d9d936166c139ad8c5.patch
    git am 9a1cd034181af628d4145202289e1993c1687db6.patch
    git am c4c4664ed1a2f35e54a33ae4e65f517721ff43b5.patch
    git am ade08aa6e5249a9e75a97393e86c250b2bcb3ec8.patch
    git am 16b25a95327f45a995f6efcf3e9d83a414231af9.patch
    git am dea62f21deb177053b84b15a519dff6c74d061d9.patch
    git am d47d367036be38c5180632ec8a3ad169a4593a88.patch
    
[/code]
[![Exclamation.png][34089]][34090] It is required to apply **all** of them, as they contain important stability/safety changes. The last patch in this series only takes care of the safety guard, which exists there specifically to block booting problematic kernels. Just removing the safety guard alone without applying all the bugfixes will lead to obscure runtime problems, please don't be tempted to do this. 
  

## ImportError: No module named _libfdt
If you see the following error when compiling on Arch Linux arm 
[code] 
    ImportError: No module named _libfdt
    
[/code]
install dtc 
[code] 
    sudo pacman -S dtc
    
[/code]
# Adding a new device to upstream U-Boot
To add a new device to mainline U-Boot, you will need the devicetree (DT) and a defconfig file. DT files are now synced automatically from the mainline kernel repository (see [the U-Boot documentation][34091]), so you need to submit your .dts file to the Linux kernel repository first. For development purposes you can place the DT manually in dts/upstream/src/arm64/allwinner. 
The defconfig file selects the SoC, and contains the DT name. It also lists those drivers that are not already selected by default (like USB or Ethernet). But the most important info in there are the DRAM settings, which are board specific, see below for more information. 
The best way is to find the device that is the most similar, and copy both files. Carefully adjust them, especially the regulator setup in the devicetree might be different and could cause harm to your device. You might want to remove or disable the PMIC completely for initial development. 
## DRAM Settings
The settings needed to set up the DRAM controller are board specific, and have often been determined by the board vendor together with Allwinner, with the help of some magic. 
### Extract boot0 parameters
A modern vendor provided boot0 image contains those DRAM parameters in its header, you can use the [sunxi-fw][34092] tool to extract the values from there. Either use some update image from the web, or extract the first sectors from the device itself, for instance from the eMMC. For the options listed in the defconfig file, just use the respective values from the column matching your SoC. 
### Failsafe DRAM settings for old (pre 2014) devices, based on standard JEDEC timings
For old A10/A13/A20 based devices, you would be able to use slow failsafe DRAM settings: 
[code] 
       CONFIG_DRAM_CLK=360
       CONFIG_DRAM_ZQ=123
       CONFIG_DRAM_EMR1=4
       CONFIG_DRAM_TIMINGS_DDR3_800E_1066G_1333J=y
    
[/code]
For a more complete list of parameters see the [U-Boot Kconfig file][34093]. 
### The settings from old (pre 2014) Android firmware
Somewhat better settings can be retrieved by the [meminfo tool][34094] from the stock Android or GNU/Linux system, provided by the device manufacturer. It still makes sense to [test the reliability][34095] of the resulting DRAM configuration. Because some vendors are providing poor configuration for ZQ or EMR1, but nevertheless trying to optimistically set the DRAM clock speed too high. 
### Performance optimized DRAM settings
Tuning DRAM setting for each individual board can provide much better performance than the failsafe defaults. This involves trial and error testing of different settings using a tool until an optimal combination is found. The [DRAM Controller page][34096] provides links to start researching this topic. This approach will be time consuming, so a satisfactory solution using one of the other approaches may be best to start with. 
# See also
  * [Mainline Kernel Howto][34097]
  * [Mainline U-Boot supported devices][34063]
  * [U-Boot/Changelog][34064]
