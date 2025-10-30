# Bookeen Notea
Bookeen Notea  
---  
[![Notea front.jpg][10273]][10274]  
Manufacturer |  [Bookeen][10275]  
Dimensions |  190 _mm_ x 230 _mm_ x 8 _mm_  
Release Date |  June 2023 (last version)   
Website |  [Product Page][10276]  
Specifications   
SoC |  [B300][10277] @ 1.8Ghz   
DRAM |  2GiB LPDDR4 @ 720MHz   
NAND |  32GB   
Power |  DC 5V @ 2A, 4000mAh 3.7V Li-Ion battery   
Features   
LCD |  157.25x209.66 (10.3" 4:3)   
Touchscreen |  Capacitive + Wacom EMR   
Audio |  internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n   
USB |  USB2.0 OTG Type C   
Other |  Accelerometer, Bluetooth BLE & BT 4.2   
Headers |  UART   
The Bookeen Notéa is a e-ink tablet based on the [B300][10277] chip. It is sold by Bookeen, a french e-book company. The tablet is manufactured by Bigme. It shares the case, screen and other components with the PineNote. 
## Contents
  * [1 Identification][10278]
  * [2 Sunxi support][10279]
    * [2.1 Current status][10280]
      * [2.1.1 U-Boot][10281]
      * [2.1.2 Linux Kernel][10282]
  * [3 Adding a serial port (**voids warranty**)][10283]
    * [3.1 Device disassembly][10284]
    * [3.2 Locating the UART][10285]
    * [3.3 Serial output][10286]
  * [4 Pictures][10287]
  * [5 FEL mode][10288]
    * [5.1 By sending '2' to UART][10289]
    * [5.2 Using fastboot oem efex][10290]
  * [6 See also][10291]

# Identification
On the back of the device, the following is printed: 
[code] 
    CYBN10F
[/code]
The PCB has the following silkscreened on it: 
[code] 
    XRZ_E126-MAIN-V1.1
    2020-12-07
[/code]
In android, under Settings->About Tablet, you will find: 
[code] 
    Android version
    8.1.0
    
    Processor type
    QuadCore-B300
    
    Firmware version
    B300-o-mr1-v1.0rc2
    
    Kernel version
    4.9.5 (gcc version 5.3.1 20160412 (Linaro GCC 5.3-2016.05) )
    chichengzao@ubuntu #10
    Thu Jun 15 10:53:49 CST 2023
    
    Build number
    OPM1.171019.026.20230928-094810 test-keys
[/code]
`sunxi-fel version` output: 
[code] 
    Warning: no 'soc_sram_info' data for your SoC (id=1755)
    AWUSBFEX soc=00001755(unknown) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
    
[/code]
# Sunxi support
## Current status
No support of the [B300][10277] SoC. 
### U-Boot
The U-Boot is not distributed. Bookeen does not have the sources and Bigme does not provide them. 
### Linux Kernel
The Linux Kernel is not distributed. Bookeen does not have the sources and Bigme does not provide them. 
# Adding a serial port (**voids warranty**)
[![][10292]][10293]
[][10294]
Notea UART pads
You can attach a serial port to the Allwinner B300 by soldering the UART pads on the PCB, see [UART howto][10295]. 
## Device disassembly
Gently unclip the black plastic case around the screen with [plastic tools][10296]. Unclip the USB port last. Be careful with the button, it is not firmly attached. 
Remove the aluminium covers on the PCB. 
## Locating the UART
[![][10297]][10298]
[][10299]
Notea soldered UART
The UART pads are labelled G, R, T, V for GND, RX, TX and VCC. Use 3.3V and do not connect VCC. 
## Serial output
[code] 
    [115]HELLO! BOOT0 is starting!
    [118]boot0 commit : 000a620ce443178c1a35bdeb5deeb23d3180f34f
    
    [135]rsb_send_initseq: rsb clk 400Khz -> 3Mhz
    [140]PMU: AXP858
    [141][pmu]: name dcdc4, min_vol 500mv, max_vol 1540, cfg_reg 0x00000016, cfg_mask 0x0000007f            step0_val 10, split1_val 1220, step1_val 20, ctrl_reg_addr 0x00000015, ctrl_bit_ofs 4
    [159][pmu]: name dcdc2, min_vol 500mv, max_vol 1540, cfg_reg 0x00000014, cfg_mask 0x0000007f            step0_val 10, split1_val 1220, step1_val 20, ctrl_reg_addr 0x00000010, ctrl_bit_ofs 1
    [177]set pll start
    [187]rtc[0] value = 0x00000000
    [190]rtc[1] value = 0x00000000
    [193]rtc[2] value = 0x00000000
    [196]rtc[3] value = 0x0000a102
    [199]rtc[4] value = 0x00000000
    [202]rtc[5] value = 0x00000000
    [205]key pressed value=0x00000016
    [209]key pressed value=0x00000016
    [252]time out
    [253]DRAM BOOT DRIVE INFO: V1.14
    [256]chip id check OK
    [259][pmu]: name dcdc5, min_vol 800mv, max_vol 1840, cfg_reg 0x00000017, cfg_mask 0x0000007f            step0_val 10, split1_val 1120, step1_val 20, ctrl_reg_addr 0x00000010, ctrl_bit_ofs 4
    [276]DRAM_VCC set to 1100 mv
    [279]DRAM CLK =720 MHZ
    [281]DRAM Type =8 (3:DDR3,4:DDR4,7:LPDDR3,8:LPDDR4)
    [320]Training result is = 00000007
    [325]Actual DRAM SIZE =2048 M
    [328]DRAM SIZE =2048 M,para1 = 0000310a,para2 = 08000000
    [341]DRAM simple test OK.
    [344]dram size =2048
    [348]card no is 2
    [350]sdcard 2 line count 8
    [352][mmc]: mmc driver ver 2018-04-08 14:50
    [356][mmc]: mmc 2 bias 00000004
    [365][mmc]: ***Try MMC card 2***
    [381][mmc]: MMC 5.1
    [383][mmc]: HSDDR52/DDR50 8 bit
    [386][mmc]: 50000000 Hz
    [388][mmc]: 29856 MB
    [390][mmc]: ***SD/MMC 2 init OK!!!***
    [490]Loading boot-pkg Succeed(index=0).
    [494]Entry_name        = scp
    [504]Entry_name        = optee
    [510]Entry_name        = u-boot
    [526]Entry_name        = soc-cfg
    [530]Entry_name        = dtb
    [534]Entry_name        = logo
    [537]Entry_name        = shutdowncharge
    [541]Entry_name        = androidcharge
    [545]Ready to disable icache.
    [548]0xffffffff 0xffffffff
    [551]0xff1affff 0xffffffff
    [553]0xff0f17ff 0xffffffff
    [556]0x1616ffff 0xffff2414
    [559]0x141dffff 0xffffffff
    [561]0x1717ffff 0xffffffff
    [564]Jump to secend Boot.
    MESSAGE: [0x0] TEE-CORE: arisc version: []
    
    
    U-Boot 2014.07 (May 25 2023 - 20:27:00) Allwinner Technology
    
    uboot commit : 0c4b5570dc773d5d2b76265612b726d7d2b3f8a3
    
    secure enable bit: 0
    normal mode: with secure monitor
    [0.595]pmbus:   ready
    [0.595]PMU: AXP858
    [0.595]PMU: AXP858 found
    [0.595]pmu_type = 49
    [0.596]BMU: AW1867
    [0.598]pmu_on_ctl:9
    [0.601]Charge current:1050 ma
    [0.602]Input current:1050 ma
    set pc_bias(1) bias:1800
    [0.608]PMU: cpux 1008 Mhz,AXI=504 Mhz
    [0.611]PLL6=600 Mhz,AHB1=200 Mhz, APB1=100Mhz MBus=400Mhz
    DRAM:  2 GiB
    Relocation Offset is: 75ddf000
    [0.655]initr_malloc
    gic: sec monitor mode
    [0.739]initr_multi_core
    PowerBus = 2( 2:vBus 3:acBus other: not exist), bat_vol=4012, safe_vol=3600
    boot up: bat_vol=4012, safe_vol=3600, charger=2
    [0.739]power on cpu1
    [cpu1]PowerBus = 2( 2:vBus 3:acBus other: not exist)
    [cpu1]Battery Voltage=4012, safe_vol=3600, Ratio=83
    [0.743]poweron cause 0
    [cpu1]STATE_NORMAL_BOOT
    [cpu1]drv_disp_init
    [0.749]power on cpu2
    workmode = 0,storage type = 2
    [cpu1]init_clocks: finish init_clocks.
    [0.753]MMC:      2
    SUNXI SD/MMC: 2
    [cpu1]EINK: lcd_x=276, lcd_y=1421, dclk=35
    [cpu1]pwm_request:pwm number = 1
    [cpu1]request pwm success, spwm0:pwm16:0x7020c00.
    [0.771]bits=5,data_len=16,width=1872,height=1404
    [0.775]lsl=11,lbl=8,ldl=234,lel=23
    [0.778]fsl=1,fbl=4,fdl=1404,fel=12
    [0.781]gdck_sta=10,lgonl=215
    Normal
    [0.786]Item0 (Map) magic is bad
    [0.787]the secure storage item0 copy0 is bad
    [0.792]Item0 (Map) magic is bad
    [0.794]the secure storage map is empty
    [0.798]no item name key_burned_flag in the map
    [0.802]sunxi storage read fail
    [0.805]sunxi secure storage has no flag
    [0.808]usb burn from boot
    delay time 0
    [cpu1]reading vcom.bin
    [0.815]usb prepare ok
    [cpu1]5 bytes read in 4 ms ([cpu1]1000 Bytes/s)
    [cpu1]drv_disp_init finish
    [0.824][cpu1]fetch script data boot_disp.output_full fail
    [0.828][cpu1]
    BMP file is to large,scn_w=276,scn_h=1421,bmp_w=380,bmp_h=328
    [1.117]overtime
    [1.117]do_burn_from_boot usb : no usb exist
    [1.122]no item name device_unlock in the map
    [1.122]sunxi storage read fail
    [1.122]no item name fastboot_status_flag in the map
    [1.122]sunxi storage read fail
    sunxi secure storage has no flag
    --------fastboot partitions--------
    -total partitions:16-
    -name-        -start-       -size-
    UDISK       : c1000000      87bfbc00
    bootloader  : 1000000       2000000
    env         : 3000000       1000000
    boot        : 4000000       2000000
    system      : 6000000       60000000
    vendor      : 66000000      f000000
    misc        : 75000000      1000000
    recovery    : 76000000      2000000
    cache       : 78000000      40000000
    metadata    : b8000000      1000000
    private     : b9000000      1000000
    frp         : ba000000      80000
    empty       : ba080000      f80000
    dto         : bb000000      1000000
    media_data  : bc000000      1000000
    device      : bd000000      4000000
    -----------------------------------
    time out
    key not det ota mode
    [4.238]Item0 (Map) magic is bad
    [4.238]the secure storage item0 copy0 is bad
    [4.239]Item0 (Map) magic is bad
    [4.239]the secure storage map is empty
    [4.239]no item name snum in the map
    [4.239]sunxi storage read fail
    reading sn.bin
    ** Unable to read file sn.bin **
    load file(sn.bin) error
    reading wavefile\bootlogo.bmp
    2629366 bytes read in 20 ms (125.4 MiB/s)
    bmp_buffer_change2Gray: sync cache
    waveform_path === default.bin
    reading default.bin
    8084496 bytes read in 51 ms (151.2 MiB/s)
    read waveform file from  default.bin   succeed
    [4.342]wavefile info: 320_R388_AF7311_ED103TC2C5_VB3300-KCD_TC.awf 2021.10.28.9:23:44:
    [4.342]eink_enable: init waveform ok
    [4.949]usb_net_init
    [4.949]run_main_loop
    Hit any key to stop autoboot:  0
    [5.063]Kernel load addr 0x40008000 size 15964 KiB
    [5.063]Kernel command line: selinux=1 androidboot.selinux=enforce buildvariant=user
    [5.063]RAM disk load addr 0x42000000 size 1158 KiB
    android.hardware = sun8iw15p1
    [5.105]
    Starting kernel ...
    
    [    0.000000] Booting Linux on physical CPU 0x0
    [    0.000000] Linux version 4.9.56 (chichengzao@ubuntu) (gcc version 5.3.1 20160412 (Linaro GCC 5.3-2016.05) ) #10 SMP PREEMPT Thu Jun 15 10:53:49 CST 2023
    [    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c5387d
    [    0.000000] CPU: div instructions available: patching division code
    [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
    [    0.000000] OF: fdt:Machine model: sun8iw15
    [    0.000000] bootconsole [earlycon0] enabled
[/code]
# Pictures
  * [![Notea front.jpg][10300]][10274]
  * [![Notea back UART.jpg][10301]][10302]
  * [![Notea Power Button.jpg][10303]][10304]
  * [![Notea USB C.jpg][10305]][10306]

# FEL mode
There are two known methods to trigger the FEL mode. 
## By sending '2' to UART
With UART active on `/dev/ttyS1`: 
  * Make sure baudrate is correct: `stty -F /dev/ttyS1 115200`
  * Spam `2` character on UART: `while [ true ]; do echo -n 2 > /dev/ttyS1; sleep 0.005; done`
  * Reboot the tablet

The tablet should reboot in FEL mode: 
[code] 
    [100]HELLO! BOOT0 is starting!
    [103]boot0 commit : 000a620ce443178c1a35bdeb5deeb23d3180f34f
    
    [109]key press : 2
    [111]rsb_send_initseq: rsb clk 400Khz -> 3Mhz
    [116]PMU: AXP858
    [117][pmu]: name dcdc4, min_vol 500mv, max_vol 1540, cfg_reg 0x00000016, cfg_mask 0x0000007f            step0_val 10, split1_val 1220, step1_val 20, ctrl_reg_addr 0x00000015, ctrl_bit_ofs 4
    [135][pmu]: name dcdc2, min_vol 500mv, max_vol 1540, cfg_reg 0x00000014, cfg_mask 0x0000007f            step0_val 10, split1_val 1220, step1_val 20, ctrl_reg_addr 0x00000010, ctrl_bit_ofs 1
    [153]set pll start
    [163]rtc[0] value = 0x00000000
    [166]rtc[1] value = 0x00000000
    [169]rtc[2] value = 0x00000000
    [172]rtc[3] value = 0x0000a102
    [175]rtc[4] value = 0x00000000
    [178]rtc[5] value = 0x00000000
    [181]detected user input 2
    [184]reset pll
[/code]
## Using `fastboot oem efex`
  * Connect the tablet to your computer
  * Install an app on the tablet to open the AOSP Parameters
  * Go to `system settings > about`
  * Tap multiple times the `build version` until you're in developper mode
  * Open developper settings
  * Change `USB mode` to `PTP`
  * Enable the `USB debugging`
  * Use `adb` on your computer (you'll need to trust your computer on the tablet)
  * `adb devices` will show you if you're properly connected
  * Use `adb reboot bootloader`, the tablet will freeze and reboot to the bootloader so you will only see the *Notéa* logo, `fastboot devices` will say: 
[code]Android Fastboot         Android Fastboot
[/code]
  * Use `fastboot oem efex`
  * Force rebooting the tablet, by holding the power button

[code] 
    [240.847]SUNXI_USB_FASTBOOT_SETUP
    [240.847]fastboot command = oem efex
    [240.847]oem operations
    set next system status
    drv_disp_exit
    sunxi_board_close_source
    �[110]HELLO! BOOT0 is starting!
    [113]boot0 commit : 000a620ce443178c1a35bdeb5deeb23d3180f34f
    
    [131]rsb_send_initseq: rsb clk 400Khz -> 3Mhz
    [135]PMU: AXP858
    [137][pmu]: name dcdc4, min_vol 500mv, max_vol 1540, cfg_reg 0x00000016, cfg_mask 0x0000007f         step0_val 10, split1_val 1220, step1_val 20, ctrl_reg_addr 0x00000015, ctrl_bit_ofs 4
    [155][pmu]: name dcdc2, min_vol 500mv, max_vol 1540, cfg_reg 0x00000014, cfg_mask 0x0000007f         step0_val 10, split1_val 1220, step1_val 20, ctrl_reg_addr 0x00000010, ctrl_bit_ofs 1
    [173]set pll start
    [183]rtc[0] value = 0x00000000
    [186]rtc[1] value = 0x00000000
    [189]rtc[2] value = 0x5aa5a55a
    [192]rtc[3] value = 0x0000b00f
    [195]rtc[4] value = 0x00000000
    [198]rtc[5] value = 0x00000000
    [201]eraly jump fel
    [203]reset pll
[/code]
`adb shell` is '_not_ root, the user is curiously named `virgo_perf1`. 
# See also
Notes: 
  * <https://github.com/Florianclume/hacking_bookeen_notea>

Other Allwinner B300 devices: 
  * Nook Glowlight 4
  * Tolino Vision 6
  * Tolino Shine 4
  * Tolino Epos 3
  * Xiaomi / Moaan InkPalm 5
