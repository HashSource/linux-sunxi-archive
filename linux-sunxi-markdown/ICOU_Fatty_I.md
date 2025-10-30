# ICOU Fatty I
ICOU Fatty I  
---  
[![ICOU Fatty I Front.png][24680]][24681]  
Manufacturer |  [ICOO][24682]  
Dimensions |  135 _mm_ x 200 _mm_ x 7 _mm_  
Release Date |  July 2013   
Website |  [Device Product Page][24683]  
Specifications   
SoC |  [A20][24684] @ 1Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  8GiB   
Power |  DC 5V @ 2A, 3500mAh 3.7V Li-Ion battery   
Features   
LCD |  768x1024 (7.85" 3:4)   
Touchscreen |  5-Finger Capacitive ([Ilitek aimvF][24685])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][24686])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2.0MP (1600x1200) rear   
Other |  Accelerometer ([Freescale MMA7660][24687])   
Headers |  UART   
## Contents
  * [1 Identification][24688]
  * [2 Sunxi support][24689]
    * [2.1 Current status][24690]
    * [2.2 Manual build][24691]
  * [3 Tips, Tricks, Caveats][24692]
    * [3.1 FEL mode][24693]
  * [4 Adding a serial port (**voids warranty**)][24694]
    * [4.1 Device disassembly][24695]
    * [4.2 Locating the UART][24696]
  * [5 Pictures][24697]
  * [6 Also known as][24698]
  * [7 See also][24699]
    * [7.1 Manufacturer images][24700]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    2013-04-10
    TOPWISE-013
    S785F-MAINBOARD-V2.0.0
    
[/code]
In Android, under Settings->About Tablet, you will find: 
  * Model Number: Fatty1
  * Build Number: 20130601-S785

# Sunxi support
## Current status
There is neither [mainline U-Boot][24701] nor [mainstream kernel][24702] support at this point. 
The legacy [U-Boot][24703] properly supports the device. 
Some features are missing on [Linux (sunxi-3.4 branch)][24704]: 
  * USB OTG doesn't work on the external connector (common to all sun7i devices) and it doesn't seem to work in either host or device mode
  * LCD does not work (it uses MIPI), but backlight works
  * Wi-Fi doesn't work (interface is never ready)
  * HDMI doesn't work (segfault)

## Manual build
  * For building u-boot, use the "ICOU_Fatty_I" target.
  * The .fex file can be found in sunxi-boards as [icou_fatty_i.fex][24705]

Everything else is the same as the [manual build howto][24706]. 
# Tips, Tricks, Caveats
## FEL mode
The VOL- button triggers [ FEL mode][24707]. This is the third button from the top on the right edge of the device. 
# Adding a serial port (**voids warranty**)
[![][24708]][24709]
[][24710]
ICOU Fatty I UART pads
## Device disassembly
Opening the device is really straightforward. There are two Phillips screws to remove on top of the device and once these are out, the back aluminium case can easily be removed using [a plastic tool][24711] to pop a few pins. 
## Locating the UART
The UART pads are clearly labeled on the PCB: GND, Rx, Tx. These pads are located on the edge of the board, left and below the RAM chips. All you have to do is solder on some wires according to our [UART howto][24712]. 
# Pictures
  * [![ICOU Fatty I Front.png][24713]][24681]
  * [![ICOU Fatty I Back.png][24714]][24715]
  * [![ICOU Fatty I Buttons.png][24716]][24717]
  * [![ICOU Fatty I Connectors.png][24718]][24719]
  * [![ICOU Fatty I PCB.jpg][24720]][24721]
  * [![ICOU Fatty I Identification.jpg][24722]][24723]

# Also known as
# See also
## Manufacturer images
