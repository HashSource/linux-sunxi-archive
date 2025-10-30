# Icoo d90w
Icoo d90w  
---  
[![Device front.jpg][25556]][25557]  
Manufacturer |  [Icoo][25558]  
Dimensions |  243.84 _mm_ x 187.96 _mm_ x 9.53 _mm_  
Release Date |  February 2012   
Website |  [Product Page][25559]  
Specifications   
SoC |  [A10][25560] @ 1Ghz   
DRAM |  1GiB DDR3 @ 408MHz   
NAND |  8/16GB   
Power |  DC 5V @ 3A, 7400mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (9.7" 4:3 IPS)   
Touchscreen |  10-finger capacitive ([Goodix GT801 2+1][25561])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188CUS)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 1.3MP (1280x1024) rear   
Other |  Accelerometer ([Manufacturer device][25562] FIXME)   
Headers |  ???   
This page needs to be properly filled according to the [New Device Howto][25563] and the [New Device Page guide][25564].
## Contents
  * [1 Identification][25565]
    * [1.1 Icoo D90w][25566]
    * [1.2 Coby Kyros MID 9742][25567]
  * [2 Sunxi support][25568]
    * [2.1 Current status][25569]
    * [2.2 Images][25570]
    * [2.3 HW-Pack][25571]
    * [2.4 BSP][25572]
    * [2.5 Manual build][25573]
  * [3 Tips, Tricks, Caveats][25574]
    * [3.1 FEL mode][25575]
  * [4 Adding a serial port (**voids warranty**)][25576]
    * [4.1 Device disassembly][25577]
    * [4.2 Locating the UART][25578]
  * [5 Pictures][25579]
  * [6 Also known as][25580]
  * [7 See also][25581]

# Identification
In android, under Settings->About Tablet, you will find... 
## Icoo D90w
  * Model Number: D90
  * Build Number: 20120323.142651

## Coby Kyros MID 9742
  * Model Number: MID9742
  * Build Number: 20120701.123627

# Sunxi support
## Current status
No patches were ever made available. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][25582]

Everything else is the same as the [manual build howto][25583]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][25584]. 
# Adding a serial port (**voids warranty**)
[![][25585]][25586]
[][25587]
DEVICE UART pads
## Device disassembly
First remove the 4 screws in the corners, then use your [plastic tool][25588] to push the edge of the back cover outwards. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][25589].
# Pictures
Take some pictures of your device, [ upload them][25590], and add them here.
  * [![Device front.jpg][25591]][25557]
  * [![Device back.jpg][25592]][25593]
  * [![Device buttons 1.jpg][25594]][25595]
  * [![Device buttons 2.jpg][25596]][25597]
  * [![Icoo-d90w-board.jpg][25598]][25599]
  * [![Device board back.jpg][25600]][25601]

# Also known as
The board was made by Shenzhen Sochip Technology Limited, and is named Sochip SC3052. Searching for this reveals several rebadges. 
  * [Icoo D90W][25602].
  * Coby Kyros MID9742
  * MP MAN MP2000 (MP948)
  * SYSBAY S-MP99

# See also
