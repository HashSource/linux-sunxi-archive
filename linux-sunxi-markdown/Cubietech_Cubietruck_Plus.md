# Cubietech Cubietruck Plus
Cubietech Cubietruck Plus  
---  
[![Cubietruck Plus Front.jpg][15359]][15360]  
Manufacturer |  [Cubietech][15361], [Cubieboard][15362]  
Dimensions |  112 _mm_ x 82 _mm_ x 18 _mm_  
Release Date |  December 2015   
Website |  [Cubietruck Plus Product Page][15363]  
Specifications   
SoC |  [A83T][15364]/[H8][15365] @ 2Ghz   
DRAM |  2GiB DDR3 @ 672MHz ([SK hynix H5TQ4G83AFR][15366] * 2)   
NAND |  8GB eMMC (FORESEE NCEFEH58-O8G)   
Power |  DC 5 V @ 2 A (3A with 2.5" SATA drive) using 4/1.7mm jack, JST XH 2.5mm Battery connector   
Features   
Video |  HDMI (Type A - full), DP (w/ Toshiba TC358777XBG MIPI DSI - DP bridge)   
Audio |  3.5mm headphone + microphone plug, onboard mic, HDMI, SPDIF, DP   
Network |  WiFi 802.11 a/b/g/n ([Ampak AP6330][15367]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][15368])   
Storage |  µSD, SATA (w/ GL830 USB 2.0 - SATA bridge)   
USB |  2 USB2.0 Host (through SMSC USB3503 HSIC USB 2.0 Hub), 1 USB2.0 OTG   
Other |  Bluetooth (Ampak AP6330), CIR, RTC battery   
Headers |  UART, I2S, I2C, SPI, CVBS, LRADC (2x),UART, PWM, CIR, CSI, LINE-IN, AUX-IN, MIPI CSI   
Cubietruck Plus is the fifth generation of the famous [Cubieboard][15369], an [A83T][15364] development board produced by Cubietech. 
## Contents
  * [1 Identification][15370]
  * [2 Sunxi support][15371]
    * [2.1 Current status][15372]
    * [2.2 Manual build][15373]
      * [2.2.1 U-Boot][15374]
        * [2.2.1.1 Mainline U-Boot][15375]
      * [2.2.2 Linux Kernel][15376]
        * [2.2.2.1 Mainline kernel][15377]
  * [3 Tips, Tricks, Caveats][15378]
    * [3.1 FEL mode][15379]
    * [3.2 Display Port][15380]
    * [3.3 SATA][15381]
    * [3.4 USB 2.0 Hosts][15382]
    * [3.5 Acrylic Case][15383]
    * [3.6 Possible software issues][15384]
    * [3.7 CPU Heating issues][15385]
  * [4 Adding a serial port][15386]
    * [4.1 Locating the UART][15387]
  * [5 Pictures][15388]
  * [6 Also known as][15389]
  * [7 See also][15390]
    * [7.1 Manufacturer images][15391]

# Identification
The board helpfully states "CUBIETRUCK PLUS". 
According to Cubieboard's resources repository, there are 2 versions: v1.0 and v1.1. Cubietech states that all retail pieces are v1.1. 
# Sunxi support
The board is supported by both mainline U-Boot and kernels. 
## Current status
## Manual build
You can build things for yourself by following our [ Manual build howto][15392] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **Cubietruck_plus_defconfig** build target. 
### Linux Kernel
#### Mainline kernel
Use the **sun8i-a83t-cubietruck-plus.dtb** device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The UBOOT button forces boot from mmc0, and drops to [ FEL mode][15393] if no boot signature is found. 
## Display Port
This board has a DP output, supported with a Toshiba TC358777XBG MIPI DSI - DP bridge. With Cubietech's images, one must switch out the FEX files to use DP instead of HDMI. This bridge chip is controlled via I2C. 
## SATA
The SATA port is not native SATA. It is supported by a GL830 USB 2.0 to SATA bridge. This chip is connected directly to the SoC's USB host. 
## USB 2.0 Hosts
Since the only USB 2.0 host is connected to the SATA bridge chip, the board has a SMSC USB3053 USB 2.0 HSIC hub chip, providing 2x Type-A USB host ports on the board.  
This USB3053 chip is controlled via I2C. Linux mainline kernel provides a driver ("usb3053") for it.  
1x OTG MicroUSB 
## Acrylic Case
The board comes with an plastic case, which is just 3 pieces of acrylic screwed together with the board using spacers. The screw holes on these are not very accurate, so one might not be able to do a complete assembly. 
## Possible software issues
If you're using Cubietech's OS image and processes get sigkilled when run under UID != 0 check the contents of _/proc/sys/vm/mmap_min_addr_. If it's [65536][15394] then try to decrease the value to 32678 or even 4096 and see whether that helps. 
## CPU Heating issues
The A83/H8 absolutely needs a heatsink, active cooling is heavily recommended, otherwise the CPU will lower max frequency or even stop using cores. 
# Adding a serial port
## Locating the UART
[![][15395]][15396]
[][15397]
DEVICE UART pads
There is a nice 0.1" connector behind the USB ports Just attach some leads according to our [UART howto][15398]. 
# Pictures
  * [![Cubietruck Plus Front.jpg][15399]][15360]
  * [![Cubietruck Plus Back.jpg][15400]][15401]
  * [![Cubietruck Plus Package.jpg][15402]][15403]

# Also known as
  * Cubieboard 5.

# See also
  * [Cubietech Cubietruck][15404]

## Manufacturer images
  * Vendor documentation, images and SDKs can be found at <http://dl.cubieboard.org/model/Cubietruck-plus/>
