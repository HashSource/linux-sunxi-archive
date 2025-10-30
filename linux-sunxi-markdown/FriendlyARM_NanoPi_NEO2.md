# FriendlyARM NanoPi NEO2
FriendlyARM NanoPi NEO2  
---  
[![NanoPi NEO2 top.jpg][20838]][20839]  
Manufacturer |  [FriendlyARM][20840]  
Dimensions |  40 _mm_ x 40 _mm_  
Release Date |  Apr 2017   
Website |  [NanoPi NEO2][20841]  
Specifications   
SoC |  [H5][20842] @ 816 Mhz   
DRAM |  512MiB DDR3   
Power |  DC 5V @ 2A via microUSB or pin headers   
Features   
Audio |  microphone, stereo line-out, I²S and [S/PDIF][20843] on pin headers   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][20844])   
Storage |  µSD   
USB |  1 USB2.0 Type A, 2 USB2.0 pin header, OTG µUSB   
Headers |  UART, SPI, I²C, 2x USB2.0 Host, analog audio, microphone   
NanoPi NEO 2 is a [H5][20842] based small form-factor development boards produced by [FriendlyARM][20845]. It has the same form factor than the previous [NanoPi NEO][20846], but with H5 instead of the H3 SoC. The NEO comes with integrated 1000 Mbps Ethernet, 1 x USB A 2.0, and a micro-SD card slot. A lot of functionality is provided via the unpopulated headers on both boards. 
## Contents
  * [1 Identification][20847]
  * [2 Sunxi support][20848]
    * [2.1 Current status][20849]
    * [2.2 BSP][20850]
    * [2.3 Manual build][20851]
      * [2.3.1 U-Boot][20852]
        * [2.3.1.1 Mainline U-Boot][20853]
      * [2.3.2 Linux Kernel][20854]
        * [2.3.2.1 Sunxi/Legacy Kernel][20855]
        * [2.3.2.2 Mainline kernel][20856]
  * [3 Expansion Port][20857]
  * [4 Tips, Tricks, Caveats][20858]
    * [4.1 FEL mode][20859]
    * [4.2 LEDs][20860]
    * [4.3 Voltage regulators][20861]
    * [4.4 DRAM][20862]
    * [4.5 USB][20863]
    * [4.6 Analog Audio][20864]
  * [5 Adding a serial port][20865]
    * [5.1 Locating the UART][20866]
  * [6 Pictures][20867]
    * [6.1 NanoPi NEO 2][20868]
  * [7 Variants][20869]
    * [7.1 NanoPi NEO Core2][20870]
    * [7.2 NanoPi NEO2 Black][20871]
  * [8 See also][20872]
    * [8.1 Manufacturer images][20873]

# Identification
# Sunxi support
## Current status
The H5 SoC support has matured since its introduction in kernel 4.12. Most of the board functionality for boards such as FriendlyARM NanoPi NEO2, including 3D graphics, hardware accelerated video and crypto, and DVFS are available with current mainline kernels. Only a very few minor features are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][20874]. 
See the [Manual build][20851] section for more details. 
  

## BSP
FriendlyELEC started in March to switch from Allwinner BSP to an own [mainline kernel fork currently remaining at 4.11.2][20875] where DT files can be found. Same with [mainline u-boot][20876]. Important: They're not following upstream conventions and eg. DRAM configuration in u-boot is [done entirely different][20877]. That means community members relying blindly on FriendlyELEC gihub repos are prone to submit wrong stuff upstream! 
## Manual build
You can build things for yourself by following our [Manual build howto][20878] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **nanopi_neo2_defconfig** (supported since v2017.07) build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
The H5 SoC has support in the [mainline kernels][20879]. 
The development process, links to patches and links to kernel fork repositories are listed on the [ Linux mainlining effort][20879] page. Patches can also be found from the arm-linux mailing list. 
Repositories with H5 patches: 
  * [Ondřej Jirman's branch for H5 based orange Pi (kernel 4.19)][20880] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)

  
Use the **sun50i-h5-nanopi-neo2.dtb** device-tree binary. 
# Expansion Port
See [FriendlyELEC wiki][20881]
# Tips, Tricks, Caveats
## FEL mode
There is no FEL button on this board. Booting without an SD card automagically enters FEL mode. 
[code] 
    ./sunxi-fel version
    AWUSBFEX soc=00001718(H5) 00000001 ver=0001 44 08 scratchpad=00017e00 00000000 00000000
[/code]
## LEDs
Two leds: a blue connected to PA10 labeled 'status' and a green one connected to PL10 labeled 'pwr'. 
## Voltage regulators
FriendlyELEC implemented no CPU voltage regulation on this board so H5 is fed all the time with 1.1V only which limits maximum clockspeed to 816 MHz based on DVFS table provided by Allwinner BSP. 
## DRAM
NanoPi NEO is available with 512 MiB but only in single bank configuration. 
## USB
The one USB host port exposed as type A receptacle is usb3. Both usb1 and usb2 are available via solder holes. USB OTG available through Micro USB. 
## Analog Audio
On NanoPi NEO 2 analog audio out and mic in is available on 5 pin header next to USB receptacle. Please check FriendlyELEC wiki or schematic for details. 
# Adding a serial port
## Locating the UART
[![][20882]][20883]
[][20884]
NanoPi NEO 2 UART pins
Four-pin UART0 header is placed next to analog audio pin header. Pinout: GND, 5V, TX, RX. Pin 1 (GND) is the one furthest from the board edge. Logic voltage is 3.3V. For more instructions refer to our [UART Howto][20885]. 
# Pictures
## NanoPi NEO 2
  * [![NanoPi NEO2 top.jpg][20886]][20839]
  * [![NanoPi NEO2 bottom.jpg][20887]][20888]

# Variants
## NanoPi NEO Core2
In the NEO Core2 variant, the ethernet and USB A connectors are replaced with unpopulated headers (similar to [NanoPi NEO Core][20889]). The variant also comes with onboard eMMC (4GB/8GB/16GB/32GB). 
## NanoPi NEO2 Black
[![][20890]][20891]
[][20892]
NanoPi NEO2 Black UART pins
In the NEO2 Black variant an eMMC socket is provided. The pins for UART0 have to be soldered in by the user. 
# See also
  * [NEO2 device page on FriendlyARM wiki][20893]
  * [NEO2 Black device page on FriendlyARM wiki][20894]

## Manufacturer images
See the manufacturer's device pages above since links change from time to time.
