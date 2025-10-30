# Blueberry PI
Blueberry PI  
---  
[![BlueberryPI-top-re.jpg][10056]][10057]  
Manufacturer |  [petit_miner][10058]  
Dimensions |  99 _mm_ x 65 _mm_  
Release Date |  available on [Tindie][10059]  
Website |  [Github Page][10060]  
Specifications   
SoC |  [V3s][10061] @ 1Ghz   
DRAM |  64MiB DDR2 Integrated @ 360MHz   
Power |  via GPIO pins or MicroUSB Jack or DC Jack   
Features   
LCD |  optional   
Audio |  Headphone Jack, Microphone   
Network |  10/100Mbps Ethernet, RTL8723BS Wifi   
Storage |  µSD, on-board SPI NOR Flash (or SPI NAND)   
USB |  1 USB2.0 OTG or 1 USB2.0 Host   
Camera |  2 Header for an OV7670 and OV2640 camera   
Headers |  15x2 GPIO pins, breadboard compatible   
The Blueberry PI is a V3s development board. It features all of the interfaces found in the V3s. The V3s comes in a 128pin TQFP package, and it is one of few SoC's which have built-in RAM. 
## Contents
  * [1 Identification][10062]
  * [2 Sunxi support][10063]
    * [2.1 Current status][10064]
      * [2.1.1 U-Boot][10065]
        * [2.1.1.1 Mainline U-Boot][10066]
      * [2.1.2 Linux Kernel][10067]
        * [2.1.2.1 Mainline kernel][10068]
  * [3 Tips, Tricks, Caveats][10069]
    * [3.1 FEL mode][10070]
    * [3.2 Locating the UART][10071]
  * [4 Pictures][10072]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Blueberry PI
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
### Linux Kernel
#### Mainline kernel
Use the **sun8i-v3s-licheepi-zero.dtb**. 
# Tips, Tricks, Caveats
## FEL mode
When the on-board flash is empty, just remove the MicroSD to enter FEL mode. 
## Locating the UART
Since the Blueberry PI has a 26pin Raspberry PI compatible Header, the UART0 port is located at the same place as on the Raspberry PI. 
# Pictures
  * [![][10073]][10057]
Overview of the board 
  * [![][10074]][10075]
Sideview 1 (Ethernet, USB) 
  * [![][10076]][10077]
Sideview 2 (DC Jack, LCD) 
  * [![][10078]][10079]
Sideview 3 (Camera Header, GPIO Header, MIPI CSI) 
  * [![][10080]][10081]
Sideview 4 (LRADC0, Headphone Jack, Wifi RTL8723BS)
