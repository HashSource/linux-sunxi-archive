# Teclast P85T
Teclast P85T  
---  
[![Teclast p85t front.jpg][54743]][54744]  
Manufacturer |  [Teclast][54745]  
Dimensions |  201.7 _mm_ x 122.4 _mm_ x 9.1 _mm_ , 340g   
Release Date |  2023   
Website |  [P85T Product Page][54746]  
Specifications   
SoC |  [A523][54747] @ 1.8Ghz   
DRAM |  4GiB LPDDR3 @ 792MHz   
NAND |  64 GiB eMMC   
Power |  DC 5V, 5000mAh 3.7V Li-Ion battery   
Features   
LCD |  IPS panel, 1280x800 (8" 16:10)   
Touchscreen |  yes   
Video |  none   
Audio |  3.5mm headphone plug, internal stereo speakers, internal microphone   
Network |  Dual band WiFi 6 ([Manufacturer device][54748]), BT 5.2   
Storage |  µSD, eMMC   
USB |  1 x USB2.0 OTG via USB-C   
Camera |  0.3MP front, 2.0MP rear   
One of the first devices with the Allwinner A523 (Cortex-A55 Octa-Core CPU). Should sell for around 80 USD. Surprisingly good look and feel (metal back) for that price class. 
## Contents
  * [1 Identification][54749]
  * [2 Sunxi support][54750]
    * [2.1 Current status][54751]
    * [2.2 Images][54752]
    * [2.3 BSP][54753]
    * [2.4 Manual build][54754]
      * [2.4.1 Mainline U-Boot][54755]
      * [2.4.2 Mainline Linux kernel][54756]
  * [3 Tips, Tricks, Caveats][54757]
    * [3.1 FEL mode][54758]
    * [3.2 Enter FEL Mode via SD card][54759]
    * [3.3 Secure boot][54760]
    * [3.4 xfel version][54761]
    * [3.5 xfel extra efuse dump][54762]
    * [3.6 BSP Boot log][54763]
  * [4 Adding a serial port (**voids warranty**)][54764]
    * [4.1 Device disassembly][54765]
    * [4.2 Locating the UART][54766]
  * [5 Pictures][54767]
  * [6 Also known as][54768]
  * [7 See also][54769]
    * [7.1 Manufacturer images][54770]

# Identification
On the back of the device, the following is printed: 
[code] 
    Teclast
    P85T
[/code]
The PCB has the following silkscreened on it: 
[/code]
[code] 
In android, under Settings->About Tablet, you will find: 
  * Model: _P85T_ROW_
  * CPU Model: _A523([[email protected]][54771][[email protected]][54771])_
  * Build Number: _V1.04_20230907_

# Sunxi support
## Current status
Not supported yet, but own code can be executed, and U-Boot/TF-A/Linux port is underway. 
## Images
Teclast provides official (PhoenixSuite) images, go to their [Support/Software Download][54772] page. The _Product ID Number_ you need for the download can be found in one of the photos below. 
## BSP
There are generic A523 BSP tarballs floating around, but nothing has been published yet. TinaLinux 5.4 BSP repos at GitHub contain some sun55iw3 code, although apparently from an earlier stage of development. 
## Manual build
You can build things for yourself by following our [ Manual build howto][54773] and by choosing from the configurations available below. 
### Mainline U-Boot
Not yet supported. 
### Mainline Linux kernel
Not yet supported. 
# Tips, Tricks, Caveats
## FEL mode
The hole between the volume and power switch allows access to a reset switch, not to a FEL button. To enter FEL mode, _dd_ a [TOC0][54774] version of fel-sdboot on a microSD card and restart the tablet with that. Any normal USB-C<->USB-A cable should do. 
Please note that while this method brings you into FEL mode, this is running in non-secure SVC, so accessing the BootROM, secure devices (like the GIC) and secure registers (to switch to AA64) is not possible. Previous SoCs could be tricked back into secure state by issuing an _smc_ call, but although this returns, the device is still in non-secure state. A [MBROM][54775] disassembly suggests that exactly an SMC call, with r0 being anything other than 0x830000f? should work, but somehow it doesn't. 
## Enter FEL Mode via SD card
Build fel-sdboot.bin (requires arm-none-eabi-gcc) 
[code] 
    git clone https://github.com/linux-sunxi/sunxi-tools.git
    cd sunxi-tools
    make fel-sdboot.bin
    cd ..
    
[/code]
requires uboot-tools and openssl 
[code] 
    openssl genrsa -out root_key.pem
    mkimage -A arm -T sunxi_toc0 -a 0x20060 -d sunxi-tools/fel-sdboot.bin output.toc0
    
[/code]
flash 
[code] 
    sudo dd if=output.toc0 of=/dev/sdX bs=1024 seek=8
    
[/code]
## Secure boot
The device has the secure fuse burnt, and the BSP Android is pretty nailed down. Fortunately the ROTPK hash is not burnt into the fuses, so any TOC0 image (as for instance created by [mkimage][54776]) can be used to execute code. This allows full access to the CPU, so AA64 code can be run in EL3 this way. 
## xfel version
[code] 
    alex@ryzen-fast ~/d/a/xfel (master)> ./xfel version
    AWUSBFEX ID=0x00189000(A523/A527/MR527/T527) dflag=0x44 dlength=0x08 scratchpad=0x00061500
    
[/code]
## xfel extra efuse dump
[code] 
    alex@ryzen-fast ~/d/a/xfel (master)> ./xfel extra efuse dump
    chipid:(0x0000 128-bits)
        02c05200 91c04824 75744c18 38931ed1 
    brom-config:(0x0010 32-bits)
        00000000 
    aldo-fix:(0x0014 1-bits)
    thermal-sensor:(0x0030 64-bits)
        01000000 00000000 
    tf-zone:(0x0028 128-bits)
        0d290d35 0d590cd2 01000000 00000000 
    oem-program:(0x003c 160-bits)
        08e18f10 052b808a f38fb900 00000048 00000000 
    write-protect:(0x0080 32-bits)
        00000000 
    read-protect:(0x0084 32-bits)
        00000000 
    lcjs:(0x0088 32-bits)
        00000000 
    attr:(0x0090 32-bits)
        00000000 
    huk:(0x0094 192-bits)
        00000000 00000000 00000000 00000000 00000000 00000000 
    reserved1:(0x00ac 64-bits)
        00000000 00000000 
    rotpk:(0x00b4 256-bits)
        00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 
    ssk:(0x00d4 128-bits)
        00000000 00000000 00000000 00000000 
    rssk:(0x00f4 256-bits)
        00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 
    sn:(0x00b0 192-bits)
        00000000 00000000 00000000 00000000 00000000 00000000 
    nv1:(0x0124 32-bits)
        00000000 
    nv2:(0x0128 32-bits)
        00000000 
    hdcp-hash:(0x0114 128-bits)
        00000000 00000000 00000000 00000000 
    backup-key:(0x0164 192-bits)
        00000000 00000000 00000000 00000000 00000000 00000000 
    backup-key2:(0x01a4 72-bits)
        00000000 00000000 
    
    
[/code]
## BSP Boot log
The BSP outputs some boot information via UART0 pinmuxed on the PortF pins 2 & 4, which can be accessed via a microSD breakout board without opening the device. 
boot log from factory firmware 
[code] 
    [140]HELLO! SBOOT is starting!
    [143]sboot commit : 0510558b5b
    [147]periph0 has been enabled
    [150]set pll end
    [151]PL gpio voltage : 3.3V
    [155]PMU: AXP2202
    [159]PMU: AXP1530
    [162]power mode:0, sys_vol:900
    [169]dram_para_total:0x20
    [172]vaild para:16  select dram para6
    [175]sunxi_adb400_process
    [178]board init ok 
    [180]rtc[3] value = 0xa202 
    [183]rtc[7] value = 0x2
    [205]enable_jtag
    [207][mmc]: mmc driver ver 2023-03-24 16:23
    [217][mmc]: Wrong media type 0x0, but host sdc2, try mmc first
    [222][mmc]: ***Try MMC card 2***
    [247][mmc]: RMCA OK!
    [249][mmc]: bias 17fb
    [251][mmc]: mmc 2 bias 17fb
    [257][mmc]: MMC 5.1
    [258][mmc]: HSSDR52/SDR25 8 bit
    [261][mmc]: 50000000 Hz
    [264][mmc]: 59648 MB
    [266][mmc]: ***SD/MMC 2 init OK!!!***
    [271]DRAM BOOT DRIVE INFO: V0.6581
    [275]DRAM_VCC set to 1200 mv
    [277]DRAM CLK =792 MHZ
    [279]DRAM Type =7 (3:DDR3,4:DDR4,6:LPDDR2,7:LPDDR3,8:LPDDR4)
    [287]DRAM SIZE =4096 MBytes, para1 = 30fa, para2 = 10007000, tpr13 = 6421
    [296]DRAM simple test OK.
    [298]dram size =4096
    [300]nsi init 2023-2-23
    [401]read toc1 from emmc 32800 sector
    [404]OLD version: 0.0
    [407]NEW version: 0.0
    [410]don't have rotpk, skip check
    [421]load rotpk hash
    [521]load vbmeta_a-key hash
    [523]load vbmeta_a hash
    [526]load vbmeta_b-key hash
    [528]load vbmeta_b hash
    [531]monitor entry=0x48000000
    [533]uboot entry=0x4a000000
    [536]optee entry=0x48600000
    [539]opensbi entry=0x0
    [541]no need rotpk flag
    [543]tunning data addr:0x4a0003e8
    [547]run out of boot0
    NOTICE:  BL31: v2.5(debug):5ddcbd3c7
    NOTICE:  BL31: Built : 15:36:49, Jun 12 2023
    NOTICE:  BL31: No DTB found.
    nsi init ok 2022-11-08
    M/TC: OP-TEE version: 3dcc1a5a (gcc version 5.3.1 20160412 (Linaro GCC 5.3-2016.05)) #1 Fri Jul  7 07:01:54 UTC 2023 arm
    E/TC:0 0 switch crypto engine to mbedtls
    
    
    U-Boot 2018.07 (Sep 07 2023 - 17:30:25 +0800) Allwinner Technology
    
    [00.618]CPU:   Allwinner Family
    [00.621]Model: sun55iw3
    I2C:   ready
    [00.644]DRAM:  4 GiB
    [00.649]Relocation Offset is: 6fa9b000
    [00.700]secure enable bit: 1
    [00.703]smc_tee_inform_fdt failed with: ffff000a
    [00.708]PMU: AXP2202
    [00.710]BMU: AXP2202
    [00.712][AXP2202] comm status : 0x0 = 0x38, 0x1 = 0xb3
    [00.717][AXP2202] onoff status: 0x20 = 0x0, 0x21 = 0x0
    [00.722][AXP2202] reboot/charge status: 0xf0 = 0x1
    AXP2202_IIN_LIM:38
    AXP2202_IIN_LIM:38
    AXP2202_IIN_LIM:38
    [00.734][axp][err]:
    b12_mode: 0
    AXP2202_IIN_LIM:38
    bias_name:pc_bias        bias_vol:1800
    [00.746]battery_check pass:radio:100, vol:4384
    [00.752]PMU: AXP1530
    [00.754]CPU=1296 MHz,PLL6=600 Mhz,AHB=200 Mhz, APB1=100Mhz  MBus=396Mhz
    [00.760]gic: sec monitor mode
    sunxi flash map init
    SPI ALL:   ready
    [00.767]flash init start
    [00.769]workmode = 0,storage type = 2
    [00.772][mmc]: mmc driver ver uboot2018:2023-03-24 16:28:00
    [00.778][mmc]: SUNXI SDMMC Controller Version:0x50500
    [00.804][mmc]: Best spd md: 4-HS400, freq: 4-150000000, Bus width: 8
    [00.809]sunxi flash init ok
    [00.812]drv_disp_init
    [00.818]handle_num : 13
    erase secure storage failed
    [00.874]sunxi_secure_storage_exit err: secure storage has not been inited
    ** Unable to read file display_param.cfg **
    lvds_clk_index = 0, disp = 0
    fdt get node offset faill: /soc/lcd0_1
    fdt get node offset faill: /soc/lcd0_2
    fdt get node offset faill: /soc/lcd0_3
    fdt get node offset faill: /soc/lcd0_4
    fdt get node offset faill: /soc/lcd0_5
    fdt get node offset faill: /soc/lcd0_6
    request pwm success, pwm0:pwm0:0x2000c00.
    lvds_clk_index = 1, disp = 2
    [00.950][DEBUG] primary_key: lcd0,okay,ret=2
    [00.954][DEBUG] primary_key: lcd1,okay,ret=2
    [00.959]lcd->hwdev_index: 1
    [00.963]lcd->hwdev_index: 1
    [00.966]lcd->hwdev_index: 1
    [00.969]lcd->hwdev_index: 1
    [00.973]lcd->hwdev_index: 1
    [00.976]lcd->hwdev_index: 1
    fdt get node offset faill: lcd4
    [00.982][DEBUG] primary_key: lcd4,okay,ret=0
    [00.986]skip lcd4
    [01.024]boot_hdmi20: [info] hdmi_init start
    [01.028]handle_num : 4
    [01.039]boot_hdmi20: [info] hdmi use inno phy!
    [01.043]boot_hdmi20: [info] hdmi_init finish
    [EDP_INFO]: edp0 probe start!
    g_edp_info[sel].irq = 176
    FDT ERROR:fdt_get_regulator_name:get property handle vdd-edp-supply error:FDT_ERR_INTERNAL
    power_name:<NULL> parse fail!
    [EDP_INFO]: vdd_regulator:<NULL>
    FDT ERROR:fdt_get_regulator_name:get property handle vcc-edp-supply error:FDT_ERR_INTERNAL
    power_name:<NULL> parse fail!
    [EDP_INFO]: vcc_regulator:<NULL>
    [EDP_INFO]: edp0 probe end!
    [01.084]drv_disp_init finish
    [01.103]Loading Environment from SUNXI_FLASH... OK
    [01.110]boot_gui_init:start
    [01.112]set disp.dev2_output_type fail. using defval=0
    [01.137]boot_hdmi20: [info] delay 20ms and re-get hpd state: 0.
    [01.162]boot_hdmi20: [info] delay 20ms and re-get hpd state: 0.
    [01.188]boot_hdmi20: [info] delay 20ms and re-get hpd state: 0.
    [01.213]boot_hdmi20: [info] delay 20ms and re-get hpd state: 0.
    [01.239]boot_hdmi20: [info] delay 20ms and re-get hpd state: 0.
    [01.245]set disp.dev_num fail. using defval=1
    disp_devices_open start: 0 end: 1 dev_num: 1 actual_dev_num: 2
    [01.255]===Lion LCD_open_flow===
    clk_set_rate: <NULL> has NULL parent
    [01.270]===Lion 0000 lcd power on===
    [01.496][LCD_panel_try_switch]: JLT080QI26184P31_21D18C g_switch_panel= 0,to_update_disp_num=1,to_update_index=0
    [lcd_readid0]:num=1,entries=7,id=0x93,0x65,0x4
    [01.610][fixup_lcdid_cmdline]:lcd_id_val=1108
    [01.614][LCD_panel_try_switch]: JLT080QI26184P31_21D18C lcm_id_tmp= 6
    pwm_request: err:this pwm has been requested!
    [01.678]===Lion LCD_open_flow===
    [01.690]===Lion 0000 lcd power on===
    [01.916][LCD_panel_try_switch]: JLT080QI26184P31_21D18 g_switch_panel= 1,to_update_disp_num=1,to_update_index=6
    [01.959][LCD_panel_init]: JLT080QI26184P31_21D18C
    [02.125]set disp.fb0_rot_used fail. using defval=0
    [02.129]set disp.fb0_rot_degree fail. using defval=0
    [02.138]set disp.fb1_rot_use[02.141]<===Lion===>0000 LCD_bl_open
    [02.200]LCD open finish
    d fail. using defval=0
    [02.204]set disp.fb1_rot_degree fail. using defval=0
    [02.209]boot_gui_init:finish
    [02.213]bmp_name=bootlogo.bmp size 3072054
    fb_save_para: fb_id(1) not open
    secure storage read hdcpkey fail
    [02.257]secure storage read hdcpkey fail with:-1
    [02.261]usb burn from boot
    delay time 0
    weak:otg_phy_config
    [02.271]usb prepare ok
    [02.546]usb sof ok
    [02.547]usb probe ok
    [02.549]usb setup ok
    set address 0x49
    set address 0x49 ok
    [02.956]do_burn_from_boot usb : have no handshake
    skip update boot_param
    List file under ULI/factory
    ** Unrecognized filesystem type **
    [02.970]update part info
    [02.992]get_bat_id_by_gpio value=1
    [02.995][fixup_batid_cmdline]:bat_id=0
    [02.999]bat_id=0,bat_cap_temp=5000
    [03.002][fixup_batcap_cmdline]:bat_cap=5000
    [03.006]battery temp is 188
    [03.025]update bootcmd
    [03.028]change working_fdt 0xb5a4ae50 to 0xb5a1ae50
    [03.033][mmc]: can't find node "mmc2" try sunxi-mmc
    disable nand error: FDT_ERR_BADPATH
    [03.043]The storage not support sample function
    fb_save_para: fb_id(1) not open
    ** Unable to read file display_param.cfg **
    [03.144]update dts
    Hit any key to stop autoboot:  0
    pubkey vbmeta_a valid
    CACHE: Misaligned operation at range [4fffffe0, 52c49020]
    ramdisk use init boot
    Android's image name: arm64
    [03.771]Starting kernel ...
    
    [03.774][mmc]: mmc exit start
    [03.791][mmc]: mmc 2 exit ok
    NOTICE:  [SCP] :wait arisc ready....
    NOTICE:  [SCP] :arisc version: [2.1V33-T2g-0a28fd3d0d-5fytri]
    NOTICE:  [SCP] :arisc startup ready
    NOTICE:  [SCP] :arisc startup notify message feedback
    NOTICE:  [SCP] :sunxi-arisc driver is starting
    BL3-1: Next image address = 0x40080000
    BL3-1: Next image spsr = 0x3c5
    [    0.000000][    T0] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
    [    0.000000][    T0] Linux version 5.15.94-android13-8-00002-g381b12479791-ab10457683 (build-user@build-host) (Android (8508608, based on r450784e) clang version 14.0.7 (https://android.googlesource.com/toolchain/llvm-project 4c603efb0cca074e9238af8b4106c30add4418f6), LLD 14.0.7) #1 SMP PREEMPT Fri Jul 7 16:27:54 UTC 2023
    [    0.000000][    T0] Machine model: sun55iw3
    [    0.000000][    T0] Stack Depot is disabled
    [    0.000000][    T0] KVM is not available. Ignoring kvm-arm.mode
    [    0.000000][    T0] earlycon: uart8250 at MMIO32 0x0000000002500000 (options '')
    [    0.000000][    T0] printk: bootconsole [uart8250] enabled
    AW_Keymint_v2_CreateEntryPoint
    Gatekeeper_TA_CreateEntryPoint
    
[/code]
# Adding a serial port (**voids warranty**)
The shiny and slick metal case begs to not be opened ;-) 
The BSP Android outputs some debug information over the PortF UART, which can be accessed via a microSD breakout board. 
[![][54777]][54778]
[][54779]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][54780]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][54781].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][54780].
# Pictures
  * [![Teclast p85t front.jpg][54782]][54744]
  * [![Teclast p85t back.jpg][54783]][54784]
  * [![Teclast p85t side.jpg][54785]][54786]
  * [![Teclast p85t top.jpg][54787]][54788]
  * [![Teclast p85t label.jpg][54789]][54790]

# Also known as
No known rebadged devices. 
# See also
A sister tablet called [Teclast P26T][54791] exists, with similar specs, but a 10" display, 128GB flash, and better cameras. 
## Manufacturer images
[Support/Software Download][54772]
Enter Product ID from one of the photos above.
