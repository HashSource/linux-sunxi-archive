# Ampe A76
Ampe A76  
---  
[![Ampe A76 Front.png][7214]][7215]  
Manufacturer |  [Ampe][7216]  
Dimensions |  196 _mm_ x 120'mm _x 8_ mm __  
Release Date |  January 2013   
Website |  [Ampe A76 Product Page][7217]  
Specifications   
SoC |  [A13][7218] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  8GB   
Power |  DC 5V @ 1.5A, 2600mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 5:3)   
Touchscreen |  5-finger capacitive ([Goodix GT818][7219])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][7220])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  2.0MP (1600x1200) front   
Other |  Accelerometer ([Freescale MMA7660][7221])   
Headers |  UART   
This page is about the latest A13 version of the Ampe A76 tablet. Note that Ampe released different hardware under the name A76. 
## Contents
  * [1 Identification][7222]
  * [2 Sunxi support][7223]
    * [2.1 Current status][7224]
    * [2.2 Manual build][7225]
    * [2.3 Mainline U-Boot][7226]
  * [3 Tips, Tricks, Caveats][7227]
    * [3.1 ADB][7228]
    * [3.2 FEL mode][7229]
  * [4 Adding a serial port (**voids warranty**)][7230]
    * [4.1 Device disassembly][7231]
    * [4.2 Locating the UART][7232]
  * [5 Pictures][7233]
  * [6 Also known as][7234]
  * [7 See also][7235]
    * [7.1 Manufacturer images][7236]

# Identification
Ampe manufactured **different tablets** under the name A76. Older versions use the A13 SoC and more recent versions ship with an A20 or A23 SoC instead of the A13. 
On the back of the device, the following is printed: 
[code] 
    Ampe
    A76
    
[/code]
The PCB has the following silkscreened on it: 
[code] 
    A7006Q-V1.1
    2013-5-21
    
[/code]
In Android, under Settings->About Tablet, you will find: 
  * Model Number: A76II
  * Build Number: C_V3.01-nuclear-anpei7am-r4.0.84-130704

This version of the tablet ships with a Windows Phone-ish interface for Android (tiles on the homescreen). 
# Sunxi support
## Current status
The device is supported and maintained in [mainline U-Boot][7237]. There is no [mainstream kernel][7238] support at this point. [Linux (sunxi-3.4 branch)][7239] properly supports the device. 
## Manual build
  * For building u-boot, use the _Ampe_A76_ target.
  * The .fex file can be found in sunxi-boards as [ampe_a76.fex][7240]

Everything else is the same as the [manual build howto][7241]. 
## Mainline U-Boot
For [ building mainline U-Boot][7242], use the _Ampe_A76_ target. 
# Tips, Tricks, Caveats
## ADB
The device does not ship with root access enabled: [ADB][7243] shell runs as unprivileged user. However, the _/data/local/tmp_ [trick to gain root access][7244] works. 
## FEL mode
Any button (VOL-, VOL+) triggers [ FEL mode][7245] at boot. 
# Adding a serial port (**voids warranty**)
[![][7246]][7247]
[][7248]
Ampe A76 UART pads
The devices uses **UART1** for U-Boot and Linux messages: make sure to properly set _console=ttyS1_ and spawn getty on ttyS1. 
## Device disassembly
The back case is rather hard to separate from the front: using a [plastic tool][7249] is highly recommended! There are up to 14 clips to pop open. The clips are far inside the inner part of the case, so don't hesitate going deep with a plastic tool. It's easier to start on the side with the connectors. 
## Locating the UART
Locate the UART on the back of the PCB according to the pinout and just solder on some wires according to our [UART howto][7250]. 
# Pictures
  * [![Ampe A76 Front.png][7251]][7215]
  * [![Ampe A76 Back.png][7252]][7253]
  * [![Ampe A76 Buttons.jpg][7254]][7255]
  * [![Ampe A76 Connectors.jpg][7256]][7257]
  * [![Ampe A76 PCB.jpg][7258]][7259]
  * [![Ampe A76 PCB detail.jpg][7260]][7261]

# Also known as
  * A76 时尚版
  * A76 时尚版Ⅱ

# See also
Other Ampe A76 models: 
  * [A76 精英版][7262]
  * [A76 经典版][7263]
  * [A76 双核版][7264]
  * [A76 双核II][7265]

## Manufacturer images
Ampe A76 [download page][7266]: 
  * A76 时尚版Ⅱ [stock Android][7267]
  * A76 时尚版 [stock Android][7268]
