# Olimex A10-OLinuXino-Lime
Olimex A10-OLinuXino-Lime  
---  
[![Olimex lime angle.jpeg][40285]][40286]  
Manufacturer |  [Olimex][40287]  
Dimensions |  84 _mm_ x 60 _mm_ x 20 _mm_  
Release Date |  December 2013   
Website |  [Product page][40288]  
Specifications   
SoC |  [A10][40289] @ 1Ghz   
DRAM |  512MiB DDR3 @ 480MHz ([MEM4G16D3EABG-125][40290])   
Power |  DC 5V @ 1A   
Features   
Video |  HDMI (Type A - Full)   
Audio |  HDMI   
Network |  10/100Mbps Ethernet ([Realtek RTL8201CP][40291])   
Storage |  µSD, SATA, 4GB NAND (optional)   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART, LCD/Touchscreen, LiPo Battery, 4 GPIO connectors   
The A10 Olinuxino LIME is a low-cost [OSHW][40292] board that fits in the palm of your hand. This board is produced by [Olimex][40293] and can be purchased for about 30€. 
## Contents
  * [1 Identification][40294]
  * [2 Sunxi support][40295]
    * [2.1 Current status][40296]
    * [2.2 Manual build][40297]
      * [2.2.1 U-Boot][40298]
        * [2.2.1.1 Sunxi/Legacy U-Boot][40299]
        * [2.2.1.2 Upstream/Mainline U-Boot][40300]
      * [2.2.2 Linux Kernel][40301]
        * [2.2.2.1 Sunxi/Legacy Kernel][40302]
        * [2.2.2.2 Upstream/Mainline kernel][40303]
  * [3 Tips, Tricks, Caveats][40304]
    * [3.1 FEL mode][40305]
    * [3.2 LCD modules][40306]
  * [4 Adding a serial port][40307]
  * [5 Pictures][40308]
  * [6 Also known as][40309]
  * [7 See also][40310]

# Identification
The board handily reads "A10-OLinuXino-Lime" on the back. 
# Sunxi support
## Current status
Fully supported. 
## Manual build
You can build things for yourself by following our [ Manual build howto][40311] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _A10-OLinuXino-Lime_ build target. 
#### Upstream/Mainline U-Boot
Use the _A10-OLinuXino-Lime_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_a10-olinuxino-lime.fex_][40312] file. 
#### Upstream/Mainline kernel
Use the _sun4i-a10-olinuxino-lime.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The recovery button (right, under the battery connector) triggers [ FEL mode][40313]. 
## LCD modules
You can attach [several Olimex LCD modules][40314] to the LCD connector (LCD_CON). You will need a 1.27mm pitch to 2.54mm 40 pin cable though. 
# Adding a serial port
[![][40315]][40316]
[][40317]
UART pins
There is a clearly marked 3 pin 2.54mm header which exposes UART0, just attach some leads according to our [UART howto][40318]. 
# Pictures
  * [![A10-LIME.jpg][40319]][40320]
  * [![Olimex LIME board top.jpg][40321]][40322]
  * [![Olimex LIME board back.jpg][40323]][40324]
  * [![Olimex lime front.jpeg][40325]][40326]
  * [![Olimex lime back.jpeg][40327]][40328]

# Also known as
This type of device has no rebadges. 
# See also
  * [Olimex wiki page with detailed board information.][40329]
  * [Olimex LIME CAD files.][40330]
