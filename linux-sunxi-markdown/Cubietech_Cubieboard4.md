# Cubietech Cubieboard4
Cubietech Cubieboard4  
---  
[250px][15127]  
Manufacturer |  [Cubietech][15128]  
Dimensions |  111 _mm_ x 111 _mm_  
Release Date |  December 2014   
Website |  [Cubieboard4 Product Page][15129]  
Specifications   
SoC |  [A80][15130] @ 1008Mhz   
DRAM |  2GiB DDR3 @ 672MHz (SK hynix H5TQ4G63AFR-PBC 4Gb * 4)   
NAND |  8GB eMMC (Samsung KLMAG2WEMB-B031)   
Power |  DC 5V @ 4A, optional Li-Ion battery   
Features   
Video |  HDMI (Type A - full), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug   
Network |  WiFi 802.11 b/g/n ([Ampak AP6330][15131]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][15132])   
Storage |  eMMC, µSD   
USB |  4 USB2.0 Host, 1 USB3.0 OTG   
Other |  IRDA, Bluetooth (Ampak AP6330)   
Headers |  UART, JTAG, LiPo Battery, GPIOs   
The Cubieboard4 Board is a development board for the Allwinner [A80][15130] SoC. 
## Contents
  * [1 Identification][15133]
  * [2 Sunxi support][15134]
    * [2.1 Current status][15135]
      * [2.1.1 Sunxi Kernel][15136]
      * [2.1.2 Sunxi U-Boot][15137]
      * [2.1.3 Mainline kernel][15138]
      * [2.1.4 Mainline u-boot][15139]
    * [2.2 Images][15140]
    * [2.3 HW-Pack][15141]
    * [2.4 BSP][15142]
    * [2.5 Manual build][15143]
    * [2.6 Mainline kernel][15144]
  * [3 Tips, Tricks, Caveats][15145]
    * [3.1 FEL mode][15146]
  * [4 Expansion Ports][15147]
    * [4.1 GPIO Connector][15148]
  * [5 Serial console port][15149]
  * [6 Pictures][15150]
  * [7 Also known as][15151]
  * [8 See also][15152]
    * [8.1 Manufacturer images][15153]

# Identification
The board has a Cubietech logo, the names "Cubietech", and "CC-A80", just above the WiFi antenna. 
# Sunxi support
## Current status
### Sunxi Kernel
Like all [A80][15130] based devices, there is no support in our sunxi kernel. 
### Sunxi U-Boot
Like all [A80][15130] based devices, there is no support in u-boot-sunxi. 
### Mainline kernel
Mainline kernel support is queued up for 4.2. Currently only MMC and UARTs are supported. 
Use the sun9i-a80-cubieboard4.dtb device-tree file for the [mainline kernel][15154]. 
### Mainline u-boot
Use the _Cubieboard4_defconfig_ build target. 
## Images
## HW-Pack
## BSP
## Manual build
Follow [SDK build howto][15155] to build u-boot and the kernel from the SDK. 
## Mainline kernel
Initial support for the A80 based on the Cubieboard 4 board is being worked on. 
Use the _sun9i-a80-cubieboard4.dtb_ device-tree file for the [mainline kernel][15154]. 
# Tips, Tricks, Caveats
## FEL mode
There is no FEL mode button on this board. 
Instead you can enter fel mode from [U-Boot][15156]. While U-Boot is starting, type CTRL+C to interrupt it. At the prompt type _efex_ to enter fel mode. 
If booting fails entirely then FEL mode can be entered by shorting pin 29-30 on the nand/emmc with a suitable metal object (tweezer or the like), by vendor official procedure. 
# Expansion Ports
The Cubieboard4 board exposes a 2 mm pitch connector for GPIO. 
## GPIO Connector
The pinout is printed on the board: 
SECTION NOT UPDATED YET
2x16 GPIO Header   
---  
1 | GPIO-ADC0  | 2 | GPIO-PL0-CPUS-TX   
3 | GPIO-ADC1  | 4 | GPIO-PL1-CPUS-RX   
5 | _GND_ | 6 | _GPIO-3V_  
7 | GPIO-HSIC-STRB  | 8 | _GND_  
9 | _GND_ | 10 | GPIO-PH6-PWM0   
11 | GPIO-HSIC-DATA  | 12 | _GND_  
13 | _GND_ | 14 | GPIO-PH14-SPI3-CLK   
15 | GPIO-PL7-1WIRE  | 16 | GPIO-PH15-SPI3-MOSI   
17 | GPIO-PM0  | 18 | GPIO-PH16-SPI3-MISO   
19 | GPIO-PM1  | 20 | GPIO-PH17-SPI3-CS0   
21 | GPIO-PM2  | 22 | GPIO-PG10-TWI3-SCK   
23 | GPIO-PM3  | 24 | GPIO-PG11-TWI3-SDA   
25 | GPIO-PM4  | 26 | GPIO-PG12-UART4-TX   
27 | GPIO-PM8  | 28 | GPIO-PG13-UART4-RX   
29 | GPIO-PM9  | 30 | GPIO-PG14-UART4-RTS   
31 | GPIO-PH2  | 32 | GPIO-PG15-UART4-CTS   
# Serial console port
[File:Cubieboard4 uart.jpg][15157]
UART header
The UART header is next to the VGA port. Pinout is printed in small font next to the header. 
1x4 UART Header   
---  
1 | GPIO-PH12-UART0-TX   
2 | GPIO-PH13-UART0-RX   
3 | NC   
4 | GND   
# Pictures
Will be uploaded later
  * Cubieboard4 front.jpg
  * Cubieboard4 back.jpg
  * Cubieboard4 board front.JPG
  * Cubieboard4 Board features.jpg

# Also known as
Cubietech also uses the name "CC-A80", both printed on the board and on their websites, for this board. 
# See also
[Cubieboard4 tutorials][15158]
## Manufacturer images
Cubietech provides firmware images on their "[Cubieboard Docs][15158]" website.
