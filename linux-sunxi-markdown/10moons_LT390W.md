# 10moons LT390W
10moons LT390W  
---  
[![10moons LT390W Front.jpg][44]][45]  
Manufacturer |  [10moons][46]  
Dimensions |  125 _mm_ x 125 _mm_ x 22 _mm_  
Release Date |  Sep 2013   
Website |  [Device Product Page][47]  
Specifications   
SoC |  [A20][48] @ 1.0Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 5.5mm x 2.5mm DC Jack   
Features   
Video |  HDMI (Type A - full), 3.5mm composite A/V connector.   
Audio |  3.5mm composite A/V connector, HDMI.   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][49]), 10/100Mbps Ethernet ([ICplus IP101GA][50])   
Storage |  µSD   
USB |  2 USB2.0 Host   
Headers |  UART Connector   
This page needs to be properly filled according to the [New Device Howto][51] and the [New Device Page guide][52].
## Contents
  * [1 Identification][53]
  * [2 Sunxi support][54]
    * [2.1 Current status][55]
    * [2.2 Manual build][56]
      * [2.2.1 U-Boot][57]
        * [2.2.1.1 Sunxi/Legacy U-Boot][58]
        * [2.2.1.2 Mainline U-Boot][59]
      * [2.2.2 Linux Kernel][60]
        * [2.2.2.1 Sunxi/Legacy Kernel][61]
        * [2.2.2.2 Mainline kernel][62]
  * [3 Tips, Tricks, Caveats][63]
    * [3.1 FEL mode][64]
  * [4 Adding a serial port (**voids warranty**)][65]
    * [4.1 Device disassembly][66]
    * [4.2 Locating the UART][67]
  * [5 Pictures][68]
  * [6 Also known as][69]
  * [7 See also][70]
    * [7.1 Manufacturer images][71]

# Identification
The board has "A20-M1303 V1.6" printed on it. (There are some other devices existing with different versions numbers such as '10moons T2', '10moons LT390W Android' but they have a completely different form factor. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Supported. 
## Manual build
Wrong! You need to add a new uboot config according to the New to the [New Device Howto][51]
  * For building u-boot, use the _cubieboard2_ target with <https://github.com/linux-sunxi/u-boot-sunxi/tree/wip/a20>
  * It is essential to set CONFIG_DRAM_CLK to 432, as opposed to the default value 480 with cubieboard2
  * A preliminary version of .fex file can be found as [10moons_LT390W.fex][72]

### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][73] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The USB port next to the µSD slot is the USB OTG port. Use the button marked K2 to trigger [ FEL mode][74]. 
# Adding a serial port (**voids warranty**)
[![][75]][76]
[][77]
LT390W UART pads
## Device disassembly
Just remove all screws at the bottom. 
## Locating the UART
There is a nice 4 pin 2.54mm pitch JST-PH connector labeled J5 as its UART0 port. Just attach some wires according to our [UART howto][78]. 
# Pictures
Take some pictures of your device, [ upload them][79], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![10moons LT390W Front.jpg][80]][45]
  * [![10moons LT390W Back.jpg][81]][82]
  * [![10moons LT390W Side.jpg][83]][84]
  * [![10moons LT390W Bottom.jpg][85]][86]
  * [![10moons LT390W mb top.jpg][87]][88]
  * [![10moons LT390W mb bot.jpg][89]][90]

# Also known as
  * 10moons LT390WD
  * 10moons LT390W 双核版
  * 10moons LT390W 安卓版
  * 10moons LT390W 战斗版
  * 10moons T2
  * 10moons 电视精灵2

# See also
## Manufacturer images
  * [Manufacturer provided Android image (YunOS)][91]
