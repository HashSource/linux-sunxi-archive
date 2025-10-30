# INET-3FTD
INET-3FTD  
---  
[![INET-3FTD Tablet Front.jpeg][24757]][24758]  
Manufacturer |  [Inet-tek][24759]  
Dimensions |  245 _mm_ x 190 _mm_ x 10 _mm_  
Release Date |  August 2012   
Specifications   
SoC |  [A10][24760] @ 1.2Ghz   
DRAM |  1GiB DDR3 @ 408MHz   
NAND |  4GB (with a theoretical upgrade possibility, [see tricks][24761])   
Power |  DC 5V @ 2.4A, 4800mAh 3.7V Li-Po battery, [AXP209][24762] power management unit   
Features   
LCD |  1024x768 (9.7" 4:3)   
Touchscreen |  5-finger capacitive (Generic ASB097-50-06)   
Video |  Mini-HDMI   
Audio |  3.5mm headphone plug, mini-HDMI, onboard microphone, speaker   
Network |  WiFi 802.11 b/g/n [Realtek RTL8188EUS][24763], USB2.0 Ethernet via built-in fast Ethernet controller   
Storage |  µSD   
USB |  2x µUSB2.0 (1x µUSB2.0 Host, 1x µUSB2.0 OTG)   
Camera |  1.3MP (1280x1024) frontal camera   
Other |  [Bosch BMA250][24764] 3-axis accelerometer   
Headers |  UART   
Allwinner A10-based tablet board. This one belongs to the INET's 3Fxx board family. 
## Contents
  * [1 Identification][24765]
    * [1.1 PCB Label][24766]
    * [1.2 Android information][24767]
      * [1.2.1 Settings information][24768]
      * [1.2.2 build.prop information][24769]
      * [1.2.3 System memory layout][24770]
  * [2 Tips, tricks, caveats][24771]
    * [2.1 FEL mode activation][24772]
      * [2.1.1 Side buttons][24773]
      * [2.1.2 UBOOT button][24774]
    * [2.2 NAND storage upgrade (voids warranty)][24761]
    * [2.3 Power supply][24775]
    * [2.4 Reset button][24776]
    * [2.5 Unused motor connector][24777]
  * [3 UART access (voids warranty)][24778]
    * [3.1 Device disassembly][24779]
    * [3.2 Locating the UART][24780]
  * [4 Also known as][24781]
  * [5 Images][24782]
  * [6 See also][24783]

## Identification
### PCB Label
[code] 
    INET-3FTD-REV01
    Zeng-gc 2012-08-28
    
[/code]
### Android information
#### Settings information
While running stock Android under **Settings** > **About tablet** the following entries can be seen for Polaroid MIDC907: 
[code] 
    Model number: MIDC497
    Android version: 4.0.4
    Baseband version: 1.5_121116
    Kernel version: 3.0.8+ inet_dada@inetsuperserver #98 Fri Nov 16 17:07:47 CST 2012
    Build number: Polaroid
    
[/code]
#### build.prop information
[code] 
    ro.build.description=crane_inet-eng 4.0.4 IMM76D 20121116 test-keys
    ro.build.fingerprint=iNet/crane_inet/crane-inet:4.0.4/IMM76D/20121116:eng/test-keys
    
[/code]
#### System memory layout
This is a printout from /proc/iomem for the default rom with stock kernel. 
[code] 
    01c03000-01c04000 : sw_nand
    01c09000-01c09fff : sun4i_csi.0
      01c09000-01c09fff : sun4i_csi.0
    01c0a000-01c0afff : disp
    01c0c000-01c0cfff : disp
    01c0d000-01c0dfff : disp
    01c0f000-01c0ffff : sunxi-mmc.0
      01c0f000-01c0ffff : sunxi-mmc
    01c16000-01c165ff : hdmi
    01c1b000-01c1bfff : disp
    01c22c00-01c22c40 : sun4i-codec
      01c22c00-01c22c3f : sun4i-codec
    01c28000-01c283ff : sunxi-uart.0
      01c28000-01c2801f : serial
    01c2ac00-01c2afff : sun4i-i2c.0
      01c2ac00-01c2afff : sun4i-i2c.0
    01c2b000-01c2b3ff : sun4i-i2c.1
      01c2b000-01c2b3ff : sun4i-i2c.1
    01c2b400-01c2b7ff : sun4i-i2c.2
      01c2b400-01c2b7ff : sun4i-i2c.2
    01c40000-01c40097 : Mali-400 GP
    01c41000-01c4102f : Mali-400 L2 cache
    01c42000-01c42027 : Mali-400 PMU
    01c43000-01c43023 : Mali-400 MMU for GP
    01c44000-01c44023 : Mali-400 MMU for PP
    01c48000-01c490ef : Mali-400 PP
    01e00000-01e0077f : disp
    01e20000-01e2077f : disp
    01e40000-01e457ff : disp
    01e60000-01e657ff : disp
    01e80000-01e8ffff : g2d
      01e80000-01e8ffff : g2d
    40000000-5bffffff : System RAM
      4002f000-40772763 : Kernel text
      40774000-4097e237 : Kernel data
    5c000000-5fffffff : Mali Sdram
    60000000-7fffffff : System RAM
    
[/code]
## Tips, tricks, caveats
### FEL mode activation
#### Side buttons
With the board powered off, hold Volume+ (HOME button on the key-panel), then hold the power button for about 2 seconds, release it and press at least 3 times immediately. 
#### UBOOT button
There is an unpopulated UBOOT switch/button connector. You can either short the pads and power the board on, or solder a switch/button and turn/press it before powering the board on. 
### NAND storage upgrade (voids warranty)
Some INET-3FTD boards have an unused NAND chip slot which you can use to upgrade the board's storage capacity. There are two known supported NAND chips: 
  * Micron 29F32G08CBACA
  * Hynix H27UCG8T2ATR

These are SMD components, so standard SMD soldering advices apply. 
### Power supply
This board supports independent 5V charging with a barrel-shaped plug connector. 
### Reset button
This board can be rebooted with a single press of the on-board RESET button. 
### Unused motor connector
There is an unused motor connector that can be enabled by editing the [FEX configuration][24784] file. 
## UART access (voids warranty)
### Device disassembly
Unscrew the two screws located on the bottom port panel. Use your [plastic tool][24785] to pry-open the device's cover - it is advised to start with one of the corners to minimize the risk of damaging the LCD screen while opening the device. 
### Locating the UART
UART connector pads are visible on the board front pictures. They are clearly silk-screened on the PCB, but hidden under the touch digitizer flex cable. Unplug the flex cable to gain access to the pads. Cables can be soldered according to our [UART howto][24786]. 
## Also known as
  * Polaroid MIDC907
  * MyPhone MyTab 10
  * DragonTouch E97
  * DX Q91

# Images
  * [![INET-3FTD Board Front.jpeg][24787]][24788]
  * [![INET-3FTD board front \(fully-populated NAND slots\).jpg][24789]][24790]

# See also
  * [Inet 3fbt][24791] is a 3Fxx family board with bluetooth module.
  * [Inet 3f][24792] is the bare-bones of 3Fxx family board.
