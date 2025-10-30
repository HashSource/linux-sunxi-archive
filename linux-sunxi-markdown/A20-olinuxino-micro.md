# Olimex A20-OLinuXino-Micro
(Redirected from [A20-olinuxino-micro][2780])
 
Olimex A20-OLinuXino-Micro  
---  
[![A20-OLinuXino.jpeg][2783]][2784]  
Manufacturer |  [Olimex][2785]  
Dimensions |  142 _mm_ x 82 _mm_ x 20 _mm_  
Release Date |  May 2013   
Website |  [Product page][2786]  
Specifications   
SoC |  [A20][2787] @ 1 Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  4GB (optional)   
Power |  DC 6-16V @ 3A   
Features   
Video |  HDMI (Type A)   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI   
Network |  10/100Mbps ethernet ([Realtek RTL8201CP][2788])   
Storage |  µSD, SD, SATA   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  2KiB EEPROM   
Headers |  UART, JTAG, LCD, VGA, 2xUEXT, LiPo battery.   
A20-OLinuXino-Micro is fully [OSHW][2789] [A20][2787] based development board from our friends at [Olimex][2790]. 
This board was [originally designed][2791] with the pin-compatible [A10][2792] in mind. While this design never shipped, Olimex can produce [A10][2792] versions of this board if you so desire. 
## Contents
  * [1 Identification][2793]
  * [2 Sunxi support][2794]
    * [2.1 Current status][2795]
    * [2.2 Images][2796]
    * [2.3 HW-Pack][2797]
    * [2.4 BSP][2798]
    * [2.5 Manual build][2799]
      * [2.5.1 U-Boot][2800]
        * [2.5.1.1 Sunxi/Legacy U-Boot][2801]
        * [2.5.1.2 Mainline U-Boot][2802]
      * [2.5.2 Linux Kernel][2803]
        * [2.5.2.1 Sunxi/Legacy Kernel][2804]
        * [2.5.2.2 Mainline kernel][2805]
  * [3 Tips, Tricks, Caveats][2806]
    * [3.1 FEL mode][2807]
    * [3.2 LCD Modules][2808]
    * [3.3 Expansion Ports][2809]
  * [4 Adding a serial port][2810]
    * [4.1 Pictures][2811]
  * [5 Also known as][2812]
  * [6 See also][2813]

# Identification
The board helpfully reads "A20-OLINUXINO-MICRO". 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
You can build things for yourself by following our [ Manual build howto][2814] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
  * The .fex file can be found in sunxi-boards as [a20-olinuxino_micro.fex][2815]
  * There are also several fex files dealing with the different LCDs in [the same directory][2816].

#### Mainline U-Boot
  * For building U-boot, use the **A20-OLinuXino_MICRO_defconfig** target.
  * There is another U-boot target for the eMMC version, **A20-OLinuXino_MICRO-eMMC_defconfig**.

Related issues: 
  * <https://github.com/rzr/u-boot/issues/2>

### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
Use the **sun7i-a20-olinuxino-micro.dtb** device-tree binary. See [mainline kernel][2817]. 
# Tips, Tricks, Caveats
## FEL mode
The recovery button triggers [ FEL mode][2818]. 
## LCD Modules
See the [ Olimex LCD Modules][2819] page for more information on how to attach and set up Olimex LCD panels on this hardware. 
## Expansion Ports
This board has multiple expansion ports: 
  * `GPIO-1 / LCD_CON` \- compatible with 4.3", 7.0", 10.1" LCD modules from Olimex, can also be used for general GPIO support.
  * `GPIO-2`, `GPIO-3`, `GPIO-4` \- general GPIO support
  * `UEXT1` and `UEXT2`

# Adding a serial port
[![][2820]][2821]
[][2822]
UART0 pins
There is a clearly marked UART on the top of the device. All you have to do is connect some wires according to our [UART howto][2823]. 
[![Exclamation-red.png][2824]][2825] **Warning: Do no connect the _3.3V_ pin. This could damage your board.**
## Pictures
  * [![A20 olinuxino micro-board front.jpg][2826]][2827]
  * [![A20 olinuxino micro-board back.jpg][2828]][2829]
  * [![A20-OLinuXino-FRONT.jpg][2830]][2831]
  * [![A20-OLinuXino-BACK.jpg][2832]][2833]

# Also known as
There are of course no rebadgers for this device, but you might sometimes see it referred to as the A20-Olinuxino. 
# See also
  * [Our local Olimex page][2790] showing all other Olimex products.
  * [Original announcement on Olimex's blog.][2791]
  * [Schematics and various docs][2834]
