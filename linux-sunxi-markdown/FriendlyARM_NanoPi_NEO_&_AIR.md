# FriendlyARM NanoPi NEO &amp; AIR

# FriendlyARM NanoPi NEO & AIR
FriendlyARM NanoPi NEO & AIR  
---  
[![Duetto di NanoPi.jpg][20931]][20932]  
Manufacturer |  [FriendlyARM][20933]  
Dimensions |  40 _mm_ x 40 _mm_  
Release Date |  July (NEO) / Oct (Air) 2016   
Website |  [NanoPi NEO][20934] / [NanoPi NEO Air][20935]  
Specifications   
SoC |  [H3][20936] @ 1.2Ghz   
DRAM |  256MiB (K4B2G1646Q-BCK0) or 512MiB (K4B4G1646Q-BCK0) DDR3   
Power |  DC 5V @ 2A via microUSB or pin headers   
Features   
Audio |  microphone, stereo line-out, I²S and [S/PDIF][20937] on pin headers   
Network |  10/100Mbps Ethernet ([H3 built-in PHY][20938]) or BT4.0/WiFi 802.11 b/g/n ([Ampak AP6212][20939])   
Storage |  µSD and 8GB eMMC (Air)   
USB |  1 USB2.0 Host (NEO), 1 USB2.0 OTG   
Other |  24 pin camera connector (Air)   
Headers |  UART, SPI, I²C, 2x USB2.0 Host, analog audio, microphone   
NanoPi NEO and NEO Air are [H3][20936] based small form-factor development boards produced by [FriendlyARM][20940]. The NEO comes with integrated 100 Mbps Ethernet while NEO Air provides network with 802.11n WiFi. Both boards have a SD card slot, but NEO Air also includes 8GB eMMC. A lot of functionality is provided via the unpopulated headers on both boards. 
## Contents
  * [1 Identification][20941]
  * [2 Sunxi support][20942]
    * [2.1 Current status][20943]
    * [2.2 Images][20944]
    * [2.3 BSP][20945]
    * [2.4 Manual build][20946]
      * [2.4.1 U-Boot][20947]
        * [2.4.1.1 Mainline U-Boot][20948]
      * [2.4.2 Linux Kernel][20949]
        * [2.4.2.1 Sunxi/Legacy Kernel][20950]
        * [2.4.2.2 Mainline kernel][20951]
  * [3 Expansion Port][20952]
  * [4 Tips, Tricks, Caveats][20953]
    * [4.1 FEL mode][20954]
    * [4.2 LEDs][20955]
    * [4.3 JTAG][20956]
    * [4.4 Voltage regulators / heat][20957]
    * [4.5 DRAM][20958]
    * [4.6 WiFi][20959]
    * [4.7 USB][20960]
    * [4.8 Analog Audio][20961]
  * [5 Adding a serial port][20962]
    * [5.1 Locating the UART][20963]
  * [6 Pictures][20964]
    * [6.1 NanoPi NEO][20965]
    * [6.2 NanoPi NEO Air][20966]
  * [7 Variants][20967]
    * [7.1 NanoPi NEO Core][20968]
  * [8 See also][20969]
    * [8.1 Manufacturer images][20970]

# Identification
Small, square board, blue soldermask, ⌀3mm mounting holes in the corners. USB type-A, Ethernet jack (with integrated magnetics) and four-pin header for UART/power near one of the edges, microSD and USB micro-B at opposite edge mounted on top side, 12 and 24 GPIO pin headers (not fitted, pads only) near other edges. Allwinner H3 and single DDR3 chip mounted on the bottom. Sticker indicating amount of RAM is placed on the Ethernet jack. Device can also be ordered without USB and Ethernet soldered (see gallery below) 
On the top side of the board, next to USB A connector, the following is silkscreened: 
[code] 
    FRIENDLYARM
    NanoPi NEO
[/code]
Starting in September 2016 a new PCB revision 1.1 is available (changes: [audio signals on the GPIO header, voltage regulator][20971]) 
# Sunxi support
## Current status
The H3 SoC support has matured since its introduction in kernel 4.2. Most of the board functionality for boards such as NanoPi NEO and NEO Air are available with current mainline kernels. Some features (hw accelerated crypto, hw spinlocks, and thermal) are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][20972]. In addition, legacy 3.4 kernels are available in various work-in-progress git branches. 
See the [Manual build][20946] section for more details. 
NanoPi NEO shares nearly all hardware details with [Orange Pi One][20973]. Detailed device information can be found on [[1]][20974] and [[2]][20935]
## Images
FriendlyARM's UbuntuCore with Qt-Embedded image can be found [here][20975]. It boots a new variant of Allwinner's 3.4.39 BSP kernel, USB and Ethernet are working fine. Armbian images for NEO based on 3.4.112 (containing new IoT low power settings) or 4.6.7 can be found [here][20976]. 
## BSP
FriendlyARM provides a [BSP based on a newer Allwinner 3.4.39 variant][20977] on Github. 
## Manual build
You can build things for yourself by following our [Manual build howto][20978] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **nanopi_neo** (supported since v2016.11) or **nanopi_neo_air** (supported since v2017.05) build target. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][20979]. 
The H3 boards can boot from [SD cards][20980], [eMMC][20981], [NAND][20982] or [SPI NOR][20983] flash (if available), and via [FEL][20984] using the OTG USB port. In U-Boot, loading the kernel is also supported from USB or ethernet (netboot). 
### Linux Kernel
#### Sunxi/Legacy Kernel
The 3.4 kernel from the official [Allwinner's git repository][20985] [does not support H3][20986] yet. But it is possible to use one of the kernel forks, based on the [lichee H3 SDK tarball][20987]: 
  * [Siarhei Siamashka's branch '20151207-embedded-lima-memtester-h3'][20988]
  * [Yann Dirson's fork][20989] added a few more fixes and adopted most of
  * [Boris Lovosevic' great initial work][20990] on Allwinner's H3 kernel

Configure this kernel using **sun8i_h3_defconfig** , the rest is explained in the [kernel compilation guide][20991]. 
Use the .fex file for generating [script.bin][20992]. The .fex file is available from [xunlong_orange_pi_pc.fex][20993]. 
When booting the legacy 3.4 kernel with the mainline U-Boot, add the following line to boot.cmd: 
[code] 
      setenv machid 1029
      setenv bootm_boot_mode sec
    
[/code]
Some other legacy kernel repositories: 
  * [3.4-lichee-based kernel][20994], based on work by [ssvb][20995] and [loboris][20996]
  * [Yocto support here][20997] glues together all the required parts to get this kernel to work with mainline u-boot, as well as accelerated X11/GLES support
  * [A newer H3 BSP variant][20977] appeared with tons of fixes which has been made available by FriendlyARM.
  * [A cleaned up fork][20998] has been adopted by Armbian project. On top of that Armbian maintains a bunch of [3.4.x patches for H3 devices][20999].

#### Mainline kernel
The mainline kernel has good support for the H3 SoC. Please refer to the [status matrix][21000] for a more detailed list of the development process, links to patches and links to kernel fork repositories. Minor drivers that are currently work-in-progress may require a) [third party patches][21001] (see also arm-linux mailing list) or b) a pre-patched distro (e.g. [Armbian][21002]). 
Repositories with H3 patches: 
  * [Ondřej Jirman's branch for H3 based orange Pi (kernel 4.19)][21003] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)
  * [Philipp Rossak's THS patches (in the sunxi-ths- branches)][21004]
  * [Corentin Labbe's HW Crypto and spinlock patches (in respective branches)][21005]

  
Use the **sun8i-h3-nanopi-neo.dtb** or **sun8i-h3-nanopi-neo-air.dtb** (depending on the board) device-tree binary. 
# Expansion Port
Both NanoPi NEO and NEO Air feature one 12-pin and one 24-pin GPIO header. Air's pin-out for those headers and the DVP camera connector can be found [here][21006]. On NEO PCB rev. 1.0 analog audio signals were present on the 12-pin header that were replaced by digital audio starting with PCB rev. 1.1. With PCB rev. 1.3 position of the UART debug header has changed and a new 5-pin analog audio header has been added (same as on NEO 2 and NEO Plus 2). All pin-out information in [FriendlyELEC's wiki page][21007]. 
# Tips, Tricks, Caveats
## FEL mode
No [FEL][21008] button. UBOOT/FEL signal pulled-up by R254 (10kΩ, mounted on the bottom side, close to H3). 
## LEDs
The board has two LEDs, mounted on the top side, between micro USB and microSD: 
  * A red LED, labelled "PWR", connected to the PL10 pin and to 3.3V via weak pull-up, thus being able to represent three states: 
    * full brightness when GPIO is set to output high
    * reduced brightness when GPIO is set to high impedance state
    * turned off when GPIO is set to output low.
  * A blue LED, labelled "STAT", connected to the PA10 pin.

## JTAG
Connect gnd and target voltage to any of the gnd and vcc3v3-ext pins on the 2x12 expansion connector (con4). Pin 22 (uart2_rx) is TCK, pin 11 (uart2_tx) is TMS, pin 15 (uart2_cts) is TDI and pin 13 (uart2_rts) is TDO. 
The JTAG sel pins that seem to be used to enable JTAG at chip power on aren't broken out but you can enable JTAG on the expansion connector once uboot has started with this command (add it to _boot script_ and compile `boot.scr` again to make it permanent): 
` mw.l 0x01c20800 0x77223333 1 `
OpenOCD configuration should look something like this (based on the config from [this page][21009] in Japanese): 
[code] 
    source [find interface/ftdi/dp_busblaster_kt-link.cfg]
    adapter_khz 300
    transport select jtag
    reset_config none
    gdb_breakpoint_override hard
    
    if { [info exists CHIPNAME] } {
       set  _CHIPNAME $CHIPNAME
    } else {
       set  _CHIPNAME sun8iw7
    }
    
    if { [info exists DAP_TAPID] } {
        set _DAP_TAPID $DAP_TAPID
    } else {
        set _DAP_TAPID 0x5ba00477
    }
    
    jtag newtap $_CHIPNAME dap -expected-id $_DAP_TAPID -irlen 4 -ircapture 0x01 -irmask 0x0f
    
    set _TARGETNAME0 $_CHIPNAME.cpu0
    set _TARGETNAME1 $_CHIPNAME.cpu1
    set _TARGETNAME2 $_CHIPNAME.cpu2
    set _TARGETNAME3 $_CHIPNAME.cpu3
    
    target create $_TARGETNAME0 cortex_a -chain-position $_CHIPNAME.dap -coreid 0
    target create $_TARGETNAME1 cortex_a -chain-position $_CHIPNAME.dap -coreid 1
    target create $_TARGETNAME2 cortex_a -chain-position $_CHIPNAME.dap -coreid 2
    target create $_TARGETNAME3 cortex_a -chain-position $_CHIPNAME.dap -coreid 3
    target smp $_TARGETNAME0 $_TARGETNAME1 $_TARGETNAME2 $_TARGETNAME3
    
    $_TARGETNAME0 configure -event gdb-attach {
        cortex_a dbginit
    }
    $_TARGETNAME1 configure -event gdb-attach {
        cortex_a dbginit
    }
    $_TARGETNAME2 configure -event gdb-attach {
        cortex_a dbginit
    }
    $_TARGETNAME3 configure -event gdb-attach {
        cortex_a dbginit
    }
    
[/code]
This is a little bit fragile but it works well enough to set breakpoints in the kernel with GDB so should be useful when debugging drivers etc. 
## Voltage regulators / heat
NanoPi NEO/Air use the same voltage regulator as NanoPi M1 and Orange Pi One/Lite switching between 1.1V and 1.3V (SY8113B [datasheet][21010]). Unlike the Xunlong boards which contain a thick copper layer inside the PCB to spread heat away from the SoC FriendlyARM chose a different design. This and maybe the smaller PCB size lead to higher temperatures compared to Orange Pis and in case you want to operate the NEO under constant high load think about adding a heatsink (FriendlyARM provides one combined with a 2mm heat pad that can be securely mounted on the board -- see gallery images below. 
On NanoPi NEO PCB rev 1.0 U7 next to DRAM is an LDO voltage regulator that provides 1.2V for various SoC parts and 1.1V for the internal Ethernet PHY. It overheats a lot and is rated 500mA max. When ordering FriendlyARM's heatsink maybe combining it with a larger heatpad that covers the whole SBC's surface is a better option than now (using a small 15x15 heat pad that connects SoC with heat sink but decreases heat dissipation for all other SBC components this way). 
## DRAM
NanoPi NEO is available with 256 MiB or 512 MiB but only in single bank configuration. NanoPi Air is available with 512 MiB (also single bank). 
DRAM is clocked at **432 MHz** by the hardware vendor. [User:Tkaiser][21011] did some consumption and thermal measurements just to find out that the board deadlocks pretty fast when running lima-memtester regardless of DRAM clockspeed (happens within minutes) but as soon as an annoying fan is added to FriendlyARM's heatsink blowing air between heatsink and SoC the board survives lima-memtester running at 600 MHz for several hours (board found powered off after increasing up to 672 from userspace after another hour). Since visual feedback is impossible on a board that lacks any display output we should consider 432 MHz to be a sane default since it both helps decreasing heat and consumption. 
Based on [User:Tkaiser][21011]'s tests reducing DRAM clockspeed by 24 MHz more (with BSP kernel 408 MHz is the lowest allowed clockspeed) is even better since it does not affect performance that much (negligible according to tinymembench) but both temperature and consumption are lowered a lot by switching from 432 MHz to 408 MHz. Test results [here][21012] and description of test setup [there][21013] (using another sunxi board's AXP209 to do consumption measurements). BSP kernel boots happily with _CONFIG_DRAM_CLK=408_ and _CONFIG_SYS_CLK_FREQ=480000000_ set in u-boot 2016.07. 
The single bank DRAM configuration is slower than dual bank configuration on all other H3 devices. Even more when taking the different DRAM clockspeeds into account. Using [tinymembench][21014] and looking at _standard memcpy_ numbers, NEO/Air clocked with 408 or 432 MHz show ~435 MB/s while other H3 boards with dual bank DRAM clocked at 624 MHz reach ~900 MB/s (for more details see [post #13 in this thread in Armbian forums][21015]). When using [cpuminer][21016] then NEO/Air clocked with 1200 MHz achieve 1.83/1.85833 khash/s with DRAM clocked at 408/432 MHz while an Orange Pi Lite with identical settings (HDMI/Mali disabled and also clocking at 1200 MHz) achieves 2.10867 khash/s with DRAM clocked at 624 MHz (that's a ~12 percent performance loss with this specific workload only due to different DRAM configuration and clockspeed) 
## WiFi
NanoPi NEO AIR has an [Ampak AP6212][20939] chip, which needs [special firmware files][21017]. 
## USB
The one USB host port exposed as type A receptacle is usb3. Both usb1 and usb2 are available via solder holes. 
## Analog Audio
On NanoPi Air analog audio out and mic in is available on 4 solder pads next to the camera connector. Please check schematic for details. 
# Adding a serial port
## Locating the UART
[![][21018]][21019]
[][21020]
NanoPi NEO UART pins
Four-pin UART0 header is placed next to USB type-A connector. Pinout: GND, 5V, TX, RX. Pin 1 (GND) is the one furthest from the board edge. Logic voltage is 3.3V. For more instructions refer to our [UART Howto][21021]. 
# Pictures
## NanoPi NEO
  * [![NanoPi NEO top.jpg][21022]][21023]
  * [![NanoPi NEO bottom.jpg][21024]][21025]
  * [![NanoPi NEO 1.jpg][21026]][21027]
  * [![NanoPi NEO 2.jpg][21028]][21029]
  * [![NanoPi NEO 3.jpg][21030]][21031]
  * [![NanoPi NEO 4.jpg][21032]][21033]
  * [![Nanopi-front.JPG][21034]][21035]
  * [![Nanopi-back.JPG][21036]][21037]
  * [![Nano Heatsink.jpg][21038]][21039]
  * [![NanoPi NEO Cluster.jpg][21040]][21041]

## NanoPi NEO Air
  * [![NanoPi Air 1.jpg][21042]][21043]
  * [![NanoPi Air 2.jpg][21044]][21045]
  * [![NanoPi Air 3.jpg][21046]][21047]

# Variants
## NanoPi NEO Core
In the NEO Core variant, the ethernet and USB A connectors are replaced with unpopulated headers. The variant also comes with onboard eMMC (4GB/8GB/16GB/32GB). 
To enable eMMC in U-Boot you have to add `CONFIG_MMC_SUNXI_SLOT_EXTRA=2` to `.config` and add `&mmc2` node to the device tree file. Something like [this][21048] or use Armbian paches [add-emmc_support_to_neo1_and_2.patch][21049] and [add-nanopi-neo-core.patch][21050] or use [add-nanopi-air-emmc.patch][21051] as an example. 
# See also
  * [Air device page on FriendlyARM wiki page][20935]
  * [NEO device page on FriendlyARM wiki page][20974]
  * [Armbian forum thread for both devices][21052]
  * [NEO Air Schematic for PCB rev 1.0][21053]
  * [NEO Schematic for PCB rev 1.0][21054]
  * [NEO Schematic for PCB rev 1.1][21055]
  * [NEO Schematic for PCB rev 1.2][21056]
  * [board mechanical drawings (dxf)][21057]

## Manufacturer images
See the manufacturer's device pages above since links change from time to time.
