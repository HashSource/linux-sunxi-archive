# EGON
The Allwinner A10, A13, A20 and A31 boot as noted over several places, [BROM][17343] is the first step in booting and is baked into chip itself. Moving from the BROM, Allwinner boots something called boot0 and boot1 from NAND. The magicvalue for the AllWinner bootloader in various places is 'eGON' and thus the bootloader shall be known as such. 
## Contents
  * [1 eGON.BRM][17344]
    * [1.1 Header][17345]
  * [2 eGON.BT0][17346]
    * [2.1 Header][17347]
      * [2.1.1 public header][17348]
      * [2.1.2 private header][17349]
    * [2.2 Loading from MMC][17350]
  * [3 eGON.BT1][17351]
    * [3.1 Header][17352]
      * [3.1.1 public header][17353]
      * [3.1.2 private header][17354]

# eGON.BRM
The BROM bootloader has been extracted from the chip and can be found in [hno's repository.][17355]. The magic signature is "eGON.BRM". The BROM seems to start at 0x4000. If the BROM has identified boot0 in NAND loads and executes it. 
## Header
  * u32, Jump to address
  * 8 * u8, Magic "eGON.BRM" (no \n)
  * u32, length
  * 4 * u8, Boot_vsn
  * 4 * u8, eGON_vsn
  * 8 * u8, platform information

# eGON.BT0
## Header
sunxi-tools/bootinfo.c 
### public header
  * u32, Jump to address
  * 8 * u8, Magic "eGON.BT0" (no \n)
  * 32u, checksum for boot0
  * 32u, length for boot0
  * 32u, header size of boot0
  * 4 * u8, header version
  * 4 * u8, Boot_vsn
  * 4 * u8, eGON_vsn
  * 8 * u8, platform information

### private header
  * u32, header size
  * 4 * u8, header version
  * boot_dram_para_t, DRAM parameters
  * s32, uart port
  * 2 * normal_gpio_cfg,
  * s32, enable_jtag (0 off, 1 on)
  * 5 * normal_gpio_cfg, jtag_gpio
  * 32 * normal_gpio_cfg, storage_gpio
  * u8 * 512 - (32 * sizeof(normal_gpio_cfg)), storage_data

## Loading from MMC
Brom loads boot0 from nand or mmc and then chainloads boot1 from mmc. Examine the assembly source, it appears that 
  * SD driver ressembles a very close similarity with u-boot's sunxi-mmc driver. So it's extremly likly those are identical
  * A SDcard is selected and checked if it is a valid card slot
  * SD/MMC reader is initialized
  * Read 2 (1 kiB) sectors starting from sector 38192 on the SD and check this against the magic value "eGON.BT1" (no \n)
  * Read the length stored in the header and check if it is the proper size (aligns in blocks of 512)
  * Read boot1 from the SD card using the length found
  * Verify the checksum of boot1
  * set eGON_vsn (even if it failed the checksum)
  * Close the SD Card

# eGON.BT1
## Header
sunxi-tools/bootinfo.c 
### public header
  * u32, Jump to address
  * 8 * u8, Magic "eGON.BT1" (no \n)
  * 32u, checksum for boot0
  * 32u, length for boot0
  * 32u, header size of boot0
  * 4 * u8, header version
  * 4 * u8, Boot_vsn
  * 4 * u8, eGON_vsn
  * 8 * u8, platform information

### private header
  * u32, header size
  * 4 * u8, header version
  * s32, uart port
  * 2 * normal_gpio_cfg, UART gpio config
  * boot_dram_para_t, DRAM parameters
  * 32k * u8, script_buf (fex)
  * boot_core_para_t, boot core parameters
  * s32, twi_port
  * 2 * normal_gpio_cfg, twi gpio config
  * s32, debug enable (0 off, 1 on)
  * s32, hold_key_min
  * s32, hold_key_max
  * u32, work_mode
  * u32, storage_type (0 = nand, 1 = sdcard, 2 = SPI-NOR
  * 32 * normal_gpio_cfg, storage_gpio
  * u8 * 512 - (32 * sizeof(normal_gpio_cfg)), storage_data
