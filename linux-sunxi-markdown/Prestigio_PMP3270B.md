# Prestigio PMP3270B
Prestigio PMP3270B  
---  
[![PMP3270B front.jpg][45846]][45847]  
Manufacturer |  [Manufacturer][45848]  
Dimensions |  _197_ x _113_ x _10.5mm_  
Release Date |  August 2012   
Website |  [Device Product Page][45849]  
Specifications   
SoC |  [A13][45850] @ 1Ghz   
DRAM |  512MiB DDR3 @ 408MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 2500mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  2-finger capacitive ([Manufacturer device][45851] FIXME)   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][45852])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Bosch BMA250][45853]), RTC (PCF8563)   
This page needs to be properly filled according to the [New Device Howto][45854] and the [New Device Page guide][45855].
## Contents
  * [1 Identification][45856]
  * [2 Sunxi support][45857]
    * [2.1 Current status][45858]
    * [2.2 Images][45859]
    * [2.3 HW-Pack][45860]
    * [2.4 BSP][45861]
    * [2.5 Manual build][45862]
    * [2.6 FEL mode][45863]
  * [3 Adding a serial port (**voids warranty**)][45864]
    * [3.1 Device disassembly][45865]
    * [3.2 Locating the UART][45866]
  * [4 Pictures][45867]
  * [5 Also known as][45868]
  * [6 See also][45869]
    * [6.1 Manufacturer images][45870]

# Identification
On the back of the device, the following is printed: 
[code] 
    PRESTIGIO MULTIPAD
    Tablet PC | PMP3270B
[/code]
The PCB has the following silkscreened on it: 
[code] 
    ME12
    2012-06-21
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _PMP3270B_
  * Build Number: _PMP3270B_V1.0.12-eng 4.0.3 IML74K 20130313 test-keys_

# Sunxi support
## Current status
Awaiting patches. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _prestigio_pmp3270_ target.
  * The .fex file can be found in sunxi-boards as [prestigio_pmp3270.fex][45871]

Everything else is the same as the [manual build howto][45872]. 
## FEL mode
The _Vol+_ button triggers [ FEL mode][45873]. 
# Adding a serial port (**voids warranty**)
[![][45874]][45875]
[][45876]
PMP3270B UART pads
## Device disassembly
There are two screws on the connector side which have to be removed first. Then carefully insert your [Plastic tool][45877] between front and back case and pop all the clips. Clips are located on the back case and should be pushed inside. Exact location of each clip is shown on the picture. 
[![][45878]][45879]
[][45880]
PMP3270 clips on back case
## Locating the UART
[UART][45881] pads are located near the board edge with battery pads under main chip. Solder on some wires according to our [UART Howto][45881]
# Pictures
Take some pictures of your device, [ upload them][45882], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![PMP3270B front.jpg][45883]][45847]
  * [![PMP3270B back.jpg][45884]][45885]
  * [![Device buttons 1.jpg][45886]][45887]
  * [![Device buttons 2.jpg][45888]][45889]
  * [![PMP3270B board front.jpg][45890]][45891]
  * [![PMP3270B board back.jpg][45892]][45893]

# Also known as
MultiPad 7.0 PRIME 
# See also
  * [Prestigio PMP3670B][45894]

## Manufacturer images
[Stock ROM v1.0.12][45895]
