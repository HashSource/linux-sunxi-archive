# Smallart Uhost1
Smallart Uhost1  
---  
[![Smallart UHOST.jpg][51034]][51035]  
Manufacturer |  [Smallart][51036]  
Dimensions |  98 _mm_ x 40 _mm_ x 13 _mm_  
Release Date |  May 2012   
Website |  [Uhost1 product page][51037]  
Specifications   
SoC |  [A10][51038] @ 1Ghz   
DRAM |  1GB DDR3 @ 360MHz   
NAND |  4GB   
Power |  USB   
Features   
Video |  HDMI (Type A - male)   
Audio |  3.5mm microphone plug, HDMI, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][51039])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  1 USB2.0 Host   
This page needs to be properly filled according to the [New Device Howto][51040] and the [New Device Page guide][51041].
## Contents
  * [1 Identification][51042]
  * [2 Sunxi support][51043]
    * [2.1 Current status][51044]
    * [2.2 Images][51045]
    * [2.3 HW-Pack][51046]
    * [2.4 BSP][51047]
    * [2.5 Manual build][51048]
  * [3 Tips, Tricks, Caveats][51049]
    * [3.1 FEL mode][51050]
    * [3.2 USB host port pins][51051]
  * [4 Adding a serial port (**voids warranty**)][51052]
    * [4.1 Device disassembly][51053]
    * [4.2 Locating the UART][51054]
  * [5 Pictures][51055]
  * [6 Also known as][51056]
  * [7 See also][51057]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings. The device's exterior is black and does not carry any identification of the manufacturer. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

The PCB has the following silkscreened nearby the HDMI male connector: 
  * Uhost U1a:

[code] 
    Smallart
    SA-A10-U1-V4.0
    2012-06-20
    
[/code]
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "uhost_u1a" target.
  * The .fex file can be found in sunxi-boards as [uhost_u1a.fex][51058]

Everything else is the same as the [manual build howto][51059]. 
# Tips, Tricks, Caveats
## FEL mode
There is a button that might trigger FEL mode.
## USB host port pins
There is a 4 pin header on the mainboard, which seems to be a usb host port. A 2.4GHz wireless module is sometimes plugged there for the "fly mouse". Pin-out is currently unknown. 
# Adding a serial port (**voids warranty**)
[![][51060]][51061]
[][51062]
DEVICE UART pads
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped.
## Locating the UART
On the backside of the board, there is a group of 4 test pads. RX/TX are bound to be one of those. For more information on finding them, check the [UART howto][51063]. 
# Pictures
  * [![Device front.jpg][51064]][51065]
  * [![Device back.jpg][51066]][51067]
  * [![Device buttons 1.jpg][51068]][51069]
  * [![Device buttons 2.jpg][51070]][51071]
  * [![K-A10 PCBA front .JPG][51072]][51073]
  * [![K-A10 PCBA back .JPG][51074]][51075]

# Also known as
  * Uhost U1a (with PCB labelled as SA-A10-U1-V4.0 2012-06-20)
  * Oval Elephant
  * Joy-it JT-SmartPC01
  * Amerry Android Stick 1.0
  * TVPeCee MMS-864.wifi+

# See also
  * [CNX-Software hands-on review][51076]
