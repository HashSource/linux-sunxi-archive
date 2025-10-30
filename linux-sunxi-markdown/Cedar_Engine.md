# Video Engine
(Redirected from [Cedar Engine][12178])
 
This page is related to the hardware, for software see: 
  * **[Cedrus][12181]** The project for a 100% libre open source driver and software.
  * **[CedarX][12182]** Allwinner's media framework software libraries.

# What should this hardware block be called?
Video Engine is the plain name used by Allwinner for the hardware block responsible for the task of decoding and encoding video formats. 
## Naming
There is some confusion around how to name this video engine, with the principal reason been the non-existent clear branding by Allwinner. 
  * **CedarX**

    is the name given to the proprietary **software** libraries for video and audio de-/encoding (CedarV + CedarA).
  * **Cedar Engine**

    is found in the kernel driver (/dev/cedar_dev) [source code][12183] where it has been directly referred to as "cedar engine" in [error/information messages][12184] and [internal variables][12185]. Take note that this is the kernel driver that was made for the proprietary libraries that already existed in Melis OS, were the media player application goes by the name ["cedar"][12186].
  * **MACC** \- **M** edia **ACC** elerate video engine

    is also found in the kernel driver and [respective headers][12187], where the [mmio area (registers)][12188] is referenced by _macc_ as a prefix for the definition of the [register base address][12189].
  * **VE** \- Video Engine

    is the most common name used in all the places for this hardware block. It is believed that **VE** is a short form of **VCE** (Video Codec Engine) to be in accordance with ACE (Audio Codec Engine) and is also the best generic name to describe this type of hardware block.
#### Naming in the datasheets and user manuals.
SOC | features label | block diagram | related registers   
---|---|---|---  
A10 | VPU | VE | VE   
A10s | VPU | VPU | VE   
A13 | VPU | VPU | VE   
A20 | Video Engine (Phoenix 3.0) | Video Engine | VE   
A23 | Video Engine | Video Engine | VE   
A31 | Video Engine | Video Engine | VE   
A31s | Video Engine | Video Engine | VE   
A33 | Video Engine | Video Engine | VE   
A80 | Video Engine | Video Engine | VE   
A83T | Video Engine | _claims decoder/encoder is part of the GPU block_ | VE   
H3 | Video Engine | Video Engine | VE   
A64 | Video Engine | Video Engine | VE
