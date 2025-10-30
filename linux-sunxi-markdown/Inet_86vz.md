# Inet 86vz
Inet 86vz  
---  
[![Freelander ph20 front.jpg][26624]][26625]  
Manufacturer |  [Inet-Tek][26626]  
Dimensions |  191 _mm_ x 116 _mm_ x 12 _mm_  
Release Date |  July 2013   
Website |  [Rebadger Product Page][26627]  
Specifications   
SoC |  [A13][26628] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  4GB   
Power |  USB, 2000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 10:6)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][26629])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][26630])   
Storage |  µSD   
USB |  1x USB2.0 OTG   
Camera |  0.3MP (640x480) front-facing   
Other |  Accelerometer ([Manufacturer device][26631] FIXME), reset button   
Headers |  UART   
## Contents
  * [1 Identification][26632]
    * [1.1 Freelander PH20][26633]
    * [1.2 TAB LC7][26634]
  * [2 Sunxi support][26635]
    * [2.1 Current status][26636]
    * [2.2 Images][26637]
    * [2.3 HW-Pack][26638]
    * [2.4 BSP][26639]
    * [2.5 Manual build][26640]
  * [3 Tips, Tricks, Caveats][26641]
    * [3.1 FEL mode][26642]
    * [3.2 USB OTG port][26643]
    * [3.3 NAND chip][26644]
    * [3.4 Installing to NAND][26645]
  * [4 Adding a serial port (**voids warranty**)][26646]
    * [4.1 Device disassembly][26647]
    * [4.2 Locating the UART][26648]
  * [5 Pictures][26649]
  * [6 Also known as][26650]
  * [7 See also][26651]

# Identification
In android, under Settings->About Tablet, you will find... 
## Freelander PH20
  * Model Number: SXZ-PH20
  * Build Number: A13_86VZ_M758C2_*.*

## TAB LC7
  * Model Number: LC7
  * Build Number: 4.2.27LCF20130913

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "INet_86VZ" target.
  * The .fex file can be found in sunxi-boards as [inet_86vz.fex][26652]

Everything else is the same as the [ Manual build howto][26653]. 
# Tips, Tricks, Caveats
## FEL mode
The vol+ button triggers [ FEL mode][26654]. 
## USB OTG port
This device comes with only a single USB port, and has no separate power connector. It therefor is only of limited use as a standalone desktop style device, as connecting a keyboard and/or mouse will only work as long as the battery lasts. 
## NAND chip
Currently (20140117) NAND access is not possible in our sunxi kernels. This is because the Samsung K9GBG08U0M is not known by libnand. [A patch exist][26655] which adds support for this NAND chip. That patch should be integrated soon. 
## Installing to NAND
Awkwardly, the Freelander PH20 default image came with a 16MB boot partition, but the FAT filesystem on it thought it was 128MB large. You will have to create a fresh FAT filesystem when [ installing to NAND][26656]. 
# Adding a serial port (**voids warranty**)
[![][26657]][26658]
[][26659]
86VZ uart
This device exposes a nice set of pads on the mainboard, but there's a catch. These pads are wired to the SD controller, and you can choose, either have an SD card, or have serial. You cannot have both. 
[ Here is a record of how i had to bend backwards to get this solved.][26660]
## Device disassembly
Remove the two screws on the side with the connectors. 
Now gently insert your [plastic tool][26661] in the space between the connector face and the back. You should soon hear the plastic clips popping. Be careful when removing the back, as the speaker is lightly glued to it. 
## Locating the UART
There are nice pads labelled "GND", "RX" and "TX" below the SD card. All you have to do is [solder on some wires][26662]. 
# Pictures
  * [![Freelander ph20 front.jpg][26663]][26625]
  * [![Freelander ph20 back.jpg][26664]][26665]
  * [![Freelander ph20 board.jpg][26666]][26667]
  * [![Storex tab lc7 board closeup.jpg][26668]][26669]
  * [![Storex tab lc7 back.jpg][26670]][26671]

# Also known as
  * [Link-create Freelander PH20][26627]
  * [Storex TAB LC7][26672]

# See also
