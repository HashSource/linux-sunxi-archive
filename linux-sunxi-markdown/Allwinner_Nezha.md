# Allwinner Nezha
Allwinner Nezha  
---  
[![Allwinner Nezha Front.jpg][6491]][6492]  
Manufacturer |  [Allwinner][6493]  
Dimensions |  85 _mm_ x 56 _mm_ x 15 _mm_  
Release Date |  April 2021   
Website |  [Product Page][6494]  
Specifications   
SoC |  [D1][6495] @ 1.0Ghz   
DRAM |  512MiB/1GiB/2GiB DDR3 @ 792MHz, 2×[H5TQ4G63EFR][6496]  
NAND |  256MB, [MX35LF2GE4AD][6497]  
Power |  DC 5V @ 2A (via OTG or dedicated USB Type-C connector)   
Features   
Video |  HDMI (Type A - full), LVDS   
Audio |  3.5mm headphone plug, HDMI, microphone array board connector, I2S   
Network |  WiFi 802.11 b/g/n ([XRadioTech XR829][6498]), 10/100/1000Mbps Ethernet ([Realtek RTL8211F][6499])   
Storage |  µSD, SPI NAND   
USB |  1 USB2.0 Host, 1 USB Type-C OTG   
Other |  Power LED, RGB LED, OK & FEL buttons   
Headers |  40-pin GPIO, DEBUG   
The Allwinner Nezha is the first [D1][6495] based board made available to the general public. It was sold through several distributors, including RVBoards and [Sipeed][6500]. 
## Contents
  * [1 Identification][6501]
  * [2 General Notes][6502]
  * [3 Sunxi support][6503]
    * [3.1 Current status][6504]
    * [3.2 Manual build][6505]
      * [3.2.1 U-Boot][6506]
        * [3.2.1.1 OpenSBI][6507]
        * [3.2.1.2 Mainline U-Boot][6508]
        * [3.2.1.3 BSP U-Boot][6509]
        * [3.2.1.4 BSP boot0 SPL][6510]
      * [3.2.2 Linux Kernel][6511]
        * [3.2.2.1 BSP Linux Kernel][6512]
        * [3.2.2.2 Mainline kernel][6513]
        * [3.2.2.3 Writing the kernel to SD card][6514]
    * [3.3 Build tool][6515]
      * [3.3.1 Buildroot][6516]
      * [3.3.2 Yocto][6517]
      * [3.3.3 SkiffOS (Buildroot)][6518]
  * [4 Tips, Tricks, Caveats][6519]
    * [4.1 RV 86][6520]
    * [4.2 FEL mode][6521]
    * [4.3 JTAG][6522]
    * [4.4 DRAM Driver][6523]
    * [4.5 Enabling U-Boot command line][6524]
    * [4.6 Default Firmware Environment][6525]
    * [4.7 Oops tracing][6526]
  * [5 Adding a serial port][6527]
  * [6 Adding a reset pin][6528]
  * [7 Development and test automation][6529]
  * [8 Pictures][6530]
  * [9 Schematic][6531]
  * [10 See also][6532]
    * [10.1 Manufacturer images][6533]

# Identification
There are at least two known revisions of the board. The older version is silkscreened `D1_DEV_DDR3_16X2_V1_0` on the top and does not have the `AWOL` logo. The newer version has the `AWOL` anagram silkscreened on the front (`d1.docs.aw-ol.com` being the official documentation website with the same logo), and the identifier `D1_DEV_DDR3_16X2_V1_2` on the back. 
The front side of both PCB versions has a variant of the Nezha logo. 
The back also has a sticker containing a QR code, with the board serial number below it. Scanning the QR code reveals the following URL: 
  * [https://d1.docs.allwinnertech.com?device=d1nezha#serial][6534] (with #serial replaced by the serial number)

# General Notes
The device is are sometimes being shipped with an SD with Debian installed. Console logs: <https://gist.github.com/heitbaum/e4dceeb7b236560b94cc66fce91cdd11>
Sometimes the device only ships with TinaLinux in NAND. Console logs booting into TinaLinux: <https://ovsienko.info/D1/minicom1.cap.txt>
The Debian images for the D1 can be found here: <https://ovsienko.info/D1/>
It is unknown how to boot from any of those images on the NAND only device. 
# Sunxi support
## Current status
Work based on mainline versions of Linux/U-Boot is very much a work in progress, and nothing finished/merged is currently available.
The BSP U-Boot/kernel use a NAND layout which merges a pair of pages from consecutive blocks into a super-page. Mainline uses the physical layout as-is. So while SPI NAND contents are accessible from both mainline and BSP kernels, they are only usable by one driver or the other. For this reason, it is recommended to install mainline software to an SD card, and leave the SPI NAND alone. 
Disabling the `CONFIG_AW_SPINAND_SIMULATE_MULTIPLANE` option in the BSP kernel should make its layout compatible with mainline, but this has not been tested. 
## Manual build
You can build things for yourself by following the instructions below. 
To build, you need a cross-compiler (riscv64-linux-gnu-gcc) and swig. 
### U-Boot
Boot firmware on the D1 consists of three parts, which largely correspond to the components used by 64-bit ARM SoCs: 
  1. U-Boot SPL (Secondary Program Loader) which is responsible for initializing DRAM and loading further firmware from storage.
  2. OpenSBI, which runs in machine mode and provides a standard "SBI" interface to less privileged modes. This is similar to how TF-A runs in EL3 and provides PSCI on 64-bit ARM.
  3. U-Boot proper, which initializes additional hardware and loads Linux from storage or the network.

#### OpenSBI
Mainline OpenSBI fully supports the C906 CPU and the Allwinner D1 SoC out of the box since version 1.1. You should use upstream OpenSBI, not any fork. 
[code] 
    git clone https://github.com/riscv-software-src/opensbi
    pushd opensbi
    make CROSS_COMPILE=riscv64-linux-gnu- PLATFORM=generic FW_PIC=y
    popd
    
[/code]
For recent versions of OpenSBI that include Kconfig support, you can reduce the size of the firmware by disabling almost all of the drivers. The only necessary ones are `FDT_IRQCHIP_PLIC`, `FDT_RESET_SUNXI_WDT`, and `FDT_SERIAL_UART8250`. 
[code] 
    make CROSS_COMPILE=riscv64-linux-musl- PLATFORM=generic menuconfig
    
[/code]
#### Mainline U-Boot
Mainline U-Boot support is mostly complete, but is not merged yet. Booting Linux from the network, USB, and an SD card works. Some refactoring of the various sunxi device drivers is still needed before any RISC-V sunxi platforms can be upstreamed. 
**NOTE: As of 2022-11-01, this branch includes full U-Boot SPL support, so using the BSP boot0 or a TOC1 image is no longer necessary.**
Download a patched version and compile it like so: 
[code] 
    git clone https://github.com/smaeul/u-boot -b d1-wip
    pushd u-boot
    make CROSS_COMPILE=riscv64-linux-gnu- nezha_defconfig
    make CROSS_COMPILE=riscv64-linux-gnu- OPENSBI=../opensbi/build/platform/generic/firmware/fw_dynamic.bin
    
[/code]
These commands will generate the file `u-boot-sunxi-with-spl.bin` which contains the entire firmware and can be written to an SD card, just like for ARM-based Allwinner boards. See [Bootable_SD_card#Bootloader][6535] for flashing instructions. 
You can also copy or symlink `fw_dynamic.bin` into the U-Boot build directory instead of exporting the `OPENSBI` variable. 
#### BSP U-Boot
BSP U-Boot is a heavily hacked U-Boot 2018-05 branch. Using it is not recommended. It is available at <https://github.com/Tina-Linux/u-boot-2018>
(This U-Boot also suit for Alleinner new chips after 2018) 
The main change is the modification of Makefle to suit the Tina Linux build system. 
There are some simple patches for port the BSP U-Boot to Buildroot: <https://github.com/YuzukiHD/Buildroot-YuzukiSBC/tree/master/buildroot/board/awol/nezha-d1s/patch/uboot>
#### BSP boot0 SPL
If you are using an old version of the mainline U-Boot branch, or the BSP U-Boot, you will need to use the BSP's boot0 as SPL. If you are using a current version of mainline U-Boot, you do not need this. 
This version has been modified so it can be built outside the BSP's build system, so it compiles with mainline GCC, and so it cooperates better with mainline firmware binaries. See the commit history for more details. Below is the process for building it and writing it to an SD card: 
[code] 
    git clone https://github.com/smaeul/sun20i_d1_spl -b mainline
    pushd sun20i_d1_spl
    make CROSS_COMPILE=riscv64-linux-gnu- p=sun20iw1p1 mmc
    sudo dd if=nboot/boot0_sdcard_sun20iw1p1.bin of=/dev/sdX bs=8192 seek=1
    popd
    
[/code]
The D1 boot ROM can read the boot0 SPL from two different locations: 
  * starting at sector 16
  * starting at sector 256

The location in sector 16 is incompatible with GPT partioning which by default uses 34 sectors. In gdisk you will have to reduce the number of entries in the partition table to ≤ 56 via the expert settings. So it may be preferable to write boot0 starting at sector 256 instead: 
[code] 
    sudo dd if=nboot/boot0_sdcard_sun20iw1p1.bin of=/dev/sdX bs=8192 seek=16
    
[/code]
A boot message tells you which location was used for booting: 
[code] 
    Loading boot-pkg Succeed(index=1)
    
[/code]
Index | Sector   
---|---  
0 | 16   
1 | 256   
Note that boot0 does some magic like enabling the T-HEAD ISA and MMU extensions. Those stay enabled all the way through entering Linux, which expects the custom PTE format. 
boot0 expects to load a TOC1 image containing OpenSBI and U-Boot (and a DTB). This is similar to, but incompatible with, mainline U-Boot SPL, which expects a FIT image. 
The mainline U-Boot branch builds a `mkimage` tool which contains rudimentary support for making TOC1 images. Since a TOC1 can contain multiple items, we must create a config file telling `mkimage` where to find them. Use the following content, adjusting the path to OpenSBI as needed: 
[code] 
    [opensbi]
    file = ../opensbi/build/platform/generic/firmware/fw_dynamic.bin
    addr = 0x40000000
    [dtb]
    file = u-boot.dtb
    addr = 0x44000000
    [u-boot]
    file = u-boot-nodtb.bin
    addr = 0x4a000000
    
[/code]
Now, continuing in the U-Boot directory, create the TOC1: 
[code] 
    vim toc1.cfg # or your editor of choice; see above
    tools/mkimage -T sunxi_toc1 -d toc1.cfg u-boot.toc1
    
[/code]
You should get output that looks like this: 
[code] 
    Allwinner TOC1 Image
    Size: 592896 bytes
    Contents: 3 items
     00000000:00000490 Headers
     00000600:00018720 => 40000000 opensbi
     00018e00:00007387 => 44000000 dtb
     00020200:00070820 => 4a000000 u-boot
    
[/code]
Now you can write this TOC1 to your SD card. Note the large (16+ MiB) offset! You will need to leave a gap before your first partition; 20 MiB should be plenty. (Or you can change `UBOOT_START_SECTOR_IN_SDMMC` in `include/spare_head.h` in boot0.) 
[code] 
    sudo dd if=u-boot.toc1 of=/dev/sdX bs=512 seek=32800
    
[/code]
If boot0 fails to load from the SD card sector 32800, it falls back to loading from the backup sector 24576. So it makes sense to write a U-Boot backup there: 
[code] 
    sudo dd if=u-boot.toc1 of=/dev/sdX bs=512 seek=24576
    
[/code]
### Linux Kernel
#### BSP Linux Kernel
The bsp Linux Kernel is available at <https://github.com/Tina-Linux/tina-d1x-linux-5.4>
#### Mainline kernel
A WIP branch is available at <https://github.com/smaeul/linux/commits/d1/all> which supports most of the hardware peripherals (Audio, Ethernet, MMC, SPI NAND, USB, RGB LCD, HDMI, MIPI DSI). 
Use the devicetree provided in RAM by the platform firmware (for U-Boot, this means `$fdtcontroladdr`). Do not load a DTB from storage. 
Build using: 
[code] 
    $ make ARCH=riscv nezha_defconfig
    ...
    $ make ARCH=riscv CROSS_COMPILE=riscv64-linux-gnu-
    ...
    
[/code]
#### Writing the kernel to SD card
You can create an ext4 partition that holds your kernel, but that partition needs to leave a gap at the start of the disk, as described above. 
In this filesystem, place the kernel in `/boot/Image` and in addition to this, create the file `/boot/extlinux/extlinux.conf` that looks similar to this: 
[code] 
    label default
    	linux /Image
    	append root=/dev/mmcblk0p2 rootwait console=ttyS0,115200 earlycon=sbi ignore_loglevel init=/lib/systemd/systemd
    
[/code]
## Build tool
### Buildroot
You can find a simple Buildroot usage at <https://github.com/YuzukiHD/Buildroot-YuzukiSBC>. 
### Yocto
The community-run [meta-riscv][6536] BSP layer includes support for the [nezha-allwinner-d1][6537]. 
  * U-Boot: <https://github.com/smaeul/u-boot/tree/d1-wip>
  * Linux kernel: <https://github.com/smaeul/linux/tree/d1/all>

### SkiffOS (Buildroot)
[SkiffOS][6538] uses Buildroot to compile a fully-featured Linux system for the Allwinner D1 including optional support for Docker containers and other applications. 
# Tips, Tricks, Caveats
## RV 86
If you have a [Lichee RV 86 Panel][6539] then build u-boot with the **lichee_rv_86_panel_defconfig** instead. 
## FEL mode
The `FEL` button triggers [ FEL mode][6540]. 
The [xfel][6541] tool has support for the D1 chip. Currently `sunxi-fel` (from [Sunxi-tools][6542]) lists the SoC as `unknown`. 
## JTAG
While in FEL mode, run `xfel jtag` to enable [JTAG][6543] access. 
Use an adjusted copy of Sipeed's config file ( <https://github.com/orangecms/RV-Debugger-BL702/tree/nezha> ) with OpenOCD for RISC-V: 
[code] 
    openocd --file tools/openocd/openocd-usb-sipeed.cfg
    Open On-Chip Debugger 0.11.0-rc1+dev-00001-g0dd3b7fa6-dirty (2020-12-24-20:50)
    Licensed under GNU GPL v2
    For bug reports, read
            http://openocd.org/doc/doxygen/bugs.html
    SiPEED USB-JTAG/TTL Ready for Remote Connections
    Info : Listening on port 6666 for tcl connections
    Info : Listening on port 4444 for telnet connections
    Info : clock speed 1000 kHz
    Info : JTAG tap: riscv.cpu tap/device found: 0x08052b43 (mfg: 0x5a1 (<unknown>), part: 0x8052, ver: 0x0)
    Error: riscv.cpu: IR capture error; saw 0x1f not 0x01
    Warn : Bypassing JTAG setup events due to errors
    Error: dtmcontrol is 0. Check JTAG connectivity/board power.
    Warn : target riscv.cpu.0 examination failed
    Info : starting gdb server for riscv.cpu.0 on 3333
    Info : Listening on port 3333 for gdb connections
    Info : accepting 'gdb' connection on tcp/3333
    
[/code]
TODO: figure out the "examination" 
## DRAM Driver
As usual there is no documentation for the memory controller or PHY IP used here. The baseline of this code was lifted from [awboot][6544], which seems to be based on some form of de-compilation of some original Allwinner code bits (with a GPL2 license tag from the very beginning). This version here is a reworked version, to match the U-Boot coding style and style of the other Allwinner DRAM drivers. 
This driver comes with a minimum baremetal for testing. Tested with D1-H, R528, T113 and D1s(F133) 
<https://github.com/YuzukiHD/TinyKasKit/tree/master/d1s-dramc>
## Enabling U-Boot command line
The preinstalled version of U-Boot requires holding down "S" during boot to enter the command line. From a booted Linux system (like the Tina Linux preinstalled in the on-board NAND) run the following command to set a three second delay during which it's possible to enter the command line on the built-in serial port: 
[code] 
    fw_setenv bootdelay 3
[/code]
Note: With the Debian image being shipped - <http://mirrors.perfxlab.cn/debian-ports> the fw_setenv and fw_printenv are not aligned to the saveenv location. 
[code] 
    Debian GNU/Linux 11 RVBoards ttyS0
    Linux RVBoards 5.4.61 #22 PREEMPT Wed Jun 16 07:27:49 UTC 2021 riscv64
    # fw_printenv
    Configuration file wrong or corrupted
    
[/code]
## Default Firmware Environment
The default firmware environment for the TinaLinux board: 
[code] 
    root[at]TinaLinux:/# fw_printenv 
    earlyprintk=sunxi-uart,0x02500000
    initcall_debug=0
    console=ttyS0,115200
    nand_root=/dev/ubiblock0_5
    mmc_root=/dev/mmcblk0p5
    mtd_name=sys
    rootfstype=squashfs
    root_partition=rootfs
    boot_partition=boot
    init=/sbin/init
    loglevel=8
    cma=8M
    mac=
    wifi_mac=
    bt_mac=
    specialstr=
    keybox_list=widevine,ec_key,ec_cert1,ec_cert2,ec_cert3,rsa_key,rsa_cert1,rsa_cert2,rsa_cert3
    dsp0_partition=dsp0
    setargs_nand=setenv bootargs ubi.mtd=${mtd_name} ubi.block=0,${root_partition} earlyprintk=${earlyprintk} clk_ignore_unused initcall_debug=${initcall_debug} console=${console} loglevel=${loglevel} root=${nand_root} rootfstype=${rootfstype} init=${init} partitions=${partitions} cma=${cma} snum=${snum} mac_addr=${mac} wifi_mac=${wifi_mac} bt_mac=${bt_mac} specialstr=${specialstr} gpt=1
    setargs_nand_ubi=setenv bootargs ubi.mtd=${mtd_name} ubi.block=0,${root_partition} earlyprintk=${earlyprintk} clk_ignore_unused initcall_debug=${initcall_debug} console=${console} loglevel=${loglevel} root=${nand_root} rootfstype=${rootfstype} init=${init} partitions=${partitions} cma=${cma} snum=${snum} mac_addr=${mac} wifi_mac=${wifi_mac} bt_mac=${bt_mac} specialstr=${specialstr} gpt=1
    setargs_mmc=setenv  bootargs earlyprintk=${earlyprintk} clk_ignore_unused initcall_debug=${initcall_debug} console=${console} loglevel=${loglevel} root=${mmc_root} rootwait  init=${init} partitions=${partitions} cma=${cma} snum=${snum} mac_addr=${mac} wifi_mac=${wifi_mac} bt_mac=${bt_mac} specialstr=${specialstr} gpt=1
    boot_dsp0=sunxi_flash read 45000000 ${dsp0_partition};bootr 45000000 0 0
    boot_normal=sunxi_flash read 45000000 ${boot_partition};bootm 45000000
    boot_recovery=sunxi_flash read 45000000 recovery;bootm 45000000
    boot_fastboot=fastboot
    bootcmd=run setargs_nand boot_dsp0 boot_normal
    bootdelay=0
    
[/code]
## Oops tracing
To get a valid callstack from an OOPS, you need to enable **CONFIG_FRAME_POINTER** or else the callstacks are not reliable. 
# Adding a serial port
[![][6545]][6546]
[][6547]
Allwinner Nezha UART pads
The `DEBUG` header at the top-right corner of the board can be used as a serial port. See the [UART howto][6548] for instructions about how to attach to it. The default baud rate is 115200. 
# Adding a reset pin
The test pin T6, as per the manual and verified, is the reset pin (RST). A wire can be attached to it, and for convenience, routed to one of the N/C (not connected) pins on the GPIO header. It can be used for test and development automation. 
# Development and test automation
A simple strategy for test automation and bringup development is as follows: 
  * attach a wire to the FEL button (possibly route to an N/C pin on the GPIO header)
  * attach a wire to the reset pin
  * attach to the UART interface
  * connect to the USB-C OTG
  * connect to the ethernet port

To test an firmware/OS image, hold FEL, trigger reset, release FEL, then use xfel to bring up DRAM, load the image, and execute it. Watch the output on the UART, try input, and see if the device becomes visible on the network. 
This can be fully automated, e.g., using another development board offering all the necessary interfaces. It can be instrumented via CI, e.g., as a GitLab runner using [ConTest][6549]. 
# Pictures
  * [![Allwinner Nezha Front.jpg][6550]][6492]
  * [![Allwinner Nezha Back.jpg][6551]][6552]
  * [![Allwinner Nezha UART.jpg][6553]][6546]
  * [![Nezha-reset.jpeg][6554]][6555]

# Schematic
  * [V1.0 board schematic][6556]
  * [V1.0 board layout and silkscreen][6557]

# See also
  * [IndieGogo campaign][6558]
  * [Data gathering thread on whycan.com (chinese)][6559]

## Manufacturer images
  * [D1_Nezha_HDMI_test_firmware Image from whycan.com (requires regristration)][6560]
