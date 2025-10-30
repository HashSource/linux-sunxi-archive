# Inet K970
Inet K970  
---  
[![Planet-1-Total.jpg][27082]][27083]  
Manufacturer |  [Inet Tek][27084]  
Dimensions |  260 _mm_ x 170 _mm_ x 11,5 _mm_  
Release Date |  August 2014   
Website |  [Board page][27085]  
Specifications   
SoC |  [A20][27086] @ 1 Ghz   
DRAM |  1GiB DDR3 @ 408 MHz   
NAND |  8 GB   
Power |  DC 5V @ 2A, 8000mAh 3.7V Polymer battery   
Features   
LCD |  1024x768 (9.7" 4:3)   
Touchscreen |  5-finger capacitive ([Focaltech FT5406EE8][27087])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8723AU][27088])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3MP (640×480) front (Device: gc0308), 2.0MP (1616×1232??? Why is this not 1920x1080???) rear (Device: gc2035)   
Other |  Accelerometer ([Freescale MMA8652][27089] / [Freescale MMA8653][27090]), Bluetooth ([Realtek RTL8723AU][27091]), [Buttons][27092]  
Headers |  [UART][27093]  
This page needs to be properly filled according to the [New Device Howto][27094] and the [New Device Page guide][27095].
## Contents
  * [1 Identification][27096]
  * [2 Sunxi support][27097]
    * [2.1 Current status][27098]
    * [2.2 Images][27099]
    * [2.3 HW-Pack][27100]
    * [2.4 BSP][27101]
    * [2.5 Manual build][27102]
    * [2.6 Mainline U-Boot][27103]
    * [2.7 Mainline kernel][27104]
  * [3 Tips, Tricks, Caveats][27105]
    * [3.1 FEL mode][27106]
    * [3.2 Reset button][27107]
  * [4 Adding a serial port (**voids warranty**)][27093]
    * [4.1 Device disassembly][27108]
    * [4.2 Locating the UART][27109]
  * [5 Pictures][27110]
  * [6 Also known as][27111]
  * [7 See also][27112]

# Identification
On the back of the device, the following is printed: 
[code] 
    Tristan Auron
    Planet 1
    
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INET-K970-REV02
    Zeng-gc
    2013-08-27
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _planet 1_
  * Build Number: _A20_K9701_K9701L2B_1210239.20121030_

# Sunxi support
## Current status
Supported by the legacy u-boot-sunxi and sunxi-3.4 kernel. 
Only partially working are: 
  * Bluetooth

Currently broken for A20 is: 
  * USB OTG

No drivers or suitable dts are readily at hand for the following devices: 
  * Power Status, (mainline, in RFC state, see following [thread][27113])
  * Nand (mainline, see [MTD Driver][27114])
  * G-Sensor
  * Cameras

## Images
## HW-Pack
## BSP
## Manual build
  * u-boot-sunxi is deprecated, use mainline u-boot as delineated below.
  * The .fex file can be found in sunxi-boards as [inet_k970.fex][27115]

Everything else is the same as the [ Manual build howto][27116]. 
## Mainline U-Boot
[![][27117]][27118]
[][27119]
U-boot showing its dialog on the LCD.
Fix target naming. For [ building mainline u-boot][27120], use the _Tristan_Auron_Planet_1_defconfig_ target. 
A [patch][27121] is currently under review. 
Until the patch and new various features hit the main repository, use the following u-boot as mainline: 
[code] 
    $ git clone -b sunxi-wip https://github.com/jwrdegoede/u-boot-sunxi/tree/sunxi-wip
[/code]
In particular, this allows an u-boot dialog using an usb-keyboard and the tablet's LCD. 
## Mainline kernel
Use the _sun7i-a20-inet-k970.dtb_ ([once accepted][27122]) device-tree file for the [mainline kernel][27123]. 
# Tips, Tricks, Caveats
## FEL mode
The _Vol+_ button triggers [ FEL mode][27124]. 
## Reset button
Like with most Inet-tek tablets, a reset button is available through the pinhole on the back. 
# Adding a serial port (**voids warranty**)
[![][27125]][27126]
[][27127]
tablet with opened back cover
While the UART is located as delineated below and works properly, note that this is an option, and I'm not advising to use it. I fact, I for one was not able to get the touchscreen going again, after reconnecting the ribbon. In case you do need an UART, which I didn't, you might want to consider using a less intrusive approach, e.g. the [MicroSD_Breakout][27128]. Additionally, current [mainline U-boot][27129] provides output to HDMI, until you have setup [LCD][27130] parameters. 
## Device disassembly
To open the tablet, first remove the two screws on the connector's side. As the picture aside shows, the back cover can most safely be lifted from the side opposite to the connectors. Try using a [Plastic tool][27131]. A spool-like tool, shown with the opened device, worked better for me. Before trying to open the tablet, notice the eyelets on the back cover clearly visible both at the cover itself and its shadows. I found it best to open it first at one of the loops in the middle. Further take care of the speaker cables when lifting the back cover. 
[![][27132]][27133]
[][27134]
UART pads
## Locating the UART
The RX,TX pads are hidden under the touchscreen ribbon located on the right side of the board's front picture. To remove the ribbon, lift the connector's lever visible as a narrow dark bar at the upper edge of the white connector. The ribbon is released then and can be pulled out of the connector without force. The GND is textually marked at another place on the board close to the right upper edge of the board's front picture and connected to the large copper area. See the gallery below for details. 
# Pictures
  * [![Planet-1-Front.jpg][27135]][27136]
  * [![Planet-1-Back.jpg][27137]][27138]
  * [![Planet-1-Connectors.jpg][27139]][27140]
  * [![Device buttons 2.jpg][27141]][27142]
  * [![Planet-1-Board-01.jpg][27143]][27144]
  * [![Device board back.jpg][27145]][27146]

  * [![Planet-1-Uart-2.jpg][27147]][27148]
  * [![Planet-1-Uart-3.jpg][27149]][27150]

# Also known as
  * [Tristan Auron Planet 1][27151]
  * [M973][27152]

# See also
