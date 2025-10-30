# Xunlong Orange Pi Lite 2
Xunlong Orange Pi Lite 2  
---  
[![Orange Pi Lite 2 Top Down.jpg][60956]][60957] [][60958]  
Manufacturer |  [OrangePi][60959]  
Dimensions |  _48mm_ x _69mm_  
Website |  [Device Product Page][60960]  
Specifications   
SoC |  [H6][60961] @ 1.8 Ghz   
DRAM |  1GiB LPDDR3 @ xxxMHz   
Power |  DC 5V @ 3A   
Features   
Video |  HDMI (Type 2.0A - full)   
Audio |  HDMI, on-board microphone   
Network |  WiFi   
Storage |  µSD   
USB |  1 USB3.0 Host 1 USB2.0 Host, 1 USB2.0 OTG   
Other |  IRDA   
Headers |  UART, JTAG, LCD, VGA  
This page needs to be properly filled according to the [New Device Howto][60962] and the [New Device Page guide][60963].
_The Orange Pi Lite 2 is a 64-bit_[H6][60961] _based single board computer produced by[Xunlong][60964]._
The Orange Pi Lite 2 is the older brother of [Orange Pi Lite][60965]. It sports the powerful Allwinner [H6][60961] SoC. In comparison to Orange Pi Lite based on [H3][60966], this board has a Quad Core Arm Cortex-A53 cpu. The SoC is capable of 4k at 60fps with it's ARM Mali-T720 MP2 Graphics Processor. 
Unlike other boards, it uses a gigabyte LPDDR3 instead of _power-eater_ DDR3. It also comes with USB 3.0 Host, unlike it's cousin, [Orange Pi One Plus][60967]. It misses the Ethernet but it's got WiFi on board which is more handy if you are using it wirelessly. It comes also with low-level interfaces such as UART, SPI ,I²C and etc. 
## Contents
  * [1 Identification][60968]
  * [2 Sunxi support][60969]
    * [2.1 Current status][60970]
    * [2.2 Images][60971]
    * [2.3 HW-Pack][60972]
    * [2.4 BSP][60973]
    * [2.5 Manual build][60974]
      * [2.5.1 U-Boot][60975]
        * [2.5.1.1 Sunxi/Legacy U-Boot][60976]
        * [2.5.1.2 Mainline U-Boot][60977]
      * [2.5.2 Linux Kernel][60978]
        * [2.5.2.1 Sunxi/Legacy Kernel][60979]
        * [2.5.2.2 Mainline kernel][60980]
  * [3 Expansion Port][60981]
  * [4 Tips, Tricks, Caveats][60982]
    * [4.1 FEL mode][60983]
    * [4.2 Device specific topic][60984]
    * [4.3 ...][60985]
  * [5 Serial port][60986]
  * [6 Pictures][60987]
  * [7 Also known as][60988]
  * [8 See also][60989]
    * [8.1 Manufacturer images][60990]

# Identification
[Template:Remove if done][60991]
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][60989]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][60992] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Give Link to kernel repo
#### Mainline kernel
Use the **sun50i-h6-orangepi-lite2.dts** device-tree binary. 
# Expansion Port
The Orange Pi Lite 2 has a 26-pin, 0.1" connector (called CON12 in the schematics) with several low-speed interfaces. 
2x13 Header   
---  
1 | _3.3V_ | 2 | _5V_  
3 | TWI1-SDA / PH6 / GPIO230  | 4 | _5V_  
5 | TWI1-SCK / PH5 / GPIO229  | 6 | _GND_  
7 | PWM1 / PH4 / GPIO228  | 8 | UART2-RTS / PD21 / GPIO117   
9 | _GND_ | 10 | UART2-CTS / PD22 / GPIO118   
11 | UART3-RX / PD24 / GPIO120  | 12 | SDC2-D3 / PC9 / GPIO73   
13 | UART3-TX / PD23 / GPIO119  | 14 | _GND_  
15 | UART3-CTS / PD26 / GPIO122  | 16 | SDC2-D2 / PC8 / GPIO72   
17 | _3.3V_ | 18 | SPI0-WP / PC7 / GPIO71   
19 | SPI0-MOSI/ PC2 / GPIO66  | 20 | _GND_  
21 | SPI0-MISO / PC3 / GPIO67  | 22 | UART3-RTS / PD25 / GPIO121   
23 | SPI0-CLK / PC0 / GPIO64  | 24 | SPI0-CS / PC5 / GPIO69   
25 | _GND_ | 26 | SPI1-CS / PH3 / GPIO227   
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
Booting without an SD card automagically enters FEL mode. 
[code] 
    ./sunxi-fel version
    AWUSBFEX soc=00001728(H6) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
[/code]
The U BOOT pin on the [H6][60961] SoC is routed to test-point TP28 on it's PCB. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Serial port
[![][60993]][60994]
[][60995]
OrangePi Lite 2 UART pads
The UART pins are located between the USB 3.0 port and the IR receiver. They are marked as _TX_ , _RX_ and _GND_ on the bottom of the PCB. Just attach some leads according to our [UART Howto][60996]. 
# Pictures
  * [![Orange Pi Lite 2 Side View.jpg][60997]][60998]
  * [![Orange Pi Lite 2 Bottom.jpeg][60999]][61000]

# Also known as
There are currently no known rebadged devices. Update this section if you know otherwise. 
# See also
  * AXP805 Datasheet: [File:AXP805 Datasheet V1.0 en.pdf][61001]
  * H6 Datasheet: [File:Allwinner H6 V200 Datasheet V1.1.pdf][61002]
  * H6 User Manual: [File:Allwinner H6 V200 User Manual V1.1.pdf][61003]
  * Schematics 2.0: [File:OrangePi Lite2 Schematics v2.0.pdf][61004]

## Manufacturer images
Optional. Add non-sunxi images in this section.
