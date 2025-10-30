# Mele A1000
(Redirected from [Mele A100][35853])
 
Mele A1000  
---  
[![Mele a1000 angle.jpeg][35856]][35857]  
Manufacturer |  [Mele][35858]  
Dimensions |  175 _mm_ x 110 _mm_ x 47 _mm_  
Release Date |  April 2012   
Website |  [Mele A1000 product page][35859]  
Specifications   
SoC |  [A10][35860] @ 1Ghz   
DRAM |  512MB/1G DDR3 @360MHz ([H5TQ2G63BFR-H9C][35861], [H5TQ2G83CFR-H9C][35862])   
NAND |  4/8 GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - Full), VGA, Composite   
Audio |  R/L Cinch, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188CUS), 10/100Mbps Ethernet (Realtek RTL8201CP)   
Storage |  SD, SATA (optional)   
USB |  3 USB2.0 Host   
Other |  IRDA (optional)   
Headers |  UART, USB OTG, USB Host   
The original A10 based Mele Set-Top-Boxes are the start of the sunxi project. These imminently hackable machines were exported by Tom Cubie of [Cubieboard][35863] fame and these devices kickstarted community development for the Allwinner A10 SoC. 
There are 8 variants of the Mele A1000. The Mele A1000 has a wedge-like shape whereas the slightly younger A2000 is more square. The A100 uses the mele A2000 square shape, but it lacks a SATA port. The Mele A1000G is a 1GiB RAM version of the Mele A1000, just like the Mele A2000G is a 1GiB version of the Mele A2000. Both come with 8GB NAND. The Mele A100G is a 1GB RAM version of the Mele A100, but keeps the 4GB NAND. Then there is the Mele A3700, which is also a 1GiB version, but it uses a completely different case design with an external wifi antenna, 8GB NAND, and has no SATA port. Last but not least, There are Dual-Core version which is use A20 for it SoC, named A100-DualCore. 
All motherboards are essentially the same, apart from tiny revisions. The 1GB versions of course have a differing layout due to the doubling of the RAM chips. The Mele A100(G) has no SATA connector soldered on, and the LED, IR & power button have moved to the center of the front of the device. The A3700 lacks SATA as well, and seems to make LED, IR and power button available through a connector. 
## Contents
  * [1 Identification][35864]
  * [2 Sunxi support][35865]
    * [2.1 Current status][35866]
    * [2.2 Images][35867]
    * [2.3 HW-Pack][35868]
    * [2.4 BSP][35869]
    * [2.5 Manual build][35870]
      * [2.5.1 Mele A1000/A2000/A100][35871]
      * [2.5.2 Mele A1000G/A2000G/A100G][35872]
      * [2.5.3 Mele A3700][35873]
    * [2.6 Mainline kernel][35874]
  * [3 Tips, Tricks, Caveats][35875]
    * [3.1 FEL mode][35876]
    * [3.2 VGA Connector][35877]
    * [3.3 Composite][35878]
    * [3.4 GPIO Access][35879]
    * [3.5 DRAM Overclock][35880]
  * [4 Adding a serial port][35881]
    * [4.1 Device disassembly][35882]
    * [4.2 Locating the UART][35883]
  * [5 Pictures][35884]
  * [6 Also known as][35885]
  * [7 See also][35886]
    * [7.1 Related devices][35887]

# Identification
In android, under Settings->About Device, you will find: 
  * Model Number: Mele-HTPC
  * Build Number: Mele-HTPC Tue Mar 27 14:40:57 CST 2012 Version 1.5

# Sunxi support
## Current status
Fully supported. 
## Images
## HW-Pack
## BSP
## Manual build
### Mele A1000/A2000/A100
  * For building u-boot, use the "Mele_A1000" target.
  * The .fex file can be found in sunxi-boards as [mele_a1000.fex][35888]

Everything else is the same as the [ Manual build howto][35889]. 
### Mele A1000G/A2000G/A100G
  * For building u-boot, use the "Mele_A1000G" target.
  * The .fex file can be found in sunxi-boards as [mele_a1000g.fex][35890]

Everything else is the same as the [ Manual build howto][35889]. 
### Mele A3700
It seems that the below targets are completely superfluous, and that the Mele A3700 should just use the A1000G target, but with SATA disabled.
  * For building u-boot, use the "Mele_A3700" target.
  * The .fex file can be found in sunxi-boards as [mele_a3700.fex][35891]

Everything else is the same as the [ Manual build howto][35889]. 
[![][35892]][35893]
[][35894]
Mele A1000 FEL "jumper"
## Mainline kernel
Use the sun4i-a10-a1000.dts device-tree file for the [mainline kernel][35895]. 
# Tips, Tricks, Caveats
## FEL mode
You can short 11K1 jumper to enter FEL mode. 
## VGA Connector
Even though the Mele comes with a blue VGA connector, and blue signifies that this is a DDC enabled VGA connector... And even though there are wires for DDC SCL/SDA all the way to the 8-pin connector on the motherboard... These wires are simply floating. The Mele A1000 and derivates simply are unable to talk to a VGA connected monitor and query it for what modes it supports. The mode will have to be hardcoded. 
## Composite
The Mele Ax000 uses DAC3 for the composite connection. So make sure to set the following in your tv_out_dac_para if you want to use composite: 
[code] 
    dac3_src = 0
    
[/code]
[![][35896]][35897]
[][35898]
GPIOs identified on A2000
## GPIO Access
The Mele A2000 (and probably A1000) have a number of pins accessible for GPIO use. Here are some that have been identified. See image for color coded locations. 
  * GPIO_PH10 (main red led)
  * GPIO_PH20 (main blue led)
  * GPIO_PH22 (unused?)
  * GPIO_PH23 (unused?)

## DRAM Overclock
The original DRAM clock in Mele A1000/A2000 is rather conservative (360 Mhz). It is possible to overclock to a higher DRAM speeds modifying the PLL5 factor N register value. Use devmem command or its busybox equivalent in Android. 
Possible PPL5 DDR clock values can be 
  * 360 Mhz(original) : b1058F91
  * 384 Mhz(safe) : b1059091
  * 408 Mhz(mostly safe) : b1059191
  * 432 Mhz(risky) : b1059291

For example, to get a 408 Mhz DRAM clock in Android execute this command (Busybox required) 
[code] 
    /system/bin/busybox devmem 0x01c20020 32 0xb1059191
    
[/code]
# Adding a serial port
[![][35899]][35900]
[][35901]
Mele A100 UART connector
## Device disassembly
Trivially unscrew 4 or 6 screws, depending on excat model. 
[![][35902]][35903]
[][35904]
Screws to loose on a Mele A2000
## Locating the UART
The Mele has a 4 pin 2.0 pitch JST-PH connector available for its UART0 port. This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. More information is available at [our UART howto][35905]. 
# Pictures
  * Mele A1000

  * [![Mele a1000 front.jpeg][35906]][35907]
  * [![Mele a1000 back.jpeg][35908]][35909]
  * [![Mele a1000 left.jpeg][35910]][35911]
  * [![Mele-a1000-pcb-front-fel.jpg][35912]][35913]

  * Mele A2000

  * [![Mele A2000 front.jpg][35914]][35915]
  * [![Mele A2000 top.jpg][35916]][35917]
  * [![Mele A2000 left side.jpg][35918]][35919]
  * [![Mele A2000 right side.jpg][35920]][35921]
  * [![Mele A2000 back.jpg][35922]][35923]
  * [![Mele A2000 board.jpg][35924]][35925]
  * [![Mele-a2000-pcb-front.jpg][35926]][35927]
  * [![Mele2kback hf.jpg][35928]][35929]

  * Mele A100

  * [![Device front.jpg][35930]][35931]
  * [![Device back.jpg][35932]][35933]
  * [![Device buttons 1.jpg][35934]][35935]
  * [![Device buttons 2.jpg][35936]][35937]
  * [![Device board front.jpg][35938]][35939]
  * [![Device board back.jpg][35940]][35941]

  

  * Mele A1000G

  * [![Device front.jpg][35930]][35931]
  * [![Device back.jpg][35932]][35933]
  * [![Device buttons 1.jpg][35934]][35935]
  * [![Device buttons 2.jpg][35936]][35937]
  * [![Device board front.jpg][35938]][35939]
  * [![Device board back.jpg][35940]][35941]

  * Mele A2000G

  * [![Device front.jpg][35930]][35931]
  * [![Device back.jpg][35932]][35933]
  * [![Device buttons 1.jpg][35934]][35935]
  * [![Device buttons 2.jpg][35936]][35937]
  * [![Device board front.jpg][35938]][35939]
  * [![Device board back.jpg][35940]][35941]

  * Mele A100G

  * [![Device front.jpg][35930]][35931]
  * [![Device back.jpg][35932]][35933]
  * [![Device buttons 1.jpg][35934]][35935]
  * [![Device buttons 2.jpg][35936]][35937]
  * [![Device board front.jpg][35938]][35939]
  * [![Device board back.jpg][35940]][35941]

  * Mele A3700

  * [![Device front.jpg][35930]][35931]
  * [![Device back.jpg][35932]][35933]
  * [![Device buttons 1.jpg][35934]][35935]
  * [![Device buttons 2.jpg][35936]][35937]
  * [![Mele A3700 PCB TOPa.jpg][35942]][35943]
  * [![Mele A3700 PCB BOTTOMa.jpg][35944]][35945]

# Also known as
The Mele A1000 motherboard in a different housing is known as the Mele A2000. The Mele A2000 which lacks SATA is sold as Mele A100. 
# See also
  * [Original Rhombus tech wiki page on hacking the Mele A1000.][35946]

## Related devices
  * [Mele A1000G Quad][35947] ([ A31 based.][35948])
