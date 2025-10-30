# MyAudio 708f
MyAudio 708f  
---  
[![My708f front.JPG][38593]][38594]  
Manufacturer |  [MyAudio][38595]  
Dimensions |  194 _mm_ x 120 _mm_ x 10 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][38596]  
Specifications   
SoC |  [A31s][38597] @ 1Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  USB, ?? mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" 16:9)   
Touchscreen |  X-finger capacitive ([Focaltech FT5202][38598])   
Video |  none   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][38599])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front   
Other |  Accelerometer ([Freescale MMA7660][38600])   
This page needs to be properly filled according to the [New Device Howto][38601] and the [New Device Page guide][38602].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][38603]
  * [2 Sunxi support][38604]
    * [2.1 Current status][38605]
    * [2.2 Images][38606]
    * [2.3 HW-Pack][38607]
    * [2.4 BSP][38608]
    * [2.5 Manual build][38609]
      * [2.5.1 U-Boot][38610]
        * [2.5.1.1 Sunxi/Legacy U-Boot][38611]
        * [2.5.1.2 Mainline U-Boot][38612]
      * [2.5.2 Linux Kernel][38613]
        * [2.5.2.1 Sunxi/Legacy Kernel][38614]
        * [2.5.2.2 Mainline kernel][38615]
  * [3 Tips, Tricks, Caveats][38616]
    * [3.1 FEL mode][38617]
    * [3.2 Device specific topic][38618]
    * [3.3 ...][38619]
  * [4 Adding a serial port (**voids warranty**)][38620]
    * [4.1 Device disassembly][38621]
    * [4.2 Locating the UART][38622]
  * [5 Pictures][38623]
  * [6 Also known as][38624]
  * [7 See also][38625]
    * [7.1 Manufacturer images][38626]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    MyAudio
    Tablet Series 7
    708F
    
    8 GB
    Designed by MyAudio
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INGENIC-CROSS
    N7S-V1.0 2013-07-11
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

^^ Stock ROM stopped working, and I cannot find the original ROM anywhere (manufacturer site disappeared, and I have no local backup of it) 
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][38625]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][38627] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][38628] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The U-BOOT (not soldered by default) button triggers [ FEL mode][38629]. It can also be accessed by holding [ Volume up][38630] button (follow the linked instructions). 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][38631]][38632]
[][38633]
UART pads at the back of PCB
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][38634]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][38635].
## Locating the UART
UART pin pair can be found at the left side of the SoC (A31s), on the opposite side of the board. The pin further away from the SoC is RX, the other is TX. Check [UART howto][38634] for a tutorial on using them. 
# Pictures
  * [![My708f front.JPG][38636]][38594]
  * [![My708f back.JPG][38637]][38638]
  * [![My708f buttons.JPG][38639]][38640]
  * [![My708f board front.JPG][38641]][38642]
  * [![My708f board back.JPG][38643]][38644]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
