# ViPER MovieMate
ViPER MovieMate  
---  
[![ViPER MovieMate 20160129 120714.jpg][58504]][58505]  
Manufacturer |  [audlabs.com ][58506]  
Dimensions |  41mm x 68mm x 2mm   
Release Date |  May 2015   
Website |  [Product Page][58507]  
Specifications   
SoC |  [A10s][58508] @ 1Ghz   
DRAM |  128MiB DDR3 @ ?MHz ([H5TQ1G63EFR-H9C][58509])   
Power |  DC 5V @ 1A   
Features   
Audio |  3.5mm headphone plug   
Storage |  16MiB of SPI flash ([MX25L12835F][58510])   
USB |  USB2.0 OTG   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][58511] and the [New Device Page guide][58512].
This device can boot from SPI flash. 
## Contents
  * [1 Identification][58513]
  * [2 Sunxi support][58514]
    * [2.1 Current status][58515]
    * [2.2 Images][58516]
    * [2.3 HW-Pack][58517]
    * [2.4 BSP][58518]
    * [2.5 Manual build][58519]
      * [2.5.1 U-Boot][58520]
        * [2.5.1.1 Sunxi/Legacy U-Boot][58521]
        * [2.5.1.2 Mainline U-Boot][58522]
      * [2.5.2 Linux Kernel][58523]
        * [2.5.2.1 Sunxi/Legacy Kernel][58524]
        * [2.5.2.2 Mainline kernel][58525]
  * [3 Tips, Tricks, Caveats][58526]
    * [3.1 FEL mode][58527]
    * [3.2 Device specific topic][58528]
    * [3.3 ...][58529]
  * [4 Adding a serial port (**voids warranty**)][58530]
    * [4.1 Device disassembly][58531]
    * [4.2 Locating the UART][58532]
  * [5 Pictures][58533]
  * [6 Also known as][58534]
  * [7 See also][58535]
    * [7.1 Manufacturer images][58536]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Manufacturer Marketing Name
    ModelNumber
[/code]
The PCB has the following silkscreened on it: 
[code] 
    LIA-BB-V6.66
    1970-01-01
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][58535]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][58537] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][58538] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][58539]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][58540]][58541]
[][58542]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][58543]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][58544].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][58543].
# Pictures
  * [![ViPERMovieMate productB 20160129 131505.jpg][58545]][58546]
  * [![ViPERMovieMate productF 20160129 131455.jpg][58547]][58548]
  * [![ViPERMovieMate B 20160129 131648.jpg][58549]][58550]
  * [![ViPERMovieMate A 20160129 131555.jpg][58551]][58552]
  * [![ViPERMovieMate Back 20160129 131426.jpg][58553]][58554]
  * [![ViPER MovieMate 20160129 120714.jpg][58555]][58505]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
