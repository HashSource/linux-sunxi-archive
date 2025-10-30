# CWM on a SDCard
## Build SD card
These are the basic steps to get a SDCard-based ClockworkMod recovery. It can come in handy if your device is unrooted or your recovery and android system are both broken, and you don't want to use LiveSuite or similar. 
  1. Get an SDCard, and connect it to your PC.
  2. Make a new, clean partition table on the card
  3. Create a new ext2 partition, covering the full card and starting at 1M. You need this free space on the front for U-Boot
  4. Download and/or build [U-Boot][11426] with MMC support. You can get a confirmed working prebuilt image made by hno on <http://www.hno.se/code/A10/OLD/u-boot-mmc-hno-v2011.09-sun4i-20120808.img> (There are also newer U-Boots but untested.)
  5. Install U-Boot on the card. If you downloaded hno's image, do `dd seek=1 skip=1 if=u-boot-mmc-hno-v2011.09-sun4i-20120808.img of=/dev/DEVICE`

### Install
  1. Unpack the CWM image for your device, and copy the contents to the ext2 partition. You can do the unpacking with 'unpackbootimg'. Here is an example CWM unpack for [ZaTab][11427] <http://turl.linux-sunxi.org/zatab-recovery.tar.gz>
  2. Make a "boot" directory on your card. Copy your device's script.bin there, as well as a kernel uImage. You will also need a boot.scr, download the previously linked example for the boot.cmd used to generate it (as well as the boot.scr itself if you want to just copy it)
  3. [Copy any files][11428] you want to flash to the SDCard
  4. Insert card on your device and turn it on. CWM should appear.

### Install with [hwpack][11429]
Install [abootimg][11430] (for Debian).  
Fetch <https://github.com/linux-sunxi/sunxi-bsp/raw/master/scripts/sunxi-media-create.sh>  
Apply patch:  

[code] 
    --- sunxi-media-create.sh
    +++ sunxi-media-create.sh
    @@ -117,6 +117,12 @@
     	*.tar.xz)
     		sudo tar xJf "$f"
     		;;
    +	*.img)
    +		abootimg -x "$f"
    +		abootimg-unpack-initrd initrd.img
    +		mv ramdisk/* .
    +		rm initrd.img
    +		;;
     	*)
     		die "$f: unknown file extension"
     		;;
    
[/code]
Execute: 
[code] 
    sudo ./sunxi-media-create.sh /dev/sdx hwpack img
    
[/code]
If you get while "Extracting RootFS" the message "initrd.img does not exist." you have to extract /system ([nandc][11431]) to get boot.img.  
Either by booting into CWM and dd'ing the nandc. First check cat /proc/partitions for /system and adjust count= as necessary: 
[code] 
    dd if=/dev/block/nandc of=/sdcard/boot.img bs=1M count=32768
    
[/code]
Or by unpacking the image with Windows described on [Miniand wiki][11432].
