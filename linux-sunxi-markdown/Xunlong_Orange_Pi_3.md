# Xunlong Orange Pi 3
Xunlong Orange Pi 3  
---  
[![Orangepi3 top.jpeg][60532]][60533]  
Manufacturer |  [OrangePi][60534]  
Dimensions |  90 _mm_ x 64 _mm_  
Release Date |  January 2019   
Website |  [Orange Pi 3 Product Page][60535]  
Specifications   
SoC |  [H6][60536] @ 1.8 Ghz   
DRAM |  1GiB/2GiB LPDDR3 @ 744MHz   
NAND |  8GB eMMC (optional)   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive)   
Features   
Video |  HDMI type A full, composite on AV port   
Audio |  3.5mm headphone plug, HDMI, onboard microphone   
Network |  WiFi 802.11 b/g/n/ac (AP6256), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][60537])   
Storage |  µSD, optional soldered eMMC   
USB |  1 USB2.0 Host, 1 USB2.0 OTG, 4 x USB3.0 host (via hub chip)   
Other |  infrared receiver, PCIe ([broken in SoC][60538])   
Headers |  26 pin GPIO, 3 pin UART   
## Contents
  * [1 Identification][60539]
  * [2 Sunxi support][60540]
    * [2.1 Current status][60541]
    * [2.2 Manual build][60542]
      * [2.2.1 U-Boot][60543]
        * [2.2.1.1 Sunxi/Legacy U-Boot][60544]
        * [2.2.1.2 Mainline U-Boot][60545]
      * [2.2.2 Linux Kernel][60546]
        * [2.2.2.1 Sunxi/Legacy Kernel][60547]
        * [2.2.2.2 Mainline kernel][60548]
        * [2.2.2.3 Firmware files][60549]
  * [3 Tips, Tricks, Caveats][60550]
    * [3.1 FEL mode][60551]
  * [4 Using serial port][60552]
    * [4.1 Locating the UART][60553]
  * [5 Pictures][60554]
  * [6 See also][60555]
    * [6.1 Manufacturer images][60556]

# Identification
The currently sold board has the following text on top: _Orange Pi 3 v1.5_. 
# Sunxi support
## Current status
The H6 SoC support has matured since its introduction in kernel 4.17. Most of the board functionality for boards such as Orange Pi 3 are available with current mainline kernels. For the missing features see: [Linux_mainlining_effort][60557]
## Manual build
You can build things for yourself by following our [ Manual build howto][60558] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
  * <https://github.com/orangepi-xunlong/OrangePiH6_uboot> \- BSP U-Boot

#### Mainline U-Boot
Use the _orangepi_3_defconfig_ build target. Available since v2021.04-rc1. 
### Linux Kernel
#### Sunxi/Legacy Kernel
  * <https://github.com/orangepi-xunlong/OrangePiH6_external> \- FEX/WiFi firmware files
  * <https://github.com/orangepi-xunlong/OrangePiH6_Linux4_9> \- BSP kernel

Config name is _OrangePiH6_3_defconfig_
#### Mainline kernel
Use the **sun50i-h6-orangepi-3.dts** device-tree binary (available since kernel 5.2). 
Mainline Linux kernel device tree file for this board is being prepared in this Linux tree: 
  * <https://megous.com/git/linux/log/?h=opi3-5.11>

The tree currently contains additional patches for the Ethernet. 
  * This branch contains support for thermal sensor, DVFS and thermal regulation:

<https://megous.com/git/linux/log/?h=ths-5.11>
#### Firmware files
For WiFi, you'll need a fw_bcm43456c5_ag.bin firmware file and nvram.txt configuration that can be found in the Xulongs's repository for H6: 
  * <https://github.com/orangepi-xunlong/OrangePiH6_external/tree/master/ap6256>

Mainline brcmfmac driver expects the firmware and nvram at the following paths relative to the firmware directory: 
  * brcm/brcmfmac43456-sdio.bin
  * brcm/brcmfmac43456-sdio.txt

For Bluetooth 5.0, you'll need a BCM4345C5.hcd firmware file that can be found in the Xulongs's repository for H6: 
  * <https://github.com/orangepi-xunlong/OrangePiH6_external/tree/master/ap6256>

The driver expects the firmware at the following path relative to the firmware directory: 
  * brcm/BCM4345C5.hcd

# Tips, Tricks, Caveats
  * USB power rails are directly connected to the 5V input power, including on the micro USB connector (you'll have trouble powering the board from the DC jack, and using the microUSB port to connect the board to a PC at the same time). The board can be powered via DC input or via microUSB with a PSU like an [Aukru 5V 3A][60559]; powering from an USB 3 port should work but is untested.
  * The schematic specifies a total current limit of 1.5A per the double USB 3.0 connector.
  * The schematic shows optional polyfuse circuit to limit the USB current, but there's no polyfuse on the v1.5 of the board.
  * UBoot does not support PMIC that's used on the board, and doesn't turn off ethernet PHY regulators after reboot, which may lead to PHY initialization failures during reboot in some configurations.
  * Ethernet might not work with current versions and their combinations of UBoot, ATF (arm-trusted-firmware) and Linux. ATF needs to be built with SUNXI_SETUP_REGULATORS=0 passed or built from a version not yet having any support for setting up respective regulator(s) (e.g. "v2.2").

## FEL mode
  * If you try this, beware of the direct connection between microUSB VBUS and DCIN.

# Using serial port
Like with other Orange Pi boards, UART uses 3.3V signalling and is 5V tolerant so you can use any of the usual USB-UART dongles. UART pin header is easily accessible. 
## Locating the UART
UART is located between the mic and the power on key. Pin order: GND-RX-TX. GND is marked by a white arrow. 
# Pictures
  * [![Orangepi3 top.jpeg][60560]][60533]
  * [![Orangepi3 bottom.jpeg][60561]][60562]
  * [![Orangepi3 eth.png][60563]][60564]
  * [![Orangepi3 hdmi.png][60565]][60566]

# See also
  * AXP805 Datasheet: [File:AXP805 Datasheet V1.0 en.pdf][60567]
  * H6 Datasheet: [File:Allwinner H6 V200 Datasheet V1.1.pdf][60568]
  * H6 User Manual: [File:Allwinner H6 V200 User Manual V1.1.pdf][60569]
  * Schematics 1.5: [File:OrangePi 3 Schematics v1.5.pdf][60570]

## Manufacturer images
Optional. Add non-sunxi images in this section.
