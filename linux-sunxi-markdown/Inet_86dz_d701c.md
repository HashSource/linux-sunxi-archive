# Inet 86dz d701c
Inet 86dz d701c  
---  
[![A727front.jpg][26309]][26310]  
Manufacturer |  [Inet-Tek][26311]  
Dimensions |  190 _mm_ x 125 _mm_ x 9.7 _mm_  
Release Date |  March 2014   
Website |  [Alibaba product page][26312]  
Specifications   
SoC |  [A23][26313] @ 1Ghz   
DRAM |  512MiB DDR3 @ 552MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][26314])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][26315])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer (TODO: [Manufacturer device][26316])   
Headers |  UART   
Another cheap $20-$80 tablet with a tolerable screen and an [A23][26313] processor. 
## Contents
  * [1 Identification][26317]
  * [2 Sunxi support][26318]
    * [2.1 Current status][26319]
    * [2.2 Images][26320]
    * [2.3 HW-Pack][26321]
    * [2.4 BSP][26322]
    * [2.5 Manual build][26323]
  * [3 Tips, Tricks, Caveats][26324]
    * [3.1 FEL mode][26325]
  * [4 Adding a serial port (**voids warranty**)][26326]
    * [4.1 Device disassembly][26327]
    * [4.2 Locating the UART][26328]
  * [5 Pictures][26329]
  * [6 Also known as][26330]
  * [7 See also][26331]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: A727
  * Build Number: A23_86DZ_D701C_131174.20131229

# Sunxi support
## Current status
Like all things A23, this hardware is not supported. It is however a prime target for development. For more information, check [ the Allwinner A23 SoC page][26313]. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][26332]

Everything else is the same as the [manual build howto][26333]. 
# Tips, Tricks, Caveats
## FEL mode
The Volume +/- buttons trigger [ FEL mode][26334]. Unfortunately, FEL mode via this method appears to be useless for dumping device info. 
# Adding a serial port (**voids warranty**)
[![][26335]][26336]
[][26337]
Inez 86dz UART pads
## Device disassembly
Unscrew 2 small screws on the button panel side. Using a [plastic tool][26338] pop out the sides and pull off the cover. 
## Locating the UART
The test pad nearest to the right side of the SD slot is serial TX. Tx is multiplexed with pin mmc pin 0, so expect to see garbage when using an SD card. 
Rx hasn't been found yet (Neither front nor back test pads nor uSD slot pins). Read-only console for now. 
# Pictures
  * [![A727front.jpg][26339]][26310]
  * [![A727 back.jpg][26340]][26341]
  * [![A727 close.jpg][26342]][26343]
  * [![A727board back.jpg][26344]][26345]
  * [![A727UART Tx Ground.jpg][26346]][26347]

# Also known as
  * [Azpen][26348] A727

# See also
  * [Ippo_q8h][26349] \- Another cheap A23 tablet.
