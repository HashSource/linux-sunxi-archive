# HDB MID S906
HDB MID S906  
---  
[![Mid s906.jpg][23499]][23500]  
Manufacturer |  [HengBiDa (HBD)][23501]  
Dimensions |  240 _mm_ x 115 _mm_ x 12 _mm_  
Release Date |  April 2013   
Website |  [Reseller Product Page][23502]  
Specifications   
SoC |  [A20][23503] @ 1Ghz   
DRAM |  1GB DDR3 @ 432MHz   
NAND |  8GB   
Power |  DC 5V @ 2A, 4000mAh battery.   
Features   
LCD |  800x480 (9" 16:9)   
Touchscreen |  capacitive ([Goodix GT911][23504])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][23505])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 1.9MP (1600x1200) rear   
Other |  Accelerometer ([Sensortek STK8312][23506])   
Headers |  UART   
## Contents
  * [1 Identification][23507]
  * [2 Sunxi support][23508]
    * [2.1 Current status][23509]
    * [2.2 Images][23510]
    * [2.3 HW-Pack][23511]
    * [2.4 BSP][23512]
    * [2.5 Manual build][23513]
  * [3 Tips/Tricks][23514]
    * [3.1 FEL mode][23515]
  * [4 Adding a serial port][23516]
    * [4.1 Device disassembly][23517]
    * [4.2 Locating the UART][23518]
  * [5 Pictures][23519]
  * [6 Similar devices][23520]
  * [7 See also][23521]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: SoftwinerEvb
  * Build Number: s906_dbl_V1.1.3_20130625_(0+614_

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "HBD_MID_S906" target.
  * The .fex file can be found in sunxi-boards as [hbd_mid_s906.fex][23522]

Everything else is the same as the [manual build howto][23523]. 
# Tips/Tricks
## FEL mode
The vol- button triggers [ FEL mode][23524]. 
# Adding a serial port
[![][23525]][23526]
[][23527]
MID S906 UART pads
## Device disassembly
Remove the two screws on the side with the connectors. 
Careful insert your [plastic tool][23528] in the space between the USB port and the back cover. Then, gently lead the tool to the edge toward the camera. You should soon hear the clips popping. Keep a plastic tool from edge to edge, while the back cover comes off. 
## Locating the UART
As shown, there are some small pads next to the SD slot. All you have to do is [solder on some wires][23529]. 
# Pictures
  * [![Mid S906 front.jpg][23530]][23531]
  * [![Mid S906 back.jpg][23532]][23533]
  * [![Mid S906 side.jpg][23534]][23535]
  * [![Mid S906 board.jpg][23536]][23537]

# Similar devices
# See also
