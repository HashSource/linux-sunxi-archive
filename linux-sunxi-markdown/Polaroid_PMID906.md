# Polaroid PMID906
Polaroid PMID906  
---  
[![Device front.jpg][45455]][45456]  
Manufacturer |  [Polaroid][45457]  
Dimensions |  24 _mm_ x 15 _mm_ x 10 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][45458]  
Specifications   
SoC |  [A13][45459] @ 1Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ 3A, 3600mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (9" 16:9)   
Touchscreen |  X-finger capacitive ([ Focaltech FT5406EE8][45460])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CTV][45461])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][45462] FIXME)   
Headers |  UART, JTAG   
This page needs to be properly filled according to the [New Device Howto][45463] and the [New Device Page guide][45464].
## Contents
  * [1 Identification][45465]
  * [2 Sunxi support][45466]
    * [2.1 Current status][45467]
    * [2.2 Images][45468]
    * [2.3 HW-Pack][45469]
    * [2.4 BSP][45470]
    * [2.5 Manual build][45471]
  * [3 Tips, Tricks, Caveats][45472]
    * [3.1 FEL mode][45473]
  * [4 Adding a serial port (**voids warranty**)][45474]
    * [4.1 Device disassembly][45475]
    * [4.2 Locating the UART][45476]
  * [5 Pictures][45477]
  * [6 Also known as][45478]
  * [7 See also][45479]

# Identification
  * Model Number: PMID900
  * Build Number: 05.01.001.004.11

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][45480]

Everything else is the same as the [manual build howto][45481]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][45482]. 
# Adding a serial port (**voids warranty**)
[![][45483]][45484]
[][45485]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][45486]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
See [the Q8 tablet format disassembly page][45487]. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][45486].
# Pictures
Take some pictures of your device, [ upload them][45488], and add them here.
  * [![Polaroid PMID906 front.jpeg][45489]][45490]
  * [![Device back.jpg][45491]][45492]
  * [![Device buttons 1.jpg][45493]][45494]
  * [![Device buttons 2.jpg][45495]][45496]
  * [![Polaroid PMID906 mainboard.jpeg][45497]][45498]
  * [![Device board back.jpg][45499]][45500]

  * [![Polaroid PMID906 front.jpeg][45489]][45490]
  * [![Polaroid PMID906 mainboard.jpeg][45497]][45498]
  * [![Polaroid PMID906 chips.jpeg][45501]][45502]
  * [![Polaroid PMID906 sidecons.jpeg][45503]][45504]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
