# Awutils
AllWinner Utils or AWUtils is an abandoned set of tools for handling Allwinner images 
  * awflash - flash devices over USB
  * awimage - pack/unpack images
  * log2bin - convert filtered UsbSnoop log data to binary file

These tools were initially intended to allow for livesuit like flashing of devices, but this project was abandoned. 
## Download
Sources can be obtained from [Ithmar's github repository][8154] and 'make' should work to build it. 
[code] 
    git clone git://github.com/Ithamar/awutils.git
    cd awutils
    make
    
[/code]
You might need some developer libraries for USB like libusb-dev 
## Usage
Usage is quite straight forward, 'awimage -v image.img'. 
Output should look something like this: 
[code] 
    ./awimage: unpacking image.img to iamge.img.dump
    Extracting: COMMON   SYS_CONFIG000000 (6032, 6032)
    Extracting: COMMON   SYS_CONFIG100000 (57653, 57664)
    Extracting: COMMON   SPLIT_0000000000 (512, 512)
    Extracting: RFSFAT16 BOOTLOADER_00000 (4668416, 4668416)
    Extracting: RFSFAT16 ENVIROMENT_00000 (131072, 131072)
    Extracting: RFSFAT16 BOOT_00000000000 (8292352, 8292352)
    Extracting: RFSFAT16 SYSTEM_000000000 (250293504, 250293504)
    Extracting: RFSFAT16 RECOVERY_0000000 (8630272, 8630272)
    Extracting: RFSFAT16 DISKFS_000000000 (8, 16)
    Extracting: RFSFAT16 VBOOTLOADER_0000 (4, 16)
    Extracting: RFSFAT16 VENVIROMENT_0000 (4, 16)
    Extracting: RFSFAT16 VBOOT_0000000000 (4, 16)
    Extracting: RFSFAT16 VSYSTEMFS_000000 (4, 16)
    Extracting: RFSFAT16 VRECOVERYFS_0000 (4, 16)
    Extracting: BOOT     BOOT0_0000000000 (24576, 24576)
    Extracting: BOOT     BOOT1_0000000000 (221184, 221184)
    Extracting: PXTOOLS  xxxxxxxxxxxxxxxx (166912, 166912)
    Extracting: FES      FES_1-1000000000 (692, 704)
    Extracting: FES      FES_1-2000000000 (3100, 3104)
    Extracting: FES      FES_200000000000 (1488, 1488)
    Extracting: FES      FES_000000000000 (80960, 80960)
    Extracting: FET      HW_SCAN_00000000 (113152, 113152)
    Extracting: FET      UPDATE_BOOT0_000 (103728, 103728)
    Extracting: FET      UPDATE_BOOT1_000 (108560, 108560)
    Extracting: FET      FET_RESTORE_0000 (4528, 4528)
    Extracting: FET      MAGIC_CRC_START_ (128, 128)
    Extracting: FET      MAGIC_CRC_EN_000 (128, 128)
    Extracting: FET      MAGIC_DE_START_0 (128, 128)
    Extracting: FET      MAGIC_DE_END_000 (128, 128)
    Extracting: FED      FED_NAND_0000000 (116736, 116736)
    Extracting: 12345678 1234567890cardtl (81920, 81920)
    Extracting: 12345678 1234567890script (2014, 2016)
    Extracting: 12345678 1234567890boot_0 (20480, 20480)
    Extracting: 12345678 1234567890boot_1 (131072, 131072)
    Extracting: 12345678 1234567890___mbr (4096, 4096)
    Extracting: 12345678 1234567890dlinfo (1340, 1344)
    Extracting: FET      CARD_UPDATE_BOT0 (21424, 21424)
    Extracting: FET      CARD_UPDATE_BOT1 (20352, 20352)
    Extracting: FED      CARD_FED_0000000 (26640, 26640)
    Extracting: FET      CARD_HW_SCAN_000 (19248, 19248)
    
[/code]
You can then enter the newly created directory image.img.dump and explore. 
Filelist.txt is a summary of what was found (similar to what is above). 
## Status
July 2014: 
  * awflash - not compilable ([patched version][8155] requires also pkg-config)
  * awimage - packing triggers error ([bypass][8156]), unpacked-then-packed and original images are differs
