# MarsBoard A10
MarsBoard A10  
---  
[![Marsboard A10 front.JPG][35489]][35490]  
Manufacturer |  [HAOYU Electronics][35491]  
Dimensions |  80 _mm_ x 55 _mm_ x 20 _mm_  
Release Date |  March 2013   
Website |  [www.marsboard.com][35492]  
Specifications   
SoC |  [A10][35493] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI   
Network |  10/100Mbps Ethernet (Realtek RTL8201CP)   
Storage |  µSD, SATA   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Headers |  2 70pin 2mm pitch headers   
This page needs to be properly filled according to the [New Device Howto][35494] and the [New Device Page guide][35495].
The MarsBoard was a short-lived credit-card sized, extendable board with an Allwinner [A10][35493] SoC. 
## Contents
  * [1 Identification][35496]
  * [2 Sunxi support][35497]
    * [2.1 Current status][35498]
    * [2.2 Images][35499]
    * [2.3 HW-Pack][35500]
    * [2.4 BSP][35501]
    * [2.5 Manual build][35502]
      * [2.5.1 U-Boot][35503]
        * [2.5.1.1 Sunxi/Legacy U-Boot][35504]
        * [2.5.1.2 Upstream/Mainline U-Boot][35505]
      * [2.5.2 Linux Kernel][35506]
        * [2.5.2.1 Sunxi/Legacy Kernel][35507]
        * [2.5.2.2 Upstream/Mainline kernel][35508]
  * [3 Tips, Tricks, Caveats][35509]
    * [3.1 FEL mode][35510]
    * [3.2 JTAG][35511]
    * [3.3 Expansion Headers][35512]
  * [4 Adding a serial port][35513]
  * [5 Pictures][35514]
  * [6 Also known as][35515]
  * [7 See also][35516]
    * [7.1 Manufacturer images][35517]

# Identification
The board reads "www.MarsBoard.com" on top, and has an A10 SoC clearly visible. 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
You can build things for yourself by following our [ Manual build howto][35518] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _Marsboard_A10_ build target. 
#### Upstream/Mainline U-Boot
Use the _Marsboard_A10_ target for building [mainline U-Boot][35519]. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_marsboard_a10.fex_][35520] file. 
#### Upstream/Mainline kernel
Use the _sun4i-a10-marsboard.dtb_ device-tree binary for the [mainline kernel][35521]. 
# Tips, Tricks, Caveats
## FEL mode
The single button near SATA port triggers [ FEL mode][35522]. 
## JTAG
[This page explains how to attach JTAG to your marsboard.][35523]
## Expansion Headers
Board have 2 x 70 pin [expansion headers][35524]. 
# Adding a serial port
[![][35525]][35526]
[][35527]
Marsboard A10 UART pads
On the P2 header, pins 64, 65 and 66 are ground, TX and RX, respectively. Attach some 2.0mm pitch leads according to our [UART howto][35528]. 
# Pictures
  * [![Marsboard A10 front.JPG][35529]][35490]
  * [![Marsboard A10 back.JPG][35530]][35531]
  * [![Marsboard A10 left.JPG][35532]][35533]
  * [![Marsboard A10 right.JPG][35534]][35535]

# Also known as
# See also
  * [File:MarsBoard Schematic V1.3.pdf][35536]
  * [Homepage.][35492] Amazingly, no information on the Marsboard A10 is still available there. That's how shortlived this device was.
  * [MarsBoard Forums (A10/A20)][35537]

## Manufacturer images
[Index of /marsboard][35538]
