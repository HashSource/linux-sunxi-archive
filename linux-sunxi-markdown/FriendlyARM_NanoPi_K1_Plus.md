# FriendlyARM NanoPi K1 Plus
FriendlyARM NanoPi K1 Plus  
---  
[![Device front.jpg][20456]][20457]  
Manufacturer |  [FriendlyARM][20458]  
Dimensions |  56 _mm_ x 85 _mm_  
Release Date |  Month year  
Website |  [FriendlyARM NanoPi K1 Plus page][20459]  
Specifications   
SoC |  [H5][20460] @ 1.3Ghz   
DRAM |  2GiB DDR3 @ xxxMHz   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI 1.4, SPDIF on GPIO connector, separate I2S connector   
Network |  WiFi 802.11 b/g/n (PCB antenna), 10/100/1000Mbps Ethernet ([Manufacturer device][20461])   
Storage |  µSD, eMMC (4.x/5.1)   
USB |  2x2 USB2.0 Host, 1x USB2.0 OTG   
Camera |  DVP Camera Interface   
Other |  Onboard PCB microphone, 1 x GPIO button   
Headers |  Debug UART, CVBS   
This page needs to be properly filled according to the [New Device Howto][20462] and the [New Device Page guide][20463].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][20464]
  * [2 Sunxi support][20465]
    * [2.1 Current status][20466]
    * [2.2 Images][20467]
    * [2.3 HW-Pack][20468]
    * [2.4 BSP][20469]
    * [2.5 Manual build][20470]
      * [2.5.1 U-Boot][20471]
        * [2.5.1.1 Sunxi/Legacy U-Boot][20472]
        * [2.5.1.2 Mainline U-Boot][20473]
      * [2.5.2 Linux Kernel][20474]
        * [2.5.2.1 Sunxi/Legacy Kernel][20475]
        * [2.5.2.2 Mainline kernel][20476]
  * [3 Tips, Tricks, Caveats][20477]
    * [3.1 FEL mode][20478]
    * [3.2 Device specific topic][20479]
    * [3.3 ...][20480]
  * [4 Adding a serial port (**voids warranty**)][20481]
    * [4.1 Device disassembly][20482]
    * [4.2 Locating the UART][20483]
  * [5 Pictures][20484]
  * [6 Also known as][20485]
  * [7 See also][20486]
    * [7.1 Manufacturer images][20487]

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
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][20486]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][20488] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][20489] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][20490]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][20491]][20492]
[][20493]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][20494]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][20495].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][20494].
# Pictures
Take some pictures of your device, [ upload them][20496], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][20497]][20457]
  * [![Device back.jpg][20498]][20499]
  * [![Device buttons 1.jpg][20500]][20501]
  * [![Device buttons 2.jpg][20502]][20503]
  * [![Device board front.jpg][20504]][20505]
  * [![Device board back.jpg][20506]][20507]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
