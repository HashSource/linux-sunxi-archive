# Eachlink H6 Mini
Eachlink H6 Mini  
---  
[![Eachlink h6 mini front.jpg][17664]][17665]  
Manufacturer |  Eachlink (?)   
Dimensions |  96 _mm_ x 96 _mm_ x 20 _mm_  
Release Date |  September 2018   
Website |  (none?)   
Specifications   
SoC |  [H6][17666] @ 1.3 Ghz   
DRAM |  3GiB DDR3 @ 840(?) MHz   
NAND |  32GB eMMC   
Power |  DC 5V @ 2A, microUSB   
Features   
Video |  HDMI (Type A full)   
Audio |  3.5mm AV plug, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek 8723BS][17667]), 10/100Mbps Ethernet ([embedded AC200][17668])   
Storage |  µSD, eMMC   
USB |  1 X USB2.0 Host, 1 X USB3.0 Host   
Other |  IRDA receiver, 7-segment display   
Headers |  UART pads   
This page needs to be properly filled according to the [New Device Howto][17669] and the [New Device Page guide][17670].
Inexpensive TV box with the H6 SoC and some decent specifications (3GiB RAM, 32GiB eMMC), but missing GBit Ethernet. 
## Contents
  * [1 Identification][17671]
  * [2 Sunxi support][17672]
    * [2.1 Current status][17673]
    * [2.2 Images][17674]
    * [2.3 Manual build][17675]
      * [2.3.1 U-Boot][17676]
        * [2.3.1.1 Mainline U-Boot][17677]
      * [2.3.2 Linux Kernel][17678]
        * [2.3.2.1 Mainline kernel][17679]
  * [3 Tips, Tricks, Caveats][17680]
    * [3.1 FEL mode][17681]
  * [4 Adding a serial port (**might void warranty?**)][17682]
    * [4.1 Device disassembly][17683]
    * [4.2 Locating the UART][17684]
  * [5 Pictures][17685]
  * [6 See also][17686]
    * [6.1 Manufacturer images][17687]

# Identification
On the back of the device, the following is printed: 
[code] 
    H6 MINI PLAYER
    HOME MEDIA CENTER
    DESIGNED BY HONG KONG
    INPUT: DC 5V / 2A
    MADE IN CHINA
[/code]
The PCB has the following silkscreened on it: 
[code] 
    H6-mini_H6_V1.1 2018-09-11
[/code]
in a later version 
[code] 
    H6-mini_H6_V1.2 2018-09-15
[/code]
# Sunxi support
## Current status
WIP. Boots mainline Linux headless (with serial console soldered as shown below), with SD card, eMMC and USB 2.0 working. 
## Images
## Manual build
You can build things for yourself by following our [ Manual build howto][17688] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Support is work in progress. [Patches][17689] have been posted to the mailing list, a repository with those patches is [available][17690]. 
### Linux Kernel
#### Mainline kernel
Any recent kernel with H6 support should work. No mainline .dts yet, use the .dtb as provided by U-Boot, by using **$fdtcontroladdr** when specifying the DTB address. 
# Tips, Tricks, Caveats
Despite being a TV box shipped with Android and the Play Store plus other sensitive apps, the box is completely open. It boots normal eGON images (as created by U-Boot) or boots happily into FEL mode with the FEL button pressed. When booting the shipped Android system, you are greeting with a prompt on the serial line. If you have the RX line fix in place, you can explore the system. A dauntless "su" will give you root privileges for full system access. 
  * The box does not seem to come with the usual AXP 805 PMIC (typically bundled with the H6). There is an IC which looks like a PMIC, judging by the coils and the many SMD components around it. However it is much smaller than the AXP and has a rather cryptic label "A8038 8099330k". The BSP log features "probe axp is dummy" and "no pmu exist".
  * The LED 7-segment display is controlled by an I2C controlled chip called FD655 from the Chinese company FDHISI (TODO: find I2C bus number, I2C address and required power lines for the display. Google turns up a Chinese datasheet, also there is some driver code on Github).
  * There are eight(!) DRAM chips, four from Samsung (K4B2G0446D) and four from Micron (D9PQL). On the v1.2 board, there are four K4B2G0446Q and four K4B2G0446C all from Samsung. It needs to be worked out whether this is to give the rather odd 3GiB or there are actually 4GiB, with the last GiB not usable.

To get a root-shell in the shipped Android system without hardware modification (uart and a serial line) via tcp instead, you can install temporarily and start **com.jaja.remoteadb**. Connect from a external PC with an installed adb 
[code] 
    $ adb connect <ip of your box>
    $ adb shell
    petrel-p1:/ #
    
[/code]
To start adb permanently listening (after reboot) to network port 5555 you set 
[code] 
    petrel-p1:/ # setprop persist.adb.tcp.port 5555
    
[/code]
You can remove com.jaja.remoteadb, after adb is permanently listening to port 5555 
[code] 
    petrel-p1:/ # pm uninstall com.jaja.remoteadb
    
[/code]
## FEL mode
There is a small hole between the two USB ports, the button behind it triggers FEL mode when held down while resetting or powering up. On the PCB there is written "UBOOT" near this button. The USB 2.0 port will act as the OTG device, you need a USB-A <-> USB-A cable for FEL mode (same as the Pine64). 
[code] 
    $ ./sunxi-fel version
    AWUSBFEX soc=00001728(H6) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
    
[/code]
If you copy the original spl from internal eMMC to an empty sd-mmc between 0x2000 and 0xa000 the box with this sd-mmc inserted will fall into FEL mode automatically: 
[code] 
    petrel-p1:/ # dd if=/dev/block/mmcblk0 of=/dev/block/mmcblk1 bs=8k seek=1 skip=1 count=4
    petrel-p1:/ # reboot
    
[/code]
You will find the original spl in the [ota-update zip][17691] as file named **boot0_sdcard.fex** with size 32768. 
# Adding a serial port (**might void warranty?**)
[![][17692]][17693]
[][17694]
H6 Mini UART pads, next to the SPDIF connector. The SOT23 footprint is marked with the (missing) FET pin names, bridge "S" and "D" to enable the RX line.
There are clearly labelled UART pads on the PCB, please refer to the [UART howto][17695] for more details on using a serial port. There is some space near the microUSB power supply socket to drill a small hole and lead the three needed cables through. 
The RX pin doesn't work out of the box, as there is a FET missing on the PCB. Normally this FET gates the RX line when the device is off, preventing it from leaking power into the system and allowing a proper shutdown and reboot. However this FET is not populated, so the RX line is not working initially: You can't type anything, but see all messages. To fix this either bridge the pins labelled "S" and "D" in the picture to the right, or solder a proper FET to the SOT23 footprint. 
[![][17696]][17697]
[][17698]
H6 Mini UART pads, next to the SPDIF connector. The resistor footprint is marked with "A" and "B", put a 10kΩ between "A" and "B" to enable the TX line.
On the v1.2 the TX pin doesn't work out of the box, too, as there is a resistor missing on the PCB. You can put a 10kΩ resistor in between the pins labeled "A" and "B". 
## Device disassembly
To open the box, turn it upside down, gently slide a [plastic tool][17699] or a knife in the small gap around all edges of the box to eventually lift the bottom plate. There is no need to remove the rubber feet. Then unscrew the four screws securing the PCB. To remove the PCB, first lift the side with the 7 segment display up (use a knife or similar tool), then gently pull the PCB out. This is needed because the backside connectors are somewhat locked into the case. 
## Locating the UART
The UART pins are located in the upper left corner on the top of the PCB, near the SPDIF connector. They are the usual 3.3V GND/TX/RX/VCC pin, clearly labelled as such. As usual, the VCC should not be needed. 
# Pictures
  * [![Eachlink h6 mini front.jpg][17700]][17665]
  * [![H6 Mini size comparison.jpg][17701]][17702]
  * [![H6 Mini back.jpg][17703]][17704]
  * [![H6 Mini side.jpg][17705]][17706]
  * [![H6 Mini bottom.jpg][17707]][17708]
  * [![H6 Mini PCB bottom.jpg][17709]][17710]
  * [![H6 Mini PCB top.jpg][17711]][17712]
  * [![H6 Mini UART.jpg][17713]][17693]
  * [![H6 Mini display.jpg][17714]][17715]
  * [![H6 Mini unknown PMIC.jpg][17716]][17717]
  * [![H6-mini H6 V1.2.jpeg][17718]][17719]

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
