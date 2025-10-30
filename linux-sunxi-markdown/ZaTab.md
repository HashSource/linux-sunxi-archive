# INet 3F
(Redirected from [ZaTab][63994])
 
INet 3F  
---  
[![INet 3F Front.png][63997]][63998]  
Manufacturer |  [iNet Tek][63999]  
Dimensions |  240 _mm_ x 185 _mm_ x 10 _mm_  
Release Date |  October 2013   
Specifications   
SoC |  [A10][64000] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  8GB/16GB   
Power |  DC 5V @ 2A, 8000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (9.7" 4:3)   
Touchscreen |  10-finger capacitive ([Goodix GT801 2+1][64001])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][64002])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  **ZaReason Zatab** :
  * 1.3MP (1280x1024) front,
  * 5MP (2560x1920) rear

**Woxter PC97** : TODO  
**Polaroid MIDC010** : TODO   
Other |  Accelerometer ([Bosch BMA250][64003])   
Headers |  UART   
## Contents
  * [1 Identification][64004]
    * [1.1 ZaReason ZaTab][64005]
    * [1.2 Polaroid MIDC010][64006]
    * [1.3 Woxter PC97][64007]
  * [2 Sunxi support][64008]
    * [2.1 Current status][64009]
    * [2.2 Manual build][64010]
    * [2.3 Mainline U-Boot][64011]
  * [3 Tips, Tricks, Caveats][64012]
    * [3.1 FEL mode][64013]
    * [3.2 USB storage mode][64014]
    * [3.3 Reset button][64015]
  * [4 Adding a serial port (**voids warranty**)][64016]
    * [4.1 Device disassembly][64017]
    * [4.2 Locating the UART][64018]
  * [5 Pictures][64019]
  * [6 Also known as][64020]

# Identification
## ZaReason ZaTab
On the back of the device, the following is printed: 
[code] 
    zareason
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INET-3F-REV03
    2012-02-06 ZGC
[/code]
In Android, under Settings->About Tablet, you will find: 
  * Model Number: ZaTab
  * Build Number: cm_zatab-userdebug 4.0.4 IMM76L eng.paulv.20120705.201823 test-keys

## Polaroid MIDC010
The PCB has the following silkscreened on it: 
[code] 
    INET-3F-REV06
    2012-03-26 PYQ
[/code]
In Android, under Settings->About Tablet, you will find: 
  * Model Number: MIDC010

## Woxter PC97
The PCB has the following silkscreened on it: 
[code] 
    INET-3F-REV06
    2012-03-26 PYQ
    
[/code]
# Sunxi support
## Current status
The device is supported and maintained in [mainline U-Boot][64021]. There is no [mainstream kernel][64022] support at this point. [Linux (sunxi-3.4 branch)][64023] properly supports the device. 
## Manual build
  * For building U-Boot, use the _iNet_3F_ target.
  * The .fex file can be found in sunxi-boards as [inet_3f.fex][64024]

Everything else is the same as the [manual build howto][64025]. 
## Mainline U-Boot
For [ building mainline U-Boot][64026], use the _iNet_3F_ target. 
# Tips, Tricks, Caveats
## FEL mode
Sending '2' over UART at boot triggers [ FEL mode][64027] from boot1. 
## USB storage mode
Sending '1' over UART at boot triggers an USB storage mode that exposes the nanda partition as well as the Android external storage. 
## Reset button
The reset button (on the PCB) reboots the device. 
# Adding a serial port (**voids warranty**)
[![][64028]][64029]
[][64030]
iNet 3F pads
## Device disassembly
The aluminium back case is very hard to detach from the rest of the device. In most cases, it will have to be damaged (or at least scratched) to open the device properly. There are no screws to remove nor any kind of glue, but the sides of the back case are curved to cover part of the front plastic part, making it stay it place very firmly. It is advised to use a [a plastic tool][64031] and start opening at the corners of the case. 
## Locating the UART
The UART pads are exposed on the PCB, under the touchscreen ribbon cable, that has to be gently removed before soldering connectors. The pads are clearly labeled on the PCB: GND, Rx, Tx. Connectors can easily be soldered according to the [UART howto][64032]. Ensure to cover the connectors with an isolating layer since the back of the touchscreen connector ribbon may have a conductive part. 
# Pictures
  * [![INet 3F Front.png][64033]][63998]
  * [![INet 3F Back.png][64034]][64035]
  * [![ZaTab.png][64036]][64037]
  * [![ZaTab Buttons.png][64038]][64039]
  * [![ZaTab Connectors.png][64040]][64041]
  * [![INet 3F PCB.jpg][64042]][64043]
  * [![INet 3F PCB detail.jpg][64044]][64045]
  * [![INet 3F PCB detail print.jpg][64046]][64047]
  * [![Zatab-board.jpg][64048]][64049]
  * [![][64050]][64051]
Polaroid MIDC010 (INET-3F-REV06) 

# Also known as
  * [ZaReason ZaTab][64052]
  * Polaroid MIDC010
  * Woxter PC97
