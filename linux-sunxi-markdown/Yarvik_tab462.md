# Yarvik tab462
Yarvik tab462  
---  
[![Yarvik tab462 front.jpg][63371]][63372]  
Manufacturer |  Yarvik   
Dimensions |  _268mm_ x _178mm_ x _11mm_  
Release Date |  September 2012   
Website |  N/A   
Specifications   
SoC |  [A10][63373] @ 1.6Ghz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  DC 5V @ 5A, 6000mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (10" 1280:800)   
Touchscreen |  capacitive   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n Realtek rtl8150   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP front, 2MP rear   
Other |  Accelerometer   
This page needs to be properly filled according to the [New Device Howto][63374] and the [New Device Page guide][63375].
## Contents
  * [1 Identification][63376]
  * [2 Sunxi support][63377]
    * [2.1 Current status][63378]
    * [2.2 Images][63379]
    * [2.3 Manual build][63380]
      * [2.3.1 U-Boot][63381]
        * [2.3.1.1 Sunxi/Legacy U-Boot][63382]
        * [2.3.1.2 Mainline U-Boot][63383]
      * [2.3.2 Linux Kernel][63384]
        * [2.3.2.1 Sunxi/Legacy Kernel][63385]
        * [2.3.2.2 Mainline kernel][63386]
  * [3 Tips, Tricks, Caveats][63387]
    * [3.1 FEL mode][63388]
  * [4 Adding a serial port (**voids warranty**)][63389]
    * [4.1 Device disassembly][63390]
    * [4.2 Locating the UART][63391]
  * [5 Pictures][63392]
  * [6 Also known as][63393]
  * [7 See also][63394]

# Identification
On the back of the device, the following is printed: 
[code] 
    Yarvik
    TAB462
[/code]
The PCB has the following silkscreened on it: 
[code] 
    A1001T v1.2
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: TAB462
  * Build Number: TAB462-eng 4.0.4 IMM76D 20120731 test-keys

# Sunxi support
## Current status
## Images
## Manual build
Not supported. 
### U-Boot
#### Sunxi/Legacy U-Boot
Not supported. 
#### Mainline U-Boot
Not supported. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Not supported. 
#### Mainline kernel
Not supported. 
# Tips, Tricks, Caveats
## FEL mode
The vol- button triggers [ FEL mode][63395]. 
# Adding a serial port (**voids warranty**)
[![][63396]][63397]
[][63398]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][63399]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][63400].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][63399].
# Pictures
  * [![Yarvik tab462 board1.jpg][63401]][63402]

# Also known as
  * Triline A1001T

# See also
