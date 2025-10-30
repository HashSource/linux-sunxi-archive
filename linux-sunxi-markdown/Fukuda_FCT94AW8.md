# Fukuda FCT94AW8
Fukuda FCT94AW8  
---  
[![Device front.jpg][21426]][21427]  
Manufacturer |  [Manufacturer][21428]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][21429]  
Specifications   
SoC |  [A33][21430] @ XGhz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  DC 5V @ 3A, 4000mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Touchscreen |  Silead GSL3676   
Video |  \-   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (RTL8189es)   
Storage |  µSD   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  front, rear   
Other |  Accelerometer (BMA250), GPS   
Headers |  na   
This page needs to be properly filled according to the [New Device Howto][21431] and the [New Device Page guide][21432].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][21433]
  * [2 Sunxi support][21434]
    * [2.1 Current status][21435]
    * [2.2 Images][21436]
    * [2.3 HW-Pack][21437]
    * [2.4 BSP][21438]
    * [2.5 Manual build][21439]
      * [2.5.1 U-Boot][21440]
        * [2.5.1.1 Sunxi/Legacy U-Boot][21441]
        * [2.5.1.2 Mainline U-Boot][21442]
      * [2.5.2 Linux Kernel][21443]
        * [2.5.2.1 Sunxi/Legacy Kernel][21444]
        * [2.5.2.2 Mainline kernel][21445]
  * [3 Tips, Tricks, Caveats][21446]
  * [4 Adding a serial port (**voids warranty**)][21447]
    * [4.1 Device disassembly][21448]
    * [4.2 Locating the UART][21449]
  * [5 Pictures][21450]
  * [6 Also known as][21451]
  * [7 See also][21452]
    * [7.1 Manufacturer images][21453]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    FUKUDA
    FCT94AW8
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INET-D98C-REV01
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: FCT94AW8
  * Build Number: A33_U98C_U902HC.20150209

# Sunxi support
## Current status
  *   * Can boot Olinuxino A33 but unable to make the touchscreen to work.
  *   * Kernel log:
  *   * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.390498] =====ctp_fetch_sysconfig_para=====.
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.395628] ctp_fetch_sysconfig_para: ctp_power_io script_get_item err.
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.403079] ctp_wakeup gpio number is 225
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.403093] ctp_irq gpio number is 37
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.403313] gslx680new: Matched TP firmware(FW_D90_GSL3675B_PG_1024600_DPT)!
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.420077] i2c-core: driver [gslX680] using legacy suspend method
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.426936] i2c-core: driver [gslX680] using legacy resume method
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.433711] i2c-core: driver [gslX680] registered
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.433729] i2c i2c-0: found normal entry for adapter 0, addr 0x40
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.433744] ctp_detect: addr= 40
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 1.437328] i2c i2c-0: master_xfer[0] W, addr=0x40, len=1
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.430154] sunxi_i2c_do_xfer()956 - [i2c0] xfer timeout (dev addr:0x40)
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.490039] i2c i2c-0: master_xfer[0] W, addr=0x40, len=1
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.490200] twi_start()403 - [i2c0] START can't sendout!
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.490212] sunxi_i2c_xfer()885 - [i2c0] Retrying transmission 1
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.490474] twi_start()403 - [i2c0] START can't sendout!
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.490485] sunxi_i2c_xfer()885 - [i2c0] Retrying transmission 2
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.490746] twi_start()403 - [i2c0] START can't sendout!
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.490758] sunxi_i2c_xfer()885 - [i2c0] Retrying transmission 3
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.550031] ctp_detect:I2C connection might be something wrong
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.556607] i2c i2c-1: found normal entry for adapter 1, addr 0x40
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.556623] i2c i2c-2: found normal entry for adapter 2, addr 0x40
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.556635] ****************************************************************
  *   * However sw-device shows "I2C connection sucess!", but touchscreen won't respond still.
  *   * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760052] ========sw_sysconfig_get_para===================
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760067] sw_sysconfig_get_para: device_twi_id is 0.
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760110] sw_get_write_info:open error ....IS(filp):1
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760124] sw_set_write_info:open error ....IS(filp):1
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760129] get write info erro!
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760136] config_info[5].str_info:gyr sensor_module_name=""
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760141]
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760146] config_info[4].str_info:light sensor_module_name=""
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760151]
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760155] config_info[3].str_info:ctp_module_name=""
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760160]
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760165] info:ctp_module_name=""
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760168] , key_name:ctp_module_name
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760175] ----ret : 17,s1 : 17---
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760179]
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760182] name:
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760187] device_name:,write_id:3
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760192] -----the name is null !-----
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760198] number:11 now_number:0,scan_number:0
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760204] scan_number:0, now_number:0
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760213] scan_number:1, now_number:1
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760219] scan_number:2, now_number:2
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760225] scan_number:3, now_number:3
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760231] sw_device_response_test: name = gslX680new, addr = 0x40
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760243] i2c i2c-0: master_xfer[0] W, addr=0x40, len=1
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760431] I2C connection sucess!
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760439] addr:0x40, response_addr:0x40
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760444] return number: 3
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760449] -----sw_chip_id_detect:chip_id_reg value:0x0
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760456] from copy name:gslX680new, strlen(name):0
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760464] sw_i2c_test: write_key_name:ctp_module_name
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760470] write_flag:1
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760490] sw_set_write_info:open error ....IS(filp):1
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760498] [sw_device]:sw_register_device_detect end!
  * Feb 1 12:12:07 A33-OLinuXino kernel: [ 6.760611] [sw_device]:sw_devices_events end!
  *   * ...
  * 

## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][21452]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][21454] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][21455] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
At the moment, already tried this instruction on building the 3.4 kernel at this [link][21456]. 
# Adding a serial port (**voids warranty**)
[![][21457]][21458]
[][21459]
DEVICE UART pads
The serial port pads can be found near the touchscreen flex cable header and the uSD card slot. Make sure to refer to our [UART howto][21460]. 
## Device disassembly
The back cover can be easily popped off. Start prying from top to bottom side(side with power button) [Plastic tool howto][21461]. 
## Locating the UART
The serial port pads can be found near the touchscreen flex cable header and the uSD card slot. Make sure to refer to our [UART howto][21460]. 
# Pictures
Some pictures of the device were uploaded here, [ upload more][21462], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET. 
  * [![Fukuda fct94aw8 board front 2.jpg][21463]][21464]
  * [![Fukuda fct94aw8 board front 3.jpg][21465]][21466]

# Also known as
Sunstech TAB917qc ??? 
# See also
[sample dmesg log][21467]
## Manufacturer images
A33-1024X600-os5.1-Sunstech_TAB917QC-8GB_20151029-TEST-OK.rar or TAB92QC.zip (adjust resolution to 1026x600)
