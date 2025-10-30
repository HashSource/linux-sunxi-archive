# Inet 86V
Inet 86V  
---  
[![Inet 86V front.jpg][26231]][26232]  
Manufacturer |  [iNet technology][26233]  
Dimensions |  190 _mm_ x 115 _mm_ x 9 _mm_  
Specifications   
SoC |  [A13][26234] @ 1.2GHz   
DRAM |  353MiB @ 432MHz   
NAND |  4GB   
Power |  5V @ ?A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][26235])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
  * [![][26236]][26232]
Tablet front 
  * [![][26237]][26238]
Tablet back 
  * [![][26239]][26240]
Tablet side 

  

## Contents
  * [1 Identification][26241]
    * [1.1 CPU-Z Information][26242]
    * [1.2 Access by adb][26243]
  * [2 Sunxi support][26244]
    * [2.1 Images][26245]
    * [2.2 Manual build][26246]
  * [3 UART][26247]
  * [4 See also][26248]

## Identification
In android, under Settings->About Tablet, you will find a build number that starts with `86V2` and Android version 4.0.4. 
Tablet dismantle and Board identification: 
[code] 
    iNET-86V-REV02
    2012-08-07 Zeng-gc
    
[/code]
  * [![][26249]][26250]
Board1 
  * [![][26251]][26252]
Board2 
  * [![][26253]][26254]
Board3 
  * [![INET-86V-REV02 front.jpg][26255]][26256]
  * [![INET-86V-REV02 back.jpg][26257]][26258]

  

### CPU-Z Information
[code] 
    Model: 28126 (nuclear_evb)
    Manufacturer: unknown
    Board: nuclear
    Hardware: sun5i
    
[/code]
  * [![][26259]][26260]
CPU-Z page1 
  * [![][26261]][26262]
CPU-Z page2 
  * [![][26263]][26264]
CPU-Z page3 

  

### Access by adb
root@android:/ # cat /proc/cpuinfo 
[code] 
      Processor       : ARMv7 Processor rev 2 (v7l)
      BogoMIPS        : 1001.88
      Features        : swp half thumb fastmult vfp edsp neon vfpv3
      CPU implementer : 0x41
      CPU architecture: 7
      CPU variant     : 0x3
      CPU part        : 0xc08
      CPU revision    : 2
      Hardware        : sun5i
      Revision        : a13b
      Serial          : 03435cb039363030504d4e3316254217
    
[/code]
root@android:/ # cat /proc/partitions 
[code] 
     major minor  #blocks  name
      93        0      26384 nanda
      93        8      16384 nandb
      93       16      32768 nandc
      93       24     524288 nandd
      93       32    1228800 nande
      93       40      16384 nandf
      93       48      32768 nandg
      93       56     262144 nandh
      93       64     262144 nandi
      93       72    1472752 nandj
    
[/code]
root@android:/ # lsmod 
[code] 
     8188eu 621096 0 - Live 0xbf152000
     mxc622x 6326 1 - Live 0xbf14c000	-> G-sensor module
     mecs 4078 2 - Live 0xbf148000
     rtl8150 10305 0 - Live 0xbf141000
     mcs7830 7581 0 - Live 0xbf13b000
     qf9700 9152 0 - Live 0xbf134000
     asix 24601 0 - Live 0xbf128000
     sun5i_csi0 33271 0 - Live 0xbf11a000
     gt2005 36907 0 - Live 0xbf10a000
     gc0308 22312 1 - Live 0xbf100000	-> Camera module
     videobuf_dma_contig 6251 1 sun5i_csi0, Live 0xbf0fb000
     videobuf_core 20242 2 sun5i_csi0,videobuf_dma_contig, Live 0xbf0f1000
     cedarx 9351 0 - Live 0xbf0ea000
     mali 150956 6 - Live 0xbf0b8000
     ump 49278 9 mali, Live 0xbf0a4000
     st1536_ts 21173 0 - Live 0xbf088000
     gsl1680 177199 0 - Live 0xbf057000
     pixcir_touch_811 23383 0 - Live 0xbf04c000
     gt811 17146 0 - Live 0xbf043000
     byd693x_ts 9094 0 - Live 0xbf033000
     zet622x 19182 0 - Live 0xbf025000
     ssd253x_ts 22661 0 - Live 0xbf01b000
     ft5x_ts 51435 7 st1536_ts,gsl1680,pixcir_touch_811,gt811,byd693x_ts,zet622x,ssd253x_ts, Live 0xbf000000
    
[/code]
root@android:/ # getevent 
[code] 
     add device 1: /dev/input/event5
      name:     "ecompass_data"
     add device 2: /dev/input/event4
      name:     "sitronix_ts"
     add device 3: /dev/input/event3		-> Touchscreen module
      name:     "gsl1680"
     add device 4: /dev/input/event2		-> Touchscreen module
      name:     "gt811"
     add device 5: /dev/input/event0
      name:     "sun4i-keyboard"
     could not get driver version for /dev/input/mice, Not a typewriter
     add device 6: /dev/input/event1
      name:     "axp20-supplyer"
    
[/code]
## Sunxi support
### Images
[This Debian image][26265] for [A13-OLinuXino][26266] with Hynix DDR3 RAM boots and works well except for the touchscreen. 
### Manual build
Mainline U-Boot can be compiled for this tablet using the A13-OLinuXino_defconfig. For the LCD to work, edit the .config file to add the LCD config for [Inet 86vs][26267] from this page: [LCD][26268].  
Otherwise, follow the [Manual build howto][26269]. 
## UART
[![][26270]][26271]
[][26272]
UART pads on the bottom of [Inet 86vs][26267]
As in all other A13 boards, you cannot use microSD and UART at the same time. You have to [boot from USB][26273] instead.  
Consider using a [MicroSD Breakout][26274] to avoid soldering. Alternatively, the Rx/Tx pads are right next to the SD card socket on the top, or in the same place on the bottom (in the same layout as in the [Inet 86vs][26267] but unlabeled).  
UART is disabled and configured completely wrong in the default script.bin file, so instead of the testing method suggested in the [UART][26275] guide, you'll need to boot [uart0-helloworld-sdboot.sunxi][26276] from USB: 
[code] 
    sudo sunxi-fel -v uboot uart0-helloworld-sdboot.sunxi
    
[/code]
## See also
  * [Inet 86vs][26267]
