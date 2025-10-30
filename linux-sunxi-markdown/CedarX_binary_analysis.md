# CedarX binary analysis
## Contents
  * [1 Object file observations][12142]
    * [1.1 From android][12143]
    * [1.2 From linux-armhf][12144]
    * [1.3 Function references][12145]

# Object file observations
While android and linux are different beasts from the userspace sense, It could be that the code was written in such way, that it could compile to both targets. Meaning that object files could be similar enough. 
## From android
The android-linux libvecore.a (md5sum 1c347a9ad3072ce3288bd6dba625b2a4) static lib contains the following object files: 
sunxi-bsp/cedarx-libs/libcedarv/android/libvecore $ arm-pc-linux-gnueabi-ar t libvecore.a | sort 
Object | Codec | extra info | notes   
---|---|---|---  
avs.o | AVS |  | though it looks incomplete   
decfile.o | General | Decode File? |   
decoder.o | General | Decoder? |   
get_bits.o | General | Read bits? |   
h264.o | MPEG4-AVC h264 | decoder |   
h264_hal.o | MPEG4-AVC h264 | hardware abstraction layer |   
h264_register.o | MPEG4-AVC h264 | direct CPU register access? |   
h264dec_drv.o | MPEG4-AVC h264 | decoder driver? |   
jpeg_dec_lib.o | JPEG | Decoder Library |   
jpeg_hal.o | JPEG | Hardware Abstraction Layer |   
libve.o |  | Video Encoder?/Engine? Library? |   
mjpeg.o | MJPEG |  |   
mp4_dec_divx311.o | MP4 DivX 3.11 | decoder |   
mp4_dec_h263.o | MP4 h263 | decoder |   
mp4_dec_vp6.o | MP4 vp6 | decoder |   
mp4_deccommon.o | MP4 | common mpeg4 (container?) decoder |   
mp4_decfrm_normal.o | MP4 | decoder frame? |   
mp4_hal.o | MP4 | Hardware Abstraction Layer |   
mp4_header.o | MP4 | container header? |   
mp4_register.o | MP4 | direct CPU register access? |   
mp4_tables_311.o | MP4 | DivX 3.11 lookup tables? |   
mp4_talbe.o | MP4 | lookup tables? |   
mp4_vld.o | MP4 | Variable Length Decoder? |   
mp4_vld_311.o | MP4 DivX 3.11 | Variable Length Decoder? |   
mpeg2.o | MPEG2 |  |   
mpeg2Dec.o | MPEG2 | Decoder |   
mpeg2Hal.o | MPEG2 | Hardware Abstraction Library |   
mpeg4.o | MPEG4-AVS |  |   
rv.o | RealVideo | 8 and 9 (Fourcc RV30 and RV40) |   
rv_core.o | RealVideo | core |   
rv_hal.o | RealVideo | Hardware Abstraction Layer |   
rv_huffTab.o | RealVideo | Huffman tables |   
vc1.o | VC1 |  | should be able to handle WMV3 bitstreams also   
vc1debug.o | VC1 | debug lib |   
vc1dec.o | VC1 | decoder |   
vc1dec_drv.o | VC1 | decoder driver |   
vc1decbit.o | VC1 |  |   
vc1decbitpl.o | VC1 |  |   
vc1decbitpltab.o | VC1 |  |   
vc1decent.o | VC1 |  |   
vc1decpic.o | VC1 |  |   
vc1decpictab.o | VC1 |  |   
vc1decseq.o | VC1 | Decoder sequencer |   
vc1decslice.o | VC1 | Decoder slicer |   
vc1gentab.o | VC1 | Table Generator |   
vc1hrd.o | VC1 |   
vc1register.o | VC1 | Direct CPU registers access? |   
vc1tools.o | VC1 | tools? |   
vp8.o | VP8 | main |   
vp8Coef.o | VP8 | Coefficients |   
vp8Dec.o | VP8 | Decoder |   
vp8DecFrm.o | VP8 | Decoder Frame? |   
vp8Hal.o | VP8 | Hardware Abstraction Layer |   
vp8Quantizer.o | VP8 | Quantizer |   
The rest of the bits are all open source, see the [linux-sunxi github][12146]. The exception is libcedarxalloc.a, but as mentioned above, we have [open_cdxalloc][12147]. 
  

## From linux-armhf
The linux-armhf libvecore.so (md5sum a026d27307e5204db191878651cc6394) shared object contains the following functions: [linux-armhf functions][12148] The rest of the bits are all open source, see the [linux-sunxi github][12146]. The exception is libcedarxalloc.a, but as mentioned above, we have [open_cdxalloc][12147]. 
## Function references
So far the following references can easily be observed with readelf -W -s. This is just an indication of some functions, by far complete as it would take way to long and is not really needed. 
FFmpeg huffman tree builder: ff_huff_build_tree() <http://ffmpeg.org/doxygen/trunk/huffman_8c.html>
libjpeg: get_soi() <http://sourceforge.net/p/libjpeg-turbo/code/HEAD/tree/trunk/jdmarker.c>
libvp62: VP62_InitCoeffScaleFactors() <http://en.verysource.com/code/5378534_1/libvp62.h.html>
H264/AVC Reference encoder/decoder: remove_frame_from_dpb() [http://iphome.hhi.de/suehring/tml/doc/lenc/html/mbuffer_8c.html#901bd781eb9aef8b79e98b8e10fbc2aa][12149]
VC1 Reference decoder: vc1_eResult vc1DECPIC_UnpackInterlaceMVModeParams() [http://wiki.multimedia.cx/index.php?title=Understanding_VC-1#vc1DECPIC_UnpackInterlaceMVModeParams][12150]
