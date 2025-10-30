# YBKJ A20 JN
YBKJ A20 JN  
---  
[![Ybkj a20 jn overview.jpg][63289]][63290]  
Manufacturer |  Unknown   
Dimensions |  150 _mm_ x 93 _mm_ x 23 _mm_  
Release Date |  August 2014   
Website |  Unknown   
Specifications   
SoC |  [A20][63291] @ 1Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full), 3.5mm AV connector   
Audio |  HDMI, SPDIF, 3.5mm AV connector   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][63292]), 10/100Mbps Ethernet ([Realtek RTL8201CP][63293])   
Storage |  SD   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][63294] and the [New Device Page guide][63295].
This A20 HTPC uses the same case as the [TXCZ A20][63296] and the [Langcent h6s][63297] HTPCs, but it comes without an external Wifi antenna. What puts this device apart from other A20 devices is that there is no Power management IC (normally an AXP209). 
## Contents
  * [1 Identification][63298]
  * [2 Sunxi support][63299]
    * [2.1 Current status][63300]
    * [2.2 Images][63301]
    * [2.3 HW-Pack][63302]
    * [2.4 BSP][63303]
    * [2.5 Manual build][63304]
  * [3 Tips, Tricks, Caveats][63305]
    * [3.1 FEL mode][63306]
    * [3.2 Picky SDCard][63307]
  * [4 Adding a serial port][63308]
    * [4.1 Device disassembly][63309]
    * [4.2 Locating the UART][63310]
  * [5 Pictures][63311]
  * [6 Also known as][63312]
  * [7 See also][63313]

# Identification
The device is completely generic, there are no labels of any kind and it comes in a plain brown cardboard box, obviously without any manual. The only markings on the black plastic case are the green Android Robot logo and "Smart Media Player" written in small characters. 
The PCB has the following silkscreened on it: 
[code] 
    YBKJ_A20_JN_V2.2
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: **SoftwinerEvb**
  * Build Number: **sugar_ref001-eng 4.2.2 JDQ39 20140403 test-keys**

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _YBKJ_A20_JN_ target (not found).
  * The .fex file can be found in sunxi-boards as [ybkj_a20_jn.fex][63314]

Everything else is the same as the [manual build howto][63315]. 
# Tips, Tricks, Caveats
## FEL mode
TODO: verify that USB OTG works.
Between the DC power connector and the SPDIF, there is a pinhole. Behind this is the button which triggers [ FEL mode][63316]. The OTG port is the USB host port on the back. 
## Picky SDCard
It seems this board is quite picky with the brand/type of SD card it will accept. The only accepted SDCard [the owner of this hardware][63317] has now is a Samsung Class 10 16GB microSD card with an original Samsung microSD to SD adapter. 
[![][63318]][63319]
[][63320]
UART pads
# Adding a serial port
## Device disassembly
There are no screws holding the two halves of the case together. The bottom half has a big clip in each corner, and small clips in the middle of all sides except the back. Carefully insert your [plastic tool][63321] between the two halves, and gently push the clips to the inside until you release them. Start with one corner and progressively work your way around the case edge. 
Be careful when opening the device, as the cable to the WiFi antenna (glued to the top cover) is quite short. 
## Locating the UART
While there are 3 UART connectors on the board, the one between the WiFi module and the RAM chip is _UART0_ which can be used for u-boot and kernel debugging. It is clearly labeled, just solder on some wires according to the [UART howto][63322]. 
# Pictures
TODO: provide a new pair of pictures for the connectors, with light coming from a different angle, so that the engraved text under the connectors can be read.
  * [![Ybkj a20 jn front.jpg][63323]][63324]
  * [![Ybkj a20 jn back.jpg][63325]][63326]
  * [![Ybkj a20 jn side.jpg][63327]][63328]
  * [![Ybkj a20 jn unboxing.jpg][63329]][63330]
  * [![Ybkj a20 jn board front.jpg][63331]][63332]
  * [![Ybkj a20 jn board back.jpg][63333]][63334]

# Also known as
# See also
  * [YBKJ A20][63335]: Another A20 HTPC, different form factor, components and PCB, but apparently from the same PCB designer ("YBKJ").
  * [TXCZ A20][63296]: Same form factor HTPC, different PCB and components.
  * [Langcent h6s][63297]: Same form factor HTPC, different PCB and components.
