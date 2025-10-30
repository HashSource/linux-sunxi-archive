# Sunvell R69
Sunvell R69  
---  
[![][51781]][51782] [][51783]Sunvell-r69-front-up  
Manufacturer |  [Sunvell][51784]  
Dimensions |  110 _mm_ x 110 _mm_ x 17.5 _mm_  
Release Date |  April 2017   
Website |  [Sunvell][51785]  
Specifications   
SoC |  [H2+][51786] @ 1.0Ghz   
DRAM |  1GiB DDR3 (different batches use different modules)   
NAND |  8GB (eMMC 4.51 on red board, MLC NAND on blue board)   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full)   
Audio |  A/V jack   
Network |  WiFi 802.11 b/g/n (XR819), 10/100Mbps Ethernet ()   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 OTG as type A   
Other |  IR receiver for remote   
Headers |  UART (internal), unknown 4-pin (internal)   
This page needs to be properly filled according to the [New Device Howto][51787] and the [New Device Page guide][51788].
The Sunvell R69 is an inexpensive TV Box/multimedia player based on Allwinner's H2+ SoC. 
## Contents
  * [1 Identification][51789]
  * [2 Sunxi support][51790]
    * [2.1 Current status][51791]
    * [2.2 Images][51792]
    * [2.3 Manual build][51793]
      * [2.3.1 U-Boot][51794]
      * [2.3.2 Linux Kernel][51795]
  * [3 Tips, Tricks, Caveats][51796]
    * [3.1 FEL mode][51797]
    * [3.2 WiFi][51798]
    * [3.3 VDD_CPUX][51799]
  * [4 Adding a serial port (**voids warranty**)][51800]
    * [4.1 Device disassembly][51801]
    * [4.2 Locating the UART][51802]
  * [5 Pictures][51803]
  * [6 Also known as][51804]
  * [7 See also][51805]
    * [7.1 Manufacturer images][51806]

# Identification
"R69" logo embossed on top cover of the device with a green border. 
In Android my version (bought 08.11.2017 ships from China) shows, under Settings->About box, you will find: 
My version shows in Android, 
  * Model Number: Mbox
  * Android version: 6.0.1 (but is fake, if you click many times the Android display the Kit-Kat Android logo)
  * Firmware Version: V2
  * Kernel version: 3.4.39 it01@it01 #0
  * Build Number: V2

A later version (using a blue PCB, and MLC NAND), ships with a much newer Android: 
  * Device name: TVBOX
  * Android version: 7.1.2 (also shows the Nougat version, so probably legit this time)
  * Kernel version: 4.4.55, built Oct 2018
  * PCB silk screen: R69-8x4BIT DDR3_V1.0 2018-06-05

# Sunxi support
## Current status
There used to be Armbian-based builds available for this box as CSC-builds (Community-supported) for kernel versions 5.3 ("current") and 5.4 ("dev") as of December 2019. 
## Images
Armbian preliminary support on forum [H2: Sunvell R69 Android TV Box][51807] starting with version 5.34 (see [to download an Ubuntu working version and additional details and tweaks][51808]). 
## Manual build
You can build things for yourself by following our [ Manual build howto][51809] and by choosing from the configurations available below. 
### U-Boot
Not yet available. 
### Linux Kernel
Not yet available. 
# Tips, Tricks, Caveats
There are at least two versions of the PCB. Earlier builds (2017) use a red PCB and contain (perfectly usable) eMMC storage, but the later blue PCB (2018) seems to be shipped with raw MLC NAND flash, which is not supported in mainline U-Boot or Linux. Both version still carry the footprint for both eMMC and MLC NAND, so variations are possible. 
The R69 is configured to boot from µSD first, so testing an alternative OS is simple. Linux images for other H2 or H3 devices can be booted, but provide incorrect GPIO assignments for at least the power LED, USB ports and so on. The most up to date fex file for the device might be in [Armbian github repository][51810]
The box contains a dual-color LED (blue and red). The blue part works fine, but the light of the red one is almost perfectly filtered by the semi-translucent plastic case, so it is not visible from the outside. 
## FEL mode
FEL mode can be triggered by pushing the Button inside the AV Jack with a nonconductive tool, like a toothpick while powering the board on. The R69 exposes H2's USB OTG port as a type A receptacle on the back next to the power socket which can be used with a male-to-male type A USB cable. The Board has boot priority for SD Card, then eMMC. FEL Mode can also be entered with a [special][51811] SD card image. 
## WiFi
PCB revision on PCB is H2-20170615-V1.3 came with XR819. 
## VDD_CPUX
According to vendor fex no voltage regulation is implemented and the CPU cores are fed with 1.2V which allows the H2+ to be clocked with 1008 MHz maximum. 
# Adding a serial port (**voids warranty**)
[![][51812]][51813]
[][51814]
UART pads
[![][51815]][51816]
[][51817]
UART pads back side
The R69 UART runs at 3.3V levels, so you need a level converter (e.g. MAX3323) to connect the board to a regular serial port. Alternatively, a USB-to-UART adapter with 3.3V levels will also work. See the [UART howto][51818] for details. 
## Device disassembly
The case is clipped together using plastic tabs on all four sides. Please see the [Plastic tool howto][51819] for details of opening cases like these. The PCB is held in place by three small Philips-head screws. Make sure to remove the µSD card before taking out the PCB. The H2+ chip is attached to an internal heat sink using a thermal pad. 
## Locating the UART
The UART (3.3V levels) is available on four solder holes (2mm spacing) in the front side. Soldering in a header will void the warranty. 
The pins are labelled **using USB-UART adapter** : 
  * Pin 1: 3V
  * Pin 2: URX
  * Pin 3: UTX
  * Pin 4: GND

Alternatively the UART pads can be accessed from the back of the board, without removing it from the case. Temporary headers can be friction fit with sufficient stability. 
# Pictures
  * [![Sunvell-r69-front-up.jpg][51820]][51782]
  * [![Sunvell-r69-front-back.jpg][51821]][51822]
  * [![Sunvell-r69-side.jpg][51823]][51824]
  * [![Sunvell-r69-back.jpg][51825]][51826]
  * [![Sunvell-r60-box-bottom.jpg][51827]][51828]
  * [![Sunvell-r60-board-bottom.jpg][51829]][51830]
  * [![Sunvell-r60-board-top.jpg][51831]][51832]
  * [![Sunvell-r60-board-wifi.jpg][51833]][51834]
  * [![Sunvell-r60-board-ram-emmc.jpg][51835]][51836]
  * [![Sunvell-r60-buttom.jpg][51837]][51838]
  * [![Sunvell-r60-uart3.jpg][51839]][51840]
  * [![Sunvell-r60-uart2.jpg][51841]][51842]
  * [![Sunvell-r60-uart1.jpg][51843]][51844]
  * [![Sunvell-R69-TTL-From-Top.jpg][51845]][51816]
  * [![Sunvell R69 Thermal Top.jpg][51846]][51847]
  * [![Sunvell R69 Thermal Bot.jpg][51848]][51849]
  * [![Sunvell r69 blue top.jpg][51850]][51851]
  * [![Sunvell r69 blue bottom.jpg][51852]][51853]

# Also known as
This box is also sold as "OSORIO M9S" or "OSORIO M9S V6" - confusingly a S905-based TV box is sold under the same name. 
# See also
  * [Thread on the armbian forum][51807]

## Manufacturer images
Optional. Add non-sunxi images in this section.
