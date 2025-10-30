# Wedo HD22
Wedo HD22  
---  
[![HD22 front.jpg][58890]][58891]  
Manufacturer |  [WeDo Innovation][58892]  
Dimensions |  93 _mm_ x 52 _mm_ x 17 _mm_  
Release Date |  December 2012   
Website |  [WeDO HD22][58893]  
Specifications   
SoC |  [A20][58894] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  8GB   
Power |  DC 5V @ 1.5A (0.75mm/2.35mm barrel plug - center positive)   
Features   
Video |  HDMI (Type A - Full), 3.5mm A/V connector   
Audio |  HDMI, 3.5mm A/V connector, 3.5mm microphone connector, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][58895])   
Storage |  µSD   
USB |  1x USB2.0 Host, 1x USB2.0 OTG   
Camera |  5.0MP (2592x1944) front (Samsung S5K4EC/OmniVision OV5640)   
Headers |  UART   
The WeDoInnov HD22 is an A20 based HTPC designed to look like a webcam. It comes with a mounting bracket so it can sit on the top of a TV set. 
## Contents
  * [1 Identification][58896]
  * [2 Sunxi support][58897]
    * [2.1 Current status][58898]
    * [2.2 Images][58899]
    * [2.3 HW-Pack][58900]
    * [2.4 BSP][58901]
    * [2.5 Manual build][58902]
  * [3 Tips, Tricks, Caveats][58903]
    * [3.1 FEL mode][58904]
    * [3.2 Camera][58905]
  * [4 Adding a serial port (**voids warranty**)][58906]
    * [4.1 Device disassembly][58907]
    * [4.2 Locating the UART][58908]
  * [5 Pictures][58909]
  * [6 Also known as][58910]
  * [7 See also][58911]
    * [7.1 Manufacturer images][58912]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: TV BOX
  * Build Number: HD22_4.2.2_V2.0_20140422

# Sunxi support
## Current status
Everything but the Samsung S5K4EC camera is supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _EU3000_ target.
  * The .fex file can be found in sunxi-boards as [eu3000.fex][58913]

Everything else is the same as the [manual build howto][58914]. 
# Tips, Tricks, Caveats
## FEL mode
There is an extra button on the PCB which can be pushed via small hole on the device's right side, in the middle before the grill. Push it during power up and it will enter into [ FEL mode][58915]. 
## Camera
Some of the early models have OmniVision OV5640 camera. More recent models come with the Samsung S5K4EC, for which no driver is currently available. 
# Adding a serial port (**voids warranty**)
[![][58916]][58917]
[][58918]
HD22 UART pads
## Device disassembly
The device is held together with three smalls screws and some plastic clips. Unscrew the three screws (one is under the QC label, this is slightly bigger then the rest), and a bit slide the bottom cover to the right (towards the two screw hole). This will unclip the plastics and you can easily detach them. 
The PCB held in place by two screws on the top casing. 
## Locating the UART
The UART pads can be found between the SoC and USB OTG connector. Just solder on some wires according to our [UART howto][58919]. Be careful though, as the pads are tiny. 
# Pictures
  * [![HD22 front.jpg][58920]][58891]
  * [![HD22 back.jpg][58921]][58922]
  * [![HD22 top.jpg][58923]][58924]
  * [![HD22 bot.jpg][58925]][58926]
  * [![HD22 box bottom.jpg][58927]][58928]
  * [![HD22 PCB top.jpg][58929]][58930]
  * [![HD22 PCB top2.jpg][58931]][58932]
  * [![HD22 PCB bot.jpg][58933]][58934]
  * [![HD22 wifi.jpg][58935]][58936]
  * [![HD22 camera.jpg][58937]][58938]

# Also known as
  * [Eny Technology EU3000][58939]
  * [U-Seek US-869][58940]

# See also
## Manufacturer images
  * [Wedo Innovation Images][58941]
