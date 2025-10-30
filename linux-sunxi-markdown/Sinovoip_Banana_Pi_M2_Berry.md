# Sinovoip Banana Pi M2 Berry
Sinovoip Banana Pi M2 Berry  
---  
[![BananaPi M2B Berry Front.JPG][50129]][50130]  
Manufacturer |  [Sinovoip][50131]  
Dimensions |  92 _mm_ x 60 _mm_ x 20 _mm_  
Release Date |  May 2017   
Website |  [BPI-M2B Product Page][50132]  
Specifications   
SoC |  [Allwinner V40][50133] @ 1.2Ghz   
DRAM |  1GiB DDR3 @ 576MHz ([Samsung K4B4G1646D-BCK0][50134] x2)   
Power |  DC 5V @ 2A Micro USB   
Features   
Video |  HDMI 1.4 @ 1080P60  
MIPI DSI (RAW LCD panels)   
Audio |  3.5mm headphone plug  
HDMI   
Network |  WiFi 802.11 b/g/n (AMPAK AP6212)  
10/100/1000Mbps Ethernet (Realtek RTL8211E/D)  
Bluetooth4.0 (AMMPAK AP6212)   
Storage |  MicroSD (up to 64 GB)  
SATA   
USB |  4x USB2.0 Host (via hub chip)  
USB2.0 OTG   
Camera |  CSI Connector   
Headers |  UART, GPIO, I2S, I2C, SPI   
This seems to be a cheaper version of the [Banana Pi M2 Ultra][50135], with only 1GB of DRAM and no eMMC. At least it still features the SATA port. 
The used SoC is a [V40][50133], but that seems to be the same as the [R40][50136]. 
## Contents
  * [1 Identification][50137]
  * [2 Sunxi support][50138]
    * [2.1 Current status][50139]
    * [2.2 Manual build][50140]
      * [2.2.1 Mainline U-Boot][50141]
      * [2.2.2 Mainline Linux Kernel][50142]
  * [3 Tips, Tricks, Caveats][50143]
    * [3.1 FEL mode][50144]
    * [3.2 SATA / power][50145]
    * [3.3 Locating the UART][50146]
  * [4 Pictures][50147]
  * [5 See also][50148]
    * [5.1 Manufacturer images][50149]

# Identification
The PCB has the following silkscreened on the front: 
[code] 
    (Banana Pi Logo) BPI-M2-Berry V1.0
[/code]
# Sunxi support
## Current status
Many features (video, USB, Ethernet, SATA) are supported by mainline Linux, but audio support is missing (see the R40 column of the [status matrix][50150] for more details). 
U-Boot support is usable, but video output is still missing. 
## Manual build
You can build things for yourself by following our [ Manual build howto][50151] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the **bananapi_m2_berry_defconfig** build target. 
### Mainline Linux Kernel
Use the **sun8i-v40-bananapi-m2-berry.dtb** device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
There is no dedicated FEL button on the board, but as there is no onboard storage, just booting without a microSD card (or using one without a valid eGON header) will trigger [FEL mode][50152]. 
## SATA / power
The official way to power the board is via the microUSB socket. As the SATA power socket on the board is also powered from this input, you need to have a good cable and a decent power supply to run (low power!) hard disks from this. Doing so will lose the USB OTG port, so powering via GPIO or powering the hard drive separately might be the better option. 
## Locating the UART
[UART][50153] port is preinstalled on the device right next to one of the USB ports. TX pin is the closest to the edge of the board, next to it RX, then GND (see Picture below) 
# Pictures
  * [![][50154]][50130]
Front 
  * [![][50155]][50156]
Back 
  * [![][50157]][50158]
Power and reset button 
  * [![][50159]][50160]
UART port 

# See also
[Banana Pi M2 Berry board schematic][50161]  
[Banana Pi M2 Ultra][50135] (bigger version with 2GB DRAM and eMMC)  
[Device page on Banana Pi Wiki][50162]  
[Official Forum][50163]  

## Manufacturer images
[Manufacturer images on Banana Pi Wiki page][50164]
