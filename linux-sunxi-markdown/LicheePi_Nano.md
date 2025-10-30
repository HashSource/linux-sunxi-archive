# LicheePi Nano
LicheePi Nano  
---  
[![LicheePi Nano Front.jpg][30818]][30819]  
Manufacturer |  [Lichee-Pi][30820]  
Dimensions |  25.4 _mm_ x 33.0 _mm_  
Release Date |  2018   
Website |  [[1]][30821]  
Specifications   
SoC |  [F1C100s][30822] @ 408Mhz   
DRAM |  32MiB DDR @ 24M~408MHz   
Power |  via GPIO pins or MicroUSB Jack   
Features   
LCD |  optional RGB LCD FPC   
Touchscreen |  optional   
Audio |  2x speaker, 1x microphone via header pins   
Network |  WiFi 802.11 b/g/n ([ESP8089][30823]) optional via µSD   
Storage |  µSD (not all models have slot), optional on-board 8MB, 16MB or 32MB SPI NOR Flash   
USB |  1 USB2.0 OTG   
Headers |  SPI, I2C, UART   
This page needs to be properly filled according to the [New Device Howto][30824] and the [New Device Page guide][30825].
Tiny development board about the size of an SD card. 
## Contents
  * [1 Identification][30826]
  * [2 Sunxi support][30827]
    * [2.1 Images][30828]
    * [2.2 Manual build][30829]
      * [2.2.1 Mainline U-Boot][30830]
      * [2.2.2 Mainline Linux Kernel][30831]
  * [3 Tips, Tricks, Caveats][30832]
    * [3.1 FEL mode][30833]
    * [3.2 Device specific topic][30834]
  * [4 Adding a serial port][30835]
  * [5 Pictures][30836]
  * [6 Schematic][30837]
  * [7 See also][30838]
    * [7.1 Manufacturer images][30839]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    LiCHEE
    NANO
[/code]
# Sunxi support
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][30838]. If no sunxi based images are available, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][30840] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _licheepi_nano_defconfig_ build target. Available since U-Boot v2022.04. 
### Mainline Linux Kernel
Use the _suniv-f1c100s-licheepi-nano.dts_ device-tree tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The FEL mode can be used over the on-board Micro-USB connector. 
On models **without** on-board flash, just removing the SD Card triggers FEL mode. 
On models **with** on-board SPI flash, according to the documentation you have the following options to enter FEL mode: 
  * "Short-circuit the 1 and 4 pins [those are VSS(GND) and CS] of the flash, power on again, release the short circuit after powering on"
  * "Before booting to the kernel, press Enter to enter uboot and execute `sf probe 0;sf erase 0 0x100000;reset`"

Both of these methods seem to be working, however keep in mind, that the latter **erases the flash chip**! This is only useful if you want to upload a new image anyway, otherwise use the first method! 
Since one of the pins of the flash chip that need to be shorted to trigger FEL mode is GND, you can use any ground point and connect it to pin 4 of the flash chip. An easy way of doing this is to use the GND pin of the board, like depicted bellow. 
[![][30841]][30842]
[][30843]
Shorting pin 4 (CS) of the flash chip to ground with a jumper cable, that is connected to the GND pin on the other end.
After successfully triggering FEL mode, you should see the following USB device on your host: 
[code] 
    Bus XXX Device XXX: ID 1f3a:efe8 Allwinner Technology sunxi SoC OTG connector in FEL/flashing mode
    
[/code]
## Device specific topic
If there are no further device specific topics to add, remove these sections.
# Adding a serial port
The UART0 RX and TX pins are on PE0 and PE1, connected to the GPIO header pins, close to the microSD card slot. They are also marked as U0TX and U0RX. They carry the 3.3V level signal from the SoC, refer to the [UART howto][30844] for more details. 
Note: The board expose 2 UART interfaces by default (UART0 and UART2), you need UART0 for the boot console. 
[![][30845]][30846]
[][30847]
UART and power hooked up to access boot console
The stock software uses 115200 baud rate. 
# Pictures
  * [![LicheePi Nano top.jpg][30848]][30849]
  * [![LicheePi Nano bottom.jpg][30850]][30851]
  * [![LicheePi Nano with pins.jpg][30852]][30853]

# Schematic
The schematic for the board can be found on the manufacturer's website: [[2]][30854]
# See also
  * [Getting started video by DVXLab on YouTube][30855]
  * [Source for the Chinese documentation on GitHub][30856]

## Manufacturer images
Optional. Add non-sunxi images in this section.
