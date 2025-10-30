# Xassette Asterisk
Xassette Asterisk  
---  
[![Xassette Asterisk RevB.jpg][59969]][59970]  
Manufacturer |  [SdtElectronics][59971]  
Dimensions |  56 _mm_ x 56 _mm_  
Release Date |  November 2021   
Website |  [Xassette-Asterisk][59972]  
Specifications   
SoC |  [D1s][59973] @ 1.0Ghz   
DRAM |  64MiB @ ? MHz   
Power |  DC 5V @ 2A (via OTG or dedicated USB Type-C connector)   
Features   
Video |  RGB, CVBS   
Audio |  3.5mm headphone plug, 3.5mm line in, I2S   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8189FTV][59974]))   
Storage |  µSD, SPI NAND   
USB |  1 USB2.0 Host, 1 USB Type-C OTG   
Other |  Power LED, FEL & RESET buttons   
Headers |  34-pin extension header, 24-pin DVP, 40-pin FPC LCD RGB, 6-pin resistive touchscreen/GPADC   
Xassette-Asterisk is an open-source reference design for [D1s][59973] developed by SdtElectronics. It was released in November 2021 and exposed all peripherals of D1s via a range of connectors, in which USB, headphones, line-in, RGB LCD, DVP camera, SD and SPI flash have on-board standard interface. The [hardware design][59972] is open-source under the [CERN OHL-w v2][59975] licence. 
This page needs to be properly filled according to the [New Device Howto][59976] and the [New Device Page guide][59977].
## Contents
  * [1 Identification][59978]
  * [2 Sunxi support][59979]
    * [2.1 Current status][59980]
    * [2.2 Images][59981]
  * [3 Tips, Tricks, Caveats][59982]
    * [3.1 FEL mode][59983]
  * [4 Pictures][59984]
  * [5 External links][59985]

# Identification
The mark "Xassette-Asterisk" can be found at the back of the PCB. 
# Sunxi support
## Current status
As [D1s][59973] has little difference between [D1][59986], the tina BSP for [D1][59986] can be adopted to [D1s][59973] without much modification. 
## Images
An image ready to be burned into the card is at [the release page in the Github repository][59987]
# Tips, Tricks, Caveats
## FEL mode
The `FEL` button triggers [ FEL mode][59988]. The [xfel][59989] tool has support for the [D1s][59973] chip. 
# Pictures
  * [![Xassette Asterisk RevB.jpg][59990]][59970]
  * [![Xassette Asterisk RevA Resources.jpg][59991]][59992]

# External links
  * [GitHub repository][59972]
  * [Hackaday Page][59993]
