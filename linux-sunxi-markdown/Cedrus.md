# Cedrus
## Contents
  * [1 Overview][12356]
  * [2 Development / Mainline Kernel][12357]
  * [3 Crowdfunding][12358]
  * [4 Current status][12359]
  * [5 Supported codec matrix][12360]

# Overview
**Cedrus** is a linux-sunxi community project which was achieved by [ reverse engineering][12361] the [Video Engine][12362] hardware block. 
    It's the name of a software project, which is a fully 100% libre and open source driver for using the hardware accelerated video de-/encoding engine found in sunxi devices. It replaces the proprietary library that has a long history of license ambiguity issues and in certain cases even (L)GPL violations.
# Development / Mainline Kernel
Interested people are welcome to join the development channel **#cedrus** on OFTC IRC (irc.oftc.net). 
This channel is logged and the logs are available at [[1]][12363]. 
Development of a mainline kernel driver and the corresponding libva-v4l2-request LibVA implementation is in progress. You can follow the development on [**Sunxi-Cedrus**][12364]. 
# Crowdfunding
On February 2, 2018 [Bootlin][12365] (formerly Free Electrons) started a [crowdfunding campaign][12366] in order to bring sunxi-cedrus into the linux mainline kernel. The main goal (MPEG2 and H264 decoding on A10, A13, A20, A33, R8 and R16) and the first stretch goal (implement H3, H5 and A64) has reached already. Delivery date of the main goal is expected to be by end of June 2018, stretch goals are expected to be delivered by end of December 2018. 
Outstanding stretch goals are: 
  * H265 decoding support
  * H264 encoding support

In October 2018, Maxime Ripard of Bootlin gave a presentation on the project at [ELCE][12367] entitled [Supporting Hardware Codecs in a Linux system][12368]. 
# Current status
The hardware is already well understood by the means of the [ reverse-engineering effort][12361], which very quickly got successful results. A large majority of the [hardware registers][12369] are documented. With this information some Proof of Concept (PoC) [example source code][12370] was written to verify that the hardware can be configured correctly from the information obtained. To forward verifying, there was implemented a [vdpau driver backend][12371] which is quite usable and can be used by any media player that uses the [vdpau framework][12372]. 
The Cedrus project aims for a proper driver and software that can be mainlined and upstreamed to the proper places, this can't happen with the vendor kernel driver in its limitations, source code quality or transbording as a security risk. 
Steps for this proper driver and software can be seen in its [planning phase][12373]. 
See for more information. 
  * [**Video Engine Register Guide**][12369]
  * [**libvdpau-sunxi**][12374]
  * [**Video Engine Planning**][12373].
  * [**Sunxi-cedrus**][12375]

# Supported codec matrix
In this colorful table is represented what is understood and supported by hardware in the **left side** , the designation VE+Number are the video engine hardware version and above are the SoCs were found. Here are only SoCs and hardware versions which was confirmed or reported, the ones that aren't here should and are expected to be very equal in mode. 
The **right side** represents the state of software. Take notice about the PoC (Proof of Concept) in which only exists for demonstration the correct understanding about the working of the hardware, sometimes the creation of this PoC is skipped. 
| A10/A20 | A13 | A31s | A80 | A33 | H3 | A64 | H5 | H6  |  | Software Support   
---|---|---|---|---|---|---|---|---|---|---|---  
| subengine | codec  | VE1623 | VE1625 | VE1633 | VE1639 | VE1667 | VE1680 | VE1689 | VE1718 | VE????  | PoC | libvdpau-sunxi | sunxi-cedrus (v4l)   
decoder | [0x100][12376] | JPEG/MJPEG  | baseline profile only  |  | n.a. | n.a.   
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
[0x200][12377] | H264  |  |  |  | (early high profile)   
VP8  |  |  | n.a. | Since Linux 5.11   
[0x300][12378] | VC1/WMV9  |  |  |  | n.a.   
[0x400][12379] | RMVB  | Unconfirmed  |  | n.a.   
[0x500][12380] | H265  |  | 8bits | 10bits  |  |  | (early)   
encoder  | [0xa00][12381]  
[0xb00][12382] | JPEG/MJPEG  | baseline profile only | not tried because of no time to try  |  | n.a. | n.a.   
H264  | baseline profile only | not tried because of no time to try  | No B frames | n.a.   
decoder | 0xe00 | JPEG  |  | Unconfirmed  |  | n.a.   
  
As can be seen in this table with the color of green, the most used video codecs are already fully reversed engineered. The codecs that are still missing are too old or/and obsolete and aren't used anymore for the creation of new video content. The content (video files) that exists encoded in this codecs is in the great majority not beyond standard definition, meaning that the task of decoding is easy done with just software decode by cpu. For this reason this codecs aren't a priority to work on. 
If anyone has a need for a yet to be support codec, please contact the people involved in the cedrus project to find what can be arranged.
