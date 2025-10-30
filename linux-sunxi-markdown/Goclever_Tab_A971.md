# Goclever Tab A971
Goclever Tab A971  
---  
[![Device front.jpg][22148]][22149]  
Manufacturer |  [GOCLEVER Technology Co Ltd.][22150]  
Dimensions |  243.5 _mm_ x 188 _mm_ x 12 _mm_  
Release Date |  2012   
Website |  [Archived product Page][22151]  
Specifications   
SoC |  [A10][22152] @ 1Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  8GB   
Power |  DC 5V @ 3A, 6000mAh 3.7V Li-Po battery   
Features   
LCD |  1024x768 (9.7" 16:9)   
Touchscreen |  5-finger capacitive ([FocalTech FT5406EE8][22153])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][22154])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Freescale MMA7660][22155]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][22156] and the [New Device Page guide][22157].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Hardware][22158]
  * [2 Identification][22159]
  * [3 Sunxi support][22160]
    * [3.1 Current status][22161]
    * [3.2 Images][22162]
    * [3.3 HW-Pack][22163]
    * [3.4 BSP][22164]
    * [3.5 Manual build][22165]
      * [3.5.1 U-Boot][22166]
        * [3.5.1.1 Sunxi/Legacy U-Boot][22167]
        * [3.5.1.2 Mainline U-Boot][22168]
      * [3.5.2 Linux Kernel][22169]
        * [3.5.2.1 Sunxi/Legacy Kernel][22170]
        * [3.5.2.2 Mainline kernel][22171]
  * [4 Tips, Tricks, Caveats][22172]
    * [4.1 FEL mode][22173]
    * [4.2 Memory info][22174]
    * [4.3 ...][22175]
  * [5 Adding a serial port (**voids warranty**)][22176]
    * [5.1 Device disassembly][22177]
    * [5.2 Locating the UART][22178]
  * [6 Pictures][22179]
  * [7 Also known as][22180]
  * [8 See also][22181]
    * [8.1 Manufacturer images][22182]

# Hardware
  * Mainboard - m101-A10-cpt
  * Accelerometer - [Freescale MMA7660][22183]
  * WIFI - [Realtek RTL8188CUS][22154]
  * Touchscreen - [FocalTech FT5406EE8][22153]
  * LCD - LG LP097X02-SLQA
  * Front camera - GC0308

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: GOCLEVER TAB A971
  * Build Number: crane_m97ft5xgoclever766-eng 4.0.3 IML74 20120816 test-keys

# Sunxi support
Works well with cubieboard 1 files 
## Current status
Work in progress 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][22181]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][22184] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][22185] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][22186]. 
## Memory info
[code] 
    dram_baseaddr = 0x40000000
    dram_clk = 432
    dram_type = 3
    dram_rank_num = 1
    dram_chip_density = 2048
    dram_io_width = 8
    dram_bus_width = 32
    dram_cas = 6
    dram_zq = 0x7b
    dram_odt_en = 0
    dram_size = 1024
    dram_tpr0 = 0x30926692
    dram_tpr1 = 0x1090
    dram_tpr2 = 0x1a0c8
    dram_tpr3 = 0x0
    dram_tpr4 = 0x0
    dram_tpr5 = 0x0
    dram_emr1 = 0x4
    dram_emr2 = 0x0
    dram_emr3 = 0x0
    
[/code]
## ...
# Adding a serial port (**voids warranty**)
[![][22187]][22188]
[][22189]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][22190]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][22191].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][22190].
# Pictures
Take some pictures of your device, [ upload them][22192], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][22193]][22149]
  * [![Device back.jpg][22194]][22195]
  * [![Device buttons 1.jpg][22196]][22197]
  * [![Device buttons 2.jpg][22198]][22199]
  * [![Device board front.jpg][22200]][22201]
  * [![Device board back.jpg][22202]][22203]

# Also known as
  * Mediacom SmartPad 910i (1:1)

# See also
  * [Cubian for A10 Tablets][22204] \- debian 7, works almost out of the box, to enable touch - modprobe tf5x_ts, there are instructions inside to enable wifi.
  * [Minimal Debian "Server" image for the Allwinner A10][22205] \- debian 8, boots in text mode but keyboard don't works
  * [Upgrading cubian to latest debian version][22206] \- update cubian to version 8 (edit script otherwise it will set locale to RU)
  * [Armbian][22207] \- debian buster or ubuntu focal, works with ssh (edit file /boot/armbian_first_run.txt.template to connect to wifi), video only via HDMI, usb keyboard works (needs DTS edit, wip).

## Manufacturer images
Optional. Add non-sunxi images in this section.
