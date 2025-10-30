# GPL Violations
[Allwinner][21675] has repeatedly violated the [GPL][21676] (and by proxy so have most hardware manufacturers and resellers using or selling products based on Allwinner chipsets). Either by not providing (Linux/Android) kernel or u-boot source at all, or by delivering trees with pre-built binaries and no matching source code. They even blatantly use [LGPL][21677] licensed code in their userspace libraries for media decoding. 
Over time, Allwinner has only increased the binary blobs present in their kernel trees, showing clearly that - even though Allwinner in the meantime (March 2014) [joined Linaro][21678] \- it is not progressing. Quite the opposite actually, and one has to worry about what value Linaro membership really has if a member is allowed to behave like this. 
Allwinner also [joined the Linux Foundation][21679] as of June 2015, while compliance issues clearly remain. 
## Contents
  * [1 In the linux kernel][21680]
    * [1.1 Camera support][21681]
      * [1.1.1 libisp][21682]
      * [1.1.2 Other camera code][21683]
    * [1.2 Touchscreen support][21684]
  * [2 U-boot][21685]
    * [2.1 Other u-boot issues][21686]
  * [3 CedarX][21687]

# In the linux kernel
Inclusion of binaries in the kernel source tree are a clear and obvious violation of the license of the linux kernel (GPL). Please note that different SoC variants had different SDK code drops from Allwinner, and their GPL license compliance status may vary. 
SoC name  | Code drop  | Known GPL license incompatibilities   
---|---|---  
providing critical functionality | providing optional functionality   
Allwinner [A10][21688]/[A13][21689]/[A20][21690] |  | No problems known or worth mentioning. | No problems known or worth mentioning.   
Allwinner [H3][21691] | h3-lichee-1.0.tar.gz | While being open source, some of the Allwinner's code in the kernel has either no license boilerplate or an "all rights reserved" license notice. Most notably this includes HDMI support. | Some binary-only libraries are used for touchscreen, NAND, ISP, HDCP.   
## Camera support
### libisp
libisp is a driver for the Image signal processor (HawkView ISP), used for camera picture preprocessing and image enhancement. 
GPL violations in: 
  * [A31/A31s SDK][21692]
  * [A23 SDK][21693]
  * [A80 SDK][21694]

### Other camera code
For A80, [allwinner introduced 3 further blobs][21694], 2 for MIPICSI, and one for a "Face detector." 
GPL violations in: 
  * [A80 SDK][21694]

## Touchscreen support
Some binary blobs for touchscreen drivers are present in several SDKs. 
GPL violations in: 
  * [A31/A31a SDK][21692]
  * [A23 SDK][21693]
  * [A80 SDK][21694]

# U-boot
Inclusion of binaries in the u-boot source tree are a clear and obvious violation of the license of u-boot (GPL). 
Allwinner published the [u-boot source dump][21695] on Github on 2015.01.15. 
## Other u-boot issues
  * drivers/video_sunxi/sunxi_v2/de_bsp/hdmi/aw/libhdcp
  * board/sunxi/sun8iw7/box_standby/cpus_pm/cpus_pm_binary.code
  * board/sunxi/sun8iw6/box_standby/cpus_pm/cpus_pm_binary.code
  * tools/gen_check_sum

# CedarX
[![MBOX icon information.png][21696]][21697] | The hardware block which accelerates decoding and encoding of video codecs by hardware, called [Video Engine][21698], [Cedar Engine][21699] or also known as VPU, was **successfully reversed-engineered** to the point of allowing the use of hardware decoding for the most popular video codecs. Find more at the **[Cedrus project][21700]** wiki page. The linux-sunxi community has all the information that is required to create a proper driver that can be mainlined, without the need of the source-code of this CedarX software library, that only has use to: 
  * Comply with the (L)GPL License.
  * Be used as a source of documentation for the few parts and video codecs still not yet reversed-engineered.

  
---|---  
  
While Allwinner has published some code on their [github account][21701], they are not compliant yet. It seems that they feel that producing only code for those codecs that actively used LGPLed symbols is enough, and that they intend to keep the other codes under wraps. This is not how the LGPL works (as it applies to the full and complete binaries produced earlier, and not to some rewritten or restructured code produced today), and Allwinner should by now be very much aware of it. 
TODO: This is the userspace library that implements media decoding (JPEG, MPEG2/4, h264, VC1, VP6/8, ...). This driver is [a mix and match of many bits][21702], including some reference decoders, surrounded by allwinner and hw specific code. But, crucially, several parts of it have been taken straight from libavcodec from the FFMPEG project. This code is LGPL, but since this code has been adapted and included, CedarX is not a dependency and the LGPL applies to the whole library, forcing Allwinner to release the lot. 
Also, [CedarXPlayerTest][21703] has staticly linked in ffmpeg demuxer.
