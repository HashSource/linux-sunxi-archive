# Olimex A10-OLinuXino-Lime
(Redirected from [A10-OLinuXino-LIME][1169])
 
Olimex A10-OLinuXino-Lime  
---  
[![Olimex lime angle.jpeg][1172]][1173]  
Manufacturer |  [Olimex][1174]  
Dimensions |  84 _mm_ x 60 _mm_ x 20 _mm_  
Release Date |  December 2013   
Website |  [Product page][1175]  
Specifications   
SoC |  [A10][1176] @ 1Ghz   
DRAM |  512MiB DDR3 @ 480MHz ([MEM4G16D3EABG-125][1177])   
Power |  DC 5V @ 1A   
Features   
Video |  HDMI (Type A - Full)   
Audio |  HDMI   
Network |  10/100Mbps Ethernet ([Realtek RTL8201CP][1178])   
Storage |  µSD, SATA, 4GB NAND (optional)   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART, LCD/Touchscreen, LiPo Battery, 4 GPIO connectors   
The A10 Olinuxino LIME is a low-cost [OSHW][1179] board that fits in the palm of your hand. This board is produced by [Olimex][1180] and can be purchased for about 30€. 
## Contents
  * [1 Identification][1181]
  * [2 Sunxi support][1182]
    * [2.1 Current status][1183]
    * [2.2 Manual build][1184]
      * [2.2.1 U-Boot][1185]
        * [2.2.1.1 Sunxi/Legacy U-Boot][1186]
        * [2.2.1.2 Upstream/Mainline U-Boot][1187]
      * [2.2.2 Linux Kernel][1188]
        * [2.2.2.1 Sunxi/Legacy Kernel][1189]
        * [2.2.2.2 Upstream/Mainline kernel][1190]
  * [3 Tips, Tricks, Caveats][1191]
    * [3.1 FEL mode][1192]
    * [3.2 LCD modules][1193]
  * [4 Adding a serial port][1194]
  * [5 Pictures][1195]
  * [6 Also known as][1196]
  * [7 See also][1197]

# Identification
The board handily reads "A10-OLinuXino-Lime" on the back. 
# Sunxi support
## Current status
Fully supported. 
## Manual build
You can build things for yourself by following our [ Manual build howto][1198] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _A10-OLinuXino-Lime_ build target. 
#### Upstream/Mainline U-Boot
Use the _A10-OLinuXino-Lime_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_a10-olinuxino-lime.fex_][1199] file. 
#### Upstream/Mainline kernel
Use the _sun4i-a10-olinuxino-lime.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The recovery button (right, under the battery connector) triggers [ FEL mode][1200]. 
## LCD modules
You can attach [several Olimex LCD modules][1201] to the LCD connector (LCD_CON). You will need a 1.27mm pitch to 2.54mm 40 pin cable though. 
# Adding a serial port
[![][1202]][1203]
[][1204]
UART pins
There is a clearly marked 3 pin 2.54mm header which exposes UART0, just attach some leads according to our [UART howto][1205]. 
# Pictures
  * [![A10-LIME.jpg][1206]][1207]
  * [![Olimex LIME board top.jpg][1208]][1209]
  * [![Olimex LIME board back.jpg][1210]][1211]
  * [![Olimex lime front.jpeg][1212]][1213]
  * [![Olimex lime back.jpeg][1214]][1215]

# Also known as
This type of device has no rebadges. 
# See also
  * [Olimex wiki page with detailed board information.][1216]
  * [Olimex LIME CAD files.][1217]
