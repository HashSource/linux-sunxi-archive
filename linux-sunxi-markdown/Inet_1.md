# Inet 1
Inet 1  
---  
[![CherryM1007Android.jpg][25904]][25905]  
Manufacturer |  [Inet-Tek][25906]  
Dimensions |  267 _mm_ x 164 _mm_ x 14 _mm_ (680g)   
Release Date |  December 2011   
Website |  [Rebadger Product Page][25907]  
Specifications   
SoC |  [A10][25908] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 5000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (10" 10:6)   
Touchscreen |  5-finger capacitive ([2x Focaltech FT5301][25909])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CTV][25910])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][25911] FIXME), reset button   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][25912] and the [New Device Page guide][25913].
## Contents
  * [1 Identification][25914]
    * [1.1 Point of View Protab2 XXL][25915]
    * [1.2 Cherry M1007][25916]
  * [2 Sunxi support][25917]
    * [2.1 Current status][25918]
    * [2.2 Images][25919]
    * [2.3 HW-Pack][25920]
    * [2.4 BSP][25921]
    * [2.5 Manual build][25922]
  * [3 Tips, Tricks, Caveats][25923]
    * [3.1 FEL mode][25924]
    * [3.2 FT5X touchscreen issues][25925]
  * [4 Adding a serial port (**voids warranty**)][25926]
    * [4.1 Device disassembly][25927]
    * [4.2 Locating the UART][25928]
  * [5 Pictures][25929]
  * [6 Also known as][25930]
  * [7 See also][25931]

# Identification
In android, under Settings->About Tablet, you will find... 
## Point of View Protab2 XXL
  * Model Number: TAB-Protab2XXL(4)
  * Kernel Version: 3.0.8+ paco@Inet #7
  * Build Number: 01F2-D1-H1-H01-1703.20120301

## Cherry M1007
  * Model Number: PC1007
  * Baseband Version: inet1.0_20
  * Kernel Version: 3.0.8+ inet._ldw@inetsuperserver #5 Mon Dec 17 20:39:56 CST 2012
  * Build Number: 01F2-D1-H1-H01-1744-20121217

# Sunxi support
## Current status
sunxi-boards support is still missing. TODO: add info about the fex and dts files that were added in September 2015 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "PoV_ProTab2_XXL" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][25932]

Everything else is the same as the [manual build howto][25933]. 
# Tips, Tricks, Caveats
## FEL mode
There is a button between power connector and Mini USB connector which triggers [ FEL mode][25934]. 
## FT5X touchscreen issues
To make ft5x touchscreen work with X you need to recompile ft5x_ts module as described at [Rhombus Tech][25935] after commenting out CONFIG_FT5X0X_MULTITOUCH in drivers/input/touchscreen/ft5x_ts.h. 
The module is availabe for kernel 3.0.39+ here: [[1]][25936]
The screen dimensions and axes will be confused. You will need to change your script.bin as described at [eLinux.org][25937] like following: 
[code] 
    ctp_screen_max_x = 600
    ctp_screen_max_y = 1024
[/code]
Axes can then be swapped with the Debian package xinput by running: 
[code] 
    xinput set-prop ft5x_ts "Evdev Axes Swap" 1
[/code]
# Adding a serial port (**voids warranty**)
[![][25938]][25939]
[][25940]
DEVICE UART pads
## Device disassembly
By removing the two screws on the connector side, the device is trivially opened. 
## Locating the UART
There are some clearly marked UART pads in the top left corner of the board, all you need to do is solder on some wires according to our [UART howto][25941]. 
# Pictures
Take some pictures of your device, [ upload them][25942], and add them here.
  * [![CherryM1007Android.jpg][25943]][25905]
  * [![CherryM1007Rear1.jpg][25944]][25945]
  * [![PP1k buttons.jpg][25946]][25947]
  * [![Device buttons 2.jpg][25948]][25949]
  * [![Device board front.jpg][25950]][25951]
  * [![Device board back.jpg][25952]][25953]

  

  * [![][25954]][25955]
Inside 
  * [![][25956]][25957]
ICB 
  * [![][25958]][25959]
ICB top left 
  * [![][25960]][25961]
ICB bottom right 
  * [![][25962]][25963]
ICB backside in housing; unscrewed and battery detached 
  * [![][25964]][25965]
Connector side with two screws 
  * [![][25966]][25967]
Connector side unscrewed and opened 

# Also known as
  * [Point of View Protab 2 XXL][25907]
  * [Cherry M1007 (PC1007)][25968]
  * [STOREX eZee'Tab10c][25969]

# See also
Add some nice to have links here. This includes related devices, and external links.
