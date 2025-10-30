# Cubietech Cubieboard
(Redirected from [Cubieboard][14599])
 
Cubietech Cubieboard  
---  
[![Cubieboard.jpeg][14602]][14603]  
Manufacturer |  [CubieTech][14604], [Cubieboard][14605]  
Dimensions |  10 _cm_ x 6 _cm_  
Release Date |  October 2012   
Website |  [Cubieboard Product page][14606]  
Specifications   
SoC |  [A10][14607] @ 1Ghz   
DRAM |  512MiB/1GiB DDR3 @ 480MHz ([GT8UB256M16BP-BG][14608], [GT8UB256M16BP-BH][14609])   
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
Cubieboard is a small (10x6cm), hacker friendly, extendable and very low-cost while powerful ARM board with Allwinner [A10][14607] SoC. 
## Contents
  * [1 Identification][14610]
  * [2 Sunxi support][14611]
    * [2.1 Current status][14612]
    * [2.2 Images][14613]
    * [2.3 HW-Pack][14614]
    * [2.4 BSP][14615]
    * [2.5 Manual build][14616]
      * [2.5.1 U-Boot][14617]
        * [2.5.1.1 Sunxi/Legacy U-Boot][14618]
        * [2.5.1.2 Upstream/Mainline U-Boot][14619]
      * [2.5.2 Linux Kernel][14620]
        * [2.5.2.1 Sunxi/Legacy Kernel][14621]
        * [2.5.2.2 Upstream/Mainline kernel][14622]
    * [2.6 Mainline kernel][14623]
  * [3 Tips, Tricks, Caveats][14624]
    * [3.1 FEL mode][14625]
    * [3.2 Hardware Hacking][14626]
    * [3.3 Software Hacking][14627]
  * [4 Adding a serial port][14628]
  * [5 Pictures][14629]
  * [6 Hardware documentation][14630]
  * [7 Also known as][14631]
  * [8 See also][14632]
    * [8.1 Cubieboard Community][14633]
    * [8.2 Other links][14634]

# Identification
The board helpfully reads "Cubietech" "Cubieboard.org" and has an A10 chip on it. :) 
# Sunxi support
## Current status
The cubieboard is well represented within the main sunxi developer community and has excellent support both in u-boot as well as 3.4 and mainline kernels. 
## Images
  * [Android firmwares.][14635]
  * [Fedora images.][14636]
  * [Ubuntu images.][14637]
  * Image creation for ArchLinuxARM (or ALARM) : [Cubieboard][14638].

Cubietech also has a bunch of official firmwares available on their [download][14639] page. 
## HW-Pack
Generating a HW pack for the cubieboard is easily done with the sunxi-bsp and well supported. 
## BSP
Under the BSP the cubieboard is simply known as cubieboard. Just run: 
[code] 
    ./configure cubieboard
    make
    
[/code]
## Manual build
You can build things for yourself by following our [ Manual build howto][14640] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _Cubieboard_ build target. 
#### Upstream/Mainline U-Boot
Use the _Cubieboard_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_cubieboard.fex_][14641] file. 
#### Upstream/Mainline kernel
Use the _sun4i-a10-cubieboard.dtb_ device-tree binary. 
## Mainline kernel
Use the sun4i-a10-cubieboard.dts device-tree file for the [mainline kernel][14642]. 
# Tips, Tricks, Caveats
## FEL mode
The FEL button triggers [ FEL mode][14643]. 
## Hardware Hacking
  * The two [expansion headers][14644] U14 and U15 invite you to create your own [extension board][14645]
  * [Adding a second SD Card slot][14646]
  * [Adding a reset button][14647]
  * [Adding a JTAG header][14648]
  * [Bypassing USB2 current limiter][14649]

## Software Hacking
  * [Building Android TV image][14650]
  * [Building jellybean for cubieboard][14651]
  * [Installing on NAND][14652]
  * [Build your own embedded linux with buildroot][14653]
  * [Run linux 3.9 on Cubieboard][14654]
  * [USB Webcam Surveillance on Cubieboard][14655]

# Adding a serial port
[![][14656]][14657]
[][14658]
DEVICE UART pads
There is a nice 2.54mm pin header near to the SoC. All you have to do is connect the correct wires, according to our [UART howto][14659] or the [ Cubieboard TTL howto][14660]. [![Exclamation-red.png][14661]][14662] **Do not connect Vcc as that might damage your board.**
# Pictures
  * [![Cubieboard1.jpg][14663]][14664]
  * [![Cubieboard-connected-booted.jpg][14665]][14666]
  * [![Cubieboard-standard.jpg][14667]][14668]
  * [![Cubieboard package list - rich.jpg][14669]][14670]
  * [![Cubieboard a10 bottom.jpg][14671]][14672]
  * [![Cubieboard a10 top.jpg][14673]][14674]

# Hardware documentation
  * <https://github.com/lipro-armbian/pddocs/tree/master/Cubietech/CubieBoard1>

# Also known as
The cubieboard was a major success, and it has become a name of its own. Therefore, no rebadging has taken place, but there might be some bad chinese rip-offs out there, which carry the same name. 
# See also
  * [Cubietech Cubieboard2][14675]
  * [Cubietech Cubietruck][14676]
  * [Wikipedia page on Cubieboard][14677]

## Cubieboard Community
Next to the sunxi community, the cubieboard has its own cummunity. 
  * [[email protected]][14678]
  * [Forums on cubieforums.com][14679]
  * `[#cubieboard][14680]` [IRC][14681] channel on [Freenode][14682]. Click to [join via WebChat)][14683].

## Other links
  * [Arch Linux on Cubieboard][14638]
  * [Berryboot multiboot bootloader][14684]
  * [Kali Linux on Cubieboard][14685]
