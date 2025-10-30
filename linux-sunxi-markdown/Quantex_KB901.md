# Quantex KB901
Quantex KB901  
---  
[![Device front.jpg][46325]][46326]  
Manufacturer |  [Mal electronics???][46327]  
Dimensions |  235 _mm_ x 146 _mm_ x 10 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][46328]  
Specifications   
SoC |  [A13][46329] @ 1 GHz   
DRAM |  512 MiB DDR3 @ 408 MHz   
NAND |  4 GB   
Power |  DC 5 V @ 3 A, 3700 mAh 3.7 V Li-Ion battery   
Features   
LCD |  800x480 (9" 16:9)   
Touchscreen |  5-finger capacitive ([Focaltech FT5x06][46330])   
Audio |  3.5 mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][46331] FIXME)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3 MP (640x480) front (Galaxycore GC0308)   
Other |  Accelerometer ([Freescale mma7660][46332]) Optical Sensor (Mouser Electronics Inc. LTR501ALS) Real Time Clock (NXP pcf8563)   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][46333] and the [New Device Page guide][46334].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurp.
## Contents
  * [1 Identification][46335]
  * [2 Sunxi support][46336]
    * [2.1 Current status][46337]
    * [2.2 Images][46338]
    * [2.3 HW-Pack][46339]
    * [2.4 BSP][46340]
    * [2.5 Manual build][46341]
  * [3 Tips, Tricks, Caveats][46342]
    * [3.1 FEL mode][46343]
  * [4 Adding a serial port (**voids warranty**)][46344]
    * [4.1 Device disassembly][46345]
    * [4.2 Locating the UART][46346]
  * [5 Pictures][46347]
  * [6 Also known as][46348]
  * [7 See also][46349]

# Identification
KB901 V1.1 is printed onto the board. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either u-boot or kernel, mention this too, but add the extra sections below.
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][46350]

Everything else is the same as the [manual build howto][46351]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][46352]. 
Currently only UART FEL has been tested. 
# Adding a serial port (**voids warranty**)
[![][46353]][46354]
[][46355]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][46356].
## Device disassembly
Provide a short description of how to open the device. Explain how the pins can be most easily popped, and mention the [Plastic tool howto][46357].
Cover could be opened on the bottom where two screws are seated. You have to remove those screws first. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][46356].
UART pads are seated near the camera and labeled GND/TX/RX. 
# Pictures
  * [![Device front.jpg][46358]][46326]
  * [![Device back.jpg][46359]][46360]
  * [![Device buttons 1.jpg][46361]][46362]
  * [![Device buttons 2.jpg][46363]][46364]
  * [![Device board front.jpg][46365]][46366]
  * [![Device board back.jpg][46367]][46368]

# Also known as
  * [Tablet T9701][46369]

# See also
