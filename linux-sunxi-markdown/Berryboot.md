# Berryboot
## Contents
  * [1 Adding your own Linux distributions to Berryboot][9914]
    * [1.1 Converting a rootfs tarball][9915]
    * [1.2 Converting a disk image][9916]
    * [1.3 Caveats when converting images][9917]
    * [1.4 Adding the image to Berryboot][9918]
  * [2 See also][9919]

# Adding your own Linux distributions to Berryboot
**(for advanced users)**
Instead of choosing a Linux distribution from the list, it is also possible to add your own Linux distribution. Berryboot accepts image files in SquashFS format. 
## Converting a rootfs tarball
To convert a rootfs, such as [ubuntu-alip][9920], execute on a normal Linux desktop computer as root: 
[code] 
    mkdir temp
    tar -C temp/ -xjf my-rootfs.tar.bz2
    mksquashfs temp my_image_for_berryboot.img -comp lzo
    
[/code]
## Converting a disk image
Some operating system images are distributed as disk images containing two partitions. A FAT partition with the boot loader and kernel files, and a second ext4 partition with everything else. We are interested in the second partition. 
With a regular Linux desktop computer that has kpartx and mksquashfs installed, you can convert the second partition to SquashFS like this: 
[code] 
    $ sudo kpartx -av image_you_want_to_convert.img 
    add map loop0p1 (252:5): 0 117187 linear /dev/loop0 1
    add map loop0p2 (252:6): 0 3493888 linear /dev/loop0 118784
    $ sudo mount /dev/mapper/loop0p2 /mnt
    $ sudo mksquashfs /mnt my_image_for_berryboot.img -comp lzo -e lib/modules
    $ sudo umount /mnt
    $ sudo kpartx -d image_you_want_to_convert.img 
    
[/code]
We are excluding /lib/modules from the image, because the kernel modules shipped with Berryboot are used instead, and shared with all distributions. 
## Caveats when converting images
Notes: 
  * Berryboot is incompatible with images that use /lib -> /usr/lib symlink constructs such as Fedora 18. To work around this, move /usr/lib to /lib, and make a symlink /usr/lib -> /lib instead. Same with /sbin
  * It is not necessary to add entries to /etc/fstab. Berryboot takes care of mounting the root filesystem.

## Adding the image to Berryboot
  * You can copy my_image_for_berryboot.img to the /images folder on the Berryboot microSD card.
  * Or you put the image file on USB stick, go to the Berryboot menu editor, hold down your mouse button over "add OS" and select "from USB stick" there.

# See also
<http://www.berryterminal.com/doku.php/berryboot_a10>
