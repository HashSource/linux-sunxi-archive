# Cedrus/Supported Codec Feature Matrix
< [Cedrus][12221]
 
In this colorful table is represented what is understood and supported by hardware in the **left side** , the designation VE+Number are the video engine hardware version and above are the SoCs were found. Here are only SoCs and hardware versions which was confirmed or reported, the ones that aren't here should and are expected to be very equal in mode. 
The **right side** represents the state of software. Take notice about the PoC (Proof of Concept) in which only exists for demonstration the correct understanding about the working of the hardware, sometimes the creation of this PoC is skipped. 
| A10/A20 | A13 | A31s | A80 | A33 | H3 | A64 | H5 | H6  |  | Software Support   
---|---|---|---|---|---|---|---|---|---|---|---  
| subengine | codec  | VE1623 | VE1625 | VE1633 | VE1639 | VE1667 | VE1680 | VE1689 | VE1718 | VE????  | PoC | libvdpau-sunxi | sunxi-cedrus (v4l)   
decoder | [0x100][12224] | JPEG/MJPEG  | baseline profile only  |  | n.a. | n.a.   
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
[0x200][12225] | H264  |  |  |  | (early high profile)   
VP8  |  |  | n.a. | Since Linux 5.11   
[0x300][12226] | VC1/WMV9  |  |  |  | n.a.   
[0x400][12227] | RMVB  | Unconfirmed  |  | n.a.   
[0x500][12228] | H265  |  | 8bits | 10bits  |  |  | (early)   
encoder  | [0xa00][12229]  
[0xb00][12230] | JPEG/MJPEG  | baseline profile only | not tried because of no time to try  |  | n.a. | n.a.   
H264  | baseline profile only | not tried because of no time to try  | No B frames | n.a.   
decoder | 0xe00 | JPEG  |  | Unconfirmed  |  | n.a.   
  
As can be seen in this table with the color of green, the most used video codecs are already fully reversed engineered. The codecs that are still missing are too old or/and obsolete and aren't used anymore for the creation of new video content. The content (video files) that exists encoded in this codecs is in the great majority not beyond standard definition, meaning that the task of decoding is easy done with just software decode by cpu. For this reason this codecs aren't a priority to work on. 
If anyone has a need for a yet to be support codec, please contact the people involved in the cedrus project to find what can be arranged.
