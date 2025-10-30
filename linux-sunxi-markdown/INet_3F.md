# INet 3F
INet 3F  
---  
[![INet 3F Front.png][24826]][24827]  
Manufacturer |  [iNet Tek][24828]  
Dimensions |  240 _mm_ x 185 _mm_ x 10 _mm_  
Release Date |  October 2013   
Specifications   
SoC |  [A10][24829] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  8GB/16GB   
Power |  DC 5V @ 2A, 8000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (9.7" 4:3)   
Touchscreen |  10-finger capacitive ([Goodix GT801 2+1][24830])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][24831])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  **ZaReason Zatab** :
  * 1.3MP (1280x1024) front,
  * 5MP (2560x1920) rear

**Woxter PC97** : TODO  
**Polaroid MIDC010** : TODO   
Other |  Accelerometer ([Bosch BMA250][24832])   
Headers |  UART   
## Contents
  * [1 Identification][24833]
    * [1.1 ZaReason ZaTab][24834]
    * [1.2 Polaroid MIDC010][24835]
    * [1.3 Woxter PC97][24836]
  * [2 Sunxi support][24837]
    * [2.1 Current status][24838]
    * [2.2 Manual build][24839]
    * [2.3 Mainline U-Boot][24840]
  * [3 Tips, Tricks, Caveats][24841]
    * [3.1 FEL mode][24842]
    * [3.2 USB storage mode][24843]
    * [3.3 Reset button][24844]
  * [4 Adding a serial port (**voids warranty**)][24845]
    * [4.1 Device disassembly][24846]
    * [4.2 Locating the UART][24847]
  * [5 Pictures][24848]
  * [6 Also known as][24849]

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
The device is supported and maintained in [mainline U-Boot][24850]. There is no [mainstream kernel][24851] support at this point. [Linux (sunxi-3.4 branch)][24852] properly supports the device. 
## Manual build
  * For building U-Boot, use the _iNet_3F_ target.
  * The .fex file can be found in sunxi-boards as [inet_3f.fex][24853]

Everything else is the same as the [manual build howto][24854]. 
## Mainline U-Boot
For [ building mainline U-Boot][24855], use the _iNet_3F_ target. 
# Tips, Tricks, Caveats
## FEL mode
Sending '2' over UART at boot triggers [ FEL mode][24856] from boot1. 
## USB storage mode
Sending '1' over UART at boot triggers an USB storage mode that exposes the nanda partition as well as the Android external storage. 
## Reset button
The reset button (on the PCB) reboots the device. 
# Adding a serial port (**voids warranty**)
[![][24857]][24858]
[][24859]
iNet 3F pads
## Device disassembly
The aluminium back case is very hard to detach from the rest of the device. In most cases, it will have to be damaged (or at least scratched) to open the device properly. There are no screws to remove nor any kind of glue, but the sides of the back case are curved to cover part of the front plastic part, making it stay it place very firmly. It is advised to use a [a plastic tool][24860] and start opening at the corners of the case. 
## Locating the UART
The UART pads are exposed on the PCB, under the touchscreen ribbon cable, that has to be gently removed before soldering connectors. The pads are clearly labeled on the PCB: GND, Rx, Tx. Connectors can easily be soldered according to the [UART howto][24861]. Ensure to cover the connectors with an isolating layer since the back of the touchscreen connector ribbon may have a conductive part. 
# Pictures
  * [![INet 3F Front.png][24862]][24827]
  * [![INet 3F Back.png][24863]][24864]
  * [![ZaTab.png][24865]][24866]
  * [![ZaTab Buttons.png][24867]][24868]
  * [![ZaTab Connectors.png][24869]][24870]
  * [![INet 3F PCB.jpg][24871]][24872]
  * [![INet 3F PCB detail.jpg][24873]][24874]
  * [![INet 3F PCB detail print.jpg][24875]][24876]
  * [![Zatab-board.jpg][24877]][24878]
  * [![][24879]][24880]
Polaroid MIDC010 (INET-3F-REV06) 

# Also known as
  * [ZaReason ZaTab][24881]
  * Polaroid MIDC010
  * Woxter PC97
