# Icoo d50
Icoo d50  
---  
[![ICOO front.JPG][25398]][25399]  
Manufacturer |  [ICOO][25400]  
Dimensions |  180 _mm_ x 12 _mm_ x 115 _mm_  
Release Date |  May 2012   
Website |  [ICOO D50][25401]  
Specifications   
SoC |  [A13][25402] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz   
NAND |  4GB   
Power |  DC 5V @ 3A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Goodix GT811][25403])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188CTV)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][25404] FIXME)   
Headers |  UART   
## Contents
  * [1 Identification][25405]
  * [2 Sunxi support][25406]
    * [2.1 Current status][25407]
    * [2.2 Images][25408]
    * [2.3 HW-Pack][25409]
    * [2.4 BSP][25410]
    * [2.5 Manual build][25411]
  * [3 Tips, Tricks, Caveats][25412]
    * [3.1 FEL mode][25413]
  * [4 Adding a serial port (**voids warranty**)][25414]
    * [4.1 Device disassembly][25415]
    * [4.2 Locating the UART][25416]
  * [5 Pictures][25417]
  * [6 Also known as][25418]
  * [7 See also][25419]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: A13-EVB
  * Build Number: nuclear_D50_sc3038n-eng 4.0.4 IMM76D 20120801 test-keys

# Sunxi support
## Current status
Awaiting patches. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Icoo_d50" target.
  * The .fex file can be found in sunxi-boards as [icoo_d50.fex][25420]

Everything else is the same as the [manual build howto][25421]. 
# Tips, Tricks, Caveats
## FEL mode
The home/back button triggers [ FEL mode][25422]. There is also a hard [FEL][25422] button labelled _Boot_ behind the hole for the microphone. 
# Adding a serial port (**voids warranty**)
[![][25423]][25424]
[][25425]
UART pads
## Device disassembly
The back cover needs to be gently pushed outwards with your [Plastic Tool][25426]. Be careful though, as the LCD and Touchpanel ribbons are short. 
## Locating the UART
On the back of the PCB, there are pads labelled "RX" and "TX". All you have to do is solder on some wires according to our [UART howto][25427]. 
# Pictures
  * [![ICOO front.JPG][25428]][25399]
  * [![ICOO back.JPG][25429]][25430]
  * [![ICOO buttons.JPG][25431]][25432]
  * [![ICOO ports.JPG][25433]][25434]
  * [![ICOO inside.JPG][25435]][25436]
  * [![ICOO board.JPG][25437]][25438]
  * [![ICOO board back.JPG][25439]][25440]

# Also known as
# See also
  * [icoo_d50.fex][25441], which awaits submission.
  * [Touch screen driver][25442]
