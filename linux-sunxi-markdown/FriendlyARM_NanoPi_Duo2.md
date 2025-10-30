# FriendlyARM NanoPi Duo2
FriendlyARM NanoPi Duo2  
---  
[![FriendlyARM NanoPi Duo2 front.jpg][20380]][20381]  
Manufacturer |  [FriendlyARM][20382]  
Dimensions |  55 _mm_ x 25.4 _mm_  
Release Date |  July 2018   
Website |  [Device Product Page][20383]  
Specifications   
SoC |  [H3][20384] @ 1.2Ghz   
DRAM |  512MiB DDR3-1600   
NAND |  0   
Power |  USB OTG or pin headers, 5V, 2A per manufacturer   
Features   
LCD |  n/a   
Touchscreen |  n/a   
Video |  n/a   
Audio |  line out and mic in on pin headers   
Network |  10/100Mbps Ethernet on pin headers([H3 built-in PHY][20385]) or BT4.0/WiFi 802.11 b/g/n ([Ampak AP6212][20386])   
Storage |  µSD, SPI NOR flash footprint   
USB |  1 USB2.0 OTG, 2x USB2.0 Host on pin headers   
Other |  IRDA, 24 pin camera connector (CSI/OV5640)   
Headers |  2xUART, 1xSPI, 1xI2C, 1xEthernet, 2xUSB2.0 Host,Line out, Mic In, CVBS, IRRX   
Compared to other boards, the main selling point here is extremely compact size and ability to be plugged into a breadboard. USB OTG, functional wifi+bt, and a footprint for SPI flash round out the distinguishing features. 
## Contents
  * [1 Identification][20387]
  * [2 Sunxi support][20388]
    * [2.1 Current status][20389]
    * [2.2 Images][20390]
    * [2.3 BSP][20391]
      * [2.3.1 4.14 tree][20392]
      * [2.3.2 3.4 tree][20393]
    * [2.4 Manual build][20394]
      * [2.4.1 U-Boot][20395]
        * [2.4.1.1 Mainline U-Boot][20396]
      * [2.4.2 Linux Kernel][20397]
        * [2.4.2.1 Mainline kernel][20398]
        * [2.4.2.2 Sunxi/Legacy Kernel][20399]
    * [2.5 FEL mode][20400]
    * [2.6 LEDS][20401]
    * [2.7 WIFI/Bluetooth][20402]
    * [2.8 Locating the UART][20403]
  * [3 Pictures][20404]
  * [4 See also][20405]
    * [4.1 Manufacturer images][20406]

# Identification
The Duo2 is a small narrow black PCB, densely packed, with "NanoPi Duo2" in very small silkscreen. 
The PCB has the following silkscreened on it: 
[code] 
    NanoPi Duo2
    v1.0 1807
[/code]
# Sunxi support
## Current status
Supported in mainline from 5.5 
## Images
[[FriendlyARM provides linux 4.14 based images][20407]] 
## BSP
FriendlyARM provides both 4.14 and 3.4 legacy trees. 
### 4.14 tree
  * <https://github.com/friendlyarm/linux.git> -b sunxi-4.14.y

### 3.4 tree
There's very little reason to use this tree. The board is supported by 4.14 from FriendlyARM themselves, and in mainline from 5.5. The tree is available at <https://github.com/friendlyarm/h3_lichee.git> with [[| documentation on the FriendlyARM wiki][20408]] 
## Manual build
You can build things for yourself by following our [ Manual build howto][20409] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
There's no explicit duo2 support in U-Boot, and it's unclear if that's valuable. The [FriendlyARM_NanoPi_Air][20410] is equivalent for most purposes. Providing a separate name for the duo2 would be a trivial patch if desired. 
### Linux Kernel
#### Mainline kernel
Use the _sun8i-h3-nanopi-duo2.dtb_ device-tree binary. 
#### Sunxi/Legacy Kernel
Not documented as not considered useful at this stage. 
## FEL mode
No FEL button, the UBOOT pin is pulled up via 10K. 
## LEDS
A red and green led are available. The red is pulled up, and intended as a power indicator. Green is free for use. 
## WIFI/Bluetooth
The [Ampak AP6212][20411] is quite well supported by linux, but it does require suitable firmware files, both for the wifi portion, and the bluetooth portion. 
## Locating the UART
The primary debug uart (uart0) is on the GPIO2 header, at the end nearest the USB connector. There is silk marking RX/TX/Ground. 
# Pictures
  * [![FriendlyARM NanoPi Duo2 front.jpg][20412]][20381]
  * [![FriendlyARM NanoPi Duo2 back.jpg][20413]][20414]
  * [![FriendlyARM NanoPi Duo2 side.jpg][20415]][20416]

# See also
  * [FriendlyARM_NanoPi_Air][20410] Very similar device, largely just a form factor change
  * [Schematic for PCB rev 1.0][20417]
  * [board mechanical drawings (dxf)][20418]

## Manufacturer images
See the manufacturer's device pages above since links change from time to time.
