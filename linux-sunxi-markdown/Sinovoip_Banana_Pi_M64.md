# Sinovoip Banana Pi M64
Banana Pi M64 Ultra is a [A64][50662] based development board produced by Sinovoip. 
**Despite its name, the M64 is incompatible to previous Banana Pi boards ([Banana Pi][50663]/[M1][50664]/[M1+][50665]/[Pro][50666]/[M2][50667]/M2+/M3), due to a different SoC - requiring different boot loaders and drivers.** It's another attempt to cash in on the Banana Pi's popularity with a SBC only sharing brand, name, ~~form factor~~ and GPIO header. 
  

Sinovoip Banana Pi M64  
---  
[![BananaPi M64 front1.jpg][50668]][50669]  
Manufacturer |  [Sinovoip][50670]  
Dimensions |  92 _mm_ x 60 _mm_ x 20 _mm_  
Release Date |  July 2016   
Website |  [M64 product page][50671]  
Specifications   
SoC |  [A64][50662] @ 1152 Mhz   
DRAM |  2GiB DDR3 @ 672 MHz ([SKhynix H5TQ4G83AFR][50672] x4)   
NAND |  8 GB eMMC (Samsung KLM8G1WEPD-B031)   
Power |  DC 5V @ 2A (4/1.7mm barrel plug), Li-Ion battery connector   
Features   
Video |  HDMI Type A - full size   
Audio |  3.5mm headphone plug, HDMI, internal microphone   
Network |  WiFi 802.11 b/g/n ([Ampak AP6212][50673]), 10/100/1000Mbps Ethernet ([Realtek 8211E][50674])   
Storage |  µSD, eMMC 5.0   
USB |  2 USB2.0 Host via Terminus Technology 4-Port hub, 1 USB2.0 OTG (micro-B)   
Other |  IRDA, reset & power button   
## Contents
  * [1 Identification][50675]
  * [2 Sunxi support][50676]
    * [2.1 Current status][50677]
    * [2.2 Images][50678]
    * [2.3 Manual build][50679]
      * [2.3.1 U-Boot][50680]
        * [2.3.1.1 Mainline U-Boot][50681]
      * [2.3.2 Linux Kernel][50682]
        * [2.3.2.1 Mainline kernel][50683]
  * [3 Expansion Port][50684]
  * [4 Tips, Tricks, Caveats][50685]
    * [4.1 FEL mode][50686]
    * [4.2 USB][50687]
    * [4.3 ESD & over-current protections][50688]
  * [5 Adding a serial port][50689]
  * [6 Pictures][50690]
  * [7 See also][50691]
    * [7.1 Manufacturer images][50692]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    BPi-M64
    v1.0
[/code]
alongside with the BananaPi (Bpi) logo. 
# Sunxi support
## Current status
From the software point of view this device is similar to the [Pine64][50693] (similar DRAM, same Ethernet and PMIC), so basic support should work with some Pine64 image. In fact the manufacturer seems to offer Pine64 images based on longsleep's builds. 
## Images
**End Users** : Here are links to current images that are not community supported: 
  * <http://www.banana-pi.org/m64-download.html>
  * <http://forum.banana-pi.org/t/bpi-m64-new-image-bpi-m64-win10iotcore10586-beta0-1/2108>

## Manual build
You can build things for yourself by following our [ Manual build howto][50694] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **bananapi_m64_defconfig** build target. 
### Linux Kernel
#### Mainline kernel
Use the **sun50i-a64-bananapi-m64.dtb** device-tree binary. 
# Expansion Port
The Banana Pi M64 has the usual 40-pin, 0.1" Raspberry Pi 2 compatible connector with several low-speed interfaces. 
2x20 Header   
---  
1 | _3.3V_ | 2 | _5V_  
3 | TWI1_SDA / PH03  | 4 | _5V_  
5 | TWI1_SCK / PH02  | 6 | _GND_  
7 | UART3_RTS / PH06  | 8 | UART2_TX / PB0 / JTAG-MS0   
9 | _GND_ | 10 | UART2_RX / PB1 / JTAG-CK0   
11 | UART3_CTS / PH07  | 12 | UART2_CTS/ PB3 / JTAG-DI0   
13 | DMIC-CLK / PH10  | 14 | _GND_  
15 | DMIC-DIN/ PH11  | 16 | UART2_RTS / PB2 / JTAG-DO0   
17 | _3.3V_ | 18 | PD4   
19 | SPI1_MOSI / PD2  | 20 | _GND_  
21 | SPI1_MISO / PD3  | 22 | PC0 / SPI0-MOSI   
23 | SPI1-CLK / PD1 / UART3-RX  | 24 | SPI1-CS / PD0 / UART3-TX   
25 | _GND_ | 26 | PC2 / SPI0-CLK   
27 | PC4  | 28 | PC3 / SPI0-CS   
29 | PC7  | 30 | _GND_  
31 | PCM0-BCLK / PB5  | 32 | PCM0-DIN / PB7   
33 | PCM0-SYNC / PB4  | 34 | _GND_  
35 | PCM0-DOUT / PB6  | 36 | PL9 / S_TWI-SDA   
37 | PL12  | 38 | PL7   
39 | _GND_ | 40 | PL8 / S_TWI-SCK   
Pin PC1, which carries the SPI0-MISO signal, is not available on a header, since it is connected to the eMMC chip. So booting from a SPI flash connected to header pins will not work on the Banana Pi M64. 
# Tips, Tricks, Caveats
## FEL mode
The FEL button (called U-Boot key in the manual) triggers [ FEL mode][50695]. 
The boot order is: SD card first, then eMMC, then FEL. Pressing the FEL button always triggers FEL mode. A SD card without an eGON header will be skipped, it continues on eMMC then. If boot0 fails to locate U-Boot, it will enter FEL mode. 
## USB
The two type A receptacles are connected to a Terminus Technology Inc. 4-Port hub on the lower PCB side that is connected to the SoC. PCB traces on the board provide a 3rd USB port connected to the hub on solder wholes next to the 40 pin GPIO header ([polarity 'information'][50696]). 
## ESD & over-current protections
Based on the schematic Rev 1.1 (September 18, 2016) the board incorporates the following protections: 
  

Protections x - no protection, ESD - Electrostatic Discharge, OC - Over-current  | Comments   
---|---  
1 | DCIN (power) | x | x | No power supply bypass   
2 | Micro SD | x | x |   
3 | Camera | x | x |   
4 | Dual USB1 | ESD | x |   
5 | Micro USB OTG | ESD | OC | Over-current protection by U8 (unknown value)   
6 | HDMI | ESD | x |   
7 | MIPI-DSI | x | x |   
8 | Ethernet | x | N/A | Over-current protection is not applicable   
9 | GPIO | x | x |   
10 | Debug UART | x | ?   
11 | Audio jack | ESD | N/A | Output current is internally limited by SoC   
# Adding a serial port
[![][50697]][50698]
[][50699]
Banana Pi M64 UART pads
There is a three pin UART header next to the Ethernet socket, it is connected to UART0. The pins are clearly labelled with GND, RX and TX. Attach a 3.3V UART interface as described in the [UART howto][50700]. 
# Pictures
  * [![BananaPi M64 front1.jpg][50701]][50669]
  * [![BananaPi M64 back.jpg][50702]][50703]

# See also
From a software point of view there is not much difference from the [Pine64][50693], which is the main development vehicle for the [A64][50662] SoC support. So please check the [Pine64][50693] page for further information. 
[Banana Pi M64 board schematic][50704]
## Manufacturer images
The official BananaPi M64 page provides already some images, those with Linux based on longsleep's Pine64 images. Be aware that they are based on already outdated BSP kernel/u-boot versions and partially use an ARMv6 userland causing unnecessary performance implications: <http://www.banana-pi.org/m64-download.html>
