# LicheePi Zero
LicheePi Zero  
---  
[![LicheePi Zero Front.jpg][30955]][30956]  
Manufacturer |  [Zepan][30957]  
Dimensions |  44 _mm_ x 26 _mm_  
Release Date |  Not generally available now   
Website |  [[1]][30958]  
Specifications   
SoC |  [V3s][30959] @ 1Ghz   
DRAM |  64MiB DDR2 Integrated @ 360MHz   
Power |  via GPIO pins or MicroUSB Jack   
Features   
LCD |  optional   
Audio |  via extension board (not available now)   
Network |  10/100Mbps Ethernet (via extension board, not available now)   
Storage |  µSD, on-board SPI NOR Flash (or SPI NAND)   
USB |  1 USB2.0 OTG   
Camera |  optional   
Headers |  15x2 GPIO pins, breadboard compatible   
This device is the first community-known V3s board, and it didn't use the PMU in the V3s official design (but dedicated DCDCs). 
## Contents
  * [1 Identification][30960]
  * [2 Sunxi support][30961]
    * [2.1 Current status][30962]
      * [2.1.1 U-Boot][30963]
        * [2.1.1.1 Mainline U-Boot][30964]
      * [2.1.2 Linux Kernel][30965]
        * [2.1.2.1 Mainline kernel][30966]
  * [3 Tips, Tricks, Caveats][30967]
    * [3.1 FEL mode][30968]
  * [4 Adding a serial port][30969]
    * [4.1 Locating the UART][30970]
  * [5 Pictures][30971]
  * [6 Also known as][30972]
  * [7 See also][30973]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Lichee
    Zero
[/code]
[code] 
    SUNXI
[/code]
# Sunxi support
## Current status
No sunxi support now, but there's some WIP code. 
### U-Boot
#### Mainline U-Boot
Use the **LicheePi_Zero_defconfig** (supported since v2017.05) build target. 
~~Not supported yet. WIP code is at[[2]][30974]~~
### Linux Kernel
#### Mainline kernel
Use the **sun8i-v3s-licheepi-zero.dtb**. 
~~Not supported yet. WIP code is at[[3]][30975]~~
# Tips, Tricks, Caveats
## FEL mode
When the on-board flash is empty, just remove the MicroSD to enter FEL mode. 
# Adding a serial port
## Locating the UART
The pins tagged "I2C1" on the board is the UART0 (muxed with I2C1). 
When seeing from top and have the "SUNXI" silkscreen at left side, the TX pin is the left (12th pin at the bottom), and the RX is the right (13th pin). 
# Pictures
  * Developer Sample:
  * [![LicheePi Zero Front.jpg][30976]][30956]
  * [![LicheePi Zero Back.jpg][30977]][30978]

  * Production:
  * [![Pic8.jpg][30979]][30980]
  * [![Pic7.jpg][30981]][30982]

  * Board references:
  * [![Pic5.jpg][30983]][30984]
  * [![Licheepizerogf.png][30985]][30986]

Note: the yellow wire seen on the back image of the sample board is because this board is one of the earliest samples, and the factory made a mistake when soldering the DCDC chip, which needs to be fixed. 
# Also known as
# See also
[LicheePi One][30987]
