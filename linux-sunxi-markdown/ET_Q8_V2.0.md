# ET Q8 V2.0
ET Q8 V2.0  
---  
[![MID756 A33.jpg][17596]][17597]  
Manufacturer |  Unidentified manufacturer "ET"   
Dimensions |  182 _mm_ x 121 _mm_ x 7 _mm_  
Release Date |  21/11/2015   
Website |  Missing product page.   
Specifications   
SoC |  [A33][17598] @ ?.?Ghz   
DRAM |  512Mb DDR3@ 480MHz (2x [512X8DDR3 fake][17599])   
NAND |  16GB   
Power |  DC 5V @ 3A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][17600])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n and Bluetooth ([RTL8703AS][17601]),   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3 MP (640x480) front, 0.3 MP (640x480) rear   
Other |  Accelerometer ([Manufacturer device][17602])   
A [Q8 style][17603] cheap tablet, but with an [A33][17598] SoC. 
**Sell as 1Gb but fake android reporting!! Only 512Mb. Does not esist 1Gb q8 form factor tablet.**
## Contents
  * [1 Identification][17604]
  * [2 Sunxi support][17605]
    * [2.1 Current status][17606]
    * [2.2 Images][17607]
    * [2.3 HW-Pack][17608]
    * [2.4 BSP][17609]
    * [2.5 Manual build][17610]
    * [2.6 Mainline U-Boot][17611]
    * [2.7 Mainline kernel][17612]
  * [3 Tips, Tricks, Caveats][17613]
    * [3.1 FEL mode][17614]
    * [3.2 Retrieving script.bin][17615]
  * [4 Adding a serial port (**voids warranty**)][17616]
    * [4.1 Device disassembly][17617]
  * [5 Pictures][17618]
  * [6 See also][17619]

# Identification
On the back of the device, the following is printed: 
[code] 
    The PCB has the following written on it:
    ET_Q8_V2.0
    151121
    
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: Q88
  * Build Number: astar_rtl8703-eng 4.4.2 KVT49L 20151229 test-keys

# Sunxi support
## Current status
Mainline U-boot OK from SD. 
Mainline Kernel OK from SD. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the q8_a33_tablet_1024x600_defconfig target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][17620]

Everything else is the same as the [manual build howto][17621]. 
## Mainline U-Boot
Use 2016.11 with default A33 1024x600. 
**q8_a33_tablet_1024x600_defconfig** file 
## Mainline kernel
Use the _sun8i-a33-et-q8.dts_ device-tree file for the [mainline kernel][17622]. With USB host mode only work with every type of cables. 
# Tips, Tricks, Caveats
## FEL mode
The Volume+ button triggers [ FEL mode][17623]. 
## Retrieving script.bin
Unlike, other allwinner devices,Script.bin is not present in the vfat partition(nanda) as file. 
Instead, It is located 0x43000000, it's size is 0x00020000. _script.bin_ can be extracted from /dev/mem using mmap() or sunxi-tools _firmware_extractor_. 
# Adding a serial port (**voids warranty**)
There are no UART pads available on this device. Instead, UART0 is multiplexed with the microSD adapter. Please refer to the [MicroSD Breakout adapter][17624] for more information.. 
## Device disassembly
See [the Q8 tablet format disassembly page][17625]. 
# Pictures
  * [![ET Q8 V2.0-PCB.jpg][17626]][17627]

# See also
  * [Other Q8 format A33 based tablets.][17628]
