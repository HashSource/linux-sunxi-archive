# Installing to NAND
[![MBOX icon important.png][27794]][27795] | This page provides installation instructions for the legacy **unmaintained** u-boot-sunxi and sunxi-3.4 kernel forks. Although it contains useful information how things work, driver for mainline kernel (3.14+) has [its own page here][27796].   
---|---  
This page explains how to put a full sunxi system on the NAND flash of your device. 
## Contents
  * [1 Prerequisite][27797]
  * [2 Backup NAND][27798]
    * [2.1 First MB][27799]
    * [2.2 Boot partition][27800]
    * [2.3 Full backup][27801]
    * [2.4 Accessing the full backup][27802]
  * [3 Partitioning][27803]
    * [3.1 nand-part][27804]
    * [3.2 Usage][27805]
    * [3.3 Example table][27806]
    * [3.4 Detailed usage information][27807]
    * [3.5 Store original table][27808]
    * [3.6 Verify nanda fs size][27809]
    * [3.7 Create the new partitioning][27810]
  * [4 U-Boot][27811]
    * [4.1 Get a toolchain][27812]
    * [4.2 Repository][27813]
    * [4.3 Determine build target][27814]
    * [4.4 Build][27815]
    * [4.5 Installation][27816]
    * [4.6 Booting][27817]
  * [5 kernel][27818]
  * [6 Create rootfs][27819]
  * [7 Sunxi Logo][27820]
  * [8 Boot][27821]

# Prerequisite
Since the NAND is soldered to the board, it is impossible to access it from any other machine but your device itself (without some specialist equipment). You first will need to get proper access to your device, for instance, [ by first building an SD-card][27822] and booting off of that. Note that "/dev/nand" is a linux-sunxi feature, and as such you will need to be running a linux-sunxi kernel to make use of it. Using other kernels (like the one on the stock Android image of your device) won't be of use. 
# Backup NAND
## First MB
It is **absolutely vital** to have a copy of the data in the first megabyte of your NAND. This contains the boot0 bootloader. If anything goes wrong, you can use this to set up a working nand boot partition again. 
[code] 
    dd if=/dev/nand of=nand.mbr.img bs=1M count=1
[/code]
## Boot partition
It is **absolutely vital** to have a copy of the data in the boot partition. If anything goes wrong, you can use these files to set up a working nand boot partition again. 
Mount nand somewhere nice, for instance a directory called _nanda.original_ and then tar it up: 
[code] 
    tar -zcvf nanda.original.tar.gz nanda.original
[/code]
## Full backup
While this is not as crucial as the first MB and the boot partition, it might be safer to also create an almost full copy of your nand. 
[code] 
    dd if=/dev/nand of=/some/place/with/enough/space
[/code]
If you do not have enough space on your SD-Card, then you need to get creative with SSHFS or NFS. 
## Accessing the full backup
If you need access to the content of the full backup later on, you can use losetup. 
The below example sets up a loop device for a nanda partition at 16MB: 
[code] 
    losetup -fro 16777216 /some/file
[/code]
# Partitioning
Because we need to use the existing first boot layers, and because of our nand drivers, we need to take very special care of our nand, and we need a special tool to partition the nand. 
## nand-part
The special partitioning tool is called [_nand-part_][27823] and it is part of [our sunxi-tools repository][27824]. Build it with a cross-compiler, or on the target device itself. 
## Usage
[code] 
    usage: ./nand-part [-f a10|a20] nand-device
           ./nand-part nand-device 'name2 len2 [usertype2]' ['name3 len3 [usertype3]'] ...
           ./nand-part [-f a10|a20] nand-device start1 'name1 len1 [usertype1]' ['name2 len2 [usertype2]'] ...
    
[/code]
The rudimentary user-interface of _nand-part_ requires you to specify each partition in single quotes. The 'start' and 'len' values are provided in sectors, so 512bytes. 
nand-part also is not smart enough to verify the size of your device. It will happily create partitions beyond the end of your device. The kernel correctly catches this and will provide the right sized devices, and the standard linux file-system creations tools will listen to what the kernel tells them. Nand-part only alters the partition table and not any filesystems, so you no information actually gets lost if you write a wrong partition table and later on restore the original. 
## Example table
Here is an example table from a hyundai A7HD with 8GB NAND, as provided by _nand-part_ : 
[code] 
    Using NAND /dev/nand, with 15958016 sectors (7792.0MB).
    
    ...
    
    mbr: version 0x00000100, magic softw311
    9 partitions
    partition  1: class =         DISK, name =   bootloader, partition start =     2048, partition size =    32768 user_type=0
    partition  2: class =         DISK, name =          env, partition start =    34816, partition size =     4096 user_type=0
    partition  3: class =         DISK, name =         boot, partition start =    38912, partition size =    65536 user_type=0
    partition  4: class =         DISK, name =       system, partition start =   104448, partition size =   614400 user_type=2
    partition  5: class =         DISK, name =         data, partition start =   718848, partition size =  1048576 user_type=2
    partition  6: class =         DISK, name =         misc, partition start =  1767424, partition size =     2048 user_type=2
    partition  7: class =         DISK, name =     recovery, partition start =  1769472, partition size =    65536 user_type=2
    partition  8: class =         DISK, name =        cache, partition start =  1835008, partition size =   524288 user_type=2
    partition  9: class =         DISK, name =        UDISK, partition start =  2359296, partition size = 13598720 user_type=0
    
[/code]
Note that all offsets and sizes for nand-part are provided in sectors, so they are 512bytes large. We can see the actual sizes by running: 
[code] 
    sfdisk -s
    /dev/nand:   7979008
    /dev/nanda:     16384
    /dev/nandb:      2048
    /dev/nandc:     32768
    /dev/nandd:    307200
    /dev/nande:    524288
    /dev/nandf:      1024
    /dev/nandg:     32768
    /dev/nandh:    262144
    /dev/nandi:   6799360
    /dev/mmcblk0:   7830528
    total: 23787520 blocks
    
[/code]
The _sfdisk_ output, in this case, counts the sd-card in, and counts the nand twice, for the total block (1kB) count. 
Note the position and size of the _bootloader_ partition. The first MB is reserved for the MBR and the _boot0_ stage of the bootloader. The _bootloader_ partition contains a FAT16 fs. For many devices, the _bootloader_ partition starts at 16MB, but for the hyundai it starts at 1MB. 
## Detailed usage information
In the standard usage mode, the _boot_ partition will not be touched. 
[code] 
    ./nand-part  /dev/nand 'root 7405568'
[/code]
This will create a single partition called _root_ which is 3616MB large, right after your _boot_ partition. The awkward user interface of nand-part requires you to list all partitions in sequence. A new run of the above command will not add a second _root_ partition after the freshly created one. 
This will then create: 
[code] 
    ...
    mbr: version 0x00000100, magic softw311
    2 partitions
    partition  1: class =         DISK, name =   bootloader, partition start =    2048, partition size =    32768 user_type=0
    partition  2: class =         DISK, name =         root, partition start =   34816, partition size =  7405568 user_type=0
    
[/code]
If you force the partitioning type, with the option '-f a10' or '-f a20', then everything has to be specified: 
[code] 
    ./nand-part -f a20 /dev/nand 32768 'boot 32768' 'root 7405568'
[/code]
This will then create: 
[code] 
    ...
    mbr: version 0x00000200, magic softw411
    2 partitions
    partition  1: class =         DISK, name =         boot, partition start =    32768, partition size =    32768 user_type=0
    partition  2: class =         DISK, name =         root, partition start =    65536, partition size =  7405568 user_type=0
    
[/code]
Note that you should never change partitioning versions like that if you wish to keep your system bootable. Also, some verions of Allwinner-boot will check that there is actually a partition called 'boot' and will not work otherwise. 
## Store original table
It is **important** that you keep a copy of the original output of nand-part around. You can use it later to restore your partition table if something goes wrong. 
[code] 
    ./nand-part > nand-part.orig.txt
[/code]
## Verify nanda fs size
At this point it is important to verify the size of the FAT16 filesystem of the boot partition. There [ have been cases where vendors have messed this up][27825], and we need to either retain or recreate this filesystem (the latter from [ the back-up][27800]). So mount _/dev/nanda_ and check the size of the filesystem with some simple like df, and verify this against the output of _nand-part_ or _sfdisk -s_
If you need to recreate the filesystem, run: 
[code] 
    mkfs.msdos -F16 /dev/nanda
[/code]
This will complain about unknown sector sizing, but this can be ignored. 
Then you need to get the contents of [ your backup tarball][27800] copied back into your new /dev/nanda. 
## Create the new partitioning
For the provided Hyundai A7HD example, the nanda fs is correct, so we substract the start and the size of 'Partition 1' off the size of the nand (in bash): 
[code] 
    echo $[15958016 - 2048 - 32768]
[/code]
Which returns 15923200. Then run the following: 
[code] 
    ./nand-part /dev/nand 2048 'boot 32768' 'root 15923200'
[/code]
This creates the following table: 
[code] 
    ...
    
    mbr: version 0x00000100, magic softw311
    2 partitions
    partition  1: class =         DISK, name =         boot, partition start =    2048, partition size =    32768 user_type=0
    partition  2: class =         DISK, name =         root, partition start =   34816, partition size = 15923200 user_type=0
    
[/code]
This renamed the 'bootloader' partition to 'boot' and kept its position and size. Then a single large partition was created to cover the rest of the NAND. 
Note: if you cannot boot stock kernel, set last partition size to zero, it will be automaticly expanded. 
# U-Boot
As stated several times before, we need a special allwinner version of u-boot to be able to boot from nand. 
## Get a toolchain
Refer to the [ Toolchain step of the U-Boot compilation howto.][27826]
## Repository
You just need to checkout out a specific branch from [ the standard u-boot repository][27827]. 
[code] 
     git checkout lichee-dev
[/code]
## Determine build target
For this version of u-boot, there are very few board specific settings, and your system ram might be configured wrong because of it. 
[code] 
    grep allwinner boards.cfg | awk '{print $1}'
[/code]
## Build
Refer to the [ Build step of the U-Boot compilation howto.][27828]
## Installation
The resulting _u-boot.bin_ binary needs to be copied to the _linux/_ directory from the boot partition in _/dev/nanda_
## Booting
This version of u-boot currently has the configuration hardcoded. It will automatically boot _linux/uImage_ in _/dev/nanda_ , with a serial console, and with _/dev/nandb_ as the root file system. 
# kernel
The standard sunxi-3.4 kernel needs no special changes for booting off of nand. [Linux_Kernel#Compilation Build it as usual][27829], and then make sure you install the _uImage_ in the _linux_ directory from the boot partition in _/dev/nanda_. 
# Create rootfs
You can now create your favourite filesytem on /dev/nandb, or for instance just run: 
[code] 
    mkfs.ext4 /dev/nandb
[/code]
After which you should be able to mount this partition and [ install a rootfs][27830]. 
Before booting into this, remember to copy your modules into the rootfs. 
# Sunxi Logo
Now that you are running a proper sunxi installation on your device, you will probably dislike the Android logo shown for a few seconds during booting. A quick fix for this is to get [this bitmap file][27831], and to overwrite the _linux.bmp_ in the _linux/_ directory from the boot partition in _/dev/nanda_
You can of course create your own, but it's not the best way to spend ones time for a result which is shown for just a few seconds. 
# Boot
If all went well, your system should now just boot off of your new sunxi installation on NAND.
