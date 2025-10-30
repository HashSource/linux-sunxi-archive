# In-Circuit ICnova A20
In-Circuit ICnova A20  
---  
[![In-circuit icnova a20 som in baseboard.jpeg][25724]][25725]  
Manufacturer |  [In-Circuit GmbH][25726]  
Dimensions |  29 _mm_ x 68 _mm_ (SO-DIMM)   
Release Date |  October 2014   
Website |  [Device Product/Wiki Page][25727]  
Specifications   
SoC |  [A20][25728] @ 1Ghz   
DRAM |  512MiB DDR3 @ 384MHz   
NAND |  4GiB originally, but this is no longer available in 2024.   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI   
Network |  10/100Mbps Ethernet ([Realtek RTL8201CP][25729])   
Storage |  µSD, SATA   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART, JTAG, LVDS, GPIO, ...   
The In-Circuit ICnova A20, also labelled "SoMPi", is a SO-DIMM sized System-On-Module which usually comes with the ADB4006 daughterboard sold by the same company. 
## Contents
  * [1 In-Circuit and open source software][25730]
  * [2 Identification][25731]
  * [3 Sunxi support][25732]
    * [3.1 Current status][25733]
    * [3.2 Manual build][25734]
      * [3.2.1 U-Boot][25735]
        * [3.2.1.1 Sunxi/Legacy U-Boot][25736]
        * [3.2.1.2 Mainline U-Boot][25737]
      * [3.2.2 Linux Kernel][25738]
        * [3.2.2.1 Sunxi/Legacy Kernel][25739]
        * [3.2.2.2 Mainline kernel][25740]
      * [3.2.3 Buildroot][25741]
  * [4 Tips, Tricks, Caveats][25742]
    * [4.1 FEL mode][25743]
  * [5 Adding a serial port][25744]
  * [6 Pictures][25745]
    * [6.1 SOM][25746]
    * [6.2 ADB4006 Baseboard][25747]
  * [7 Also known as][25748]
  * [8 See also][25749]
    * [8.1 Manufacturer images][25750]

# In-Circuit and open source software
On their website, In-Circuit used to claim that they had a Board-Support-Package available, and that they were available for "linux driver development and adaptation", but no such code was available from [their website or wiki][25751] for the longest time. The device itself came shipped with a totally unaltered cubieboard2 cubiez image. 
After buying the hardware, [Luc Verhaegen][25752] contacted in-circuit GmbH with a request for the u-boot and linux kernel source code on 20150919. And again on 20150922. A [buildroot tarball][25753] was provided on 20150929. 
In [their documentation][25754], In-circuit GmbH stated "Combining the power and software-ease of community proven embedded boards like: +Banana-Pi, Cubie, OlinuXino and PCDUINO3". The provided buildroot tarball clearly used our sunxi-3.4 kernel, our classic sunxi u-boot, sunxi-tools, sunxi-mali and sunxi-cedarx, so this "community proven" thing is clearly very uni-directional. It is not clear why In-Circuit chose this mode of cooperation with the sunxi community, but it left a rather bad taste in the mouth. 
Support for this board was only added to the kernel in [may 2023][25755], and to u-boot in [november 2023][25756]. 9 years after this hardware was released. These commits are likely more a personal project of [Ludwig Kormann][25757], an employee of In-Circuit GmbH, rather than company policy. Ludwig then went and removed the historically accurate and still very relevant information from 2015, from this wiki on the 29th of january of 2024. 
All in all, In-Circuit GmbH does not feel like a serious "linux driver development and adaptation" partner. If you really want to build an embedded device around an Allwinner A20 based SOM, take a look at [Olimex A20-SOM][25758] instead, or get one of [ the other Community devices][25759]. 
# Identification
The SO-DIMM System-On-Module has absolutely no discernable markings on it. 
On the ADB4006 daughterboard, below where the SOM sits, it reads: 
[code] 
    SoMPi
[/code]
On the back of the ADB4006 daughterboard PCB, the following is silkscreened: 
[code] 
    IN-CIRCUIT
    ENGINEERING AS A PASSION
    ICnova ADB4006
    Application Development Board
    for SoMPi
    design and copyright by
    In-Circuit GmbH
    www.in-circuit.de
[/code]
# Sunxi support
## Current status
Fully upstreamed. 
DTSes and u-boot config were upstreamed in may and november 2023 respectively. Due to the rather advanced support for the A20 by the open source community, no further work was required by an in-circuit employee about 9 years after the release of this hardware. So much for "linux driver development and adaptation". 
## Manual build
You can build things for yourself by following our [ Manual build howto][25760] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _INCIRCUIT_ICNOVA_A20_ build target. 
#### Mainline U-Boot
Use the _icnova-a20-adb4006_defconfig_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [in-circuit_icnova_a20_on_adb4006.fex][25761] file. 
#### Mainline kernel
Use the _sun7i-a20-icnova-a20-adb4006.dtb_ device-tree binary. 
### Buildroot
Use the _icnova-a20-adb4006_defconfig_ build target. 
# Tips, Tricks, Caveats
## FEL mode
The 'Boot' button triggers [ FEL mode][25762]. 
# Adding a serial port
[![][25763]][25764]
[][25765]
ADB4006 primary UART connector
On the top side of the ADB4006 baseboard, there is a nicely marked UART0 connector. Just attached some leads according to our [UART howto][25766]. 
There are further headers with UART2/5/6/7 on the board, but they are unpopulated. 
# Pictures
## SOM
  * [![In-circuit icnova a20 som front.jpeg][25767]][25768]
  * [![In-circuit icnova a20 som back.jpeg][25769]][25770]

## ADB4006 Baseboard
  * [![In-circuit icnova a20 baseboard front.jpeg][25771]][25772]
  * [![In-circuit icnova a20 baseboard back.jpeg][25773]][25774]
  * [![In-circuit icnova a20 baseboard connectors 1.jpeg][25775]][25776]
  * [![In-circuit icnova a20 baseboard connectors 2.jpeg][25777]][25778]

# Also known as
In-Circuit sometimes calls it _SomPi_ but even the domain [sompi.de][25779] has long expired (status 20150924). 
# See also
  * [Olimex A20-SOM][25758]

## Manufacturer images
  * The manufacturer mentioned Cubieboard2 images, but of course did not link to these directly. Beware though, Cubieboard2 and this device are of course not 100% compatible (even though In-Circuit claimed otherwise).
  * After several requests over more than a week in september 2015, a link to [this buildroot tarball][25753] was provided.
