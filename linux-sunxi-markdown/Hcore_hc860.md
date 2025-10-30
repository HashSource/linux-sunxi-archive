# Hcore hc860
Hcore hc860  
---  
[![Hcore hc860 full.jpeg][23872]][23873]  
Manufacturer |  [Cosmvision][23874]  
Dimensions |  130 _mm_ x 100 _mm_ x 35 _mm_  
Release Date |  December 2012   
Website |  [Product Page][23875]  
Specifications   
SoC |  [A10][23876] @ 1Ghz   
DRAM |  1GB DDR3 @ 384MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A), VGA, AV 3.5mm connector.   
Audio |  HDMI, AV breakout cable.   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CTV][23877]), 10/100Mbps Ethernet ([Realtek RTL8201CP][23878])   
Storage |  SD   
USB |  4 USB2.0 Host   
Other |  IRDA   
Headers |  UART   
## Contents
  * [1 Identification][23879]
  * [2 Sunxi support][23880]
    * [2.1 Current status][23881]
    * [2.2 Images][23882]
    * [2.3 HW-Pack][23883]
    * [2.4 BSP][23884]
    * [2.5 Manual build][23885]
  * [3 Tips, Tricks, Caveats][23886]
    * [3.1 VGA connector][23887]
    * [3.2 FEL mode][23888]
  * [4 Adding a serial port (**voids warranty**)][23889]
    * [4.1 Device disassembly][23890]
    * [4.2 Locating the UART][23891]
  * [5 Pictures][23892]
  * [6 Also known as][23893]
  * [7 See also][23894]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: SoftwinnerEvb
  * Kernel Version: 3.0.8 zjq@dell-PowerEdge-T710 #2 Thu Jan 17 11:59:39 CST 2013
  * Build Number: apollo_huangcheng-eng 4.0.4 IMM76D 20130118 test-keys

# Sunxi support
## Current status
Working. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "HCore_HC860" target.
  * The .fex file can be found in sunxi-boards as [hcore_hc860.fex][23895]

Everything else is the same as the [ Manual build howto][23896]. 
# Tips, Tricks, Caveats
## VGA connector
Like all devices derived from the Allwinner A10 reference board, this device does not have DDC support on its VGA connector, even though its connector is blue. 
## FEL mode
Forget it. There seems to be no USB device or OTG port available, so our lack of any buttons apart from power is not the only stumbling block to get to FEL mode. 
# Adding a serial port (**voids warranty**)
[![][23897]][23898]
[][23899]
DEVICE UART pads
The [UART][23900] is easy to spot on the mainboard and just needs some jumperwires soldered on. 
## Device disassembly
This set-top-box is trivially disassembled by removing some screws. 
## Locating the UART
The uart pads are located between the power-button and the ram chips. The top pin is Vcc and should not be connected. The bottom pin is obviously ground. The second pin from the top is TX. Just solder on some wires and attach a UART-USB module as described in our [UART howto][23900]. 
# Pictures
  * [![Hcore hc860 front.jpeg][23901]][23902]
  * [![Hcore hc860 top.jpeg][23903]][23904]
  * [![Hcore hc860 right.jpeg][23905]][23906]
  * [![Hcore hc860 back.jpeg][23907]][23908]
  * [![Hcore hc860 board.jpeg][23909]][23910]

# Also known as
This device carries a big "tvpad3" logo on the top, but there are no known clones so far. 
# See also
