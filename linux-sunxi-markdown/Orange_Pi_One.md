# Xunlong Orange Pi One &amp; Lite

# Xunlong Orange Pi One & Lite
(Redirected from [Orange Pi One][42437])
 
Xunlong Orange Pi One & Lite  
---  
[![Orange Pi One Lite.jpg][42440]][42441]  
Manufacturer |  [OrangePi][42442]  
Dimensions |  69 _mm_ x 48 _mm_  
Release Date |  Jan (One) / May (Lite) 2016   
Website |  [Orange Pi One/Lite Product Pages][42443]  
Specifications   
SoC |  [H3][42444] @ 1.2 GHz   
DRAM |  512MiB DDR3 ([K4B4G1646D-BCK0][42445])   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive)  
or via GPIO header pins   
Features   
Video |  HDMI (HDCP, CEC)   
Audio |  HDMI   
Network |  10/100 Ethernet (One), RTL8189FTV WiFi (Lite)   
Storage |  µSD   
USB |  1 or 2 USB 2.0 Host, 1 µUSB 2.0 OTG   
Other |  TV-OUT through solder pads, [CIR][42446] and Microphone on Lite   
Headers |  3 pin UART, CSI, 40 pin GPIO   
_Orange Pi One_ and _Lite_ are [H3][42444] based development boards produced by [Xunlong][42447]. 
The _**One**_ is clearly [Orange Pi PC][42448]'s little/smaller sibling. Compared to the _PC_ the following is different: smaller size, 512MiB instead of 1GiB DRAM (still two DDR3L modules making use of the full 32 bit memory bandwidth), 2 USB host ports aren't exposed and the following is also missing: [CIR][42446] receiver, microphone and TRRS jack for Audio/CVBS video. 
The _**Lite**_ features RTL8189FTV WiFi (shipping with a small external antenna connected to the u.FL connector between the USB ports), saves the Ethernet port but regains one more USB port, [CIR][42446] receiver and microphone. 
Xunlong chose a different voltage regulator on these two boards that requires software adjustments to get dynamic voltage frequency scaling (dvfs) working. Apart from that Xunlong tried to keep both small boards as compatible as possible to the _PC_ so that all OS images for the _PC_ work with _One_ and _Lite_ with just two drawbacks: Non functional dvfs without fex file adjustments and no WiFi without new drivers on the _Lite_. 
## Contents
  * [1 Identification][42449]
  * [2 Sunxi support][42450]
    * [2.1 Current status][42451]
    * [2.2 Manual build][42452]
      * [2.2.1 U-Boot][42453]
        * [2.2.1.1 Mainline U-Boot][42454]
      * [2.2.2 Linux Kernel][42455]
        * [2.2.2.1 Sunxi/Legacy Kernel][42456]
        * [2.2.2.2 Mainline kernel][42457]
  * [3 Expansion Port][42458]
  * [4 Tips, Tricks, Caveats][42459]
    * [4.1 FEL mode][42460]
    * [4.2 Compatibility][42461]
    * [4.3 CPU clock speed limit][42462]
    * [4.4 DRAM clock speed limit][42463]
    * [4.5 DRAM clock speed limit (automated statistical analysis)][42464]
    * [4.6 LEDs][42465]
    * [4.7 Camera module][42466]
    * [4.8 HDMI to DVI converters][42467]
    * [4.9 Orientation of the GPIO header][42468]
    * [4.10 Adding ports/connectors that are missing][42469]
  * [5 Adding a serial port][42470]
    * [5.1 Locating the UART][42471]
  * [6 Pictures][42472]
    * [6.1 Orange Pi One][42473]
    * [6.2 Orange Pi Lite][42474]
  * [7 See also][42475]
    * [7.1 OS images][42476]
  * [8 References][42477]

# Identification
OPi One PCB has the following silkscreened on it: 
[code] 
    Orange Pi One V1.1
[/code]
Orange Pi Lite shows: 
[code] 
    Orange Pi Lite V1.1
[/code]
# Sunxi support
## Current status
The H3 SoC support has matured since its introduction in kernel 4.2. Most of the board functionality for boards such as Orange Pi One & Lite are available with current mainline kernels. Some features (hw accelerated crypto, hw spinlocks, and thermal) are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][42478]. In addition, legacy 3.4 kernels are available in various work-in-progress git branches. 
See the [Manual build][42452] section for more details. 
  

## Manual build
You can build things for yourself by following our [Manual build howto][42479] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_one** or **orangepi_lite** (supported since v2016.05/v2016.09) build target. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][42480]. 
The H3 boards can boot from [SD cards][42481], [eMMC][42482], [NAND][42483] or [SPI NOR][42484] flash (if available), and via [FEL][42485] using the OTG USB port. In U-Boot, loading the kernel is also supported from USB or ethernet (netboot). HDMI support in U-Boot is still WIP. 
### Linux Kernel
#### Sunxi/Legacy Kernel
The 3.4 kernel from the official [Allwinner's git repository][42486] [does not support H3][42487] yet. But it is possible to use one of the kernel forks, based on the [lichee H3 SDK tarball][42488]: 
  * [Siarhei Siamashka's branch '20151207-embedded-lima-memtester-h3'][42489]
  * [Yann Dirson's fork][42490] added a few more fixes and adopted most of
  * [Boris Lovosevic' great initial work][42491] on Allwinner's H3 kernel

Configure this kernel using **sun8i_h3_defconfig** , the rest is explained in the [kernel compilation guide][42492]. 
Use the .fex file for generating [script.bin][42493]. Armbian maintains a [bunch of 3.4.x patches][42494] for H3 devices. There you can also find the necessary patch set to support the new 8189FTV WiFi chip on the _Lite_. 
  
Since the manufacturer did not provide new fex files when Orange Pi One has been released in early 2016 you might want to use Armbian's (community developed) fex files: [orangepione.fex][42495] and [orangepilite.fex][42496] since they support the different voltage regulator on these boards, the new WiFi chip on the _Lite_ and implement community derived improved THS settings (dynamic voltage frequency scaling and optimized thermal/throttling settings -- look at the _dvfs_table_ and _cooler_table_ sections in the fex files above). 
When booting the legacy 3.4 kernel with the mainline U-Boot, add the following line to boot.cmd: 
[code] 
      setenv machid 1029
      setenv bootm_boot_mode sec
    
[/code]
Some other legacy kernel repositories: 
  * [3.4-lichee-based kernel][42497], based on work by [ssvb][42498] and [loboris][42499]
  * [Yocto support here][42500] glues together all the required parts to get this kernel to work with mainline u-boot, as well as accelerated X11/GLES support
  * [A newer H3 BSP variant][42501] appeared with tons of fixes which has been made available by FriendlyARM.
  * [A cleaned up fork][42502] has been adopted by Armbian project. On top of that Armbian maintains a bunch of [3.4.x patches for H3 devices][42494].

#### Mainline kernel
The mainline kernel has good support for the H3 SoC. Please refer to the [status matrix][42503] for a more detailed list of the development process, links to patches and links to kernel fork repositories. Minor drivers that are currently work-in-progress may require a) [third party patches][42504] (see also arm-linux mailing list) or b) a pre-patched distro (e.g. [Armbian][42505]). 
Repositories with H3 patches: 
  * [Ondřej Jirman's branch for H3 based orange Pi (kernel 4.19)][42506] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)
  * [Philipp Rossak's THS patches (in the sunxi-ths- branches)][42507]
  * [Corentin Labbe's HW Crypto and spinlock patches (in respective branches)][42508]

  
Use the **sun8i-h3-orangepi-one.dtb** or **sun8i-h3-orangepi-lite.dtb** device-tree binary. 
# Expansion Port
The Orange Pi One & Lite both have a Raspberry Pi model B+ compatible 40-pin, 0.1" connector with several low-speed interfaces. **Warning: The header's orientation on these 2 boards is 180°, please check 'pin 1' marking carefully (especially if you plan to insert power through GPIO header)**
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
Both boards will fail over to FEL mode if it doesn't detect a card present in the µSD slot. There is no dedicated FEL button. 
## Compatibility
Since Xunlong didn't provide new OS images with Orange Pi One's release users try to use images/settings for Orange Pi PC. While this seems to work and Ethernet and USB are functional on the _One_ the logs get flooded with "ARISC ERROR" messages due to a different voltage regulator ([full log][42509]): 
[code] 
    [ARISC ERROR] :message process error
    [ARISC ERROR] :message addr   : f004b840
    [ARISC ERROR] :message state  : 5
    [ARISC ERROR] :message attr   : 2
    [ARISC ERROR] :message type   : 30
    [ARISC ERROR] :message result : ff
    [ARISC WARING] :callback not install
    [cpu_freq] ERR:set cpu frequency to 1008MHz failed!
[/code]
On the _Orange Pi PC_ the [SY8106A][42510] is accessible through I2C and the H3's [AR100][42511] OpenRISC core tries to adjust the CPU core voltage (VDD_CPUX) this way. On _One_ and _Lite_ a different voltage regulator is used: the SY8113B ([datasheet][42512]) is a step-down converter that can adjust its output voltage driven by two resistors. [According to Xunlong staff][42513] on OPi One this is used to switch between 1.1V at 624 MHz and 1.3V at every cpufreq above. Users that looked a little bit closer discovered that the similar AX3833 is used on the first batch of boards instead (see Gallery and link to datasheet below). 
To get reliable performance/thermal behaviour with OS images that use legacy 3.4.x kernels adopted fex settings are needed. Please have a look in the aforementioned fex files from Armbian that implement this correctly. Same regarding WiFi: Please see above where to get the necessary patches to get RTL8189FTV up and running (the good news: since OpenELEC team who fixed the drivers relied on 8189es driver already ported to mainline the necessary fixes can be easily used to get WiFi working with kernel 4.x too) 
## CPU clock speed limit
Xunlong advertises both boards as being only capable of running at 'up to 1.2GHz'. Since the SY8113B/AX3833 voltage regulator should only be able to switch between 1.1V and 1.3V this would prevent clocking the SoC higher than 1200MHz according to the common comments in the FEX files from various H3 SDK variants: 
[code] 
    ; dvfs voltage-frequency table configuration
    ;
    ; pmuic_type:0:none, 1:gpio, 2:i2c
    ; pmu_gpio0: gpio config.
    ; pmu_levelx: 0~9999: voltage(mV), 10000~90000:gpio0 state. voltage form high to low.
    ;
    ; extremity_freq(Hz): cpu extremity frequency when run benckmark or demo apk
    ;                     1536MHz@1500mV with radiator, 1296MHz@1340mV without radiator
    ; max_freq: cpu maximum frequency, based on Hz, can not be more than 1200MHz
    ; min_freq: cpu minimum frequency, based on Hz, can not be less than 60MHz
    ;
    ; LV_count: count of LV_freq/LV_volt, must be < 16
    ;
    ; LV1: core vdd is 1.50v if cpu frequency is (1296Mhz,  1536Mhz]
    ; LV2: core vdd is 1.34v if cpu frequency is (1200Mhz,  1296Mhz]
    ; LV3: core vdd is 1.32v if cpu frequency is (1008Mhz,  1200Mhz]
    ; LV4: core vdd is 1.20v if cpu frequency is (816Mhz,   1008Mhz]
    ; LV5: core vdd is 1.10v if cpu frequency is (648Mhz,    816Mhz]
    ; LV6: core vdd is 1.04v if cpu frequency is (0Mhz,      648Mhz]
    ; LV7: core vdd is 1.04v if cpu frequency is (0Mhz,      648Mhz]
    ; LV8: core vdd is 1.04v if cpu frequency is (0Mhz,      648Mhz]
    
[/code]
## DRAM clock speed limit
DRAM is clocked at **672 MHz** by the hardware vendor. But the reliability still needs to be verified. One of the ways of doing reliability tests may be <https://github.com/ssvb/lima-memtester/releases/tag/20151207-orange-pi-pc-fel-test> (developed for Orange Pi PC). An adoption of this using a fex file suited for Orange Pi One's/Lite's different voltage regulator is available [here][42514] (md5sum: e600db41f94446bb77224223fc1dc2a0 fel-boot-lima-memtester-on-orange-pi-one-v3.tgz). Use the _fel-boot-lima-memtester-on-orange-pi-one_ script inside to test both boards. 
Hardware  | Diagnostic software  | lima-memtester passes (survives until the red LED)  | lima-memtester fails  | Notes   
---|---|---|---|---  
[User:Beda][42515]'s Orange Pi One | fel-boot-lima-memtester-on-orange-pi-one-v3.tar.gz | 744 MHz | 768 MHz | **No heatsink**. 768 MHz fails after running for approx. 30 seconds   
[User:Tkaiser][42516]'s Orange Pi One | fel-boot-lima-memtester-on-orange-pi-**one** -v3.tar.gz | 744 MHz | 768 MHz | **Now with heatsink**. 768 MHz fails after running for approx. 20 seconds (similar to fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz)   
[User:Michal][42517]'s Orange Pi One #1 | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 672 MHz | 696 MHz | **No heatsink**. 696 MHz fails after running for ~5 minutes   
[User:Michal][42517]'s Orange Pi One #2 | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 696 MHz | 720 MHz | **No heatsink**. 720 MHz fails after running for ~2 minutes   
[User:Rreignier][42518]'s Orange Pi One | fel-boot-lima-memtester-on-orange-**one** -v3.tar.gz | 696 MHz | 720 MHz | **No heatsink**. 720 MHz fails after running for ~1 minute (similar to fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz)   
[User:Emsi88][42519]'s Orange Pi One | fel-boot-lima-memtester-on-orange-**one** -v3.tar.gz | 696 MHz | 720 MHz | **With small heatsink**. 720MHz fails after ~2hours , 744MHz fails after ~25sec.   
[User:Dvl36][42520]'s Orange Pi One | fel-boot-lima-memtester-on-orange-**one** -v3.tar.gz | 672 MHz | 696 MHz | **No heatsink**. 696 MHz fails after running for ~5 minutes   
[User:Tkaiser][42516]'s Orange Pi Lite | fel-boot-lima-memtester-on-orange-pi-pc-v3.tar.gz | 648 MHz | 672 MHz | **Cheap heatsink**. 672 MHz fails after running for approx. 3 minutes   
**We need still more test results in the table above in order to have more accurate statistics and finally pick a safe default DRAM clock speed for U-Boot. Preferably there should be at least 10 entries in the table (more is always better). And there are no "good" or "bad" test results. Even if your result looks very similar to the already reported results from the other people, please still add yours to the table! Because if people don't feel like reporting their "boring" results, then "interesting" outliers will unfortunately skew the statistics. Thanks!**
## DRAM clock speed limit (automated statistical analysis)
Below is an intermediate analysis of the currently reported results, using the [lima-memtester-genchart][42521] script (run the script using this page URL as the command line argument). Assuming that the [Gaussian distribution][42522] is a good approximation, try to predict what percentage of boards is expected to pass the lima-memetser test at different DRAM clock frequencies. The [lima-memtester][42523] page provides more information. 
Updating the analysis report:
[code]
    wget https://raw.githubusercontent.com/ssvb/lima-memtester/master/lima-memtester-genchart
    ruby lima-memtester-genchart https://linux-sunxi.org/Xunlong_Orange_Pi_One
    # copy/paste the script output into the linux-sunxi wiki
    
[/code]
DRAM clock speed  | Percentage of boards failing the lima-memtester test  | Theoretical pessimistic upper bound of the failure percentage using Chebyshev's inequality for lower semivariance [[1]][42524] | Histogram   
---|---|---|---  
Experimental results  | Theoretical prediction (assuming Gaussian distribution) [[2]][42525]  
504 MHz | 0.00 % (0/8) | 0.00 % | 1.19 % |   
528 MHz | 0.00 % (0/8) | 0.00 % | 1.52 % |   
552 MHz | 0.00 % (0/8) | 0.00 % | 2.03 % |   
576 MHz | 0.00 % (0/8) | 0.01 % | 2.83 % |   
600 MHz | 0.00 % (0/8) | 0.07 % | 4.23 % |   
624 MHz | 0.00 % (0/8) | 0.67 % | 7.00 % |   
648 MHz | 0.00 % (0/8) | 3.85 % | 13.71 % |   
672 MHz | 12.50 % (1/8) | 14.44 % | 38.10 % | *   
696 MHz | 37.50 % (3/8) | 36.18 % | 100.00 % | **   
720 MHz | 75.00 % (6/8) | 63.82 % | 100.00 % | ***   
744 MHz | 75.00 % (6/8) | 85.56 % | 100.00 % |   
768 MHz | 100.00 % (8/8) | 96.15 % | 100.00 % | **   
792 MHz | 100.00 % (8/8) | 99.33 % | 100.00 % |   
  1. [↑][42526] If nothing is known about the distribution of samples, then at least [Chebyshev's inequality][42527] can be used to get a rough idea about the probabilities of encountering reliability problems at different DRAM clock speeds. But this method is _very conservative_ and substantially overestimates probabilities (being too generic has its price).
  2. [↑][42528] We can assume that the [Gaussian distribution][42522] is a good approximation for our experimental data, calculate theoretical probabilities and do an [exact test of goodness-of-fit][42529] to see if the experimental data does not contradict with the theory. There is a nice [XNomial][42530] library for R, which can do the job:
[code]P value  (LLR)  =  0.5308
             P value (Prob)  =  0.603
             P value (Chisq) =  0.698
         
[/code]
If the [p-values][42531] listed above happen to be too low (less than 0.05) and reject our [null hypothesis][42532] about having the Gaussian distribution, then Chebyshev's inequality estimates still can be used. 

## LEDs
The boards have two LEDs next to the 40 pin GPIO header: 
  * A red LED, connected to the PA15 pin.
  * A green LED, connected to the PL10 pin.

When using kernel 3.4 with Xunlong's or loboris' settings then the LEDs can only be switched on/off. By changing the definition in the fex files (see [patch][42533] or [the aforementioned fex files for the One/Lite OpenElec and Armbian use][42456]) both LEDs can be used the usual way (using different triggers and so on) 
## Camera module
Xunlong sells also a cheap 2MP camera (an attempt to fix the driver's limited resolutions can be found [here][42534]). Unlike Orange Pi Plus/2 that can directly connect to the camera module for the Orange Pi PC/One/Lite an 'expansion board' is needed (see gallery below). If you order from Xunlong simply tell them that you need the camera for Orange Pi One or Lite and they ship camera together with the small board. 
## HDMI to DVI converters
When trying to use HDMI to DVI converters with Allwinner's 3.4.x kernel for H3/R16/A83T/H8/R58 a small fix has to be applied. The fex file has to be modified (and converted back to script.bin afterwards) so that the following has been added to the _[hdmi_para]_ section: 
[code] 
    hdcp_enable = 0
    hdmi_cts_compatibility = 1
[/code]
## Orientation of the GPIO header
Due to the position of USB and/or Ethernet jacks Xunlong chose to rotate the 40 pin GPIO connector by 180° so RPi HATs can still be used but will project over the board in the opposite direction than intended. Keep this also in mind when you want to power the board through GPIO pins 2/4/6 (2/4 being connected directly with DC-IN and 6 being GND) 
## Adding ports/connectors that are missing
On the _One_ the two missing USB ports, analog audio out, microphone, [CIR][42446] receiver and TV out are still [available for people with soldering skills][42535]. Have a look into the gallery below or in the aforementioned thread for details. Same applies to the one missing USB port, analog audio out and TV out on the _Lite_
# Adding a serial port
## Locating the UART
The UART pins are located next to Ethernet / USB jack on the boards. They are marked as _TX_ , _RX_ and _GND_ on the PCB. Just attach some leads according to our [UART Howto][42536]. 
[![Orange Pi One UART.jpg][42537]][42538]
[][42539]
# Pictures
## Orange Pi One
  * [![Orange Pi One Top.jpg][42540]][42541]
  * [![Orange Pi One Bottom.jpg][42542]][42543]
  * [![Orange Pi One 1.jpg][42544]][42545]
  * [![Orange Pi One 2.jpg][42546]][42547]
  * [![Orange Pi One 3.jpg][42548]][42549]
  * [![Orange Pi One 4.jpg][42550]][42551]
  * [![Orange Pi One Heatsink.jpg][42552]][42553]
  * [![Orange Pi One with Camera2.jpg][42554]][42555]
  * [![Orange Pi One with Camera.jpg][42556]][42557]
  * [![Orange Pi One AX3833 instead of SY8113B.jpg][42558]][42559]
  * [![Orange Pi One Adding Ports 1.jpg][42560]][42561]
  * [![Orange Pi One Adding Ports 2.jpg][42562]][42563]
  * [![Orange Pi One IR schema.jpg][42564]][42565]

## Orange Pi Lite
Please note that the boards are sold without any heatsink. This is just the [tester's standard heatsink for all H3 boards][42566] now. 
  * [![Orange Pi Lite top.jpg][42567]][42568]
  * [![Orange Pi Lite bottom.jpg][42569]][42570]
  * [![Orange Pi Lite 1.jpg][42571]][42572]
  * [![Orange Pi Lite 2.jpg][42573]][42574]
  * [![Orange Pi Lite 3.jpg][42575]][42576]
  * [![Orange Pi Lite 4.jpg][42577]][42578]

# See also
  * [Xunlong Orange Pi site][42579]
  * [Official Github Repository][42580].
  * [Official Orange Pi Form][42581].
  * [H3_Manual_build_howto][42582]
  * Opi One Schematic v1.1: [File:ORANGE PI-ONE-V1 1.pdf][42583]
  * Opi Lite Schematic v1.1: [File:Orange pi-lite-v1 1.pdf][42584]
  * AX3833 datasheet: [File:AX3833.pdf][42585]

## OS images
At the moment only OS images relying on Allwinner's 3.4.x BSP kernel are available for the boards. Most of them suffer from wrong settings for the different voltage regulator used on _One_ and _Lite_ , the only known exceptions are currently the [Armbian images][42586] and [OpenELEC][42587] for both boards and WiFi support for the _Lite_. Xunlong also released a [new Android image for the _Lite_][42588] that should support the new WiFi chip and also work with the _One_ (just based on assumptions and not tested). 
In case you want to use other OS images with _One_ and _Lite_ be prepared to adjust fex settings to get thermal/performance settings right, that you need a kernel patch for the new WiFi module on the _Lite_ and that all OS images except OpenELEC/Armbian use a horribly outdated kernel version 3.4.39 missing tons of fixes. 
# References
