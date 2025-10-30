# Sinovoip Banana Pi M2 Ultra
(Redirected from [Banana Pi M2 Ultra][9226])
 
Banana Pi M2 Ultra is a [R40][9229] based development board produced by Sinovoip. 
**Despite its name, the M2 Ultra is incompatible to previous Banana Pi boards ([Banana Pi][9230]/[M1][9231]/[M1+][9232]/[Pro][9233]/[M2][9234]/[M2+][9235]/[M3][9236]/[M64][9237]), due to a different SoC - requiring different boot loaders and drivers.** It's another attempt to cash in on the Banana Pi's popularity with a SBC only sharing brand, name, ~~form factor~~ and GPIO header. 
  

Sinovoip Banana Pi M2 Ultra  
---  
[![Banana Pi M2 Ultra top.jpg][9238]][9239]  
Manufacturer |  [Sinovoip][9240]  
Dimensions |  92 _mm_ x 60 _mm_  
Release Date |  November 2016   
Website |  [BPI-M2U Product Page][9241]  
Specifications   
SoC |  [R40][9229] @ up to 1.2Ghz   
DRAM |  2GiB DDR3 @ 576MHz ([SKhynix H5TQ4G83AFR][9242] x4)   
NAND |  8GB eMMC 4.5 (Samsung KLM8G1WEMB-B031)   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive), Li-Ion battery connector available, (PMIC: AXP221S G9107BC 69V1)   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug, HDMI, internal microphone   
Network |  WiFi 802.11 b/g/n ([AMPAK AP6212][9243]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][9244])   
Storage |  µSD, SATA   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  IR   
Headers |  UART, LCD, Camera, Raspberry Pi 2 compatible header   
## Contents
  * [1 Identification][9245]
  * [2 Sunxi support][9246]
    * [2.1 Current status][9247]
    * [2.2 Images][9248]
    * [2.3 BSP][9249]
    * [2.4 Manual build][9250]
      * [2.4.1 U-Boot][9251]
        * [2.4.1.1 Mainline U-Boot][9252]
      * [2.4.2 Linux Kernel][9253]
        * [2.4.2.1 Mainline kernel][9254]
  * [3 Tips, Tricks, Caveats][9255]
    * [3.1 FEL mode][9256]
    * [3.2 LEDs][9257]
    * [3.3 SATA][9258]
    * [3.4 'Quality control' related problems][9259]
  * [4 Adding a serial port][9260]
    * [4.1 Locating the UART][9261]
  * [5 Pictures][9262]
  * [6 Also known as][9263]
  * [7 Variants][9264]
  * [8 See also][9265]
    * [8.1 Documents][9266]
    * [8.2 OS images][9267]

# Identification
The PCB has the following silkscreened on it along with a BananaPi logo: 
[code] 
    BPi-M2-Ultra
            V1.0
    
[/code]
# Sunxi support
## Current status
Banana Pi M2 Ultra is currently supported by both mainline U-Boot and kernels. 
## Images
[http://wiki.banana-pi.org/Banana_Pi_BPI-M2U#Image_Release][9268]
## BSP
<https://github.com/BPI-SINOVOIP/BPI-M2U-bsp/>
## Manual build
You can build things for yourself by following our [ Manual build howto][9269] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **Bananapi_M2_Ultra_defconfig** (supported since v2017.05) build target. 
### Linux Kernel
#### Mainline kernel
Use the **sun8i-r40-bananapi-m2-ultra.dtb** (supported since at least 4.15) device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The unlabeled surface mount button next to the UART pins triggers [ FEL mode][9270]. 
## LEDs
The board has 3 LEDs, in red, green and blue, conveniently labeled R, G, and B. The red LED also serves as the power LED by default. 
## SATA
The SATA port on this board provides _real_ SATA (no USB-to-SATA bridge used) but performance seems similar to A20 though (main limitation being not that great sequential write performance -- see [SATA page][9271] for details). The SATA power port is directly wired to DC-DC so connected disks will neither be powered when running on battery nor when users try to power BPi M2 Ultra through the Micro USB port. Without an appropriate PSU with 4.0mm/1.7mm barrel plug you can forget about powering a disk from the board. Please see also [troubleshooting powering issues][9272]. 
## 'Quality control' related problems
In case you experience HDMI or other problems with this board it's somewhat likely that the [QC sticker is reponsible for][9273] (_quality control_ seems to have a different meaning with this hardware vendor). 
# Adding a serial port
## Locating the UART
[![Banana Pi M2 Ultra uart.jpg][9274]][9275]
[][9276]
The UART pins are located in the bottom right corner, next to the RJ45 Ethernet port. They are marked as TX, RX and GND on the PCB. Just attach some leads according to our [UART howto][9277]. 
# Pictures
  * [![Banana Pi M2 Ultra top.jpg][9278]][9279]
  * [![Banana Pi M2 Ultra bottom.jpg][9280]][9281]
  * [![Banana Pi M2 Ultra 1024px.jpg][9282]][9283]

# Also known as
The marketing material (e.g. the [product page][9241]) also refers to the board as Banana Pi BPI-M2U. 
# Variants
Since around 2020 V1.1 is sold, which contains an A40i SOC. It uses PH23 for turning on USB-A power, which is NC on V1.0. There the USB-A ports are always powered, which can be checked turning on the SOCs without an SD card inserted. **CAVEAT:** Powering through micro USB will reset the board due to power starving while booting, as the axp221s is default configured for only 900mA. Use **i2c dev 0; i2c mw 34 30 63** at U-Boot cmdline to allow for more power. 
Also the 8GB eMMC changed chip hangs vanilla kernels up to at least 6.13, known workaround are disabling via DT or limit to 1 Bit transfers. The workaround is documented in [this forum thread][9284]. 
# See also
## Documents
  * [Schematics][9285] (now on 'google driver' and baidu)
  * Since customers asked in their forum the unusual 6 pin battery connector is now [documented somehow][9286]
  * Please be aware that 'information' on BPi M2 Ultra [Gitbook][9287] page is mostly copy&paste from other Banana Pi pages and might contain mistakes (count of LEDs and USB host ports wrong, DRAM clockspeed copied from BPi M3 and so on)

## OS images
[Official OS Images][9288]
