# Sinlinx SinA33
Sinlinx SinA33  
---  
[![SinA33 front.jpg][49592]][49593]  
Manufacturer |  [Sinlinx][49594]  
Dimensions |  99 _mm_ x 82 _mm_  
Release Date |  November 2014   
Website |  [Device Product Page][49595]  
Specifications   
SoC |  [A33][49596] @ 1008Mhz   
DRAM |  1GiB DDR3 (Samsung K4B4G1646Q-HYKO * 2)@ 552MHz   
NAND |  4GB eMMC (Toshiba THGBM5G5A1JBAIR)   
Power |  DC 5V @ 2A, Battery connector   
Features   
Audio |  3.5mm headphone plug, 3.5mm microphone plug   
Storage |  µSD, eMMC   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  LCD, CSI, SDIO, LDARC, User GPIO   
The Sinlinx SinA33 is an [A33][49596] based development board by Sinlinx. 
This page needs to be properly filled according to the [New Device Howto][49597] and the [New Device Page guide][49598].
## Contents
  * [1 Identification][49599]
  * [2 Sunxi support][49600]
    * [2.1 Current status][49601]
    * [2.2 Manual build][49602]
      * [2.2.1 U-Boot][49603]
        * [2.2.1.1 Mainline U-Boot][49604]
      * [2.2.2 Linux Kernel][49605]
        * [2.2.2.1 Mainline kernel][49606]
  * [3 Tips, Tricks, Caveats][49607]
    * [3.1 FEL mode][49608]
    * [3.2 Optional LCD or VGA output][49609]
  * [4 Adding a serial port][49610]
    * [4.1 Locating the UART][49611]
  * [5 Pictures][49612]
    * [5.1 Manufacturer images][49613]

# Identification
On the back of the device, the following is printed: 
[code] 
    Manufacturer Marketing Name
    ModelNumber
[/code]
The PCB has the following silkscreened on it: 
[code] 
    SINA33 芯灵思 | SINLINX
[/code]
# Sunxi support
## Current status
There is no support for [A33][49596] in **legacy** sunxi, but the board is supported by mainline U-Boot & kernels. 
## Manual build
You can build things for yourself by following our [ Manual build howto][49614] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _Sinlinx_SinA33_defconfig_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _sun8i-a33-sina33.dtb_ device-tree tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][49615]. 
## Optional LCD or VGA output
Sinlinx provides a separate 7" LCD module or an LCD to VGA converter module, which can be connected to the board with a ribbon cable. 
# Adding a serial port
## Locating the UART
UART0 and UART1 are available on the USER IO header. UART0 and UART2 share the same RX/TX pins with different mux values. 
# Pictures
  * [![SinA33 front.jpg][49616]][49593]
  * [![SinA33 back.jpg][49617]][49618]
  * [![SinA33 buttons 1.jpg][49619]][49620]
  * [![SinA33 buttons 2.jpg][49621]][49622]
  * [![SinA33 buttons 3.jpg][49623]][49624]

## Manufacturer images
Sinlinx provides Android and Linux images to buyers, hosted on BaiduPan (Baidu's cloud storage).
