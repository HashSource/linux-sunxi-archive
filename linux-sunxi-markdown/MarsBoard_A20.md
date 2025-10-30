# MarsBoard A20
MarsBoard A20  
---  
[![MarsBoard A20 Overview.jpg][35650]][35651]  
Manufacturer |  [HAOYU Electronics][35652]  
Dimensions |  80 _mm_ x 55 _mm_ x 20 _mm_  
Release Date |  April 2013   
Website |  [Product page.][35653]  
Specifications   
SoC |  [A20][35654] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI,   
Network |  10/100Mbps Ethernet ([Realtek RTL8201CP][35655])   
Storage |  µSD, SATA   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Headers |  2 70pin 2mm pitch headers   
This page needs to be properly filled according to the [New Device Howto][35656] and the [New Device Page guide][35657].
The MarsBoard was a short-lived, credit-card sized, extendable board with an Allwinner [A20][35654] SoC. It is an update of the [MarsBoard A10][35658]. 
A new device by the same manufacturer is confusingly also called [Marsboard A20][35659]. It is a completely different design though, with a SOM and a baseboard. This newer board is not documented on this page. 
## Contents
  * [1 Identification][35660]
  * [2 Sunxi support][35661]
    * [2.1 Current status][35662]
    * [2.2 Images][35663]
    * [2.3 HW-Pack][35664]
    * [2.4 BSP][35665]
    * [2.5 Manual build][35666]
      * [2.5.1 Sunxi/Legacy U-Boot][35667]
    * [2.6 Mainline U-Boot][35668]
    * [2.7 Mainline kernel][35669]
  * [3 Tips, Tricks, Caveats][35670]
    * [3.1 FEL mode][35671]
  * [4 Adding a serial port][35672]
  * [5 Pictures][35673]
  * [6 See also][35674]
    * [6.1 Manufacturer images][35675]

# Identification
The board reads "www.MarsBoard.com" on top, and has an A20 SoC clearly visible. 
# Sunxi support
## Current status
Only supported by the legacy U-Boot / kernel. 
## Images
## HW-Pack
## BSP
## Manual build
#### Sunxi/Legacy U-Boot
  * For building u-boot, use the "Marsboard_A20" or "Marsboard_A20_debug" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][35676]

Everything else is the same as the [manual build howto][35677]. 
## Mainline U-Boot
Not currently supported. 
## Mainline kernel
Not currently supported. 
# Tips, Tricks, Caveats
You can install any iso-image for Cubieboard2, for example Armbian. It works fine! 
## FEL mode
A button right next to the SATA connector triggers [ FEL mode][35678]. 
# Adding a serial port
[![][35679]][35680]
[][35681]
240px UART pads
On the P2 header, pins 64, 65 and 66 are ground, TX and RX, respectively. Either solder on some leads, or insert some pins according to our [UART howto][35682]. Be warned though, this is a 2.0mm pitch connector, and not the usual 2.54mm. 
# Pictures
  * [![MarsBoard A20 Overview.jpg][35683]][35651]
  * [![MarsBoard A20 Back.jpg][35684]][35685]
  * [![MarsBoard A20 Front.jpg][35686]][35687]
  * [![MarsBoard A20 Rear.jpg][35688]][35689]
  * [![MarsBoard A20 Left.jpg][35690]][35691]
  * [![MarsBoard A20 Right.jpg][35692]][35693]

# See also
  * [File:MarsBoard Schematic V1.3.pdf][35694]
  * [Homepage.][35695] Amazingly, no information on the Marsboard A20 is still available there. That's how shortlived this device was.
  * [MarsBoard Forums (A10/A20)][35696] (The forums are awash in spam, and almost useless for purposes of information or support.)

## Manufacturer images
[Index of /marsboard][35697]
