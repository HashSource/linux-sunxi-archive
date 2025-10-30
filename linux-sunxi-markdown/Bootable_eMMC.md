# Bootable eMMC
## Contents
  * [1 Introduction][10857]
  * [2 Information for devboard designers][10858]
  * [3 The BROM implementation details][10859]
  * [4 Installing mainline U-Boot in a boot partition][10860]
    * [4.1 Installation from Linux][10861]
    * [4.2 Installation from U-Boot][10862]
  * [5 See also][10863]

## Introduction
First of all, any eMMC can be also used as a regular SD card. Which means that it can be treated as a single large block device representing its full capacity. And the first stage bootloader (U-Boot SPL or Allwinner's boot0) is expected to be stored in a special hardcoded place between the MBR and the first partition, which does not play very nice with GPT partitioning. But if you are happy with this particular setup, then just go to the [Bootable SD card][10864] page for further information and instructions. 
eMMC supports separate boot partitions for storing the bootloader. They are not sharing the same block device with the data. 
At least Allwinner [H3][10865] is expected to support eMMC boot paritions because the manual says "Supports eMMC boot operation and alternative boot operation". The JEDEC eMMC spec mentions "boot operation" and "alternative boot operation". 
## Information for devboard designers
TBD 
## The BROM implementation details
The following information has been gained by experimentation and observation (on the A64) and has not been yet verified by examining BROM code. The BROM seems to follow the eMMC boot specification, the only restriction is the limited set of supported eMMC boot timing/width configurations. 
After checking for valid boot signatures on the SD card (SDC0), the BROM will check the eMMC boot partition configuration in EXT_CSD[179] (if it finds an eMMC device on SDC2). If it finds a boot partition to be enabled in bits [5:3] (either a 1 or a 2 in there, selecting one of the two boot partitions), it will try to boot from the first sectors of that selected boot partition, following the usual eGON boot protocol. BOOT_ACK (EXT_CSD[179], bit 6) must be set in the device, or the BROM will not boot from the partition. The BOOTBUS configuration must have been set to 4-bit SDR, with or without high-speed timings. If booting from the eMMC boot partition fails, the BROM will try to find valid boot signatures on the eMMC user partition, at offsets 8k and 128k. 
The BROM will mark the boot source in SRAM_A1[0x28] with the EMMC tag (0x02), the same used when booting from offset 8k of the normal eMMC user data partition. This prevents the SPL from easily telling the normal eMMC boot apart from loading from the eMMC boot partition. 
## Installing mainline U-Boot in a boot partition
Examination of [`mmc_burn_boot`][10866] function in the A64's BSP u-boot code and experimentation confirm that booting from a eMMC boot partition is indeed supported and that BootROM expects the `boot0` code located at the first sector of such partition. At least for the A64 chip, this has been proven to be correct: when a boot partition is properly activated (as specified by the eMMC standard, JESD84-B51), the `boot0` gets loaded and the boot goes as usual. 
For the BROM to find and load the SPL from a boot partition, some eMMC registers have to be configured (once). This can be done from Linux or from mainline U-Boot. The combined U-Boot image can then be written to the boot partition. 
The U-Boot SPL itself needs to know that it has to load the rest of U-Boot proper (plus TF-A and DTB) from the boot partition. For current mainline U-Boot this requires enabling `CONFIG_SUPPORT_EMMC_BOOT`, and also setting `CONFIG_SYS_MMCSD_RAW_MODE_U_BOOT_SECTOR` to 0x40. This will hardcode the boot partition as the U-Boot proper eMMC location. 
### Installation from Linux
First we need to disable eMMC boot partitions write protection in Linux (for more details, check <https://www.kernel.org/doc/Documentation/mmc/mmc-dev-parts.txt>): 
[code] 
       echo 0 > /sys/block/mmcblk1boot0/force_ro
       echo 0 > /sys/block/mmcblk1boot1/force_ro
    
[/code]
Then we can use the `mmc-utils` package to setup the eMMC boot configuration registers (this needs to be done only once, the settings are persistent, but can be changed again): 
[code] 
       sudo apt-get install mmc-utils
       mmc bootbus set single_hs x1 x4 /dev/mmcblk1
       mmc bootpart enable 1 1 /dev/mmcblk1    # enable partition 1, enable BOOT_ACK bits
    
[/code]
The U-Boot image can then be written to the boot partition: 
[code] 
       dd if=u-boot-sunxi-with-spl.bin of=/dev/mmcblk1boot0 bs=4k
    
[/code]
On the next reboot, U-Boot should be loaded from the boot partition. 
### Installation from U-Boot
The proper eMMC configuration allowing to boot from these partitions can be easily setup inside mainline u-boot with `SUPPORT_EMMC_BOOT` option enabled. Executing these [two commands][10867] in the u-boot's shell activates booting from the first boot partition (this needs to be done only once, the settings are persistent, but can be changed again): 
[code] 
       # mmc bootbus <dev> <bus_width> <reset_boot_bus_width> <boot_mode>
       mmc bootbus 1 1 0 0
       # mmc partconf <dev> <boot_ack> <boot_partition> <partition_acces>
       mmc partconf 1 1 1 0
    
[/code]
The U-Boot image file should then be transferred into memory, via any desired method (SD card/eMMC FAT/ext4, USB drives, TFTP). It can then be written to the boot partition: 
[code] 
       tftpboot 0x50000000 u-boot-sunxi-with-spl.bin   # or load from some ext4 or FAT partition
       mmc dev 1                                       # select the eMMC device
       mmc partconf 1 1 1 1                            # switch to boot partition 1 (the last "1" specifies the partition number)
       mmc write 0x50000000 0 0x7f0                    # generous upper limit for the size of the U-Boot image    
    
[/code]
As an alternative, use the [Fastboot][10868] approach. 
## See also
  * <http://www.jedec.org/standards-documents/results/jesd84-b51>
