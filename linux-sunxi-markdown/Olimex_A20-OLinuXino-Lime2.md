# Olimex A20-OLinuXino-Lime2
Olimex A20-OLinuXino-Lime2  
---  
[![Lime2 top.jpg][40801]][40802]  
Manufacturer |  [Olimex][40803]  
Dimensions |  84 _mm_ x 60 _mm_ x 20 _mm_  
Release Date |  September 2014   
Website |  [Device Product Page][40804]  
Specifications   
SoC |  [A20][40805] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz   
eMMC |  4GB (optional)   
NAND |  4GB (optional)   
Power |  DC 5V ([5.5/2.1 jack][40806]), 3.7V LiPo (JST PHR-2 header)   
Features   
Video |  HDMI (Type A, full)   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211CL][40807] PHY in rev. A-E, [Realtek RTL8211E][40808] PHY in rev. F-G2, [ Micrel KSZ9031][40809] PHY in rev. H-L)   
Storage |  µSD, SATA   
USB |  2x USB2.0 Host, 1x mini USB2.0 OTG   
Headers |  UART, 5x GPIO headers   
The [A20 Olinuxino LIME2][40810] is an [OSHW][40811] board produced by [Olimex][40812]. 
The A20-OLinuXino-LIME2 is an upgrade of the [Olimex A20-OLinuXino-Lime][40813], but it comes with 1GiB RAM and gigabit ethernet. There are also two extra variants with onboard storage: [A20-OLinuXIno-LIME2-4GB][40814] with 4GB NAND and [A20-OLinuXino-LIME2-eMMC][40815] with 4GB eMMC. 
## Contents
  * [1 Identification][40816]
  * [2 Sunxi support][40817]
    * [2.1 Current status][40818]
    * [2.2 Manual build][40819]
      * [2.2.1 U-Boot][40820]
        * [2.2.1.1 Sunxi/Legacy U-Boot][40821]
        * [2.2.1.2 Mainline U-Boot][40822]
      * [2.2.2 Linux Kernel][40823]
        * [2.2.2.1 Sunxi/Legacy Kernel][40824]
        * [2.2.2.2 Mainline kernel][40825]
  * [3 Tips, Tricks, Caveats][40826]
    * [3.1 FEL mode][40827]
    * [3.2 GMAC quirks][40828]
      * [3.2.1 Possible causes][40829]
      * [3.2.2 Workarounds or fixes][40830]
        * [3.2.2.1 calibrate at PHY][40831]
        * [3.2.2.2 slowdown][40832]
        * [3.2.2.3 master mode][40833]
        * [3.2.2.4 calibrate at MAC][40834]
      * [3.2.3 Further testing][40835]
        * [3.2.3.1 Port Olimex board-detection to mainline u-boot][40836]
        * [3.2.3.2 Change device-tree to use PHY-mode RGMII-ID][40837]
        * [3.2.3.3 Misc. ideas][40838]
    * [3.3 GMAC-related software bugs][40839]
    * [3.4 Expansion ports][40840]
    * [3.5 Booting from SPI Flash][40841]
    * [3.6 Using LiPo battery][40842]
    * [3.7 SATA power connector][40843]
    * [3.8 Hardware reliability][40844]
      * [3.8.1 DRAM clock speed limit][40845]
      * [3.8.2 DRAM test results][40846]
  * [4 Adding a serial port][40847]
  * [5 Pictures][40848]
  * [6 See also][40849]
    * [6.1 Manufacturer images][40850]

# Identification
The board is marked as _A20-OLinuXino-Lime_ on both the top and bottom of the PCB. 
Note that it is not marked as Lime2. The Lime2 variant can be distinguished by the presence of two dram chips on the top of the board between the SoC and the USB connectors, also the ethernet phy is on the bottom of the board instead of the top. 
# Sunxi support
## Current status
Supported. 
  * Mainline kernel patches posted to linux-arm-kernel mailing list 2014-09-28
  * Mainline u-boot patches posted to u-boot mailing list 2014-09-28

## Manual build
You can build things for yourself by following our [ Manual build howto][40851] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _A20-OLinuXino_Lime2_ build target. __FEL_ version is also available for USB booting. 
#### Mainline U-Boot
Use the _A20-OLinuXino-Lime2_defconfig_ build target or _A20-OLinuXino-Lime2-eMMC_defconfig_ if you have the eMMC version. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_a20-olinuxino_lime2.fex_][40852] file. (Please note that this fex file adopted DRAM clock setting from the Lime2's predecessor - only _dram_tpr4_ differs for unknown reasons. Using this fex file the DRAM is clocked with just 384 MHz, which costs some few percent performance depending on the application used.) 
#### Mainline kernel
Use either _sun7i-a20-olinuxino-lime2.dtb_ or _sun7i-a20-olinuxino-lime2-emmc.dtb_ device-tree binary. 
[![][40853]][40854]
[][40855]
Recovery button
# Tips, Tricks, Caveats
## FEL mode
The Recovery button (under sata connector, nearest hdmi connector) triggers [ FEL mode][40856]. 
[![][40857]][40858]
[][40859]
Lime2 UEXT connector
## GMAC quirks
Different ethernet PHY is used [depending on board revision][40860] Each of those designs have quirks at gigabit speeds, with slightly different symptoms: 
  * Rev. A-E with [Realtek RTL8211CL][40807] PHY looses packets **receiving** at gigabit speed **[in slave mode][40861]**
  * Rev. F-G2 with [Realtek RTL8211E][40808] PHY looses packets **transmitting** at gigabit speed
  * Rev. H-L with [ Micrel KSZ9031][40809] PHY looses packets **transmitting** at gigabit speed

### Possible causes
A possible cause for packet loss **only** at gigabit speed is wrongly calibrated trace length compensation a.k.a. [RGMII][40862] timing a.k.a. TX/RX skew: the sum of a) physical wiring length between MAC and PHY, b) compensations in MAC, and c) compensations in PHY, must result in a 1.5-2 ns delay from TX source clock in MAC and RX source clock in PHY.   

A possible cause for packet loss only in master or slave mode is failure to seed or align with [RGMII source-synchronous clock][40862] (this is [newest suspected cause for rev. A-E boards][40863] but an older guess of the cause being clock _calibration_ [seems not ruled out][40864]). 
A possible cause for packet loss only for Micrel PHY is [a bug][40865] fixed since mainline linux v5.1 and unfixed in mainline u-boot (as of v2020.07). 
### Workarounds or fixes
#### calibrate at PHY
Proper fix for rev. F and newer is to apply [trace length compensation][40866] at the PHY. 
This is done by default (also for rev. H and newer despite commit message mentioning only realtek not Micrel) [since mainline linux v5.15][40867] and [since mainline u-boot v2022.04][40868];   
before that it is supported by custom-compiling a device-tree binary with above change applied [since mainline linux v5.9][40869] (and backported to [v5.8.15][40869]) and [since mainline u-boot v2022.04][40870]. 
Related documentation about Micrel KSZ9031 PHY compensations where updated since [v5.12][40871]. 
#### slowdown
A simple general workaround is to avoid speeds showing package loss, either by [advertising][40872] only lower speeds, or by turning off auto-negotiation and setting one specific lower speed, or doing similar advertising/fixation at the peer host.   
Mainline u-boot supports environment variable `disable_giga` for Micrel 9031 PHY [since v2017.09][40873]; i.e. setting `disable_giga` in u-boot environment should work for rev. H-L boards.   
Linux supports changing speed and auto-negotiation with ethtool or systemd (see option advertise in either `man ethtool` or `man systemd.link`).   
Beware: You may need additional changes with [older linux or u-boot][40839]. 
#### master mode
A workaround for rev. A-E boards is to force the device into master mode, either by fixating device to only offer master mode or by fixating peer device to only offer slave mode.   
Beware: This workaround has the adverse effect of **complete network failure at any speed with a peer device in master mode!**   
Mainline linux supports forcing master or slave mode [since v5.7][40874] which should be possible to control from ethtool [v5.8 or newer][40875].   
Mainline u-boot supports option `RTL8211X_PHY_FORCE_MASTER=y` for any Realtek RTL8211x PHY [since v2016.05][40876], and limited to Realtek RTL8211B/C PHYs since [v2017.01][40877] (i.e. it is _ignored_ on newer revisions of LIME2); it is [enabled by default][40878] for defconfig `A20-OLinuXino-Lime2` (since v2016.05 [intermittently][40839] and) since [v2020.04][40879]; it is _not enabled_ for defconfig `A20-OLinuXino-Lime2-eMMC` (available since v2017.09).   
Beware: You may need additional changes with [older linux or u-boot][40839]. 
#### calibrate at MAC
A workaround for rev. F and newer (and maybe rev. A-E as well?) is to apply [trace length compensation][40866] at the MAC.   
Mainline u-boot supports compensating at MAC [since v2015.04][40880] using option `CONFIG_GMAC_TX_DELAY`.   
[Olimex fork of u-boot][40881] hardcodes the equivalent of `CONFIG_GMAC_TX_DELAY=2` for rev. F-G2 boards, and the equivalent of `CONFIG_GMAC_TX_DELAY=4` for rev. H-L boards.   
[Some][40882] have alternative had success with rev. G2 and u-boot option `CONFIG_GMAC_TX_DELAY=4`.   
[Some][40883] have alternatively had success with rev. K and u-boot option `CONFIG_GMAC_TX_DELAY=3`, also noting that the Micrel PHY gets significantly hotter than the older Realtek [RTL8211CL][40807]/[RTL8211E][40808] PHYs.   
Beware: **A bugfix optimal for one board revision[may adversely affect other board revisions][40884]!**   
Beware: You may need additional changes with [older linux or u-boot][40839]. 
### Further testing
Current approach in mainline u-boot of unconditionally compensating at MAC require different values for rev. F-G2 as for rev. H-K. 
#### Port Olimex board-detection to mainline u-boot
Olimex fork of u-boot probes and apply compensations conditional to i2c eeprom information about board revision. Maybe that can be ported to mainline u-boot. 
#### Change device-tree to use PHY-mode RGMII-ID
Changing device-tree to use PHY-mode RGMII-ID (not RGMII), and rely on driver-specific default compensations, has been succesfully tested to work with rev. H-L board. 
Tests require recompiling u-boot to not apply other ethernet quirks, and then use a device-tree binary patched like this: 
[code] 
    dtc sun7i-a20-olinuxino-lime2.dtb | sed 's/"rgmii"/"rgmii-id"/' | dtc -o test - && mv --force test sun7i-a20-olinuxino-lime2.dtb
    
[/code]
(beware that above code is sloppy and may wreak havoc on other revisions of the device tree files than the current one) 
If this works reliably for all three board revisions, solution is probably to first get a patch [like this (applied for another board since v5.13)][40885] accepted in mainline linux, and then have mainline u-boot drop current quirks. 
#### Misc. ideas
  * test rev. A-E board with u-boot option `CONFIG_GMAC_TX_DELAY=N` at various values and **without`RTL8211X_PHY_FORCE_MASTER=y`**
  * test rev. F-G2 board with u-boot option `CONFIG_RTL8211E_PINE64_GIGABIT_FIX=y`
  * test rev. F-G2 board with u-boot option `CONFIG_GMAC_TX_DELAY=N` at various values (including 2 or 3 which some find optimal)
  * test rev. H-L board with u-boot option `CONFIG_PHY_MICREL_KSZ9031=y` and u-boot command `setenv disable_giga`
  * test rev. H-L board with u-boot options `CONFIG_PHY_MICREL_KSZ9031=y` and `CONFIG_GMAC_TX_DELAY=N` with the latter at various values (including 3 or 4 which some find optimal)
  * test with u-boot and Linux device-tree option `phy-mode = "rgmii-id"`
  * inspect with ethtool 5.8 or newer if ethernet is in master or slave mode when conducting other tests, and try force the opposite mode to check if a calibration setup behaves same in both modes.

## GMAC-related software bugs
Rev. A-E would fail to work in master mode, because [workaround for a GMAC quirk][40828] was accidentally disabled since [v2017.03][40886]).   
Fixed since mainline u-boot [v2020.04][40879]. 
Rev. H-L would fail to work or lose packets at 100 megabit or gigabit speeds, because Micrel PHY driver was not loaded by default.   
Fixed since mainline linux [v5.5][40887] and mainline u-boot [v2021.01][40888]. 
## Expansion ports
The internal GPIO headers appear to be mirrored compared to the original Lime boards [[1]][40889]. Due to this there are specific A20-OLinuXino-Lime2-UEXT adapters, however as of 2014-09-28 these do not appear to be available directly from the Olimex shop. 
## Booting from SPI Flash
See the main [Bootable_SPI_flash][40890] article for generic guides on how to boot from SPI flash. With SPI flash it is possible to use SATA or network boot without any need to use an SD card for storing the U-Boot bootloader. 
[Since rev. K][40891] all Lime2 boards are equipped with SPI NOR flash. 
In case you have older revision, it is possible to add it yourself, as this requires soldering wires to 3 pads on the empty NAND socket in order to get access to the PC0,PC1,PC2 pins. 
  

  * [![A20 LIME2 with SPI0 soldered.jpg][40892]][40893]
  * [![A20 LIME2 with SPI0 soldered-part-2.jpg][40894]][40895]

## Using LiPo battery
Warning! Battery connector, JST, is exactly the same as SATA power connector! 
PMIC [AXP209][40896] can charge LiPo battery and it has DC-DC bust-up converter to power the board from battery. 
LED "CHGLED" (near battery connector): yellow — battery is charging. 
If you connect the battery when the board is powered off, it will not power on automatically. 
## SATA power connector
Unlike other sunxi boards the Olimex boards don't use the JST XH 0.1"/2.5mm header for SATA power but the smaller JST PHR-2 header normally used for connecting LiPo batteries. 
## Hardware reliability
There are known cases where Lime2 boards are failing in the wild. The main suspects are DRAM clock speed and CPU core voltage. For more information see [Hardware Reliability Tests]. 
### DRAM clock speed limit
DRAM is clocked at **480 MHz** by the hardware vendor (in fact even [532Mhz is mentioned in the blog][40889]). The board uses somewhat non-standard resistors for ZQ calibration (ZQ = **330 Ohm** , SZQ = **330 Ohm**), but at least they seem to be the same in Lime2 revisions from Rev.B to Rev.E according to the board schematics. Still it's best to always mention the board revision in the results table in order to avoid any surprises. 
### DRAM test results
Having done runs on a larger set of boards, initial test results looked appalling. Machines that where known to have caused trouble in the past, failed within the hour. Others kept going for a few hours actually. We did notice temperature variation influences. On a Monday, the heating in the building was broken and the ambient temperature was only 20 degrees Celsius and 3 boards ran overnight without a problem. On Wednesday the heating was fixed and the ambient temperature rose to 23 degrees Celsius and all three boards had crashed. All of the initial 6 test subjects crashed and failed at their stock 480 DRAM frequency setting! 
Expanding this test to influence ambient temperature, even more interesting results where found. For example, 456 Mhz seemed stable at 22 degrees Celsius, but with an ambient temperature of 50 degrees Celsius a few boards still crashed. Lowering the frequency even more, to 432 MHz stabilized that and thus the ambient temperature was increased to 70 degrees Celsius. Here the sunxi_tp_temp, which is very unreliable, reported core temperatures of about 77 degrees Celsius. The board however remained running stable at least one hour. 
[Lima-memtester][40897] was used for testing. The full tests results can be seen in this [sheet][40898], and can eventually be modified into table below. 
Hardware  | Diagnostic software  | lima-memtester passes  | lima-memtester fails  | Notes   
---|---|---|---|---  
[User:JohnDoe][40899]'s A20-OLinuXino-Lime2 Rev.? | fel-boot-lima-memtester-on-a20-lime2-v1.tar.gz | ? MHz | ? MHz | ? MHz fails after running for ? minutes   
# Adding a serial port
[![][40900]][40901]
[][40902]
UART connector
There is a clearly marked UART0 connector on the edge of the board beside the ethernet connector. All you have to do is attach some leads according to our [UART howto][40903]. 
# Pictures
  * [![Lime2 top.jpg][40904]][40802]
  * [![Lime2 bot.jpg][40905]][40906]
  * [![Lime2 fel.jpg][40907]][40854]
  * [![Lime2 uext.jpg][40908]][40858]

# See also
  * [Olimex A10-OLinuXino-Lime][40909]
  * [Olimex A20-OLinuXino-Lime][40813]
  * [Lime2 schematics & CAD files][40910]

## Manufacturer images
[Olimex images for Lime2][40911]
