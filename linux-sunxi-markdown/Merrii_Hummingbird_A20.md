# Merrii Hummingbird A20
Merrii Hummingbird A20  
---  
[![Merrii Hummingbird A20 - front.jpg][37735]][37736]  
Manufacturer |  [Merrii Vision][37737]  
Dimensions |  65 _mm_ x 100 _mm_ x 10 _mm_  
Release Date |  November 2013   
Website |  [Product page][37738]  
Specifications   
SoC |  [A20][37739] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz   
NAND |  4GB   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug)   
Features   
Video |  HDMI, CVBS (via Phone Jack), TV in(via Phone Jack)   
Audio |  3.5mm headphone plug, 3.5mm line-in plug, HDMI   
Network |  WiFi 802.11 b/g/n ([Ampak AP6210][37740]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][37741])   
Storage |  µSD, SATA (+5v power)   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  IRDA (Vishay HS0038B), Bluetooth ([Ampak AP6210][37742])   
Headers |  UART, 2 x 50 pins expansion connectors   
This page needs to be properly filled according to the [New Device Howto][37743] and the [New Device Page guide][37744].
## Contents
  * [1 Identification][37745]
  * [2 Sunxi support][37746]
    * [2.1 Current status][37747]
    * [2.2 Images][37748]
    * [2.3 HW-Pack][37749]
    * [2.4 BSP][37750]
    * [2.5 Manual build][37751]
    * [2.6 Mainline kernel][37752]
  * [3 Tips, Tricks, Caveats][37753]
    * [3.1 FEL mode][37754]
  * [4 Adding a serial port][37755]
  * [5 Pictures][37756]
  * [6 Also known as][37757]
  * [7 See also][37758]

# Identification
The board helpfully reads "Merrii Vision"(in Chinese), "www.merrii.com" on the PCB. 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Merrii_Hummingbird_A20" target.
  * The .fex file can be found in sunxi-boards as [merrii_hummingbird_a20.fex][37759]

Everything else is the same as the [manual build howto][37760]. 
## Mainline kernel
Use the _sun7i-a20-hummingbird.dts_ device-tree file for the [mainline kernel][37761]. 
# Tips, Tricks, Caveats
## FEL mode
The "U-boot" button triggers [ FEL mode][37762]. 
# Adding a serial port
[![][37763]][37764]
[][37765]
Hummingboard A20 UART pads
There is a nice 2.54mm pitch connector between the NAND and the µSD slot, the pin-out is printed right next to it. Just attach some leads according to our [UART howto][37766]. 
# Pictures
Take some pictures of your device, [ upload them][37767], and add them here.
  * [![Merrii Hummingbird A20 - front.jpg][37768]][37736]
  * [![Device board back.jpg][37769]][37770]

# Also known as
# See also
  * [Merrii Hummingbird A31][37771]
