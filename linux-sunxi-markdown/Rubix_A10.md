# Rubix A10
Rubix A10  
---  
[![Rubix-A10 TOP.png][47728]][47729]  
Manufacturer |  [Rubix][47730]  
Dimensions |  70 _mm_ x 73 _mm_ x 25 _mm_  
Release Date |  2013  
Website |  [(defunct)][47730]  
Specifications   
SoC |  [Allwinner A10][47731] @ 1.0Ghz   
DRAM |  1GiB DDR3L @ xxxMHz   
NAND |  4GiB, 64 bits   
Power |  DC 5V @ 2A mini-USB; DC 12V @ 1.5A adapter   
Features   
Touchscreen |  N/A   
Video |  HDMI (Type A)   
Audio |  3.5mm headphone plug, HDMI   
Network |  150MBit @ 40MHz WiFi 802.11bgn, Bluetooth 2.1/3/4/BLE ([Realtek RTL8723AS Wifi+BT Combo Module][47732])   
Storage |  µSDXC, SATA controller   
USB |  2x USB2.0 host ports, 1x mini USB2.0   
Headers |  26 pin Pi-compatible header, Arduino-compatible pass-though headers top and bottom   
This page needs to be properly filled according to the [New Device Howto][47733] and the [New Device Page guide][47734].
The Rubix A10 can be used standalone as a Linux-powered SoC single board computer, and/or as a stackable "Arduino PC shield" (little Linux PC attached atop Arduino; develop code in IDE and upload to the attached Arduino.) 
## Contents
  * [1 Identification][47735]
  * [2 Sunxi support][47736]
    * [2.1 Current status][47737]
    * [2.2 Images][47738]
    * [2.3 HW-Pack][47739]
    * [2.4 BSP][47740]
    * [2.5 Manual build][47741]
      * [2.5.1 U-Boot][47742]
        * [2.5.1.1 Sunxi/Legacy U-Boot][47743]
        * [2.5.1.2 Mainline U-Boot][47744]
      * [2.5.2 Linux Kernel][47745]
        * [2.5.2.1 Sunxi/Legacy Kernel][47746]
        * [2.5.2.2 Mainline kernel][47747]
  * [3 Tips, Tricks, Caveats][47748]
    * [3.1 FEL mode][47749]
    * [3.2 Device specific topic][47750]
    * [3.3 ...][47751]
    * [3.4 Locating the UART][47752]
  * [4 Pictures][47753]
  * [5 Also known as][47754]
  * [6 See also][47755]
    * [6.1 Manufacturer images][47756]

# Identification
The black printed circuit board reads on top side, upper right corner: 
[code] 
    RUBIX-A10 [REV 1.1]
    
[/code]
The lower left corner near the DC 12V connector reads: 
[code] 
    RUB-A1001 Copyright 2013
    
[/code]
On the back of the board near the center, the following is printed like a stylized logo as on the original packaging: 
[code] 
    Rubix A-10
    
[/code]
and beneath that logo it reads: 
[code] 
    www.SmartRubix.com
    
[/code]
The PCB has the following miscellaneous info silk-screened on the back of it: 
[code] 
    RCY-2 E10444
    132 : 94v-0it
    
[/code]
# Sunxi support
## Current status
Device shipped with Linaro Linux Desktop installed to the NAND FlashROM; kernel 3.4.x.sun4i+. It seems to be a blend of Linaro and Lubuntu 12.04. First boot hung and corrupted the NAND; subsequently booted it successfully using the same image but from microSD. Hardware support seems to be fairly complete, using supplied legacy kernel, though much more poking and testing to do. A search of Mainline Linux kernel did not reveal any .DTB or KConfigs or any mention of Rubix A10 though there are numerous other boards with this chipset in Mainline, with varying levels of hardware/device support. 
## Images
As of this writing, these Dropbox links still work, and from these, you can download the original Uboot (.img), the bootloader (.img), the entire filesystem (.tar.gz) or the entire OS bootable image (.img.gz) ready to dd onto a micro SD card and boot. 
[mmcuboot.img - Uboot image][47757]
[mmcbootloader.img - Bootloader image][47758]
[mmcrubix.tar.gz - Rubix filesystem][47759]
[mmcrubix_full.img.gz - Bootable image][47760]
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][47761] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][47762] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
**Caveat #1** : This device seems _quite uncommon_ ; searching internet for days reveals a _very_ thin assortment of threads on Arduino forums (literally about two threads), there's no community like with Pi or Arduino, barely a mention of this board anywhere except a few places including online stores which still apparently have some Rubix in stock, for sale at wildly varying prices. 
**Caveat #2** : Nothing is included in the box: no paper instructions, no SD card, no power cord or adapter, etc; nothing in there but the Rubix board, with the OS on its NAND flash ROM. And as of this writing, the SmartRubix website is defunct, so today it would be probably quite impossible to get official help or customer support. On the bright side, I will be adding here some helpful instructions (mainly Linux shell commands & procedures) from Rubix, which I have found on the internet, regarding repairing or installing the original OS to NAND or SDcard, details about the partitioning scheme, and how to rebuild or customize the original OS. 
## FEL mode
The something button probably triggers [ FEL mode][47763]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
[![][47764]][47765]
[][47766]
Rubix A10 UART pins
## Locating the UART
The RX, TX, GND pins are within the 26-pin Pi-type header near the top of the board (see image to the right). See the [[UART howto][47767]] for info about connecting to a UART using a serial terminal. 
# Pictures
  * [![][47768]][47769]
Original package 
  * [![][47770]][47729]
Board top 
  * [![][47771]][47772]
Board underside 
  * [![][47773]][47774]
Various I/O #1 
  * [![][47775]][47776]
Various I/O #2 

[![][47777]][47778]
[][47779]
Default Desktop
Default Desktop photo shows Openbox and LXpanel at first login after setting some font sizes. Rubix HDMI-out is connected to a 1680x1050 (native) LCD monitor's DVI input, using an HDMI-to-DVI adapter. Display detected & working nicely at correct resolution upon first boot; no configuring required. 
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
