# Tanix TX6s
Tanix TX6s  
---  
[![Tanix TX6S front.jpg][54446]][54447]  
Manufacturer |  [Tanix][54448]  
Dimensions |  width 113 _mm_ (including antenna - 100 _mm_ excluding the antenna) x breadth 100 _mm_ x height 20 _mm_ (100 _mm_ if antenna vertical)   
Release Date |  Late 2019   
Website |  [Tanix TX6s Product Page][54449]  
Specifications   
SoC |  [H616][54450] @ 1.51Ghz   
DRAM |  2/4GiB DDR3 @ 1600MHz, 8 * Micron D9PQL MT41K1G4RH-125:E   
Power |  DC 5V @ 2A   
Features   
Audio |  HDMI, SPDIF   
Network |  WiFi 802.11 a/b/g/n/ac ([Ampak AP6330][54451]), 10/100Mbps Ethernet ([Integrated H616 PHY][54452])   
Storage |  µSD, eMMC   
USB |  3 USB2.0 Host   
Other |  IRDA   
This page needs to be properly filled according to the [New Device Howto][54453] and the [New Device Page guide][54454].
## Contents
  * [1 Identification][54455]
  * [2 General Notes][54456]
  * [3 Sunxi support][54457]
    * [3.1 Current status][54458]
    * [3.2 Manual build][54459]
      * [3.2.1 U-Boot][54460]
        * [3.2.1.1 Mainline U-Boot][54461]
      * [3.2.2 Linux Kernel][54462]
        * [3.2.2.1 Mainline kernel][54463]
  * [4 Tips, Tricks, Caveats][54464]
    * [4.1 FEL mode][54465]
    * [4.2 Chips/ICs][54466]
    * [4.3 Device specific topic][54467]
  * [5 Adding a serial port (**voids warranty**)][54468]
    * [5.1 Device disassembly][54469]
    * [5.2 Locating the UART][54470]
  * [6 Pictures][54471]
  * [7 Also known as][54472]
  * [8 See also][54473]
    * [8.1 Manufacturer images][54474]

# Identification
On the back of the device, the following is printed, along with a serial number and mac address: 
[code] 
    Model: TX6S-H
[/code]
The PCB has the following silkscreened on it: 
[code] 
    CS_H616_TX6S_B4_V3.0
    20191218
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model: _TX6s_
  * Kernel version: _4.9.170 #10 Tue Dec 15:15:02 CST 2020_
  * Build: _cupid_p1-userdebug 10 QP1A.191105.004 eng.hanxia. 20201219.091846 test-keys_

# General Notes
The device is shipped with an eMMC with Android installed 
I have uploaded console logs to capture the starting point with this board. 
[u-boot 2021.04 environment (boot from TF)][54475]
[serial bootlog (Android)][54476]
[serial bootlog (minimyth2 - 20210529)][54477]
# Sunxi support
## Current status
The basis of the H616 SoC mainline effort has been included in 5.12. Preliminary Linux and Trusted Firmware patches are available and are in the process of being mainlined. H616 U-Boot support has been merged into v2021.04. The Tanix TX6s is not yet included in current 5.12 kernel. The sun50i-h616-tanix-tx6s.dts and tanix_tx6s_defconfig are in the process of being upstreamed. 
## Manual build
You can build things for yourself by following our [ Manual build howto][54478] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **tanix_tx6s_defconfig** build target. 
### Linux Kernel
#### Mainline kernel
Use the **sun50i-h616-tanix-tx6s.dtb** device-tree binary. 
# Tips, Tricks, Caveats
The PCB is mounted upside down in the case, so the connectors are all flipped over (USB, SD card, HDMI, Ethernet). 
## FEL mode
Left of the SD-card slot, there is a button (barely) visible through the ventilation slots. It triggers [ FEL mode][54479] mode when held down while resetting or powering up. On the PCB this button is not marked (there is another button not marked between SPDIF and the 2 USB 2.0 on the back). You will need a USB-A <-> USB-A cable for FEL mode. 
## Chips/ICs
Manufacturer | Part | Description | Kernel Config | Kernel Driver / Description | Specification   
---|---|---|---|---|---  
Allwinner | H616 | Allwinner H616 (sun50iw9p1) is a SoC that features a Quad-Core Cortex-A53 ARM CPU, and a Mali-G31 MP2 GPU from ARM |  |  |   
FPE | H16101MC | 10/100 Base-T Transformer Modules Compliant With IEEE 802.3 standards including Baseline Wander Compensation specification of 350 H OCL when biased a. | dwmac_sun8i |  |   
Ampak | SP6330-X |  |  | Android is using Dongle Host Driver, version 1.579.77.41.11 // NVRAM version: AP6330_NVRAM_V1.0_20121130 // nvram_ap6330.txt // fw_bcm40183b2_ag.bin // config_ap6330.txt // clm.blob // F1 signature read @0x18000000=0x16044330 // F1 signature OK, socitype:0x1 chip:0x4330 rev:0x4 pkg:0x0 // Firmware: wl0: Jan 6 2014 15:11:29 version 5.90.195.89.13 FWID 01-72f124c5 |   
Fuzhou Fuda Hisi Microelectronics Co., Ltd. | FD650B-S |  |  | fdhisi,fd650 // FD650: fd650_driver_init: FD650 Driver init. // FD650: NOTE: register_fd650_driver:::register fd650 driver success. Not yet upstream. See [https://lore.kernel.org/lkml/[email protected]/][54480] for discussions on LED/VFD upstream.  |   
Shenzhen X-Powers Technology Co., Ltd | AXP305 |  | AXP305_POWER | axp305 pmic support |   
Micron | 8 * D9PQL MT41K1G4RH-125:E | Package = (1G4) 1 Gig x 4 // Revision = (RH) 78-ball 9mm x 10.5mm FBGA // Speed Grade = (-125) = 1.25ns @ CL = 11 (DDR3-1600) // Target tRCD-tRP-CL = 11-11-11 // tRCD-tRP-CL (ns) = 13.75 // Revision = :E |  |  | 1.35V DDR3L SDRAM // 800 MHz   
SCY | sNAND E64GBIB62ABE00 / 2046-B1 110333 |  |  | While called sNAND, this is a 57.6 GiB eMMC. |   
## Device specific topic
This device uses DDR3L (not LPDDR3) memory! 
Device is also equipped with 4-digit 7-segment display, driven by FD650B-S chip. 
# Adding a serial port (**voids warranty**)
## Device disassembly
[![][54481]][54482]
[][54483]
Tanix TX6s remove top lid
There are no screws holding the plastic lid in place. 
To open the box, Gently slide a [plastic tool][54484] or a knife in the small gap around all edges of the box to eventually lift the top plate, releasing 9 plastic tabs in the holding the cover. I started on the front, and then with a little leverage (in the front centre) was able to disengage the clips on the sides, and finally the back. 
To remove the PCB, remove the 3 screws, then lift the side with the 7 segment display up, then gently pull this side the PCB up. This is allow you to then remove the PCB - the backside connectors somewhat protude into the backside of the case. 
## Locating the UART
[![][54485]][54486]
[][54487]
Tanix TX6s UART pads
[![][54488]][54489]
[][54490]
Tanix TX6s UART pads pcb v4.1
The UART pads are located beside the USB port on the side of board. They are marked as _TX_ , _RX_ and _GND_ on the PCB. Just attach some leads according to the [UART Howto][54491]. Speed is 152000. 
# Pictures
Take some pictures of your device, [ upload them][54492], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Tanix TX6s pcb top.jpg][54493]][54494]
  * [![Tanix TX6s pcb bottom.jpg][54495]][54496]
  * [![20220303 093711.jpg][54497]][54498]
  * [![TX6S 20220303 back.jpg][54499]][54500]
  * [![TX6S 20220303 side FEL.jpg][54501]][54502]
  * [![TX6S 20220303 UART.jpg][54503]][54489]
  * [![Device front.jpg][54504]][54505]
  * [![Device back.jpg][54506]][54507]

# Also known as
There is also the [TX6][54508] TV box, sometimes selling alongside the TX6s. It uses the H6 Allwinner chip versus the H616 Allwinner chip. 
  * Likely that the **TICTID T6 PRO** is the same hardware. - <http://www.oranth.com/product-3661-41850.html>

# See also
Add some nice to have links here. This includes related devices, and external links.
  * Oranth Product Webpage - <http://www.oranth.com/product-3661-5919-40967.html>
  * Detailed Review - <https://androidpctv.com/review-tanix-tx6s-opinion/>

## Manufacturer images
  * **Tanix-Box_com-TX6s_android10_20200730.img:** <https://drive.google.com/file/d/1xg1Awd8xH7DqSwfsZTZdbWM5stJyNU8J/view?usp=sharing>

  * **Tanix-Box_com-TX6s_full_ota_20200730.zip:** <https://drive.google.com/file/d/1dL5nXOxk-jqKGTEt-xLjNq6BaymSIP-c/view?usp=sharing>
