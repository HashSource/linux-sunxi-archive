# KOHOTECH KP100 MB V3.0
KOHOTECH KP100 MB V3.0  
---  
[![03 beam flat.jpg][29405]][29406]  
Manufacturer |  [KOHO][29407]  
Dimensions |  150 _mm_ x 110 _mm_  
Release Date |  02 2015   
Website |  [Device Product Page][29408]  
Specifications   
SoC |  [A20][29409] @ 1Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  4GB   
Power |  AC 230V @ 0.5A   
Features   
LCD |  854 x 480   
Touchscreen |  no   
Video |  LCD   
Audio |  PAM8403 audio amplifier   
Network |  WiFi 802.11 b/g/n ([Ampak AP6210][29410])   
Storage |  NAND, µSD (assembly variant)   
USB |  1 USB2.0 Host (assembly variant), 1 USB2.0 OTG (assembly variant)   
Camera |  N/A   
Other |  N/A   
Headers |  N/A   
This page needs to be properly filled according to the [New Device Howto][29411] and the [New Device Page guide][29412].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][29413]
  * [2 Sunxi support][29414]
    * [2.1 Current status][29415]
    * [2.2 Manual build][29416]
      * [2.2.1 U-Boot][29417]
        * [2.2.1.1 Sunxi/Legacy U-Boot][29418]
        * [2.2.1.2 Mainline U-Boot][29419]
      * [2.2.2 Linux Kernel][29420]
        * [2.2.2.1 Sunxi/Legacy Kernel][29421]
        * [2.2.2.2 Mainline kernel][29422]
  * [3 Tips, Tricks, Caveats][29423]
    * [3.1 FEL mode][29424]
    * [3.2 Device specific topic][29425]
    * [3.3 ...][29426]
  * [4 Adding a serial port (**voids warranty**)][29427]
    * [4.1 Device disassembly][29428]
    * [4.2 Locating the UART][29429]
  * [5 Also known as][29430]
  * [6 See also][29431]

# Identification
On the back of the device, the following is printed: 
[code] 
    Beam
    v1.01
[/code]
The PCB has the following silkscreened on it: 
[code] 
    KP100_MB_V3.0
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _[Template:Beam][29432]_
  * Build Number: _[Template:KRT16S][29433]_

# Sunxi support
## Current status
Fex file added to sunxi-boards Give a brief overview of the current status of support under sunxi here.
## Manual build
You can build things for yourself by following our [ Manual build howto][29434] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][29435] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][29436]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][29437]][29438]
[][29439]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][29440]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][29441].
## Locating the UART
The UART pins are jus tsome testpads hidden on the bottom side of the PCB. It requires opening up the device to get to them! 
  * [![KP100 MB V3.0 UART.jpg][29442]][29438]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
