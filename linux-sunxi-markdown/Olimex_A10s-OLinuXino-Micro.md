# Olimex A10s-OLinuXino-Micro
Olimex A10s-OLinuXino-Micro  
---  
[![A10s-OlinuXino-MICRO-4GB-Top.jpg][40371]][40372] [][40373]  
Manufacturer |  [Olimex][40374]  
Dimensions |  101.6 _mm_ x 81.28 _mm_ 20 _mm_  
Release Date |  May 2013   
Website |  [Product Page][40375]  
Specifications   
SoC |  [A10s][40376] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  4GB (optional)   
Power |  DC 5V @ 1A   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug, 3.5mm line-in plug, HDMI, microphone by soldering wires to board   
Network |  10/100Mbps Ethernet ([Realtek RTL8201CP][40377])   
Storage |  µSD, SD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Other |  EEPROM   
Headers |  UART, JTAG, LCD, UEXT, 3x GPIO connectors   
The A10s-Olinuxino-MICRO is an [A10s][40376] based development board made by [Olimex][40378]. Like all [Olimex hardware][40378], it is fully [Open Source Hardware][40379]. 
Because the [A10s][40376] is no longer actively supported by Allwinner, this board should not be used for new designs or new projects. 
## Contents
  * [1 Identification][40380]
  * [2 Sunxi support][40381]
    * [2.1 Current status][40382]
    * [2.2 Images][40383]
    * [2.3 HW-Pack][40384]
    * [2.4 BSP][40385]
    * [2.5 Manual build][40386]
    * [2.6 Mainline kernel][40387]
  * [3 Tips, Tricks, Caveats][40388]
    * [3.1 FEL mode][40389]
    * [3.2 LCD modules][40390]
    * [3.3 Expansion ports][40391]
  * [4 Adding a serial port][40392]
  * [5 Pictures][40393]
  * [6 Also known as][40394]
  * [7 See also][40395]

# Identification
It says "A10s-OLinuXino-MICRO" on the top. It just doesn't get easier than that! 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "A10s-OLinuXino-Micro" target.
  * The .fex file can be found in sunxi-boards as [a10s-olinuxino-m.fex][40396]

Everything else is the same as the [manual build howto][40397]. 
## Mainline kernel
Use the sun5i-a10s-olinuxino-micro.dts device-tree file for the [mainline kernel][40398]. 
# Tips, Tricks, Caveats
## FEL mode
The BOOT/REC button triggers [ FEL mode][40399]. 
## LCD modules
You can attach [several Olimex LCD modules][40400] to the LCD connector (LCD_CON). 
## Expansion ports
Several expansion options are provided: 
  * [A UEXT connector][40401]. This is meant for attaching [Olimex UEXT modules][40402].
  * A 14 pin IO connector (GPIO-1).
  * A 40 pin IO connector (GPIO-2).
  * A 10 pin IO connector (GPIO-3).

# Adding a serial port
[![][40403]][40404]
[][40405]
UART connector
There is a 2.54mm pitch connector marked UART0 on the board. All you have to do is connect the leads according to our [UART howto][40406]. The pin identifiers are shown on the bottom side of the board. 
# Pictures
  * [![A10s-OlinuXino-MICRO-4GB-Top.jpg][40407]][40372]
  * [![A10s-OlinuXino-MICRO-4GB-Bottom.jpg][40408]][40409]
  * [![A10s-OlinuXino-MICRO-4GB-UART0.jpg][40410]][40404]
  * [![A10s-OlinuXino-MICRO-4GB-UART0-Bottom.jpg][40411]][40412]
  * [![A10s-OlinuXino-MICRO-4GB-Boot-Rec.jpg][40413]][40414]
  * [![A10s-OlinuXino-MICRO-4GB-Power.jpg][40415]][40416]

# Also known as
There are no rebadgers for this type of device. 
# See also
  * [Other Olimex hardware][40378]
  * [User manual][40417]
  * [Olimex github repository with all CAD files and schematics.][40418]
