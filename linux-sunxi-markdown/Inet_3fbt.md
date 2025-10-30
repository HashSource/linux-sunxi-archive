# Inet 3fbt
Inet 3fbt  
---  
[![Kogan Agora KATBL10A16DA Front.jpeg][26152]][26153]  
Manufacturer |  [Inet-Tek][26154]  
Dimensions |  243 _mm_ x 190 _mm_ x 12 _mm_  
Release Date |  May 2012   
Website |  Missing product page   
Specifications   
SoC |  [A10][26155] @ 1 GHz   
DRAM |  1 GiB DDR3 @ 360 MHz   
NAND |  16 GB   
Power |  DC 5 V @ 500 mA minimum, 4500 mAh 3.7 V Li-Ion battery   
Features   
LCD |  1024x768 (10" 4:3)   
Touchscreen |  5-finger capacitive ([Focaltech FT5406EE8][26156])   
Video |  HDMI (Type C - mini)   
Audio |  3.5 mm headphone plug, mini HDMI, internal "stereo" speakers   
Network |  WiFi 802.11 b/g/n ([Broadcom BCM40183][26157])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3 MP (640x480) front, 2.0 MP (1920x1080) rear   
Other |  Accelerometer ([Bosch BMA250][26158]), Bluetooth ([Broadcom BCM40183][26159])   
Headers |  UART   
## Contents
  * [1 Identification][26160]
  * [2 Sunxi support][26161]
    * [2.1 Current status][26162]
    * [2.2 Manual build][26163]
  * [3 Tips, Tricks, Caveats][26164]
    * [3.1 Power supply / Charging][26165]
    * [3.2 Reset button][26166]
    * [3.3 FEL mode][26167]
    * [3.4 WiFi][26168]
  * [4 Adding a serial port (**voids warranty**)][26169]
    * [4.1 Device disassembly][26170]
    * [4.2 Locating the UART][26171]
  * [5 Pictures][26172]
  * [6 Found in][26173]
  * [7 See also][26174]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    INET-3FBT-REV01
    2012-06-22
[/code]
In Android on the Kogan Agora, under Settings->About Tablet, you will find: 
  * Model Number: _KATBL10A16DA_
  * Build Number: _KoganAgoraICS4.0_

# Sunxi support
## Current status
Supported 
## Manual build
  * For building U-Boot, use the _INet_3FBT_ target.
  * The .fex file can be found in sunxi-boards as [inet_3fbt.fex][26175]

Everything else is the same as the [manual build howto][26176]. 
# Tips, Tricks, Caveats
## Power supply / Charging
This board has a separate barrel socket for a 5 V power supply, however it will also charge off the micro-USB "computer" port. 
## Reset button
There is a reset button next to the UART pads accessible through a hole in the back of the case. 
## FEL mode
The Vol+ (middle) button triggers [ FEL mode][26177]. 
Alternatively, an "U-Boot" pad is available on the PCB near the WiFi chip. (On the front at the top, to the left of the antenna connection) 
## WiFi
Wifi chip is part of a shared [Wifi][26178]/[Bluetooth][26179] module called _iNet i10 T0C601C_. This has a [Broadcom BCM40183][26157] chip embedded in it. 
# Adding a serial port (**voids warranty**)
[![][26180]][26181]
[][26182]
iNet 3FBT UART pads
## Device disassembly
Remove two screws from the connector side. Carefully insert your [plastic tool][26183] between the metal back cover and the frame, and gently push the frame to the outside until the clips release. Go all around until all clips have release. 
Since the Kogan Agora tablet has the same case as the Eken A90 style tablets, [this youtube video might also help][26184]. 
Be careful when opening the device though, as the speakers are glued to the back cover. 
## Locating the UART
The UART pads are nicely silkscreened on the board, under the touchscreen cable, right next to the reset button. All you have to do is solder on some wires according to our [UART howto][26185]. 
# Pictures
  * [![Kogan Agora KATBL10A16DA Front.jpeg][26186]][26153]
  * [![Kogan Agora KATBL10A16DA Back.jpeg][26187]][26188]
  * [![INet 3FBT Rev01 Board Ports.jpeg][26189]][26190]
  * [![Kogan Agora KATBL10A16DA Top Buttons.jpeg][26191]][26192]
  * [![INet 3FBT Rev01 Board Front.jpeg][26193]][26194]
  * [![INet 3FBT Rev01 Board Back.jpeg][26195]][26196]

# Found in
  * Kogan Agora 10" 16 GB (as documented on this page).
  * Kraun ktab 9.7 9704DD
  * Mediatek 930i

# See also
  * The [Inet 3f][26197] is a cut down version of this tablet, lacking bluetooth.
