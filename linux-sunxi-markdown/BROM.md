# BROM
## Contents
  * [1 A10/A20][8460]
    * [1.1 Reset vector][8461]
    * [1.2 eGON Boot][8462]
    * [1.3 Source code for boot0 and boot1][8463]
  * [2 A31][8464]
  * [3 A64][8465]
  * [4 U-Boot SPL limitations][8466]
  * [5 Other booting methods][8467]

## A10/A20
After power-up, the A10/A20 boots from an integrated, non-replaceable 32 KiB ROM chip (Boot ROM or BROM). This could be considered the primary program-loader. The SoC starts to fetch instructions from address 0xffff0000 which is where the BROM is located at. The BROM split up into two parts: The first part (at 0xffff0000) is the [FEL mode][8468] and the second is the [eGON.BRM][8469] (located at 0xffff4000). 
### Reset vector
The [reset vector][8470] is located at the very begining of FEL mode: at address 0xffff0000. On reset, it jumps to 0xffff0028 where it [loads][8471] 0xffff4000 (eGON.BRM) into the program counter to be executed next. 
### eGON Boot
The [eGON Boot ROM][8469] performs a few tasks: 
  1. does some [co-processor setup][8472] ([c15][8473], (virtual) System Control Coprocessor).
  2. [disables][8474] the [WatchDog Timer][8475]
  3. [setups][8476] [CPU, AXI, AHB and APB0 clocks][8477]
  4. [enables][8478] [AHB Gating][8479]
  5. [enables][8480] [APB0 Gating][8481]
  6. [sets][8482] the Stack Pointer to 32K
  7. then it [jumps][8483] to ['boot'][8484] which immediately [jumps to][8485] [check_uboot][8486]
  8. [check_uboot][8486] setups up some registers, then [checks the status pin][8487] (often called FEL pin, BSP pin or **uboot**) 
     1. if the pin is low (connected to GND) [executes][8488] [FEL][8468] mode at 0xffff0020.
     2. If the pin is high it continues trying to boot from the following media and on failure continues to the next in order. 
        1. [SD Card0][8489] also known as [MMC0][8490]
        2. [Internal NAND flash][8491] also known as [NAND][8492]
        3. [SD Card2][8493] also known as [MMC2][8494]
        4. [SPI connected NOR flash][8495] also known as [SPI][8496]
        5. [If all fails][8497], [FEL/USB Boot][8498] mode is [executed][8499] from 0xffff0020

As can be seen, the A10/A20 has several ways to boot and a lot would need to go wrong or 'fail' before entering [FEL mode][8498]. This is especially important if there is a valid header in the NAND flash. Obviously this can be abused, by corrupting the header and thus forcing failure. If no other boot options are available, then FEL mode should be the final result. As a bypass mechanism, the A10 has the so called _Boot Select Pin (BSP)_. This pin is normally internally pulled up by a 50KΩ resistor. If the pin is pulled low to GND, the A10 will try to boot into [FEL mode][8498]. Otherwise the above boot-order will be tried. 
### Source code for boot0 and boot1
The source code for boot0 and boot1 for the A20 chip is included in [an SDK from Olimex][8500]:   
[A20-SDK.torrent][8501]
As of March 2015 Allwinner has also published bootloader code on [GitHub][8502]. 
## A31
Instead of falling through boot options, the A31 boots slightly differently. One fel pin, which is the same as A10/A20. Two boot select pins, boot sel0 and boot sel1, which decide where to boot. The fel key priority is higher than the boot select key. The boot-flow process is explained briefly below. 
[code] 
    boot-> check fel key pressed (yes)-> check if sd0 bootable(no) -->go to fel mode
                             \                                   \
                              \                              (yes)\__ boot from sd0
                               \ 
                                \                                       _____[00] boot from nand flash (go to fel mode if failed)
                           (no)  \                                     /_____[01] boot from sd2 (go to fel mode if failed)
                                  \                                   /
                                   \___check boot sel[0:1]-------------------[10] boot from emmc2 (go to fel mode if failed)
                                                                      \
                                                                       \______[11] boot from spi (go to fel mode if failed)
    by hipboi
    
[/code]
## A64
The boot-flow process is explained briefly below (based on experimenting with [Pine64][8503] and [Jide Remix Mini][8504]): 
[code] 
    boot-> check fel key pressed (yes)--> FEL mode (boot from USB OTG)
                              \  
                          (no) \
                                \-------> 1) try to boot from SMHC0 (SD card)
                                          2) try to boot from SMHC2 (eMMC)
                                          3) try to boot from SPI0 (SPI NOR Flash)
                                          4) FEL mode (boot from USB OTG)
    
[/code]
FIXME: The A64 manual says that booting is supported from "NAND Flash", "SD/TF card", "eMMC" and "Nor Flash", but does not provide any details. "NAND Flash" is not listed above because we have not seen such devices yet. 
## U-Boot SPL limitations
In order to be recognized by the BROM, the SPL needs to written to a certain location on the SD card (see [ SD Card Layout][8505]) and have a special header with a correct checksum. Such special header can be added to a binary file using the [Mksunxiboot][8506] tool. The size of the SPL must be a multiple of 8 KiB in NAND and a multiple of 512 bytes on the SD card (see the ["sunxi/nand: change BLOCK_SIZE in mksunxiboot to match NAND block size"][8507] commit in U-Boot). 
SoC name  | SPL size limit on MMC  | SPL size limit on NAND  | SPL load address  | Initial stack pointer value (SP register)  | Notes   
---|---|---|---|---|---  
Allwinner [A10][8508] | 24 KiB |  | 0x00000 | sp=0x07FF8 | There is an artificial 24 KiB limit and anything larger is rejected by the BROM   
Allwinner [A13][8509] | 0x7E00 |  | 0x00000 | sp=0x07FF8 | Sizes larger than 0x7E00 bytes are rejected by the BROM. Exactly 0x7E00 is fine, as verified by writing a special pattern at the end of the SPL file and checking it in the SRAM. Note that the top of the SPL stack needs to be changed in U-Boot sources from 0x8000 to something like 0x7000 in order to make it a clean experiment.   
Allwinner [A20][8510] | 24 KiB |  | 0x00000 | sp=0x07FF8 | There is an artificial 24 KiB limit and anything larger is rejected by the BROM   
Allwinner [A31s][8511] | 32 KiB |  | 0x00000 | sp=0x27FD8 | Sizes larger than 32 KiB are rejected by the BROM. Exactly 32 KiB is fine, as verified by writing a special pattern at the end of the SPL and checking it in the SRAM.   
Allwinner [A64][8512] | 32 KiB |  | 0x10000 | sp=0x47FE0 | Sizes larger than 32 KiB are rejected by the BROM. Exactly 32 KiB is fine, as verified by writing a special pattern at the end of the SPL and checking it in the SRAM.   
Allwinner [H3][8513] | 32 KiB |  | 0x00000 | sp=0x0F7DC | Sizes larger than 32 KiB are rejected by the BROM. Exactly 32 KiB is fine, as verified by writing a special pattern at the end of the SPL and checking it in the SRAM.   
Allwinner [H6][8514] | 139 KiB |  | 0x20000 | sp=0x42dd8 | Sizes larger than 139 KiB are NOT rejected by the BROM, but won't execute, probably crash the BROM by overwriting its stack or data.   
Allwinner [H616][8515] | 212 KiB |  | 0x20000 | sp=0x551c4 | Sizes larger than 212 KiB are NOT rejected by the BROM, but won't execute, probably crash the BROM by overwriting its stack or data.   
Early SoC variants (A10 and A20) used to have a somewhat artificial 24 KiB restriction of the SPL size. Then A13 tried to increase this limit to almost 32 KiB. Later SoC variants (A31 / H3 / A64) have a 32 KiB size limit for the SPL, though this is still artificial, as the A64, for instance, has 192 KiB of contiguous SRAM space. The latest SoCs (H6, H616) lift this limit, and are most likely just restricted by the BROM's own SRAM usage. 
It is possible to increase the practical size limit to some extent by [making use of runtime decompression (via LZO or UCL)][8516]. As an additional bonus, compression should eliminate repeatable patterns, which are supposedly bad for MLC NAND and maybe (?) help the [NAND hardware randomizer][8517] to some extent. And while we are at it, the runtime decompressor code could also take care of applying relocations, allowing to use the same unified SPL binary even on devices with different SPL load addresses. 
## Other booting methods
  * [How to boot the A10 over the network][8518]
