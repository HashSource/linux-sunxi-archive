# Boot Android from SdCard
## Contents
  * [1 How to create bootable Android SdCard][10413]
    * [1.1 Extract file from Android Image][10414]
      * [1.1.1 Extract Kernel and Ramdisk][10415]
      * [1.1.2 Extract system image:][10416]
      * [1.1.3 Extract recovery image:][10417]
      * [1.1.4 Decompress the ramdisk data:][10418]
    * [1.2 SD card Partition][10419]
      * [1.2.1 Format][10420]
    * [1.3 BootLoader][10421]
    * [1.4 Copy to SD card][10422]
  * [2 Automated Flash Kitchen][10423]
    * [2.1 Requirements][10424]
    * [2.2 Enhancements][10425]
    * [2.3 General information][10426]
  * [3 Pre-built A10 SDcard images][10427]

## How to create bootable Android SdCard
First extract needed files from an android image , You will need awutils and android tools. 
[code] 
      $ wget <http://dl.linux-sunxi.org/users/arete74/tools.tar.gz>
      $ tar -zxvf tools.tar.gz
    
[/code]
[AWUtils][10428]
[code] 
      $ git clone <https://github.com/Ithamar/awutils.git>
      $ cd awutils
      $ make
    
[/code]
### Extract file from Android Image
Resources for Cubieboard A10: 
  * <http://docs.cubieboard.org/tutorials/cb1/installation/cubieboard_android-4.0.x_release>
  * <http://dl.cubieboard.org/model/cubieboard1/Image/android/>

In this guide the name of the Android Image is android.img 
[code] 
      $ awimage -u android.img
    
[/code]
This command creates a folder called android.dump which will contain many files. The three following files are the ones we are interested in: 
**RFSFAT16_BOOT_00000000000** (the boot partition) 
**RFSFAT16_RECOVERY_0000000** (the recovery partition) 
**RFSFAT16_SYSTEM_000000000** (the system partition, ext4 sparse) 
**RFSFAT16_BOOTLOADER_00000** (the bootloader partition) 
For simplicity rename: 
[code] 
    cp android.img.dump/RFSFAT16_BOOT_00000000000 ../boot.img
    cp android.img.dump/RFSFAT16_RECOVERY_0000000 ../recovery.img
    cp android.img.dump/RFSFAT16_SYSTEM_000000000 ../system.img
    cp android.img.dump/RFSFAT16_BOOTLOADER_00000 ../bootloader.img
    cd ..
    
[/code]
#### Extract Kernel and Ramdisk
Extract the kernel and boot RAM disk as follows: 
[code] 
      $ ./tools/split_bootimg.pl boot.img
      Page size: 2048 (0x00000800)
      Kernel size: 4215036 (0x004050fc)
      Ramdisk size: 974998 (0x000ee096)
      Second size: 0 (0x00000000)
      Board name:
      Command line: console=ttyS0,115200 rw init=/init loglevel=5
      Writing boot.img-kernel ... complete.
      Writing boot.img-ramdisk.gz ... complete.
    
[/code]
Decompress the ramdisk data: 
[code] 
      $ mkdir boot
      $ cd boot 
      $ gunzip -c ../boot.img-ramdisk.gz | cpio -i
      $ tar -cpvf ../boot.tar *
      $ cd ..
    
[/code]
Convert **kernel** to **uImage** : 
[code] 
      $ mkimage -A arm -O linux -T kernel -C none -a 0x40008000 -e 0x40008000 -n "Linux 2.6" -d boot.img-kernel uImage
    
[/code]
#### Extract system image:
[code] 
      $ ./tools/simg2img system.img system1.img
      $ mkdir system
      $ mount -o loop system1.img system
      $ cd system
      $ tar -cpvf ../system.tar *
      $ cd ..
      $ umount system
    
[/code]
#### Extract recovery image:
[code] 
       $ ./tools/split_bootimg.pl recovery.img
      Page size: 2048 (0x00000800)
      Kernel size: 4215036 (0x004050fc)
      Ramdisk size: 974998 (0x000ee096)
      Second size: 0 (0x00000000)
      Board name:
      Command line: console=ttyS0,115200 rw init=/init loglevel=5
      Writing recovery.img-kernel ... complete.
      Writing recovery.img-ramdisk.gz ... complete.
    
[/code]
#### Decompress the ramdisk data:
[code] 
      $ mkdir recovery
      $ cd recovery
      $ gunzip -c ../recovery.img-ramdisk.gz | cpio -i
      $ tar -cpvf ../recovery.tar *
      $ cd ..
    
[/code]
### SD card Partition
Partitions description: 
WARNING: At the start we need a 17 MB unallocated partition, required for flash sunxi-spl and u-boot.bin without corrupting the SD. 
partition  | Size  | Name  | Fs  | Description   
---|---|---|---|---  
/dev/sdc1  | 16MiB  | bootloader  | VFAT  | Files to assist the bootloader.   
/dev/sdc2  | 36MiB  | boot  | EXT4  | ramdisk   
/dev/sdc3  | 500 MiB  | system  | EXT4  | Android's /system partition   
/dev/sdc4  | Fill all space  | extend  | Extend Partition   
/dev/sdc5  | 300MiB  | data  | EXT4  |   
/dev/sdc6  | 16 MiB  | misc  | EXT4  |   
/dev/sdc7  | 36 Mib  | recovery  | EXT4  | Android's recovery partition   
/dev/sdc8  | 125 MiB  | cache  | EXT4  |   
/dev/sdc9  | 16 MiB  | private  | EXT4  |   
/dev/sdc10  | 1-2 GiB  | UDISK  | VFAT  |   
  
Now, identify the device of the card and export it as `$card`: 
[code] 
    card=/dev/XXX (XXX should be replaced with the name of your device, eg. sdc or mmcblk0)
    
[/code]
Since /dev/mmcblk0 partitions are named like mmcblk0p1, let's define a prefix: 
[code] 
    cardp=/dev/sdX
    
[/code]
or: 
[code] 
    cardp=/dev/mmcblkXp
    
[/code]
[code] 
    dd if=/dev/zero of=$card bs=1M count=1
    blockdev --rereadpt $card
    
[/code]
When using sfdisk from an util-linux < 2.26: 
[code] 
    cat <<EOT | sfdisk --in-order -uM $card
    17,16,c
    ,36,83
    ,500,83
    ,,5
    ,300,83
    ,16,83
    ,36,83
    ,125,83
    ,16,83
    ,,83
    EOT
    
[/code]
Since util-linux 2.26 sfdisk has changed much, use: 
[code] 
    cat <<EOT | sfdisk $card
    start=17MiB,size=16MiB,type=c
    start=33MiB,size=36MiB,type=83
    start=69MiB,size=500MiB,type=83
    start=596MiB,type=5
    size=300MiB,type=83
    size=16MiB,type=83
    size=36MiB,type=83
    size=125MiB,type=83
    size=16MiB,type=83
    type=83
    EOT
    
[/code]
#### Format
[code] 
    mkfs.vfat -n bootloader ${cardp}1
    mkfs.ext4 -L boot       ${cardp}2
    mkfs.ext4 -L system     ${cardp}3
    mkfs.ext4 -L data       ${cardp}5
    mkfs.ext4 -L misc       ${cardp}6
    mkfs.ext4 -L recovery   ${cardp}7
    mkfs.ext4 -L cache      ${cardp}8
    mkfs.ext4 -L private    ${cardp}9
    mkfs.vfat -n UDISK      ${cardp}10
    
[/code]
remove huge_file option from EXT4 fs (android kernel not have this option!!!) 
[code] 
    tune2fs -O ^huge_file ${cardp}2
    tune2fs -O ^huge_file ${cardp}3
    tune2fs -O ^huge_file ${cardp}5
    tune2fs -O ^huge_file ${cardp}6
    tune2fs -O ^huge_file ${cardp}7
    tune2fs -O ^huge_file ${cardp}8
    tune2fs -O ^huge_file ${cardp}9
    
[/code]
### BootLoader
For SD card booting you can try one of these pair of files from [Hackberry][10429]: 
  * **1GB:** [sunxi-spl.bin][10430] [u-boot.bin][10431]
  * **512MB:** [sunxi-spl.bin][10432] [u-boot.bin][10433]

[code] 
    dd if=spl/sunxi-spl.bin of=$card bs=1024 seek=8
    dd if=u-boot.bin of=$card bs=1024 seek=32
    
[/code]
**Note:** The above will not work for the Cubieboard A10, you can try the images below or compile u-boot your self. 
**For Cubieboard A10:**
If you are in a pinch, you can try the files below, but it is recommended if you can that you compile them your self: 
  * [u-boot.img][10434]
  * [sunxi-spl.bin][10435]
  * [u-boot-sunxi-with-spl.bin][10436]

[code] 
    git clone <https://github.com/linux-sunxi/u-boot-sunxi.git>
    make cubieboard_config
    make
    
[/code]
**Note:** It is recommended for best results that you compile it if you can on the device you plan to use it on. 
For cross compilation: 
[code] 
    git clone <https://github.com/linux-sunxi/u-boot-sunxi.git>
    make cubieboard_config CROSS_COMPILE=arm-linux-gnueabihf-
    
[/code]
Next, install your new u-boot on your sdcard: 
[code] 
    dd if=u-boot-sunxi-with-spl.bin of=/dev/sdX bs=1024 seek=8
    
[/code]
or if you prefer to install the components separately: 
[code] 
    dd if=spl/sunxi-spl.bin of=/dev/sdX bs=1024 seek=8
    dd if=u-boot.img of=/dev/sdX bs=1024 seek=40
    
[/code]
If you have issues at boot time you will find that setting up debug serial console will help a lot to find your issue. 
**Reference:** <https://github.com/linux-sunxi/u-boot-sunxi/wiki>
### Copy to SD card
[code] 
    mkdir bootloader
    mount -o loop bootloader.img bootloader
    
[/code]
Copy files to bootloader partition: 
[code] 
    mount ${card}1 /mnt/
    cp uImage  /mnt
    cp bootloader/script.bin /mnt
    
    cat >/mnt/uEnv.txt << EOT
    fexfile=script.bin
    kernel=uImage
    extraargs=root=/dev/mmcblk0p2 loglevel=8 rootwait console=ttyS0,115200 rw init=/init mac_addr=00:AE:99:A3:E4:AF
    boot_mmc=fatload mmc 0 0x43000000 ${fexfile}; fatload mmc 0 0x48000000 ${kernel}; bootm 0x48000000
    EOT
    
[/code]
Recovery uEnv.txt 
[code] 
    cat >/mnt/uEnv_recovery.txt << EOT
    fexfile=script.bin
    kernel=uImage
    extraargs=root=/dev/mmcblk0p7 loglevel=8 rootwait console=ttyS0,115200 rw init=/init mac_addr=00:AE:99:A3:E4:AF
    boot_mmc=fatload mmc 0 0x43000000 ${fexfile}; fatload mmc 0 0x48000000 ${kernel}; bootm 0x48000000
    EOT
    
    umount /mnt
    umount bootloader
    
[/code]
Copy data to Ramdisk partition: 
[code] 
    mount ${card}2 /mnt
    tar -xpvf boot.tar -C /mnt
    
[/code]
**Note:** If you would like to add additional Wifi drivers, you can actually do that here. [This][10437] reference will help you get the idea of what needs to be done to include additional Wifi modules for android. 
This page also includes the kernel modules for r8712u and directions on how to compile and add your own Wifi modules. 
Modify the name partition in init.sun4i.rc 
[code] 
    sed -i "s/nandd/mmcblk0p3/g"  /mnt/init.sun4i.rc
    sed -i "s/nande/mmcblk0p5/g"  /mnt/init.sun4i.rc
    sed -i "s/nandh/mmcblk0p8/g"  /mnt/init.sun4i.rc
    sed -i "s/nandi/mmcblk0p10/g" /mnt/init.sun4i.rc
    umount /mnt
    
[/code]
Copy data to system partition: 
[code] 
    mount ${card}3 /mnt
    tar -xpvf system.tar -C /mnt
    umount /mnt
    
[/code]
Copy data to recovery partition: 
[code] 
    mount ${card}7 /mnt
    tar -xpvf recovery.tar -C /mnt
    sed -i "s/nandf/mmcblk0p6/g"  /mnt/ueventd.sun4i.rc
    umount /mnt
    sync
    
[/code]
Now you can boot Android from SD card. 
## Automated Flash Kitchen
Thierry Merle has assembled a Flash Kitchen originally for the Mele A2000 but it also works for other A10 devices. 
Download v2 from here: <http://tmerle.blogspot.fr/2012/09/mele-a2000-my-own-linux-flash-kitchen.html>
After having put the original.img file (PhoenixCard source image), run "make build_sdcard" as root and it should create everything needed to generate the SD card boot files in sdcard/. 
Then, you will have to 'cd sdcard/', then run 'make DEV=/dev/sdX' (where X is the device letter of your SD card). 
### Requirements
Wine - in order to extract/build the flash image (look below for enhancements). 
Root access for scripts other than img_1extract.sh/img_2build.sh. 
The script will create /system in your root directory. This is necessary if you make symbolic links in "system" filesystem. 
Of course, you need an original image (that you will rename as original.img) to start hacking. 
### Enhancements
  * If you don't have Wine you can use Ithamar's awutils [[1]][10438] in img_1extract.sh instead of unimg.exe. You can find more info in [Awutils][10428].

  * Here's abootimg statically linked and stripped for i386 and amd64: <https://www.dropbox.com/s/xbe2u7ai6aqaob1/abootimg_i386+amd64_statically_linked+stripped.tar.xz>

i386 is untested natively so to be sure also included are the static libraries libblkid.a and libuuid.a and you might need blkid.h 
Change the LDLIBS line in the Makefile as follows: 
[code] 
    LDLIBS=-static -lblkid -luuid -L.
    
[/code]
  * #!/bin/bash and function function_name() work better together in mkA10card.sh

  * "partition ends on cylinder 1023, beyond the end of the disk"

You have to make some adjustments to partitions.txt. It's for a 16 GB SD card and so it will show something like Capacity: 18446744 TB (-8,198,815,744 bytes). So you have to calculate partitions.txt yourself. 
### General information
  * When make fails and you want to run it again:

[code] 
    tar: .: Cannot change ownership to uid 1000, gid 1000: Operation not permitted"
    
[/code]
FAT does not allow UID, GID and symlinks. You have to copy the files manually. 
## Pre-built A10 SDcard images
As an assist here, I have created a few **8GB** SDcard images for Android on the Cubieboard A10 (**Use at your own risk, they are to be considered developmental images**): 
Images based on Android TV 1.0 NAND image: 
  * [For Cubieboard A10 w/ 512MB Ram - Image][10439]
  * [For Cubieboard A10 w/ 512MB Ram - MD5 for Image][10440]
  * [For Cubieboard A10 w/ 1024MB Ram - Image][10441]
  * [For Cubieboard A10 w/ 1024MB Ram - MD5 for Image][10442]

Image based on Android TV 2.2 (8192cu WiFi chipset) NAND image: 
  * [For Cubieboard A10 w/ 1024MB Ram - Image][10443]
  * [For Cubieboard A10 w/ 1024MB Ram - MD5 for Image][10444]

To install use `dd` in Linux or Win32DiskImager in Windows to write the image to your SDcard. 
Notes about the above images
    
  * The 512Mb image above is based on the A10-OLinuXino-LIME Android image located [here.][10445] but uses the system, boot and recovery from the linux-sunxi Android TV 1.0 image and uses the Olimex u-boot image and kernel.
  * If you want, the Olimex image will run on the Cubieboard A10, however, as Olimex never released an A10 board with 1GB ram, the image's u-boot only supports up to 512Mb of memory.
  * If you boot and use the 512mb image you will be limited to 512Mb ram in Android (Keep in mind that the GPU gets assigned memory as well so with this image you have roughly 306Mb of usable memory).
  * All other images have a custom compiled u-boot that was compiled using the directions below on a Cubieboard A10 running Debian Server.
  * These images do have some apps already installed and do not come in a factory reset state. I took the liberty to install Bubbleupnp, Mxplayer, Chrome, Firefox and a few other goodies that you may find useful.
  * If you do not care for the already installed apps, simply do a factory reset your self on first boot.
  * Since you will be booting from the SDcard, you will obviously not have an SDcard available to leverage for downloads. Some apps will give errors when trying to download files as there is no 'SDcard' present.
  * To help with not having an SDcard available, I have left you quite a large internal storage partition, so you shouldn't have issues with installing any needed apps.
  * Some wifi adapters may be compatible with these images, but I am not sure which are included in the Olimex kernel. The TV 2.2 images includes the chipsets noted.
  * Some SDcards are really slow! The slower your card the longer it will take to boot and the more laggy things will seem. I recommend a Class 10 card for best performance (Class 4 will work, but will be slow).
