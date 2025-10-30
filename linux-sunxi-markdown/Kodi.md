# Kodi
**[Kodi][29625]** (formerly _XBMC_) is a popular free and open source (GPL) software media center for playing videos, music, pictures, games and more.  

This article contains some background you need to know, when you are planning to get Kodi running on your Allwinner SoC.  
**It's important to be aware of the history of XBMC on sunxi devices and the history of CedarX code in general, as well as the position of Allwinner, Team-Kodi and the linux-sunxi community.**
## Contents
  * [1 History][29626]
  * [2 Linux-sunxi community][29627]
  * [3 Technical overview][29628]
    * [3.1 Video engine kernel driver][29629]
    * [3.2 Sunxi display driver][29630]
    * [3.3 Mali (3D) kernel driver + userspace library][29631]
    * [3.4 Support for sunxi in Kodi][29632]
  * [4 Kodi via libvdpau-sunxi][29633]
  * [5 Alternative media players][29634]
  * [6 Conclusion][29635]
  * [7 References][29636]

# History
In history (since 2012), there have been a bunch of solutions (e.g. empat0, gimli) to get Kodi running on Allwinner SoCs using the closed sourced libraries from Allwinner (provided via the initial makers of cubieboard) for hardware accelerated video decoding. One problem of these implementation is, that these closed source libs have bugs in their linux version. Using the android version via libhybris solves this bug. The GPL issue still remaines.  

**Team-Kodi** , the official development team of Kodi, negotiated support due to lack of resources and - the more important reason - the fact, that Allwinner was [violating the GPL][29637] with these binaries. It is prooved, that they are still [violating the GPL][29637] with the binaries they shipped at the beginning, because they never released the source for them. Team-Kodi does currently not recommend that any end-user buy Allwinner A1x or A2x based hardware for the specific purpose of only running Kodi. There are a few threads in the kodi forum that one can read to get the whole story regarding Allwinner and their support to Team-Kodi. Team-Kodi in fact did not get effective Allwinner support in the end.[[1]][29638]  

Due to massive pressure of the **linux-sunxi community** (in fact that have only been a few designated developers), Allwinner tried to solve the CedarX GPL violation issue with releasing a rewrite of their CedarX code, summarized as their "media-codec". This new media-codec provides the source for direct register access of the video decoding engine within the SoC. Codecs are now included via plugins. The basic decoder and MPEG2, MJPEG, MPEG4 and H246 codecs implementation are available as GPL'ed source, while the encoder and the other codecs are includeable only via a closed source library still. It's not prooved, that these closed source library is GPL compliant.  

In the meantime, many parts of the video decoding engine have been reverse engineered by a few developers of the linux-sunxi community, so that the hardware can be accessed via real open source code, independent of any code which was released by Allwinner. The working name of this community based piece of software is [Cedrus][29639]. The sad thing about the media-codec release of Allwinner is the fact, that it does not provide any other funtionality with it's open source part, that was not known already due to the [reverse engineering effort][29640].  

# Linux-sunxi community
While all these efforts have been done by the linux-sunxi community, there has been nearly **NO** support from Allwinner since now, helping the community to do a open source driver for their video engine, which is [able to be merged into the mainline kernel][29641] in the end. Even though it was possible to figure out the [register's usage][29642] of the video engine and to build a [vdpau backend][29643] which demonstrates the usage of the sunxi video decoding/encoding engine. With this [libvdpau-sunxi backend][29643] it's possible to support hardware accelerated video decoding on common media players which support VDPAU. Even though linux-sunxi community does get no help from Allwinner in these task (and nearly zero in all the others btw.), a small group of developers has started to think about a v4l2 kernel driver. Main goal for the community is to support the sunxi video decoding/encoding engine within the mainline kernel.  

# Technical overview
To run Kodi on sunxi devices without GPL violating code and the official linux kernel, we basically need a few things: 
### Video engine kernel driver
The existing kernel module is not mainlineable, so there has work been started to create a [kernel driver based on a v4l2 mem2mem device][29641]. (not finished)  

**Important:** Many people are interested in quick and dirty solutions to get things to work. They do not care about GPL violance, binary usage, Allwinner ignorating the community ... So this ends up in self-baked vendor adjusted solutions which base on GPL violating binaries or the 'dubious' Allwinner media-codec. This can mainly be recognized in the "kodi-sunxi" dedicated forum threads of the different vendors (OrangePi, BananaPi - naming two examples). It's obvious, that motivation for such a driver is still very low, when neither the 'USER' nor the 'VENDORS' are interested in a free open source driver and go on preferring Allwinner code. Allwinner, the company that does not support the linux-sunxi community, which is responsible for their whole mainlining task.
### Sunxi display driver
Work for the other important part (display driver), which is needed for (open source) Kodi on sunxi devices and [mainline kernel][29644], has been started, too. (not finished) 
### Mali (3D) kernel driver + userspace library
It's possible to use the provided [mali userspace libraries][29645] together with the out-of-tree third party kernel driver.   

### Support for sunxi in Kodi
As soon as there are kernel drivers for display and the video engine, which are useable with the mainline kernel (in-kernel or out-of-tree), Kodi integration can be started. Everybody, especially Team-Kodi developers, is very welcome to support the linux-sunxi community with this task. 
# Kodi via libvdpau-sunxi
The main goals will take some time. Fortunately [github user mosterta][29646] has announced a [kodi fork][29647], which already uses open source community code. Video decoding is done hardware accelerated via an adapted libvdpau-sunxi version, which makes OpenGL/ES integration (via Mali) and zero-copy possible. It's recommended to support this version in the meanwhile, until the work required to allow a more future-proof integration is completed. In order to get that fork of kodi working, you have to patch a lot. See the [Kodi forum thread][29648] for building instructions. 
# Alternative media players
Alternative media players (such as mpv or mplayer) or [VDR][29649] are supported via [libvdpau-sunxi][29650]. They do not depend on mali, but still require the legacy sunxi-3.4 kernel due to lack of display and video engine support in the mainline kernel. They work pretty stable, though libvdpau-sunxi is just proof-of-concept code. 
# Conclusion
It's obvious again, that the main goal must be to bring this media related drivers into the mainline kernel. It's the only solution, if one seriously wants to run media apps, especially Kodi, on a sunxi device. But this all will not happen, if interest in open source drivers seems to be that small, as it seems to be at the moment. 
# References
  1. [↑][29651] <http://forum.kodi.tv/showthread.php?tid=126995> Allwinner A10 : Is XBMC ported to MALI-400MP ?
