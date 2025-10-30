# Xunlong Orange Pi 3 LTS
Orange Pi 3 LTS is a successor of Orange Pi 3, with no PCIe slot, and only 1 USB3.0 port. 
Xunlong Orange Pi 3 LTS  
---  
[![OPI3LTS front.jpg][60606]][60607]  
Manufacturer |  Xunlong   
Dimensions |  width _56_ x breadth _85_  
Release Date |  Month 2022  
Website |  [[1]][60608]  
Specifications   
SoC |  [H6][60609] @ 1.8Ghz   
DRAM |  2GiB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  DC 5V @ 3A, TypeC   
Features   
Video |  HDMI (Type A - full),   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal microphone   
Network |  WiFi 802.11 b/g/n ([859][60610]), 10/100/1000Mbps Ethernet ([YT8513C][60611])   
Storage |  µSD, SATA   
USB |  1 USB3.0 + 2 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART,   
This page needs to be properly filled according to the [New Device Howto][60612] and the [New Device Page guide][60613].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][60614]
  * [2 Sunxi support][60615]
    * [2.1 Current status][60616]
    * [2.2 Images][60617]
    * [2.3 HW-Pack][60618]
    * [2.4 BSP][60619]
    * [2.5 Manual build][60620]
      * [2.5.1 U-Boot][60621]
        * [2.5.1.1 Sunxi/Legacy U-Boot][60622]
        * [2.5.1.2 Mainline U-Boot][60623]
      * [2.5.2 Linux Kernel][60624]
        * [2.5.2.1 Sunxi/Legacy Kernel][60625]
        * [2.5.2.2 Mainline kernel][60626]
  * [3 Tips, Tricks, Caveats][60627]
    * [3.1 FEL mode][60628]
    * [3.2 Device specific topic][60629]
    * [3.3 ...][60630]
  * [4 Adding a serial port (**voids warranty**)][60631]
    * [4.1 Device disassembly][60632]
    * [4.2 Locating the UART][60633]
  * [5 Pictures][60634]
  * [6 Schematic][60635]
  * [7 Also known as][60636]
  * [8 See also][60637]
    * [8.1 Manufacturer images][60638]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange  PI3 LTS 
    V1.4
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][60637]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][60639] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][60640] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][60641]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][60642]][60643]
[][60644]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][60645]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][60646].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][60645].
# Pictures
Take some pictures of your device, [ upload them][60647], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![OPI3LTS front.jpg][60648]][60607]
  * [![OPI3LTS back.jpg][60649]][60650]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
