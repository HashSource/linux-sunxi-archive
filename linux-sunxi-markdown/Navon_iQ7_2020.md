# Navon iQ7 2020
Navon iQ7 2020  
---  
[![Iq7 2020 front.jpeg][39145]][39146]  
Manufacturer |  [Importer: HungaroFlotta Kft. (defunt)][39147] [archive][39148]  
Dimensions |  191 _mm_ x 116 _mm_ x 11.7 _mm_  
Release Date |  unknown   
Website |  [not applicable]   
Specifications   
SoC |  [A50][39149] @ 1.5Ghz   
DRAM |  1GiB Samsung K4B2G0446Q-BYQ0 DDR3L   
NAND |  8GB SpecTek PFF62-10AL   
Power |  microUSB 5V @ 1.5A, 2500mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7")   
Touchscreen |  Capacitive (unknown)   
Audio |  3.5mm headphone plug, internal speaker   
Network |  XradioTech XR829   
Storage |  µSD, NAND   
USB |  microUSB combo host + OTG   
Camera |  2MP (1600x1200) GC2385 rear, VGA GC030A rear   
Other |  Accelerometer   
## Contents
  * [1 Identification][39150]
  * [2 Sunxi support][39151]
    * [2.1 Current status][39152]
    * [2.2 FEL mode][39153]
  * [3 Adding a serial port (**voids warranty**)][39154]
    * [3.1 Device disassembly][39155]
  * [4 Pictures][39156]
  * [5 Also known as][39157]

# Identification
On the back of the device, the following is printed: 
[code] 
    NAVON
    iQ7 2020
[/code]
The PCB has the following silkscreened on it: 
[code] 
    A50-86V-V2.0
    08B-20200718
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _iQ7_
  * Build Number: _Navon_V1.00_20201023_

# Sunxi support
inexistent 
## Current status
no support 
## FEL mode
Holding VOL+, pressing and holding power for 2 seconds, then pressing power 3 times triggers [ FEL mode][39158]. 
# Adding a serial port (**voids warranty**)
[![][39159]][39160]
[][39161]
UART pads
Has not been tested yet, should be 3.3V serial UART according to the [UART howto][39162]. You need to remove the board from the housing and peel up the insulating layer from the board to find the exposed GND, TX, RX pads. The VOL+, VOL-, POWER buttons are **separate plastic pieces from the housing** , make sure you don't lose them. The following screws need to be unfastened from the board: one below MIC+ and MIC-, one above the PFF62-10AL 8GB NAND and the one above the CAM connector. The flex cables are held down with black pieces of adhesive you need to pull off carefully. The speaker, battery and wifi antenna are soldered to the board. 
## Device disassembly
Top two screws need to be unfastened and the back needs to be popped off using a guitar pick. Refer to the [ Plastic tool howto][39163]. 
  

# Pictures
  * [![Iq7 2020 back.jpeg][39164]][39165]
  * [![Iq7 2020 front.jpeg][39166]][39146]
  * [![Iq7 2020 internal.jpeg][39167]][39168]
  * [![Iq7 2020 mb.jpeg][39169]][39170]

# Also known as
KRONO KIDS FIVE
