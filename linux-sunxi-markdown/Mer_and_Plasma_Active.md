# Mer and Plasma Active
This tutorial helps on creating an image based on Mer and Plasma Active, the reference hardware for this tutorial is an [Eoma68][37609] plugged into an [Improv][37610], but should be easy to adapt it to other Allwinner based devices. 
## Contents
  * [1 Install the SDK][37611]
  * [2 Create an image from the Kickstart][37612]
  * [3 Install the OS on the nand][37613]
  * [4 Ready to use images][37614]

# Install the SDK
To create an image, you need a working MER SDK, you can find instructions on how to do so on the [Mer wiki][37615]. 
# Create an image from the Kickstart
Kickstarts for Mer and Plasma Active are maintained on this [Git project][37616]. to clone it ype: 
[code] 
       git clone <git://anongit.kde.org/plasma-active-kickstart>
    
[/code]
Now, enter in the MER sdk, and from within it move into the git repo. The kickstarter are created from a bunch of modular YAML files, so to obtain the final kickstart file type from the plasma-active-kickstart folder: 
[code] 
       mer-kickstarter -e . -c releases/plasma-active-4.yaml -o plasma-active-latest-ks/
    
[/code]
plasma-active-4.yaml takes the RPMS from repos of a stable release, the other yaml files in the releases folder takes the packages from varying degrees of experimental stages. 
Once mer-kickstarter ran, it will generate kickstart files in the plasma-active-latest-ks/ folder, for every hardware adaptation available, the one we need is plasma-active-armv7hl-sunxi-eoma68-improv.ks 
Let's move in the plasma-active-latest-ks and launch mic to create the image: 
[code] 
      cd plasma-active-latest-ks/
      sudo mic create raw plasma-active-armv7hl-sunxi-eoma68-improv.ks -o . --pkgmgr=yum --arch=armv7hl --logfile=plasma-active-build.log
    
[/code]
The file plasma-active-armv7hl-sunxi-eoma68-improv-mmcblk0p.raw is the image we need, we can put it on a microsd: 
[code] 
      sudo dd if=plasma-active-armv7hl-sunxi-eoma68-improv-mmcblk0p.raw of=/dev/sdb
    
[/code]
That microsd will already be capable of booting via FEL on USB. If instead you configured your on board u-boot to boot from microSD, you have to put U-boot on the first 1024KB of the card. 
Since the MER kickstarter is not able to create an image with the first 1024KB empty, you'll have to resize the partition with Parted or Gparted (pay attention that GParted can only wotk with MiB, so you need to make at least 2Mib of empty space at the beginning of the SD) Then, you may put spl and uboot at the beginning of the card: 
[code] 
      dd if=spl/sunxi-spl.bin of=$card bs=1024 seek=8
      dd if=u-boot.img of=$card bs=1024 seek=40
    
[/code]
To do that, you need u-boot-sunxi cross compiled from your pc (see <http://rhombus-tech.net/allwinner/a20/boot/>) At this point you SD card will be able to boot MER. 
# Install the OS on the nand
After you have a system that works correctly from the microSD, you can install it on the nand, with the following steps: 
  * partition the nand following [this tutorial][37617]
  * alternatively, you can dd on the nand [this][37618] previously partitioned empty image, with

[code] 
      dd if=/mnt/sda1/eoma68-A20-nand-bare-latest.raw of=/dev/nand
    
[/code]
(provided /mnt/sda1 is an USB stick mounted from the Eoma device.) 
  * copy the root filesystem on the nand:

[code] 
      mkdir /mnt/nandb
      mount -t auto /dev/nandb /mnt/nandb
      rsync -a -h --progress /bin /etc /home /lib /media /opt /root /run /sbin /srv /tmp /usr /var /mnt/nandb
    
[/code]
  * correct /mnt/nandb/etc/fstab for / to use /dev/nandb and /boot to use /dev/nanda

# Ready to use images
Alternatively, you can find some ready to use images [here][37619], most notably: 
  * [eoma68-A20-nand-bare-latest.raw.bz2][37620]: an empty image: use this if you want a partitioned nand on which you want to put a root filesystem of a distribution of your choice.
  * [mer-essentials-armv7hl-sunxi-eoma68-improv-mmcblk0p-latest.raw.bz2][37621]: a Mer image with a quite minimal installation, ready to be written on a miniSD card.
  * [plasma-active-armv7hl-sunxi-eoma68-improv-mmcblk0p-latest.raw.bz2][37622]: an image of Mer with Plasma Active and Plasma Desktop installed and ready to go, ready to be written on a miniSD card.
  * [mer-essentials-armv7hl-sunxi-eoma68-improv-nand-latest.raw.bz2][37623]: an installed Mer image with a quite minimal installation, ready to be written on the internal NAND
  * [plasma-active-armv7hl-sunxi-eoma68-improv-nand-latest.raw.bz2][37624]: an image of Mer with Plasma Active and Plasma Desktop installed and ready to go, ready to be written on the internal NAND.

To write an image on the nand, boot from an SD card, in which you previously put the image file of the nand, or alternatively put it on an USB stick and then with an USB hub mount it within the system running on the Eoma68, then you can dd it on the nand. 
Warning: this will destroy all the data you previously had in the internal storage of your system, it is advised to backup /dev/nand with dd beforehand
Backup: 
[code] 
      dd if=/dev/nand of=/mnt/sda1/nand-backup.raw
    
[/code]
Write the new image: 
[code] 
      dd if=/mnt/sda1/plasma-active-armv7hl-sunxi-eoma68-improv-nand-latest.raw of=/dev/nand
    
[/code]
