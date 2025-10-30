# Xunlong Orange Pi 2
Xunlong Orange Pi 2  
---  
[![Xunlong OrangePi2.jpg][60383]][60384]  
Manufacturer |  [OrangePi][60385]  
Dimensions |  93 _mm_ x 60 _mm_  
Release Date |  March 2015   
Website |  [Orange Pi 2 Product Page][60386]  
Specifications   
SoC |  [H3][60387] @ 1.3 GHz   
DRAM |  1GiB DDR3 @ 600MHz   
NAND |  no nand available   
Power |  DC 5V @ 2A (via DC input)   
Features   
Video |  HDMI output with HDCP, HDMI CEC, HDMI 30 function, Integrated CVBS, simultaneous output of HDMI and CVBS   
Audio |  3.5 mm Jack and HDMI   
Network |  10/100Mbps Ethernet(RJ45), WiFi (Realtek RTL8189ETV, IEEE 802.11 b/g/n)   
Storage |  TF card(Max 64GB)/MMC card slot   
USB |  4 USB2.0 Host, 1 USB2.0 OTG   
Other |  [CIR][60388]  
Headers |  1 pin UART, 3 pin UART, LCD/ LVDS, CSI, 40 pin GPIO   
_Orange Pi 2_ is [H3][60387] based development board produced by [Xunlong][60389]. The concept is based on the original [Orange Pi][60390]. Both, Orange Pi 2 and its smaller cousin [Orange Pi Mini 2][60391] (similar to [Orange Pi Mini][60392]) were released in March 2015. The board is based on a quad-core [H3][60387] CPU, and offers a TF card slot, onboard Ethernet (10/100M Ethernet RJ45) and WiFi (802.11 b/g/n), 40 pin GPIO and 4 x USB type A connectors, but does not come with the SATA port like the [A20][60393] based original [Orange Pi][60390] did. 
## Contents
  * [1 Identification][60394]
  * [2 Sunxi support][60395]
    * [2.1 Current status][60396]
    * [2.2 Manual build][60397]
      * [2.2.1 U-Boot][60398]
        * [2.2.1.1 Mainline U-Boot][60399]
      * [2.2.2 Linux Kernel][60400]
        * [2.2.2.1 Sunxi/Legacy Kernel][60401]
        * [2.2.2.2 Mainline kernel][60402]
  * [3 Tips, Tricks, Caveats][60403]
    * [3.1 FEL mode][60404]
    * [3.2 LEDs][60405]
    * [3.3 Expansion Ports][60406]
  * [4 Adding a serial port][60407]
    * [4.1 Locating the UART][60408]
  * [5 Pictures][60409]
  * [6 Variants][60410]
  * [7 Also known as][60411]
  * [8 See also][60412]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi 2
[/code]
# Sunxi support
## Current status
The H3 SoC support has matured since its introduction in kernel 4.2. Most of the board functionality for boards such as Orange Pi 2 are available with current mainline kernels. Some features (hw accelerated crypto, hw spinlocks, and thermal) are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][60413]. In addition, legacy 3.4 kernels are available in various work-in-progress git branches. 
See the [Manual build][60397] section for more details. 
  

## Manual build
You can build things for yourself by following our [Manual build howto][60414] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_2** (supported since v2016.05) build target. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][60415]. 
The H3 boards can boot from [SD cards][60416], [eMMC][60417], [NAND][60418] or [SPI NOR][60419] flash (if available), and via [FEL][60420] using the OTG USB port. In U-Boot, loading the kernel is also supported from USB or ethernet (netboot). HDMI support in U-Boot is still WIP. 
### Linux Kernel
#### Sunxi/Legacy Kernel
The 3.4 kernel from the official [Allwinner's git repository][60421] [does not support H3][60422] yet. But it is possible to use one of the kernel forks, based on the [lichee H3 SDK tarball][60423]: 
  * [Siarhei Siamashka's branch '20151207-embedded-lima-memtester-h3'][60424]
  * [Yann Dirson's fork][60425] added a few more fixes and adopted most of
  * [Boris Lovosevic' great initial work][60426] on Allwinner's H3 kernel

Configure this kernel using **sun8i_h3_defconfig** , the rest is explained in the [kernel compilation guide][60427]. 
Use the .fex file for generating [script.bin][60428]. The .fex file can be found here for now [orangepi2.fex][60429]. This was extracted from the android sdcard image. 
When booting the legacy 3.4 kernel with the mainline U-Boot, add the following line to boot.cmd: 
[code] 
      setenv machid 1029
      setenv bootm_boot_mode sec
    
[/code]
Some other legacy kernel repositories: 
  * [3.4-lichee-based kernel][60430], based on work by [ssvb][60431] and [loboris][60432]
  * [Yocto support here][60433] glues together all the required parts to get this kernel to work with mainline u-boot, as well as accelerated X11/GLES support
  * [A newer H3 BSP variant][60434] appeared with tons of fixes which has been made available by FriendlyARM.
  * [A cleaned up fork][60435] has been adopted by Armbian project. On top of that Armbian maintains a bunch of [3.4.x patches for H3 devices][60436].

#### Mainline kernel
The mainline kernel has good support for the H3 SoC. Please refer to the [status matrix][60437] for a more detailed list of the development process, links to patches and links to kernel fork repositories. Minor drivers that are currently work-in-progress may require a) [third party patches][60438] (see also arm-linux mailing list) or b) a pre-patched distro (e.g. [Armbian][60439]). 
Repositories with H3 patches: 
  * [Ondřej Jirman's branch for H3 based orange Pi (kernel 4.19)][60440] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)
  * [Philipp Rossak's THS patches (in the sunxi-ths- branches)][60441]
  * [Corentin Labbe's HW Crypto and spinlock patches (in respective branches)][60442]

  
Use the **sun8i-h3-orangepi-2.dtb** device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The button marked _SW3_ , located between the HDMI and TTL UART, triggers [ FEL mode][60443] when pressed during boot. 
To [ verify][60444] you have successfully entered FEL mode, check the output of `fel version`. For the Orange Pi 2, it should look like: 
[code] 
    AWUSBFEX soc=00001680(unknown) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
[/code]
## LEDs
For those with a transparent case (or no case at all) the Orange Pi 2's LED activity is good. The **red** power LED (_D7_) can be turned off. 
## Expansion Ports
The Orange Pi 2 exposes a 2.54mm pitch connector. 
Extension Header   
---  
1x40 Header   
1 | _3.3V_ | 2 | _VCC-5V_  
3 | [PA12][60445] (TWI0-SDA/DI_RX/EINT12) | 4 | _VCC-5V_  
5 | [PA11][60446] (TWI0-SCK/DI_TX/EINT11) | 6 | _GND_  
7 | [PA6][60447] (SIM_PWREN/PWM1/PA_EINT6) | 8 | [PA13][60448] (SPI1_CS/UART3_TX/PA_EINT13)  
9 | _GND_ | 10 | [PA14][60449] (SPI1_CLK/UART3_RX/PA_EINT14)  
11 | [PA1][60450] (UART2_RX/JTAG_CK0/PA_EINT1) | 12 | [PD14][60451](RGMII_NULL/MII_TXERR/RMII_NULL)  
13 | [PA0][60452] (UART2_TX/JTAG_MS0/PA_EINT0) | 14 | _GND_  
15 | [PA3][60453] (UART2_CTS/JTAG_DI0/PA_EINT3) | 16 | [PC4][60454] (NAND_CE0)  
17 | _3.3V_ | 18 | [PC7][60455] (NAND_RB1)  
19 | [PC0][60456] (NAND_WE/SPI0_MOSI) | 20 | _GND_  
21 | [PC1][60457] (NAND_ALE/SPI0_MISO) | 22 | [PA2][60458] (UART2_RTS/JTAG_DO0/PA_EINT2)  
23 | [PC2][60459] (NAND_CLE/SPI0_CLK) | 24 | [PC3][60460] (NAND_CE1/SPI0_CS)  
25 | _GND_ | 26 | [PA21][60461] (PCM0_DIN/SIM_VPPPP/PA_EINT21)  
27 | [PA19][60462] (PCM0_CLK/TWI1_SDA/PA_EINT19) | 28 | [PA18][60463] (PCM0_SYNC/TWI1_SCK/PA_EINT18)  
29 | [PA7][60464] (SIM_CLK/PA_EINT7) | 30 | _GND_  
31 | [PA8][60465] (SIM_DATA/PA_EINT8) | 32 | [PG8][60466] (UART1_RTS/PG_EINT8)  
33 | [PA9][60467] (SIM_RST/PA_EINT9) | 34 | _GND_  
35 | [PA10][60468] (SIM_DET/PA_EINT10) | 36 | [PG9][60469] (UART1_CTS/PG_EINT9)  
37 | [PA20][60470] (PCM0_DOUT/SIM_VPPEN/PA_EINT20) | 38 | [PG6][60471] (UART1_TX/PG_EINT6)  
39 | _GND_ | 40 | [PG7][60472] (UART1_RX/PG_EINT7)  
# Adding a serial port
[![][60473]][60474]
[][60475]
UART pads
## Locating the UART
The UART pins are located on J3 between DC input and Uboot Button(SW3) of the board. They are marked as _TX_ , _RX_ and _GND_ on the PCB. Just attach some leads according to our [UART Howto][60476]. 
# Pictures
  * [![Xunlong OrangePi2 front.jpg][60477]][60478]
  * [![Xunlong OrangePi2 back.jpg][60479]][60480]
  * [![Xunlong Orangepi2 d.jpg][60481]][60482]
  * [![Xunlong Orangepi2 u.jpg][60483]][60484]
  * [![Xunlong Orangepi2 l.jpg][60485]][60486]
  * [![Xunlong Orangepi2 r.jpg][60487]][60488]

# Variants
  * The original [Orange Pi][60390] was released in November 2014. The Orange Pi features a standard TF card slot and a 26 pin GPIO connector (similar to the Raspberry Pi A/B).
  * The smaller cousin [Orange Pi Mini 2][60391] (similar to [Orange Pi Mini][60392]) were also released in March 2015.

# Also known as
# See also
There are several websites about Orange Pi 2 and claiming to support it. It has to be clarified, what is "official" and who is behind this sites. 
  * [Xunlong Orange Pi site][60489]
  * ["Official" Github Repository][60490].
  * ["Official" Orange Pi Form][60491].
  * [H3_Manual_build_howto][60492].

Currently only an android image for an [sdcard][60493] is provided via OrangePi's Website.
