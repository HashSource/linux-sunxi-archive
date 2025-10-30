# Gentoo
There are some sunxi or A10 portage overlays floating around the net. 
## Contents
  * [1 Introduction][21996]
    * [1.1 sunxi-bsp][21997]
      * [1.1.1 Crosscompiler][21998]
      * [1.1.2 Dependencies][21999]
        * [1.1.2.1 qemu][22000]
      * [1.1.3 Building sunxi-bsp][22001]
    * [1.2 Debian][22002]
      * [1.2.1 debootstrap][22003]

# Introduction
## sunxi-bsp
As descriped in the [Manual_build_howto][22004] guide, Gentoo can be used just fine to build the sunxi-bsp. There are some dependencies however. Besides the obvious, git, a cross-compiler is needed. It is possible to use the pre-compiled linaro toolchain, but why would you? 
### Crosscompiler
Gentoo has the magnificent [Embedded Handbook][22005] which describes in detail how to setup a cross compiler. The jist of it is emerge crossdev. Once crossdev is installed, it's time to build a crosscompiler. 
[code] 
    crossdev -S -P -v -t arm-pc-linux-gnueabi
[/code]
If you wish to use uclibc instead of regular gnu-libc, you can do easily by replacing _gnu_ with _uclibc_. 
[code] 
    crossdev -S -P -v -t arm-pc-linux-uclibceabi
[/code]
This will build a cross-compiler using regular libc and the Embedded ABI (eabi) and by default uses hardfloat. If you wish to use softfloat, call crossdev with 'softfloat' in the _vendor_ field. In the below example we use **pc_softfloat** but just **softfloat** is sufficient. 
[code] 
    crossdev -S -P -v -t arm-pc_softfloat-linux-gnueabi
[/code]
While building gcc with soft-float support is understandable, the A10 has hardfloat support, so usage of softfloats isn't necessary. 
Any other combination of course is also possible, like using abi instead of eabi. See **crossdev -t help** for more information. 
The resulting links will be installed into /usr/bin. On the case of an x86_64 host, you can find them on /usr/x86_64-pc-linux-gnu/arm-pc-linux-gnueabi/gcc-bin/<gcc-version>
### Dependencies
Besides the cross-compiler, _u-boot-tools_ is needed to be able to build u-boot. It is optional for the kernel or any rootfs. Installing the final result onto an SD-Card requires sudo (even when running the final step as root) and sfdisk to partition the SD-Card from the script. Also partprobe is required to be able autodetect the newly created partitions, as sfdisk -R doesn't seem to work on Gentoo. 
#### qemu
To be able to chroot from an x86 based machine into the arm image, qemu with user-space ARM support is needed. There is an excellent [Gentoo Manual][22006]. Quickly summarized; 
[code] 
    QEMU_USER_TARGETS="arm" USE=static-user emerge -1 app-emulation/qemu
    
[/code]
Next you need to register BINFMT wrapper (you also need to have **CONFIG_BINFMT_MISC** enabled in your kernel) which tells the system to run arm binaries through qemu emulation layer. So either use the init script: 
[code] 
    /etc/init.d/qemu-binfmt start
    
[/code]
or register it manually: 
[code] 
    echo ':arm:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x28\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-arm:' > /proc/sys/fs/binfmt_misc/register
    
[/code]
### Building sunxi-bsp
For the rest the [Manual_build_howto][22004] guide can be used as you would, just remember to pass **CROSS_COMPILE=arm-pc-linux-gnueabi-** to any make as a variable, e.g. **make CROSS_COMPILE=arm-pc-linux-gnueabi-** Equally it is possible to edit the default in the Makefile for the compiler used (not recommended) or install the toolchain as _arm-linux-gnueabihf_ (not recommended either). 
## Debian
While Gentoo is an awesome distribution, and even using embedded Gentoo is quite possible, it isn't quite the easiest way. Also, having Gentoo natively on the A10 allows either to build all packages on a buildhost and turn Gentoo into a binary distro on the A10 or build natively, which is silly in terms of time used to compile, space required, etc. On the other hand, running embedded Debian isn't so bad, and even on Gentoo, we can use cross-deboostrap! 
### debootstrap
Debootstrap can be emerged quite easily on Gentoo. It is advised to remove the '-nls' USE flag to save some dependencies. If nls is heavily really required for deboostrap (I don't think the final rootfs is limited by it, but need to confirm) do set the flag of course. 
Within the sunxi-bsp, go to the _rootfs' directory; then:_
[code] 
    mkdir debfs-armhf
    dd if=/dev/zero of=debfs-armhf.img bs=1M count=1536
    mkfs.ext4 -F debfs-armhf.img
    mount -o loop debfs-armhf.img debfs-armhf
    
[/code]
This should yield a empty image loopback mounted. Running deboostrap on it: 
[code] 
    debootstrap --verbose --no-check-gpg --arch armhf --variant=minbase --foreign sid debfs-armhf http://ftp.debian.org/debian
[/code]
Now cd into the partially filled image and copy the statically linked qemu-user binary.
