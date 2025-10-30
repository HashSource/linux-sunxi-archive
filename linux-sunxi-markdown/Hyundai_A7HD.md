# Hyundai A7HD
Hyundai A7HD  
---  
[![A7hd front.jpeg][24505]][24506]  
Manufacturer |  [Hyundai Digital (defunct)][24507]  
Dimensions |  174 _mm_ x 118 _mm_ x 8.9 _mm_  
Release Date |  April 2012   
Website |  [Product Page(defunct)][24508]  
Specifications   
SoC |  [A10][24509] @ 1Ghz   
DRAM |  1GiB DDR3 @ 360MHz   
NAND |  8GB   
Power |  DC 5V, 3400mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" 17:10 FFS-IPS)   
Touchscreen |  5-point capacitive ([Goodix GT801][24510])   
Video |  HDMI (Type C - mini)   
Audio |  2.5mm headphone plug, built-in microphone, HDMI   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][24511])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][24512] FIXME)   
Headers |  UART   
## Contents
  * [1 Identification][24513]
  * [2 Sunxi support][24514]
    * [2.1 Current status][24515]
    * [2.2 Images][24516]
    * [2.3 HW-Pack][24517]
    * [2.4 BSP][24518]
    * [2.5 Manual build][24519]
    * [2.6 Mainline kernel][24520]
  * [3 Tips, Tricks, Caveats][24521]
    * [3.1 FEL mode][24522]
    * [3.2 Flaky WiFi][24523]
    * [3.3 Powerdown with UART attached][24524]
  * [4 Adding a serial port (**voids warranty**)][24525]
    * [4.1 Device disassembly][24526]
    * [4.2 Locating the UART][24527]
  * [5 Pictures][24528]
  * [6 Also known as][24529]
  * [7 See also][24530]

# Identification
On the back of the device, the following is printed: 
[code] 
    S7-S
    ... With Android
    Designed by Lovendesign in China
    Assembled in China
[/code]
The PCB has the following silkscreened on it: 
[code] 
    RK-S7S01-V1.2_20120215
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _A7 HD_
  * Build Number: _RKS7S01_A7HD_20120412_

# Sunxi support
## Current status
Supported. Touchscreen unknown. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _hyundai_a7hd_ target.
  * The .fex file can be found in sunxi-boards under as [hyundai_a7hd.fex][24531]

Everything else is the same as the [manual build howto][24532]. 
## Mainline kernel
Use the sun4i-a10-hyundai-a7hd.dts device-tree file for the [mainline kernel][24533]. 
# Tips, Tricks, Caveats
## FEL mode
There are 4 buttons on the A7HD, the left one is the powerbutton, and any of the three other buttons can be used to trigger FEL mode, as described in the [FEL mode howto][24534]. 
## Flaky WiFi
The A7HD has a known issue with less than ideal WiFi reception. The fix is to re-route the WiFi antenna, but in order to do that you need to partly disassemble your device and remove the back. 
Further information can be found in [this android forum post][24535]. 
## Powerdown with UART attached
The A7HD suffers from the same problem as other A10 devices. When you power down with the UART still attached, some power continues to flow into the device, and it will not power down properly. So disconnect the UART if you need to do a proper power down. 
# Adding a serial port (**voids warranty**)
[![][24536]][24537]
[][24538]
A7HD UART pads
## Device disassembly
Carefully insert your [plastic tool][24539] into the long edges, and push the plastic outwards while pushing the aluminium back plate inward, and work the whole 2 long sides. Now insert your plastic tool into the short edge, and push the aluminium backplate outwards. 
## Locating the UART
There are some pre-tinned pads available on the front side of the motherboard, right next to the SoC. All you have to do is attach some wires according to our [UART howto][24540]. Use very thin wires to export this UART, as otherwise you will get pressure points on your LCD and your back cover might not fit properly anymore. 
# Pictures
  * [![A7hd front.jpeg][24541]][24506]
  * [![A7hd back.jpeg][24542]][24543]
  * [![A7hd top.jpeg][24544]][24545]
  * [![A7hd right.jpeg][24546]][24547]
  * [![A7hd bottom.jpeg][24548]][24549]
  * [![Hyundai a7hd board front.jpg][24550]][24551]
  * [![Hyundai a7hd board back.jpg][24552]][24553]

# Also known as
  * The most common name is Hyundai A7HD, even though the motherboard states RK-S7S01
  * Sold as [Cherry Mobility M-728][24554] by the Kruidvat store chain in Holland.
  * [Yarvik GoTab Ion 7" (TAB275)][24555]

# See also
[Hyundai A7HD online Review][24556]
