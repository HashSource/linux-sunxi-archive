# Lctech Pi F1C200s
Lctech Pi F1C200s  
---  
[![Lctech Pi F1C200s side.jpg][30313]][30314]  
Manufacturer |  [Shenzen LC Technology][30315]  
Dimensions |  76 _mm_ x 38 _mm_ x 5 _mm_  
Release Date |  2021?   
Website |  [Device Product Page][30316]  
Specifications   
SoC |  [F1C200s][30317] @ 408 Mhz   
DRAM |  64MiB DDR1 @ 156 MHz   
NAND |  128 MiB SPI-NAND   
Power |  DC 5V via USB-C, GPIO   
Features   
Video |  RGB LCD FPC connector   
Audio |  on-board microphone, mono class-D amp (two pins)   
Network |  none, but WiFi through SDIO possible   
Storage |  µSD, SPI-NAND   
USB |  1 USB2.0 Type-C OTG   
Headers |  RGB LCD 40pin FPC, Touch 6pin FPC(I2C), MIPI CSI camera 24pin FPC, USB-Type C UART, unsoldered GPIO header pins   
This page needs to be properly filled according to the [New Device Howto][30318] and the [New Device Page guide][30319].
A comparably small development board (though larger than most other F1Cx00s boards), with two USB Type-C ports. 
## Contents
  * [1 Identification][30320]
  * [2 Sunxi support][30321]
    * [2.1 Current status][30322]
    * [2.2 Images][30323]
    * [2.3 Manual build][30324]
      * [2.3.1 Mainline U-Boot][30325]
      * [2.3.2 Mainline Linux Kernel][30326]
  * [3 Expansion ports][30327]
  * [4 Tips, Tricks, Caveats][30328]
    * [4.1 FEL mode][30329]
  * [5 Serial port][30330]
  * [6 Pictures][30331]
  * [7 Schematic][30332]
  * [8 Also known as][30333]
  * [9 See also][30334]
    * [9.1 Manufacturer images][30335]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Lctech Pi F1c200s v1.1
        (303F1C200S1)
      www.lctech-inc.com
[/code]
Older versions are marketed as CherryPi, with a cherry logo silkscreened on the top. Newer revisions (v1.1) have no logo, just the "Lctech Pi F1C200s" name. All share the (now defunct) "www.lctech-inc.com" URL. Nothing is printed naming-wise on the back. 
# Sunxi support
## Current status
Mostly covered by the generic F1C100s support in both Linux and U-Boot. The DT is in the Linux kernel repository starting from v6.4-rc1. 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][30334]. If no sunxi based images are available, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][30336] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _lctech_pi_f1c200s_defconfig_ build target. Available since U-Boot v2023.07. 
### Mainline Linux Kernel
Use the _suniv-f1c200s-lctech-pi.dts_ devicetree binary, merged into and available since Linux v6.4-rc1. Earlier kernels work if fed the proper DTB from U-Boot. 
# Expansion ports
The board features two single-line rows of header pins, which are not populated. The shorter header on the right hand side has the first 12 pins from PortE, but no Vcc or GND pin: 
digital header   
---  
1 | PE0 | UART0-RX | I2C2-SCK   
2 | PE1 | UART0-TX | I2C2-SDA   
3 | PE2 | GPIO-130 | CLK-OUT   
4 | PE3 | GPIO-131 | RSB-SCK   
5 | PE4 | GPIO-132 | RSB-SDA   
6 | PE5 | GPIO-133 | __  
7 | PE6 | GPIO-134 | PWM1   
8 | PE7 | SPI1-CS | UART2-TX   
9 | PE8 | SPI1-MOSI | UART2-RX   
10 | PE9 | SPI1-CLK | UART2-RTS   
11 | PE10 | SPI1-MISO | UART2-CTS   
12 | PE11 | IR-RX | CLK-OUT   
The longer header on the other side provides both 5V and 3.3V (plus the only GND pin), a few digital signals, but also many analogue ones: 
analogue header   
---  
1 | __|  5V | __  
2 | PD12 | I2C0-SCK | __  
3 | PD0 | I2C0-SDA | __  
4 | __|  GND | __  
5 | __|  RST | __  
6 | __|  3.3V | __  
7 | PA3 | SPI1-MISO | UART1-TX, GPIO-3   
8 | PA2 | SPI1-CLK | UART1-RX, GPIO-2   
9 | PA1 | SPI1-MOSI | UART1-CTS, GPIO-1   
10 | PA0 | SPI1-CS | UART1-RTX, GPIO-0   
11 | __|  A-GND | __  
12 | __|  TV-OUT | __  
13 | __|  LRADC | key resistor network   
14 | __|  FMINL | (Line-In)   
15 | __|  FMINR | (Line-In)   
16 | __|  OUT- | (from amplifier)   
17 | __|  OUT+ | (from amplifier)   
18 | __|  HPCOM | (Headphone)   
# Tips, Tricks, Caveats
## FEL mode
The **BOOT** button connects the SPI0_MISO pin to GND, thus preventing SPI-NAND boot. If no SD card is inserted, this triggers FEL mode. 
# Serial port
The device features a CH340 compatible USB to serial adapter chip, which connects the SoC's PortA UART1 pins (PA2, PA3) to an USB Type-C connector. So serial console just requires a USB cable. 
# Pictures
  * [![Lctech Pi F1C200s side.jpg][30337]][30314]
  * [![Lctech Pi F1C200s top.jpg][30338]][30339]
  * [![Lctech Pi F1C200s USB-C.JPG][30340]][30341]
  * [![Lctech Pi F1C200s bottom.JPG][30342]][30343]

# Schematic
[File:CherryPi-F1C200S.pdf][30344]
# Also known as
Initially this device seemed to have been sold under the Cherry Pi brand name, from the same manufacturer. Newer versions and the current website just use the "Lctech Pi" name now. 
# See also
[CNX-Software article][30345]
## Manufacturer images
