# Retro Games Ltd RGL001
Retro Games Ltd RGL001  
---  
[![C64MiniOuterCase.JPG][47301]][47302]  
Manufacturer |  Retro Games Ltd   
Dimensions |  105 _mm_ x 205 _mm_ x 35 _mm_  
Release Date |  February 2018   
Website |  <http://thec64.com>  
Specifications   
SoC |  [A20][47303] @ XGhz   
DRAM |  512 DDR3 @ xxxMHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ 1A   
Features   
Video |  HDMI (Type A- full)   
Audio |  HDMI   
Storage |  Internal   
Headers |  UART, VCC (Unpopulated but drilled)   
This page needs to be properly filled according to the [New Device Howto][47304] and the [New Device Page guide][47305].
Known as the C64-mini, this has a scaled down exterior of a commodore-64, which came with a bog standard [A20][47303] SoC inside, running an emulator. 
## Contents
  * [1 Identification][47306]
  * [2 Sunxi support][47307]
    * [2.1 Current status][47308]
    * [2.2 Images][47309]
    * [2.3 HW-Pack][47310]
    * [2.4 BSP][47311]
    * [2.5 Manual build][47312]
      * [2.5.1 U-Boot][47313]
        * [2.5.1.1 Sunxi/Legacy U-Boot][47314]
        * [2.5.1.2 Mainline U-Boot][47315]
      * [2.5.2 Linux Kernel][47316]
        * [2.5.2.1 Sunxi/Legacy Kernel][47317]
        * [2.5.2.2 Mainline kernel][47318]
  * [3 Tips, Tricks, Caveats][47319]
    * [3.1 Obtaining a root shell][47320]
    * [3.2 Default root password][47321]
    * [3.3 FEL mode][47322]
    * [3.4 Board observations][47323]
  * [4 Adding a serial port (**voids warranty**)][47324]
    * [4.1 Device disassembly][47325]
    * [4.2 Locating the UART][47326]
  * [5 Pictures][47327]
  * [6 See also][47328]
    * [6.1 Manufacturer images][47329]

# Identification
On the back of the device, the following is printed: 
[code] 
    The C64 Mini
    RGL001
[/code]
The PCB has the following silkscreened on it: 
[code] 
    THEC64 V1.0
    Retro Games Ltd 2018
[/code]
Under Settings->System, you will find: 
  * Build: theC64-1.0.1-argent
  * Build Date: 02-01-2018 19:08:23

# Sunxi support
## Current status
Unknown 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][47328]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][47330] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][47331] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
There is a remote button that will start FEL mode, located underneath the device manufacturer's sticker, allowing you to enter FEL without disassembling the case. 
## Obtaining a root shell
Root shell can be obtained by using the UART: Connect the UART and establish a terminal session. Insert a USB thumb drive in either of the two USB host ports. It doesn't matter what is on the thumb drive, as long as it has a mountable filesystem (FAT is fine). Power on the board while continuously sending 's' via the serial console to interrupt u-boot. 
At the u-boot prompt, the process is as follows: 
[code] 
    redquark#setenv nand_root /dev/sda
    redquark#boot
    read boot or recovery all
    [     48.085]sunxi flash read :offset 1000000, 11549075 bytes OK
    [     48.100]ready to boot
    [     48.103][mmc]: MMC Device 2 not found
    [     48.107][mmc]:  mmc  not find,so not exit
    NAND_UbootExit
    NB1 : NAND_LogicExit
    [     48.111]
    Starting kernel ...
    
    [    0.991847] rtc_hw_init(416) err: set clksrc to external losc failed! rtc time will be wrong
    [    1.001419] sunxi_rtc_gettime(34): err, losc_err_flag is 1
    [    1.076451] [hdmi]hdmi module init
    [    1.082448] ##fb init:w=1280,h=720,fbmode=0
    [    1.099610] sunxi_rtc_gettime(34): err, losc_err_flag is 1
    [    1.105737] sunxi-rtc sunxi-rtc: hctosys: unable to read the hardware clock
    root=/dev/sda
    wait /dev/sda ready
    wait /dev/sda ready
    wait /dev/sda ready
    wait /dev/sda ready
    [    4.953983] sd 0:0:0:0: [sda] No Caching mode page present
    [    4.960123] sd 0:0:0:0: [sda] Assuming drive cache: write through
    [    4.984607] sd 0:0:0:0: [sda] No Caching mode page present
    [    4.990741] sd 0:0:0:0: [sda] Assuming drive cache: write through
    [    5.014615] sd 0:0:0:0: [sda] No Caching mode page present
    [    5.020950] sd 0:0:0:0: [sda] Assuming drive cache: write through
    e2fsck /dev/sda return 8
    mount /dev/sda return 255
    
    / # insmod /lib/modules/3.4.39/nand.ko 
    / # mount /dev/nandb /mnt
    [   65.852040] EXT4-fs (nandb): couldn't mount as ext3 due to feature incompatibilities
    [   65.944133] EXT4-fs (nandb): couldn't mount as ext2 due to feature incompatibilities
    / # passwd
    Changing password for root
    New password: 
    Retype password: 
    Password for root changed by root
    / # mv /mnt/etc/shadow /mnt/etc/shadow.old
    / # cp /etc/shadow /mnt/etc
    / # umount /mnt
    / # 
    
[/code]
Power off the board and boot normally. You should be able to log in as root using the password you set. 
## Default root password
The default root password for the TheC64 (Mini and full size) as well as the The VIC 20 is "chuckpeddle". 
## FEL mode
FEL can be entered by holding the remote button or the on board button labeled UBOOT. It can also be entered using the serial console by sending "2" on boot. 
## Board observations
There is a button on the board marked "Recovery" however it seems to have no effect. There is are many unpopulated solder pads including an SD card slot and second DRAM chip. The resistors are also unpopulated. 
# Adding a serial port (**voids warranty**)
[![C64MiniUART.JPG][47332]][47333]
[][47334]
The UART is very easy to interface. It has standard 0.01" American pin spacing and is already drilled. You can use standard header pins or a JST connector. 
Pins are, in order from top to bottom as per photo; 3.3v, Rx, Tx, GND 
In this photo, the customer has already added the UART pins. The board mounts upside down so the pins were placed on the reverse side to allow ease of access. 
See [UART howto][47335]
## Device disassembly
There is no need to remove or damage the device manufacturer's sticker unless you wish to access the u-boot switch without disassembling the case. The four screws are located under the friction pads. 
## Locating the UART
The UART is immediately West of the processor and very easy to see. 
# Pictures
  * [![C64MiniBoardLower.JPG][47336]][47337]
  * [![C64MiniBoardTop.JPG][47338]][47339]

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
In early April 2018 the company released a firmware update. It is only 2554418 bytes in size. binwalk reports the following: 
[code] 
    DECIMAL       HEXADECIMAL     DESCRIPTION
    --------------------------------------------------------------------------------
    48            0x30            ELF, 32-bit LSB executable, ARM, version 1 (SYSV)
    200340        0x30E94         SHA256 hash constants, little endian
    407696        0x63890         SHA256 hash constants, little endian
    516732        0x7E27C         SHA256 hash constants, little endian
    519698        0x7EE12         Unix path: /proc/sys/crypto/fips_enabled
    647825        0x9E291         Copyright string: "Copyright (C) 2000-2016 Free Software Foundation, Inc."
    647880        0x9E2C8         Copyright string: "Copyright (C) 2012-2016 g10 Code GmbH"
    647918        0x9E2EE         Copyright string: "Copyright (C) 2013-2016 Jussi Kivilinna"
    647980        0x9E32C         SHA256 hash constants, little endian
    668100        0xA31C4         CRC32 polynomial table, little endian
    683952        0xA6FB0         Copyright string: "Copyright 2003, 2004, 2010, 2013, 2014, 2015, 2016 g10 Code GmbH"
    
[/code]
