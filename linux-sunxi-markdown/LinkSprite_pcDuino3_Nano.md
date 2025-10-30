# LinkSprite pcDuino3 Nano
LinkSprite pcDuino3 Nano  
---  
[![Linksprite pcduino3 nano general2.JPG][31418]][31419]  
Manufacturer |  [LinkSprite][31420]  
Dimensions |  96 _mm_ x 64 _mm_ x 20 _mm_  
Release Date |  September 2014   
Website |  [Device Product Page][31421]  
Specifications   
SoC |  [A20][31422] @ 1Ghz   
DRAM |  1GiB DDR3 @ 408MHz ([K4B4G1646Q-HYK0][31423])   
NAND |  4GB MLC NAND (H27UBG8T2BTR-BC)   
Power |  DC 5V @ 2A (micro-usb)   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug, HDMI   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][31424])   
Storage |  µSD, SATA   
USB |  2 USB2.0 Host, 1 microUSB2.0 OTG   
Other |  IR   
Headers |  UART, MIPI (camera), Arduino-compatible headers   
The LinkSprite pcDuino v3 Nano is an [A20][31422] development board with Arduino-compatible headers. 
## Contents
  * [1 Identification][31425]
  * [2 Sunxi support][31426]
    * [2.1 Current status][31427]
    * [2.2 Manual build][31428]
      * [2.2.1 U-Boot][31429]
        * [2.2.1.1 Sunxi/Legacy U-Boot][31430]
        * [2.2.1.2 Upstream/Mainline U-Boot][31431]
      * [2.2.2 Linux Kernel][31432]
        * [2.2.2.1 Sunxi/Legacy Kernel][31433]
        * [2.2.2.2 Upstream/Mainline kernel][31434]
  * [3 Tips, Tricks, Caveats][31435]
    * [3.1 SATA power connector][31436]
    * [3.2 FEL mode][31437]
    * [3.3 Expansion Ports][31438]
  * [4 Adding a serial port][31439]
    * [4.1 Locating the UARTs][31440]
  * [5 Pictures][31441]
  * [6 Variants][31442]
  * [7 Also known as][31443]
  * [8 See also][31444]
    * [8.1 Manufacturer images][31445]

# Identification
A white, credit-card-sized PCB with an A20 chip. "PCDUINO_NANO" is marked on the board to the right of the A20. 
# Sunxi support
## Current status
Fully supported by the upstream U-Boot and kernel, and the legacy kernel; it's _not_ supported by the legacy U-Boot. 
## Manual build
You can build things for yourself by following our [ Manual build howto][31446] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Not supported. 
#### Upstream/Mainline U-Boot
Use the _Linksprite_pcDuino3_Nano_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_linksprite_pcduino3_nano.fex_][31447] file. 
#### Upstream/Mainline kernel
Use the _sun7i-a20-pcduino3-nano.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## SATA power connector
The pcDuino3 Nano's SATA power connector uses a JST XH 2.5mm header, and is compatible with the Cubieboard. It's not compatible with the Banana Pi/Pro/M1+ and Orange Pi, where 5V and GND are inverted. 
## FEL mode
The "UBOOT" button triggers [ FEL mode][31448]. 
## Expansion Ports
The pcDuino3 Nano provides Arduino-style 0.1" connectors. 
[![][31449]][31450]
[][31451]
An Arduino breadboard shield that interferes with the USB0 connector
Not all Arduino shields will be compatible with this board, for several reasons: 
  * The GPIOs operate at 3.3V rather than 5V.
  * The analogue input pins on a real Arduino can also be configured as GPIOs; here they can only be inputs.
  * The larger-than-standard PCB size and the position of the UART0 connector means some shields won't physically fit.

J9   
---  
1x8 Header   
1 | _NC_  
2 | _3V3_SYS_  
3 | _RESET#_  
4 | _3V3_SYS_  
5 | _DC_5V_  
6 | _GND_  
7 | _GND_  
8 | _DC_5V_  
J12   
---  
1x6 Header   
1 | _LRADC0_  
2 | _LRADC1_  
3 | _XP_TP_  
4 | _XN_TP_  
5 | _YP_TP_  
6 | _YN_TP_  
J8   
---  
1x10 Header   
1 | [PH10][31452] (LCD1_D10/ERXD1/KP_IN2/MS_D2/EINT10/CSI1_D10)  
2 | [PH05][31453] (LCD1_D05/UART4_RX/EINT5/CSI1_D5)  
3 | [PI10][31454] (SPI0_CS0/UART5_TX)  
4 | [PI12][31455] (SPI0_MOSI/UART6_TX/CLK_OUT_A)  
5 | [PI13][31456] (SPI0_MISO/UART6_RX/CLK_OUT_B)  
6 | [PI11][31457] (SPI0_CLK/UART5_RX)  
7 | _GND_  
8 | 0.1uF capacitor to GND   
9 | [PB21][31458] (TWI2_SDA)  
10 | [PB20][31459] (TWI2_SCK)  
J11   
---  
1x8 Header   
1 | [PI19][31460] (SPI1_MISO/UART2_RX)  
2 | [PI18][31461] (SPI1_MOSI/UART2_TX)  
3 | [PH07][31462] (LCD1_D07/UART5_RX/MS_CLK/EINT7/CSI1_D7)  
4 | [PH06][31463] (LCD1_D06/UART5_TX/MS_BS/EINT6/CSI1_D6)  
5 | [PH08][31464] (LCD1_D08/ERXD3/KP_IN0/MS_D1/EINT8/CSI1_D9)  
6 | [PB02][31465] (PWM0)  
9 | [PI03][31466] (PWM1/TWI4_SDA)  
10 | [PH09][31467] (LCD1_D09/ERXD2/KP_IN1/MS_D0/EINT9/CSI1_D8)  
# Adding a serial port
[![][31468]][31469]
[][31470]
UART header with a Prolific PL2303 USB serial cable attached
## Locating the UARTs
The pcDuino3 Nano provides access to four (and a half) of the A20's UARTs. See the [UART howto][31471] for more details. 
The 3-pin header labelled "UART" sticking out from the side of the board is the A20's UART0. Pin 1 (with a square pad, closest to the IR receiver) is RX, pin 2 is ground, pin 3 is TX. 
UART2, UART5 and UART6 (RX/TX), as well as UART4 (RX only) are available on the Arduino connectors. UART2 is in the standard place for an Arduino UART. 
Note that the labelling in [LinkSprite's diagram][31472] is a bit confusing -- UART2 is described from the A20's point of view but UART0 from the serial cable's point of view, i.e. RX and TX are reversed for UART0. 
# Pictures
  * [![PcDuino3 Nano top.jpeg][31473]][31474]
  * [![PcDuino3 Nano bottom.jpeg][31475]][31476]
  * [![Linksprite pcduino3 nano general.JPG][31477]][31478]

# Variants
The [pcDuino3 Nano **Lite**][31479] is a version with no flash memory (NAND) and without IR receiver. 
# Also known as
This device has not been rebadged. 
# See also
  * [LinkSprite pcDuino][31480]
  * [LinkSprite pcDuino2][31481]
  * [LinkSprite pcDuino3][31482]
  * [Schematic][31483]
  * [Diagram of pcDuino v3 Nano connectors and header pinouts][31472]
  * [LinkSprite's pcDuino kernel repository on GitHub][31484]
  * [pcDuino3 Nano ubuntu and android images][31485]
  * [Armbian's working fex file for the pcDuino3 Nano derived from the one shipped with Linksprite's Linux images][31486]

## Manufacturer images
The [Ubuntu 14 image that LinkSprite provides][31485] uses a modified linux-sunxi 3.4 kernel. Their patches and build scripts are available [on GitHub][31484]. 
The most important modification is in the GMAC driver, to set the GMAC_TX_DELAY parameter to 3. This adjusts the relative timing of the clock and data signals to the PHY in order to compensate for differing trace lengths on the PCB ([details][31487]; the [Banana Pi][31488] has the same problem). Without this modification, the Ethernet port will work at 100Mbit but not at 1000Mbit. Upstream U-Boot now sets this parameter itself, so the kernel patch isn't needed any more ([patch][31489]). 
In the meantime [Armbian][31490] also supports the pcDuino3 Nano with Debian Wheezy, Jessie or Ubuntu Trusty and with both kernel 3.4.x and 4.1.x (including SoC temp fixes).
