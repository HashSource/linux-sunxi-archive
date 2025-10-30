# IRULU X11
IRULU X11  
---  
[![Irulu x11 front.jpg][25167]][25168]  
Manufacturer |  [[1]][25169]  
Dimensions |  261 _mm_ x 163 _mm_ x 11 _mm_  
Release Date |  Month year  
Website |  [[2]][25170]  
Specifications   
SoC |  [A33][25171] @ 1,3Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  8/16GB   
Power |  DC 5V @ 2A, 5500mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (10.1" X:Y)   
Touchscreen |  5-finger capacitive ([Silead GSL3676][25172])   
Video |  None   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n, Bluetooth 4.0 ([RTL8723cs][25173])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2.0MP (1600x1200) rear   
Other |  Accelerometer ([Manufacturer device][25174])   
Headers |  None   
This page needs to be properly filled according to the [New Device Howto][25175] and the [New Device Page guide][25176].
A low-cost tablet with a 1024x600 display. It is also called iRULU eXpro X1Plus. 
## Contents
  * [1 Identification][25177]
    * [1.1 Version 1.1][25178]
    * [1.2 Version 1.2][25179]
    * [1.3 Differences 16GB Version][25180]
  * [2 Sunxi support][25181]
    * [2.1 Current status][25182]
    * [2.2 Images][25183]
    * [2.3 HW-Pack][25184]
    * [2.4 BSP][25185]
    * [2.5 Manual build][25186]
      * [2.5.1 U-Boot][25187]
        * [2.5.1.1 Sunxi/Legacy U-Boot][25188]
        * [2.5.1.2 Mainline U-Boot][25189]
      * [2.5.2 Linux Kernel][25190]
        * [2.5.2.1 Sunxi/Legacy Kernel][25191]
        * [2.5.2.2 Mainline kernel][25192]
  * [3 Tips, Tricks, Caveats][25193]
    * [3.1 FEL mode][25194]
    * [3.2 Device specific topic][25195]
    * [3.3 ...][25196]
  * [4 Adding a serial port (**voids warranty**)][25197]
    * [4.1 Device disassembly][25198]
    * [4.2 Locating the UART][25199]
  * [5 Pictures][25200]
    * [5.1 Version 1.1][25201]
    * [5.2 Version 1.2][25202]
  * [6 Also known as][25203]
  * [7 See also][25204]
    * [7.1 Manufacturer images][25205]

# Identification
There are two version of this tablet available. Both has the following printed on the back of the device: 
[code] 
    Model No.: X11
    POWER SOURCE: 5V 2.0A max
    Designed by iRULU in USA
    Assembled in China
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _X11_
  * Android version: _5.1.1_
  * Firmware version: _v3.3rc5_
  * Kernel version: _3.4.39_ builder11@YHK-T620 #36 Fri Sep 18 19:12:16 CST 2015
  * Build Number: _LMY47V.20150918_

### Version 1.1
The PCB has the following silkscreened on it: 
[code] 
    PHT
    MID_V108_V1.1
    MAINBOARD_V1.1
    151228
[/code]
### Version 1.2
The PCB has the following silkscreened on it: 
[code] 
    PHT_V108_V1.2_0901
    160901
[/code]
### Differences 16GB Version
Hardware | Version 1.1 | Version 1.2   
---|---|---  
NAND | 2x SK hynix H27UCG8T2ETR | 1x SK hynix H26M52002CKR   
RAM | 2x Samsung K4B4G08468-HCH9 | 2x Micron PE028 6HP77 D9SGR 125 (can not read)   
WLAN | [RTL8723bs][25173] | [RTL8723cs][25173]  
  

# Sunxi support
[![][25206]][25207]
[][25208]
iRULU X11 running U-BOOT
[![][25209]][25210]
[][25211]
iRULU X11 running LXDE
## Current status
TODO 
  * find the accelerometer on the pcb :)

You can boot uboot/linux with this device and the basic things are working. I'm using here Arch Linux ARM. 
  

Hardware | mainline linux | Note   
---|---|---  
v1.1 | v1.2   
CPUfreq | working | working   
LCD | no | no | works, but not good (colorless, less gamma), needs probably an init sequence (see here: [starry768x1024.c][25212], this module is used by the Android OS)   
Backlight | working | working   
Touchscreen | not tested yet | working | needs firmware "gsl1680e_101.fw" extraxted from gslX680new.ko, using ts_uinput from [tslib][25213]  
W-LAN | rtl8723bs   
working | rtl8723cs   
not tested yet | rtl8723bs is in staging since linux-4.12 (also a firmware is needed) / rtl8723cs is available out of tree   
Bluetooth | not tesetd yet | not tested yet |   
Sound | not tested yet | not tested yet |   
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][25204]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][25214] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][25215] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The Volume+ button triggers [ FEL mode][25216]. Verify with sunxi-fel: 
[code] 
    sunxi-fel -l
    USB device 008:010   Allwinner A33     0461872a:035400c2:9ab76905:00000000
    
    sunxi-fel version
    AWUSBFEX soc=00001667(A33) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
    
[/code]
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][25217]][25218]
[][25219]
UART0 on iRULU X11 V1.1
There are UART pads available on this device, but they are not tested and probably multiplexed with the microSD adapter. 
## Device disassembly
This can easily be done with a [Plastic tool][25220] or a sharp fingernail. 
## Locating the UART
[UART][25221] is located next to the CPU [A33][25171]. 
# Pictures
  * [![Irulu x11 front.jpg][25222]][25168]
  * [![Irulu x11 back.jpg][25223]][25224]
  * [![Irulu x11 inside.jpg][25225]][25226]
  * [![Irulu x11 buttons.jpg][25227]][25228]

## Version 1.1
  * [![Irulu x11 pcb v1 1.jpg][25229]][25230]

## Version 1.2
  * [![Irulu x11 pcb v1 2.jpg][25231]][25232]

# Also known as
List rebadged devices here.
# See also
  * more infos on this [external site][25233]

## Manufacturer images
Optional. Add non-sunxi images in this section.
