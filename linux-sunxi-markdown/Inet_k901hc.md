# Inet k901hc
Inet k901hc  
---  
[![Inet k901c front.jpg][27683]][27684]  
Manufacturer |  [inet-tek][27685]  
Dimensions |  240 _mm_ x 148 _mm_ x 11.5 _mm_  
Release Date |  May 2013   
Website |  [Device Product Page][27686]  
Specifications   
SoC |  [A20][27687] @ 1 Ghz   
DRAM |  512MiB DDR3 @ 408 MHz   
NAND |  4GB   
Power |  USB charging only 5V @ 1.5A, 3100mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (9" 16:9)   
Touchscreen |  5-finger capacitive ([Focaltech FT5402DQT][27688])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][27689])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  1.3MP (640x480) front   
Other |  Accelerometer (TODO:  [Manufacturer device][27690])   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][27691] and the [New Device Page guide][27692].
## Contents
  * [1 Identification][27693]
  * [2 Sunxi support][27694]
    * [2.1 Current status][27695]
    * [2.2 Images][27696]
    * [2.3 HW-Pack][27697]
    * [2.4 BSP][27698]
    * [2.5 Manual build][27699]
  * [3 Tips, Tricks, Caveats][27700]
    * [3.1 FEL mode][27701]
  * [4 Adding a serial port (**voids warranty**)][27702]
    * [4.1 Device disassembly][27703]
    * [4.2 Locating the UART][27704]
  * [5 Pictures][27705]
  * [6 Also known as][27706]
  * [7 See also][27707]
    * [7.1 Manufacturer images][27708]

# Identification
On the back of the device, the following is printed: 
[code] 
    i-INN
    PRO 9.0 Dual Core U Black
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INET-K90-REV01
    Zeng-gc 2013-05-29
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _PRO 9.0 Dual Core U Black_
  * Build Number: _PRO_9.0_Dal_Core_U_Black.20130903_

# Sunxi support
## Current status
Awaiting patches. Linux can be booted by using boot images for a20-olinuxino_micro with script.bin from the k901c's internal flash. The USB OTG port does not work though. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _Inet_K901C_ target.
  * The .fex file can be found in sunxi-boards as [inet_k901hc.fex][27709]

Everything else is the same as the [manual build howto][27710]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][27711]. 
# Adding a serial port (**voids warranty**)
[![][27712]][27713]
[][27714]
K901C UART pads
## Device disassembly
Carefully insert your [Plastic tool][27715] between the front and back covers, and gently push the back cover outwards, until you hear the clips release. Go around the whole device. 
## Locating the UART
A set of clearly marked UART pads are available right next to the reset button and the SD-Card slot. All you have to do is solder on some wires according to our [UART howto][27716] but this is not comunicating 115200 N81. 
# Pictures
  * [![Inet k901c front.jpg][27717]][27684]
  * [![Inet k901c back.jpg][27718]][27719]
  * [![Inet k901c connectors.jpg][27720]][27721]
  * [![Inet k901c internal.jpg][27722]][27723]
  * [![Inet k901c board front.jpg][27724]][27725]

# Also known as
i-INN PRO 9.0 Dual Core U Black 
# See also
## Manufacturer images
