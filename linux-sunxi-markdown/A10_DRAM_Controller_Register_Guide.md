# A10 DRAM Controller Register Guide
Note: slightly different revisions of the same DRAM controller are used in sun4i (Allwinner [A10][1548]), sun5i (Allwinner [A13][1549]) and sun7i (Allwinner [A20][1550]). This register guide covers them all. And the differences are explained in the register descriptions where appropriate. 
  
DRAMC Base Address: 0x01c01000 
# DRAM Controller registers
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[SDR_CCR][1551]` | `0x0000` | `4B` | ` `  
`[SDR_DCR][1552]` | `0x0004` | `4B` | ` `  
`[SDR_IOCR][1553]` | `0x0008` | `4B` | ` `  
`[SDR_CSR][1554]` | `0x000c` | `4B` | ` Data Training Status register`  
`[SDR_DRR][1555]` | `0x0010` | `4B` | ` Refresh Ratio`  
`[SDR_TPR0][1556]` | `0x0014` | `4B` | ` Timing parameters 0`  
`[SDR_TPR1][1557]` | `0x0018` | `4B` | ` Timing parameters 1`  
`[SDR_TPR2][1558]` | `0x001c` | `4B` | ` Timing parameteres 2`  
`[SDR_RSLR0][1559]` | `0x004c` | `4B` | ` DQS Gating System Latency for Rank 0`  
`[SDR_RSLR1][1559]` | `0x0050` | `4B` | ` DQS Gating System Latency for Rank 1`  
`[SDR_RDGR0][1560]` | `0x005c` | `4B` | ` DQS Gating Phase Select for Rank 0`  
`[SDR_RDGR1][1560]` | `0x0060` | `4B` | ` DQS Gating Phase Select for Rank 1`  
`[SDR_ODTCR][1561]` | `0x0098` | `4B` | `ODT Configuration Register `  
`[SDR_DTR0][1562]` | `0x009c` | `4B` | ` Data Training Data register 0 `  
`[SDR_DTR1][1563]` | `0x00a0` | `4B` | ` Data Training Data register 1`  
`[SDR_DTAR][1564]` | `0x00a4` | `4B` | ` Data Training Addres Register`  
`[SDR_ZQCR0][1565]` | `0x00a8` | `4B` | ` ZQ impedance control register`  
`[SDR_ZQCR1][1566]` | `0x00ac` | `4B` | ` `  
`[SDR_ZQSR][1567]` | `0x00b0` | `4B` | ` ZQ impedance status register`  
`[SDR_IDCR][1568]` | `0x00b4` | `4B` | ` Initialization Delay Configuration Register`  
`[SDR_MR][1569]` | `0x01f0` | `4B` | ` Mode Register`  
`[SDR_EMR][1570]` | `0x01f4` | `4B` | ` Extended mode register`  
`[SDR_EMR2][1571]` | `0x01f8` | `4B` | ` Extended mode register 2`  
`[SDR_EMR3][1572]` | `0x01fc` | `4B` | ` Extended mode register 3 `  
`[SDR_DLLGCR][1573]` | `0x0200` | `4B` | ` DLL General Control Register`  
`[SDR_DLLCR0][1574]` | `0x0204` | `4B` | ` DLL Control Register (Command lane)`  
`[SDR_DLLCR1][1574]` | `0x0208` | `4B` | ` DLL Control Register (Byte lane 0)`  
`[SDR_DLLCR2][1574]` | `0x020c` | `4B` | ` DLL Control Register (Byte lane 1)`  
`[SDR_DLLCR3][1574]` | `0x0210` | `4B` | ` DLL Control Register (Byte lane 2)`  
`[SDR_DLLCR4][1574]` | `0x0214` | `4B` | ` DLL Control Register (Byte lane 3)`  
`[SDR_DQTR0][1575]` | `0x0218` | `4B` | ` DQ Timing Register 0`  
`[SDR_DQTR1][1576]` | `0x021c` | `4B` | ` DQ Timing Register 1`  
`[SDR_DQTR2][1577]` | `0x0220` | `4B` | ` DQ Timing Register 2`  
`[SDR_DQTR3][1578]` | `0x0224` | `4B` | ` DQ Timing Register 3`  
`[SDR_DQSTR0][1579]` | `0x0228` | `4B` | ` `  
`[SDR_DQSTR1][1580]` | `0x022c` | `4B` | ` `  
`[SDR_CR][1581]` | `0x0230` | `4B` | ` `  
`[SDR_CFSR][1582]` | `0x0234` | `4B` | ` `  
`[SDR_DPCR][1583]` | `0x023c` | `4B` | ` Power Save Control Register `  
`[SDR_APR][1584]` | `0x0240` | `4B` | ` Arbiter Period Register`  
`[SDR_TLR][1585]` | `0x0244` | `4B` | ` Priority Level Data Threshold Register`  
`[SDR_HPCR][1586]` | `0x0250` | `4B` | ` Host port configuration register `  
`[SDR_SCSR][1587]` | `0x02e0` | `4B` | ` Controller select magic `  
## SDR_CCR
Default value: 0x80020000(A10) / 0x90020000(A20)  
Offset: 0x0000 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCR_DRAM_INIT` | `31` | `Read/Write` | `` | `0/1` | Set to 1 to init DRAM chip; cleared on completion   
`CCR_DATA_TRAINING` | `30` | `Read/Write` | `` | `` | Set to 1 to start data traning; cleared on completion   
`CCR_IB` | `29` | `Read/Write` | `0x0` | `` | _unknown, fixed at 0_  
`CCR_ITM_DISABLE` | `28` | `Read/Write` | `` | `0/1` | Set to 1 to disable Interface Timing Module   
`CCR_FLUSH` | `27` | `Read/Write` | `` | `0/1` | Flush controller; cleared on completion   
`` | `26:18` | `Read/Write` | `` | `0/1` | _reserved_  
`CCR_DQS_DRIFT_COMP` | `17` | `Read/Write` | `0x1` | `` | DQS Drift Compensation   
`CCR_DQS_DRIFT_LIMIT` | `16:15` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = no limit
    0x1 = 90°
    0x2 = 180°
    0x3 = 270°
    
[/code]
| DQS Drift limit, only sets error flag   
`CCR_DQS_GATE` | `14` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = active window mode
    0x1 = passive window mode
    
[/code]
| DQS gate window mode   
`CCR_RBB` | `13` | `Read/Write` | `0` | `` | _unknown, rk29_  
`` | `12:6` | `Read/Write` | `0` | `` | _reserved/unknown_  
`CCR_CMD_RATE` | `5` | `Read/Write` | `0` | `
[code] 
    0x0 = 2T
    0x1 = 1T
    
[/code]
` | Command rate. Setting 1T is only supported on sun7i hardware and slightly reduces latency. Has no effect on sun4i/sun5i.   
`` | `4:0` | `Read/Write` | `0` | `` | _unknown, rk29 has ECC and hostport enable there_  
## SDR_DCR
Default value: 0x000004d4(A10) / 0x00000454(A20)  
Offset: 0x0004 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`DCR_CMD_EXEC` | `31` | `Read/Write` | `0x0` | `` | Write 0x1 to execute command, cleared on finish   
`DCR_CMD` | `30:27` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = NOP
    0x1 = Clock stop (???)
    0x2 = Self Refresh
    0x3 = Refresh
    0x4 = DDR3 reset (???)
    0x5 = Precharge all
    0x6 = Deep power down (???)
    0x7 = SDRAM mode exit
    0x8-0xa = _reserved_
    0xb = SDRAM ZQ calibration short
    0xc = SDRAM ZQ calibration long
    0xd = _reserved_
    0xe = Power down
    0xf = SDRAM NOP
    
[/code]
| Command (list not verified!)   
`DCR_CUR_RANK` | `26:25` | `Read/Write` | `0x0` | `` | Current rank for command   
`` | `24:19` | `Read/Write` | `0x0` | `` | _reserved_ (MVAR, RDIMM, DO_INIT on rk29)?   
`` | `18` | `Read/Write` | `0x0` | `` | _unknown_ MPRDQ?   
`` | `17:15` | `Read/Write` | `0x0` | `` | _unknown_ PDQ?   
`DCR_INTERLEAVE` | `14:13` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = sequential
    0x1 = bank interleaving
    0x2 = rank interleaving
    0x3 = fixed address (???)
    
[/code]
| Interleaving mode   
`DCR_RANK_ALL` | `12` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = only rank DCR_CUR_RANK
    0x1 = all ranks
    
[/code]
| Send command to all ranks   
`DCR_RANK_NUM` | `11:10` | `Read/Write` | `0x1` | ` `
[code]
    rank num = this value + 1
    
[/code]
| Number of Ranks   
`` | `9` | `Read/Write` | `0x0` | `` | _unknown_ PIO?   
`DCR_BUS_WIDTH` | `8:6` | `Read/Write` | `0x1/0x3` | `
[code] 
    0x0 = _unknown_
    0x1 = 16 bit
    0x2 = _unknown_
    0x3 = 32 bit
    ... = _reserved ???_
    
[/code]
``` | Bus width (also called SIO in some sources)   
`DCR_DENSITY` | `5:3` | `Read/Write` | `0x2` | ` `
[code]
    0x0 = 256M
    0x1 = 512M
    0x2 = 1G
    0x3 = 2G
    0x4 = 4G
    0x5 = 8G
    ... = _reserved_
    
[/code]
| DRAM chip density   
`DCR_IO_WIDTH` | `2:1` | `Read/Write` | `0x2` | ` `
[code]
    0x0 = x4 (???)
    0x1 = x8
    0x2 = x16
    0x3 = _reserved_
    
[/code]
| DRAM chip IO width   
`DCR_TYPE` | `0` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = DDR2
    0x1 = DDR3
    
[/code]
| DRAM type   
## SDR_IOCR
Default value: 0x00000000  
Offset: 0x0008 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`IOCR_DQS_RTT` | `31` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = always
    0x1 = dynamic
    
[/code]
| DQS dynamic RTT control   
`IOCR_DQ_RTT` | `30` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = always
    0x1 = dynamic
    
[/code]
| DQ dynamic RTT control   
`IOCR_RTTOE` | `29` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = 2 + max(RSLR)
    0x1 = 2 + max(RSLR) + CL + AL
    
[/code]
| RTT output enable cycles before read _(unverified)_  
`IOCR_RTTOH` | `28:26` | `Read/Write` | `0x0` | ` `
[code]
    RTTOH cycles = this value + 1
    
[/code]
| RTT output hold cycles after read _(unverified)_  
`` | `25:24` | `Read/Write` | `0x0` | `` | _reserved_  
`IOCR_AUTO_DATA_IOPD` | `23:22` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = disabled
    0x1 = only in self-refresh state
    0x2 = only in power-down state
    0x3 = in self-refresh and power-down state
    
[/code]
| Automatic data channel IO power-down   
`IOCR_AUTO_DATA_OE` | `21:20` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = disabled
    0x1 = only in self-refresh state
    0x2 = only in power-down state
    0x3 = in self-refresh and power-down state
    
[/code]
| Automatic data channel output enable _(unverified)_  
`IOCR_AUTO_CMD_IOPD` | `19:18` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = disabled
    0x1 = only in self-refresh state
    0x2 = only in power-down state
    0x3 = in self-refresh and power-down state
    
[/code]
| Automatic command channel IO power-down   
`IOCR_AUTO_CMD_OE` | `17:16` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = disabled
    0x1 = only in self-refresh state
    0x2 = only in power-down state
    0x3 = in self-refresh and power-down state
    
[/code]
| Automatic command channel output enable _(unverified)_  
`` | `15:11` | `Read/Write` | `0x0` | `` | _reserved/unknown_  
`IOCR_CK_DS` | `10` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = reduced
    0x1 = full
    
[/code]
| Clock drive strength _(unverified, taken from rk29)_  
`IOCR_ADD_DS` | `9` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = reduced
    0x1 = full
    
[/code]
| Address drive strength _(unverified, taken from rk29)_  
`IOCR_DQS_DS` | `8` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = reduced
    0x1 = full
    
[/code]
| DQS drive strength _(unverified, taken from rk29)_  
`IOCR_DQ_DS` | `7` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = reduced
    0x1 = full
    
[/code]
| DQ drive strength _(unverified, taken from rk29)_  
`IOCR_DQS_RTT` | `6:5` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = disabled
    0x1 = 150
    0x2 = 75
    0x3 = 50
    
[/code]
| DQS RTT value _(unverified, taken from rk29)_  
`IOCR_DQ_RTT` | `4:3` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = disabled
    0x1 = 150
    0x2 = 75
    0x3 = 50
    
[/code]
| DQ RTT value _(unverified, taken from rk29)_  
`IOCR_TEST_EN` | `2` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = disabled
    0x1 = enabled
    
[/code]
| Enable test signal output (???)   
`IOCR_DQS_ODT` | `1` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = DQS ODT disabled
    0x1 = DQS ODT enabled
    
[/code]
| Enable DQS on-die termination   
`IOCR_DQ_ODT` | `0` | `Read/Write` | `0x0` | ` `
[code]
    0x0 = DQ ODT disabled
    0x1 = DQ ODT enabled
    
[/code]
| Enable DQ on-die termination   
## SDR_CSR
Default value: 0x00000000  
Offset: 0x000C 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CSR_DTIERR` | `21` | `Read/Write` | `0` | `` | An indicator of a DQS gate training failure. This bit is set to 1 if more than one possible gating delay has been found (which is abnormal)   
`CSR_DTERR` | `20` | `Read/Write` | `0` | `` | An indicator of a DQS gate training failure. This bit is set to 1 if no gating delay could be found   
## SDR_DRR
Default value: 0x086c9883  
Offset: 0x0010 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`RD` | `31` | `Read/Write` | `0` | ` `
[code]
    0x0 = enabled
    0x1 = disabled
    
[/code]
| Disable auto-refresh   
`` | `30:28` | `Read/Write` | `0` | `` | _reserved_  
`RFBURST` | `27:24` | `Read/Write` | `0x8` | ` `
[code]
    burst length = this value + 1
    
[/code]
| Refresh burst length   
`tRFPRD` | `23:8` | `Read/Write` | `0x6c98` | ` `
[code]
    tRFPRD = (tREFI * dram_clock) * RFBURST - 200
    
[/code]
_\- 200 looks like some safety margin and might not be necessary_ | Refresh period   
`tRFC` | `7:0` | `Read/Write` | `0x83` | `` | Refresh cycle time   
## SDR_TPR0
Default value: 0x30926692  
Offset: 0x0014 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`tCCD` | `31` | `Read/Write` | ` 0` | ` For DDR2: 
[code] 
    0x0 = BL/2
    0x1 = BL/2 + 1
    
[/code]
For DDR3: 
[code] 
    0x0 = 4 cycles
    0x1 = 5 cycles
    
[/code]
``` | READ to READ and WRITE to WRITE command delay   
`tRC` | `30:25` | `Read/Write` | ` 0x18` | ` 2-42 valid` | ACTIVATE to ACTIVATE command delay (in the same bank)   
`tRRD` | `24:21` | `Read/Write` | ` 0x4` | ` 1-8 valid` | ACTIVATE to ACTIVATE command delay (in a different bank)   
`tRAS` | `20:16` | `Read/Write` | ` 0x12` | ` 2-31 valid` | ACTIVATE to PRECHARGE command delay   
`tRCD` | `15:12` | `Read/Write` | ` 0x6` | ` ` | ACTIVATE to READ/WRITE command delay   
`tRP` | `11:8` | `Read/Write` | ` 0x6` | ` ` | PRECHARGE to ACTIVATE/REFRESH command delay   
`tWTR` | `7:5` | `Read/Write` | ` 0x3` | ` 1-6 valid` | WRITE to READ command delay   
`tRTP` | `4:2` | `Read/Write` | ` 0x3` | ` 2-6 valid` | READ to PRECHARGE command delay   
`tMRD` | `1:0` | `Read/Write` | ` 0x2` | ` For DDR3: 
[code] 
    0x0 = 4 cycles
    0x1 = 5 cycles
    0x2 = 6 cycles
    0x3 = 7 cycles
    
[/code]
``` | MODE REGISTER SET to MODE REGISTER SET command delay   
## SDR_TPR1
Default value: 0x00001090  
Offset: 0x0018 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TP` | `31` | `Read/Write` | `0x0` | `` | _unknown_ (the bitfield name originates from the Chinese BWDSP100 manual)   
`XWR` | `30:27` | `Read/Write` | `0x0` | `` | _unknown_ (the bitfield name originates from the Chinese BWDSP100 manual)   
`XCL` | `24:23` | `Read/Write` | `0x0` | `` | _unknown_ (the bitfield name originates from the Chinese BWDSP100 manual)   
`` | `22:16` | `Read only` | `0x0` | `` | _reserved_  
`tRNKWTW` | `15:14` | `Read/Write` | `0x0` | `` | _unknown_ (maybe WRITE to WRITE delay in different ranks?)   
`tRNKRTR` | `13:12` | `Read/Write` | `0x1` | `` | _unknown_ (maybe READ to READ delay in different ranks?)   
`tRTODT` | `11` | `Read/Write` | `0x0` | `
[code] 
    0x0 = default
    0x1 = extra cycle
    
[/code]
``` | READ to ODT delay   
`tMOD` | `10:9` | `Read/Write` | `0x0` | ` For DDR3: 
[code] 
    0x0 = 12 cycles
    0x1 = 13 cycles
    0x2 = 14 cycles
    0x3 = 15 cycles
    
[/code]
``` | MODE REGISTER SET to any other command delay   
`tFAW` | `8:3` | `Read/Write` | `0x12` | ` 2-31 valid` | Four ACTIVATE commands period. No more than four ACTIVATE commands can be issued in a window of this duration.   
`tRTW` | `2` | `Read/Write` | `0x0` | `
[code] 
    0x0 = default
    0x1 = extra cycle
    
[/code]
``` | READ to WRITE command delay. The TI Keystone2 manual hints that it might be only used during initialization/leveling (but not for normal operations). And recommends to set it to 1.   
`tAOND_tAOFD` | `1:0` | `Read/Write` | `0x0` | `` | _DDR2 only_  
## SDR_TPR2
Default value: 0x0001a0c8  
Offset: 0x001c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:19` | `Read only` | `0` | `` | _reserved_  
`tCKE` | `18:15` | `Read/Write` | `0x3` | `tCKE(min) + 1nCK` | Minimum CKE low width for Self Refresh entry to exit timing   
`tXP` | `14:10` | `Read/Write` | `0x8` | `max(tXP, tXPDLL)` | Exit Power Down timing   
`tXS` | `9:0` | `Read/Write` | `0xC8` | `max(tXS, tXSDLL)` | Exit Self Refresh timing   
## SDR_RSLRn
Default value: 0x00000000  
Offset: 0x004c (SDR_RSLR0) / 0x0050 (SDR_RSLR1) 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `11:9` | `Read/Write` | `0` | `` | Lane 3 DQS gating system latency, cycles   
`` | `8:6` | `Read/Write` | `0` | `` | Lane 2 DQS gating system latency, cycles   
`` | `5:3` | `Read/Write` | `0` | `` | Lane 1 DQS gating system latency, cycles   
`` | `2:0` | `Read/Write` | `0` | `` | Lane 0 DQS gating system latency, cycles   
## SDR_RDGRn
Default value: 0x00000055  
Offset: 0x005c (SDR_RDGR0) / 0x0060 (SDR_RDGR1) 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `7:6` | `Read/Write` | `1` | `
[code] 
    0 = 90 degrees
    1 = 180 degrees
    2 = 270 degrees
    3 = 360 degrees
    
[/code]
``` | Lane 3 DQS gating phase select   
`` | `5:4` | `Read/Write` | `1` | `
[code] 
    0 = 90 degrees
    1 = 180 degrees
    2 = 270 degrees
    3 = 360 degrees
    
[/code]
``` | Lane 2 DQS gating phase select   
`` | `3:2` | `Read/Write` | `1` | `
[code] 
    0 = 90 degrees
    1 = 180 degrees
    2 = 270 degrees
    3 = 360 degrees
    
[/code]
``` | Lane 1 DQS gating phase select   
`` | `1:0` | `Read/Write` | `1` | `
[code] 
    0 = 90 degrees
    1 = 180 degrees
    2 = 270 degrees
    3 = 360 degrees
    
[/code]
``` | Lane 0 DQS gating phase select   
## SDR_ZQCR0
Default value: 0x07b00000  
Offset: 0x00a8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`ZCAL` | `31` | `Read/Write` | `0` | `` | ZQ calibration trigger. Writing 1 to this bit initiates the ZQ calibration. This bit is self clearing on sun7i, but not on sun5i. The calibration makes use of the two divisors from ZPROG bits and the external high precision 240 ohm resistor to find the matching correct ZCTRL/ZDATA settings for the internal on-die resistors.   
`ZDEN` | `28` | `Read/Write` | `0` | `` | If this bit is set to 1, then the user supplied data from the ZDATA bits is used instead of doing actual calibration.   
`ZPROG` | `27-20` | `Read/Write` | `0x7b` | `
[code] 
    bits 27:24 = On-die termination divisor
    bits 23:20 = Output impedance divisor
    
[/code]
``` | Divisors for the external 240 ohm high precision reference resistor connected to the SoC.   
`ZDATA` | `19:0` | `Read/Write` | `0` | ` `
[code]
    bits 19:15 = pull-up on-die termination impedance
    bits 14:10 = pull-down on-die termination impedance
    bits 9:5   = pull-up output impedance
    bits 4:0   = pull-down output impedance
    
[/code]
| The user supplied impedance settings, which are taken into use and copied to ZCTRL if the ZDEN bit is set   
## SDR_ZQCR1
Default value: 0x00000000  
Offset: 0x00ac 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`unknown` | `31:28` | `Read/Write` | `0` | `` | unknown   
`unknown` | `27:24` | `Write only?` | `0` | `` | Unless bit 24 is set, the sun7i hardware fails to boot with ZQ calibration and ODT enabled. These bits always read back as 0, so this looks like some sort of a write-only register part.   
`CALPRD?` | `23:0` | `Read/Write` | `0` | `` | unknown   
## SDR_ZQSR
Default value: ?  
Offset: 0x00b0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`ZDONE` | `31` | `Read only` | `0` | ` `
[code]
    0 = ZQ calibration is still in progress or has never run
    1 = ZQ calibration has completed
    
[/code]
| ZQ calibration progress status   
`ZCTRL` | `19:0` | `Read only` | `?` | ` `
[code]
    bits 19:15 = pull-up on-die termination impedance
    bits 14:10 = pull-down on-die termination impedance
    bits 9:5   = pull-up output impedance
    bits 4:0   = pull-down output impedance
    
[/code]
| The current impedance settings   
## SDR_IDCR
Example of [use in boot0][1588]  
Default value: 0x00c80064  
Offset: 0x00b4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:30` | `Read only` | `0` | `` | _reserved_  
`tDINIT1?` | `29:17` | `Read/Write` | `0x64` | `` | unknown   
`tDINIT0` | `16:0` | `Read/Write` | `0x64` | `` | CKE low time during DRAM initialization. Is measured in DRAM clock cycles, which are additionally multiplied by 2 for sun4i/sun5i or 3 for sun7i to get the actual delay. The DDR3 spec requires to wait for at least 500 us   
## SDR_DLLCRn
Default value: 0xc0000000  
Offset: 0x0204 (SDR_DLLCR0) / 0x0208 (SDR_DLLCR1) / 0x020C (SDR_DLLCR2) / 0x0210 (SDR_DLLCR3) / 0x0214 (SDR_DLLCR4) 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`DLLCR_DISABLE` | `31` | `Read/Write` | `1` | `` | DLL disable   
`DLLCR_NRESET` | `30` | `Read/Write` | `1` | `` | DLL reset   
`DLLCR_SDPHASE` | `17:14` | `Read/Write` | `0` | ` `
[code]
    0x0 =  90 degrees
    0x1 =  72 degrees
    0x2 =  54 degrees
    0x3 =  36 degrees
    0x4 = 108 degrees
    0x5 =  90 degrees
    0x6 =  72 degrees
    0x7 =  54 degrees
    0x8 = 126 degrees
    0x9 = 108 degrees
    0xa =  90 degrees
    0xb =  72 degrees
    0xc = 144 degrees
    0xd = 126 degrees
    0xe = 108 degrees
    0xf =  90 degrees
    
[/code]
|   
`DLLCR_MFWDLY` | `11:9` | `Read/Write` | `0` | `` |   
`DLLCR_MFBDLY` | `8:6` | `Read/Write` | `0` | `` |   
## SDR_DPCR
Default value: 0x00000000  
Offset: 0x023c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`DPCR_MAGIC` | `31:16` | `Write-only` | `0` | `` | Any attempts to write to the SDR_DPCR register are ignored unless these high 16 bites are set to the 0x1651 magic value on sun7i. Writes to SDR_DPCR are always allowed on sun5i and it has no special magic value. These bits always read back as 0.   
`` | `15:1` | `Read-only?` | `0` | `` | reserved?   
`` | `0` | `Read/Write` | `0` | ` `
[code]
    0 - Normal mode
    1 - DRAM pad is on hold and the SoC is ready to power down,
        while DRAM may remain in self-refresh mode and retain data
    
[/code]
| On sun5i and sun7i hardware this bit can (or must?) be set to 1 after putting DRAM in self-refresh mode. Likewise, it needs to be set back to 0 when returning from the self-refresh mode. The value of this register is apparently backed by the battery and survives reboots.   
## SDR_HPCR
Default value: ??  
Offset: 0x250+4*port 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`RdCntEn` | `31` | `Read/Write?` | `?` | `` | Host port read counter enable   
`WrCntEn` | `30` | `Read/Write?` | `` | `` | Host port write counter enable   
`` | `29:16` | `Read only?` | `` | `` | _reserved_  
`CmdNum` | `15:8` | `Read/Write?` | `` | `` | Host port command number   
`WaitState` | `7:4` | `Read/Write?` | `` | `` | Host port wait state   
`PrioLevel` | `3:2` | `Read/Write?` | `` | `` | Host port priority level   
`` | `1` | `Read only?` | `` | `` | _reserved_ \- setting this bit seems to raise priority on sun5i   
`AcsEn` | `0` | `Read/Write?` | `` | `` | Host port access enabled   
Ports (verify me!): 
  * 04 (0x260): usb0 host port
  * 05 (0x264): usb1 host port
  * 16 (0x290): cpu host port
  * 20 (0x2a0): csi0 host port
  * 27 (0x2bc): csi1 host port (verified)

# Register dumps
## A10
### Reset
before controller select magic  | after controller select magic   
---|---
[code] 
    0000: 000329c4 33058a69 14140f54 07103065 
    0010: 372c0c30 000000c7 00000000 88442211 
    0020: 00000000 00000000 00001111 00001111 
    0030: 00000000 00000000 00000000 00000000 
    0040: 00000000 00000000 00000000 00000000 
    0050: 00000000 00000000 00000000 00000000 
    0060: 00330012 00000300 00000000 07b00000 
    0070: 00000000 00000000 00000210 00000000 
    0080: 00000000 00000000 00000000 00000000 
    0090: 00000000 00000000 00000000 00000000 
    00a0: 00000000 00000000 00000000 00000000 
    00b0: 00000000 00000000 00000000 00000000 
    00c0: 00000000 00000000 00000000 00000000 
    00d0: 00000000 00000000 00000000 00000000 
    00e0: 00000000 00000000 00000000 00000000 
    00f0: 00000000 00000000 00000000 00000000 
    0100: 00000000 00000000 00000000 00000000 
    0110: 00000000 00000000 00000000 00000000 
    0120: 00000000 00000000 00000000 00000000 
    0130: 00000000 00000000 00000000 00000000 
    0140: 00000000 00000000 00000000 00000000 
    0150: 00000000 00000000 00000000 00000000 
    0160: 00000000 00000000 00000000 00000000 
    0170: 00000000 00000000 00000000 00000000 
    0180: 00000000 00000000 00000000 00000000 
    0190: 00000000 00000000 00000000 00000000 
    01a0: 00000000 00000000 00000000 00000000 
    01b0: 00000000 00000000 00000000 00000000 
    01c0: 00000000 00000000 00000000 00000000 
    01d0: 00000000 00000000 00000000 00000000 
    01e0: 00000000 00000000 00000000 00000000 
    01f0: 00000000 00000000 00000000 00000000 
    0200: 03737000 c0000000 c0000000 c0000000 
    0210: c0000000 c0000000 ffffffff ffffffff 
    0220: ffffffff ffffffff 00003333 00003333 
    0230: 00000000 000000ff 00000000 00000000 
    0240: 00008000 00010400 00000000 00000000 
    0250: 00000001 00000001 00000001 00000001 
    0260: 00000001 00000001 00000000 00000000 
    0270: 00000000 00000000 00000000 00000000 
    0280: 00000000 00000000 00000000 00000000 
    0290: 00000001 00000001 00000001 00000001 
    02a0: 00000001 00000001 00000001 00000001 
    02b0: 00000001 00000001 00000001 00000001 
    02c0: 00000001 00000001 00000000 00000001 
    02d0: 00000000 00000000 00000000 00000000 
    02e0: 00000000 00000000 00000000 00000000 
    02f0: 00000000 00000000 00000000 00000000 
    
[/code]  
| 
[code] 
    0000: 80020000 000004d4 00000000 00000000 
    0010: 086c9883 3092666e 00001090 0001a0c8 
    0020: 00000000 00000000 00000000 00000000 
    0030: 00000000 00000000 00000000 00000000 
    0040: 00000000 00000000 00000000 00000000 
    0050: 00000000 00000000 00000000 00000055 
    0060: 00000055 00000000 00000000 00000000 
    0070: 00000000 00000000 00000000 00000000 
    0080: 00000000 00000000 00000000 00000000 
    0090: 00000000 00000000 00210000 dd22ee11 
    00a0: 7788bb44 00000000 07b00000 00000000 
    00b0: 00000000 00c80064 00000000 00000000 
    00c0: 00000000 00000000 00000000 00000000 
    00d0: 00000000 00000000 00000000 00000000 
    00e0: 00000000 00000000 00000000 00000000 
    00f0: 00000000 00000000 00000000 00000000 
    0100: 00000000 00000000 00000000 00000000 
    0110: 00000000 00000000 00000000 00000000 
    0120: 00000000 00000000 00000000 00000000 
    0130: 00000000 00000000 00000000 00000000 
    0140: 00000000 00000000 00000000 00000000 
    0150: 00000000 00000000 00000000 00000000 
    0160: 00000000 00000000 00000000 00000000 
    0170: 00000000 00000000 00000000 00000000 
    0180: 00000000 00000000 00000000 00000000 
    0190: 00000000 00000000 00000000 00000000 
    01a0: 00000000 00000000 00000000 00000000 
    01b0: 00000000 00000000 00000000 00000000 
    01c0: 00000000 00000000 00000000 00000000 
    01d0: 00000000 00000000 00000000 00000000 
    01e0: 00000000 00000000 00000000 00000000 
    01f0: 00000a52 00000000 00000000 00000000 
    0200: 03737000 c0000000 c0000000 c0000000 
    0210: c0000000 c0000000 ffffffff ffffffff 
    0220: ffffffff ffffffff 00003333 00003333 
    0230: 00000000 000000ff 00000000 00000000 
    0240: 00008000 00010400 00000000 00000000 
    0250: 00000001 00000001 00000001 00000001 
    0260: 00000001 00000001 00000000 00000000 
    0270: 00000000 00000000 00000000 00000000 
    0280: 00000000 00000000 00000000 00000000 
    0290: 00000001 00000001 00000001 00000001 
    02a0: 00000001 00000001 00000001 00000001 
    02b0: 00000001 00000001 00000001 00000001 
    02c0: 00000001 00000001 00000000 00000001 
    02d0: 00000000 00000000 00000000 00000000 
    02e0: 00000000 00000000 00000000 00000000 
    02f0: 00000000 00000000 00000000 00000000 
    
[/code]  
### CB1 after boot0/1
[code] 
    01c01000: 00004000 000030e5 00cc0000 00000000    [[email protected]][1589]..........
    01c01010: 0882cf9d 30926692 00001090 0001a0c8    .....f.0........
    01c01020: 00000000 00000000 00000000 00000000    ................
    01c01030: 00000000 00000000 00000000 00000000    ................
    01c01040: 00000000 00000000 00000000 00000249    ............I...
    01c01050: 00000000 00000000 00000000 00000056    ............V...
    01c01060: 00000055 00000000 00000000 00000000    U...............
    01c01070: 00000000 00000000 00000000 00000000    ................
    01c01080: 00000000 00000000 00000000 00000000    ................
    01c01090: 00000000 00000000 00210000 dd22ee11    ..........!...".
    01c010a0: 7788bb44 00000000 07b00000 00000000    D..w............
    01c010b0: 8006b948 00c9ffff 00000000 00000000    H...............
    01c010c0: 00000000 00000000 00000000 00000000    ................
    01c010d0: 00000000 00000000 00000000 00000000    ................
    01c010e0: 00000000 00000000 00000000 00000000    ................
    01c010f0: 00000000 00000000 00000000 00000000    ................
    01c01100: 00000000 00000000 00000000 00000000    ................
    01c01110: 00000000 00000000 00000000 00000000    ................
    01c01120: 00000000 00000000 00000000 00000000    ................
    01c01130: 00000000 00000000 00000000 00000000    ................
    01c01140: 00000000 00000000 00000000 00000000    ................
    01c01150: 00000000 00000000 00000000 00000000    ................
    01c01160: 00000000 00000000 00000000 00000000    ................
    01c01170: 00000000 00000000 00000000 00000000    ................
    01c01180: 00000000 00000000 00000000 00000000    ................
    01c01190: 00000000 00000000 00000000 00000000    ................
    01c011a0: 00000000 00000000 00000000 00000000    ................
    01c011b0: 00000000 00000000 00000000 00000000    ................
    01c011c0: 00000000 00000000 00000000 00000000    ................
    01c011d0: 00000000 00000000 00000000 00000000    ................
    01c011e0: 00000000 00000000 00000000 00000000    ................
    01c011f0: 00001a20 00000000 00000000 00000000     ...............
    01c01200: 03737000 40000000 40000000 40000000    .ps....@...@...@
    01c01210: 40000000 40000000 ffffffff ffffffff    ...@...@........
    01c01220: ffffffff ffffffff 00003333 00003333    ........33..33..
    01c01230: 00006ffc 000000ff 00000000 00000000    .o..............
    01c01240: 00008000 00010400 00000000 00000000    ................
    01c01250: 00000301 00000301 00000301 00000301    ................
    01c01260: 00000301 00000301 00000000 00000000    ................
    01c01270: 00000000 00000000 00000000 00000000    ................
    01c01280: 00000000 00000000 00000000 00000000    ................
    01c01290: 00001031 00001031 00000735 00001035    1...1...5...5...
    01c012a0: 00001035 00000731 00001031 00000735    5...1...1...5...
    01c012b0: 00001035 00001031 00000731 00001035    5...1...1...5...
    01c012c0: 00001031 00000301 00000301 00000731    1...........1...
    01c012d0: 00000000 00000000 00000000 00000000    ................
    01c012e0: 00000000 00000000 00000000 00000000    ................
    
[/code]
## A20
### Reset
[code] 
    0000: 90020000 00000454 00000000 00000000 
    0010: 086c9883 3092666e 00001090 0001a0c8 
    0020: 00000000 00000000 00000000 00000000 
    0030: 00000000 00000000 00000000 00000000 
    0040: 00000000 00000000 00000000 00000000 
    0050: 00000000 00000000 00000000 00000055 
    0060: 00000055 00000000 00000000 00000000 
    0070: 00000000 00000000 00000000 00000000 
    0080: 00000000 00000000 00000000 00000000 
    0090: 00000000 00000000 00210000 dd22ee11 
    00a0: 7788bb44 00000000 07b00000 00000000 
    00b0: 0005294a 00c80064 00000000 00000000 
    00c0: 00000000 00000000 00000000 00000000 
    00d0: 00000000 00000000 00000000 00000000 
    00e0: 00000000 00000000 00000000 00000000 
    00f0: 00000000 00000000 00000000 00000000 
    0100: 00000000 00000000 00000000 00000000 
    0110: 00000000 00000000 00000000 00000000 
    0120: 00000000 00000000 00000000 00000000 
    0130: 00000000 00000000 00000000 00000000 
    0140: 00000000 00000000 00000000 00000000 
    0150: 00000000 00000000 00000000 00000000 
    0160: 00000000 00000000 00000000 00000000 
    0170: 00000000 00000000 00000000 00000000 
    0180: 00000000 00000000 00000000 00000000 
    0190: 00000000 00000000 00000000 00000000 
    01a0: 00000000 00000000 00000000 00000000 
    01b0: 00000000 00000000 00000000 00000000 
    01c0: 00000000 00000000 00000000 00000000 
    01d0: 00000000 00000000 00000000 00000000 
    01e0: 00000000 00000000 00000000 00000000 
    01f0: 00000a52 00000000 00000000 00000000 
    0200: 03737000 c0000000 c0000000 c0000000 
    0210: c0000000 c0000000 ffffffff ffffffff 
    0220: ffffffff ffffffff 00003333 00003333 
    0230: c7000000 000003ff 00000000 00000000 
    0240: 00008000 01010400 00000000 00000000 
    0250: 00000001 00000001 00000001 00000001 
    0260: 00000001 00000001 00000001 00000001 
    0270: 00000000 00000000 00000000 00000000 
    0280: 00000000 00000000 00000000 00000000 
    0290: 00000001 00000001 00000001 00000001 
    02a0: 00000001 00000001 00000001 00000001 
    02b0: 00000001 00000001 00000001 00000001 
    02c0: 00000001 00000001 00000000 00000001 
    02d0: 00000000 00000000 00000000 00000000 
    02e0: 00000000 00000000 00000000 00000000 
    02f0: 00000000 00000000 00000000 00000000 
    
[/code]
### CB2 after boot0/1
[code] 
    01c01000: 00004020 000030e5 00000000 00000000     @...0..........
    01c01010: 0875a983 42d899b7 0000a090 00022a00    ..u....B.....*..
    01c01020: 00000000 00000000 00000000 00000000    ................
    01c01030: 00000000 00000000 00000000 00000000    ................
    01c01040: 00000000 00000000 00000000 00000249    ............I...
    01c01050: 00000000 00000000 00000000 00000065    ............e...
    01c01060: 00000055 00000000 00000000 00000000    U...............
    01c01070: 00000000 00000000 00000000 00000000    ................
    01c01080: 00000000 00000000 00000000 00000000    ................
    01c01090: 00000000 00000000 00210000 dd22ee11    ..........!...".
    01c010a0: 7788bb44 00000000 07f00000 00000002    D..w............
    01c010b0: 8002b75e 00c9ffff 00000000 00000000    ^...............
    01c010c0: 00000000 00000000 00000000 00000000    ................
    01c010d0: 00000000 00000000 00000000 00000000    ................
    01c010e0: 00000000 00000000 00000000 00000000    ................
    01c010f0: 00000000 00000000 00000000 00000000    ................
    01c01100: 00000000 00000000 00000000 00000000    ................
    01c01110: 00000000 00000000 00000000 00000000    ................
    01c01120: 00000000 00000000 00000000 00000000    ................
    01c01130: 00000000 00000000 00000000 00000000    ................
    01c01140: 00000000 00000000 00000000 00000000    ................
    01c01150: 00000000 00000000 00000000 00000000    ................
    01c01160: 00000000 00000000 00000000 00000000    ................
    01c01170: 00000000 00000000 00000000 00000000    ................
    01c01180: 00000000 00000000 00000000 00000000    ................
    01c01190: 00000000 00000000 00000000 00000000    ................
    01c011a0: 00000000 00000000 00000000 00000000    ................
    01c011b0: 00000000 00000000 00000000 00000000    ................
    01c011c0: 00000000 00000000 00000000 00000000    ................
    01c011d0: 00000000 00000000 00000000 00000000    ................
    01c011e0: 00000000 00000000 00000000 00000000    ................
    01c011f0: 00001a50 00000004 00000010 00000000    P...............
    01c01200: 03737000 40000000 40000000 40000000    .ps....@...@...@
    01c01210: 40000000 40000000 ffffffff ffffffff    ...@...@........
    01c01220: ffffffff ffffffff 00003333 00003333    ........33..33..
    01c01230: c7017ffc 000003ff 00000000 00000000    ................
    01c01240: 00008000 01010400 00000000 00000000    ................
    01c01250: 00000301 00000301 00000301 00000301    ................
    01c01260: 00000301 00000301 00000301 00000301    ................
    01c01270: 00000000 00000000 00000000 00000000    ................
    01c01280: 00000000 00000000 00000000 00000000    ................
    01c01290: 00001031 00001031 00000735 00001035    1...1...5...5...
    01c012a0: 00001035 00000731 00001031 00000735    5...1...1...5...
    01c012b0: 00001035 00001031 00000731 00001035    5...1...1...5...
    01c012c0: 00000001 00001031 00000000 00001031    ....1.......1...
    01c012d0: 00000000 00000000 00000000 00000000    ................
    01c012e0: 00000000 00000000 00000000 00000000    ................
    
[/code]
### CB2 after u-boot-spl (wip/a20)
[code] 
    01c01000: 00004020 000030e5 00000000 00000055     @...0......U...
    01c01010: 0882cf83 42d899b7 0000a090 00022a00    .......B.....*..
    01c01020: 00000000 00000000 00000000 00000000    ................
    01c01030: 00000000 00000000 00000000 00000000    ................
    01c01040: 00000000 00000000 00000000 00000249    ............I...
    01c01050: 00000000 00000000 00000000 00000055    ............U...
    01c01060: 00000055 00000000 00000000 00000000    U...............
    01c01070: 00000000 00000000 00000000 00000000    ................
    01c01080: 00000000 00000000 00000000 00000000    ................
    01c01090: 00000000 00000000 00210000 dd22ee11    ..........!...".
    01c010a0: 7788bb44 00000000 07f00000 00000002    D..w............
    01c010b0: 0005294a 00c9ffff 00000000 00000000    J)..............
    01c010c0: 00000000 00000000 00000000 00000000    ................
    01c010d0: 00000000 00000000 00000000 00000000    ................
    01c010e0: 00000000 00000000 00000000 00000000    ................
    01c010f0: 00000000 00000000 00000000 00000000    ................
    01c01100: 00000000 00000000 00000000 00000000    ................
    01c01110: 00000000 00000000 00000000 00000000    ................
    01c01120: 00000000 00000000 00000000 00000000    ................
    01c01130: 00000000 00000000 00000000 00000000    ................
    01c01140: 00000000 00000000 00000000 00000000    ................
    01c01150: 00000000 00000000 00000000 00000000    ................
    01c01160: 00000000 00000000 00000000 00000000    ................
    01c01170: 00000000 00000000 00000000 00000000    ................
    01c01180: 00000000 00000000 00000000 00000000    ................
    01c01190: 00000000 00000000 00000000 00000000    ................
    01c011a0: 00000000 00000000 00000000 00000000    ................
    01c011b0: 00000000 00000000 00000000 00000000    ................
    01c011c0: 00000000 00000000 00000000 00000000    ................
    01c011d0: 00000000 00000000 00000000 00000000    ................
    01c011e0: 00000000 00000000 00000000 00000000    ................
    01c011f0: 00001a50 00000004 00000010 00000000    P...............
    01c01200: 03737000 40000000 40000000 40000000    .ps....@...@...@
    01c01210: 40000000 40000000 ffffffff ffffffff    ...@...@........
    01c01220: ffffffff ffffffff 00003333 00003333    ........33..33..
    01c01230: c7017ffc 000003ff 00000000 00000000    ................
    01c01240: 00008000 01010400 00000000 00000000    ................
    01c01250: 00000301 00000301 00000301 00000301    ................
    01c01260: 00000301 00000301 00000301 00000301    ................
    01c01270: 00000000 00000000 00000000 00000000    ................
    01c01280: 00000000 00000000 00000000 00000000    ................
    01c01290: 00001031 00001031 00000735 00001035    1...1...5...5...
    01c012a0: 00001035 00000731 00001031 00000735    5...1...1...5...
    01c012b0: 00001035 00001031 00000731 00001035    5...1...1...5...
    01c012c0: 00000001 00001031 00000000 00000731    ....1.......1...
    01c012d0: 00000000 00000000 00000000 00000000    ................
    01c012e0: 00000000 00000000 00000000 00000000    ................
    
[/code]
