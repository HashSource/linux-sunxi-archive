# Milagrow MGPT09
Milagrow MGPT09  
---  
[![Softwinners Crane A088 Device.jpg][38017]][38018]  
Manufacturer |  Softwinners   
Dimensions |  191.1 _mm_ x 117 _mm_ x 12.53 _mm_  
Release Date |  Dec 2012   
Specifications   
SoC |  [A10][38019] @ 1Ghz   
DRAM |  1GB DDR3 @ ? MHz   
NAND |  8 GB   
Power |  DC 5V @ 2A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 5:3)   
Touchscreen |  5-finger capacitive ([Focaltech 5x (ft5x_ts v1.0.1)][38020])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone/microphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][38021]), Bluetooth, 3G SIM slot (standard sized)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2MP rear   
Other |  Accelerometer ([ MMAx][38022], Listed as MMA im CPUZ)   
  

## Contents
  * [1 Identification][38023]
  * [2 Sunxi support][38024]
    * [2.1 Current status][38025]
    * [2.2 Images][38026]
    * [2.3 HW-Pack][38027]
    * [2.4 BSP][38028]
    * [2.5 Manual build][38029]
  * [3 Tips, Tricks, Caveats][38030]
    * [3.1 FEL mode][38031]
    * [3.2 Recovery mode][38032]
    * [3.3 Device specific topic][38033]
    * [3.4 ...][38034]
  * [4 Adding a serial port (**voids warranty**)][38035]
    * [4.1 Device disassembly][38036]
    * [4.2 Locating the UART][38037]
  * [5 Pictures][38038]
  * [6 Also known as][38039]
  * [7 See also][38040]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: MGPT09
  * Build Display ID: MGPT09 20121210

On running getprop through a terminal emulator, you'll find: 
  * Build Description: A088_V1.1.4_20121208_r798_0cf8c6f
  * Build Fingerprint: softwinners/crane_a088/crane-a088:4.0.4/IMM76D/20121208:eng/test-keys
  * Build Date: 2012 12 08 17:38:42 CST

  

# Sunxi support
## Current status
.fex file and bootinfo has been obtained from a livesuite image. A pull request for the fex file was created. 
Building u-boot and kernel are WIP. 
## Images
Full livesuit image provided by Milagrow Humantech is avaiable. 
## HW-Pack
Add Softwinners Crane A088 HW-pack specifics here.
## BSP
Add Softwinners Crane A088 BSP specifics here.
## Manual build
WIP 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
Hold the Vol up button while powering on the device, and then press the power button a 3-5 times to enter [ FEL mode][38041]. 
## Recovery mode
No known way to enter the recovery. 
## Device specific topic
## ...
# Adding a serial port (**voids warranty**)
[![][38042]][38043]
[][38044]
UART pads
## Device disassembly
Remove the back cover by separating the snaps all around. The main board is fastened using 3 screws. Disconnect the square shaped connector in the corner and the display connector to flip the main board. 
## Locating the UART
UART0 TX, RX pins and a GND pin (possibly test pads) are visible towards the center of the main board on the backside. 
# Pictures
  * [![A088 Front.jpg][38045]][38046]
  * [![A088 Back.jpg][38047]][38048]
  * [![Side Ports.jpg][38049]][38050]
  * [![A088 Top Buttons.jpg][38051]][38052]
  * [![A088 Board Front 1.jpg][38053]][38054]
  * [![A088 Board Front 2.jpg][38055]][38056]
  * [![A088 Board Front 3.jpg][38057]][38058]
  * [![A088 Board Front 4.jpg][38059]][38060]
  * [![A088 Board Back 1.jpg][38061]][38062]
  * [![A088 Board Back 2.jpg][38063]][38064]

# Also known as
Milagrow MGPT09-8  
Milagrow TabTop 7.16C  
Softwinners Crane A088 
# See also
<https://www.milagrowhumantech.com/>
