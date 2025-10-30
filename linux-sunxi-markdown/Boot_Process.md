# Boot Process
Our SoCs have a very specific boot process. First it executes [ a tiny on chip rom (BROM)][10478] which then checks the buttons for [FEL][10479] mode and then starts checking the various storage options for a valid boot signature at the right location. 
Generally, the BROM first check [ SD-card][10480] boot availability, then in second, [NAND][10481] one. The BROM will try to load the [SPL][10482] from U-Boot in each of these devices, which in turn loads the [kernel][10483]. 
## Contents
  * [1 NAND and SD-card][10484]
  * [2 Other][10485]
  * [3 Determining boot source][10486]
    * [3.1 Network][10487]
    * [3.2 SATA][10488]
    * [3.3 USB][10489]
  * [4 A10 Boot overview][10490]

# NAND and SD-card
There is no real difference between NAND and an SD-card apart from the fact that directly attached flash use the Sunxi NAND controller directly while SD-Cards come with a standard interface and an embedded controller. The sunxi nand controller is harder to implement than the sunxi sd-card controller, and the sample code provided by allwinner is rather large (and shared between [U-boot][10491] and the kernel). 
  * "[Bootable SD card][10480]" article contains more informations about SD card boot process and explains how to make a bootable SD card.
  * "[NAND][10481]" article contains more informations about NAND boot process
  * "[Installing to NAND][10492]" article contains informations to make a bootable NAND.

# Other
That's also possible to boot system on other devices (SATA, USB, network using TFTP/NFS,...) but [U-boot][10491] standing on NAND or SD card is needed as first boot step. 
# Determining boot source
On boards that have a choice of different boot media, it is sometimes useful to determine which device the bootloader was started from. In U-Boot, this can be done by inspecting the byte at address 0x28 (tested on S3): 
[code] 
       => md.b 0x28 1
       00000028: 03
    
[/code]
In this case, the value 03 indicates that we booted from SPI NOR. The byte reads 0 when booting from SD card. 
## Network
The kernel can be loaded using TFTP, that is supported by U-boot and system can be booted using NFS. In network boot process, each of this choice are not mandatory for the other one. 
  * "[How_to_boot_the_A10_or_A20_over_the_network][10493]" explains how to configure U-boot for TFTP boot and NFS for system network boot process.

## SATA
[A10][10494] and [A20][10495] SoCs, support [SATA][10496] controler. U-boot also support SATA boot process. That's so possible to boot on SATA device (hard disc drive, solid state device, ...). 
In this case, [initial Ramdisk][10497] is needed. 
  * [Category:Devices with SATA port][10498] contains list of devices with SATA port.

## USB
Most devices with Allwinner SoC have USB ports. U-boot also support USB Boot but U-boot needs to be built specifically for booting over USB 
  * [FEL/USBBoot][10499] explains how to prepare U-boot for USB boot.

# A10 Boot overview
While the Allwinner series of SoC's are quite open, there is an unmodifiable ROM called [BROM][10478] or Boot ROM that is in charge of booting the SoC. The BROM will try to load the [SPL][10482] from U-Boot, which in turn loads the kernel. 
It should be noted, that if using Allwinner bootloaders (especially true when booting from nand storage), the order is slightly different. [BROM][10478] loads boot0 as its SPL and that chainloads boot1. These all reside in unaccessable (not easily anyway) nand flash, before the partition table. boot1 loads [boot.axf][10500] from the first fat partition which in turn chainloads (in our case) u-boot and then the kernel. It is in theory possible to directly boot the kernel, or some other OS. Also boot.axf has the ability to display images on the framebuffer.
