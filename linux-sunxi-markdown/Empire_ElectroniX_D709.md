# Empire ElectroniX D709
Empire ElectroniX D709  
---  
[![Empire electronix d709 front.jpg][17994]][17995]  
Manufacturer |  [Empire ElectroniX][17996]  
Dimensions |  8.6 _mm_ x 121 _mm_ x 193 _mm_  
Release Date |  February 2013  
Website |  N/A   
Specifications   
SoC |  [A13][17997] @ 1GHz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" X:Y)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][17998])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek 8188EUS][17999])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][18000])   
  

## Contents
  * [1 Identification][18001]
  * [2 Sunxi support][18002]
    * [2.1 Current status][18003]
    * [2.2 Manual build][18004]
      * [2.2.1 U-Boot][18005]
        * [2.2.1.1 Sunxi/Legacy U-Boot][18006]
        * [2.2.1.2 Mainline U-Boot][18007]
      * [2.2.2 Linux Kernel][18008]
        * [2.2.2.1 Sunxi/Legacy Kernel][18009]
        * [2.2.2.2 Mainline kernel][18010]
  * [3 Tips, Tricks, Caveats][18011]
    * [3.1 FEL mode][18012]
    * [3.2 Device specific topic][18013]
    * [3.3 ...][18014]
  * [4 Adding a serial port (**voids warranty**)][18015]
    * [4.1 Device disassembly][18016]
    * [4.2 Locating the UART][18017]
  * [5 Pictures][18018]
  * [6 Also known as][18019]
  * [7 See also][18020]
    * [7.1 Manufacturer images][18021]

# Identification
On the back of the device, the following is printed: 
[code] 
    Empire
    ElectroniX
    EMP2012110104720
[/code]
The PCB has the following silkscreened on it: 
On its back: 
[code] 
    MID_7#PCB_VRE1.2
    2012/08/20
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
U-Boot support [was added in 2015][18022]
A fex file [was written as well][18023]. 
  

## Manual build
You can build things for yourself by following our [ Manual build howto][18024] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][18025] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The Volume- button triggers [ FEL mode][18026]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][18027]][18028]
[][18029]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][18030]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][18031].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][18030].
# Pictures
Take some pictures of your device, [ upload them][18032], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Empire electronix d709 front.jpg][18033]][17995]
  * [![Device back.jpg][18034]][18035]
  * [![Device buttons 1.jpg][18036]][18037]
  * [![Device buttons 2.jpg][18038]][18039]
  * [![Empire electronix d709 pcb.jpg][18040]][18041]
  * [![Empire electronix d709 pcb back.jpg][18042]][18043]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
