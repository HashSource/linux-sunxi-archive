# Anbernic RG35XX H
Anbernic RG35XX H  
---  
[![RG35XX-H Device Front.png][7366]][7367]  
Manufacturer |  [Anbernic][7368]  
Dimensions |  Length 18.7cm;Width 9.3cm;Height 3cm   
Release Date |  December 2023   
Website |  [Device Page][7369]  
Specifications   
SoC |  H700 @ 1.5Ghz   
DRAM |  1GiB LPDDR4 @ 672 MHz   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  640x480 (3.5" 4:3)   
Video |  mini HDMI   
Audio |  3.5mm headphone plug, HDMI, SPDIF, internal stereo speakers   
Network |  WiFi 802.11 b/g/n + BT 4.2   
Storage |  2 x µSD   
USB |  1 x USB2.0 Type-C OTG/power, 1 x USB2.0 Type-C host   
Other |  (only pcb v4) RTC (BM8563)   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][7370] and the [New Device Page guide][7371].
Handheld gaming device built around an Allwinner [H700][7372] CPU. The device internals are basically the same as the [RG35XX Plus][7373]
## Contents
  * [1 Identification][7374]
  * [2 Sunxi support][7375]
    * [2.1 Current status][7376]
    * [2.2 Manual build][7377]
      * [2.2.1 Mainline U-Boot][7378]
      * [2.2.2 Mainline Linux Kernel][7379]
  * [3 Tips, Tricks, Caveats][7380]
    * [3.1 FEL mode][7381]
  * [4 Adding a serial port (**voids warranty**)][7382]
    * [4.1 Device disassembly][7383]
    * [4.2 Locating the UART][7384]
  * [5 Pictures][7385]
  * [6 See also][7386]
    * [6.1 Manufacturer images][7387]

# Identification
On the back of the device, the following is printed: 
[code] 
    ANBERNIC
    Model No. RG35XX H
[/code]
The PCB has the following silkscreened on it: 
[code] 
    RG35XX H_V3.0
    2023-12-14
[/code]
Or 
[code] 
    RG35XX H_V4.0
    2024-01-08
[/code]
# Sunxi support
## Current status
Mainline support is work in progress. See the [RG35XX status][7388] for updates. 
## Manual build
You can build things for yourself by following our [ Manual build howto][7389] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Mainline Linux Kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
Booting with a USB-C cable connected to the USB-OTG port (DC/OTG at top of the device) without an SD card inserted triggers FEL mode. 
# Adding a serial port (**voids warranty**)
[![][7390]][7391]
[][7392]
UART pads
The UART header is located between the left SDCARD and left speaker [UART howto][7393]
## Device disassembly
Remove the four Torx T6 screws from the rear case. There's a small gap between the back and the rest of the case, just use a pick to open it up. The L1/R1 and L2/R2 buttons may fall when you open the case, but they are simple to reinsert and don't have any springs. 
## Locating the UART
The UART pins are GND, TX, RX, GND. 
# Pictures
  * [![RG35XX-H board.png][7394]][7395]
  * [![RG35XX-H H700.png][7396]][7397]
  * [![][7398]][7399]
PCB v4 
  * [![][7400]][7401]
CPU detail (PCB v4) 
  * [![][7402]][7403]
RTC (PCB v4) 

# See also
See the [RG35XX Plus][7373] page. 
## Manufacturer images
Optional. Add non-sunxi images in this section.
