# Sinovoip Banana Pi BPI-6204
Sinovoip Banana Pi BPI-6204  
---  
[![Device front.jpg][49767]][49768]  
Manufacturer |  [Sinovoip][49769]  
Dimensions |  105 _mm_ x 145 _mm_ x 36 _mm_  
Release Date |  ~May 2024   
Website |  [BPI-6202/6204 Product Page][49770]  
Specifications   
SoC |  [A40i][49771] @ 1.2Ghz   
DRAM |  2GiB DDR3 (SK Hynix KH5TQ4G83EFR-RDC x4)   
NAND |  8GB eMMC 5.1 (Samsung KLM8G1GETF-B041)   
Power |  DC 24V @ 1A   
Features   
Video |  HDMI 1.4 (Type A - full)   
Network |  WiFi 802.11 b/g/n (AMPAK AP6212)  
10/100/1000Mbps Ethernet (Realtek RTL8211E)  
10/100 Ethernet (IC+ IP101GR)  
Bluetooth4.0 (AMMPAK AP6212)   
Storage |  MicroSD (up to 64 GB)  
M.2 (B-Key) SSD SATA   
USB |  2x USB2.0 Host  
USB2.0 OTG   
Other |  M.2 (B-Key) for 4G/5G LTE w/micro SIM  
4x RS485, RS232, CAN   
Headers |  GPIO, SPI   
This page needs to be properly filled according to the [New Device Howto][49772] and the [New Device Page guide][49773].
Industrial controller with full-featured SCADA system 
The used SoC is a [A40i][49771], but that seems to be the same as the [R40][49774] except with industrial temperature range. 
## Contents
  * [1 Identification][49775]
  * [2 Sunxi support][49776]
    * [2.1 Current status][49777]
    * [2.2 Images][49778]
    * [2.3 HW-Pack][49779]
    * [2.4 BSP][49780]
    * [2.5 Manual build][49781]
      * [2.5.1 U-Boot][49782]
        * [2.5.1.1 Sunxi/Legacy U-Boot][49783]
        * [2.5.1.2 Mainline U-Boot][49784]
      * [2.5.2 Linux Kernel][49785]
        * [2.5.2.1 Sunxi/Legacy Kernel][49786]
        * [2.5.2.2 Mainline kernel][49787]
  * [3 Tips, Tricks, Caveats][49788]
    * [3.1 FEL mode][49789]
    * [3.2 Device specific topic][49790]
    * [3.3 ...][49791]
  * [4 Adding a serial port (**voids warranty**)][49792]
    * [4.1 Device disassembly][49793]
    * [4.2 Locating the UART][49794]
  * [5 Pictures][49795]
  * [6 Schematic][49796]
  * [7 See also][49797]
    * [7.1 Manufacturer images][49798]

# Identification
The PCB has the following silkscreened on the front: 
[code] 
    CSA6204-A0
    scada
[/code]
  

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][49797]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][49799] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][49800] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][49801]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][49802]][49803]
[][49804]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][49805]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][49806].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][49805].
# Pictures
Take some pictures of your device, [ upload them][49807], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][49808]][49768]
  * [![Device back.jpg][49809]][49810]
  * [![Device buttons 1.jpg][49811]][49812]
  * [![Device buttons 2.jpg][49813]][49814]
  * [![Device board front.jpg][49815]][49816]
  * [![Device board back.jpg][49817]][49818]

# Schematic
[Schematic download][49819]
# See also
[Sinovoip Banana Pi M2 Berry][49820]  
[Sinovoip Banana Pi M2 Ultra][49821]  
[Device page on Banana Pi Wiki][49822]  
[Official Forum][49823]  

## Manufacturer images
[Manufacturer images on Banana Pi Wiki page][49824]
