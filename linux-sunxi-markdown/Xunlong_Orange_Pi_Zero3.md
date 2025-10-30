# Xunlong Orange Pi Zero3
Xunlong Orange Pi Zero3  
---  
[![OPi Zero3 top.jpg][62917]][62918] [][62919]  
Manufacturer |  [Xunlong][62920]  
Dimensions |  _50mm_ x _55mm_  
Release Date |  Jun 2023   
Website |  [Orange Pi Zero3][62921]  
Specifications   
SoC |  [H618][62922] @ 1.512 Ghz   
DRAM |  1/1.5/2/4GiB LPDDR4 @ 792 MHz   
Power |  DC 5V @ 2A via USB-C connector   
Features   
Video |  Micro HDMI 2.0a, CVBS on header   
Audio |  Line out on header, HDMI audio   
Network |  WiFi 802.11 a/b/g/n (Cdtech 20U5622), 10/100/1000Mbps Ethernet ([Motorcomm YT8531][62923])   
Storage |  µSD, 128Mbit [SPI flash][62924] (zBit 25VQ128ASIG)   
USB |  1 X USB2.0 Host, 1 X USB2.0 OTG, 2 X USB2.0 Host on header   
Not to be confused with Orange Pi 3 (H6) or Orange Pi Zero2 (H616). This is the H618 version from 2023. It's a slightly updated successor of the Orange Pi Zero2, with some component, board layout and size changes (see below for more details). 
## Contents
  * [1 Identification][62925]
  * [2 General Notes][62926]
  * [3 Sunxi support][62927]
    * [3.1 Current status][62928]
    * [3.2 Images][62929]
    * [3.3 BSP][62930]
    * [3.4 Manual build][62931]
      * [3.4.1 U-Boot][62932]
      * [3.4.2 Linux Kernel][62933]
  * [4 Expansion ports][62934]
  * [5 Tips, Tricks, Caveats][62935]
    * [5.1 FEL mode][62936]
    * [5.2 LEDs][62937]
    * [5.3 SPI booting][62938]
  * [6 Serial port][62939]
  * [7 Pictures][62940]
  * [8 See also][62941]

# Identification
A serial number sticker can be found on the back of the board: 
[code] 
    OPI- Zero3-xGB
    <SerialNumber>
[/code]
The PCB has a version number silkscreened nest to the SOC and RAM: 
[code] 
    Orange Pi
    Zero3 v1.2
[/code]
# General Notes
Some differences to the [Orange Pi Zero 2][62942]: 
Feature | [Orange Pi Zero2][62942] | Orange Pi Zero3   
---|---|---  
SoC | H616 | H618   
DRAM type | DDR3 | LPDDR4   
DRAM sizes | 512MB/1GB | 1/1.5/2/4 GB   
SPI flash size | 2MB | 16MB   
PMIC | AXP305 | AXP313a   
Ethernet PHY | RTL8211F | YT8531C   
For a change, there is some Linux (Android kernel) image on the SPI flash, although it seems to be misconfigured to not show much output on HDMI or serial. It's the usual Allwinner provided BSP kernel, in the very outdated (and hacked) version 4.9.170, compiled by an even older compiler. 
The LEDs are software controlled, so won't light up until something is explicitly telling them so. The shipped SPI flash image does so after a few seconds. 
# Sunxi support
## Current status
The Orange Pi Zero3 uses the H618 SoC, which is mostly software compatible with the H616, just with a larger L2 cache and a change in the CPU cluster control IP, affecting TF-A and U-Boot only. 
This board is an updated version of the Orange Pi Zero2, but uses a different PMIC, DRAM type and Ethernet PHY, all of which requiring software changes (DT changes and new drivers). Pure Orange Pi Zero2 images will not work. PMIC and Ethernet PHY are already supported by the latest mainline Linux kernel, LPDDR4 and the PMIC are also supported by latest U-Boot. 
## Images
## BSP
TBC 
## Manual build
You can build things for yourself by following our [ Manual build howto][62943] and by choosing from the configurations available below. 
### U-Boot
Use the **orangepi_zero3_defconfig** build target. Available since v2024.01-rc5. 
Does not have compatibility for a 1.5GB board. 
### Linux Kernel
Use the **sun50i-h618-orangepi-zero3.dtb** device-tree binary from a mainline kernel, available since v6.6. 
The PMIC and the Ethernet PHY are supported since v6.5-rc1, so the board just needs the proper DTB to run with this or later kernels. 
# Expansion ports
The Orange Pi Zero3 has a 26-pin, 0.1" populated connector with several low-speed interfaces. 
The primary function follows loosely the old Raspberry Pi pin assignment (TWI3 (aka I2C), UART5, SPI1, GPIOs), but pinmuxing gives access to more interfaces (not all at the same time): UART2 (incl. h/w handshake), TWI2, TWI4, SPDIF, PWM1, PWM2, single bit MMC2. 
2x13 Header   
---  
__| __|  3.3V | 1 |  | 2 | 5V | __| __  
SPI1_CS0 / UART2_TX | PH5 | I2C3-SDA | 3 |  | 4 | 5V | __| __  
SPDIF_OUT | PH4 | I2C3-SCK | 5 |  | 6 | GND | __| __  
__|  PC9 | GPIO-73 | 7 |  | 8 | UART5-TX | PH2 | SPDIF_CLK / PWM2 / TWI2_SCK   
__| __|  GND | 9 |  | 10 | UART5-RX | PH3 | PWM1 / TWI2_SDA   
SCD2_CMD | PC6 | GPIO-70 | 11 |  | 12 | GPIO-75 | PC11 | __  
SDC2_CLK | PC5 | GPIO-69 | 13 |  | 14 | GND | __| __  
__|  PC8 | GPIO-72 | 15 |  | 16 | GPIO-79 | PC15 | SPI0_WP   
__| __|  3.3V | 17 |  | 18 | GPIO-78 | PC14 | __  
UART2_RTS / TWI4_SDA | PH7 | SPI1-MOSI | 19 |  | 20 | GND | __| __  
UART2_CTS | PH8 | SPI1-MISO | 21 |  | 22 | GPIO-71 | PC7 | __  
UART2_RX / TWI4_SCK | PH6 | SPI1-SCK | 23 |  | 24 | SPI1-CS | PH9 | __  
__| __|  GND | 25 |  | 26 | GPIO-74 | PC10 | SCD2_D0   
The Orange Pi Zero3 has another 13-pin, 0.1" header with USB and analogue interfaces. The 13-pin interface board originally used for Orange Pi Zero is compatible with Zero3, but the microphone on the board is no longer available. 
1x13 Header   
---  
1 | _5V_  
2 | _GND_  
3 | USB2-DM   
4 | USB2-DP   
5 | USB3-DM   
6 | USB3-DP   
7 | LINEOUTR   
8 | LINEOUTL   
9 | TV-OUT   
10 | PC1   
11 | PI16   
12 | PI6   
13 | [CIR][62944]-RX / PH10   
# Tips, Tricks, Caveats
## FEL mode
No dedicated FEL button. [FEL mode][62945] will be entered without an SD card and with no valid eGON signature on the SPI flash. Alternatively the usual FEL trigger SD card image can be used. 
The USB-C connector used to power the board carries the USB-OTG signals for the FEL mode, so the board needs to be powered through a host computer or a powered USB hub for using FEL mode. 
## LEDs
There are two unlabelled LEDs on the board, a red and a green one. According to the schematic they are Power (red) and Status (green), but both are connected to GPIOs (PC12 and PC13), so need active software toggling to light up. 
## SPI booting
The board contains a 16MB SPI NOR flash chip, and the SoC can boot firmware from there. 
# Serial port
[![][62946]][62947]
[][62948]
OrangePi Zero 3 UART pins
The UART pins are located near one corner of the board, in a clearly distinct group of three pins. They are marked as _TX_ , _RX_ and _GND_ on the PCB. Just attach some leads according to our [UART Howto][62949]. 
# Pictures
  * [![OPi Zero3 connectors.jpg][62950]][62951]
  * [![OPi Zero3 chips.jpg][62952]][62953]
  * [![OPi Zero3 top.jpg][62954]][62918]

# See also
