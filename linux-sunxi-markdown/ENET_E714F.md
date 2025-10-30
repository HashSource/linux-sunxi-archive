# ENET E714F
ENET E714F  
---  
[![ENET E714F front.jpg][17452]][17453]  
Manufacturer |  [ENET][17454]  
Dimensions |  181mm x 121mm x 10.5mm   
Release Date |  10 2015   
Specifications   
SoC |  [A23][17455] @ 1.5 Ghz   
DRAM |  512MiB DDR3 @ 432 MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 2500mAh 3.7V Li-polymer battery   
Features   
LCD |  7" 800x480   
Touchscreen |  5-finger capacitive ([Silead GSL1680][17456])   
Video |  Lcd   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8703AS][17457])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP hi704 (640x480) front, 0.3MP hi704 (640x480) rear   
Other |  Bluetooth,Accelerometer mir3da (da380)   
Headers |  UART   
The ENET E714F is a cheap chinese tablet , a clone of the Q8 tablet. 
## Contents
  * [1 Identification][17458]
  * [2 Sunxi support][17459]
    * [2.1 Current status][17460]
    * [2.2 HW-Pack][17461]
    * [2.3 BSP][17462]
    * [2.4 Manual build][17463]
      * [2.4.1 U-Boot][17464]
        * [2.4.1.1 Sunxi/Legacy U-Boot][17465]
        * [2.4.1.2 Mainline U-Boot][17466]
      * [2.4.2 Linux Kernel][17467]
        * [2.4.2.1 Sunxi/Legacy Kernel][17468]
        * [2.4.2.2 Mainline kernel][17469]
    * [2.5 FEL mode][17470]
    * [2.6 Device specific topic][17471]
  * [3 Adding a serial port (**voids warranty**)][17472]
    * [3.1 Device disassembly][17473]
    * [3.2 Locating the UART][17474]
  * [4 Pictures][17475]
  * [5 See also][17476]

# Identification
On the back of the device, the following is printed: 
[code] 
    ENET E714F
    E714F
[/code]
The PCB has the following silkscreened on it: 
[code] 
    BM750_V3.12
    2015 10_12
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: E714F
  * Build Number: 207_polaris_uarmmid-eng 4.4.2 KVT49L 20160518.test-keys

# Sunxi support
## Current status
supported under mainline u-boot and mainline kernel. 
## HW-Pack
## BSP
## Manual build
You can build things for yourself by following our [ Manual build howto][17477] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
not supported 
#### Mainline U-Boot
Use the "q8_a23_tablet_800x480_defconfig" build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
not supported 
#### Mainline kernel
Use the "sun8i-a23-q8-tablet.dtb" device-tree binary. 
  

## FEL mode
The Volume+ button triggers [ FEL mode][17478]. 
## Device specific topic
Although the Soc is labeled A33 Quad Core, and The android say QuadCore-A33 , this is actually An A23 Soc ! 
  

# Adding a serial port (**voids warranty**)
[![][17479]][17480]
[][17481]
ENET E714F UART pads
## Device disassembly
See [the Q8 tablet format disassembly page][17482]. 
## Locating the UART
the exposed UART pads are for R_UART These pads correspond to PL2/3 , and doesn't provide output under stock android , but works with mainline u-boot and mainline kernel , UART pads are located very near the SoC on the upper right corner , see the photo . please refer to [UART howto][17483] for more information 
# Pictures
  * [![ENET E714F front.jpg][17484]][17453]
  * [![ENET E714F back.jpg][17485]][17486]
  * [![ENET E714F Board Front.jpg][17487]][17488]

  

# See also
[Other Q8 format A33 based tablets.][17489]
