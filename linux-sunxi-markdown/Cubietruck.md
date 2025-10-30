# Cubietech Cubietruck
(Redirected from [Cubietruck][15529])
 
Cubietech Cubietruck  
---  
[![Cubietruck-7 Frontside RevA.JPG][15532]][15533]  
Manufacturer |  [Cubietech][15534], [Cubieboard][15535]  
Dimensions |  110 _mm_ x80 _mm_ x??_mm_  
Release Date |  October 2013   
Website |  [Cubietruck Product Page][15536]  
Specifications   
SoC |  [A20][15537] @ 1Ghz   
DRAM |  2GiB DDR3 @ 480MHz ([GT8UB512M8EN-BG][15538] or [H5TQ4G63AFR-PBC][15539])   
NAND |  8GB ([H27UCG8T2ATR-BC][15540])   
Power |  DC 5 V @ 2 A (3A with 2.5" SATA drive) using 4/1.7mm jack, JST XH 2.5mm Battery connector   
Features   
Video |  HDMI (Type A - full), VGA   
Audio |  3.5 mm headphone plug, HDMI, S/PDIF   
Network |  WiFi 802.11 b/g/n (Ampak AP6210), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][15541])   
Storage |  µSD, SATA 2.0   
USB |  2 USB 2.0 Host, 1 mini-USB2.0 OTG   
Other |  Bluetooth (Ampak AP6210), IRDA, RTC   
Headers |  UART, I2S, I2C, SPI, CVBS, LRADC (2x),UART, PS2, PWM (2x), TS/CSI, IRDA, LINE-IN, FM-IN, MIC-IN, TV-IN (4x), ...   
Cubietruck is the third generation of the famous [Cubieboard][15542], and is the most full-featured board to date. 
## Contents
  * [1 Identification][15543]
  * [2 Sunxi support][15544]
    * [2.1 Current status][15545]
    * [2.2 Images][15546]
    * [2.3 Manual build][15547]
      * [2.3.1 U-Boot][15548]
        * [2.3.1.1 Sunxi/Legacy U-Boot][15549]
        * [2.3.1.2 Upstream/Mainline U-Boot][15550]
      * [2.3.2 Linux Kernel][15551]
        * [2.3.2.1 Sunxi/Legacy Kernel][15552]
        * [2.3.2.2 Upstream/Mainline kernel][15553]
  * [3 Tips, Tricks, Caveats][15554]
    * [3.1 Fel mode][15555]
    * [3.2 VGA][15556]
    * [3.3 DRAM frequency][15557]
    * [3.4 Wifi][15558]
      * [3.4.1 Networkmanager][15559]
    * [3.5 Bluetooth][15560]
    * [3.6 Battery][15561]
    * [3.7 SATA power][15562]
    * [3.8 Cubietech Kernel source][15563]
    * [3.9 Expansion Ports][15564]
      * [3.9.1 Uncommon 2.0mm pitch connector size][15565]
  * [4 Adding a serial port][15566]
  * [5 Pictures][15567]
  * [6 Hardware documentation][15568]
  * [7 Also known as][15569]
  * [8 See also][15570]
    * [8.1 Vendor images][15571]

# Identification
The board helpfully states "CUBIETRUCK". 
There are two revisions of the A20. Since Feb 2014 it is RevB. The Rev state is not printed on the board and is not retrievable from the SoC. There is also no information regarding the differences of these revisions. There is evidence of different behavior and boot problems with older kernel on RevB cubietrucks. 
# Sunxi support
## Current status
Mostly supported. See [Tips, Tricks, Caveats][15554] below for more details. 
## Images
Instruction to make ArchLinux ARM images for [Cubietruck][15572]. 
## Manual build
You can build things for yourself by following our [ Manual build howto][15573] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _Cubietruck_ build target. 
#### Upstream/Mainline U-Boot
Use the _Cubietruck_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_cubietruck.fex_][15574] file. 
#### Upstream/Mainline kernel
Use the _sun7i-a20-cubietruck.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## Fel mode
There is a button marked 'FEL' next to the full-size usb ports, which triggers [ FEL mode][15575]. 
## VGA
The Cubietruck is the only board to date that has a properly implemented VGA connector with DDC. Load-detection is also reliable. In future kernel versions (with [sunxi-kms][15576]), VGA and the attached monitor will be detected properly and will require no intervention. 
For now though, you need to [ edit the FEX file][15577] still. 
There is one issue with VGA though. Due to bad PCB placement, there is some crosstalk between Wifi and VGA in certain videomodes. 
## DRAM frequency
[code] 
    <tomee^> arokux: 432MHz. that's the speed at which my board runs with sunxi bootloader, too. but look here:http://dl.cubieboard.org/software/a20-cubietruck/common/ct-v101_sys_config.fex
    <tomee^> arokux: I simply do not know why 432MHz if the hardware can do 480... they downclocked it for security purposes in the first batch?
    <arokux> tomee^: sorry, I have no idea.
    <tomee^> arokux: I've heard somewhere that someone complained about overheating of the prototype
    <arokux> tomee^: Turl may know.
    <Turl> dunno, we should ask benn
    
[/code]
See [this][15578] conversation on memory frequency problems. 
## Wifi
There is an AMPAK AP6210 Wifi+BT chip on board with PCB antenna, but it is not clear what exactly is inside: 
    
  * Broadcom BCM43362 + BCM20710
  * Broadcom BCM4330 / BCM40183 Based Chipset
  * Cubietech says it is BCM4329/BCM40181

If your're using the Cubietech's kernel, you can enable the module with 
[code] 
       modprobe bcmdhd
    
[/code]
There is a parameter op_mode, which allows you to enable AP mode, for example 
[code] 
       modprobe bcmdhd op_mode=2
    
[/code]
For the linux-sunxi's 3.4 kernel, you will need a special driver, instructions to integrate and compile the [AMPAK AP6210 Wifi and Bluetooth driver][15579] with the sunxi-3.4 source code are avalable. 
### Networkmanager
The Lubuntu Desktop images has NetworkManager running. It spawns its own wpa_supplicant, which is respawned once you kill it. This wpa_supplicant will also interfere with yours, if you want to configure WLAN Adapter by yourself. I have removed NetworkManager and was able to successfully configure WiFi. 
[code] 
       wpa_supplicant -D nl80211 -B -i wlan0 -c <(wpa_passphrase YOUR_SSID YOUR_PASSWORD)
    
[/code]
## Bluetooth
This is a new or differently wired chip, status UNKNOWN, please test it! 
Huang Benn said [here][15580] (the cubietruck chipset AMPAK) ap6210 is a combo of wifi(bcm40181) and bt(bcm20710). the firmwares can be found here: [wifi/bluetooth driver][15581]
    Here is some info on how to get the bcmdhd compiled with workarounds / ideas how to overcome problems
[code] 
    <tomee^> arokux:   CC [M]  drivers/net/wireless/bcmdhd/dhd_linux.o drivers/net/wireless/bcmdhd/dhd_linux.c: In function ‘dhd_os_prealloc’: drivers/net/wireless/bcmdhd/dhd_linux.c:5192:2: error: implicit declaration of function ‘wl_android_prealloc’ [-Werror=implicit-function-declaration]
    <tomee^> arokux: I guess you should ifdef the DHD_OS_PREALLOC option for non-android builds... or I did something wrong
    <tomee^> arokux: it comes from the bcmdhd driver compilation
    <tomee^> arokux: when I disabled buffer preallocation for it, it went through
    <tomee^> arokux: CONFIG_DHD_USE_STATIC_BUF=y broke the compilation. CONFIG_DHD_USE_STATIC_BUF=n made it work. maybe this flag should depend on android or some other build environment
    
[/code]
## Battery
Tha battery backups the power supply. It allows an uninterruptible operation. Depending on the battery capacity several hours of operation are possible. 
The battery will be charged during operation. A 3.7 Volt Lithium polymer battery is needed. The JST XH 0.1"/2.5mm connector is near the ethernet port (see frontside board pictures). 
For kernel 3.4: 
  * The battery capacity in mA has to be set in the fex file.
  * The current voltage can be read here /sys/class/power_supply/battery/voltage_now
  * The current status charging/discharging can be read here /sys/class/power_supply/battery/status

## SATA power
The cubietruck is prepared to power directly a 3.5" HDD with Cubietech's optional _3.5 inch HDD addon package_. Unlike other sunxi boards that feature an onboard SATA-power-connector suitable for powering 2.5" disks the Cubie solution is able to feed 3.5 disks that need both 5V/12V from a single 12V power source (using a 5.5/2.1 power barrel). The Addon board contains a step-down converter supplying 5V on 2 USB type A ports (from where you can feed the board using an USB-to-4/1.7mm-cable) and provides 12V on a JST XH 0.1"/2.5mm header. An identical header on the Cubietruck routes the 12V to the SATA connector on the board's edge (see gallery below). 
Both 5V and 12V power connectors towards disk also use the JST XH 2.5mm header. [Banana Pi][15582]/[Pro][15583]/[M1+][15584], [Orange Pi][15585], [Orange Pi Mini][15586] and [pcDuino3 Nano][15587] use all the same JST header to provide 5V to a SATA disk. But only the pcDuino uses the same polarity, on Bananas/Oranges 5V/GND are inversed! So you could use Cubietech's _3.5 inch HDD addon package_ with pcDuino3 Nano or use the 2.5" SATA-power kits available for the pcDuino with Cubieboards without modifications. But due to different polarity the different _Pis_ are incompatible and would require cable modifications. 
## Cubietech Kernel source
There are kernels developed by Cubietech, they are supposed to have all features working. 
  * Kernel: <https://github.com/cubieboard/linux-sunxi>
  * fex and kernel config: <https://github.com/cubieboard/cubie_configs>

Reportedly AP mode does not work with the WiFi driver in this kernel. 
This kernel is abandoned by Cubietech, but can still have something interesting, such as: <https://github.com/cubieboard2/linux-sunxi/tree/sunxi-3.4-ct-dev/drivers/net/ethernet/allwinner/gmac>
## Expansion Ports
The cubietruck exposes 2 2.0 mm pitch connectors with lots of expansion possibilities. 
CN8 (Near Ethernet connector)   
---  
2x15 Header   
1 | _GND_ | 2 | _3.3V_  
3 | _AVCC_ | 4 | _RESET#_  
5 | [PC19][15588] (SPI2-CS0/EINT12) | 6 | [PC21][15589] (SPI2-MOSI/EINT14)  
7 | [PC20][15590] (SPI2-CLK/EINT13) | 8 | [PC22][15591] (SPI2-MISO/EINT15)  
9 | [PB14][15592] (SPI2-CS0/JTAG_MS0) | 10 | [PB16][15593] (SPI2-MOSI/JTAG_DO0)  
11 | [PB15][15594] (SPI2-CLK/JTAG_CK0) | 12 | [PB17][15595] (SPI2-MISO/JTAG_DI0)  
13 | _GND_ | 14 | _GND_  
15 | [PI20][15596] (FMIN-L/PS2SCLK0/UART7-TX/HSCL) | 16 | [PI14][15597] (PS2SCLK1/EINT26)  
17 | [PI21][15598] (FMIN-R/PS2SDA0/UART7-RX/HSDA) | 18 | [PI15][15599] (PS2SDA1/EINT27)  
19 | [PI3][15600] (PWM1) | 20 | [PB3][15601] (IR0-TX)  
21 | [PB2][15602] (PWM0) | 22 | [PB4][15603] (IR0-RX)  
23 | [PB18][15604] (TWI1-SCK) | 24 | _LINEIN-L_  
25 | [PB19][15605] (TWI1-SDA) | 26 | _LINEIN-R_  
27 | _CVBS_ | 28 | _LRADC0_  
29 | _VCC-5V_ | 30 | _LRADC1_  
CN9 (Near USB Ports)   
---  
CSI1/TS/TP/TVIN   
1 | 3.3V  | 2 | 3.3V   
3 | [PG0][15606] (TS1_CLK/CSI1-PCLK) | 4 | [PG3][15607] (TS1_ERR/CSI1-VSYNC)  
5 | [PG2][15608] (TS1_SYNC/CSI1-HSYNC) | 6 | [PG1][15609] (TS1_DVLD/CSI1-MCLK)  
7 | [PG4][15610] (TS1_D0/CSI1-D0) | 8 | [PG5][15611] (TS1_D1/CSI1-D1)  
9 | [PG6][15612] (TS1_D2/CSI1-D2/UART3-TX) | 10 | [PG7][15613] (TS1_D3/CSI1-D3/UART3-RX)  
11 | [PG8][15614] (TS1_D4/CSI1-D4/UART3-RTS) | 12 | [PG9][15615] (TS1_D5/CSI1-D5/UART3-CTS)  
13 | [PG10][15616] (TS1_D6/CSI1-D6/UART4-TX) | 14 | [PG11][15617] (TS1_D7/CSI1-D7/UART4-RX)  
15 | _GND_ | 16 | _GND_  
Analog   
17 | _XP-I2SDO1_ | 18 | _TVIN0-I2SMCLK_  
19 | _XN-I2SDO2_ | 20 | _TVIN1-BTPCMCLK_  
21 | _YP-I2SDO3_ | 22 | _TVIN2-BTPCMSYNC_  
23 | _XN-BTPCMIN_ | 24 | _TVIN3-BTPCMOUT_  
### Uncommon 2.0mm pitch connector size
_2.0mm_ pitch connectors is not a common size, as the common connector size is _2.54mm_ pitch, which makes it hard to source connectors, or source parts to crimp such connectors. You can find some hits with a search for _2.00mm dupont connector_. 
Some common makes and model of these connectors (and crimps) are: 
  * [Harwin M22][15618]: can be found at reputable electronics distributors.
  * [Joint Tech Electronic A2015][15619]
  * [Scondar SCT2015][15620]
  * [ST Technology Dupont 2.0][15621]
  * [LHE A2004][15622]

Here is [good guide to crimping your own connectors.][15623]
# Adding a serial port
[![][15624]][15625]
[][15626]
UART pins in green circle
There is a nice 0.1" connector behind the USB ports, just plug in your [UART][15627] adapter. 
# Pictures
  * [![CT overview.jpg][15628]][15629]
  * [![Cubietruck-7 Frontside RevA.JPG][15630]][15533]
  * [![Cubietruck-3 Backside RevA.JPG][15631]][15632]
  * [![CT disk assembly.jpg][15633]][15634]
  * [![Cubietruck-2 SSD-Mount RevA.JPG][15635]][15636]
  * [![Cubietruck with SATA Add-On.JPG][15637]][15638]

# Hardware documentation
  * <https://github.com/lipro-armbian/pddocs/tree/master/Cubietech/CubieBoard3-CubieTruck>

# Also known as
The cubieboards are a well known brandname nowadays and there are no rebadgers. The Cubietruck is also known as Cubieboard 3. 
# See also
  * [FAQ][15639]
  * [Cubietech Cubieboard][15542]
  * [Cubietech Cubieboard2][15640]

  * [cubieboard.org - official homepage][15641]
  * [docs.cubieboard.org - cubie's user manual][15642]
  * [Cubietruck schematic][15643]

## Vendor images
  * [Android images][15644]
  * [Lubuntu desktop][15645]
  * [Lubuntu server][15646]
  * [Downloads for all up-to-date images for cubietruck][15647]
