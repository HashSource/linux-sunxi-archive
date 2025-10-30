# Olimex A13-OLinuXino
(Redirected from [A13-Olinuxino][1847])
 
Olimex A13-OLinuXino  
---  
[![Olimex-a13-olinuxino-rev e-id.jpg][1850]][1851]  
Manufacturer |  [Olimex][1852]  
Dimensions |  120 _mm_ x 120 _mm_ x 20 _mm_  
Release Date |  August 2012   
Website |  [Product Page][1853]  
Specifications   
SoC |  [A13][1854] @ 1Ghz   
DRAM |  512MiB DDR3 @ 408MHz   
NAND |  4GB (Optional)   
Power |  DC 6V-16V (1A @ 6V)   
Features   
Video |  VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CTV][1855] \- Optional)   
Storage |  µSD   
USB |  3 USB2.0 Host (GL850G hub), 1 USB2.0 OTG   
Other |  RTC   
Headers |  UART, JTAG, Li-Po battery connector, LCD. UEXT, 2x GPIO expansions ports.   
The A13-Olinuxino was the first Allwinner based development board made by [Olimex][1856]. Like all [Olimex hardware][1856], it is fully [Open Source Hardware][1857]. 
## Contents
  * [1 Identification][1858]
  * [2 Sunxi support][1859]
    * [2.1 Current status][1860]
    * [2.2 Images][1861]
    * [2.3 HW-Pack][1862]
    * [2.4 BSP][1863]
    * [2.5 Manual build][1864]
    * [2.6 Mainline kernel][1865]
  * [3 Tips, Tricks, Caveats][1866]
    * [3.1 FEL mode][1867]
    * [3.2 Power Supply Voltage][1868]
    * [3.3 VGA][1869]
    * [3.4 LCD modules][1870]
    * [3.5 Expansion ports][1871]
  * [4 Adding a serial port][1872]
  * [5 Pictures][1873]
  * [6 Also known as][1874]
  * [7 See also][1875]

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
  * The .fex file can be found in sunxi-boards as [a13-olinuxino.fex][1876]

Everything else is the same as the [manual build howto][1877]. 
## Mainline kernel
Use the sun5i-a13-olinuxino.dts device-tree file for the [mainline kernel][1878]. 
# Tips, Tricks, Caveats
## FEL mode
The Home button triggers [ FEL mode][1879]. 
## Power Supply Voltage
**Warning, while you can boot this board at 5V it really is preferable to boot this board at 6V.**
For instance, enabling the backlight on the 7" LCD module will immediately hardlock the board at 5V, while at 6V it is perfectly stable. 
## VGA
Even though the [A13][1854] does not provide DACs itself, the A13-Olinuxino has a VGA connector. 
This is implemented through 3 separate DAC chips (NXP LVC244A) which are connected to the LCD0 lines. This in turn means that you cannot use an LCD and a VGA monitor at the same time, but this is ok as the [A13][1854] can only drive one display at a time anyway. 
Due to the bandwidth limitations of the A13 SoC, the best resolution you can hope for is 800x600. 
## LCD modules
You can attach [several Olimex LCD modules][1880] to the [LCD connector (LCD_CON)][1881]. 
## Expansion ports
Several expansion options are provided: 
  * [A UEXT connector][1882]. This is meant for attaching [Olimex UEXT modules][1883].
  * [A 10 pin IO connector (GPIO-1)][1884].
  * [A 40 pin IO connector (GPIO-2)][1885].

# Adding a serial port
[![][1886]][1887]
[][1888]
Revision C and up UART pads
The earlier revisions of the A13-OLinuXino (Revisions A and B) had a separate UART1 connector which shared lines with the SD connector. You had to use the UART lines on the [UEXT connector][1882], to be able to use an SD card as well as serial. 
From revision C onwards, there is the unpopulated UART0 connector, which shares those same lines with the SD Card lines. There is also a populated UART1 connector, which is standalone. 
For a connector pin-out, the easiest way is to refer to the pin descriptions on the back of the board. Simply attach your leads according to our [UART howto][1889]. 
# Pictures
  * [![][1890]][1891]
Early board, front. 
  * [![][1892]][1893]
Early board, back. 
  * [![][1894]][1895]
Later board, front. 
  * [![][1896]][1897]
Later board, back. 

# Also known as
There are no rebadgers for this type of device. 
# See also
  * [Olimex A13-OLinuXino-Micro][1898]: a cut-down, cheaper version of this board.
  * [Other Olimex hardware][1856]
  * [User manual][1899]
  * [Olimex github repository with all CAD files and schematics.][1900]
