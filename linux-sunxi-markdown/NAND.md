# NAND
[![MBOX icon important.png][38678]][38679] | This page provides installation instructions for the legacy unmaintained u-boot-sunxi and sunxi-3.4 kernel forks. Although it contains useful information how things work, driver for mainline kernel (3.14+) has [its own page here][38680].   
---|---  
  

[![MBOX icon important.png][38678]][38679] | Also see: [Mainline_NAND_Howto][38681] and [Linux_mainlining_effort#Status_Matrix][38682].   
---|---  
In the sunxi world, NAND (a type of flash memory) signifies the on board flash memory of a sunxi device. Our main u-boot version currently does not support booting from NAND and an altered allwinner version or an experimental MTD u-boot version (with MTD kernel driver) needs to be used instead. 
## Contents
  * [1 Background][38683]
  * [2 Installing to NAND][38684]
  * [3 nand-part][38685]
    * [3.1 nand-part output][38686]
  * [4 MTD driver][38687]
    * [4.1 MTD driver for sunxi-3.4 kernel][38688]
    * [4.2 MTD driver for mainline Linux kernel (3.14+)][38689]
  * [5 More information on BROM NAND][38690]
  * [6 Manufacturers][38691]
    * [6.1 SK Hynix][38692]
      * [6.1.1 H27UCG8T2ATR-BC][38693]
  * [7 See also][38694]
  * [8 Documents][38695]

# Background
Our SoCs have a very specific [ boot process][38696]. First it executes [ a tiny on chip rom (BROM)][38697] which then checks the buttons for [FEL][38698] mode and then starts checking the various storage options for a valid boot signature at the right location. 
There is no real difference between NAND and an SD-card apart from the fact that directly attached flash use the Sunxi NAND controller directly while SD-Cards come with a standard interface and an embedded controller usually based today on cortex-m0 core that runs proprietary firmware which implements flash translation layer that performs wear leveling. The sunxi nand controller is harder to implement than the sunxi sd-card controller, and the sample code provided by allwinner is rather large (and shared between U-boot and the kernel). 
Then there is the NAND hw randomizer that gets in the way. Allwinner uses one setting for the BROM and the second boot stage (boot0/SPL), and another setting for normal use. With this setup, it is currently not implemented to access both bits at the same time. This currently provides another barrier for implementation, as one first needs to be able to read/write this area. While this is not beyond fixing, these are quite a few hoops to jump through. 
As a result of the above, we have to use the existing second and third stages of the allwinner nand boot process, and we need to use nand-part for partitioning. If we had proper u-boot support, we would not need any of that. 
It is very likely that this usage of the NAND is going to disappear completely in future. The plans for mainline support currently involves a [MTD device driver][38687], and no longer a block device driver. This would render a large part of the content of this wiki page outdated. 
# Installing to NAND
There is [a nice, full howto][38699] available which explains how to install and boot from NAND. 
# nand-part
There is a utility which is part of [sunxi-tools][38700], called nand-part. It has many many issues: 
  * The licensing is all muddled up. The author is not chinese, but the main file which only carries his copyright has chinese comments.
  * Barely passes as C-code. There are very few C style comments, and return values are 1 for success and 0 for failure.
  * Doesn't care about the size of the block device (how hard would it have been to check BLKGETSIZE64), and allows the creation of partition tables which are not contained within the bounds of the block device.
  * There are two known versions of allwinner nand partition tables. Instead of checking the magic and version fields, the code is fully duplicated but with different structs, and both versions of the code get run to see which one sticks. This needs to have the two versions of the structs living side by side (version the structure names!).

It needs a day or so of work by a proper coder. 
As an extra, the format of the allwinner nand partitioning is really simple. It should be easy to write a simple interactive user interface like fdisk has, as the amount of options are really limited. **m** , **p** , **n** , **d** , **v** , **w** , **q** for the standard uses, and **f** for toggling a mode which gives the ability to alter the first partition and for changing the partitioning version. 
This utility can be redeveloped without hardware. A dump of the nand of a machines first MB, plus a dd from /dev/zero, can be presented as a loop device. For an example of this, check [ this][38701]. 
## nand-part output
Below is the typical output of the nand partitioning of a Mele A1000. 
[code] 
    check partition table copy 0: mbr: version 0x00000100, magic softw311
    OK
    check partition table copy 1: mbr: version 0x00000100, magic softw311
    OK
    check partition table copy 2: mbr: version 0x00000100, magic softw311
    OK
    check partition table copy 3: mbr: version 0x00000100, magic softw311
    OK
    mbr: version 0x00000100, magic softw311
    9 partitions
    partition  1: class =         DISK, name =       BOOTFS, partition start =     2048, partition size =    32768 user_type=0
    partition  2: class =         DISK, name =      LROOTFS, partition start =    34816, partition size =    65536 user_type=2
    partition  3: class =         DISK, name =    LSYSTEMFS, partition start =   100352, partition size =   524288 user_type=2
    partition  4: class =         DISK, name =      LDATAFS, partition start =   624640, partition size =  3145728 user_type=2
    partition  5: class =         DISK, name =         MISC, partition start =  3770368, partition size =     2048 user_type=2
    partition  6: class =         DISK, name =  LRECOVERYFS, partition start =  3772416, partition size =    65536 user_type=2
    partition  7: class =         DISK, name =     LCACHEFS, partition start =  3837952, partition size =   262144 user_type=2
    partition  8: class =         DISK, name =          env, partition start =  4100096, partition size =     4096 user_type=0
    partition  9: class =         DISK, name =        UDISK, partition start =  4104192, partition size =        0 user_type=0
    check partition table copy 0: mbr: version 0x00000100, magic softw311
    OK
    check partition table copy 1: mbr: version 0x00000100, magic softw311
    OK
    check partition table copy 2: mbr: version 0x00000100, magic softw311
    OK
    check partition table copy 3: mbr: version 0x00000100, magic softw311
    OK
    mbr: version 0x00000100, magic softw311
    9 partitions
    partition  1: class =         DISK, name =       BOOTFS, partition start =     2048, partition size =    32768 user_type=0
    partition  2: class =         DISK, name =      LROOTFS, partition start =    34816, partition size =    65536 user_type=2
    partition  3: class =         DISK, name =    LSYSTEMFS, partition start =   100352, partition size =   524288 user_type=2
    partition  4: class =         DISK, name =      LDATAFS, partition start =   624640, partition size =  3145728 user_type=2
    partition  5: class =         DISK, name =         MISC, partition start =  3770368, partition size =     2048 user_type=2
    partition  6: class =         DISK, name =  LRECOVERYFS, partition start =  3772416, partition size =    65536 user_type=2
    partition  7: class =         DISK, name =     LCACHEFS, partition start =  3837952, partition size =   262144 user_type=2
    partition  8: class =         DISK, name =          env, partition start =  4100096, partition size =     4096 user_type=0
    partition  9: class =         DISK, name =        UDISK, partition start =  4104192, partition size =        0 user_type=0
    
[/code]
# MTD driver
MTD U-Boot default partition table: 
Partition Size | Uses   
---|---  
1M | U-Boot SPL   
4M | U-Boot   
3M | U-Boot Enviroment   
9M | Packimg(combine kernel & script.bin)   
8M | Linux Kernel   
64M | Initramfs/Small rootfs   
- | Uses for custom   
## MTD driver for sunxi-3.4 kernel
[MTD driver for sunxi-3.4 kernel][38702] requires [modified u-boot][38703]. It is not stable and therefore not suitable for production environment. 
## MTD driver for mainline Linux kernel (3.14+)
[MTD driver for Linux 3.14+][38704] is currently in progress of [being reviewed][38705] and has [its own page here][38680]. 
# More information on BROM NAND
The BROM contains a very basic NAND driver that does not support bad blocks. This driver also does **not** use Chip ID to identify the part, like the Linux NAND driver does, and so it blindly attempts to read Boot0 out of Flash using a sequence of predefined configurations. For A10/A20, the configurations, in order, are as follows: 
Interface | Hardware page | Address cycles | ECC capacity | ECC page | CPU   
---|---|---|---|---|---  
asynchronous | 1024 B | 5 | 64 b | 1024 B | A10/A20   
asynchronous | 1024 B | 5 | 64 b | 512 B | A10/A20   
asynchronous | 1024 B | 4 | 64 b | 1024 B | A10/A20   
asynchronous | 1024 B | 4 | 64 b | 512 B | A10/A20   
asynchronous | 8192 B | 5 | 24 b | 1024 B | A20   
asynchronous | 8192 B | 5 | 40 b | 1024 B | A20   
asynchronous | 4096 B | 5 | 64 b | 1024 B | A20   
asynchronous | 4096 B | 5 | 64 b | 512 B | A20   
DDR timing 1 | 1024 B | 5 | 64 b | 1024 B | A10/A20   
DDR timing 2 | 1024 B | 5 | 64 b | 1024 B | A10/A20   
DDR timing 3 | 1024 B | 5 | 64 b | 1024 B | A10/A20   
DDR timing 1 | 1024 B | 5 | 64 b | 512 B | A10/A20   
DDR timing 2 | 1024 B | 5 | 64 b | 512 B | A10/A20   
DDR timing 3 | 1024 B | 5 | 64 b | 512 B | A10/A20   
DDR timing 1 | 4096 B | 5 | 64 b | 512 B | A20   
DDR timing 2 | 4096 B | 5 | 64 b | 512 B | A20   
DDR timing 3 | 4096 B | 5 | 64 b | 512 B | A20   
Note that a lot of modern Flash (large page NAND) would not be supported well by the configurations available on A10, so A20 adds a whole bunch. 
At first, the BROM tries to use all of those configurations to read a Boot0 image starting at page 0 of Flash. However, because of bad blocks (or other considerations like partition table location), all of those options may fail. BROM will then attempt reading a Boot0 image starting at pages 0x40, 0x80, 0xC0, ..., 0x1C0. Only then will it give up and proceed with other boot options (or FEL). 
looks to me that H3 is looking only at 0x00, 0x80, 0x100... tried it with 
page 0 0x00000 -> worked 
page 0x40 0x20000 -> not worked (0x20000 -> 64*2048(=pagesize)) 
page 0x80 0x40000 -> worked 
page 0xC0 0x60000 -> not worked 
page 0x100 0x80000 -> worked 
wrote u-boot spl under linux with: "nandwrite --start=0x80000 -o -n /dev/mtd0 sunxi-spl-with-ecc.bin" 
# Manufacturers
## SK Hynix
#### H27UCG8T2ATR-BC
NAND 64Gb(8192M x 8bit) Legacy MLC NAND Flash, page: 8,192 + 640 bytes, block: 256 pages = 2M + 160K bytes, device: 4180 blocks = 73,835,520 Kbits 
Datasheet: <http://www.szyuda88.com/uploadfile/cfile/2013419135343223.pdf>
# See also
  * [Open NAND Flash Interface Specification][38706].

# Documents
  * [File:A33 Nand Flash Controller Specification.pdf][38707](PDF, 29 pages, 2014-02-28)
