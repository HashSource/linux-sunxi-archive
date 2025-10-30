# Debootstrap
On debian based systems, you can manually initialize an installation using _debootstrap_. 
This whole process takes half an hour or so (depending on network bandwidth and disk setup, direct to sd-card will be slower), and will result in a 250MB root filesystem, or a 80MB tarball, 
## Contents
  * [1 Pre-requisites][16467]
  * [2 First stage][16468]
  * [3 Second stage][16469]
    * [3.1 From a different host architecture][16470]
    * [3.2 From the same architecture][16471]
    * [3.3 Debootstrap second stage][16472]
  * [4 Mandatory setup][16473]
    * [4.1 Add root passwd][16474]
    * [4.2 Hostname][16475]
    * [4.3 Fstab][16476]
      * [4.3.1 Add tmpfs][16477]
      * [4.3.2 Add root filesystem][16478]
      * [4.3.3 Add boot partition (if present)][16479]
    * [4.4 Serial console][16480]
      * [4.4.1 With systemd][16481]
      * [4.4.2 With upstart][16482]
      * [4.4.3 With sysvinit][16483]
  * [5 Optional/deferrable setup][16484]
    * [5.1 Locales][16485]
    * [5.2 Configure ethernet with dhcp][16486]
    * [5.3 More complete apt sources.list][16487]
      * [5.3.1 Debian][16488]
      * [5.3.2 Ubuntu][16489]
    * [5.4 Openssh-server][16490]
      * [5.4.1 Root login over SSH][16491]
        * [5.4.1.1 Key based authentication][16492]
        * [5.4.1.2 Password based authentication][16493]
      * [5.4.2 PRNG entropy seeding speedups (debian buster!)][16494]
      * [5.4.3 Date/Time][16495]
  * [6 Cleanup][16496]
  * [7 Tarring up the result][16497]

# Pre-requisites
  * A debian based distribution.
  * package **debootstrap**
  * package **qemu-user-static** if you are doing this from a different architecture

It is assumed that your target filesystem is mounted in **/mnt**
Also, figure out which distribution version you wish to use. Current debian stable is called _trixie_ (debian 13.1, dated 20250906), and a current ubuntu is called _noble_ (Ubuntu 24.04.3 LTS aka "Noble Numbat", dated 20250807). 
# First stage
This step can be run from any host architecture. 
**armhf**
[code] 
    debootstrap --arch=armhf --foreign <distro> /mnt/
[/code]
**arm64**
[code] 
    debootstrap --arch=arm64 --foreign <distro> /mnt/
[/code]
Replace <distro> with your preferred distribution, probably _trixie_ or _noble_. 
# Second stage
## From a different host architecture
Copy qemu to the target filesystem and chroot to target: 
**armhf**
[code] 
    cp /usr/bin/qemu-arm-static /mnt/usr/bin/
    chroot /mnt /usr/bin/qemu-arm-static /bin/sh -i
[/code]
**arm64**
[code] 
    cp /usr/bin/qemu-aarch64-static /mnt/usr/bin/
    chroot /mnt /usr/bin/qemu-aarch64-static /bin/sh -i
[/code]
## From the same architecture
Chroot to target: 
[code]
    chroot /mnt /bin/sh -i
[/code]
## Debootstrap second stage
[code] 
    /debootstrap/debootstrap --second-stage
[/code]
It's also possible to use `qemu-debootstrap` instead of manual two-stage bootstrap. 
# Mandatory setup
## Add root passwd
While in the chroot, run:
[code]
    passwd
[/code]
## Hostname
You do not wish to have your rootfs have the same hostname as your host machine, so it is wise to change this now, as this will surreptitiously influence things like your ssh keys. 
Simply edit _/etc/hostname_ , this can be done from both inside and outside of the chroot. 
## Fstab
This can be done from both inside and outside of the chroot. 
### Add tmpfs
[code] 
    none		/tmp	tmpfs	defaults,noatime,mode=1777	0	0
[/code]
### Add root filesystem
[code] 
    /dev/mmcblk0p2	/	ext4	defaults	0	1 
[/code]
Rename this to _/dev/mmcblk0p1_ if you use a single partition. 
### Add boot partition (if present)
[code] 
    /dev/mmcblk0p1	/boot	ext4	defaults	0	2 
[/code]
Adjust filesystemtype (currently ext4) accordingly. 
## Serial console
### With systemd
  * From within the chroot:
[code]systemctl enable [[email protected]][16498]
[/code]

  * Outside of chroot:
[code]ln -s /lib/systemd/system/[[email protected]][16498] /mnt/etc/systemd/system/getty.target.wants/[[email protected]][16498]
[/code]

### With upstart
Please follow [this ubuntu howto][16499], which can be done from outside the chroot. 
### With sysvinit
Add the following line to _/etc/inittab_ , independent of chroot (apart from the path): 
[code] 
    T0:2345:respawn:/sbin/getty -L ttyS0 115200 vt100
[/code]
# Optional/deferrable setup
Most of these things can be done from within the chroot or on the actual machine. They are really nice to have, but not totally necessary before the first boot of the target machine. 
If debians servers are not resolving, you might need to copy the hosts' resolv.conf to the target filesystem before chrooting back in. 
## Locales
Run:
[code]
    apt-get install locales
    dpkg-reconfigure locales
[/code]
It might make sense to choose _en_US.UTF-8_
## Configure ethernet with dhcp
Add the following to _/etc/network/interfaces_
[code] 
    auto lo eth0
    allow-hotplug eth0
    iface lo inet loopback
    iface eth0 inet dhcp
[/code]
Direct editing is preferred over catting, as that will overwrite any inclusion of interfaces.d/ 
## More complete apt sources.list
Here are some expanded sources.lists, which are bound to be out of date. Edit _/etc/apt/sources.list_ and add. 
### Debian
Replace _trixie_ with your chosen debian distribution name. 
[code] 
    deb http://deb.debian.org/debian/ trixie main contrib non-free
    deb-src http://deb.debian.org/debian/ trixie main contrib non-free
    deb http://deb.debian.org/debian/ trixie-updates main contrib non-free
    deb-src http://deb.debian.org/debian/ trixie-updates main contrib non-free
    deb http://deb.debian.org/debian-security/ trixie-security/updates main contrib non-free
    deb-src http://deb.debian.org/debian-security/ trixie-security/updates main contrib non-free
[/code]
### Ubuntu
Replace _noble_ with your chosen ubuntu version. 
[code] 
    deb http://ports.ubuntu.com/ noble main universe
    deb-src http://ports.ubuntu.com/ noble main universe
    deb http://ports.ubuntu.com/ noble-security main universe
    deb-src http://ports.ubuntu.com/ noble-security main universe
    deb http://ports.ubuntu.com/ noble-updates main universe
    deb-src http://ports.ubuntu.com/ noble-updates main universe
[/code]
## Openssh-server
Run:
[code]
    apt-get install openssh-server
[/code]
### Root login over SSH
If you want access as root, you will need to edit _/etc/ssh/sshd_config_. 
#### Key based authentication
Uncomment the following line: 
[code] 
    #PermitRootLogin prohibit-password
[/code]
And add your key to _/root/.ssh/authorized_keys_. 
#### Password based authentication
Uncomment the _PermitRootLogin_ line, and set it to _yes_. 
[code] 
    PermitRootLogin yes
[/code]
### PRNG entropy seeding speedups (debian buster!)
In case you notice long startup times for ssh server (or any other software calling `getrandom()`, see [debian bug #912087][16500]) on your device, it can be alleviated by installing `haveged` package: 
[code] 
    apt install haveged
[/code]
This issue is not seen on Debian 9 (Stretch), but does occur on Debian 10 (Buster). 
### Date/Time
If _apt-update_ errors out while verifying signatures: 
[code] 
    Err:2 http://deb.debian.org/debian-security trixie-security/updates InRelease
      Sub-process /usr/bin/sqv returned an error code (1), error message is: Verifying signature:            Not live until 2025-10-29T08:24:51Z Verifying signature:            Not live until 2025-10-29T08:24:51Z
[/code]
Then you might need to set the date/time closer to reality: 
[code] 
    date --set 20251029 --set 11:41:14
[/code]
You might want to install a secure NTP client, one (systemd-timesyncd) is now part of the systemd world-domination project. 
# Cleanup
From within the chroot, run _apt-get clean_ to remove cached packages. 
If you were using a qemu chroot, then you need to remove _/mnt/usr/bin/qemu-arm-static_ or _/usr/bin/qemu-aarch64-static_. 
If you needed the hosts' resolv.conf, then you need to remove _/mnt/etc/resolv.conf_
# Tarring up the result
You spent some time setting this up, and you might not want to retrace the above steps every few days, so you might as well throw this into a 100ish MB tarball: 
From the host, from within _/mnt/_ , run: 
[code] 
    tar -cjpf /home/user/sunxi_rootfs.tar.bz2 .
[/code]
Be careful when you unpack that, as rootfses are pretty much the only time tarballs should be untarred in the local directory.
