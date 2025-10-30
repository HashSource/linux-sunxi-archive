# YBKJ A20
YBKJ A20  
---  
[![YBKJ A20-Device front.jpg][63216]][63217]  
Manufacturer |  Unknown   
Dimensions |  90 _mm_ x 120 _mm_ x 30 _mm_  
Release Date |  Unknown   
Website |  Unknown   
Specifications   
SoC |  [A20][63218] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full), Composite   
Audio |  3.5mm headphone plug, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][63219]), 10/100Mbps Ethernet ([Realtek RTL8201CP][63220])   
Storage |  SD   
USB |  2 USB2.0 Host, No USB2.0 OTG   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][63221] and the [New Device Page guide][63222].
## Contents
  * [1 Identification][63223]
  * [2 Sunxi support][63224]
    * [2.1 Current status][63225]
    * [2.2 Manual build][63226]
  * [3 Tips, Tricks, Caveats][63227]
    * [3.1 FEL mode][63228]
  * [4 Adding a serial port (**voids warranty**)][63229]
    * [4.1 Device disassembly][63230]
    * [4.2 Locating the UART][63231]
  * [5 Pictures][63232]
  * [6 Also known as][63233]
  * [7 See also][63234]

# Identification
PCB Board marked with "YBKJ_A20_V3.0". There are no other identifiable markings. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: SoftwinerEvb
  * Build Number: sugar_ref001-eng 4.2.2 JDQ39 20131115 test-keys
  * Android Kernel: 3.3.0 zhoujiequan@zhoujiequan-desktop #25

# Sunxi support
## Current status
  * U-boot patch still missing.
  * Sunxi kernel 3.4 + Debian armhf confirmed working
  * No DTB for mainline yet.

## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [ybkj_a20.fex][63235]

Everything else is the same as the [manual build howto][63236]. 
# Tips, Tricks, Caveats
## FEL mode
There is no USB OTG so [FEL mode][63237] is pointless. However, it can be triggered by sending '2' via the serial console as normal. 
# Adding a serial port (**voids warranty**)
[![][63238]][63239]
[][63240]
DEVICE UART pads
## Device disassembly
Lid is held on with a few plastic clips. I was able to remove it without any tools as it was quite loose. Just pull it off with your fingernails. 
## Locating the UART
Connector J10 is conveniently silk screened with pinout for serial port. Just solder on jumper leads according to our [UART howto][63241]. 
# Pictures
Take some pictures of your device, [ upload them][63242], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![YBKJ A20-Device front.jpg][63243]][63217]
  * [![Device back.jpg][63244]][63245]
  * [![Device buttons 1.jpg][63246]][63247]
  * [![Device buttons 2.jpg][63248]][63249]
  * [![YBKJ A20-bfront.jpg][63250]][63251]
  * [![YBKJ A20-brear.jpg][63252]][63253]

# Also known as
Gather some names.
Sold under many descriptions on Ebay. 
# See also
There's another board with the exact same PCB labelled TXCZ_A20_V3.0 but with different chips (so, would require different kernel modules).
