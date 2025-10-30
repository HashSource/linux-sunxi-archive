# Inet D70 A33
Inet D70 A33  
---  
[![INET-D70-REV06 0004.jpg][26921]][26922]  
Manufacturer |  [iNet Tek][26923]  
Dimensions |  190mm x 115mm x 9.7mm   
Specifications   
SoC |  [A33][26924]  
DRAM |  512MiB DDR3   
NAND |  8GB   
Power |  DC 5V @ 3A, 2300mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" 16:9)   
Touchscreen |  Multi-finger capacitive ([Silead GSL1686][26925])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][26926])   
Storage |  µSD   
USB |  USB2.0 OTG   
Camera |  0.3MP (640x480) front, 0.3MP (640x480) rear   
Headers |  UART   
## Contents
  * [1 Identification][26927]
    * [1.1 D70B-REV01][26928]
  * [2 Manual build][26929]
    * [2.1 U-Boot][26930]
      * [2.1.1 Mainline U-Boot][26931]
    * [2.2 Linux Kernel][26932]
      * [2.2.1 Mainline kernel][26933]
  * [3 Tips, Tricks, Caveats][26934]
    * [3.1 FEL mode][26935]
    * [3.2 Device specific topic][26936]
  * [4 Adding a serial port (**voids warranty**)][26937]
    * [4.1 Device disassembly][26938]
    * [4.2 Locating the UART][26939]
  * [5 Pictures][26940]
  * [6 Also known as][26941]
  * [7 See also][26942]

# Identification
Case: 
[code] 
    STYLUS
    iDROID
     
    ETAB B7041 * 8GB * USB 5V - 2.0A [Ring: -, Tip: +]
    Made in China
[/code]
PCB: 
[code] 
    INET-D70-REV06
    Zeng-gc 2014-12-12
[/code]
Android -> Settings -> About Tablet: 
[code] 
    Model Number: ETAB B7041
    Build Number: RS24082015C
[/code]
### D70B-REV01
There is another similar version which has the following details but the board could not be booted. It has 2 Kingston D2516EC4BXGGB DRAMs instead of single and FORESEE 8GB NCEMASD9-08G eMMC instead of SKhynix H27UCG8T2ETR-BC NAND Flash. 
PCB: 
On front and back 
[code] 
    INET-D70B-REV01
    Zeng-gc 2014-08-22
    
[/code]
Back 
[code] 
    iU70B-BTC-V01 单8G 1/2
    PCBA:310U70BAC1BB06
    510120160524007 屏:亿星BOE
    RF 20160526
    
[/code]
# Manual build
You can build things for yourself by following our [ Manual build howto][26943] and by choosing from the configurations available below. 
  

### U-Boot
#### Mainline U-Boot
The _q8_a33_tablet_1024x600_defconfig_ build target seems to produce a working U-Boot image. 
  

### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
  

# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
  

## FEL mode
To enter [ FEL mode][26944]: 
  1. Switch off the device.
  2. Hold down the **Vol-** and **Power** buttons.
  3. Release the **Power** button once u-boot reports: _key pressed value=0xb_.
  4. Press the **Power** three times, u-boot should report: _you can unclench the key to update now_.
  5. Release the **Vol-** button.

  
It is possible to [query the device version][26945] at this stage, but [reading results in failure][26946]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
  

# Adding a serial port (**voids warranty**)
[![][26947]][26948]
[][26949]
UART pads
  

## Device disassembly
  1. Remove the two screws surrounding the button panel interface.
  2. Insert a suitable [plastic tool][26950] into the seam of the casing next to one of the screw holes.
  3. Gently slide the tool towards and around the nearest corner.
  4. If the first clip has not been released at this point, twist the tool slowly to pry the casing halves apart.
  5. Place the tool on the opposite end of the released clip and proceed by sliding the tool towards the next clip.
  6. Continue carefully around the perimeter of the casing until all clips have been released.

  

## Locating the UART
UART TX and RX can be found between the µSD connector, NAND Flash IC, and Touchscreen FPC connector. See the [UART howto][26951] for further information. 
# Pictures
  * [![INET-D70-REV06 0004.jpg][26952]][26922]
  * [![INET-D70-REV06 0003.png][26953]][26954]
  * [![INET-D70-REV06 0001.png][26955]][26956]
  * [![][26957]][26958]
D70B-REV01: Front 
  * [![][26959]][26960]
D70B-REV01: Back 

# Also known as
  * Robuste ES711. (Algeria).-- Stock ROM: <http://www.robuste.dz/es711/>
  * Bitmore Colortab7. (Greece).-- Working ROM: <http://www.robuste.dz/es711/>
  * Digma Optima 7.11 TT7041AW (Russia). --The above ROM is working fine.

# See also
[Inet D70 A23][26961]
