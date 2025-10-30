# Sipeed MaixSense
Sipeed MaixSense  
---  
[![MaixSense front.jpg][50886]][50887]  
Manufacturer |  [Sipeed][50888]  
Dimensions |  33 _mm_ x 39.9 _mm_ x 9 _mm_  
Release Date |  Not fully released yet   
Specifications   
SoC |  [R329][50889] @ 1.512Ghz   
DRAM |  256MiB co-packaged DDR3 @ 774MHz   
Power |  DC 5V via Type-C ports   
Features   
LCD |  240x240 (1.52" 1:1)   
Audio |  on-board two microphonee and one speaker   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8723BS/RTL8723DS][50890])   
Storage |  µSD, SPI NOR/NAND (NC)   
USB |  1 USB2.0 OTG (In Type-C port with hack to generate an ID signal)   
Other |  On-board USB2UART for debug UART   
Headers |  two GPIO headers   
Sipeed MaixSense is a development kit by Sipeed, utilizing their own Sipeed Maix IIA SoM. 
## Contents
  * [1 Identification][50891]
  * [2 Sunxi support][50892]
    * [2.1 Current status][50893]
    * [2.2 Manual build][50894]
      * [2.2.1 U-Boot][50895]
        * [2.2.1.1 Mainline U-Boot][50896]
      * [2.2.2 Linux Kernel][50897]
        * [2.2.2.1 Mainline kernel][50898]
  * [3 Tips, Tricks, Caveats][50899]
    * [3.1 FEL mode][50900]
  * [4 Adding a serial port][50901]
  * [5 Pictures][50902]
  * [6 Schematic][50903]
  * [7 See also][50904]

# Identification
On the baseboard, Sipeed logo, 
[code]
    Sipeed
[/code]
and 
[code]
    MaixSense
[/code]
is silkscreened, and on the SoM, 
[code]
    Sipeed
[/code]
and 
[code]
    M2A
[/code]
. 
# Sunxi support
## Current status
Mainline support is WIP. 
## Manual build
You can build things for yourself by following our [ Manual build howto][50905] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Still being done. To try out the working-in-progress code, retrieve the code at [[1]][50906] and use the _sipeed_maixsense_defconfig_ build target. 
### Linux Kernel
#### Mainline kernel
Still being done. To try out the working-in-progress code, retrieve the code at [[2]][50907] and use the _sun50i-r329-maixsense.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
By default no SPI Flash is soldered, that means just removing SD card makes the SoC to enter FEL. 
# Adding a serial port
Just plug a cable connected to your PC to the port at the down side (next to the 4-pin connector, which provides another UART, not the debug one). An onboard CH340 USB-UART bridge is available for accessing the debug UART. 
# Pictures
Sipeed Maix IIA SoM: 
  * [![M2A front.png][50908]][50909]
  * [![M2A back.png][50910]][50911]

MaixSense Kit: 
  * [![MaixSense front.jpg][50912]][50887]
  * [![MaixSense back.png][50913]][50914]

# Schematic
\- [Maix II A schematics][50915] \- [MaixSense schematics][50916]
# See also
\- [Official description at Jishu community][50917]
