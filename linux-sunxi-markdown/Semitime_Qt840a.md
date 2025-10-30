# Semitime Qt840a
Semitime Qt840a  
---  
[![Qt840a front.jpg][48992]][48993]  
Manufacturer |  [Semitime][48994]  
Dimensions |  100 _mm_ x 100 _mm_ x 23 _mm_  
Release Date |  November 2013   
Website |  [Device Product Page][48995]  
Specifications   
SoC |  [A20][48996] @ 1Ghz   
DRAM |  512MiB DDR3 @ 384MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full), 3.5mm A/V connector   
Audio |  3.5mm A/V connector, HDMI, internal microphone   
Network |  WiFi 802.11 b/g/n ([Broadcom AP6330][48997]), 10/100Mbps Ethernet ([ICplus IP101GA][48998])   
Storage |  µSD   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  Bluetooth ([Broadcom AP6330][48999]), IRDA  
Headers |  UART, JTAG   
This page needs to be properly filled according to the [New Device Howto][49000] and the [New Device Page guide][49001].
This HTPC uses a pretty common case design, and sometimes can be found as the _Q5_ or _I12_TvBox_ or unbranded. But whereas the _Q5_ or _I12_TvBox_ use a [Ampak AP6210][49002] Wifi/BT module, the QT840 uses the [Ampak AP6330][49002]. 
## Contents
  * [1 Identification][49003]
  * [2 Sunxi support][49004]
    * [2.1 Current status][49005]
    * [2.2 Images][49006]
    * [2.3 HW-Pack][49007]
    * [2.4 BSP][49008]
    * [2.5 Manual build][49009]
    * [2.6 Mainline kernel][49010]
  * [3 Tips, Tricks, Caveats][49011]
    * [3.1 FEL mode][49012]
    * [3.2 JTAG][49013]
  * [4 Adding a serial port (**voids warranty**)][49014]
    * [4.1 Device disassembly][49015]
    * [4.2 Locating the UART][49016]
  * [5 Pictures][49017]
  * [6 Also known as][49018]
  * [7 See also][49019]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: SoftwinerEvb
  * Build Number: homelet_sugar 4.2.2 JDQ39 xxxxx test-keys

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "qt840a" target.
  * The .fex file can be found in sunxi-boards as [qt840a.fex][49020]

Everything else is the same as the [manual build howto][49021]. 
## Mainline kernel
Use the sun7i-a20-i12-tvbox.dts device-tree file for the [mainline kernel][49022]. 
# Tips, Tricks, Caveats
## FEL mode
The push button on the rearside of the board triggers [ FEL mode][49023]. 
## JTAG
There are some JTAG pads right next to the [ UART pads][49016]. Here is the pin-out: 
  * TP3: JTAG-MS
  * TP4: JTAG-CK
  * TP5: JTAG-DO
  * TP6： JTAG-DI

# Adding a serial port (**voids warranty**)
[![][49024]][49025]
[][49026]
QT840a UART pads
## Device disassembly
Only clips attach the top of the case to the rest of it. Insert your [plastic tool][49027] along the top edge, and gently push the outside rim outwards, the clips should soon release. 
## Locating the UART
There are some clearly visible test pads next to the SoC. All you need to do is attach some wires according to our [UART howto][49028]. 
Pin-out: 
  * TP1: UART0-TX
  * TP2: UART0-RX

# Pictures
Take some pictures of your device, [ upload them][49029], and add them here.
  * [![Qt840a front.jpg][49030]][48993]
  * [![Qt840a connectors 1.jpg][49031]][49032]
  * [![Qt840a connectors 2.jpg][49033]][49034]
  * [![Qt840a button.jpeg][49035]][49036]
  * [![Device board front.jpg][49037]][49038]
  * [![Device board back.jpg][49039]][49040]

# Also known as
# See also
