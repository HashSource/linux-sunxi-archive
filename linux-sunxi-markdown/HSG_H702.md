# HSG H702
HSG H702  
---  
[![HSG H702 front.jpg][23627]][23628]  
Manufacturer |  [HannStar][23629]  
Dimensions |  181 _mm_ x 121 _mm_ x 10.5 _mm_  
Release Date |  April 2013   
Website |  Unknown   
Specifications   
SoC |  [A13][23630] @ 1Ghz   
DRAM |  512MiB DDR3 @ 432MHz (Micron MT41J256M16HA-125 256X16DDR3 HL)   
NAND |  4GB (Samsung K9GBG08U0A)   
Power |  DC 5V @ 2A, ????mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][23631])   
Audio |  3.5mm headphone plug, built-in microphone.   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][23632])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  640x480 (VGA) front-facing, Optional rear-facing camera   
Other |  Accelerometer ([Freescale MMA7660][23633]), RTC (NXP PCF8563)   
A standard [Q8 format][23634], [A13][23630] based tablet, but with separate [UART][23635] pads. 
## Contents
  * [1 Identification][23636]
  * [2 Sunxi support][23637]
    * [2.1 Current status][23638]
    * [2.2 Images][23639]
    * [2.3 HW-Pack][23640]
    * [2.4 BSP][23641]
    * [2.5 Manual build][23642]
    * [2.6 Mainline kernel][23643]
  * [3 Tips, Tricks, Caveats][23644]
    * [3.1 FEL mode][23645]
  * [4 Adding a serial port (**voids warranty**)][23646]
    * [4.1 Device disassembly][23647]
    * [4.2 Locating the UART][23648]
  * [5 Pictures][23649]
  * [6 Also known as][23650]
  * [7 See also][23651]

# Identification
The PCB is clearly marked **HSG_H702_V1.2**. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: SoftwinerEVB
  * Build Number: nuclear_evb-eng 4.0.4 IMM76D 20130418test-keys

The android strings are not helpful as both are generic [A13][23630] Allwinner strings. The only option to properly identify this device is by [opening up the case][23647] and reading the markings on the board. 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "A13_MID" target.
  * The .fex file can be found in sunxi-boards as [hsg_h702.fex][23652]

Everything else is the same as the [manual build howto][23653]. 
## Mainline kernel
Use the _sun5i-a13-hsg-h702.dts_ device-tree file for the [mainline kernel][23654]. 
# Tips, Tricks, Caveats
## FEL mode
The Volume+ button triggers [ FEL mode][23655]. 
# Adding a serial port (**voids warranty**)
[![][23656]][23657]
[][23658]
HSG H702 UART pads
## Device disassembly
See [the Q8 tablet format disassembly page][23659]. 
## Locating the UART
On the front of the mainboard, there are two test pads next to the SoC. Solder on some wires according to our [UART howto][23635]. These pads are connected to UART1, and are not multiplexed with the SD card. 
# Pictures
  * [![HSG H702 front.jpg][23660]][23628]
  * [![HSG H702 back.jpg][23661]][23662]
  * [![HSG H702 buttons 1.jpg][23663]][23664]
  * [![HSG H702 buttons 2.jpg][23665]][23666]
  * [![HSG H702 innards.jpg][23667]][23668]
  * [![HSG H702 board front.jpg][23669]][23670]
  * [![HSG H702 board back.jpg][23671]][23672]

# Also known as
# See also
  * [Other Q8 format A13 based tablets.][23673]
