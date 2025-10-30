# Onda vi40
Onda vi40  
---  
[![Device front.jpg][41822]][41823]  
Manufacturer |  [Onda][41824]  
Dimensions |  242 _mm_ x 190 _mm_ x 12 _mm_  
Release Date |  February 2012   
Website |  [Product Page][41825]  
Specifications   
SoC |  [A10][41826] @ 1Ghz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  16GB   
Power |  DC 5V @ 2.1A, 6500mAh ??V Li-Ion battery   
Features   
LCD |  1024x768 (9.7" 4:3 IPS)   
Touchscreen |  5-finger capacitive (TODO: [Manufacturer device][41827])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n (Manufacturer device)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  1.3MP (1280x1024) front, 5MP (2560x1920) rear   
Other |  Accelerometer ([manufacturer device][41828])   
Headers |  UART, JTAG, ???  
This page needs to be properly filled according to the [New Device Howto][41829] and the [New Device Page guide][41830].
## Contents
  * [1 Identification][41831]
  * [2 Sunxi support][41832]
    * [2.1 Current status][41833]
    * [2.2 Images][41834]
    * [2.3 HW-Pack][41835]
    * [2.4 BSP][41836]
    * [2.5 Manual build][41837]
  * [3 Tips, Tricks, Caveats][41838]
    * [3.1 FEL mode][41839]
    * [3.2 Device specific topic][41840]
    * [3.3 ...][41841]
  * [4 Adding a serial port (**voids warranty**)][41842]
    * [4.1 Device disassembly][41843]
    * [4.2 Locating the UART][41844]
  * [5 Pictures][41845]
  * [6 Also known as][41846]
  * [7 See also][41847]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: `ONDA MID`
  * Build Number: `mid-eng 4.1.1 JRO03C 20121018 test-keys`
  * Kernel: 3.0.8+
  * Baseband version (sic): v0.4rc1
  * Android version: 4.1.1

# Sunxi support
## Current status
No patches submitted yet. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][41848]

Everything else is the same as the [manual build howto][41849]. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][41850]. 
## Device specific topic
## ...
# Adding a serial port (**voids warranty**)
[![][41851]][41852]
[][41853]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][41854]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
First need to remove the rubber caps in each corner on the back plate and then remove the tiny screws. Then we've GOT SOME HEADACHES! as it seems the case is glued shut see: <https://www.youtube.com/watch?v=gvyKorhEncY>
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][41854].
# Pictures
Take some pictures of your device, [ upload them][41855], and add them here.
  * [![Device front.jpg][41856]][41823]
  * [![Device back.jpg][41857]][41858]
  * [![Device buttons 1.jpg][41859]][41860]
  * [![Device buttons 2.jpg][41861]][41862]
  * [![Device board front.jpg][41863]][41864]
  * [![Device board back.jpg][41865]][41866]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
