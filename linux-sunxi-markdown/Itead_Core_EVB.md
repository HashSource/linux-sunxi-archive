# Itead Core EVB
Itead Core EVB  
---  
[![Device front.jpg][28260]][28261]  
Manufacturer |  [ITEAD][28262]  
Dimensions |  140 _mm_ x 90 _mm_ x 20 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][28263]  
Specifications   
SoC |  [A20][28264] @ [Template:1][28265]Ghz   
DRAM |  1GiB/2GiB   
NAND |  4GB   
Power |  DC 7V - 23V   
Features   
LCD |  none   
Touchscreen |  none   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone / microphone plug, HDMI, SPDIF (toslink / optical)   
Network |  10/100/1000Mbps Ethernet ([Manufacturer device][28266])   
Storage |  µSD, SATA   
USB |  3 USB2.0 Host, 1 USB2.0 OTG   
Camera |  none   
Other |  IRDA, 2 color LED   
Headers |  UART, JTAG, LCD, VGA, I2C...   
This page needs to be properly filled according to the [New Device Howto][28267] and the [New Device Page guide][28268].
## Contents
  * [1 Identification][28269]
  * [2 Sunxi support][28270]
    * [2.1 Current status][28271]
    * [2.2 Images][28272]
    * [2.3 Manual build][28273]
      * [2.3.1 U-Boot][28274]
        * [2.3.1.1 Sunxi/Legacy U-Boot][28275]
        * [2.3.1.2 Mainline U-Boot][28276]
      * [2.3.2 Linux Kernel][28277]
        * [2.3.2.1 Sunxi/Legacy Kernel][28278]
        * [2.3.2.2 Mainline kernel][28279]
  * [3 Tips, Tricks, Caveats][28280]
    * [3.1 FEL mode][28281]
    * [3.2 UART][28282]
  * [4 Pictures][28283]
  * [5 Also known as][28284]
    * [5.1 Manufacturer images][28285]

# Identification
On the back of the device, the following is printed: 
[code] 
    ITEAD Core EVB
    Open Source Hardware
[/code]
The PCB has the following silkscreened on it: 
[code] 
    ITEAD Core EVB
    Open Source Hardware
[/code]
# Sunxi support
## Current status
This device runs both mainline and legacy u-boot as well as mainline & legacy kernels. 
## Images
No sunxi images available from ITEAD 
## Manual build
You can build things for yourself by following our [ Manual build howto][28286] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][28287] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Networking is flaky. Specifically - on some power-ups - the device does not request an address over DHCP, and rebooting / `dhcpcd eth0` does not fix this situation. Only a power cycle seems to work. However, booting with UART0 connected (especially with the device's RCV & GND connected) seems to make this work 100% of the time. 
## FEL mode
The _FEL_ button triggers [ FEL mode][28288]. 
## UART
UART-0 is available via pins on the J4 (32 pin) side connector. 
[![][28289]][28290]
[][28291]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][28292]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
# Pictures
Take some pictures of your device, [ upload them][28293], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][28294]][28261]
  * [![Device back.jpg][28295]][28296]
  * [![Device buttons 1.jpg][28297]][28298]
  * [![Device buttons 2.jpg][28299]][28300]
  * [![Device board front.jpg][28301]][28302]
  * [![Device board back.jpg][28303]][28304]

# Also known as
AW2401 AW2402 
## Manufacturer images
