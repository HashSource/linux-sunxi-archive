# CherryPi PC H6
CherryPi PC H6  
---  
[![CherryPi PC H6.jpg][12416]][12417] [][12418]  
Manufacturer |  [Shenzhen LC Technology Co., LTD.][12419]  
Dimensions |  85 _mm_ x 56 _mm_  
Release Date |  January 2021   
Website |  [CherryPi PC H6 Product Page][12420]  
Specifications   
SoC |  [H6][12421] @ 1.8Ghz   
DRAM |  1GiB LPDDR3 @ xxxMHz (Allwinner AW52A8G32 x1)   
NAND |  8 GB eMMC   
Power |  via 5V Type-C USB or via 5V microB OTG   
Features   
Video |  HDMI (Type A - full)   
Audio |  via HDMI only   
Network |  WiFi 802.11 b/g/n ([Ampak AP6212][12422]), 10/100 Mbps Ethernet ([HanRun hr91105a][12423])   
Storage |  µSD, eMMC   
USB |  1 x USB2.0 Host, 1 x USB2.0 OTG, 1 x USB3.0 Host   
Other |  infrared receiver   
Headers |  26pin GPIO, 3pin UART   
CherryPi PC H6 is a development board by Shenzhen LC Technology Co., Ltd. based on Allwinner H6 in a standard Raspberry Pi 3/4 form factor. 
## Contents
  * [1 Stock firmware][12424]
  * [2 Mainline Linux support][12425]
  * [3 Tips, Tricks, Caveats][12426]
    * [3.1 USB subsystem][12427]
    * [3.2 FEL mode][12428]
  * [4 Serial port][12429]
  * [5 References][12430]

# Stock firmware
The board comes with a preinstalled Android TV-tailored firmware based on v3.10.65 Linux kernel. The firmware has no root access. 
# Mainline Linux support
The board is able to boot mainline Linux kernel (such as v5.4.65) with Ubuntu Focal rootfs. A device image could be prepared using Xulong orangepi-build[[1]][12431], with OrangePi 3 selected as a target device. The OrangePi 3 device tree is not fully compatible with Cherry Pi PC H6[[2]][12432]. Ethernet adapter does not work; wireless adapter works, but with a very low bandwidth. Wireless connection could be established with NetworkManager cli: 
[code] 
       nmcli d wifi connect <WiFiSSID> password <WiFiPassword>
    
[/code]
# Tips, Tricks, Caveats
## USB subsystem
  * USB2 mini port has been tested to work safely in OTG mode. In order to enable OTG mode, do the following:

  1. decompile /boot/dtb/allwinner/sun50i-h6-orangepi-3.dtb to dts with a corresponding dtc compiler
  2. change dr_mode from "host" to "otg" for node usb@5100000
  3. compile dts back into dtb
  4. overwrite /boot/dtb/allwinner/sun50i-h6-orangepi-3.dtb with the new dtb
  5. reboot

  * USB3 A port is operated by the DWC3 driver, and may have OTG support as well, but this one is not tested and can be unsafe

## FEL mode
The UBOOT (Upgrade) button triggers [ FEL mode][12433]. 
# Serial port
Standard on-board GND/TX/RX 3-pin UART pin header (3.3V), refer to the [UART howto][12434] for more information. 
# References
  1. [↑][12435] <https://github.com/orangepi-xunlong/orangepi-build>
  2. [↑][12436] <https://github.com/dmikushin/chpivsopidts>
