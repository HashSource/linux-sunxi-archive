# Inet D70 A23
(Redirected from [Inet d70][27262])
 
Inet D70 A23  
---  
[![Inet-d70-0000.jpg][27265]][27266]  
Manufacturer |  [iNet Tek][27267]  
Dimensions |  190 _mm_ x 115 _mm_ x 9.7 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][27268]  
Specifications   
SoC |  [A23][27269] @ 60MHz - 1.536GHz   
DRAM |  512MiB DDR3 @ 552MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 2000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  Multi-Finger Capacitive ([Silead GSL1680][27270])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][27271])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 0.3MP (640x480) rear   
Other |  Accelerometer ([Manufacturer device][27272])   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][27273] and the [New Device Page guide][27274].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
  

## Contents
  * [1 Identification][27275]
  * [2 Sunxi support][27276]
    * [2.1 Current status][27277]
    * [2.2 Images][27278]
    * [2.3 HW-Pack][27279]
    * [2.4 BSP][27280]
    * [2.5 Manual build][27281]
    * [2.6 Mainline U-Boot][27282]
    * [2.7 Mainline kernel][27283]
  * [3 Tips, Tricks, Caveats][27284]
    * [3.1 FEL mode][27285]
    * [3.2 Obtaining script.bin][27286]
  * [4 Adding a serial port (**voids warranty**)][27287]
    * [4.1 Device disassembly][27288]
    * [4.2 Locating the UART][27289]
    * [4.3 UART Cable Routing][27290]
  * [5 Pictures][27291]
  * [6 Also known as][27292]
  * [7 See also][27293]
    * [7.1 Manufacturer images][27294]

# Identification
Case: 
[code] 
    Fondi
[/code]
  
PCB: 
[code] 
    INET-D70-REV03
    Zeng-gc 2014-07-01
[/code]
  
Android -> Settings -> About Tablet: 
[code] 
    Model Number: T725B
    Build Number: A23_D70_D708C_1410038.20141021
[/code]
  

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either U-Boot or kernel, mention this too, but add the extra sections below.
  

## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][27293]. If no sunxi based images are available, this section can be left blank.
  

## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
  

## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
  

## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][27295]

Everything else is the same as the [manual build howto][27296]. 
  

## Mainline U-Boot
If there is mainline U-Boot support, add this section.
For [ building mainline U-Boot][27297], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
  

## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][27298]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
  

# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
  

## FEL mode
To enter [ FEL mode][27299]: 
  1. Switch off the device.
  2. Hold down the **Vol-** and **Power** buttons.
  3. Release the **Power** button once u-boot reports: _key pressed value=0xb_.
  4. Press the **Power** three times, u-boot should report: _you can unclench the key to update now_.
  5. Release the **Vol-** button.

  
It is possible to [query the device version][27300] at this stage, but [reading results in failure][27301]. 
  

## Obtaining script.bin
  1. Cross-compile, and statically link, the _script_extractor_ utility from [sunxi-tools][27302].
  2. Transfer the _script_extractor_ binary to the device.
  3. Execute _script_extractor_ , redirecting its output to a file named **script.bin**.
  4. Transfer **script.bin** to the host.

  

# Adding a serial port (**voids warranty**)
[![][27303]][27304]
[][27305]
UART leads
## Device disassembly
  1. Remove the two screws surrounding the button panel interface.
  2. Insert a suitable [plastic tool][27306] into the seam of the casing next to one of the screw holes.
  3. Gently slide the tool towards and around the nearest corner.
  4. If the first clip has not been released at this point, twist the tool slowly to pry the casing halves apart.
  5. Place the tool on the opposite end of the released clip and proceed by sliding the tool towards the next clip.
  6. Continue carefully around the perimeter of the casing until all clips have been released.

  

## Locating the UART
The **TX** and **RX** pads are located next to the Touchscreen ZIF connector, and the negative battery terminal provides the **GND** reference. Please review the [UART howto][27307] for further information. 
  

## UART Cable Routing
As an alternative to carefully boring a hole in the rear casing, the Rear Camera may be removed for convenient cable access 
# Pictures
  * [![Inet-d70-0000.jpg][27308]][27266]
  * [![Inet-d70-0001.jpg][27309]][27310]
  * [![INET-D70-REV03 0001.png][27311]][27312]
  * [![INET-D70-REV03 0003.png][27313]][27314]
  * [![Inet-d70-0004.jpg][27315]][27316]
  * [![Inet-d70-0005.jpg][27317]][27318]

# Also known as
[Fondi T725B][27319]
  

# See also
[Inet D70 A33][27320]
  

## Manufacturer images
Optional. Add non-sunxi images in this section.
