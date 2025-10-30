# Inet k100c
Inet k100c  
---  
[![Inet k100c front.jpg][27441]][27442]  
Manufacturer |  [Inet][27443]  
Dimensions |  261 _mm_ x 165 _mm_ x 12 _mm_  
Release Date |  April 2013   
Website |  [Missing Product Page][27444]  
Specifications   
SoC |  [A20][27445] @ 1Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  8GB   
Power |  DC 5V @ 2A, 6000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (10.1" 16:9)   
Touchscreen |  capacitive ([FocalTech FT5402DQT][27446])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, mic, stereo speakers   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][27447])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2MP (1920x1080) back   
Other |  Accelerometer (TODO: [Manufacturer device][27448])   
Headers |  UART   
## Contents
  * [1 Identification][27449]
  * [2 Sunxi support][27450]
    * [2.1 Current status][27451]
    * [2.2 Images][27452]
    * [2.3 HW-Pack][27453]
    * [2.4 BSP][27454]
    * [2.5 Manual build][27455]
  * [3 Tips, Tricks, Caveats][27456]
    * [3.1 FEL mode][27457]
    * [3.2 LVDS panel][27458]
  * [4 Adding a serial port (**voids warranty**)][27459]
    * [4.1 Device disassembly][27460]
    * [4.2 Locating the UART][27461]
  * [5 Pictures][27462]
  * [6 Also known as][27463]
  * [7 See also][27464]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: MID
  * Build Number: K100C-L1-D35-20130920

# Sunxi support
## Current status
  * Basic u-boot and kernel works.
  * The LVDS panel works if a clock is added in fex file.
  * Touch chip (focaltech ft0402) is initialized and i2c irq seems to work, but no valid data is present. With evtest garbage data appears when touching screen, but no valid coordinates.

## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "K1001L1C" target.
  * The .fex file can be found in sunxi-boards as [k1001l1c.fex][27465]

Everything else is the same as the [ Manual build howto][27466]. 
# Tips, Tricks, Caveats
## FEL mode
The back button triggers [ FEL mode][27467]. 
[![][27468]][27469]
[][27470]
UART pads
## LVDS panel
TODO.
# Adding a serial port (**voids warranty**)
## Device disassembly
Remove the 2 screws on the connector side. The screen edge extends beyond the connectors, and with the device lying on its display, gently push the outer rim out with your [plastic tool][27471]. You will soon hear the clamps pop. 
## Locating the UART
There are clearly labeled pads, on the top left edge, near the camera, you just need to solder on some wires. For more info, refer to the [UART howto][27472]. 
# Pictures
  * [![Inet k100c front.jpg][27473]][27442]
  * [![Inet k100c back.jpg][27474]][27475]
  * [![Inet k100c connectors.jpg][27476]][27477]
  * [![Inet k100c buttons.jpg][27478]][27479]
  * [![Inet k100c innards.jpg][27480]][27481]
  * [![Inet k100c board top.jpg][27482]][27483]

# Also known as
  * The motherboard is named Inet K100, and the variant shown here is a K100-C (from the sticker on the top of the board).
  * GD Ippo K1001
  * Noname or iRulu K1001L1
  * Also sometimes called CF-66
  * Serioux Surya Fun SMO10DC

# See also
  * [Yones Toptech BD1078][27484]: same case, different board.
