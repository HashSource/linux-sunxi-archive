# ClockworkPi R01
ClockworkPi R01  
---  
[![Clockworkpi R01 front.jpg][12999]][13000]  
Manufacturer |  [Clockwork][13001]  
Dimensions |  67.6 _mm_ x 31 _mm_  
Release Date |  03/2022   
Website |  [DevTerm Home Page][13002]  
Specifications   
SoC |  [D1][13003] @ 1.0Ghz   
DRAM |  1GiB DDR3 @ 792MHz, 2×[H5TQ4G63EFR][13004]  
Features   
This page needs to be properly filled according to the [New Device Howto][13005] and the [New Device Page guide][13006].
## Contents
  * [1 Software Support][13007]
  * [2 Add-ons][13008]
  * [3 Carrier Boards][13009]
    * [3.1 Clockwork nomenclature][13010]
    * [3.2 ClockworkPi v3.14][13011]
      * [3.2.1 Known Issue: DevTerm Kit: "UART" port on "ext" board is unstable or "read only"][13012]
    * [3.3 Waveshare Compute Module PoE Board][13013]
    * [3.4 WaveShare PiLaptop][13014]
  * [4 Pictures][13015]
  * [5 External links][13016]

## Software Support
Linux and U-Boot upstreaming are in progress. See [Allwinner_Nezha#Manual_build][13017] for build instructions. For U-Boot on the DevTerm, use the `devterm_r_01_defconfig` configuration. 
## Add-ons
On the back/bottom side are solder pads for a SPI flash, NAND or NOR. You need to add resistors in order to use it. The top left pin close to the edge is pin 1 (CS). 
## Carrier Boards
ClockworkPi's R-01 "core" module is pin compatible with RaspberryPi CM3 via DDR2-SODIMM 200 Pins interface. 
#### Clockwork nomenclature
  * "core": such as R01, slots into a CM3 compatible interface on the "mainboard".
  * "mainboard": is the [ClockworkPi v3.14][13018] which accepts a "core" (R01),
  * "exp" - M.2 interface
  * "kit" - bundles together "core", "main", "ext", etc. Examples are [DevTerm Kit R-01][13019] and [uConsole Kit R-01][13020]

### ClockworkPi v3.14
This board features 
  * PMU which supports reliable and complete lithium battery charge and discharge management
  * Integrated 5G-WIFI (802.11ac) + Bluetooth 5.0
  * High-gain antenna
  * 3x USB-A 2.0 interface
  * USB-C* charging port
  * TF card (Micro SD card) slot
  * 40 Pins MIPI screen interface
  * Micro-HDMI interface
  * 3.5 headphone jack, supports microphone input
  * Onboard stereo audio power amplifier chip
  * 40 Pins GPIOs expansion interface (using standard 0.5mm FPC connector)
  * 52 Pins extension module interface (using standard M.2 Mini PCI-E connector) for the “EXT. module”. Pins for UART are on this connector.

[Schematics][13021]
#### Known Issue: DevTerm Kit: "UART" port on "ext" board is unstable or "read only"
DevTerm's "exp" board has electrical issues with the USB OTG UART. See: 
  * <https://forum.clockworkpi.com/t/devterm-r-01-ext-board-uart-is-read-only/8704>
  * <https://github.com/emutyworks/DevTerm-R01/wiki/Connect-with-USB-UART>
  * Another fix is to add jumper wires to UART Rx, Tx, Ground and use an external high-quality **3.3v** UART. **DO NOT USE THIS METHOD WITH AN RS232 ADAPTER.**

### Waveshare Compute Module PoE Board
[Waveshare wiki][13022]
This board features a PoE ethernet port connected via USB to the module. 
In addition, there are 3 micro USB ports for power supply, a built-in USB serial adapter, and USB host, as well as 4 USB-A host connectors. 
Note that this board offers **no** access to USB0, which is the OTG/FEL USB port. 
More connectors: 
  * video: HDMI (Type A - full), 1x MIPI DSI, 2x MIPI CSI
  * audio: via HDMI, I2S
  * storage: µSD slot
  * fan header
  * 2 LEDs for power status and "Power ACT" (not applicable to the R01?)

### WaveShare PiLaptop
[Waveshare wiki][13023]
Whether this laptop works with the R01 needs confirmation. It was designed for the Raspberry Pi CM3. 
## Pictures
  * [![][13024]][13000]
front view 
  * [![][13025]][13026]
back view 
  * [![][13027]][13028]
Waveshare PoE board 

# External links
  * [hardware design, schematics, kernel patches, etc][13029]
