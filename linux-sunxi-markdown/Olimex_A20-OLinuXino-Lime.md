# Olimex A20-OLinuXino-Lime
Olimex A20-OLinuXino-Lime  
---  
[![Olimex lime angle.jpeg][40709]][40710]  
Manufacturer |  [Olimex][40711]  
Dimensions |  84 _mm_ x 60 _mm_ x 20 _mm_  
Release Date |  July 2014   
Website |  [Product page][40712]  
Specifications   
SoC |  [A20][40713] @ 1Ghz   
DRAM |  512MiB DDR3 @ 480MHz   
NAND |  4GB (optional)   
Power |  DC 5V @ 1A   
Features   
Video |  HDMI (Type A - Full)   
Audio |  HDMI   
Network |  10/100Mbps Ethernet ([Realtek RTL8201CP][40714])   
Storage |  µSD, SATA   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART, LCD/Touchscreen, LiPo Battery, 4 GPIO connectors   
The A20 Olinuxino LIME is a low-cost [OSHW][40715] board that fits in the palm of your hand. This board is produced by [Olimex][40716] and can be purchased for about 33€. A20-OLinuXino-LIME looks identical to [Olimex A10-OLinuXino-Lime][40717], except for the more powerful A20 processor. 
There is a second version of the A20 Lime (with 1GiB of RAM and Gigabit ethernet), called the [Olimex A20-OLinuXino-Lime2][40718]. 
## Contents
  * [1 Identification][40719]
  * [2 Sunxi support][40720]
    * [2.1 Current status][40721]
    * [2.2 Images][40722]
    * [2.3 HW-Pack][40723]
    * [2.4 BSP][40724]
    * [2.5 Manual build][40725]
      * [2.5.1 Mainline U-Boot][40726]
    * [2.6 Mainline kernel][40727]
  * [3 Tips, Tricks, Caveats][40728]
    * [3.1 FEL mode][40729]
    * [3.2 LCD modules][40730]
  * [4 Adding a serial port][40731]
  * [5 Pictures][40732]
  * [6 Also known as][40733]
  * [7 See also][40734]

# Identification
The board handily reads "A20-OLinuXino-Lime" on the back. 
# Sunxi support
## Current status
Supported. 
## Images
Official images can be found [here][40735]. 
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _A20-OLinuXino-Lime_ target.
  * The .fex file can be found in sunxi-boards as [a20-olinuxino_lime.fex][40736]
  * The device name for flash-kernel is _Olimex A20-OLinuXino-LIME_

Everything else is the same as the [manual build howto][40737]. 
#### Mainline U-Boot
Use the _A20-OLinuXino-Lime_defconfig_ build target. 
## Mainline kernel
Use the _sun7i-a20-olinuxino-lime.dts_ device-tree file for the [mainline kernel][40738]. 
# Tips, Tricks, Caveats
## FEL mode
The recovery button (right, under the battery connector) triggers [ FEL mode][40739]. 
## LCD modules
You can attach [several Olimex LCD modules][40740] to the LCD connector (LCD_CON). You will need a 1.27mm pitch to 2.54mm 40 pin cable though. 
# Adding a serial port
[![][40741]][40742]
[][40743]
UART pins
There is a clearly marked 3 pin 2.54mm header which exposes UART0, just attach some leads according to our [UART howto][40744]. 
# Pictures
  * [![Olimex-A20-LIME.jpg][40745]][40746]
  * [![Olimex-A20-LIME-back.jpg][40747]][40748]
  * [![Olimex A20-LIME board top.jpg][40749]][40750]
  * [![Olimex A20-LIME board back.JPG][40751]][40752]
  * [![Olimex A20-LIME package.JPG][40753]][40754]
  * [![Olimex lime front.jpeg][40755]][40756]
  * [![Olimex lime back.jpeg][40757]][40758]

# Also known as
This type of device has no rebadges. 
# See also
  * [Olimex A10-OLinuXino-Lime][40717]
  * [Olimex A20-OLinuXino-Lime2][40718]
  * [Other olimex devices][40716]
  * [Olimex wiki page with detailed board information.][40759]
