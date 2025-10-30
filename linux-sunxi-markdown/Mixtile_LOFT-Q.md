# Mixtile LOFT-Q
Mixtile LOFT-Q  
---  
[![IMG 0395.JPG][38203]][38204]  
Manufacturer |  [Focalcrest][38205]  
Dimensions |  120 _mm_ x 120 _mm_  
Website |  ~~[Device Product Page][38206]~~  
Specifications   
SoC |  [A31][38207] @ 1Ghz   
DRAM |  2GiB DDR3 @ 312MHz   
eMMC |  8GB   
Power |  DC 12V @ 4A   
Features   
Video |  HDMI (Type A - full)   
Audio |  toslink plug, HDMI, on-board microphone   
Network |  WiFi 802.11 b/g/n + BT (AP6234), 10/100/1000Mbps Ethernet, Zigbee NXP JN5168   
Storage |  SD SATA   
USB |  4 USB2.0 Host   
Headers |  UART, JTAG, LCD, SPI, TWI, RTP, CSI, MIPI CSI, MIPI DSI, IR   
## Contents
  * [1 Identification][38208]
  * [2 Sunxi support][38209]
    * [2.1 Current status][38210]
      * [2.1.1 Sunxi Kernel][38211]
      * [2.1.2 Sunxi U-Boot][38212]
      * [2.1.3 Mainline kernel][38213]
      * [2.1.4 Mainline U-Boot][38214]
    * [2.2 Images][38215]
    * [2.3 HW-Pack][38216]
    * [2.4 BSP][38217]
    * [2.5 Manual build][38218]
  * [3 Tips, Tricks, Caveats][38219]
    * [3.1 FEL mode][38220]
      * [3.1.1 Datasheet][38221]
    * [3.2 Expansion Ports][38222]
  * [4 Adding a serial port][38223]
  * [5 Pictures][38224]
  * [6 Also known as][38225]
  * [7 See also][38226]

# Identification
The board reads "Mixtile LOFT-Q" 
The board comes with Android 4.4.2 (3.3.0 kernel) preloaded in the EMMC. 
  * Model Number: Softwinner

# Sunxi support
## Current status
The Mixtile LOFT-Q is only partially supported, benefited from Humming bird. 
### Sunxi Kernel
Like all [A31][38207] based devices, there is no support in our sunxi kernel. 
### Sunxi U-Boot
Linux-sunxi's U-Boot currently lacks SPL support. This means that you have to chain load it from Allwinner's bootloader How?. 
### Mainline kernel
Mainline kernel support is included in 3.17. Currently only UARTs, USB, I2C, and GMAC are supported. 
Use the sun6i-a31-hummingbird.dtb device-tree file for the [mainline kernel][38227]. 
### Mainline U-Boot
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [hummingbird_a31.fex][38228]

Everything else is the same as the [manual build howto][38229]. 
# Tips, Tricks, Caveats
## FEL mode
The U-Boot button triggers [ FEL mode][38230]. See [ BROM][38231] for more information on the boot sequence. 
### Datasheet
Will soon be released. 
## Expansion Ports
The Mixtile LOFT-Q exposes 3 x 60 pins 0.5 mm pitch connectors with lots of expansion possibilities. 
J4 "CSI/MIPI-DSI"   
---  
2x30 Header   
1 | CSI-D0  | 2 | CSI-D1   
3 | CSI-D2  | 4 | CSI-D3   
5 | CSI-D4  | 6 | CSI-D5   
7 | CSI-D6  | 8 | CSI-D7   
9 | CSI-D8  | 10 | CSI-D9   
11 | CSI-D10  | 12 | CSI-D11   
13 | _GND_ | 14 | CSI-HSYNC   
15 | CSI-VSYNC  | 16 | TWI0-SCK   
17 | TWI0-SDA  | 18 | _GND_  
19 | CSI-MCLK  | 20 | CSI-PCLK   
21 | _GND_ | 22 | VDD1V8-CSI   
23 | VDD1V8-CSI  | 24 | _GND_  
25 | _VCC-5V_ | 26 | _VCC-5V_  
27 | _GND_ | 28 | _VCC-3V3_  
29 | _VCC-3V3_ | 30 | _GND_  
31 | MCSI-MCLK  | 32 | _NC_  
33 | _NC_ | 34 | _GND_  
35 | DSI-D0N  | 36 | DSI-D0P   
37 | _GND_ | 38 | DSI-D1N   
39 | DSI-D1P  | 40 | _GND_  
41 | DSI-D2N  | 42 | DSI-D2P   
43 | _GND_ | 44 | DSI-D3N   
45 | DSI-D3P  | 46 | _GND_  
47 | DSI-CKN  | 48 | DSI-CKP   
49 | "GND"  | 50 | SPDIF-IN   
51 | SPDIF-OUT  | 52 | _GND_  
53 | I2S1-DIN  | 54 | I2S1-BCLK   
55 | I2S1-LRCK  | 56 | I2S1-MCLK   
57 | EARGND2  | 58 | LRADC0   
59 | EARGND2  | 60 | LRADC0   
J5 ""   
---  
2x30 Header   
1 | _VCC-5V_ | 2 | _VCC-5V_  
3 | _GND_ | 4 | _VCC-LCD_  
5 | _VCC-LCD_ | 6 | _GND_  
7 | UART4-TX  | 8 | UART4-RX   
9 | _GND_ | 10 | _VCC-JTAG_  
11 | _VCC-JTAG_ | 12 | AP-RESET#   
13 | TMS0  | 14 | TCK0   
15 | TDO0  | 16 | TDI0   
17 | JTAG-SEL0  | 18 | _GND_  
19 | SPI0-MOSI  | 20 | 'SPI0-MISO   
21 | SPI0-CLK  | 22 | SPI0-CS0   
23 | _GND_ | 24 | CSI2-D0N   
25 | CSI2-D0P  | 26 | _GND_  
27 | CSI2-D1N  | 28 | CSI2-D1P   
29 | _GND_ | 30 | CSI2-D2N   
31 | CSI2-D2P  | 32 | _GND_  
33 | CSI2-D3N  | 34 | CSI2-D3P   
35 | _GND_ | 36 | DSI-D0P   
37 | CSI2-CKP  | 38 | _GND_  
39 | TWI3-SCK  | 40 | TWI3-SDA   
41 | _GND_ | 42 | MCS-MCLK1   
43 | _GND_ | 44 | CAM-R-STBY-EN   
45 | CAM-R-RESET#  | 46 | _GND_  
47 | GPIO-PH0  | 48 | GPIO-PH1   
49 | GPIO-PH2  | 50 | GPIO-PH3   
51 | GPIO-PH4  | 52 | GPIO-PH5   
53 | GPIO-PH6  | 54 | GPIO-PH7   
55 | GPIO-PH8  | 56 | GPIO-PH29   
57 | GPIO-PH30  | 58 | _GND_  
59 | USB-DP0  | 60 | USB-DM0   
J6 "LCD/LVDS"   
---  
2x30 Header   
1 | LVDS0-D0P (LCD0-D0)  | 2 | LVDS0-D0N (LCD0-D1)   
3 | _GND_ | 4 | LVDS0-D1P (LCD0-D2)   
5 | LVDS0-D1N (LCD0-D3)  | 6 | _GND_  
7 | LVDS0-D2P (LCD0-D4)  | 8 | LVDS0-D2N (LCD0-D5)   
9 | _GND_ | 10 | LVDS0-CLKP (LCD0-D6)   
11 | LVDS0-CLKN (LCD0-D7)  | 12 | _GND_  
13 | LVDS0-D3P (LCD0-D8)  | 14 | LVDS0-D3N (LCD0-D9)   
15 | _GND_ | 16 | LVDS1-D0P (LCD0-D10)   
17 | LVDS1-D0N (LCD0-D11)  | 18 | _GND_  
19 | LVDS1-D1P (LCD0-D12)  | 20 | LVDS1-D1N (LCD0-D13)   
21 | _GND_ | 22 | LVDS1-D2P (LCD0-D14)   
23 | LVDS1-D2N (LCD0-D15)  | 24 | _GND_  
25 | LVDS1-CLKP (LCD0-D16)  | 26 | LVDS1-CLKN (LCD0-D17)   
27 | _GND_ | 28 | LVDS1-D3P (LCD0-D18)   
29 | LVDS1-D3N (LCD0-D19)  | 30 | _GND_  
31 | LCD0-D20  | 32 | LCD0-D21   
33 | LCD0-D22  | 34 | LCD0-D23   
35 | LCD0-CLK  | 36 | LCD0-HSYNC   
37 | LCD0-DE  | 38 | LCD0-VSYNC   
39 | LCD0-PWM  | 40 | LCD0-BL-EN   
41 | _GND_ | 42 | CTP-WAKE   
43 | CTP-INT  | 44 | TWI1-SCK   
45 | TWI1-SDA  | 46 | _GND_  
47 | RTP-X1  | 48 | RTP-X2   
49 | RTP-Y1  | 50 | RTP-Y2   
51 | _GND_ | 52 | _VCC2V8-LCD_  
53 | _VCC2V8-LCD_ | 54 | _VCC2V8-LCD_  
55 | _GND_ | 56 | _VCC1V8-LCD_  
57 | _VCC2V8-LCD_ | 58 | _GND_  
59 | _VCC-5V_ | 60 | _VCC-5V_  
J21 "LED/IR/POWER-ON"   
---  
2x4 Header   
1 | _VCC-NRF_ | 2 | _GND_  
3 | IR-RX  | 4 | PWR-ON   
5 | LED1-R  | 6 | LED2-G   
7 | LED3-B  | 8 | _GND_  
J7 "AUDIO IN/OUT"   
---  
2x3 Header   
1 | SPKL  | 2 | SPKR   
3 | AGND  | 4 | AGND   
5 | LINEINL  | 6 | LINEINR   
# Adding a serial port
[![][38232]][38233]
[][38234]
UART pins
The UART header is next to USB host. Just attach some leads according to our [UART howto][38235]. 
# Pictures
  * [![LOFT-Q-FG.jpg][38236]][38237]
  * [![LOFT-Q-BG.jpg][38238]][38239]
  * [![LOFT-Q-FrontPanel.jpg][38240]][38241]
  * [![LOFT-Q-DiskConnector.jpg][38242]][38243]

# Also known as
# See also
