# Pcduino8 A80 Board
Pcduino8 A80 Board  
---  
[![A80 Pcduino8 Board Front.jpg][44083]][44084] [][44085]  
Manufacturer |  [Pcduino][44086]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  August 2014   
Website |  [Device Product Page][44087]  
Specifications   
SoC |  [A80][44088] @ 1008Mhz   
DRAM |  2GiB DDR3 @ 672MHz (SK hynix H5TQ4G63AFR-PBC 4Gb * 4)   
NAND |  8GB NAND(SK-Hynix H27UCG8T2BTA-B031)   
Power |  DC 5V @ 3A, optional Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug   
Network |  WiFi 802.11 b/g/n ([Ampak AP6330][44089]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][44090])   
Storage |  µSD   
USB |  2 USB2.0 Host, 1 USB3.0 OTG   
Other |  IRDA   
Headers |  UART, JTAG, LiPo Battery, Camera interface, GPIOs   
This page needs to be properly filled according to the [New Device Howto][44091] and the [New Device Page guide][44092].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
The A80 Pcduino8 Board is the first commercially available board for the Allwinner [A80][44088] SoC. For most parts the Pcduino8 board is identical to the [Merrii A80 Optimus Board][44093], however this one has NAND IC instead of EMMC. 
## Contents
  * [1 Identification][44094]
  * [2 Sunxi support][44095]
    * [2.1 Current status][44096]
    * [2.2 Images][44097]
    * [2.3 HW-Pack][44098]
    * [2.4 BSP][44099]
    * [2.5 Manual build][44100]
    * [2.6 Mainline U-Boot][44101]
    * [2.7 Mainline kernel][44102]
  * [3 Tips, Tricks, Caveats][44103]
    * [3.1 FEL mode][44104]
    * [3.2 Android][44105]
      * [3.2.1 Partition Table][44106]
      * [3.2.2 Source Code][44107]
    * [3.3 ...][44108]
  * [4 Adding a serial port][44109]
  * [5 Pictures][44110]
  * [6 See also][44111]
    * [6.1 Manufacturer images][44112]

# Identification
The board has a clearly recognizable Pcduino beta label on it, and its white, a common PCB overlay color for all Pcduino products. 
  
In android, under Settings->About Tablet, you will find: 
  * Model Number: UltraOcta A80 OptimusBoard (Its not a mistake. It actually reports a different board as the model)
  * Build Number: KOT49H

# Sunxi support
## Current status
Not supported yet. 
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][44111]
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here.
## BSP
Add MANUFACTURER DEVICE BSP specifics here.
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][44113]

Everything else is the same as the [manual build howto][44114]. 
## Mainline U-Boot
Not supported yet. 
## Mainline kernel
Not supported yet. 
If there is mainline kernel support, add this section.
Use the FAMILY-CHIP-DEVICE.dtb device-tree file for the [mainline kernel][44115]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
FEL mode yet to be found on the Pcduino8, one button acts as hard-reset, other one as power key(used in Android) 
## Android
It comes with Android 4.4.2 KOT49H, and 3.4 based kernel. 
### Partition Table
bootloader = /dev/block/nanda 
env = /dev/block/nanda 
boot = /dev/block/nandc 
system = /dev/block/nandd 
misc = /dev/block/nande 
recovery = /dev/block/nandf 
cache = /dev/block/nandg 
metadata = /dev/block/nandh 
private = /dev/block/nandi 
UDISK(userdata) = /dev/block/nandj 
### Source Code
Kernel source: 
A80 common device: <https://github.com/skoperst/android_device_sunxi_kylincommon> Pcduino8 device: <https://github.com/skoperst/android_device_sunxi_kylinoptimus>
How to compile CWM/AOSP based recovery for the device: 
[code] 
    . build/envsetup
    lunch kylin_optimus-eng
    make recoveryimage
[/code]
## ...
# Adding a serial port
The UART header is next to the Ethernet port. Use the provided UART cable. 
# Pictures

# See also
Pcduino's guide to flashing android image: <http://learn.linksprite.com/pcduino/quick-start/pcduino8/re-flash-android-image-to-pcduino8-beta/>
## Manufacturer images
Image provided by Pcduino(Should be used with PhoenixCard-309 method): 
<https://s3.amazonaws.com/pcduino/Images/8beta/Android/sun9iw1p1_android_optimus.img>
