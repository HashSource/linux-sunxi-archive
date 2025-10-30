# Allwinner A83TDevBoard
Allwinner A83TDevBoard  
---  
[![H8HomeletV20-A83T-Front.jpg][6406]][6407]  
Manufacturer |  [Allwinner][6408]  
Dimensions |  128 _mm_ x 67 _mm_  
Release Date |  May 2015   
Website |  N/A   
Specifications   
SoC |  [A83T][6409] @ XGhz   
DRAM |  1GiB DDR3 @ 672MHz ([Samsung K4B4G-1646D-BCK0][6410] * 2)   
NAND |  8GB eMMC (FORESEE NCFSESA8-08G)   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI Type A, CVBS   
Audio |  HDMI, RCA   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8189ETV][6411]), 10/100Mbps Ethernet ([X-Powers AC200][6412])   
Storage |  µSD   
USB |  1 USB2.0 OTG (host mode), 1 USB2.0 EHCI/OHCI   
Headers |  UART, IRDA   
This page needs to be properly filled according to the [New Device Howto][6413] and the [New Device Page guide][6414].
This is a limited edition product verification board that is used here for the purpose of mainline support of the A83T SoC. 
## Contents
  * [1 Identification][6415]
  * [2 Sunxi support][6416]
    * [2.1 Current status][6417]
    * [2.2 Images][6418]
    * [2.3 HW-Pack][6419]
    * [2.4 BSP][6420]
    * [2.5 Manual build][6421]
    * [2.6 Mainline U-Boot][6422]
    * [2.7 Mainline kernel][6423]
  * [3 Tips, Tricks, Caveats][6424]
    * [3.1 FEL mode][6425]
  * [4 Adding a serial port][6426]
    * [4.1 Device disassembly][6427]
    * [4.2 Locating the UART][6428]
  * [5 Pictures][6429]
  * [6 Also known as][6430]
  * [7 See also][6431]
    * [7.1 Manufacturer images][6432]

# Identification
On the front of the board, the following is printed: 
[code] 
    H8_HOMLET_PROTO_V2_0
    20141015 L4
[/code]
The PCB has the following silkscreened on it: 
[code] 
    TEAN-E120399 
    94V-OML1
[/code]
These markings do not have specific significance to the A83T since this is a product verification board. 
# Sunxi support
## Current status
There is ongoing discussion at [https://groups.google.com/forum/#!topic/linux-sunxi/_woM2vJmcuc][6433] regarding the mainline support of the SoC in this board. 
## Images
## HW-Pack
## BSP
The repository at <https://github.com/allwinner-zh/bootloader> contains 
  * BSP for the A83T, <https://github.com/allwinner-zh/bootloader/tree/master/basic_loader/bsp/bsp_for_a83>

## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][6434]

Everything else is the same as the [manual build howto][6435]. 
## Mainline U-Boot
For [ building mainline U-Boot][6436], use the 'h8_homlet_v2_defconfig' target. 
  

The reference source code from Allwinner is at <https://github.com/allwinner-zh/bootloader> contains 
  * Boot 0 source code for the A83T, <https://github.com/allwinner-zh/bootloader/tree/master/basic_loader/boot0>
  * U-boot 2011.09 for the A83T, <https://github.com/allwinner-zh/bootloader/tree/master/u-boot-2011.09>

## Mainline kernel
Basic support is available in mainline kernel for A83T. 
Use sun8i-a83t-allwinner-h8homlet-v2.dtb device-tree tree binary. 
There is a 3.4 source tree for the A83T at <https://github.com/allwinner-zh/linux-3.4-sunxi/tree/A83T>
# Tips, Tricks, Caveats
The following table is a comparison of the A83T SoC to other SoCs from the A-series. 
Module | Description   
---|---  
CPU | Cortex-A7 MP4 in 2 clusters, the MCPM is more likely as the A80   
CCI400 | It's same as the A80   
DRAMM | It's more likely as the A80   
Timer | It's same as the A31 and A20   
CCU | It's more likely as the A80   
DMA | It's same as the A31   
PinCtrl | It's same as the A31   
UART | It's same as the A31 and A20   
RSB | It's same as the A80 and A33   
SPI | It's same as the A31 and A20   
TWI | It's same as the A31 and A20   
NAND | It's more likely as the A80 and A33, but the clk/dma/pin are different   
SD/eMMC | It's same as the A31 and A20   
USB2.0 OTG | It's same as the A31 and A20   
USB HCI | It's same as the A31 and A20   
USB HSIC | It's same as the A80   
GMAC | It's a new IP, is more different of the platform before   
Security Engine | It's same as the A80   
Display Engine | It's a new IP, is more different of the platforms before   
Source: Kevin@Allwinner 
The following image shows the description of the modules on the board. 
  * [![][6437]][6438]
Description of modules on the board 

## FEL mode
To enter into [ FEL mode][6439], 
  1. connect the serial console
  2. keep pressing the 2 key in the serial console and at the same time switch on the board

# Adding a serial port
[![][6440]][6441]
[][6442]
A83T Produce verification board UART pads
The UART is located at the bottom-right of the board. The above image shows the location of GND, TX and RX. See more at the [UART howto][6443]. 
## Device disassembly
## Locating the UART
The UART is located at the bottom-right of the board. 
# Pictures
  * [![H8HomeletV20-A83T-Front.jpg][6444]][6407]
  * [![H8HomeletV20-A83T-Back.jpg][6445]][6446]

# Also known as
# See also
  * [Datasheet and User Guide][6447]
  * [Linux 3.4 kernel source code][6448]
  * [U-boot 2011.09 source code][6449]
  * [Boot0 source code][6450]
  * [BSP configuration][6451]

## Manufacturer images
  * [Linux image][6452] (81MB, SHA-256 hash: 72fdb9a18c0b9bd81fbdcc6fd486e521def625e20b089ae3a3a2f96ff5d8c99c)
  * [Android image][6453] (333MB, SHA-256 hash: 8239dd7db83cd578c0f0bd3de6dca884fa01333e32c1885e5b5bb1755281ceb3)
