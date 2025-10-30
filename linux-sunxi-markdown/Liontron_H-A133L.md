# Liontron H-A133L
Liontron H-A133L  
---  
[![Liontron h a133l.jpg][32655]][32656]  
Manufacturer |  [Liontron][32657]  
Dimensions |  100 _mm_ x 80 _mm_ x 7 _mm_  
Release Date |  2023(?)   
Website |  [Device Product Page][32658]  
Specifications   
SoC |  [A133][32659] @ 1.6Ghz   
DRAM |  1-4GiB LPDDR4   
NAND |  8-128 GiB eMMC   
Power |  DC 9V-15V   
Features   
Video |  LVDS/MIPI-DSI (H-A133L), parallel RGB LCD (H-A133R), NO HDMI   
Audio |  3.5mm headphone plug, MIC and line-out on header   
Network |  WiFi 4 & BT 4.2 ([XR829][32660]), Fast Ethernet   
Storage |  µSD, eMMC   
USB |  1xUSB2.0 Type-A Host, 1xUSB2.0 Type-A (OTG), 3xUSB2.0 on headers   
Headers |  JST: power in, speakers, 3 USB2.0, backlight, LVDS, MIPI-DSI, 2 UART, I2C, LED, 5 GPIO, RTC, power/reset, microphone, Line-Out, PoE, 12V LED   
Industrial A133 development board. Breaks out peripherals including serial, I2C, SPI on JST connectors, but also offers standard USB 2.0 and 100M Ethernet connectors. Different versions of the board ship with different video interfaces: LVDS on 2mm pin headers, MIPI-DSI FPC, or 40/50pin RGB FPC connectors. Ships with Android. 
## Contents
  * [1 Identification][32661]
  * [2 Sunxi support][32662]
    * [2.1 Current status][32663]
    * [2.2 Manual build][32664]
      * [2.2.1 Mainline U-Boot][32665]
      * [2.2.2 Mainline Linux Kernel][32666]
  * [3 Tips, Tricks, Caveats][32667]
    * [3.1 FEL mode][32668]
    * [3.2 BSP boot log][32669]
  * [4 Accessing the serial port][32670]
  * [5 Pictures][32671]

# Identification
Stickers indicate the board configuration, and on the underside the silkscreen shows the model: 
[code] 
    MODEL: H-A133L 
    REV: 3.0
    DATE: 2023-10-10
[/code]
# Sunxi support
## Current status
Basic headless operation supported in mainline. 
## Manual build
You can build things for yourself by following our [ Manual build howto][32672] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the **liontron-h-a133l_defconfig** build target. Available since v2025.10-rc1. 
### Mainline Linux Kernel
Use the **sun50i-a133-liontron-h-a133l.dtb** device-tree binary from a mainline kernel, available since v6.16. Kernels starting with v6.12 should work when fed with a DTB from later kernel versions. 
Ethernet support was added to the DT in v6.17-rc1, but would work with older kernels already. 
# Tips, Tricks, Caveats
## FEL mode
The FEL button triggers [ FEL mode][32673]. 
## BSP boot log
The Android version installed on the eMMC boots a BSP based Linux kernel. The firmware (boot0, TF-A, U-Boot) messages are shown on UART0, but the kernel does not output anything. 
BSP boot log (no kernel messages) 
[code] 
    [137]HELLO! BOOT0 is starting!
    [140]BOOT0 commit : 83e3c82
    [143]set pll start
    [145]periph0 has been enabled
    [148]set pll end
    [150][pmu]: bus read error
    [153]PMU: AXP803
    [172]vaild para:1  select dram para0
    [176]board init ok
    [198]DRAM BOOT DRIVE INFO: V0.61
    [201]the chip id is 0x1400
    [204]the chip id is 0x1400
    [207]the chip id is 0x1400
    [209]the chip id is 0x1400
    [212]the chip id is 0x1400
    [215]chip id check OK
    [224]DRAM_VCC set to 1100 mv
    [227]DRAM CLK =792 MHZ
    [229]DRAM Type =8 (3:DDR3,4:DDR4,7:LPDDR3,8:LPDDR4)
    [240]DRAM SIZE =1024 MBytes, para1 = 30ea, para2 = 4001000, tpr13 = 7521
    [252]DRAM simple test OK.
    [254]dram size =1024
    [256]chipid = 54401400
    [258]nsi init ok 2020-4-7
    [262]card no is 2
    [264]sdcard 2 line count 8
    [266][mmc]: mmc driver ver 2020-05-25 09:40-202007019516
    [277][mmc]: Wrong media type 0x0
    [281][mmc]: ***Try SD card 2***
    [285][mmc]: mmc 2 cmd 8 timeout, err 100
    [289][mmc]: mmc 2 cmd 8 err 100
    [292][mmc]: mmc 2 send if cond failed
    [296][mmc]: mmc 2 cmd 55 timeout, err 100
    [300][mmc]: mmc 2 cmd 55 err 100
    [303][mmc]: mmc 2 send app cmd failed
    [307][mmc]: ***Try MMC card 2***
    [332][mmc]: RMCA OK!
    [334][mmc]: bias 4
    [336][mmc]: mmc 2 bias 4
    [339][mmc]: MMC 5.1
    [341][mmc]: HSSDR52/SDR25 8 bit
    [344][mmc]: 50000000 Hz
    [346][mmc]: 7456 MB
    [348][mmc]: ***SD/MMC 2 init OK!!!***
    [441]Loading boot-pkg Succeed(index=0).
    [445]Entry_name        = u-boot
    [456]Entry_name        = monitor
    [459]Entry_name        = scp
    [468]set arisc reset to de-assert state
    [472]Entry_name        = dtb
    [476]tunning data addr:0x4a0003e8
    [479]Jump to second Boot.
    NOTICE:  BL3-1: v1.0(debug):e138ea9
    NOTICE:  BL3-1: Built : 09:21:33, 2020-11-18
    NOTICE:  BL3-1 commit: 8
    NOTICE:  cpuidle init version V2.0
    ERROR:   Error initializing runtime service tspd_fast
    NOTICE:  BL3-1: Preparing for EL3 exit to normal world
    NOTICE:  BL3-1: Next image address = 0x4a000000
    ?OTICE:  BL3-1: Next image spsr = 0x1d3
    
    U-Boot 2018.05-g4c06572 (Apr 30 2024 - 17:41:55 +0800) Allwinner Technology
    
    [00.563]CPU:   Allwinner Family
    [00.566]Model: sun50iw10
    I2C:   [I2C-DBG] sunxi_i2c_init,line:600:    i2c1 info:5c(slaveaddr),200000(speed)
    ready
    [00.826]DRAM:  1 GiB
    [00.829]Relocation Offset is: 35e69000
    [00.879]secure enable bit: 0
    [00.883][ARISC ERROR] :get [allwinner,sunxi-hwspinlock] device node error
    CACHE: Misaligned operation at range [7ffa6d40, 7ffa7058]
    [SCP] :sunxi-arisc driver begin startup 2
    [SCP] :0x1
    [SCP] :arisc version: []
    [SCP] :arisc startup ready
    [SCP] :arisc startup notify message feedback
    [SCP] :send hard sync feedback message: 0x900200
    [SCP] :sunxi-arisc driver v1.10 is starting
    [I2C-DBG] sunxi_i2c_init,line:600:    i2c6 info:34(slaveaddr),200000(speed)
    [00.926]PMU: AXP803
    [02.928]PMU: AXP803
    FDT ERROR:fdt_get_regulator_name:get property handle twi-for-pmu-supply error:FDT_ERR_INTERNAL
    bias_name:pc_bias	 bias_vol:1800
    [04.981]CPU=1008 MHz,PLL6=600 Mhz,AHB=200 Mhz, APB1=100Mhz  MBus=400Mhz
    [04.987]flash init start
    [04.989]workmode = 0,storage type = 2
    [04.992][mmc]: mmc driver ver uboot2018:2020-5-25 9:26:00-2021-09-17 14:45:00
    [05.000][mmc]: get sdc_type fail and use default host:tm4.
    [05.012][mmc]: SUNXI SDMMC Controller Version:0x50300
    [05.037][mmc]: Best spd md: 4-HS400, freq: 3-100000000, Bus width: 8
    [05.043]sunxi flash init ok
    [05.046]drv_disp_init
    ** Unable to read file display_param.cfg **
    Load config file display_param.cfg failed
    request pwm success, pwm0:pwm0:0x300a000.
    [05.089]drv_disp_init finish
    [I2C-DBG] sunxi_i2c_init,line:586:    [I2C-WRN]:i2c1 has been initialized
    [I2C-DBG] sunxi_i2c_init,line:600:    i2c1 info:5c(slaveaddr),200000(speed)
    [05.110]gic: sec monitor mode
    [05.114]Loading Environment from SUNXI_FLASH... OK
    [05.123]Item0 (Map) magic is bad
    [05.125]the secure storage item0 copy0 magic is bad
    [05.130]Item0 (Map) magic is bad
    [05.133]the secure storage item0 copy1 magic is bad
    [05.138]Item0 (Map) magic is bad
    [05.141]usb burn from boot
    delay time 0
    weak:otg_phy_config
    [05.151]usb prepare ok
    [05.954]overtime
    [05.959]do_burn_from_boot usb : no usb exist
    [05.963]boot_gui_init:start
    [05.968]set disp.dev2_output_type fail. using defval=0
    [I2C-DBG] sunxi_i2c_read,line:497:    twi_send_slave_addr error
    [I2C-DBG] sunxi_i2c_read,line:497:    twi_send_slave_addr error
    [06.038]boot_gui_init:finish
    [06.040]bmp_name=bootlogo.bmp
    691256 bytes read in 4 ms (164.8 MiB/s)
    [06.061]update dts
    ** Unable to read file ULI/factory/snum.txt **
    [06.072]load file(ULI/factory/snum.txt) error.
    ** Unable to read file ULI/factory/mac.txt **
    [06.086]load file(ULI/factory/mac.txt) error.
    ** Unable to read file ULI/factory/wifi_mac.txt **
    [06.099]load file(ULI/factory/wifi_mac.txt) error.
    ** Unable to read file ULI/factory/bt_mac.txt **
    [06.118]soc ic_ver:0x6, qa_val:0x0, markid:0x54401400 dclk[0-9999]
    
    ** Unable to read file ULI/factory/specialstr.txt **
    [06.133]load file(ULI/factory/specialstr.txt) error.
    [06.143]update part info
    [06.167]update bootcmd
    Hit any key to stop autoboot:  0 
    [06.226]LCD open finish
    [06.513]Starting kernel ...
    
    [06.515][mmc]: mmc exit start
    [06.534][mmc]: mmc 2 exit ok
    
[/code]
# Accessing the serial port
UART0 is exposed on a 4-pin JST 2.0mm header (GND-RX-TX-VCC, as indicated on the silkscreen). It's the usual 3.3V TTL level, refer to the [UART howto][32674] for more details. 
# Pictures
  * [![Liontron h a133l underside.jpg][32675]][32676]
  * [![Liontron h a133l dram wifi.jpg][32677]][32678]
  * [![Liontron h a133l chips.jpg][32679]][32680]
  * [![Liontron h a133l front.jpg][32681]][32682]
  * [![Liontron h a133l left.jpg][32683]][32684]
  * [![Liontron h a133l back.jpg][32685]][32686]
  * [![Liontron h a133l right.jpg][32687]][32688]
