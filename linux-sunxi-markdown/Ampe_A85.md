# Ampe A85
Ampe A85  
---  
TBD  
Manufacturer |  Ampe or Sanei   
Dimensions |  210 _mm_ x 155 _mm_ x 10 _mm_  
Release Date |  March 2012   
Website |  [(defunct)][7303]  
Specifications   
SoC |  [A10][7304] @ 1Ghz   
DRAM |  1GiB DDR3 @ 456MHz   
NAND |  8GB or possibly 16GB   
Power |  DC 5V, 3600mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (8" IPS)   
Touchscreen |  5-point capacitive ([Focaltech ft5x_ts][7305])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, built-in microphone, HDMI   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8192cu][7306])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][7307]  
This page needs to be properly filled according to the [New Device Howto][7308] and the [New Device Page guide][7309].
## Contents
  * [1 Identification][7310]
    * [1.1 Hardware][7311]
  * [2 Sunxi support][7312]
    * [2.1 Current status][7313]
    * [2.2 Images][7314]
    * [2.3 HW-Pack][7315]
    * [2.4 BSP][7316]
    * [2.5 Manual build][7317]
    * [2.6 Mainline kernel][7318]
  * [3 Tips, Tricks, Caveats][7319]
    * [3.1 FEL mode][7320]
  * [4 Adding a serial port (**voids warranty**)][7321]
    * [4.1 Device disassembly][7322]
    * [4.2 Locating the UART][7323]
  * [5 Pictures][7324]
  * [6 Also known as][7325]
  * [7 See also][7326]

# Identification
From the script.fex, the device is also identified as follows: 
[code] 
    [product]
    version = "1.0"
    machine = "A10-EVB-V1.1"
    
[/code]
The PCB has the following silkscreened on it: 
[code] 
    A970T V1.3
[/code]
This board is shared with other tablets, probably with a 9.7" display ('9.7 LCD' is silkscreened near the display connector). It probably has the same board as the [Sanei N90][7327]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _A7 HD_
  * Build Number: _RKS7S01_A7HD_20120412_

## Hardware
  * NAND: 8Gb Micron 29F64G08CBAAA x 1 (or x2 for 16Gb version)
  * RAM: 4 x 256Mb Hynix H5TQ2G83CFR DDR3
  * PMU: AXP209
  * Touchscreen controller: Focaltech FT5406EE8
  * Wifi: Realtek 8188CUS
  * Bluetooth: RDA5876 with FM tuner

# Sunxi support
## Current status
Unknown 
## Images
## HW-Pack
## BSP
## Manual build
TBD 
## Mainline kernel
TBD 
# Tips, Tricks, Caveats
## FEL mode
TBD 
  

# Adding a serial port (**voids warranty**)
TBD 
## Device disassembly
Carefully insert your [plastic tool][7328] into the long edges, and push the plastic outwards while pushing the aluminium back plate inward, and work the whole 2 long sides. Now insert your plastic tool into the short edge, and push the aluminium backplate outwards. 
## Locating the UART
TBD 
# Pictures
  * TBD

# Also known as
  * This device was sold as the Ampe A85 Deluxe and also the Sanei N83 Deluxe.
  * The board may have been implemented in other Ampe / Sanei A10 tablet products

# See also
[[1]][7329]
