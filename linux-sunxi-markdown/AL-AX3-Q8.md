# AL-AX3-Q8
AL-AX3-Q8  
---  
[![Device front.jpg][5143]][5144]  
Manufacturer |  [Along][5145]  
Dimensions |  Q8   
Release Date |  June 2015  
Website |  [Device Product Page][5146]  
Specifications   
SoC |  [A33][5147] @ XGhz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ 2A, ????mAh 3.7V Li-Ion battery   
Features   
LCD |  Q8   
Touchscreen |  5-finger capacitive ([ GSL1680][5148])   
Video |  none   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer esp8089][5149])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer MMA8653FC][5150])   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][5151] and the [New Device Page guide][5152].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb. This device has eMMC pads under NAND chip 
## Contents
  * [1 Identification][5153]
  * [2 Sunxi support][5154]
    * [2.1 Current status][5155]
    * [2.2 Manual build][5156]
      * [2.2.1 Mainline U-Boot][5157]
      * [2.2.2 Mainline kernel][5158]
    * [2.3 FEL mode][5159]
    * [2.4 ...][5160]
  * [3 Adding a serial port (**voids warranty**)][5161]
    * [3.1 Device disassembly][5162]
    * [3.2 Locating the UART][5163]
  * [4 Pictures][5164]
  * [5 Also known as][5165]
  * [6 See also][5166]
    * [6.1 Manufacturer images][5167]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
The PCB has the following silkscreened on it: 
[code] 
    AL-Ax3-Q8-V1.1
    2015-01-21
[/code]
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. Works fine with q8_a33_tablet_800x480_defconfig 
## Manual build
You can build things for yourself by following our [ Manual build howto][5168] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Mainline kernel
Use the _sun8i-a33-q8-tablet.dtb_ device-tree binary. 
## FEL mode
When tablet is off, hold both volume buttons and power button, release power button and start pressing it for 3 seconds 
## ...
# Adding a serial port (**voids warranty**)
[![][5169]][5170]
[][5171]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][5172]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
2 UART pads are just below A33 SoC package. 
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][5173].
Standard Q8 disassembly applies 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][5172]. 2 UART pads are just below A33 SoC package. 
# Pictures
Take some pictures of your device, [ upload them][5174], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][5175]][5144]
  * [![Device back.jpg][5176]][5177]
  * [![Device buttons 1.jpg][5178]][5179]
  * [![Device buttons 2.jpg][5180]][5181]
  * [![Device board front.jpg][5182]][5183]
  * [![Device board back.jpg][5184]][5185]

# Also known as
List rebadged devices here.
  * AL-AX3-Q8-V6051-V2.0
  * AL-AX3-Q8-V1.1
  * MID721QC

# See also
Add some nice to have links here. This includes related devices, and external links. [High resolution photos of device internals][5186]
## Manufacturer images
Optional. Add non-sunxi images in this section.
