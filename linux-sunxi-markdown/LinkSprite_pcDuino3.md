# LinkSprite pcDuino3
LinkSprite pcDuino3  
---  
[![Pcd v3 front.jpg][31336]][31337]  
Manufacturer |  [LinkSprite][31338]  
Dimensions |  125 _mm_ x 66 _mm_ x height _mm_  
Release Date |  April 2014   
Website |  [Device Product Page][31339]  
Specifications   
SoC |  [A20][31340] @ 1Ghz   
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
  * [1 Identification][31341]
  * [2 Sunxi support][31342]
    * [2.1 Current status][31343]
    * [2.2 Images][31344]
    * [2.3 HW-Pack][31345]
    * [2.4 BSP][31346]
    * [2.5 Manual build][31347]
    * [2.6 Mainline kernel][31348]
  * [3 Tips, Tricks, Caveats][31349]
    * [3.1 FEL mode][31350]
    * [3.2 Expansion headers][31351]
  * [4 Adding a serial port][31352]
  * [5 Pictures][31353]
  * [6 Variants][31354]
  * [7 See also][31355]

# Identification
On the back of the board, it helpfully reads "pcDuino Dual core". 
# Sunxi support
## Current status
Supported. 
There are even patches for [ mainline][31356] on the [Mailing list][31357]. These provide basic board support, along with USB and SATA. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "pcduino3" target.
  * The .fex file can be found in sunxi-boards as [linksprite_pcduino3.fex][31358]

Everything else is the same as the [manual build howto][31359]. 
## Mainline kernel
Use the _sun7i-a20-pcduino3.dts_ device-tree file for the [mainline kernel][31356]. 
In order to make ethernet work for pcDuino3b, you will have to edit the device-tree file: simply copy _& gmac{...}_ section from _sun7i-a20-pcduino3**-nano**.dts_ to _sun7i-a20-pcduino.dts_. 
# Tips, Tricks, Caveats
## FEL mode
The UPGRADE/SW2 button triggers [FEL mode][31360]. 
## Expansion headers
[![][31361]][31362]
[][31363]
pcDuino3b headers
SPI0 pins are wired to both: P7 and J8 pins. SPI0 clock is additionally wired to LED_CLK. 
  

P3 (Debug Port)  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | TX (Square Pad) | [PB23][31364]  
2 | GND |   
3 | RX | [PB22][31364]  
P10  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | GPIO14 | [PH11][31365]  
2 | GPIO15 | [PH12][31365]  
3 | GPIO16 | [PH13][31365]  
4 | GPIO17 | [PH14][31365]  
pcDuino name | Sunxi name   
---|---  
LED  LED 1 - Power LED |   
LED 2 - Wifi LED |   
LED RX | [PH15][31365]  
LED RX | [PH16][31365]  
LED CLK / SPI0_CLK / GPIO13 | [PI11][31366]  
SW  pcDuino name | Sunxi name   
---|---  
SW1 - Reset |   
SW2 - Upgrade | [FEL mode][31360]  
SW3 - BACK | [PH17][31365]  
SW4 - HOME | [PH18][31365]  
SW5 - MENU | [PH19][31365]  
P6  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | SPI1_MISO / GPIO12 | [PC22][31367]  
2 | +5V DC / SPI1 GPIO20 / GPIO20 | [PC19][31367]  
3 | SPI1_CLK / GPIO13 | [PC20][31367]  
4 | SPI1_MOSI / GPIO11 / PWM11 | [PC21][31367]  
5 | RESET |   
6 | GND |   
P7  Pin number | pcDuino name | Sunxi name   
---|---|---  
1 | SPI0_MISO / GPIO12 | [PI13][31366]  
2 | +5V DC |   
3 | SPI0_CLK / GPIO13 | [PI11][31366]  
4 | SPI0_MOSI / GPIO11 / PWM11 | [PI12][31366]  
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
1 | GPIO0 / UART2_RX | [PI19][31366]  
2 | GPIO1 / UART2_TX | [PI18][31366]  
3 | GPIO2 | [PH7][31365]  
4 | GPIO3 / PWM3 | [PH6][31365]  
5 | GPIO4 | [PH8][31365]  
6 | GPIO5 / PWM5 | [PB2][31364]  
7 | GPIO6 / PWM6 | [PI3][31366]  
8 | GPIO7 | [PH9][31365]  
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
1 | GPIO8 | [PH10][31365]  
2 | GPIO9 / PWM9 | [PH5][31365]  
3 | SPI0_SS / GPIO10 / PWM10 | [PI10][31366]  
4 | SPI0_MOSI / GPIO11 / PWM11 | [PI12][31366]  
5 | SPI0_MISO / GPIO12 | [PI13][31366]  
6 | SPI0_CLK / GPIO13 | [PI11][31366]  
7 | GND |   
8 | AREF |   
9 | TWI2_SDA | [PB21][31364]  
10 | TWI2_SCL | [PB20][31365]  
# Adding a serial port
[![][31368]][31369]
[][31370]
UART pads
There is a 3pin 2.54mm pitch header near the wifi module, called "UART_0" (P3 - Debug Port). All you have to do is attach some jumper wires according to our [UART howto][31371]. 
# Pictures
  * [![Pcd v3 front.jpg][31372]][31337]
  * [![Pcd v3 back.jpg][31373]][31374]

# Variants
At some point in 2015, Linksprite started selling an updated variant of the pcDuino V3 called pcDuino v3 _B_ (or pcDuino3B). Compared to the original board, v3B updated the ethernet connection to Gigabit Ethernet. Other than that, the board layout stayed the same. 
# See also
  * [LinkSprite pcDuino][31375]
  * [LinkSprite pcDuino2][31376]
  * [LinkSprite pcDuino3 Nano][31377]
  * [Board schematic.][31378]
