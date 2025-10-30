# Xunlong Orange Pi Plus 2E
Xunlong Orange Pi Plus 2E  
---  
[![Orange Pi Plus 2E top small.jpg][62285]][62286]  
Manufacturer |  [OrangePi][62287]  
Dimensions |  108 _mm_ x 67 _mm_  
Release Date |  May 2016   
Website |  [Orange Pi Plus 2E Product Page][62288]  
Specifications   
SoC |  [H3][62289] @ 1.3GHz[[1]][62290]  
DRAM |  2GiB DDR3 @ 672MHz ([H5TC4G83AFR-PBA][62291])   
NAND |  16GB eMMC Flash (KLMAG2GEND-B031)   
Power |  DC 5V @ 3A (4.0mm/1.7mm barrel plug - centre positive)   
Features   
Video |  HDMI (HDCP, CEC), CVBS   
Audio |  3.5 mm Jack, HDMI, Microphone   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][62292]), WiFi 802.11 b/g/n (Realtek RTL8189FTV)   
Storage |  µSD, eMMC   
USB |  3 USB 2.0 Host, 1 µUSB 2.0 OTG   
Other |  [CIR][62293]  
Headers |  3 pin UART, CSI, 40 pin GPIO   
Orange Pi Plus 2E is a development board produced by [Xunlong][62294], based on the [H3][62289] SoC. It comes with 2GB of DDR3, integrated 16GB eMMC, and gigabit ethernet. It is very similar to [Orange Pi Plus 2][62295], but comes with a newer RTL8189FTV implementation of WiFi and three USB ports with full USB2 bandwidth, but without an onboard SATA bridge, 
## Contents
  * [1 Identification][62296]
  * [2 Sunxi support][62297]
    * [2.1 Current status][62298]
    * [2.2 Manual build][62299]
      * [2.2.1 U-Boot][62300]
        * [2.2.1.1 Mainline U-Boot][62301]
      * [2.2.2 Linux Kernel][62302]
        * [2.2.2.1 Sunxi/Legacy Kernel][62303]
        * [2.2.2.2 Mainline kernel][62304]
  * [3 Expansion Port][62305]
  * [4 Tips, Tricks, Caveats][62306]
    * [4.1 FEL mode][62307]
    * [4.2 Compatibility][62308]
    * [4.3 DRAM clock speed limit][62309]
    * [4.4 Orientation of the GPIO header][62310]
  * [5 Adding a serial port][62311]
    * [5.1 Locating the UART][62312]
  * [6 Pictures][62313]
  * [7 Variants][62314]
  * [8 References][62315]
  * [9 See also][62316]
    * [9.1 Manufacturer images][62317]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi
    Plus 2E V1.1
[/code]
# Sunxi support
## Current status
The H3 SoC support has matured since its introduction in kernel 4.2. Most of the board functionality for boards such as Orange Pi Plus 2E are available with current mainline kernels. Some features (hw accelerated crypto, hw spinlocks, and thermal) are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][62318]. In addition, legacy 3.4 kernels are available in various work-in-progress git branches. 
See the [Manual build][62299] section for more details. 
  

## Manual build
You can build things for yourself by following our [Manual build howto][62319] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_plus2e_defconfig** (supported since v2016.09) build target. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][62320]. 
The H3 boards can boot from [SD cards][62321], [eMMC][62322], [NAND][62323] or [SPI NOR][62324] flash (if available), and via [FEL][62325] using the OTG USB port. In U-Boot, loading the kernel is also supported from USB or ethernet (netboot). HDMI support in U-Boot is still WIP. 
### Linux Kernel
#### Sunxi/Legacy Kernel
The 3.4 kernel from the official [Allwinner's git repository][62326] [does not support H3][62327] yet. But it is possible to use one of the kernel forks, based on the [lichee H3 SDK tarball][62328]: 
  * [Siarhei Siamashka's branch '20151207-embedded-lima-memtester-h3'][62329]
  * [Yann Dirson's fork][62330] added a few more fixes and adopted most of
  * [Boris Lovosevic' great initial work][62331] on Allwinner's H3 kernel

Configure this kernel using **sun8i_h3_defconfig** , the rest is explained in the [kernel compilation guide][62332]. 
Use the .fex file for generating [script.bin][62333]. Use the [xunlong_orange_pi_plus_2e.fex][62334] or [Armbian's preliminary fex file for the Plus 2E][62335] containing performance/thermal fixes for _dvfs_table_ and _cooler_table_. 
When booting the legacy 3.4 kernel with the mainline U-Boot, add the following line to boot.cmd: 
[code] 
      setenv machid 1029
      setenv bootm_boot_mode sec
    
[/code]
Some other legacy kernel repositories: 
  * [3.4-lichee-based kernel][62336], based on work by [ssvb][62337] and [loboris][62338]
  * [Yocto support here][62339] glues together all the required parts to get this kernel to work with mainline u-boot, as well as accelerated X11/GLES support
  * [A newer H3 BSP variant][62340] appeared with tons of fixes which has been made available by FriendlyARM.
  * [A cleaned up fork][62341] has been adopted by Armbian project. On top of that Armbian maintains a bunch of [3.4.x patches for H3 devices][62342].

#### Mainline kernel
The mainline kernel has good support for the H3 SoC. Please refer to the [status matrix][62343] for a more detailed list of the development process, links to patches and links to kernel fork repositories. Minor drivers that are currently work-in-progress may require a) [third party patches][62344] (see also arm-linux mailing list) or b) a pre-patched distro (e.g. [Armbian][62345]). 
Repositories with H3 patches: 
  * [Ondřej Jirman's branch for H3 based orange Pi (kernel 4.19)][62346] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)
  * [Philipp Rossak's THS patches (in the sunxi-ths- branches)][62347]
  * [Corentin Labbe's HW Crypto and spinlock patches (in respective branches)][62348]

  
Use the **sun8i-h3-orangepi-plus2e.dtb** device-tree binary. 
# Expansion Port
[![][62349]][62350]
[][62351]
Board pin layout
  
The Orange Pi Plus 2E has a Raspberry Pi model B+ compatible 40-pin, 0.1" connector with several low-speed interfaces. 
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
The FEL button between microphone and UART header triggers [ FEL mode][62352]. 
## Compatibility
The _Plus 2E_ is somehow a hybrid between _[Orange Pi PC][62353]_ and _[Orange Pi Plus 2][62295]_. It shares the USB setup with the _PC_ (not using an internal USB hub and no USB-to-SATA bridge) and exposes all 3 USB hosts ports as well as the USB OTG directly on USB receptacles without the need to share bandwidth. And with the _Plus 2_ it shares type/amount of DRAM and onboard eMMC storage, Gigabit Ethernet and the board size. Like all larger Orange Pi boards the [SY8106A][62354] voltage regulator is used allowing fine grained control of the _VDD_CPUX_ core voltage. 
Regarding software compatiblity all that's needed are slight modifications to the fex file (using USB stuff from _PC_ and Ethernet from _Plus/Plus 2_) when using legacy kernels. Mainline kernel and U-Boot directly support this board. The board comes with the eMMC already populated with Android. 
Like on [Orange Pi PC Plus][62355] and [Orange Pi Lite][62356] the formerly used _8189ETV_ WiFi module has been replaced with an onboard _8189FTV_ solution. The available driver has to be build differently, needs some fixes and shows currently the behaviour that it chooses a different MAC address on every reboot. 
## DRAM clock speed limit
[![MBOX icon important.png][62357]][62358] | WARNING: For yet unknown reasons the _lima-memtester_ tool does not work as designed on the _Plus 2E_ (no spinning cube therefore no heavy load so currently it's just a _memtester_ without _lima_ so the results below are worthless and tests have to be repeated when the tool has been fixed).   
---|---  
DRAM is clocked at **672 MHz** by the hardware vendor. But the reliability still needs to be verified. One of the ways of doing reliability tests may be <https://github.com/ssvb/lima-memtester/releases/tag/20151207-orange-pi-pc-fel-test> (developed for Orange Pi PC). An adoption of this using fex files suited for Orange Pi Plus 2E is available [here][62359] (md5sum: ca8b910a5f60bbd11781423e8ade59fd fel-boot-lima-memtester-on-orange-pi-h3-v3.tar.bz2). Use the _fel-boot-lima-memtester-on-orange-pi-plus-2e_ script inside. 
Since the board features an Android populated eMMC the procedure to run lima-memtester through FEL is as follows: eject SD card, connect OTG cable to your host, press the [FEL button][62307], then provide power through barrel plug or GPIO pins, then start the _fel-boot-lima-memtester-on-orange-pi-plus-2e_ on your host. Most probably lima-memtester will continue to run when you cut DC-IN since after the board has been powered on it can also use 5V provided through OTG port. 
Hardware  | Diagnostic software  | lima-memtester passes (survives until the red LED)  | lima-memtester fails  | Notes   
---|---|---|---|---  
[User:Tkaiser][62360]'s Orange Pi Plus 2E | fel-boot-lima-memtester-on-orange-pi-h3-v3.tar.bz2 | 744 MHz | 768 MHz | **cheap heatsink**. 768 MHz fails after running for approx. 4 minutes   
[User:lanefu][62361]'s Orange Pi Plus 2E | fel-boot-lima-memtester-on-orange-pi-h3-v3.tar.bz2 | 768 MHz | 792 MHz | **no heatsink**. 792 MHz parameter causes fel-boot-lima-memtester to fail to connect to FEL usb   
## Orientation of the GPIO header
Xunlong chose to rotate the 40 pin GPIO connector by 180° so RPi HATs can still be used but will project over the board in the opposite direction than intended. Keep this also in mind when you want to power the board through GPIO pins 2/4/6 (2/4 being connected directly with DC-IN and 6 being GND) 
# Adding a serial port
## Locating the UART
[![][62362]][62363]
[][62364]
UART pins
The UART header is between FEL and power button (simplified layout: ..MIC.. [TX][RX][GND] ..DC-IN..). Just attach some leads according to our [UART howto][62365]. 
# Pictures
Please note that the board is sold without heatsink. This is just the [tester's standard heatsink for all H3 boards][62366] now. 
  * [![Orange Pi+2e front.JPG][62367]][62368]
  * [![Orange Pi+2e back.JPG][62369]][62370]
  * [![Orange Pi Plus 2E top.jpg][62371]][62372]
  * [![Orange Pi Plus 2E bottom.jpg][62373]][62374]
  * [![Orange Pi Plus 2E 1.jpg][62375]][62376]
  * [![Orange Pi Plus 2E 2.jpg][62377]][62378]
  * [![Orange Pi Plus 2E 3.jpg][62379]][62380]
  * [![Orange Pi Plus 2E 4.jpg][62381]][62382]

# Variants
  * Named almost similar the more expensive _[Orange Pi Plus 2][62295]_ is rather different due to another USB setup (using a slow onboard USB-to-SATA bridge and an internal USB hub leading to shared USB bandwidth) and an older WiFi implementation (RTL8189ETV instead of RTL8189FTV now used)

# References
  1. [↑][62383] Orange Pi product pages show H3 @ 1.6GHz but this can be considered marketing. Limiting maximum cpufreq to 1296 MHz is realistic and when using a heatsink the board can run rather heavy workloads on all 4 CPU cores at this clockspeed

# See also
  * [File:Orangepi-plus-2e-v1 1-schematic.pdf][62384]

## Manufacturer images
