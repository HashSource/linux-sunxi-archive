# Xunlong Orange Pi Zero Plus 2
Xunlong Orange Pi Zero Plus 2  
---  
[![OPi Zero Plus 2 Top.jpg][63094]][63095]  
Manufacturer |  [OrangePi][63096]  
Dimensions |  46 _mm_ x 48 _mm_  
Release Date |  March 2017   
Website |  [Orange Pi Zero Plus 2 Product Page][63097]  
Specifications   
SoC |  [H3][63098] / [H5][63099]  
DRAM |  512 MiB DDR3   
Power |  DC 5V via µUSB or pin headers   
Features   
Video |  HDMI, CVBS on pin headers   
Audio |  microphone, stereo line-out on pin headers   
Network |  [AP6212 Wi-Fi sdio-id:02D0:A9A6][63100]  
Storage |  µSD, 8GB eMMC on board   
USB |  1 USB 2.0 OTG, 2 x USB 2.0 on pin headers   
Other |  [CIR][63101] on pin headers   
Headers |  3 pin UART, 26 + 13 pin GPIO   
Orange Pi Zero Plus 2 and Orange Pi Zero Plus 2 H5 are development boards produced by [Xunlong][63102]. Orange Pi Zero Plus 2 is based on [H3][63098] SoC while the H5 version uses [H5][63099]. 
## Contents
  * [1 Identification][63103]
  * [2 Sunxi support][63104]
    * [2.1 Current status][63105]
    * [2.2 Manual build][63106]
      * [2.2.1 U-Boot][63107]
        * [2.2.1.1 Mainline U-Boot][63108]
      * [2.2.2 Linux Kernel][63109]
        * [2.2.2.1 Sunxi/Legacy Kernel][63110]
        * [2.2.2.2 Mainline kernel][63111]
  * [3 Expansion Port][63112]
  * [4 Tips, Tricks, Caveats][63113]
    * [4.1 Powering the board][63114]
    * [4.2 FEL Mode][63115]
    * [4.3 Onboard eMMC][63116]
    * [4.4 LEDs][63117]
    * [4.5 Camera][63118]
    * [4.6 USB header][63119]
    * [4.7 JTAG][63120]
  * [5 Adding a serial port][63121]
    * [5.1 Locating the UART][63122]
  * [6 Pictures][63123]
  * [7 Variants][63124]
  * [8 Also known as][63125]
  * [9 See also][63126]
    * [9.1 Manufacturer images][63127]
  * [10 References][63128]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi Zero Plus 2 V1.0
[/code]
# Sunxi support
## Current status
The H3 SoC support has matured since its introduction in kernel 4.2. Most of the board functionality for boards such as Orange Pi Zero Plus 2 are available with current mainline kernels. Some features (hw accelerated crypto, hw spinlocks, and thermal) are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][63129]. In addition, legacy 3.4 kernels are available in various work-in-progress git branches. 
See the [Manual build][63106] section for more details. 
  

## Manual build
You can build things for yourself by following our [Manual build howto][63130] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_zero_plus2_defconfig** (H5 version supported since v2017.07) / **orangepi_zero_plus2_h3_defconfig** (H3 version supported since v2020.01) build target. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][63131]. 
The H3 boards can boot from [SD cards][63132], [eMMC][63133], [NAND][63134] or [SPI NOR][63135] flash (if available), and via [FEL][63136] using the OTG USB port. In U-Boot, loading the kernel is also supported from USB or ethernet (netboot). HDMI support in U-Boot is still WIP. 
### Linux Kernel
#### Sunxi/Legacy Kernel
The 3.4 kernel from the official [Allwinner's git repository][63137] [does not support H3][63138] yet. But it is possible to use one of the kernel forks, based on the [lichee H3 SDK tarball][63139]: 
  * [Siarhei Siamashka's branch '20151207-embedded-lima-memtester-h3'][63140]
  * [Yann Dirson's fork][63141] added a few more fixes and adopted most of
  * [Boris Lovosevic' great initial work][63142] on Allwinner's H3 kernel

Configure this kernel using **sun8i_h3_defconfig** , the rest is explained in the [kernel compilation guide][63143]. 
Use the .fex file for generating [script.bin][63144]. Partially supported but an [Armbian legacy image][63145] with nearly full hardware support already exists. 
When booting the legacy 3.4 kernel with the mainline U-Boot, add the following line to boot.cmd: 
[code] 
      setenv machid 1029
      setenv bootm_boot_mode sec
    
[/code]
Some other legacy kernel repositories: 
  * [3.4-lichee-based kernel][63146], based on work by [ssvb][63147] and [loboris][63148]
  * [Yocto support here][63149] glues together all the required parts to get this kernel to work with mainline u-boot, as well as accelerated X11/GLES support
  * [A newer H3 BSP variant][63150] appeared with tons of fixes which has been made available by FriendlyARM.
  * [A cleaned up fork][63151] has been adopted by Armbian project. On top of that Armbian maintains a bunch of [3.4.x patches for H3 devices][63152].

#### Mainline kernel
The mainline kernel has good support for the H3 SoC. Please refer to the [status matrix][63153] for a more detailed list of the development process, links to patches and links to kernel fork repositories. Minor drivers that are currently work-in-progress may require a) [third party patches][63154] (see also arm-linux mailing list) or b) a pre-patched distro (e.g. [Armbian][63155]). 
Repositories with H3 patches: 
  * [Ondřej Jirman's branch for H3 based orange Pi (kernel 4.19)][63156] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)
  * [Philipp Rossak's THS patches (in the sunxi-ths- branches)][63157]
  * [Corentin Labbe's HW Crypto and spinlock patches (in respective branches)][63158]

  
Use the **sun50i-h5-orangepi-zero-plus2.dtb** (H5 version) / **sun8i-h3-orangepi-zero-plus2.dtb** (H3 version) device-tree binary. 
# Expansion Port
The Orange Pi Zero Plus 2 has a 26-pin, 0.1" unpopulated connector with several low-speed interfaces. It's marketed as Raspberry Pi-compatible.  
Table below is based on Xunlong's board schematic and [product][63159] page. 
2x13 Header   
---  
1 | _3.3V_ | 2 | _5V_  
3 | TWI0_SDA / PA12 / GPIO12  | 4 | _5V_  
5 | TWI0_SCK / PA11 / GPIO11  | 6 | _GND_  
7 | PWM1 / PA06 / GPIO6  | 8 | UART2_TX / PA00 / GPIO0   
9 | _GND_ | 10 | UART2_RX / PA01 / GPIO1   
11 | S-TWI-SCK / PL0 / GPIO352  | 12 | PD11 / GPIO107   
13 | S-TWI-SDA / PL1 / GPIO353  | 14 | _GND_  
15 | UART2_CTS / PA03 / GPIO3  | 16 | TWI1-SDA / PA19 / GPIO19   
17 | _3.3V_ | 18 | TWI1-SCK / PA18 / GPIO18   
19 | SPI1_MOSI / PA15 / GPIO15  | 20 | _GND_  
21 | SPI1_MISO / PA16 / GPIO16  | 22 | UART2_RTS / PA02 / GPIO2   
23 | SPI1_CLK / PA14 / GPIO14  | 24 | SPI1_CS / PA13 / GPIO13   
25 | _GND_ | 26 | PD14 / GPIO110   
  
The Orange Pi Zero Plus 2 has another 13-pin, 0.1" header with several low-speed interfaces. 
TODO: This table was taken from the Orange Pi Zero's wiki page as the Orange Pi Zero Plus 2 details are still . It's _probably_ the same for the Zero Plus 2 (the Xunlong's datasheet and product pages seem to agree). Use at your own risk. 
1x13 Header   
---  
1 | _5V_  
2 | _GND_  
3 | USB-DM2   
4 | USB-DP2   
5 | USB-DM3   
6 | USB-DP3   
7 | LINEOUTR   
8 | LINEOUTL   
9 | TV-OUT   
10 | MIC-BIAS   
11 | MIC1P   
12 | MIC1N   
13 | [CIR][63101]-RX   
# Tips, Tricks, Caveats
## Powering the board
Unlike most other Orange Pi boards, the Orange Pi Zero Plus 2 can be powered through the Micro USB jack (being a normal USB OTG port otherwise) or via one of the [Expansion Port][63160] pin headers (using 5V/GND pins). 
There is no power on/off switch or reboot switch on the board. 
## FEL Mode
The Orange Pi Zero Plus 2 runs the standard [Allwinner BootROM][63161] when the SoC starts up. There are no buttons or connectors to select FEL mode so the BootROM will only enter FEL mode if a special SD card is present or if there are no valid boot options. For example if there is no boot option on the SPI NOR chip and no SD card is present then plugging the board's micro-USB port into a USB port on a PC will show up as a FEL device. Using [Sunxi tools][63162] and issuing: 
[code] 
    $ sunxi-fel ver
    
[/code]
shows: 
[code] 
    AWUSBFEX soc=00001680(H3) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
    
[/code]
## Onboard eMMC
An 8GB onboard eMMC is present and supported by the Armbian image. 
Benchmark: iozone -e -I -a -s 100M -r 4k -r 16k -r 512k -r 1024k -r 16384k -i 0 -i 1 -i 2 
[code] 
                                                                 random    random
                 kB  reclen    write  rewrite    read    reread    read     write
             102400       4     5350     5923    12191    12233     9453     5861
             102400      16    17258    19735    28225    27445    24999    18945
             102400     512    36332    34508    59980    60008    59936    33483
             102400    1024    34079    35472    61459    61508    61546    33952
             102400   16384    36899    36954    67638    67631    67605    36413
    
[/code]
## LEDs
The board has two LEDs next to DRAM: 
  * A green LED, connected to PL10.
  * A red LED, connected to PA17.

## Camera
vip_dev0_power_en = PA08 
## USB header
[![][63163]][63164]
[][63165]
PC case USB port
To make a trivial adapter you can use "pc case usb port" but you will need to rearrange the pins: 
1 - 5V - red 2 - GND - black 3 - dm - white 4 - dp - green 
## JTAG
TODO 
# Adding a serial port
## Locating the UART
[![][63166]][63167]
[][63168]
Orange Pi Zero Plus 2 UART pinout
The UART pins are located next to unpopulated 26-pin header on the board. They are marked as _TX_ , _RX_ and _GND_ on the PCB with barely visible letters. Just attach some leads according to our [UART Howto][63169]. 
# Pictures
  * [![OPi Zero Plus 2 Top.jpg][63170]][63095]
  * [![OPi Zero Plus 2 Bottom.jpg][63171]][63172]

# Variants
  * Currently two variants of the Orange Pi Zero Plus 2 boards exist - one with H3 and the other with H5 SoC. Otherwise the boards seem identical.

# Also known as
# See also
  * opi0+2h3 schematics [File:ORANGE PI-ZERO-PLUS2 V1 0.pdf][63173]
  * [Xunlong Orange Pi site][63174]
  * [Official Github Repository][63175]
  * [Official Orange Pi Forums][63176]

## Manufacturer images
# References
