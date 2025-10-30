# Xunlong Orange Pi Mini
(Redirected from [Orange Pi Mini][42338])
 
Xunlong Orange Pi Mini  
---  
[![Xunlong Orangepi mini.png][42341]][42342]  
Manufacturer |  [OrangePi][42343]  
Dimensions |  94 _mm_ x 59 _mm_  
Release Date |  November 2014   
Website |  [Orange Pi Mini Product Page][42344]  
Specifications   
SoC |  [A20][42345] @ 1Ghz   
DRAM |  1GiB DDR3 @ 960MHz   
NAND |  no nand available   
Power |  DC 5V @ 2A (best via DC input)   
Features   
Video |  HDMI (Type A - full), CVBS, RGB/LVDS   
Audio |  3.5 mm jack, PHOUT   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][42346]), wifi 802.11 b/g/n   
Storage |  SD, SATA (with power connector: JST XH 2.5mm header, providing +5V)   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  [CIR][42347]  
Headers |  1 pin UART, 3 pin UART, LCD/ LVDS, CSI, 40 pin GPIO   
Orange Pi Mini is [A20][42345]-based development board produced by [Xunlong][42348]. Feature-wise, the Orange Pi Mini is rather similar to the original [Orange Pi][42349], but it lacks the VGA output and onboard optional flash, and it has only 2 USB ports. Instead of two 26 + 18 pin expansion ports, the board has a single 40 pin expansion port. 
## Contents
  * [1 Identification][42350]
  * [2 Sunxi support][42351]
    * [2.1 Current status][42352]
    * [2.2 Images][42353]
    * [2.3 HW-Pack][42354]
    * [2.4 BSP][42355]
    * [2.5 Manual build][42356]
    * [2.6 Mainline kernel][42357]
  * [3 Expansion Port][42358]
  * [4 Tips, Tricks, Caveats][42359]
    * [4.1 FEL mode][42360]
    * [4.2 LEDs][42361]
    * [4.3 SATA][42362]
  * [5 Adding a serial port][42363]
    * [5.1 Locating the UART][42364]
  * [6 Pictures][42365]
  * [7 Variants][42366]
  * [8 Also known as][42367]
  * [9 See also][42368]
    * [9.1 Manufacturer images][42369]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi Mini
[/code]
# Sunxi support
## Current status
Supported.  

**Note:** Orange Pi Mini's GMAC is not supported in the community kernel. A commit within [Orange Pi Github fork of linux-sunxi-3.4][42370] seems to provide GMAC support for Orange Pi Mini. This has to be proved and merged into linux-sunxi. 
Xunlong seems to use an important tweak of both the Linux 3.4 kernel and U-Boot networking code for the Orange Pi Mini: The GMAC driver is specifically modified to set the GMAC_TX_DELAY parameter to 3. This adjusts the relative timing of the clock and data signals to the PHY in order to compensate for differing trace lengths on the PCB ([details][42371]; the [pcDuino3 Nano][42372] has the same problem). Without this modification, the Ethernet port will work at 100Mbit, but not (or not reliably) at 1000Mbit. Upstream U-Boot now sets this parameter itself, so the kernel patch isn't needed any more ([patch][42373]). 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _Orangepi_mini_ target (`make orangepimini_config`).
  * The .fex file can be found in sunxi-boards as [orangepimini.fex][42374]

Everything else is the same as the [manual build howto][42375]. 
## Mainline kernel
Use the _sun7i-a20-orangepi-mini.dtb_ device-tree file for the [mainline kernel][42376]
# Expansion Port
The Orange Pi Mini has a 40-pin, 0.1" connector with several low-speed interfaces. 
2x20 Header   
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
27 | PB5 I2S_MCLK  | 28 | PI12   
29 | PB6 I2S_BCLK  | 30 | _GND_  
31 | PB7 I2S_LRCK  | 32 | PI20 UART7_TX   
33 | PB8 I2S_DO0  | 34 | _GND_  
35 | PB12 I2S_DI  | 36 | PI21 UART7_RX   
37 | PB13 SDPIF_D0  | 38 | PH3   
39 | _GND_ | 40 | PH5   
# Tips, Tricks, Caveats
## FEL mode
The button marked _SW3_ , located beside the wifi module, triggers [ FEL mode][42377] when pressed during boot. (_SW3_ pulls the A20 _BOOTSEL_ pin to low level.) 
If no SD card is present, the A20 will automatically fall back to FEL mode (as this device has no other means of booting, like e.g. onboard NAND flash). So if you want to enforce FEL mode, you may simply remove the SD card and connect to the Orange Pi Mini via the DC input(the one next to the TF card slot upside). This also supplies power to the board at the same time. 
To [ verify][42378] you have successfully entered FEL mode, check the output of `fel version`. For the Orange Pi Mini, it should look like: 
[code] 
    AWUSBFEX soc=00001651(A20) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
[/code]
## LEDs
For those with a transparent case (or no case at all) the Orange Pi Mini's LED activity is good. The **red** power LED (_D2_) can be turned off. 
## SATA
If you wish to connect a SATA drive (2.5" mobile harddisk or SSD) to the Orange Pi Mini: Make sure your power supply is connected to the "DC-IN" port, and can deliver sufficient current (e.g. 5V/2000mA). Using the OTG port or an inadequate power supply might result in your SATA device not being detected. 
# Adding a serial port
TODO: The section is mostly a copy&paste from the "Banana Pi" page. Some of it may be incorrect, or might not apply to this device. Please review / rework the information, and remove this reminder when done.
While the GPIO pinout of the Orange Pi Mini is designed to be compatible to the Raspberry Pi, it's important to notice subtle differences in the serial ports. The Orange Pi Mini has some additional pins that already provide two more serial ports. 
The default serial port **/dev/ttyS0** , used for (bootstrap) debugging and the serial console, is located at J11 - refer to the picture and instructions below. The Raspberry's "original" serial port on GPIO 14 and 15 (CON3, pins 8 and 10) can usually be accessed as **/dev/ttyS2** on the Orange Pi Mini. J12 also provides another serial port on pins 4 (_RXD_) and 6 (_TXD_), which should map to **/dev/ttyS3**. 
_Note:_ The actual mapping between physical pins, UART numbers and/or device names may depend on the specific kernel and [ configuration][42379] used. If in doubt, check the boot messages: `dmesg | grep -i uart`
[![][42380]][42381]
[][42382]
UART pads
## Locating the UART
The UART pins are located in the upper right corner of the board. They are marked as _TXD_ , _RXD_ and _GND_ on the PCB. Just attach some leads according to our [UART Howto][42383]. 
# Pictures
  * [![Orangepi mini front.jpg][42384]][42385]
  * [![Orangepi mini back.jpg][42386]][42387]
  * [![Xunlong Orange Pi Mini side d.jpg][42388]][42389]
  * [![Xunlong Orange Pi Mini side d.jpg][42388]][42389]
  * [![Xunlong Orange Pi Mini side l.jpg][42390]][42391]
  * [![Xunlong Orange Pi Mini side r.jpg][42392]][42393]

# Variants
  * The original [Orange Pi][42349] was released in November 2014. The orange pi features a standard TF card slot and a 26 pin GPIO connector (similar to the Raspberry Pi A/B).

# Also known as
# See also
There are several websites about Orange Pi Mini and claiming to support it. It has to be clarified, what is "official" and who is behind this sites. 
  * [Xunlong Orange Pi site][42394]
  * ["Official" Github Repository][42395].
  * ["Official" Orange Pi Form][42396].
  * [Manual for building an SD-card image][42397]

## Manufacturer images
A various amount of [prebuilt images][42398] is provided via OrangePi's Website.
