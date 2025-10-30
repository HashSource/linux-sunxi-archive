# CedarX/libve
< [CedarX][12005]
 
## Contents
  * [1 Introduction][12008]
  * [2 Using the native Linux library][12009]
  * [3 Using libhybris wrapped Android libraries][12010]
    * [3.1 Testing libhybris wrapped Android libraries with VLC][12011]
    * [3.2 Testing libhybris wrapped Android libraries with XBMC][12012]
    * [3.3 Having problems with the Android libraries?][12013]

# Introduction
libve is a small proprietary library, which is providing the core of [CedarX][12005] video decoding functionality. There is some documentation about the use of libve API here [[1]][12014]. Also the sources of [CedarX/VLC][12015] and [CedarX/XBMC][12016] media players can be used as examples. 
# Using the native Linux library
There is a Linux armhf blob available at [[2]][12017] (af9caeac58876819623e8e7ac3ee19798079a102 libvecore.so). Unfortunately it has little practical value because of a serious decoding bug: <https://github.com/linux-sunxi/cedarx-libs/issues/1>
A good example of a file triggering this bug is Sintel trailer: <http://download.blender.org/durian/trailer/sintel_trailer-1080p.mp4>
But don't lose your hope yet and move on to the next section. 
# Using [libhybris][12018] wrapped Android libraries
First we need to get access to the Android /system directory with the required Android libraries. 
One way to do this is just by simply mounting this directory for the vendor provided Android firmware in NAND. But make sure that a recent Android firmware is used (unfortunately ABI keeps changing between releases). This method was successfully tested on Mele A2000 with Mele_HTPC_20130116_V1.3.1.img vendor provided firmware [[3]][12019]. 
[code] 
      mkdir /system
      mount /dev/nandd /system
    
[/code]
An alternative method can be used in the case if your Android blobs are not compatible (cause crashes) or you don't have Android in NAND in the first place. It is possible to build Android from sources for cubieboard (or some other Allwinner A10 hardware) using the instructions from <http://martinbrook.blogspot.fi/2013/04/adventures-with-libhybris-and-andriod.html>. For convenience, a minimal set of pre-built libraries can be obtained by using the following instructions: 
[code] 
      cd /
      wget <http://people.freedesktop.org/~siamashka/files/20130509/system.tar.gz>
      tar -xzf system.tar.gz
      cd /system/lib
      wget <https://github.com/allwinner-dev-team/android_external_cedarx/raw/ef36cd760e9d76a2/CedarAndroidLib/LIB_JB_F23/libcedarv_adapter.so>
      wget <https://github.com/allwinner-dev-team/android_external_cedarx/raw/ef36cd760e9d76a2/CedarAndroidLib/LIB_JB_F23/libcedarv_base.so>
      wget <https://github.com/allwinner-dev-team/android_external_cedarx/raw/ef36cd760e9d76a2/CedarAndroidLib/LIB_JB_F23/libcedarxosal.so>
      wget <https://github.com/allwinner-dev-team/android_external_cedarx/raw/ef36cd760e9d76a2/CedarAndroidLib/LIB_JB_F23/libve.so>
    
[/code]
Then we need to compile and install libhybris with CedarX libve patches (to some directory of your choice, but *not* into /usr because it would clash with GLESv2 Mali libraries): 
[code] 
      git clone -b cedarx <git://github.com/ssvb/libhybris.git>
      cd libhybris/hybris
      ./autogen.sh --prefix=/usr/local/hybris
      make
      make install
    
[/code]
That's all. Now you should have /usr/local/hybris/lib/libvecore.so library, which is a drop-in replacement for the native libvecore.so 
## Testing libhybris wrapped Android libraries with [VLC][12020]
The VLC test itself can be done with: 
[code] 
      export LD_LIBRARY_PATH=/usr/local/hybris/lib
      wget <http://download.blender.org/durian/trailer/sintel_trailer-1080p.mp4>
      ./cvlc --demux ffmpeg --codec cedar --vout cedarfb --no-osd sintel_trailer-1080p.mp4
    
[/code]
The Sintel trailer video used in this example normally triggers severe decoding bugs in the native Linux blob. With the libhybris wrapped and loaded Android blobs this video should play perfectly fine. 
## Testing libhybris wrapped Android libraries with XBMC
First replace libvecore.so with a symlink to the libhybris wrapper: 
[code] 
      cd /allwinner/xbmc-pvr-binhf/lib
      mv libvecore.so libvecore.so.old_native_linux_blob
      ln -s /usr/local/hybris/lib/libvecore.so libvecore.so
    
[/code]
Then run XBMC: 
[code] 
      cd /allwinner/xbmc-pvr-binhf/lib/xbmc
      ./xbmc.bin
    
[/code]
## Having problems with the Android libraries?
~~Please report them to<https://github.com/ssvb/libhybris/issues> ~~
~~Note: please only report the cases when libhybris wrapped Android libraries work worse than the native Linux library (otherwise it is unlikely to have anything to do with the libhybris wrapper). Also don't forget to describe the steps needed to reproduce the issue, some information about the video player (VLC or XBMC) and a link to the sample file causing problems.~~
The promise to debug issues in the libhybris libve wrapper has already expired and it is not maintained anymore. Please consider using <https://github.com/linux-sunxi/libvdpau-sunxi> as a solution for hardware accelerated video decoding.
