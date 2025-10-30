# Cedrus
(Redirected from [Libvdpau-sunxi][30755])
 
## Contents
  * [1 Overview][30758]
  * [2 Development / Mainline Kernel][30759]
  * [3 Crowdfunding][30760]
  * [4 Current status][30761]
  * [5 Supported codec matrix][30762]

# Overview
**Cedrus** is a linux-sunxi community project which was achieved by [ reverse engineering][30763] the [Video Engine][30764] hardware block. 
    It's the name of a software project, which is a fully 100% libre and open source driver for using the hardware accelerated video de-/encoding engine found in sunxi devices. It replaces the proprietary library that has a long history of license ambiguity issues and in certain cases even (L)GPL violations.
# Development / Mainline Kernel
Interested people are welcome to join the development channel **#cedrus** on OFTC IRC (irc.oftc.net). 
This channel is logged and the logs are available at [[1]][30765]. 
Development of a mainline kernel driver and the corresponding libva-v4l2-request LibVA implementation is in progress. You can follow the development on [**Sunxi-Cedrus**][30766]. 
# Crowdfunding
On February 2, 2018 [Bootlin][30767] (formerly Free Electrons) started a [crowdfunding campaign][30768] in order to bring sunxi-cedrus into the linux mainline kernel. The main goal (MPEG2 and H264 decoding on A10, A13, A20, A33, R8 and R16) and the first stretch goal (implement H3, H5 and A64) has reached already. Delivery date of the main goal is expected to be by end of June 2018, stretch goals are expected to be delivered by end of December 2018. 
Outstanding stretch goals are: 
  * H265 decoding support
  * H264 encoding support

In October 2018, Maxime Ripard of Bootlin gave a presentation on the project at [ELCE][30769] entitled [Supporting Hardware Codecs in a Linux system][30770]. 
# Current status
The hardware is already well understood by the means of the [ reverse-engineering effort][30763], which very quickly got successful results. A large majority of the [hardware registers][30771] are documented. With this information some Proof of Concept (PoC) [example source code][30772] was written to verify that the hardware can be configured correctly from the information obtained. To forward verifying, there was implemented a [vdpau driver backend][30773] which is quite usable and can be used by any media player that uses the [vdpau framework][30774]. 
The Cedrus project aims for a proper driver and software that can be mainlined and upstreamed to the proper places, this can't happen with the vendor kernel driver in its limitations, source code quality or transbording as a security risk. 
Steps for this proper driver and software can be seen in its [planning phase][30775]. 
See for more information. 
  * [**Video Engine Register Guide**][30771]
  * [**libvdpau-sunxi**][30776]
  * [**Video Engine Planning**][30775].
  * [**Sunxi-cedrus**][30777]

# Supported codec matrix
In this colorful table is represented what is understood and supported by hardware in the **left side** , the designation VE+Number are the video engine hardware version and above are the SoCs were found. Here are only SoCs and hardware versions which was confirmed or reported, the ones that aren't here should and are expected to be very equal in mode. 
The **right side** represents the state of software. Take notice about the PoC (Proof of Concept) in which only exists for demonstration the correct understanding about the working of the hardware, sometimes the creation of this PoC is skipped. 
| A10/A20 | A13 | A31s | A80 | A33 | H3 | A64 | H5 | H6  |  | Software Support   
---|---|---|---|---|---|---|---|---|---|---|---  
| subengine | codec  | VE1623 | VE1625 | VE1633 | VE1639 | VE1667 | VE1680 | VE1689 | VE1718 | VE????  | PoC | libvdpau-sunxi | sunxi-cedrus (v4l)   
decoder | [0x100][30778] | JPEG/MJPEG  | baseline profile only  |  | n.a. | n.a.   
MPEG1  |  |  |  |   
MPEG2  |  |  |  |   
MPEG4  |  |  |  |   
MS-MPEG4  |  |  | n.a. | n.a.   
WMV1  |  |   
WMV2  |  |   
DIVX  |  |  |   
XDIV  |  |  | n.a.   
H263  |  |   
VP6  |  |   
? | Sorenson  | Unconfirmed  |   
AVS  | Unconfirmed  |   
[0x200][30779] | H264  |  |  |  | (early high profile)   
VP8  |  |  | n.a. | Since Linux 5.11   
[0x300][30780] | VC1/WMV9  |  |  |  | n.a.   
[0x400][30781] | RMVB  | Unconfirmed  |  | n.a.   
[0x500][30782] | H265  |  | 8bits | 10bits  |  |  | (early)   
encoder  | [0xa00][30783]  
[0xb00][30784] | JPEG/MJPEG  | baseline profile only | not tried because of no time to try  |  | n.a. | n.a.   
H264  | baseline profile only | not tried because of no time to try  | No B frames | n.a.   
decoder | 0xe00 | JPEG  |  | Unconfirmed  |  | n.a.   
  
As can be seen in this table with the color of green, the most used video codecs are already fully reversed engineered. The codecs that are still missing are too old or/and obsolete and aren't used anymore for the creation of new video content. The content (video files) that exists encoded in this codecs is in the great majority not beyond standard definition, meaning that the task of decoding is easy done with just software decode by cpu. For this reason this codecs aren't a priority to work on. 
If anyone has a need for a yet to be support codec, please contact the people involved in the cedrus project to find what can be arranged.
