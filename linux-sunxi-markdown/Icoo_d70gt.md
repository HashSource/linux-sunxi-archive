# Icoo d70gt
Icoo d70gt  
---  
[![Device front.jpg][25476]][25477]  
Manufacturer |  [Icoo][25478]  
Dimensions |  193 _mm_ x 120 _mm_ x 12 _mm_  
Release Date |  April 2012   
Website |  [Product Page][25479]  
Specifications   
SoC |  [A10][25480] @ 1Ghz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  4/8/16GB   
Power |  DC 5V @ ?A, 3500mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" X:Y)   
Touchscreen |  5-finger capacitive ([Goodix GT801][25481])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][25482])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  1.3MP (1280x1024) front   
Other |  Accelerometer ([Freescale MMA7660][25483])   
This page needs to be properly filled according to the [New Device Howto][25484] and the [New Device Page guide][25485].
## Contents
  * [1 Identification][25486]
  * [2 Sunxi support][25487]
    * [2.1 Current status][25488]
    * [2.2 Images][25489]
    * [2.3 HW-Pack][25490]
    * [2.4 BSP][25491]
    * [2.5 Manual build][25492]
  * [3 Tips, Tricks, Caveats][25493]
    * [3.1 FEL mode][25494]
  * [4 Adding a serial port (**voids warranty**)][25495]
    * [4.1 Device disassembly][25496]
    * [4.2 Locating the UART][25497]
  * [5 Pictures][25498]
  * [6 Also known as][25499]
  * [7 See also][25500]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

# Sunxi support
## Current status
No patches have been submitted and the board is not supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][25501]

Everything else is the same as the [manual build howto][25502]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][25503]. 
# Adding a serial port (**voids warranty**)
[![][25504]][25505]
[][25506]
DEVICE UART pads
## Device disassembly
The mainboard and battery are tied to the back cover, so be careful when opening this device . Use your [[Plastic_tool|plastic tool] to gently push the edge of the bottom cover outwards, you should soon hear clips releasing. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][25507].
# Pictures
Take some pictures of your device, [ upload them][25508], and add them here.
  * [![Device front.jpg][25509]][25477]
  * [![Device back.jpg][25510]][25511]
  * [![Device buttons 1.jpg][25512]][25513]
  * [![Device buttons 2.jpg][25514]][25515]
  * [![Icoo-d70gt-board.jpg][25516]][25517]
  * [![Device board back.jpg][25518]][25519]
  * [![Icoo-d70gt-openwebos1.jpg][25520]][25521]

# Also known as
The board was developed by Shenzhen Sochips Technology limited, and is called the Sochips SC3061. No other references turn up on the internet but the Icoo D70GT. 
# See also
