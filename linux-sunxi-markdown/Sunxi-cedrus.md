# Sunxi-Cedrus
(Redirected from [Sunxi-cedrus][52005])
 
Sunxi-Cedrus is an effort to bring hardware-accelerated video decoding and encoding support for Allwinner SoCs to the **mainline** Linux kernel. Additional userspace components that interface with the kernel driver are also provided, for typical GNU/Linux-based systems. 
## Contents
  * [1 Components][52008]
  * [2 Status][52009]
    * [2.1 Codec Support][52010]
    * [2.2 SoC Support][52011]
    * [2.3 Player Support][52012]
  * [3 Installation][52013]
    * [3.1 Linux][52014]
    * [3.2 libva-v4l2-request][52015]
    * [3.3 libdrm-sun4i][52016]
    * [3.4 v4l2-request-test][52017]
    * [3.5 libva-dump][52018]
  * [4 Usage and Configuration][52019]
    * [4.1 System][52020]
    * [4.2 VLC][52021]
      * [4.2.1 Examples][52022]
    * [4.3 v4l2-request-test][52023]
      * [4.3.1 Examples][52024]
  * [5 Current Development][52025]
    * [5.1 2019.03 Release][52026]
    * [5.2 2018.07 Release][52027]
      * [5.2.1 Known Limitations][52028]
    * [5.3 Weekly Reports][52029]
  * [6 Community][52030]
  * [7 Past Development][52031]
    * [7.1 Installation][52032]
    * [7.2 Supported features][52033]
    * [7.3 Known bugs and limitations][52034]
    * [7.4 Technical details and implementation][52035]
    * [7.5 More info][52036]

## Components
Support for Sunxi-Cedrus is implemented through various components, either in kernel space or userspace: 
  * the **Cedrus V4L2 M2M kernel driver**
  * the **v4l2-request VAAPI backend**

Additional userspace components are also available, for development purposes: 
  * the **v4l2-request-test** standalone tool, that allows testing the -Cedrus VPU driver
  * the **sun4i-specific libdrm** , with support for allocating buffers in the MB32-tiled NV12 format used by the VPU
  * the **dump libVA backend** , that allows dumping metadata and slices from videos

Video players that support libVA should be compatible with the v4l2-request libVA backend. However, details in implementations might result in incompatibility with certain players. See [Player Support][52012] for the status of tested players. 
## Status
### Codec Support
Support status for specific codecs in the v4l2-request **libVA backend** is presented in the following table: 
Codec  | Decoding  | Encoding   
---|---|---  
**MJPEG** | Missing  | Missing   
**MPEG2** | Supported  | N/A   
**MPEG4** | Missing  | N/A   
**VP6** | Missing  | N/A   
**H264** | Supported (early high profile)  | Missing   
**VP8** | Supported (since Linux 5.11)  | N/A   
**H265** | Supported (early)  | N/A   
**VP9** | Missing  | N/A   
### SoC Support
Support for specific SoCs in the **V4L2 M2M kernel driver** is presented in the following table: 
Platform  | Cedrus Driver Status  | DRM Planes Status   
---|---|---  
**A10** | Supported (5.1)  | Supported (5.1)   
**A13/A10s** | Supported (4.20)  | Missing (broken)   
**A20** | Supported (4.20)  | Supported (5.1)   
**A23** | Untested  | Untested   
**A33** | Supported (4.20)  | Supported   
**A64** | Supported (5.0)  | Supported   
**H3** | Supported (4.20)  | Supported   
**H5** | Supported (5.0)  | Supported   
**H6** | Supported (5.1)  | Supported (5.0)   
**H616** | Untested  | Untested   
**R40** | Supported (5.10)  | Untested   
**V3/V3s** | Untested  | Untested   
### Player Support
The following players were tested with the v4l2-request **libVA backend** : 
Player  | X11 Status  | EGL/GLES Status  | DRM Hardware Plane Status  | X11/Xv Hardware Plane Status   
---|---|---|---|---  
**VLC** | Supported  | Missing (broken)  | N/A  | Missing   
**GStreamer** | Missing (broken)  | Untested  | Untested  | Untested   
**MPV** | Missing (broken)  | Missing  | Missing  | Missing   
**Kodi (downstream)** | Untested  | Missing (broken)  | Supported  | N/A   
## Installation
### Linux
The first step to installing Cedrus support is to build a Linux kernel with the latest patch series for the driver. A tree with all the required patches is available at: 
  * Repository: <https://github.com/bootlin/linux-cedrus>
  * Tag: **release-2019.03**

The following kernel configuration options must be selected: 
[code] 
    CONFIG_MEDIA_SUPPORT
    CONFIG_MEDIA_CONTROLLER
    CONFIG_MEDIA_CONTROLLER_REQUEST_API
    CONFIG_V4L_MEM2MEM_DRIVERS
    CONFIG_VIDEO_SUNXI_CEDRUS
    
[/code]
In addition, the target device must contain the proper description for **display engine support in its device-tree source**. 
Details about building a mainline Linux kernel are available on the [Mainline Kernel Howto][52037] page. 
Note that the **associated kernel headers must be installed to the target device** for the userspace components to build. 
Decoding H.264/H.265 videos can require a large amount of CMA memory, so it is recommended to set a large CMA pool, e.g. using the `cma` kernel command line parameter. For instance, 256 MiB should be enough to decode 1080p H.264 videos: `cma=256M`. 
The first mainline kernel release containing Cedrus support is 4.20 (scheduled for release December 2018 or Jan 2019). Newer Cedrus code is available in the bootlin git repository linked above. 
### libva-v4l2-request
The main userspace component that supports the Cedrus VPU driver is the libva-v4l2-request VAAPI backend. It is available at: 
  * Repository: <https://github.com/bootlin/libva-v4l2-request>
  * Tag: **release-2019.03**

The backend can be **built and installed on the target device** by following these steps: 
[code] 
    git clone https://github.com/bootlin/libva-v4l2-request -b release-2019.03
    cd libva-v4l2-request
    ./autogen.sh && make && sudo make install
    
[/code]
**Note:** release-2019.03 of libva-v4l2-request may not build with newer kernel i.e. Linux 6.x. But LibreELEC supports sunxi VPU hardware decoding (i.e. LibreELEC 12.0), with v4l2-request patches in ffmpeg and kernel. 
Hardware decoding in Kodi can be checked by pressing key O during video playing to activate Player Process Information OSD. See <https://kodi.wiki/view/Player_process_info#Player_Process_Info>
### libdrm-sun4i
**This is deprecated and no longer needed for other components to build.**
libdrm-sun4i imports the updated sun4i-drm Linux kernel driver definitions for installation in userspace and is available at: 
  * Repository: <https://github.com/bootlin/libdrm-sun4i.git>
  * Branch: **master**

It can be **built and installed on the target device** through the following steps: 
[code] 
    git clone https://github.com/bootlin/libdrm-sun4i
    cd libdrm-sun4i
    ./autogen.sh --prefix=/usr && make && sudo make install
    
[/code]
Alternatively to building libdrm-sun4i, the `sun4i_drm.h` file can be placed into `/usr/include/drm` directly. 
### v4l2-request-test
The v4l2-request-test tool is available at: 
  * Repository: <https://github.com/bootlin/v4l2-request-test.git>
  * Tag: **release-2019.03**

It can be **built on the target device** through the following steps: 
[code] 
    git clone https://github.com/bootlin/v4l2-request-test.git -b release-2019.03
    cd v4l2-request-test
    make
    
[/code]
### libva-dump
The libva-dump VAAPI backend is available at: 
  * Repository: <https://github.com/bootlin/libva-dump.git>
  * Branch: **master**

It can be **built on the host or the target device** through the following steps: 
[code] 
    git clone https://github.com/bootlin/libva-dump.git
    cd libva-dump
    ./autogen.sh && make && sudo make install
    
[/code]
## Usage and Configuration
### System
In order to access the device nodes created by the Cedrus kernel driver, the user that will be decoding videos needs to be added to the `video` group. 
Alternatively, the permissions of the `/dev/video0` and `/dev/media0` nodes can be changed to allow access by this user. 
### VLC
In order to use VLC with Cedrus, the libva-v4l2-request VAAPI backend must be installed on the system. VLC must also be configured to use VAAPI for video decoding, through the following menus: 
  * `Tools > Preferences > Input / Codecs > Codecs > Hardware-accelerated decoding > VA-API video decoder`
  * `Tools > Preferences > Video > Display > Output > X11 video output (XCB)`

While OpenGL video output might be supported (with GPU support installed), it was not tested at this point. 
Although VLC has been configured to use VAAPI for video decoding, libVA must be instructed to use libva-v4l2-request through the `LIBVA_DRIVER_NAME` environment variable : 
[code] 
    export LIBVA_DRIVER_NAME=v4l2_request
    vlc path/to/video.mpeg
    
[/code]
#### Examples
Here are some examples of VLC usage for specific use cases: 
  * Remote testing without audio, scaling and OSD:

[code] 
    export LIBVA_DRIVER_NAME=v4l2_request
    export DISPLAY=:0
    vlc --no-audio --no-autoscale --no-osd --play-and-exit path/to/video.mpeg
    
[/code]
### v4l2-request-test
v4l2-request-test is preferably used from its repository directory: the default path to the video slices is relative from the root of the repository. Since the tool uses the DRM KMS device directly, no graphical session (not even a login manager) must be running concurrently. 
The tool currently contains a single preset with slices that allow decoding the first 25 frames of the sample MPEG2 Big Buck Bunny video. More presets can be added from the data dumped with libva-dump. v4l2-request-test usage is displayed when the tool is called with the `-h` argument. 
#### Examples
Examples of v4l2-request-test use include: 
  * Decoding frames at 25 fps in a loop, with information:

[code] 
    ./v4l2-request-test -f 25 -l
    
[/code]
  * Decoding frames as fast as possible in a loop:

[code] 
    ./v4l2-request-test -ql
    
[/code]
  * Specifying the right nodes when another V4L2 driver is loaded:

[code] 
    ./v4l2-request-test -v /dev/video1 -m /dev/media1
    
[/code]
## Current Development
From March to August 2018, the development of both the Cedrus V4L2 kernel driver and the Cedrus libVA backend was undertaken by: 
  * **Paul Kocialkowski** , intern at Bootlin
  * **Maxime Ripard** , engineer at Bootlin

This effort was funded by the [related crowdfunding][52038] started by Bootlin in February 2018. 
### 2019.03 Release
A second release of Cedrus was packed in March 2019, following up on numerous interface changes and new platforms support. 
The source code for the required components of the release are available on Bootlin's GitHub space, with the `release-2019.03` tag: 
  * [linux-cedrus][52039]
  * [v4l2-request-test][52040]
  * [libva-v4l2-request][52041]

### 2018.07 Release
A first release of Cedrus was presented in July 2018, with an [associated blog post on the Bootlin blog][52042]. 
The source code for the required components of the release are available on Bootlin's GitHub space, with the `release-2018.07` tag: 
  * [linux-cedrus][52043]
  * [v4l2-request-test][52044]
  * [libva-v4l2-request][52045]
  * [Kodi][52046]
  * [LibreELEC][52047]

A root filesystem tarball built from the LibreELEC release, which includes Kodi and libva-v4l2-request, is also available (with a checksum and a detached GPG signature): 
  * [LibreELEC-cedrus-release-2018.07.tar.gz][52048], ([LibreELEC-cedrus-release-2018.07.tar.gz.sha512sum][52049], [LibreELEC-cedrus-release-2018.07.tar.gz.asc][52050])

The root filesystem includes neither boot software nor kernel support: both have to be installed in addition to extracting the filesystem on the target medium. Instructions to build the kernel are available at: [#Linux][52014]
#### Known Limitations
Some limitations in the software present in the release are known and listed as follows: 
  * Decoding H264 videos (especially in high resolutions) may consume more memory than there is available in the dedicated pool. This is because Kodi does not yet interact properly with VAAPI when freeing buffers. The result is that Kodi will hang or display a fully black video.

### Weekly Reports
Reports on the advancement of the development of Sunxi-Cedrus are posted regularly on the [Bootlin Blog][52051], starting week 10 of 2018: 
  * [Week 35 Final Status Update][52052]
  * [Week 34 Status Update][52053]
  * [Week 33 Status Update][52054]
  * [Week 32 Status Update][52055]
  * [Week 31 Status Update][52056]
  * [Week 30 Status Update][52057]
  * [Delivery of Allwinner VPU driver main goals][52058]
  * [Week 28 Status Update][52059]
  * [Week 27 Status Update][52060]
  * [Week 26 Status Update][52061]
  * [Week 25 Status Update][52062]
  * [Week 24 Status Update][52063]
  * [Week 23 Status Update][52064]
  * [Week 22 Status Update][52065]
  * [Week 21 Status Update][52066]
  * [Week 20 Status Update][52067]
  * [Week 19 Status Update][52068]
  * [Week 18 Status Update][52069]
  * [Week 17 Status Update][52070]
  * [Week 16 Status Update][52071]
  * [Week 15 Status Update][52072]
  * [Week 14 Status Update][52073]
  * [Week 13 Status Update][52074]
  * [Week 12 Status Update][52075]
  * [Week 11 Status Update][52076]
  * [Week 10 Status Update][52077]

## Community
The community revolving around Sunxi-Cedrus can be contacted through different means: 
  * The [linux-sunxi mailing list][52078], with the developers involved in carbon copy
  * The **#cedrus** channel on the [freenode][52079] IRC network

## Past Development
Initial work on the Sunxi-Cedrus V4l2 kernel driver and libVA backend was carried out by **Florent Revest** (kido) during an internship at Bootlin (formerly Free Electrons), resulting in a proof-of-concept driver and associated backend with MPEG2 and partial MPEG4 support for the A13 SoC. 
If you want to try it, you need a board with an A13 SoC, this page will try to guide you from your first steps with the driver to the details of its implementation. Make sure you've checked the known bugs and limitations before using it. 
### Installation
This procedure has been tested on the NextThingCo's CHIP board but should be adaptable to other A13 boards supported by the 4.8 mainline kernel. The first thing you need to do is to recompile a kernel with the sunxi-cedrus v4l driver and the corresponding device tree entry. You can follow the [Mainline Kernel Howto][52037] but using the following repository: 
[code] 
    https://github.com/FlorentRevest/linux-sunxi-cedrus
[/code]
Use menuconfig to enable the VPU driver in Device Drivers -> Multimedia support -> Memory-to-memory multimedia devices -> Sunxi CEDRUS VPU driver. The driver should be compiled into the kernel and not as a module. 
Your kernel will be located in arch/arm/boot/zImage and device tree in arch/arm/boot/dts/sun5i-r8-chip.dtb Don't forget to install kernel headers to your distribution if you want to be able to compile sunxi-cedrus-drv-video. 
On a standard debian jessie system you will need to install the following build dependencies: 
[code] 
    apt install git autoconf automake libtool pkg-config gcc libdrm-dev libva-dev libx11-dev make g++ vlc xorg
[/code]
You will be able to compile and install a newer version of libVA supporting the LIBVA_DRIVER_NAME environment variable and then the sunxi-cedrus libVA backend: 
[code] 
    git clone https://github.com/01org/libva
    cd libva
    git checkout 695f99ef0405cf4255e7767b44effb0da2fe706e
    ./autogen.sh --prefix=/usr --libdir=/usr/lib/arm-linux-gnueabihf/
    make
    sudo make install
[/code]
[code] 
    git clone https://github.com/FlorentRevest/sunxi-cedrus-drv-video
    cd sunxi-cedrus-drv-video
    ./autogen.sh
    make # DRM_CFLAGS=-I/path/to/your/linux/headers
    sudo make install
[/code]
Once installed, make sure you've exported the environment variable telling VA to use the sunxi_cedrus backend, activate the VA X11 decoding in VLC settings (Tools -> Preferences -> Input / Codecs -> set 'Hardware-accelerated decoding' to 'VA-API video decoder via X11') and then run one of the sample media file you can find [here][52080] and [here][52081]
[code] 
    xinit&
    export DISPLAY=:0.0
    export LIBVA_DRIVER_NAME=sunxi_cedrus
    vlc big_buck_bunny_480p_MPEG2_MP2_25fps_1800K.MPG
    vlc ducks_take_off_420_720p25.mp4
[/code]
### Supported features
  * MPEG2 Decoding
  * Partial MPEG4 Decoding

### Known bugs and limitations
  * H264 and H265 are not supported (some of the underlying problems include: allocating 19 surfaces at once and queueing several slices by frames)
  * MPEG4 decoding has some glitches. When something moves in a video it usualy draws some kind of trace behind it, this behavior is believed to come from an inconsistency in movement prediction. (VLC also tries to SyncSurface more often than needed which results in error when dequeuing the capture buffers)
  * No encoding: this can be added later on but hasn't been tried yet
  * Direct rendering: currently, buffers coming out of the v4l driver in a tiled pixel format are converted to a standard YUV pixel format and then rendered on screen by ffmpeg/vlc. As soon as the support for YUV DRM planes will be added to the kernel, this behavior can be replaced and the performances will be much better.
  * Currently the video can only be played at a zoom of 1:1, otherwise the scaling is done by ffmpeg in full CPU and it is too slow. Having that in the DRM driver would also allow for hardware accelerated frames scaling.
  * We currently can't play a MPEG2 file and then a MPEG4 file (or vice versa) or the output will be full of garbage pixels. This is probably due to some registers of the MPEG engine being kept between the two decoding and "polluting" the MPEG4 decoding with older values from MPEG2 decoding. We should find a way to clear those registers when receiving a S_FMT ioctl in the kernel driver or when closing the video device.

### Technical details and implementation
The Cedrus project has provided reverse engineering of the Allwinner's proprietary [CedarX][52082] blob for a couple of years. This work has been done on the Allwinner's 3.4 kernel and led to the creation of a libVDPAU backend interfacing with the "cedar_dev" and "disp" kernel drivers available in the vendor's kernel. The "cedar_dev" kernel driver directly mapped registers and memory from the [ VE][52083] to the userspace and could potentially be a security risk. Those two drivers couldn't be upstreamed because they don't use any standard API or framework. 
In order to use the [ VE][52083] on a mainline kernel, a new proper kernel driver had to be written from scratch with mainlinable methods in mind. The correct way to implement a codec device is to use the "video4linux" framework, referenced as v4l2. v4l2 handles many kind of video devices, some of them are cameras and sends data to a CAPTURE queue, others are screens and use data from an OUTPUT queue. Codec devices require a flow of data from OUTPUT to CAPTURE, they are "memory-to-memory" devices. 
Until now, most of the codec devices were able to handle raw bitstream via a firmware, which means that the OUTPUT queue (containing the compressed input data) could directly contain a MPEG file and the CAPTURE queue was filled with video frames. But the inner working of Allwinner's VPU is different, indeed it requires prior bitstream parsing into smaller frames/slices alongside headers' data. This parsing can not be done in the kernel side since it would be a complex codebase to maintain so it requires a new user-space usecase, hence a new API. 
The "Frame API" described [here][52084] has been designed for the Rockchip's VP8 decoding support and is implemented [here][52085] and [here][52086] The "Frame API" aims to standardize the way VPU drivers should communicate frame by frame with the userspace. The advocated method is to bind "buffers" containing slice data from the OUTPUT queue to "extended controls" containing frame's header. The extended controls mechanism allows to send complex data structures to the kernel and program device's registers accordingly. However, the userspace might want to queue several frames in a row and set the corresponding extended controls at the same time. If the registers are programmed at the time an extended control is received, this means that at the time of processing a buffer, the registers might be programmed for another frame. This scenario is to be fixed by the "Request API". 
The idea behind this API is to allow atomic operations like a QBUF and a S_EXT_CTRLS. As of August 2016, the "Request API" is still at the state of RFC, it has had quite a few proposals for the past few years but none of them got accepted into the kernel. [The latest RFCs][52087], related to the Media API are not able to handle controls so sunxi-cedrus had to use an [older RFC.][52088]
The "sunxi-cedrus" kernel driver is hence made of a m2m v4l2 driver handling requests of MPEG2 or MPEG4 frames data with a standard header extended control. At the time of processing the m2m queue, it programs the VPU's registers depending on the used codec. Currently [MPEG2][52089] and [MPEG4][52090] are the only supported formats but H264 and H265 would be the next step. 
A second limitation of the Allwinner's VPU is the need for buffers in the lower 256M of RAM. In order to allocate large sets of data in this area, "sunxi-cedrus" [reserves a DMA pool][52091] that is then used by videobuf's dma-contig backend() to allocate input and output buffers easily and integrate that with the v4l QBUF/DQBUF APIs. 
From the userspace side of things, all the prior bitstream parsing is done by VA users(such as ffmpeg). Standard VA-API headers are given to the VA backend "sunxi-cedrus-drv-video" which is just in charge of ensuring a correspondence between v4l2 buffers and controls and VA structures. We can compare a VAPicture to a buffer plus an extended control in the OUTPUT queue and a VASurface to a multiplanar buffer in the CAPTURE queue. An Image is then "derived" from a Surface to produce a standard set of NV12 buffers that can be shown on screen by VLC for example. VA-API was an extremely appropriate choice compared to VDPAU since the data it provides are often very similar to the ones the VPU expects. 
### More info
You can HL Florent Revest (kido) on #cedrus on irc.freenode.net for in depth questions
