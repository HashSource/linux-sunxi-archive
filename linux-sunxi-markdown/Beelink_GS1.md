# Beelink GS1
Beelink GS1  
---  
[![Beelink GS1 above.jpg][9642]][9643]  
Manufacturer |  [Shenzhen AZW Technology][9644]  
Dimensions |  100 _mm_ x 100 _mm_ x 17 _mm_  
Specifications   
SoC |  [H6][9645] @ 1.8Ghz   
DRAM |  2GiB LPDDR3 @744 MHz, SpecTek SM512M32V01MD2LPF-107 or 3GiB LPDDR3   
NAND |  16GB (eMMC 5.0) Toshiba THGBMBG7D2KBAIL, or 32GB (eMMC 5.0)   
Power |  DC 5V @ 2A,   
Features   
Video |  HDMI (Type A - full)   
Audio |  HDMI, SPDIF,   
Network |  WiFi 802.11 b/g/n/ac ([Fn-Link 6222B-PRB][9646]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][9647])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB3.0 HOST   
This page needs to be properly filled according to the [New Device Howto][9648] and the [New Device Page guide][9649].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][9650]
  * [2 Sunxi support][9651]
    * [2.1 Current status][9652]
    * [2.2 Manual build][9653]
      * [2.2.1 U-Boot][9654]
        * [2.2.1.1 Mainline U-Boot][9655]
      * [2.2.2 Linux Kernel][9656]
        * [2.2.2.1 Sunxi/Legacy Kernel][9657]
        * [2.2.2.2 Mainline kernel][9658]
  * [3 Tips, Tricks, Caveats][9659]
    * [3.1 FEL mode][9660]
    * [3.2 Device specific topic][9661]
    * [3.3 ...][9662]
  * [4 Adding a serial port (**voids warranty**)][9663]
    * [4.1 Device disassembly][9664]
    * [4.2 Locating the UART][9665]
  * [5 Pictures][9666]
  * [6 Also known as][9667]
  * [7 See also][9668]
    * [7.1 Manufacturer images][9669]

# Identification
On the bottom of the device, the following is printed: 
[code] 
    Model:Beelink GS1
[/code]
The PCB has the following silkscreened on it: 
[code] 
    beelink
    GS1
    Ver:2.0
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _Beelink GS1_
  * Build Number: _102NO_

# Sunxi support
## Current status
Beelink GS1 is currently supported by both mainline U-Boot and kernels. 
## Manual build
You can build things for yourself by following our [ Manual build howto][9670] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
use the **beelink_gs1_defconfig** (supported since v2019.07) build target. 
Write u-boot-sunxi-with-spl.bin to an SD card with "dd if=u-boot-sunxi-with-spl.bin of=/dev/[SD] bs=1024 seek=8 conv=notrunc" 
### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
use the **sun50i-h6-beelink-gs1.dtb** (kernel 5.2+). [https://git.kernel.org/pub/scm/linux/kernel/git/sunxi/linux.git/commit/?h=sunxi/for-next&id=089bee8dd119ba084dee6b17a2e1a53df4f30193][9671]
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The button on the bottom of the PCB triggers FEL mode (to be confirmed). It is reachable through a small hole in the bottom plastic cover. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][9672]][9673]
[][9674]
UART pads
The GS1 UART runs at 3.3V levels, so you need a level converter (e.g. MAX3323) to connect the board to a regular serial port. Alternatively, a USB-to-UART adapter with 3.3V levels will also work. 
## Device disassembly
The case is clipped together using plastic tabs on all four sides. Please see the [Plastic tool howto][9675] for details of opening cases like these. The PCB is held in place by three small Philips-head screws. Make sure to remove the µSD card before taking out the PCB. 
## Locating the UART
The UART (3.3V levels) is available on four solder holes (2mm spacing) next to the eMMC chip slot. Soldering in a header will void the warranty. 
With the square pad as pin 1 the pinout is as follows **confirmed using USB-UART adapter** : 
  * Pin 1: GND
  * Pin 2: RxD
  * Pin 3: TxD
  * Pin 4: 3v3

# Pictures
  * [![Beelink GS1 top.jpg][9676]][9677]
  * [![Beelink GS1 base.jpg][9678]][9679]
  * [![Beelink GS1 back.jpg][9680]][9681]
  * [![Beelink GS1 side.jpg][9682]][9683]
  * [![Beelink GS1 pcbtop.jpg][9684]][9685]
  * [![Beelink GS1 pcbbottom.jpg][9686]][9687]
  * [![Beelink GS1 heatsink.jpg][9688]][9689]
  * [![Beelink GS1 box.jpg][9690]][9691]

# Also known as
There are currently no known rebadged devices. Update this section if you know otherwise. 
# See also
  * [Beelink_GS1 on 'wikidevi'][9692]
  * AXP805 Datasheet: [File:AXP805 Datasheet V1.0 en.pdf][9693]
  * H6 Datasheet: [File:Allwinner H6 V200 Datasheet V1.1.pdf][9694]
  * H6 User Manual: [File:Allwinner H6 V200 User Manual V1.1.pdf][9695]
  * [xda-developers Review][9696]

## Manufacturer images
Optional. Add non-sunxi images in this section.
