# Xunlong Orange Pi Plus
Xunlong Orange Pi Plus  
---  
[![Xunlong OrangePi Plus.jpg][62022]][62023]  
Manufacturer |  [OrangePi][62024]  
Dimensions |  108 _mm_ x 60 _mm_  
Release Date |  February 2015   
Website |  [Orange Pi Plus Product Page][62025]  
Specifications   
SoC |  [H3][62026] @ 1.3GHz   
DRAM |  1GiB DDR3 @ 672MHz ([K4B4G1646Q-HYK0][62027])   
NAND |  8GB EMMC Flash   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive)   
Features   
Video |  HDMI (HDCP, CEC), CVBS   
Audio |  3.5 mm Jack, HDMI, Microphone   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][62028]), WiFi 802.11 b/g/n ([Realtek RTL8189ETV][62029])   
Storage |  µSD (max 64GB), SATA 2.0 (via GL830 USB-to-SATA bridge, +5V power on JST XH 2.5mm connector)   
USB |  4 USB 2.0 Host (via FE1.1s hub), 1 USB 2.0 OTG   
Other |  [CIR][62030]  
Headers |  3 pin UART, CSI, 40 pin GPIO   
Orange Pi Plus is a [H3][62026] based development board produced by [Xunlong][62031], released in February 2015. It comes with onboard 8 GB eMMC flash, gigabit Ethernet, and 802.11 b/g/n WiFi, Video Outputs (HDMI with CEC, CVBS, simultaneous output to both) and a Raspberry Pi A+/B+ style 40 pin GPIO header. An upgraded version [Orange Pi Plus 2][62032] with twice the RAM and onboard flash was later released. 
## Contents
  * [1 Identification][62033]
  * [2 Sunxi support][62034]
    * [2.1 Current status][62035]
    * [2.2 Manual build][62036]
      * [2.2.1 U-Boot][62037]
        * [2.2.1.1 Mainline U-Boot][62038]
      * [2.2.2 Linux Kernel][62039]
        * [2.2.2.1 Sunxi/Legacy Kernel][62040]
        * [2.2.2.2 Mainline kernel][62041]
  * [3 Expansion Port][62042]
  * [4 Tips, Tricks, Caveats][62043]
    * [4.1 FEL mode][62044]
    * [4.2 LEDs][62045]
    * [4.3 SATA][62046]
    * [4.4 DRAM clock speed limit][62047]
    * [4.5 DRAM clock speed limit (automated statistical analysis)][62048]
  * [5 Adding a serial port][62049]
    * [5.1 Locating the UART][62050]
  * [6 Pictures][62051]
  * [7 Variants][62052]
  * [8 Also known as][62053]
  * [9 See also][62054]
    * [9.1 Manufacturer images][62055]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi Plus
[/code]
# Sunxi support
## Current status
The H3 SoC support has matured since its introduction in kernel 4.2. Most of the board functionality for boards such as Orange Pi Plus are available with current mainline kernels. Some features (hw accelerated crypto, hw spinlocks, and thermal) are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][62056]. In addition, legacy 3.4 kernels are available in various work-in-progress git branches. 
See the [Manual build][62036] section for more details. 
  

## Manual build
You can build things for yourself by following our [Manual build howto][62057] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_plus** (supported since v2016.01) build target. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][62058]. 
The H3 boards can boot from [SD cards][62059], [eMMC][62060], [NAND][62061] or [SPI NOR][62062] flash (if available), and via [FEL][62063] using the OTG USB port. In U-Boot, loading the kernel is also supported from USB or ethernet (netboot). HDMI support in U-Boot is still WIP. 
### Linux Kernel
#### Sunxi/Legacy Kernel
The 3.4 kernel from the official [Allwinner's git repository][62064] [does not support H3][62065] yet. But it is possible to use one of the kernel forks, based on the [lichee H3 SDK tarball][62066]: 
  * [Siarhei Siamashka's branch '20151207-embedded-lima-memtester-h3'][62067]
  * [Yann Dirson's fork][62068] added a few more fixes and adopted most of
  * [Boris Lovosevic' great initial work][62069] on Allwinner's H3 kernel

Configure this kernel using **sun8i_h3_defconfig** , the rest is explained in the [kernel compilation guide][62070]. 
Use the .fex file for generating [script.bin][62071]. 
  
When booting the legacy 3.4 kernel with the mainline U-Boot, add the following line to boot.cmd: 
[code] 
      setenv machid 1029
      setenv bootm_boot_mode sec
    
[/code]
Some other legacy kernel repositories: 
  * [3.4-lichee-based kernel][62072], based on work by [ssvb][62073] and [loboris][62074]
  * [Yocto support here][62075] glues together all the required parts to get this kernel to work with mainline u-boot, as well as accelerated X11/GLES support
  * [A newer H3 BSP variant][62076] appeared with tons of fixes which has been made available by FriendlyARM.
  * [A cleaned up fork][62077] has been adopted by Armbian project. On top of that Armbian maintains a bunch of [3.4.x patches for H3 devices][62078].

#### Mainline kernel
The mainline kernel has good support for the H3 SoC. Please refer to the [status matrix][62079] for a more detailed list of the development process, links to patches and links to kernel fork repositories. Minor drivers that are currently work-in-progress may require a) [third party patches][62080] (see also arm-linux mailing list) or b) a pre-patched distro (e.g. [Armbian][62081]). 
Repositories with H3 patches: 
  * [Ondřej Jirman's branch for H3 based orange Pi (kernel 4.19)][62082] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)
  * [Philipp Rossak's THS patches (in the sunxi-ths- branches)][62083]
  * [Corentin Labbe's HW Crypto and spinlock patches (in respective branches)][62084]

  
Use the **sun8i-h3-orangepi-plus.dtb** device-tree binary. 
# Expansion Port
The Orange Pi Plus has a Raspberry Pi model B+ compatible 40-pin, 0.1" connector with several low-speed interfaces. 
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
The button marked _SW3_ , located between the HDMI and SATA, triggers [ FEL mode][62085] when pressed during boot. (_SW3_ pulls the H3 _BOOTSEL_ pin to low level.) 
To [ verify][62086] you have successfully entered FEL mode, check the output of `fel version`. For the Orange Pi Plus, it should look like: 
[code] 
    AWUSBFEX soc=00001680(unknown) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
[/code]
## LEDs
For those with a transparent case (or no case at all) the Orange Pi Plus's LED activity is good. The **red** power LED (_D7_) can be turned off. 
## SATA
Be aware that the H3 SoC used on the Orange Pi Plus isn't SATA capable and therefore the SATA port is provided by a slow USB-to-SATA-bridge (especially write speeds are substandard and [do not exceed 15 MB/s][62087]). This means you can neither expect [SATA performance][62088] nor full SATA functionality. While the used GL830 bridge supports [S.M.A.R.T.][62089] attributes it does not support S.M.A.R.T. status notification (overall health indicator of the disk – instead of _PASSED_ or _FAILED_ you will only get _SMART Status not supported: Incomplete response, ATA output registers missing_). 
If you wish to connect a SATA drive (2.5" mobile harddisk or SSD) to the Orange Pi Plus: Make sure your power supply is connected to the "DC-IN" port, and can deliver sufficient current (e.g. 5V/2000mA). Using the OTG port or an inadequate power supply might result in your board not being working. You should also note that the board's SATA-power connector uses the same polarity as other Orange or Banana Pis. Therefore cable kits from CubieTech and LinkSprite that use the same jack are incompatible due to inverted polarity. 
## DRAM clock speed limit
DRAM is clocked at **672 MHz** by the hardware vendor. But the reliability still needs to be verified. One of the ways of doing reliability tests may be <https://github.com/ssvb/lima-memtester/releases/tag/20151207-orange-pi-pc-fel-test> (it checks the Orange Pi PC DRAM setup in the current mainline U-Boot v2016.01-rc2 + [a bugfix][62090]). 
NOTE: While this test image was made for the Orange Pi PC, it also runs on the Orange Pi Plus. 
Hardware  | Diagnostic software  | lima-memtester passes (survives until the red LED)  | lima-memtester fails  | Notes   
---|---|---|---|---  
[User:Camh][62091]'s Orange Pi Plus 1 | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 720 MHz | 744 MHz | **Heatsink (35mmx25mm) covering SoC and RAM**. 744MHz only failed when left running overnight. It made it to the red LED.   
[User:Camh][62091]'s Orange Pi Plus 2 | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 696 MHz | 720 MHz | **Heatsink (35mmx25mm) covering SoC and RAM**. 720MHz failed in < 30s.   
[User:Camh][62091]'s Orange Pi Plus 3 | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 720 MHz | 744 MHz | **Heatsink (35mmx25mm) covering SoC and RAM**. 744MHz failed in < 30s.   
[User:Camh][62091]'s Orange Pi Plus 4 | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 672 MHz | 696 MHz | **Heatsink (35mmx25mm) covering SoC and RAM**. 696MHz failed in > 4 hrs. It made it to the red LED.   
[User:Jemk][62092]'s Orange Pi Plus | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 768 MHz | 792 MHz | **Small Heatsink (15mmx15mm)**. 792 MHz fails in SPL, but 768 MHz passes overnight run. I don't know if these results can be trusted.   
[User:Rellla][62093]'s Orange Pi Plus | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 720 MHz | 744 MHz | **No Heatsink**. Up to 720 MHz passed until red led.   
[User:von fritz][62094]'s Orange Pi Plus | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 768 MHz | 792 MHz | **Heatsink (20mmx20mm)**. Up to 768 MHz passed until red led, 792 MHz fails with libusb usb_bulk_send error -9.   
See the [Orange Pi PC DRAM clock speed limit][62095] for how to perform an analysis of these results. 
## DRAM clock speed limit (automated statistical analysis)
Updating the analysis report:
[code]
    wget https://raw.githubusercontent.com/ssvb/lima-memtester/master/lima-memtester-genchart
    ruby lima-memtester-genchart https://linux-sunxi.org/Xunlong_Orange_Pi_Plus
    # copy/paste the script output into the linux-sunxi wiki
    
[/code]
DRAM clock speed  | Percentage of boards failing the lima-memtester test  | Theoretical pessimistic upper bound of the failure percentage using Chebyshev's inequality for lower semivariance [[1]][62096] | Histogram   
---|---|---|---  
Experimental results  | Theoretical prediction (assuming Gaussian distribution) [[2]][62097]  
528 MHz | 0.00 % (0/7) | 0.00 % | 1.33 % |   
552 MHz | 0.00 % (0/7) | 0.00 % | 1.70 % |   
576 MHz | 0.00 % (0/7) | 0.00 % | 2.25 % |   
600 MHz | 0.00 % (0/7) | 0.01 % | 3.12 % |   
624 MHz | 0.00 % (0/7) | 0.08 % | 4.61 % |   
648 MHz | 0.00 % (0/7) | 0.64 % | 7.48 % |   
672 MHz | 0.00 % (0/7) | 3.55 % | 14.22 % |   
696 MHz | 14.29 % (1/7) | 13.09 % | 36.80 % | *   
720 MHz | 28.57 % (2/7) | 33.03 % | 100.00 % | *   
744 MHz | 71.43 % (5/7) | 59.64 % | 100.00 % | ***   
768 MHz | 71.43 % (5/7) | 82.31 % | 100.00 % |   
792 MHz | 100.00 % (7/7) | 94.63 % | 100.00 % | **   
816 MHz | 100.00 % (7/7) | 98.91 % | 100.00 % |   
840 MHz | 100.00 % (7/7) | 99.85 % | 100.00 % |   
  1. [↑][62098] If nothing is known about the distribution of samples, then at least [Chebyshev's inequality][62099] can be used to get a rough idea about the probabilities of encountering reliability problems at different DRAM clock speeds. But this method is _very conservative_ and substantially overestimates probabilities (being too generic has its price).
  2. [↑][62100] We can assume that the [Gaussian distribution][62101] is a good approximation for our experimental data, calculate theoretical probabilities and do an [exact test of goodness-of-fit][62102] to see if the experimental data does not contradict with the theory. There is a nice [XNomial][62103] library for R, which can do the job:
[code]P value  (LLR)  =  0.5425
             P value (Prob)  =  0.5506
             P value (Chisq) =  0.6407
         
[/code]
If the [p-values][62104] listed above happen to be too low (less than 0.05) and reject our [null hypothesis][62105] about having the Gaussian distribution, then Chebyshev's inequality estimates still can be used. 

# Adding a serial port
TODO: The section is mostly a copy&paste from the "Banana Pi" page. Some of it may be incorrect, or might not apply to this device. Please review / rework the information, and remove this reminder when done.
While the GPIO pinout of the Orange Pi Plus is designed to be compatible to the Raspberry Pi, it's important to notice subtle differences in the serial ports. The Orange Pi Plus has some additional pins that already provide two more serial ports. 
The default serial port **/dev/ttyS0** , used for (bootstrap) debugging and the serial console, is located at J11 - refer to the picture and instructions below. The Raspberry's "original" serial port on GPIO 14 and 15 (CON3, pins 8 and 10) can usually be accessed as **/dev/ttyS2** on the Orange Pi Plus. J12 also provides another serial port on pins 4 (_RX_) and 6 (_TX_), which should map to **/dev/ttyS3**. 
_Note:_ The actual mapping between physical pins, UART numbers and/or device names may depend on the specific kernel and [ configuration][62106] used. If in doubt, check the boot messages: `dmesg | grep -i uart`
[![][62107]][62108]
[][62109]
UART pads
## Locating the UART
The UART pins are located between MIC and audio input of the board. They are marked as _TX_ , _RX_ and _GND_ on the PCB. Just attach some leads according to our [UART Howto][62110]. 
# Pictures
  * [![Xunlong OrangePi Plus front.jpg][62111]][62112]
  * [![Xunlong OrangePi Plus back.jpg][62113]][62114]
  * [![Xunlong Orange Pi Plus side d.jpg][62115]][62116]
  * [![Xunlong Orange Pi Plus side u.jpg][62117]][62118]
  * [![Xunlong Orange Pi Plus side l.jpg][62119]][62120]
  * [![Xunlong Orange Pi Plus side r.jpg][62121]][62122]

# Variants
  * The original [Orange Pi][62123] was released in November 2014. The Orange Pi features a standard TF card slot and a 26 pin GPIO connector (similar to the Raspberry Pi A/B).
  * An upgraded version [Orange Pi Plus 2][62032] with twice the RAM and onboard flash was later released.

# Also known as
# See also
There are several websites about Orange Pi Plus and claiming to support it. It has to be clarified, what is "official" and who is behind this sites. 
  * [Xunlong Orange Pi site][62025]
  * ["Official" Github Repository][62124].
  * ["Official" Orange Pi Form][62125].
  * [H3_Manual_build_howto][62126]

## Manufacturer images
A various amount of [prebuilt images][62127] is provided via OrangePi's Website.
