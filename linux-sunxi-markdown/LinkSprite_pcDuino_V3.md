# LinkSprite pcDuino3
(Redirected from [LinkSprite pcDuino V3][31875])
 
LinkSprite pcDuino3  
---  
[![Pcd v3 front.jpg][31878]][31879]  
Manufacturer |  [LinkSprite][31880]  
Dimensions |  125 _mm_ x 66 _mm_ x height _mm_  
Release Date |  April 2014   
Website |  [Device Product Page][31881]  
Specifications   
SoC |  [A20][31882] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz   
NAND |  4GB   
Power |  DC 5V @ 2A (micro-USB)   
Features   
Video |  HDMI (Type A, full)   
Audio |  3.5mm headphone plug, HDMI   
Network |  WiFi 802.11bgn (Realtek RTL8188EUS), 10/100Mbps Ethernet (IC+ IP101A)   
Storage |  µSD, SATA   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Other |  IR   
Headers |  UART, LVDS connector, Arduino-compatible headers   
## Contents
  * [1 Identification][31883]
  * [2 Sunxi support][31884]
    * [2.1 Current status][31885]
    * [2.2 Images][31886]
    * [2.3 HW-Pack][31887]
    * [2.4 BSP][31888]
    * [2.5 Manual build][31889]
    * [2.6 Mainline kernel][31890]
  * [3 Tips, Tricks, Caveats][31891]
    * [3.1 FEL mode][31892]
    * [3.2 Expansion headers][31893]
  * [4 Adding a serial port][31894]
  * [5 Pictures][31895]
  * [6 Variants][31896]
  * [7 See also][31897]

# Identification
On the back of the board, it helpfully reads "pcDuino Dual core". 
# Sunxi support
## Current status
Supported. 
There are even patches for [ mainline][31898] on the [Mailing list][31899]. These provide basic board support, along with USB and SATA. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "pcduino3" target.
  * The .fex file can be found in sunxi-boards as [linksprite_pcduino3.fex][31900]

Everything else is the same as the [manual build howto][31901]. 
## Mainline kernel
Use the _sun7i-a20-pcduino3.dts_ device-tree file for the [mainline kernel][31898]. 
In order to make ethernet work for pcDuino3b, you will have to edit the device-tree file: simply copy _& gmac{...}_ section from _sun7i-a20-pcduino3**-nano**.dts_ to _sun7i-a20-pcduino.dts_. 
# Tips, Tricks, Caveats
## FEL mode
The UPGRADE/SW2 button triggers [FEL mode][31902]. 
## Expansion headers
[![][31903]][31904]
[][31905]
pcDuino3b headers
SPI0 pins are wired to both: P7 and J8 pins. SPI0 clock is additionally wired to LED_CLK. 
  

P3 (Debug Port)  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | TX (Square Pad) | [PB23][31906]  
2 | GND |   
3 | RX | [PB22][31906]  
P10  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | GPIO14 | [PH11][31907]  
2 | GPIO15 | [PH12][31907]  
3 | GPIO16 | [PH13][31907]  
4 | GPIO17 | [PH14][31907]  
pcDuino name | Sunxi name   
---|---  
LED  LED 1 - Power LED |   
LED 2 - Wifi LED |   
LED RX | [PH15][31907]  
LED RX | [PH16][31907]  
LED CLK / SPI0_CLK / GPIO13 | [PI11][31908]  
SW  pcDuino name | Sunxi name   
---|---  
SW1 - Reset |   
SW2 - Upgrade | [FEL mode][31902]  
SW3 - BACK | [PH17][31907]  
SW4 - HOME | [PH18][31907]  
SW5 - MENU | [PH19][31907]  
P6  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | SPI1_MISO / GPIO12 | [PC22][31909]  
2 | +5V DC / SPI1 GPIO20 / GPIO20 | [PC19][31909]  
3 | SPI1_CLK / GPIO13 | [PC20][31909]  
4 | SPI1_MOSI / GPIO11 / PWM11 | [PC21][31909]  
5 | RESET |   
6 | GND |   
P7  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | SPI0_MISO / GPIO12 | [PI13][31908]  
2 | +5V DC |   
3 | SPI0_CLK / GPIO13 | [PI11][31908]  
4 | SPI0_MOSI / GPIO11 / PWM11 | [PI12][31908]  
5 | RESET |   
6 | GND |   
J12  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | A0 |   
2 | A1 |   
3 | A2 |   
4 | A3 |   
5 | A4 |   
6 | A5 |   
J11  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | GPIO0 / UART2_RX | [PI19][31908]  
2 | GPIO1 / UART2_TX | [PI18][31908]  
3 | GPIO2 | [PH7][31907]  
4 | GPIO3 / PWM3 | [PH6][31907]  
5 | GPIO4 | [PH8][31907]  
6 | GPIO5 / PWM5 | [PB2][31906]  
7 | GPIO6 / PWM6 | [PI3][31908]  
8 | GPIO7 | [PH9][31907]  
J9  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | not connected |   
2 | IOREF |   
3 | RESET |   
4 | 3.3V DC output |   
5 | 5V DC output |   
6 | GND |   
7 | GND |   
8 | +5V in |   
J8  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | GPIO8 | [PH10][31907]  
2 | GPIO9 / PWM9 | [PH5][31907]  
3 | SPI0_SS / GPIO10 / PWM10 | [PI10][31908]  
4 | SPI0_MOSI / GPIO11 / PWM11 | [PI12][31908]  
5 | SPI0_MISO / GPIO12 | [PI13][31908]  
6 | SPI0_CLK / GPIO13 | [PI11][31908]  
7 | GND |   
8 | AREF |   
9 | TWI2_SDA | [PB21][31906]  
10 | TWI2_SCL | [PB20][31907]  
# Adding a serial port
[![][31910]][31911]
[][31912]
UART pads
There is a 3pin 2.54mm pitch header near the wifi module, called "UART_0" (P3 - Debug Port). All you have to do is attach some jumper wires according to our [UART howto][31913]. 
# Pictures
  * [![Pcd v3 front.jpg][31914]][31879]
  * [![Pcd v3 back.jpg][31915]][31916]

# Variants
At some point in 2015, Linksprite started selling an updated variant of the pcDuino V3 called pcDuino v3 _B_ (or pcDuino3B). Compared to the original board, v3B updated the ethernet connection to Gigabit Ethernet. Other than that, the board layout stayed the same. 
# See also
  * [LinkSprite pcDuino][31917]
  * [LinkSprite pcDuino2][31918]
  * [LinkSprite pcDuino3 Nano][31919]
  * [Board schematic.][31920]
