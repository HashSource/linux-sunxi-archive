# IRULU X47
IRULU X47  
---  
[![Device front.jpg][25268]][25269]  
Manufacturer |  [[1]][25270]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [[2]][25271]  
Specifications   
SoC |  [A33][25272] @ XGhz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  8GiB (actual) / 16GiB (advertised)   
Power |  DC 5V @ 2A, 4000mAh 3.7V Li-Ion battery (5200 mAh advertised)   
Features   
LCD |  800x1280 (7" X:Y)   
Touchscreen |  X-finger capacitive ([GSL1680][25273])   
Video |  None   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([RTL8723cs][25274])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2.0MP (1600x1200) rear   
Other |  Accelerometer ([Manufacturer device][25275]), GPS   
Headers |  None   
This page needs to be properly filled according to the [New Device Howto][25276] and the [New Device Page guide][25277].
A low-cost tablet with 1280x800 IPS display. There is some discrepancy in model numbers (X4, X7, X47) but X47 is what appears in Android. 
## Contents
  * [1 Identification][25278]
  * [2 Sunxi support][25279]
    * [2.1 Current status][25280]
    * [2.2 Images][25281]
    * [2.3 Manual build][25282]
      * [2.3.1 U-Boot][25283]
        * [2.3.1.1 Sunxi/Legacy U-Boot][25284]
        * [2.3.1.2 Mainline U-Boot][25285]
      * [2.3.2 Linux Kernel][25286]
        * [2.3.2.1 Sunxi/Legacy Kernel][25287]
        * [2.3.2.2 Mainline kernel][25288]
        * [2.3.2.3 Stock U-Boot and Android boot log][25289]
    * [2.4 FEL mode][25290]
    * [2.5 Device disassembly][25291]
    * [2.6 Locating the UART][25292]
  * [3 Tips, Tricks, Caveats][25293]
  * [4 Pictures][25294]
  * [5 Also known as][25295]
  * [6 See also][25296]
    * [6.1 Manufacturer images][25297]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Designed by iRULU in USA Made in China Model X7
[/code]
The PCB has the following silkscreened on it: 
[code] 
    V708_V1.1_0918
    MAINBOARD_V1.1
    PHT
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _X47_
  * Android version: _5.1.1_
  * Firmware version: _v3.3rc5_
  * Kernel version: _3.4.39_ pht-lzg@Ubuntu-lzg #61 Tue Apr 12 14:34:49 CST 2016
  * Build Number: _KVT49L.20160412_

# Sunxi support
## Current status
Work in progress. 
It is possible to boot mainline U-Boot and stock Debian Stretch R2 armhf kernel over UART using the [FEL/USBBoot][25298] technique. No devices are accessible, possibly except for the USB port. 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][25296]. If no sunxi based images are available, this section can be removed.
## Manual build
Not attempted. 
### U-Boot
#### Sunxi/Legacy U-Boot
Not attempted. 
#### Mainline U-Boot
U-Boot v2016.09 was used successfully with Sinlinx_SinA33_defconfig and microSD UART changes. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Not attempted. 
#### Mainline kernel
Use the _sun8i-a33-sinlinx-sina33.dtb_ device-tree binary with microSD UART changes. 
**Boot log (click Expand):**
[code] 
    [    0.000000] Booting Linux on physical CPU 0x0
    [    0.000000] Linux version 4.9.0-1-armmp ([[email protected]][25299]) (gcc version 6.3.0 20161229 (Debian 6.3.0-2) ) #1 SMP Debian 4.9.2-2 (2017-01-12)
    [    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c5387d
    [    0.000000] CPU: div instructions available: patching division code
    [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
    [    0.000000] OF: fdt:Machine model: Sinlinx SinA33
    [    0.000000] efi: Getting EFI parameters from FDT:
    [    0.000000] efi: UEFI not found.
    [    0.000000] cma: Reserved 16 MiB at 0x7f000000
    [    0.000000] Memory policy: Data cache writealloc
    [    0.000000] psci: probing for conduit method from DT.
    [    0.000000] psci: Using PSCI v0.1 Function IDs from DT
    [    0.000000] percpu: Embedded 14 pages/cpu @ef6b0000 s27724 r8192 d21428 u57344
    [    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 260416
    [    0.000000] Kernel command line: console=ttyS0,115200
    [    0.000000] PID hash table entries: 4096 (order: 2, 16384 bytes)
    [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
    [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
    [    0.000000] Memory: 979600K/1048576K available (7168K kernel code, 956K rwdata, 2212K rodata, 1024K init, 396K bss, 52592K reserved, 16384K cma-reserved, 245752K highmem)
    [    0.000000] Virtual kernel memory layout:
    [    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
    [    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
    [    0.000000]     vmalloc : 0xf0800000 - 0xff800000   ( 240 MB)
    [    0.000000]     lowmem  : 0xc0000000 - 0xf0000000   ( 768 MB)
    [    0.000000]     pkmap   : 0xbfe00000 - 0xc0000000   (   2 MB)
    [    0.000000]     modules : 0xbf000000 - 0xbfe00000   (  14 MB)
    [    0.000000]       .text : 0xc0008000 - 0xc0800000   (8160 kB)
    [    0.000000]       .init : 0xc0b00000 - 0xc0c00000   (1024 kB)
    [    0.000000]       .data : 0xc0c00000 - 0xc0cef27c   ( 957 kB)
    [    0.000000]        .bss : 0xc0cf1000 - 0xc0d54104   ( 397 kB)
    [    0.000000] Hierarchical RCU implementation.
    [    0.000000] 	Build-time adjustment of leaf fanout to 32.
    [    0.000000] 	RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
    [    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=32, nr_cpu_ids=4
    [    0.000000] NR_IRQS:16 nr_irqs:16 16
    [    0.000000] arm_arch_timer: Architected cp15 timer(s) running at 24.00MHz (phys).
    [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
    [    0.000006] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
    [    0.000019] Switching to timer-based delay loop, resolution 41ns
    [    0.001021] clocksource: timer: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635851949 ns
    [    0.002359] Console: colour dummy device 80x30
    [    0.002400] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=120000)
    [    0.002416] pid_max: default: 32768 minimum: 301
    [    0.002690] Security Framework initialized
    [    0.002704] Yama: disabled by default; enable with sysctl kernel.yama.*
    [    0.002742] AppArmor: AppArmor disabled by boot time parameter
    [    0.002833] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
    [    0.002845] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
    [    0.003968] CPU: Testing write buffer coherency: ok
    [    0.004021] ftrace: allocating 26610 entries in 79 pages
    [    0.059575] /cpus/cpu@0 missing clock-frequency property
    [    0.059609] /cpus/cpu@1 missing clock-frequency property
    [    0.059622] /cpus/cpu@2 missing clock-frequency property
    [    0.059637] /cpus/cpu@3 missing clock-frequency property
    [    0.059649] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
    [    0.059692] Setting up static identity map for 0x40100000 - 0x40100098
    [    0.063904] EFI services will not be available.
    [    0.065565] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
    [    0.066673] CPU2: thread -1, cpu 2, socket 0, mpidr 80000002
    [    0.067726] CPU3: thread -1, cpu 3, socket 0, mpidr 80000003
    [    0.067814] Brought up 4 CPUs
    [    0.067841] SMP: Total of 4 processors activated (192.00 BogoMIPS).
    [    0.067848] CPU: All CPU(s) started in HYP mode.
    [    0.067853] CPU: Virtualization extensions available.
    [    0.068831] devtmpfs: initialized
    [    0.074883] VFP support v0.3: implementor 41 architecture 2 part 30 variant 7 rev 5
    [    0.075258] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 9556302231375000 ns
    [    0.076042] pinctrl core: initialized pinctrl subsystem
    [    0.077681] NET: Registered protocol family 16
    [    0.079399] DMA: preallocated 256 KiB pool for atomic coherent allocations
    [    0.081425] No ATAGs?
    [    0.081460] hw-breakpoint: found 5 (+1 reserved) breakpoint and 4 watchpoint registers.
    [    0.081471] hw-breakpoint: maximum watchpoint size is 8 bytes.
    [    0.082122] Serial: AMBA PL011 UART driver
    [    0.114352] vgaarb: loaded
    [    0.115300] media: Linux media interface: v0.10
    [    0.115358] Linux video capture interface: v2.00
    [    0.115448] pps_core: LinuxPPS API ver. 1 registered
    [    0.115456] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <[[email protected]][25299]>
    [    0.115480] PTP clock support registered
    [    0.117059] clocksource: Switched to clocksource arch_sys_counter
    [    0.163645] VFS: Disk quotas dquot_6.6.0
    [    0.163755] VFS: Dquot-cache hash table entries: 1024 (order 0, 4096 bytes)
    [    0.176922] NET: Registered protocol family 2
    [    0.177890] TCP established hash table entries: 8192 (order: 3, 32768 bytes)
    [    0.177976] TCP bind hash table entries: 8192 (order: 4, 65536 bytes)
    [    0.178092] TCP: Hash tables configured (established 8192 bind 8192)
    [    0.178171] UDP hash table entries: 512 (order: 2, 16384 bytes)
    [    0.178233] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes)
    [    0.178561] NET: Registered protocol family 1
    [    0.179088] Unpacking initramfs...
    [    0.455925] Freeing initrd memory: 29604K (c8317000 - ca000000)
    [    0.458180] futex hash table entries: 1024 (order: 4, 65536 bytes)
    [    0.458416] audit: initializing netlink subsys (disabled)
    [    0.458536] audit: type=2000 audit(0.425:1): initialized
    [    0.459080] Initialise system trusted keyrings
    [    0.459614] workingset: timestamp_bits=14 max_order=18 bucket_order=4
    [    0.459831] zbud: loaded
    [    0.787136] Key type asymmetric registered
    [    0.787154] Asymmetric key parser 'x509' registered
    [    0.787246] bounce: pool size: 64 pages
    [    0.787363] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
    [    0.787540] io scheduler noop registered
    [    0.787549] io scheduler deadline registered
    [    0.787608] io scheduler cfq registered (default)
    [    0.787894] sunxi-rsb 1f03400.rsb: could not find pctldev for node /soc@01c00000/pinctrl@01f02c00/r_rsb, deferring probe
    [    0.789472] sun8i-a23-r-pinctrl 1f02c00.pinctrl: Reset controller missing
    [    0.793610] sun8i-a33-pinctrl 1c20800.pinctrl: initialized sunXi PIO driver
    [    0.797655] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
    [    0.799635] console [ttyS0] disabled
    [    0.819876] 1c28000.serial: ttyS0 at MMIO 0x1c28000 (irq = 32, base_baud = 1500000) is a U6_16550A
    [    1.469901] console [ttyS0] enabled
    [    1.474003] Serial: AMBA driver
    [    1.481234] libphy: Fixed MDIO Bus: probed
    [    1.486120] mousedev: PS/2 mouse device common for all mice
    [    1.493442] sun6i-rtc 1f00000.rtc: rtc core: registered rtc-sun6i as rtc0
    [    1.500255] sun6i-rtc 1f00000.rtc: RTC enabled
    [    1.506801] ledtrig-cpu: registered to indicate activity on CPUs
    [    1.513555] NET: Registered protocol family 10
    [    1.519107] mip6: Mobile IPv6
    [    1.522132] NET: Registered protocol family 17
    [    1.526582] mpls_gso: MPLS GSO support
    [    1.530402] ThumbEE CPU extension supported.
    [    1.534695] Registering SWP/SWPB emulation handler
    [    1.540339] registered taskstats version 1
    [    1.544470] Loading compiled-in X.509 certificates
    [    1.559808] alg: No test for pkcs1pad(rsa,sha256) (pkcs1pad(rsa-generic,sha256))
    [    1.569214] Loaded X.509 cert 'Debian Project: Ben Hutchings: 008a018dca80932630'
    [    1.576933] zswap: loaded using pool lzo/zbud
    [    1.585110] sunxi-rsb 1f03400.rsb: could not find pctldev for node /soc@01c00000/pinctrl@01f02c00/r_rsb, deferring probe
    [    1.599076] sun8i-a23-r-pinctrl 1f02c00.pinctrl: initialized sunXi PIO driver
    [    1.606612] sunxi-rsb 1f03400.rsb: RSB running at 3000000 Hz
    [    1.613055] sun6i-rtc 1f00000.rtc: setting system clock to 1970-01-01 00:05:35 UTC (335)
    [    1.621186] sr_init: No PMIC hook to init smartreflex
    [    1.626388] sr_init: platform driver register failed for SR
    [    1.632245] PM: Hibernation image not present or could not be loaded.
    [    1.632324] vcc3v0: disabling
    [    1.635294] vcc3v3: disabling
    [    1.638282] vcc5v0: disabling
    [    1.642772] Freeing unused kernel memory: 1024K (c0b00000 - c0c00000)
    [    1.700737] random: systemd-udevd: uninitialized urandom read (16 bytes read)
    [    1.707435] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.709468] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.709939] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.709468] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.709939] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.710400] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.710913] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.711322] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.711752] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.712385] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.712780] random: udevadm: uninitialized urandom read (16 bytes read)
    [    1.837588] usbcore: registered new interface driver usbfs
    [    1.843267] usbcore: registered new interface driver hub
    [    1.848822] usbcore: registered new device driver usb
    [    1.863187] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    [    1.873709] ehci-platform: EHCI generic platform driver
    [    1.876414] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
    [    1.880242] ohci-platform: OHCI generic platform driver
    [    1.880791] ohci-platform 1c1a400.usb: Generic Platform OHCI controller
    [    1.880836] ohci-platform 1c1a400.usb: new USB bus registered, assigned bus number 1
    [    1.905654] ohci-platform 1c1a400.usb: irq 26, io mem 0x01c1a400
    [    1.971380] usb usb1: New USB device found, idVendor=1d6b, idProduct=0001
    [    1.978222] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [    1.985461] usb usb1: Product: Generic Platform OHCI controller
    [    1.991391] usb usb1: Manufacturer: Linux 4.9.0-1-armmp ohci_hcd
    [    1.971380] usb usb1: New USB device found, idVendor=1d6b, idProduct=0001
    [    1.978222] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [    1.985461] usb usb1: Product: Generic Platform OHCI controller
    [    1.991391] usb usb1: Manufacturer: Linux 4.9.0-1-armmp ohci_hcd
    [    1.997406] usb usb1: SerialNumber: 1c1a400.usb
    [    2.004360] hub 1-0:1.0: USB hub found
    [    2.008213] hub 1-0:1.0: 1 port detected
    [    2.014940] ehci-platform 1c1a000.usb: EHCI Host Controller
    [    2.020696] ehci-platform 1c1a000.usb: new USB bus registered, assigned bus number 2
    [    2.028962] ehci-platform 1c1a000.usb: irq 25, io mem 0x01c1a000
    [    2.047098] ehci-platform 1c1a000.usb: USB 2.0 started, EHCI 1.00
    [    2.053511] usb usb2: New USB device found, idVendor=1d6b, idProduct=0002
    [    2.060322] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [    2.067552] usb usb2: Product: EHCI Host Controller
    [    2.072439] usb usb2: Manufacturer: Linux 4.9.0-1-armmp ehci_hcd
    [    2.078453] usb usb2: SerialNumber: 1c1a000.usb
    [    2.083891] hub 2-0:1.0: USB hub found
    [    2.087770] hub 2-0:1.0: 1 port detected
    
[/code]
#### Stock U-Boot and Android boot log
**Click Expand:**
[code] 
    HELLO! BOOT0 is starting!
    boot0 version : 4.0.0
    fel_flag = 0x00000000
    rtc[0] value = 0x00000000
    rtc[1] value = 0x00000000
    rtc[2] value = 0x00000000
    rtc[3] value = 0x00000000
    DRAM DRIVE INFO: V1.6
    DRAM Type =3 (2:DDR2,3:DDR3,6:LPDDR2,7:LPDDR3)
    
    sum=a115f59a
    src_sum=a115f59a
    Ready to disable icache.
    Jump to secend Boot.
    [      0.311]
    
    U-Boot 2011.09-rc1-00004-gfccb1ec-dirty (Oct 13 2016 - 18:16:02) Allwinner Technology 
    
    [      0.320]version: 1.1.0
    [      0.407]pmbus:   normal or secure os
    ready
    [      0.412]PMU: AXP221
    [      0.414]PMU: AXP22x found
    bat_vol=3187, ratio=100
    [      0.420]PMU: dcdc3 1200
    [      0.422]PMU: pll1 1008 Mhz,PLL6=600 Mhz
    AXI=336 Mhz,AHB=200 Mhz, APB1=100 Mhz 
    set power on vol to default
    dcdc1_vol = 3000
    dcdc2_vol = 1200
    dcdc3_vol = 1200
    dcdc4_vol = 0
    dcdc5_vol = 1650
    aldo2_vol = 2500
    aldo3_vol = 3000
    eldo1_vol = 1800
    find power_sply to end
    vbus exist
    vbus pc exist, limit to pc
    fel key old mode
    run key detect
    no key found
    no key input
    dram_para_set start
    dram_para_set end
    [      1.629]DRAM:  1 GiB
    relocation Offset is: 35b09000
    smcl's set manager is NULL
    <axp22, dc1sw>
    workmode = 0
    [      2.057]NAND: NAND_UbootInit
    NAND_UbootInit start
    NB1 : enter NAND_LogicInit
    uboot:nand version: 2 2d 20160718 1042 
    nand : get id_number_ctl fail, 1
    uboot:nand info: a714dead ffff4a42 318c 40704 5 
    nand : get sorting_flag fail, a
    nand : get CapacityLevel fail, 7fb9c075
    not burn nand partition table!
    NB1 : nftl num: 2 
     init nftl: 0 
    NB1 : NAND_LogicInit ok, result = 0x0 
    [      2.752]sunxi flash init ok
    sunxi secure storage is not supported
    [      2.759]usb burn from boot
    delay time 0
    [      2.830]usb prepare ok
    usb sof ok
    [      3.067]usb probe ok
    [      3.069]usb setup ok
    set address 0x6
    [      6.071]timer occur
    [      6.106]do_burn_from_boot usb : have no handshake
    In:    serial
    Out:   serial
    Err:   serial
    --------fastboot partitions--------
    -total partitions:13-
    -name-        -start-       -size-      
    bootloader  : 1000000       2000000     
    env         : 3000000       1000000     
    boot        : 4000000       1000000     
    system      : 5000000       80000000    
    misc        : 85000000      1000000     
    recovery    : 86000000      2000000     
    cache       : 88000000      30000000    
    metadata    : b8000000      1000000     
    private     : b9000000      1000000     
    frp         : ba000000      80000       
    empty       : ba080000      f80000      
    alog        : bb000000      5000000     
    UDISK       : c0000000      0           
    -----------------------------------
    base bootcmd=run setargs_nand boot_normal
    bootcmd set setargs_nand
    key 0
    recovery key high 255, low 3
    cant find fstbt value
    misc partition found
    to be run cmd=run setargs_nand boot_normal
    
    ** Unable to read "sn.txt" from sunxi_flash 8:0 **
    load file(sn.txt) error 
    serial is: XXXX
    mount part name bootloader
    cant open script.bin, maybe it is not exist
    WORK_MODE_BOOT
    board_status_probe
    screen_id =0, screen_width =800, screen_height =1280
    [     12.351]power trigger
    bat_exist=32
    sunxi_bmp_charger_display
    screen_id =0, screen_width =800, screen_height =1280
    [     12.366]Hit any key to stop autoboot:  0 
    read boot or recovery all
    [     12.872]sunxi flash read :offset 4000000, 13187431 bytes OK
    no signature
    [     12.882]ready to boot
    para err in disp_ioctl, cmd = 0xa,screen id = 1
    [     12.889][mmc]: MMC Device 2 not found
    [     12.893][mmc]:  mmc  not find,so not exit
    NAND_UbootExit
    NB1 : NAND_LogicExit
    nand release dma:0
    [     12.897]
    Starting kernel ...
    [    0.567351] WRN:L486(drivers/usb/sunxi_usb/hcd/hcd0/sunxi_hcd0.c):get no_suspend status failed
    
[/code]
## FEL mode
Push and hold Volume Up. Push Power and hold for about two seconds. Repeatedly push Volume Up. 
It is easier to do this with UART attached. 
## Device disassembly
{{Easily done with a [Plastic tool howto][25300] (or a sharp fingernail).}} 
## Locating the UART
[MicroSD Breakout adapter][25301] should be used for [UART howto][25302]. There are almost no test pads on the PCB. Since the built-in U-Boot uses microSD pins for UART, it is unlikely that additional UART pads exist. 
# Tips, Tricks, Caveats
Do not put sharp objects into the hole marked as Reset because it is actually a microphone. Android is extremely slow on this device. 
# Pictures
Take some pictures of your device, [ upload them][25303], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][25304]][25269]
  * [![Device back.jpg][25305]][25306]
  * [![Device buttons 1.jpg][25307]][25308]
  * [![Device buttons 2.jpg][25309]][25310]
  * [![Device board front.jpg][25311]][25312]
  * [![Device board back.jpg][25313]][25314]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
