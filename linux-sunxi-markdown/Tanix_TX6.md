# Tanix TX6
Tanix TX6  
---  
[![Tanix tx6 front.png][54342]][54343]  
Manufacturer |  Tanix   
Dimensions |  105 _mm_ x 105 _mm_ x 25 _mm_  
Release Date |  Late 2018   
Website |  www.tanix-box.com   
Specifications   
SoC |  [H6][54344] @ 1.5Ghz   
DRAM |  2/4GiB DDR3 @ 667MHz/800Mhz[[1]][54345]  
NAND |  16/32/64GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full)   
Audio |  HDMI, SPDIF   
Network |  WiFi: 802.11 b/g/n/ac ([47822BS-10][54346] or [RTL8822CS][54346]) or 802.11 b/g/n ([XRadio XR819][54347]); 10/100Mbps Ethernet ([Manufacturer device][54348])   
Storage |  µSD, eMMC   
USB |  2 USB2.0 Host, 1 USB3.0   
Other |  IRDA   
This page needs to be properly filled according to the [New Device Howto][54349] and the [New Device Page guide][54350].
Inexpensive TV box with the H6 SoC and either mid-range specifications (4GiB RAM, 32/64GiB eMMC, 2.4 and 5Ghz AC Wifi) or low end specs (2GiB RAM, 16GiB eMMC, 2.4n Wifi), but missing GBit Ethernet. 
Several versions of this box are available with different memory configurations and wifi chips. All versions seem to use the same PCB which has a layout that supports **both** wifi chips (only one is populated of course). 
## Contents
  * [1 Identification][54351]
    * [1.1 Stock Android information][54352]
  * [2 Sunxi support][54353]
    * [2.1 Current status][54354]
    * [2.2 Manual build][54355]
      * [2.2.1 U-Boot][54356]
        * [2.2.1.1 Mainline U-Boot][54357]
      * [2.2.2 Linux Kernel][54358]
        * [2.2.2.1 SDK Kernel][54359]
        * [2.2.2.2 Mainline kernel][54360]
  * [3 Tips, Tricks, Caveats][54361]
    * [3.1 FEL mode][54362]
    * [3.2 Device specific topic][54363]
  * [4 Adding a serial port (**voids warranty**)][54364]
    * [4.1 Device disassembly][54365]
    * [4.2 Locating the UART][54366]
  * [5 Pictures][54367]
  * [6 Also known as][54368]
  * [7 See also][54369]
    * [7.1 Manufacturer images][54370]
  * [8 References][54371]

# Identification
On the back of the device, the following is printed on a sticker: 
[code] 
    Model: TX6
[/code]
Some devices have version suffix: 
[code] 
    Model: TX6-A
[/code]
On the bottom side of the PCB there is a sticker with information about the model variant: 
  * **TX-6** (no-suffix version): 4GiB RAM / 32GiB eMMC - Wifi: RTL8822 ([47822BS-10][54372])

[code] 
    TX6
    4+32(RTL8822)
    2018110050
[/code]
PCB version (silkscreened near the SoC): `CS_H6_TX28_V1.0 20181023 L4`  
This earlier version's PCB doesn't include unpopulated connections for XR819.[[2]][54373]
  * **Version A** : 4GiB RAM / 32GiB eMMC - Wifi: XR819 ([XRadio XR819][54347])

[code] 
    TX6-A
    4+32(819) V2.3
    20190920
[/code]
PCB version (silkscreened near the SoC): `CS_H6_TX28_V2.3 20190518.L4`
  * **Version H** : 4GiB RAM / 32/64GiB eMMC - Wifi: RTL8822 ([47822BS-10][54372])

[code] 
    TX6-H
    4+64(RTL8822) V2.3
    20190716
[/code]
There's also version with datecode: 20190924. 
  * **TX6-H (second version)** 4GiB RAM / 64GiB eMMC- Wifi: RTL8822CS ([RTL8822CS][54374])

[code] 
    TX6-H
    4+64G(RTL8822CS) V2.7
    12068 20201219
[/code]
PCB version (silkscreened near the SoC): `CS_H6_TX28_V2.7 20200616.L6`
  * **Version L:** 3GiB RAM / 16GiB eMMC- Wifi: XR819 ([XRadio XR819][54347])

[code] 
    TX6-L
    3+16(819) V2.3
    2019010013
[/code]
  * **Version P:** 2GiB RAM / 16GiB eMMC- Wifi: XR819 ([XRadio XR819][54347])

[code] 
    TX6-P
    2+16(819) V2.3
    20190801
[/code]
PCB version (silkscreened near the SoC): `CS_H6_TX28_V2.3 20190518.L4`
## Stock Android information
Android information from stock firmware, available under `Settings->About`: 
  * Model Number: TX6
  * Kernel Version: 4.9.118
  * Build Number: p281-userdebug 9 PPR1.181005.003

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Manual build
You can build things for yourself by following our [ Manual build howto][54375] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### SDK Kernel
Use the [tanix_tx6.fex][54376] file. 
#### Mainline kernel
From linux-5.4-rc1 use the _sun50i-h6-tanix-tx6.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
There is a slight issue with the SD-card slot: This is not the spring loaded type, but the one where the SD-card is removed by pulling it out. This is nearly impossible, since the SD-card does not protude from the slot when fully inserted. It does not help that removing the PCB from an opened device becomes quite tricky while an SD-card is present. Sticking a little strip of scotch tape etc. to the SD-card solves this (see pic). 
[![][54377]][54378]
[][54379]
Tanix TX6 SD-card slot and (modded) access to UART
The pin header connector to the left of the picure was added for easy access to the serial console [See also "locating the UART"][54366]. 
## FEL mode
Left of the SD-card slot, there is a button (barely) visible through the ventilation slots. It triggers [ FEL mode][54380] mode when held down while resetting or powering up. On the PCB this button is marked as "SW001" (there is another button marked "SW900" which cannot be reached without opening the box - purpose unknown). ToDo: Which of the two USB 2.0 ports will act as the OTG device? You will need a USB-A <-> USB-A cable for FEL mode. 
## Device specific topic
This device uses DDR3 (not LPDDR3) memory! 
Device is also equipped with 4-digit 7-segment display, driven by FD650B-S chip. 
# Adding a serial port (**voids warranty**)
[![][54381]][54382]
[][54383]
Tanix TX6 UART pads
The UART pad is this units are not clearly marked ("TX, "RX", ...). The correct pads are part of a 5 pad connector on the right front side of the device. Looking at the opened box with the CPU cooler facing upwards the pads are located on the left side of the PCB toward the front. The leftmost pad is TX, the one next to it provides RX and the two righmost pads are connected to ground (see picture). Please refer to the UART howto page [UART howto][54384] for more details on using a serial port. 
## Device disassembly
To open the box, turn it upside down and remove the rubber feet at each corner. This will expose 4 screws which have to be removed. Gently slide a plastic tool or a knife in the small gap around all edges of the box to eventually lift the bottom plate, releasing four plastic tabs in the middle of each side holding the cover. To remove the PCB, first lift the side with the 7 segment display up, then gently pull this side the PCB up. This is allow you to then remove the PCB - the backside connectors somewhat protude into the backside of the case. 
## Locating the UART
Looking at the opened box with the CPU cooler facing upwards the pads are located on the left side of the PCB toward the front. The leftmost pad is TX, the one next to it provides RX and the two righmost pads are connected to ground (see picture). Please refer to the UART howto page [UART howto][54384] for more details on using a serial port. 
# Pictures
  * Version TX6-H
  * [![Tanix tx6 front.png][54385]][54343]
  * [![Tanix tx6 bottom.png][54386]][54387]
  * [![Tanix tx6 pcb top.png][54388]][54389]
  * [![Tanix tx6 pcb bottom.png][54390]][54391]
  * [![Tanix tx6 fd650.jpg][54392]][54393]
  * [![Tanix tx6 micron emmc.jpg][54394]][54395]

  * Version TX6-H (Version 2)
  * [![Tanix tx6 h2 pcb top.jpg][54396]][54397]
  * [![Tanix tx6 h2 pcb bottom.jpg][54398]][54399]

  * Version TX6-A
  * [![Tanix-tx-6-a-board.jpg][54400]][54401]
  * [![Tanix-tx-6-a-board-back.jpg][54402]][54403]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
# References
  1. [↑][54404] Chips marked with: HYH9 - 667Mhz, HYK0 - 800Mhz
  2. [↑][54405] [https://forum.freaktab.com/forum/tv-player-support/allwinner-tv-players/751595-tanix-tx6-tv-box-allwinner-h6-4-32gb-dual-wifi-bt4-1-or-5?p=757381#post757381][54406]
