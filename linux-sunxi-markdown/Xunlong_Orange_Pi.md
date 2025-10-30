# Xunlong Orange Pi
Xunlong Orange Pi  
---  
[![Xunlong OrangePi.png][60269]][60270]  
Manufacturer |  [OrangePi][60271]  
Dimensions |  112 _mm_ x 60 _mm_  
Release Date |  November 2014   
Website |  [Orange Pi Product Page][60272]  
Specifications   
SoC |  [A20][60273] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  8GB(optional)   
Power |  DC 5V @ 2A (best via DC input)   
Features   
Video |  HDMI (Type A - full), CVBS, RGB/LVDS, VGA   
Audio |  3.5 mm jack, PHOUT   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][60274]), wifi 802.11 b/g/n   
Storage |  SD, SATA (with power connector: JST XH 2.5mm header, providing +5V)   
USB |  4 USB2.0 Host, 1 USB2.0 OTG   
Other |  [CIR][60275]  
Headers |  2 pin UART, 9 pin UART (including power source), LCD/ LVDS, CSI, 26 pin GPIO   
Orange Pi is [A20][60273] based development board produced by [Xunlong][60276]. The Orange Pi was released in November 2014 and featured a standard TF card slot and a 26 pin GPIO connector (similar to the Raspberry Pi A/B). The Orange Pi franchise has later been supplemented with other Orange Pi boards, but only the original Orange Pi and [Orange Pi Mini][60277] are actually based on [A20][60273]. 
## Contents
  * [1 Identification][60278]
  * [2 Sunxi support][60279]
    * [2.1 Current status][60280]
    * [2.2 Images][60281]
    * [2.3 HW-Pack][60282]
    * [2.4 BSP][60283]
    * [2.5 Manual build][60284]
      * [2.5.1 U-Boot][60285]
        * [2.5.1.1 Sunxi/Legacy U-Boot][60286]
        * [2.5.1.2 Mainline U-Boot][60287]
      * [2.5.2 Linux Kernel][60288]
        * [2.5.2.1 Sunxi/Legacy Kernel][60289]
        * [2.5.2.2 Mainline kernel][60290]
  * [3 Expansion Port][60291]
  * [4 Tips, Tricks, Caveats][60292]
    * [4.1 FEL mode][60293]
    * [4.2 LEDs][60294]
    * [4.3 SATA][60295]
  * [5 Adding a serial port][60296]
    * [5.1 Locating the UART][60297]
  * [6 Pictures][60298]
  * [7 Variants][60299]
    * [7.1 A20 based][60300]
    * [7.2 Other SoCs][60301]
  * [8 Also known as][60302]
  * [9 See also][60303]
    * [9.1 Manufacturer images][60304]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi
[/code]
# Sunxi support
## Current status
Supported, but no longer manufactured by Xunlong. (2016-05-24) 
**Note:** Orange Pi's GMAC is not supported in the community kernel. A commit within [Orange Pi Github fork of linux-sunxi-3.4][60305] seems to provide GMAC support for Orange Pi. This has to be proved and merged into linux-sunxi. 
Xunlong seems to use an important tweak of both the Linux 3.4 kernel and U-Boot networking code for the Orange Pi: The GMAC driver is specifically modified to set the GMAC_TX_DELAY parameter to 3. This adjusts the relative timing of the clock and data signals to the PHY in order to compensate for differing trace lengths on the PCB ([details][60306]; the [pcDuino3 Nano][60307] has the same problem). Without this modification, the Ethernet port will work at 100Mbit, but not (or not reliably) at 1000Mbit. Upstream U-Boot now sets this parameter itself, so the kernel patch isn't needed any more ([patch][60308]). 
## Images
## HW-Pack
## BSP
## Manual build
You can build things for yourself by following our [ Manual build howto][60309] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
The .fex file can be found in sunxi-boards as [orangepi.fex][60310]
#### Mainline U-Boot
For building u-boot, use the **orangepi** target (`make orangepi_config`). 
### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
Use the **sun7i-a20-orangepi.dtb** device-tree file for the [mainline kernel][60311]
# Expansion Port
The Orange Pi has a 26-pin, 0.1" connector with several low-speed interfaces. 
2x13 Header   
---  
1 | _3.3V_ | 2 | _5V_  
3 | PB21 TWI2-SDA  | 4 | _5V_  
5 | PB20 TWI2-SCK  | 6 | _GND_  
7 | PI3 PWM1  | 8 | PH0 UART3_TX   
9 | _GND_ | 10 | PH1 UART3_RX   
11 | PI19 UART2_RX  | 12 | PH2   
13 | PI18 UART2_TX  | 14 | _GND_  
15 | PI17 UART2_CTS  | 16 | PH20 CAN_TX   
17 | _3.3V_ | 18 | PH21 CAN_RX   
19 | PI12 SPI0_MOSI  | 20 | _GND_  
21 | PI13 SPI0_MISO  | 22 | PI16 UART2_RTS   
23 | PI11 SPI0_CLK  | 24 | PI10 SPI0_CS0   
25 | _GND_ | 26 | PI14 SPI0_CS1   
  
The Orange Pi also has a 18-pin, 0.1" connector with several low-speed interfaces. 
2x9 Header   
---  
1 | _5V_ | 2 | _3.3V_  
3 | PH5  | 4 | PI21 UART7_RX   
5 | PH3  | 6 | PI20 UART7_TX   
7 | _GND_ | 8 | _GND_  
9 | RESET#  | 10 | LRADC1   
11 | ADC_Y2  | 12 | LRADC0   
13 | ADC_Y1  | 14 | _GND_  
15 | ADC_X2  | 16 | UART0_RX   
17 | ADC_X1  | 18 | UART0_TX   
  

# Tips, Tricks, Caveats
## FEL mode
The button marked _SW2_ , located between the VGA and USB host connectors, triggers [ FEL mode][60312] when pressed during boot. (_SW2_ pulls the A20 _BOOTSEL_ pin to low level.) 
If no SD card is present, the A20 will automatically fall back to FEL mode (as this device has no other means of booting, like e.g. onboard NAND flash). So if you want to enforce FEL mode, you may simply remove the SD card and connect to the Orange Pi via the DC input(the one next to the audio output). This also supplies power to the board at the same time. 
To [ verify][60313] you have successfully entered FEL mode, check the output of `fel version`. For the Orange Pi, it should look like: 
[code] 
    AWUSBFEX soc=00001651(A20) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
[/code]
## LEDs
For those with a transparent case (or no case at all) the Orange Pi's LED activity is good. The **red** power LED (_D2_) can be turned off. 
## SATA
If you wish to connect a SATA drive (2.5" mobile harddisk or SSD) to the Orange Pi: Make sure your power supply is connected to the "DC-IN" port, and can deliver sufficient current (e.g. 5V/2000mA). Using the OTG port or an inadequate power supply might result in your SATA device not being detected. 
# Adding a serial port
TODO: The section is mostly a copy&paste from the "Banana Pi" page. Some of it may be incorrect, or might not apply to this device. Please review / rework the information, and remove this reminder when done.
While the GPIO pinout of the Orange Pi is designed to be compatible to the Raspberry Pi, it's important to notice subtle differences in the serial ports. The Orange Pi has some additional pins that already provide two more serial ports. 
The default serial port **/dev/ttyS0** , used for (bootstrap) debugging and the serial console, is located at J11 - refer to the picture and instructions below. The Raspberry's "original" serial port on GPIO 14 and 15 (CON3, pins 8 and 10) can usually be accessed as **/dev/ttyS2** on the Orange Pi. J12 also provides another serial port on pins 4 (_RXD_) and 6 (_TXD_), which should map to **/dev/ttyS3**. 
_Note:_ The actual mapping between physical pins, UART numbers and/or device names may depend on the specific kernel and [ configuration][60314] used. If in doubt, check the boot messages: `dmesg | grep -i uart`
[![][60315]][60316]
[][60317]
UART pads
## Locating the UART
The UART pins are located in the upper right corner of the board. They are marked as _TX_ , _RX_ and _GND_ on the PCB. Just attach some leads according to our [UART Howto][60318]. **Do not connect the red wire (VCC or 3.3V/5V), as that might damage your board.**
# Pictures
  * [![Orangepi front.png][60319]][60320]
  * [![Orangepi back.jpg][60321]][60322]
  * [![Orangepi side d.jpg][60323]][60324]
  * [![Orangepi side u.jpg][60325]][60326]
  * [![Orangepi side l.jpg][60327]][60328]
  * [![Orangepi side r.jpg][60329]][60330]

# Variants
## A20 based
  * The [Xunlong Orange Pi Mini][60331] was released in November 2014, too. It has two TF card slots and only has 2 USB Host.

## Other SoCs
  * The [Orange Pi Plus][60332] was presented in February 2015. It's a new board, and it uses the AllWinner [H3][60333] SoC. It Has a 8GB EMMC Flash, Onboard Network(10/100/1000M Ethernet RJ45), Onboard WIFI(Realtek RTL8189ETV, IEEE 802.11 b/g/n), Video Outputs(Supports HDMI CEC, Supports HDMI 3D function, Integrated CVBS, Supports simultaneous output of HDMI and CVBS) and a 40 pin GPIO header (that mimics the Raspberry Pi A+/B+ models).
  * The [Orange Pi 2][60334] and [Orange Pi Mini 2][60335] are released in March 2015. They are both based on a quad-core [H3][60333] CPU, and offer TF card slot, onboard Network(10/100M Ethernet RJ45), 40 pin GPIO and 4 USB type A connectors. They are difference in _onboard wifi_. Orange Pi 2 has wifi module, while Orange Pi Mini 2 does not have. However, the two kinds of devices do not have _SATA_ any more.

# Also known as
# See also
There are several websites about Orange Pi and claiming to support it. It has to be clarified, what is "official" and who is behind this sites. 
  * [Xunlong Orange Pi site][60336]
  * ["Official" Github Repository][60337].
  * ["Official" Orange Pi Form][60338].
  * [Manual for building an SD-card image][60339]

## Manufacturer images
A various amount of [prebuilt images][60340] is provided via OrangePi's Website.
