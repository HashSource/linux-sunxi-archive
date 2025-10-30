# CherryPi PC V7
CherryPi PC V7  
---  
[![CherryPi PC V7 Top.jpeg][12547]][12548]  
Manufacturer |  [Shenzhen LC Technology][12549]  
Dimensions |  85 _mm_ x 56 _mm_  
Release Date |  January 2021   
Website |  [LcTech Pi H3 V7 Product Page][12550]  
Specifications   
SoC |  [H3][12551] @ 1.2Ghz   
DRAM |  1GiB DDR3 (SK hynix H5TQ4G63CFR-RDC × 2)   
NAND |  8GB (Samsung KLM8G1GETF-B041)   
Power |  via 5V Type-C USB or via 5V microB OTG   
Features   
Video |  HDMI (Type A - full), CVBS   
Audio |  3.5mm headphone plug, HDMI, on-board microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8189FTV][12552]), 10/100 Ethernet   
Storage |  µSD, eMMC   
USB |  2 x USB2.0 Host, 1 x USB2.0 OTG   
Camera |  MIPI CSI   
Other |  infrared receiver   
Headers |  26pin GPIO, 3pin UART   
This page needs to be properly filled according to the [New Device Howto][12553] and the [New Device Page guide][12554].
## Contents
  * [1 Identification][12555]
  * [2 Stock firmware][12556]
    * [2.1 Manual build][12557]
      * [2.1.1 U-Boot][12558]
        * [2.1.1.1 Mainline U-Boot][12559]
      * [2.1.2 Linux Kernel][12560]
        * [2.1.2.1 Mainline kernel][12561]
    * [2.2 Locating the UART][12562]
  * [3 Pictures][12563]
  * [4 Also known as][12564]
  * [5 See also][12565]

# Identification
CherryPi PC V7 is a development board by Shenzhen LC Technology Co., Ltd. based on Allwinner H3 with a standard Raspberry Pi 3/4 board size. At some point name was changed to Lctech Pi H3 V7 
The PCB has the following silkscreened on the bottom: 
[code] 
    CherryPi-PC V7.3
    www.lctech-inc.com
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _dolphin_
  * Build Number: _dolphin_fvd_p2-eng 4.4.2 KOT49H 20200906 test-keys_

# Stock firmware
The board comes with a preinstalled Android 4.4.2 firmware based on v3.4.39 Linux kernel. U-Boot is 2011.90-rc1 Allwinner v1.1.0 
## Manual build
You can build things for yourself by following our [ Manual build howto][12566] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the orangepi_plus build target. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][12567]. 
The H3 boards can boot from [SD cards][12568], [eMMC][12569], [NAND][12570] or [SPI NOR][12571] flash (if available), and via [FEL][12572] using the OTG USB port. In U-Boot, loading the kernel is also supported from USB or ethernet (netboot). HDMI support in U-Boot is still WIP. 
### Linux Kernel
#### Mainline kernel
Board appears to be compatible with images built for the [Xunlong_Orange_Pi_Plus][12573] so use the sun8i-h3-orangepi-plus.dtb device-tree binary. 
## Locating the UART
Standard on-board GND/TX/RX 3-pin UART pin header (3.3V) located between HDMI and OTG ports, refer to the [UART howto][12574] for more information. 
# Pictures
  * [![CherryPi PC V7 Top.jpeg][12575]][12548]
  * [![CherryPi PC V7 Bottom.jpeg][12576]][12577]

# Also known as
Lctech Pi H3 V7 
# See also
[CNX-Software article][12578] [LinuxGizmos article][12579]
