# TXCZ A20
TXCZ A20  
---  
[![Txcz a20 front.jpg][53656]][53657]  
Manufacturer |  ~~[Shenzhen Tianxing Chuangzhan Electronic Co., Ltd.][53658]~~  
Dimensions |  89 _mm_ x 145 _mm_ x 24 _mm_  
Website |  Missing.   
Specifications   
SoC |  [A20][53659] @ 1Ghz   
DRAM |  512MiB DDR3 @ 384MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full), 3.5mm A/V connector.   
Audio |  3.5mm A/V connector, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][53660]), 10/100Mbps Ethernet ([ICplus IP101A][53661])   
Storage |  SD   
USB |  3 USB2.0 Host   
Other |  IRDA   
Headers |  UART pads   
This HTPC uses the same formfactor as the [Langcent H6S][53662] but has a different board and therefor different settings. 
## Contents
  * [1 Identification][53663]
  * [2 Sunxi support][53664]
    * [2.1 Current status][53665]
    * [2.2 Images][53666]
    * [2.3 HW-Pack][53667]
    * [2.4 BSP][53668]
    * [2.5 Manual build][53669]
  * [3 Tips, Tricks, Caveats][53670]
    * [3.1 FEL mode][53671]
  * [4 Adding a serial port (**voids warranty**)][53672]
    * [4.1 Device disassembly][53673]
    * [4.2 Locating the UART][53674]
  * [5 Pictures][53675]
  * [6 Also known as][53676]
  * [7 See also][53677]
    * [7.1 Manufacturer images][53678]

# Identification
The board has "TXCZ_A20_V1.0" printed on it. (There are some other devices existing with different versions numbers such as [TXCZ_A20_V3.0][53679] but they have a completely different form factor. They do report using the same model and similar build number, though, so perhaps they're compatible.) 
In android, under Settings->About Tablet, you will find: 
  * Model Number: BBA22
  * Build Number: BBA22-UI4-V2.0.4

# Sunxi support
## Current status
Supported. 
Issue: There appears to be some issues with the PHY drivers. This results in not being able to properly detect if a cable is connected to the ethernet port (it thinks there's always one connected regardless). If you're using a connection manager that tries to maintain a single connection you'll have problems. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _TXCZ_A20_ target.
  * The .fex file can be found in sunxi-boards as [txcz_a20.fex][53680]

Everything else is the same as the [manual build howto][53681]. 
# Tips, Tricks, Caveats
## FEL mode
Due to a lack of USB device ports, [FEL][53682] is not possible. 
# Adding a serial port (**voids warranty**)
[![][53683]][53684]
[][53685]
UART pads
## Device disassembly
There are no screws, only plastic clips. There is one clip on each of the 4 corners and one in the middle of each side excluding the back (so 7 clips in total). Just turn the device upside down and gently push your [plastic tool][53686] between bottom and top cover until they release. 
## Locating the UART
There is a 4 hole connector labeled J10, all you need to do is solder on some wires according to our [UART howto][53687]. 
# Pictures
  * [![Txcz a20 front.jpg][53688]][53657]
  * [![Txcz a20 back.jpg][53689]][53690]
  * [![Txcz a20 bottom.jpg][53691]][53692]
  * [![Txcz a20 side.jpg][53693]][53694]
  * [![Txcz a20 inside top.jpg][53695]][53696]
  * [![Txcz a20 inside bottom.jpg][53697]][53698]

Manufacturer provided pictures of a pre-production board: 
  * [![TXCZ A20 manufacturers top.jpg][53699]][53700]
  * [![TXCZ A20 manufactures bottom.jpg][53701]][53702]

# Also known as
  * [Ninss Tech BBA22][53703]
  * [Ninss Tech BAA22][53704]
  * Visson Android Tv Box H1
  * Visson Android Tv Box H3 (slightly different plastic box, but same inside)
  * Sunchip SDK-728 and SDK-828 (looks identical, but needs verification)

# See also
  * [Langcent H6S][53662]: a highly similar device using the same formfactor.

## Manufacturer images
