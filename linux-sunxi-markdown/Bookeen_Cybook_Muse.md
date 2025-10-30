# Bookeen Cybook Muse
Bookeen Cybook Muse  
---  
[![CYBME1S-BK front.jpg][10189]][10190]  
Manufacturer |  [Bookeen][10191]  
Dimensions |  110 x 150 x 5 mm   
Release Date |  10/2015  
Website |  [Leclerc shop][10192]  
Specifications   
SoC |  [A13][10193] @ 1Ghz   
DRAM |  256MiB DDR3 @ 360MHz   
Power |  DC 5V @ 3A, 1900mAh 3.7V Li-Ion battery   
Features   
LCD |  90x122 (6" 4:3)   
Touchscreen |  2-finger capacitive ([Goodix][10194])   
Video |  EPD (eInk) using [TPS65185 PMIC][10195]  
Network |  WiFi 802.11 b/g/n ([Realtek 8188eus][10196])   
Storage |  µSD / internal eMMC : 2Gb   
USB |  1 USB2.0 Host   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][10197] and the [New Device Page guide][10198].
Bookeen is French company dealing with e-books and consumer electronics. The Muse is their main 6 inches eReader, with different version. The case is the same, but the screen resolution and the inside memory are different. You can look at the back of the device to know its reference. 
## Contents
  * [1 Identification][10199]
  * [2 Sunxi support][10200]
    * [2.1 Current status][10201]
    * [2.2 Manual build][10202]
      * [2.2.1 U-Boot][10203]
        * [2.2.1.1 Mainline U-Boot][10204]
        * [2.2.1.2 Linux Kernel][10205]
        * [2.2.1.3 Mainline kernel][10206]
  * [3 Tips, Tricks, Caveats][10207]
    * [3.1 FEL mode][10208]
    * [3.2 Device specific topic][10209]
    * [3.3 ...][10210]
  * [4 Adding a serial port (**voids warranty**)][10211]
    * [4.1 Device disassembly][10212]
    * [4.2 Locating the UART][10213]
  * [5 Pictures][10214]
  * [6 Variants][10215]
  * [7 See also][10216]
    * [7.1 Manufacturer images][10217]

# Identification
On the back of the device, the following is printed: 
[code] 
    CYBOOK MUSE by BOOKEEN SAS
    CYBME1S-BK
[/code]
This is for the eMMC, 800x600 device. 
  * [![][10218]][10219]
back side 

The PCB has the following silkscreened on it: 
[code] 
    M1 / F1 / F2 V1.2
    20150727
[/code]
  * [![][10220]][10221]
CYBME1S-BK PCB 

# Sunxi support
## Current status
Not supported by Linux mainline. But Bookeen has a [Github][10222] repo with some sources. 
## Manual build
You can build things for yourself by following our [ Manual build howto][10223] and by choosing from the configurations available below. 
### U-Boot
U-Boot 2011 source code is released [here][10224]. 
#### Mainline U-Boot
Not supported yet, there is no device tree file available. 
#### Linux Kernel
Source code for kernel 3.0 is released [here][10225]. It is very similar to the allwinner source released a few years ago. 
#### Mainline kernel
Not supported. No device tree available. 
# Tips, Tricks, Caveats
There are multiple devices using this form factor. You should read the serial on the back. 
## FEL mode
You can enter FEL mode with [special][10226] SD card. 
## Device specific topic
The device uses an e-ink display driven by [TPS65185 PMIC][10195] chip (same PMIC seems to be used on Kobo and Nook eReaders). The driver seems to be software only, and is available in the kernel source code. 
## ...
# Adding a serial port (**voids warranty**)
[![][10227]][10228]
[][10229]
DEVICE UART pads
The motherboard has 4 pins labelled 3V3/TX/RX/GND. Connecting them allows to see the boot process, and to get access to a busybox shell. Login is root, with no password. 
## Device disassembly
No screws, only remove the back side. 
## Locating the UART
RX/TX/GND is clearly labeled on the board :) 
# Pictures
  * [![CYBME1S-BK A13.jpg][10230]][10231]
  * [![CYBME1S-BKsd.jpg][10232]][10233]

# Variants
  * [Adlibris Letto][10234] (Sweden)
  * [Saraiva Lev][10235] (Brazil)
  * Nolim Nolimbook ([France][10236] / [Spain][10237])

Model: CYBOY4S-CF, s/n: CF605xxxxxxxxxxxxx, PCB markings: IDIG_E025_V1.2 / BK6027_V1.2 / 20130821 
has 4GB nand 
# See also
[Bookeen's Github.][10222] [Bookeen's website.][10191] [Guide about rooting the device with the existing software][10238] [How to make custom ROM for Cybook e-readers][10239]
## Manufacturer images
