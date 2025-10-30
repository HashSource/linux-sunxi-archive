# Inet D70 A23
Inet D70 A23  
---  
[![Inet-d70-0000.jpg][26832]][26833]  
Manufacturer |  [iNet Tek][26834]  
Dimensions |  190 _mm_ x 115 _mm_ x 9.7 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][26835]  
Specifications   
SoC |  [A23][26836] @ 60MHz - 1.536GHz   
DRAM |  512MiB DDR3 @ 552MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 2000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  Multi-Finger Capacitive ([Silead GSL1680][26837])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][26838])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 0.3MP (640x480) rear   
Other |  Accelerometer ([Manufacturer device][26839])   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][26840] and the [New Device Page guide][26841].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
  

## Contents
  * [1 Identification][26842]
  * [2 Sunxi support][26843]
    * [2.1 Current status][26844]
    * [2.2 Images][26845]
    * [2.3 HW-Pack][26846]
    * [2.4 BSP][26847]
    * [2.5 Manual build][26848]
    * [2.6 Mainline U-Boot][26849]
    * [2.7 Mainline kernel][26850]
  * [3 Tips, Tricks, Caveats][26851]
    * [3.1 FEL mode][26852]
    * [3.2 Obtaining script.bin][26853]
  * [4 Adding a serial port (**voids warranty**)][26854]
    * [4.1 Device disassembly][26855]
    * [4.2 Locating the UART][26856]
    * [4.3 UART Cable Routing][26857]
  * [5 Pictures][26858]
  * [6 Also known as][26859]
  * [7 See also][26860]
    * [7.1 Manufacturer images][26861]

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
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][26860]. If no sunxi based images are available, this section can be left blank.
  

## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
  

## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
  

## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][26862]

Everything else is the same as the [manual build howto][26863]. 
  

## Mainline U-Boot
If there is mainline U-Boot support, add this section.
For [ building mainline U-Boot][26864], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
  

## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][26865]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
  

# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
  

## FEL mode
To enter [ FEL mode][26866]: 
  1. Switch off the device.
  2. Hold down the **Vol-** and **Power** buttons.
  3. Release the **Power** button once u-boot reports: _key pressed value=0xb_.
  4. Press the **Power** three times, u-boot should report: _you can unclench the key to update now_.
  5. Release the **Vol-** button.

  
It is possible to [query the device version][26867] at this stage, but [reading results in failure][26868]. 
  

## Obtaining script.bin
  1. Cross-compile, and statically link, the _script_extractor_ utility from [sunxi-tools][26869].
  2. Transfer the _script_extractor_ binary to the device.
  3. Execute _script_extractor_ , redirecting its output to a file named **script.bin**.
  4. Transfer **script.bin** to the host.

  

# Adding a serial port (**voids warranty**)
[![][26870]][26871]
[][26872]
UART leads
## Device disassembly
  1. Remove the two screws surrounding the button panel interface.
  2. Insert a suitable [plastic tool][26873] into the seam of the casing next to one of the screw holes.
  3. Gently slide the tool towards and around the nearest corner.
  4. If the first clip has not been released at this point, twist the tool slowly to pry the casing halves apart.
  5. Place the tool on the opposite end of the released clip and proceed by sliding the tool towards the next clip.
  6. Continue carefully around the perimeter of the casing until all clips have been released.

  

## Locating the UART
The **TX** and **RX** pads are located next to the Touchscreen ZIF connector, and the negative battery terminal provides the **GND** reference. Please review the [UART howto][26874] for further information. 
  

## UART Cable Routing
As an alternative to carefully boring a hole in the rear casing, the Rear Camera may be removed for convenient cable access 
# Pictures
  * [![Inet-d70-0000.jpg][26875]][26833]
  * [![Inet-d70-0001.jpg][26876]][26877]
  * [![INET-D70-REV03 0001.png][26878]][26879]
  * [![INET-D70-REV03 0003.png][26880]][26881]
  * [![Inet-d70-0004.jpg][26882]][26883]
  * [![Inet-d70-0005.jpg][26884]][26885]

# Also known as
[Fondi T725B][26886]
  

# See also
[Inet D70 A33][26887]
  

## Manufacturer images
Optional. Add non-sunxi images in this section.
