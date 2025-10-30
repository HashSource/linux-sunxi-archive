# Linux mainlining history
This page contains history of mainlining effort up to kernel version 4.18. Newer versions can be seen on the main [Sunxi Linux Mainlining Effort][32357] page. 
## Contents
  * [1 Merged into 4.18][32358]
  * [2 Merged into 4.17][32359]
  * [3 Merged into 4.16][32360]
  * [4 Merged into 4.15][32361]
  * [5 Merged into 4.14][32362]
  * [6 Merged into 4.13][32363]
  * [7 Merged into 4.12][32364]
  * [8 Merged into 4.11][32365]
  * [9 Merged into 4.10][32366]
  * [10 Merged into 4.9][32367]
  * [11 Merged into 4.8][32368]
  * [12 Merged into 4.7][32369]
  * [13 Merged into 4.6][32370]
  * [14 Merged into 4.5][32371]
  * [15 Merged into 4.4][32372]
  * [16 Merged into 4.3][32373]
  * [17 Merged into 4.2][32374]
  * [18 Merged into 4.1][32375]
  * [19 Merged into 4.0][32376]
  * [20 Merged into 3.19][32377]
  * [21 Merged into 3.18][32378]
  * [22 Merged into 3.17][32379]
  * [23 Merged into 3.16][32380]
  * [24 Merged into 3.15][32381]
  * [25 Merged into 3.14][32382]
  * [26 Merged into 3.13][32383]
  * [27 Merged into 3.12][32384]
  * [28 Merged into 3.11][32385]
  * [29 Merged into 3.10][32386]
  * [30 Merged into 3.9][32387]
  * [31 Merged into 3.8][32388]

## Merged into 4.18
Driver Changes 
  * A33 
    * MIPI DSI

  * A83t 
    * SMP Support

  * H6 
    * R_CCU / PRCM
    * R_PIO

  * R40 
    * EMAC support

Device Tree Changes 
  * A33 
    * MIPI DSI

  * A83t 
    * SMP Support
    * SID

  * H3 / H5 
    * R_I2C
    * CPUFreq

  * H6 
    * R_CCU / PRCM
    * R_PIO
    * R_INTC
    * R_I2C 
      * PCF8563 RTC for [PineH64][32389]

  * R40 
    * EMAC support 
      * Ethernet enabled for [Banana Pi M2 Ultra][32390]

New Devices Supported 
  * [Nintendo NES Classic Edition][32391]
  * [Libre Computer Board ALL-H3-CC‎][32392] ver. H2+ / H5
  * [Olimex A20-SOM-EVB-eMMC][32393]

## Merged into 4.17
Driver changes 
  * A80 
    * SMP

  * A83T 
    * HDMI support
    * PMIC ADC and Battery power supply support

  * H3 / H5 
    * HDMI support

  * H6 
    * Basic support
    * PIO pinctrl support (R_PIO not supported)
    * CCU clock/reset support (R_CCU/PRCM not supported)

Device tree changes 
  * A64 
    * SimpleFB
    * I2S
    * SPDIF
    * Watchdog

  * SPI enabled for [Orange Pi R1][32394]

  * SDIO WiFi enabled for [FriendlyARM NanoPi NEO Air][32395]

  * eMMC enabled for [FriendlyARM Nanopi M1 Plus][32396], [FriendlyARM NanoPi NEO Air][32395]

  * HDMI video output enabled for [MK802][32397], [MK808C][32398], [Mele I7][32399], [Banana Pi M3][32400], [Banana Pi][32401], [Orange Pi Mini][32402], [Banana Pi M2+][32403], [Beelink X2][32404], Libre Computer ALL-H3-CC, [FriendlyARM NanoPi M1][32405], [Xunlong Orange Pi 2][32406], [Xunlong Orange Pi Lite][32407], [Xunlong Orange Pi One][32407], [Orange Pi PC][32408], [Orange Pi PC 2][32409], [Xunlong Orange Pi Prime][32410], [Xunlong Orange Pi Zero Plus 2][32411]

  * LEDs enabled for [Banana Pi M3][32400]

  * VGA output enabled for [Cubieboard 4][32412]

  * Audio codec enabled for [Olimex A33-OLinuXino][32413]

  * Power supplies enabled for [Olimex A33-OLinuXino][32413], [A23/A33 reference tablet design][32414], [TBS A711][32415] (battery only)

New devices supported 
  * [Olimex TERES-I laptop][32416]
  * [Olimex A20-SOM204][32417]
  * [PineH64][32389]
  * [Sinovoip Banana Pi M2 Zero][32418]
  * [Xunlong Orange Pi Zero Plus][32419]

## Merged into 4.16
Drivers: 
  * Display 
    * LVDS support
    * DE2 (multi-plane support, HW scaling)
  * [A83T][32420]
    * Display (LCD) support
    * I2S support
  * [H3][32421]/[H5][32422]
    * SimpleFB support

Device tree changes: 
  * SoC specific 
    * [A83T][32420]
      * [I2C][32423], [I2S][32424] added
      * First display pipeline ([LCD][32425]/LVDS)
      * GPIO for AXP81x PMIC
    * [H3][32421]/[H5][32422]
      * SimpleFB

  * Board specific 
    * Audio codec enabled for [ Olimex A13-Olinuxino][32426]
    * WiFi/BT enabled for [Xunlong Orange Pi Zero Plus 2][32411]
    * AXP803 regulators added for [Xunlong Orange Pi Win][32427]
    * EMAC enabled for [FriendlyARM NanoPi NEO Plus2][32428], [Cubietech Cubietruck Plus][32429], [Sinovoip Banana Pi M3][32430], [FriendlyARM NanoPi M1][32405]
    * USB OTG enabled for [FriendlyARM NanoPi NEO][32431]
    * LEDs enabled for [Sinovoip Banana Pi M64][32432]
    * HDMI enabled for [LinkSprite pcDuino3 Nano][32433]

New boards supported: 
  * [Xunlong Orange Pi R1][32434]
  * [Libre Computer Board ALL-H3-CC][32392] (H3 variant)

## Merged into 4.15
Drivers: 
  * [A10][32435]/[A20][32436]/[A31][32437]
    * display
    * HDMI controller
  * sunxi-ng clocks 
    * audio PLL sigma-delta modulation support for accurate audio playback
  * [A33][32438]
    * Audio codec fixes
  * [A64][32439]
    * DMA controller

Device tree changes: 
  * SoC specific 
    * [A10][32435]/[A20][32436]
      * CCU sunxi-ng style clock conversion
      * Display pipeline
      * HDMI controller
    * [A31][32437]
      * HDMI controller
      * I2S controllers
    * [A64][32439]
      * DMA controller
      * EMAC
      * SPI
    * [H3][32421]/[H5][32422]
      * EMAC
    * [R40][32440]
      * Basic dtsi
      * Watchdog
      * USB

  * Board specific 
    * IR receiver for [FriendlyARM NanoPi M1][32405]
    * WiFi, BT and IR receiver for [FriendlyARM Nanopi M1 Plus][32396]
    * HDMI enabled on [Merrii Hummingbird A31][32441], [Sinlinx SinA31s][32442], [MSI Primo81][32443], [Cubietech Cubieboard][32444], [Cubietech Cubieboard2][32445], [Cubietech Cubietruck][32446], [Banana Pi M1+][32447], [Olimex A10-OLinuXino-Lime][32448], [Olimex A20-OLinuXino-Lime][32449], [Olimex A20-OLinuXino-Lime2][32450], [Olimex A20-OLinuXino-Micro][32451]
    * ACIN and Battery power supplies enabled on [Lamobo R1][32452] and A13 reference design tablets
    * AXP803 PMIC regulators and WiFi enabled for [Allwinner A83TDevBoard][32453], [Banana Pi M3][32400], [Cubietech Cubietruck Plus][32429]
    * AXP803 PMIC regulators and USB OTG enabled for [TBS A711][32415]
    * EMAC re-enabled for various [A64][32439]/[H3][32421]/[H5][32422] boards

  * Cleanups 
    * Removal of GPIO pinmux settings for [A10][32435] and [A80][32454]

New boards supported: 
  * [TBS A711][32415]
  * [FriendlyARM NanoPi NEO Plus2][32428]
  * [Olimex A20-OLinuXino-Micro][32451] eMMC variant
  * [Sinovoip Banana Pi M2 Berry][32455]
  * [Sinovoip Banana Pi M2 Ultra][32456]

## Merged into 4.14
Drivers: 
  * [A10s][32457]
    * HDMI DDC I2C Adapter
    * HDMI CEC support
  * most of Allwinner SoC 
    * sun4i-ss SecuritySystem PRNG driver
  * [A10][32435]/[A20][32436]
    * CCU Clock-ng support
  * [A10][32435]/[A20][32436]/[A31][32437]/[A33][32438]/[H3][32421]
    * MUSB fixes [(commit)][32458] [(commit)][32459]
  * [A64][32439]
    * SRAM controller driver
  * [A83T][32420]
    * SD/MMC support
    * AXP813 PMIC
    * USB support
  * [H3][32421]
    * [I2S][32424] support
  * [R40][32440]
    * CCU sunxi-ng style clock driver support
    * pinctrl support

  * AXP PMICs 
    * PEK time fix for AXP22x

Device tree changes: 
  * SoC specific 
    * [A83T][32420] / [A64][32439]
      * R_INTC interrupt controller
    * [A83T][32420]
      * RSB support
      * SD/MMC support
      * AXP813 PMIC and codec
      * USB host support

  * Board specific 
    * AXP803 basic support and regulators for [Pine64][32460] and [SoPine][32461]
    * USB and WiFi enabled for [Sinovoip Banana Pi M64][32432]
    * ~~Ethernet for[Beelink X2][32404]~~
    * USB OTG for [Beelink X2][32404]
    * SD/MMC for [Cubietech Cubietruck Plus][32429] and [Allwinner A83TDevBoard][32453]
    * AXP813 PMIC for [Cubietech Cubietruck Plus][32429] and [Allwinner A83TDevBoard][32453]
    * AC100 chip for [Cubietech Cubietruck Plus][32429] and [Allwinner A83TDevBoard][32453]
    * USB hosts for [Cubietech Cubietruck Plus][32429] and [Allwinner A83TDevBoard][32453]

New boards supported: 
  * [Olimex A64-OLinuXino][32462]
  * [FriendlyARM NanoPi A64][32463]
  * [Sinovoip Banana Pi M2 Magic][32464]
  * [Sinovoip Banana Pi M3][32430]

## Merged into 4.13
Drivers: 
  * [A10s][32457]
    * HDMI support

  * [V3s][32465]
    * Clock driver for Display Engine 2.0
    * DRM/KMS display driver support for Display Engine 2.0
    * codec support

  * [A64][32439] / [A83T][32420] / [H2+][32466] / [H3][32421] / [H5][32422]
    * ~~dwmac-sun8i ethernet driver~~ Unfinished due to unstable DT binding

  * [A83T][32420]
    * Clock driver

Device tree changes: 
  * SoC Specific 
    * LRADC, MMC1, SPI, Display Engine 2.0 for [V3s][32465]

  * Board Specific 
    * Enable AXP PMIC battery support on [NextThingCo CHIP][32467], [Sinlinx SinA33][32468]
    * Enable USB OTG on [Banana Pi M2+][32403], [Orange Pi PC][32408], [ Orange Pi PC Plus][32469], [Orange Pi Plus 2E][32470]
    * Enable dedicated USB hosts for USB OTG on [Pine64][32460]
    * ~~Enable dwmac-sun8i for Ethernet on various boards~~ Removed due to unstable DT binding

Added board support: 
  * [FriendlyARM NanoPi NEO2][32471]
  * [Xunlong Orange Pi Prime][32410]
  * [Xunlong Orange Pi Win][32427]
  * [ Orange Pi Zero Plus 2 H5][32472]
  * [LicheePi Zero][32473] dock board

## Merged into 4.12
  * [H3][32421]
    * USB OTG support

  * [H5][32422]
    * New SoC variant, similar to [H3][32421], but ARM64 with Cortex-A53 cores.
    * pinctrl driver
    * CCU (sunxi-ng) driver
    * USB OTG support

  * [A31][32437]/[H3][32421] SPI 
    * Support transfers larger than 64 bytes

  * AXP PMICs 
    * AXP803 basic support
    * ACIN Power Supply driver
    * ADC IIO driver
    * Battery Power Supply driver

Added board support: [FriendlyARM NanoPi NEO Air][32395], [Xunlong Orange Pi PC 2][32474]
## Merged into 4.11
  * [A23][32475]
    * Audio codec device tree changes

  * [A31][32437]
    * SPDIF output support

  * [A33][32438]
    * cpufreq support
    * Audio codec support

  * [A64][32439]
    * MMC Support
    * USB support

  * [A80][32454]
    * sunxi-ng style clock support

  * [H2+][32466]
    * New SoC variant, similar to [H3][32421]

  * [H3][32421]
    * Audio codec device tree changes
    * SPDIF output support

  * [V3s][32465]
    * New SoC support
    * USB PHY driver
    * pinctrl driver
    * CCU driver

Added board support: [LicheePi One][32476], [Xunlong Orange Pi Zero][32477], [LicheePi Zero][32473], [Sinovoip Banana Pi M64][32432]
## Merged into 4.10
  * [A23][32475]
    * Audio Codec driver

  * [A31][32437]/[A31s][32478]
    * Display Driver (first pipeline)
    * Audio Codec support

  * [A64][32439]
    * Clock driver

  * [A80][32454]
    * External SDIO WiFi

  * [H3][32421]
    * Audio Codec driver
    * SPI

Added board support: NextThingCo CHIP Pro, [Pine64][32460], [FriendlyARM NanoPi M1][32405]
## Merged into 4.9
  * [GR8][32479]
    * SoC Support

  * [AXP209][32480]
    * GPIO support

  * [A31][32437]
    * SPDIF support

  * [A23][32475]/[A33][32438]
    * sunxi-ng CCU driver

  * [A31][32437]/[A31s][32478]
    * sunxi-ng CCU driver

  * [A33][32438]
    * Display Driver

  * [A64][32439]
    * USB PHY support

  * [H3][32421]
    * PWM support (commit)]
    * I2C support

  * AXP806 PMIC 
    * regulator support

  * AC100 RTC / codec IC 
    * mfd driver
    * RTC driver

Added board support: [ Orange Pi PC Plus][32481], [Olimex A33-OLinuXino][32413], [Xunlong Orange Pi Lite][32482], [Inet q972][32483], [Empire Electronix M712][32484], [Xunlong Orange Pi Plus 2][32485], [Xunlong Orange Pi Plus 2E][32486], [FriendlyARM NanoPi NEO][32431], 
## Merged into 4.8
  * [A10][32435]/[A20][32436]
    * Display engine clocks (TCON, FE, DE)
    * I2S audio interface driver

  * [H3][32421]
    * Clocks (through sunxi-ng)
    * USB multi-reset lines support
  * AXP2xx driver: 
    * External drivebus support
    * AXP223 USB power supply support
    * AXP809 PMIC support

  * [BCM53125 support][32487]
    * This switch is used in [Lamobo / Banana Pi R1][32452]

Added board support: [ Banana Pi M2+ H2+][32488], [ Banana Pi M1+][32489]
## Merged into 4.7
  * [A13][32490]/[R8][32491]
    * Display Engine support

  * [A10][32435]/[A20][32436]
    * SPDIF Support

  * [A31][32437]/[A23][32475]/[H3][32421] DMAengine improvements for H3 audio support (WiP: Jean-Francois Moine) [patch-v6][32492]

  * [H3][32421]
    * USB support (multi-reset line support delayed til 4.8)

Added board support: 
  * [Xunlong Orange Pi One][32493]
  * [Xunlong Orange Pi 2][32406]
  * [Xunlong Orange Pi PC][32494]
  * Dserve DSRV9703C
  * Polaroid MID2809PXE4
  * colorfly e708 q1
  * Difrence DIT4350

## Merged into 4.6
  * [![Sticky-note-pin.png][32495]][32496] _Note:_ For devices that use eMMC, old device trees may no longer work with this version (i.e. you have to rebuild your _.dtb_ files). Expect eMMC I/O errors otherwise.

  * Allwinner [A83T][32420] support 
    * Initial bringup
    * timer, watchdog and reboot

  * [H3][32421]
    * R_PIO support

  * [A64][32439]
    * pinctrl driver
    * generic arm64 Allwinner platform (ARCH_SUNXI) support

  * NAND 
    * ECC layout definition rework (partially) and randomizer support

  * A10/A20 SPDIF driver

  * AXP223 PMIC support

  * eMMC HS-DDR support for all currently supported SoCs except [A80][32454]

Added board support: [Allwinner A83TDevBoard][32453], [Cubietech Cubietruck Plus][32429]
## Merged into 4.5
  * Allwinner [A80][32454] support 
    * IR receiver driver
    * NMI controller
    * PRCM driver
    * R_PIO support
    * RSB driver

  * Allwinner H3 SoC support 
    * H3 USB PHY clocks

  * A10/A20 Video Engine clocks

  * MIC1 capture for sun4i codec

  * Audio codec enabled on various boards

Added board support: [Xunlong Orange Pi Plus][32497]
[![Exclamation.png][32498]][32499] Known problems:
  * Release tag v4.5 contains a change that broke _stmmac_ networking on quite a few sunxi devices. The symptoms are

[code] 
    [ 13.196778] libphy: PHY stmmac-0:ffffffff not found
    [ 13.204800] eth0: Could not attach to PHY
    [ 13.204809] stmmac_open: Cannot attach to PHY (error: -19)
[/code]
A quick fix is to revert commit **88f8b1b** which introduced the regression. See <http://lists.infradead.org/pipermail/linux-arm-kernel/2016-March/415939.html>, [https://www.mail-archive.com/[email protected]/msg104119.html][32500], <https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=823493>.  
Version _v4.5-rc7_ is known to be still okay, _v4.6-rc2_ fixes stmmac again. 
## Merged into 4.4
  * [R8][32491] SoC support

  * [A10][32435] / [A20][32436]
    * CAN driver [(commit)][32501]

  * [A10][32435] / [A10s][32457] / [A13][32490] / [A20][32436]
    * Audio Codec driver
    * Audio clocks (PLL2)
    * Audio codec related DTS bits 
      * Enabled on [Cubieboard][32502], [Cubieboard2][32503], [Cubietruck][32504], [ C.H.I.P.][32467], [Mele A1000][32505]

  * [A23][32475] / [A33][32438]
    * RSB (Reduced Serial Bus) driver
    * PWM enabled

  * [A83T][32420]
    * PIO driver

  * [AXP202][32506]/[AXP209][32480]
    * USB power supply driver
    * Support for OTG vbus detection via AXP pmic
    * DTS nodes for OTG vbus support

Added board support: Olimex A20 EVB [(commit)][32507], Unified Q8 format tablet, Wits Pro A20 DKT [(commit)][32508], Yones Toptech bs1078v2 [(commit)][32509], Wobo i5 [(commit)][32510], [ C.H.I.P.][32467] [(commit)][32511], [Sinlinx SinA31s][32442], [MSI Primo81][32443] [(commit)][32512], [Sinovoip Banana Pi M2][32513] [(commit)][32514]
## Merged into 4.3
  * [A10][32435] / [A13][32490] / [A20][32436] / [A23][32475] / [A31][32437]
    * Enable OTG controller [(commit)][32515]

  * [A10][32435] / [A10s][32457] / [A13][32490] / [A20][32436]
    * Support for DMA engine

  * [A23][32475] / [A33][32438]
    * Support for USB-controllers

  * most of Allwinner SoC 
    * Support for [Security System][32516] [(commit)][32517]

  * [AXP152][32518]
    * AXP152 mfd support

Added board support: Iteaduino Plus A10, Ippo-q8h-a33 v1.2 
## Merged into 4.2
  * [A10][32435] / [A10s][32457] / [A13][32490] / [A20][32436] / [A31][32437] / [A23][32475]
    * SRAM Controller

  * [A23][32475]
    * SMP support [(commit)][32519]
    * Architected timer support

  * [A31][32437]/[A31s][32478]
    * CPUFreq support

  * [A33][32438]
    * Machine support [(commit)][32520]
    * Bring-up sharing most drivers with [A23][32475]
    * pinctl driver [(commit)][32521]
    * PIO controller [(commit)][32522]

  * [A80][32454]
    * Architected timer support
    * USB support

  * [AXP221][32523] PMIC driver

  * [H3][32421]
    * Introduce H3 support [(commit)][32524]
    * DMA Controller [(commit)][32525]

Added board support: [LinkSprite pcDuino3 Nano][32433], [Cubietech Cubieboard4][32412], [Gemei G9][32526], [Auxtek T004][32527], [Utoo P66][32528], [Wexler TAB 7200][32529], [MK808C][32398], [Jesurun Q5][32530], [Xunlong Orange Pi][32531], [Xunlong Orange Pi Mini][32532], [Sinlinx SinA33][32468]
## Merged into 4.1
  * [A80][32454]
    * USB PHY driver

  * [AXP202][32506]/[AXP209][32480]
    * DT bindings

## Merged into 4.0
  * [A10][32435] / [A20][32436]
    * PS/2 Controller

  * [A13][32490] / [A31][32437]
    * IR receiver

  * [A31s][32478]
    * bring-up sharing majority of drivers with [A31][32437]
    * pinctrl driver
    * Touchscreen controller

  * [A80][32454]
    * MMC

  * All SoCs 
    * LRADC Input driver
    * CPUFreq
    * PWM Driver

  * AXP209 power button input driver

Added board support: [CSQ CS908][32533], [LeMaker Banana Pro][32534], [Chuwi V7 CW0825][32535], [Rikomagic mk802][32536], [Rikomagic mk802ii][32537], [Rikomagic mk802_a10s][32538], [MarsBoard A10][32539], [Hyundai A7HD][32540]
## Merged into 3.19
  * [A10][32435] / [A10s][32457] / [A13][32490] / [A20][32436] / [A31][32437] / [A23][32475]
    * Simple Framebuffer 
      * In order to use that, you'll need a recent mainline u-boot (2015.01+)
    * USB phy driver support for usb0

  * [A10][32435] / [A20][32436]
    * NAND [[1]][32541]
      * Only works for SLC NAND for now
      * Some additional work is needed for MLC NANDs

  * [A23][32475]
    * DMAengine driver (shared with A31) [[2]][32542]

  * [A80][32454]
    * initial machine support [[3]][32543]
    * basic clocks and reset [[4]][32544]
    * pinctrl driver [[5]][32545]
    * extra UART, I2C, LEDS [[6]][32546]

Related merges: [sunxi-simplefb-for-3.19][32547]
Added board support: [Mele M3][32548], [LeMaker Banana Pi][32549], [Merrii A80 Optimus Board][32550], [Olimex A20-OLinuXino-Lime2][32450]
## Merged into 3.18
  * [A31][32437]/[A23][32475]
    * RTC [[7]][32551]
    * Watchdog [[8]][32552]

  * [A23][32475]
    * MMC
    * pinctrl
    * DMA
    * I2C

Added board support: [Olimex A20-OLinuXino-Lime][32449], [Merrii Hummingbird A20][32553], [HSG H702][32554]
## Merged into 3.17
  * A10/A20 
    * IR driver

  * A31 
    * PIO/R_PIO external interrupts
    * DMAengine
    * GMAC

  * A23 
    * Timers, UARTs, initial bringup
    * Basic clocks
    * PIO/R_PIO drivers

Related merges: [clk-for-linus-3.17][32555], [mfd-for-linus-3.17][32556], [pinctrl-v3.17-1][32557], [soc-for-3.17][32558], [dt-for-3.17][32559], [slave-dma for-linus][32560], [v4l_for_linus][32561], 
Added Board Support: [Merrii Hummingbird A31][32441], BA10, [LinkSprite pcDuino V3][32562], [Ippo q8h][32563]
## Merged into 3.16
  * AXP20x regulator support

  * All 
    * MMC support

  * A31 
    * USB support
    * PRCM
    * SMBus Regmap
    * Special Pins Muxer
    * P2WI Controller

  * A10 
    * Touchscreen controller [[9]][32564]
    * Touchscreen controller temperature sensor [[10]][32565]

Related Merges: [defconfig-for-3.16][32566], [drivers-for-3.16][32567], [dt-for-3.16][32568], [soc-for-3.16][32569], [usb-3.16-rc1][32570], [pinctrl-v3.16-1][32571], [clk-for-linus-3.16][32572], [clk-for-linus-3.16-part2][32573], [mmc-updates-for-3.16-rc1][32574], [mfd-for-linus-3.16][32575], [regulator-v3.16][32576], [input-for-linus][32577]
Added board support: [Mele M9][32578], [R7][32579]
## Merged into 3.15
  * All SoCs 
    * SPI
  * A10/A10s/A13/A20 
    * OHCI
    * EHCI
  * A10/A20 
    * AHCI
  * A20/A31 
    * NMI controller
  * A20 
    * GMAC
  * A31 
    * I2C

Related merges: [[11]][32580], [[12]][32581], [[13]][32582], [[14]][32583], [[15]][32584], [[16]][32585], [[17]][32586]
Added board support: [LinkSprite_pcDuino][32587], [Inet 97f][32588], [A10-OLinuXino-LIME][32589]
## Merged into 3.14
  * A31 
    * Reset Controller Support
    * SMP
  * A20 
    * SMP (via PSCI)
    * External clock outputs
  * High Speed Timers
  * RTC driver (A10/A20) [(commit)][32590]
  * RTP (DT only)
  * GMAC support in stmmac driver
  * AP6210 WiFi (BCM43362) support in brcmfmac driver

Related merges: [[18]][32591], [[19]][32592], [[20]][32593], [[21]][32594], [[22]][32595]
Added board support: [Olimex A13-OLinuXino-Micro][32596] [(commit)][32597]
## Merged into 3.13
  * SID Driver
  * I2C for A20
  * sunxi_defconfig
  * Bug fixes [[23]][32598]

Added board support: [Cubietruck][32504]
## Merged into 3.12
  * A31 support 
    * Basic SoC + GPIO
    * Clock support
  * A20 support 
    * Basic SoC + GPIO
    * Clock support
  * A10s clocks
  * Clock Source and Clock Event rework
  * Watchdog driver

Related merges: [[24]][32599], [[25]][32600], [[26]][32601], [[27]][32602], [[28]][32603], [[29]][32604]
Added board support: [A31 EVB][32605], [A20-OLinuXino-Micro][32606], [Cubieboard2][32503], [Mele A1000][32505]
## Merged into 3.11
  * IRQ support for the PIO
  * I2C Driver
  * EMAC Driver
  * A10s support

Related merges: [[30]][32607], [[31]][32608], [[32]][32609], [[33]][32610], [[34]][32611], [[35]][32612]
Added board support: [Olimex A10s-OLinuXino-Micro][32613]
## Merged into 3.10
  * LED support
  * Clock driver
  * Complete UART support

Related merges: [[36]][32614], [[37]][32615], [[38]][32616]
Added Board Support: [Pineriver_H24][32617]
## Merged into 3.9
  * PINCTRL driver
  * GPIO-lib based driver

Related merges: [[39]][32618]
Added Board Support: [Miniand_Hackberry][32619]
## Merged into 3.8
  * Initial support for Allwinner SoCs [(commit)][32620]
  * Timer [(commit)][32621]
  * UART
  * Device Tree
  * Interrupt controller [(commit)][32622]

Related merges: [[40]][32623], [[41]][32624]
Added board support: [Cubieboard][32502], [A13-OLinuXino][32625]
