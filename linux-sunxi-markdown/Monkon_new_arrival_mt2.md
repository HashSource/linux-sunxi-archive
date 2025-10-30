# Monkon new arrival mt2
Monkon new arrival mt2  
---  
[![Monkon mt2 front.jpeg][38443]][38444]  
Manufacturer |  [Unidentified Manufacturer][38445]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  September 2014 (At least)   
Website |  [Missing Device Product Page][38446]  
Specifications   
SoC |  [A20][38447] @ 1Ghz   
DRAM |  1GiB DDR3 @ xxxMHz (Hynix h5tq1g63dfr)   
Power |  USB, 400mAh 3.3V Li-Ion battery   
Features   
LCD |  WidthxHeight (2.7" X:Y)   
Video |  HDMI (Type B - mini), AV connector   
Audio |  HDMI, internal speaker, internal microphone, AV connector   
Storage |  µSD, 8MiB SPI Flash (Macronix MX 25L6406E M2I-126)   
USB |  1 USB2.0 OTG   
Camera |  2MP (1920x1080) front (separate module)   
Other |  6 LEDs attached to camera module.   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][38448] and the [New Device Page guide][38449].
The Monkon New Arrival MT2 is an [A20][38447] based "DashCam" (Dashboard camera), which does not even run linux or android from its 8MiB SPI ROM. It is very cheap and very bad for what it is supposed to do, and the reviews on amazon.co.uk are terrible. 
## Contents
  * [1 Identification][38450]
  * [2 Sunxi support][38451]
    * [2.1 Current status][38452]
    * [2.2 Manual build][38453]
      * [2.2.1 U-Boot][38454]
        * [2.2.1.1 Sunxi/Legacy U-Boot][38455]
        * [2.2.1.2 Mainline U-Boot][38456]
      * [2.2.2 Linux Kernel][38457]
        * [2.2.2.1 Sunxi/Legacy Kernel][38458]
        * [2.2.2.2 Mainline kernel][38459]
  * [3 Tips, Tricks, Caveats][38460]
    * [3.1 FEL mode][38461]
  * [4 Adding a serial port (**voids warranty**)][38462]
    * [4.1 Device disassembly][38463]
    * [4.2 Locating the UART][38464]
  * [5 Pictures][38465]
  * [6 Also known as][38466]
  * [7 See also][38467]
    * [7.1 Manufacturer images][38468]

# Identification
On the camera side of the device, the following is printed: 
[code] 
    CAR CAM CORDER
[/code]
and 
[code] 
    FHD 1080p
[/code]
The Monkon badge was crudely glued on the back of the Monkon rebadged device. 
The back of the mainboard has the following silkscreened on it: 
[code] 
    TF101_JQ537_MAIN V1.4
    2014-09-30
[/code]
# Sunxi support
## Current status
Not supported. 
Since this hardware is not using a linux or an android, it remains to be seen what can be retrieved from the SPI rom. There is a good chance that support will have to be created from scratch. 
## Manual build
You can build things for yourself by following our [ Manual build howto][38469] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][38470]file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][38471]. 
# Adding a serial port (**voids warranty**)
[![][38472]][38473]
[][38474]
Monkon MT2 UART pads (unconfirmed)
## Device disassembly
Remove the 4 tiny screws, and then you can carefully remove the front bezel with your [Plastic tool][38475]. 
Start from the top edge (the side without the buttons). This side needs to be moved in, as there are two clips which need to be pushed inwards, and which then easily release from the rest of the housing. The two sides can then be pushed outwards from the main housing, so the clips there release. Rotate the bezel slightly, and the most fragile clip at the bottom of the bezel should give way. 
Dismantling the rest of the device should now be straightforward. 
## Locating the UART
There are 4 pads north of the DRAM module, which are marked: _GND_ , _5V_ , _5V_ and _RX_. The TX is probably one of the 5V lines. Just solder on some wires according to our [UART howto][38476]. 
So far, no UART output has been detected. 
# Pictures
  * [![Monkon mt2 front.jpeg][38477]][38444]
  * [![Monkon mt2 back.jpeg][38478]][38479]
  * [![Monkon mt2 top.jpeg][38480]][38481]
  * [![Monkon mt2 bottom.jpeg][38482]][38483]
  * [![Monkon mt2 left.jpeg][38484]][38485]
  * [![Monkon mt2 board front.jpeg][38486]][38487]
  * [![Monkon mt2 board back.jpeg][38488]][38489]
  * [![Monkon mt2 internal camera module.jpeg][38490]][38491]
  * [![Monkon mt2 internal camera connected.jpeg][38492]][38493]
  * [![Monkon mt2 internal reassembled.jpeg][38494]][38495]

# Also known as
The Monkon is clearly a cheap rebadge job, and will have been sold under a few different guises, and can still easily be found on aliexpress. 
# See also
## Manufacturer images
