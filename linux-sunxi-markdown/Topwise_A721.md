# Topwise A721
Topwise A721  
---  
[![Device front.jpg][55355]][55356]  
Manufacturer |  [Topwise][55357]  
Dimensions |  198 _mm_ x 117 _mm_ x 9.8 _mm_  
Release Date |  February 2012   
Website |  Missing product page.   
Specifications   
SoC |  [A10][55358] @ 1Ghz   
DRAM |  512MiB @ 360MHz   
NAND |  4/8GB   
Power |  DC 5V @ ?A, Unknown mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive/resistive ([Manufacturer device][55359] FIXME)   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CTV][55360])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Domintech DMARD06][55361])   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][55362] and the [New Device Page guide][55363].
The "MID" formfactor was very popular in 2012. Therefor there are probably some variations with respect to the amount of NAND, camera and wifi modules. 
There is some confusion, as to which device this is. The layout of the buttons and connectors seems to be compatible with the [A710][55364], but the board is crucially different. 
In 2012, this board was also sold standalone, as the Gooseberry. The gooseberry forum now is abandoned and full of spam. 
## Contents
  * [1 Identification][55365]
  * [2 Sunxi support][55366]
    * [2.1 Current status][55367]
    * [2.2 Images][55368]
    * [2.3 HW-Pack][55369]
    * [2.4 BSP][55370]
    * [2.5 Manual build][55371]
  * [3 Tips, Tricks, Caveats][55372]
    * [3.1 FEL mode][55373]
  * [4 Adding a serial port (**voids warranty**)][55374]
    * [4.1 Device disassembly][55375]
    * [4.2 Locating the UART][55376]
  * [5 Pictures][55377]
  * [6 Also known as][55378]
  * [7 See also][55379]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: MID
  * Build Number: 20120323-A721.0.5.3

# Sunxi support
## Current status
Only the gooseberry board has been properly verified. 
## Images
## HW-Pack
## BSP
[BSP][55380] works properly and is able to prepare bootable SD cards and [LiveSuit][55381] images, as tested on gooseberry board. 
## Manual build
**Warning: The below instructions are for the standalone gooseberry board, they might not be suited for an actual A721 tablet.**
  * For building u-boot, use the "Gooseberry_A721" target.
  * The .fex file can be found in sunxi-boards as [gooseberry_a721.fex][55382]

Everything else is the same as the [manual build howto][55383]. 
# Tips, Tricks, Caveats
## FEL mode
The Volume+ button triggers [ FEL mode][55384]. 
# Adding a serial port (**voids warranty**)
[![][55385]][55386]
[][55387]
A721 UART pads
## Device disassembly
Provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped.
## Locating the UART
On the back of the board, there are pads marked "UART0-TX" and "UART0-RX". All you have to do is solder on some wires according to our [UART howto][55388]. 
# Pictures
Take some pictures of your device, [ upload them][55389], and add them here.
  * [![Device front.jpg][55390]][55356]
  * [![Device back.jpg][55391]][55392]
  * [![Device buttons 1.jpg][55393]][55394]
  * [![Device buttons 2.jpg][55395]][55396]
  * [![A721 Gooseberry front.jpg][55397]][55398]
  * [![A721 Gooseberry back.jpg][55399]][55400]
  * [![][55401]][55402]
Inside front 
  * [![][55403]][55404]
Inside back 
  * [![LY-F1 A721.jpg][55405]][55406]

# Also known as
There are probably tons of rebadgers, as this formfactor was very popular and got produced by several manufacturers. 
Some possible suspects are: 
  * Lyric F1 (LY-F1), which probably also shipped with an [A710][55364] board.
  * TomTop c1315
  * DVC z7

  * The bare board was also sold as the Gooseberry.

# See also
  * [A710][55364]: has the same packaging, but a different board inside.
