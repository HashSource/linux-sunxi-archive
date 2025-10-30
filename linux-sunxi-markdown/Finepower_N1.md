# Finepower N1
Finepower N1  
---  
[![FinePower N1-1.jpg][19521]][19522]  
Manufacturer |  [Finepower][19523]  
Dimensions |  193 _mm_ x 115 _mm_ x 10.4 _mm_  
Release Date |  2017   
Website |  [Device Product Page][19524]  
Specifications   
SoC |  [A33][19525] @ 1.2Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 2200mAh 3.7V Li-Ion battery   
Features   
LCD |  7" 1024x600   
Touchscreen |  X-finger capacitive/resistive ([Hynitron CST2XX][19526])   
Video |  LCD   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([RTL8703BS][19527])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][19528])   
## Contents
  * [1 Identification][19529]
  * [2 Sunxi support][19530]
    * [2.1 Current status][19531]
      * [2.1.1 Android modules][19532]
    * [2.2 Manual build][19533]
      * [2.2.1 U-Boot][19534]
        * [2.2.1.1 Mainline U-Boot][19535]
      * [2.2.2 Linux Kernel][19536]
        * [2.2.2.1 Mainline kernel][19537]
    * [2.3 FEL mode][19538]
  * [3 Adding a serial port (**voids warranty**)][19539]
    * [3.1 Device disassembly][19540]
    * [3.2 Locating the UART][19541]
  * [4 Pictures][19542]
  * [5 See also][19543]

# Identification
On the back of the device, the following is printed: 
[code] 
    FinePower
    Model: N1
    Rev.2
[/code]
The PCB has the following silkscreened on it: 
[code] 
    TZX-723VC4
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _N1_
  * Build Number: _N1_R01_13.04.2018_V1.2_

# Sunxi support
## Current status
Supported under mainline u-boot and mainline kernel. 
##### Android modules
[code] 
    cst2xx 18173 0 - Live 0xbf331000
    sc7660 13524 0 - Live 0xbf329000
    cdc_ether 5099 0 - Live 0xbf323000
    rtl8150 9023 0 - Live 0xbf31c000
    mcs7830 6292 0 - Live 0xbf316000
    qf9700 7805 0 - Live 0xbf310000
    asix 17150 0 - Live 0xbf307000
    usbnet 17700 4 cdc_ether,mcs7830,qf9700,asix, Live 0xbf2fc000
    sunxi_keyboard 3021 0 - Live 0xbf2f8000
    sw_device 14991 0 - Live 0xbf2f0000
    vfe_v4l2 448072 0 - Live 0xbf268000
    s5k6aafx 21182 0 - Live 0xbf25e000
    bf3603 9619 0 - Live 0xbf257000
    sp2519 10857 0 - Live 0xbf250000
    sp0a19 11296 0 - Live 0xbf249000
    sp0838 10574 0 - Live 0xbf242000
    bf3920 9807 0 - Live 0xbf23b000
    bf3703 9570 0 - Live 0xbf234000
    siv121du 10782 0 - Live 0xbf22d000
    gc2155 12592 0 - Live 0xbf225000
    gc2145 12536 0 - Live 0xbf21d000
    gc2035 12824 0 - Live 0xbf215000
    gc0309 10622 0 - Live 0xbf20e000
    gc0329 10478 0 - Live 0xbf207000
    gc0312 10535 0 - Live 0xbf200000
    gc0308 10822 0 - Live 0xbf1f9000
    gc0328 10687 0 - Live 0xbf1f2000
    vfe_subdev 4771 17 vfe_v4l2,s5k6aafx,bf3603,sp2519,sp0a19,sp0838,bf3920,bf3703,siv121du,gc2155,gc2145,gc2035,gc0309,gc0329,gc0312,gc0308,gc0328, Live 0xbf1ed000
    vfe_os 3951 2 vfe_v4l2,vfe_subdev, Live 0xbf1e8000
    cci 21602 16 s5k6aafx,bf3603,sp2519,sp0a19,sp0838,bf3920,bf3703,siv121du,gc2155,gc2145,gc2035,gc0309,gc0329,gc0312,gc0308,gc0328, Live 0xbf1dc000
    videobuf_dma_contig 5567 1 vfe_v4l2, Live 0xbf1d7000
    videobuf_core 16520 2 vfe_v4l2,videobuf_dma_contig, Live 0xbf1cd000
    leds_sunxi 1359 0 - Live 0xbf1c9000
    mali 212058 20 - Live 0xbf181000 (O)
    lcd 116877 0 - Live 0xbf15f000
    disp 992768 8 mali,lcd, Live 0xbf058000
    nand 294363 8 - Live 0xbf000000 (O)
    
[/code]
## Manual build
You can build things for yourself by following our [ Manual build howto][19544] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the "q8_a33_tablet_1024x600_defconfig" build target. 
### Linux Kernel
#### Mainline kernel
Use the "sun8i-a33-q8-tablet.dtb" device-tree binary.  
  
**Wi-Fi** kernel module: <https://github.com/Icenowy/rtl8723cs/tree/new-driver-by-megous>  
Tested with kernel **5.15.0-rc1-00014-g316346243be6**  
How to compile:  

[code] 
    make -C [KERNEL_PATH] ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- M="$(pwd)" modules \
    CONFIG_RTL8723CS=m
    
[/code]
For turn off power save execute: 
[code] 
    echo 'options 8723cs rtw_power_mgnt=0 rtw_enusbss=0' | sudo tee /etc/modprobe.d/8723cs.conf
[/code]
**CONFIG_IPV6** must be **OFF** in kernel otherwise Wi-Fi driver will crash! 
## FEL mode
The something button triggers [ FEL mode][19545]. 
# Adding a serial port (**voids warranty**)
[![][19546]][19547]
[][19548]
UART pads near soc
There a two pads right of A33 chip. They are actually B0 and B1 pads of SOC. 
## Device disassembly
See [the Q8 tablet format disassembly page][19549]. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][19550].
# Pictures
  * [![FinePower N1-1.jpg][19551]][19522]
  * [![FinePower N1-3.jpg][19552]][19553]
  * [![FinePower N1-4.jpg][19554]][19555]
  * [![FinePower N1-5.jpg][19556]][19557]
  * [![FinePower N1-6.jpg][19558]][19559]

# See also
[Other Q8 format A33 based tablets.][19560]
