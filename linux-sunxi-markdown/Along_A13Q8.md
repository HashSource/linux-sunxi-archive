# Along A13Q8
Along A13Q8  
---  
[![Device front.jpg][7030]][7031]  
Manufacturer |  [Along][7032]  
Dimensions |  182 _mm_ x 121 _mm_ x 7 _mm_  
Release Date |  August 2013   
Website |  Missing Product Page   
Specifications   
SoC |  [A13][7033] @ 1Ghz   
DRAM |  512MiB DDR3 @ 360MHz ([Spectek PEB15-15E][7034])   
NAND |  4GB   
Power |  DC 5V @ 2A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][7035])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][7036])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  640x480 (VGA) front-facing, Optional rear-facing camera   
Other |  Accelerometer ([Manufacturer device][7037] FIXME)   
This page needs to be properly filled according to the [New Device Howto][7038] and the [New Device Page guide][7039].
A standard [A13][7033] based, [Q8 style][7040] device. 
## Contents
  * [1 Identification][7041]
  * [2 Sunxi support][7042]
    * [2.1 Current status][7043]
    * [2.2 Images][7044]
    * [2.3 HW-Pack][7045]
    * [2.4 BSP][7046]
    * [2.5 Manual build][7047]
  * [3 Tips, Tricks, Caveats][7048]
    * [3.1 FEL mode][7049]
  * [4 Adding a serial port (**voids warranty**)][7050]
    * [4.1 Device disassembly][7051]
    * [4.2 Locating the UART][7052]
  * [5 Pictures][7053]
  * [6 Also known as][7054]
  * [7 See also][7055]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    AL-A13Q8-V8_5
    REV:8.5
    2013.08.07
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either U-Boot or kernel, mention this too, but add the extra sections below.
## Images
## HW-Pack
## BSP
## Manual build
  * For building U-Boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][7056]

Everything else is the same as the [manual build howto][7057]. 
# Tips, Tricks, Caveats
## FEL mode
The Volume- button triggers [ FEL mode][7058]. 
# Adding a serial port (**voids warranty**)
There are no UART pads available on this device. You will have to use the [MicroSD Breakout adapter][7059]. 
## Device disassembly
See [the Q8 tablet format disassembly page][7060]. 
## Locating the UART
Pins 151 and 152 of the TQFP do not seem to be wired up. You might get away with attaching a very very thin wire to it, but that requires some very creative soldering. 
# Pictures
Take some pictures of your device, [ upload them][7061], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][7062]][7031]
  * [![Device back.jpg][7063]][7064]
  * [![Device buttons 1.jpg][7065]][7066]
  * [![Device buttons 2.jpg][7067]][7068]
  * [![A13boardback.jpg][7069]][7070]
  * [![Device board back.jpg][7071]][7072]

# Also known as
# See also
  * [Other Q8 format A13 based tablets.][7073]
