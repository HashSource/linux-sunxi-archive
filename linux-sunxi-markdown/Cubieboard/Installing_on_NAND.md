# Cubieboard/Installing on NAND
< [Cubieboard][14184]
 
## Contents
  * [1 Automatically, with Install-Cubian][14187]
  * [2 Manually][14188]
    * [2.1 Copy the SD-card image to a card][14189]
    * [2.2 Boot your Cubieboard from the card][14190]
    * [2.3 Write the boot partition and partition table to NAND][14191]
    * [2.4 Create the OS partition on NAND][14192]
    * [2.5 Copy the kernel to NAND][14193]
    * [2.6 Copy the filesystem][14194]
    * [2.7 Finish setting-up your OS][14195]

## Automatically, with Install-Cubian
Update, cubieplayer has made a Linux image for cubieboard1 called [Cubian][14196]. which supports automatic [NAND][14197] installation for [Cubieboard1][14184] and [Cubieboard2][14198]. Quote from [Cubian Wiki][14199]
[code] 
    Install Cubian to NAND is pretty simple.
    First, you need to install it to Micro-SD card by the tutorial above, then boot and login to your Cubieboard. 
    Once you logged in, execute the following command
    sudo ~/nandinstall/install.sh
    
[/code]
If you want to port Linux on your SD-card to NAND manually, please continue to read the tutorial below 
## Manually
First, download and uncompress a couple of files: 
  * [Debian Wheezy SD-card image][14200] (Thanks Guillaume).
  * [NAND boot partition and MBR image][14201] ([Thanks Lawrence][14202])
  * CONFIG_SUNXI_NAND=y is needed in kernel configuration

### Copy the SD-card image to a card
The first step to installation is to copy the SD-card image to an SD card (make sure it's large enough!) 
I'm using a Mac. If you are too, you can do this by: 
  * Typing `mount`. The mounted partition on the card will be listed in there somewhere, with a name like `/dev/diskXs1` (where `X` is a number).
  * Unmount it by typing `umount /dev/diskXs1` (replace the `X` with the number from the previous steps). If there is more than one partition on the card (`/dev/diskXs2`, `/dev/diskXs3` etc.) unmount them all.
  * Now, you need to copy the Debian SD card image onto the SD card, with a command like `sudo dd bs=4096 if=~/Downloads/debian_wheezy_armhf_v1_mele.img of=/dev/diskX` \- again, the `X` should be the same number as in the previous steps. Note that there's no trailing `sY` this time, because we're copying the image over the whole disk, and the numerical 'sY' suffixes refer to partitions.
  * After the `dd` command is complete, the system will probably auto-mount the new boot partition on the SD card (this is just a small MS-DOS formatted partition that's used for booting). Eject it, and remove the SD card.
  * Now you have Debian on the SD card!

On Linux, the steps will be quite similar. On Windows they will not, but the goal is the same. 
### Boot your Cubieboard from the card
Next you can boot your Cubieboard with the system on the SD card. Plug it in to your Ethernet network, plug in the SD card, and plug in the power. The power light will come on immediately, followed shortly (maybe 15-20 seconds later) by LED 2. In about 30 seconds, booting will be complete, and the Cubieboard will have obtained an IP from your DHCP server or router. You'll need to find out what this IP is from your router. 
After you have the Cubieboard's IP, you can ssh to it. On a UNIX system like a Mac or Linux, that's just a simple `ssh root@<CUBIEBOARD IP ADDRESS>` in a terminal. The password is also `root`. You should be logged in and get a command prompt. 
### Write the boot partition and partition table to NAND
Now finally we got to the point where we can start modifying contents of the internal NAND. 
First, we need to get the boot partition we downloaded earlier on onto the NAND. You can either copy it over using SCP, then use `dd` to write it to `/dev/nand` (`dd bs=4096 if=./cubie_nand_uboot_partition_image.bin of=/dev/nand`), or just copy it directly there with SCP (on my Mac, `scp ~/Downloads/cubie_nand_uboot_partition_image.bin root@<CUBIEBOARD IP ADDRESS>:/dev/nand`). 
After that **wait for 30 seconds (this seems like it should not be necessary, but guides I read recommended it, and I'm paranoidly cargo-culting the advice)** , then a 'reboot' is in order. 
### Create the OS partition on NAND
**Warning ! Depending on system image used, nand partition devices have not the same name**. It could be `/dev/nanda` and `/dev/nandb`, or `/dev/nand1` and `/dev/nand2`. To know what names are used, type `ls /dev/nand*`. We assume here that it's _nanda_ for first partition and _nandb_ for second one. 
After the board reboots, SSH in to it again. Now, we'll create our Linux partition. The image we copied to the NAND already has the partition table and the boot partition on it, so all we need to do is format the partition we'll use by doing `mkfs.ext4 /dev/nandb`. After that, we can mount it with `mount /dev/nandb /mnt`. 
### Copy the kernel to NAND
Next, we'll copy the Linux kernel off the SD card. It's on the SD card's boot partition. 
**Warning:** On the example given image, the boot and the root partition are not the same, but on some images (as [Arch Linux ARM for CB2][14203] for example), there is only one ext4 partition for the root and the boot, in this case, mounting two times the filesystem could damage it. You can know how much partition are created on your SD card by typing `ls /dev/mmcblk0*`. `mmcblk0` is the whole card device file, `mmcblk0p1` the first partition, and `mmcblk0p2` the second partition. 
So to simplify the following tuto, you can in the case of only one partition (only mmcblk0p1) the files are in `/boot/` instead of `/tmp/boot/` mounted partition. 
If your image as the one given in the example has two partition, your root partion (mounted as /) is not the one containing the root filesystem, so we'll mount it by creating a directory to mount it into (`mkdir /tmp/boot`), and then mounting it (`mount /dev/mmcblk0p1 /tmp/boot`). After that, we copy the kernel image out of it into a boot directory on our new partition (`mkdir /mnt/boot` then `cp -a /tmp/boot/uImage /mnt/boot/uImage`). 
If you want to use [Hwpack][14204] features, you should copy `uImage` and `script.bin` files from Hwpack `kernel` directory instead of `/tmp/boot/uImage`. 
### Copy the filesystem
All that remains now is to copy over the Linux filesystem. I used `rsync` for that (thanks patwood: [http://www.cubieforums.com/index.php/topic,73.msg241.html#msg241][14205]). 
First, I created a file to contain all the directories I _didn't_ want the contents of. The contents of that file were: 
[code] 
    /dev/*
    /proc/*
    /sys/*
    /media/*
    /mnt/*
    /run/*
    /tmp/*
    
[/code]
Then a simple `rsync -avc --exclude-from=EXCLUDE_FILE / /mnt` copied the files. 
For using Cubieboard-specific modules from Hwpack, copy the Hwpack `rootfs` directory contents to `/mnt`. 
That's it! Do a `shutdown -h now`, and when the lights go out, remove the SD card. Now, power the Cubieboard back up, and you'll have Debian running entirely from the NAND. 
### Finish setting-up your OS
Now, it's time to properly set things up. An `apt-get update` then an `apt-get dist-upgrade` is a pretty good first step to get things up to date. You'll probably want to then create a user account and change the root password. My next steps were to edit `/etc/hostname` to give my board a good name, then `apt-get install man` and `apt-get install g++`. Most of the software you'll need can be installed with `apt-get` \- but I won't go into more detail, that's all just generic Debian and Linux stuff, not specific to the Cubieboard.
