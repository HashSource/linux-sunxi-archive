# A64/Memory map
< [A64][4018]
 
The full memory map can be found in the official [A64 user manual][4021], this table here just shows deviations from that (as found by experiments on the SoC) or annotations. 
## Memory Map
Start  | End  | Size  | Name  | Remarks   
---|---|---|---|---  
`0x00000000` | `0x0000FFFF` | `64KiB` | [BROM][4022] | Only a small part is used (0x0000 ~ 0x8080)   
`0x00010000` | `0x00017FFF` | `32KiB` | [SRAM A1][4023] | The Boot ROM loads the first user provided code (usually boot0 or U-Boot's SPL, loaded from eMMC, SD card, SPI flash or FEL) into this region and executes it.   
`0x00018000` | `0x00032FFF` | `108KiB` | [SRAM C][4023] | Contiguous with the SRAM A1.  
Following the manual this region should be larger (160KiB, 0x18000-0x3FFFF). Also this region doesn't work reliably when AHB1 is clocked at 200MHz but well when clocked at 100MHz (which is the frequency used by FEL mode)[[1]][4024].   
`0x00033000` | `0x0003FFFF` | `52KiB` | RAZ/WI  | The manual claims this is part of SRAM C, but this region is always read as zero with writes ignored.   
`0x00040000` | `0x00043FFF` | `16KiB` | [arisc excp][4025] | ARISC exception vectors: sparsely implemented, only one 32-bit word at each 256 Byte boundary, followed by a hardcoded OpenRISC NOP (0x15000000).   
`0x00044000` | `0x00053FFF` | `64KiB` | [SRAM A2][4023] | This region is tightly coupled to the [ARISC][4026] core, so OpenRISC code is normally loaded here.   
Peripherals   
`0x01C28000` | `0x01C283FF` | `1KiB` | [UART 0][4027] | This is the UART used by the firmware (boot0, ATF) and U-Boot.   
Memory   
`0x40000000` | `0xFFFFFFFF` | `3GiB` | [SDRAM][4028] | DRAM space, up to 3GiB.   
# References
  1. [↑][4029] [http://irclog.whitequark.org/linux-sunxi/2016-06-29#16862925][4030]
