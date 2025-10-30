# Coby MID7042
Coby MID7042  
---  
[![Device front.jpg][13064]][13065]  
Manufacturer |  [Coby Electronics (defunct)][13066]  
Dimensions |  195.6 _mm_ x 114.3 _mm_ x 10.2 _mm_  
Release Date |  April 2012   
Website |  [Device Product Page][13067]  
Specifications   
SoC |  [A10][13068] @ 1Ghz   
DRAM |  1GiB DDR3   
NAND |  4/8GB   
Power |  DC 5V @ 2A, 3500mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  X-finger capacitive ([Manufacturer device][13069] FIXME)   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (Manufacturer device)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][13070] FIXME)   
Headers |  UART, JTAG   
This page needs to be properly filled according to the [New Device Howto][13071] and the [New Device Page guide][13072].
## Contents
  * [1 Identification][13073]
  * [2 Sunxi support][13074]
    * [2.1 Current status][13075]
    * [2.2 Images][13076]
    * [2.3 HW-Pack][13077]
    * [2.4 BSP][13078]
    * [2.5 Manual build][13079]
  * [3 Tips, Tricks, Caveats][13080]
    * [3.1 FEL mode][13081]
  * [4 Adding a serial port (**voids warranty**)][13082]
    * [4.1 Device disassembly][13083]
    * [4.2 Locating the UART][13084]
  * [5 Pictures][13085]
  * [6 Also known as][13086]
  * [7 See also][13087]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: MID7042
  * Build Number: 20120409.181217

# Sunxi support
## Current status
Everything except for the touchscreen seems to work. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Coby_MID7042" target.
  * The .fex file can be found in sunxi-boards as [coby_mid7042.fex][13088]

Everything else is the same as the [manual build howto][13089]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][13090]. 
# Adding a serial port (**voids warranty**)
[![][13091]][13092]
[][13093]
UART and JTAG pads
## Device disassembly
Provide a short description of how to open the device. Explain how the pins can be most easily popped.
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][13094].
# Pictures
Take some pictures of your device, [ upload them][13095], and add them here.
  * [![Device front.jpg][13096]][13065]
  * [![Device back.jpg][13097]][13098]
  * [![Device buttons 1.jpg][13099]][13100]
  * [![Device buttons 2.jpg][13101]][13102]
  * [![Device board front.jpg][13103]][13104]
  * [![Device board back.jpg][13105]][13106]

# Also known as
Pendopad 4.0 7" PP4MT-7 
# See also
