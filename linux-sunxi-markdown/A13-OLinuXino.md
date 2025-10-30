# Olimex A13-OLinuXino
(Redirected from [A13-OLinuXino][1757])
 
Olimex A13-OLinuXino  
---  
[![Olimex-a13-olinuxino-rev e-id.jpg][1760]][1761]  
Manufacturer |  [Olimex][1762]  
Dimensions |  120 _mm_ x 120 _mm_ x 20 _mm_  
Release Date |  August 2012   
Website |  [Product Page][1763]  
Specifications   
SoC |  [A13][1764] @ 1Ghz   
DRAM |  512MiB DDR3 @ 408MHz   
NAND |  4GB (Optional)   
Power |  DC 6V-16V (1A @ 6V)   
Features   
Video |  VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CTV][1765] \- Optional)   
Storage |  µSD   
USB |  3 USB2.0 Host (GL850G hub), 1 USB2.0 OTG   
Other |  RTC   
Headers |  UART, JTAG, Li-Po battery connector, LCD. UEXT, 2x GPIO expansions ports.   
The A13-Olinuxino was the first Allwinner based development board made by [Olimex][1766]. Like all [Olimex hardware][1766], it is fully [Open Source Hardware][1767]. 
## Contents
  * [1 Identification][1768]
  * [2 Sunxi support][1769]
    * [2.1 Current status][1770]
    * [2.2 Images][1771]
    * [2.3 HW-Pack][1772]
    * [2.4 BSP][1773]
    * [2.5 Manual build][1774]
    * [2.6 Mainline kernel][1775]
  * [3 Tips, Tricks, Caveats][1776]
    * [3.1 FEL mode][1777]
    * [3.2 Power Supply Voltage][1778]
    * [3.3 VGA][1779]
    * [3.4 LCD modules][1780]
    * [3.5 Expansion ports][1781]
  * [4 Adding a serial port][1782]
  * [5 Pictures][1783]
  * [6 Also known as][1784]
  * [7 See also][1785]

# Identification
It says "A13-OLinuXino" on the top. It just doesn't get easier than that! 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "A13-OLinuXino" target.
  * The .fex file can be found in sunxi-boards as [a13-olinuxino.fex][1786]

Everything else is the same as the [manual build howto][1787]. 
## Mainline kernel
Use the sun5i-a13-olinuxino.dts device-tree file for the [mainline kernel][1788]. 
# Tips, Tricks, Caveats
## FEL mode
The Home button triggers [ FEL mode][1789]. 
## Power Supply Voltage
**Warning, while you can boot this board at 5V it really is preferable to boot this board at 6V.**
For instance, enabling the backlight on the 7" LCD module will immediately hardlock the board at 5V, while at 6V it is perfectly stable. 
## VGA
Even though the [A13][1764] does not provide DACs itself, the A13-Olinuxino has a VGA connector. 
This is implemented through 3 separate DAC chips (NXP LVC244A) which are connected to the LCD0 lines. This in turn means that you cannot use an LCD and a VGA monitor at the same time, but this is ok as the [A13][1764] can only drive one display at a time anyway. 
Due to the bandwidth limitations of the A13 SoC, the best resolution you can hope for is 800x600. 
## LCD modules
You can attach [several Olimex LCD modules][1790] to the [LCD connector (LCD_CON)][1791]. 
## Expansion ports
Several expansion options are provided: 
  * [A UEXT connector][1792]. This is meant for attaching [Olimex UEXT modules][1793].
  * [A 10 pin IO connector (GPIO-1)][1794].
  * [A 40 pin IO connector (GPIO-2)][1795].

# Adding a serial port
[![][1796]][1797]
[][1798]
Revision C and up UART pads
The earlier revisions of the A13-OLinuXino (Revisions A and B) had a separate UART1 connector which shared lines with the SD connector. You had to use the UART lines on the [UEXT connector][1792], to be able to use an SD card as well as serial. 
From revision C onwards, there is the unpopulated UART0 connector, which shares those same lines with the SD Card lines. There is also a populated UART1 connector, which is standalone. 
For a connector pin-out, the easiest way is to refer to the pin descriptions on the back of the board. Simply attach your leads according to our [UART howto][1799]. 
# Pictures
  * [![][1800]][1801]
Early board, front. 
  * [![][1802]][1803]
Early board, back. 
  * [![][1804]][1805]
Later board, front. 
  * [![][1806]][1807]
Later board, back. 

# Also known as
There are no rebadgers for this type of device. 
# See also
  * [Olimex A13-OLinuXino-Micro][1808]: a cut-down, cheaper version of this board.
  * [Other Olimex hardware][1766]
  * [User manual][1809]
  * [Olimex github repository with all CAD files and schematics.][1810]
