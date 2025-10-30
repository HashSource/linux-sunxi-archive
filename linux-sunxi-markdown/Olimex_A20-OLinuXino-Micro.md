# Olimex A20-OLinuXino-Micro
Olimex A20-OLinuXino-Micro  
---  
[![A20-OLinuXino.jpeg][40953]][40954]  
Manufacturer |  [Olimex][40955]  
Dimensions |  142 _mm_ x 82 _mm_ x 20 _mm_  
Release Date |  May 2013   
Website |  [Product page][40956]  
Specifications   
SoC |  [A20][40957] @ 1 Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  4GB (optional)   
Power |  DC 6-16V @ 3A   
Features   
Video |  HDMI (Type A)   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI   
Network |  10/100Mbps ethernet ([Realtek RTL8201CP][40958])   
Storage |  µSD, SD, SATA   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  2KiB EEPROM   
Headers |  UART, JTAG, LCD, VGA, 2xUEXT, LiPo battery.   
A20-OLinuXino-Micro is fully [OSHW][40959] [A20][40957] based development board from our friends at [Olimex][40960]. 
This board was [originally designed][40961] with the pin-compatible [A10][40962] in mind. While this design never shipped, Olimex can produce [A10][40962] versions of this board if you so desire. 
## Contents
  * [1 Identification][40963]
  * [2 Sunxi support][40964]
    * [2.1 Current status][40965]
    * [2.2 Images][40966]
    * [2.3 HW-Pack][40967]
    * [2.4 BSP][40968]
    * [2.5 Manual build][40969]
      * [2.5.1 U-Boot][40970]
        * [2.5.1.1 Sunxi/Legacy U-Boot][40971]
        * [2.5.1.2 Mainline U-Boot][40972]
      * [2.5.2 Linux Kernel][40973]
        * [2.5.2.1 Sunxi/Legacy Kernel][40974]
        * [2.5.2.2 Mainline kernel][40975]
  * [3 Tips, Tricks, Caveats][40976]
    * [3.1 FEL mode][40977]
    * [3.2 LCD Modules][40978]
    * [3.3 Expansion Ports][40979]
  * [4 Adding a serial port][40980]
    * [4.1 Pictures][40981]
  * [5 Also known as][40982]
  * [6 See also][40983]

# Identification
The board helpfully reads "A20-OLINUXINO-MICRO". 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
You can build things for yourself by following our [ Manual build howto][40984] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
  * The .fex file can be found in sunxi-boards as [a20-olinuxino_micro.fex][40985]
  * There are also several fex files dealing with the different LCDs in [the same directory][40986].

#### Mainline U-Boot
  * For building U-boot, use the **A20-OLinuXino_MICRO_defconfig** target.
  * There is another U-boot target for the eMMC version, **A20-OLinuXino_MICRO-eMMC_defconfig**.

Related issues: 
  * <https://github.com/rzr/u-boot/issues/2>

### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
Use the **sun7i-a20-olinuxino-micro.dtb** device-tree binary. See [mainline kernel][40987]. 
# Tips, Tricks, Caveats
## FEL mode
The recovery button triggers [ FEL mode][40988]. 
## LCD Modules
See the [ Olimex LCD Modules][40989] page for more information on how to attach and set up Olimex LCD panels on this hardware. 
## Expansion Ports
This board has multiple expansion ports: 
  * `GPIO-1 / LCD_CON` \- compatible with 4.3", 7.0", 10.1" LCD modules from Olimex, can also be used for general GPIO support.
  * `GPIO-2`, `GPIO-3`, `GPIO-4` \- general GPIO support
  * `UEXT1` and `UEXT2`

# Adding a serial port
[![][40990]][40991]
[][40992]
UART0 pins
There is a clearly marked UART on the top of the device. All you have to do is connect some wires according to our [UART howto][40993]. 
[![Exclamation-red.png][40994]][40995] **Warning: Do no connect the _3.3V_ pin. This could damage your board.**
## Pictures
  * [![A20 olinuxino micro-board front.jpg][40996]][40997]
  * [![A20 olinuxino micro-board back.jpg][40998]][40999]
  * [![A20-OLinuXino-FRONT.jpg][41000]][41001]
  * [![A20-OLinuXino-BACK.jpg][41002]][41003]

# Also known as
There are of course no rebadgers for this device, but you might sometimes see it referred to as the A20-Olinuxino. 
# See also
  * [Our local Olimex page][40960] showing all other Olimex products.
  * [Original announcement on Olimex's blog.][40961]
  * [Schematics and various docs][41004]
