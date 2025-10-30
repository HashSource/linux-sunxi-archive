# X96QPro+
X96QPro+  
---  
[![X96qpro+ front.jpg][59645]][59646]  
Manufacturer |  [Manufacturer][59647]  
Dimensions |  140 _mm_ x 90 _mm_ x 20 _mm_  
Release Date |  August 2024   
Website |  [Device Product Page][59648]  
Specifications   
SoC |  [H728][59649] @ 1.8Ghz   
DRAM |  2GiB/4GiB DDR3L @ 792MHz (8*Micron MT41K1G4RH-107:E)   
NAND |  16/32/64 GB eMMC   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug, HDMI, SPDIF   
Network |  WiFi 6 ([AICSemi AIC8800][59650]), 10/100/1000Mbps Ethernet ([Maxio MAE0621][59651])   
Storage |  µSD, eMMC   
USB |  2 USB2.0 Host, 1 USB3.0 Host   
Other |  infrared sensor, 4-digit 7-segment display   
Headers |  2 * serial (unsoldered)   
This page needs to be properly filled according to the [New Device Howto][59652] and the [New Device Page guide][59653].
TV set top box with one USB3.0 plus two USB 2.0 sockets and Gigabit Ethernet, powered by the H728 SoC (8*Cortex-A55). Make sure to get all letters, there are many TV boxes using the X96 prefix. In particular the [X96Q][59654] and [X96QPro][59655] are quite different devices using a different [SoC][59656]. 
## Contents
  * [1 Identification][59657]
  * [2 Sunxi support][59658]
    * [2.1 Current status][59659]
    * [2.2 Manual build][59660]
      * [2.2.1 Mainline U-Boot][59661]
      * [2.2.2 Mainline Linux Kernel][59662]
  * [3 Tips, Tricks, Caveats][59663]
    * [3.1 FEL mode][59664]
    * [3.2 on board buttons/headers][59665]
  * [4 Adding a serial port (**voids warranty**)][59666]
    * [4.1 Device disassembly][59667]
    * [4.2 Locating the UART][59668]
  * [5 Pictures][59669]
  * [6 See also][59670]
    * [6.1 Manufacturer images][59671]

# Identification
Has the X96Q logo embossed on the top, followed by the "Pro+" name. 
On the back of the device, the following is printed: 
[code] 
         X96Q PRO+
    RAM: 4G   DC:5V == 2.0A
    ROM: 64G  VID:56 01 8 25
[/code]
The PCB has a sticker on it: 
[code] 
    BA947 V1.2 AIC8800D40
    4+64    BSK241019002
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Supported for basic headless use in mainline Linux and U-Boot, development closely follows the A523/T527 upstreaming progress. USB3.0 and Ethernet support are work in progress, with patches being on the list already. The Ethernet PHY (Maxio MAE0621) is not yet supported in mainline, but should work with the generic driver. The AIC8800 WiFi chip is not supported. Out-of-tree patches for both chips exist, though, but would need to be ported, polished and upstreamed. 
## Manual build
You can build things for yourself by following our [ Manual build howto][59672] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _x96q_pro_plus_defconfig_ build target. Supported since v2025.10-rc1. 
### Mainline Linux Kernel
Basic headless support is working since v6.15, with the DT being merged in v6.16. eMMC access is broken still. 
Use the _sun55i-h728-x96qpro+.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
There is a FEL button on the PCB (behind the 3.5mm headphone socket). It can be reached by a non-conductive tool (like a toothpick) through the socket, and will trigger FEL mode when pressed while the box reboots or is powered on. Alternatively, enter FEL mode with the fel-sdboot.sunxi image written to a micro-SD card. 
The USB 2.0 socket closer to the back of the device, around the corner of the power button, is connected to USB controller 0, a non-standard USB A-to-A cable can be used to connect using FEL. 
## on board buttons/headers
There is a reset button on the board, behind the SPDIF socket, though it cannot be triggered from the outside. There is a second set of serial pins, between the SD card slot and the USB 2.0 socket. 
There is also a marking for an unpopulated cr1220/1225 battery holder for the RTC. Soldering the wires of a cr2032 case onto the square-ish pads works, the date/time survives a powerloss. Wire from top of battery goes to the pad nearest to the power barrel. 
# Adding a serial port (**voids warranty**)
[![][59673]][59674]
[][59675]
X96QPro+ UART pads
## Device disassembly
There is a small warranty sticker across one edge that needs to be cut to open the case. 
Turn the device over, and slide a [plastic tool][59676] around the edges of the bottom plate. This is just held in place with clips, there are NO screws hidden under the rubber feet. Lift the bottom place up. The PCB is held in place by three small Philips screws. 
## Locating the UART
The debug UART0 pins are located between the SPDIF and the USB3.0 socket, and are clearly labelled GND, RX, TX, 3.3V. Solder three wires there, and leave 3.3V unconnected. Connect to an adapter translating the 3.3V TTL logic level to something standard, so either USB or 12V RS232. The [UART howto][59677] has more information. 
# Pictures
Take some pictures of your device, [ upload them][59678], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![X96qpro+ front.jpg][59679]][59646]
  * [![X96qpro+ back.jpg][59680]][59681]
  * [![X96qpro+ side.jpg][59682]][59683]
  * [![X96qpro+ top.jpg][59684]][59685]
  * [![X96qpro+ bottom.jpg][59686]][59687]
  * [![X96qpro+ pcb top.jpg][59688]][59689]
  * [![X96qpro+ pcb bottom.jpg][59690]][59691]
  * [![X96qpro+ pcb wifi eth.jpg][59692]][59693]

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
