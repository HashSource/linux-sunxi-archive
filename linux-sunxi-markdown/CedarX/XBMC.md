# CedarX/XBMC
< [CedarX][11916]
 
**This page is outdated**. It's about running an outdated version of XBMC with GPL violating software.  

Please refer to the new [Kodi page][11919]!
**Kodi** (formerly **XBMC**) is a popular free and open source media player software application designed as a 10-foot frontend graphical home theater (a.k.a. media center) interface for large-screen televisions. Made to be controlled with a remote control it enables ARM-based media players and set-top boxes like those with Allwinner SoCs with [CedarX][11916] VPU (Video Processor Unit) to hardware decode and play high-definition videos, music, and other digital media files from local and network storage media, as well as stream podcasts, videocasts, and such of the internet, and displayed in a appealing way on your living-room TV. 
This article contain instructions on compiling and developing Kodi/XBMC on and for Allwinner SoCs that features the [CedarX][11916] VPU, like [A10][11920], [A10s][11921], [A13][11922], [A20][11923], and [A23][11924]. Note that these instructions are specifically only meant for developers and advanced or expert Linux users that can actively assist with the porting process. 
## Contents
  * [1 Overview][11925]
  * [2 Building Kodi/XBMC for A10 and A20 SoC series][11926]
    * [2.1 Prerequisites][11927]
      * [2.1.1 Prepare your SD-Card][11928]
      * [2.1.2 Boot into your target system][11929]
      * [2.1.3 Install the dependencies for XBMC (needs update!)][11930]
    * [2.2 Native Compile of XBMC][11931]
      * [2.2.1 Prerequisites for native compile][11932]
      * [2.2.2 Checkout the source code][11933]
      * [2.2.3 Build][11934]
    * [2.3 Cross Compile of XBMC][11935]
      * [2.3.1 Setup Cross Compiler][11936]
      * [2.3.2 Prerequisites for Cross Compiling][11937]
      * [2.3.3 Checkout the source code][11938]
      * [2.3.4 Update XBMC build config][11939]
      * [2.3.5 Build][11940]
      * [2.3.6 Move XBMC to target system][11941]
    * [2.4 Start XBMC][11942]
    * [2.5 Using the Android libraries via libhybris][11943]
    * [2.6 Troubleshooting][11944]
  * [3 Configuring XBMC dependencies for Linux on A10 based devices][11945]
    * [3.1 Getting IR (infrared) remotes working on A10 based media players][11946]
  * [4 Enabling dirty regions (a.k.a. dirty textures) for XBMC][11947]
  * [5 Sources implementing CedarX support in XBMC][11948]
  * [6 See also][11949]
  * [7 xternal Links][11950]
  * [8 References][11951]

# Overview
Kodi/XBMC has already have an initial but ultimatly obsolete port for the A10 / A20 SoC with [CedarX][11916] hardware accelerated video decoding, this experimental third-party port and the code patches have however not made it upstream into mainline Kodi/XBMC.[[1]][11952][[2]][11953]
Pre-built application binaries of this initial port are not available so therefore you will need to compile Kodi/XBMC yourself, at least until if and when code for these CedarX based Allwinner SoCs makes it into the mainline XBMC upstream at <http://kodi.tv>
Team-Kodi (who before used to be known as Team-XBMC), the official development team of Kodi/XBMC, does currently not recommend that any end-user buy Allwinner A1x or A2x based hardware for the specific purpose of only running Kodi/XBMC since they do not have the resources to support this platform as of yet. 
More information about Kodi/XBMC can be found on wikipedia <http://en.wikipedia.org/wiki/XBMC> and the Kodi wiki <http://wiki.kodi.tv> or <http://forum.kodi.tv>
# Building Kodi/XBMC for A10 and A20 SoC series
This is a little how-to of steps to compile XBMC for devices using Allwinner A10 and A20 SoC series (e.g. for hardware like Mele A1000, Cubieboard, and Banana Pi) based on Empat0's GitHub sources <http://github.com/empatzero/xbmca10>. The development work on the coding side was all done by Empat0 (a.k.a. empat zero). The used repository in the example below is however from <http://github.com/rellla/xbmca10> which is currently the newest and contains a few adaptions. It is a fork of empat0's work. If you want an only A20 version you can use this repository: <https://github.com/fflayol/xbmc> . 
The result should be a Debian armhf system with XBMC using [CedarX][11916] for hardware accelerated video decoding. 
This version of XBMC runs directly on the framebuffer, and thus XServer is therefor not needed! 
## Prerequisites
There are more ways to prepare a working rootfs for XBMC. You can either prepare the sdcard directly as described or you can chroot into the rootfs on your host system and sync it with your sdcard later when you have finished. So the following steps can also be done in a chroot on your host if you are cross-compiling. 
### Prepare your SD-Card
Create a bootable SD-Card follwing [ our manual build howto][11954] and Debian. Be sure to use a kernel with mali-drivers-version r3p0 (sunxi-3.0 should be good). 
### Boot into your target system
Boot the new debian from the sd-card directly on the target and bring the system up to date: 
[code] 
     root@mele:~/# apt-get update
     root@mele:~/# apt-get upgrade
    
[/code]
### Install the dependencies for XBMC (needs update!)
[code] 
     root@mele:~/# apt-get build-dep xbmc
    
[/code]
    this should install the following packages:``
` `    `autoconf automake autopoint autotools-dev binutils bsdmainutils build-essential bzip2 cmake cmake-data comerr-dev cpp cpp-4.4 cpp-4.6 curl debhelper dpkg-dev emacsen-common fontconfig-config g++ g++-4.4 g++-4.6 gawk gcc gcc-4.4 gcc-4.4-base gcc-4.6 gcc-4.6-base gettext gettext-base git git-man gperf groff-base html2text intltool-debian krb5-multidev libao-common libao-dev libao4 libarchive12 libasound2 libasound2-dev libasprintf0c2 libass-dev libass4 libasyncns0 libavahi-client-dev libavahi-client3 libavahi-common-data libavahi-common-dev libavahi-common3 libavcodec-dev libavcodec53 libavfilter-dev libavfilter2 libavformat-dev libavformat53 libavutil-dev libavutil51 libbluetooth-dev libbluetooth3 libbluray-dev libbluray1 libboost-date-time1.49-dev libboost-date-time1.49.0 libboost-dev libboost-serialization1.49-dev libboost-serialization1.49.0 libboost-thread-dev libboost-thread1.49-dev libboost-thread1.49.0 libboost1.49-dev libbz2-dev libc-dev-bin libc6-dev libcaca-dev libcaca0 libcdio-dev libcdio13 libcec-dev libcec1 libcroco3 libcurl3 libcurl3-gnutls libcurl4-gnutls-dev libcwiid-dev libcwiid1 libdbus-1-3 libdbus-1-dev libdirac-encoder0 libdirectfb-1.2-9 libdirectfb-dev libdirectfb-extra libdpkg-perl libdrm2 libelf1 libenca-dev libenca0 liberror-perl libexpat1 libexpat1-dev libflac-dev libflac8 libfontconfig1 libfontconfig1-dev libfreetype6 libfreetype6-dev libfribidi-dev libfribidi0 libgcrypt11-dev libgettextpo0 libgl1-mesa-dev libgl1-mesa-glx libglapi-mesa libglew-dev libglew1.7 libglib2.0-bin libglib2.0-dev libglu1-mesa libglu1-mesa-dev libgmp10 libgnutls-dev libgnutls-openssl27 libgnutlsxx27 libgomp1 libgpg-error-dev libgsm1 libgssrpc4 libhal-dev libhal-storage-dev libhal-storage1 libhal1 libice-dev libice6 libicu48 libidn11-dev libiso9660-8 libiso9660-dev libjasper-dev libjasper1 libjbig-dev libjbig0 libjpeg8 libjpeg8-dev libjson0 libkadm5clnt-mit8 libkadm5srv-mit8 libkdb5-6 libkrb5-dev liblcms1 libldap-2.4-2 libldap2-dev libltdl-dev libltdl7 liblzo2-2 liblzo2-dev libmad0 libmad0-dev libmicrohttpd-dev libmicrohttpd10 libmikmod2 libmikmod2-dev libmodplug-dev libmodplug1 libmp3lame-dev libmp3lame0 libmpc2 libmpeg2-4 libmpeg2-4-dev libmpfr4 libmysqlclient-dev libmysqlclient18 libnettle4 libnfs-dev libnfs1 libogg-dev libogg0 libopencv-core2.3 libopencv-imgproc2.3 libopenjpeg2 liborc-0.4-0 libp11-kit-dev libpcre3-dev libpcrecpp0 libpipeline1 libplist-dev libplist1 libpng12-0 libpng12-dev libpopt0 libpostproc-dev libpostproc52 libpthread-stubs0 libpthread-stubs0-dev libpulse-dev libpulse-mainloop-glib0 libpulse0 libpython2.7 librtmp-dev librtmp0 libsamplerate0 libsamplerate0-dev libsasl2-2 libschroedinger-1.0-0 libsdl-image1.2 libsdl-image1.2-dev libsdl-mixer1.2 libsdl-mixer1.2-dev libsdl1.2-dev libsdl1.2debian libshairport-dev libshairport1 libsigsegv2 libslang2-dev libsm-dev libsm6 libsmbclient libsmbclient-dev libsndfile1 libspeex1 libsqlite3-0 libsqlite3-dev libssh2-1 libssh2-1-dev libssl-dev libstdc++6-4.4-dev libstdc++6-4.6-dev libswscale-dev libswscale2 libtalloc2 libtasn1-3-dev libtdb1 libtheora0 libtiff4 libtiff4-dev libtiffxx0c2 libtimedate-perl libtinyxml-dev libtinyxml2.6.2 libtool libts-0.0-0 libts-dev libudev-dev libunistring0 libva-dev libva-egl1 libva-glx1 libva-tpi1 libva-x11-1 libva1 libvdpau-dev libvdpau1 libvorbis-dev libvorbis0a libvorbisenc2 libvorbisfile3 libvpx1 libwbclient0 libwebp-dev libwebp2 libx11-dev libx11-xcb1 libx264-123 libxau-dev libxcb-glx0 libxcb1-dev libxdamage1 libxdmcp-dev libxext-dev libxfixes3 libxi6 libxml2-dev libxmlrpc-core-c3 libxmu-dev libxmu-headers libxmu6 libxrandr-dev libxrandr2 libxrender-dev libxrender1 libxt-dev libxt6 libxtst6 libxvidcore4 libxxf86vm1 libyajl-dev libyajl2 linux-libc-dev m4 make man-db mesa-common-dev mysql-common patch pkg-config po-debconf python python-dev python-imaging python-minimal python-support python2.7 python2.7-dev python2.7-minimal tsconf ttf-dejavu-core ucf x11-common x11proto-core-dev x11proto-input-dev x11proto-kb-dev x11proto-randr-dev x11proto-render-dev x11proto-xext-dev xorg-sgml-doctools xtrans-dev yasm zip zlib1g-dev`
need to install 3 more dependencies: 
[code] 
     root@mele:~/# apt-get install swig default-jre libgtk2.0-bin libssh-4 libssh-dev
    
[/code]
ensure you use hardware acceleration 
[code] 
     root@mele:~/# echo -e "\nA10HWR=1" >> /etc/environment (to set it permanently)
    
[/code]
Now go on with [ Native Compile][11931] or [ Cross Compile][11935]. 
## Native Compile of XBMC
### Prerequisites for native compile
Create a swap-file, because otherwise the compiler runs out of memory during compiling and aborts 
[code] 
     root@mele:~/# dd if=/dev/zero of=/swap bs=1M count=384
     root@mele:~/# mkswap -c /swap
     root@mele:~/# swapon /swap
    
[/code]
Create your workspace directory: 
[code] 
     root@mele:~/# mkdir melehacking
     root@mele:~/# cd melehacking
    
[/code]
### Checkout the source code
[code] 
     root@mele:~/melehacking# apt-get install git
     root@mele:~/melehacking# git clone <git://github.com/rellla/xbmca10.git>
     root@mele:~/melehacking# cd xbmca10
     root@mele:~/melehacking/xbmca10# git checkout stage/Frodo
    
[/code]
### Build
The following external libs/ repos are used/ downloaded: 
  * taglib: <https://github.com/downloads/taglib/taglib/taglib-1.8.tar.gz>
  * cedarx: <https://github.com/linux-sunxi/cedarx-libs/tree/master/libcedarv/linux-armhf>
  * libmad: <ftp://ftp.mars.org/pub/mpeg/libmad-0.15.1b.tar.gz>
  * mali: <https://github.com/linux-sunxi/sunxi-mali-proprietary/tree/master/r3p0/armhf>
  * mali-dev: <https://github.com/linux-sunxi/sunxi-mali/tree/master/include>

Build dependencies 
[code] 
     root@mele:~/melehacking/xbmca10# cd tools/a10/depends
     root@mele:~/melehacking/xbmca10/tools/a10/depends# make
    
[/code]
Build xbmc itself 
[code] 
     root@mele:~/melehacking/xbmca10/tools/a10/depends# make -C xbmc
     root@mele:~/melehacking/xbmca10/tools/a10/depends# cd ../../../
     root@mele:~/melehacking/xbmca10# make install
    
[/code]
Move on to [#Start_XBMC][11942] and start XBMC. 
## Cross Compile of XBMC
This was tested with github.com/rellla/xbmca10 and built in Debian Sid as host. You will need several packages on the build system and a copy of the root file system of the target to build against. This howto assumes you are running off an SD card with the root file system in /dev/sdb2. 
### Setup Cross Compiler
  * At first set up your [toolchain][11955].

### Prerequisites for Cross Compiling
  * Sync and move SD card to build system
  * Mount the rootfs of the prepared SD Card

[code] 
     root@debian:~/# mount /dev/sdb2 /mnt/rootfs-a10
    
[/code]
  * Create symlinks to the mounted libraries

[code] 
     root@debian:~/# ln -s /mnt/rootfs-a10/lib/arm-linux-gnueabihf /lib/arm-linux-gnueabihf
     root@debian:~/# ln -s /mnt/rootfs-a10/usr/lib/arm-linux-gnueabihf /usr/lib/arm-linux-gnueabihf
     root@debian:~/# ln -s /mnt/rootfs-a10/usr/include/arm-linux-gnueabihf /usr/include/arm-linux-gnueabihf
    
[/code]
  * Install the dependencies for building XBMC on the host system

[code] 
     root@debian:~/# apt-get build-dep xbmc
     root@debian:~/# apt-get install shtool swig default-jre
    
[/code]
Note: If compiling on a 64 bit system there is a known bug with the libcurl headers not working with 32 bit programs. To work around the problem build on a 32 bit system, or copy the file /usr/include/curl/curlbuild.h from a 32 bit system to your 64 bit build host. 
  * Create your workspace directory:

[code] 
     root@debian:~/# mkdir melehacking
     root@debian:~/# cd melehacking
    
[/code]
### Checkout the source code
[code] 
     root@debian:~/melehacking# git clone <git://github.com/rellla/xbmca10.git>
     root@debian:~/melehacking# cd xbmca10
     root@debian:~/melehacking/xbmca10# git checkout stage/Frodo
    
[/code]
### Update XBMC build config
Update this section at line 48 of tools/a10/depends/depends.mk with your values, e.g. 
[code] 
     #where is your arm rootfs
     SDKSTAGE=/mnt/rootfs-a10
     #where is your xbmc install root 
     XBMCPREFIX=/allwinner/xbmc-pvr-bin$(HF)
     #where is your toolchain
     TOOLCHAIN=/usr/arm-linux-gnueabi$(HF)
    
[/code]
### Build
At this point the settings are basically the same for the native build: Build dependencies 
[code] 
     root@debian:~/melehacking/xbmca10# cd tools/a10/depends
     root@debian:~/melehacking/xbmca10/tools/a10/depends# make
    
[/code]
Build xbmc itself 
[code] 
     root@debian:~/melehacking/xbmca10/tools/a10/depends# make -C xbmc
     root@debian:~/melehacking/xbmca10/tools/a10/depends# cd ../../../
     root@debian:~/melehacking/xbmca10# make install
    
[/code]
### Move XBMC to target system
You should copy from your install location on your build system to an identical location on the target system (may not vital that they have the same path) like so ... 
[code] 
     root@debian:~/melehacking/xbmca10/cp -r /allwinner/xbmc-pvr-binhf /mnt/rootfs-a10/allwinner/xbmc-pvr-binhf
    
[/code]
To redistribute it, you can also create a tarball: 
[code] 
     root@debian:~/melehacking/xbmca10/tools/a10/depends# make -C package tarball
    
[/code]
This results in a xbmca10.tar.gz which includes all needed (and stripped) files in /allwinner/xbmc-pvr-binhf. This can easily be copied and extracted on the target rootfs. 
Umount your SD Card 
[code] 
     root@debian:~/melehacking/xbmca10# umount /dev/sdb2
    
[/code]
and boot it on your A10 Device. 
## Start XBMC
After a reboot you modprobe the needed modules (depending on the used kernel version): 
[code] 
     root@mele:~/# modprobe disp
     root@mele:~/# modprobe lcd
     root@mele:~/# modprobe hdmi
     root@mele:~/# modprobe mali
     root@mele:~/# export A10HWR=1 (ensure to have this set if not rebooting!)
     root@mele:~/# cd /allwinner/xbmc-pvr-bin/lib/xbmc
     root@mele:/allwinner/xbmc-pvr-bin/lib/xbmc# ./xbmc.bin
    
[/code]
## Using the Android libraries via libhybris
Due to some bugs in the native linux binaries of cedarx, _ssvb_ succeeded to use libhybris and the Android binaries instead. This is the recommended way. See [CedarX/libve][11956]. 
## Troubleshooting
  * (native) If you get a compiler error when processing h264.o or building xbmc.bin, then check, if swap is enabled. The compiler ran out of memory!
  * (native) If deb-building fails, check, if your tmp-directory has enough free space and is no tmpfs, because of the lack of memory an mele.
  * To use the bash-script bin/xbmc to start xbmc, you have to comment out the exec of FEH.py, because of a failing test of glxinfo -> no display found.
  * Depending on your setup you may have to change some things to build
  * If mysql_config is not found, even though it is clearly there you can set disable-mysql in Makefile under xbmca10/tools/a10/depends/xbmc
  * Header files might not be where they are expected, this can be fixed with symlinks and copying headers, for example...

[code] 
     ln -s usr/include/dbus1.0/dbus usr/include/dbus 
    
[/code]
  * Once you get in trouble with some mesa conflicts, ensure to not have installed the following packages on your target system:

[code] 
     libegl1-mesa libegl1-mesa-dev libegl1-mesa-drivers libgles2-mesa libgles2-mesa-dev
    
[/code]
  * Check the discussion section for more notes.
  * Ensure that you have installed ALL of the dependencies, header files etc. in your target rootfs and ensure that they are available during build. The build script does not search for them on your host-rootfs!

# Configuring XBMC dependencies for Linux on A10 based devices
## Getting IR (infrared) remotes working on A10 based media players
For getting IR (infrared) remote controls working on the A10 based media players, please see the [LIRC][11957] article in this wiki. Place a suitable [Lircmap.xml][11958] in userdata-directory. 
# Enabling dirty regions (a.k.a. dirty textures) for XBMC
This dirty region (a.k.a. dirty texture) feature in XBMC is designed to improve XBMC's GUI renderer performance on the GPU by only drawing when something like a texture changes on the screen, that region is then marked as dirty by XBMC's GUI library and only that region is redraw region on the screen. 
This feature is however still a little buggy and therefor not enabled by default in XBMC, but all users of XBMC on A10 based devices can try enabling the hidden "dirty regions" (a.k.a. "dirty textures") rendering feature advanced setting themselves manually. 
  * <http://wiki.xbmc.org/index.php?title=HOW-TO:Enable_dirty_regions>
  * <http://xbmc.org/theuni/2011/06/19/working-with-dirty-regions/>
  * [http://wiki.xbmc.org/index.php?title=Advancedsettings.xml#.3Calgorithmdirtyregions.3E][11959]

Dirty regions are any parts of the screen that have changed since the last frame. By not re-rendering what hasn't changed, big speed gains can be seen. Because all GPUs work differently, only Mode 3, combined with nofliptimeout=0, is guaranteed to be safe for everyone, but current timing issues with nofliptimeout keep this from being the default. Note that with "dirty regions" your system CPU usage might go up a little (because it is doing the dirty regions calculations) but your GPU usage will be much lower, and since it is the GPU and not CPU that is the bottleneck in XBMC for embedded systems your GUI performance will be better even though the CPU usage is higher. 
value | result | description   
---|---|---  
0  | Off  | The entire viewport is always rendered, which is the same as having the dirty regions feature disabled. This is the default mode.   
1  | Union  | All dirty regions are grouped into the smallest possible rectangle. This is typically the fastest mode for slower GPUs due to only making one pass.   
2  | Cost reduction  | Each dirty region is presented separately, in as many passes as there are regions.   
3  | Whole Screen  | The entire screen is rendered if there are any dirty regions. This, combined with nofliptimeout is a safe default for drivers that clear buffer contents (manifests as blinking or vibrating images)   
To enable dirty regions manually you need to create a "advancedsettings.xml" text file youself and put the XML <algorithmdirtyregions> enabling tags in there and copying to your "/userdata/" folder (/home/username/.xbmc/userdata/). 
Example: ` `
`
[code]
      <gui>    
        <algorithmdirtyregions>1</algorithmdirtyregions>
      </gui>
    
[/code]
```
``
You could also try to enable the <nofliptimeout> feature but that is even more experimental so know that it can cause even more GUI rendering issues in XBMC 
Example: ` `
`
[code]
      <gui>    
        <nofliptimeout>1000</nofliptimeout>
      </gui>
    
[/code]
```
``
To have both of these enabled your "advancedsettings.xml" then the finished file should look something like this: 
` `
`
[code]
    <advancedsettings>
      <gui>    
        <algorithmdirtyregions>1</algorithmdirtyregions>
        <nofliptimeout>1000</nofliptimeout>
      </gui>
    </advancedsettings>
    
[/code]
```
``
# Sources implementing CedarX support in XBMC
  * <https://github.com/empatzero/xbmca10>
    * <https://github.com/rellla/xbmca10> Recommended fork of empatzero ([Diff to upstream][11960])
    * <https://github.com/vidonme/xbmc/> Sources of [VidOn.Me Player][11961]? Seems to be a fork from empatzero. ([Diff to upstream][11962] and [Github Compare][11963]) This repo is reported from VidOn.me to be the "official" source code for their Allwinner XBMC version, yet the only code commit from VidOn.me themselves is [this one][11964].
  * <https://github.com/huceke/xbmc/tree/allwinner> Gimli's implementation ([Diff to upstream][11965])

# See also
  * [CedarX][11916] \- Library for Allwinner CedarX VPU (Video Processor Unit) used for audio and video decoding and encoding hardware off-loading on A1x and A2x SoC series. 
    * [CedarXVideoRenderingChart][11966] \- Overview chart of working/ non working video files
  * [LIRC (Linux Infrared Remote Control) for IR receivers and and remotes][11957]
  * [Tvheadend TV Tuner Server and PVR backend][11967]

# xternal Links
  * <http://kodi.tv> \- Kodi.tv the official Kodi/XBMC website with wiki and forums. 
    * <http://github.com/xbmc/xbmc/> \- The upstream Kodi mainstream source code repository on GitHub.
  * [XBMC Official Community Forum discussion about porting to Allwinner A10][11968]
  * [Jas Hacks Hackberry A10 - XBMC on Ubuntu 12.10 image][11969]
  * [Buildroot XBMC on the Mele A1000 (Allwinner A10)][11970]
  * [XBMC for Linux on AllWinner A10 Devices? It Works! (Sort of)][11971]

# References
  1. [↑][11972] <http://www.j1nx.nl/buildroot-xbmc-on-mele-a1000-allwinner-a10/> Buildroot XBMC on the Mele A1000 (Allwinner A10)
  2. [↑][11973] <http://www.cnx-software.com/2012/11/12/xbmc-for-linux-on-allwinner-a10-devices-it-works-sort-of/> XBMC for Linux on AllWinner A10 Devices? It Works! (Sort of)
