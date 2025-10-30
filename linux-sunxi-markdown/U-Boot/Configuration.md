# U-Boot/Configuration
< [U-Boot][56421]
 
This article provides a collection of various scenarios for booting with U-Boot. 
## Contents
  * [1 Boot][56424]
  * [2 Setting u-boot environment variables][56425]
  * [3 SD Card (legacy kernel)][56426]
  * [4 NAND][56427]
  * [5 NFS][56428]
  * [6 FB console][56429]
  * [7 LCD Settings][56430]

## Boot
For getting these bits loaded onto the hardware, please refer to the respective howto: 
  * [ SD Card][56431]
  * [NAND][56432]
  * [ SPI NOR Flash][56433]
  * [ USB OTG][56434]
  * [ Ethernet][56435]

For booting from sd with mainline u-boot, the recommended way is: 
  * create a file _boot.cmd_ on the first partition (also check [Kernel arguments][56436] for extra 'bootargs' options):

mainline kernel  | sunxi-3.4 kernel   
---|---
[code] 
    setenv bootargs console=ttyS0,115200 root=/dev/mmcblk0p2 rootwait panic=10
    load mmc 0:1 0x43000000 ${fdtfile} || load mmc 0:1 0x43000000 boot/${fdtfile}
    load mmc 0:1 0x42000000 uImage || load mmc 0:1 0x42000000 boot/uImage
    bootm 0x42000000 - 0x43000000
    
[/code]  
| 
[code] 
    setenv bootm_boot_mode sec
    setenv bootargs console=ttyS0,115200 root=/dev/mmcblk0p2 rootwait panic=10
    load mmc 0:1 0x43000000 script.bin || load mmc 0:1 0x43000000 boot/script.bin
    load mmc 0:1 0x42000000 uImage || load mmc 0:1 0x42000000 boot/uImage
    bootm 0x42000000
    
[/code]  
    [![Information.png][56437]][56438] If you're wondering why setting **bootm_boot_mode** might be necessary for older kernels, have a look at the details of [PSCI][56439].
    [![Sticky-note-pin.png][56440]][56441] _Note:_ Directly using a **zImage** is also supported by U-Boot for the sunxi platform. Substitute _zImage_ in place of _uImage_ in the commands above, and then use the **bootz** command instead of _bootm_.
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
## SD Card (legacy kernel)
[code] 
    setenv bootargs console=ttyS0,115200 root=/dev/mmcblk0p2 rootwait panic=10 ${extra}
    ext2load mmc 0 0x43000000 script.bin
    ext2load mmc 0 0x48000000 uImage
    bootm 0x48000000
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
Recent version of U-Boot are able to boot from NFS as well as TFTP, but you have to get rid of the automatic setup of FTP. Check [ Ethernet][56435] for more information. 
[![Sticky-note-pin.png][56440]][56441] _Note:_ on the A20 based cubieboards, this only seems to work on the stable kernel, not on stage. 
## FB console
To get U-Boot output shown on the built-in framebuffer driver (currently, HDMI only at 1024x768), add the following to your boot.cmd: 
[code] 
    setenv stdout=serial,vga
    setenv stderr=serial,vga
[/code]
The default environment has these values set as well. 
## LCD Settings
There is a [separate wiki page about configuring LCD][56442] in U-Boot.
