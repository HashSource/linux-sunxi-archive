# CedarX/VideoRenderingChart
< [CedarX][12081](Redirected from [CedarXVideoRenderingChart][12082])
 
This site should grow to an overview chart, to see which codecs/files work with [CedarX][12081], A10 VPU (Video Processor Unit) hardware accelerated video decoding. 
Tests can be done with [XBMC Media Center][12085] and [VLC (VideoLAN Client)][12086] media player software or other software supporting [CedarX][12081] off-loading. 
This information should help programmers to improve usage of CedarX. Please also note that software decoding on CPU should not be discussed in this article. 
## Contents
  * [1 Overview][12087]
    * [1.1 Overview of cedarX video rendering issues on A10][12088]
  * [2 Known issues][12089]
  * [3 Samples for testing][12090]
  * [4 See also][12091]

# Overview
Feel free to add and edit with your issues and files or mark files working. File analyses could be done with [Mediainfo][12092]. Exported HTML-Info should be linked. 
### Overview of cedarX video rendering issues on A10
Works (VLC) | Works (XBMC) | Container | Video/Format | Video/CodecID (FourCC/IFF/OSType) | Resolution/Framerate | Audio/Format | Bitrate/Samplerate | Audio/Codec_ID (FourCC/IFF/OSType) | SampleFile | issues (XBMC native) | issues (VLC native) | issues (XBMC libhybris) | issues (VLC libhybris) | issues (mplayer [libvdpau-sunxi][12093])   
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Yes | Yes | MPEG-4 | AVC [[email protected]][12094] | avc1 | 1920x1080@25fps | AAC LC | VBR [[email protected]][12094] kHz | AAC | [[1]][12095] | None | None |  |  | unknown video format   
Yes | Yes | Matroska | AVC [[email protected]][12094] | V_MPEG4/ISO/AVC | 1280x720@25fps | - | - | - | [[2]][12096] | None | None |  |  | None   
Yes | Yes | AVI | MPEG-4 Visual Simple@L1 | MP4V | 1920x1080@25fps | MPEG1 Layer 3 | CBR [[email protected]][12094] kHz | MP3 | [[3]][12097] | None | None |  |  | None   
Yes | Yes | MPEG-4 | MPEG-4 Visual Advanced Simple@L1 |  | 1280x720@25fps | - | - | - | [[4]][12098] | Jerky / Rubberbanding playback | None |  |  | None   
Yes | Yes | MPEG-PS | MPEG-2 Main@High |  | 1920x1080@25fps | MPEG1 Layer 2 | CBR [[email protected]][12094] | MP2 | [[5]][12099] | None | None |  |  | None   
Yes | Yes | MPEG-PS | MPEG-2 Main@High 1440 | HDV 720p | 1280x720@25fps | - | - | - | [[6]][12100] | None | None |  |  | None   
Yes | Yes | MPEG-4 | AVC [[email protected]][12094], weightp=2 | avc1 | 1920x1080@24fps | AAC LC | VBR 127Kbps@48 kHz | AAC | [[7]][12101] | Lots of artifacts | Lots of artifacts |  |  | None   
Yes | Yes | WEBM | VP8 | webm | 1920x1080@25fps | vorbis | 996kbps @48/48/24 kHz | VORBIS | [[8]][12102] | None | None |  |  | unknown video format   
|  | MPEG-TS (1080i) | AVC [[email protected]][12094] |  | 1920x1080@25fps | AC3 | CBR 384Kbps@48 kHz |  | [[9]][12103] |  |  | Lag video and sound | None | None   
|  | MPEG-4 | AVC [[email protected]][12094] |  | [[email protected]][12094] | AC3 | CBR 320Kbps@48 kHz |  | [[10]][12104] | Artifacts and lag video | Only artifacts | Only lag video | None | None   
|  | MPEG-4 | AVC [[email protected]][12094] |  | 1280x720@24fps | DTS | CBR 2 046 Kbps / 1 509 Kbps@48 kHz |  | [[11]][12105] | Artifacts and lag video | Only artifacts | Only lag video | None | None   
# Known issues
The use of [weighted P-frame prediction][12106] in H.264/AVC encoded files results in blocky artifacts when using the cedarx blobs compiled for linux. There is also a discussion thread at doom10.org forum [[12]][12107]
For example, adding '--weightp 0' option to x264 encoder command line produces a good file from the [Sintel movie trailer][12101]
[code] 
     x264 --weightp 0 -o testfile-good.mkv sintel_trailer-1080p.mp4
    
[/code]
While using the defaults produces a broken file 
[code] 
     x264 -o testfile-bad.mkv sintel_trailer-1080p.mp4
    
[/code]
Note: the media player from Android ICS firmware for Mele A2000 does not seem to have any problems with weighted P-frame prediction. 
Also see [[13]][12108]
A **workaround** for this issue is to use the Android libs via libhybris: [CedarX/libve][12109]
# Samples for testing
  * <http://samplemedia.linaro.org> \- Linaro samplemedia server
  * <http://samples.mplayerhq.hu> MPlayer has a very large collection of samples.
  * <http://www.demo-world.eu/trailers/> \- Demo World Trailers (DTS THX Dolby WMV Movie Distributor VOB Trailers)

# See also
  * [CedarX][12081] \- Library for Allwinner A10 VPU (Video Processor Unit) used for audio and video decoding and encoding hardware off-loading.
  * [CedarX/libve][12109] \- Using the Android blob on linux via libhybris
  * [CedarX/XBMC][12085] \- XBMC Media Center
  * [CedarX/VLC][12086] \- VideoLAN Client
  * [Mediainfo][12092] \- Analysis tool for Video Files
  * [Sample Media on linaro.org][12110]
