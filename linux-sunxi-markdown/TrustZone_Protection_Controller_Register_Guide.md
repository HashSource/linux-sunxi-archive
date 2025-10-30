# TrustZone Protection Controller Register Guide
## Contents
  * [1 TrustZone Protection Controller Unit][55968]
    * [1.1 TZPC Config][55969]
    * [1.2 TZPC Registers][55970]
      * [1.2.1 TZPC_DECPORT0_SIZE][55971]
      * [1.2.2 TZPC_DECPORT0_STA][55972]
      * [1.2.3 TZPC_DECPORT0_SET][55973]
      * [1.2.4 TZPC_DECPORT0_CLR][55974]
      * [1.2.5 TZPC_CPU_CONTROL][55975]
    * [1.3 Initial values][55976]
      * [1.3.1 default map][55977]
      * [1.3.2 all to 1][55978]
      * [1.3.3 all to 0][55979]

# TrustZone Protection Controller Unit
Allows certain area's of the Software Interface to secure/in-secure. 
It currently seems that the A10 only has 1 trustzone protection controller unit, TZPC0. Furthermore only the Interupt Controller (Bit0) and RTC & Alarm (Bit1) Modules appear to be securable. 
#### TZPC Config
Register  | Bit  | TZPC0 Module Name   
---|---|---  
`TZPC_DECPORT0` | `0` `` | `INTC`  
`TZPC_DECPORT0` | `1` `` | `RTC & Alarm`  
`TZPC_DECPORT0` | `2` `` | `Undefined`  
`TZPC_DECPORT0` | `3` `` | `Undefined`  
`TZPC_DECPORT0` | `4` `` | `Undefined`  
`TZPC_DECPORT0` | `5` `` | `Undefined`  
`TZPC_DECPORT0` | `6` `` | `Undefined`  
`TZPC_DECPORT0` | `7` `` | `Undefined`  
#### TZPC Registers
TZPC Base address: 0x01c23400 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`TZPC_DECPORT0_SIZE` | `0x0000` | `4 B` | `TZPC R0SIZE Register`  
`TZPC_DECPORT0_STA` | `0x0004` | `4 B` | `TZPC Decode Port0 Status`  
`TZPC_DECPORT0_SET` | `0x0008` | `4 B` | `TZPC Decode Port0 Set`  
`TZPC_DECPORT0_CLR` | `0x000c` | `4 B` | `TZPC Decode Port0 Clear`  
`TZPC_CPU_CTRL` | `0x0020` | `4 B` | `CPU Control Register`  
##### TZPC_DECPORT0_SIZE
Default value: 0x00000010  
Offset: 0x00 
Bit  | Read/Write  | Default  | Description   
---|---|---|---  
`0:9` | `Read` | `0x10` | ` `
[code]
          SEC_RAM_SIZE
          Secure Ram region size in 4KiB steps
          0x0000 = No secure region
          0x0001 = 4KiB secure region
          0x0002 = 8KiB secure region
          0x0003 = 12KiB secure region
          0x0004 = 16KiB secure region
          ...
          0x0010 = 64KiB secure region
          ...
          0x01ff = 2044KiB secure region
          0x0200 >= Entire ram is secure region.
      
    
[/code]  
`10:31` |  |  | Undefined   
##### TZPC_DECPORT0_STA
Default value: 0x00000000  
Offset: 0x04 
Bit  | Read/Write  | Default  | Description   
---|---|---|---  
`0:7` | `Read` | `0x00` | ` `
[code]
          STA_DEC_PROT_OUT
          Status of the decode-protection output
          0 = secure
          1 = non-secure
      
    
[/code]  
`8:31` |  |  | Undefined   
##### TZPC_DECPORT0_SET
Default value: 0x00000000  
Offset: 0x08 
Bit  | Read/Write  | Default (Hex)  | Description   
---|---|---|---  
`0:7` | `Read/Write` | `0x00` | ` `
[code]
          SET_DEC_PROT_OUT
          Set decode protection bits
          (Currently only Bit0 and 1, INTC and RTC&Alarm)
          0 = Nothing
          1 = Set to non-secure
      
    
[/code]  
`8:31` |  |  | Undefined   
##### TZPC_DECPORT0_CLR
Default value: 0x00000000  
Offset: 0x0c 
Bit  | Read/Write  | Default (Hex)  | Description   
---|---|---|---  
`0:7` | `Read/Write` | `0x00` | ` `
[code]
          CLR_DEC_PROT_OUT
          Clear protection
          (Currently only Bit0 and 1, INTC and RTC&Alarm)
          0 = Nothing
          1 = Set to secure
      
    
[/code]  
`8:31` |  |  | Undefined   
##### TZPC_CPU_CONTROL
Default value: 0x00000002  
Offset: 0x20 
Bit  | Read/Write  | Default  | Description   
---|---|---|---  
`0` | `Read/Write` | `0b0` | ` `
[code]
          CP15SDISABLE
          Disable write access to CP15 registers
          0 = enable
          1 = disable
      
    
[/code]  
`1:7` |  |  | Reserved   
`8:31` |  |  | Undefined   
## Initial values
### default map
md 0x01c23400 0x9 
[code] 
    01c23400: 00000010 00000000 00000000 00000000    ................
    01c23410: 00000000 00000000 00000000 00000000    ................
    01c23420: 00000002    ....
    
[/code]
### all to 1
mw 0x01c23400 0xffffffff 0x9  
md 0x01c23400 0x9 
[code] 
    01c23400: 00000010 00000000 00000000 00000000    ................
    01c23410: 00000000 00000000 00000000 00000000    ................
    01c23420: 000000ff    ....
    
[/code]
### all to 0
mw 0x01c23400 0x00 0x9  
md 0x01c23400 0x9 
[code] 
    01c23400: 00000010 00000000 00000000 00000000    ................
    01c23410: 00000000 00000000 00000000 00000000    ................
    01c23420: 00000000    ....
    
[/code]
