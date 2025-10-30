# SRAM Controller Register Guide
# SRAM Controller
## Overview
Static Random Access Memory [SRAM][48482] is used by devices, such as the CPU, for extra fast memory or as cache. 
On the the SRAM is split up into segments, A, B, C, D, NAND and CPU, A - is generally usable ram 48kB CPU caches not mapped to address space and can't be used by any other purpose C,D sections can be mapped over SRAM config but it required for internal hardware caches for VE, NAND, ISP 
## SRAM Sections
Section  | Subsection  | Address  | Size  | Description  | Usable  | A10  | A13  | A20  | A31  | A23   
---|---|---|---|---|---|---|---|---|---|---  
**A** | A1  | `0x00000000 - 0x00003fff` | 16 kiB / 32kiB on A31  |  | Y  | Y  | Y  | Y  | Y  | Y   
| A2  | `0x00004000 - 0x00007fff` | 16 kiB  |  | Y  | Y  | Y  | Y  | N  | N   
| A3  | `0x00008000 - 0x0000b3ff` | 13 kiB  | EMAC  | Y  | Y  | Y  | Y[[1]][48483] | N  | N   
| A4  | `0x0000b400 - 0x0000bfff` | 3 kiB  | EMAC  | Y  | Y  | ?  | Y[[2]][48484] | N  | N   
| A2  | `0x00044000 - 0x00053fff` | 64 kiB  | Shared with [AR100][48485] OpenRISC core  | N  | N  | N  | N  | Y  | Y   
| VE SRAM  | `0x00004000 - 0x0000ffff` | 64 kiB  |  | N  | N  | N  | N  | ?  | Y   
**B** | B  | `0x00020000 - 0x0002ffff` | 64 kiB  | Secure RAM  | Y  | Y  | N  | Y  | Y  | N   
**C** | C1  | `0x01d00000 - 0x01d7ffff` | 512 kiB {first 62 kiB work on A10, rest is partly read only, wraps around after 0x01d40000}  | CedarV  | Y[[3]][48486] | Y  | Y  | Y  | N  | N   
| C2  | `0x01d80000 - 0x01d9ffff` | 128 kiB {first 6912 B work on A10, rest is partly forced zero}  | CedarA  | Y[[4]][48487] | Y  | ?  | Y  | N  | N   
| C3  | `0x01dc0000 - 0x01dcffff` | 64 kiB {unconfirmed}  | ISP/BIST  | N[[5]][48488] | Y  | Y  | Y  | N  | N   
**D** | D  | `0x00010000 - 0x00010fff` | 4 kiB {unconfirmed}  | USB FIFOs  | Y[[6]][48489] | Y  | Y  | Y  | Y  | N   
**NAND** | NAND  | `0x01c03400 - 0x01c03c00` {unconfirmed}  | 2 kiB  | NAND flash controller  | Y  | Y  | Y  | ?   
**CPU** | CPU I-cache  | Not mapped  | 32 kiB  |  | N  | Y  | Y  | Y  | Y  | Y   
| CPU D-Cache  | Not mapped  | 32 kiB  |  | N  | Y  | Y  | Y  | Y  | Y   
| CPU L2 Cache  | Not mapped  | 256/128 kiB  |  | N  | Y  | Y  | Y  | Y  | Y   
  1. [↑][48490] For A20 SRAM_A3_A4_MAP set up for emac by default, so you should change it for make it usable
  2. [↑][48491] For A20 SRAM_A3_A4_MAP set up for emac by default, so you should change it for make it usable
  3. [↑][48492] VE must be enabled (AHB gate and VE SCLK)
  4. [↑][48493] ACE must be enabled (AHB gate and ACE SCLK)
  5. [↑][48494] Changing bit SRAM_C3_MAP doesn't allow writing to SRAM_C3( as like others there should be need enable ISP/BIST gate and clock but uncheked)
  6. [↑][48495] Register SRAM_CTL1_CFG needs SRAM_D_MAP set to 0 to allow access

It should be noted, that all accessability tests where done using the u-boot console. It is possible that some secret combination (like emac) needs to be set to actually allow writing. 
## SRAM Registers
SRAM Base address: 0x01c00000 
Register Name  | Offset  | Size  | Description  | A31  | A20   
---|---|---|---|---|---  
`SRAM_CTL0_CFG` | `0x0000` | `DWORD` | SRAM Control register 0  | Y  | Y   
`SRAM_CTL1_CFG` | `0x0004` | `DWORD` | SRAM Control register 1  | Y  | Y   
`SRAM_TIMING_CTRL` | `0x0008` | `DWORD` | {unconfirmed} 000000ff on a20 set possible  | ?  | Y   
`SRAM_BIST_CTRL` | `0x0014` | `DWORD` | {looks present but don't know how it works}  | ?  | Y   
`SRAM_BIST_??` | `0x0018` | `DWORD` | {looks present but don't know how it works}  | ?  | Y   
`SRAM_BIST_START_ADDR` | `0x001c` | `DWORD` | {looks present but don't know how it works}  | ?  | Y   
`SRAM_BIST_END_ADDR` | `0x0020` | `DWORD` | {looks present but don't know how it works}  | ?  | Y   
`SRAM_VER_REG` | `0x0024` | `DWORD` | Version Register  | Y  | Y   
`SRAM_NMI_CTRL` | `0x0030` | `DWORD` | see A20 manual {others unconfirmed}  | N  | Y   
`SRAM_NMI_PEND` | `0x0034` | `DWORD` | see A20 manual {others unconfirmed}  | N  | Y   
`SRAM_NMI_EN` | `0x0038` | `DWORD` | see A20 manual  | N  | Y   
`SRAM_EMA` | `0x0044` | `DWORD` | Undocumented magic in boot0.  | N  | Y   
` SRAM_GPU_DXT_BC_EN` | `0x0050` | `DWORD` | GPU DXT BC Enable (A31 only)  | Y  | N   
` SRAM_GPU_SW_GATE` | `0x0054` | `DWORD` | GPU SW Gathing (A31 only)  | Y  | N   
` SRAM_GPU_POWER_STATUS` | `0x0060` | `DWORD` | GPU Power Status(A31 only)  | Y  | N   
### SRAM_CTL0_CFG
Default value: 0x7fffffff  
Offset: 0x0000 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`SRAM_C1_MAP` | `0:30` | `Read/Write` | `0x7fffffff` | ` `
[code]
        0 = CPU/DMA
        1 = VE
      
    
[/code]
| Each bit represents a page to be mapped to the CPU/DMA unit or to the VE. Each bit (combination) may represent a byte/page of sram C1   
| `31` |  |  | `reserved`  
### SRAM_CTL1_CFG
Default value A10: 0x1300  
Default value A20: 0x1314 Default value A13: 0x1000  

Offset: 0x0004 
Name  | Bit  | Read/Write  | Default (Binary)  | Values  | Description   
---|---|---|---|---|---  
`SRAM_D_MAP` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = CPU/DMA
        1 = USB0
      
    
[/code]
| Map SRAM D to either the CPU/DMA unit or to USB0   
`reserved` | `1` |  |  |  |   
`SRAM_` | `2` | `Read/Write` | `0b0` | ` `
[code]
        0 = ?
        1 = ?
      
    
[/code]
| [EMAC][48496] at the least changes this.A20 have this set by default   
`reserved` | `3` |  |  |  |   
`SRAM_A3_A4_MAP` | `4:5` | `Read/Write` | `0b00` | ` `
[code]
        00 = CPU/DMA
        01 = EMAC
        10 = no operation
        11 = no operation
      
    
[/code]
| Map SRAM A3 and A4 to either the CPU/DMA unit or to EMAC   
`reserved` | `6:7` |  |  |  |   
`SRAM_C2_MAP` | `8:9` | `Read/Write` | `0b11` | ` `
[code]
        00 = CPU/BIST
        01 = AE
        10 = CE
        11 = ACE
      
    
[/code]
| Map SRAM C2 to either the CPU/BIST unit or to the AE or to the CE or to the ACE   
`reserved` | `10:11` |  |  |  |   
`SRAM_C3_MAP` | `12` | `Read/Write` | `0b1` | ` `
[code]
        0 = CPU/BIST
        1 = ISP
      
    
[/code]
| Map SRAM C3 to either the CPU/BIST unit or to ISP   
`reserved?` | `13:22` | `Read/Write` | `0` |  |   
`reserved` | `22:30` | `Read Only` | `0b0` | Reserved  |   
`SRAM_BIST_DMA_CTL` | `31` | `Read/Write` | `0b0` | ` `
[code]
        0 = DMA
        1 = BIST
      
    
[/code]
| Normal DMA or BIST control (build in self test)   
### SRAM_VER_REG
Default value: 0x0000100   
Offset: 0x0024   

Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
VER_CHIP_ID  | 31:16  | Readonly  | 0x0000  | ` `
[code]
       if VER_R_EN is set:
        0x1623 = A10
        0x1625 = A13/A10s/R8
        0x1633 = A31/A31s
        0x1639 = A80
        0x1650 = A23
        0x1651 = A20
        0x1667 = A33
        0x1680 = H3
        0x1689 = A64/H64
        0x1701 = R40
        0x1718 = H5
       otherwise
        0
      
    
[/code]
| Chip ID. Requires VER_R_EN to be set.   
VER_R_EN  | 15  | Read/Write  | 0  | ` `
[code]
       0 = Disabled
       1 = Enabled
      
    
[/code]
| Enable VER_CHIP_ID reading in upper bits   
BOOT_SEL_PAD_STA  | 6:8  | Read  | \-  | For A10 
[code]
    0b000 = U-BOOT button pressed
    0b001 = U-BOOT button released
    
[/code]
For A31 
[code] 
    0b000 = All buttons pressed
    0b100 = U-BOOT button released
    0b111 = Boot from NAND
    0b110 = Boot from SD2
    0b101 = Boot from eMMC2
    0b100 = Boot from SPI-NOR
    0b111 = All buttons released
    
[/code]
| Current status of BootSelect pin(s), should be sampled by APB clock, no hardware debounce [[1]][48497]  
VER_BITS  | 7:0  | Read  | 0b001  |  | Mask revision level of SoC   
  1. [↑][48498] [https://github.com/hno/Allwinner-Info/blob/master/BROM/ffff4000.s#L2402][48499]

### SRAM_BIST_CTRL
Default value: 0x0000100   
Offset: 0x0024   

Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
SRAM_BIST_EN  | 0  | Read/Write  | 0  | ` `
[code]
     
    
[/code]
| looks like enable bit   
SRAM_BIST_START  | 1  | Read/Write  | 0  | ` `
[code]
     
    
[/code]
| looks like start, toggle it to 0 than to 1 when enable bit set will change RO register part   
SRAM_BIST_TOGGLE_?  | 7  | Read/Write  | 0  | ` `
[code]
     
    
[/code]
| enable crc like value on RO part   
### SRAM_EMA
Default value: 0x00  
Offset: 0x0044 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`SRAM_EMA_EN` | `0:31` | `Read/Write` | `0x0000` | ` `
[code]
      
    
[/code]
| Some caching related DRAM setup; boot0 sources describe this as "config ema for cache sram". It is initialized to 0x1800 very early in u-boot.   
| `31` |  |  | `reserved`  
## Initial values
In the 0x01c00000 - 0x01c00fff region, designated as SRAM Register, only a small section here is documented. It can be found using the u-boot console, some other default values. 0x01c00016 = 0x0200 0x01c00026 = 0x0100 0x01c00030 - 0x01c000f0 appears to be 0. 0x01c000100 - 0x1c00fff appears to 'wrap around' and display the same section again, so higher address lines seem to be unmapped. 
### Default map
#### A20
[code] 
    01c00000: 7fffffff 00001314 00000000 00000000    ................
    01c00010: 00000000 00000200 00000000 00000000    ................
    01c00020: 00000000 00000100 00000000 00000000    ................
    01c00030: 00000000 00000001 00000000 00000000    ................
    01c00040: 00000000 00000000 00000000 00000000    ................
    01c00050: 00000000 00000000 00000000 00000000    ................
    01c00060: 00000000 00000000 00000000 00000000    ................
    01c00070: 00000000 00000000 00000000 00000000    ................
    01c00080: 00000000 00000000 00000000 00000000    ................
    01c00090: 00000000 00000000 00000000 00000000    ................
    01c000a0: 00000000 00000000 00000000 00000000    ................
    01c000b0: 00000000 00000000 00000000 00000000    ................
    01c000c0: 00000000 00000000 00000000 00000000    ................
    01c000d0: 00000000 00000000 00000000 00000000    ................
    01c000e0: 00000000 00000000 00000000 00000000    ................
    01c000f0: 00000000 00000000 00000000 00000000    ................
    
[/code]
All to 1 
[code] 
    01c00000: ffffffff 80ff13ff 000000ff 00000000    ................
    01c00010: 00000000 000001ff ffffffff ffffffff    ................
    01c00020: ffffffff 16518100 00000000 00000000    ......Q.........
    01c00030: 00000003 00000000 00000001 00000000    ................
    01c00040: 00000000 00000000 00000000 00000000    ................
    01c00050: 00000000 00000000 00000000 00000000    ................
    01c00060: 00000000 00000000 00000000 00000000    ................
    01c00070: 00000000 00000000 00000000 00000000    ................
    01c00080: 00000000 00000000 00000000 00000000    ................
    01c00090: ffffffff 00ffffff 0000ffff 00000000    ................
    01c000a0: 00000000 00000000 00000000 00000000    ................
    01c000b0: 00000000 00000000 00000000 00000000    ................
    01c000c0: 00000000 00000000 00000000 00000000    ................
    01c000d0: 00000000 00000000 00000000 00000000    ................
    01c000e0: 00000000 00000000 00000000 00000000    ................
    01c000f0: 00000000 00000000 00000000 00000000    ................
    
    
[/code]
#### A10
[code] 
    md 0x01c00000 0x40
    01c00000: 7fffffff 00001300 00000000 00000000    ................
    01c00010: 00000000 00000200 00000000 00000000    ................
    01c00020: 00000000 00000100 00000000 00000000    ................
    01c00030: 00000000 00000000 00000000 00000000    ................
    01c00040: 00000000 00000000 00000000 00000000    ................
    01c00050: 00000000 00000000 00000000 00000000    ................
    01c00060: 00000000 00000000 00000000 00000000    ................
    01c00070: 00000000 00000000 00000000 00000000    ................
    01c00080: 00000000 00000000 00000000 00000000    ................
    01c00090: 00000000 00000000 00000000 00000000    ................
    01c000a0: 00000000 00000000 00000000 00000000    ................
    01c000b0: 00000000 00000000 00000000 00000000    ................
    01c000c0: 00000000 00000000 00000000 00000000    ................
    01c000d0: 00000000 00000000 00000000 00000000    ................
    01c000e0: 00000000 00000000 00000000 00000000    ................
    01c000f0: 00000000 00000000 00000000 00000000    ................
    
[/code]
#### A31
[code] 
    01c00000: 7fffffff 00001300 00000000 00000000    ................
    01c00010: 00000000 00000200 00000000 00000000    ................
    01c00020: 00000000 16338700 00000000 00000000    ......3.........
    01c00030: 00000000 00000000 00000000 00000000    ................
    01c00040: 22222222 22223a22 00000000 00000000    """"":""........
    01c00050: 00000000 00000001 00000001 00000000    ................
    01c00060: 00000000 00000000 00000000 00000000    ................
    01c00070: 00000200 00000000 00000000 00000000    ................
    
[/code]
### All to 1
mw 0x01c00000 0xffffffff 0x40  
md 0x01c00000 0x40 
[code] 
    01c00000: ffffffff 800f13ff ffffffff 00000000    ................
    01c00010: 00000000 000002ff ffffffff ffffffff    ................
    01c00020: ffffffff 16238100 000f0007 00000000    ......#.........
    01c00030: 00000000 00000000 00000000 00000000    ................
    01c00040: 00000000 00000000 00000000 00000000    ................
    01c00050: 00000000 00000000 00000000 00000000    ................
    01c00060: 00000000 00000000 00000000 00000000    ................
    01c00070: 00000000 00000000 00000000 00000000    ................
    01c00080: 00000000 00000000 00000000 00000000    ................
    01c00090: ffffffff 00ffffff 0000ffff 00000000    ................
    01c000a0: 00000000 00000000 00000000 00000000    ................
    01c000b0: 00000000 00000000 00000000 00000000    ................
    01c000c0: 00000000 00000000 00000000 00000000    ................
    01c000d0: 00000000 00000000 00000000 00000000    ................
    01c000e0: 00000000 00000000 00000000 00000000    ................
    01c000f0: 00000000 00000000 00000000 00000000    ................
    
[/code]
### All to 0
mw 0x01c00000 0x00 0x40  
md 0x01c00000 0x40 
[code] 
    01c00000: 00000000 00000000 00000000 00000000    ................
    01c00010: 00000000 00000200 00000000 00000000    ................
    01c00020: 00000000 00000100 00000000 00000000    ................
    01c00030: 00000000 00000000 00000000 00000000    ................
    01c00040: 00000000 00000000 00000000 00000000    ................
    01c00050: 00000000 00000000 00000000 00000000    ................
    01c00060: 00000000 00000000 00000000 00000000    ................
    01c00070: 00000000 00000000 00000000 00000000    ................
    01c00080: 00000000 00000000 00000000 00000000    ................
    01c00090: 00000000 00000000 00000000 00000000    ................
    01c000a0: 00000000 00000000 00000000 00000000    ................
    01c000b0: 00000000 00000000 00000000 00000000    ................
    01c000c0: 00000000 00000000 00000000 00000000    ................
    01c000d0: 00000000 00000000 00000000 00000000    ................
    01c000e0: 00000000 00000000 00000000 00000000    ................
    01c000f0: 00000000 00000000 00000000 00000000    ................
    
[/code]
