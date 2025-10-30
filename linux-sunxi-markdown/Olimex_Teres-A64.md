# Olimex Teres-A64
Olimex Teres-A64  
---  
[![Teres-1.jpg][41318]][41319]  
Manufacturer |  [OLIMEX][41320]  
Release Date |  [12th Oct 2017][41321]  
Website |  [https://olimex.com/products/DIY-Laptop][41322]  
Specifications   
SoC |  [AllWinner A64][41323] (4x Cortex-A53 @ 1152 MHz)   
DRAM |  2GB DDR3L RAM @ 672 MHz ([2x Hynix H5TC8G63AMR-PBA][41324])   
NAND |  16GB eMMC ([MTFC16GAKAENA-4M][41325]) + SDCard   
Power |  DC 5V @ 1~3A, up to 9500mAh 3.7V Li-Ion battery   
Features   
LCD |  1366x768 IPS ([N11BGE-EA2 Rev.C3][41326])   
Video |  HDMI (mini)   
Audio |  3.5mm headphone plug HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([[RTL8723BS][41327]])   
Storage |  µSD, NAND   
USB |  2 USB2.0 Host, X USB2.0 OTG   
Camera |  VGA (640x480) front   
This page needs to be properly filled according to the [New Device Howto][41328] and the [New Device Page guide][41329].
Do it yourself laptop, hacker friendly. 
## Contents
  * [1 Engineers, Maintainers and Contributors][41330]
  * [2 Identification][41331]
  * [3 Sunxi support][41332]
    * [3.1 Current status][41333]
      * [3.1.1 Linux Kernel Support][41334]
      * [3.1.2 Linux Distribution Support][41335]
        * [3.1.2.1 Debian GNU/Linux][41336]
        * [3.1.2.2 Ubuntu][41337]
        * [3.1.2.3 NixOS][41338]
        * [3.1.2.4 Arch Linux][41339]
        * [3.1.2.5 Parabola GNU/Linux][41340]
        * [3.1.2.6 GNU Guix GNU/Linux][41341]
        * [3.1.2.7 Gentoo Linux][41342]
        * [3.1.2.8 PostmarketOS][41343]
        * [3.1.2.9 Alpine Linux][41344]
    * [3.2 Manual build][41345]
      * [3.2.1 The Bootloader][41346]
      * [3.2.2 Crust][41347]
      * [3.2.3 Arm Trusted Firmware][41348]
      * [3.2.4 U-Boot][41349]
        * [3.2.4.1 Sunxi/Legacy U-Boot][41350]
      * [3.2.5 Linux Kernel][41351]
        * [3.2.5.1 Sunxi/Legacy Kernel][41352]
        * [3.2.5.2 Mainline kernel][41353]
  * [4 Linux Kernel Configuration Reference][41354]
    * [4.1 Contiguous Memory Allocator (CMA)][41355]
    * [4.2 Unified Extensible Firmware Interface (UEFI)][41356]
    * [4.3 Battery][41357]
    * [4.4 Wireless][41358]
    * [4.5 Display][41359]
  * [5 Tips, Tricks, Caveats][41360]
    * [5.1 FEL mode][41361]
  * [6 Modifications][41362]
    * [6.1 Recommended][41363]
      * [6.1.1 Add VCC-in Fuse][41364]
      * [6.1.2 Cut the power cable][41365]
      * [6.1.3 3D print a new case][41366]
      * [6.1.4 Mount a heatspreader on the SoC and DRAM][41367]
    * [6.2 Known][41368]
      * [6.2.1 AllWinner H64][41369]
      * [6.2.2 Faster eMMC chipset][41370]
  * [7 Adding a serial port][41371]
  * [8 Known issues][41372]
    * [8.1 Power connector wear][41373]
    * [8.2 Phone signal might disrupt audio][41374]
    * [8.3 Power-on power supply connection][41375]
    * [8.4 Disfunctional display when BL31.bin is compiled with SUNXI_SETUP_REGULATORS=0][41376]
    * [8.5 Broken ANX6345 on Linux 6.5+ (non-LTS version)][41377]
  * [9 Hardening][41378]
    * [9.1 Bootloader][41379]
  * [10 Pictures][41380]
  * [11 See also][41381]
    * [11.1 Manufacturer images][41382]

# Engineers, Maintainers and Contributors
  * _[Tsvetan Usunov][41383]_ \-- Hardware Engineer and Supplier
  * _[Dan Koloff][41384]_ \-- Main Repository Maintainer
  * _[Dimitar Gamishev][41385]_ \-- The Linux Kernel Mainline and Hardware Engineer
  * _[Lub][41386]_ \-- Official Technical Support
  * _[KREYREN][41387]_ \-- Maintainer of Armbian, Debian GNU/Linux, Ubuntu, (Devuan GNU/Linux), NixOS, (GNU Guix GNU/Linux), PostmarketOS, (Alpine Linux), Parabola GNU/Linux, (Archlinux ARM). Contributor to The Linux Kernel
  * _[JC Staudt][41388]_ \-- Debian GNU/Linux Maintainer
  * _[Milan P. Stanić][41389]_ \-- Alpine Linux Maintainer
  * _[Tom Hall][41390] (former)_ \-- NixOS Maintainer
  * _[Bill Auger][41391]_ \-- Parabola GNU/Linux Maintainer
  * _[Denis 'GNUtoo' Carikli][41392]_ \-- Parabola GNU/Linux Maintainer
  * _[Alexey Korepanov][41393]_ \-- Gentoo Linux Maintainer
  * _[Jeff Moe][41394]_ \-- Engineer of 3D printable case
  * _[Chris Boudacoff][41395]_ \-- teres1-debug developer
  * _Torsten Duwe_ \-- [Linux kernel contributor who fixed ANX6345 power up sequence][41396]
  * _Harald Geyer_ \-- [Linux kernel contributor who reported issue with ANX6345][41396]
  * (and many more!)

# Identification
The PCB has the following silkscreened on it: 
[code] 
    TERES
    PCB1-A64-MAIN 
    REV. B
[/code]
Along with the availability in the olimex web shop mid-2017, PCB1 Rev.C was released. 
# Sunxi support
## Current status
Generally works with mainline: 
  * Linux kernel since release 4.19. Development oriented around LTS versions, others might have issues, 6.5 LTS discouraged due to insufficient QA on the kernel dev side
  * U-Boot Bootloader since [[504bf79][41397]] targeted release 2019.07
  * Crust firmware since release 6.0
  * Arm Trusted Firmware since 2.8.14

### Linux Kernel Support
Due to recent issues with Quality Assurance in the Linux Kernel in relation to arm64 and riscv64 it was decided to track the known working versions for stable/production/mission-critical environment. All of these versions are LTS, non-LTS versions should always be considered broken and unsable: 
  * 6.1.71 - NKI
  * 6.1.72 - NKI
  * 6.1.[73-75] - NT
  * 6.1.76 - NKI
  * 6.5.X - Currently display not working, affected by [ANX6345 issues causing broken rendering][41398]

Legend: 
  * NKI = No Known Issues
  * NT = Not Tested

The 'Stable' kernel version is not considered sane for mission-critical and production environment. 
### Linux Distribution Support
The device is fully mainlined so as long as you have a sane bootloader it should work on any distribution with the generic aarch64 rootfs, see [https://linux-sunxi.org/Bootable_OS_images][41399] for options. 
#### Debian GNU/Linux
Fully supported through the armbian framework, follow <https://www.armbian.com/olimex-teres-a64> for more info. 
For manual installation follow <https://wiki.debian.org/InstallingDebianOn/Olimex/Teres-I>
#### Ubuntu
Fully supported through the armbian framework, follow <https://www.armbian.com/olimex-teres-a64> for more info. 
#### NixOS
In development.. Kreyren's nixos configuration for daily driver may be used as a reference: <https://github.com/Kreyren/nixos-config/tree/WORK-IN-PROGRESS/machines/tsvetan>
#### Arch Linux
Distro refuses to support arm as an architecture or any contributions affiliated with it. The fork 'Arch Linux ARM' preliminary image is available on <http://git.dotya.ml/kreyren/teres-a64-arch-preliminary>
#### Parabola GNU/Linux
Compatibility patches submitted and should be supported. 
#### GNU Guix GNU/Linux
Patch submitted, but ignored by distro - <https://issues.guix.gnu.org/62024>
#### Gentoo Linux
Support provided through <https://github.com/khumarahn/teres1-gentoo>
#### PostmarketOS
In development, support submitted in <https://gitlab.com/postmarketOS/pmaports/-/merge_requests/4743>
Refer to the device's postmarketos wiki for details: <https://wiki.postmarketos.org/wiki/OLIMEX_Teres_i>
#### Alpine Linux
Was fully supported, but maintainer was inactive, now awaits linux kernel optimizations <https://gitlab.alpinelinux.org/alpine/aports/-/issues/15732>
Manual build instructions on <https://arvanta.net/alpine/alpine-on-olimex>, for automatic build see PostmarketOS's pmbootstrap. 
## Manual build
You can build things for yourself by following our [ Manual build howto][41400] and by choosing from the configurations available below. 
### The Bootloader
To begin with manual build you will need a U-Boot compiled with BL31.bin from ARM Trusted Firmware and SCP.bin from Crust to have a working power management mainly for suspend and hibernation. 
### Crust
To build crust proceed to download it's source code from <https://github.com/crust-firmware/crust> version higher or equal 6.0. 
Then refer to the [https://github.com/crust-firmware/crust?tab=readme-ov-file#prerequisites][41401] and [https://github.com/crust-firmware/crust?tab=readme-ov-file#building-the-firmware][41402] for instructions on how to build the firmware, in short you will need standard make and C dependencies with OpenRISC 1000 (not RISC-V) cross compiler. 
Prior to launching the compilation invoke `make teres_i_defconfig` to configure the compilation for the device. 
### Arm Trusted Firmware
For building ARM Trusted Firmware (AT-F) begin to download it's source code from <https://github.com/ARM-software/arm-trusted-firmware>, then refer to the documentation on <https://github.com/ARM-software/arm-trusted-firmware?tab=readme-ov-file> and build the BL31.bin binary. 
### U-Boot
The board is [[expected to be][41403]] fully supported since v2019.07. 
With both SCP.bin from Crust and BL31.bin from ARM Trusted Firmware above we can begin the U-Boot compilation. 
Start by downloading the source code from e.g. <https://github.com/u-boot/u-boot>, then export the environmental variables: 
  * SCP=/path/to/scp.bin/from/crust
  * BL31=/path/to/bl31.bin/from/at-f

Then refer to the documentation for build instructions: <https://docs.u-boot.org/en/stable/board/allwinner/sunxi.html>
When asked for boardname, use `teres_i_defconfig`. 
#### Sunxi/Legacy U-Boot
Use the `teres_i_defconfig` build target and hope for the best. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Fex file not provided, fixme? 
  

#### Mainline kernel
Use the _sun50i-a64-teres-i.dts_ device-tree binary. 
Linux-4.19 has most of the relevant drivers included and since 5.14 it should have all of the drivers implemented and track with mainline. 
U-Boot needs to be configured correctly (with teres_i_defconfig and not adjusting SUNXI_ variables) to initialize the PMIC and perform the powerup sequence described in kicad files for the display to work without issues. 
# Linux Kernel Configuration Reference
work in progress reference only 
The [dt_to_config][41404] script within the linux kernel can be used to obtain reference configuration generated from DeviceTree, dump available on <https://gitea.itycodes.org/itycodes/olimex-teres/src/branch/master/dt_dump.txt>
### Contiguous Memory Allocator (CMA)
[CMA][41405] is a memory allocator within the kernel which allows allocating large chunks of memory with contiguous physical memory addresses. 
[code] 
    CONFIG_CMA_SIZE_MBYTES 128
    
[/code]
Alternatively this option can be parsed in the kernel command line during bootloader phase: 
[code] 
     "cma=128M"
    
[/code]
  * **128M** is needed to prevent instability and crashes (mainly observed on GNOME)
  * **256M** is recommended for setup with [CEDRUS (Kernel Module)][41406] to manage hardware video decoding.

### Unified Extensible Firmware Interface (UEFI)
[code] 
    CONFIG_EFI=y # Enable EFI
    CONFIG_EFI_VARS_PSTORE=y
    CONFIG_PSTORE=y
    CONFIG_MISC_FILESYSTEMS=y
    CONFIG_EFI_STUB=y
    CONFIG_DMI=y
    CONFIG_EFI_ESRT=y
    CONFIG_EFI_PARAMS_FROM_FDT=y
    CONFIG_EFI_RUNTIME_WRAPPERS=y
    CONFIG_EFI_GENERIC_STUB=y
    
[/code]
### Battery
The device is using AXP803(QFN68_8x8mm) for power management. 
Confidence: Low, likely misses some configuration 
[code] 
    CONFIG_POWER_SUPPLY=y
    CONFIG_BATTERY_AXP20X=y # Seems to include drivers for AXP803 despite the name
    CONFIG_I2C=y
    CONFIG_MFD_AXP20X_I2C=y
    CONFIG_MFD_AXP20X=y
    CONFIG_IIO=y
    CONFIG_PINCTRL_AXP209=y
    INPUT_AXP20X_PEK=y
    INPUT_MISC=y # Unsure ifneeded
    
[/code]
### Wireless
The base model uses RTL8723BS: 
Confidence: Low, might miss some configuration 
[code] 
    CONFIG_RTL8723BS=y
    CONFIG_WIRELESS=y
    CONFIG_NET=y
    CONFIG_NETDEVICS=y
    CONFIG_WLAN=y
    CONFIG_MMC=y
    CONFIG_CFG80211=y
    CONFIG_STAGING=y
    
[/code]
### Display
For post-bootloader display initialization (initrd and the OS) assuming that the bootloader was able to initialize the power rails and the display: 
[code] 
    CONFIG_DRM=y
    CONFIG_DRM_ANALOGIX_ANX6345=y
    CONFIG_DRM_SUN4I=y
    CONFIG_DRM_SUN8I_MIXER=y
    CONFIG_SUN8I_TCON_TOP=y
    
    # TO BE FINISHED.. PATCHES WORK IN PROGRESS..
    CONFIG_DRM_SUN8I_DW_HDMI=y # For HDMI
    CONFIG_DRM_SUN6I_DSI=y # For MIPI-DSI
    
[/code]
Which translates to these modules: 
[code] 
    sun4i-drm
    sun4i-tcon
    sun8i-mixer
    sun8i_tcon_top
    gpu-sched
    drm
    drm_shmem_helper
    drm_kms_helper
    drm_dma_helper
    drm_display_helper
    analogix_anx6345
    analogix_dp
    
[/code]
# Tips, Tricks, Caveats
## FEL mode
The main PCB has a solder jumper labeled "UBOOT1", next to the internal expansion connector "CON3". A drop of solder will pull A64's ball F17 low and should activate [ FEL mode][41407]. The corresponding USB OTG however is only available on the internal extension connectors, so an appropriate breakout PCB seems to be the bigger task. 
# Modifications
The device is designed to be hackable without any limitations and is using industrial PCBs that make soldering on it very easy even if you don't know what you are doing. 
## Recommended
### Add VCC-in Fuse
In case the charging is too slow for you or you often change chargers, then [consider adding a fuse][41408] to the VCC-in to protect the internal electronics: 
[![Teres-fuse-mod.png][41409]][41410]
The stock charger can provide 5VDC3A. If charging it's too slow, probably the PMIC axp803 is configured for accepting max 1.5A, and cpu uses about 0.7A at idle, so only 0.8A remains for charging battery. 
You can increase the current from the plug changing the settings of the axp803 (I suggest 2.5A): 
  
# echo 2500000 > /sys/class/power_supply/axp813-ac/input_current_limit 
### Cut the power cable
To be able to charge teres from practically anything that provides the very common 5V 1~3A you can cut the power cable and use WAGO connectors for wire splicing or making a USB-A to Barrel Jack cable. 
### 3D print a new case
Out of the factory the devices comes with a generic case that can be found on chinese markets and their imports, you can find plans and 3D models online, but it's unknown if you can make changes and redistribute them. 
To address these concerns there is a 3D-printable case that also provides provides various quality of life improvements such as better management of the device's antenna within the case etc.. 
See <https://code.forksand.com/forksand/olimex-teres-case>
### Mount a heatspreader on the SoC and DRAM
The device is able to cool itself under normal load, but with e.g. aluminium heatspreader the device can be overclocked or kept at higher frequencies under extensive loads for longer. 
## Known
### AllWinner H64
The [H64][41411] is pin-compatible replacement for the device's [A64][41412] that improved H.264 decoding from 1080p to 4K resolutions and adds a TS interface. 
The software stack of A64 and H64 are very similar, but you will probably have to make software changes to get the H64 to work without issues on teres. 
### Faster eMMC chipset
The main bottleneck of teres's responsibility and performance is the eMMC while the MTFC32GAPALNA-AAT has been found to be pin-compatible, but the teres's mainboard might not be able to provide the needed power to run at optimal performance without a jumper-cable mod. 
You can also install the system on the microsd, modern microsd are cheap. 
# Adding a serial port
[![][41413]][41414]
[][41415]
DEVICE UART pads
PCB1 has solder pads for a 3-pin header. A horizontal pin header would however bump into the battery, once assembled. 
On Revision C boards, a serial port is provided through the audio jack. It can be enabled via an analog switch controlled by bit 9 on Port L, which has to be pulled low. Otherwise it will be a plain audio jack, as on Rev.B boards. You can find more information on [[Olimex github repo][41395]]. 
OLIMEX sell a specific cable: [[Teres usb debug][41416]]. The Pinebook debug cable also works. 
If you decide to build your adapter cable, connect the tx to the tip of the jack, rx to central ring, and ground to the sleeve: 
[code] 
    TX  RX
     |   |    
    === == ====|||||||||---------
             |
            GND
    
[/code]
They must be 3.3V compatible. 
The board's RX is protected with a diode ("D4"), so 5V should work as well. Never connect to a rs232 serial port directly. 
Usually usb serial adapters with 1/10" pin headers are 5v or 3.3v level compatible, but if in doubt, double check it. 
# Known issues
### Power connector wear
The power connector starts to expire after around 1000 insertions and needs to be serviced. 
  * <https://github.com/OLIMEX/DIY-LAPTOP/issues/67>

### Phone signal might disrupt audio
The cell phone signal on a phone put close to the device might produce static noise. 
  * <https://github.com/OLIMEX/DIY-LAPTOP/issues/59>

### Power-on power supply connection
The device powers on when connected to the power supply 
  * <https://github.com/OLIMEX/DIY-LAPTOP/issues/34>

### Disfunctional display when BL31.bin is compiled with SUNXI_SETUP_REGULATORS=0
The The Arm-Trusted-Firmware's BL31 is responsible for PMIC initialization that should be correctly printed in serial console as: 
[code] 
     U-Boot SPL 2024.01 (Jan 18 2024 - 19:32:49 +0100)
     DRAM: 2048 MiB
     Trying to boot from MMC1
     NOTICE:  BL31: v2.10.0	(debug):
     NOTICE:  BL31: Built : 01:25:38, Dec  4 2023
     NOTICE:  BL31: Detected Allwinner A64/H64/R18 SoC (1689)
     NOTICE:  BL31: Found U-Boot DTB at 0x20a2d98, model: Olimex A64 Teres-I
     INFO:    ARM GICv2 driver initialized
     INFO:    Configuring SPC Controller
     INFO:    PMIC: Probing AXP803 on RSB
     INFO:    PMIC: aldo1 voltage: 2.800V
     INFO:    PMIC: dcdc1 voltage: 3.300V
     INFO:    PMIC: dcdc5 voltage: 1.500V
     INFO:    PMIC: dcdc6 voltage: 1.100V
     INFO:    PMIC: dldo1 voltage: 3.300V
     INFO:    PMIC: dldo2 voltage: 2.500V
     INFO:    PMIC: dldo3 voltage: 1.200V
     INFO:    PMIC: dldo4 voltage: 3.300V
     INFO:    PMIC: fldo1 voltage: 1.200V
     INFO:    PMIC: Enabling DC SW
     INFO:    BL31: Platform setup done
     INFO:    BL31: Initializing runtime services
     INFO:    BL31: cortex_a53: CPU workaround for erratum 843419 was applied
     INFO:    BL31: cortex_a53: CPU workaround for erratum 855873 was applied
     INFO:    BL31: cortex_a53: CPU workaround for erratum 1530924 was applied
     INFO:    PSCI: Suspend is unavailable
     INFO:    BL31: Preparing for EL3 exit to normal world
     INFO:    Entry point address = 0x4a000000
     INFO:    SPSR = 0x3c9
    
[/code]
If your U-Boot initializes with: 
[code] 
     U-Boot SPL 2024.01 (Jan 20 2024 - 10:52:04 +0000)
     DRAM: 2048 MiB
     Trying to boot from MMC1
     NOTICE:  BL31: lts-v2.8.14(release):
     NOTICE:  BL31: Built : 10:47:18, Jan 20 2024
     NOTICE:  BL31: Detected Allwinner A64/H64/R18 SoC (1689)
     NOTICE:  BL31: Found U-Boot DTB at 0x20a2d98, model: Olimex A64 Teres-I
    
[/code]
Then you likely need to review your BL31.bin's compilation logs for the presence of 'SUNXI_SETUP_REGULATORS=0 such as [https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/59249/diffs#082488b14c7615f24feec8cd5916dfbd77c6a78d_41_41][41417]. 
This issue affected alpine's u-boot <=2024.01-r2 and was addressed in: 
  * <https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/59177>
  * <https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/59249>
  * <https://gitlab.alpinelinux.org/alpine/aports/-/commit/34e1f452115975ac88b04d3bbe0b75436a5b0f69>

### Broken ANX6345 on Linux 6.5+ (non-LTS version)
During discussion in <https://lore.kernel.org/linux-clk/4831731.31r3eYUQgx@jernej-laptop> about optimizing rate selection for NKM clocks it was proposed to set immune rate for pll-video0 instead of initial rate to enable a new functionalities [https://lore.kernel.org/linux-kernel/[email protected]][41418] which lead to the breakage of the ANX6345 (the Parallel LCD to eDP bridge module) initialization in Linux kernel starting during 6.5 development cycle: 
[https://lore.kernel.org/linux-sunxi/[email protected]/T/][41419]
Just in case you need to build kernel during the same cycle kernel, they may not boot for double free bug. This was the fix: 
<https://lore.kernel.org/lkml/CAJZ5v0jnGiQLWci3=-PM-8StYL4Dqa19HJhVLRVhDkvmuosjPA@mail.gmail.com/t/>
This patch was provided as a temporary hotfix to get the display on the device to work again on these kernels. 
[code] 
     diff --git a/drivers/clk/sunxi-ng/ccu-sun50i-a64.c b/drivers/clk/sunxi-ng/ccu-sun50i-a64.c
     index ea701bc51ade..fc906712a0ad 100644
     --- a/drivers/clk/sunxi-ng/ccu-sun50i-a64.c
     +++ b/drivers/clk/sunxi-ng/ccu-sun50i-a64.c
     @@ -200,7 +200,7 @@ static struct ccu_nkm pll_mipi_clk = {
      		.reg		= 0x040,
      		.hw.init	= CLK_HW_INIT("pll-mipi", "pll-video0",
      					      &ccu_nkm_ops,
     -					      CLK_SET_RATE_UNGATE | CLK_SET_RATE_PARENT),
     +					      CLK_SET_RATE_UNGATE),
      		.features	= CCU_FEATURE_CLOSEST_RATE,
      	},
      };
    
[/code]
Follow-up: [https://lore.kernel.org/lkml/[email protected]/][41420]
# Hardening
## Bootloader
If you are concerned about unauthorized write access to the SPI which is a common place for the bootloader firmware, you can bridge the pin WP1 with solder or add a physical swtich which will implement a hardware write protection to the SPI chip, refer to the documentation of [WINBOUND W25Q128FV][41421] to learn how this works. 
[![Teres-wp.png][41422]][41423]
Note that without additional changes the attacker may still be able to boot from USB or SDCard. 
# Pictures
Take some pictures of your device, [ upload them][41424], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][41425]][41426]
  * [![Device back.jpg][41427]][41428]
  * [![Device buttons 1.jpg][41429]][41430]
  * [![Device buttons 2.jpg][41431]][41432]
  * [![Device board front.jpg][41433]][41434]
  * [![Device board back.jpg][41435]][41436]

# See also
  * [TERES-I on Debian wiki][41437]
  * [TERES-I on PostmarketOS wiki][41438]
  * [Teres on NixOS wiki][41439]
  * [Itycodes' documentation for the A64 kernel modules][41440]
  * [Itycodes' teres-I docs][41441]
  * [NixOS issue about crashes in GNOME, CMA-related][41442]

## Manufacturer images
The legacy OLIMEX image of Ubuntu Mate can be downloaded, using torrent. It uses allwinner provided linux kernel 3.10 and u-boot, but are not recommended for a daily use. 
[[[1]][41443]]
