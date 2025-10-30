# LinkSprite pcDuino Lite WiFi
LinkSprite pcDuino Lite WiFi  
---  
[![Pcduino lite wifi top.jpg][31685]][31686]  
Manufacturer |  [Linksprite][31687]  
Dimensions |  105 _mm_ x 53 _mm_  
Website |  [Product Page][31688]  
Specifications   
SoC |  [A10][31689] @ 1Ghz   
DRAM |  256MiB DDR3 @ 408MHz ([H5TQ1G83BFR][31690])   
NAND |  2GB   
Power |  DC 5V @ 2A (micro-USB)   
Features   
Video |  HDMI   
Audio |  HDMI   
Network |  WiFi 802.11b/g/n (Realtek RTL8188CUS)   
Storage |  µSD   
USB |  USB 2.0 Host, USB 2.0 OTG   
Headers |  UART, SPI, Arduino Compatible Headers   
## Contents
  * [1 Identification][31691]
  * [2 Sunxi support][31692]
    * [2.1 Current status][31693]
    * [2.2 Manual build][31694]
      * [2.2.1 U-Boot][31695]
        * [2.2.1.1 Sunxi/Legacy U-Boot][31696]
        * [2.2.1.2 Mainline U-Boot][31697]
      * [2.2.2 Linux Kernel][31698]
        * [2.2.2.1 Sunxi/Legacy Kernel][31699]
        * [2.2.2.2 Mainline kernel][31700]
    * [2.3 HW-Pack][31701]
    * [2.4 BSP][31702]
  * [3 Tips, Tricks, Caveats][31703]
    * [3.1 Building images using Yocto][31704]
    * [3.2 Building images using Buildroot][31705]
    * [3.3 FEL mode][31706]
    * [3.4 LEDs][31707]
    * [3.5 DRAM][31708]
    * [3.6 Compatibility with Arduino shields][31709]
  * [4 Adding a serial port][31710]
  * [5 Pictures][31711]
  * [6 See also][31712]
    * [6.1 Manufacturer images][31713]

# Identification
A white PCB with an A10 chip and Arduino compatible headers on it. Sticker on the back of the board helpfully reads "pcDuino lite WiFi". 
# Sunxi support
## Current status
  * Supported by the upstream U-Boot and kernel
  * Supported by legacy sunxi/legacy kernel v3.4
  * Not supported by the legacy U-Boot, though basic implementation is available in 3rd party work-in-progress github branch.

## Manual build
You can build things for yourself by following our [ Manual build howto][31714] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
This board is not supported by [legacy U-Boot][31715]. Use **pcDuino_Lite_WiFi_config** from 3rd party [development branch][31716]. 
#### Mainline U-Boot
Config **Linksprite_pcDuino_defconfig** for [LinkSprite_pcDuino][31717] works fine for pcDuino-Lite-WiFi board as well. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [**pcduino-lite-wifi.fex**][31718] file. 
#### Mainline kernel
  * Use the default **sunxi_defconfig** kernel configuration file as a baseline, and run _menuconfig_ to enable extra device drivers, such as USB keyboard/mouse or wireless dongle. For instance, enable _CONFIG_RTL8192CU_ in order to make the onboard Realtek WiFi card work.
  * Device-tree **sun4i-a10-pcduino.dts** for [LinkSprite_pcDuino][31717] works fine for pcDuino-Lite-WiFi board as well. It may need to be tweaked depending on the Arduino shield in use.

## HW-Pack
TODO 
## BSP
TODO 
# Tips, Tricks, Caveats
## Building images using Yocto
Core images for pcDuino-Lite-WiFi board can be built using the following basic building blocks: 
  * [poky][31719]: reference distribution of the Yocto Project
  * [meta-openembedded][31720]: collection of layers for the OE-core universe
  * [meta-sunxi][31721]: official sunxi OpenEmbedded layer for Allwinner-based boards

This [README][31722] provides build instructions specific to pcDuino-Lite-WiFi board including the following configurations: 
  * images with sunxi/legacy U-Boot and kernel based on Yocto v1.8 _Fido_ release
  * images with upstream U-Boot and kernel based on Yocto v2.1 _Krogoth_ release

## Building images using Buildroot
Support for pcDuino boards has been added to buildroot. Build instructions are available in [readme.txt][31723]. Follow the same instructions for pcDuino-Lite-WiFi. 
## FEL mode
The UPGRADE button (SW2) triggers FEL mode. 
## LEDs
The board has 5 yellow LEDs: 
  * LED1: power indicator (always on)
  * LED2: WiFi indicator, connected to the WiFi chip
  * LED3: labeled RX, accessible via GPIO (PH16 pin)
  * LED4: labeled TX, accessible via GPIO (PH15 pin)
  * LED5: labeled CLK, which is connected to the PI11 pin and can also have a dedicated use as SPI0_CLK. This CLK LED serves as either an SPI activity indicator when SPI hardware is connected or just an ordinary LED if no SPI hardware is present.

## DRAM
RAM of the board is powered by two 128Mx8 DDR3 chips (Hynix [H5TQ1G83BFR-H9C][31690] 215V), both on the front side of the PCB. 
## Compatibility with Arduino shields
The pcDuino has pinout pretty similar to the Arduino and implements an Arduino-style API (in C/C++), but it's not perfectly compatible with the Arduino platform. 
Generally, the Arduino ADC reference voltage is AVCC = 5V, so its range is also 5V. However, the pcDuino ADC reference voltage is 3.3V, so pcDuino ADC range is only 3.3V. It works well with a 3.3V Arduino Uno R3. To measure a 5V signal with Arduino, use a voltage divider. 
# Adding a serial port
[![][31724]][31725]
[][31726]
DEVICE UART pads
P3 header with 3 pins (TX - pin with square pad in the corner, GND, RX) exposes UART0. Make sure to refer to [UART howto][31727]. 
# Pictures
  * [![Pcduino lite wifi top.jpg][31728]][31686]
  * [![Pcduino lite wifi bottom.jpg][31729]][31730]
  * [![Pcduino lite wifi reset.jpg][31731]][31732]
  * [![Pcduino lite wifi upgrade.jpg][31733]][31734]

# See also
  * [LinkSprite_pcDuino][31717]
  * [LinkSprite pcDuino V2][31735]
  * [LinkSprite pcDuino V3][31736]

## Manufacturer images
Manufacturer images for pcDuino Lite WiFi are available on LinkSprite [download page][31737]
