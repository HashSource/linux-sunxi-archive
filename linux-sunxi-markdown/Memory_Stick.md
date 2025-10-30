# Memory Stick
  1. ifndef __MS_H__
  2. define __MS_H__

  1. include "sunii.h"

  1. define MS_REG_o_CMD 0x00
  2. define MS_REG_o_DAT 0x04
  3. define MS_REG_o_STA 0x08
  4. define MS_REG_o_SYS 0x0c
  5. define MS_REG_o_ECTL 0x10
  6. define MS_REG_o_EINT 0x14
  7. define MS_REG_o_ESTA 0x18

  1. define MS_REG_CMD __REG(MSHC_REGS_BASE + MS_REG_o_CMD)
  2. define MS_REG_DAT __REG(MSHC_REGS_BASE + MS_REG_o_DAT)
  3. define MS_REG_STA __REG(MSHC_REGS_BASE + MS_REG_o_STA)
  4. define MS_REG_SYS __REG(MSHC_REGS_BASE + MS_REG_o_SYS)
  5. define MS_REG_ECTL __REG(MSHC_REGS_BASE + MS_REG_o_ECTL)
  6. define MS_REG_EINT __REG(MSHC_REGS_BASE + MS_REG_o_EINT)
  7. define MS_REG_ESTA __REG(MSHC_REGS_BASE + MS_REG_o_ESTA)

  1. define VIO_DMA 1
  2. define VIO_IRQ 0

  1. define MEMORY_STICK_1x (0)
  2. define MEMORY_STICK_PRO (1)
  3. define UNKNOWN_CARD (-1)

  1. define READ_ONLY 0x1
  2. define READ_WRITE 0x0

  1. define FAT12 0x0
  2. define FAT16 0x1
  3. define FAT32 0x2

  1. define QUICK_FORMAT 0x0
  2. define FULL_FORMAT 0x1

  1. define TPC_READ_REG 0x4
  2. define TPC_WRITE_REG 0xb
  3. define TPC_SET_RW_REG_ADRS 0x8
  4. define TPC_GET_INT 0x7
  5. define TPC_SET_CMD 0xe
  6. define TPC_READ_PAGE_DATA 0x2
  7. define TPC_WRITE_PAGE_DATA 0xd
  8. define TPC_READ_LONG_DATA 0x2
  9. define TPC_READ_SHORT_DATA 0x3
  10. define TPC_WRITE_LONG_DATA 0xd
  11. define TPC_WRITE_SHORT_DATA 0xc
  12. define TPC_EX_SET_CMD 0x9

  1. define MS_BLOCK_READ 0xaa
  2. define MS_BLOCK_WRITE 0x55
  3. define MS_BLOCK_END 0x33
  4. define MS_BLOCK_ERASE 0x99
  5. define MS_FLASH_STOP 0xcc
  6. define MS_SLEEP 0x5a
  7. define MS_CLEAR_BUF 0xc3
  8. define MS_RESET 0x3c

  1. define MSPRO_READ_DATA 0x20
  2. define MSPRO_WRITE_DATA 0x21
  3. define MSPRO_READ_ATRB 0x24
  4. define MSPRO_STOP 0x25
  5. define MSPRO_ERASE 0x26
  6. define MSPRO_SET_IBD 0x46
  7. define MSPRO_GET_IBD 0x47
  8. define MSPRO_FORMAT 0x10
  9. define MSPRO_SLEEP 0x11

  1. define REG_INT 0x01
  2. define REG_STATUS 0x02
  3. define REG_TYPE 0x04
  4. define REG_CATEGORY 0x06
  5. define REG_CLASS 0x06
  6. define REG_SYSPAR 0x10

  1. define MSPRO_REG_DATACNT0 0x11
  2. define MSPRO_REG_DATACNT1 0x12
  3. define MSPRO_REG_DATAADR0 0x13
  4. define MSPRO_REG_DATAADR1 0x14
  5. define MSPRO_REG_DATAADR2 0x15
  6. define MSPRO_REG_DATAADR3 0x16
  7. define MSPRO_REG_ATPCPAR 0x17
  8. define MSPRO_REG_CMDPAR 0x18

  1. define MS_REG_STATUS1 0x3
  2. define MS_REG_BLOCKADR0 0x13
  3. define MS_REG_BLOCKADR1 0x12
  4. define MS_REG_BLOCKADR2 0x11
  5. define MS_REG_CMDPAR 0x14
  6. define MS_REG_PAGEADR 0x15
  7. define MS_REG_OVERWFLAG 0x16
  8. define MS_REG_MANAGEFLAG 0x17
  9. define MS_REG_LOGADR0 0x18
  10. define MS_REG_LOGADR1 0x19
  11. define MS_REG_RESERVE0 0x1a
  12. define MS_REG_RESERVE1 0x1b
  13. define MS_REG_RESERVE2 0x1c
  14. define MS_REG_RESERVE3 0x1d
  15. define MS_REG_RESERVE4 0x1e

[code] 
    typedef struct 
    {
     __u8 fat_type;//@0x0
     __u32 whole_sector_number;//@0x4
     __u32 sectors_per_cluster;//@0x8
    } FILE_SYS_t;
    
[/code]
[code] 
    typedef struct 
    {
     __s8 type;//@0x0
     __u8 rw;//@0x1
     __u8 interface_mode;//@0x2
     __u8 system_status_reg;//@0x3
     __u8 interface_type_reg;//@0x4
     __u8 category_reg;//@0x5
     __u8 class_reg;//@0x6
     FILE_SYS_t filesys;//@0x8
    } MS_CARD_INFO_t;
    
[/code]
[code] 
    typedef struct 
    {
     __u8 pages_per_block;//@0x0
     __u8 boot_block[2];//@0x1
     __u8 n_boot_block;//@0x3
     __u16 table_block;//@0x4
     __u8 n_disable_block;//@0x6
     __u16 disable_block[32];//@0x8
     __u8 nsegment;//@0x48
     __u8 cur_segment;//@0x49
     __u16 l2p[496];//@0x4A
     __u16 free[16];//@0x42A
    } MS1X_GLOBAL_INFO_t;
    
[/code]
  1. define ACCESS_BY_DMA 1
  2. define ACCESS_BY_AHB 0

  1. define SERIAL_MODE 1
  2. define PARALLEL_MODE 0

[code] 
    typedef struct 
    {
     __u8 access_mode;//@0x0
     __u8 busy_cnt;//@0x1
     __u8 edian;//@0x2
    } MSC_CARD_CONFIG_INFO_t;
    
[/code]
  1. endif
