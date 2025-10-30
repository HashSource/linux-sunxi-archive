# Gemei G9
Gemei G9  
---  
[![Gemei g9 front.jpg][21824]][21825]  
Manufacturer |  Gemei Technologies (Defunct)   
Dimensions |  244 _mm_ x 187 _mm_ x 12 _mm_  
Release Date |  February 2012   
Website |  ~~www.gemeitech.com~~  
Specifications   
SoC |  [A10][21826] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz/480MHz (4x [NT5CB256M8DN-CG][21827])   
NAND |  16GB (2x Micron MT29F64G08CBAAAWP MLC)   
Power |  DC 5V @ 3A, 8000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (9.7" 4:3) ([LG LP097X02-SLQ2][21828])   
Touchscreen |  10-finger capacitive ([Goodix GT801 2+1][21829])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][21830])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  1.3MP (1280x1024) front, 5MP (2560x1920) rear   
Other |  Accelerometer ([Bosch BMA250][21831])   
Headers |  UART   
## Contents
  * [1 Identification][21832]
  * [2 Sunxi support][21833]
    * [2.1 Mainline status][21834]
      * [2.1.1 u-boot supported since 2015.4][21835]
      * [2.1.2 Linux kernel supported since 4.1][21836]
        * [2.1.2.1 Things todo][21837]
    * [2.2 sunxi-3.4 status][21838]
  * [3 Tips, Tricks, Caveats][21839]
    * [3.1 FEL mode][21840]
    * [3.2 ...][21841]
  * [4 Adding a serial port (**voids warranty**)][21842]
    * [4.1 Device disassembly][21843]
    * [4.2 Locating the UART][21844]
  * [5 Pictures][21845]
  * [6 Also known as][21846]
  * [7 See also][21847]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: `MID970`
  * Build Number: `03F2-P1-H1-H01-AH40.20120330`
  * Kernel version: `3.0.8+ inet_dada@InetSoftware #162`

# Sunxi support
## Mainline status
### u-boot supported since 2015.4
  * Use `sunxi_Gemei_G9_defconfig` target

### Linux kernel supported since 4.1
  * `sun4i-a10-gemei-g9.dts`

#### Things todo
  * Audio input (need A10 codec support)
  * Battery management (axp209 powersupply driver)
  * Camera interface (no CSI driver)
  * NAND
  * Touchscreen (no gt801_2plus1 driver)
  * USB OTG (host mode part works)

## sunxi-3.4 status
Somewhat supported. Wifi doesn't work 
  * The .fex file can be found in sunxi-boards as [gemei_g9.fex][21848].

Everything else is the same as the [manual build howto][21849]. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][21850]. 
## ...
# Adding a serial port (**voids warranty**)
[![][21851]][21852]
[][21853]
Gemei G9 UART pads
## Device disassembly
Remove the two screws on the connectors side. Gently pry the back cover off with your [plastic tool][21854]. 
## Locating the UART
There are clearly labelled UART pads under the touchscreen cable. Just solder on some wires according to our [UART howto][21855]. 
# Pictures
  * [![Gemei g9 front.jpg][21856]][21825]
  * [![Gemei-g9-back.jpg][21857]][21858]
  * [![Gemei-G9-buttons1.jpg][21859]][21860]
  * [![Gemei-g9 buttons2.jpg][21861]][21862]
  * [![Gemei g9 mainboard front.jpg][21863]][21864]
  * [![Gemei g9 mainboard back.jpg][21865]][21866]
  * [![Gemei g9 touch controller.jpg][21867]][21868]

  * [![Gemei g9 overview.jpg][21869]][21870]
  * [![Gemei g9 board overview.jpg][21871]][21872]
  * [![Gemei g9 touch controller annotated.jpg][21873]][21874]
  * [![Gemei g9 mainboard front annotated.jpg][21875]][21876]

# Also known as
# See also
[Teardown on slatedroid forums.][21877]
