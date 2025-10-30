# ET-Q8 A33
ET-Q8 A33  
---  
[![MID756 A33.jpg][17525]][17526]  
Manufacturer |  Unidentified manufacturer "ET"   
Dimensions |  182 _mm_ x 121 _mm_ x 7 _mm_  
Release Date |  November 2014   
Website |  Missing product page.   
Specifications   
SoC |  [A33][17527] @ ?.?Ghz   
DRAM |  512MiB DDR3 @ 384MHz (1x [P3P4GF4BLF-GDJ][17528])   
NAND |  4GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][17529])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([RDA Microelectronics RDA5990P][17530]),   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3 MP (640x480) front, 0.3 MP (640x480) rear   
Other |  Accelerometer ([Manufacturer device][17531])   
This page needs to be properly filled according to the [New Device Howto][17532] and the [New Device Page guide][17533].
A [Q8 style][17534] cheap tablet, but with an [A33][17527] SoC. 
## Contents
  * [1 Identification][17535]
  * [2 Sunxi support][17536]
    * [2.1 Current status][17537]
    * [2.2 Images][17538]
    * [2.3 HW-Pack][17539]
    * [2.4 BSP][17540]
    * [2.5 Manual build][17541]
    * [2.6 Mainline U-Boot][17542]
    * [2.7 Mainline kernel][17543]
  * [3 Tips, Tricks, Caveats][17544]
    * [3.1 FEL mode][17545]
    * [3.2 Retrieving script.bin][17546]
  * [4 Adding a serial port (**voids warranty**)][17547]
    * [4.1 Device disassembly][17548]
  * [5 Pictures][17549]
  * [6 See also][17550]

# Identification
On the back of the device, the following is printed: 
[code] 
    The PCB has the following written on it:
    ET_Q8_A23_A33_v1.6 
    140903
    
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: MID-756
  * Build Number: astar_rda-eng 4.4.2 KVT 49L 20141110 test-keys

# Sunxi support
## Current status
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][17551]

Everything else is the same as the [manual build howto][17552]. 
## Mainline U-Boot
## Mainline kernel
Use the _sun8i-a33-et-q8-v1.6.dts_ device-tree file for the [mainline kernel][17553]. 
# Tips, Tricks, Caveats
## FEL mode
The Volume+ button triggers [ FEL mode][17554]. 
## Retrieving script.bin
Unlike, other allwinner devices,Script.bin is not present in the vfat partition(nanda) as file. 
Instead, It is located 0x43000000, it's size is 0x00020000. script.bin can be extracted from /dev/mem using mmap(). 
# Adding a serial port (**voids warranty**)
There are no UART pads available on this device. Instead, UART0 is multiplexed with the microSD adapter. Please refer to the [MicroSD Breakout adapter][17555] for more information.. 
## Device disassembly
See [the Q8 tablet format disassembly page][17556]. 
# Pictures
  * [![ET Q8 V2.0-PCB.jpg][17557]][17558]

# See also
  * [Other Q8 format A33 based tablets.][17559]
