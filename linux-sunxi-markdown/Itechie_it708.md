# Itechie it708
Itechie it708  
---  
[![IMG 2833.png][28509]][28510]  
Manufacturer |  [iTechie]   
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  2011   
Website |  [Device Product Page][28511]  
Specifications   
SoC |  [A13][28512] @ 1.2Ghz   
DRAM |  512MiB DDR3 @ 666MHz   
NAND |  8GB   
Power |  DC 5V @ 2A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (7" 800:480)   
Touchscreen |  capacitive/resistive ([Manufacturer device][28513])   
Video |  HDMI (Type C - micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][28514])   
Storage |  µSD   
USB |  USB2.0 OTG   
Camera |  5.0MP front, 1.2MP rear   
Other |  Accelerometer , GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA,   
  

## Contents
  * [1 Identification][28515]
  * [2 Sunxi support][28516]
    * [2.1 Current status][28517]
    * [2.2 Images][28518]
    * [2.3 HW-Pack][28519]
    * [2.4 BSP][28520]
    * [2.5 Manual build][28521]
      * [2.5.1 U-Boot][28522]
        * [2.5.1.1 Sunxi/Legacy U-Boot][28523]
        * [2.5.1.2 Mainline U-Boot][28524]
      * [2.5.2 Linux Kernel][28525]
        * [2.5.2.1 Sunxi/Legacy Kernel][28526]
        * [2.5.2.2 Mainline kernel][28527]
  * [3 Tips, Tricks, Caveats][28528]
    * [3.1 FEL mode][28529]
    * [3.2 Getting the script.bin][28530]
  * [4 Adding a serial port (**voids warranty**)][28531]
    * [4.1 Device disassembly][28532]
    * [4.2 Locating the UART][28533]
  * [5 Pictures][28534]
  * [6 Schematic][28535]
  * [7 Also known as][28536]
  * [8 See also][28537]
    * [8.1 Manufacturer images][28538]

# Identification
Model number IT-708 Android version 4.0.4 Baseband version M1190_V1.0.9_P10 Kernel version 3.0.8+ Sun Apr 7 10:06:42 CST 2013 Build number IT-708_dblgc0329_ep_2g_V1.1.10_20130407_m721_1a4f49b 
Motherboard 
F761I-MAINBOARD-V3.0.0 TOPWISE-013 2013/03/01 
  
On the back of the device, the following is printed: 
[code] 
    iTechie
    IT-708
[/code]
The PCB has the following silkscreened on it: 
[code] 
    F761I-MAINBOARD-V3.0.0
    TOPWISE-013 2013/03/01
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _IT-708_
  * Build Number: _IT-708_dblgc0329_ep_2g_V1.1.10_20130407_m721_1a4f49b_

# Sunxi support
## Current status
All Hardware working, in android system, but no luck so far with U-Boot I manage barely to load some bare metal assembly codes to turn on the lcd backlight and blink the charging led using bit banging i2c to the Power controller AXP209 but nothing else. 
## Images
## HW-Pack
## BSP
## Manual build
You can build things for yourself by following our [ Manual build howto][28539] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [[1]][28540] file. 
#### Mainline kernel
Use the _Allwinner A13_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The Vol_Up + Power button triggers [ FEL mode][28541]. here is how: connect the usb to the pc make sure your android is totally shut down (vol_down + power for 10 to 15 sec) hold Vol_Up + Power Button for 2 to 3 sec while still holding Vol_Up release power button then tap power button 3 to 4 times until you see the ask for permission to connect on your computer 
## Getting the script.bin
the script.bin is not easy to obtain using FEL mode but you can access it thru ADB by getting nanda image and unpack it using this command: adb pull /dev/block/nanda ./nanda.img 
# Adding a serial port (**voids warranty**)
[![][28542]][28543]
[][28544]
UART pads
## Device disassembly
no screws for this device just use the plastic sharp wedge from the side to open the back cover. take care of the speaker which may be attached to the back cover, so do not pull hard and try to get the speaker from the cover slowly. 
## Locating the UART
I do not use UART and not recommended using it anyway but if necessary you can use the SD-Card Pins thru a converter. this is the safest way and avoiding soldering on the board. 
# Pictures
  * [![IMG 2833.png][28545]][28510]
  * [![IMG 2834.png][28546]][28547]
  * [![IMG 2792.png][28548]][28549]
  * [![IMG 2807.png][28550]][28551]

# Schematic
# Also known as
# See also
## Manufacturer images
