# Build Instructions for Ubuntu
## Contents
  * [1 Build Instructions for Ubuntu][10900]
  * [2 Build Pre-requisites][10901]
  * [3 Getting the Cross-Toolchain][10902]
  * [4 Building u-boot][10903]
  * [5 Setting up the sd card][10904]
  * [6 Ubuntu Core][10905]
  * [7 Ubuntu Core for Offline instalation][10906]
  * [8 Configuring the system][10907]
    * [8.1 flash-kernel][10908]
    * [8.2 Kernel modules][10909]
    * [8.3 Base configuration files][10910]
    * [8.4 Prepare Login][10911]
    * [8.5 chroot and setup][10912]

# Build Instructions for Ubuntu
**Reference: Ubuntu 15.04 Vivid Vervet**
# Build Pre-requisites
[code] 
    sudo apt-get install build-essential git
    
[/code]
Useful for building or troubleshooting older builds: 
[code] 
    sudo apt-get install u-boot-tools sunxi-tools
    
[/code]
# Getting the Cross-Toolchain
See also: [Toolchain][10913]
  * Add the ArmHF architecture

[code] 
    sudo dpkg --add-architecture armhf
    
[/code]
  * Modify existing sources, restricting to appropriate architectures (i.e. all i386 and amd64 package sources are prefixed as "deb [arch=i386,amd64]")

[code] 
    sudo sed 's~\(\(deb\(-src\)*\) \([^\[]\)\)~\2 [arch=i386,amd64] \4~' /etc/apt/sources.list | sudo tee /etc/apt/sources.list
    #Manually configure third party sources
    sudo sed 's~\(\(deb\(-src\)*\) \([^\[]\)\)~\2 [arch=i386,amd64] \4~' /etc/apt/sources.list.d/*.list
    
[/code]
  * Create source list for the port architecture(s) (this adds the armhf port sources to apt)

[code] 
    sudo bash -c 'cat > /etc/apt/sources.list.d/armhf-ports.list <<EOT
    deb [arch=armhf] http://ports.ubuntu.com/ `lsb_release -cs` main universe multiverse restricted
    deb [arch=armhf] http://ports.ubuntu.com/ `lsb_release -cs`-updates main universe multiverse restricted
    deb [arch=armhf] http://ports.ubuntu.com/ `lsb_release -cs`-security main universe multiverse restricted
    EOT'
    
[/code]
  * Update apt and install crossbuild tools for armhf

[code] 
    sudo apt-get update
    sudo apt-get install crossbuild-essential-armhf
    
[/code]
# Building u-boot
Mainline u-boot works fine: 
[code] 
     git clone -b v2015.04 <git://git.denx.de/u-boot.git>
     cd u-boot
     make CROSS_COMPILE=arm-linux-gnueabihf- Mele_A1000_defconfig
     make -j4 CROSS_COMPILE=arm-linux-gnueabihf-
    
[/code]
_search in the directory configs/ for your board, the file name looks like <board_name>_defconfig_
(Also refer to [Mainline_U-boot#Compile U-Boot][10914]) 
# Setting up the sd card
Enter an interactive superuser sudo shell 
[code] 
     sudo su -
    
[/code]
${card} is the SD device (ie _/dev/sdc_). ${partition} is the partition number (ie. _1_). Warning: This will delete the content. 
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
This will first clean the card (at least the first 1M), install the u-boot bootloader you compiled in the step before, and then you can create -for example- one partition, format it, and mount it to _/mnt/_ for use in the next steps. 
(Also refer to [Bootable_SD_card][10915]) 
# Ubuntu Core
<https://wiki.ubuntu.com/Core>
  * Download Ubuntu Core filesystem   

Link to Ubuntu Core download:   
Ubuntu 15.04 (Vivid Vervet) - <http://cdimage.ubuntu.com/ubuntu-core/releases/vivid/release/>
  * Extract Ubuntu Core filesystem to the mounted SD card

[code] 
    cd /mnt
    sudo tar zxvf $path_to_root_fs
    
[/code]
  * Install qemu-arm-static

[code] 
     sudo apt-get install qemu-user-static
    
[/code]
  * Prepare chroot environment

[code] 
     cp /usr/bin/qemu-arm-static /mnt/usr/bin/
     mount chproc /mnt/proc -t proc
     mount chsys /mnt/sys -t sysfs
    
[/code]
[code] 
     cp /etc/resolv.conf /mnt/etc/resolv.conf
    
[/code]
will allow network access after chroot-ing (in step 7) by copying the DNS resolver configuration 
  * Open a chroot session into the target root filesystem. This will allow you to install packages and configure the target system before it is bootable.

[code] 
     sudo LC_ALL=C LANGUAGE=C LANG=C chroot /mnt
    
[/code]
[code] 
     for f in /sys /proc /dev ; do mount --rbind $f /mnt/$f ; done ; chroot /mnt\
    
[/code]
will go to a chroot, see [Is there an easier way to chroot than bind-mounting?][10916] for details about mount rbind 
[code] 
     apt-get update && apt-get install linux-{headers,image}-generic
    
[/code]
will install kernel ("linux") 
Note: it's possible that apt-get update will not work because no network is present. 
# Ubuntu Core for Offline instalation
  * Download the Linux Kernel

[code] 
    apt-get download linux-generic:armhf flash-kernel:armhf linux-base linux-image-generic:armhf linux-headers-generic:armhf devio:armhf
    
[/code]
  * Install flash-kernel

[code] 
    dpkg -i devio_1.2-1build2_armhf.deb
    
[/code]
  * Install the kernel:

[code] 
     # dpkg -i /tmp/$dependencies
     # dpkg -i /tmp/$kernel
    
[/code]
  * Copy the kernel and any dependencies to the target root filesystem, e.g.

[code] 
    cp $path_to_kernel/*deb /mnt/tmp
    
[/code]
  

# Configuring the system
## flash-kernel
We are going to use flash-kernel to generate the _boot.src_. Tell it which hardware we're aiming for. (Devices listed in: _/usr/share/flash-kernel/db/all.db_) 
[code] 
     mkdir /mnt/etc/flash-kernel/
     echo "Cubietech Cubietruck" >> /mnt/etc/flash-kernel/machine
    
[/code]
Kernel arguments: 
[code] 
    echo 'LINUX_KERNEL_CMDLINE="console=ttyS0,115200 hdmi.audio=EDID:0 disp.screen0_output_mode=EDID:1280x1024p60 root=/dev/mmcblk0p1 rootwait panic=10 ${extra}"' >> /mnt/etc/default/flash-kernel
    
[/code]
## Kernel modules
Write extra modules that should be loaded at boot time to _/mnt/etc/modules_. 
[code] 
     echo "rtc_sunxi" >> /etc/initramfs-tools/modules
    
[/code]
## Base configuration files
[code] 
     echo "/dev/mmcblk0p1  /           ext4    relatime,errors=remount-ro        0       1" > /mnt/etc/fstab
     echo "HOSTNAME" > /mnt/etc/hostname
    
[/code]
Hint: Please consider using your favorite debian-mirror instead of _ftp.debian.org_. 
[code] 
    cat <<EOF > /mnt/etc/apt/sources.list
    # 
    
    deb http://ftp.debian.org/debian/ testing main non-free contrib
    deb-src http://ftp.debian.org/debian/ testing main non-free contrib
    
    deb http://security.debian.org/ testing/updates main contrib non-free
    deb-src http://security.debian.org/ testing/updates main contrib non-free
    
    # testing-updates, previously known as 'volatile'
    deb http://ftp.debian.org/debian/ testing-updates main contrib non-free
    deb-src http://ftp.debian.org/debian/ testing-updates main contrib non-free
    EOF
[/code]
[code] 
    cat <<EOF > /mnt/etc/apt/sources.list.d/experimental.list
    deb http://ftp.debian.org/debian/ unstable main non-free contrib
    deb-src http://ftp.debian.org/debian/ unstable main non-free contrib
    
    deb http://ftp.debian.org/debian/ experimental main non-free contrib
    deb-src http://ftp.debian.org/debian/ experimental main non-free contrib
    EOF
[/code]
[code] 
    cat <<EOF > /mnt/etc/apt/preferences.d/experimental
    Package: *
    Pin: release o=Debian,a=unstable
    Pin-Priority: 150
    
    Package: *
    Pin: release a=experimental
    Pin-Priority: -10
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
Now _chroot_ in to the new system, install kernel and set everything up. 
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
       apt-get update
       apt-get install locales && dpkg-reconfigure locales
       dpkg-reconfigure tzdata
    
[/code]
Install the kernel and u-boot (u-boot from debian is not used, but it does no harm and i'll include it for future reference) 
[code] 
       apt-get -t experimental install linux-image-3.16-rc6-armmp-lpae u-boot u-boot-tools
    
[/code]
Or, if you want simple frame-buffer support (on some cards) go with kernel >3.19: 
[code] 
       apt-get -t experimental install linux-image-3.19.0-trunk-armmp-lpae u-boot u-boot-tools
    
[/code]
Install non-free firmware and add one currently missing file to the wifi-firmware: 
[code] 
       apt-get install firmware-linux firmware-brcm80211 sunxi-tools flash-kernel
       wget -O /lib/firmware/brcm/brcmfmac43362-sdio.txt <http://dl.cubieboard.org/public/Cubieboard/benn/firmware/ap6210/nvram_ap6210.txt>
    
[/code]
Install a few other things: 
[code] 
       apt-get install console-setup keyboard-configuration systemd systemd-sysv openssh-server ntp
    
[/code]
At this point, debian should have generated a kernel image _/boot/vmlinuz-???_ and an initrd _/boot/initrd.img-???_ for you. Generate the _/boot/boot.scr_ , set a password and after a little cleanup you're set: 
[code] 
       flash-kernel
       passwd root
       exit
    
[/code]
