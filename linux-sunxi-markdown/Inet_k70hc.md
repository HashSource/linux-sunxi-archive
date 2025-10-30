# Inet k70hc
Inet k70hc  
---  
[![Inet k70hc front.jpg][27600]][27601]  
Manufacturer |  [Inet][27602]  
Dimensions |  181 _mm_ x 110 _mm_ x 9 _mm_  
Release Date |  May 2013   
Website |  [K70HC product page][27603]  
Specifications   
SoC |  [A20][27604] @ 1.2Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  8GB   
Power |  USB charging only, 3200mAh ?V Li-Ion battery   
Features   
LCD |  1024x600 (7" TN)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][27605])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][27606])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2MP (1600x1200) rear (optional)   
Other |  Accelerometer (TODO: [Manufacturer device][27607]), Bluetooth, reset button   
Headers |  UART   
## Contents
  * [1 Identification][27608]
  * [2 Sunxi support][27609]
    * [2.1 Current status][27610]
    * [2.2 Images][27611]
    * [2.3 HW-Pack][27612]
    * [2.4 BSP][27613]
    * [2.5 Manual build][27614]
  * [3 Tips, Tricks, Caveats][27615]
    * [3.1 FEL mode][27616]
    * [3.2 USB OTG port][27617]
  * [4 Adding a serial port][27618]
    * [4.1 Device disassembly][27619]
    * [4.2 Locating the UART][27620]
  * [5 Pictures][27621]
  * [6 Also known as][27622]
  * [7 See also][27623]

# Identification
In android, under Settings->About Tablet, you will find... 
For the Leliktec rebadge: 
  * Model Number: K701HC
  * Build Number: A20_K70_K701HC_*.*

For the W-Tech rebadge: 
  * Model Number: BW-0708
  * Build Number: A20_K70_K701C.* W-Tech S/N *

# Sunxi support
## Current status
Working. 
The USB OTG port totally refuses to work. This needs to be properly debugged still, perhaps this is an issue of our kernel on A20, perhaps this is just this tablets config. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "INet_K70HC" target.
  * The .fex file can be found in sunxi-boards as [inet_k70hc.fex][27624]

Everything else is the same as the [manual build howto][27625]. 
# Tips, Tricks, Caveats
## FEL mode
The back button triggers [ FEL mode][27626]. 
## USB OTG port
This device comes with only a single USB port, and has no separate power connector. It therefor is only of limited use as a standalone desktop style device, as connecting a keyboard and/or mouse will only work as long as the battery lasts. 
[![][27627]][27628]
[][27629]
K70HC UART pads.
# Adding a serial port
## Device disassembly
Remove the two screws on the side with the connectors. 
Now gently insert your [plastic tool][27630] in the space between the connector face and the back. All of the clip hooks are on the back plate, so you need to gently force the edge of the back plate inwards, while the edge of the front side of the device needs to be gently forced out. You should soon hear the plastic clips popping. Be careful when removing the back, as the speaker is lightly glued to it. 
## Locating the UART
There are nice pads labelled "GND", "RX" and "TX" below the SD card. All you have to do is [solder on some wires][27631]. 
# Pictures
  * [![Inet k70hc front.jpg][27632]][27601]
  * [![Inet k70hc back.jpg][27633]][27634]
  * [![Inet k70hc board.jpg][27635]][27636]
  * [![Perfeo7510hd back cover.jpg][27637]][27638]
  * [![Perfeo 7510hd back cover removed.jpg][27639]][27640]
  * [![Perfeo 7510hd mainboard.jpg][27641]][27642]
  * [![Perfeo7510hd wifi module rtl8188e.jpg][27643]][27644]
  * [![Perfeo7510hd booting debian wheezy.jpg][27645]][27646]

# Also known as
  * [LélikTec Avalon 7HD][27647] (single camera)
  * [Perfeo 7510-HD][27648] (dual camera, Kingston DDR3 chips running @ 408 MHz)
  * [CCE Motion Hold TR72][27649] (dual camera)
  * It also seems to be sold by the "Cash & Carry" group in Mauritius where it carries "W-Tech" on the back.

# See also
