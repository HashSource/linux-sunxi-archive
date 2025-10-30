# FES
FES is a low-level USB interface used by LiveSuit to flash firmware to the device. It works on top of [FEL][19084]. Thus you must activate FEL mode first, then you can enter FES mode using FEL commands. 
## Contents
  * [1 Implementations][19085]
  * [2 Booting to FES][19086]
    * [2.1 Boot 2.0][19087]
    * [2.2 Boot 1.0][19088]
  * [3 Requests][19089]
  * [4 Banner][19090]

## Implementations
The FEL protocol is consistent in implementation, however the same cannot be said about FES protocol. There are two versions of the protocol, the newer one has more commands available and it's easier to switch device into FES. Allwinner uses "boot1.0" and "boot2.0" in their SDK to specify FES protocol version. The 2.0 version for the first time appeared in late 2013 along with Android 4.4 SDK release, and it's used on most devices sold with Android 4.4+. 
## Booting to FES
You can use `sunxi-fel` tool from [Sunxi-tools][19091] to boot to FES, or [FELix][19092] which has a dedicated command for that. 
### Boot 2.0
  1. You need two files from LiveSuit image: fes1.fex and u-boot.fex
  2. Write fes1.fex at 0x2000
  3. Execute code at 0x2000. If everything goes well you can access device's DRAM
  4. Write u-boot.fex at 0x4a000000 (sunxi's [u-boot][19093] doesn't have implemented FES protocol)
  5. Set work mode of u-boot to USB mode: Write 0x10 at 0x4a0000e0
  6. Execute code at 0x4a000000

### Boot 1.0
More universal, as DRAM config isn't precompiled into binaries. But it's more difficult to enter manually, because you have to recreate DRAM config. 
  1. You need four files from LiveSuit image: fes_1-1.fex, fes_1-2.fex, fes.fex, fes_2.fex
  2. Write DRAM config at 0x7010 (180(sun4i and older) or 512 bytes (sun6i+))
  3. Write fes_1-1.fex at 0x7210
  4. Execute code at 0x7220
  5. Write fes_1-2.fex at 0x2000
  6. Execute code at 0x2000
  7. Write fes.fex at 0x40200000
  8. Write fes_2.fex at 0x7220
  9. Execute code at 0x7220

Structure of DRAM config (sun4i): 
[code] 
      uint32le :unk1, :initial_value => 0x2000000               # 0x00
      uint32le :unk2, :initial_value => 0x2000000               # 0x04
      uint32le :unk3, :initial_value => 0x2000100               # 0x08
      uint32le :unk4, :initial_value => 128                     # 0x0C
      uint32le :unk5                                            # 0x10
      uint32le :unk6                                            # 0x14
      uint32le :uart_debug_tx, :initial_value => 0x7C4AC1       # 0x18
      uint32le :uart_debug_port, :inital_value => 0             # 0x1C
      array    :unk7, :type => :uint32le, :initial_length => 15 # 0x20
      uint32le :dram_baseaddr, :initial_value => 0x40000000     # 0x5C
      uint32le :dram_clk, :initial_value => 408                 # 0x60
      uint32le :dram_type, :initial_value => 3                  # 0x64
      uint32le :dram_rank_num, :initial_value => 1              # 0x68
      uint32le :dram_chip_density, :initial_value => 4096       # 0x6C
      uint32le :dram_io_width, :initial_value => 16             # 0x70
      uint32le :dram_bus_width, :initial_value => 32            # 0x74
      uint32le :dram_cas, :initial_value => 6                   # 0x78
      uint32le :dram_zq, :initial_value => 0x7F                 # 0x7C
      uint32le :dram_odt_en                                     # 0x80
      uint32le :dram_size, :initial_value => 1024               # 0x84
      uint32le :dram_tpr0, :initial_value => 0x30926692         # 0x88
      uint32le :dram_tpr1, :initial_value => 0x1090             # 0x8C
      uint32le :dram_tpr2, :initial_value => 0x1A0C8            # 0x90
      uint32le :dram_tpr3                                       # 0x94
      uint32le :dram_tpr4                                       # 0x98
      uint32le :dram_tpr5                                       # 0x9C
      uint32le :dram_emr1, :initial_value => 4                  # 0xA0
      uint32le :dram_emr2                                       # 0xA4
      uint32le :dram_emr3                                       # 0xA8
      array    :unk8, :type => :uint32le, :initial_length => 2  # 0xAC
    
[/code]
Structure of DRAM config (sun6i) 
[code] 
      array    :unknown, :type => :uint8, :initial_length => 24     # 0x00
      uint32le :uart_debug_tx, :initial_value => 0x7C4A87           # 0x18
      uint32le :uart_debug_port, :inital_value => 0                 # 0x1C
      uint32le :dram_clk, :initial_value => 240                     # 0x20
      uint32le :dram_type, :initial_value => 3                      # 0x24
      uint32le :dram_zq, :initial_value => 0xBB                     # 0x28
      uint32le :dram_odt_en, :initial_value => 0                    # 0x2C
      uint32le :dram_para1, :initial_value => 0x10F40400            # 0x30, &=0xffff => DRAM size (1024)
      uint32le :dram_para2, :initial_value => 0x1211                # 0x34
      uint32le :dram_mr0, :initial_value => 0x1A50                  # 0x38
      uint32le :dram_mr1, :initial_value => 0                       # 0x3C
      uint32le :dram_mr2, :initial_value => 24                      # 0x40
      uint32le :dram_mr3, :initial_value => 0                       # 0x44
      uint32le :dram_tpr0, :initial_value => 0                      # 0x48
      uint32le :dram_tpr1, :initial_value => 0x80000800             # 0x4C
      uint32le :dram_tpr2, :initial_value => 0x46270140             # 0x50
      uint32le :dram_tpr3, :initial_value => 0xA0C4284C             # 0x54
      uint32le :dram_tpr4, :initial_value => 0x39C8C209             # 0x58
      uint32le :dram_tpr5, :initial_value => 0x694552AD             # 0x5C
      uint32le :dram_tpr6, :initial_value => 0x3002C4A0             # 0x60
      uint32le :dram_tpr7, :initial_value => 0x2AAF9B               # 0x64
      uint32le :dram_tpr8, :initial_value => 0x604111D              # 0x68
      uint32le :dram_tpr9, :initial_value => 0x42DA072              # 0x6C
      uint32le :dram_tpr10, :initial_value => 0                     # 0x70
      uint32le :dram_tpr11, :initial_value => 0                     # 0x74
      uint32le :dram_tpr12, :initial_value => 0                     # 0x78
      uint32le :dram_tpr13, :initial_value => 0                     # 0x7C
      uint32le :dram_size, :initial_value => (1024 << 20)           # 0x80,  1024 MB
      array    :reserved, :type => :uint32le, :initial_length => 95 # 0x84
    
[/code]
  

## Requests
Command  | Hex code  | Description  | Sent/received   
---|---|---|---  
FES_TRANSMITE  | 0x201  | Read or write data  |   
FES_RUN  | 0x202  | Execute code at address  | No data   
FES_INFO  | 0x203  |  | Received (16 bytes) 
[code]
    00000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  |................|
    00000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  |................|
[/code]  
FES_GET_MSG  | 0x204  |  |   
FES_UNREG_FED  | 0x205  |  |   
FES_DOWNLOAD  | 0x206  | Write data to the device (boot 2.0+)  |   
FES_UPLOAD  | 0x207  | Read data from the device (boot 2.0+)  |   
FES_VERIFY  | 0x208  | Do the same as FES_VERIFY_VALUE and FES_VERIFY_STATUS (boot 2.0+). Unimplemented on most devices  |   
FES_QUERY_STORAGE  | 0x209  | Check if device is booted from NAND or SDCard (boot 2.0+)  | 
[code]
    00000000  00 00 00 00   |....|
[/code]  
FES_FLASH_SET_ON  | 0x20A  | Enable access to NAND Flash / SD card (executes sunxi_sprite_init(0)) (boot 2.0+)  | No data   
FES_FLASH_SET_OFF  | 0x20B  | Disable access to NAND Flash / SD card (executes sunxi_sprite_exit(1)) (boot 2.0+)  | No data   
FES_VERIFY_VALUE  | 0x20C  | Check checksum of given memory block  |   
FES_VERIFY_STATUS  | 0x20D  | Check last operation result  |   
FES_FLASH_SIZE_PROBE  | 0x20E  | Get capacity of storage (boot 2.0+)  |   
FES_TOOL_MODE  | 0x20F  | Set u-boot work mode (boot 2.0+). Can be used to reboot device  |   
FES_MEMSET  | 0x210  | Fill memory block with a byte value (boot 2.0+)  |   
FES_PMU  | 0x211  | Change PMU configuration (boot 2.0+)  | Send following struct ` struct pmu_config_t { char pmu_type[16]; char vol_name[16]; u32 voltage; u32 gate; }; `  
Receive return code of axp_set_supply_status_byname(pmu_config.pmu_type, pmu_config.vol_name, pmu_config.voltage, pmu_config.gate)   
FES_UNSEQMEM_READ  | 0x212  | Direct read memory (boot 2.0+)  | Send struct after request `unseq_mem_config { u32 addr; u32 value; }; `  
FES_UNSEQMEM_WRITE  | 0x213  | Direct write memory (boot 2.0+)  | Send struct after request `unseq_mem_config { u32 addr; u32 value; }; `  
## Banner
FES mode has a nice ASCII banner printed out on uart (boot 1.0 only) 
[code] 
    [FES]:=================================================================================================
    [FES]:=                                                                                               =
    [FES]:=                                         EEMMMMMMLL                                            =
    [FES]:=                                     ::MMMHOLIGANEE                                            =
    [FES]:=                                   ::MM.                                                       =
    [FES]:=                                   MMFF                                                        =
    [FES]:=                                 FFMM                                                          =
    [FES]:=                                MMMM                                                           =
    [FES]:=                              ..MMFF                                                           =
    [FES]:=                              EEMM.                                           FFMMMM           =
    [FES]:=          . MMMMMMMM    MMMMMMMMMMMMMMMMMM      FFMMMMMM::      ::MMMM      BBMMMMFF           =
    [FES]:=        ::MM  . MMMM          MMMM            MM.   MMMMMM    EE..EEMM::  EE::                 =
    [FES]:=        MM      MMMM        ::MMLL          EEMM    MMMMFF  .       MMMM::::                   =
    [FES]:=      MMMM    FFMMI         BBMM            MMI     MMMM            MMMMEE                     =
    [FES]:=      MMMM  . MM::          MMMM          MMMM    BBMM              MMMM                       =
    [FES]:=    BBMMFF::EE              MMMM          MMMM  MM::                BBMM..                     =
    [FES]:=    MMMMEE                I MMI         I MMMM::                  ::FFMMFF                     =
    [FES]:=    MMMM          LL      MMMM          EEMMMM        LL          BB  MMMM                     =
    [FES]:=    MMMM      I MM        MMMM          MMMMMM      MM::        MM    MMMM                     =
    [FES]:=    MMMMMMMMMMEE          MMMM          .GUANLI@HUANG.   BB    BB      FFMM.                   =
    [FES]:=      MMMMMM..          I MMI             MMMMMMEE      MMMMMM          MMEE                   =
    [FES]:=                        MMMM                                            MMMM                   =
    [FES]:=                        MMMM                                            ::MM::                 =
    [FES]:=                        MM                                                BBMM        MM       =
    [FES]:=                      EEBB                                                  BBMM..  MMMM       =
    [FES]:=                      MM                                                      ..EEMMFF         =
    [FES]:=          MMMMMMMMMMMM                                                                         =
    [FES]:=          MMMMMMMMI                                                                            =
    [FES]:=                                                                                               =
    [FES]:=================================================================================================
    
[/code]
