# Semitime g2
Semitime g2  
---  
[![Semitime g2 front.jpg][49078]][49079]  
Manufacturer |  [Semitime][49080]  
Dimensions |  88.5 _mm_ x 35 _mm_ x 13.4 _mm_  
Release Date |  December 2012   
Website |  [Reseller Product Page][49081]  
Specifications   
SoC |  [A10s][49082] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type C - mini)   
Audio |  HDMI, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8189ES][49083])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  none!   
This is an obvious [Rikomagic MK802+][49084] clone, but it contains an [A10s][49082] SoC instead. It is not clear whether it was ever sold by Rikomagic itself, or whether it was only marketed by third parties. 
## Contents
  * [1 Identification][49085]
  * [2 Sunxi support][49086]
    * [2.1 Current status][49087]
    * [2.2 Images][49088]
    * [2.3 HW-Pack][49089]
    * [2.4 BSP][49090]
    * [2.5 Manual build][49091]
    * [2.6 Mainline kernel][49092]
  * [3 Tips, Tricks, Caveats][49093]
    * [3.1 FEL mode][49094]
  * [4 Adding a serial port (**voids warranty**)][49095]
    * [4.1 Device disassembly][49096]
    * [4.2 Locating the UART][49097]
  * [5 Pictures][49098]
  * [6 Also known as][49099]
  * [7 See also][49100]

# Identification
This device is clearly marked as an MK802+ on the case, and is often sold as such. It however has 1GB of RAM and an A10s chip inside. The paper manual mentions "AK-212MinPC". The board is marked as "ST-G2", together with the kernel version strings, this led us to the manufacturer. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: SoftwinnerEvb
  * Kernel-Version: 3.0.8 qliu00@semitime #6 Mon Dec 10:44:01 CST 2012
  * Build Number: elite_nm307_v11-eng 4.0.4 IMMQ76D 20121210 test-keys

Incidentally, that's the same android image that is running on the [ Megafeis A08][49101]. 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Semitime_G2" target.
  * The .fex file can be found in sunxi-boards as [semitime_g2.fex][49102]

Everything else is the same as the [manual build howto][49103]. 
## Mainline kernel
Use the _sun5i-a10s-mk802.dts_ device-tree file for the [mainline kernel][49104]. 
# Tips, Tricks, Caveats
## FEL mode
There is a special button to trigger [ FEL mode][49105]. You can reach it through the bottom-left hole of the top cover of the device. 
# Adding a serial port (**voids warranty**)
[![][49106]][49107]
[][49108]
Bad routing: Not a UART!
## Device disassembly
The three piece case is clicked together. Do not try to get the semi-transparent bit around the USB Host connector off, as it is clipped into the top and you could damage the clip. Just gently push your [plastic tool][49109] between the bottom and the top, and push the top part of the shell outwards. You will soon hear the clips release. 
## Locating the UART
On the board labelled **VER:1.0** , due to bad routing, the two pads which were meant to be the [UART][49110] instead turned out to be PB11 and PB14, rendering them useless. You will have to resort to a [MicroSD breakout board][49111] to get serial on this device. 
# Pictures
  * [![Semitime g2 front.jpg][49112]][49079]
  * [![Semitime g2 back.jpg][49113]][49114]
  * [![Semitime g2 board front.jpg][49115]][49116]
  * [![Semitime g2 board back.jpg][49117]][49118]

# Also known as
  * It is often branded as an A10s based [MK802+][49084], but it just shares the external packaging and has MK802+ written on the top cover.

# See also
  * [Rikomagic MK802][49119]: The 512MiB [A10][49120] based original, which has the same case.
  * [Rikomagic MK802+][49084]: The 1GiB [A10][49120] based device, which also has the same case.
  * [Megafeis A08][49101]: Different board, different exterior, but it has the same android identification strings.
