# Teclast P50Ai
Teclast P50Ai  
---  
[![Teclast-P50Ai-front.png][54623]][54624]  
Manufacturer |  [Teclast][54625]  
Dimensions |  258 _mm_ x 170 _mm_ x 8.3 _mm_ , 540g   
Release Date |  2024   
Website |  [P50Ai Product Page][54626]  
Specifications   
SoC |  [A733][54627] @ 2.0Ghz   
DRAM |  6 GiB LPDDR5 @ Unknown MHz   
NAND |  128 GiB UFS   
Power |  DC 5V, 7000mAh 3.7V Li-Ion battery   
Features   
LCD |  1280x800@90Hz (10.92" 16:10)   
Touchscreen |  yes   
Video |  USB-C DisplayPort video out   
Audio |  3.5mm headphone plug, internal stereo speakers, internal microphone   
Network |  WiFi 6 ([AICSemi AIC8800][54628]), BT 5.4   
Storage |  µSD, eMMC   
USB |  1 x USB3.0 OTG via USB-C, 1 x USB host-only   
Camera |  5MP front, 13MP + 0.08MP rear   
The first device with the Allwinner A733 (Cortex-A76 Dual-Core, Cortex-A55 Hexa-Core, RISC-V E902 Single-Core CPU). Sells for around 80 USD. Surprisingly good look and feel (metal back) for that price class. 
## Contents
  * [1 Pictures][54629]
  * [2 Locating the UART][54630]
  * [3 Boot log (stock firmware)][54631]
  * [4 See also][54632]
  * [5 Manufacturer images][54633]

# Pictures
  * [![Teclast-P50Ai-back-cover-inside.jpg][54634]][54635]
  * [![Teclast-P50Ai-internal-cpu.jpg][54636]][54637]
  * [![Teclast-P50Ai-main-board-pmic.jpg][54638]][54639]
  * [![Teclast-P50Ai-ddr5-ic.jpg][54640]][54641]
  * [![Teclast-P50Ai-UFS.jpg][54642]][54643]
  * [![Teclast-P50Ai-pcb back.jpg][54644]][54645]

# Locating the UART
UART is exposed via the Micro SD card slot. A Micro SD breakout is required (or opening the tablet and soldering cables directly). 
More information can be found here: [https://linux-sunxi.org/MicroSD_Breakout][54646]
# Boot log (stock firmware)
The BSP outputs some boot information via UART0 pinmuxed on the PortF pins 2 & 4, which can be accessed via a microSD breakout board without opening the device. 
boot log from factory firmware 
[code] 
    [641]HELLO! SBOOT is starting!
    [644]sboot commit : {12e38aac}
    [650]PMU: AXP8191
    [652]pmu_chip_id = 14
    [654]set pll start
    [656]cpul clk 0xf8802700!
    [659]cpub clk 0xf8802700!
    [662]dsu clk 0xf8801e00!
    [665]set pll end
    [671]dram_para_total:0xf
    [674]vaild para:16  select dram para1
    [677]board init ok
    [679]rtc[3] value = 0xa301
    [682]rtc[7] value = 0x2
    [684]enable_jtag
    [686]Driver version 0.0.9 2024.11.20 10:19
    [705]Cal words efuse addr 0x60 value 0x966e0000, addr 0x64 value 0x4f23976e
    [754]Device  up at:[755][RX, TX]: gear=[4, 4], lane[2, 2], pwr[FAST MODE, FAST MODE], rate = 2
    [763]sc st 2
    [764]Read blk size 4096,capacity 31246335
    [768]DRAM BOOT DRIVE INFO: V0.596
    [773]DRAM_VCC set to 560 mv
    [775]DRAM CLK =1800 MHZ
    [777]DRAM Type =9 (8:LPDDR4,9:LPDDR5)
    [915]Training result is = 7
    [917]DRAM Pstate 1 training, frequency is 1200 Mhz
    [1091]Training result is = 7
    [1094]DRAM Pstate 2 training, frequency is 800 Mhz
    [1433]Training result is = 7
    [1436]DRAM Pstate 3 training, frequency is 400 Mhz
    [1534]Training result is = 7
    [1537]DRAM Pstate 0 training, frequency is 1800 Mhz
    [1545]Actual DRAM SIZE =6144 M
    [1548]DRAM SIZE =6144 MBytes, para1 = a10a, para2 = 18001001, dram_tpr13 = 10065
    [1558]DRAM simple test OK.
    [1560]dram size = 6144
    [1568]aw root ceritf rsa 2048
    [1571]OLD version: 0.0
    [1573]NEW version: 0.0
    [1576]don't have rotpk, skip check
    [1801]monitor entry=0x48000000
    [1804]uboot entry=0x4a000000
    [1806]optee entry=0x48600000
    [1809]opensbi entry=0x0
    [1812]no need rotpk flag
    [1814]sec_mem_map[0]: addr = 0x48000000, size = 0x100000
    [1819]sec_mem_map[1]: addr = 0x48600000, size = 0x100000
    [1825]run out of boot0
    NOTICE:  BL31: OP-TEE 64bit detected
    NOTICE:  BL31: U-BOOT 32bit detected
    NOTICE:  BL31: v2.5(debug):5fc237a6a
    NOTICE:  BL31: Built : 18:21:25, Feb 21 2025
    NOTICE:  BL31: No DTB found.
    NOTICE:  SEC mem [0]: addr = 0x48000000, size = 0x100000
    NOTICE:  SEC mem [1]: addr = 0x48600000, size = 0x100000
    NOTICE:  DRM mem [2]: addr = 0xb6a00000, size = 0x9600000
    M/TC: OP-TEE version: 18450130 (gcc version 9.2.1 20191025 (GNU Toolchain for the A-profile Architecture 9.2-2019.12 (arm-9.10))) #1 Sat Feb 22 07:09:25 UTC 2025 aarch64
    M/TC: OP-TEE 64bit
    ETC:0 0 plat_rng_init:460 prng seed by trng
    
    
    U-Boot 2018.07 (Mar 21 2025 - 19:34:32 +0800) Allwinner Technology
    
    [01.935]CPU:   Allwinner Family
    [01.938]Model: sun60iw2
    I2C:   ready
    [02.052]DRAM:  6 GiB
    [02.056]Relocation Offset is: 6c79c000, reloc addr is: b679c000
    [02.116]secure enable bit: 1
    [02.120]PMU: AXP8191
    [02.122]PMU: AXP8191 VER_A
    [02.127]BMU: AXP515
    [02.130][AXP8191] charge/reboot status:0x1
    [02.133][AXP515] charge/reboot status:0x62
    [02.148][AXP515] battery exist:1
    [02.163][AXP8191] onoff status: 0x50 = 0x0, 0x51 = 0x0
    [02.168][AXP8191] charge status: 0x4 = 0x0
    [02.171][AXP515] poweron irq: 0x4a:0x0, 0x4b:0x0
    [02.176][AXP515] on/off status 0x6:0x0
    [02.181]CPU=1014 MHz,PLL6=1200 Mhz,AHB=200 Mhz, APB1=24Mhz  MBus=600Mhz
    [02.187]gic: sec monitor mode
    [02.198]flash init start
    [02.200]workmode = 0,storage type = 8
    [ufs]:Driver version 0.0.23 2024.11.20 14:12
    [ufs]:Cal words 0x60:val 0x966e0000, 0x64:val 0x4f23976e
    [ufs]:[RX, TX]: gear=[4, 4], lane[2, 2], pwr[FAST MODE, FAST MODE], rate = 2
    [ufs]:qTotalRawDeviceCapacity 0x000000000EE64000, max_num_alloc_units 0x00007732
    [ufs]:qTotalRawDeviceCapacity 0x000000000EE64000, CapacityAdjFactor 0x00000001, bAllocationUnitSize 0x01, dSegmentSize 0x00002000, max_num_alloc_units 0x00007732, res_num_alloc_units 0
    x00000004
    [ufs]:dNumAllocUnits:0x000c0000
     [ufs]:bLogicalBlockSize:0
     [ufs]:bProvisioningType:3
     [ufs]:bdatareliability:1
     [ufs]:ufshcd_write_desc_param: param size is over buff len,only write buff_len
    [ufs]:__ufshcd_query_descriptor: opcode 0x02 for idn 1 failed, index 0, err = 250
    [ufs]:__ufshcd_query_descriptor: opcode 0x02 for idn 1 failed, index 0, err = 250
    [ufs]:__ufshcd_query_descriptor: opcode 0x02 for idn 1 failed, index 0, err = 250
    [ufs]:ufshcd_write_desc_param: Failed writing descriptor. desc_id 1, desc_index 0, param_offset 0, ret 250[ufs]:write config des:config logical unit
    [ufs]:sc st 2
    [ufs]:scsi status:Check conditon
    [ufs]:blk size 4096,capacity 31246336 block
    [02.361]sunxi flash init ok
    [02.388]Loading Environment from SUNXI_FLASH... erase secure storage failed
    OK
    [02.398][AXP8191] charge/reboot status:0x0
    [02.416]Warn: can't find connect driver
    success get enable-num=0x2
    success get lcd_id=0x1b38
    success get bias-slave-addr=0x3e
    i2c_get_bus_num is busnum = 1
    i2c_get_bus_num is not SUNXI_VIR_I2C1!
    num=[0] reg=0xda val=0x99
    num=[1] reg=0xdb val=0x51
    [fixup_lcdid_cmdline]:lcd_id_val=1b38
    dsi0@5506000:  detailed mode clock 119166 kHz, flags[0]
        H: 0800 0840 0844 0884
        V: 1280 2203 2207 2247
    bus_format: 0
    secure storage read hdcpkey fail
    [03.289]usb burn from boot
    delay time 0
    [03.295]usb prepare ok
    [03.534]usb sof ok
    [03.536]usb probe ok
    [03.538]usb setup ok
    set address 0x9
    set address 0x9 ok
    [03.944]do_burn_from_boot usb : have no handshake
    skip update boot_param
    List file under ULI/factory
    Error: FAT sector size mismatch (fs=4096, dev=512)
    [03.960]update part info
    [03.965]battery temp is 264
    [03.968]update bootcmd
    [04.004]change working_fdt 0xb274be30 to 0xb271be30
    ret 0
    [04.038]update dts
    Hit any key to stop autoboot:  0
    val is 379
    Android's image name: arm64
    ERROR: reserving fdt memory region failed (addr=b6a00000 size=9600000)
    ERROR: reserving fdt memory region failed (addr=b27e1000 size=3e8000)
    [04.378]Starting kernel ...
    
    [04.380]total: 4380 ms
    
    [ufs]:sync cache
    NOTICE:  [SCP] :wait arisc ready....
    NOTICE:  [SCP] :arisc version: [-00661-gb9f31a5b5a8-dirty]
    NOTICE:  [SCP] :arisc startup ready
    NOTICE:  [SCP] :arisc startup notify message feedback
    NOTICE:  [SCP] :sunxi-arisc driver is starting
    NOTICE:  BL3-1: Next image address = 0x40080000
    NOTICE:  BL3-1: Next image spsr = 0x3c9
    [    0.000000][    T0] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
    [    0.000000][    T0] Linux version 6.6.30-android15-8-gcdcd52e8915f-ab12246136-4k (kleaf@build-host) (Android (11368308, +pgo, +bolt, +lto, +mlgo, based on r510928) clang version 18.
    0.0 (https://android.googlesource.com/toolchain/llvm-project 477610d4d0d988e69dbc3fae4fe86bff3f07f2b5), LLD 18.0.0) #1 SMP PREEMPT Mon Aug 19 16:01:06 UTC 2024
    [    0.000000][    T0] KASLR disabled due to lack of seed
    [    0.000000][    T0] random: crng init done
    [    0.000000][    T0] Machine model: sun60iw2
    [    0.000000][    T0] stackdepot: disabled
    [    0.000000][    T0] earlycon: uart8250 at MMIO32 0x0000000002500000 (options '')
    [    0.000000][    T0] printk: bootconsole [uart8250] enabled
    [    0.279185][  T124] AW BSP version: UNKNOWN, 2025-03-21 19:34:38
    AW_Keymint_v3_CreateEntryPoint
    Gatekeeper_TA_CreateEntryPoint
    
[/code]
# See also
A sister tablet called [Teclast T60Ai][54647] exists, with similar specs, but with a 12" display, UFS 3.1 (vs 3.0 on this one), and bigger (8000mAh vs 7000) battery . 
# Manufacturer images
[Support/Software Download][54648]
Enter Product ID "G5B1".
