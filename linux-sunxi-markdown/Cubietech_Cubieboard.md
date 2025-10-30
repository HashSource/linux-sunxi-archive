# Cubietech Cubieboard
Cubietech Cubieboard  
---  
[![Cubieboard.jpeg][14904]][14905]  
Manufacturer |  [CubieTech][14906], [Cubieboard][14907]  
Dimensions |  10 _cm_ x 6 _cm_  
Release Date |  October 2012   
Website |  [Cubieboard Product page][14908]  
Specifications   
SoC |  [A10][14909] @ 1Ghz   
DRAM |  512MiB/1GiB DDR3 @ 480MHz ([GT8UB256M16BP-BG][14910], [GT8UB256M16BP-BH][14911])   
NAND |  4GB (Samsung K9GBG08U0A-SCB0)   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive)   
Features   
Video |  HDMI, LVDS, CVBS   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI   
Network |  10/100 Ethernet (Realtek RTL8201CP)   
Storage |  µSD, SATA (+5v power)   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  IRDA (Vishay HS0038B)   
Headers |  2 48pin expansion ports which export (amongst others): I2C (TWI), SPI, RGB/LVDS, CSI/TS, FM-IN, ADC, CVBS, VGA, SPDIF-OUT, touch-panel   
Cubieboard is a small (10x6cm), hacker friendly, extendable and very low-cost while powerful ARM board with Allwinner [A10][14909] SoC. 
## Contents
  * [1 Identification][14912]
  * [2 Sunxi support][14913]
    * [2.1 Current status][14914]
    * [2.2 Images][14915]
    * [2.3 HW-Pack][14916]
    * [2.4 BSP][14917]
    * [2.5 Manual build][14918]
      * [2.5.1 U-Boot][14919]
        * [2.5.1.1 Sunxi/Legacy U-Boot][14920]
        * [2.5.1.2 Upstream/Mainline U-Boot][14921]
      * [2.5.2 Linux Kernel][14922]
        * [2.5.2.1 Sunxi/Legacy Kernel][14923]
        * [2.5.2.2 Upstream/Mainline kernel][14924]
    * [2.6 Mainline kernel][14925]
  * [3 Tips, Tricks, Caveats][14926]
    * [3.1 FEL mode][14927]
    * [3.2 Hardware Hacking][14928]
    * [3.3 Software Hacking][14929]
  * [4 Adding a serial port][14930]
  * [5 Pictures][14931]
  * [6 Hardware documentation][14932]
  * [7 Also known as][14933]
  * [8 See also][14934]
    * [8.1 Cubieboard Community][14935]
    * [8.2 Other links][14936]

# Identification
The board helpfully reads "Cubietech" "Cubieboard.org" and has an A10 chip on it. :) 
# Sunxi support
## Current status
The cubieboard is well represented within the main sunxi developer community and has excellent support both in u-boot as well as 3.4 and mainline kernels. 
## Images
  * [Android firmwares.][14937]
  * [Fedora images.][14938]
  * [Ubuntu images.][14939]
  * Image creation for ArchLinuxARM (or ALARM) : [Cubieboard][14940].

Cubietech also has a bunch of official firmwares available on their [download][14941] page. 
## HW-Pack
Generating a HW pack for the cubieboard is easily done with the sunxi-bsp and well supported. 
## BSP
Under the BSP the cubieboard is simply known as cubieboard. Just run: 
[code] 
    ./configure cubieboard
    make
    
[/code]
## Manual build
You can build things for yourself by following our [ Manual build howto][14942] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _Cubieboard_ build target. 
#### Upstream/Mainline U-Boot
Use the _Cubieboard_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_cubieboard.fex_][14943] file. 
#### Upstream/Mainline kernel
Use the _sun4i-a10-cubieboard.dtb_ device-tree binary. 
## Mainline kernel
Use the sun4i-a10-cubieboard.dts device-tree file for the [mainline kernel][14944]. 
# Tips, Tricks, Caveats
## FEL mode
The FEL button triggers [ FEL mode][14945]. 
## Hardware Hacking
  * The two [expansion headers][14946] U14 and U15 invite you to create your own [extension board][14947]
  * [Adding a second SD Card slot][14948]
  * [Adding a reset button][14949]
  * [Adding a JTAG header][14950]
  * [Bypassing USB2 current limiter][14951]

## Software Hacking
  * [Building Android TV image][14952]
  * [Building jellybean for cubieboard][14953]
  * [Installing on NAND][14954]
  * [Build your own embedded linux with buildroot][14955]
  * [Run linux 3.9 on Cubieboard][14956]
  * [USB Webcam Surveillance on Cubieboard][14957]

# Adding a serial port
[![][14958]][14959]
[][14960]
DEVICE UART pads
There is a nice 2.54mm pin header near to the SoC. All you have to do is connect the correct wires, according to our [UART howto][14961] or the [ Cubieboard TTL howto][14962]. [![Exclamation-red.png][14963]][14964] **Do not connect Vcc as that might damage your board.**
# Pictures
  * [![Cubieboard1.jpg][14965]][14966]
  * [![Cubieboard-connected-booted.jpg][14967]][14968]
  * [![Cubieboard-standard.jpg][14969]][14970]
  * [![Cubieboard package list - rich.jpg][14971]][14972]
  * [![Cubieboard a10 bottom.jpg][14973]][14974]
  * [![Cubieboard a10 top.jpg][14975]][14976]

# Hardware documentation
  * <https://github.com/lipro-armbian/pddocs/tree/master/Cubietech/CubieBoard1>

# Also known as
The cubieboard was a major success, and it has become a name of its own. Therefore, no rebadging has taken place, but there might be some bad chinese rip-offs out there, which carry the same name. 
# See also
  * [Cubietech Cubieboard2][14977]
  * [Cubietech Cubietruck][14978]
  * [Wikipedia page on Cubieboard][14979]

## Cubieboard Community
Next to the sunxi community, the cubieboard has its own cummunity. 
  * [[email protected]][14980]
  * [Forums on cubieforums.com][14981]
  * `[#cubieboard][14982]` [IRC][14983] channel on [Freenode][14984]. Click to [join via WebChat)][14985].

## Other links
  * [Arch Linux on Cubieboard][14940]
  * [Berryboot multiboot bootloader][14986]
  * [Kali Linux on Cubieboard][14987]
