# Eearl H1026A
Eearl H1026A  
---  
[![Device front.jpg][17755]][17756]  
Manufacturer |  [Eearl Group LTD][17757]  
Dimensions |  278 _mm_ x 188 _mm_ x 25 _mm_  
Release Date |  August 2012   
Website |  [Product Page][17758]  
Specifications   
SoC |  [A10][17759], @ 1Ghz   
DRAM |  512MiB/1GiB DDR3   
NAND |  4/8GB   
Power |  DC 5V @ ?A, ??mAh 3.7V Li-Ion battery  
Features   
LCD |  1024x600 (10" ~16:9)   
Audio |  3.5mm headphone plug   
Network |  WiFi 802.11 b/g (Realtek RTL8192CU), 10/100Mbps Ethernet (Manufacturer device)   
Storage |  SD   
USB |  3 USB2.0 Host, X USB2.0 OTG  
Camera |  0.3MP (640x480) front-facing   
Other |  Keyboard, 2-button touchpad   
Headers |  UART, JTAG, USB2.0 OTG   
This page needs to be properly filled according to the [New Device Howto][17760] and the [New Device Page guide][17761].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurp.
## Contents
  * [1 Identification][17762]
  * [2 Sunxi support][17763]
    * [2.1 Current status][17764]
    * [2.2 Images][17765]
    * [2.3 HW-Pack][17766]
    * [2.4 BSP][17767]
    * [2.5 Manual build][17768]
  * [3 Tips, Tricks, Caveats][17769]
    * [3.1 FEL mode][17770]
  * [4 Adding a serial port (**voids warranty**)][17771]
    * [4.1 Device disassembly][17772]
    * [4.2 Locating the UART][17773]
  * [5 Pictures][17774]
  * [6 Also known as][17775]
  * [7 See also][17776]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

# Sunxi support
## Current status
Everything works. Camera is UVC and requires a modified driver. 
## Images
Debian (Squeeze) SD card image: [a10_netbook_4gb.tar.xz][17777]
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "H6" target.
  * The .fex file can be found in sunxi-boards as [h6.fex][17778]

Everything else is the same as the [manual build howto][17779]. 
# Tips, Tricks, Caveats
## FEL mode
There is a button marked **uboot** between the ram chips and the usb ports, which triggers [ FEL mode][17780]. 
# Adding a serial port (**voids warranty**)
[![][17781]][17782]
[][17783]
DEVICE UART pads
## Device disassembly
Provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped.
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][17784].
# Pictures
  * [![Device front.jpg][17785]][17756]
  * [![Device back.jpg][17786]][17787]
  * [![Device buttons 1.jpg][17788]][17789]
  * [![Device buttons 2.jpg][17790]][17791]
  * [![H6-netbook-mainboard.jpg][17792]][17793]
  * [![H6-netbook-mainboard-back.jpg][17794]][17795]

# Also known as
The same motherboard could have been resold inside the 7" A10 Netbook. 
# See also
  * [cnx-software announcement][17796]
