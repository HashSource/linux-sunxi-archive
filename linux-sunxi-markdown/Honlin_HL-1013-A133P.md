# Honlin HL-1013-A133P
Honlin HL-1013-A133P  
---  
[![HL 1013 A133P Netbook.jpg][24184]][24185]  
Manufacturer |  [Manufacturer][24186]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][24187]  
Specifications   
SoC |  [A133][24188] @ XGhz   
DRAM |  2GiB LPDDR3 @ xxxMHz   
eMMC |  32GiB   
Power |  DC 5V @ 2A, 3600mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (6.98" ~16:9)   
Audio |  3.5mm headphone+mic plug, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([Xradio Tech XR829][24189])   
Storage |  SD (full size)   
USB |  2x USB2.0 Host, 1x USB2.0 OTG   
Camera |  ??.?MP (????x????) front   
This page needs to be properly filled according to the [New Device Howto][24190] and the [New Device Page guide][24191].
## Contents
  * [1 Identification][24192]
  * [2 Sunxi support][24193]
    * [2.1 Current status][24194]
    * [2.2 Manual build][24195]
      * [2.2.1 U-Boot][24196]
      * [2.2.2 Linux Kernel][24197]
  * [3 Tips, Tricks, Caveats][24198]
    * [3.1 FEL mode][24199]
  * [4 Adding a serial port (**voids warranty**)][24200]
    * [4.1 Device disassembly][24201]
    * [4.2 Locating the UART][24202]
  * [5 Pictures][24203]
  * [6 See also][24204]

# Identification
There aren't any obvious manufacturer or branding markings on the case. 
On Amazon US, it is listed as: 
[code] 
    Goldengulf
    GG-789-A133
[/code]
The PCB has the following silkscreened on it: 
[code] 
    Efercro
    NA70_MB_V1.3
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _HL_1013_A133P_
  * Build Number: _HL_1013_A133P_US_20230725_

# Sunxi support
## Current status
Not supported yet. 
## Manual build
You can build things for yourself by following our [ Manual build howto][24205] and by choosing from the configurations available below. 
### U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
The OTG port is accessible via the USB-C power input port at the rear of the device. It can be used for [ADB][24206] access from another system. 
## [ FEL mode][24207]
There is a tiny button underneath the keyboard, accessible via a cutout on the right side, near the USB-A ports. 
[![][24208]][24209]
[][24210]
FEL button location on main PCB
Running "adb reboot efex" from a host connected to the OTG port also works when the device is booted into the stock Android OS. 
# Adding a serial port (**voids warranty**)
[![][24211]][24212]
[][24213]
Wires soldered to UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][24214]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
  1. Remove the LCD assembly. There are screws underneath the 4 rubber pads in the corners. Use a [plastic tool][24215] to disengage the clips holding the two halves of the LCD assembly together. There are 3 clips each on the left, right, and bottom edges, and 4 clips on the top edge.
  2. Remove the keyboard. There are 4 latches near the "ESC", "F4/F5", "F9/F10", and "Delete" keys.
  3. Remove the screws on the bottom of the device. There is one clip by the touchpad on the front edge.

## Locating the UART
There are pads on the PCB with "RX", "TX", and "GND" silkscreen labels nearby. UART is active, solder wires to the pads. The [UART howto][24214] will be useful. 
# Pictures
Pictures of the outside will be added at a future date. In the meanwhile, some can be found on Amazon's product page (see below). 
  * [![][24216]][24185]
Open 
  * [![Device back.jpg][24217]][24218]
  * [![][24219]][24220]
Bottom Case 
  * [![][24221]][24222]
Main PCB top 
  * [![][24223]][24224]
Main PCB bottom 
  * [![][24225]][24226]
A133P and Samsung DRAM 

# See also
[Amazon US product page, as of Aug. 1, 2024][24227]
