# CSI
## Contents
  * [1 CSI on mainline Linux with v4l2][11287]
    * [1.1 Kernel config options][11288]
    * [1.2 Userspace configuration][11289]
      * [1.2.1 Media bus and capture formats][11290]
      * [1.2.2 Sensor sub-device configuration][11291]
    * [1.3 Capturing Images][11292]
      * [1.3.1 FFMpeg][11293]
    * [1.4 Caveats / TODOs][11294]
      * [1.4.1 JPEG media bus format buffers][11295]
      * [1.4.2 MIPI CSI-2][11296]
  * [2 BSP kernel supported camera's sensors table][11297]
    * [2.1 Reference][11298]

# CSI on mainline Linux with v4l2
The CSI (CMOS Sensor Interface) hardware block is partially supported in mainline Linux. Support for the hardware block found on [A31][11299] and later generations is already upstream, while the one found on [A10][11300]/[A20][11301] is being worked on, as of 2019/04/12. 
Currently parallel and BT.656 (embedded sync) interfaces are supported. MIPI CSI-2 is not. 
The mainline driver uses v4l2 with the sub-device API and media controller API. 
## Kernel config options
To enable the driver, please first check if you have the **VIDEO_DEV** , **MEDIA_CONTROLLER** and **VIDEO_V4L2_SUBDEV_API** Kconfig options enabled. 
Then once you enable **V4L_PLATFORM_DRIVERS** you should be able to enable **VIDEO_SUN6I_CSI** for the A31 CSI driver. For the A10/A20 CSI driver, enable **VIDEO_SUN4I_CSI**. (Provided you have the patches applied.) 
## Userspace configuration
It is recommended to use an up-to-date version of v4l-utils, as older versions, such as the one in Debian Stable (1.12.x) has some bugs, and doesn't understand all formats or knobs. 
The usage of the media controller and sub-device API means configuration of the capture options is slightly complicated. The **media-ctl** and **v4l2-ctl** are used. 
If you are using buildroot, enable **BR2_PACKAGE_LIBV4L** and **BR2_PACKAGE_LIBV4L_UTILS** in the make menuconfig to be able to use **media-ctl** and **v4l2-ctl**. media-ctl source and development have been moved to v4l-utils since June 2014. 
### Media bus and capture formats
To see the current settings of the media bus, use 
[code] 
    $ media-ctl --print-topology
    
    Media controller API version 5.1.0
    
    Media device information
    ------------------------
    driver          sun6i-csi
    model           Allwinner Video Capture Device
    serial
    bus info
    hw revision     0x0
    driver version  5.1.0
    
    Device topology
    - entity 1: sun6i-csi (1 pad, 1 link)
                type Node subtype V4L flags 0
                device node name /dev/video0
            pad0: Sink
                    <- "ov5640 1-003c":0 [ENABLED,IMMUTABLE]
    
    - entity 5: ov5640 1-003c (1 pad, 1 link)
                type V4L2 subdev subtype Sensor flags 0
                device node name /dev/v4l-subdev0
            pad0: Source
                    [fmt:UYVY8_2X8/640x480 field:none]
                    -> "sun6i-csi":0 [ENABLED,IMMUTABLE]
    
    
[/code]
On systems with the Cedrus driver enabled, the media device may not be the default one, in which case you should use 
[code] 
    $ media-ctl --device /dev/mediaN --print-topology
    
[/code]
To set the capture format (including the bus format and capture size), you specify the properties of the source pad. 
[code] 
    $ media-ctl --set-v4l2 '"ov5640 1-003c":0[fmt:UYVY8_2X8/720x480]'
    
[/code]
Here the entity name **"ov5640 1-003c"** can also be replaced with the entity ID **5**. 
This configures a capture size of 720x480 pixels with the UYVY8_2X8 bus format, which is YUV 4:2:0. See [Media Bus Formats][11302] for a list and description of formats. 
The capture resolution specified here must match what is requested by the capture application, otherwise the kernel driver will report an error and refuse to capture. 
### Sensor sub-device configuration
Sensors can have a number of control knobs that can be configured from userspace. These range from image orientation to power line frequency to test patterns. 
To see the full list of control knobs along with menu item descriptions, use 
[code] 
    $ v4l2-ctl --list-ctrls-menus
    
    User Controls
    
                           contrast (int)    : min=0 max=255 step=1 default=0 value=0 flags=slider
                         saturation (int)    : min=0 max=255 step=1 default=64 value=64 flags=slider
                                hue (int)    : min=0 max=359 step=1 default=0 value=0 flags=slider
            white_balance_automatic (bool)   : default=1 value=1 flags=update
                        red_balance (int)    : min=0 max=4095 step=1 default=0 value=0 flags=inactive, slider
                       blue_balance (int)    : min=0 max=4095 step=1 default=0 value=0 flags=inactive, slider
                           exposure (int)    : min=0 max=65535 step=1 default=0 value=885 flags=inactive, volatile
                     gain_automatic (bool)   : default=1 value=1 flags=update
                               gain (int)    : min=0 max=1023 step=1 default=0 value=248 flags=inactive, volatile
                    horizontal_flip (bool)   : default=0 value=0
                      vertical_flip (bool)   : default=0 value=0
               power_line_frequency (menu)   : min=0 max=3 default=1 value=1
                                    0: Disabled
                                    1: 50 Hz
                                    2: 60 Hz
                                    3: Auto
    
    Camera Controls
    
                      auto_exposure (menu)   : min=0 max=1 default=0 value=0 flags=update
                                    0: Auto Mode
                                    1: Manual Mode
    
    Image Processing Controls
    
                       test_pattern (menu)   : min=0 max=4 default=0 value=0
                                    0: Disabled
                                    1: Color bars
                                    2: Color bars w/ rolling bar
                                    3: Color squares
                                    4: Color squares w/ rolling bar
    
    
[/code]
Note that if the system has multiple video devices, you may need to specify which one to use: 
[code] 
    $ v4l2-ctl --device=/dev/videoN --list-ctrls-menus
    
[/code]
To set an option, use 
[code] 
    $ v4l2-ctl --set-ctrl=vertical_flip=1
    
[/code]
Or multiple options at once 
[code] 
    $ v4l2-ctl --set-ctrl=power_line_frequency=2,vertical_flip=1,horizontal_flip=1
    
[/code]
## Capturing Images
### FFMpeg
FFMpeg supports capturing from v4l2 devices. However it does not support configuration of the media bus or sub-devices. Please use the commands shown in the previous sections instead. 
To capture from the first video device, use 
[code] 
    $ ffmpeg -s WxH -i /dev/video0 output.mjpg
    
[/code]
This captures and encodes a video of W by H pixels from the first video device to an M-JPEG file. 
Note that W and H must match what you previously set with **media-ctl**. The system default is 640x480. 
If you also specified a different bus format, such as JPEG_1X8, you will need to tell FFMpeg as well, using 
[code] 
    $ ffmpeg -input_format mjpeg -s WxH -i /dev/video0 output.mjpg
    
[/code]
  

## Caveats / TODOs
### JPEG media bus format buffers
The JPEG media bus format support in the driver does not trim the returned buffer. In other words, the full buffer is passed back to userspace, with trailing zeros. This means the user will end up with enormous JPEG files without post-processing. 
There are already several JPEG parsers in the kernel. A proposal was made to combine and generalize them, which could then be used in our CSI driver to detect the end of the JPEG stream. This has not been implemented yet. 
### MIPI CSI-2
While a few Allwinner SoCs support MIPI CSI-2, details on the hardware is sparse. No one has attempted to support this yet. 
# BSP kernel supported camera's sensors table
Vendor | Part Number | Pixels | Type | Specification | Focus | AVDD | DOVDD | DVDD | AFVCC | NOTE   
---|---|---|---|---|---|---|---|---|---|---  
OmniVision | OV7670 | 0.3M | Photo/Video | 640*480@30fps  
352*176@30fps  
320*240@30fps  
176*144@30fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
OmniVision | OV2655 | 2M | Photo/Video | 1600*1200  
800*600@30fps  
640*480@30fps | Fixed focus | 2.8 | 2.8 | 1.5 | NC | Basic image can fine tune the effect   
OmniVision | OV2643 | 2M | Photo/Video | 1600*1200  
1280*760@30fps  
640*480@30fps | Fixed focus | 2.8 | 2.8 | 1.5 | NC | Module FPC needs to be as short as possible   
OmniVision | OV3660 | 3M | Photo/Video | 2048*1536@5fps  
1600*1200@5fps  
1280*720@30fps  
640*480@30fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
OmniVision | OV5640 | 5M | Photo/Video | 2592*1936@5fps  
2048*1536@5fps  
1600*1200@5fps  
1280*960@5fps  
1024*768@5fps  
1920*1080@30fps  
1280*720@30fps  
640*480@30fps | Fixed focus/Autofocus | 2.8 | 2.8 | 1.5 | 2.8~3 | 1.OV5640 drive capability module selection FPC.  
Need to be as short as possible.  
2\. Recommendation module model effects and auto-focus function is fine.  
If the election of the other modules, and does not guarantee results.   
OmniVision | OV5647 | 5M | Photo/Video | 5M@15fps  
1080p@30fps  
720p@30fps | Autofocus | 2.8 | 2.8 | 1.5 | 2.8 |   
Micron | MT9V112 | 0.3M | Photo/Video | 640*480@30fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Micron | MT9M112 | 1.3M | Photo/Video | 1280*1024@15fps  
640*512@30fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Micron | MT9M113 | 1.3M | Photo/Video | 1280*1024@15fps  
640*512@30fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Micron | MT9D112 | 1.3M | Photo/Video | 1600*1200@15fps  
640*480@30fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Galaxy Core | GC0307 | 0.3M | Video | 640*480@15fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Galaxy Core | GC0308 | 0.3M | Video | 640*480@15fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Galaxy Core | GC0309 | 0.3M | Video | 640*480@15fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Galaxy Core | GC0329 | 0.3M | Video | 640*480@15fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Galaxy Core | GT2005 | 2M | Photo/Video | 1600*1200@15fps  
1280*720@15fps  
800*600@30fps  
640*480@30fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Galaxy Core | GT2035 | 2M | Photo/Video | 1600*1200@2fps  
1280*720@10fps  
800*600@10fps  
640*480@10fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Galaxy Core | GC2015 | 2M | Photo/Video | 1600*1200@2fps  
1280*1024@2fps  
1024*768@2fps  
800*600@8fps  
640*480@8fps | Fixed focus | 2.8 | 2.8 | 2.8 | NC |   
Hynix | HI704 | 0.3M | Video | 640*480@20fps | Fixed focus | 2.8 | 2.8 | 2.8 | NC | I2C and other devices share may be a conflict   
Hynix | HI253 | 6M | Photo/Video | 1600*1200  
1280*720@15fps  
800*600@30fps  
640*480@30fps  
320*240@30fps | Fixed focus/Autofocus | 2.8 | 2.8 | 1.8 | NC |   
SETi | SIV121D | 0.3M | YUV | 640x480@30fps | Fixed focus | 2.8 | 1.8/2.8 | internal | NC | based on SIV121C datasheet   
Superpix | SP0838 | 0.3M | Video | 640*480@20fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Superpix | SP2518 | 2M | Video | 1600*1200@15fps | Fixed focus | 2.8 | 2.8 | 1.8 | NC |   
Samsung | S5K4EC | 5M | Photo/Video | 2560*[[email protected]][11303]  
2048*[[email protected]][11303]  
1920*1080@15fps  
1280*720@30fps  
640*480@30fps | Autofocus | 2.8 | 2.8 | 1.2 | 2.8~3 |   
TOSHIBA | T8ET5 | 5M | Video | 5M@15fps  
2048*[[email protected]][11303]  
1080p@30fps  
720p@30fps | Autofocus | 2.8 | 2.8 | 1.5 | 2.8 |   
## Reference
~~*[[1]][11304] Allwinnertech Wiki~~
