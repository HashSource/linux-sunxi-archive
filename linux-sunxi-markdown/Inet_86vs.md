# Inet 86vs
Inet 86vs  
---  
[![MID705 front.jpg][26464]][26465]  
Manufacturer |  [iNet technology][26466]  
Dimensions |  190 _mm_ x 115 _mm_ x 9 _mm_  
Release Date |  July 2013   
Website |  [86VS Product Page][26467]  
Specifications   
SoC |  [A13][26468] @ 1GHz   
DRAM |  512MiB DDR3 @ 408MHz   
NAND |  4GB   
Power |  5V @ ?A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][26469])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][26470])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][26471] FIXME), reset button   
Headers |  UART   
## Contents
  * [1 Identification][26472]
  * [2 Sunxi support][26473]
    * [2.1 Current status][26474]
    * [2.2 Images][26475]
    * [2.3 HW-Pack][26476]
    * [2.4 BSP][26477]
    * [2.5 Manual build][26478]
  * [3 Tips, Tricks, Caveats][26479]
    * [3.1 FEL mode][26480]
  * [4 Adding a serial port (**voids warranty**)][26481]
    * [4.1 Device disassembly][26482]
    * [4.2 Locating the UART][26483]
  * [5 Pictures][26484]
  * [6 Also known as][26485]
  * [7 See also][26486]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: MID705
  * Build Number: A13_86VS_M758C1_1304117.20130629

# Sunxi support
## Current status
Supported. 
WiFi reception is very poor probably due to bad antenna. 
Tested: 
  * boot from SD card - mmc0
  * PMU
  * original nand flash content access
  * LCD
  * USB OTG (ethernet gadget)
  * USB HOST (wifi)
  * tablet keys

Don't work: 
  * touchscreen
  * networking

Untested (should work): 
  * mali
  * cedar

Detected by kernel but needs testing: 
  * rtc
  * USB WiFi
  * audio

Unknown: 
  * accelerometer
  * camera

## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the **INet_86VS** target.
  * The .fex file can be found in sunxi-boards as [inet_86.fex][26487]

Everything else is the same as the [manual build howto][26488]. 
# Tips, Tricks, Caveats
## FEL mode
[![][26489]][26490]
[][26491]
u-boot button pads between the battery (red and black) and WiFi antenna (gray) wires   
u-boot test pads below WiFi subboard
The VOL+ button triggers [ FEL mode][26492]. 
Alternatively, there is a pad labeled **u-boot** near the wifi. Connecting this to ground also triggers [ FEL mode][26492]. Pads for a UBOOT button are also available on the board. 
# Adding a serial port (**voids warranty**)
[![][26493]][26494]
[][26495]
UART pads (under the plastic)
Some pads are available on the board, but they are multiplexed with the SD card. So use a [MicroSD Breakout][26496] board. The ones from Sparkfun or DX should work with the cover on, but you have to remove the back cover to attach the cubietech one. 
## Device disassembly
Be careful to first remove the SD Card. 
The tablet has screws next to the connectors. The board is on the display part and the bottom cover is removed. Remove the screws and pry the bottom cover open with your [plastic tool][26497]. 
Make sure the USB port is inserted into the cover first when reassembling. 
## Locating the UART
[UART][26498] is marked on the bottom of the PCB (between the PCB and display) and on the top under the tape holding ctp connector. Both connect to the SD slot so you can as well use a SD breakout board. The FEX file does not enable UART. 
UART1 pins are used for CSI and connected to a 24pin 0.5mm pitch FFC connector which is used for camera. Probing with a multimeter confirms that the console pins seem to be connected somewhere around the middle of the connector. The pitch is the same as IDE ZIF connector but IDE is 40pin. 
It is possible to use a [generic ffc][26499] and an [IDE ZIF to 3.5" adaptor][26500] to connect to the pins routed to CSI. I can confirm using the u-boot gpio command that the pins actually connect to the ide connector when the cable is inserted properly but I cannot get the console working. Unfortunately the 24pin cable gets loose easily in 40pin connector. 
# Pictures
  * [![MID705 front.jpg][26501]][26465]
  * [![Mid705 back.jpg][26502]][26503]
  * [![MID705 buttons.jpg][26504]][26505]
  * [![Manta MID705 pcb top.jpg][26506]][26507]
  * [![Manta MID705 board bottom.jpg][26508]][26509]
  * [![Manta MID705 board bottom detail1.jpg][26510]][26511]
  * [![Manta MID705 board bottom detail2.jpg][26512]][26513]
  * [![Manta MID705 chips1.jpg][26514]][26490]
  * [![Manta MID705 chips2.jpg][26515]][26516]
  * [![Manta MID705 display cable bottom.jpg][26517]][26518]
  * [![Manta MID705 display cable top.jpg][26519]][26520]
  * [![Manta MID705 pcb battery.jpg][26521]][26522]
  * [![Manta MID705 pcb top detail.jpg][26523]][26524]

# Also known as
Rev1.0 was marketed as 
  * [Manta MID701][26525] ([Device Disassembly][26526])
  * [Polaroid MIDC407][26527]

Rev2.0 (documented) was sold as: 
  * [Manta MID705][26528]

# See also
