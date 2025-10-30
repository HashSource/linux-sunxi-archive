# TBS A711
TBS A711  
---  
[![TBS A711 front.jpg][53307]][53308]  
Manufacturer |  [TBS AG][53309]  
Dimensions |  approx. 226 _mm_ x 122 _mm_ x 11 _mm_  
Release Date |  2017   
Specifications   
SoC |  [A83T][53310] @ 2.0 Ghz   
DRAM |  1 GiB LPDDR3 @ 732 MHz   
NAND |  8 GB (eMMC)   
Power |  6000 mAh 3.7V Li-Ion battery, AXP813 PMIC   
Features   
LCD |  1024x600 (7" 16:9)   
Touchscreen |  Multitouch capacitive FT5xxx ([Focaltech][53311])   
Audio |  3.5 mm TRRS microphone and headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Ampak AP6210][53312]), combined with BlueTooth   
Storage |  µSD, eMMC   
USB |  3 USB2.0 internal hosts, 1 USB2.0 OTG   
Camera |  1 MP front, 5 MP (2592x1944) rear   
Other |  Accelerometer ([Bosch BMA250][53313]), magnetic sensor, GPS, light sensor, fingerprint reader   
## Contents
  * [1 Identification][53314]
  * [2 Sunxi support][53315]
    * [2.1 Current status][53316]
    * [2.2 Manual build][53317]
      * [2.2.1 U-Boot][53318]
        * [2.2.1.1 Sunxi/Legacy U-Boot][53319]
        * [2.2.1.2 Mainline U-Boot][53320]
      * [2.2.2 Linux Kernel][53321]
        * [2.2.2.1 Sunxi/Legacy Kernel][53322]
        * [2.2.2.2 Mainline kernel][53323]
  * [3 Tips, Tricks, Caveats][53324]
    * [3.1 LCD and touch issues][53325]
    * [3.2 FEL mode][53326]
  * [4 Adding a serial port (**voids warranty**)][53327]
    * [4.1 Device disassembly][53328]
    * [4.2 Locating the UART][53329]
  * [5 Pictures][53330]
  * [6 Miscellaneous][53331]

# Identification
There is nothing printed on the back of the device in the rectangle designed for it. There is "TBS" and logo on the front side. 
The PCB has the following silkscreened on it: 
[code] 
    A711 A83T V2.0
    2016.01.20
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: Octopus A83 F1
  * Build Number: octopus_a711-eng

# Sunxi support
## Current status
The device is supported. 
## Manual build
Support in the community maintained sunxi-3.4 kernel is not planned. 
Fex file patch was sent to the mailing list ([https://www.mail-archive.com/[email protected]/msg21573.html][53332]). 
### U-Boot
#### Sunxi/Legacy U-Boot
Device was originally shipped with u-boot-2011.09. 
#### Mainline U-Boot
Supported since 2018.01. 
Devicetree source: sun8i-a83t-tbs-a711.dts 
Defconfig: tbs_a711_defconfig 
Working branch was: <https://github.com/tbs-biometrics/u-boot-a711/tree/tbs/2017.07>
### Linux Kernel
#### Sunxi/Legacy Kernel
Allwinner kernel 3.4.39 was used. 
#### Mainline kernel
Starting 4.15 there is _sun8i-a83t-tbs-a711.dts_ devicetree source in mainline. 
Working branch for basic support: <https://github.com/tbs-biometrics/linux-a711/tree/tbs/4.13>
Working branch for CSI support: <https://github.com/megous/linux/tree/linux-tbs>
# Tips, Tricks, Caveats
## LCD and touch issues
There were a few revisions of the board. The changes were in the LCD timing (timing changes just in the fex file) and a touchscreen configuration (`ctp_exchange_x_y_flag` and `ctp_revert_*_flag` were inverted). 
## FEL mode
There is a footprint labeled UBOOT on the board. It is located near the CPU. It is not tested but it should be usable to go into the [ FEL mode][53333]. 
# Adding a serial port (**voids warranty**)
[![][53334]][53335]
[][53336]
TBS A711 UART connector
There is an easily accessible UART receptacle on the board (you need to disassemble the tablet to access them). 
## Device disassembly
  1. There are four screws on the sides of the tablet. Unscrew them.
  2. You need to pop the pins to remove the back side. [Plastic tool][53337] is very helpful.

## Locating the UART
UART recetacle is labeled UART0 and it is located near the soldering pads for vibrator. It operates at 3 V. See the image for the pin assignment and [UART howto][53338] for more information. 
# Pictures
  * [![TBS A711 front.jpg][53339]][53308]
  * [![TBS A711 back.jpg][53340]][53341]
  * [![TBS A711 buttons.jpg][53342]][53343]
  * [![TBS A711 board front.jpg][53344]][53345]
  * [![Device board back.jpg][53346]][53347]

# Miscellaneous
Some tablets were donated to the community. The number of tablets for community is limited now (this may change in the future). See [https://www.mail-archive.com/[email protected]/msg21568.html][53348].
