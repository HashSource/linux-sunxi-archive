# Xunlong Orange Pi Plus 2
Xunlong Orange Pi Plus 2  
---  
[![Xunlong OrangePi Plus 2.jpg][62166]][62167]  
Manufacturer |  [OrangePi][62168]  
Dimensions |  108mm x 67mm   
Release Date |  December 2015   
Website |  [Orange Pi Plus 2 Product Page][62169]  
Specifications   
SoC |  [H3][62170] @ 1.2GHz[[1]][62171]  
DRAM |  2GiB DDR3 @ ?MHz ([H5TC4G83AFR-PBA][62172])   
NAND |  16GB EMMC Flash (in 2016 KLMAG2GEND-B031 but now slower [KLMAG2WEPD-B031][62173])   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive)   
Features   
Video |  HDMI (HDCP, CEC), CVBS   
Audio |  3.5 mm Jack, HDMI, Microphone   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][62174]), WiFi 802.11 b/g/n (Realtek RTL8189ETV)   
Storage |  µSD (max 64GB), SATA 2.0 (via GL830 USB-to-SATA bridge, +5V power on JST XH 2.5mm connector)   
USB |  4 USB 2.0 Host (via FE1.1s hub), 1 USB 2.0 OTG   
Other |  [CIR][62175]  
Headers |  3 pin UART, CSI, 40 pin GPIO   
Orange Pi Plus 2 is a [H3][62170] based development board produced by [Xunlong][62176]. It is an upgraded version of [Orange Pi Plus][62177] with twice the RAM and onboard flash. It is also similar to [Orange Pi Plus 2E][62178], but comes with an older RTL8189ETV implementation of WiFi, with an onboard SATA bridge connected to of the USB ports, and with four USB ports connected to an internal USB hub. This design significantly reduces the available total USB bandwidth of the device. 
## Contents
  * [1 Identification][62179]
  * [2 Sunxi support][62180]
    * [2.1 Current status][62181]
    * [2.2 Manual build][62182]
      * [2.2.1 U-Boot][62183]
        * [2.2.1.1 Mainline U-Boot][62184]
      * [2.2.2 Linux Kernel][62185]
        * [2.2.2.1 Sunxi/Legacy Kernel][62186]
        * [2.2.2.2 Mainline kernel][62187]
  * [3 Expansion Port][62188]
  * [4 Tips, Tricks, Caveats][62189]
    * [4.1 FEL mode][62190]
    * [4.2 Compatibility][62191]
    * [4.3 Overheating][62192]
  * [5 Serial port][62193]
    * [5.1 Locating the UART][62194]
  * [6 Pictures][62195]
  * [7 References][62196]
  * [8 Variants][62197]
  * [9 See also][62198]
    * [9.1 Manufacturer images][62199]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi
    Plus 2 V1.1
[/code]
# Sunxi support
## Current status
The H3 SoC support has matured since its introduction in kernel 4.2. Most of the board functionality for boards such as Orange Pi Plus 2 are available with current mainline kernels. Some features (hw accelerated crypto, hw spinlocks, and thermal) are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][62200]. In addition, legacy 3.4 kernels are available in various work-in-progress git branches. 
See the [Manual build][62182] section for more details. 
The device works quite well on kernel 3.4 (Ethernet, Audio, USB devices, eMMC), but without support for onboard Wi-Fi module. Both, the mainline kernel and U-Boot support the board functionality, but currently no U-Boot defconfig nor a device-tree file for this particular board are available. 
## Manual build
You can build things for yourself by following our [Manual build howto][62201] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_plus_2e** (as a workaround until dedicated defconfig is available) build target. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][62202]. 
The H3 boards can boot from [SD cards][62203], [eMMC][62204], [NAND][62205] or [SPI NOR][62206] flash (if available), and via [FEL][62207] using the OTG USB port. In U-Boot, loading the kernel is also supported from USB or ethernet (netboot). HDMI support in U-Boot is still WIP. 
### Linux Kernel
#### Sunxi/Legacy Kernel
The 3.4 kernel from the official [Allwinner's git repository][62208] [does not support H3][62209] yet. But it is possible to use one of the kernel forks, based on the [lichee H3 SDK tarball][62210]: 
  * [Siarhei Siamashka's branch '20151207-embedded-lima-memtester-h3'][62211]
  * [Yann Dirson's fork][62212] added a few more fixes and adopted most of
  * [Boris Lovosevic' great initial work][62213] on Allwinner's H3 kernel

Configure this kernel using **sun8i_h3_defconfig** , the rest is explained in the [kernel compilation guide][62214]. 
Use the .fex file for generating [script.bin][62215]. It's possible to use one of [forks on GitHub][62216] to create Debian / Ubuntu image with kernel 3.4. Images for Orange Pi Plus should work without problems. 
When booting the legacy 3.4 kernel with the mainline U-Boot, add the following line to boot.cmd: 
[code] 
      setenv machid 1029
      setenv bootm_boot_mode sec
    
[/code]
Some other legacy kernel repositories: 
  * [3.4-lichee-based kernel][62217], based on work by [ssvb][62218] and [loboris][62219]
  * [Yocto support here][62220] glues together all the required parts to get this kernel to work with mainline u-boot, as well as accelerated X11/GLES support
  * [A newer H3 BSP variant][62221] appeared with tons of fixes which has been made available by FriendlyARM.
  * [A cleaned up fork][62222] has been adopted by Armbian project. On top of that Armbian maintains a bunch of [3.4.x patches for H3 devices][62223].

#### Mainline kernel
The mainline kernel has good support for the H3 SoC. Please refer to the [status matrix][62224] for a more detailed list of the development process, links to patches and links to kernel fork repositories. Minor drivers that are currently work-in-progress may require a) [third party patches][62225] (see also arm-linux mailing list) or b) a pre-patched distro (e.g. [Armbian][62226]). 
Repositories with H3 patches: 
  * [Ondřej Jirman's branch for H3 based orange Pi (kernel 4.19)][62227] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)
  * [Philipp Rossak's THS patches (in the sunxi-ths- branches)][62228]
  * [Corentin Labbe's HW Crypto and spinlock patches (in respective branches)][62229]

  
Use the **sun8i-h3-orangepi-plus-2e.dtb** device-tree binary. 
# Expansion Port
The Orange Pi Plus 2 has a Raspberry Pi model B+ compatible 40-pin, 0.1" connector with several low-speed interfaces. 
2x20 Header   
---  
1 | _3.3V_ | 2 | _5V_  
3 | PA12 (TWI0_SDA/DI_RX/PA_EINT12) | 4 | _5V_  
5 | PA11 (TWI0_SCK/DI_TX/PA_EINT11) | 6 | _GND_  
7 | PA6 (SIM_PWREN/PWM1/PA_EINT6) | 8 | PA13 (SPI1_CS/UART3_TX/PA_EINT13)  
9 | _GND_ | 10 | PA14 (SPI1_CLK/UART3_RX/PA_EINT14)  
11 | PA1 (UART2_RX/JTAG_CK/PA_EINT1) | 12 | PD14   
13 | PA0 (UART2_TX/JTAG_MS/PA_EINT0) | 14 | _GND_  
15 | PA3 (UART2_CTS/JTAG_DI/PA_EINT3) | 16 | PC4   
17 | _3.3V_ | 18 | PC7   
19 | PC0 (SPI0_MOSI) | 20 | _GND_  
21 | PC1 (SPI0_MISO) | 22 | PA2 (UART2_RTS/JTAG_DO/PA_EINT2)  
23 | PC2 (SPI0_CLK) | 24 | PC3 (SPI0_CS)  
25 | _GND_ | 26 | PA21 (PCM0_DIN/SIM_VPPPP/PA_EINT21)  
27 | PA19 (PCM0_CLK/TWI1_SDA/PA_EINT19) | 28 | PA18 (PCM0_SYNC/TWI1_SCK/PA_EINT18)  
29 | PA7 (SIM_CLK/PA_EINT7) | 30 | _GND_  
31 | PA8 (SIM_DATA/PA_EINT8) | 32 | PG8 (UART1_RTS/PG_EINT8)  
33 | PA9 (SIM_RST/PA_EINT9) | 34 | _GND_  
35 | PA10 (SIM_DET/PA_EINT10) | 36 | PG9 (UART1_CTS/PG_EINT9)  
37 | PA20 (PCM0_DOUT/SIM_VPPEN/PA_EINT20) | 38 | PG6 (UART1_TX/PG_EINT6)  
39 | _GND_ | 40 | PG7 (UART1_RX/PG_EINT7)  
# Tips, Tricks, Caveats
## FEL mode
The FEL button (SW3) next to the UART pins triggers [ FEL mode][62230]. 
## Compatibility
Device should be compatible with images for Orange Pi Plus with some minor issues (notably - Wi-Fi chip not working), but all other major components should work out of the box: 
  * Ethernet
  * USB Devices
  * eMMC Storage
  * Internal Audio
  * USB-SATA Chip

## Overheating
Due to quite high frequency (around 1.6 GHz) it's possible to easily overheat chip which may lead to decreasing CPU / DDR frequency or disabling one or more CPUs. Installing heatsink and using cpufreq should help to avoid this problem. 
# Serial port
## Locating the UART
[![][62231]][62232]
[][62233]
UART pins
Serial port is located near power jack, between SW3 and SW4 buttons. Pins are marked as Tx / Rx / GND on PCB. Please refer to [UART Howto][62234] in case of any problems. 
# Pictures
  * [![Xunlong OrangePi Plus 2 front.jpg][62235]][62236]
  * [![Xunlong OrangePi Plus 2 back.jpg][62237]][62238]
  * [![Xunlong OrangePi Plus 2 side.jpg][62239]][62240]
  * [![Xunlong OrangePi Plus 2 side2.jpg][62241]][62242]
  * [![Xunlong OrangePi Plus 2 top.jpg][62243]][62244]
  * [![Xunlong OrangePi Plus 2 bottom.jpg][62245]][62246]

# References
  1. [↑][62247] The 1.6GHz seem to be specified mainly for marketing reasons. Expect problems when trying to run the device at this frequency under constant load, e.g. [overheating][62192]. ~1.2GHz is probably a more realistic figure.

# Variants
  * _[Orange Pi Plus][62177]_ is pretty similar regarding USB/SATA but has half the amount of DRAM and eMMC storage
  * Named pretty similar the cheaper _[Orange Pi Plus 2E][62248]_ adds Realtek RTL8189FTV SDIO-based WiFi directly on the board (as opposed to a soldered-on module), exposes all USB host ports without an internal hub and saves the slow GL830 USB-to-SATA bridge.

# See also
<http://www.orangepi.org/orangepibbsen/forum.php>
## Manufacturer images
