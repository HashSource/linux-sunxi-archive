# Wexler TAB A720
Wexler TAB A720  
---  
[![Wexler TAB A720-1.jpg][59060]][59061]  
Manufacturer |  [Wexler][59062] (dead link)   
Dimensions |  194 _mm_ x 114 _mm_ x 9 _mm_  
Release Date |  November 2014   
Website |  [Device Product Page][59063]  
Specifications   
SoC |  [A23][59064] @ 1.5Ghz   
DRAM |  512MiB DDR3 @ 240MHz   
NAND |  4GB   
Power |  USB, 2500mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  X-finger capacitive/resistive ([Silead GSL1680][59065])   
Video |  LCD   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Espressif ESP8089][59066])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
## Contents
  * [1 Identification][59067]
  * [2 Sunxi support][59068]
    * [2.1 Current status][59069]
      * [2.1.1 Tested and working with patches:][59070]
      * [2.1.2 Working but with problems:][59071]
      * [2.1.3 Not working:][59072]
      * [2.1.4 Android modules][59073]
    * [2.2 Manual build][59074]
      * [2.2.1 U-Boot][59075]
        * [2.2.1.1 Mainline U-Boot][59076]
      * [2.2.2 Linux Kernel][59077]
        * [2.2.2.1 Mainline kernel][59078]
    * [2.3 FEL mode][59079]
  * [3 Adding a serial port (**voids warranty**)][59080]
    * [3.1 Device disassembly][59081]
    * [3.2 Locating the UART][59082]
  * [4 Pictures][59083]

# Identification
On the back of the device, the following is printed: 
[code] 
    WEXLER.TAB A720
[/code]
The PCB has the following silkscreened on it: 
[code] 
    A23_M7085_L_V02
    2014_C5_29
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _TAB A720_
  * Build Number: _TAB A720_20141115_3.2.0_INT_

# Sunxi support
## Current status
Unsupported in mainline kernel, mostly because of non-standard LCD (but really i don't know).  
Patches for kernel and U-Boot can be found in this repository: <https://gitlab.com/ariarolin/sunxi-wexler-tab-a720>   

##### Tested and working with patches:
Display  
U-Boot v2021.07  
Kernel 5.14.0 (commit 78e709522d2c012cb0daad2e668506637bffb7c2)  
DTB  
SDcard  
USB OTG  
Brightness  
Hardware keys  
Mali / lima (GPU)  
Audio (by default speaker is off, enable it by uncommenting in device tree)   
Touchscreen (use this firmware <https://gitlab.com/ariarolin/sunxi-wexler-tab-a720/-/blob/master/firmware/gsl1680-wexler-taba720.fw>)   
(my xorg.conf.d (calibration) for touchscreen is here: <https://gitlab.com/ariarolin/sunxi-wexler-tab-a720/-/tree/master/touchscreen_config/xorg.conf.d>)  

##### Working but with problems:
Wifi - use this kernel module <https://github.com/Icenowy/esp8089/tree/cleanup> (Known problem - cannot connect to hidden SSID, not tested with normal)  

##### Not working:
Cedrus (hardware media acceleration)  
Rotation  
Accelerometer (it's mxc622x, no known driver for mainline)  
Camera  
  
Problems encountered:  

  1. Kernel 5.14.0 does not shutdown fully (screen is off but power is on) (on 5.8.0 all OK)

##### Android modules
[code] 
    gslX680new 134112 0 - Live 0x00000000 (F)
    mxc622x 4025 0 - Live 0x00000000
    rtl8150 8115 0 - Live 0x00000000
    mcs7830 4948 0 - Live 0x00000000
    qf9700 5188 0 - Live 0x00000000
    asix 12322 0 - Live 0x00000000
    sunxi_keyboard 2749 0 - Live 0x00000000
    sw_device 12200 0 - Live 0x00000000
    vfe_v4l2 217660 0 - Live 0x00000000
    gc0308 9360 1 - Live 0x00000000
    vfe_subdev 3827 2 vfe_v4l2,gc0308, Live 0x00000000
    vfe_os 3175 2 vfe_v4l2,vfe_subdev, Live 0x00000000
    cci 2954 1 gc0308, Live 0x00000000
    videobuf_dma_contig 3821 1 vfe_v4l2, Live 0x00000000
    videobuf_core 15500 2 vfe_v4l2,videobuf_dma_contig, Live 0x00000000
    leds_sunxi 1279 0 - Live 0x00000000
    mali 179969 15 - Live 0x00000000 (O)
    lcd 7184 0 - Live 0x00000000
    disp 1045213 8 mali,lcd, Live 0x00000000
    nand 256473 8 - Live 0x00000000 (O)
    
[/code]
## Manual build
You can build things for yourself by following our [ Manual build howto][59084] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
**For unknown reason, git u-boot is not working with tablet, use v2021.07 release**  
First, apply this patch: <https://gitlab.com/ariarolin/sunxi-wexler-tab-a720/-/blob/master/patches/U-BOOT_0001-Add-Wexler-TAB-A720-support.patch>  
Then, use the _Wexler_TAB_A720_defconfig_ build target. 
### Linux Kernel
#### Mainline kernel
First, apply this patch: <https://gitlab.com/ariarolin/sunxi-wexler-tab-a720/-/blob/master/patches/LINUX_0001-Add-Wexler-TAB-A720-support.patch>  
Then, use the _sun8i-a23-wexler-tab-a720.dtb_ device-tree binary. 
## FEL mode
With SD card: [https://linux-sunxi.org/FEL#Through_a_special_SD_card_image][59085]  
I do not tried search FEL buttons. 
# Adding a serial port (**voids warranty**)
[![][59086]][59087]
[][59088]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][59089]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
See [the Q8 tablet format disassembly page][59090]. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][59089].
# Pictures
  * [![Wexler TAB A720-1.jpg][59091]][59061]
  * [![Wexler TAB A720-2.jpg][59092]][59093]
  * [![Wexler TAB A720-3.jpg][59094]][59095]
  * [![Wexler TAB A720-4.jpg][59096]][59097]
  * [![Wexler TAB A720-5.jpg][59098]][59099]
