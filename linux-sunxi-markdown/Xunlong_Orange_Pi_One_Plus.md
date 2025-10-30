# Xunlong Orange Pi One Plus
Xunlong Orange Pi One Plus  
---  
[![Orange pi one plus top.jpg][61634]][61635]  
Manufacturer |  [OrangePi][61636]  
Dimensions |  68 _mm_ x 48 _mm_  
Release Date |  December 2017   
Website |  [Device Product Page][61637]  
Specifications   
SoC |  [H6][61638] @ 1.8 Ghz   
DRAM |  1GiB LPDDR3 @ xxxMHz   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive), Micro USB (5V @ 2A) OTG power supply, or via GPIO header pins   
Features   
Video |  HDMI (Type 2.0A - full)   
Audio |  HDMI, on-board microphone   
Network |  10/100/1000Mbps Ethernet (Realtek RTL8211)   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Other |  IRDA   
Headers |  UART, JTAG, LCD, VGA  
This page needs to be properly filled according to the [New Device Howto][61639] and the [New Device Page guide][61640].
_The Orange Pi One Plus is a 64-bit_[H6][61638] _based single board computer by[Xunlong][61641]._
The Orange Pi One Plus is an upgrade from the previous [Orange Pi One][61642]. It uses the new Allwinner [H6][61638] SoC. In comparison to Orange Pi One, this board has Quad Core Arm Cortex-A53 cpu. The SoC also has 4k capabilities at 60fps due to it's Mali T720 GPU. 
In comparison to DDR3 RAM present in most SBCs, the One Plus uses 1GiB of LPDDR3 RAM. The board has 1 USB 2.0 port, Gigabit Ethernet, Pi Compatible GPIO header, OTG, etc. 
The [H6][61638] support USB 3.0 but the board doesn't got it implemented. However, it's cousin, [Orange Pi Lite 2][61643] have one. 
## Contents
  * [1 Identification][61644]
  * [2 Sunxi support][61645]
    * [2.1 Current status][61646]
    * [2.2 Manual build][61647]
      * [2.2.1 Mainline U-Boot][61648]
      * [2.2.2 Linux Kernel][61649]
        * [2.2.2.1 Sunxi/Legacy Kernel][61650]
        * [2.2.2.2 Mainline kernel][61651]
  * [3 Expansion Port][61652]
  * [4 Tips, Tricks, Caveats][61653]
    * [4.1 FEL mode][61654]
  * [5 Adding a serial port][61655]
  * [6 Pictures][61656]
  * [7 Also known as][61657]
  * [8 See also][61658]
    * [8.1 Manufacturer images][61659]

# Identification
_The One Plus has a black-colored pcb, different from it's[older brother][61642]._
On the top of the device, the following is printed: 
[code] 
    Orange Pi
    ONE PLUS
[/code]
The PCB has the following silkscreened on it: 
[code] 
    V2.0
[/code]
Some boards have the following instead: 
[code] 
    V3.0
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _molly_
  * Build Number: _petrel_fvd_p1-eng 7.0 NRD91N 20180110 test-keys_

# Sunxi support
## Current status
Supported in both mainline U-Boot and Linux. 
## Manual build
You can build things for yourself by following our [ Manual build howto][61660] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the **orangepi_one_plus_defconfig** (supported since v2018.09) build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_orangepi_one_plus.fex_][61661] file. This was extracted from the android sdcard image. 
#### Mainline kernel
Use the **sun50i-h6-orangepi-one-plus.dtb** device-tree binary. 
# Expansion Port
The Orange Pi One Plus has a 26-pin, 0.1" connector with several low-speed interfaces. To learn about accessing the GPIO pins through sysfs with mainline kernel read [GPIO][61662]  

2x13 Header   
---  
1 | _3.3V_ | 2 | _5V_  
3 | PH06 (TWI1_SDA/SPI1_MISO/OWA_IN/PH_EINT6) | 4 | _5V_  
5 | PH05 (TWI1_SCK/SPI1_MOSI/OWA_MCLK/PH_EINT5) | 6 | _GND_  
7 | PH04 (PWM1/SPI1_CLK/PH_EINT4) | 8 | PD21 (UART2_RTS)  
9 | _GND_ | 10 | PD22 (PWM0/UART2_CTS)  
11 | PD24 (TWI2_SDA/UART3_RX) | 12 | PC09   
13 | PD23 (TWI2_SCK/UART3_TX) | 14 | _GND_  
15 | PD26 (UART3_CTS) | 16 | PC08   
17 | _3.3V_ | 18 | PC07 (SPI0_WP)  
19 | PC02 (SPI0_MOSI) | 20 | _GND_  
21 | PC03 (SPI0_MISO) | 22 | PD25 (UART3_RTS)  
23 | PC00 (SPI0_CLK) | 24 | PC05 (SPI0_CS0)  
25 | _GND_ | 26 | PH03 (SPI1_CS/PH_EINT3)  
# Tips, Tricks, Caveats
## FEL mode
Booting without an SD card automagically enters FEL mode. 
[code] 
    ./sunxi-fel version
    AWUSBFEX soc=00001728(H6) 00000001 ver=0001 44 08 scratchpad=00027e00 00000000 00000000
[/code]
The H6 UBOOT pin is routed to test-point TP28 on the PCB. 
# Adding a serial port
[![Orange Pi One Plus UART pins][61663]][61664]
This device has a three pin UART header as shown in the picture. On the underside of the board, TX, RX, and GND are marked. Wires should be attached as described [Here][61665]
# Pictures
  * [![Orange pi one plus top.jpg][61666]][61635]
  * [![Orange pi one plus bottom.jpg][61667]][61668]
  * [![Orange pi one plus side.jpg][61669]][61670]

# Also known as
There are currently no known rebadged devices. Update this section if you know otherwise. 
# See also
  * AXP805 Datasheet: [File:AXP805 Datasheet V1.0 en.pdf][61671]
  * H6 Datasheet: [File:Allwinner H6 V200 Datasheet V1.1.pdf][61672]
  * H6 User Manual: [File:Allwinner H6 V200 User Manual V1.1.pdf][61673]
  * Schematics 2.0: [File:OrangePi OnePlus Schematics v2.0.pdf][61674]

## Manufacturer images
  * <http://www.orangepi.org/downloadresources/>
