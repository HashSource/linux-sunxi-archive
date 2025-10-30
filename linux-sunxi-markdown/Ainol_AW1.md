# Ainol AW1
Ainol AW1  
---  
[![Ainol AW1 Front.png][6117]][6118]  
Manufacturer |  [Ainol][6119]  
Dimensions |  190 _mm_ x 115 _mm_ x 8 _mm_  
Release Date |  October 2013   
Website |  [Ainol AW1 Product Page][6120]  
Specifications   
SoC |  [A20][6121] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  8GiB   
Power |  2400mAh 3.7V Li-Ion battery, USB   
Features   
LCD |  800x480 (7" 5:3)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][6122])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Ampak AP6210][6123])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  2.0MP (1600x1200) front   
Other |  Accelerometer ([STMicroelectronics LIS3DH][6124]), Bluetooth (Ampak AP6210), [SPCI socket][6125].   
Headers |  UART, I2C   
The Ainol AW1 is a cheap 7" A20 based tablet that comes with an SPCI connector, allowing [ a 3G modem module][6126] to be plugged in. 
## Contents
  * [1 Identification][6127]
  * [2 Sunxi support][6128]
    * [2.1 Current status][6129]
    * [2.2 Manual build][6130]
      * [2.2.1 U-Boot][6131]
        * [2.2.1.1 Sunxi/Legacy U-Boot][6132]
        * [2.2.1.2 Mainline U-Boot][6133]
      * [2.2.2 Linux Kernel][6134]
        * [2.2.2.1 Sunxi/Legacy Kernel][6135]
        * [2.2.2.2 Mainline kernel][6136]
  * [3 Tips, Tricks, Caveats][6137]
    * [3.1 FEL mode][6138]
    * [3.2 SPCI slot / 3G Modem][6139]
  * [4 Adding a serial port (**voids warranty**)][6140]
    * [4.1 Device disassembly][6141]
    * [4.2 Locating the UART][6142]
  * [5 Pictures][6143]
  * [6 Also known as][6144]
  * [7 See also][6145]
    * [7.1 Manufacturer images][6146]

# Identification
On the back of the device, the following is printed: 
[code] 
    ainol
    3G AW1
[/code]
The PCB has the following silkscreened on it: 
[code] 
    NOVO-707FC-A1_V02_13073100
    
[/code]
In Android, under Settings->About Tablet, you will find: 
  * Model Number: Numy_3G_AW1
  * Build Number: 20130924

# Sunxi support
## Current status
Supported, but lacks [ mainline kernel support][6136], and some features are missing under our [ sunxi kernel][6135]. 
## Manual build
You can build things for yourself by following our [ Manual build howto][6147] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _Ainol_AW1"_ build target. 
#### Mainline U-Boot
Use the _Ainol_AW1_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_ainol_aw1.fex_][6148] file. 
Some features are missing on [Linux (sunxi-3.4 branch)][6149]: 
  * USB OTG doesn't work on the external connector (common to all sun7i devices) and it doesn't seem to work in either host or device mode
  * Wi-Fi support is not there but external patches are available (it segfaults as-is)
  * Touchscreen support is not there but external patches are available (untested)

#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
Any button (VOL-, VOL+, HOME) triggers [ FEL mode][6150] from boot1. 
Sending '2' over UART at boot triggers [ FEL mode][6150] from boot1. 
## SPCI slot / 3G Modem
The device has a SPCI modem connector that allows connecting a specifically designed 3G/4G/Voice module. An example of such a modem is [ the Huawei E1220][6125], which sometimes gets sold with this tablet. 
# Adding a serial port (**voids warranty**)
[![][6151]][6152]
[][6153]
Ainol AW1 UART pads
## Device disassembly
The plastic back case is very easy to open. There are no screws but only a few clips that are easy to pop: you probably don't even need a [plastic tool][6154] for this. 
Once the PCB is exposed, there are 4 Philips screws to remove on the lower part of the PCB. You must also remove the LCD/touchscreen connections by lifting up the black parts on the connectors and releasing the flexible flat cable, on the top-right part of the PCB. At this point, you should be able to flip the PCB to the right, exposing its back. 
A black isolant sticker covers the back of the PCB: remove it for now but don't forget to **put it back later** , as it isolates the many test pins from the conductive surface of the back of the screen! 
## Locating the UART
Locate the UART on the back of the PCB according to the pinout and just solder on some wires according to our [UART howto][6155]. 
# Pictures
  * [![Ainol AW1 Front.png][6156]][6118]
  * [![Ainol AW1 Back.png][6157]][6158]
  * [![Ainol AW1 Buttons.jpg][6159]][6160]
  * [![Ainol AW1 Connectors.jpg][6161]][6162]
  * [![Ainol AW1 Modem in.jpg][6163]][6164]
  * [![Ainol AW1 PCB.jpg][6165]][6166]
  * [![Ainol AW1 PCB back covered.jpg][6167]][6168]
  * [![Ainol AW1 PCB back.jpg][6169]][6170]
  * [![Ainol AW1 PCB detail.jpg][6171]][6172]

# Also known as
  * Ainol 3G AW1
  * Ainol Numy 3G AW1
  * Ainol Novo 3G AW1

# See also
## Manufacturer images
  * Ainol AW1 [stock Android][6173]
