# Mainline Debian HowTo
This page describes bootstrapping Debian jessie with it's default (mainline) linux kernel (3.16) to create a SD-card with a clean (official) install. Based on the [instructions on the official debian wiki][33794]
To summarize the process: Most work is the normal debian bootstrapping procedure. To make the SD-card bootable, we use a precompiled version of U-Boot provided by the Debian installer team. Tested on [Cubieboard 1][33795] and [Cubietruck][33796], should work on other boards, too. 
## Contents
  * [1 Caveats][33797]
  * [2 Using a ready-made installation SD card image instead of bootstrapping][33798]
  * [3 Getting a cross toolchain][33799]
  * [4 Creating a bootable SD Card with U-Boot][33800]
    * [4.1 Building U-Boot yourself][33801]
    * [4.2 Downloading precompiled U-Boot images][33802]
    * [4.3 Setting up the SD-card][33803]
  * [5 Bootstrapping Debian][33804]
  * [6 Configuring the system][33805]
    * [6.1 flash-kernel][33806]
    * [6.2 Kernel modules][33807]
    * [6.3 Base configuration files][33808]
    * [6.4 Prepare Login][33809]
    * [6.5 chroot and setup][33810]
  * [7 Cleanup][33811]
  * [8 Boot][33812]
    * [8.1 Manual boot (serial console)][33813]
      * [8.1.1 systemd][33814]
  * [9 Conclusion][33815]
  * [10 See also][33816]
  * [11 External Links][33817]

## Caveats
  * The kernel comes without display drivers, so **you won't get any display-output with this guide**! Use [UART][33818] or ssh to login.
  * The current Debian jessie kernels (3.16.7-ckt11-1 at the time of writing) do not support NAND yet, so only SATA and MMC/SD-card storage is supported.
  * We will use a recent version of U-Boot and device tree. The Allwinner-specific [script.bin][33819] isn't needed anymore.

## Using a ready-made installation SD card image instead of bootstrapping
If you are being lazy, then it is possible to download a bootable SD card image for [A10][33820]/[A10s][33821]/[A20][33822] based devices with the debian installer and write it to an SD card: 
[code] 
      wget <https://github.com/ssvb/sunxi-bootsetup/releases/download/20141215-sunxi-bootsetup-prototype/20141215-sunxi-bootsetup-prototype-v6.img.xz>
      xzcat 20141215-sunxi-bootsetup-prototype-v6.img.xz > ${card}
      sync
    
[/code]
Then boot from this SD card and use a menu based installer, which is accessible on the UART serial console. Ignore warnings about the missing kernel modules. When asked about partitioning the SD card, any choice should be fine. But erasing the existing partition is probably the most clean and preferable solution (the installer itself is running from RAM and does not depend on any data from the SD card during the installation). At the end of the process, you should get a clean (official) installation of Debian, installed from the network. The mainline non-modified release of U-Boot v2015.01 is used as a bootloader. 
Every part of this SD card image can be reconstructed from sources. The instructions are available at <https://github.com/ssvb/sunxi-bootsetup/releases/tag/20141215-sunxi-bootsetup-prototype>
And the '**official' debian installer initrd file** is taken right from the debian website. This bootable SD card image just provides a bit more convenient deployment method instead of the TFTP or USB stick tricks from the <https://wiki.debian.org/InstallingDebianOn/Allwinner> wiki page. Refreshing the initrd file to a more up to date build is possible in the following way: 
[code] 
       wget <http://d-i.debian.org/daily-images/armhf/daily/netboot/initrd.gz>
       gzip -d initrd.gz
       lzma initrd
       mkimage -A arm -O linux -T ramdisk -C lzma -a 0x43300000 -n "Debian Installer" -d initrd.lzma initrd-debian-netboot.lzma.uboot
    
[/code]
And then replace the 'initrd-debian-netboot.lzma.uboot' file on the SD card with the newly generated one. 
Supported devices: [Cubieboard][33823], [Cubieboard2][33824], [Cubietruck][33825], [A10-OLinuXino-LIME][33826], [Mele A2000][33827] and many others (which are yet to be tested). 
# Getting a cross toolchain
Refer to [Toolchain][33828]. This is not needed if you do not intent to build U-Boot by yourself. 
# Creating a bootable SD Card with U-Boot
There are two options: Build U-Boot yourself or use the images provided by the Debian installer team. 
## Building U-Boot yourself
Mainline U-Boot works fine: 
[code] 
     git clone -b v2015.01 <http://git.denx.de/u-boot.git>
     cd u-boot
     make Cubietruck_config
     make -j$(nproc) CROSS_COMPILE=arm-linux-gnueabihf-
    
[/code]
(Also refer to [U-Boot#Compile U-Boot][33829]) 
## Downloading precompiled U-Boot images
Download the U-Boot image _u-boot-sunxi-with-spl.bin.gz_ for your hardware from <http://d-i.debian.org/daily-images/armhf/daily/u-boot/>, i.e. for _Cubieboard 1_
[code] 
     wget <http://d-i.debian.org/daily-images/armhf/daily/u-boot/Cubieboard/u-boot-sunxi-with-spl.bin.gz>
    
[/code]
or for _Cubietruck_
[code] 
     wget <http://d-i.debian.org/daily-images/armhf/daily/u-boot/Cubietruck/u-boot-sunxi-with-spl.bin.gz>
    
[/code]
then unzip: 
[code] 
     gunzip u-boot-sunxi-with-spl.bin.gz
    
[/code]
## Setting up the SD-card
${card} is the SD device (ie _/dev/sdc_). ${partition} is the partition number (ie. _1_). [![Exclamation.png][33830]][33831] _Warning:_ This will delete the content. 
[code] 
     dd if=/dev/zero of=${card} bs=1M count=1
     dd if=u-boot-sunxi-with-spl.bin of=${card} bs=1024 seek=8
    
[/code]
Create partition(s). ie one big partition beginning with sector 2048, type 83 (Linux) 
[code] 
     fdisk ${card}
    
[/code]
[code] 
     mkfs.ext4 ${card}${partition}
     mount ${card}${partition} /mnt
    
[/code]
This will first clean the card (at least the first 1M), install the U-Boot bootloader you compiled/downloaded in the step before, and then you can create -for example- one partition, format it, and mount it to _/mnt/_ for use in the next steps. 
(Also refer to [Bootable_SD_card][33832]) 
# Bootstrapping Debian
This will bootstrap Debian stable (aka _Jessie_) 
[code] 
     qemu-debootstrap --verbose --include=${kernel},locales,flash-kernel,sunxi-tools,firmware-linux,debconf --arch=armhf --components main,contrib,non-free jessie /mnt <http://ftp.debian.org/debian>
    
[/code]
with ${kernel} being either _linux-image-armmp_ for Cubieboard 1 or _linux-image-armmp-lpae_ for Cubietruck. For Cubieboard 2, _linux-image-armmp-lpae_ should be the correct kernel. You need to have the packages [qemu-user-static][33833] and [debootstrap][33834] installed. 
If in doubt, have a look at the [Debian wiki][33835] or the official documentation. 
# Configuring the system
## flash-kernel
We are going to use flash-kernel to generate the _boot.src_. Tell it which hardware we're aiming for. (Devices listed in: _/usr/share/flash-kernel/db/all.db_) 
[code] 
     mkdir /mnt/etc/flash-kernel/
     echo "Cubietech Cubietruck" >> /mnt/etc/flash-kernel/machine
    
[/code]
or for Cubieboard 1 use 
[code] 
     echo "Cubietech Cubieboard" >> /mnt/etc/flash-kernel/machine
    
[/code]
Kernel arguments: 
[code] 
    echo 'LINUX_KERNEL_CMDLINE="console=ttyS0,115200 hdmi.audio=EDID:0 disp.screen0_output_mode=EDID:1280x1024p60 root=/dev/mmcblk0p1 rootwait panic=10 ${extra}"' >> /mnt/etc/default/flash-kernel
    
[/code]
## Kernel modules
Write extra modules that should be loaded at boot time to _/mnt/etc/modules_. 
[code] 
     echo "rtc_sunxi" >> /mnt/etc/initramfs-tools/modules
    
[/code]
This module does not exist for the linux-image-armmp kernels, so it is not available for Cubieboard 1. 
## Base configuration files
[code] 
     echo "/dev/mmcblk0p1  /           ext4    relatime,errors=remount-ro        0       1" > /mnt/etc/fstab
     echo "HOSTNAME" > /mnt/etc/hostname
    
[/code]
Add your hostname to the 127.0.0.1 and ::1 lines in /mnt/etc/hosts, e.g. 
[code] 
     nano /mnt/etc/hosts
    
[/code]
Hint: Please consider using your favorite debian-mirror instead of _ftp.debian.org_. 
[code] 
    cat <<EOF > /mnt/etc/apt/sources.list
    # 
    
    deb http://ftp.debian.org/debian/ jessie main non-free contrib
    deb-src http://ftp.debian.org/debian/ jessie main non-free contrib
    
    deb http://security.debian.org/ jessie/updates main contrib non-free
    deb-src http://security.debian.org/ jessie/updates main contrib non-free
    
    # jessie-updates, previously known as 'volatile'
    deb http://ftp.debian.org/debian/ jessie-updates main contrib non-free
    deb-src http://ftp.debian.org/debian/ jessie-updates main contrib non-free
    EOF
[/code]
[code] 
    cat <<EOF > /mnt/etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).
    
    # The loopback network interface
    auto lo
    iface lo inet loopback
    
    # The primary network interface
    allow-hotplug eth0
    iface eth0 inet dhcp
    EOF
[/code]
## Prepare Login
Remember: We won't have any display output, so we can eiter: spawn a login on the serial console: 
[code] 
     echo "T0:23:respawn:/sbin/getty -L ttyS0 115200 vt100" >> /mnt/etc/inittab
    
[/code]
and/or use ssh. Since debian disabled root password-login in jessie, re-enable it: 
[code] 
     sed -i "s/^PermitRootLogin without-password/PermitRootLogin yes/" /mnt/etc/ssh/sshd_config
    
[/code]
or copy your key: 
[code] 
     umask 077; mkdir /mnt/root/.ssh/ cat ~/.ssh/id_rsa.pub >> /mnt/root/.ssh/authorized_keys
    
[/code]
## chroot and setup
Now _chroot_ in to the new system and set everything up. 
[code] 
     mount -t proc chproc /mnt/proc
     mount chsys /mnt/sys -t sysfs
     mount -t devtmpfs chdev /mnt/dev || mount --bind /dev /mnt/dev
     mount -t devpts chpts /mnt/dev/pts
     echo -e '#!/bin/sh\nexit 101' > /mnt/usr/sbin/policy-rc.d
     chmod 755 /mnt/usr/sbin/policy-rc.d
     DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true LC_ALL=C LANGUAGE=C LANG=C chroot /mnt dpkg --configure -a
    
[/code]
[code] 
     LC_ALL=C LANGUAGE=C LANG=C chroot /mnt
    
[/code]
The next steps are executed inside the chroot: 
[code] 
       dpkg-reconfigure locales
       dpkg-reconfigure tzdata
    
[/code]
Optional: Install U-Boot (U-Boot from debian is not used, but it does no harm and i'll include it for future reference) 
[code] 
       apt-get install u-boot u-boot-tools
    
[/code]
Or, if you want simple frame-buffer support (on some cards) go with kernel >3.19. For this, you need to add experimental sources for apt: 
[code] 
       apt-get -t experimental install linux-image-3.19.0-trunk-armmp-lpae u-boot u-boot-tools
    
[/code]
Install non-free firmware and add one currently missing file to the wifi-firmware (not for Cubieboard 1): 
[code] 
       apt-get install firmware-brcm80211
       wget -O /lib/firmware/brcm/brcmfmac43362-sdio.txt <http://dl.cubieboard.org/public/Cubieboard/benn/firmware/ap6210/nvram_ap6210.txt>
    
[/code]
Install a few other things: 
[code] 
       apt-get install console-setup keyboard-configuration openssh-server ntp
    
[/code]
At this point, debian should have generated a kernel image _/boot/vmlinuz-???_ and an initrd _/boot/initrd.img-???_ for you. Generate the _/boot/boot.scr_ , set a password and after a little cleanup you're set: 
[code] 
       flash-kernel
       passwd root
       exit
    
[/code]
# Cleanup
[code] 
     rm /mnt/usr/sbin/policy-rc.d
     rm /mnt/usr/bin/qemu-arm-static
     umount /mnt/dev/pts && umount /mnt/dev && umount /mnt/sys && umount /mnt/proc && umount /mnt
     sync
    
[/code]
# Boot
Now you should be able to boot your brand new debian installation. Hopefully it'll boot, pull up networking and you're able to login via ssh. 
## Manual boot (serial console)
If it doesn't boot, you'll want an 3,3V USB [UART][33818] module to debug. U-Boot seems to be powerful and gives helpful error messages. If it says something like `'CRC error' 'loading default environment'`, that's okay, we want default. (Side note: use the filesize variable or give the size in hexadecimal) 
[code] 
     setenv bootargs console=ttyS0,115200n8 hdmi.audio=EDID:0 disp.screen0_output_mode=EDID:1280x1024p60 root=/dev/mmcblk0p1 rootwait panic=10 ${extra}
     ext4load mmc 0:1 0x47000000 boot/dtb-3.16.0-4-armmp-lpae
     ext4load mmc 0:1 0x46000000 boot/vmlinuz-3.16.0-4-armmp-lpae
     ext4load mmc 0:1 0x48000000 boot/initrd.img-3.16.0-4-armmp-lpae
     bootz 0x46000000 0x48000000:${filesize} 0x47000000
    
[/code]
### systemd
Newer debian uses systemd by default. Beside activing ttyS0 there using 
[code] 
    systemctl enable [[email protected]][33836]
    
[/code]
make sure your kernel has 
[code] 
    CONFIG_FHANDLE=y
    
[/code]
Also note that semantic of 'halt' is not yet reestablished. Use 'poweroff' instead, meanwhile. 
# Conclusion
As of now it is possible to run Debian with a recent mainline kernel and only few changes to the system. We can throw away some of the crude, device-specific things like the modifications to the kernel, 'script.bin'... U-Boot is on the right track and Debian-installer will be usable on various sunxi-based systems, once a recent kernel arrives in the installer builds. 
What's left to be done is: 
  * Optimizing the system
  * Getting some/any graphics support

# See also
  * [Mainline Kernel Howto][33837]
  * [Bootable SD card][33838]

# External Links
  * <https://wiki.debian.org/InstallingDebianOn/Allwinner>
  * <https://github.com/igorpecovnik/Cubietruck-Debian/blob/master/build.sh>
