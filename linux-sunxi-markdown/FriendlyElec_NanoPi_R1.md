# FriendlyElec NanoPi R1
FriendlyElec NanoPi R1  
---  
[![Device front.jpg][21335]][21336]  
Manufacturer |  [FriendlyElec][21337]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  February 2019   
Website |  [Device Product Page][21338]  
Specifications   
SoC |  [H3][21339] @ 1.2Ghz   
DRAM |  512MiB/1GiB/ DDR3 @ ?MHz   
Power |  DC 5V @ 2A, via microUSB or pin headers   
Features   
Network |  WiFi ([AP6212][21340]), 1x10/100/1000Mbps Ethernet([Realtek RTL8211E][21341]), 1x 10/100 Ethernet([Realtek RTL8152B][21342]), Bluetooth 4.0   
Storage |  µSD, 8GB eMMC (optional)   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  RTC with battery   
Headers |  UART   
NanoPi R1 is a [H3][21339] based small form-factor router produced by [FriendlyARM][21343]. The R1 comes with integrated 1000 Mbps Ethernet, 100Mbps Ethernet, UART port, 802dot11 bgn WiFi, 2 x USB A 2.0, and a micro-SD card slot. It is normally sold in a black metal case 
## Contents
  * [1 Identification][21344]
  * [2 Sunxi support][21345]
    * [2.1 Current status][21346]
    * [2.2 Images][21347]
    * [2.3 HW-Pack][21348]
    * [2.4 BSP][21349]
    * [2.5 Manual build][21350]
      * [2.5.1 U-Boot][21351]
        * [2.5.1.1 Sunxi/Legacy U-Boot][21352]
        * [2.5.1.2 Mainline U-Boot][21353]
      * [2.5.2 Linux Kernel][21354]
        * [2.5.2.1 Sunxi/Legacy Kernel][21355]
        * [2.5.2.2 Mainline kernel][21356]
  * [3 Tips, Tricks, Caveats][21357]
    * [3.1 FEL mode][21358]
    * [3.2 Device specific topic][21359]
    * [3.3 ...][21360]
  * [4 Adding a serial port][21361]
    * [4.1 Device disassembly][21362]
    * [4.2 Locating the UART][21363]
  * [5 Pictures][21364]
  * [6 See also][21365]
    * [6.1 Manufacturer images][21366]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    FRIENDLY
    ELEC
    NanoPi R1
[/code]
# Sunxi support
## Current status
The H3 SoC support has matured since its introduction in kernel 4.2. Most of the board functionality for boards such as {{{board}}} are available with current mainline kernels. Some features (hw accelerated crypto, hw spinlocks, and thermal) are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][21367]. In addition, legacy 3.4 kernels are available in various work-in-progress git branches. 
See the [Manual build][21350] section for more details. 
  

  

## Images
FriendlyARM's UbuntuCore and OpenWrt images based on 4.14 kernel can be found [here][21368]. Armbian images for R1 based on 5.15 kernel can be found [here][21369]
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
FriendlyARM provides a BSP based on a newer Allwinner 4.14 variant [here][21370]
## Manual build
You can build things for yourself by following our [ Manual build howto][21371] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][21372] file. 
#### Mainline kernel
The dts is not mainline but it is available here: <https://github.com/armbian/build/blob/master/patch/kernel/sunxi-dev/xxx-add-nanopi-r1-and-duo2.patch>
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][21373]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port
[![][21374]][21375]
[][21376]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][21377]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
This device comes preassembled in a metal case. For ease of disassembly, remove the antenna, then undo the four screws holding the antenna-end plate to the body. (The antenna connector may catch on the plate if you try to remove the board from the ethernet end.) The board will then slide out of the case. To reassemble, line up the edges of the heat sink and board with the rails in the case body and slide the board back in. Reattach the plate and antenna. 
## Locating the UART
Three-pin UART0 header is placed next to between the micro-USB and WAN ports. Pinout: GND, TX, RX. Pin 1 (GND) is the one closest to the board edge. Logic voltage is 3.3V. For more instructions refer to our UART Howto. 
# Pictures
Take some pictures of your device, [ upload them][21378], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][21379]][21336]
  * [![Device back.jpg][21380]][21381]
  * [![Device buttons 1.jpg][21382]][21383]
  * [![Device buttons 2.jpg][21384]][21385]
  * [![Device board front.jpg][21386]][21387]
  * [![Device board back.jpg][21388]][21389]

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
