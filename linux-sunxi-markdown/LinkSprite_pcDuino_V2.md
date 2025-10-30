# LinkSprite pcDuino2
(Redirected from [LinkSprite pcDuino V2][31771])
 
LinkSprite pcDuino2  
---  
[![Pcd v2 front.jpg][31774]][31775]  
Manufacturer |  [Linksprite][31776]  
Dimensions |  125 _mm_ x 52 _mm_ x height _mm_  
Release Date |  September 2013   
Website |  [Product Page][31777]  
Specifications   
SoC |  [A10][31778] @ 1GHz   
DRAM |  1GiB DDR3 @ 360MHz ([H5TQ2G83CFR-H9C][31779], [NT5CB256M8BN-CG][31780])   
NAND |  2/4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full)   
Audio |  HDMI   
Network |  WiFi 802.11bgn (Realtek RTL8188CUS), 10/100Mbps Ethernet (IC+ IP101A)   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART, Arduino Compatible Headers   
The pcDuino2 is an [A10][31778] based development board with [Arduino][31781] compatible headers. Unlike many other A10 based boards, this one does not have a SATA connector. 
## Contents
  * [1 Identification][31782]
  * [2 Sunxi support][31783]
    * [2.1 Current status][31784]
    * [2.2 Images][31785]
    * [2.3 HW-Pack][31786]
    * [2.4 BSP][31787]
    * [2.5 Manual build][31788]
    * [2.6 Mainline U-Boot][31789]
    * [2.7 Mainline kernel][31790]
  * [3 Tips, Tricks, Caveats][31791]
    * [3.1 FEL mode][31792]
    * [3.2 LEDs][31793]
    * [3.3 DRAM][31794]
      * [3.3.1 a10-tpr3-scan results from pcDuino2 with HYNIX DDR3 @408MHz][31795]
      * [3.3.2 a10-tpr3-scan results from pcDuino2 with NANYA DDR3 @432MHz][31796]
    * [3.4 Expansion headers][31797]
    * [3.5 Arduino shields compatibility][31798]
  * [4 Adding a serial port][31799]
  * [5 Pictures][31800]
  * [6 Also known as][31801]
  * [7 See also][31802]

# Identification
On the back of the board, it helpfully says "pcDuino V2". 
# Sunxi support
## Current status
Fully supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the pcDuino target.
  * The .fex file can be found in sunxi-boards as [linksprite_pcduino2.fex][31803]

Everything else is the same as the [manual build howto][31804]. 
## Mainline U-Boot
For [ building mainline u-boot][31805], use the _Linksprite_pcDuino_ board name. 
## Mainline kernel
Use the _sun4i-a10-pcduino.dts_ device-tree file for the [mainline kernel][31806]. 
# Tips, Tricks, Caveats
## FEL mode
The UPGRADE (SW2, near the HDMI connector) button triggers [FEL mode][31807]. 
## LEDs
The board has 5 green LEDs. One of them is an always-on power indicator. Two LEDs labelled TX and RX are accessible via GPIO (using the PH15 and PH16 pins). One LED labelled CLK is connected to the PI11 pin, which can also have a dedicated use as SPI0_CLK. So this CLK LED serves either as an SPI activity indicator or just as an ordinary LED if no SPI hardware is connected. And there is also one more WIFI LED on the board, which is connected to the WIFI chip. 
## DRAM
This board uses four x8 DDR3 chips (two on the front side of the PCB and two on the back side). So far SKhynix and NANYA chips have been encountered. [SKhynix has reliability problems][31808] at clock speeds higher than 360MHz. Preliminary tests show that NANYA appears to be reasonably good and at least [works without problems][31809] at the default 408MHz settings from the vendor. 
Below are the [a10-tpr3-scan][31810] results with the default U-Boot settings, just after setting the DRAM clock frequency a little bit too high. The a10-tpr3-scan tool suggests to change the tpr3 value to 0x181111 for HYNIX and to 0x041111 for NANYA. Basically, the delay settings need to be changed in different directions for improving reliability. The HYNIX settings are bad for NANYA and the other way around. The default tpr3 value 0x000000 happens to be on the edge of the reliable/unreliable boundary in both cases. 
### a10-tpr3-scan results from pcDuino2 with HYNIX DDR3 @408MHz
[![][31811]][31812]
[][31813]
SKhynix [H5TQ2G83CFR-H9C][31779]
| dcdc3_vol = 1250  
dram_clk = 408  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 6  
dram_zq = 0x7b (0x6b96900)  
dram_odt_en = 0  
dram_tpr0 = 0x30926692  
dram_tpr1 = 0x1090  
dram_tpr2 = 0x1a0c8  
dram_tpr3 = 0x0  
dram_emr1 = 0x0  
dram_emr2 = 0x0  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06050505  
active_windowing = 0  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x0733**3** 3| 0x0722**2** 2| 0x0711**1** 1| 0x0700**0** 0| 0x07EE**E** E| 0x07DDDD  
**0x06**|  0x0633**3** 3| 0x0622**2** 2| 0x0611**1** 1| 0x0600**0** 0| 0x06EE**E** E| 0x06DD**D** D  
**0x05**|  0x0533**3** 3| 0x0522**2** 2| 0x0511**1** 1| 0x0500**0** 0| 0x05EE**E** E| 0x05DD**D** D  
**0x04**|  0x0433**3** 3| 0x0422**2** 2| 0x0411**1** 1| 0x0400**0** 0| 0x04EE**E** E| 0x04DD**D** D  
**0x03**|  0x0333**3** 3| 0x0322**2** 2| 0x0311**1** 1| 0x0300**0** 0| 0x03EE**E** E| 0x03DD**D** D  
**0x02**|  0x0233**3** 3| 0x0222**2** 2| 0x0211**1** 1| 0x0200**0** 0| 0x02EE**E** E| 0x02DD**D** D  
**0x01**|  0x013333| 0x012222| 0x0111**1** 1| 0x0100**0** 0| 0x01EE**E** E| 0x01DD**D** D  
**0x00**|  0x003333| 0x002222| 0x001111| 0x000000| 0x00EE**E** E| 0x00DD**D** D  
**0x08**|  0x083333| 0x082222| 0x0811**1** 1| 0x080000| 0x08EEEE| 0x08DD**D** D  
**0x10**|  0x103333| 0x102222| 0x101111| 0x100000| 0x10EEEE| 0x10DDDD  
**0x18**|  0x183333| 0x182222| 0x181111| 0x180000| 0x18EEEE| 0x18DDDD  
**0x20**|  0x203333| 0x202222| 0x201111| 0x200000| 0x20EEEE| 0x20DDDD  
**0x28**|  0x283333| 0x282222| 0x281111| 0x280000| 0x28EEEE| 0x28DDDD  
**0x30**|  0x303**3** 33| 0x302**2** 22| 0x301**1** 11| 0x300**0** 00| 0x30E**E** EE| 0x30DD**D** D  
**0x38**|  0x383**3** 33| 0x382**2** 22| 0x381**1** 11| 0x380**0** 00| 0x38E**E** EE| 0x38D**D** D**D**  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=35, bitflip=20]  
  
Total number of successful memtester runs: 383  
  
Best luminance at the height 0.5 is above 0x181111, score = 0.857  
Best luminance at the height 1.0 is above 0x181111, score = 0.792  
Best luminance at the height 2.0 is above 0x181111, score = 0.703  
Best luminance at the height 4.0 is above 0x181111, score = 0.589  
  
Read errors per lane: [0, 0, 11, 0]. Lane 1 is the most noisy/problematic.  
  
Write errors per lane: [0, 11, 33, 1]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 1.  
Errors from the lane 2 are not intersecting with the errors from the worst lane 1.  
  
### a10-tpr3-scan results from pcDuino2 with NANYA DDR3 @432MHz
[![][31814]][31815]
[][31816]
NANYA [NT5CB256M8BN-CG][31780]
| dcdc3_vol = 1250  
dram_clk = 432  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 6  
dram_zq = 0x7b (0x6b91800)  
dram_odt_en = 0  
dram_tpr0 = 0x30926692  
dram_tpr1 = 0x1090  
dram_tpr2 = 0x1a0c8  
dram_tpr3 = 0x0  
dram_emr1 = 0x0  
dram_emr2 = 0x0  
dram_emr3 = 0x0  
dqs_gating_delay = 0x05050505  
active_windowing = 0  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07EEEE| 0x07D**D** DD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06EEEE| 0x06D**D** DD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05EEEE| 0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04EEEE| 0x04DDDD  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03D**D** DD  
**0x02**|  0x023333| 0x022222| 0x021111| 0x020000| 0x02EEEE| 0x02D**D** DD  
**0x01**|  0x013333| 0x012222| 0x011**1** 11| 0x010000| 0x01E**E** EE| 0x01D**D** DD  
**0x00**|  0x003333| 0x002**2** 22| 0x001**1** 1**1**|  0x000**0** 00| 0x00EEEE| 0x00D**D** DD  
**0x08**|  0x083**3** 33| 0x08222**2**|  0x081**1** 11| 0x080**0** 0**0**|  0x08E**E** E**E**|  0x08DDDD  
**0x10**|  0x103**3****3****3**|  0x102**2****2****2**|  0x101**1** 1**1**|  0x10000**0**|  0x10EEE**E**|  0x10DDDD  
**0x18**|  0x1833**3****3**|  0x182222| 0x181**1****1****1**|  0x180**0** 00| 0x18EE**E****E**|  0x18DDDD  
**0x20**|  0x203**3****3****3**|  0x202**2** 22| 0x20111**1**|  0x200**0** 00| 0x20E**E** EE| 0x20DDDD  
**0x28**|  0x283**3** 33| 0x282**2** 22| 0x281**1** 11| 0x280**0** 00| 0x28E**E** EE| 0x28DDDD  
**0x30**|  0x30**3****3** 33| 0x302**2** 22| 0x301**1** 11| 0x300**0** 00| 0x30E**E** EE| 0x30DDDD  
**0x38**|  0x383**3** 33| 0x38222**2**|  0x381**1** 11| 0x380**0** 0**0**|  0x38E**E** EE| 0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=36, solidbits=9]  
  
Total number of successful memtester runs: 456  
  
Best luminance at the height 0.5 is above 0x041111, score = 0.894  
Best luminance at the height 1.0 is above 0x041111, score = 0.844  
Best luminance at the height 2.0 is above 0x041111, score = 0.770  
Best luminance at the height 4.0 is above 0x031111, score = 0.668  
  
Read errors per lane: [0, 6, 0, 0]. Lane 2 is the most noisy/problematic.  
  
Write errors per lane: [1, 32, 6, 16]. Lane 2 is the most noisy/problematic.  
Errors from the lane 0 are 56.2% eclipsed by the worst lane 2.  
Errors from the lane 1 are 66.7% eclipsed by the worst lane 2.  
Errors from the lane 3 are 100.0% eclipsed by the worst lane 2.  
  
## Expansion headers
J11 (Closer to the corner with the ethernet connector) |  | J12 (Closer to the corner with the HDMI connector)  
---|---|---  
Pin number | pcDuino name | Sunxi name | Pin number | pcDuino name | Sunxi name   
1 | UART2_RX | [PI19][31817] | 6 | ADC_5 |   
2 | UART2_TX | [PI18][31818] | 5 | ADC_4 |   
3 | GPIO2 | [PH7][31819] | 4 | ADC_3 |   
4 | PWM0 | [PH6][31820] | 3 | ADC_2 |   
5 | GPIO3 | [PH8][31821] | 2 | ADC_1 |   
6 | PWM1 | [PB2][31822] | 1 | ADC_0 |   
7 | PWM2 | [PI3][31823] |   
8 | GPIO4 | [PH9][31824]  
J8 (Closer to the corner with the WIFI chip) | J9 (Closer to the corner with the USB connector)  
Pin number | pcDuino name | Sunxi name | Pin number | pcDuino name | Sunxi name   
1 | GPIO5 |  | 8 | DC_5V |   
2 | PWM3 |  | 7 | GND |   
3 | SPI0_CS |  | 6 | GND |   
4 | SPI0_MOSI |  | 5 | DC_5V |   
5 | SPI0_MISO |  | 4 | 3V3_SYS |   
6 | SPI0_CLK |  | 3 | RESET |   
7 | GND |  | 2 | 3V3_SYS |   
8 |  |  | 1 |  |   
9 | TWI2-SDA |   
10 | TWI2-SCK |   
## Arduino shields compatibility
[![][31825]][31826]
[][31827]
ITeadstudio 2.4 TFT LCD Touch shield can be only successfully used with jumper wires
The advertised compatibility with Arduino shields is not always perfect. 
# Adding a serial port
[![][31828]][31829]
[][31830]
UART pads
There is 2.54mm pitch header next to the Wifi Module, labelled "UART". All you need to do is connect some jumper wires according to our [UART howto][31831]. 
# Pictures
  * [![Pcd v2 front.jpg][31832]][31775]
  * [![Pcd v2 back.jpg][31833]][31834]

# Also known as
This type of device has no rebadges. 
# See also
  * [LinkSprite pcDuino][31835]
  * [LinkSprite pcDuino3][31836]
  * [User Guide.][31837]
  * [Schematics (2013-09-17)][31838]
