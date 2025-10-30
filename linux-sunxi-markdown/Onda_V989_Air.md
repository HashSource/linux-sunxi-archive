# Onda V989 Air
Onda V989 Air  
---  
[Onda V989 Air][41656]  
Manufacturer |  [Onda][41657]  
Dimensions |  241 _mm_ x 169 _mm_ x 7.9 _mm_  
Release Date |  February 2015   
Website |  [V989 Air Product Page][41658]  
Specifications   
SoC |  [A83T][41659] @ 2.0Ghz   
DRAM |  2GiB DDR3 @ 456MHz   
NAND |  16GB, 32GB   
Power |  DC 5V @ 2.5A, 8000mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (9.7" 1536:2048)   
Touchscreen |  10-finger capacitive ([Silead GSL1680][41660])   
Video |  No video ports   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek 8723bs][41661])   
Storage |  µSD   
USB |  1 MicroUSB port   
Camera |  1.9MP (1600x1200) front, 0.3MP (640x480) rear   
Other |  Accelerometer ([Bosch BMA250][41662])   
Headers |  UART, JTAG, LCD...   
## Contents
  * [1 Identification][41663]
  * [2 Sunxi support][41664]
    * [2.1 Current status][41665]
    * [2.2 Images][41666]
    * [2.3 HW-Pack][41667]
    * [2.4 BSP][41668]
    * [2.5 Manual build][41669]
    * [2.6 Mainline U-Boot][41670]
    * [2.7 Mainline kernel][41671]
  * [3 Tips, Tricks, Caveats][41672]
    * [3.1 FEL mode][41673]
  * [4 Adding a serial port (**voids warranty**)][41674]
    * [4.1 Device disassembly][41675]
    * [4.2 Locating the UART][41676]
  * [5 Pictures][41677]
  * [6 See also][41678]
    * [6.1 Manufacturer images][41679]

# Identification
On the back of the device, the following is printed: 
[code] 
    ONDA
    V989 AIR
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INET-N978-REV02
    Zeng-gc 2014-12-31
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _V989 Air Core8_
  * Build Number: _A83T_N978_N9781L2BC_1501088.20150527_
  * Kernel version: _Linux version 3.4.39 (inet_lzq@superFAE03) (gcc version 4.6.3 20120201 (prerelease) (crosstool-NG linaro-1.13.1-2012.02-20120222 - Linaro GCC 2012.02))_

# Sunxi support
Needs a lot of work. 
## Current status
No Uboot defconfig at this moment. 
No defconfig in linux-sunxi project. 
A83T kernel sources were released April, 17 2015 [Github][41680]
## Images
No sunxi images availible at this moment. See Manufacturer images
## HW-Pack
No HW-pack availible. 
## BSP
No BSP availible. 
## Manual build
  * For building U-Boot, use the _onda_v989_air_defconfig_ target, which will soon be added.
  * The .fex file soon could be found in sunxi-boards as [onda_v989_air.fex][41681]

Everything else is the same as the [manual build howto][41682]. 
## Mainline U-Boot
If there is mainline U-Boot support, add this section.
For [ building mainline U-Boot][41683], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][41684]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][41685]. 
# Adding a serial port (**voids warranty**)
[![][41686]][41687]
[][41688]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][41689]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][41690].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][41689].
# Pictures
Take some pictures of your device, [ upload them][41691], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][41692]][41693]
  * [![Device back.jpg][41694]][41695]
  * [![Device buttons 1.jpg][41696]][41697]
  * [![Device buttons 2.jpg][41698]][41699]
  * [![Device board front.jpg][41700]][41701]
  * [![Device board back.jpg][41702]][41703]

# See also
[Topic on Onda Forums][41704]
## Manufacturer images
LiveSuit/OndaSuit/PhoenixSuit image (android version 4.4.4) [Yandex Disk][41705]
