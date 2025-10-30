# Cedrus/libvdpau-sunxi
< [Cedrus][12260]
 
[![MBOX icon edit-clear.png][12263]][12264] | **This page is kind of outdated and needs a cleanup.** Prerequisites, the OSD part and memory reservation have changed a bit with the last few commits. See the [README][12265] in the meantime.   
---|---  
## Contents
  * [1 Overview][12266]
  * [2 Installation][12267]
    * [2.1 Prerequisites][12268]
    * [2.2 Reserve memory for the VPU][12269]
    * [2.3 Cedar module][12270]
      * [2.3.1 Write access persmissions][12271]
    * [2.4 Installing libvdpau-sunxi library][12272]
      * [2.4.1 Prerequisites][12273]
      * [2.4.2 Compiling source][12274]
    * [2.5 Playing video][12275]
    * [2.6 OSD support][12276]

## Overview
[libvdpau-sunxi][12265] is a vdpau driver backend implementation for the [vdpau framework][12277]. 
[Cedrus/libvdpau_integration_matrix ][12278] gives an overview about the VDPAU API functions currently supported in libvdpau-sunxi. It also lists the required functions for various programs. 
## Installation
[![MBOX icon important.png][12279]][12280] | **SECURITY NOTE** : Currently the open source driver is implemented as replacement of the blob. Blob and current open source replacement driver (libvdpau-sunxi) use Allwinner's kernel driver that remaps registers for use in userspace, with Allwinner's display driver used for hardware overlay. Together with access to physical memory, and dangerous VE DMA ability it makes a serious security problem. That should be replaced in a proper way in ongoing mainline process.   
---|---  
### Prerequisites
Various things are required to get cedrus to play back video. This list can act as a quick start. 
  * [Proper memory reservation][12281]
  * cedar module either compiled in or the module loaded
  * write access permissions on /dev/disp and /dev/cedar_dev

    
  * on A10/A20, A13, add /dev/g2d for osd
  * on A33 or H3, add /dev/ion

  * libvdpau-sunxi library installed
  * enviroment variable telling libvdpau which library to use

### Reserve memory for the VPU
The VE needs a block of memory to store (de)coded frames in. The kernel needs to be informed about this before booting. To do so, the kernel command line needs to be modified. This can be done at compiletime or by modifying the bootloaders [Kernel_arguments][12282]. By default Allwinner reserves 80 Megabytes but depending on the player being used and video being decoded, less can suffice or more can be necessary. Feel free to experiment with the amount, but if available, 128 MiB is a nice number to test things with. This can be set by the following kernel argument. 
[code] 
    sunxi_ve_mem_reserve=128
[/code]
**NOTE:** This kernel parameter is ignored in recent linux-sunxi 3.4 kernels, if CMA is enabled in kernel configuration. If CONFIG_CMA=y, ve_size is hardcoded to 80MB in sunxi_cedar kernel module. 
For A33 or H3, if you use the kernel from official SDK, you should modify the memory reservation configuration of ion memory allocator. 32 MB seems to be enough for 720p H.264 decoding, and 64MB is enough for 1080p H.264 decoding. 
### Cedar module
Depending on where the kernel came from, the Cedar kernel driver is either available as module or built in. To see whether it is available, check whether /dev/cedar_dev exists. If not, run _modprobe sun4i_cedar_dev_ (in future versions this should be called sunxi_cedar_dev, and for official kernel of A33 or H3 it's called cedar_dev). There should now be a /dev/cedar_dev. 
#### Write access persmissions
To be able to pass data to the VE, proper permission to /dev/cedar_dev is required. 
For testing, manually setting permissions is fine. 
[code] 
    chown <username>:<usergroup> /dev/cedar_dev
    chmod 666 /dev/cedar_dev
[/code]
The VE only decodes the video codec. To have it appear on the display, write access permission to /dev/disp is required. 
[code] 
    chown <username>:<usergroup> /dev/disp
    chmod 666 /dev/disp
[/code]
For the official kernel of A33 or H3, cedar do not allocate memory by itself, but it uses ion. So for these devices, write and read permission to /dev/ion is needed. 
[code] 
    chown <username>:<usergroup> /dev/ion
    chmod 666 /dev/ion
[/code]
To do this properly with udev rules, create files for each under /etc/udev/rules.d/ 
50-disp.rules 
[code] 
    KERNEL=="disp", MODE="0660", GROUP="video"
[/code]
50-cedar.rules 
[code] 
    KERNEL=="cedar_dev", MODE="0660", GROUP="video"
[/code]
50-ion.rules 
[code] 
    KERNEL=="ion", MODE="0660", GROUP="video"
[/code]
### Installing libvdpau-sunxi library
There are currently no pre-compiled binaries available and have to be compiled from source. This most likely has to be performed on the target device, while possible to be cross compiled. 
#### Prerequisites
  * git (yum install git | apt-get install git | emerge git)
  * gcc (yum group-install "Development Tools" | apt-get install build-essential)
  * pkg-config (apt-get install pkg-config)
  * libvdpau-dev >= 1.1 (yum install libvdpau-dev | apt-get install libvdpau-dev | emerge libvdpau) or build from [source][12283]
  * libcedrus (<https://github.com/linux-sunxi/libcedrus>)
  * pixman (<http://www.pixman.org>)

#### Compiling source
The current libvdpau-sunxi code is stored on github. 
[code] 
    git clone https://github.com/linux-sunxi/libvdpau-sunxi.git
    cd libvdpau-sunxi
    make
    sudo make install
[/code]
Pay close attention as to where these libraries get installed. Depending on the distro in use, it's most likely they will need to be put in **/usr/lib/vdpau**. If they are not put there, manually copy them there. With the driver now installed, it is important to tell vdpau to use this library. By default it will try to load and use the nVidia vdpau implementation. 
[code] 
    export VDPAU_DRIVER=sunxi
[/code]
The latest git version of [Xorg#fbturbo_driver][12284] can report the DRI2 VDPAU name as 'sunxi', if 'sunxi_cedar_mod' kernel module loaded successfully. See [commit][12285]
### Playing video
With everything setup properly, it should now be possible to playback hardware accelerated media! 
The best test file would be one of the well known sample media's. The big buck bunny is an often used one. <http://samplemedia.linaro.org/H264/big_buck_bunny_1080p_H264_AAC_25fps_7200K.MP4>
Depending if you use mpv or mplayer2, the following options are required. For mplayer2: 
[code] 
     mplayer -vo vdpau -vc ffmpeg12vdpau,ffh264vdpau, [filename]
[/code]
For mpv: 
[code] 
     mpv --vo=vdpau --hwdec=vdpau --hwdec-codecs=all [filename]
[/code]
Note: There have been reports that some mplayer versions in certain repositories are not compiled with vdpau support. 
Now you can also try to use other files, but note it has to be mpeg1, mpeg2 or h264 encoded! 
### OSD support
We have simple OSD implementation, either using G2D hardware acceleration (on A10/A20) or CPU via pixman (on newer SoCs lacking G2D). 
Access to G2D is also required. 
[code] 
    chmod 666 /dev/g2d
[/code]
To do this properly with udev rules, create a file under /etc/udev/rules.d/ 
50-g2d.rules 
[code] 
    KERNEL=="g2d", MODE="0660", GROUP="video"
[/code]
and make sure that the user wanting to decode video is in the video group! 
To turn on OSD support during runtime: 
[code] 
    export VDPAU_OSD=1
[/code]
  
Note: mplayer's "-ass" osd not currently supported, due to lack of 'alpha only' surfaces support in current G2D driver
