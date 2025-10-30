# Xunlong Orange Pi Zero Plus
(Redirected from [Orange Pi Zero Plus][43532])
 
Xunlong Orange Pi Zero Plus  
---  
[![OPi Zero Plus Small.jpg][43535]][43536]  
Manufacturer |  [OrangePi][43537]  
Dimensions |  46 _mm_ x 48 _mm_  
Release Date |  October 2017   
Website |  [Orange Pi Zero Plus Product Page][43538]  
Specifications   
SoC |  [H5][43539] @ 1.2 GHz   
DRAM |  512 MiB DDR3   
Power |  DC 5V DC-IN via µUSB or pin headers   
Features   
Video |  CVBS (on pin headers)   
Audio |  microphone, stereo line-out on pin headers   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][43540]), WiFi 802.11 b/g/n (Realtek RTL8189FTV)   
Storage |  µSD, 16Mb SPI NOR Flash on board   
USB |  1 USB 2.0 Host, 1 USB 2.0 OTG, 2 x USB 2.0 on pin headers   
Other |  [CIR][43541] on pin headers   
Headers |  3 pin UART, 26 + 13 pin GPIO   
The Xunlong Orange Pi Zero Plus is a small form factor board produced by [Xunlong][43542]. It bears resemblance to [Xunlong Orange Pi Zero][43543]. The Plus version differs from the original by having the H5 SoC instead of H3, gigabit ethernet support (Realtek RTL8211E), and WiFi 802.11 b/g/n provided with RTL8189FTV instead of XR819. The memory options are limited to 512MB of DDR3. 
## Contents
  * [1 Identification][43544]
  * [2 Sunxi support][43545]
    * [2.1 Current status][43546]
    * [2.2 BSP][43547]
    * [2.3 Manual build][43548]
      * [2.3.1 U-Boot][43549]
        * [2.3.1.1 Mainline U-Boot][43550]
      * [2.3.2 Linux Kernel][43551]
        * [2.3.2.1 Sunxi/Legacy Kernel][43552]
        * [2.3.2.2 Mainline kernel][43553]
  * [3 Expansion Port][43554]
  * [4 Tips, Tricks, Caveats][43555]
    * [4.1 FEL Mode][43556]
    * [4.2 LEDs][43557]
    * [4.3 Voltage regulators][43558]
    * [4.4 DRAM][43559]
    * [4.5 USB][43560]
  * [5 Adding a serial port][43561]
    * [5.1 Locating the UART][43562]
  * [6 Pictures][43563]
  * [7 See also][43564]
    * [7.1 Manufacturer images][43565]
  * [8 References][43566]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi Zero plus V1.1
[/code]
# Sunxi support
## Current status
The H5 SoC support has matured since its introduction in kernel 4.12. Most of the board functionality for boards such as Orange Pi Zero Plus, including 3D graphics, hardware accelerated video and crypto, and DVFS are available with current mainline kernels. Only a very few minor features are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][43567]. 
See the [Manual build][43548] section for more details. 
  

## BSP
There are some somewhat abandoned 3.10 BSP code drops available in 'OrangePiLibra' and FriendlyELEC's github repos. Check the [orangepi-xunlong][43568] and [OrangePiLibra][43569] repositories in case of interest. 
It seems no device settings are contained and the BSP is broken anyway at least with regard to voltage regulation (that's also the reason vendor OS images seem to be limited to 1008 MHz since at this cpufreq those Orange Pi do not immediately crash with BSP kernel). 
## Manual build
You can build things for yourself by following our [Manual build howto][43570] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_zero_plus_defconfig** (supported since v2018.07) build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
The H5 SoC has support in the [mainline kernels][43571]. 
The development process, links to patches and links to kernel fork repositories are listed on the [ Linux mainlining effort][43571] page. Patches can also be found from the arm-linux mailing list. 
Repositories with H5 patches: 
  * [Ondřej Jirman's branch for H5 based orange Pi (kernel 4.19)][43572] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)

  
Use the **sun50i-h5-orangepi-zero-plus.dtb** device-tree binary. 
# Expansion Port
The Orange Pi Zero Plus has the usual 26-pin, 0.1" unpopulated connector with several low-speed interfaces. 
2x13 Header   
---  
1 | _3.3V_ | 2 | _5V_  
3 | TWI0_SDA / PA12 / GPIO12  | 4 | _5V_  
5 | TWI0_SCK / PA11 / GPIO11  | 6 | _GND_  
7 | PWM1 / PA06 / GPIO6  | 8 | UART1_TX / PG06 / GPIO198   
9 | _GND_ | 10 | UART1_RX / PG07 / GPIO199   
11 | UART2_RX / PA01 / GPIO1  | 12 | SIM_CLK/PA_EINT7 / PA07 / GPIO7   
13 | UART2_TX / PA00 / GPIO0  | 14 | _GND_  
15 | UART2_CTS / PA03 / GPIO3  | 16 | TWI1-SDA / PA19 / GPIO19   
17 | _3.3V_ | 18 | TWI1-SCK / PA18 / GPIO18   
19 | SPI1_MOSI / PA15 / GPIO15  | 20 | _GND_  
21 | SPI1_MISO / PA16 / GPIO16  | 22 | UART2_RTS / PA02 / GPIO2   
23 | SPI1_CLK / PA14 / GPIO14  | 24 | SPI1_CS / PA13 / GPIO13   
25 | _GND_ | 26 | SIM_DET/PA_EINT10 / PA10 / GPIO10   
The board has another 13-pin, 0.1" header with several low-speed interfaces. 
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
13 | [CIR][43541]-RX   
A cheap ['Expansion board'][43573] for this connector is available exposing all interfaces (2 x USB, [CIR][43541] receiver, microphone and combined AV TRRS jack) and can be ordered together with the board on Aliexpress. **Attention:** Expect problems when using the Expansion board to connect more USB devices when you want to power the board through the Micro USB connector ([known to cause all sorts of troubles][43574]). Voltage drops affecting stability are likely to happen so better think about providing power through 5V/GND pins on the 26 pin header in this case. 
The [NAS Expansion board][43575] is also a great companion transforming the 2 USB2 ports on the 13 pin header into either SATA ports or exposing them to the outside just like the above Expansion board is doing. For full USB/UAS performance you might need to [upgrade the firmware of the used JMS578 SATA bridges][43576]. 
# Tips, Tricks, Caveats
## FEL Mode
The Orange Pi Zero Plus runs the standard [Allwinner BootROM][43577] when the SoC starts up. There are no buttons or connectors to select FEL mode so the BootROM will only enter FEL mode if a special SD card is present or if there are no valid boot options. For example if there is no boot option on the SPI NOR chip and no SD card is present then plugging the board's micro-USB port into a USB port on a PC will show up as a FEL device. Using [Sunxi tools][43578] and issuing: 
[code] 
    $ sunxi-fel ver
    
[/code]
shows: 
[code] 
    AWUSBFEX soc=00001680(H3) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
    
[/code]
## LEDs
The board has two LEDs next to DRAM: 
  * A red LED, connected to the PA17 pin.
  * A green LED, connected to the PL10 pin.

## Voltage regulators
There's a SY8113B voltage regulator on the board able to switch VDD_CPUX between 1.1V and 1.3V and toggled by PL06 pin. This allows stable operation at 816MHz @ 1.1V (based on Allwinner BSP comments and most probably a little bit higher) and 1200 MHz @ 1.3V. 
## DRAM
The vendor OS images clock the DRAM more or less by accident with 624 MHz (_/sys/devices/1c62000.dramfreq/devfreq/dramfreq/cur_freq_ reads _624000_) but these images seem to use settings for Orange Pi PC2 without any adjustments for the device in question (16-bit single bank DRAM config) so it can be expected that this device when settings are submitted upstream will get the usual _CONFIG_DRAM_CLK=672_ to repeat the usual instability mess we all love so much. 
As a reference some [tinymembench][43579] numbers all with 1008 MHz cpufreq: 
  * [BSP u-boot and dramfreq driver, DRAM clocked with 624 MHz since BSP default][43580] (**not** 672 MHz as can be read in the .dtb!)
  * [Mainline u-boot 2017.09 and _CONFIG_DRAM_CLK=624_][43581]
  * [Mainline u-boot 2017.09 and _CONFIG_DRAM_CLK=408_][43582]

## USB
The one USB host port exposed as type A receptacle is usb1. Both usb2 and usb3 are available via solder holes. USB OTG available through Micro USB. 
# Adding a serial port
## Locating the UART
The UART pins are located next to Ethernet jack on the board. They are marked as _TX_ , _RX_ and _GND_ on the PCB. Just attach some leads according to our [UART Howto][43583]. 
# Pictures
  * [![OPi Zero Plus Top.jpg][43584]][43585]
  * [![OPi Zero Plus Bottom.jpg][43586]][43587]
  * [![OPi Zero Plus 1.jpg][43588]][43589]
  * [![OPi Zero Plus 2.jpg][43590]][43591]
  * [![OPi Zero Plus 3.jpg][43592]][43593]
  * [![OPi Zero Plus 4.jpg][43594]][43595]

# See also
  * [Xunlong Orange Pi site][43596]
  * [Official Github Repository][43597].
  * [Official Orange Pi Forums][43598].
  * [Orange Pi Zero Plus Schematic 1.0][43599]

## Manufacturer images
  * [Official OS images][43600]

# References
