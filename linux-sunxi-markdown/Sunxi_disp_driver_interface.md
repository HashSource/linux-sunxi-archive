# Sunxi disp driver interface
[![MBOX icon important.png][52724]][52725] | This page provides outdated set of instructions and needs to be updated to reflect current status.   
---|---  
The allwinner provided sunxi disp driver has many severe issues and needs to be significantly redesigned. Since the allwinner engineers decided to directly use numbers for ioctls, instead of using the _IO macros, there is no way around redefining all of them to begin with. We will try to keep the current interface stable for as long as possible, and make the future break or breaks as abrupt and complete as possible. But: 
**The /dev/disp interface will break and will in the end vanish completely!**
## Contents
  * [1 First!][52726]
  * [2 The goal][52727]
  * [3 The path][52728]
  * [4 Current users][52729]
    * [4.1 Allwinner Android support code][52730]
  * [5 Stable IOCTLs][52731]
  * [6 Color format mapping table][52732]
  * [7 Deinterlacer][52733]

## First!
The disp ioctl header file has been cleaned up and some versioning has been added. Be sure to get the correct header file from the kernel source (LINK!). 
In Documentation/sunxi/disp/ there is disp_version.c which gives a good example of how to easily support the new and mandatory versioning ioctl. 
## The goal
## The path
## Current users
Below is a list of the current users of the disp interface, where the repository for this code is, and how the responsible author can notified of breakage. 
### Allwinner Android support code
## Stable IOCTLs
The following IOCTLs and their structures are known to be in active use as they were flagged to us by the programs listed in the previous section. We will try to do our utmost best to keep these IOCTLs stable. All other ioctls are a bit of a free-for-all, and will not be checked for.</ br> There is a very good overview of all available ioctls and how to use them: 
  * [Documentation/sunxi/disp/disp_ioctls.txt][52734]
  * [Sunxi disp driver interface/IOCTL][52735]

  

  * DISP_CMD_EXECUTE_CMD_AND_STOP_CACHE
  * DISP_CMD_FB_RELEASE
  * DISP_CMD_FB_REQUEST
  * DISP_CMD_GET_OUTPUT_TYPE
  * DISP_CMD_HDMI_GET_HPD_STATUS
  * DISP_CMD_HDMI_GET_MODE
  * DISP_CMD_HDMI_OFF
  * DISP_CMD_HDMI_ON
  * DISP_CMD_HDMI_SET_MODE
  * DISP_CMD_HDMI_SUPPORT_MODE
  * DISP_CMD_LAYER_ALPHA_OFF
  * DISP_CMD_LAYER_ALPHA_ON
  * DISP_CMD_LAYER_BOTTOM
  * DISP_CMD_LAYER_CK_OFF
  * DISP_CMD_LAYER_CK_ON
  * DISP_CMD_LAYER_CLOSE
  * DISP_CMD_LAYER_GET_BLACK_EXTEN_LEVEL
  * DISP_CMD_LAYER_GET_CHROMA_SHARP_LEVEL
  * DISP_CMD_LAYER_GET_LUMA_SHARP_LEVEL
  * DISP_CMD_LAYER_GET_PARA
  * DISP_CMD_LAYER_GET_VPP_EN
  * DISP_CMD_LAYER_GET_WHITE_EXTEN_LEVEL
  * DISP_CMD_LAYER_OPEN
  * DISP_CMD_LAYER_RELEASE
  * DISP_CMD_LAYER_REQUEST
  * DISP_CMD_LAYER_SET_ALPHA_VALUE
  * DISP_CMD_LAYER_SET_BLACK_EXTEN_LEVEL
  * DISP_CMD_LAYER_SET_CHROMA_SHARP_LEVEL
  * DISP_CMD_LAYER_SET_LUMA_SHARP_LEVEL
  * DISP_CMD_LAYER_SET_PARA
  * DISP_CMD_LAYER_SET_PIPE
  * DISP_CMD_LAYER_SET_SCN_WINDOW
  * DISP_CMD_LAYER_SET_WHITE_EXTEN_LEVEL
  * DISP_CMD_LAYER_TOP
  * DISP_CMD_LAYER_VPP_OFF
  * DISP_CMD_LAYER_VPP_ON
  * DISP_CMD_LCD_OFF
  * DISP_CMD_LCD_ON
  * DISP_CMD_SCN_GET_HEIGHT
  * DISP_CMD_SCN_GET_WIDTH
  * DISP_CMD_SET_COLORKEY
  * DISP_CMD_START_CMD_CACHE
  * DISP_CMD_VIDEO_GET_FRAME_ID
  * DISP_CMD_VIDEO_SET_FB
  * DISP_CMD_VIDEO_START
  * DISP_CMD_VIDEO_STOP

## Color format mapping table
__disp_pixel_fmt_t | __disp_pixel_mod_t | __disp_pixel_seq_t | br_swap | DirectFB | Gstreamer | KMS | V4L2   
---|---|---|---|---|---|---|---  
DISP_FORMAT_YUV444 | DISP_MOD_INTERLEAVED | DISP_SEQ_AYUV |  | n/a | n/a | n/a |   
DISP_SEQ_VUYA |  | n/a | n/a | n/a |   
DISP_MOD_NON_MB_PLANAR |  |  | DSPF_YUV444P | GST_VIDEO_FORMAT_Y444 | DRM_FORMAT_YUV444 |   
DISP_FORMAT_YUV422 | DISP_MOD_INTERLEAVED | DISP_SEQ_YUYV |  | DSPF_YUY2 | GST_VIDEO_FORMAT_YUY2 | DRM_FORMAT_YUYV |   
DISP_SEQ_UYVY |  | DSPF_UYVY | GST_VIDEO_FORMAT_UYVY | DRM_FORMAT_UYVY |   
DISP_SEQ_YVYU |  | n/a | GST_VIDEO_FORMAT_YVYU | DRM_FORMAT_YVYU |   
DISP_SEQ_VYUY |  | n/a | n/a | DRM_FORMAT_VYUY |   
DISP_MOD_NON_MB_UV_COMBINED | DISP_SEQ_UVUV |  | DSPF_NV16 | GST_VIDEO_FORMAT_NV16 | DRM_FORMAT_NV16 |   
DISP_SEQ_VUVU |  | DSPF_YV16 | n/a | DRM_FORMAT_NV61 |   
DISP_MOD_NON_MB_PLANAR |  |  | n/a | GST_VIDEO_FORMAT_Y42B | DRM_FORMAT_YUV422 |   
DISP_FORMAT_YUV420 | DISP_MOD_NON_MB_UV_COMBINED | DISP_SEQ_UVUV |  | DSPF_NV12 | GST_VIDEO_FORMAT_NV12 | DRM_FORMAT_NV12 |   
DISP_SEQ_VUVU |  | DSPF_NV21 | GST_VIDEO_FORMAT_NV21 | DRM_FORMAT_NV21 |   
DISP_MOD_NON_MB_PLANAR |  |  | DSPF_I420 | GST_VIDEO_FORMAT_I420 | DRM_FORMAT_YUV420 |   
DISP_FORMAT_YUV411 | DISP_MOD_NON_MB_UV_COMBINED | DISP_SEQ_UVUV |  | n/a | n/a | n/a |   
DISP_SEQ_VUVU |  | n/a | n/a | n/a |   
DISP_MOD_NON_MB_PLANAR |  |  | n/a | GST_VIDEO_FORMAT_Y41B | DRM_FORMAT_YUV411 |   
DISP_FORMAT_ARGB8888 | DISP_MOD_INTERLEAVED | DISP_SEQ_ARGB | true | DSPF_ABGR | GST_VIDEO_FORMAT_ABGR | DRM_FORMAT_ABGR8888 |   
false | DSPF_ARGB | GST_VIDEO_FORMAT_ARGB | DRM_FORMAT_ARGB8888 |   
DISP_SEQ_BGRA | true | n/a | GST_VIDEO_FORMAT_RGBA | DRM_FORMAT_RGBA8888 |   
false | n/a | GST_VIDEO_FORMAT_BGRA | DRM_FORMAT_BGRA8888 |   
DISP_FORMAT_ARGB888 | DISP_MOD_INTERLEAVED | DISP_SEQ_ARGB | true | n/a | GST_VIDEO_FORMAT_xBGR | DRM_FORMAT_XBGR8888 |   
false | DSPF_RGB32 | GST_VIDEO_FORMAT_xRGB | DRM_FORMAT_XRGB8888 |   
DISP_SEQ_BGRA | true | n/a | GST_VIDEO_FORMAT_RGBx | DRM_FORMAT_RGBX8888 |   
false | n/a | GST_VIDEO_FORMAT_BGRx | DRM_FORMAT_BGRX8888 |   
DISP_FORMAT_RGB888 | DISP_MOD_INTERLEAVED |  | true | n/a | GST_VIDEO_FORMAT_BGR | DRM_FORMAT_BGR888 |   
false | DSPF_RGB24 | GST_VIDEO_FORMAT_RGB | DRM_FORMAT_RGB888 |   
DISP_MOD_PLANAR |  |  | n/a | GST_VIDEO_FORMAT_GBR | n/a |   
DISP_FORMAT_CSIRGB | DISP_MOD_PLANAR |  |  | n/a | GST_VIDEO_FORMAT_GBR | n/a |   
DISP_FORMAT_RGB655 | DISP_MOD_INTERLEAVED | DISP_SEQ_P10 | true | n/a | n/a | n/a |   
false | n/a | n/a | n/a |   
DISP_SEQ_P01 | true | DSPF_BGR555 | GST_VIDEO_FORMAT_BGR15 | n/a |   
false | DSPF_RGB555 | GST_VIDEO_FORMAT_RGB15 | n/a |   
DISP_FORMAT_RGB565 | DISP_MOD_INTERLEAVED | DISP_SEQ_P10 | true | n/a | n/a | n/a |   
false | n/a | n/a | n/a |   
DISP_SEQ_P01 | true | n/a | GST_VIDEO_FORMAT_BGR16 | DRM_FORMAT_BGR565 |   
false | DSPF_RGB16 | GST_VIDEO_FORMAT_RGB16 | DRM_FORMAT_RGB565 |   
DISP_FORMAT_RGB556 | DISP_MOD_INTERLEAVED | DISP_SEQ_P10 | true | n/a | n/a | n/a |   
false | n/a | n/a | n/a |   
DISP_SEQ_P01 | true | n/a | n/a | n/a |   
false | n/a | n/a | n/a |   
DISP_FORMAT_ARGB1555 | DISP_MOD_INTERLEAVED | DISP_SEQ_P10 | true | n/a | n/a | n/a |   
false | n/a | n/a | n/a |   
DISP_SEQ_P01 | true | n/a | n/a | DRM_FORMAT_ABGR1555 |   
false | DSPF_ARGB1555 | n/a | DRM_FORMAT_ARGB1555 |   
DISP_FORMAT_RGBA5551 | DISP_MOD_INTERLEAVED | DISP_SEQ_P10 | true | n/a | n/a | n/a |   
false | n/a | n/a | n/a |   
DISP_SEQ_P01 | true | n/a | n/a | DRM_FORMAT_BGRA5551 |   
false | DSPF_RGBA5551 | n/a | DRM_FORMAT_RGBA5551 |   
DISP_FORMAT_ARGB4444 | DISP_MOD_INTERLEAVED | DISP_SEQ_P10 | true | n/a | n/a | n/a |   
false | n/a | n/a | n/a |   
DISP_SEQ_P01 | true | n/a | n/a | DRM_FORMAT_ABGR4444 |   
false | DSPF_ARGB4444 | n/a | DRM_FORMAT_ARGB4444 |   
DISP_FORMAT_8BPP | DISP_MOD_INTERLEAVED | DISP_SEQ_P3210 |  | n/a | n/a | n/a |   
DISP_SEQ_P0123 |  | DSPF_LUT8 | GST_VIDEO_FORMAT_RGB8P | DRM_FORMAT_C8 |   
DISP_FORMAT_4BPP | DISP_MOD_INTERLEAVED | DISP_SEQ_P76543210 |  | n/a | n/a | n/a |   
DISP_SEQ_P67452301 |  | n/a | n/a | n/a |   
DISP_SEQ_P10325476 |  | n/a | n/a | n/a |   
DISP_SEQ_P01234567 |  | DSPF_LUT4 | n/a | n/a |   
DISP_FORMAT_2BPP | DISP_MOD_INTERLEAVED | DISP_SEQ_2BPP_BIG_BIG |  | n/a | n/a | n/a |   
DISP_SEQ_2BPP_BIG_LITTER |  | n/a | n/a | n/a |   
DISP_SEQ_2BPP_LITTER_BIG |  | n/a | n/a | n/a |   
DISP_SEQ_2BPP_LITTER_LITTER |  | DSPF_LUT2 | n/a | n/a |   
DISP_FORMAT_1BPP | DISP_MOD_INTERLEAVED | DISP_SEQ_1BPP_BIG_BIG |  | n/a | n/a | n/a |   
DISP_SEQ_1BPP_BIG_LITTER |  | n/a | n/a | n/a |   
DISP_SEQ_1BPP_LITTER_BIG |  | DSPF_A1_LSB | n/a | n/a |   
DISP_SEQ_1BPP_LITTER_LITTER |  | DSPF_A1 | n/a | n/a |   
Missing |  |  |  | DSPF_A8   
DSPF_RGB332   
DSPF_ALUT44   
DSPF_AiRGB   
DSPF_ARGB2554   
DSPF_RGBA4444   
DSPF_AYUV   
DSPF_A4   
DSPF_ARGB1666   
DSPF_ARGB6666   
DSPF_RGB18   
DSPF_RGB444   
DSPF_ARGB8565   
DSPF_AVYU   
DSPF_RGBAF88871 | GST_VIDEO_FORMAT_ENCODED   
GST_VIDEO_FORMAT_YV12   
GST_VIDEO_FORMAT_AYUV   
GST_VIDEO_FORMAT_v210   
GST_VIDEO_FORMAT_v216   
GST_VIDEO_FORMAT_GRAY8   
GST_VIDEO_FORMAT_GRAY16_BE   
GST_VIDEO_FORMAT_GRAY16_LE   
GST_VIDEO_FORMAT_v308   
GST_VIDEO_FORMAT_UYVP   
GST_VIDEO_FORMAT_A420   
GST_VIDEO_FORMAT_YUV9   
GST_VIDEO_FORMAT_YVU9   
GST_VIDEO_FORMAT_IYU1   
GST_VIDEO_FORMAT_ARGB64   
GST_VIDEO_FORMAT_AYUV64   
GST_VIDEO_FORMAT_r210   
GST_VIDEO_FORMAT_I420_10BE   
GST_VIDEO_FORMAT_I420_10LE   
GST_VIDEO_FORMAT_I422_10BE   
GST_VIDEO_FORMAT_I422_10LE   
GST_VIDEO_FORMAT_Y444_10BE   
GST_VIDEO_FORMAT_Y444_10LE   
GST_VIDEO_FORMAT_GBR_10BE   
GST_VIDEO_FORMAT_GBR_10LE   
GST_VIDEO_FORMAT_NV24 | DRM_FORMAT_RGB332   
DRM_FORMAT_BGR233   
DRM_FORMAT_XRGB4444   
DRM_FORMAT_XBGR4444   
DRM_FORMAT_RGBX4444   
DRM_FORMAT_BGRX4444   
DRM_FORMAT_RGBA4444   
DRM_FORMAT_BGRA4444   
DRM_FORMAT_XRGB1555   
DRM_FORMAT_XBGR1555   
DRM_FORMAT_RGBX5551   
DRM_FORMAT_BGRX5551   
DRM_FORMAT_XRGB2101010   
DRM_FORMAT_XBGR2101010   
DRM_FORMAT_RGBX1010102   
DRM_FORMAT_BGRX1010102   
DRM_FORMAT_ARGB2101010   
DRM_FORMAT_ABGR2101010   
DRM_FORMAT_RGBA1010102   
DRM_FORMAT_BGRA1010102   
DRM_FORMAT_AYUV   
DRM_FORMAT_NV24   
DRM_FORMAT_NV42   
DRM_FORMAT_NV12MT   
DRM_FORMAT_YUV410   
DRM_FORMAT_YVU410   
DRM_FORMAT_YVU411   
DRM_FORMAT_YVU420   
DRM_FORMAT_YVU422   
DRM_FORMAT_YVU444 |   
## Deinterlacer
There is a deinterlacer implemented in Sunxi Display Driver. It seems to be controlled by the scaler's registers and is activated by the DISP_CMD_VIDEO iotcl's. [This scheme][52736] gives an overview about how the necessary registers are set within sunxi display driver. 
[Allwinner's example code][52737] should give a few hints, how the ioctl workflow should work.
