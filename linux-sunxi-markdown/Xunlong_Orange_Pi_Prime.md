# Xunlong Orange Pi Prime
Xunlong Orange Pi Prime  
---  
[![Orange Pi Prime top.jpg][62423]][62424]  
Manufacturer |  [OrangePi][62425]  
Dimensions |  98 _mm_ x 60 _mm_  
Release Date |  April 2017   
Website |  [Orange Pi Prime Product Page][62426]  
Specifications   
SoC |  [H5][62427] @ XGhz   
DRAM |  2GiB DDR3 @ xxxMHz   
Power |  DC 5V @ 3A,   
Features   
Video |  HDMI (Type A/B/C - full), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, internal microphone   
Network |  WiFi 802.11 b/g/n (Realtek RTL8723BS), 10/100/1000Mbps Ethernet (Realtek RTL8211E)   
Storage |  µSD, optional SPI NOR Flash on board   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  CSI connector   
Other |  Bluetooth, ([Manufacturer device][62428]), IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
_Orange Pi Prime_ is [H5][62427] based development board produced by [Xunlong][62429]. It comes with onboard gigabit Ethernet, 802.11 b/g/n WiFi + Bluetooth 4.0, HDMI, three USB 2.0 HOST, one USB 2.0 OTG. 
This page needs to be properly filled according to the [New Device Howto][62430] and the [New Device Page guide][62431].
## Contents
  * [1 Identification][62432]
  * [2 Sunxi support][62433]
    * [2.1 Current status][62434]
    * [2.2 BSP][62435]
    * [2.3 Manual build][62436]
      * [2.3.1 U-Boot][62437]
        * [2.3.1.1 Mainline U-Boot][62438]
      * [2.3.2 Linux Kernel][62439]
        * [2.3.2.1 Sunxi/Legacy Kernel][62440]
        * [2.3.2.2 Mainline kernel][62441]
  * [3 Expansion Port][62442]
  * [4 Tips, Tricks, Caveats][62443]
    * [4.1 FEL mode][62444]
    * [4.2 Device specific topic][62445]
    * [4.3 ESD & over-current protections][62446]
  * [5 Adding a serial port][62447]
  * [6 Pictures][62448]
  * [7 Also known as][62449]
  * [8 See also][62450]
    * [8.1 Manufacturer images][62451]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi
    Prime v1.0
[/code]
# Sunxi support
## Current status
The H5 SoC support has matured since its introduction in kernel 4.12. Most of the board functionality for boards such as Orange Pi Prime, including 3D graphics, hardware accelerated video and crypto, and DVFS are available with current mainline kernels. Only a very few minor features are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][62452]. 
See the [Manual build][62436] section for more details. 
  

## BSP
There are some somewhat abandoned 3.10 BSP code drops available in 'OrangePiLibra' and FriendlyELEC's github repos. Check the [orangepi-xunlong][62453] and [OrangePiLibra][62454] repositories in case of interest. 
It seems no device settings are contained and the BSP is broken anyway at least with regard to voltage regulation (that's also the reason vendor OS images seem to be limited to 1008 MHz since at this cpufreq those Orange Pi do not immediately crash with BSP kernel). 
## Manual build
You can build things for yourself by following our [Manual build howto][62455] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_prime_defconfig** (supported since v2017.07) build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
The H5 SoC has support in the [mainline kernels][62456]. 
The development process, links to patches and links to kernel fork repositories are listed on the [ Linux mainlining effort][62456] page. Patches can also be found from the arm-linux mailing list. 
Repositories with H5 patches: 
  * [Ondřej Jirman's branch for H5 based orange Pi (kernel 4.19)][62457] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)

  
Use the **sun50i-h5-orangepi-prime.dtb** device-tree binary. 
# Expansion Port
The Orange Pi Prime has a Raspberry Pi model B+ compatible 40-pin, 0.1" connector with several low-speed interfaces. 
2x20 Header   
---  
1 | _3.3V_ | 2 | _5V_  
3 | PA12 with 2k pullup (TWI0_SDA/DI_RX/PA_EINT12) | 4 | _5V_  
5 | PA11 with 2k pullup (TWI0_SCK/DI_TX/PA_EINT11) | 6 | _GND_  
7 | PA6 (SIM_PWREN/PWM1/PA_EINT6) | 8 | PA13 (SPI1_CS/UART3_TX/PA_EINT13)  
9 | _GND_ | 10 | PA14 (SPI1_CLK/UART3_RX/PA_EINT14)  
11 | PA1 (UART2_RX/JTAG_CK/PA_EINT1) | 12 | PD14   
13 | PA0 (UART2_TX/JTAG_MS/PA_EINT0) | 14 | _GND_  
15 | PA3 (UART2_CTS/JTAG_DI/PA_EINT3) | 16 | PC4   
17 | _3.3V_ | 18 | PC7   
19 | PC0 (SPI0_MOSI) | 20 | _GND_  
21 | PC1 (SPI0_MISO) | 22 | PA2 (UART2_RTS/JTAG_DO/PA_EINT2)  
23 | PC2 (SPI0_CLK) | 24 | PC3 (SPI0_CS)  
25 | _GND_ | 26 | PA21 (PCM0_DIN/SIM_VPPPP/PA_EINT21)  
27 | PA19 with 2k pullup (PCM0_CLK/TWI1_SDA/PA_EINT19) | 28 | PA18 with 2k pullup (PCM0_SYNC/TWI1_SCK/PA_EINT18)  
29 | PA7 (SIM_CLK/PA_EINT7) | 30 | _GND_  
31 | PA8 (SIM_DATA/PA_EINT8) | 32 | PG8 (UART1_RTS/PG_EINT8)  
33 | PA9 (SIM_RST/PA_EINT9) | 34 | _GND_  
35 | PA10 (SIM_DET/PA_EINT10) | 36 | PG9 (UART1_CTS/PG_EINT9)  
37 | PA20 (PCM0_DOUT/SIM_VPPEN/PA_EINT20) | 38 | PG6 (UART1_TX/PG_EINT6)  
39 | _GND_ | 40 | PG7 (UART1_RX/PG_EINT7)  
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][62458]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ESD & over-current protections
Based on the schematic Rev 1.0 (September 29, 2016) the board incorporates the following protections: 
Protections x - no protection, ESD - Electrostatic Discharge, OC - Over-current  | Comments   
---|---  
1 | Power jack | ESD (1) | x | Uses TVS diode, power supply bypass.   
2 | Micro SD | x | x |   
4 | Camera | x | x |   
5 | Dual USB1 | ESD (1) | OC (1.1A) | Over-current protection provided by SY6280, 1.1A shared for both ports, power supply bypass.   
6 | USB2 | ESD (1) | OC (1.1A) | Over-current protection provided by SY6280, power supply bypass.   
6 | Micro USB | ESD (1) | OC (680mA) | Over-current protection provided by SY6280, power supply bypass.   
7 | HDMI | ESD (1) | x |   
8 | Ethernet | x | N/A | Over-current protection is not applicable   
9 | GPIO | x | x |   
10 | Debug UART | x | ?   
11 | Audio jack | x | N/A | Output current is internally limited by SoC   
Notes: 
  1. On online OrangePi Prime pictures as well as on personal pictures it can be noticed that manufacturer has removed all ESD protection components on all USB ports and on I2C bus of HDMI port.

  * [![Orange Pi Prime ESD missing on USB HDMI.jpg][62459]][62460]
  * [![Orange Pi Prime ESD missing on MicroUSB.jpg][62461]][62462]

# Adding a serial port
[![][62463]][62464]
[][62465]
UART pins
The board exposes Debug serial 3-pin port which is located between Reset and Power switches (see picture on the right). The 3-pin port layout is the following: 
  1. GND
  2. CPU RX
  3. CPU TX

This connector is connected to UART0 using pins PA4 (TX) and PA5 (RX). Please refer to our [UART howto][62466] for further details. 
# Pictures
  * [![Orange Pi Prime top.jpg][62467]][62424]
  * [![Orange Pi Prime bottom.jpg][62468]][62469]
  * [![Orange Pi Prime USB.jpg][62470]][62471]
  * [![Orange Pi Prime buttons.jpg][62472]][62473]
  * [![Orange Pi Prime HDMI.jpg][62474]][62475]
  * [![Orange Pi Prime GPIO.jpg][62476]][62477]

# Also known as
List rebadged devices here.
# See also
[OrangePi Prime Schematic V1.0][62478]
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
