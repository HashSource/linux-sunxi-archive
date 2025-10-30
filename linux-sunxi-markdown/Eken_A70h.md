# Eken A70h
Eken A70h  
---  
[![A70h outer front.JPG][17832]][17833]  
Manufacturer |  [Eken][17834]  
Dimensions |  239 _mm_ x 147 _mm_ x 11.5 _mm_  
Release Date |  November 2013   
Website |  [Eken X73 product page][17835]  
Specifications   
SoC |  [A23][17836] @ XGhz   
DRAM |  512MiB DDR3 @ XMHz   
NAND |  8GB   
Power |  DC 5V @ 3A, 2500mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  X-finger capacitive ([Silead GSL1680][17837])   
Video |  LCD only   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([ device][17838])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0,3MP (VGA) (640x480) front, 0,3MP (640x480) rear, LED flash   
Other |  Reset button, Accelerometer (TODO: [Manufacturer device][17839])   
Headers |  UART, I2C   
This page needs to be properly filled according to the [New Device Howto][17840] and the [New Device Page guide][17841].
## Contents
  * [1 Identification][17842]
  * [2 Sunxi support][17843]
    * [2.1 Current status][17844]
    * [2.2 Images][17845]
    * [2.3 HW-Pack][17846]
    * [2.4 BSP][17847]
    * [2.5 Manual build][17848]
  * [3 Tips, Tricks, Caveats][17849]
    * [3.1 FEL mode][17850]
  * [4 Adding a serial port (**voids warranty**)][17851]
    * [4.1 Device disassembly][17852]
    * [4.2 Locating the UART][17853]
  * [5 Pictures][17854]
  * [6 Also known as][17855]
  * [7 See also][17856]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: A70H
  * Build Number: polaris_a70H-eng 4.2.2 JDQ39 20131228 test-keys

This image matches the android image used on the [ Ippo Q8H v2][17857], which has a different case design. 
# Sunxi support
## Current status
Like all things A23, this hardware is not supported. It is however a prime target for development. For more information, check [ the Allwinner A23 SoC page][17836]. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][17858]

Everything else is the same as the [manual build howto][17859]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][17860]. 
# Adding a serial port (**voids warranty**)
[![][17861]][17862]
[][17863]
DEVICE UART pads
## Device disassembly
Gently push the back cover outwards from the screen with your [plastic tool][17864]. You should soon feel the clips pop. When closing back up, replace the connector side first. 
## Locating the UART
Verify the information below according to our [UART howto][17865].
There are 2 pads right next to the SoC. The one closest to the SoC is RX/TX, the other is RX/TX. Attach some wires according to our [UART howto][17865]. 
# Pictures
  * [![A70h outer front.JPG][17866]][17833]
  * [![A70h outer back.JPG][17867]][17868]
  * [![A70h outer side.JPG][17869]][17870]
  * [![A70h innards.JPG][17871]][17872]
  * [![A70h inner top.JPG][17873]][17874]
  * [![A70h inner back.JPG][17875]][17876]

# Also known as
This hardware is sold under many guises. If it is claimed to be an A13 tablet but with a 4.2.2 android, then chances are that it is an A23 one instead. 
Examples: 
  * P100
  * A20h
  * Eken A70H
  * Eken X73

These are frequently mentioned: 
  * A20x
  * [A70x][17877]
  * Q88 Pro

But likely they are [A70x][17877]. Note the micro HDMI port between the micro and normal USB ports on the [A70x][17877]
# See also
  * [Ippo q8h][17878]
