# CedarX/VideoRenderingChart
< [CedarX][11858]
 
This site should grow to an overview chart, to see which codecs/files work with [CedarX][11858], A10 VPU (Video Processor Unit) hardware accelerated video decoding. 
Tests can be done with [XBMC Media Center][11861] and [VLC (VideoLAN Client)][11862] media player software or other software supporting [CedarX][11858] off-loading. 
This information should help programmers to improve usage of CedarX. Please also note that software decoding on CPU should not be discussed in this article. 
## Contents
  * [1 Overview][11863]
    * [1.1 Overview of cedarX video rendering issues on A10][11864]
  * [2 Known issues][11865]
  * [3 Samples for testing][11866]
  * [4 See also][11867]

# Overview
Feel free to add and edit with your issues and files or mark files working. File analyses could be done with [Mediainfo][11868]. Exported HTML-Info should be linked. 
### Overview of cedarX video rendering issues on A10
Works (VLC) | Works (XBMC) | Container | Video/Format | Video/CodecID (FourCC/IFF/OSType) | Resolution/Framerate | Audio/Format | Bitrate/Samplerate | Audio/Codec_ID (FourCC/IFF/OSType) | SampleFile | issues (XBMC native) | issues (VLC native) | issues (XBMC libhybris) | issues (VLC libhybris) | issues (mplayer [libvdpau-sunxi][11869])   
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Yes | Yes | MPEG-4 | AVC [[email protected]][11870] | avc1 | 1920x1080@25fps | AAC LC | VBR [[email protected]][11870] kHz | AAC | [[1]][11871] | None | None |  |  | unknown video format   
Yes | Yes | Matroska | AVC [[email protected]][11870] | V_MPEG4/ISO/AVC | 1280x720@25fps | - | - | - | [[2]][11872] | None | None |  |  | None   
Yes | Yes | AVI | MPEG-4 Visual Simple@L1 | MP4V | 1920x1080@25fps | MPEG1 Layer 3 | CBR [[email protected]][11870] kHz | MP3 | [[3]][11873] | None | None |  |  | None   
Yes | Yes | MPEG-4 | MPEG-4 Visual Advanced Simple@L1 |  | 1280x720@25fps | - | - | - | [[4]][11874] | Jerky / Rubberbanding playback | None |  |  | None   
Yes | Yes | MPEG-PS | MPEG-2 Main@High |  | 1920x1080@25fps | MPEG1 Layer 2 | CBR [[email protected]][11870] | MP2 | [[5]][11875] | None | None |  |  | None   
Yes | Yes | MPEG-PS | MPEG-2 Main@High 1440 | HDV 720p | 1280x720@25fps | - | - | - | [[6]][11876] | None | None |  |  | None   
Yes | Yes | MPEG-4 | AVC [[email protected]][11870], weightp=2 | avc1 | 1920x1080@24fps | AAC LC | VBR 127Kbps@48 kHz | AAC | [[7]][11877] | Lots of artifacts | Lots of artifacts |  |  | None   
Yes | Yes | WEBM | VP8 | webm | 1920x1080@25fps | vorbis | 996kbps @48/48/24 kHz | VORBIS | [[8]][11878] | None | None |  |  | unknown video format   
|  | MPEG-TS (1080i) | AVC [[email protected]][11870] |  | 1920x1080@25fps | AC3 | CBR 384Kbps@48 kHz |  | [[9]][11879] |  |  | Lag video and sound | None | None   
|  | MPEG-4 | AVC [[email protected]][11870] |  | [[email protected]][11870] | AC3 | CBR 320Kbps@48 kHz |  | [[10]][11880] | Artifacts and lag video | Only artifacts | Only lag video | None | None   
|  | MPEG-4 | AVC [[email protected]][11870] |  | 1280x720@24fps | DTS | CBR 2 046 Kbps / 1 509 Kbps@48 kHz |  | [[11]][11881] | Artifacts and lag video | Only artifacts | Only lag video | None | None   
# Known issues
The use of [weighted P-frame prediction][11882] in H.264/AVC encoded files results in blocky artifacts when using the cedarx blobs compiled for linux. There is also a discussion thread at doom10.org forum [[12]][11883]
For example, adding '--weightp 0' option to x264 encoder command line produces a good file from the [Sintel movie trailer][11877]
[code] 
     x264 --weightp 0 -o testfile-good.mkv sintel_trailer-1080p.mp4
    
[/code]
While using the defaults produces a broken file 
[code] 
     x264 -o testfile-bad.mkv sintel_trailer-1080p.mp4
    
[/code]
Note: the media player from Android ICS firmware for Mele A2000 does not seem to have any problems with weighted P-frame prediction. 
Also see [[13]][11884]
A **workaround** for this issue is to use the Android libs via libhybris: [CedarX/libve][11885]
# Samples for testing
  * <http://samplemedia.linaro.org> \- Linaro samplemedia server
  * <http://samples.mplayerhq.hu> MPlayer has a very large collection of samples.
  * <http://www.demo-world.eu/trailers/> \- Demo World Trailers (DTS THX Dolby WMV Movie Distributor VOB Trailers)

# See also
  * [CedarX][11858] \- Library for Allwinner A10 VPU (Video Processor Unit) used for audio and video decoding and encoding hardware off-loading.
  * [CedarX/libve][11885] \- Using the Android blob on linux via libhybris
  * [CedarX/XBMC][11861] \- XBMC Media Center
  * [CedarX/VLC][11862] \- VideoLAN Client
  * [Mediainfo][11868] \- Analysis tool for Video Files
  * [Sample Media on linaro.org][11886]
