# Anbernic RG35XX Plus
Anbernic RG35XX Plus  
---  
[![RG35XX+Front.jpg][7437]][7438]  
Manufacturer |  [Anbernic][7439]  
Dimensions |  81 _mm_ x 117 _mm_ x 22 _mm_  
Release Date |  November 2023   
Website |  [[1]][7440]  
Specifications   
SoC |  [H700][7441] @ 1.5 Ghz   
DRAM |  1GiB LPDDR4 @ 672 MHz   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  640x480 (3.5" 4:3) (likely [ER-TFT035-07][7442] with [NV3052C][7443] driver)   
Video |  mini HDMI   
Audio |  3.5mm headphone plug, HDMI, internal mono speaker   
Network |  WiFi 802.11 b/g/n + BT 4.2 ([Realtek 8821CS][7444])   
Storage |  2 x µSD   
USB |  1 x USB Type-C OTG   
Other |  vibration motor   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][7445] and the [New Device Page guide][7446].
Handheld gaming device built around an Allwinner [H700][7441] CPU. One of the first devices with an AXP717 PMIC. 
## Contents
  * [1 Variants][7447]
  * [2 Identification][7448]
  * [3 Sunxi support][7449]
    * [3.1 Current status][7450]
    * [3.2 Manual build][7451]
      * [3.2.1 Mainline U-Boot][7452]
      * [3.2.2 Mainline Linux Kernel][7453]
  * [4 Tips, Tricks, Caveats][7454]
    * [4.1 FEL mode][7455]
    * [4.2 information from vendor firmware][7456]
  * [5 Adding a serial port (**voids warranty**)][7457]
    * [5.1 Device disassembly][7458]
    * [5.2 Locating the UART][7459]
  * [6 Pictures][7460]
  * [7 See also][7461]
    * [7.1 Manufacturer images][7462]

# Variants
  * **[RG35XX-H][7463]** : H horizontal form factor, adds analog thumb sticks and a second USB-C OTG port,
  * **RG35XX 2024** : Removes the Wifi/BT chip
  * **RG35XX-SP** : Hinged clamshell form factor with a lid sensor.

# Identification
On the back of the device, the following is printed: 
[code] 
    Anbernic RG35XX plus
[/code]
The PCB has the following silkscreened on it: 
[code] 
    RG 35XX Plus_V4 2023-09-25
[/code]
# Sunxi support
## Current status
Mainline support is work in progress. On top of the generic H616 support (which misses display capability at the moment), this device requires support for the LCD and the AXP717 PMIC. 
Mainline support: 
  * [Base][7464], [-Plus][7465] and [-H][7466] device specific DT] for regulators, console, Wifi, BT, SD1, gamepad buttons, LEDs (6.10)
  * Wifi and BT (CONFIG_RTW88_8821CS)
  * AXP717 PMIC in AXP20X driver (CONFIG_*_AXP20X_*), supporting regulators and RSB communication.
  * AXP717 USB power support (5V boost regulator)
  * Power LED
  * Non-maskable interrupt (supports PMIC interrupts, CONFIG_SUNXI_NMI_INTC) and general purpose ADC (supports thumbsticks on -H device, CONFIG_SUN20I_GPADC)
  * H616/H700/T507 DE33 [Display engine][7467]

Working parts (with currently WIP patches): 
  * Basic U-Boot support (<https://git.sr.ht/~tokyovigilante/u-boot>)
  * DRAM init in u-boot (based on the T507).
  * AXP717 PMIC driver for ([u-boot][7468])
  * Battery support (??)
  * Second SD card slot
  * H700/T507 [LCD timing controller ???][7469]
  * RGB [panel driver][7470] with GPIO backlight (NV3052C driver IC)
  * Mali GPU enablement (supported by Panfrost, just needs [platform power domain driver][7471] and [DTS and driver tweaks][7472])
  * PWM driver for backlight (competing approaches to sync currently, [WIP patch v12][7473] and [alternate approach][7474] on LKML).

In-progress: 
  * Video Engine (not device specific, H264/H265 HW acceleration) ([via Cedrus][7475])
  * Audio [codec][7476] (porting from Allwinner H616 non-mainline driver)
  * Audio hub (non-mainline [driver][7477])
  * HDMI output * [HDMI port][7478]
  * HDMI audio (requires/alongside audio hub support)
  * 32KHz clock [auto-calibration][7479]
  * Vibration motor (depends on PWM support)
  * USB host support for OTG support (will need significant driver rework)

## Manual build
You can build things for yourself by following our [ Manual build howto][7480] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Mainline Linux Kernel
Use the _[Template:Sun50i-h700-anbernic-rg35xx-2024.dtb][7481]_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
Booting with a USB-C cable connected to the USB-OTG port (at the bottom of the device) without an SD card inserted triggers [ FEL mode][7482]. 
## information from vendor firmware
**Please note that this is not usable for mainline kernels and contains a lot of nonsense. It is however a decent source of information, given the lack of schematics:**
Decompiled BSP device tree: [sun50i-h700-anbernic-rg35xxph.dts][7483]
regulator_summary dump from factory firmware 
[code] 
    [/sys/kernel/debug]# cat /sys/kernel/debug/regulator/regulator_summary
     regulator                      use open bypass voltage current     min     max
    -------------------------------------------------------------------------------
     regulator-dummy                  0    8      0     0mV     0mA     0mV     0mV
        6000000.hdmi                                                    0mV     0mV
        6000000.hdmi                                                    0mV     0mV
        5311000.ohci3-controller                                        0mV     0mV
        5310000.ohci2-controller                                        0mV     0mV
        5200000.ohci1-controller                                        0mV     0mV
        5311000.ehci3-controller                                        0mV     0mV
        5310000.ehci2-controller                                        0mV     0mV
        5200000.ehci1-controller                                        0mV     0mV
     axp2202-dcdc1                    0    2      0  1160mV     0mA   500mV  1540mV
        cpu0                                                         1160mV  1160mV
        reg-virt-consumer.0.auto                                        0mV     0mV
     axp2202-dcdc2                    0    1      0   940mV     0mA   500mV  3400mV
        reg-virt-consumer.1.auto                                        0mV     0mV
     axp2202-dcdc3                    0    1      0  1100mV     0mA   500mV  1840mV
        reg-virt-consumer.2.auto                                        0mV     0mV
     axp2202-dcdc4                    0    1      0  1000mV     0mA  1000mV  3700mV
        reg-virt-consumer.3.auto                                        0mV     0mV
     axp2202-aldo1                    0    2      0  1800mV     0mA   500mV  3500mV
        sdc2                                                            0mV     0mV
        reg-virt-consumer.4.auto                                        0mV     0mV
     axp2202-aldo2                    0    1      0  1800mV     0mA   500mV  3500mV
        reg-virt-consumer.5.auto                                        0mV     0mV
     axp2202-aldo3                    0    1      0  1800mV     0mA   500mV  3500mV
        reg-virt-consumer.6.auto                                        0mV     0mV
     axp2202-aldo4                    0    2      0  1800mV     0mA   500mV  3500mV
        5096000.codec                                                1800mV  1800mV
        reg-virt-consumer.7.auto                                        0mV     0mV
     axp2202-bldo1                    0    1      0  1800mV     0mA   500mV  3500mV
        reg-virt-consumer.8.auto                                        0mV     0mV
     axp2202-bldo2                    0    1      0  1800mV     0mA   500mV  3500mV
        reg-virt-consumer.9.auto                                        0mV     0mV
     axp2202-bldo3                    0    1      0  2800mV     0mA   500mV  3500mV
        reg-virt-consumer.10.auto                                       0mV     0mV
     axp2202-bldo4                    0    1      0  1200mV     0mA   500mV  3500mV
        reg-virt-consumer.11.auto                                       0mV     0mV
     axp2202-cldo1                    1    2      0  3300mV     0mA   500mV  3500mV
        5096000.codec                                                3300mV  3300mV
        reg-virt-consumer.12.auto                                       0mV     0mV
     axp2202-cldo2                    0    1      0  3300mV     0mA   500mV  3500mV
        reg-virt-consumer.13.auto                                       0mV     0mV
     axp2202-cldo3                    0    1      0  3300mV     0mA   500mV  3500mV
        reg-virt-consumer.14.auto                                       0mV     0mV
     axp2202-cldo4                    1    1      0  3300mV     0mA   500mV  3500mV
        reg-virt-consumer.15.auto                                       0mV     0mV
     axp2202-rtcldo                   0    1      0  1800mV     0mA  1800mV  1800mV
        reg-virt-consumer.16.auto                                       0mV     0mV
     axp2202-cpusldo                  0    1      0   900mV     0mA   500mV  1400mV
        reg-virt-consumer.17.auto                                       0mV     0mV
     axp2202-vmid                     0    0      0     0mV     0mA     0mV     0mV
     axp2202-drivevbus                0    0      0     0mV     0mA     0mV     0mV
    
[/code]
boot log from factory firmware 
[code] 
    [37]HELLO! BOOT0 is starting!
    [40]BOOT0 commit : 749c1f9a-dirty
    [43]set pll start
    [45]periph0 has been enabled
    [49]set pll end
    [50][pmu]: bus read error
    [53][pmu]: bus read error
    [55]PMU: AXP2202
    [64]vaild para:8  select dram para0
    [67]board init ok
    [69]rtc[1] value = 0x4801b400
    [72]rtc[2] value = 0x11000004
    [75]DRAM BOOT DRIVE INFO: V0.651
    [78]the chip id is 0x6c00
    [81]chip id check OK
    [83]DRAM_VCC set to 1100 mv
    [86][DST] Dram DST Loop1
    [110]read_calibration error
    [124]read_calibration error
    [138]read_calibration error
    [152]read_calibration error
    [166]read_calibration error
    [180]read_calibration error
    [193]read_calibration error
    [207]read_calibration error
    [221]read_calibration error
    [235]read_calibration error
    [238]retraining final error
    [254][AUTO DEBUG]32bit,1 ranks training success!
    [415][DST] Lclk,0x00008888,Memtest Pass
    [419][DST] Clk =672 MHz
    [421][DST] R_2d
    [1600][DST] R_2d_hv_D2:0x18-0x64,0x4d(332mV),0
    [1605][DST] R_2d_hv_D2:0x30~0x4c,0x3e
    [1608][DST] R_2d tpr6 = 0x3e808080
    [1619][DST] R_1st
    [1635][DST] DB0 R_1st:3,0~26,27,0x07
    [1652][DST] DB1 R_1st:3,0~26,27,0x07
    [1670][DST] DB2 R_1st:3,0~25,26,0x06
    [1687][DST] DB3 R_1st:3,0~25,26,0x06
    [1690][DST] R_1st Tpr12 = 0x06060707
    [1694][DST] W_2st
    [1779][DST] DB0 W_2st:0,16~40,25,0x1c
    [1841][DST] DB1 W_2st:0,19~42,24,0x1e
    [1906][DST] DB2 W_2st:0,19~44,26,0x1f
    [1964][DST] DB3 W_2st:0,16~40,25,0x1c
    [1967][DST] W_2st Tpr11 = 0x1c1f1e1c
    [1971][DST] R_2st
    [2003][DST] DB0 R_2st:3,0~25,26,0x06
    [2037][DST] DB1 R_2st:3,0~25,26,0x06
    [2067][DST] DB2 R_2st:3,0~22,23,0x05
    [2100][DST] DB3 R_2st:3,0~23,24,0x05
    [2104][DST] R_2st Tpr12 = 0x05050606
    [2268][DST] RV_C, VW:0x38-0x44, DW:120ps
    [2365][DST] Dram DST Success
    [2368]DRAM CLK =672 MHZ
    [2370]DRAM Type =8 (3:DDR3,4:DDR4,7:LPDDR3,8:LPDDR4)
    [2382]Actual DRAM SIZE =1024 M
    [2385]DRAM SIZE =1024 MBytes, para1 = 30fa, para2 = 4000000, dram_tpr13 = 2006c61
    [2399]DRAM simple test OK.
    [2401]rtc standby flag is 0x0, super standby flag is 0x0
    [2407]dram size =1024
    [2409]key press :
    [2412]card no is 0
    [2414]sdcard 0 line count 4
    [2416][mmc]: mmc driver ver 2021-10-12 13:56
    [2421][mmc]: b mmc 0 bias 0
    [2429][mmc]: Wrong media type 0x0
    [2432][mmc]: ***Try SD card 0***
    [2442][mmc]: HSSDR52/SDR25 4 bit
    [2445][mmc]: 50000000 Hz
    [2448][mmc]: 59638 MB
    [2450][mmc]: ***SD/MMC 0 init OK!!!***
    [2560]Loading boot-pkg Succeed(index=0).
    [2564][mmc]: b mmc 0 bias 0
    [2567]Entry_name        = u-boot
    [2577]Entry_name        = monitor
    [2581]Entry_name        = dtbo
    [2584]Entry_name        = dtb
    [2588]Jump to second Boot.
    NOTICE:  BL3-1: v1.0(debug):335ab35
    NOTICE:  BL3-1: Built : 14:03:48, 2023-12-07
    NOTICE:  BL3-1 commit: 8
    NOTICE:  cpuidle init version V2.0
    ERROR:   Error initializing runtime service tspd_fast
    NOTICE:  BL3-1: Preparing for EL3 exit to normal world
    NOTICE:  BL3-1: Next image address = 0x4a000000
    ▒OTICE:  BL3-1: Next image spsr = 0x1d3
    
    U-Boot 2018.05 (Dec 19 2023 - 22:45:47 +0800) Allwinner Technology
    
    [02.673]CPU:   Allwinner Family
    [02.676]Model: sun50iw9
    I2C:   ready
    [02.680]DRAM:  1 GiB
    [02.684]Relocation Offset is: 35eba000
    [02.731]secure enable bit: 0
    [02.734]pmu_axp152_probe pmic_bus_read fail
    [02.738]pmu_axp1530_probe pmic_bus_read fail
    [02.742]PMU: AXP2202
    [02.745]BMU: AXP2202
    [02.747][AXP2202] comm status : 0x0 = 0x39, 0x1 = 0xb2
    [02.752][AXP2202] onoff status: 0x20 = 0x0, 0x21 = 0x0
    AXP2202_IIN_LIM:38
    AXP2202_IIN_LIM:38
    [02.763][axp][err]:
    b12_mode: 0
    AXP2202_IIN_LIM:38
    FDT ERROR:fdt_get_regulator_name:get property handle twi-supply error:FDT_ERR_INTERNAL
    [02.796]battery_check pass:radio:68, vol:4005
    [02.801]CPU=1008 MHz,PLL6=600 Mhz,AHB=200 Mhz, APB1=100Mhz  MBus=400Mhz
    [02.809]drv_disp_init
    [02.844]__clk_enable: clk is null.
    [02.850]drv_disp_init finish
    [02.852]gic: sec monitor mode
    [02.885]flash init start
    [02.887]workmode = 0,storage type = 1
    [02.890]MMC:     0
    [02.892][mmc]: mmc driver ver uboot2018:2021-07-19 14:09:00
    [02.898][mmc]: get sdc_type fail and use default host:tm1.
    [02.909][mmc]: Using default timing para
    [02.912][mmc]: SUNXI SDMMC Controller Version:0x40200
    [02.930][mmc]: card_caps:0x3000000a
    [02.933][mmc]: host_caps:0x3000003f
    [02.937]sunxi flash init ok
    [02.941]Loading Environment from SUNXI_FLASH... OK
    [02.958]out of usb burn from boot: not need burn key
    [02.963]boot_gui_init:start
    partno erro : can't find partition Reserve0
    [02.975]Get Reserve0 partition number fail!
    tcon_de_attach:de=0,tcon=0===LCD_power_on:178
    --allen--data0 = 192
    [02.990]boot_gui_init:finish
    [02.994]bmp_name=bootlogo.bmp
    partno erro : can't find partition bootloader
    ===lcd_panel_uboot_fj035fhd05_v1_init:261 lcd_type = 0
    921654 bytes read in 185 ms (4.8 MiB/s)
    [03.201]Item0 (Map) magic is bad
    [03.204]the secure storage item0 copy0 magic is bad
    [03.209]Item0 (Map) magic is bad
    [03.211]the secure storage item0 copy1 magic is bad
    [03.216]Item0 (Map) magic is bad
    [03.222]update dts
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    [03.292]update part info
    [03.303]update bootcmd
    [03.305]No ethernet found.
    Hit any key to stop autoboot:  0
    ===LCD_bl_open:197
    [03.346]LCD open finish
    Android's image name: sun50i_arm64
    [04.236]Starting kernel ...
    
    [04.239][mmc]: MMC Device 2 not found
    [04.242][mmc]: mmc 2 not find, so not exit
    [    0.000000] Booting Linux on physical CPU 0x0
    [    0.000000] Linux version 4.9.170 (cc@cc-H81M-S1) (gcc version 5.3.1 20160412 (Linaro GCC 5.3-2016.05) ) #254 SMP PREEMPT Tue Dec 19 15:45:52 CST 2023
    [    0.000000] Boot CPU: AArch64 Processor [410fd034]
    [    0.000000] bootconsole [earlycon0] enabled
    [    0.000000] allen_boe_lcd=0, str=old
    [    0.081607] BOOTEVENT:        81.602957: ON
    [    0.590028] axp2101-regulator axp2101-regulator.0: Setting DCDC frequency for unsupported AXP variant
    [    0.590400] axp2101-regulator axp2101-regulator.0: Error setting dcdc frequency: -22
    [  ▒[    1.027215] uart uart1: get regulator failed
    [    1.053666] [NAND][NE] Not found valid nand node on dts
    [    1.061736] sunxi-wlan soc@03000000:wlan: get gpio chip_en failed
    [    1.068619] sunxi-wlan soc@03000000:wlan: get gpio power_en failed
    [    1.176039] hci: request ohci0-controller gpio:272
    [    1.181792] hci: request ohci1-controller gpio:147
    [    1.401334] --[allen]-- sunxi_gpadc_probe: 321
    [    1.406532] ---[allen] sunxi_gpadc_probe: allen_gpadc_enable_flg=1
    [    1.424704] VE: get debugfs_mpp_root is NULL, please check mpp
    [    1.424704]
    [    1.432928] VE: sunxi ve debug register driver failed!
    [    1.432928]
    [    1.444351] axp2202_usb_power: axp2202-acin device is not configed, not use vbus-det
    [    1.444351]
    [    1.625522] mmc:failed to get gpios
    [    1.684881] sunxi-mmc sdc1: smc 2 p1 err, cmd 52, RTO !!
    [    1.691701] sunxi-mmc sdc1: smc 2 p1 err, cmd 52, RTO !!
    [    1.702105] sunxi-mmc sdc1: smc 2 p1 err, cmd 5, RTO !!
    [    1.708800] sunxi-mmc sdc1: smc 2 p1 err, cmd 5, RTO !!
    [    1.715490] sunxi-mmc sdc1: smc 2 p1 err, cmd 5, RTO !!
    [    1.722182] sunxi-mmc sdc1: smc 2 p1 err, cmd 5, RTO !!
    [    1.735084] ERROR: pinctrl_get for HDMI2.0 DDC fail
    [    1.758169] cpu cpu1: opp_list_debug_create_link: Failed to create link
    [    1.765734] cpu cpu1: _add_opp_dev: Failed to register opp debugfs (-12)
    [    1.773304] cpu cpu2: opp_list_debug_create_link: Failed to create link
    [    1.780764] cpu cpu2: _add_opp_dev: Failed to register opp debugfs (-12)
    [    1.788356] cpu cpu3: opp_list_debug_create_link: Failed to create link
    [    1.795814] cpu cpu3: _add_opp_dev: Failed to register opp debugfs (-12)
    [    1.852839] [sound  402][CODEC-HDMI sunxi_codec_dev_probe] register codec-hdmi success
    [    1.862589] [asoc_simple_probe, 432]
    [    1.868199] [asoc_simple_probe, 432]
    [    1.872975] [asoc_simple_probe, 432]
    [    1.877084] [asoc_simple_probe, 432]
    [    1.882373] [asoc_simple_probe, 432]
    ▒[/init]: getty is ttyS0
    [/init]: RootDevice is "/dev/mmcblk0p5" , GPT_SUPPORT=1
    [/init]: Try to load EMMC ...
    e2fsck 1.42.12 (29-Aug-2014)
    /dev/mmcblk0p5 has unsupported feature(s): metadata_csum
    e2fsck: Get a newer version of e2fsck!
    [    2.546932] cgroup: cgroup2: unknown option "nsdelegate"
    
    Welcome to Ubuntu 18.04.6 LTS!
    
    [  OK  ] Created slice User and Session Slice.
    [  OK  ] Reached target Remote File Systems.
    [  OK  ] Reached target Swap.
    [  OK  ] Started Dispatch Password Requests to Console Directory Watch.
    [  OK  ] Created slice System Slice.
    [  OK  ] Listening on Journal Audit Socket.
    [  OK  ] Reached target Slices.
    [  OK  ] Listening on udev Kernel Socket.
    [  OK  ] Created slice system-serial\x2dgetty.slice.
    [  OK  ] Listening on Journal Socket.
             Mounting Kernel Debug File System...
             Starting Load Kernel Modules...
             Starting Create Static Device Nodes in /dev...
    [    3.503993] [asoc_simple_probe, 432]
             Starting Set the console keyboard layout...
    [  OK  ] Listening on /dev/initctl Compatibility Named Pipe.
    [  OK  ] Listening on Journal Socket (/dev/log).
    [  OK  ] Listening on udev Control Socket.
             Starting udev Coldplug all Devices...
             Starting Journal Service...
    [  OK  ] Started Forward Password Requests to Wall Directory Watch.
    [  OK  ] Reached target Paths.
    [  OK  ] Reached target Local Encrypted Volumes.
             Starting Remount Root and Kernel File Systems...
    [  OK  ] Started Journal Service.
    [  OK  ] Mounted Kernel Debug File System.
    [  OK  ] Started Load Kernel Modules.
    [  OK  ] Started Create Static Device Nodes in /dev.
    [  OK  ] Started Set the console keyboard layout.
    [  OK  ] Started Remount Root and Kernel File Systems.
             Starting Load/Save Random Seed...
    [  OK  ] Reached target Local File Systems (Pre).
    [  OK  ] Reached target Local File Systems.
             Starting Set console font and keymap...
             Starting udev Kernel Device Manager...
             Mounting FUSE Control File System...
             Starting Apply Kernel Variables...
             Mounting Kernel Configuration File System...
             Starting Flush Journal to Persistent Storage...
    [  OK  ] Started udev Kernel Device Manager.
    [  OK  ] Started udev Coldplug all Devices.
    [  OK  ] Started Load/Save Random Seed.
    [  OK  ] Started Set console font and keymap.
    [  OK  ] Mounted FUSE Control File System.
    [  OK  ] Started Apply Kernel Variables.
    [  OK  ] Mounted Kernel Configuration File System.
             Starting Raise network interfaces...
    [  OK  ] Started Flush Journal to Persistent Storage.
             Starting Create Volatile Files and Directories...
    [FAILED] Failed to start Create Volatile Files and Directories.
    See 'systemctl status systemd-tmpfiles-setup.service' for details.
    [  OK  ] Started Raise network interfaces.
    [  OK  ] Found device /dev/ttyS0.
    [  OK  ] Reached target Sound Card.
             Starting Update UTMP about System Boot/Shutdown...
             Starting Network Name Resolution...
    [  OK  ] Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
    [  OK  ] Started Update UTMP about System Boot/Shutdown.
             Starting Load/Save RF Kill Switch Status...
    [  OK  ] Reached target System Initialization.
    [  OK  ] Started Daily Cleanup of Temporary Directories.
    [  OK  ] Started Daily apt download activities.
    [  OK  ] Started Discard unused blocks once a week.
    [  OK  ] Started Message of the Day.
    [  OK  ] Listening on D-Bus System Message Bus Socket.
    [  OK  ] Reached target Sockets.
    [  OK  ] Reached target Basic System.
             Starting launcher.service...
    [  OK  ] Started Set the CPU Frequency Scaling governor.
             Starting Save/Restore Sound Card State...
             Starting Modem Manager...
             Starting Restore /etc/resolv.conf i…fore the ppp link was shut down...
             Starting Dispatcher daemon for systemd-networkd...
    [  OK  ] Started Regular background program processing daemon.
             Starting Login Service...
    [  OK  ] Started D-Bus System Message Bus.
             Starting Network Manager...
             Starting WPA supplicant...
    [  OK  ] Started Daily apt upgrade and clean activities.
    [  OK  ] Reached target Timers.
    [  OK  ] Started Load/Save RF Kill Switch Status.
    [  OK  ] Started Network Name Resolution.
    [  OK  ] Started launcher.service.
    [  OK  ] Started Restore /etc/resolv.conf if…before the ppp link was shut down.
    [  OK  ] Started Save/Restore Sound Card State.
    [  OK  ] Started Login Service.
    [  OK  ] Started WPA supplicant.
             Starting Authorization Manager...
    [  OK  ] Reached target Host and Network Name Lookups.
    [  OK  ] Stopped Network Manager.
             Starting Network Manager...
    [  OK  ] Started Authorization Manager.
             Starting Hostname Service...
    [  OK  ] Started Dispatcher daemon for systemd-networkd.
    [  OK  ] Started Modem Manager.
    [  OK  ] Started Hostname Service.
    [  OK  ] Started Network Manager.
             Starting Network Manager Script Dispatcher Service...
    [  OK  ] Reached target Network.
             Starting /etc/rc.local Compatibility...
             Starting Permit User Sessions...
    [  OK  ] Started Unattended Upgrades Shutdown.
    [  OK  ] Started Permit User Sessions.
    [  OK  ] Started Network Manager Script Dispatcher Service.
             Starting Set console scheme...
    [  OK  ] Started Set console scheme.
    [  OK  ] Created slice system-getty.slice.
    [    8.354837] sunxi-mmc sdc1: smc 2 p1 err, cmd 52, RTO !!
    [    8.361672] sunxi-mmc sdc1: smc 2 p1 err, cmd 52, RTO !!
             Starting Bluetooth service...
    [    9.077491] [asoc_simple_probe, 432]
    [    9.103607] [asoc_simple_probe, 432]
    [  OK  ] Started /etc/rc.local Compatibility.
    [  OK  ] Started Getty on tty1.
    [  OK  ] Started Serial Getty on ttyS0.
    [  OK  ] Reached target Login Prompts.
    [  OK  ] Reached target Multi-User System.
    [  OK  ] Reached target Graphical Interface.
             Starting Update UTMP about System Runlevel Changes...
    [  OK  ] Started Bluetooth service.
    [  OK  ] Started Update UTMP about System Runlevel Changes.
    [   11.296108] Bluetooth: Non-link packet received in non-active state
    
[/code]
# Adding a serial port (**voids warranty**)
The right side of the main board (as viewed from the rear after removing the cover) contains [UART howto][7484] headers. This presumably voids the warranty, but there is no specific warning about this on the device. 
## Device disassembly
Remove the Torx T6 screws from the rear case, and remove the battery cover. The case back will pop off with minimal effort, revealing the mainboard. Unplugging the battery will allow the rear case to be fully removed. 
## Locating the UART
[![][7485]][7486]
[][7487]
UART pads
# Pictures
  * [![RG35XX+Front.jpg][7488]][7438]
  * [![RG35XX+Board.jpg][7489]][7490]
  * [![RG35XX+PMIC.jpg][7491]][7492]
  * [![RG35XX-plus without shield.png][7493]][7494]

# See also
Hardware platform wise very similar to the [RG35XX-H][7463], which is in a different form factor and has two USB ports. 
## Manufacturer images
Optional. Add non-sunxi images in this section.
