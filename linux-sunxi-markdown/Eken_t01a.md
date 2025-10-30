# Eken t01a
Eken t01a  
---  
[![T01a front.jpg][17913]][17914]  
Manufacturer |  [Eken][17915]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  2012   
Website |  [Device Product Page][17916]  
Specifications   
SoC |  [A10][17917] @ 1.008Ghz   
DRAM |  384MiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480px (7" 16:9)   
Touchscreen |  2-finger capacitive ([Manufacturer device][17918])   
Video |  mini HDMI   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][17919])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 miniUSB2.0   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][17920])   
Headers |  UART, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][17921] and the [New Device Page guide][17922].
## Contents
  * [1 Identification][17923]
  * [2 Sunxi support][17924]
    * [2.1 Current status][17925]
    * [2.2 BSP][17926]
    * [2.3 Manual build][17927]
      * [2.3.1 U-Boot][17928]
        * [2.3.1.1 Sunxi/Legacy U-Boot][17929]
        * [2.3.1.2 Mainline U-Boot][17930]
      * [2.3.2 Linux Kernel][17931]
        * [2.3.2.1 Sunxi/Legacy Kernel][17932]
        * [2.3.2.2 Mainline kernel][17933]
  * [3 Tips, Tricks, Caveats][17934]
    * [3.1 FEL mode][17935]
    * [3.2 Device specific topic][17936]
    * [3.3 ...][17937]
  * [4 Adding a serial port (**voids warranty**)][17938]
    * [4.1 Device disassembly][17939]
    * [4.2 Locating the UART][17940]
  * [5 Pictures][17941]
  * [6 Also known as][17942]
  * [7 See also][17943]
    * [7.1 Manufacturer images][17944]

# Identification
Surprinsingly, on the back of the device there's no more than a Made in China label with a few regulatory logos. 
The PCB has the following silkscreened on it: 
[code] 
    T01A_V6
    2012.02.06
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: T01A
  * Build Number: crane_evb-eng 4.0.3 IML74K 20120320 test-keys

# Sunxi support
## Current status
This device is still WIP, some stuff hasn't been tested. In fact, almost everything lives in personal repos. But you're more than welcomed to try them and open issues on broken stuff. 
  

## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][17945] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the **Eken_T01A** build target. 
Development currently is being done in a fork available here: <https://github.com/SaulNunez/u-boot-sunxi-eken-t01a/tree/sunxi>. Technically it should be ready, but I haven't had the time to set a build environment to get something to test. 
#### Mainline U-Boot
WIP Almost ready, DTB for the device has basic support for hardware, NAND doesn't currently work. 
Use the **eken_t01a_defconfig** build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [eken_t01a.fex][17946] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
FEL mode is triggered by the reset button. It's located up, left of the volume rocker. 
In a non powered state, press the reset button and the power on button, this will make the device boot up to FEL mode. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][17947]][17948]
[][17949]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][17950]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
Opening this tablet requires removing two screws on the back. Now the device is only hold together by about ten plastic tabs. Grab the back cover from the right side with the ports, nudge a finger between the usb port and the back cover, try nudge your nails between the sides, the trick is making the back cover to bend to the outside to not put strain on the tabs. 
## Locating the UART
UART is located as tests pads near the A10 SoC.In some models, it is extremely easy to see which test pads need to be soldered to with a soldermask describing what signal they are carrying (see _Connecting RS232 to T01a_ down bellow). 
# Pictures
  * [![T01a front.jpg][17951]][17914]
  * [![T01a volume buttons.jpeg][17952]][17953]
  * [![T01a ports.jpeg][17954]][17955]
  * [![T01a board front.jpeg][17956]][17957]
  * [![Device board back.jpg][17958]][17959]

# Also known as
Supersonic SC-75MID 
# See also
[Connecting RS232 to T01a][17960]
  

## Manufacturer images
Optional. Add non-sunxi images in this section.
