# Tronsmart Draco H3
Tronsmart Draco H3  
---  
[![Tronsmart Draco H3.jpg][55889]][55890]  
Manufacturer |  [Tronsmart][55891]  
Release Date |  April 2015   
Website |  [Device Product Page][55892]  
Specifications   
SoC |  [H3][55893]  
DRAM |  1GiB   
eMMC |  8GB (FORESEE NCEFES78-08G)   
Power |  DC 5V via MicroUSB   
Features   
Video |  HDMI   
Audio |  HDMI   
Network |  BT4.0/WiFi 802.11 b/g/n ([Ampak AP6212][55894])   
Storage |  eMMC, µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][55895] and the [New Device Page guide][55896].
## Contents
  * [1 Identification][55897]
  * [2 Sunxi support][55898]
    * [2.1 Current status][55899]
    * [2.2 Images][55900]
    * [2.3 HW-Pack][55901]
    * [2.4 BSP][55902]
    * [2.5 Manual build][55903]
      * [2.5.1 U-Boot][55904]
        * [2.5.1.1 Sunxi/Legacy U-Boot][55905]
        * [2.5.1.2 Mainline U-Boot][55906]
      * [2.5.2 Linux Kernel][55907]
        * [2.5.2.1 Sunxi/Legacy Kernel][55908]
        * [2.5.2.2 Mainline kernel][55909]
  * [3 Tips, Tricks, Caveats][55910]
    * [3.1 FEL mode][55911]
    * [3.2 Device specific topic][55912]
    * [3.3 ...][55913]
  * [4 Adding a serial port (**voids warranty**)][55914]
    * [4.1 Device disassembly][55915]
    * [4.2 Locating the UART][55916]
  * [5 Pictures][55917]
  * [6 Schematic][55918]
  * [7 Also known as][55919]
  * [8 See also][55920]
    * [8.1 Manufacturer images][55921]

# Identification
On the front of the device, the following is printed: 
[code] 
    Tronsmart Draco H3
[/code]
In android, under Settings->About Device, you will find: 
  * Model Number: _Draco H3_
  * Build Number: _dolphin-fvd-p1-end 4.4.2 KOT49H 20150619 test-keys_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][55920]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][55922] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
No official support yet. Boots with **orangepi_pc_defconfig**
### Linux Kernel
#### Sunxi/Legacy Kernel
Only useful for A10/A10s/A13 and A20 based devices. Remove this section otherwise.
Use the [_MANUFACTURER_DEVICE.fex_][55923] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][55924]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][55925]][55926]
[][55927]
Draco H3 UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][55928]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
The two halves of the case are held together with clips. It can be pried apart carefully. The _Fn_ button will fall out when you do so. 
## Locating the UART
UART is located on the four obvious through-holes. 
Pin | Function   
---|---  
1 | Gnd   
2 | RX   
3 | TX   
4 | ?   
# Pictures
  * [![Tronsmart Draco H3 PCB front.jpg][55929]][55930]
  * [![Tronsmart Draco H3 PCB back.jpg][55931]][55932]

# Schematic
No schematic is available, but here is some hardware info gathered from the stock android build: 
**GPIO mapping:**
[code] 
    # cat /sys/kernel/debug/gpio
    GPIOs 0-383, platform/sunxi-pinctrl, sunxi-pinctrl:
     gpio-15  (?                   ) out hi
     gpio-16  (?                   ) out hi
     gpio-166 (cd                  ) in  hi
     gpio-205 (?                   ) out hi
     gpio-354 (?                   ) out hi
     gpio-355 (?                   ) out hi
     gpio-362 (?                   ) out lo
    # ls -l /sys/class/gpio_sw
    lrwxrwxrwx root     root              2021-12-15 13:23 PA15 -> ../../devices/platform/gpio_sw.1/gpio_sw/PA15
    lrwxrwxrwx root     root              2021-12-15 13:23 PL10 -> ../../devices/platform/gpio_sw.0/gpio_sw/PL10
    lrwxrwxrwx root     root              1970-01-01 19:00 normal_led -> ../../devices/platform/gpio_sw.1/gpio_sw/PA15
    lrwxrwxrwx root     root              1970-01-01 19:00 standby_led -> ../../devices/platform/gpio_sw.0/gpio_sw/PL10
    
[/code]
**Pinctrl mapping:**
[code] 
    # cat /sys/kernel/debug/pinctrl/pinctrl-handles
    Requested pin control handlers their pinmux maps:
    device: sunxi-pinctrl current state: none
    device: twi0 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PA11 (11) function: twi0 (10)
        type: MUX_GROUP controller sunxi-pinctrl group: PA12 (12) function: twi0 (10)
      state: suspend
        type: MUX_GROUP controller sunxi-pinctrl group: PA11 (11) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PA12 (12) function: io_disable (5)
    device: twi1 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PA18 (18) function: twi1 (16)
        type: MUX_GROUP controller sunxi-pinctrl group: PA19 (19) function: twi1 (16)
      state: suspend
        type: MUX_GROUP controller sunxi-pinctrl group: PA18 (18) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PA19 (19) function: io_disable (5)
    device: uart0 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PA4 (4) function: uart0 (7)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PA4 (4) 00010002
        type: MUX_GROUP controller sunxi-pinctrl group: PA5 (5) function: uart0 (7)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PA5 (5) 00010002
      state: suspend
        type: MUX_GROUP controller sunxi-pinctrl group: PA4 (4) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PA5 (5) function: io_disable (5)
    device: uart1 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PG6 (88) function: uart1 (26)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PG6 (88) 00010002
        type: MUX_GROUP controller sunxi-pinctrl group: PG7 (89) function: uart1 (26)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PG7 (89) 00010002
        type: MUX_GROUP controller sunxi-pinctrl group: PG8 (90) function: uart1 (26)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PG8 (90) 00010002
        type: MUX_GROUP controller sunxi-pinctrl group: PG9 (91) function: uart1 (26)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PG9 (91) 00010002
      state: suspend
        type: MUX_GROUP controller sunxi-pinctrl group: PG6 (88) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PG7 (89) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PG8 (90) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PG9 (91) function: io_disable (5)
    device: ts0 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PE0 (59) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE1 (60) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE2 (61) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE3 (62) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE4 (63) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE5 (64) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE6 (65) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE7 (66) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE8 (67) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE9 (68) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE10 (69) function: ts0 (22)
        type: MUX_GROUP controller sunxi-pinctrl group: PE11 (70) function: ts0 (22)
      state: suspend
        type: MUX_GROUP controller sunxi-pinctrl group: PE0 (59) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE1 (60) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE2 (61) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE3 (62) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE4 (63) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE5 (64) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE6 (65) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE7 (66) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE8 (67) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE9 (68) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE10 (69) function: io_disable (5)
        type: MUX_GROUP controller sunxi-pinctrl group: PE11 (70) function: io_disable (5)
    device: s_cir0 current state: default
      state: default
        type: MUX_GROUP controller sunxi-pinctrl group: PL11 (107) function: s_cir0 (32)
        type: CONFIGS_GROUP controller sunxi-pinctrl group PL11 (107) 00010002
      state: suspend
        type: MUX_GROUP controller sunxi-pinctrl group: PL11 (107) function: io_disable (5)
    
[/code]
**Bootloader log:**
[code] 
    HELLO! BOOT0 is starting!
    boot0 version : 4.0.0
    fel_flag = 0x00000000
    rtc[0] value = 0x00000000
    rtc[1] value = 0x00000000
    rtc[2] value = 0x00000000
    rtc[3] value = 0x00000000
    rtc[4] value = 0x00000000
    rtc[5] value = 0x00000000
    rtc[6] value = 0x00000000
    rtc[7] value = 0x00000000
    DRAM DRIVE INFO: V1.3
    the chip id is 0x00000081
    the chip id is 0x00000081
    the chip id is 0x00000081
    the chip id is 0x00000081
    the chip id is 0x00000081
    the gpio type set is 0x00000000
    READ DQS LCDL = 00232223
    DRAM Type = 3 (2:DDR2,3:DDR3,6:LPDDR2,7:LPDDR3)
    DRAM CLK = 576 MHz
    DRAM zq value: 003b3bfb
    DRAM dram para1: 10f40400
    DRAM dram para2: 00000000
    DRAM workmode1: 000009f4
    DRAM SIZE =1024 M
    odt delay
    dram size =1024
    card boot number = 2
    card no is 2
    sdcard 2 line count 8
    [mmc]: mmc driver ver 2015-04-13 16:07:39
    [mmc]: ***Try SD card 2***
    [mmc]: mmc 2 cmd 8 err 00000100
    [mmc]: mmc 2 cmd 8 err 00000100
    [mmc]: mmc 2 send if cond failed
    [mmc]: mmc 2 cmd 55 err 00000100
    [mmc]: mmc 2 cmd 55 err 00000100
    [mmc]: mmc 2 send app cmd failed
    [mmc]: ***Try MMC card 2***
    [mmc]: mmc re-update_phase
    [mmc]: mmc re-update_phase
    [mmc]: 8bit ddr!!!
    [mmc]: mmc re-update_phase
    [mmc]: MMC ver 4.5
    [mmc]: SD/MMC Card: 8bit, capacity: 7393MB
    [mmc]: vendor: Man 00880103 Snr 359cfe3e
    [mmc]: product: NCard
    [mmc]: revision: 2.0
    [mmc]: ***SD/MMC 2 init OK!!!***
    sdcard 2 init ok
    The size of uboot is 000dc000.
    sum=c691213e
    src_sum=c691213e
    set_mmc_para,sdly 50M 0
    set_mmc_para,sdly 25M 0
    Succeed in loading uboot from sdmmc flash.
    Ready to disable icache.
    Jump to secend Boot.
    SUNXI_NORMAL_MODE
    [      0.315]e mode
    
    U-Boot 2011.09-rc1-00003-g9c79696 (Apr 16 2015 - 20:12:04) Allwinner Technology
    
    [      0.324]version: 1.1.0
    normal mode
    [      0.331]pmbus:   ready
    not set main pmu id
    axp_probe error
    gpio value=0x0
    cpux freq run low
    [      0.371]PMU: pll1 1008 Mhz,PLL6=600 Mhz
    AXI=336 Mhz,AHB=200 Mhz, APB1=100 Mhz
    sid read already
    fel key new mode
    run key detect
    no key found
    no key input
    dram_para_set start
    dram_para_set end
    normal mode
    [      0.402]DRAM:  1 GiB
    relocation Offset is: 35af7000
    [box standby] read rtc = 0x0
    [box_start_os] mag be start_type no use
    user_gpio config
    user_gpio ok
    gic: normal or no secure os mode
    workmode = 0
    MMC:     2
    [      0.481][mmc]: mmc driver ver 2015-04-13 14:50:00
    [      0.486][mmc]: get sdc_phy_wipe fail.
    [      0.490][mmc]: get sdc0 sdc_erase fail.
    [      0.494][mmc]: get sdc_2xmode ok, val = 1
    [      0.498][mmc]: get sdc_ddrmode ok, val = 1
    [      0.502][mmc]: get sdc_f_max fail,use default  50000000Hz
    [      0.508][mmc]: get card_line ok, card_line = 8
    [      0.512][mmc]: get sdc_ex_dly_used fail,use default
    [      0.517][mmc]: SUNXI SD/MMC: 2
    [      0.531][mmc]: *Try SD card 2*
    [      0.534][mmc]: mmc 2 cmd 8 err 100
    [      0.540][mmc]: mmc send if cond failed
    [      0.544][mmc]: mmc 2 cmd 55 err 100
    [      0.549][mmc]: send app cmd failed
    [      0.552][mmc]: *Try MMC card 2*
    [      0.605][mmc]: mmc re-update_phase
    [      0.610][mmc]: mmc re-update_phase
    [      0.618][mmc]: mmc re-update_phase
    [      0.623][mmc]: ddr8
    [      0.629][mmc]: mmc re-update_phase
    [      0.646][mmc]: CID 0x8801034e 0x43617264 0x20359cfe 0x3e568259
    [      0.651][mmc]: MMC ver 4.5
    [      0.654][mmc]: mmc clk 50000000
    [      0.657][mmc]: SD/MMC Card: 8bit, capacity: 7393MB
    [      0.662][mmc]: boot0 capacity: 4000KB,boot1 capacity: 4000KB
    [      0.668][mmc]: ***SD/MMC 2 init OK!!!***
    [      0.718][mmc]: erase_grp_size:0x400WrBlk * 0x200 = 0x80000 Byte
    [      0.724][mmc]: secure_feature 0x15
    [      0.727][mmc]: secure_removal_type  0x0
    [      0.731]sunxi flash init ok
    script config pll_de to 864 Mhz
    Not Found clk pll_video1 in script
    script config pll_video to 297 Mhz
    [boot]disp_init_tv
    [DISP_TV] disp_init_tv enter g_tv_used
    screen 0 do not support TV TYPE!
    [BOOOT_DISP_TV] disp tv device_registered
    axp chipid not care,use default regulator tree
    unable to find regulator vcc-hdmi-18 from [pmu1_regu] or [pmu2_regu]
    enable power vcc-hdmi-18, ret=-1
    DRV_DISP_Init end
    boot_disp.auto_hpd=1
    auto hpd check has 100 times!
    auto check no any connected, the output_type is 4
    read byte = 10
    [get_display_resolution] = 404
    get the output mode from android(saved by type[4]) is 4
    not support this mode[4], use inline mode[4]
    attched ok, mgr0<-->device0, type=4, mode=4----
    ready to set mode
    [      2.225]finally, output_type=0x4, output_mode=0x4, screen_id=0x0, disp_para=0x0
    read byte = 10
    [get_display_resolution] = 404
    read byte = 10
    [get_display_resolution] = 20b
    In:    serial
    Out:   serial
    Err:   serial
    --------fastboot partitions--------
    -total partitions:14-
    -name-        -start-       -size-
    bootloader  : 1000000       1000000
    env         : 2000000       1000000
    boot        : 3000000       1000000
    system      : 4000000       34000000
    misc        : 38000000      1000000
    recovery    : 39000000      2000000
    sysrecovery : 3b000000      30000000
    private     : 6b000000      1000000
    Reserve0    : 6c000000      1000000
    klog        : 6d000000      1000000
    Reserve1    : 6e000000      2000000
    Reserve2    : 70000000      1000000
    cache       : 71000000      28000000
    UDISK       : 99000000      0
    -----------------------------------
    base bootcmd=run setargs_nand boot_normal
    bootcmd set setargs_mmc
    key 0
    cant find rcvy value
    cant find fstbt value
    misc partition found
    to be run cmd=run setargs_mmc boot_normal
    the secure storage map is empty
    no item name mac in the map
    sunxi storage read fail
    no item name wifi_mac in the map
    sunxi storage read fail
    no item name bt_mac in the map
    sunxi storage read fail
    no item name specialstr in the map
    sunxi storage read fail
    no item name serialno in the map
    sunxi storage read fail
    check user data form private
    the user data'magic is bad
    WORK_MODE_BOOT
    adver not need show
    sunxi_bmp_logo_display
    f_read btr over hd12896
    read byte = 3686454
    [      2.866]screen_id =0, screen_width =1280, screen_height =720
    [      2.872]frame buffer address 46400036
    [      2.876]Hit any key to stop autoboot:  0
    read boot or recovery all
    [      3.286]sunxi flash read :offset 3000000, 12942284 bytes OK
    [      3.294]ready to boot
    board_display_setenv:  disp_para=0 init_disp=20b0404
    [      3.301][mmc]: mmc exit start
    [      3.316][mmc]: mmc 2 cmd 8 err 100
    [      3.321][mmc]: mmc send if cond failed
    [      3.325][mmc]: mmc 2 cmd 55 err 100
    [      3.330][mmc]: send app cmd failed
    [      3.342][mmc]: get sdc_phy_wipe fail.
    [      3.346][mmc]: get sdc0 sdc_erase fail.
    [      3.350][mmc]: get sdc_2xmode ok, val = 1
    [      3.354][mmc]: get sdc_ddrmode ok, val = 1
    [      3.358][mmc]: get sdc_f_max fail,use default  50000000Hz
    [      3.363][mmc]: get card_line ok, card_line = 8
    [      3.368][mmc]: get sdc_ex_dly_used fail,use default
    [      3.373][mmc]: mmc 2 exit ok
    [      3.376]
    Starting kernel ...
    
    [sun8i_fixup]: From boot, get meminfo:
            Start:  0x40000000
            Size:   1024MB
    ion_carveout reserve: 160m@0 300m@0 130m@1 200m@1
    ion_reserve_common: ion reserve: [0x4d400000, 0x60000000]!
    
[/code]
  
**Kernel dmesg log:**
[code] 
    [    0.000000] Booting Linux on physical CPU 0
    [    0.000000] Initializing cgroup subsys cpu
    [    0.000000] Linux version 3.4.39 (root@cx-server) (gcc version 4.6.3 20120201 (prerelease) (crosstool-NG linaro-1.13.1-2012.02-20120222 - Linaro GCC 2012.02) ) #1 SMP PREEMPT Tue Jun 9 14:48:17 CST 2015
    [    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c5387d
    [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
    [    0.000000] Machine: sun8i
    [    0.000000] cma: CMA: reserved 300 MiB at 4d400000
    [    0.000000] Memory policy: ECC disabled, Data cache writealloc
    [    0.000000] On node 0 totalpages: 262144
    [    0.000000] free_area_init_node: node 0, pgdat c09525c0, node_mem_map c120b000
    [    0.000000]   Normal zone: 1404 pages used for memmap
    [    0.000000]   Normal zone: 0 pages reserved
    [    0.000000]   Normal zone: 158340 pages, LIFO batch:31
    [    0.000000]   HighMem zone: 900 pages used for memmap
    [    0.000000]   HighMem zone: 101500 pages, LIFO batch:31
    [    0.000000] script_init enter!
    [    0.000000] script_init exit!
    [    0.000000] PERCPU: Embedded 8 pages/cpu @c1b21000 s11264 r8192 d13312 u32768
    [    0.000000] pcpu-alloc: s11264 r8192 d13312 u32768 alloc=8*4096
    [    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3
    [    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 259840
    [    0.000000] Kernel command line: console=ttyS0,115200 root=/dev/block/mmcblk0p7 init=/init loglevel=8 vmalloc=384M partitions=bootloader@mmcblk0p2:env@mmcblk0p5:boot@mmcblk0p6:system@mmcblk0p7:misc@mmcblk0p8:recovery@mmcblk0p9:sysrecovery@mmcblk0p10:private@mmcblk0p11:Reserve0@mmcblk0p12:klog@mmcblk0p13:Reserve1@mmcblk0p14:Reserve2@mmcblk0p15:cache@mmcblk0p16:UDISK@mmcblk0p1 mac_addr= wifi_mac= bt_mac= specialstr= serialno= boot_type=2 disp_para=404 init_disp=20b0404 fb_base=0x46400000 config_size=35120 axp_chipid=-1
    [    0.000000] PID hash table entries: 4096 (order: 2, 16384 bytes)
    [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
    [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
    [    0.000000] Memory: 1024MB = 1024MB total
    [    0.000000] Memory: 716864k/716864k available, 331712k reserved, 409600K highmem
    [    0.000000] Virtual kernel memory layout:
    [    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
    [    0.000000]     fixmap  : 0xfff00000 - 0xfffe0000   ( 896 kB)
    [    0.000000]     vmalloc : 0xe7800000 - 0xff000000   ( 376 MB)
    [    0.000000]     lowmem  : 0xc0000000 - 0xe7000000   ( 624 MB)
    [    0.000000]     pkmap   : 0xbfe00000 - 0xc0000000   (   2 MB)
    [    0.000000]     modules : 0xbf000000 - 0xbfe00000   (  14 MB)
    [    0.000000]       .text : 0xc0008000 - 0xc088d2fc   (8725 kB)
    [    0.000000]       .init : 0xc088e000 - 0xc08ddc00   ( 319 kB)
    [    0.000000]       .data : 0xc08de000 - 0xc0954f60   ( 476 kB)
    [    0.000000]        .bss : 0xc0955714 - 0xc0b28920   (1869 kB)
    [    0.000000] Preemptible hierarchical RCU implementation.
    [    0.000000]       Additional per-CPU info printed with stalls.
    [    0.000000] NR_IRQS:544
    [    0.000000] Architected local timer running at 24.00MHz.
    [    0.000000] Switching to timer-based delay loop
    [    0.000000] sched_clock: 32 bits at 24MHz, resolution 41ns, wraps every 178956ms
    [    0.000000] Console: colour dummy device 80x30
    [    0.000247] Calibrating delay loop (skipped), value calculated using timer frequency.. 4800.00 BogoMIPS (lpj=24000000)
    [    0.000272] pid_max: default: 32768 minimum: 301
    [    0.000695] Mount-cache hash table entries: 512
    [    0.001786] Initializing cgroup subsys debug
    [    0.001805] Initializing cgroup subsys cpuacct
    [    0.001817] Initializing cgroup subsys freezer
    [    0.001858] CPU: Testing write buffer coherency: ok
    [    0.001914] ftrace: allocating 23363 entries in 69 pages
    [    0.030289] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
    [    0.030309] [sunxi_smp_prepare_cpus] enter
    [    0.030349] Setting up static identity map for 0x40603d40 - 0x40603d98
    [    0.031394] CPU1: Booted secondary processor
    [    0.031394] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
    [    0.031528] CPU2: Booted secondary processor
    [    0.031528] CPU2: thread -1, cpu 2, socket 0, mpidr 80000002
    [    0.031528] CPU3: Booted secondary processor
    [    0.031528] CPU3: thread -1, cpu 3, socket 0, mpidr 80000003
    [    0.040202] Brought up 4 CPUs
    [    0.040222] SMP: Total of 4 processors activated (19200.00 BogoMIPS).
    [    0.040831] devtmpfs: initialized
    [    0.045188] wakeup src cnt is : 2.
    [    0.045201] [exstandby]leave extended_standby_enable_wakeup_src : event 0x800000
    [    0.045214] [exstandby]leave extended_standby_enable_wakeup_src : wakeup_gpio_map 0x0
    [    0.045226] [exstandby]leave extended_standby_enable_wakeup_src : wakeup_gpio_group 0x40
    [    0.045239] [exstandby]leave extended_standby_enable_wakeup_src : event 0x800000
    [    0.045251] [exstandby]leave extended_standby_enable_wakeup_src : wakeup_gpio_map 0x0
    [    0.045263] [exstandby]leave extended_standby_enable_wakeup_src : wakeup_gpio_group 0x40
    [    0.045276] sunxi pm init
    [    0.045725] pinctrl core: initialized pinctrl subsystem
    [    0.061030] NET: Registered protocol family 16
    [    0.062123] DMA: preallocated 2048 KiB pool for atomic coherent allocations
    [    0.062123] script_sysfs_init success
    [    0.062123] sunxi_dump_init success
    [    0.062123] gpiochip_add: registered GPIOs 0 to 383 on device: sunxi-pinctrl
    [    0.062123] sunxi-pinctrl sunxi-pinctrl: initialized sunXi PIO driver
    [    0.062667] hw-breakpoint: found 5 (+1 reserved) breakpoint and 4 watchpoint registers.
    [    0.062684] hw-breakpoint: maximum watchpoint size is 8 bytes.
    [    0.062979] [sunxi-module]: [sunxi-module.0] probe success
    [    0.063022] script config pll_video to 297 Mhz
    [    0.063040] script config pll_de to 864 Mhz
    [    0.063055] script config pll_ve to 402 Mhz
    [    0.063085] sunxi_default_clk_init
    [    0.063096] try to set pll6ahb1 to 200000000
    [    0.063117] try to set ahb clk source to pll6ahb1
    [    0.063127] set ahb clk source to pll6ahb1
    [    0.063138] try to set ahb1 to 200000000
    [    0.063151] try to set apb1 to 100000000
    [    0.063918] ===fe3o4==== sunxi_root_procfs_attach ret:0
    [    0.070416] bio: create slab <bio-0> at 0
    [    0.070496] [ARISC] :sunxi-arisc driver v1.04
    [    0.085323] [ARISC] :arisc version: [v0.1.52]
    [    0.085345] [sunxi-module]: arisc register success
    [    0.160815] [ARISC] :sunxi-arisc driver v1.04 startup succeeded
    [    0.170540] SCSI subsystem initialized
    [    0.170764] usbcore: registered new interface driver usbfs
    [    0.170846] usbcore: registered new interface driver hub
    [    0.170881] usbcore: registered new device driver usb
    [    0.170881] twi_chan_cfg()340 - [twi0] has no twi_regulator.
    [    0.170881] twi_chan_cfg()340 - [twi1] has no twi_regulator.
    [    0.170881] twi_chan_cfg()340 - [twi2] has no twi_regulator.
    [    0.170881] Linux video capture interface: v2.00
    [    0.171068] Advanced Linux Sound Architecture Driver Version 1.0.25.
    [    0.171659] Bluetooth: Core ver 2.16
    [    0.171702] NET: Registered protocol family 31
    [    0.171713] Bluetooth: HCI device and connection manager initialized
    [    0.171727] Bluetooth: HCI socket layer initialized
    [    0.171738] Bluetooth: L2CAP socket layer initialized
    [    0.171778] Bluetooth: SCO socket layer initialized
    [    0.172029] cfg80211: Calling CRDA to update world regulatory domain
    [    0.172094] Switching to clocksource arch_sys_counter
    [    0.187925] FS-Cache: Loaded
    [    0.188232] CacheFiles: Loaded
    [    0.200642] NET: Registered protocol family 2
    [    0.200951] IP route cache hash table entries: 32768 (order: 5, 131072 bytes)
    [    0.201629] TCP established hash table entries: 131072 (order: 8, 1048576 bytes)
    [    0.203525] TCP bind hash table entries: 65536 (order: 7, 786432 bytes)
    [    0.204451] TCP: Hash tables configured (established 131072 bind 65536)
    [    0.204464] TCP: reno registered
    [    0.204479] UDP hash table entries: 512 (order: 2, 16384 bytes)
    [    0.204517] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes)
    [    0.204866] NET: Registered protocol family 1
    [    0.205350] RPC: Registered named UNIX socket transport module.
    [    0.205363] RPC: Registered udp transport module.
    [    0.205373] RPC: Registered tcp transport module.
    [    0.205383] RPC: Registered tcp NFSv4.1 backchannel transport module.
    [    0.205611] Unpacking initramfs...
    [    0.392064] Freeing initrd memory: 2088K
    [    0.392703] hw perfevents: enabled with ARMv7 Cortex_A7 PMU driver, 5 counters available
    [    0.392838] sunxi_reg_init enter
    [    0.393786] audit: initializing netlink socket (disabled)
    [    0.393844] type=2000 audit(0.390:1): initialized
    [    0.395075] highmem bounce pool size: 64 pages
    [    0.397247] NTFS driver 2.1.30 [Flags: R/W].
    [    0.397458] fuse init (API version 7.18)
    [    0.397967] msgmni has been set to 1204
    [    0.399042] io scheduler noop registered
    [    0.399054] io scheduler deadline registered
    [    0.399172] io scheduler cfq registered (default)
    [    0.399532] [DISP]disp_module_init
    [    0.399873] cmdline,disp=404
    [    0.467045] [DISP]disp_module_init finish
    [    0.467273] sw_uart_get_devinfo()1503 - uart0 has no uart_regulator.
    [    0.467290] sw_uart_get_devinfo()1503 - uart1 has no uart_regulator.
    [    0.467713] uart0: ttyS0 at MMIO 0x1c28000 (irq = 32) is a SUNXI
    [    0.467728] sw_uart_pm()890 - uart0 clk is already enable
    [    0.467749] sw_console_setup()1233 - console setup baud 115200 parity n bits 8, flow n
    [    0.563869] console [ttyS0] enabled
    [    1.045567] uart1: ttyS1 at MMIO 0x1c28400 (irq = 33) is a SUNXI
    [    1.413080] sunxi_cmatest_init enter
    [    1.417092] sunxi_cmatest_init success
    [    1.421476] sunxi_di_init get di_by_pass err!
    [    1.431291] loop: module loaded
    [    1.435009] sunxi_spi_chan_cfg()1377 - [spi-0] has no spi_regulator.
    [    1.442114] sunxi_spi_chan_cfg()1377 - [spi-1] has no spi_regulator.
    [    1.449217] tun: Universal TUN/TAP device driver, 1.6
    [    1.454852] tun: (C) 1999-2004 Max Krasnyansky <[[email protected]][55933]>
    [    1.462125] gmac0 not be used
    [    1.465455] gmac0: probe of gmac0 failed with error -22
    [    1.471326] PPP generic driver version 2.4.2
    [    1.476251] PPP BSD Compression module registered
    [    1.481507] PPP Deflate Compression module registered
    [    1.487911] PPP MPPE Compression module registered
    [    1.493274] NET: Registered protocol family 24
    [    1.498245] PPTP driver version 0.8.5
    [    1.502626] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    [    1.529970] sunxi-ehci sunxi-ehci.1: SW USB2.0 'Enhanced' Host Controller (EHCI) Driver
    [    1.538925] sunxi-ehci sunxi-ehci.1: new USB bus registered, assigned bus number 1
    [    1.547960] sunxi-ehci sunxi-ehci.1: irq 104, io mem 0xf1c1a000
    [    1.570038] sunxi-ehci sunxi-ehci.1: USB 0.0 started, EHCI 1.00
    [    1.577311] hub 1-0:1.0: USB hub found
    [    1.581521] hub 1-0:1.0: 1 port detected
    [    1.606319] sunxi-ehci sunxi-ehci.2: SW USB2.0 'Enhanced' Host Controller (EHCI) Driver
    [    1.615263] sunxi-ehci sunxi-ehci.2: new USB bus registered, assigned bus number 2
    [    1.624215] sunxi-ehci sunxi-ehci.2: irq 106, io mem 0xf1c1b000
    [    1.650045] sunxi-ehci sunxi-ehci.2: USB 0.0 started, EHCI 1.00
    [    1.656638] ehci_irq: highspeed device connect
    [    1.661716] hub 2-0:1.0: USB hub found
    [    1.665894] hub 2-0:1.0: 1 port detected
    [    1.690699] sunxi-ehci sunxi-ehci.4: SW USB2.0 'Enhanced' Host Controller (EHCI) Driver
    [    1.699624] sunxi-ehci sunxi-ehci.4: new USB bus registered, assigned bus number 3
    [    1.708570] sunxi-ehci sunxi-ehci.4: irq 110, io mem 0xf1c1d000
    [    1.730045] sunxi-ehci sunxi-ehci.4: USB 0.0 started, EHCI 1.00
    [    1.737248] hub 3-0:1.0: USB hub found
    [    1.741453] hub 3-0:1.0: 1 port detected
    [    1.746212] sunxi-ehci sunxi-ehci.4: remove, state 1
    [    1.751767] usb usb3: USB disconnect, device number 1
    [    1.758217] sunxi-ehci sunxi-ehci.4: USB bus 3 deregistered
    [    1.774506] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
    [    1.801466] sunxi-ohci sunxi-ohci.1: SW USB2.0 'Open' Host Controller (OHCI) Driver
    [    1.809999] sunxi-ohci sunxi-ohci.1: new USB bus registered, assigned bus number 3
    [    1.818469] sunxi-ohci sunxi-ohci.1: irq 105, io mem 0xf1c1a400
    [    1.870100] ehci_irq: highspeed device disconnect
    [    1.884593] hub 3-0:1.0: USB hub found
    [    1.888779] hub 3-0:1.0: 1 port detected
    [    1.913558] sunxi-ohci sunxi-ohci.2: SW USB2.0 'Open' Host Controller (OHCI) Driver
    [    1.922101] sunxi-ohci sunxi-ohci.2: new USB bus registered, assigned bus number 4
    [    1.930574] sunxi-ohci sunxi-ohci.2: irq 107, io mem 0xf1c1b400
    [    1.994670] hub 4-0:1.0: USB hub found
    [    1.998850] hub 4-0:1.0: 1 port detected
    [    2.003671] Initializing USB Mass Storage driver...
    [    2.009253] usbcore: registered new interface driver usb-storage
    [    2.015943] USB Mass Storage support registered.
    [    2.021156] usbcore: registered new interface driver ums-alauda
    [    2.027787] usbcore: registered new interface driver ums-cypress
    [    2.034540] usbcore: registered new interface driver ums-datafab
    [    2.041282] usbcore: registered new interface driver ums_eneub6250
    [    2.048215] usbcore: registered new interface driver ums-freecom
    [    2.054965] usbcore: registered new interface driver ums-isd200
    [    2.061619] usbcore: registered new interface driver ums-jumpshot
    [    2.068448] usbcore: registered new interface driver ums-karma
    [    2.074999] usbcore: registered new interface driver ums-onetouch
    [    2.081866] usbcore: registered new interface driver ums-realtek
    [    2.088595] usbcore: registered new interface driver ums-sddr09
    [    2.095245] usbcore: registered new interface driver ums-sddr55
    [    2.101950] usbcore: registered new interface driver ums-usbat
    [    2.108587] usbcore: registered new interface driver usbserial
    [    2.115105] usbserial: USB Serial Driver core
    [    2.120030] usbcore: registered new interface driver option
    [    2.126264] USB Serial support registered for GSM modem (1-port)
    [    2.133510] file system registered
    [    2.139083] android_usb gadget: Mass Storage Function, version: 2009/09/11
    [    2.146771] android_usb gadget: Number of LUNs=3
    [    2.151928]  lun0: LUN: removable file: (no medium)
    [    2.157354]  lun1: LUN: removable file: (no medium)
    [    2.162797]  lun2: LUN: removable file: (no medium)
    [    2.168584] android_usb gadget: android_usb ready
    [    2.174010]  uinput result 0 , vmouse_init
    [    2.179338] mousedev: PS/2 mouse device common for all mice
    [    2.185810] ls_fetch_sysconfig_para: type err  device_used = -1064103068.
    [    2.193481] =========script_get_err============
    [    2.198518] ltr_init: ls_fetch_sysconfig_para err.
    [    2.204442] sunxi-rtc sunxi-rtc: rtc core: registered sunxi-rtc as rtc0
    [    2.211970] IR RC5(x) protocol handler initialized
    [    2.217393] sunxi tsc version 0.1
    [    2.221732] register_tsiomem: check_mem_region return: 0
    [    2.227655] register_tsiomem: devp->regsaddr: 0xf1c06000
    [    2.233727] sunxi cedar version 0.1
    [    2.237741] [cedar]: install start!!!
    [    2.242042] [cedar]: install end!!!
    [    2.245954] sunxi_wdt_init_module: sunxi WatchDog Timer Driver v1.0
    [    2.253124] sunxi_wdt_probe: devm_ioremap return wdt_reg 0xf1c20ca0, res->start 0x01c20ca0, res->end 0x01c20cbf
    [    2.264335] sunxi_wdt_probe: initialized (g_timeout=16s, g_nowayout=0)
    [    2.271816] wdt_enable, write reg 0xf1c20cb8 val 0x00000000
    [    2.278020] timeout_to_interv, line 167
    [    2.282303] interv_to_timeout, line 189
    [    2.286567] wdt_set_tmout, write 0x000000b0 to mode reg 0xf1c20cb8, actual timeout 16 sec
    [    2.296205] device-mapper: ioctl: 4.22.0-ioctl (2011-10-19) initialised: [[email protected]][55933]
    [    2.305688] Bluetooth: HCI UART driver ver 2.2
    [    2.310992] [cpu_freq] ERR:get cpu extremity frequency from sysconfig failed, use max_freq
    [    2.321637] [mmc]: SD/MMC/SDIO Host Controller Driver(v1.111 2015-4-13 15:24) Compiled in Jun  9 2015 at 14:44:34
    [    2.333102] [mmc]: get mmc0's sdc_power is null!
    [    2.338253] [mmc]: get mmc1's sdc_power is null!
    [    2.343403] [mmc]: get mmc1's 2xmode ok, val = 1
    [    2.348534] [mmc]: get mmc1's ddrmode ok, val = 1
    [    2.353810] [mmc]: get mmc2's sdc_power is null!
    [    2.358948] [mmc]: get mmc2's 2xmode ok, val = 1
    [    2.364103] [mmc]: get mmc2's ddrmode ok, val = 1
    [    2.369345] [mmc]: MMC host used card: 0x7, boot card: 0x4, io_card 2
    [    2.377662] [mmc]: sdc2 set ios: clk 0Hz bm OD pm OFF vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.380071] usb 4-1: new low-speed USB device number 2 using sunxi-ohci
    [    2.395925] [mmc]: sdc2 set ios: clk 0Hz bm PP pm UP vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.406043] [mmc]: sdc0 set ios: clk 0Hz bm OD pm OFF vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.407313] [mmc]: sdc2 power_supply is null
    [    2.420046] [mmc]: sdc2 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.434200] [mmc]: sdc1 set ios: clk 0Hz bm OD pm OFF vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.440854] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 52,  RTO !!
    [    2.441698] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 52,  RTO !!
    [    2.441732] [mmc]: sdc2 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.444239] [mmc]: sdc2 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.446164] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 8,  RTO !!
    [    2.446193] *******************Try sdio*******************
    [    2.447011] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 5,  RTO !!
    [    2.447849] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 5,  RTO !!
    [    2.448686] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 5,  RTO !!
    [    2.449521] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 5,  RTO !!
    [    2.449551] *******************Try sd *******************
    [    2.450371] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 55,  RTO !!
    [    2.451209] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 55,  RTO !!
    [    2.452046] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 55,  RTO !!
    [    2.452884] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 2 err, cmd 55,  RTO !!
    [    2.452912] *******************Try mmc*******************
    [    2.452925] [mmc]: sdc2 set ios: clk 400000Hz bm OD pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.453371] [mmc]: sdc2 set ios: clk 400000Hz bm OD pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.453493] [mmc]: sdc2 set ios: clk 400000Hz bm OD pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.453613] [mmc]: sdc2 set ios: clk 400000Hz bm OD pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.456113] [mmc]: sdc2 set ios: clk 400000Hz bm OD pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.491252] [mmc]: sdc2 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.503646] [mmc]: sdc2 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.504090] [mmc]: sdc2 set ios: clk 25000000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.504488] [mmc]: sdc2 set ios: clk 25000000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [    2.504605] [mmc]: sdc2 set ios: clk 25000000Hz bm PP pm ON vdd 3.3V width 1 timing MMC-HS(SDR20) dt B
    [    2.504691] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 1 timing MMC-HS(SDR20) dt B
    [    2.504812] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 1 timing MMC-HS(SDR20) dt B
    [    2.504928] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 8 timing MMC-HS(SDR20) dt B
    [    2.505660] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 8 timing MMC-HS(SDR20) dt B
    [    2.505770] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 8 timing UHS-DDR50 dt B
    [    2.505858] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 8 timing UHS-DDR50 dt B
    [    2.505966] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 8 timing UHS-DDR50 dt B
    [    2.506079] mmc0: new high speed DDR MMC card at address 0001
    [    2.506590] mmcblk0: mmc0:0001 NCard  7.21 GiB
    [    2.506853] mmcblk0boot0: mmc0:0001 NCard  partition 1 4.00 MiB
    [    2.507092] mmcblk0boot1: mmc0:0001 NCard  partition 2 4.00 MiB
    [    2.541035]  mmcblk0: p1 p2 p3 < p5 p6 p7 p8 p9 p10 p11 p12 p13 p14 p15 p16 >
    [    2.541087] mmcblk0: p1 size 10151936 extends beyond EOD, truncated
    [    2.544985] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 8 timing UHS-DDR50 dt B
    [    2.557771]  mmcblk0boot1: unknown partition table
    [    2.558437] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 8 timing UHS-DDR50 dt B
    [    2.570951]  mmcblk0boot0: unknown partition table
    [    2.571496] usbcore: registered new interface driver usbhid
    [    2.571506] usbhid: USB HID core driver
    [    2.829765] ashmem: initialized
    [    2.829832] *******************mmc init ok *******************
    [    2.830598] generic-usb 0003:1A2C:0C21.0001: input,hidraw0: USB HID v1.10 Keyboard [USB USB Keyboard] on usb-sunxi-ohci-1/input0
    [    2.852829] logger: created 256K log 'log_main'
    [    2.858007] logger: created 256K log 'log_events'
    [    2.863415] logger: created 256K log 'log_radio'
    [    2.868684] logger: created 256K log 'log_system'
    [    2.874289] sunxi_oops: heming add OOPS_INFO_ADDR = -20
    [    2.884399] asoc: sndcodec <-> sunxi-codec mapping ok
    [    2.894734] asoc: sndhdmi <-> sunxi-hdmiaudio.0 mapping ok
    [    2.902026] u32 classifier
    [    2.905036]     Actions configured
    [    2.908824] Netfilter messages via NETLINK v0.30.
    [    2.911039] generic-usb 0003:1A2C:0C21.0002: input,hidraw1: USB HID v1.10 Mouse [USB USB Keyboard] on usb-sunxi-ohci-1/input1
    [    2.926734] nf_conntrack version 0.5.0 (16033 buckets, 64132 max)
    [    2.934057] ctnetlink v0.93: registering with nfnetlink.
    [    2.940050] NF_TPROXY: Transparent proxy support initialized, version 4.1.0
    [    2.947804] NF_TPROXY: Copyright (c) 2006-2007 BalaBit IT Ltd.
    [    2.954805] xt_time: kernel timezone is -0000
    [    2.959828] IPv4 over IPv4 tunneling driver
    [    2.965062] gre: GRE over IPv4 demultiplexor driver
    [    2.970518] ip_gre: GRE over IPv4 tunneling driver
    [    2.976620] ip_tables: (C) 2000-2006 Netfilter Core Team
    [    2.982792] arp_tables: (C) 2002 David S. Miller
    [    2.988008] TCP: cubic registered
    [    2.991713] Initializing XFRM netlink socket
    [    2.996830] NET: Registered protocol family 10
    [    3.003073] Mobile IPv6
    [    3.005824] ip6_tables: (C) 2000-2006 Netfilter Core Team
    [    3.012068] IPv6 over IPv4 tunneling driver
    [    3.018025] NET: Registered protocol family 17
    [    3.023029] NET: Registered protocol family 15
    [    3.028163] Bluetooth: RFCOMM TTY layer initialized
    [    3.033801] Bluetooth: RFCOMM socket layer initialized
    [    3.039519] Bluetooth: RFCOMM ver 1.11
    [    3.043711] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
    [    3.049626] Bluetooth: BNEP filters: protocol multicast
    [    3.055455] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
    [    3.062205] L2TP core driver, V2.0
    [    3.066001] PPPoL2TP kernel driver, V2.0
    [    3.070386] L2TP IP encapsulation support (L2TPv3)
    [    3.075810] L2TP netlink interface
    [    3.079620] L2TP ethernet pseudowire support (L2TPv3)
    [    3.085795] VFP support v0.3: implementor 41 architecture 2 part 30 variant 7 rev 5
    [    3.094351] ThumbEE CPU extension supported.
    [    3.099112] Registering SWP/SWPB emulation handler
    [    3.104484] sunxi_bootup_extend_init: bootup extend state 1
    [    3.111753] cmdline,disp=404
    [    3.115079] [HDMI] power vcc-hdmi-18
    [    3.635527] [DISP] disp_hdmi_set_detect,line:404:hdmi0's mgr is NULL
    [    3.640769] [DISP] disp_device_attached,line:94:attched ok, mgr0<-->device0, type=4
    [    3.641695] cmdline,disp=404
    [    3.641847] [DISP] disp_init_tv,line:531:screen 0 do not support TV TYPE!
    [    3.641864] [DISP] bsp_disp_tv_register,line:938:'ptv is null
    [    3.641873] tv registered!!
    [    3.671369] sunxi-rtc sunxi-rtc: setting system clock to 1970-01-01 00:00:07 UTC (7)
    [    3.680028] ths_fetch_sysconfig_para: type err  device_used = 1.
    [    3.688300] CPU Budget:Register notifier
    [    3.692710] CPU Budget:register Success
    [    3.696982] sunxi-budget-cooling sunxi-budget-cooling: Cooling device registered: thermal-budget-0
    [    3.716113] [rf_pm]: Did not config module_power0 in sys_config
    [    3.722754] [rf_pm]: Did not config module_power1 in sys_config
    [    3.729340] [rf_pm]: Did not config module_power2 in sys_config
    [    3.735949] [rf_pm]: Did not config module_power3 in sys_config
    [    3.742551] [rf_pm]: mod has no chip_en gpio
    [    3.747295] [rf_pm]: regulator on.
    [    3.751103] [rf_pm]: set losc_out 32k out[wifi_pm]: wifi gpio init is OK !!
    [    3.759565] ALSA device list:
    [    3.762890]   #0: audiocodec
    [    3.766088]   #1: sndhdmi
    [    3.769570] Freeing init memory: 316K
    [    3.779985] init (1): /proc/1/oom_adj is deprecated, please use /proc/1/oom_score_adj instead.
    [    3.843445] init: open path: /dev/bus/usb/001/001
    [    4.001274] init: open path: /dev/bus/usb/002/001
    [    4.153876] init: open path: /dev/bus/usb/003/001
    [    4.431178] init: open path: /dev/bus/usb/004/001
    [    4.590279] init: open path: /dev/bus/usb/004/002
    [    4.768679] init: /dev/hw_random not found
    [    4.773630] init: defined DONT_SHOW_INITLOGO
    [    4.779029] init: /sys/class/switch/cvbs/state is exist
    [    4.784900] init: The device is not low memory 1002
    [    4.790620] init: init_disp=0x20b0404, type=2, id=1
    [    4.796284] init: disp=1,type=2,mode=11
    [    4.799322] [NAND]nand init start, nand0_used_flag is 0
    [    4.799365] [NAND]nand driver is disabled
    [    4.810970] [DISP] disp_device_attached_and_enable,line:159:attched ok, mgr1<-->device1, type=2, mode=11
    [    4.830826] disp_tv_set_hpd  state = 1
    [    4.882102] [mmc]: sdc2 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 8 timing UHS-DDR50 dt B
    [    5.422252] init: start e2fsck listening...
    [    5.550781] EXT4-fs (mmcblk0p7): mounted filesystem with ordered data mode. Opts: (null)
    [    5.696127] EXT4-fs (mmcblk0p16): recovery complete
    [    5.702488] EXT4-fs (mmcblk0p16): mounted filesystem with ordered data mode. Opts: nomblk_io_submit,errors=remount-ro
    [    5.780116] fs_mgr: Running /system/bin/e2fsck on /dev/block/by-name/cache
    [    5.833225] e2fsck->main: e2fsck start...
    [    5.837729] e2fsck->pipe_write: pipe_write type=1
    [    5.850721] e2fsck: e2fsck 1.41.14 (22-Dec-2010)
    [    5.855920] e2fsck: /dev/block/by-name/cache: clean, 16/40960 files, 5261/163840 blocks
    [    5.872533] EXT4-fs (mmcblk0p16): mounted filesystem with ordered data mode. Opts: nomblk_io_submit,barrier=1
    [    5.930864] EXT4-fs (mmcblk0p1): recovery complete
    [    5.936881] EXT4-fs (mmcblk0p1): mounted filesystem with ordered data mode. Opts: nomblk_io_submit,errors=remount-ro
    [    6.010088] fs_mgr: Running /system/bin/e2fsck on /dev/block/by-name/UDISK
    [    6.022765] e2fsck->main: e2fsck start...
    [    6.027266] e2fsck->pipe_write: pipe_write type=1
    [    6.042428] e2fsck: e2fsck 1.41.14 (22-Dec-2010)
    [    6.047599] e2fsck: /dev/block/by-name/UDISK: clean, 6360/315744 files, 224070/1260800 blocks
    [    6.064925] EXT4-fs (mmcblk0p1): mounted filesystem with ordered data mode. Opts: nomblk_io_submit,barrier=1,noauto_da_alloc
    [    6.183116] init: dont need format /dev/block/by-name/private
    [    6.426898] init: C_IN_START
    [    6.430170] init: path = /dev/block/by-name/cache
    [    6.435481] init: C_IN_START
    [    6.438721] init: path = /dev/block/by-name/UDISK
    [    6.593294] Failed to get mali parameter!
    [    6.598273] Init Mali gpu successfully
    [    6.603831] Mali: Mali device driver loaded
    [    6.790494] usbcore: registered new interface driver uvcvideo
    [    6.796909] USB Video Class driver (v1.1.1)
    [    6.824884] [SPDIF]sunxi-spdif cannot find any using configuration for controllers, return directly!
    [    6.876000] [SPDIF]sndspdif cannot find any using configuration for controllers, return directly!
    [    6.922005] [SPDIF] driver not init,just return.
    [    6.969347] gpio_pin_1(362) gpio_request
    [    6.973976] gpio_pin_2(15) gpio_request
    [    6.978463] gpio name is PL10, ret = 0
    [    6.983029] gpio name is PA15, ret = 0
    [    6.987396] gpio_init finish with uesd 1!
    [    7.153709] usbcore: registered new interface driver snd-usb-audio
    [    7.200893] init: /dev/hw_random not found
    [    7.212137] init: get_disp_policy: 2 for modify configs.
    [    7.217967] init: untracked pid 81 exited
    [    7.231650] Bluetooth: MSM Sleep Mode Driver Ver 1.2
    [    7.256409] usbcore: registered new interface driver asix
    [    7.270132] usbcore: registered new interface driver qf9700
    [    7.283818] usbcore: registered new interface driver MOSCHIP usb-ethernet driver
    [    7.300217] usbcore: registered new interface driver rtl8150
    [    7.317064] usbcore: registered new interface driver cdc_ether
    [    7.324310] [rfkill]: rfkill set power 1
    [    7.348122] healthd: Could not open /sys/class/power_supply
    [    7.351792] init: cannot find '/system/etc/install-recovery.sh', disabling 'flash_recovery'
    [    7.363879] healthd: No charger supplies found
    [    7.368850] healthd: BatteryStatusPath not found
    [    7.374084] healthd: BatteryHealthPath not found
    [    7.379260] healthd: BatteryPresentPath not found
    [    7.384595] healthd: BatteryCapacityPath not found
    [    7.389963] healthd: BatteryVoltagePath not found
    [    7.395278] healthd: BatteryTemperaturePath not found
    [    7.396693] multi-ir: add mapping table, identity 0x9f00, powerkey 0x57
    [    7.401594] multi-ir: add mapping table, identity 0xfb04, powerkey 0x1a
    [    7.415711] healthd: BatteryTechnologyPath not found
    [    7.443012] android_usb: already disabled
    [    7.447799] init: using deprecated syntax for specifying property 'sys.usb.config', use ${name} instead
    [    7.459181] init: using deprecated syntax for specifying property 'sys.usb.config', use ${name} instead
    [    7.461538] adb_open
    [    7.461556] mtp_bind_config
    [    7.461581] ep_matches, wrn: endpoint already claimed, ep(0xc093067c, 0xe619dc00, ep1in-bulk)
    [    7.461595] ep_matches, wrn: endpoint already claimed, ep(0xc093067c, 0xe619dc00, ep1in-bulk)
    [    7.461607] ep_matches, wrn: endpoint already claimed, ep(0xc09306c8, 0xe619dc00, ep1out-bulk)
    [    7.461617] gadget_is_softwinner_otg is not -int
    [    7.461624] gadget_is_softwinner_otg is not -int
    [    7.461676] adb_bind_config
    [    7.461687] ep_matches, wrn: endpoint already claimed, ep(0xc093067c, 0xe619dc00, ep1in-bulk)
    [    7.461699] ep_matches, wrn: endpoint already claimed, ep(0xc09306c8, 0xe619dc00, ep1out-bulk)
    [    7.461712] ep_matches, wrn: endpoint already claimed, ep(0xc093067c, 0xe619dc00, ep1in-bulk)
    [    7.461724] ep_matches, wrn: endpoint already claimed, ep(0xc09306c8, 0xe619dc00, ep1out-bulk)
    [    7.461735] ep_matches, wrn: endpoint already claimed, ep(0xc0930714, 0xe619bec0, ep2in-bulk)
    [   16.697760] warning: `zygote' uses 32-bit capabilities (legacy support in use)
    [   36.691553] healthd: battery l=0 v=0 t=0.0 h=1 st=1 chg=
    [   36.702896] request_suspend_state: wakeup (3->0) at 36702880727 (1970-01-02 00:00:19.927395842 UTC)
    [   36.862975] lowmemorykiller: lowmem_shrink: convert oom_adj to oom_score_adj:
    [   36.870987] lowmemorykiller: oom_adj 1 => oom_score_adj 58
    [   36.877097] lowmemorykiller: oom_adj 3 => oom_score_adj 176
    [   36.883317] lowmemorykiller: oom_adj 5 => oom_score_adj 294
    [   36.889515] lowmemorykiller: oom_adj 7 => oom_score_adj 411
    [   36.895742] lowmemorykiller: oom_adj 9 => oom_score_adj 529
    [   36.901966] lowmemorykiller: oom_adj 15 => oom_score_adj 1000
    [   37.338765] init: no such service 'dhcpcd_'
    [   37.360125] vmouse_input_dev_open
    [   37.460073] vmouse_input_dev_close
    [   37.560129] vmouse_input_dev_open
    [   42.570661] dhd_module_init: in
    [   42.574266] ======== bcm_wlan_set_plat_data ========
    [   42.579836] bcm_wlan_get_oob_irq enter.
    [   42.584284] gpio [202] map to virq [10] ok
    [   42.588852] host_oob_irq: 10
    [   42.592308] host_oob_irq_flags=4
    [   42.595902] dhd_wifi_platform_load: Enter
    [   42.600433] Power-up adapter 'DHD generic adapter'
    [   42.606073] wifi_platform_set_power = 1
    [   42.610380] ======== PULL WL_REG_ON HIGH! ========
    [   42.615716] [wifi_pm]: set wl_reg_on 1 !
    [   42.789036] acc_open
    [   42.791596] acc_release
    [   42.930150] wifi_platform_bus_enumerate device present 1
    [   42.936669] ======== Card detection to detect SDIO card! ========
    [   42.944211] [mmc]: sdc1 set ios: clk 0Hz bm PP pm UP vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [   42.946012] [DISP] disp_ioctl,line:1328:para err in disp_ioctl, cmd = 0x9,screen id = 2
    [   42.965968] [mmc]: sdc1 power_supply is null
    [   42.990104] [mmc]: sdc1 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [   43.022445] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 1 err, cmd 52,  RTO !!
    [   43.031488] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 1 err, cmd 52,  RTO !!
    [   43.039771] [mmc]: sdc1 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [   43.052675] [mmc]: sdc1 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [   43.064920] [mmc]: *** sunxi_mci_dump_errinfo(L824): smc 1 err, cmd 8,  RTO !!
    [   43.073115] *******************Try sdio*******************
    [   43.079610] [mmc]: sdc1 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing LEGACY(SDR12) dt B
    [   43.099818] mmc2: queuing unknown CIS tuple 0x80 (2 bytes)
    [   43.107930] mmc2: queuing unknown CIS tuple 0x80 (3 bytes)
    [   43.115851] mmc2: queuing unknown CIS tuple 0x80 (3 bytes)
    [   43.125036] mmc2: queuing unknown CIS tuple 0x80 (7 bytes)
    [   43.222107] [mmc]: sdc1 set ios: clk 400000Hz bm PP pm ON vdd 3.3V width 1 timing SD-HS(SDR25) dt B
    [   43.232463] [mmc]: sdc1 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 1 timing SD-HS(SDR25) dt B
    [   43.243026] [mmc]: sdc1 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 4 timing SD-HS(SDR25) dt B
    [   43.255870] mmc2: new high speed SDIO card at address 0001
    [   43.263261] *******************sdio init ok*******************
    [   43.279505] bcmsdh_register: register client driver
    [   43.285135] bcmsdh_sdmmc: bcmsdh_sdmmc_probe Enter
    [   43.290627] bcmsdh_sdmmc: bcmsdh_sdmmc_probe Enter
    [   43.295975] bus num (host idx)=2, slot num (rca)=1
    [   43.301344] found adapter info 'DHD generic adapter'
    [   43.307564] F1 signature read @0x18000000=0x1540a9a6
    [   43.316585] F1 signature OK, socitype:0x1 chip:0xa9a6 rev:0x0 pkg:0x4
    [   43.325134] DHD: dongle ram size is set to 524288(orig 524288) at 0x0
    [   43.332641] wifi_platform_get_mac_addr
    [   43.337013] dhd_custom_get_mac_address Enter
    [   43.341830] dhd_custom_get_mac_address wifi_mac=
    [   43.348765] wl_create_event_handler(): thread:wl_event_handler:22d started
    [   43.348783] tsk Enter, tsk = 0xe5b21410
    [   43.364254] p2p0: P2P Interface Registered
    [   43.369152] dhd_attach(): thread:dhd_watchdog_thread:231 started
    [   43.376088] dhd_attach(): thread:dhd_dpc:233 started
    [   43.381827] dhd_attach(): thread:dhd_rxf:234 started
    [   43.387369] dhd_deferred_work_init: work queue initialized
    [   43.393951] dhd_custom_get_mac_address Enter
    [   43.398743] dhd_custom_get_mac_address wifi_mac=
    [   43.403931] Dongle Host Driver, version 1.201.34.2 (r491657)
    [   43.403941] Compiled in drivers/net/wireless/bcmdhd on Jun  9 2015 at 14:45:07
    [   43.420084] Register interface [wlan0]  MAC: 00:90:4c:11:22:33
    [   43.420092]
    [   43.428261] dhd_prot_ioctl : bus is down. we have nothing to do
    [   43.434970] bcmsdh_oob_intr_unregister: Enter
    [   43.439864] bcmsdh_oob_intr_unregister: irq is not registered
    [   43.446316] dhd_txglom_enable: enable 0
    [   43.450599] dhd_bus_devreset:  WLAN OFF DONE
    [   43.455447] wifi_platform_set_power = 0
    [   43.459781] ======== PULL WL_REG_ON LOW! ========
    [   43.465162] [wifi_pm]: set wl_reg_on 0 !
    [   43.469868] dhd_module_init: Exit err=0
    [   44.800351] dhd_open: Enter e5822800
    [   44.804379]
    [   44.804390] Dongle Host Driver, version 1.201.34.2 (r491657)
    [   44.804396] Compiled in drivers/net/wireless/bcmdhd on Jun  9 2015 at 14:45:07
    [   44.825511] wl_android_wifi_on in 1
    [   44.829426] wl_android_wifi_on in 2: g_wifi_on=0
    [   44.834667] wifi_platform_set_power = 1
    [   44.838955] ======== PULL WL_REG_ON HIGH! ========
    [   44.844395] [wifi_pm]: set wl_reg_on 1 !
    [   45.150083] sdio_reset_comm():
    [   45.153514] [mmc]: sdc1 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 4 timing SD-HS(SDR25) dt B
    [   45.166119] [mmc]: sdc1 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 4 timing SD-HS(SDR25) dt B
    [   45.177747] [mmc]: sdc1 set ios: clk 150000Hz bm PP pm ON vdd 3.3V width 4 timing LEGACY(SDR12) dt B
    [   45.189134] [mmc]: sdc1 set ios: clk 150000Hz bm PP pm ON vdd 3.3V width 4 timing LEGACY(SDR12) dt B
    [   45.224260] mmc2: queuing unknown CIS tuple 0x80 (2 bytes)
    [   45.234397] mmc2: queuing unknown CIS tuple 0x80 (3 bytes)
    [   45.244747] mmc2: queuing unknown CIS tuple 0x80 (3 bytes)
    [   45.258375] mmc2: queuing unknown CIS tuple 0x80 (7 bytes)
    [   45.492684] [mmc]: sdc1 set ios: clk 150000Hz bm PP pm ON vdd 3.3V width 4 timing SD-HS(SDR25) dt B
    [   45.503052] [mmc]: sdc1 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 4 timing SD-HS(SDR25) dt B
    [   45.513602] [mmc]: sdc1 set ios: clk 50000000Hz bm PP pm ON vdd 3.3V width 4 timing SD-HS(SDR25) dt B
    [   45.524566]
    [   45.524572]
    [   45.524575] dhd_bus_devreset: == WLAN ON ==
    [   45.532712] F1 signature read @0x18000000=0x1540a9a6
    [   45.541217] F1 signature OK, socitype:0x1 chip:0xa9a6 rev:0x0 pkg:0x4
    [   45.549521] DHD: dongle ram size is set to 524288(orig 524288) at 0x0
    [   45.557232] dhd_conf_read_config: Ignore config file /system/vendor/modules/config.txt
    [   45.566081] dhd_conf_set_fw_name_by_chip: firmware_path=/system/vendor/modules/fw_bcm43438a0.bin
    [   45.575925] Final fw_path=/system/vendor/modules/fw_bcm43438a0.bin
    [   45.582852] Final nv_path=/system/vendor/modules/nvram_ap6212.txt
    [   45.589668] Final conf_path=/system/vendor/modules/config.txt
    [   45.800643] NVRAM version: AP6212_NVRAM_V1.0_20140603
    [   45.807383] dhdsdio_write_vars: Download, Upload and compare of NVRAM succeeded.
    [   45.874226] dhd_bus_init: enable 0x06, ready 0x06 (waited 0us)
    [   45.881324] bcmsdh_oob_intr_register: Enter
    [   45.886012] bcmsdh_oob_intr_register OOB irq=10 flags=4
    [   45.892121] bcmsdh_oob_intr_register: enable_irq_wake
    [   45.897773] bcmsdh_oob_intr_register: enable_irq_wake failed with -6
    [   45.905973] dhd_conf_set_band: Set band 0
    [   45.911055] wifi_platform_get_mac_addr
    [   45.915317] dhd_custom_get_mac_address Enter
    [   45.920206] dhd_custom_get_mac_address wifi_mac=
    [   45.929901] Firmware up: op_mode=0x0005, MAC=94:a1:a2:75:3f:96
    [   45.936571] dhd_conf_set_country: Set country CN, revision 0
    [   46.008067] Country code: CN (CN/0)
    [   46.012910] dhd_conf_set_roam: Set roam_off 1
    [   46.035290] Firmware version = wl0: Jun  6 2014 14:50:39 version 7.10.226.49 (r) FWID 01-8962686a
    [   46.045557]   Driver: 1.201.34.2 (r491657)
    [   46.045567]   Firmware: wl0: Jun  6 2014 14:50:39 version 7.10.226.49 (r) FWID 01-8962686a
    [   46.059637] dhd_txglom_enable: enable 0
    [   46.067455] dhd_wlfc_hostreorder_init(): successful bdcv2 tlv signaling, 64
    [   46.076604] wl_android_wifi_on: Success
    [   46.082417] p2p0: p2p_dev_addr=96:a1:a2:75:3f:96
    [   46.163172] dhd_open: Exit ret=0
    [   47.134208] EXT4-fs (mmcblk0p7): re-mounted. Opts: (null)
    [   47.214804] init: sys_prop: permission denied uid:1003  name:service.bootanim.exit
    [   47.553327] Connectting with xx:xx:xx:xx:xx:xx channel (1) ssid "xxxxxxx", len (15)
    [   47.553336]
    [   47.560949] wl_bss_connect_done succeeded with xx:xx:xx:xx:xx:xx
    [   47.710954] wl_bss_connect_done succeeded with xx:xx:xx:xx:xx:xx
    [   48.166545] dhd_pno_get_for_batch: Batching SCAN mode is not enabled
    [   48.174839] dhd_pno_stop_for_batch : PNO BATCH MODE is not enabled
    [   48.181815] NULL POINTER (_dhd_pno_clear_all_batch_results) : head->next is NULL
    [   48.190085] NULL POINTER (_dhd_pno_clear_all_batch_results) : head->next is NULL
    [   48.736040] qtaguid: iface_stat: stat_update() wlan0 not found
    [   49.507806] [ddrfreq] temperature=62 C, ddr freq up
    [   49.513789] CPU Budget:update CPU 0 cpufreq max to 1008000 min to 480000
    [   49.586812] [rfkill]: rfkill set power 1
    [   49.810781] [rfkill]: rfkill set power 0
    [   53.001304] CPU1: shutdown
    [   53.004356] [hotplug]: cpu(0) try to kill cpu(1)
    [   53.009549] [hotplug]: cpu1 is killed! .
    [   54.005892] EXT4-fs (mmcblk0p7): re-mounted. Opts: (null)
    [   54.262284] EXT4-fs (mmcblk0p7): re-mounted. Opts: (null)
    [   54.328715] EXT4-fs (mmcblk0p7): re-mounted. Opts: (null)
    [   56.001031] CPU1: Booted secondary processor
    [   57.001359] CPU3: shutdown
    [   57.004430] [hotplug]: cpu(0) try to kill cpu(3)
    [   57.009685] [hotplug]: cpu3 is killed! .
    [   57.214059] [ddrfreq] temperature=63 C, ddr freq up
    [   57.219713] CPU Budget:update CPU 0 cpufreq max to 1008000 min to 480000
    [   57.300070] p2p0: no IPv6 routers present
    [   59.500919] CPU3: Booted secondary processor
    [   62.001343] CPU2: shutdown
    [   62.004401] [hotplug]: cpu(1) try to kill cpu(2)
    [   62.009587] [hotplug]: cpu2 is killed! .
    [   64.501310] CPU1: shutdown
    [   64.504369] [hotplug]: cpu(3) try to kill cpu(1)
    [   64.509547] [hotplug]: cpu1 is killed! .
    [   66.500874] CPU1: Booted secondary processor
    [   67.347779] healthd: battery l=0 v=0 t=0.0 h=1 st=1 chg=
    [   68.001323] CPU1: shutdown
    [   68.004381] [hotplug]: cpu(3) try to kill cpu(1)
    [   68.009559] [hotplug]: cpu1 is killed! .
    [   71.000977] CPU1: Booted secondary processor
    [   72.001352] CPU3: shutdown
    [   72.004426] [hotplug]: cpu(0) try to kill cpu(3)
    [   72.009869] [hotplug]: cpu3 is killed! .
    
[/code]
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
