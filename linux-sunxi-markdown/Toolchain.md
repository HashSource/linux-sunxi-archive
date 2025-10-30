# Toolchain
This page describes how to get a Toolchain, a build environment matching your target device's architecture, so you can cross-compile for that architecture. 
## Contents
  * [1 General information][55211]
    * [1.1 Cross-compile versus native][55212]
    * [1.2 Packaged versus standalone toolchain][55213]
    * [1.3 armhf versus armel][55214]
      * [1.3.1 Using armel with our wiki][55215]
  * [2 Installation as part of a distribution][55216]
    * [2.1 Debian/Ubuntu][55217]
      * [2.1.1 ArmHF (32bit)][55218]
      * [2.1.2 AArch64][55219]
      * [2.1.3 Known issues/Caveats][55220]
        * [2.1.3.1 Ubuntu 16.04 LTS (xenial xerus)][55221]
    * [2.2 Fedora][55222]
    * [2.3 Gentoo][55223]
      * [2.3.1 ArmHF (32bit)][55224]
        * [2.3.1.1 AArch64][55225]
        * [2.3.1.2 OpenRISC][55226]
    * [2.4 OpenSUSE/SUSE][55227]
    * [2.5 Arch Linux][55228]
      * [2.5.1 ArmHF][55229]
  * [3 Standalone toolchain installation][55230]
    * [3.1 Linaro][55231]
      * [3.1.1 Legacy sunxi kernel][55232]
    * [3.2 Bootlin][55233]

# General information
A toolchain is a set of system libraries, compilers and other tools which allow you to build (in our case, cross-compile) u-boot and the kernel for a target platform. 
## Cross-compile versus native
With quad 64-bit cores clocked at 1.5GHz it is feasible to build any code directly on the target machine. Usually though, modern x86 machines are clocked several times faster, often have more cores or threads available, and much more memory installed and much faster IO. It still makes sense to cross-compile in most cases, especially for building the kernel. 
Our wiki is geared towards cross compilation, but if you do want to compile on the target machine directly, you can alter the build instructions from (typically): 
[code] 
    make CROSS_COMPILE=arm-linux-gnueabihf-
[/code]
to simply: 
[code] 
    make
[/code]
by trivially removing the _CROSS_COMPILE_ argument. 
## Packaged versus standalone toolchain
These days, linux distributions package armhf, armel and aarch64 toolchains for you. A packaged toolchain will be kept up to date with your distribution, and should be available in your PATH without your intervention. 
Standalone toolchains are big tarballs with a whole toolchain inside. This allows for user-local installation, but is not kept up to date with your distribution package management, and you need to add this toolchain to your PATH. 
There should be little point in using a standalone toolchain, so use the version that comes with your distribution. 
## armhf versus armel
Around the mid 2010s, a new 32bit arm ABI (application binary interface) was introduced to make use of the floating point units on most modern ARM cores. This is called Hard-Float, for hardware-floating-point-unit. The newer ABI is now called **armhf**. Armhf has since become the go-to default. 
Mixing armhf and armel ABIs between bootloader, kernel and rootfs should theoretically work, but your mileage may vary. 
Throughout this wiki, we default to the hardfloat toolchain for armv7/32bit architectures. 
### Using armel with our wiki
If you are using an armel toolchain, then whenever you see something like: 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf-
[/code]
You can just replace **arm-linux-gnueabihf-** with **arm-linux-gnueabi-**
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi-
[/code]
# Installation as part of a distribution
## Debian/Ubuntu
### ArmHF (32bit)
[code] 
    apt-get install gcc-arm-linux-gnueabihf
[/code]
### AArch64
[code] 
    apt-get install gcc-aarch64-linux-gnu
[/code]
### Known issues/Caveats
#### Ubuntu 16.04 LTS (xenial xerus)
The gcc version in Ubuntu 16.04 (gcc version 5.4.0 20160609) bugs while compiling U-Boot: 
[code] 
    {standard input}: Assembler messages:
    {standard input}:323: Error: push/pop do not support {reglist}^ -- `pop {r0,r1,r2,r3,r4,r9,ip,pc}^'
    scripts/Makefile.build:280: recipe for target 'arch/arm/cpu/armv7/sunxi/psci.o' failed
[/code]
If you really wish to still use 16.04 today, you might need to get a [standalone toolchain][55234]
## Fedora
[code] 
    yum install gcc-arm-linux-gnu
[/code]
## Gentoo
The [crossdev tool][55235][[1]][55236] is the standard way of dealing with crosscompilers in Gentoo. Command line options are used to specify any arbitrary mix of different versions of the kernel headers, glibc, binutils and gcc. You can also use the -S option instead (to pick whatever is considered to be stable at the moment), but in this case the crosscompiler will be also upgraded as part of the regular distribution updates, which might be a bit annoying. 
### ArmHF (32bit)
Even though Gentoo normally uses **armv7a-hardfloat-linux-gnueabi** as the toolchain triplet on ARM, we can also use Debian alike **arm-linux-gnueabihf** variant in order to be able to use the compilation instructions from the linux-sunxi wiki as-is (without substituting the toolchain name). 
[code] 
    emerge crossdev
    crossdev --kernel =3.18 --libc =2.20-r2 --binutils =2.24-r3 --gcc =4.8.5 \
             --genv 'USE="-fortran -mudflap -nls -openmp multilib" EXTRA_ECONF="--with-cpu=cortex-a8 --with-float=hard"' -t arm-linux-gnueabihf
    
[/code]
#### AArch64
[code] 
    emerge crossdev
    crossdev --kernel =3.18 --libc =2.21-r1 --binutils =9999 --gcc =4.9.3 \
             --genv 'USE="-fortran -mudflap -nls -openmp multilib -sanitize" EXTRA_ECONF="--enable-fix-cortex-a53-843419"' -t aarch64-linux-gnu
    
[/code]
Note: binutils =9999 (fetch sources from git) should be replaced with =2.26 as soon as binutils 2.26 is added to portage. Such new binutils version is necessary for having a Cortex-A53 erratum 843419 workaround. 
#### OpenRISC
If you have one of the Allwinner SoC variants with an additional [OpenRISC core][55237] (for example [A31][55238] and [H3][55239] have it), then you might want to also build an OpenRISC crosscompiler too: 
[code] 
    emerge crossdev
    mkdir -p /etc/portage/patches/cross-or1k-elf/gcc-5.2.0
    cd /etc/portage/patches/cross-or1k-elf/gcc-5.2.0
    wget https://gist.githubusercontent.com/ssvb/28e22f4086af26ec9cd0/raw/8d3d091177156a92497f31de3bfb3d7da9e52649/0001-OpenRISC-support-for-GCC-5.2.0.patch
    crossdev --binutils =2.25.1-r1 --gcc =5.2.0 --libc =2.2.0.20150423 \
             --genv 'USE="cxx multilib -fortran -mudflap -nls -openmp -sanitize"' \
             -s4 -t or1k-elf
    
[/code]
Please note that the upstream GCC does not support OpenRISC yet, so the OpenRISC code is still brewing in <https://github.com/openrisc/or1k-gcc.git> and we can solve this problem by just providing a patch for GCC in the _/etc/portage/patches_ directory. 
* * *
  1. [↑][55240] The Gentoo website has undergone a major overhaul as of April 2015. While a backup of the old content is still available, it seems to have left the _Gentoo Embedded Handbook_ in a non-functional state. You can still find a copy [via archive.org][55241]. The wiki article on [Raspberry Pi Cross building][55242] might also be helpful.

## OpenSUSE/SUSE
## Arch Linux
### ArmHF
Install these AUR packages, one at a time, in order: 
[code] 
    arm-linux-gnueabihf-binutils
    arm-linux-gnueabihf-gcc-stage1
    arm-linux-gnueabihf-linux-api-headers
    arm-linux-gnueabihf-glibc-headers
    arm-linux-gnueabihf-gcc-stage2
    arm-linux-gnueabihf-glibc
    
[/code]
# Standalone toolchain installation
## Linaro
For the longest time, Linaro has been providing [ready built toolchains for you to download][55243]. 
Download a gcc-linaro-<major>.<minor>-<year>.<month>.tar.xz file and untar it. 
You will find a bin directory in there. Temporarily add it to the environment you are building from: 
[code] 
    export PATH="$PATH":/home/user/folder/gcc-linaro-arm-linux-gnueabihf-*_linux/bin/
[/code]
### Legacy sunxi kernel
If you, for whatever reason, still want to use the 2012-2014 era legacy 3.4 sunxi kernel, it makes sense to use the [4.9.4 linaro toolchain][55244]. 
The 4.8 linaro toolchain was known to have issues when building the sunxi kernel. 
## Bootlin
Bootlin also provices [glibc / musl / uclibc based toolchains][55245].
