# Merrii A80 Optimus Board
Merrii A80 Optimus Board  
---  
[![A80 Optimus front.jpg][37657]][37658]  
Manufacturer |  [Merrii][37659]  
Dimensions |  135 _mm_ x 70 _mm_  
Release Date |  August 2014   
Website |  [Device Product Page][37660]  
Specifications   
SoC |  [A80][37661] @ 1008Mhz   
DRAM |  2GiB DDR3 @ 672MHz (SK hynix H5TQ4G63AFR-PBC 4Gb * 4)   
NAND |  16GB eMMC (Samsung KLMAG2WEMB-B031)   
Power |  DC 5V @ 3A, optional Li-Ion battery   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug   
Network |  WiFi 802.11 b/g/n ([Ampak AP6330][37662]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][37663])   
Storage |  eMMC, µSD   
USB |  2 USB2.0 Host, 1 USB3.0 OTG   
Other |  IRDA, Bluetooth (Ampak AP6330)   
Headers |  UART, JTAG, LiPo Battery, Camera interface, GPIOs   
The A80 Optimus Board is a official development board for the Allwinner [A80][37661] SoC, targeting both developers and consumers. 
## Contents
  * [1 Identification][37664]
  * [2 Sunxi support][37665]
    * [2.1 Current status][37666]
      * [2.1.1 Sunxi Kernel][37667]
      * [2.1.2 Sunxi U-Boot][37668]
      * [2.1.3 Mainline kernel][37669]
      * [2.1.4 Mainline u-boot][37670]
    * [2.2 Images][37671]
    * [2.3 HW-Pack][37672]
    * [2.4 BSP][37673]
    * [2.5 Manual build][37674]
    * [2.6 Mainline kernel][37675]
  * [3 Tips, Tricks, Caveats][37676]
    * [3.1 FEL mode][37677]
  * [4 Expansion Ports][37678]
    * [4.1 GPIO Connector][37679]
    * [4.2 Camera/MIPI connector][37680]
  * [5 JTAG][37681]
  * [6 Serial console port][37682]
  * [7 Pictures][37683]
  * [8 See also][37684]
    * [8.1 Manufacturer images][37685]

# Identification
The board has a clearly recognizable Allwinner logo, the name "Allwinner Tech", and "OPTIMUS BOARD", all uppercase, in the lower right hand corner. 
# Sunxi support
## Current status
### Sunxi Kernel
Like all [A80][37661] based devices, there is no support in our sunxi kernel. 
### Sunxi U-Boot
Like all [A80][37661] based devices, there is no support in u-boot-sunxi. 
### Mainline kernel
Mainline kernel support is queued up for 3.19. Currently only UARTs are supported. 
Use the sun9i-a80-optimus.dtb device-tree file for the [mainline kernel][37686]. 
### Mainline u-boot
Like all [A80][37661] based devices, there is no support in mainline u-boot. 
## Images
## HW-Pack
## BSP
## Manual build
Follow [SDK build howto][37687] to build u-boot and the kernel from the SDK. 
## Mainline kernel
Initial support for the A80 based on the A80 Optimus board is being worked on. 
Use the sun9i-a80-optimus.dtb device-tree file for the [mainline kernel][37686]. 
# Tips, Tricks, Caveats
## FEL mode
There is no FEL mode button on this board. 
Instead you can enter fel mode from [U-Boot][37688]. While U-Boot is starting, type CTRL+C to interrupt it. At the prompt type _efex_ to enter fel mode. 
If booting fails entirely then FEL mode can be entered by shorting pin 29-30 on the nand/emmc with a suitable metal object (tweezer or the like), by vendor official procedure. 
# Expansion Ports
The A80 Optimus board exposes a 2 mm pitch connector for GPIO, and a Camera/MIPI connector [connector details needed]. 
## GPIO Connector
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
## Camera/MIPI connector
2x17 MIPI Camera Header   
---  
1 | GND  | 2 | AFVCC-CAM   
3 | MIPI-CSI2-CLKP  | 4 | AFVCC-CAM   
5 | MIPI-CSI2-CLKN  | 6 | DVDD-CAM   
7 | GND  | 8 | VCC-IO-CAM   
9 | MIPI-CSI2-D2P  | 10 | NC   
11 | MIPI-CSI2-D2N  | 12 | MIPI-CSI2-MCLK   
13 | GND  | 14 | NC   
15 | MIPI-CSI2-D0P  | 16 | NC   
17 | MIPI-CSI2-D0N  | 18 | MIPI-CSI-SCK   
19 | GND  | 20 | MIPI-CSI-SDA   
21 | MIPI-CSI2-D3P  | 22 | MIPI-CSI-RESET   
23 | MIPI-CSI2-D3N  | 24 | MIPI-CSI-PWDN   
25 | GND  | 26 | NC   
27 | MIPI-CSI2-D1P  | 28 | GND   
29 | MIPI-CSI2-D1N  | 30 | NC   
31 | GND  | 32 | GND   
33 | GND  | 34 | GND   
# JTAG
The board have a dedicated JTAG port with 2mm pinspacing. 
2x7 JTAG Header   
---  
1 | VCC-PH  | 2 | GND   
3 | NC  | 4 | GND   
5 | CPUB-TDI  | 6 | GND   
7 | CPUB-TMS  | 8 | GND   
9 | CPUB-TCK  | 10 | GND   
11 | CPUB-TDO  | 12 | NC   
13 | VCC-PH  | 14 | GND   
  

# Serial console port
[![][37689]][37690]
[][37691]
UART header
The UART header is next to the Ethernet port. The board comes with a custom USB UART cable that fits direclty into the header. 
1x5 UART Header   
---  
1 | GND   
2 | GND   
3 | VCC-PH   
4 | GPIO-PH13-UART0-RX   
5 | GPIO-PH12-UART0-TX   
# Pictures
  * [![A80 Optimus front.jpg][37692]][37658]
  * [![A80 Optimus back.jpg][37693]][37694]
  * [![A80 optimus board front.JPG][37695]][37696]
  * [![A80 Optimus Board features.jpg][37697]][37698]

# See also
  * [Pcduino8 A80 Board][37699]: this board has a very similar layout and is probably closely related.

## Manufacturer images
Merrii provides firmware images for hardware owners, currently through their customer support.
