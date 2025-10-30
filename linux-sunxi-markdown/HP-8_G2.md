# HP-8 G2
HP-8 G2  
---  
[![Device front.jpg][23571]][23572]  
Manufacturer |  Neostra Industrial(HK)Ltd   
Dimensions |  width _137mm_ x breadth _12mm_ x height _200mm_  
Release Date |  Feb 2014   
Website |  <https://support.hp.com/us-en/product/hp-8-g2-tablet/7174132/model/7450677>  
Specifications   
SoC |  A33 @ 1.2 Ghz   
DRAM |  1GiB DDR3 @ 552 MHz   
NAND |  16GB eMMC   
Power |  DC 5V @ 2A, 4000mAh 3.7V Li-Ion battery   
Features   
LCD |  Width x Height (7.85" 1024:768) IPS [LP079X01]   
Touchscreen |  Multitouch [GT911_MB783Q6]   
Video |  Internal LCD   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n [AP6476], Bluetooth 4 + LE   
Storage |  µSD,   
USB |  Micro USB 2.0   
Camera |  0.3MP front, 2.0MP rear   
Other |  Accelerometer, GPS   
Headers |  Unknown UART and JTAG might be accessible via SD card, requires breakout board   
  

## Contents
  * [1 Identification][23573]
  * [2 Sunxi support][23574]
    * [2.1 Current status][23575]
    * [2.2 Images][23576]
    * [2.3 HW-Pack][23577]
    * [2.4 BSP][23578]
    * [2.5 Manual build][23579]
      * [2.5.1 U-Boot][23580]
        * [2.5.1.1 Sunxi/Legacy U-Boot][23581]
        * [2.5.1.2 Mainline U-Boot][23582]
      * [2.5.2 Linux Kernel][23583]
        * [2.5.2.1 Sunxi/Legacy Kernel][23584]
        * [2.5.2.2 Mainline kernel][23585]
    * [2.6 FEL mode][23586]
    * [2.7 Note][23587]
    * [2.8 Device disassembly][23588]
    * [2.9 Locating the UART][23589]
  * [3 Pictures][23590]
  * [4 Also known as][23591]
  * [5 See also][23592]
    * [5.1 Manufacturer images][23593]

# Identification
HP 8 G2 Model Model no. 1411 
On the back of the device, the following is printed: 
[code] 
    HP 8
    PN J5T67AA
    RMN HSTNH-N408F
    
[/code]
The PCB has the following silkscreened on it: 
[code] 
    Unknown
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: HP 8 G2
  * Build Number: KVT49L20150123

# Sunxi support
## Current status
Not supported 
## Images
No official images exist, HP provide an update.zip from which fex files can be extracted 
## HW-Pack
Unknown 
## BSP
Unknown 
## Manual build
Unknown 
### U-Boot
#### Sunxi/Legacy U-Boot
Unknown 
#### Mainline U-Boot
The unit will begin to boot if u-bot if built with Sinlinx_SinA33_defconfig 
Interfaces appear and disappear while booting, but attempts to connect so far have been unsuccessful. Because the LCD isn't correctly configured no console shows on the screen. 
The unit shares more similarities with PHT_801H_A33_V1.0.fex but no defconfig file exists 
### Linux Kernel
#### Sunxi/Legacy Kernel
Unknown 
#### Mainline kernel
Unknown 
## FEL mode
The unit can be put into FEL mode by booting with a suitable microsd card. See instructions for sunxi-tools 
## Note
If connected via adb attempts to access bootloader or fastboot softbricks the device. 
It MAY be possible to recover by allowing the battery to run completely flat, turn the unit on, wait for boot logo to appear, leave device to run down. 
## Device disassembly
HP provide an illustrated guide for disassembly in the Service Document for this device. 
## Locating the UART
It may be possible to access the UART via the microSD slot 
# Pictures
  * [![Device front.jpg][23594]][23572]

# Also known as
The device was designed and manufactured for HP, no other versions are known. 
# See also
None 
## Manufacturer images
Refer to HP website
