# INet 3W
INet 3W  
---  
[![INet 3W Front.png][24916]][24917]  
Manufacturer |  [iNet Tek][24918]  
Dimensions |  243 _mm_ x 187 _mm_ x 10 _mm_  
Release Date |  October 2013   
Specifications   
SoC |  [A10][24919] @ 1Ghz   
DRAM |  1GiB @ 408MHz   
NAND |  8GB   
Power |  DC 5V @ 2A, 5000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (9.7" 4:3)   
Touchscreen |  10-finger capacitive ([Focaltech FT5406EE8][24920])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([iNet i10][24921])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3MP (640x480) front (Galaxycore GC0308), 2MP 1600x1200) rear (Galaxy Core GT2005)   
Other |  Accelerometer ([Bosch BMA250][24922]), Bluetooth ([Broadcom BCM40183][24923]), WCDMA modem (HTF HWM630), SIM card port   
Headers |  UART   
The iNet 3W tablet comes with a WCDMA modem and a SIM card port. 
## Contents
  * [1 Identification][24924]
  * [2 Sunxi support][24925]
    * [2.1 Current status][24926]
    * [2.2 Manual build][24927]
    * [2.3 Mainline U-Boot][24928]
  * [3 Tips, Tricks, Caveats][24929]
    * [3.1 FEL mode][24930]
    * [3.2 USB storage mode][24931]
    * [3.3 Reset button][24932]
  * [4 Adding a serial port (**voids warranty**)][24933]
    * [4.1 Device disassembly][24934]
    * [4.2 Locating the UART][24935]
  * [5 Pictures][24936]
  * [6 Also known as][24937]
  * [7 See also][24938]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    INET-3W-REV03
    Zng-gc 2013-03-26
    
[/code]
In Android, under Settings->About Tablet, you will find: 
  * Model Number: _M9701TW_
  * Build Number: _03W1-P1-H2-H02-CY40.20121230_

# Sunxi support
## Current status
The device is supported and maintained in [mainline U-Boot][24939]. There is no [mainstream kernel][24940] support at this point. [Linux (sunxi-3.4 branch)][24941] boots on the device, but most features are untested. 
## Manual build
  * For building U-Boot, use the _iNet_3W_ target.
  * The .fex file can be found in sunxi-boards as [inet_3w.fex][24942]

Everything else is the same as the [manual build howto][24943]. 
## Mainline U-Boot
For [ building mainline U-Boot][24944], use the _iNet_3W_ target. 
# Tips, Tricks, Caveats
## FEL mode
Sending '2' over UART at boot triggers [ FEL mode][24945] from boot1. 
## USB storage mode
Sending '1' over UART at boot triggers an USB storage mode that exposes the nanda partition as well as the Android external storage. 
## Reset button
The reset button (on the PCB) reboots the device. 
# Adding a serial port (**voids warranty**)
[![][24946]][24947]
[][24948]
iNet 3W UART pads
## Device disassembly
In order to open the device, there are two Phillips screws to remove from the side with the connectors. The pins from the white part are easy to pop but it is advised to use a [a plastic tool][24949], starting from the side with the connectors. The front panel is very fragile and pressuring the screen to pop open the pins can easily end up in breaking the touch screen panel. 
## Locating the UART
The UART pads are exposed in a very visible way on the PCB, close to the touchscreen connector. The pads are clearly labeled on the PCB: GND, Rx, Tx. Connectors can easily be soldered according to the [UART howto][24950]. 
# Pictures
  * [![INet 3W Front.png][24951]][24917]
  * [![INet 3W Back.png][24952]][24953]
  * [![INet 3W Buttons.jpg][24954]][24955]
  * [![INet 3W Connectors.jpg][24956]][24957]
  * [![INet 3W PCB.jpg][24958]][24959]
  * [![INet 3W PCB detail.jpg][24960]][24961]

# Also known as
  * AM-975

# See also
  * [DealExtreme Product Page][24962]
