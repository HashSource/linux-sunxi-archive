# VE Planning
This is a page for planning the effort of the writing of a driver for the video engine in the right way (well, in the best possible way). 
  

## V4L2 codec interface
The only existent kernel framework suited for this type of hardware device is the video-for-linux [codec interface][58086]. Presentation [Video4Linux2: Path to a Standardized Video Codec API][58087] and [Other users][58088] of this same framework. 
However not without a few obstacles. 
#### Tile format
  * For the tile format specific to this video engine, V4l2 doesn't have (yet) this pixel format. Until then, as in v4l2, the pixel formats are represented as fourcc identifiers in an u32 value. It will be sufficient to define this custom tile format in the driver and user headers. [Example.][58089]

#### 256MiB limit
  * This video engine requires contiguous physical memory buffers to be located in the lower 256MiB of memory.

    ideally if possible instead of having a fixed memory region, all should be available for allocation 
  * videobuf2-dma-contig, allocates physical contiguous buffers, but to restrit to low 256M, requires _dma_declare_coherent_memory_ to be called. [Example.][58090] The declared memory region must be reserved using the generic [/reserved-memory][58091] node.
  * from outside mainline there exists also [videobuf2-cma-phys][58092] and [videobuf2-ion][58093]

#### Decoder batching
  * decoder will work notably faster when frames are batched (not one shoot mode).

#### Device nodes
  * not all combination of the aggregated pixel formats (from isp subengine, encoder, decoder) are possible.

    From this [example][58094], we can see that multiple device nodes is preferred. The use of three device nodes appears to be the most suited.
[code] 
    /dev/videoW
       isp subengine    -  raw pixel formats => raw pixel formats subset
    
    /dev/videoX
       encoder          -  raw pixel formats => bitstream formats
    
    /dev/videoY
       decoder          -  bitstream formats => raw pixel format
    
[/code]
#### No parsing in kernel
  * this video engine is a fixed function engine, this is a advantage by its simplicity, but in other ways this means that bitstream parsing can't be done by a firmware. Bitstream parsing in the kernel is not allowed.

    
  * More information from a[Linux Kernel Media Workshop][58095] where this matter was discussed, copied here for easyness.

[code] 
    13: Hugues Fruchet: Video codecs
    
        There's a need to parse bitstream fields for those codecs, but that requires complex code (10K lines). Moving it to kernel could make it unstable, as it is harsh to write those parsers without any risk of causing crashes.
        It seems to be better to put those parsers inside libv4l, using an open source license.
    
    Results:
    
        Drivers that require proprietary user space components should stay out of mainline
        Multi-format buffers could be useful here
        The hardware/firmware needs a lot of data extracted from the bitstream next to the bitstream itself. This is a custom format, so it is OK to add a new pixelformat for each of those formats. Such complex parsing should be done in userspace in libv4l2.
        If very little parsing is required (MPEG), then that can be done in the kernel instead.
        Recommendation is to start simple with e.g. just an MPEG implementation.
    
[/code]
    
  * [**Request API**][58096], is a newer still experimental addition to V4L2 and Media Controller framework. In resume, any number of controls (configuration data) can be packed in a object called _request_ , and if attached to a buffer, the driver can apply this configuration to the hardware when processing said buffer.

    
  * [Linux Kernel Summit Media WorkShop - Planning Out the Future of Media on Linux][58097]
  * [V4L2 on steroids: The Request API][58098] ([Video.][58099])
  * [Media Request API (RFC patches)][58100] [v2][58101]
  * [Report of the V4L2 Request API brainstorm meeting - Oct 10-11/2016][58102]
  * [2017 is the Year of the Linux Video Codec Drivers - Laurent Pinchart, Ideas on Board ][58103]
  * [V4L2 Jobs API WIP - a RFC follow-up to the Request API][58104]

## Way to go forward.
  * initial we can ignore that bitstream parsing is been done in the kernel, and first aim to have a working driver.

    
  * other option can be to split the driver in a common part that can be mainlined, and for each codec do as a submodule that can compiled out of tree. This also allows the distributions to choose which codecs to include.

  * this means that initially we will not worry about working for the inclusion in the mainline kernel (because the bitstream parsing will be rejected.)
  * using libv4l2 as suggested above to do the bitstream parsing in user space.

    
  * in this [paragraph][58105] is explained that libv4l2 can transparently convert between formats, when the requested format mismatch the formats supported by the hardware driver. As in V4L2 a codec bitstream is considered as in equal mode to an image format, it should be possible to also convert bitstream format to a pre-parsed bitstream format compatible with the specificities of this video engine.
  * there is also [libv4l2 plugins][58106], in which could offer a possible way to do this transparent bitstream conversion.
  * perpendicular [discussion][58107] that reaffirms the place for bitstream parsers.

## Progress status
_Detail of the conclusion of each step for each target kernel version (sunxi-3.4 / distro kernel / mainline)._
## User Land
  * Will aim to preserve the compatibility with similar users of v4l2 codec interfaces. Within its limits.
  * By the motive of the numerous video codecs apis in existence and equal mode the number of media players, the implementation of the support is outside the scope of this effort.
  * Only will be written simple programs for testing and example in how to use.

#### gstreamer
  * already includes [support][58108] for v4l2 mem2mem _decoder_ devices. [the development of video4linux decoder support][58109]

  * _encoder_ is _**work in progress**_ [Bug 728438 - v4l2: Implement a v4l2 video encoder ][58110]

#### ffmpeg
  * there were some [patches][58111] but they didn't go forward.
