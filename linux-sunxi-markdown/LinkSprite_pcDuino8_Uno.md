# LinkSprite pcDuino8 Uno
LinkSprite pcDuino8 Uno  
---  
[![PcDuino8 Uno Front.jpg][31528]][31529]  
Manufacturer |  [LinkSprite][31530]  
Dimensions |  96 _mm_ x 56 _mm_ x 20 _mm_  
Release Date |  October 2015   
Website |  [PcDuino8 Product Page][31531]  
Specifications   
SoC |  [H8][31532] @ 2Ghz   
DRAM |  1GiB DDR3 @ xxxMHz   
Power |  DC 5V @ 2A (micro-usb)   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug, HDMI   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][31533])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART, MIPI (camera), Arduino-compatible headers   
This page needs to be properly filled according to the [New Device Howto][31534] and the [New Device Page guide][31535].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][31536]
  * [2 Sunxi support][31537]
    * [2.1 Current status][31538]
    * [2.2 Manual build][31539]
      * [2.2.1 U-Boot][31540]
        * [2.2.1.1 Sunxi/Legacy U-Boot][31541]
        * [2.2.1.2 Mainline U-Boot][31542]
      * [2.2.2 Linux Kernel][31543]
        * [2.2.2.1 Sunxi/Legacy Kernel][31544]
        * [2.2.2.2 Mainline kernel][31545]
  * [3 Tips, Tricks, Caveats][31546]
    * [3.1 CPU Heating issues][31547]
    * [3.2 FEL mode][31548]
    * [3.3 Arduino Compatability][31549]
  * [4 Adding a serial port][31550]
    * [4.1 Locating the UART][31551]
  * [5 Pictures][31552]
  * [6 Also known as][31553]
  * [7 See also][31554]
    * [7.1 Manufacturer images][31555]

# Identification
A white PCB with an H8 chip. 
The PCB has the following silkscreened on it: 
[code] 
    PcDuino8 Uno
    V01
    www.pcduino.com
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
There currently is no support for this board. There are other H8 devices supported, so support may be possible. 
## Manual build
You can build things for yourself by following our [ Manual build howto][31556] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Unsupported. 
#### Mainline U-Boot
Unsupported. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Unsupported. 
#### Mainline kernel
Unsupported. 
# Tips, Tricks, Caveats
## CPU Heating issues
The A83/H8 absolutely needs a heatsink, active cooling is heavily recommended, otherwise the CPU will lower max frequency or even stop using cores. 
## FEL mode
The UBOOT button triggers [ FEL mode][31557]. 
## Arduino Compatability
pcDuino8 Uno is pin to pin compatible with Arduino so that existing Arduino shields can be installed on pcDuino and many Arduino libraries can run in pcDuino programming environment. 
# Adding a serial port
## Locating the UART
The pcDuino8 Uno provides access two of the H8's UARTs. See the [UART howto][31558] for more details. 
The 3-pin header labelled "UART" sticking out from the side of the board is the H8's UART0. Pin 1 (with a square pad, closest to the uSD slot) is TX, pin 2 is ground, pin 3 is RX. 
UART3 is available on the Arduino connectors. UART3 is in the standard place for an Arduino UART. 
# Pictures
  * [![PcDuino8 Uno Front.jpg][31559]][31529]
  * [![PcDuino8 Uno Back.jpg][31560]][31561]

# Also known as
This device has not been rebadged. 
# See also
  * [LinkSprite pcDuino][31562]
  * [LinkSprite pcDuino Lite][31563]
  * [LinkSprite pcDuino Lite WiFi][31564]
  * [LinkSprite pcDuino2][31565]
  * [LinkSprite pcDuino3][31566]
  * [LinkSprite pcDuino3 Nano][31567]
  * [Schematic][31568]
  * [Developers Kit for OpenCV User Guide][31569]
  * [LinkSprite's pcDuino8 kernel repository on GitHub][31570]
  * [pcDuino8 Uno ubuntu and android images][31571]

## Manufacturer images
The [Ubuntu 14 image that LinkSprite provides][31572] uses a modified linux-sunxi 3.4.39 kernel. Their patches and build scripts are available [on GitHub][31570]. 
There is also a [Ubuntu 14 image bundled with OpenCV][31573]. 
Also available is an [Android 4.4 image provided by LinkSprite][31574].
