# LinkSprite pcDuino Lite
LinkSprite pcDuino Lite  
---  
[![Device front.jpg][31610]][31611]  
Manufacturer |  [Linksprite][31612]  
Website |  [Product Page][31613]  
Specifications   
SoC |  [A10][31614] @ 1Ghz   
DRAM |  512MiB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI   
Audio |  ?   
Network |  10/100Mbps Ethernet ([Manufacturer device][31615])   
Storage |  µSD   
USB |  ?   
Headers |  ?   
  
This device is very similar to the [LinkSprite pcDuino][31616]. The main difference is that it has 512M of RAM instead of 1G. 
## Contents
  * [1 Identification][31617]
  * [2 Sunxi support][31618]
    * [2.1 U-Boot][31619]
      * [2.1.1 Mainline U-Boot][31620]
    * [2.2 Linux Kernel][31621]
      * [2.2.1 Mainline kernel][31622]
  * [3 Tips, Tricks, Caveats][31623]
    * [3.1 FEL mode][31624]
    * [3.2 Locating the UART][31625]
  * [4 Pictures][31626]
  * [5 Also known as][31627]
  * [6 TODO][31628]
  * [7 See also][31629]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Manufacturer Marketing Name
    ModelNumber
[/code]
The PCB has the following silkscreened on it: 
[code] 
    LIA-BB-V6.66
    1970-01-01
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
### U-Boot
#### Mainline U-Boot
Using the Linksprite_pcDuino_defconfig build target works with u-boot v2019.01. 
### Linux Kernel
#### Mainline kernel
At the time of writing, there is no pcDuino Lite dts in Linux, but when using the **sun4i-a10-pcduino.dts** device-tree file of the [mainline kernel][31630], many peripheral work out of the box. 
Status with linux-libre 5.3.1-gnu-1 in Parabola: 
  * microSD works: booted with the rootfs on it
  * Ethernet works
  * The two USB host port work: tested with an USB key

# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][31631]. 
## Locating the UART
[![][31632]][31633]
[][31634]
LinkSprite pcDuino UART pads
The RX, TX, and GND pins are located near the MENU button as shown in tthe picture. Just attach some leads according to our [UART Howto][31635]. 
# Pictures
Take some pictures of your device, [ upload them][31636], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][31637]][31611]
  * [![Device back.jpg][31638]][31639]
  * [![Device buttons 1.jpg][31640]][31641]
  * [![Device buttons 2.jpg][31642]][31643]
  * [![Device board front.jpg][31644]][31645]
  * [![Device board back.jpg][31646]][31647]

# Also known as
List rebadged devices here.
# TODO
  * Find the schematics, vendor images, vendor source code and document the differences with the pcDuino
  * If relevant, send patches in upstream Linux and u-boot to support the pcDuino Lite
  * Complete the missing section in this wiki page

# See also
  * [LinkSprite pcDuino][31616]
  * [LinkSprite pcDuino V2][31648]
  * [LinkSprite pcDuino V3][31649]
  * [LinkSprite pcDuino Lite WiFi][31650]
