# Zeki TB782B
Zeki TB782B  
---  
[![TB782B front.jpg][64163]][64164]  
Manufacturer |  [Zeki][64165]  
Dimensions |  196 _mm_ x 122 _mm_ x 13 _mm_  
Release Date |  June 2012   
Website |  [Product page][64166]  
Specifications   
SoC |  [A10][64167] @ 1Ghz   
DRAM |  1GB DDR3 @ xxxMHz   
NAND |  8GB NAND   
Power |  DC 5V @ 3A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  7" 800x480   
Touchscreen |  5-point capacitive multi-touch ([Manufacturer device][64168] FIXME)   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI   
Network |  WiFi 802.11 b/g/n   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front-facing   
Other |  Accelerometer ([Manufacturer device][64169] FIXME)   
Headers |  UART, JTAG, I2C, USB2.0 host   
This page needs to be properly filled according to the [New Device Howto][64170] and the [New Device Page guide][64171].
## Contents
  * [1 Identification][64172]
  * [2 Sunxi support][64173]
    * [2.1 Current status][64174]
    * [2.2 Images][64175]
    * [2.3 HW-Pack][64176]
    * [2.4 BSP][64177]
    * [2.5 Manual build][64178]
  * [3 Tips, Tricks, Caveats][64179]
    * [3.1 FEL mode][64180]
  * [4 Adding a serial port (**voids warranty**)][64181]
    * [4.1 Device disassembly][64182]
    * [4.2 Locating the UART][64183]
  * [5 Pictures][64184]
  * [6 Also known as][64185]
  * [7 See also][64186]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: TB782B
  * Build Number: A10_sun4i_crane *

# Sunxi support
## Current status
No patches have been submitted. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][64187]

Everything else is the same as the [manual build howto][64188]. 
# Tips, Tricks, Caveats
## FEL mode
There is a pinhole on right side that triggers [ FEL mode][64189]. 
# Adding a serial port (**voids warranty**)
[![][64190]][64191]
[][64192]
TB782B UART pads
## Device disassembly
Start from the top left area. gently insert your [plastic tool][64193] into the gap and go around the complete tablet counter-clockwise. there are no screws holding the tablet in place and no ribbons to be careful of. 
## Locating the UART
There pads to the immediate left of the SoC are RX and TX, just solder on some wires according to the [UART howto][64194]. 
# Pictures
This device urgently needs a set of decent pictures, as the first set was taken rather hastily and was never steady. 
  * [![TB782B front.jpg][64195]][64164]
  * [![Device back.jpg][64196]][64197]
  * [![Device buttons 1.jpg][64198]][64199]
  * [![Device buttons 2.jpg][64200]][64201]
  * [![TB782B board front.jpg][64202]][64203]
  * [![TB782B board back.jpg][64204]][64205]

# Also known as
# See also
