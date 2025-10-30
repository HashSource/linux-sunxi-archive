# Xunlong Orange Pi Mini 2
Xunlong Orange Pi Mini 2  
---  
[![Xunlong Orangepi mini2.jpg][61139]][61140]  
Manufacturer |  [OrangePi][61141]  
Dimensions |  93 _mm_ x 60 _mm_  
Release Date |  March 2015   
Website |  [Orange Pi Mini 2 Product Page][61142]  
Specifications   
SoC |  [H3][61143] @ 1.2GHz   
DRAM |  1GiB DDR3 @ 600MHz   
NAND |  no nand available   
Power |  DC 5V @ 2A (via DC input)   
Features   
Video |  HDMI output with HDCP, HDMI CEC, HDMI 30 function, Integrated CVBS, simultaneous output of HDMI and CVBS   
Audio |  3.5 mm Jack and HDMI   
Network |  10/100Mbps Ethernet(RJ45)   
Storage |  TF card(Max 64GB)/MMC card slot   
USB |  4 USB2.0 Host, 1 USB2.0 OTG   
Other |  [CIR][61144]  
Headers |  1 pin UART, 3 pin UART, LCD/ LVDS, CSI, 40 pin GPIO   
Orange Pi Mini 2 is [H3][61143] based development board produced by [Xunlong][61145]. The concept is based on the original [Orange Pi Mini][61146]. Both, Orange Pi 2 and its smaller cousin Orange Pi Mini 2 were released in March 2015. The board is based on a quad-core [H3][61143] CPU, and offers a TF card slot, onboard Ethernet (10/100M Ethernet RJ45), 40 pin GPIO and 4 x USB type A connectors, but does not come with WiFi or a SATA port like the [A20][61147] based original [Orange Pi Mini][61146] did. 
## Contents
  * [1 Identification][61148]
  * [2 Sunxi support][61149]
    * [2.1 Current status][61150]
    * [2.2 Manual build][61151]
      * [2.2.1 U-Boot][61152]
        * [2.2.1.1 Mainline U-Boot][61153]
      * [2.2.2 Linux Kernel][61154]
        * [2.2.2.1 Sunxi/Legacy Kernel][61155]
        * [2.2.2.2 Mainline kernel][61156]
  * [3 Tips, Tricks, Caveats][61157]
    * [3.1 FEL mode][61158]
    * [3.2 LEDs][61159]
  * [4 Adding a serial port][61160]
    * [4.1 Locating the UART][61161]
  * [5 Pictures][61162]
  * [6 Variants][61163]
  * [7 Also known as][61164]
  * [8 See also][61165]
    * [8.1 Manufacturer images][61166]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi mini 2
[/code]
# Sunxi support
## Current status
The H3 SoC support has matured since its introduction in kernel 4.2. Most of the board functionality for boards such as Orange Pi Mini 2 are available with current mainline kernels. Some features (hw accelerated crypto, hw spinlocks, and thermal) are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][61167]. In addition, legacy 3.4 kernels are available in various work-in-progress git branches. 
See the [Manual build][61151] section for more details. 
  

## Manual build
You can build things for yourself by following our [Manual build howto][61168] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_2** (as a workaround until Orange Pi Mini 2 defconfig is available) build target. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][61169]. 
The H3 boards can boot from [SD cards][61170], [eMMC][61171], [NAND][61172] or [SPI NOR][61173] flash (if available), and via [FEL][61174] using the OTG USB port. In U-Boot, loading the kernel is also supported from USB or ethernet (netboot). HDMI support in U-Boot is still WIP. 
### Linux Kernel
#### Sunxi/Legacy Kernel
The 3.4 kernel from the official [Allwinner's git repository][61175] [does not support H3][61176] yet. But it is possible to use one of the kernel forks, based on the [lichee H3 SDK tarball][61177]: 
  * [Siarhei Siamashka's branch '20151207-embedded-lima-memtester-h3'][61178]
  * [Yann Dirson's fork][61179] added a few more fixes and adopted most of
  * [Boris Lovosevic' great initial work][61180] on Allwinner's H3 kernel

Configure this kernel using **sun8i_h3_defconfig** , the rest is explained in the [kernel compilation guide][61181]. 
Use the .fex file for generating [script.bin][61182]. 
  
When booting the legacy 3.4 kernel with the mainline U-Boot, add the following line to boot.cmd: 
[code] 
      setenv machid 1029
      setenv bootm_boot_mode sec
    
[/code]
Some other legacy kernel repositories: 
  * [3.4-lichee-based kernel][61183], based on work by [ssvb][61184] and [loboris][61185]
  * [Yocto support here][61186] glues together all the required parts to get this kernel to work with mainline u-boot, as well as accelerated X11/GLES support
  * [A newer H3 BSP variant][61187] appeared with tons of fixes which has been made available by FriendlyARM.
  * [A cleaned up fork][61188] has been adopted by Armbian project. On top of that Armbian maintains a bunch of [3.4.x patches for H3 devices][61189].

#### Mainline kernel
The mainline kernel has good support for the H3 SoC. Please refer to the [status matrix][61190] for a more detailed list of the development process, links to patches and links to kernel fork repositories. Minor drivers that are currently work-in-progress may require a) [third party patches][61191] (see also arm-linux mailing list) or b) a pre-patched distro (e.g. [Armbian][61192]). 
Repositories with H3 patches: 
  * [Ondřej Jirman's branch for H3 based orange Pi (kernel 4.19)][61193] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)
  * [Philipp Rossak's THS patches (in the sunxi-ths- branches)][61194]
  * [Corentin Labbe's HW Crypto and spinlock patches (in respective branches)][61195]

  
Use the **sun8i-h3-orangepi-2.dtb** (until a dedicated dtb is available) device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The button marked _SW3_ , located between the HDMI and TTL UART, triggers [ FEL mode][61196] when pressed during boot. 
To [ verify][61197] you have successfully entered FEL mode, check the output of `fel version`. For the Orange Pi Mini 2, it should look like: 
[code] 
    AWUSBFEX soc=00001680(unknown) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
[/code]
## LEDs
For those with a transparent case (or no case at all) the Orange Pi Mini 2's LED activity is good. The **red** power LED (_D7_) can be turned off. 
# Adding a serial port
[![][61198]][61199]
[][61200]
UART pads
## Locating the UART
The UART pins are located between DC input and Uboot Button(SW3) of the board. They are marked as _TX_ , _RX_ and _GND_ on the PCB. Just attach some leads according to our [UART Howto][61201]. **Do not connect the red wire (VCC or 3.3V/5V), as that might damage your board.**
# Pictures
  * [![Xunlong Orangepi mini2 front.jpg][61202]][61203]
  * [![Xunlong Orangepi mini2 back.jpg][61204]][61205]
  * [![Xunlong Orangepi mini2 d.jpg][61206]][61207]
  * [![Xunlong Orangepi mini2 u.jpg][61208]][61209]
  * [![Xunlong Orangepi mini2 l.jpg][61210]][61211]
  * [![Xunlong Orangepi mini2 r.jpg][61212]][61213]

# Variants
  * The original [Orange Pi][61214] and [Orange Pi Mini][61146] were released in November 2014.
  * The [Orange Pi 2][61215] variant was also released in March 2015. This version also comes with onboard WiFi.

# Also known as
# See also
There are several websites about Orange Pi Mini 2 and claiming to support it. It has to be clarified, what is "official" and who is behind this sites. 
  * [Xunlong Orange Pi site][61216]
  * ["Official" Github Repository][61217].
  * ["Official" Orange Pi Form][61218].
  * [H3_Manual_build_howto][61219].

## Manufacturer images
A various amount of [prebuilt images][61220] is provided via OrangePi's Website.
