# F60 Action Camera
F60 Action Camera  
---  
[![F60 Action Camera Front.jpg][18773]][18774]  
Manufacturer |  Various   
Dimensions |  60 _mm_ x 42 _mm_ x 26 _mm_  
Release Date |  October 2013   
Website |  [Device Product Page][18775]  
Specifications   
SoC |  [V3][18776] @ 1Ghz   
DRAM |  128MiB DDR3 @ 648MHz   
SPI NOR |  8MiB   
Power |  900mAh 3.7V Li-Ion battery, USB   
Features   
LCD |  320x240 (2" 4:3, ST7789V)   
Video |  HDMI (Type D - micro, EP952 encoder)   
Audio |  internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Allwinner XR819][18777])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  8.0MP (3280x2460, IMX179)   
Headers |  UART   
The F60 Action Camera is a V3-based device that ships with a 3.4 Allwinner downstream modified Linux kernel with a standalone camera interface called **camdroid**. 
## Contents
  * [1 Identification][18778]
  * [2 Sunxi support][18779]
    * [2.1 Current status][18780]
  * [3 Tips, Tricks, Caveats][18781]
    * [3.1 ADB access][18782]
    * [3.2 FEL mode][18783]
  * [4 Adding a serial port (**voids warranty**)][18784]
    * [4.1 Device disassembly][18785]
    * [4.2 Locating the UART][18786]
  * [5 Pictures][18787]
  * [6 Also known as][18788]

# Identification
This device is often marketed as a **V3 4K Action Camera**. 
The PCB has the following silkscreen marking: 
[code] 
    SL631_MAIN_V2.3
    2017-10-19
    
[/code]
# Sunxi support
## Current status
There is currently no source code available for the device in Linux and U-Boot (either upstream or downstream modified versions), thus no support is available. 
The source code from this somewhat similar board may be useful [[1]][18789]. Otherwise, it may be useful to search for the Allwinner platform number (sun8iw8p1 ?) and uboot. 
# Tips, Tricks, Caveats
## ADB access
ADB can be obtained by connecting the device via USB and selecting **Charging Mode** on it. ADB gives access to a root shell. 
## FEL mode
The boot software appears to hold when a button is pushed during boot, which is perhaps a way to trigger FEL mode. More investigation is required on that aspect. 
# Adding a serial port (**voids warranty**)
[![][18790]][18791]
[][18792]
F60 Action Camera UART pads
## Device disassembly
The first step to open the device is to remove the clipped front cover in order to access four screws that need to be removed before the device can be taken out of its case. Removing the device from its case completely requires disconnecting the LCD panel cable. Since the panel is held on the other side of the device, this can be tricky. An easy way to disconnect the panel consists in removing the glued glass protection from the other side of the device (the panel is not glued to it, only the case on the side is) and lifting the LCD panel. It can then be disconnected properly. 
## Locating the UART
The UART of the V3 SoC is exposed with two pads on the bottom side of the PCB. They are located close to the LCD panel connector, as indicated in the associated picture. Wires can be soldered to these pads and connected according to the [UART howto][18793]. 
# Pictures
  * [![F60 Action Camera Front.jpg][18794]][18774]
  * [![F60 Action Camera Top.jpg][18795]][18796]
  * [![F60 Action Camera Buttons Side.jpg][18797]][18798]
  * [![F60 Action Camera Connectors Side.jpg][18799]][18800]
  * [![F60 Action Camera PCB Top.jpg][18801]][18802]
  * [![F60 Action Camera PCB Bottom.jpg][18803]][18804]
  * [![F60 Action Camera PCB and LCD.jpg][18805]][18806]
  * [![F60 Action Camera UART.jpg][18807]][18791]

# Also known as
  * Furibee F60 Action Camera
