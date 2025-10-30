# Boot0
## Contents
  * [1 Overview][10376]
  * [2 Structure of Boot0][10377]
  * [3 Boot0 Example (armhf GAS)][10378]
  * [4 Boot0 Checksum Example "C"][10379]

## Overview
Boot0 is the secondary program-loader, it's loaded by [BROM][10380] in the [Boot Process][10381]. 
  * The information is incomplete, in the short time I'll fill in the missing data

## Structure of Boot0
Offset  | Name  | Size  | Notes   
---|---|---|---  
0x00 | B_INS | 4 | Branch instruction to Code Starting Point   
0x04 | Magic | 8 | Ascii string "eGON.BT0" (No Null-terminated )   
0x0c | Checksum | 4 | Simple 4-bytes Checksum (Before calculate checksum this must be 0x5F0A6C39 )   
0x10 | Size | 4 | Size of Boot0, it's must be 8-KiB aligned in NAND and 512-Bytes aligned in MMC   
0x14 | Code | - | Code of SPL. The size depends on the processor and if it 's loaded from SPI, NAND or MMC   
  * clarification: These aren't the official names

## Boot0 Example (armhf GAS)
[code] 
    _start:
      b code
      .ascii "eGON.BT0"
      .word 0x5F0A6C39, aligned_len
    
    code:
      bl reset
      ...
      ...
    
[/code]
## Boot0 Checksum Example "C"
[code] 
    ...
    ...
      checksum = 0;
      while(read(fd, &word, 4))
        checksum += word;
    
      lseek(fd, CHECKSUM_OFFSET, SEEK_SET);
      write(fd, &checksum, 4);
    ...
    ...
    
[/code]
