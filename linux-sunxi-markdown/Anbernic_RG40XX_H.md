# Anbernic RG40XX H
Anbernic RG40XX H  
---  
[![RG40XX H front.jpg][7528]][7529]  
Manufacturer |  [Anbernic][7530]  
Dimensions |  163 _mm_ x 79 _mm_ x 16 _mm_  
Release Date |  June 2024   
Website |  [[1]][7531]  
Specifications   
SoC |  [H700][7532] @ 1.5 Ghz   
DRAM |  1GiB LPDDR4 @ 672 MHz   
Power |  DC 5V @ 1.5A, 3200mAh 3.7V Li-Po battery   
Features   
LCD |  640x480 (4.0" 4:3)   
Video |  mini HDMI   
Audio |  3.5mm headphone plug, HDMI, internal mono speaker   
Network |  WiFi 802.11 b/g/n + BT 4.2 ([Realtek 8821CS][7533])   
Storage |  2 x µSD   
USB |  1 x USB Type-C OTG   
Other |  vibration motor   
Headers |  SWD (?), UART   
This page needs to be properly filled according to the [New Device Howto][7534] and the [New Device Page guide][7535].
Handheld gaming device built around an Allwinner [H700][7532] CPU. Slightly larger variant of [Anbernic_RG35XX_Plus][7536]
## Contents
  * [1 Identification][7537]
  * [2 Sunxi support][7538]
    * [2.1 Current status][7539]
    * [2.2 Manual build][7540]
      * [2.2.1 U-Boot][7541]
        * [2.2.1.1 Mainline U-Boot][7542]
      * [2.2.2 Linux Kernel][7543]
        * [2.2.2.1 Mainline kernel][7544]
  * [3 Tips, Tricks, Caveats][7545]
    * [3.1 FEL mode][7546]
  * [4 Adding a serial port (**voids warranty**)][7547]
    * [4.1 Device disassembly][7548]
    * [4.2 Locating the UART][7549]
  * [5 Pictures][7550]
  * [6 See also][7551]
    * [6.1 Manufacturer images][7552]

# Identification
On the back of the device, the following is printed: 
[code] 
    ANBERNIC
    MODEL No.RG 40XX H
[/code]
The PCB has the following silkscreened on it: 
[code] 
    RG40XXH_MB_V02
    2024-04-30
[/code]
# Sunxi support
## Current status
Mainline support is work in progress. See the [RG35XX status][7553] for updates. 
## Manual build
You can build things for yourself by following our [ Manual build howto][7554] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
There's a CH32V003 chip near the SWD (?) pads, most likely it drives the RGB LEDs and is controlled by main SoC through another UART port. 
boot log from factory firmware, version RG40XXH-V1.0.3-EN16GB-240822.IMG 
[code] 
    [91]HELLO! BOOT0 is starting!
    [94]BOOT0 commit : 749c1f9a-dirty
    [97]set pll start
    [100]periph0 has been enabled
    [103]set pll end
    [105][pmu]: bus read error
    [107][pmu]: bus read error
    [110]PMU: AXP2202
    [118]vaild para:8  select dram para0
    [122]board init ok
    [124]rtc[2] value = 0xf
    [126]DRAM BOOT DRIVE INFO: V0.651
    [129]the chip id is 0x6c00
    [132]chip id check OK
    [135]DRAM_VCC set to 1100 mv
    [137][DST] Dram DST Loop1
    [274][DST] Lclk,0x00008888,Memtest Pass
    [278][DST] Clk =672 MHz
    [280][DST] R_2d
    [1459][DST] R_2d_hv_D2:0x1c-0x5c,0x41(280mV),0
    [1463][DST] R_2d_hv_D2:0x34~0x44,0x3c
    [1467][DST] R_2d tpr6 = 0x3c808080
    [1478][DST] R_1st
    [1493][DST] DB0 R_1st:3,0~24,25,0x06
    [1510][DST] DB1 R_1st:3,0~26,27,0x07
    [1528][DST] DB2 R_1st:3,0~26,27,0x07
    [1545][DST] DB3 R_1st:3,0~24,25,0x06
    [1548][DST] R_1st Tpr12 = 0x06070706
    [1552][DST] W_2st
    [1610][DST] DB0 W_2st:0,25~53,29,0x27
    [1670][DST] DB1 W_2st:0,28~54,27,0x29
    [1730][DST] DB2 W_2st:0,28~55,28,0x29
    [1789][DST] DB3 W_2st:0,25~51,27,0x26
    [1792][DST] W_2st Tpr11 = 0x26292927
    [1796][DST] R_2st
    [1836][DST] DB0 R_2st:3,1~24,24,0x06
    [1874][DST] DB1 R_2st:3,2~24,23,0x07
    [1912][DST] DB2 R_2st:3,1~23,23,0x06
    [1945][DST] DB3 R_2st:3,0~23,24,0x05
    [1949][DST] R_2st Tpr12 = 0x05060706
    [2113][DST] RV_C, VW:0x36-0x42, DW:120ps
    [2209][DST] Dram DST Success
    [2212]DRAM CLK =672 MHZ
    [2215]DRAM Type =8 (3:DDR3,4:DDR4,7:LPDDR3,8:LPDDR4)
    [2227]Actual DRAM SIZE =1024 M
    [2230]DRAM SIZE =1024 MBytes, para1 = 30fa, para2 = 4000000, dram_tpr13 = 2006c61
    [2243]DRAM simple test OK.
    [2246]rtc standby flag is 0x0, super standby flag is 0x0
    [2251]dram size =1024
    [2255]card no is 0
    [2256]sdcard 0 line count 4
    [2259][mmc]: mmc driver ver 2021-10-12 13:56
    [2264][mmc]: b mmc 0 bias 0
    [2272][mmc]: Wrong media type 0x0
    [2275][mmc]: ***Try SD card 0***
    [2284][mmc]: HSSDR52/SDR25 4 bit
    [2287][mmc]: 50000000 Hz
    [2290][mmc]: 59356 MB
    [2292][mmc]: ***SD/MMC 0 init OK!!!***
    [2402]Loading boot-pkg Succeed(index=0).
    [2406][mmc]: b mmc 0 bias 0
    [2409]Entry_name        = u-boot
    [2419]Entry_name        = monitor
    [2423]Entry_name        = dtbo
    [2426]Entry_name        = dtb
    [2430]Jump to second Boot.
    NOTICE:  BL3-1: v1.0(debug):f30a720
    NOTICE:  BL3-1: Built : 16:02:57, 2024-06-26
    NOTICE:  BL3-1 commit: 8
    NOTICE:  cpuidle init version V2.0
    ERROR:   tsp_ep_info->pc is NULL
    ERROR:   Error initializing runtime service tspd_fast
    NOTICE:  BL3-1: Preparing for EL3 exit to normal world
    NOTICE:  BL3-1: Next image address = 0x4a000000
    NOTICE:  BL3-1: Next image spsr = 0x1d3
    
    U-Boot 2018.05 (Aug 22 2024 - 10:49:30 +0800) Allwinner Technology
    
    [02.518]CPU:   Allwinner Family
    [02.521]Model: sun50iw9
    I2C:   ready
    [02.525]DRAM:  1 GiB
    [02.528]Relocation Offset is: 35eba000
    [02.576]secure enable bit: 0
    [02.579]pmu_axp152_probe pmic_bus_read fail
    [02.583]pmu_axp1530_probe pmic_bus_read fail
    [02.587]PMU: AXP2202
    [02.590]BMU: AXP2202
    [02.592][AXP2202] comm status : 0x0 = 0x18, 0x1 = 0xd5
    [02.597][AXP2202] onoff status: 0x20 = 0x1, 0x21 = 0x2
    AXP2202_IIN_LIM:38
    AXP2202_IIN_LIM:38
    [02.608][axp][err]:
    b12_mode: 0
    AXP2202_IIN_LIM:38
    FDT ERROR:fdt_get_regulator_name:get property handle twi-supply error:FDT_ERR_INTERNAL
    [02.641]battery_check pass:radio:80, vol:3968
    [02.646]CPU=1008 MHz,PLL6=600 Mhz,AHB=200 Mhz, APB1=100Mhz  MBus=400Mhz
    [02.654]drv_disp_init
    [02.688]__clk_enable: clk is null.
    [02.694]drv_disp_init finish
    [02.697]gic: sec monitor mode
    [02.729]flash init start
    [02.731]workmode = 0,storage type = 1
    [02.735]MMC:	 0
    [02.736][mmc]: mmc driver ver uboot2018:2021-07-19 14:09:00
    [02.743][mmc]: get sdc_type fail and use default host:tm1.
    [02.753][mmc]: Using default timing para
    [02.757][mmc]: SUNXI SDMMC Controller Version:0x40200
    [02.774][mmc]: card_caps:0x3000000a
    [02.777][mmc]: host_caps:0x3000003f
    [02.781]sunxi flash init ok
    [02.784]Loading Environment from SUNXI_FLASH... OK
    [02.801]out of usb burn from boot: not need burn key
    [02.806]boot_gui_init:start
    partno erro : can't find partition Reserve0
    [02.819]Get Reserve0 partition number fail!
    tcon_de_attach:de=0,tcon=0===LCD_power_on:184
    --allen--PE_input[31:0] = 0x77777777
    --allen--PE_input[31:0] = 0x6777777
    --allen--PE_pull[31:0] = 0x0
    --allen--PE_pull[31:0] = 0x5000
    --allen--PE_data[31:0] = 0xc0
    [02.847]boot_gui_init:finish
    [02.851]bmp_name=bootlogo.bmp
    partno erro : can't find partition bootloader
    ===lcd_panel_uboot_fj035fhd05_v1_init:267 lcd_type = 0
    921654 bytes read in 355 ms (2.5 MiB/s)
    [03.228]get_boot_dram_update_flag 1
    [03.231]begin to update boot0 atfer ota
    [03.237]boot0 size:65536
    size 65536
    ===allencc==: <TURNNING_DRAM> download_normal_boot0 L281,mode=0
    ===allen==: download_normal_boot0 L288
    dram para[0] = 2a0
    dram para[1] = 8
    dram para[2] = 8080808
    dram para[3] = e0e0e0e
    dram para[4] = e0e
    dram para[5] = 7887bbbb
    dram para[6] = 30fa
    dram para[7] = 4000000
    dram para[8] = 0
    dram para[9] = 34
    dram para[10] = 1b
    dram para[11] = 33
    dram para[12] = 3
    dram para[13] = 0
    dram para[14] = 0
    dram para[15] = 4
    dram para[16] = 72
    dram para[17] = 0
    dram para[18] = 9
    dram para[19] = 0
    dram para[20] = 0
    dram para[21] = 24
    dram para[22] = 0
    dram para[23] = 0
    dram para[24] = 1
    dram para[25] = 0
    dram para[26] = 3c808080
    dram para[27] = 402f6633
    dram para[28] = 26292927
    dram para[29] = 5060706
    dram para[30] = 2006c61
    dram para[31] = 0
    storage type = 1
    [03.325]sunxi_flash_mmc_download_spl: write back spl done
    [03.343]sunxi_flash_mmc_download_spl: write main spl done
    [03.348]update boot0 success
    [03.352]Item0 (Map) magic is bad
    [03.354]the secure storage item0 copy0 magic is bad
    [03.360]Item0 (Map) magic is bad
    [03.363]the secure storage item0 copy1 magic is bad
    [03.367]Item0 (Map) ===LCD_bl_open:203
    [03.373]LCD open finish
    magic is bad
    [03.380]update dts
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    partno erro : can't find partition private
    [03.444]update part info
    start detect rtc domain...
    rtc domain status: okay [0x90000000]
    [03.460]update bootcmd
    [03.462]No ethernet found.
    Hit any key to stop autoboot:  0
    Android's image name: sun50i_arm64
    [04.378]Starting kernel ...
    
    [04.380][mmc]: MMC Device 2 not found
    [04.384][mmc]: mmc 2 not find, so not exit
    [    0.000000] Booting Linux on physical CPU 0x0
    [    0.000000] Linux version 4.9.170 (flower@flower-B85M-D2V) (gcc version 5.3.1 20160412 (Linaro GCC 5.3-2016.05) ) #1 SMP PREEMPT Thu Aug 22 10:54:04 CST 2024
    [    0.000000] Boot CPU: AArch64 Processor [410fd034]
    [    0.000000] bootconsole [earlycon0] enabled
    [    0.000000] allen_boe_lcd=0, str=old
    [    0.081644] BOOTEVENT:        81.639165: ON
    [    0.591472] sunxi:i2c_sunxi@twi3[ERR]: get supply failed!
    [    0.592114] sunxi:i2c_sunxi@twi5[ERR]: get supply failed!
    [    0.600484] axp2101-regulator axp2101-regulator.0: Setting DCDC frequency for unsupported AXP variant
    [    0.600563] axp2101-regulator axp2101-regulator.0: Error setting dcdc frequency: -22
    [  [    1.007239] uart uart1: get regulator failed
    [    1.012726] uart uart5: get regulator failed
    [    1.038917] [NAND][NE] Not found valid nand node on dts
    [    1.046777] sunxi-wlan soc@03000000:wlan: get gpio chip_en failed
    [    1.053634] sunxi-wlan soc@03000000:wlan: get gpio power_en failed
    [    1.156002] hci: request ohci0-controller gpio:272
    [    1.161710] hci: request ohci1-controller gpio:147
    [    1.381273] --[allen]-- sunxi_gpadc_probe: 321
    [    1.386471] ---[allen] sunxi_gpadc_probe: allen_gpadc_enable_flg=1
    [    1.403925] rtc-pcf8563 5-0051: low voltage detected, date/time is not reliable.
    [    1.415004] VE: get debugfs_mpp_root is NULL, please check mpp
    [    1.415004]
    [    1.423228] VE: sunxi ve debug register driver failed!
    [    1.423228]
    [    1.435078] axp2202_usb_power: axp2202-acin device is not configed, not use vbus-det
    [    1.435078]
    [    1.615573] mmc:failed to get gpios
    [    1.684850] sunxi-mmc sdc1: smc 2 p1 err, cmd 52, RTO !!
    [    1.691702] sunxi-mmc sdc1: smc 2 p1 err, cmd 52, RTO !!
    [    1.702208] sunxi-mmc sdc1: smc 2 p1 err, cmd 5, RTO !!
    [    1.708969] sunxi-mmc sdc1: smc 2 p1 err, cmd 5, RTO !!
    [    1.715719] sunxi-mmc sdc1: smc 2 p1 err, cmd 5, RTO !!
    [    1.722418] sunxi-mmc sdc1: smc 2 p1 err, cmd 5, RTO !!
    [    1.735101] ERROR: pinctrl_get for HDMI2.0 DDC fail
    [    1.758406] cpu cpu1: opp_list_debug_create_link: Failed to create link
    [    1.765901] cpu cpu1: _add_opp_dev: Failed to register opp debugfs (-12)
    [    1.773470] cpu cpu2: opp_list_debug_create_link: Failed to create link
    [    1.780973] cpu cpu2: _add_opp_dev: Failed to register opp debugfs (-12)
    [    1.788562] cpu cpu3: opp_list_debug_create_link: Failed to create link
    [    1.796014] cpu cpu3: _add_opp_dev: Failed to register opp debugfs (-12)
    [    1.862330] rtc-pcf8563 5-0051: low voltage detected, date/time is not reliable.
    [    1.870588] rtc-pcf8563 5-0051: hctosys: unable to read the hardware clock
    [    1.879871] [sound  402][CODEC-HDMI sunxi_codec_dev_probe] register codec-hdmi success
    [    1.889622] [asoc_simple_probe, 432]
    [    1.895454] [asoc_simple_probe, 432]
    [    1.900074] [asoc_simple_probe, 432]
    [    1.904206] [asoc_simple_probe, 432]
    [    1.909573] [asoc_simple_probe, 432]
    [/init]: getty is ttyS0
    [/init]: RootDevice is "/dev/mmcblk0p5" , GPT_SUPPORT=1
    [/init]: Try to load EMMC ...
    e2fsck 1.42.12 (29-Aug-2014)
    /dev/mmcblk0p5 has unsupported feature(s): metadata_csum
    e2fsck: Get a newer version of e2fsck!
    [    2.537367] systemd[1]: Failed to find module 'autofs4'
    [    2.546828] cgroup: cgroup2: unknown option "nsdelegate,memory_recursiveprot"
    [    2.555477] cgroup: cgroup2: unknown option "nsdelegate"
    
    Welcome to Ubuntu 22.04 LTS!
    
    [  OK  ] Created slice Slice /system/getty.
    [  OK  ] Created slice Slice /system/modprobe.
    [  OK  ] Created slice Slice /system/serial-getty.
    [  OK  ] Created slice User and Session Slice.
    [  OK  ] Started Dispatch Password …ts to Console Directory Watch.
    [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
    [  OK  ] Reached target Local Encrypted Volumes.
    [  OK  ] Reached target Path Units.
    [  OK  ] Reached target Remote File Systems.
    [  OK  ] Reached target Slice Units.
    [  OK  ] Reached target Swaps.
    [  OK  ] Reached target Local Verity Protected Volumes.
    [  OK  ] Listening on Syslog Socket.
    [  OK  ] Listening on initctl Compatibility Named Pipe.
    [  OK  ] Listening on Journal Audit Socket.
    [  OK  ] Listening on Journal Socket (/dev/log).
    [  OK  ] Listening on Journal Socket.
    [  OK  ] Listening on udev Control Socket.
    [  OK  ] Listening on udev Kernel Socket.
             Mounting Kernel Debug File System...
             Starting Journal Service...
             Starting Load Kernel Module configfs...
             Starting Load Kernel Module drm...
             Starting Load Kernel Module fuse...
             Starting Load Kernel Modules...
             Starting Remount Root and Kernel File Systems...
    [    4.019209] [asoc_simple_probe, 432]
             Starting Coldplug All udev Devices...
    [  OK  ] Started Journal Service.
    [  OK  ] Mounted Kernel Debug File System.
    [  OK  ] Finished Load Kernel Module configfs.
    [  OK  ] Finished Load Kernel Module drm.
    [  OK  ] Finished Load Kernel Module fuse.
    [  OK  ] Finished Load Kernel Modules.
    [  OK  ] Finished Remount Root and Kernel File Systems.
             Mounting FUSE Control File System...
             Mounting Kernel Configuration File System...
             Starting Flush Journal to Persistent Storage...
             Starting Load/Save Random Seed...
             Starting Apply Kernel Variables...
             Starting Create System Users...
    [  OK  ] Finished Coldplug All udev Devices.
    [  OK  ] Mounted FUSE Control File System.
    [  OK  ] Mounted Kernel Configuration File System.
    [  OK  ] Finished Flush Journal to Persistent Storage.
    [  OK  ] Finished Apply Kernel Variables.
    [  OK  ] Finished Create System Users.
             Starting Create Static Device Nodes in /dev...
    [  OK  ] Finished Create Static Device Nodes in /dev.
    [  OK  ] Reached target Preparation for Local File Systems.
    [  OK  ] Reached target Local File Systems.
             Starting Set Up Additional Binary Formats...
             Starting Create Volatile Files and Directories...
             Starting Rule-based Manage…for Device Events and Files...
             Starting Uncomplicated firewall...
    [FAILED] Failed to start Set Up Additional Binary Formats.
    See 'systemctl status systemd-binfmt.service' for details.
    [  OK  ] Finished Create Volatile Files and Directories.
    [  OK  ] Finished Uncomplicated firewall.
    [  OK  ] Reached target Preparation for Network.
             Starting Network Name Resolution...
             Starting Record System Boot/Shutdown in UTMP...
    [  OK  ] Started Rule-based Manager for Device Events and Files.
    [  OK  ] Finished Record System Boot/Shutdown in UTMP.
    [  OK  ] Reached target System Initialization.
    [  OK  ] Started Daily dpkg database backup timer.
    [  OK  ] Started Periodic ext4 Onli…ata Check for All Filesystems.
    [  OK  ] Started Discard unused blocks once a week.
    [  OK  ] Started Daily rotation of log files.
    [    5.635591] proc: unrecognized mount option "hidepid=invisible" or missing value
    [  OK  ] Started Daily man-db regeneration.
    [  OK  ] Started Message of the Day.
    [  OK  ] Started Daily Cleanup of Temporary Directories.
    [  OK  ] Reached target Timer Units.
    [  OK  ] Listening on D-Bus System Message Bus Socket.
    [  OK  ] Listening on UUID daemon activation socket.
    [  OK  ] Reached target Socket Units.
    [  OK  ] Reached target Basic System.
    [  OK  ] Started Regular background program processing daemon.
    [  OK  ] Started D-Bus System Message Bus.
             Starting Network Manager...
    [  OK  ] Started Save initial kernel messages after boot.
             Starting Remove Stale Onli…t4 Metadata Check Snapshots...
             Starting launcher.service...
             Starting Dispatcher daemon for systemd-networkd...
             Starting Authorization Manager...
             Starting System Logging Service...
             Starting User Login Management...
             Starting WPA supplicant...
    [  OK  ] Started Network Name Resolution.
    [  OK  ] Found device /dev/ttyS0.
    [  OK  ] Reached target Host and Network Name Lookups.
    [  OK  ] Reached target Hardware activated USB gadget.
             Starting Save/Restore Sound Card State...
    [  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
             Starting Load/Save RF Kill Switch Status...
    [  OK  ] Started Load/Save RF Kill Switch Status.
    [  OK  ] Started System Logging Service.
    [  OK  ] Finished Save/Restore Sound Card State.
    [  OK  ] Reached target Sound Card.
    [  OK  ] Started launcher.service.
    [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
    [  OK  ] Started User Login Management.
    [  OK  ] Started WPA supplicant.
    [  OK  ] Started Network Manager.
    [  OK  ] Started Authorization Manager.
    [  OK  ] Reached target Network.
             Starting Modem Manager...
             Starting /etc/rc.local Compatibility...
             Starting OpenBSD Secure Shell server...
             Starting Hostname Service...
             Starting Permit User Sessions...
    [  OK  ] Started Unattended Upgrades Shutdown.
    [  OK  ] Finished Permit User Sessions.
    [    8.234763] sunxi-mmc sdc1: smc 2 p1 err, cmd 52, RTO !!
    [    8.241559] sunxi-mmc sdc1: smc 2 p1 err, cmd 52, RTO !!
    [    8.755449] proc: unrecognized mount option "hidepid=invisible" or missing value
    [    9.101497] [asoc_simple_probe, 432]
    [  OK  ] Started /etc/rc.local Compatibility.
    [    9.133052] [asoc_simple_probe, 432]
             Stopping Network Manager...
    [  OK  ] Started Getty on tty1.
    [  OK  ] Started Serial Getty on ttyS0.
    [  OK  ] Reached target Login Prompts.
    [  OK  ] Started Hostname Service.
             Starting Network Manager Script Dispatcher Service...
    [  OK  ] Started Modem Manager.
    [  OK  ] Started Network Manager Script Dispatcher Service.
    [  OK  ] Started Dispatcher daemon for systemd-networkd.
    [  OK  ] Stopped Network Manager.
             Starting Network Manager...
    [  OK  ] Started Network Manager.
             Starting Bluetooth service...
    [  OK  ] Started Bluetooth service.
    [   10.904406] rtc-pcf8563 5-0051: low voltage detected, date/time is not reliable.
    
    Ubuntu 22.04 LTS ANBERNIC ttyS0
    
    ANBERNIC login: [   13.675395] Bluetooth: Non-link packet received in non-active state
    
[/code]
## FEL mode
Booting with a USB-C cable connected to the USB-OTG port (DC/OTG at top of the device) without an SD card inserted triggers FEL mode. 
# Adding a serial port (**voids warranty**)
UART pads are on placed on the left side of the PCB, close to AXP717 chip (see attached photo). They are not marked in any way. 
[![][7555]][7556]
[][7557]
UART pads
## Device disassembly
Remove the four Torx T5 screws from the rear case. There's a small gap between the back and the rest of the case, just use a pick to open it up. The L2/R2 buttons are screwed to the rest of the case, once they are removed, L1/R1 buttons may fall out, but they are easy to reinsert. The buttons at the top are also loose, so be careful not to lose them. 
## Locating the UART
See attached photo 
# Pictures
  * [![RG40XX H front.jpg][7558]][7529]
  * [![RG40XX H back.jpg][7559]][7560]
  * [![RG40XX H pcb top.jpg][7561]][7562]
  * [![RG40XX H pcb bottom.jpg][7563]][7564]
  * [![RG40XX H inside pcb removed.jpg][7565]][7566]

# See also
[H700][7532]
[Anbernic_RG35XX_Plus][7536]
## Manufacturer images
[Vendor firmware][7567]
