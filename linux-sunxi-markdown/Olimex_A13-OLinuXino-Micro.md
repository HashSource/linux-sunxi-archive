# Olimex A13-OLinuXino-Micro
Olimex A13-OLinuXino-Micro  
---  
[![A13-OLinuXino-Micro-frontside.jpg][40458]][40459]  
Manufacturer |  [Olimex][40460]  
Dimensions |  100 _mm_ x 85 _mm_ x 20 _mm_  
Release Date |  November 2012   
Website |  [Product Page][40461]  
Specifications   
SoC |  [A13][40462] @ 1Ghz   
DRAM |  256MiB DDR3 @408MHz ([H5TQ2G63BFR-H9C][40463])   
Power |  DC 5V @ 1A   
Features   
Video |  VGA   
Audio |  3.5mm headphone plug   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART, JTAG, LCD. UEXT, 2x GPIO expansions ports.   
This page needs to be properly filled according to the [New Device Howto][40464] and the [New Device Page guide][40465].
The Olimex A13-OLinuXino-Micro is a shrunk down, cheaper version of the [A13-OLinuXino][40466]. The differences against the A13-OLinuXino are that it has half the ram, a single USB Host port, only u-boot and reset buttons, no RTC, battery connector, NAND or Wifi. As with all [ Olimex Devices][40467] this board is [Open Source Hardware][40468]. 
## Contents
  * [1 Identification][40469]
  * [2 Sunxi support][40470]
    * [2.1 Current status][40471]
    * [2.2 Images][40472]
    * [2.3 HW-Pack][40473]
    * [2.4 BSP][40474]
    * [2.5 Manual build][40475]
    * [2.6 Mainline kernel][40476]
  * [3 Tips, Tricks, Caveats][40477]
    * [3.1 FEL mode][40478]
    * [3.2 VGA][40479]
    * [3.3 LCD modules][40480]
    * [3.4 Expansion ports][40481]
  * [4 Adding a serial port][40482]
  * [5 Pictures][40483]
  * [6 Also known as][40484]
  * [7 See also][40485]

# Identification
The board handily reads "A13-OLinuXino-MICRO". 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "A13-OLinuXino-Micro" target.
  * The .fex file can be found in sunxi-boards as [a13-olinuxinom.fex][40486]

Everything else is the same as the [manual build howto][40487]. 
## Mainline kernel
Use the sun5i-a13-olinuxino-micro.dts device-tree file for the [mainline kernel][40488]. 
# Tips, Tricks, Caveats
## FEL mode
The U-Boot button triggers [ FEL mode][40489]. 
## VGA
Even though the [A13][40462] does not provide DACs itself, the A13-Olinuxino has a VGA connector. 
This is implemented through 3 separate DAC chips (NXP LVC244A) which are connected to the LCD0 lines. This in turn means that you cannot use an LCD and a VGA monitor at the same time, but this is ok as the [A13][40462] can only drive one display at a time anyway. 
Due to the bandwidth limitations of the A13 SoC, the best resolution you can hope for is 800x600. 
## LCD modules
You can attach [several Olimex LCD modules][40490] to the [LCD connector (LCD_CON)][40491]. 
## Expansion ports
Several expansion options are provided: 
  * [A UEXT connector][40492]. This is meant for attaching [Olimex UEXT modules][40493].
  * [A 10 pin IO connector (GPIO-1)][40494].
  * [A 40 pin IO connector (GPIO-2)][40495].

TODO: verify that the GPIO pin-outs are a 1-1 match with the [A13-OLinuXino][40466]
# Adding a serial port
[![][40496]][40497]
[][40498]
DEVICE UART pads
In the top left corner of the device, there are some pins marked UART1. The pin-out is described at the back of the board. All you have to do is connect some leads according to our [UART howto][40499]. 
# Pictures
Take some pictures of your device, [ upload them][40500], and add them here.
  * [![A13-OLinuXino-Micro-frontside.jpg][40501]][40459]
  * [![A13-OLinuXino-Micro-backside.jpg][40502]][40503]
  * [![Olinuxino micro a13 revb top.jpg][40504]][40505]
  * [![Olinuxino micro a13 uart 2.jpg][40506]][40507]
  * [![Olinuxino micro a13 usb serial f cable.jpg][40508]][40509]

# Also known as
There are no rebadgers for this type of device. 
# See also
  * [A13-OLinuXino][40466]: this boards big brother.
  * [Other Olimex hardware][40467]
  * [User manual][40510]
  * [Olimex github repository with all CAD files and schematics.][40511]
