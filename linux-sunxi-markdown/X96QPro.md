# X96QPro
X96QPro  
---  
[![X96QPro.jpg][59726]][59727]  
Manufacturer |  SUNNZO   
Dimensions |  108 _mm_ x 108 _mm_ x 18 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][59728]  
Specifications   
SoC |  [H313][59729] @ 1.008Ghz   
DRAM |  1GiB LPDDR3 @ 648MHz   
NAND |  8GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full), CVBS   
Audio |  3.5mm AV plug, SPDIF, HDMI   
Network |  WiFi: 802.11 b/g/n ([XRadio XR819][59730]); 10/100Mbps Ethernet ([Internal][59731])   
Storage |  µSD, eMMC   
USB |  2 USB2.0 Host   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][59732] and the [New Device Page guide][59733].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][59734]
  * [2 Sunxi support][59735]
    * [2.1 Current status][59736]
    * [2.2 Manual build][59737]
      * [2.2.1 Mainline U-Boot][59738]
      * [2.2.2 Mainline Linux Kernel][59739]
  * [3 Tips, Tricks, Caveats][59740]
    * [3.1 FEL mode][59741]
    * [3.2 Device specific topic][59742]
    * [3.3 ...][59743]
  * [4 Adding a serial port (**voids warranty**)][59744]
    * [4.1 Device disassembly][59745]
    * [4.2 Locating the UART][59746]
  * [5 Pictures][59747]
  * [6 Schematic][59748]
  * [7 Also known as][59749]
  * [8 See also][59750]
    * [8.1 Manufacturer images][59751]

# Identification
The top has an "X96Q Pro" logo embossed in the centre 
On the bottom of the device, the following is embossed: 
[code] 
    TT TV BOX
    ANDROID PLAYER
    Model: X96Q Pro RAM: 1G ROM:8G
[/code]
The PCB has the following silkscreened on it: 
[code] 
    X96
    BA306_627_V3.0 20405
[/code]
In android, under Settings->About, you will find: 
  * Model Number: _TODO_
  * Build Number: _TODO_

# Sunxi support
## Current status
Not yet supported, but U-Boot and kernel support WIP. Since it uses the AC200 integrated 100MBit Ethernet PHY, it relies on pending mainline support for the chip to have working Ethernet. 
## Manual build
You can build things for yourself by following our [ Manual build howto][59752] and by choosing from the configurations available below. 
### Mainline U-Boot
### Mainline Linux Kernel
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The button on the top of the PCB triggers [ FEL mode][59753] mode (to be confirmed). It is reachable through the CVBS connector.. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][59754]][59755]
[][59756]
X96QPro UART pads
To get access to the UART pads, you have to open the box. 
## Device disassembly
To open up the case, remove the feet to expose the screws. 
## Locating the UART
The UART pads are located on the top right of the device PCB, between USB 1 and the CVBS socket, providing RX, TX and GND signals, as pictured. The assignment is printed on the other side. To solder some wires or pins, just remove the PCB (three screws). To route the wires outside the case, you could drill a small hole anywhere to the right on the pcb where there is an empty space in the case. Once done, follow the [UART howto][59757]. 
boot log with factory firmware 
[code] 
    [240]HELLO! BOOT0 is starting!
    [243]BOOT0 commit : 803d783
    [245]set pll start
    [248]periph0 has been enabled
    [251]set pll end
    [253]unknow PMU
    [255]unknow PMU
    [257]PMU: AXP1530
    [259]dram return write ok
    [261]board init ok
    [263]DRAM BOOT DRIVE INFO: V0.645
    [267]the chip id is 0x5000
    [269]chip id check OK
    [273]DRAM_VCC set to 1200 mv
    [276]DRAM CLK =648 MHZ
    [278]DRAM Type =7 (3:DDR3,4:DDR4,7:LPDDR3,8:LPDDR4)
    [286]Actual DRAM SIZE =1024 M
    [289]DRAM SIZE =1024 MBytes, para1 = 30fa, para2 = 4000000, dram_tpr13 = 6061
    [302]DRAM simple test OK.
    [305]rtc standby flag is 0x0, super standby flag is 0x0
    [310]dram size =1024
    [313]card no is 2
    [315]sdcard 2 line count 8
    [318][mmc]: mmc driver ver 2020-09-10 15:32
    [327][mmc]: Wrong media type 0x0, but host sdc2, try mmc first
    [333][mmc]: ***Try MMC card 2***
    [357][mmc]: RMCA OK!
    [359][mmc]: bias 4
    [362][mmc]: MMC 5.0
    [363][mmc]: HSSDR52/SDR25 8 bit
    [367][mmc]: 50000000 Hz
    [369][mmc]: 7456 MB
    [371][mmc]: ***SD/MMC 2 init OK!!!***
    [450]Loading boot-pkg Succeed(index=0).
    [454]Entry_name        = u-boot
    [464]Entry_name        = monitor
    [467]Entry_name        = dtbo
    [470]Entry_name        = dtb
    [474]tunning data addr:0x4a0003e8
    [477]Jump to second Boot.
    NOTICE:  BL3-1: v1.0(debug):76097ec
    NOTICE:  BL3-1: Built : 14:52:17, 2021-04-20
    NOTICE:  BL3-1 commit: 8
    NOTICE:  cpuidle init version V1.0
    ERROR:   Error initializing runtime service tspd_fast
    NOTICE:  BL3-1: Preparing for EL3 exit to normal world
    NOTICE:  BL3-1: Next image address = 0x4a000000
    NOTICE:  BL3-1: Next image spsr = 0x1d3
    
    U-Boot 2018.05 (Nov 22 2021 - 10:00:03 +0800) Allwinner Technology
    
    [00.556]CPU:   Allwinner Family
    [00.559]Model: sun50iw9
    I2C:   ready
    [00.563]DRAM:  1 GiB
    [00.566]Relocation Offset is: 35ebf000
    [00.607]secure enable bit: 0
    [00.610]pmu_axp152_probe pmic_bus_read fail
    [00.614]PMU: AXP1530
    [00.620]CPU=1008 MHz,PLL6=600 Mhz,AHB=200 Mhz, APB1=100Mhz  MBus=400Mhz
    [00.628]drv_disp_init
    [00.659]__clk_enable: clk is null.
    [00.665]drv_disp_init finish
    [00.667]gic: sec monitor mode
    [00.696]flash init start
    [00.698]workmode = 0,storage type = 2
    [00.701]MMC: 2
    [00.702][mmc]: mmc driver ver uboot2018:2021-07-19 14:09:00
    [00.709][mmc]: get sdc_type fail and use default host:tm4.
    [00.720][mmc]: SUNXI SDMMC Controller Version:0x40502
    [00.744][mmc]: Best spd md: 3-HS200/SDR104, freq: 4-150000000, Bus width: 8
    [00.751]sunxi flash init ok
    [00.754]Loading Environment from SUNXI_FLASH... OK
    [00.764]usb burn from boot
    delay time 0
    weak:otg_phy_config
    [00.777]usb prepare ok
    [01.580]overtime
    [01.584]do_burn_from_boot usb : no usb exist
    [01.588]boot_gui_init:start
    FAT: Misaligned buffer address (7be78e78)
    32 bytes read in 4 ms (7.8 KiB/s)
    tcon_de_attach:de=0,tcon=2[01.872]boot_gui_init:finish
    [01.876]bmp_name=bootlogo.bmp
    3686456 bytes read in 28 ms (125.6 MiB/s)
    [01.917][mmc]: delete mmc-hs400-1_8v from dtb
    [01.924]update dts
    ** Unrecognized filesystem type **
    [01.935]load file(ULI/factory/rootwait init.txt) error.
    ** Unrecognized filesystem type **
    [01.949]load file(ULI/factory/snum.txt) error.
    [01.953]name in map mac
    ** Unrecognized filesystem type **
    [01.965]load file(ULI/factory/wifi_mac.txt) error.
    ** Unrecognized filesystem type **
    [01.978]load file(ULI/factory/bt_mac.txt) error.
    ** Unrecognized filesystem type **
    [01.992]load file(ULI/factory/selinux.txt) error.
    ** Unrecognized filesystem type **
    [02.005]load file(ULI/factory/specialstr.txt) error.
    [02.017]update part info
    [02.040]update bootcmd
    [02.042]No ethernet found.
    Hit any key to stop autoboot:  0 
    [02.257]Starting kernel ...
    
[/code]
# Pictures
  * [![X96QPro Top.jpg][59758]][59759]
  * [![X96QPro Bottom.jpg][59760]][59761]
  * [![X96QPro Box.jpg][59762]][59763]
  * [![X96QPro Rear.jpg][59764]][59765]
  * [![X96QPro Side.jpg][59766]][59767]
  * [![X96QPro PCB Top.jpg][59768]][59769]
  * [![X96QPro PCB Bottom.jpg][59770]][59771]
  * [![X96QPro Heatsink.jpg][59772]][59773]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
