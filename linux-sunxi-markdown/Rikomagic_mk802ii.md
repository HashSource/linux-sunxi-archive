# Rikomagic mk802ii
Rikomagic mk802ii  
---  
[![Mk802ii-front.jpg][47557]][47558]  
Manufacturer |  [Rikomagic][47559]  
Dimensions |  90 _mm_ x 30 _mm_ x 13 _mm_  
Release Date |  September 2012   
Website |  [MK802ii Product Page][47560]  
Specifications   
SoC |  [A10][47561] @ 1Ghz   
DRAM |  1GiB DDR3 @ 408MHz   
NAND |  4GB   
Power |  DC 5V through a separate USB Mini port   
Features   
Video |  HDMI (Type A - male)   
Audio |  HDMI   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188CUS)   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART   
This is a completely redesigned version of the [MK802 HDMI Stick][47562]. The most stricking difference is that it has a male HDMI connector for plugging straight into a monitor or TV. 
It seems that there are at least 2 different case designs for the MK802II. They both share the same innards though. 
## Contents
  * [1 Identification][47563]
  * [2 Sunxi support][47564]
    * [2.1 Current status][47565]
    * [2.2 Images][47566]
    * [2.3 HW-Pack][47567]
    * [2.4 BSP][47568]
    * [2.5 Manual build][47569]
    * [2.6 Mainline U-Boot][47570]
    * [2.7 Mainline kernel][47571]
  * [3 Tips, Tricks, Caveats][47572]
    * [3.1 FEL mode][47573]
  * [4 Adding a serial port (**voids warranty**)][47574]
    * [4.1 Device disassembly][47575]
    * [4.2 Locating the UART][47576]
  * [5 Pictures][47577]
  * [6 Also known as][47578]
  * [7 See also][47579]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: Rikomagic MK802II
  * Build Number: RKM-emg4.0.4IMM76D20121206

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "mk802ii" target.
  * The .fex file can be found in sunxi-boards as [mk802ii.fex][47580]

Everything else is the same as the [manual build howto][47581]. 
## Mainline U-Boot
For [ building mainline u-boot][47582], use the _mk802ii_defconfig_ board name. 
## Mainline kernel
Use the _sun4i-a10-mk802ii.dts_ device-tree file for the [mainline kernel][47583]. 
# Tips, Tricks, Caveats
## FEL mode
There is a hole next to the SD slot, under which is the "uboot" button which triggers [ FEL mode][47584]. 
# Adding a serial port (**voids warranty**)
[![][47585]][47586]
[][47587]
MK802ii UART pads
## Device disassembly
The bottom cover clips into the top cover, so you need to push the sides of the top cover outwards with your [plastic tool][47588]. Start at the HDMI connector, as you have some purchase there. The mainboard is clicked into the top cover, and also requires some wriggling to get out. 
## Locating the UART
There are some minuscule pads on the bottom side of the board, as shown in the picture. You need to have decent soldering skills to be able to attach wires to those. More information is available in the [UART howto][47589]. 
# Pictures
  * [![][47590]][47558]
Mk802ii top view 
  * [![][47591]][47592]
Mk802ii back view 
  * [![][47593]][47594]
Mk802ii top PCB layer 
  * [![][47595]][47596]
Mk802ii bottom PCB layer 
  * [![][47597]][47598]
A slightly altered case. 
  * [![][47599]][47600]
The back view of the different case. 
  * [![][47601]][47602]
USB power and host 
  * [![][47603]][47604]
USB OTG, Uboot hole and microSD 

# Also known as
The exterior is clearly marked as MK802, but neither shares the board or the case with [that device][47562], and the formfactor is slightly different. 
# See also
  * [Rikomagic MK802][47562]: The original MK802.
  * [Two users add a UART on the Rikomagic forums][47605]
