# Inet 10F
Inet 10F  
---  
{{{image}}}  
Manufacturer |  [Inet-Tek][26004]  
Dimensions |  267 _mm_ x 164 _mm_ x 18 _mm_ (570g)   
Release Date |  2012   
Specifications   
SoC |  [A10][26005] @ 1Ghz   
DRAM |  1024MiB DDR3   
NAND |  4GB   
Power |  DC 5V @ 2A, 5500mAh Li-Ion battery   
Features   
LCD |  1024x600 (10" 10:6)   
Touchscreen |  5-finger capacitive ()   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][26006])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2.0MP back   
Other |  Accelerometer ([Manufacturer device][26007] FIXME), reset button   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][26008] and the [New Device Page guide][26009].
## Contents
  * [1 Identification][26010]
    * [1.1 Manual build][26011]
      * [1.1.1 Mainline U-Boot][26012]
      * [1.1.2 Linux Kernel][26013]
        * [1.1.2.1 Mainline kernel][26014]
  * [2 Tips, Tricks, Caveats][26015]
    * [2.1 FEL mode][26016]
  * [3 Adding a serial port (**voids warranty**)][26017]
    * [3.1 Device disassembly][26018]
    * [3.2 Locating the UART][26019]
  * [4 Pictures][26020]
  * [5 Also known as][26021]
  * [6 See also][26022]

# Identification
On the back of the device, the following is printed: 
[code] 
    POINT OF VIEW MOBII icon
    TAB-PROTAB25XXL
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INET-10F-REV03
    Zeng-gc 2012-10-26
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _POV_TAB-PROTAB25XXL_
  * Build Number: _10F2-P1-H1-H01-2911.2012208_

## Manual build
You can build things for yourself by following our [ Manual build howto][26023] and by choosing from the configurations available below. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. --> TODO but inet1 uboot works for now 
### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][26024]. 
# Adding a serial port (**voids warranty**)
see inet1, they contact pads are not marked rx/tx but are there (3 contact pads ) 
## Device disassembly
By removing the two screws on the connector side, the device is trivially opened. 
## Locating the UART
There are some UART pads next to the wire going to the wifi antenna, all you need to do is solder on some wires according to our [UART howto][26025]. 
# Pictures
Take some pictures of your device, [ upload them][26026], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
