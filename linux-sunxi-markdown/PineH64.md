# PineH64
PineH64  
---  
[![Pineh64 top.jpg][44565]][44566]  
Manufacturer |  [Pine64][44567]  
Dimensions |  133 _mm_ x 80 _mm_ x 19 _mm_ (model A), 85 _mm_ x 56 _mm_ x 18.8 _mm_ (model B)   
Release Date |  January 2018   
Website |  [Pine64 Wiki][44568]  
Specifications   
SoC |  [H6][44569] @ 1.8GHz   
DRAM |  1GiB/2GiB/3GiB LPDDR3 @ 800MHz   
Power |  DC 5V@3A, 3.5mm/1.35mm barrel plug   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone/mic plug, HDMI, SPDIF, I2S   
Network |  10/100/1000Mbps Ethernet ([Realtek 8211E][44570])   
Storage |  µSD, eMMC (module), 128Mbit SPI NOR flash   
USB |  2 USB2.0 Host, 1 USB3.0 Host   
Other |  miniPCIe, RTC battery connector   
Headers |  RPi2 "compatible" connector, "Euler" connector, WiFi/BT connector, 2x5 pins "EXP" header   
H6-based SBC from PINE64. Two models exist, a discontinued Model A, and the replacement Model B. 
## Contents
  * [1 Identification][44571]
  * [2 Sunxi support][44572]
    * [2.1 Current status][44573]
    * [2.2 BSP][44574]
    * [2.3 Manual build][44575]
      * [2.3.1 U-Boot][44576]
      * [2.3.2 Linux Kernel][44577]
  * [3 Tips, Tricks, Caveats][44578]
    * [3.1 FEL mode][44579]
  * [4 Serial port / UART][44580]
  * [5 Pictures][44581]
  * [6 See also][44582]

# Identification
There is a pine cone like logo on the top silk screen, also it says "Pine H64" under the logo. Also on the SoC there is a quite prominent "H6" print. 
The board has two variants, Model A and Model B. Model A has the same size with a Pine A64+ and is equipped with a PCIe slot; Model B dropped the slot, and has the form factor of an RPi model B. The Model A variant has been discontinued and is no longer sold. It has been superseded by the Model B. 
The board has various revisions, many of them are engineering samples, only two revisions will be the final edition, one model A and one model B. 
On the back of the device, the following is printed: 
[code] 
    Designed in Silicon Valley, California. Built in Silicon Delta, China.
[/code]
For the first ES revision of Model A, The PCB has the following silkscreened on it (This revision is quite rare, and when you see it usually it will have a jumper wire because of a fault when designing the power circuit for LPDDR3.): 
[code] 
    PINE_H64_VER1.1
    2017-10-26
[/code]
For the second ES revision of Model A, The PCB has the following silkscreened on it: 
[code] 
    PINE_H64_VER1.1
    2018-01-09
[/code]
For the first ES revision of Model B, The PCB has the following silkscreened on it: 
[code] 
    PINE_H64_MODEL_B
    2018-05-26
[/code]
At least one revision of Model B has the following silkscreened on it: 
[code] 
    PINE_H64_MODEL_B
    2018-10-17
[/code]
Currently shipping Model B units (as of 2019-12-30) have the following silkscreen: 
[code] 
    PINE_H64_MODEL_B
    2018-12-12
[/code]
# Sunxi support
## Current status
The board is well supported in both the mainline Linux kernel and in U-Boot, also by some third-party image providers. 
## BSP
A beta version of the H6 BSP was released on 2018/01/30... 
  * <https://github.com/Allwinner-Homlet/H6-BSP4.9-brandy>
  * <https://github.com/Allwinner-Homlet/H6-BSP4.9-tools>
  * <https://github.com/Allwinner-Homlet/H6-BSP4.9-linux>

## Manual build
You can build things for yourself by following our [ Manual build howto][44583] and by choosing from the configurations available below. 
### U-Boot
Use the **pine_h64_defconfig** build target in mainline U-Boot (supported since v2018.09). 
### Linux Kernel
Use the **sun50i-h6-pine-h64.dtb** (model A) and **sun50i-h6-pine-h64-model-b.dts** (model B) devicetree binary from the mainline kernel. 
# Tips, Tricks, Caveats
## FEL mode
There is no dedicated FEL mode button. Without a (bootable) eMMC module and with no boot image on the SPI flash, the board will enter FEL when powered up without an SD card (out of the box experience). 
Otherwise the [ special FEL SD card][44584] will force FEL mode. 
# Serial port / UART
[![][44585]][44586]
[][44587]
DEVICE UART pads
On the model A the debug UART 0 is exposed both on the 10-pin EXP connector as well as on the 34-pin Euler connector. Refer to the picture on the right to find the pins. The location is the same as on the [ Pine64 board][44588]. 
On the model B the UART is exposed on the 6-pin header connector between the HDMI and headphone jacks. The pins are on the front row, closer to the board's edge: TX, RX, GND, from left (HDMI) to right (headphone). 
# Pictures
  * [![][44589]][44590]
Pine H64 model A 
  * [![PineH64 Bottom.jpg][44591]][44592]
  * [![PineH64 1.jpg][44593]][44594]
  * [![PineH64 2.jpg][44595]][44596]
  * [![PineH64 3.jpg][44597]][44598]
  * [![PineH64 4.jpg][44599]][44600]
  * [![][44601]][44602]
Pine H64 model B 

# See also
  * [PineH64 Rev 1.1 Board Schematic][44603]

  * [Pine64 wiki][44604]
  * [PineH64 wiki page][44568]
  * [Pine64 Forum][44605]
