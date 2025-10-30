# GoClever Tab A73
GoClever Tab A73  
---  
[![Device front.jpg][22038]][22039]  
Manufacturer |  [GOCLEVER Technology Co Ltd.][22040]  
Dimensions |  192 _mm_ x 122 _mm_ x 12 _mm_  
Release Date |  November 2011   
Website |  [Archived product Page][22041]  
Specifications   
SoC |  [A10][22042] @ 1Ghz   
DRAM |  512MiB DDR3 @ 384MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 3400mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([FocalTech FT5306DE4][22043])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8192CUS][22044])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([MMA7660][22045] or [MXC622X][22046]), vibration motor.   
Headers |  UART, JTAG   
This page needs to be properly filled according to the [New Device Howto][22047] and the [New Device Page guide][22048].
libv> there seem to be 3 different board versions, but no pictures of any boards are apparently available. I fear that this device will end up being a rebadger of either a [A710][22049] or [A721][22050].
## Contents
  * [1 Different motherboard versions][22051]
  * [2 Identification][22052]
  * [3 Sunxi support][22053]
    * [3.1 Current status][22054]
    * [3.2 Images][22055]
    * [3.3 HW-Pack][22056]
    * [3.4 BSP][22057]
    * [3.5 Manual build][22058]
  * [4 Tips, Tricks, Caveats][22059]
    * [4.1 FEL mode][22060]
    * [4.2 Touchscreen][22061]
    * [4.3 meminfo][22062]
    * [4.4 FEX][22063]
  * [5 Adding a serial port (**voids warranty**)][22064]
    * [5.1 Device disassembly][22065]
    * [5.2 Locating the UART][22066]
  * [6 Pictures][22067]
    * [6.1 V1][22068]
    * [6.2 V2][22069]
    * [6.3 V3][22070]
  * [7 Also known as][22071]
  * [8 See also][22072]

# Different motherboard versions
There were 3 hardware versions (HwvX) released by GoClever. They have a different PCB, camera or g-sensor: 
Hardware version  | Serial numbers  | Camera module  | G-sensor (module)  | Available Android versions (official)   
---|---|---|---|---  
HWv1  | GCA731111XXXX  | GC0308  | [ MMA7660][22045] | 2.3.4, 4.0.3   
HWv2  | GCA731201xxxx - GCA731205xxxx  | SP0838  | [ MXC622X][22046] | 2.3.4, 4.0.3   
HWv3  | GCTA731206xxxx  | GC0308  | [ MXC622X][22046] | 4.0.4   
GCTA731207XXXX is made with the parts that were in stock - there are some components from HWv2. and some from HWv3. 
# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: GOCLEVER TAB A73
  * Build Number: crane_evb-eng 4.0.3 IML74K 20120504 test-keys

# Sunxi support
## Current status
Unsupported. No patches were ever submitted. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][22073]

Everything else is the same as the [manual build howto][22074]. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][22075]. 
## Touchscreen
In most situations, you will need to disable multitouch on the FT5X touchscreen driver (for instance, by commenting out CONFIG_FT5X0X_MULTITOUCH in drivers/input/touchscreen/ft5x_ts.h). 
The kernel for HWv2 has a working driver. 
## meminfo
[code] 
    dram_clk = 384
    dram_type = 3
    dram_rank_num = 1
    dram_chip_density = 2048
    dram_io_width = 16
    dram_bus_width = 32
    dram_cas = 6
    dram_zq = 0x7c
    dram_odt_en = 0
    dram_tpr0 = 0x30926692
    dram_tpr1 = 0x1090
    dram_tpr2 = 0x1a0c8
    dram_tpr3 = 0x0
    dram_emr1 = 0x4
    dram_emr2 = 0x0
    dram_emr3 = 0x0
[/code]
This was not turned into a u-boot patch yet. 
## FEX
  * [FEX for GCA731201xxxx][22076].
  * [FEX for GCA73 1111xxxx][22077] and [A721][22050].

# Adding a serial port (**voids warranty**)
[![][22078]][22079]
[][22080]
DEVICE UART pads
## Device disassembly
Remove the 4 screws. Now gently push your [Plastic tool][22081] between the plastic outer edge and the metal back cover. Try to go around the whole board until you hear some clips pop, and do this until all clips have released. Be careful when opening the device, as the Wifi antenna is taped to the back cover. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][22082].
# Pictures
## V1
Take some pictures of your device, [ upload them][22083], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][22084]][22039]
  * [![Device back.jpg][22085]][22086]
  * [![Device buttons 1.jpg][22087]][22088]
  * [![Device buttons 2.jpg][22089]][22090]
  * [![Device board front.jpg][22091]][22092]
  * [![Device board back.jpg][22093]][22094]

## V2
  * [![Goclever tab a73 v2 front.jpg][22095]][22096]
  * [![Goclever tab a73 v2 back.jpg][22097]][22098]
  * [![Goclever tab a73 v2 connectors.jpg][22099]][22100]
  * [![Goclever tab a73 v2 hw buttons.jpg][22101]][22102]
  * [![Goclever tab a73 v2 capacitive buttons.jpg][22103]][22104]
  * [![Goclever tab a73 v2 internal.jpg][22105]][22106]
  * [![Goclever tab a73 v2 board back.jpg][22107]][22108]
  * [![Goclever tab a73 v2 board front.jpg][22109]][22110]

## V3
Take some pictures of your device, [ upload them][22083], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][22084]][22039]
  * [![Device back.jpg][22085]][22086]
  * [![Device buttons 1.jpg][22087]][22088]
  * [![Device buttons 2.jpg][22089]][22090]
  * [![Device board front.jpg][22091]][22092]
  * [![Device board back.jpg][22093]][22094]

# Also known as
  * Texet TM-7025 (1:1 clone of HWv1)
  * Vedia X7 (1:1 clone of HWv1)
  * Bmorn V11 (1:1 clone of HWv2)
  * Eken T02 (clone of HWv2/HWv3)
  * Saycool A720

# See also
  * [Polish forum post about increasing RAM][22111].
  * [All about GOCLEVER A73 (PL)][22112] \- for example HW versions, cameras and g-sensors
  * [ROMs and MODs for A73 (PL)][22113]
