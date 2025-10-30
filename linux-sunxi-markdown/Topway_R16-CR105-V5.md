# Topway R16-CR105-V5
Topway R16-CR105-V5  
---  
[![Topway.jpg][55277]][55278]  
Manufacturer |  [Topway][55279]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][55280]  
Specifications   
SoC |  [R16][55281] @ 1.6Ghz   
DRAM |  1GiB DDR3   
NAND |  16GB   
Power |  DC 12V   
Features   
LCD |  WidthxHeight (10" X:Y)   
Touchscreen |  10-finger capacitive/resistive ([Manufacturer device][55282])   
Video |  Built in lcd   
Audio |  3.5mm microphone plug, internal microphone, dac connected to TDA7560 to drive 4 carspeakers.   
Network |  WiFi 802.11 b/g/n [RTL8188FTV][55283]  
Storage |  EMMC, USB   
USB |  2x USB2.0 Host, 1x USB2.0 OTG   
Camera |  video-in for dash-cam/rear-camera (parking)   
Other |  GPS, dvd-decoder (SUNPLUS 8202TQ), Bluetooth [IVT BlueSoleil i140][55284]  
Headers |  UART, JTAG, LCD, VGA, ...   
This page is still a work in progress.
This device is known under several brands and device specific model numbers. However, they all share the same cpu module (with emmc, ram and AXP223 controller, usb-hub). Therefor I used manufacturer of the module and it's specific model number. 
## Contents
  * [1 Identification][55285]
  * [2 Sunxi support][55286]
    * [2.1 Current status][55287]
    * [2.2 Images][55288]
    * [2.3 HW-Pack][55289]
    * [2.4 BSP][55290]
    * [2.5 Manual build][55291]
      * [2.5.1 U-Boot][55292]
        * [2.5.1.1 Sunxi/Legacy U-Boot][55293]
        * [2.5.1.2 Mainline U-Boot][55294]
      * [2.5.2 Linux Kernel][55295]
        * [2.5.2.1 Sunxi/Legacy Kernel][55296]
        * [2.5.2.2 Mainline kernel][55297]
  * [3 Tips, Tricks, Caveats][55298]
    * [3.1 FEL mode][55299]
    * [3.2 Device specific topic][55300]
    * [3.3 ...][55301]
  * [4 Adding a serial port (**voids warranty**)][55302]
    * [4.1 Device disassembly][55303]
    * [4.2 Locating the UART][55304]
  * [5 Pictures][55305]
  * [6 Also known as][55306]
  * [7 See also][55307]
    * [7.1 Manufacturer images][55308]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Manufacturer Marketing Name
    ModelNumber
[/code]
The PCB has the following silkscreened on it: 
[code] 
    kr-6228-mb-v01
    2016-06-22
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model: QuadCore-R16 (astar_d7)
  * Manufacturer: Allwinner
  * Baseband Version: Not Available
  * RIL Version: sw-dataonly-ril-for-6.0_v1.0
  * Build Number: astar_d7-eng 6.0.1 MOB30R 20161112 test-keys
  * Build Fingerprint: Allwinner/astar_d7/astar-d7:6.0.1/MOB30R/20161112:eng/test-keys
  * Bootloader: unknown
  * Java VM: ART 2.1.0
  * OS Version: Marshmallow (6.0.1)
  * SDK: 23

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][55307]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][55309] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][55310] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][55311]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][55312]][55313]
[][55314]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][55315]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][55316].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][55315].
# Pictures
[All pictures][55317]
# Also known as
[Redpower 21213B][55318] [eonon GA2162][55319] There are also units from other brands (The hw_id is in front of the brand): 
  * 1 - Create
  * 3 - Anstar
  * 7 - Waybo
  * 17 - RedPower, Kaier
  * 22 - Infidini
  * 35 - Penhui
  * 36 - Topway
  * 152 - SMARTECH

# See also
[4PDA][55320] [XDAdevelopers][55321] [XDAdevelopers][55322]
## Manufacturer images
Optional. Add non-sunxi images in this section.
