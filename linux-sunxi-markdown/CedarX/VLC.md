# CedarX/VLC
< [CedarX][11818]
 
[![MBOX icon deletion.png][11821]][11822] | **The content of this page is obsolete and its use is not recommend.** This instructions of how to build and use are based in a VLC fork which is not in active development (older more than 4 years from last activity). The added support depends in an very old version of the binary libraries, that are incompatible with the _frequent_ API changes of newer versions of [CedarX][11818] binary libraries.   
---|---  
[![MBOX icon important.png][11823]][11824] | **For how to use[VLC][11825] in sunxi, please see the [VLC main page][11825].**  
---|---  
VLC also known as "_VideoLAN Client_ " player is a open-source cross-platform video player. For more info check the wikipedia. 
VLC support for [CedarX][11818] was added by Wills Wang. VLC support and especially this page is work in progress. 
# Compilation
In building tree, the default libvecore.so is armhf version, it come from [here][11826]
If you use armel, you need replace it with [this version][11827]
Build libcedarx at first, do: 
[code] 
    git clone https://github.com/willswang/libcedarx
    cd libcedarx
    ./autogen.sh
    ./configure --host=arm-linux-gnueabihf --prefix=<your installation path>
    make
    make install
    
[/code]
If the above fails at autogen.sh, be sure to install libtools. 
[code] 
    apt-get install libtool
    
[/code]
Build vlc with cedar support, do: 
[code] 
    apt-get build-dep vlc #only once, both target and host rootfs
    apt-get remove lua5.2 # may not be needed on your system, you must use lua 5.1 to build vlc
    git clone https://github.com/willswang/vlc
    cd vlc
    ./bootstrap
    ./configure --host=arm-linux-gnueabihf --prefix=<your installation path> --enable-cedar
    make
    make install
    
[/code]
If you dont want to cross-compile, remove --host, set prefix to /usr and compile on device, compilation time is around one and a half hours. 
# Usage
Give everyone rights to use disp and [CedarX][11818]
[code] 
    chmod 777 /dev/disp
    chmod 777 /dev/cedar_dev
    
[/code]
Start vlc with command line interface: 
[code] 
    cvlc --demux ffmpeg --codec cedar --vout cedarfb --no-osd <media file>
    
[/code]
You can use standard cvlc hotkeys, but remember that there is no OSD support yet. 
# Problems/TODO
  * Is fb0_scaler_mode_enable/fb1_scaler_mode_enable needs to be disabled for cedarfb?
  * No output modules support apart from cedarfb which uses raw framebuffer access (not compatible with xf86-video-mali and any other driver/device that wants to write raw at the same moment).
  * No support for GUI of the VLC, only command line VLC is supported
  * 1080p and such movies with high bitrate sometimes buffer too slow and frames are dropping.
  * No support for OSD because of lack of YUV420
