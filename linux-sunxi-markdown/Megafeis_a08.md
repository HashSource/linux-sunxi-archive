# Megafeis a08
Megafeis a08  
---  
[![Device front.jpg][35778]][35779]  
Manufacturer |  [Megafeis][35780]  
Dimensions |  width _mm_ x breadth'mm _x height_mm __  
Release Date |  July 2013   
Website |  [Product Page][35781]  
Specifications   
SoC |  [A10s][35782] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  4GB   
Power |  DC 5V @ 1.5A   
Features   
Video |  HDMI (Type A - male)   
Audio |  HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek device][35783])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][35784] and the [New Device Page guide][35785].
## Contents
  * [1 Identification][35786]
  * [2 Sunxi support][35787]
    * [2.1 Current status][35788]
    * [2.2 Images][35789]
    * [2.3 HW-Pack][35790]
    * [2.4 BSP][35791]
    * [2.5 Manual build][35792]
  * [3 Tips, Tricks, Caveats][35793]
    * [3.1 FEL mode][35794]
  * [4 Adding a serial port (**voids warranty**)][35795]
    * [4.1 Device disassembly][35796]
    * [4.2 Locating the UART][35797]
  * [5 Pictures][35798]
  * [6 Also known as][35799]
  * [7 See also][35800]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: SoftwinnerEvb
  * Kernel-Version: 3.0.8 qliu00@semitime #6 Mon Dec 10:44:01 CST 2012
  * Build Number: elite_nm307_v11-eng 4.0.4 IMMQ76D 20121210 test-keys

Incidentally, that's the same android image that is running on the [Semitime g2][35801]. 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Megafeis_A08" target.
  * The .fex file can be found in sunxi-boards as [megafeis_a08.fex][35802]

Everything else is the same as the [manual build howto][35803]. 
# Tips, Tricks, Caveats
## FEL mode
The is a UBoot button which triggers [ FEL mode][35804]. You can reach it through a hole in the case, left, about in the middle of the top cover of the device. 
# Adding a serial port (**voids warranty**)
[![][35805]][35806]
[][35807]
DEVICE UART pads
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped.
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][35808].
There are 3 obvious pads below the SoC. Two of them are bound to be RX and TX. See the [UART howto][35808] for more information on determining which is which, and how to solder on some wires. 
# Pictures
Take some pictures of your device, [ upload them][35809], and add them here.
  * [![Device front.jpg][35810]][35779]
  * [![Device back.jpg][35811]][35812]
  * [![Device buttons 1.jpg][35813]][35814]
  * [![Device buttons 2.jpg][35815]][35816]
  * [![Megafeis a08 board top.jpg][35817]][35818]
  * [![Megafeis a08 board bottom.jpg][35819]][35820]

# Also known as
# See also
  * [Semitime_g2][35801]: Different board, different exterior, but it has the same android identification strings.
