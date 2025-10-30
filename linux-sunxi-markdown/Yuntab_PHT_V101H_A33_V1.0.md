# Yuntab PHT V101H A33 V1.0
Yuntab PHT V101H A33 V1.0  
---  
[![PHT V101H A33 V10-front.JPG][63779]][63780]  
Manufacturer |  Yuntab   
Dimensions |  260 _mm_ x 150 _mm_ x 10 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][63781]  
Specifications   
SoC |  [A33][63782] @ XGhz   
DRAM |  512MiB/1GiB/2GiB DDR3 @ xxxMHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (X" X:Y)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][63783])   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][63784]), 10/100/1000Mbps Ethernet ([Manufacturer device][63785])   
Storage |  µSD, SATA   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][63786]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][63787] and the [New Device Page guide][63788]. INCOMPLETE - UNDER CONSTRUCTION
## Contents
  * [1 Identification][63789]
  * [2 Sunxi support][63790]
    * [2.1 Current status][63791]
    * [2.2 Images][63792]
    * [2.3 HW-Pack][63793]
    * [2.4 BSP][63794]
    * [2.5 Manual build][63795]
      * [2.5.1 U-Boot][63796]
        * [2.5.1.1 Sunxi/Legacy U-Boot][63797]
        * [2.5.1.2 Mainline U-Boot][63798]
      * [2.5.2 Linux Kernel][63799]
        * [2.5.2.1 Sunxi/Legacy Kernel][63800]
        * [2.5.2.2 Mainline kernel][63801]
  * [3 Tips, Tricks, Caveats][63802]
    * [3.1 FEL mode][63803]
    * [3.2 Device specific topic][63804]
    * [3.3 Device disassembly][63805]
    * [3.4 Locating the UART][63806]
  * [4 Pictures][63807]
  * [5 Also known as][63808]
  * [6 See also][63809]
    * [6.1 Manufacturer images][63810]

# Identification
On the back of the device, the following is printed: 
[code] 
    YUNTAB
    A33HD 8GB
[/code]
The PCB has the following silkscreened on it: 
[code] 
    PHT V101H_A33_V1.0
    2015_02_28
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _YUNTAB_
  * Processor Type: _QuadCore-A33_
  * Android-Version: _4.4.2_
  * Firmware Version: _v2.0_
  * Kernel Version: _eng06@phtaa-To-be-filled-by-O-E-M #3 Tue Dec 16 10:54:06 CST 2014_
  * Build Number: _yuntab_V101_4.4.2_20150407_

_sunxi-fel_ displays 
[code] 
    # ./sunxi-fel version
    AWUSBFEX soc=00001667(A33) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
    
[/code]
# Sunxi support
## Current status
Not supported. 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][63809]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][63811] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Using the _ga10h_v1_1_defconfig_ build target _seems_ to work (initial tests done). 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_PHT_V101H_A33_V1.0.fex_][63812] file ([Pull request][63813]). 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][63814]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## Device disassembly
The device can easily be opened with a [Plastic tool][63815] (no screws). 
## Locating the UART
The UART has not been located yet. Maybe the [UART howto][63816] helps.
# Pictures
  * [![PHT V101H A33 V10-front.JPG][63817]][63780]
  * [![PHT V101H A33 V10-back.JPG][63818]][63819]
  * [![PHT V101H A33 V10-buttons.JPG][63820]][63821]
  * [![PHT V101H A33 V10-mic-sticker.JPG][63822]][63823]
  * [![PHT V101H A33 V10-pcb.JPG][63824]][63825]

# Also known as
List rebadged devices here.
# See also
The device _seems_ to be very similar to the [IRULU X11][63826] as both have the same PCB label (PHT ...) and almost identical support chips. This [external site][63827] has some interesting info which could be helpful for the Yuntab as well. 
## Manufacturer images
