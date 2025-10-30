# Whatsminer CB4 v10
Whatsminer CB4 v10  
---  
[![Back CB4 10.png][59133]][59134]  
Manufacturer |  [W h a t s m i n e r][59135]  
Dimensions |  74 _mm_ x 105 _mm_ x 1.2 _mm_  
Release Date |  03 2020   
Website |  [[1]][59136]  
Specifications   
SoC |  [H6][59137] CV200 OS @ 1.32Ghz   
DRAM |  256MiB DDR3 @ 672MHz   
NAND |  256MB?   
Power |  DC 12V @ ?A, no battery   
Features   
Network |  10/100Mbps Ethernet (rmii   
Storage |  microSD, nand   
Other |  4 UART, PSU IO, Hashboard IO, lots of extra unused IOs on the PCB   
Headers |  UART   
This is a Whatsminer control board used to control the hashboards via 3 dedicated i2c buses. The PCB has a number of unused IOs that could be repurposed for various hardware interfaces, including JTAG, but probably also USB and possibly even a graphics interface. 
## Contents
  * [1 Identification][59138]
  * [2 Sunxi support][59139]
    * [2.1 Current status][59140]
    * [2.2 Manual build][59141]
    * [2.3 FEL mode][59142]
    * [2.4 Locating the UART][59143]
  * [3 Pictures][59144]

# Identification
The PCB has the following silkscreen on the front: 
[code] 
    CB4_V10
    20200303
[/code]
# Sunxi support
This is very much work in progress at this point. 
## Current status
No support yet in sunxi. 
## Manual build
The hello world from sunxi-tools works. The Orangepi 3 u-boot partly works, but fails to initialize the RAm and displays an message to that effect. With changes to the RAM settings it is possible to reach a u-boot shell with still some limited hardware support (no nand or ethernet). 
## FEL mode
It is possible to enter [ FEL][59145] mode by pressing the 2 key during the BOOT0 sequence, but due to the lack of an available USB port this is not useful, nor is it necessary as it is possible to boot directly from SD card anyway. 
## Locating the UART
The board breaks out a 4-pin header, labelled VCC, RX, GND, TX - do not connect the VCC header. This can be used with a Serial 3.3V TTL adapter at 115,200bps 8N1 to monitor the boot process. Except for the FEL interrupt, there is seemingly no other interaction possible from WhatsMiner-SDCard-Burn-Image-h6os-20220422.18.img firmware versions. 
# Pictures
  * [![][59146]][59134]
Front of the PCB 
  * [![][59147]][59148]
Back of the PCB
