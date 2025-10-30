# X96 Mate
X96 Mate  
---  
[![X96 mate.jpg][59811]][59812]  
Manufacturer |  Shenzhen Hechuang Intelligent Co.   
Dimensions |  105 _mm_ x 105 _mm_ x 19 _mm_  
Release Date |  end of 2020   
Website |  unknown/none   
Specifications   
SoC |  [H616][59813] @ 1.5 Ghz (BSP)   
DRAM |  4GiB DDR3L @ 648MHz (BSP), 8 * Micron MT41K1G4   
eMMC |  32/64 GB (Samsung KLMCG4JENB-B041)   
Power |  DC 5V @ 2A, 5.5/2.1 mm barrel plug   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm AV plug, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([AW859A][59814]), 10/100Mbps Ethernet (integrated H616 PHY)   
Storage |  µSD, eMMC   
USB |  2 USB2.0 Host   
Other |  Front LED display, IRDA   
Headers |  UART pads on PCB   
A typical China-made TV box, offered on eBay and various Chinese outlets. Comes with 4GB of DRAM and is comparably cheap for that. 
## Contents
  * [1 Identification][59815]
  * [2 Sunxi support][59816]
    * [2.1 Current status][59817]
    * [2.2 Manual build][59818]
      * [2.2.1 Mainline U-Boot][59819]
      * [2.2.2 Mainline Linux Kernel][59820]
  * [3 Tips, Tricks, Caveats][59821]
    * [3.1 FEL mode][59822]
  * [4 Adding a serial port (**voids warranty**)][59823]
    * [4.1 Device disassembly][59824]
    * [4.2 Locating the UART][59825]
  * [5 Pictures][59826]
  * [6 Also known as][59827]
    * [6.1 Manufacturer images][59828]

# Identification
The top has an "X96" logo embossed in the centre, in the lower right corner it reads "Mate". 
On the back of the device, the following is printed: 
[code] 
    OTT TV BOX
    ANDROID PLAYER
    Model: X96 Mate RAM: 4G
                    ROM: 64G
[/code]
The PCB has the following silkscreened on it: 
[code] 
    BA306_141 V1.0 20272
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _X96MATE_PLUS_
  * Build Number: _X96MATE_PLUS_20200818-2117_

# Sunxi support
## Current status
Basic support merged in the respective mainline repositories, USB and Ethernet are still WIP. Since it uses the AC200 integrated 100MBit Ethernet PHY, it relies on pending mainline support for that IP to have working Ethernet. 
## Manual build
You can build things for yourself by following our [ Manual build howto][59829] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _x96_mate_defconfig_ build target. Available since v2023.01-rc1. 
### Mainline Linux Kernel
Use the **sun50i-h616-x96-mate.dtb** devicetree binary from a mainline kernel, available since v6.0. 
# Tips, Tricks, Caveats
The PCB is mounted upside down in the case, so the connectors are all flipped over (USB, SD card, HDMI, Ethernet). 
## FEL mode
There is a button on the PCB (behind the AV socket), it can be reached by a non-conductive tool like a toothpick through the AV socket. This is *not* a hardware FEL button, but instead just connected to GPIO PH9. The vendor firmware implements FEL button behaviour, by sampling this GPIO at boot time, then branching to the BootROM FEL routine. There are patches for mainline U-Boot to achieve the same: when pushing this button during boot, the board will enter FEL mode. 
Alternatively, enter FEL mode with the fel-sdboot.sunxi image written to an SD card. 
The rear, white USB socket is connected to USB controller 0, a non-standard USB A-to-A cable can be used to connect using FEL. 
# Adding a serial port (**voids warranty**)
[![][59830]][59831]
[][59832]
X96 Mate UART pads
To get access to the UART pads, you have to open the box. There is a seal sticker on the device, which you have to break to get inside it. 
## Device disassembly
Flip the box over and remove the two lower rubber feet on the bottom (the ones closest to the front). Remove the two screws that are hiding beneath. Now use a [plastic tool][59833] to slide between the whole rim of the device and pry open the hooks that hold the bottom plate to the upper shell. The bottom plate can then be easily removed to open the box, the PCB is mounted to the upper plastic shell. Two more screws hold the PCB down there, and need to be removed to get access to the lower side of the PCB, to solder the UART wires. 
## Locating the UART
The UART pads are located on the top right of the device PCB, between the USB and the IR connector, providing 3.3V RX, TX and GND signals, as pictured. The assignment is printed on the bottom side of the PCB. To solder some wires or pins, just remove the PCB (two screws). To route the wires outside the case, you could drill a small hole between the AV and IR connector. Once done, follow the [UART howto][59834]. 
# Pictures
  * [![X96 mate.jpg][59835]][59812]
  * [![X96 mate rear.jpg][59836]][59837]
  * [![X96 mate bottom.jpg][59838]][59839]
  * [![X96 mate pcb top.jpg][59840]][59841]
  * [![X96 mate pcb bottom.jpg][59842]][59843]
  * [![X96 mate bottom plate.jpg][59844]][59845]

# Also known as
There is an "X96 Mini" TV box, sometimes sailing alongside the Mate 4G/32G and 4G/64G versions. It seems to have 2G RAM and 16G eMMC, but has an Amlogic S905W SoC, so it's not compatible and not an Allwinner chip. 
## Manufacturer images
[Some firmware image of unknown origin.][59846]
