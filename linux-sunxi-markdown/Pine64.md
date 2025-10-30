# Pine64
Pine64  
---  
[![Pine64 top.jpg][44422]][44423]  
Manufacturer |  [Pine64][44424]  
Dimensions |  133 _mm_ x 80 _mm_ x 19 _mm_  
Release Date |  February 2016   
Website |  [Pine64 Wiki][44425]  
Specifications   
SoC |  [A64][44426] @ 1152MHz   
DRAM |  512MiB/1GiB/2GiB DDR3L @ 672MHz (Samsung K4B2G1646Q-BCK0 / [Samsung K4B4G1646Q-HYK0][44427] * 2 / [Samsung K4B4G0846E][44428] * 4)   
NAND |  none   
Power |  DC 5V @ 2A, 3.7V Li-Ion battery connector, Euler connector   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone/microphone plug   
Network |  (optional) WiFi 802.11 b/g/n ([Realtek 8723BS][44429]), 10/100/1000Mbps Ethernet ([Realtek 8211E][44430]) (plus version), 10/100Mbps Ethernet ([Realtek 8201FN][44430]) (non-plus version)   
Storage |  µSD   
USB |  2 USB2.0 Host   
Other |  DSI, CSI, TP, RTC   
Headers |  RPi2 compatible GPIO, "Euler" connector, WiFi/BT connector, 2x5 pins "EXP" header   
The Pine64 is a cost-optimized board sporting [ARMv8 (64-bit ARM)][44431] capable cores. It was one of the first available boards with a 64-bit Allwinner chip, and one of the first affordable boards with an 64-bit ARM core in general. 
## Contents
  * [1 Identification][44432]
    * [1.1 Different models][44433]
  * [2 Sunxi support][44434]
    * [2.1 Current status][44435]
    * [2.2 Images][44436]
    * [2.3 BSP][44437]
    * [2.4 Manual build][44438]
      * [2.4.1 U-Boot][44439]
        * [2.4.1.1 Sunxi/Legacy U-Boot][44440]
        * [2.4.1.2 Mainline U-Boot][44441]
      * [2.4.2 Trusted Firmware-A (TF-A, formerly known as ATF)][44442]
      * [2.4.3 Linux Kernel][44443]
  * [3 Tips, Tricks, Caveats][44444]
    * [3.1 Boot sequence][44445]
      * [3.1.1 Legacy BSP boot sequence][44446]
    * [3.2 FEL mode][44447]
    * [3.3 SPI NOR Flash][44448]
    * [3.4 Expansion headers][44449]
    * [3.5 AXP803 PMIC][44450]
    * [3.6 DC5V/BAT POWER jumper][44451]
    * [3.7 Gigabit PHY issue][44452]
    * [3.8 CPU clock speed limit][44453]
    * [3.9 USB controllers and ports][44454]
  * [4 Serial port / UART][44455]
  * [5 Pictures][44456]
    * [5.1 Pine64+ (2 GB)][44457]
    * [5.2 Pine64+ (1 GB)][44458]
    * [5.3 Pine64 (512 MB)][44459]
  * [6 Variants][44460]
  * [7 See also][44461]
    * [7.1 Manufacturer images][44462]

# Identification
There is a pine cone like logo next to the uSD slot, also it says "Pine64" under the logo. Also on the SoC there is a quite prominent "A64" print. 
On the back of the device, the following is printed: 
[code] 
    Designed in Silicon Valley, California. Built in Silicon Delta, China.
[/code]
The PCB has the following silkscreened on it: 
[code] 
    A64-DB-Rev B
    2015-12-17
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _Pine A64_
  * Build Number: _tulip_t1-eng 5.1.1 LVY4BE 20151210 test-keys_

## Different models
So far there are three different models: 
  * The Pine64 with 512MB DRAM
  * The Pine64+ with 1GB DRAM
  * The Pine64+ with 2GB DRAM

The last two seem to be identical apart from the installed DRAM size. Differences between the Pine64 and the Pine64+ are: 
  * The Pine64 only supports Fast Ethernet. So the PHY chip will be a Realtek 8201 instead of the 8211 on the bigger model. The 8211 speaks RGMII, while the 8201 is using the MII interface. This requires differences in the DT.
  * The smaller model will lack the connectors for the touchscreen, LCD screen and the camera port.

# Sunxi support
## Current status
The [A64][44426] SoC [mainline kernel][44463] and firmware support is very mature and the Pine64 is one of best supported boards. Virtually every feature of the SoC and the board are supported, often generic distribution provide explicit Pine64 support. 
Due to its nature as an early example of an ARM64 capable board, there are many Linux images out there, some still using an updated and enhanced version of Allwinner's BSP kernel. There is little to no reason to use a BSP kernel today. 
## Images
**End Users** : 
[[1]][44464] Here are links to current images that are community supported: 
  * [Ubuntu Base image by Longsleep (from pine64.pro)][44465]
  * [Ubuntu Minimal image by ayufan (from pine64.pro)][44466]
  * [Arch Linux image Mainline XFCE (from pine64.org)][44467]
  * [Debian Jessie with Mate DE by Lenny Raposo (from pine64.org)][44468]
  * [Armbian for PINE64][44469]

(You should also cross-check the Wiki page that's linked under [Manufacturer Images][44470].) 
* * *
**Developers** : Get apritzel's github [basic image][44471] first. For instructions see the _README.md_ in there for now. 
longsleep has also built a minimal Ubuntu image combined with the the BSP Kernel that can be downloaded [here][44472]. You will find instructions [here][44473] on how to set it up. 
This image is intended for developers and comes with the following: 
  * BSP Linux Kernel 3.10.65+
  * BSP U-Boot
  * Ubuntu Ubuntu 16.04 (Xenial Xerus) aarch64
  * HDMI at 1080P
  * HDMI analog audio (alsa, pulseaudio)
  * Ethernet (including 1000M)
  * USB
  * Wifi

## BSP
Allwinner's BSP contains an arm64 Linux kernel based on Linaro's LSK-3.10.65 (includes Linaro and Android patches). It has traces (commented or not-configured code parts) of nasty experiments (like entering the kernel in AArch64 EL3 or running in secure EL1). This released/leaked code does not exactly match what's on the provided Android images. The BSP kernel is entered in non-secure El1, thus denying any kind of virtualization (like KVM). 
## Manual build
You can build things for yourself by following our [ Manual build howto][44474] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
The Allwinner provided BSP package contains U-Boot source code, which contains a 32-bit port based on the 2014.07 release. The code as in the tarball does not even compile, also the whole port is severely crippled, just enough to boot an Android system from MMC. Limitations include: missing booti support (no direct kernel image load, only Android kernel images can be used), no network support, only loading data from Android partitions (no filesystem support), completely non-standard DT bindings, no support for easy FDT loading, etc. For the complete rant see the Wiki history ;-) 
However the existing code base was fixed and extended by longsleep to allow loading kernels directly (using booti and proper FDT support) and adding filesystem support, thus overcoming the most severe limitations. The most current code base can be found [here][44475]. 
At the moment this U-Boot version is required to boot BSP kernels. 
#### Mainline U-Boot
The board is fully supported since v2017.07. Use the `pine64_plus_defconfig` target to build a U-Boot image. This includes support for the 512MB "non-plus" version, which will be detected at runtime. You need an ARM Trusted Firmware build (bl31.bin, see below), which will be included in the FIT image. 
The `booti` command is supported to load Linux arm64 kernel images, also `bootefi` is available to launch Aarch64 EFI applications (like grub2). There is no support for launching 32-bit kernels, though support for this is technically possible and might be added in the future. 
In contrast to the BSP version, the mainline port is a 64-bit version, so the Allwinner provided boot0/ATF pair will not boot this without further changes/patches. 
There is a [README][44476] file in the U-Boot tree describing in more detail how to compile U-Boot for the board. This should be in sync with what the current U-Boot code base supports. 
### Trusted Firmware-A (TF-A, formerly known as ATF)
All 64-bit Allwinner SoCs require a build of the BL31 part of Trusted Firmware. This provides proper SMP handling, including the reference implementation of the PSCI runtime, also errata workaround, among other things. TF-A is a BSD licensed [Open Source project][44477]. 
To build the required bl31.bin file, check out the master branch and build it for the A64 target with an AArch64 cross compiler: 
[code] 
    $ git clone <https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git>
    $ cd trusted-firmware-a
    $ make CROSS_COMPILE=aarch64-linux-gnu- PLAT=sun50i_a64 DEBUG=1
    
[/code]
You will need the bl31.bin file, either copy it from the build/sun50i_a64/debug directory into the root of the U-Boot tree or let the BL31 environment variable point to it. 
### Linux Kernel
The mainline Linux kernel supports the Pine64 very well, including advanced features like 3D graphics, video acceleration and DVFS. 
  * Basic support has been merged into Linux v4.10-rc1, though this does not support MMC, so can only be used with an initrd. Also it lacks support for any other peripheral except I2C and UART (serial console).
  * MMC and USB support was merged into 4.11-rc1, which brings the support into some kind of usable state, though Ethernet support is still missing.
  * The Ethernet driver was finally added in the 4.15 release.

For the full story check the [status matrix][44463]. 
For basic support the device tree from U-Boot can be used for the kernel as well, just provide $fdtcontroladdr as the respective booti argument. 
To build a kernel for the board, clone the recent mainline Linux tree and build a "defconfig" kernel like this: 
[code] 
    $ export CROSS_COMPILE=aarch64-linux-gnu-
    $ ARCH=arm64 make clean defconfig
    $ ARCH=arm64 make -j4 Image
    
[/code]
The generated dtb files for the different Pine64 versions are called **sun50i-a64-pine64-lts.dtb** , **sun50i-a64-pine64-plus.dtb** , and **sun50i-a64-pine64.dtb**. 
# Tips, Tricks, Caveats
## Boot sequence
The A64 SoC is wired to come out of reset in 32-bit secure supervisor mode. As other Allwinner devices, the A64 SoC starts executing BROM code (mapped at address 0), which is consequently ARM32 code. The ROM covers the first 64KB, but uses less space for the normal non-secure boot version. If the code does not detect a FEL condition (no or invalid SD card inserted), it will load 32KB from sector 16 (8 KByte) of the microSD card to SRAM and will execute this. At least the first instructions of this code need to be still 32-bit ARM code. 
Mainline U-Boot [resets to AArch64][44478] as early as possible, and runs the following code (including ATF and U-Boot proper, then the kernel) in 64-bit mode. 
### Legacy BSP boot sequence
The Allwinner firmware runs mostly in AArch32, with boot0 loading U-Boot (32-bit also) from the microSD card at sector 38192 (19096 KByte). It also loads a (hacked) version of ARM Trusted Firmware (ATF) into DRAM and code for the arisc management core into SRAM. Finally it does a [RMR write][44479] to warm-reset the SoC in AArch64 execution state and jumps to the ATF entry point by putting its address in the [RVBAR register][44480]. ATF will then initialize the boot core for non-secure execution and drop to non-secure AArch32 EL1 to run U-Boot. 
U-Boot then runs happily in 32-bit. Only just before it starts the kernel, it uses a custom smc service call back into (Allwinner's version of) ARM Trusted Firmware to hand over the kernel entry point. The ATF code will then return into _AArch64_ non-secure EL1, but using the provided kernel entry point instead of returning to U-Boot. 
## FEL mode
The Pine64 board will fail over to [FEL mode][44481] if it doesn't detect a card present in the µSD slot. 
[![Exclamation.png][44482]][44483] A tricky and potentially confusing part is that the only Micro USB receptacle (labelled as "POWER JACK") is used exclusively for providing power to the board, and is _not_ connected to any USB controller in the SoC. The actual USB **OTG** controller in the SoC is connected to the **upper USB host receptacle**. So it needs a somewhat special USB cable (A male to A male) or an adapter (A male to Mini/Micro B female) to connect your Pine64 board to your desktop PC, which is running the [sunxi-fel][44484] tool. 
As soon as you boot your Pine64 into FEL mode (remember, don't insert a SD card) you should find a new USB device: 
[code] 
       $ lsusb
       Bus 001 Device 005: ID 1f3a:efe8
    
[/code]
[code] 
       $ ./sunxi-fel version
       AWUSBFEX soc=00001689(A64) 00000001 ver=0001 44 08 scratchpad=00017e00 00000000 00000000
    
[/code]
For actually loading software via FEL mode, refer to the generic [A64 FEL booting][44485] instructions. 
## SPI NOR Flash
It should be possible to have an extra hardware accessory, pluggable into the Raspberry Pi compatible expansion header to add a small SPI NOR Flash on SPI0 pins. It can store a bootable firmware and provide all the [fashionable "industry standards"][44486] compatibility for running AArch64 server grade Linux distributions (not exactly now, but maybe some time in the future). The [Bootable SPI flash][44487] page provides additional details. 
A [driver model compatible SPI driver for u-boot][44488] is currently being worked on. The Pine64+ board has been tested and is fully supported by this driver. 
## Expansion headers
Documentation about the pin assignments and more specifications (like the physical dimensions of the board) can be found in the [Hardware section][44489] of the [official Pine64 Wiki][44490]. 
## AXP803 PMIC
Some of the default reset voltages after cold boot are not exactly matching the board specification. For example, the voltage on the Euler connector's "3.3V" pin is in fact 3.0V (DCDC1) until Allwinner's bootloader configures the PMIC. In the current "upstream" firmware stack ARM Trusted Firmware [sets up the PMIC][44491] and programs DCDC1 to the specified 3.3V. It also enables DC1SW to power the Ethernet PHY. 
The DRAM voltage is provided from DCDC5, which can be set to 1.5V by default according to the AXP803 manual. Moreover, the AXP803 manual is explicitly recommending to use DCDC5 specifically for DRAM. This is safe even with 1.35V DDR3L chips, because they are [compatible with 1.5V too][44492]. However the [default reset voltage appears to be in fact set to 1.24V][44493] at least in the pre-production batch of Pine64 boards, because the DCDC5SET pin is left floating there. 
## DC5V/BAT POWER jumper
[![][44494]][44495]
[][44496]
DC5V BAT POWER jumper
On the 1GB and 2GB Pine64+ variants a DC5V/BAT POWER switch can be used to bypass the MT3608 boost converter (input voltage to 5V). If the board is powered from DC-IN (micro-USB or Euler connector), the DC5V setting connects the input voltage to the USB power supply rails, in BAT setting 5V is generated from any of the connected power sources (e.g. battery or DC-IN). The USB ports are current-limited to about 650mA per port in either setting. 
Please be aware that when using the jumper in DC5V position an insufficient supply voltage is directly visible on the USB ports. If the Pine64+ is running on battery, the USB ports are only powered when the BAT setting is used. 
## Gigabit PHY issue
A couple of Pine64+ (both 1GB and 2GB variants) is affected by Gigabit Ethernet problems. In GbE mode transfer speeds are low, many retransmits happen and packets get lost. In the meantime [it's confirmed that this is a hardware issue][44497]. If you're affected you can try to force Pine64+ in Fast Ethernet mode (using _ethtool -s eth0 speed 100 duplex full_ or an Ethernet cable with just 2 cable pairs) but it's unlikely that other software fixes cure the problem. Please refer to the aforementioned thread how/whether Pine64 comes up with a solution. 
## CPU clock speed limit
The voltage-frequency table for Allwinner A64 can be found in FEX files included in the A64 SDK: 
[code] 
    ; dvfs voltage-frequency table configuration
    ;
    ; max_freq: cpu maximum frequency, based on Hz
    ; min_freq: cpu minimum frequency, based on Hz
    ;
    ; lv_count: count of lv_freq/lv_volt, must be < 16
    ;
    ; lv1: core vdd is 1.30v if cpu frequency is (1104Mhz, 1152Mhz]
    ; lv2: core vdd is 1.26v if cpu frequency is (1008Mhz, 1104Mhz]
    ; lv3: core vdd is 1.20v if cpu frequency is (816Mhz,  1008Mhz]
    ; lv4: core vdd is 1.10v if cpu frequency is (648Mhz,   816Mhz]
    ; lv5: core vdd is 1.04v if cpu frequency is (480Mhz,   648Mhz]
    ; lv6: core vdd is 1.04v if cpu frequency is (480Mhz,   648Mhz]
    ; lv7: core vdd is 1.04v if cpu frequency is (480Mhz,   648Mhz]
    ; lv8: core vdd is 1.04v if cpu frequency is (480Mhz,   648Mhz]
    
[/code]
Based on the data from this table, 1152MHz @1.3V is the fastest cpufreq operating point. Additionally, the AXP803 PMIC uses 1.1V default voltage for DCDC2/DCDC3 (VDD-CPU). Which means that the the CPU can be safely clocked up to 816MHz before the PMIC is initialized. 
## USB controllers and ports
The A64 SoC includes two USB 2.0 EHCI/OHCI host controllers. The first host controller (HCI0) is connected to a PHY switch, which can be toggled between driving a normal USB PHY (connected to the lower USB receptable on the board) and HSIC pins on the SoC, which allow connecting on-board USB peripherals (often a hub), though this is not used on the board. 
The second host controller (USB-OTG-HCI) shares a USB PHY with the (separate!) OTG controller and is connected to the upper receptable on the Pine64 board. So this socket can either be driven by a normal host controller interface or by the OTG controller - which provides a host mode as well, though apparently not without issues. 
# Serial port / UART
[![][44498]][44499]
[][44500]
Pine64 UART pins
The board connects 4 of the SoCs UART to easily accessible header pins. There is UART2 on the RPi connector, also UART3 and UART4 on the Euler connector. UART0 is the main UART used by Allwinner's firmware for boot and debug messages and is accessible on pins 29 (TXD), 30 (RXD), 25/34 (GND) on the Euler connector (this is not mentioned in the official connector description). Better **always** use UART0 on the EXP connector nearby, accessible on pins 7 (TXD), 8 (RXD), 9 (GND). The RX pin on there is connected via a FET to the SoC's pin, so it prevents injecting power via this line. 
All of the UARTs use 3.3V voltage levels. Look at our [UART howto][44501] for further instructions. 
A connected UART cable to Euler pins is leaking power and this causes some annoyances. For example, unplugging and plugging back a power cable does not reboot the board cleanly. Thus using UART0 on EXP connector instead is highly recommended. If you still want to use the Euler connector availability of a reset button is recommended for doing any reasonable software development. 
The board does not have a hardware reset button out of the box, but a button can be easily connected to the appropriate pin on the expansion connector. Also a standard micro switch (upright version) can be soldered on the board next to the USB sockets to ease early development ;-) 
# Pictures
## Pine64+ (2 GB)
  * [![20160401 210300.jpg][44502]][44503]
  * [![Pineplus2g-back.jpg][44504]][44505]

## Pine64+ (1 GB)
  * [![Pine64 top.jpg][44506]][44423]
  * [![Pine 64 5.jpg][44507]][44508]
  * [![Pine 64 1.jpg][44509]][44510]
  * [![Pine 64 2.jpg][44511]][44512]
  * [![Pine 64 3.jpg][44513]][44514]
  * [![Pine 64 4.jpg][44515]][44516]
  * [![Pine64 Powered through Euler Connector.jpg][44517]][44518]

## Pine64 (512 MB)
  * [![Pine64 nonplus.jpg][44519]][44520]

# Variants
  * Pine Inc produces also a SoM variant + baseboard called [SoPine 64][44521]. Schematics and some documentation are provided. Obvious changes are 2GB LPDDR3 DRAM ([_boot0_ available][44522]), 128 Mb SPI flash on the SoM and the opportunity to use eMMC on the baseboard.
  * [Pinebook][44523] has been announced in Nov 2016. 2017 production batches will use 2GB LPDDR3 while the 2016 prototype boards have 4 DDR3L modules on the logicboard. Some iozone numbers for the onboard eMMC from a preliminary developer sample are [available here][44524] (take this with a grain of salt since production batches might contain a different eMMC module).

# See also
  * [wiki.pine64.org Further info on the hardware and firmware][44490].
  * [forum.pine64.org Discussion on pine64][44525]
  * [Pine A64 512MB Rev B Board Schematic][44526]
  * [Pine A64+ 1GB Rev B Board Schematic][44527]
  * [Pine A64+ 2GB Rev C Board Schematic][44528]
  * [SoPine A64 Compute Module Schematic][44529]
  * [SoPine Baseboard “Model A” Schematic][44530]
  * [Pinebook Logicboard Schematic][44531]

## Manufacturer images
[Pine A64 Android release and Linux BSP][44532]
