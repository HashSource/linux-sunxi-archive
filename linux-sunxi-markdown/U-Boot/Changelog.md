# U-Boot/Changelog
< [U-Boot][56207]
 
## Contents
  * [1 Status][56210]
    * [1.1 In Progress][56211]
    * [1.2 Next Release (v2019.07)][56212]
    * [1.3 v2019.04][56213]
    * [1.4 v2019.01][56214]
    * [1.5 v2018.11][56215]
    * [1.6 v2018.09][56216]
    * [1.7 v2018.07][56217]
    * [1.8 v2018.05][56218]
    * [1.9 v2018.03][56219]
    * [1.10 v2018.01][56220]
    * [1.11 v2017.11][56221]
    * [1.12 v2017.09][56222]
    * [1.13 v2017.07][56223]
    * [1.14 v2017.05][56224]
    * [1.15 v2017.03][56225]
    * [1.16 v2017.01][56226]
    * [1.17 v2016.11][56227]
    * [1.18 v2016.09][56228]
    * [1.19 v2016.07][56229]
    * [1.20 v2016.05][56230]
    * [1.21 v2016.03][56231]
    * [1.22 v2016.01][56232]
    * [1.23 v2015.10][56233]
    * [1.24 v2015.07][56234]
    * [1.25 v2015.04][56235]
    * [1.26 v2015.01][56236]
    * [1.27 v2014.10][56237]
    * [1.28 v2014.07][56238]

# Status
The current U-Boot release fully supports major functions (except NAND) on all the older Allwinner SoCs ([A10][56239]/[A10s][56240]/[A13][56241]/[A20][56242]/[A23][56243]/[A31][56244]/[A31s][56245]) and has basic support for the more recent [A33][56246], [A64][56247], [A80][56248], [A83T][56249], [H2+][56250], [H3][56251], [H5][56252], and [V3s][56253](No MPI-DSI Lcd). 
The next release will be v2019.07. 
See also: [U-Boot Release Cycle and Release Schedule][56254]. 
## In Progress
  * [A83T][56249] USB support (WiP: Chen-Yu Tsai (wens)) [patch-rfc][56255]
  * [A83T][56249] PSCI support (WiP: Timothy Pearson) [patch-rfc][56256]
  * [H2+][56250]/[H3][56251]/[A64][56247] HDMI / Composite out support (WiP: Jernej Škrabec) [git-repo][56257]
  * [A20][56242] SPI driver (WiP: Stephan van Schaik (Swabbles)) [patch-rfc][56258] [git-repo][56259]
  * [A31][56244]/[A80][56248]/[A64][56247] SPI driver (WiP: Philipp Tomsich) [patch-v1][56260]
  * [R40][56261] [Banana Pi M2 Ultra][56262] support (WiP: Chen-Yu Tsai (wens)) [patch][56263]

## Next Release (v2019.07)
[Development branch][56264]
  * Boards 
    * [Beelink GS1][56265]
    * [Oceanic 5205 5inMFD][56266]
    * [Olimex Teres-A64][56267]

## v2019.04
[v2019.04 Release branch][56268]
  * Boards 
    * [Emlid Neutis N5][56269]

## v2019.01
[v2019.01 Release branch][56270]
  * Boards 
    * [Pine Pinebook][56271]
    * [Pine Pine64-LTS][56272]
    * [Sinovoip Banana Pi M2 Zero][56273]
    * [Xunlong Orange Pi Lite 2][56274]

## v2018.11
[v2018.11 Release branch][56275]
## v2018.09
[v2018.09 Release branch][56276]
  * Boards 
    * [ Pine64 SoPINE][56277]
    * [Xunlong Orange Pi One Plus][56278]
    * [PineH64][56279]

## v2018.07
[v2018.07 Release branch][56280]
  * Boards 
    * [ Orange Pi R1 ][56281]
    * [Libre Computer Board ALL-H3-CC‎][56282], H2+ version
    * [Libre Computer Board ALL-H3-CC‎][56282], H5 version
    * [Orange Pi Zero Plus][56283]
    * [ Banana Pi M2 Berry][56284]

## v2018.05
[v2018.05 Release branch][56285]
  * Boards 
    * [Olimex A20-SOM204-EVB][56286]
    * [Olimex A20-SOM204-EVB][56286] with eMMC

## v2018.03
[v2018.03 Release branch][56287]
  * Boards 
    * [Libre Computer Board ALL-H3-CC‎][56282], H3 version

## v2018.01
[v2018.01 Release branch][56288]
  * Boards 
    * [NanoPi NEO Plus 2][56289]
    * [TBS A711][56290]

## v2017.11
[v2017.11 Release branch][56291]
  * Boards 
    * [Olimex A20-OLinuXino-Micro][56292] eMMC variant
    * [FriendlyARM Nanopi M1 Plus][56293]
    * [Sinovoip Banana Pi M2][56294] Magic

## v2017.09
[v2017.09 Release branch][56295]
  * Boards 
    * [ NanoPi A64 ][56296]
    * [ OLinuXino Lime2 (A20)][56297] with eMMC
    * [ OLinuXino A64][56298]

## v2017.07
[v2017.07 Release branch][56299]
  * Boards 
    * [Xunlong Orange Pi Win][56300] and Win Plus
    * [Xunlong Orange Pi Prime][56301]
    * [Xunlong Orange Pi Zero Plus 2][56302]

## v2017.05
[v2017.05 Release branch][56303]
  * [A64][56247] SPL support
  * [H5][56252] support (with SPL)
  * Boards 
    * [Xunlong Orange Pi PC 2][56304]
    * [FriendlyARM NanoPi NEO Air][56305]

## v2017.03
[v2017.03 Release branch][56306]
  * [enable H3 EMAC for the nanopi neo][56307]
  * [add proper device tree for Orange Pi Zero boards][56308]
  * [OrangePi Zero: defconfig: enable SPI flash][56309]
  * [OrangePi Zero: add Ethernet node][56310]

## v2017.01
[v2017.01 Release branch][56311]
  * add support for [Nintendo NES Classic Edition][56312]

## v2016.11
[v2016.11 Release branch][56313]
  * Hans de Goede and Ian Campbell step down as U-boot Sunxi maintainers

  * A80 
    * Full SPL support

  * A64 
    * USB support

  * H3 
    * DRAM impedance calibration fixes

  * Boards 
    * [FriendlyARM NanoPi NEO][56314]
    * [Sinlinx SinA33][56315]
      * USB host and OTG support
    * [Cubietech Cubieboard4][56316]

## v2016.09
[v2016.09 Release branch][56317]
  * General 
    * GPIO fixes
    * PSCI rewrite in C part 2
    * NAND controller driver
    * H3/A64 Ethernet (EMAC) support

  * Boards 
    * [Empire Electronix M712][56318]
    * [Inet Q972][56319]
    * [Olimex A33-OLinuXino][56320]
    * [ Xunlong Orange Pi PC Plus][56321]
    * [Xunlong Orange Pi Plus 2E][56322]

## v2016.07
[v2016.07 Release branch][56323]
  * AXP809 PMIC support

  * PSCI rewrite in C part 1

  * Boards 
    * [Allwinner R16 EVB][56324]
    * [Inet 86dz][56325]
    * [Polaroid MID2407PXE03][56326]

## v2016.05
[v2016.05 Release branch][56327]
  * [A23][56243]
    * Support new revisions

  * [A64][56247]
    * 64-bit ARMv8 port, basic support (MMC, UART, no USB, no Ethernet)
    * (basic) EFI support (allows booting EFI applications (like grub) or kernels)

  * I2C support fix for families with separate reset control

  * SID e-fuse support for A83T and H3

  * Sync up dts files with Linux kernel
  * Update compatible strings for GPIO

  * Boards 
    * colorfly e708 q1, Difrence DIT4350, Polaroid MID2809PXE4, Itead Ibox, icnova-a20-swac, yones toptech bs1078-v2, Dserve DSRV9703C,
    * [Cubietech Cubietruck Plus][56328]
    * [Sinlinx SinA31s][56329]
    * [Xunlong Orange Pi 2][56330]
    * [Pine64][56331]
    * [LicheePi Zero][56332]

## v2016.03
[v2016.03 Release branch][56333]
  * PRCM i2c support

  * A83T 
    * LPDDR3 support

  * H3 
    * USB host support
    * PSCI (security switches included)
    * sy8106a i2c-based regulator support

  * AXP PMICs 
    * Power off support

  * Boards 
    * [Banana Pi M3][56334] (SinoVoip BPi-M3)

[![Exclamation.png][56335]][56336] Known problems:   

  * Commit [c32a6fd][56337] breaks MII detection (and thus U-Boot networking) for sunxi GMAC.

You might observe the PHY not initializing (e.g. no LED activity), and the command `mii info` likely will list useless information on all available PHY slots (0x00-0x1F). Commit [fc8991c][56338] fixes it again, but unfortunately that means U-Boot release **v2016.03 is affected**. 
## v2016.01
[v2016.01 Release branch][56339]
  * sun8i-H3 support

  * Boards 
    * Empire Electronix D709 tablet
    * A83T HomletV2 Board
    * [Lamobo R1][56340]
    * [Xunlong Orange Pi Plus][56341]
    * [Xunlong Orange Pi PC][56342]
    * [ C.H.I.P.][56343]

## v2015.10
[v2015.10 Release branch][56344]
  * Console/display output

    
  * ANX9804 LCD-eDP bridge chip support
  * Composite video output support

  * NAND SPL driver

  * Boards 
    * Olimex A20-SOM-EVB
    * A10s-Wobo-i5 (settop box)
    * Point of View pov protab2-ips9 tablet
    * Auxtek-T003 HDMI stick
    * A10 tablets based on the iNet-tek iNet-1 mainboard (e.g. Point of View Protab2 XXL, Cherry M1007)
    * A10 tablets based on the inet9f-rev03 mainboard (e.g. qware tb-g100 tablet)
    * A13 tablets based on on the inet98v_rev2 mainboard
    * A10 tablets based on the inet97fv2 mainboard
    * A23 tablets based on the gt90h-v4 mainboard

## v2015.07
[v2015.07 Release branch][56345]
  * Serial number support
  * Device model support 
    * Ethernet
    * GPIO
  * sun8i (A33) support (including SPL)
  * sun9i (A80) basic support 
    * UART
    * MMC
  * sun6i/sun8i 
    * PSCI CPU hotplugging
  * SPL 
    * ~~NAND support~~ reverted: [Revert commit][56346]

  * Boards: 
    * [Mixtile LOFT-Q][56347]
    * [Ainol AW1][56348]
    * [Yones Toptech BD1078][56349]
    * [iNet 3W][56350]
    * [iNet 3F][56351]
    * [ET-Q8 A33][56352]
    * [ Ippo q8h v1.2 A33 1024x600][56353]
    * [ga10h v1.1][56354]
    * [Merrii A80 Optimus Board][56355]

## v2015.04
[v2015.04 Release branch][56356]
  * sun7i (A20) [PSCI][56357] CPU hotplug
  * sun8i (A23) SPL 
    * RSB
    * AXP223

  * sun9i (A80) basic support 
    * Clocks
    * RSB

  * Console/display output 
    * VGA via internal DAC
    * VGA via external DAC on LCD interface
    * LVDS
    * SSD2828 MIPI bridge
    * tl059wv5c0 LCD panel

  * USB OTG

  * Boards: 
    * [CSQ CS908][56358]
    * [Merrii Hummingbird A31][56359]
    * [ Ippo q8h v1.2][56360]
    * [MSI Primo81][56361]
    * [MSI Primo73][56362]
    * [LinkSprite pcDuino][56363]
    * [LinkSprite pcDuino V2][56364]
    * [LeMaker Banana Pro][56365]
    * [Rikomagic mk802][56366]
    * [Rikomagic mk802ii][56367]
    * [Semitime g2][56368] (See also [Format_MK802][56369] with A10s)
    * [MarsBoard A10][56370]
    * [Gemei G9][56371]
    * [Chuwi V7 CW0825][56372]
    * [Mele M5][56373]
    * [Hyundai A7HD][56374]
    * [LinkSprite pcDuino3 Nano][56375]
    * [TZX-Q8-713B7][56376]
    * [Inet 86vs][56377]
    * [Ampe A76][56378]
    * [Jesurun Q5][56379]
    * [MK808C][56380]
    * [Mele I7][56381]
    * [Forfun Q88DB][56382]
    * [Wits Pro A20 DKT][56383]
    * [Xunlong Orange Pi][56384]
    * [Xunlong Orange Pi Mini][56385]
    * [Wexler TAB 7200][56386]

## v2015.01
[v2015.01 Release branch][56387]
  * sun6i (A31) processor support 
    * P2WI
    * AXP221
    * SPL
    * GMAC
  * sun8i (A23) processor support (no SPL)
  * sun6i/sun8i reset support
  * Console/display output 
    * HDMI only
    * simplefb

  * Boards: 
    * [Mele M3][56388]
    * [Olimex A20-OLinuXino-Lime2][56297]
    * WITS Colombus Board
    * [Mele M9][56389]

## v2014.10
[v2014.10 Release branch][56390]
  * AHCI (SATA)
  * sun4i (AKA A10) and sun5i (AKA A10s and A13) processors
  * EMAC Ethernet
  * AXP152 and AXP209 power controllers
  * EHCI USB
  * SMP support for sun7i via [PSCI][56357].

  * Boards: 
    * [LeMaker Banana Pi][56391]

## v2014.07
[v2014.07 Release branch][56392]
  * sun7i (AKA A20) processors
  * MMC
  * GMAC Ethernet
  * Boards: 
    * [Cubietech Cubietruck][56393]
