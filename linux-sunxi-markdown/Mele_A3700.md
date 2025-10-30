# Mele A1000
(Redirected from [Mele A3700][36847])
 
Mele A1000  
---  
[![Mele a1000 angle.jpeg][36850]][36851]  
Manufacturer |  [Mele][36852]  
Dimensions |  175 _mm_ x 110 _mm_ x 47 _mm_  
Release Date |  April 2012   
Website |  [Mele A1000 product page][36853]  
Specifications   
SoC |  [A10][36854] @ 1Ghz   
DRAM |  512MB/1G DDR3 @360MHz ([H5TQ2G63BFR-H9C][36855], [H5TQ2G83CFR-H9C][36856])   
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
The original A10 based Mele Set-Top-Boxes are the start of the sunxi project. These imminently hackable machines were exported by Tom Cubie of [Cubieboard][36857] fame and these devices kickstarted community development for the Allwinner A10 SoC. 
There are 8 variants of the Mele A1000. The Mele A1000 has a wedge-like shape whereas the slightly younger A2000 is more square. The A100 uses the mele A2000 square shape, but it lacks a SATA port. The Mele A1000G is a 1GiB RAM version of the Mele A1000, just like the Mele A2000G is a 1GiB version of the Mele A2000. Both come with 8GB NAND. The Mele A100G is a 1GB RAM version of the Mele A100, but keeps the 4GB NAND. Then there is the Mele A3700, which is also a 1GiB version, but it uses a completely different case design with an external wifi antenna, 8GB NAND, and has no SATA port. Last but not least, There are Dual-Core version which is use A20 for it SoC, named A100-DualCore. 
All motherboards are essentially the same, apart from tiny revisions. The 1GB versions of course have a differing layout due to the doubling of the RAM chips. The Mele A100(G) has no SATA connector soldered on, and the LED, IR & power button have moved to the center of the front of the device. The A3700 lacks SATA as well, and seems to make LED, IR and power button available through a connector. 
## Contents
  * [1 Identification][36858]
  * [2 Sunxi support][36859]
    * [2.1 Current status][36860]
    * [2.2 Images][36861]
    * [2.3 HW-Pack][36862]
    * [2.4 BSP][36863]
    * [2.5 Manual build][36864]
      * [2.5.1 Mele A1000/A2000/A100][36865]
      * [2.5.2 Mele A1000G/A2000G/A100G][36866]
      * [2.5.3 Mele A3700][36867]
    * [2.6 Mainline kernel][36868]
  * [3 Tips, Tricks, Caveats][36869]
    * [3.1 FEL mode][36870]
    * [3.2 VGA Connector][36871]
    * [3.3 Composite][36872]
    * [3.4 GPIO Access][36873]
    * [3.5 DRAM Overclock][36874]
  * [4 Adding a serial port][36875]
    * [4.1 Device disassembly][36876]
    * [4.2 Locating the UART][36877]
  * [5 Pictures][36878]
  * [6 Also known as][36879]
  * [7 See also][36880]
    * [7.1 Related devices][36881]

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
  * The .fex file can be found in sunxi-boards as [mele_a1000.fex][36882]

Everything else is the same as the [ Manual build howto][36883]. 
### Mele A1000G/A2000G/A100G
  * For building u-boot, use the "Mele_A1000G" target.
  * The .fex file can be found in sunxi-boards as [mele_a1000g.fex][36884]

Everything else is the same as the [ Manual build howto][36883]. 
### Mele A3700
It seems that the below targets are completely superfluous, and that the Mele A3700 should just use the A1000G target, but with SATA disabled.
  * For building u-boot, use the "Mele_A3700" target.
  * The .fex file can be found in sunxi-boards as [mele_a3700.fex][36885]

Everything else is the same as the [ Manual build howto][36883]. 
[![][36886]][36887]
[][36888]
Mele A1000 FEL "jumper"
## Mainline kernel
Use the sun4i-a10-a1000.dts device-tree file for the [mainline kernel][36889]. 
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
[![][36890]][36891]
[][36892]
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
[![][36893]][36894]
[][36895]
Mele A100 UART connector
## Device disassembly
Trivially unscrew 4 or 6 screws, depending on excat model. 
[![][36896]][36897]
[][36898]
Screws to loose on a Mele A2000
## Locating the UART
The Mele has a 4 pin 2.0 pitch JST-PH connector available for its UART0 port. This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. More information is available at [our UART howto][36899]. 
# Pictures
  * Mele A1000

  * [![Mele a1000 front.jpeg][36900]][36901]
  * [![Mele a1000 back.jpeg][36902]][36903]
  * [![Mele a1000 left.jpeg][36904]][36905]
  * [![Mele-a1000-pcb-front-fel.jpg][36906]][36907]

  * Mele A2000

  * [![Mele A2000 front.jpg][36908]][36909]
  * [![Mele A2000 top.jpg][36910]][36911]
  * [![Mele A2000 left side.jpg][36912]][36913]
  * [![Mele A2000 right side.jpg][36914]][36915]
  * [![Mele A2000 back.jpg][36916]][36917]
  * [![Mele A2000 board.jpg][36918]][36919]
  * [![Mele-a2000-pcb-front.jpg][36920]][36921]
  * [![Mele2kback hf.jpg][36922]][36923]

  * Mele A100

  * [![Device front.jpg][36924]][36925]
  * [![Device back.jpg][36926]][36927]
  * [![Device buttons 1.jpg][36928]][36929]
  * [![Device buttons 2.jpg][36930]][36931]
  * [![Device board front.jpg][36932]][36933]
  * [![Device board back.jpg][36934]][36935]

  

  * Mele A1000G

  * [![Device front.jpg][36924]][36925]
  * [![Device back.jpg][36926]][36927]
  * [![Device buttons 1.jpg][36928]][36929]
  * [![Device buttons 2.jpg][36930]][36931]
  * [![Device board front.jpg][36932]][36933]
  * [![Device board back.jpg][36934]][36935]

  * Mele A2000G

  * [![Device front.jpg][36924]][36925]
  * [![Device back.jpg][36926]][36927]
  * [![Device buttons 1.jpg][36928]][36929]
  * [![Device buttons 2.jpg][36930]][36931]
  * [![Device board front.jpg][36932]][36933]
  * [![Device board back.jpg][36934]][36935]

  * Mele A100G

  * [![Device front.jpg][36924]][36925]
  * [![Device back.jpg][36926]][36927]
  * [![Device buttons 1.jpg][36928]][36929]
  * [![Device buttons 2.jpg][36930]][36931]
  * [![Device board front.jpg][36932]][36933]
  * [![Device board back.jpg][36934]][36935]

  * Mele A3700

  * [![Device front.jpg][36924]][36925]
  * [![Device back.jpg][36926]][36927]
  * [![Device buttons 1.jpg][36928]][36929]
  * [![Device buttons 2.jpg][36930]][36931]
  * [![Mele A3700 PCB TOPa.jpg][36936]][36937]
  * [![Mele A3700 PCB BOTTOMa.jpg][36938]][36939]

# Also known as
The Mele A1000 motherboard in a different housing is known as the Mele A2000. The Mele A2000 which lacks SATA is sold as Mele A100. 
# See also
  * [Original Rhombus tech wiki page on hacking the Mele A1000.][36940]

## Related devices
  * [Mele A1000G Quad][36941] ([ A31 based.][36942])
