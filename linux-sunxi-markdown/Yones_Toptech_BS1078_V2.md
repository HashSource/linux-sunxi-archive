# Yones Toptech BS1078 V2
Yones Toptech BS1078 V2  
---  
[![Yones toptech bs1078 v2 front.jpg][63627]][63628]  
Manufacturer |  [Yones TopTech][63629]  
Dimensions |  260 _mm_ x 165 _mm_ x 10 _mm_  
Release Date |  January 2014   
Website |  [Device Product Page][63630]  
Specifications   
SoC |  [A31s][63631] @ 1.2Ghz (Quad-core Cortex-A7)   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  USB, DC 5V @ 2A, 6000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (10.1" 16:9)   
Touchscreen |  5-finger capacitive ([SiLead GSL3675][63632])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([RTL8723AS][63633]) (USB Module)   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2.0MP (1600x1200)rear   
Other |  Accelerometer ([Manufacturer device][63634])   
This page needs to be properly filled according to the [New Device Howto][63635] and the [New Device Page guide][63636].
## Contents
  * [1 Identification][63637]
  * [2 Sunxi support][63638]
    * [2.1 Current status][63639]
    * [2.2 Images][63640]
    * [2.3 HW-Pack][63641]
    * [2.4 BSP][63642]
    * [2.5 Manual build][63643]
    * [2.6 Mainline U-Boot][63644]
    * [2.7 Mainline kernel][63645]
  * [3 Tips, Tricks, Caveats][63646]
    * [3.1 FEL mode][63647]
    * [3.2 ...][63648]
  * [4 Adding a serial port (**voids warranty**)][63649]
    * [4.1 Device disassembly][63650]
    * [4.2 Locating the UART][63651]
  * [5 Pictures][63652]
  * [6 Also known as][63653]
  * [7 See also][63654]
    * [7.1 Manufacturer images][63655]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    YONESTOPTECH-BS1078-20140125 V2-
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _Q102_
  * Build Number: _fiber_q102-eng 4.4.2 KOT49H DDR420 20140621_

# Sunxi support
## Current status
Able to boot to serial console using mainline A31-Hummingbird dts and mainline kernel using sunxi_defconfig and root file system built with buildroot. 
## Images
## HW-Pack
## BSP
## Manual build
No support in the community maintained sunxi-3.4 kernel is planned. Please skip to the next Mainline U-Boot/Mainline kernel sections. 
## Mainline U-Boot
Working on a real U-Boot defconfig for this tablet 
For [ building mainline U-Boot][63656], use the _Hummingbird_A31_defconfig_ target. 
## Mainline kernel
Working on a real dts for this tablet 
Use the _sun6i-a31s-yones-toptech-bs1078-v2.dts_ device-tree file for the [mainline kernel][63657]. 
  * Use the rtl8723au driver in the staging drivers for WIFI. Setting ht_enable=0 when loading the driver to disable 802.11n seems to work better. With 802.11n enabled, the driver drops packets.

# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][63658]. 
## ...
# Adding a serial port (**voids warranty**)
Use the UART pads and an appropriate level shifter to attach a serial port to the tablet. 
See the "Locating the UART" section for information on where the UART pads are located at. 
See [UART howto][63659] for information on how to communicate with the UART. 
## Device disassembly
[![Yones toptech bs1078 v2 button1.jpg][63660]][63661]
Remove two metal screws on the right side of the device then use a guitar pick style plastic opening tool to separate the back panel from the tablet. See also [Plastic tool howto][63662]. 
## Locating the UART
[![Yones toptech bs1078 v2 pcb back.jpg][63663]][63664]
On the backside of the board there are two test points marked RX and TX which are the serial port. The entire back of the board is covered in black tape that must be peeled off to expose the the test points. After soldering wires to the test points, it is no longer possible to screw the board back into the case because of the thickness of the wires . 
See [UART howto][63659] for information on how to communicate with the UART. 
# Pictures
Take some pictures of your device, [ upload them][63665], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Yones toptech bs1078 v2 front.jpg][63666]][63628]
  * [![Yones toptech bs1078 v2 back.jpg][63667]][63668]
  * [![Yones toptech bs1078 v2 button1.jpg][63669]][63661]
  * [![Yones toptech bs1078 v2 button2.jpg][63670]][63671]
  * [![Yones toptech bs1078 v2 pcb front.jpg][63672]][63673]
  * [![Yones toptech bs1078 v2 pcb back.jpg][63674]][63664]

# Also known as
# See also
## Manufacturer images
