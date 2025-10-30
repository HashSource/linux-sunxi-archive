# Sharevdi x1
Sharevdi x1  
---  
[![X1.jpg][49455]][49456]  
Manufacturer |  [Sharevdi][49457]  
Dimensions |  _155mm_ x _105mm_ x _15mm_  
Release Date |  N/A   
Website |  [X1][49458]  
Specifications   
SoC |  [A20][49459] @ 1.2Ghz   
DRAM |  512MiB DDR3   
NAND |  4GB   
Power |  DC 5V   
Features   
LCD |  none   
Touchscreen |  none   
Video |  HDMI, VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug   
Network |  WiFi 802.11 b/g/n (RTL8188EUS), 10/100Mbps Ethernet (RTL8201CP)   
Storage |  none   
USB |  2 X USB2.0 (GL850G)   
Camera |  none   
Other |  none   
Headers |  UART0, UART1, JP1   
## Contents
  * [1 Identification][49460]
  * [2 Sunxi support][49461]
    * [2.1 Current status][49462]
    * [2.2 Locating the UART][49463]
    * [2.3 U-Boot][49464]
    * [2.4 Boot log][49465]
  * [3 Pictures][49466]

# Identification
On the front of the device, the following is printed: 
[code] 
    Sharevdi
[/code]
# Sunxi support
## Current status
Not supported 
## Locating the UART
UART1 - [1]-GND, [2]-Tx, [3]Rx, [4]-VCC 
## U-Boot
[code] 
    U-Boot 2011.09-rc1 (Jun 03 2015 - 14:33:37) Allwinner Technology
    arm-linux-gnueabihf-gcc (crosstool-NG linaro-1.13.1-4.7-2013.04-20130415 - Linaro GCC 2013.04) 4.7.3 20130328 (prerelease)
    GNU ld (GNU Binutils for Ubuntu) 2.22
[/code]
## Boot log
[code] 
    HELLO! BOOT0 is starting!
    boot0 version : 2.0.0
    read dram para.
    dram driver version: 1.15
    dram size =512MB
    0xffffffff
    super_standby_flag = 0
    Succeed in opening nand flash.
    block from 2 to 6
    deal block 2
    Succeed in reading Boot1 file head.
    The size of Boot1 is 0x00068000.
    The file stored in 0x00000000 of block 2 is perfect.
    Check is correct.
    Ready to disable icache.
    Succeed in loading Boot1.
    Jump to Boot1.
    [       0.161] boot1 version : 2.0.0
    [       0.161] pmu type = 3
    [       0.263] bat vol = 0 mv
    [       0.276] axi:ahb:apb=4:2:2
    [       0.276] set dcdc2=1400mv, clock=912M successed
    [       0.278] key
    [       2.491] LRADC key timeout without power key
    [       2.491] flash init start
    [       2.492] NB1 : enter NFB_Init
    [       2.496] NB1 : enter phy init
    [       2.499] [NAND] nand driver(A20) version: 0x0x00000002, 0x0x00000012, data: 0x426fff5c 1111692653
    [       2.508] get the good blk ratio from hwscan : 870 
    [       2.513] NB1 : nand phy init ok
    [       3.094] _RepairLogBlkTbl start
    [       3.095] Log Block Index 0x00000000, LogicBlockNum: 0x0000002a, LogBlockType: 0x00000000
    [       3.100] log0: 0x00000377, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.107] datablock: 0x00000378, lastusedpage: 0x00000074
    [       3.114] Log Block Index 0x00000001, LogicBlockNum: 0x0000007a, LogBlockType: 0x00000000
    [       3.121] log0: 0x00000380, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.128] datablock: 0x000003a0, lastusedpage: 0x0000002f
    [       3.134] Log Block Index 0x00000002, LogicBlockNum: 0x00000079, LogBlockType: 0x00000000
    [       3.142] log0: 0x0000038c, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.148] datablock: 0x000003a1, lastusedpage: 0x00000061
    [       3.155] Log Block Index 0x00000003, LogicBlockNum: 0x00000078, LogBlockType: 0x00000000
    [       3.162] log0: 0x0000038d, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.169] datablock: 0x000003a2, lastusedpage: 0x00000064
    [       3.176] Log Block Index 0x00000004, LogicBlockNum: 0x00000072, LogBlockType: 0x00000000
    [       3.183] log0: 0x00000389, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.190] datablock: 0x000003a8, lastusedpage: 0x00000002
    [       3.196] Log Block Index 0x00000005, LogicBlockNum: 0x00000068, LogBlockType: 0x00000000
    [       3.204] log0: 0x00000381, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.210] datablock: 0x000003b2, lastusedpage: 0x000000f9
    [       3.217] Log Block Index 0x00000006, LogicBlockNum: 0x00000067, LogBlockType: 0x00000000
    [       3.224] log0: 0x0000038b, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.231] datablock: 0x000003b3, lastusedpage: 0x0000006e
    [       3.238] Log Block Index 0x00000007, LogicBlockNum: 0x00000053, LogBlockType: 0x00000000
    [       3.245] log0: 0x00000382, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.251] datablock: 0x000003c7, lastusedpage: 0x00000002
    [       3.258] Log Block Index 0x00000008, LogicBlockNum: 0x00000052, LogBlockType: 0x00000000
    [       3.265] log0: 0x00000387, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.272] datablock: 0x000003c8, lastusedpage: 0x00000033
    [       3.279] Log Block Index 0x00000009, LogicBlockNum: 0x0000004d, LogBlockType: 0x00000000
    [       3.286] log0: 0x00000383, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.293] datablock: 0x000003cd, lastusedpage: 0x00000002
    [       3.299] Log Block Index 0x0000000a, LogicBlockNum: 0x00000038, LogBlockType: 0x00000000
    [       3.307] log0: 0x00000384, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.313] datablock: 0x000003e2, lastusedpage: 0x00000002
    [       3.320] Log Block Index 0x0000000b, LogicBlockNum: 0x00000031, LogBlockType: 0x00000000
    [       3.327] log0: 0x00000388, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.334] datablock: 0x000003e9, lastusedpage: 0x00000063
    [       3.341] Log Block Index 0x0000000c, LogicBlockNum: 0x00000030, LogBlockType: 0x00000000
    [       3.348] log0: 0x0000037e, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.355] datablock: 0x000003ea, lastusedpage: 0x00000002
    [       3.361] Log Block Index 0x0000000d, LogicBlockNum: 0x00000029, LogBlockType: 0x00000000
    [       3.369] log0: 0x0000038a, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.375] datablock: 0x000003f0, lastusedpage: 0x000000af
    [       3.382] Log Block Index 0x0000000e, LogicBlockNum: 0x00000041, LogBlockType: 0x00000000
    [       3.389] log0: 0x000003f1, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.396] datablock: 0x000003d9, lastusedpage: 0x00000056
    [       3.402] Log Block Index 0x0000000f, LogicBlockNum: 0x00000028, LogBlockType: 0x00000000
    [       3.410] log0: 0x00000392, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.416] datablock: 0x000003f2, lastusedpage: 0x00000062
    [       3.423] Log Block Index 0x00000010, LogicBlockNum: 0x0000007c, LogBlockType: 0x00000000
    [       3.430] log0: 0x000003f3, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.437] datablock: 0x0000039e, lastusedpage: 0x00000007
    [       3.444] Log Block Index 0x00000011, LogicBlockNum: 0x0000007b, LogBlockType: 0x00000000
    [       3.451] log0: 0x000003fa, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.458] datablock: 0x0000039f, lastusedpage: 0x00000016
    [       3.464] Log Block Index 0x00000012, LogicBlockNum: 0x00000074, LogBlockType: 0x00000000
    [       3.472] log0: 0x000003fb, Log1: 0x0000ffff, WriteIndex: 0x00000000
    [       3.478] datablock: 0x000003a6, lastusedpage: 0x00000035
    [       3.484] _RepairLogBlkTbl end
    [       3.494] NB1 : init ok
    [       3.494] flash init finish
    [       3.496] fs init ok
    [       3.497] fattype FAT16
    [       3.499] fs mount ok
    [       3.506] script finish
    [       3.507] nand good_block_ratio=870
    [       3.508] storage_type=0
    [       3.519] 0
    [       3.520] set pc
    [       3.520] usbdc_vol = 4000, usbdc_cur = 0
    [       3.522] usbpc_vol = 4400, usbpc_cur = 0
    [       3.526] init to usb pc
    [       3.529] set pc
    [       3.610] battery enough
    [       3.610] power_start=0x00000000
    [       3.610] pre sys mode
    [       3.613] key value = 2
    [       3.615] recovery key high 40, low 10
    [       3.633] show pic finish
    [       3.633] load kernel start
    [       3.651] load kernel successed
    [       3.651] start address = 0x4a000000
    [       4.339] power exit detect
    
    U-Boot 2011.09-rc1 (Jun 03 2015 - 14:33:37) Allwinner Technology 
    
    CPU:   SUNXI Family
    Board: SUN7I-EVB
    DRAM:  512 MiB
    NAND:  NB1 : enter NFB_Init
    [NAND] nand driver(A20) version: 0x2, 0x12, data: 12 1610225552
    [NAND] set nand_good_block_ratio 870 
    NB1 : nand phy init ok
    NB1 : init ok
    1740 MiB
    In:    serial
    Out:   serial
    Err:   serial
    --------fastboot partitions--------
    -total partitions:5-
    -name-        -start-       -size-      
    bootloader  : 8000          10000       
    env         : 18000         8000        
    boot        : 20000         8000        
    rootfs      : 28000         80000       
    UDISK       : a8000         2be000      
    -----------------------------------
    no misc partition is found
    Hit any key to stop autoboot:  1 0 
    
    Starting kernel ...
    
    root=/dev/nandd
    insmod nand.ko return 0
    e2fsck /dev/nandd return 0
    mount /dev/nandd return 0
    Profile Done
    Start root...
    [root@CC100 /] #startsystem...
    UI_NO
    ******UI_NO****
    manage.sh....
    ioctl[SIOCSIWAP]: Operation not permitted
    HK2
    a1234567
    psk
    OK
    QVNCServer created on port 5900
    "1024768" 
    0
    usernames "" 
    
    passwds "" 
    
    initflag wai ==  "0" 
    
    initflag li==  "0" 
    
    "psk" 
    "psk" 
    "psk" 
    "psk" 
    "HK2" "a1234567" "psk" 
    OK
    1 
    str init() 0 
    
    passwd "" 
    
    OK
    OK
    OK
    udhcpc (v1.21.0) started
    Setting IP address 0.0.0.0 on wlan0
    Sending discover...
    Sending discover...
    Sending discover...
    No lease, failing
    
    
[/code]
# Pictures
  * [![X1 front.jpg][49467]][49468]
  * [![X1 back.jpg][49469]][49470]
  * [![X1 flash.jpg][49471]][49472]
  * [![X1 lan.jpg][49473]][49474]
  * [![X1 power.jpg][49475]][49476]
  * [![X1 ram.jpg][49477]][49478]
  * [![X1 usb.jpg][49479]][49480]
  * [![X1 wifi.jpg][49481]][49482]
