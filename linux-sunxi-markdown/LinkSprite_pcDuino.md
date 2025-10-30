# LinkSprite pcDuino
LinkSprite pcDuino  
---  
[![Pcduino1 front.jpg][31152]][31153]  
Manufacturer |  [Linksprite][31154]  
Dimensions |  125 _mm_ x 52 _mm_ x height _mm_  
Release Date |  February 2013   
Website |  [Product Page][31155]  
Specifications   
SoC |  [A10][31156] @ 1Ghz   
DRAM |  1GiB DDR3 @ 408MHz   
NAND |  2GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full)   
Audio |  HDMI   
Network |  10/100Mbps Ethernet (Manufacturer device)   
Storage |  µSD   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART, Arduino Compatible Headers   
The LinkSprite pcDuino is an [A10][31156] based development board with [Arduino][31157] compatible headers. 
This page needs to be properly filled according to the [New Device Howto][31158] and the [New Device Page guide][31159].
## Contents
  * [1 Identification][31160]
  * [2 Sunxi support][31161]
    * [2.1 Current status][31162]
    * [2.2 Images][31163]
    * [2.3 HW-Pack][31164]
    * [2.4 BSP][31165]
    * [2.5 Manual build][31166]
      * [2.5.1 U-Boot][31167]
        * [2.5.1.1 Mainline U-Boot][31168]
      * [2.5.2 Linux Kernel][31169]
        * [2.5.2.1 Mainline kernel][31170]
  * [3 Tips, Tricks, Caveats][31171]
    * [3.1 FEL mode][31172]
  * [4 Adding a serial port][31173]
    * [4.1 Locating the UART][31174]
  * [5 Pictures][31175]
  * [6 Also known as][31176]
  * [7 See also][31177]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    LH-1
[/code]
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "pcDuino" target.
  * The .fex file can be found in sunxi-boards as [pcduino.fex][31178]

Everything else is the same as the [manual build howto][31179]. 
### U-Boot
#### Mainline U-Boot
Use the **Linksprite_pcDuino_defconfig** build target. 
### Linux Kernel
#### Mainline kernel
Use the **sun4i-a10-pcduino.dts** device-tree file for the [mainline kernel][31180]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][31181]. 
# Adding a serial port
## Locating the UART
[![][31182]][31183]
[][31184]
LinkSprite pcDuino UART pads
The RX, TX, and GND pins are located near the MENU button as shown in tthe picture. Just attach some leads according to our [UART Howto][31185]. 
# Pictures
  * [![Pcduino1 front.jpg][31186]][31153]
  * [![Pcduino1 back.jpg][31187]][31188]

# Also known as
# See also
  * [LinkSprite pcDuino Lite][31189]
  * [LinkSprite pcDuino V2][31190]
  * [LinkSprite pcDuino V3][31191]
  * [LinkSprite pcDuino Lite WiFi][31192]
  * [User Guide.][31193]
  * [Schematics.][31194]
