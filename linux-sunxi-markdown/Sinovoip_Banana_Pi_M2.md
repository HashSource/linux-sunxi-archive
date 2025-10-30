# Sinovoip Banana Pi M2
Banana Pi M2 is [A31s][50023] based development board produced by Sinovoip. 
**Despite its name the M2 is incompatible to Banana Pi/M1/M1+/Pro due to a different SoC - requiring different boot loaders and drivers.**
  

Sinovoip Banana Pi M2  
---  
[![Banana Pi M2 top small.jpg][50024]][50025]  
Manufacturer |  [Sinovoip][50026]  
Dimensions |  92 _mm_ x 60 _mm_  
Release Date |  May 2015   
Website |  [Device Product Page][50027]  
Specifications   
SoC |  [A31s][50028] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  \-   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive)   
Features   
Video |  HDMI (Type A - full), LVDS/RGB   
Audio |  3.5mm [TRRS/OMTP plug][50029] (stereo+mic), HDMI, on-board microphone   
Network |  WiFi 802.11 b/g/n ([Ampak AP6181][50030]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][50031])   
Storage |  µSD, no SATA   
USB |  4 USB2.0 Host (using an internal _Terminus Technology Inc. 4-Port HUB_), 1 USB2.0 OTG (µ-USB)   
Other |  IrDA   
Headers |  3 pin UART, LCD/ LVDS, CSI, 40 pin GPIO, WiFi external antenna connector (Hirose U.FL)   
## Contents
  * [1 Identification][50032]
  * [2 Sunxi support][50033]
    * [2.1 Current status][50034]
    * [2.2 Images][50035]
      * [2.2.1 Manufacturer images][50036]
    * [2.3 HW-Pack][50037]
    * [2.4 BSP][50038]
    * [2.5 Manual build][50039]
    * [2.6 Mainline U-Boot][50040]
    * [2.7 Mainline kernel][50041]
  * [3 Tips, Tricks, Caveats][50042]
    * [3.1 Powering the board][50043]
    * [3.2 Power on button][50044]
    * [3.3 Expansion Ports][50045]
  * [4 Adding a serial port][50046]
  * [5 Pictures][50047]
  * [6 Also known as][50048]
  * [7 Variants][50049]
    * [7.1 BPi-M2+][50050]
  * [8 See also][50051]

# Identification
The board reads "BPI-M2" next to a large "BPI" logo and has the same dimensions and mounting hole positions as other Banana models (to which the M2 is incompatible due to different SoC/GPU). DRAM and A31s SoC are on the upper PCB side therefore differentiation is easy by looking at the SoC's 'A31s' labelling and the four USB ports. 
# Sunxi support
## Current status
The Banana Pi M2 is only partially supported. 
The manufacturer provides some Android images that can only be burned using PhoenixCard on Windows and some Linux images that are broken more or less. The Linux images based on older Allwinner 3.3.0 kernel are broken regarding Gbit Ethernet initialisation, the ones that are based on release candidates of kernel 4.0.0 lack correct hardware initialisation in the device tree files so Wi-Fi isn't working. 
Sinovoip [cloned some github ressources][50052] where all the relevant stuff for the M2 (fex/dts files) is still missing at the time of this writing. Several months later they provide cloned linux kernel and U-Boot repos and hide the only two files of interest in there: dts and defconfig files -- see below. 
## Images
### Manufacturer images
  * Various [prebuilt images][50053] are provided via the bananapi.com website, the ones based on Linux all broken one way or the other.

## HW-Pack
## BSP
## Manual build
No support in the community maintained sunxi-3.4 kernel is planned. In the meantime the manufacturer provides an Android SDK (Allwinner kernel 3.3, U-Boot 2011.09-rc1) on [baidu.com][50054]. 
Please skip to the next Mainline U-Boot/Mainline kernel sections. 
## Mainline U-Boot
Use the **Sinovoip_BPI_M2_defconfig** (supported since v2016.01) build target. Sinovoip's [official U-Boot distribution][50055] seems unmaintained now, but when using their version, the target is **BananaPi_M2**. 
## Mainline kernel
Don't use SinoVoip's broken _[sun6i-a31s-bananapi-m2.dtb][50056]_ device-tree file but the kernel source's _sun6i-a31s-sinovoip-bpi-m2.dtb_ to be used with [mainline kernel][50057]. 
# Tips, Tricks, Caveats
## Powering the board
It's recommended to use the 4/1.7mm jack to power the board to avoid voltage drops often seen with Micro USB. When providing power using the USB OTG port the 2 USB ports next to Ethernet won't work. Any PSU advertised for Cubieboards or Orange Pis should work. 
## Power on button
Handle with care since it might break easily (3 times touched and already bent and almost broken) 
## Expansion Ports
The Banana Pi M2 exposes a 3 pin UART header, a 40 pin header with 2.54 mm pitch connectors that that mimics the Raspberry Pi A+/B+/2 models 
# Adding a serial port
[![][50058]][50059]
[][50060]
UART pins
The UART header is next to the status LEDs and the Ethernet port. Just attach some leads according to our [UART howto][50061]. 
# Pictures
  * [![Banana Pi M2 top.jpg][50062]][50063]
  * [![Banana Pi M2 bottom.jpg][50064]][50065]
  * [![Banana Pi M2 front.jpg][50066]][50067]
  * [![Banana Pi M2 back.jpg][50068]][50069]
  * [![Banana Pi M2 left.jpg][50070]][50071]
  * [![Banana Pi M2 right.jpg][50072]][50073]
  * [![Banana Pi M2 UART Power connected.jpg][50074]][50075]
  * [![Banana Pi M2 broken power-button.jpg][50076]][50077]

# Also known as
# Variants
## BPi-M2+
  * In March 2016 SinoVoip published [Banana Pi M2+][50078]. This board is based on a different SoC ([Allwinner H3][50079]), and uses a form factor of 65mm x 65mm - so expect it to be **incompatible** with the M2 in most aspects.
  * In Jun 2017 Sinovoip [published the specs][50080] for Banana Pi BPI-M2M aka [Banana Pi M2 Magic][50081], which is based on [Allwinner A33][50082]. The board also comes with an integrated amplifier for a 4ohm/2.5W speaker.

# See also
  * [Manufacturer's forum][50083]
  * [Github repository][50084]
  * [PCB Dimensions][50085]
  * [fex used for SinoVoip's kernel 3.3 based images][50086]
  * [Schematics V1.0][50087] (obvisouly for a different PCB revision, eg. RTL8188EUS/USB Wi-Fi and not AP6181/SDIO as in reality)
  * [Current Schematics][50088]
  * [LeMaker Banana Pi][50089]
  * [LeMaker Banana Pro][50090]
