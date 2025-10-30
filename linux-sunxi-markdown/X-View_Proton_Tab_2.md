# X-View Proton Tab 2
X-View Proton Tab 2  
---  
[![X-View Proton Tab 2 Front.jpg][59478]][59479]  
Manufacturer |  [X-View][59480]  
Dimensions |  13 _mm_ x 80 _mm_ x 123 _mm_  
Release Date |  September, 2013  
Website |  [Proton Tab 2][59481]  
Specifications   
SoC |  [A13][59482] @ 1.1Ghz   
DRAM |  512MiB DDR3 @ MHz   
NAND |  4/8GB   
Power |  DC 5V @ 1A, 1400mAh 3.7V Li-Ion battery   
Features   
LCD |  480x272 (4.3" 16:9)   
Touchscreen |  5-finger capacitive ([Sitronix ST1530-N40][59483])   
Video |  none   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][59484])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][59485]),   
Headers |  UART, LCD   
This page needs to be properly filled according to the [New Device Howto][59486] and the [New Device Page guide][59487].
## Contents
  * [1 Identification][59488]
  * [2 Sunxi support][59489]
    * [2.1 Current status][59490]
    * [2.2 Images][59491]
    * [2.3 HW-Pack][59492]
    * [2.4 BSP][59493]
    * [2.5 Manual build][59494]
      * [2.5.1 U-Boot][59495]
        * [2.5.1.1 Sunxi/Legacy U-Boot][59496]
        * [2.5.1.2 Mainline U-Boot][59497]
      * [2.5.2 Linux Kernel][59498]
        * [2.5.2.1 Sunxi/Legacy Kernel][59499]
        * [2.5.2.2 Mainline kernel][59500]
    * [2.6 FEL mode][59501]
  * [3 Adding a serial port (**voids warranty**)][59502]
    * [3.1 Device disassembly][59503]
    * [3.2 Locating the UART][59504]
  * [4 Pictures][59505]

# Identification
On the back of the device, the following is printed: 
[code] 
    X-View
[/code]
The PCB has the following silkscreened on the front side: 
[code] 
    M434 V4.1.0
    KF006-MAINBOARD-V4.1.0
    2012/08/11
[/code]
On the back side: 
[code] 
    3213
    F-M E351308
    94V-0
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _Tablet 434_
  * Build Number: _PROTON TAB 2 20130903_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][59506]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][59507] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][59508] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
## FEL mode
The Home or Volume + buttons trigger [ FEL mode][59509]. 
# Adding a serial port (**voids warranty**)
[![][59510]][59511]
[][59512]
X-View Proton Tab 2 UART pads
Luckily this device has easy and exposed pads to solder three wires for a UART interface. Refer to [UART howto][59513] for more information. 
## Device disassembly
The back cover is the first part to come out. Refer to [Plastic tool howto][59514] for more information on how to open the device. 
## Locating the UART
The three pads are located right above the nand flash. Removing the battery or softening the adhesive is recommended to avoid touching it with the soldering iron. For more information refer to [UART howto][59513]. 
# Pictures
  * [![X-View Proton Tab 2 Front.jpg][59515]][59479]
  * [![X-View Proton Tab 2 Back.jpg][59516]][59517]
  * [![X-View Proton Tab 2 Side-Buttons.jpg][59518]][59519]
  * [![X-View Proton Tab 2 Bottom-Buttons.jpg][59520]][59521]
  * [![X-View Proton Tab 2 dissasembled.jpg][59522]][59523]
  * [![X-View Proton Tab 2 PCB-back.jpg][59524]][59525]
