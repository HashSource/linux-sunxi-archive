# USB OTG Controller Register Guide
## Contents
  * [1 USB Vocabulary][57366]
  * [2 USB OTG][57367]
    * [2.1 Info][57368]
    * [2.2 USB OTG Controller Registers][57369]
      * [2.2.1 Default Map][57370]
      * [2.2.2 Common Registers][57371]
        * [2.2.2.1 PCTL / POWER][57372]
        * [2.2.2.2 DEVCTL][57373]
        * [2.2.2.3 VEND0][57374]
      * [2.2.3 Endpoint Registers][57375]
        * [2.2.3.1 Endpoint 0][57376]
        * [2.2.3.2 Endpoint 1 ~ N][57377]
    * [2.3 USB Port Controller Registers][57378]
      * [2.3.1 Default Map][57379]
      * [2.3.2 Register List][57380]
      * [2.3.3 ISCR][57381]
      * [2.3.4 PHY_CTRL][57382]
    * [2.4 USB PHY Control Register Addresses][57383]
  * [3 Documentation][57384]

# USB Vocabulary
**HCD** \- Host Controller Driver 
**UDC** \- USB Device Controller 
# USB OTG
All Allwinner A-series SoCs come with one USB OTG controller. The controller has been identified as a Mentor Graphics Inventra HDRC (High-speed Dual Role Controller), which is supported by the "musb" driver. However, the register addresses are scrambled. 
The A20 manual lists the following features 
  * Complies with USB 2.0 specification
  * Supports high-speed, full-speed, and low-speed in host mode
  * Supports high-speed and full-speed in device mode
  * 64 byte endpoint 0 for control transfer
  * Supports up to 5 user configurable endpoints for bulk, isochronous, control, and interrupt bi-directional transfers

The USB OTG controller is connected to a port controller. Only the data pins are exported from the SoC. The port controller is also used to control or tune the USB PHYs for the other USB host controllers. 
## Info
  * USB OTG Controller base address: 0x01c13000
  * USB Port Controller base address: 0x01c13400

## USB OTG Controller Registers
### Default Map
[code] 
    sun7i# md 0x01c13000 0x100
    01c13000: 6f427dee 6f427dee 6f427dee 6f427dee    .}Bo.}Bo.}Bo.}Bo
    01c13010: 6f427dee 6f427dee 00000000 00000000    .}Bo.}Bo........
    01c13020: 00000000 00000000 00000000 00000000    ................
    01c13030: 00000000 00000000 00000000 00000000    ................
    01c13040: 00008020 00000000 00000000 00000000     ...............
    01c13050: 00000000 00000000 00000000 00000000    ................
    01c13060: 00000000 00000000 00000000 00000000    ................
    01c13070: 00000000 00000000 00000000 00000000    ................
    01c13080: 00000000 00000000 00000000 00000000    ................
    01c13090: 00000000 00000000 00000000 00000000    ................
    01c130a0: 00000000 00000000 00000000 00000000    ................
    01c130b0: 00000000 00000000 00000000 00000000    ................
    01c130c0: 000b55de 5c727780 0000003c 00000000    .U...wr\<.......
    01c130d0: 00000000 05e64074 00000000 00000000    ....t@..........
    01c130e0: 00000000 00000000 00000000 00000000    ................
    01c130f0: 00000000 00000000 00000000 00000000    ................
    01c13100: 00000000 00000000 00000000 00000000    ................
    01c13110: 00000000 00000000 00000000 00000000    ................
    01c13120: 00000000 00000000 00000000 00000000    ................
    01c13130: 00000000 00000000 00000000 00000000    ................
    01c13140: 00000000 00000000 00000000 00000000    ................
    01c13150: 00000000 00000000 00000000 00000000    ................
    01c13160: 00000000 00000000 00000000 00000000    ................
    01c13170: 00000000 00000000 00000000 00000000    ................
    01c13180: 00000000 00000000 00000000 00000000    ................
    01c13190: 00000000 00000000 00000000 00000000    ................
    01c131a0: 00000000 00000000 00000000 00000000    ................
    01c131b0: 00000000 00000000 00000000 00000000    ................
    01c131c0: 00000000 00000000 00000000 00000000    ................
    01c131d0: 00000000 00000000 00000000 00000000    ................
    01c131e0: 00000000 00000000 00000000 00000000    ................
    01c131f0: 00000000 00000000 00000000 00000000    ................
    01c13200: 00000000 00000000 00000000 00000000    ................
    01c13210: 00000000 00000000 00000000 00000000    ................
    01c13220: 00000000 00000000 00000000 00000000    ................
    01c13230: 00000000 00000000 00000000 00000000    ................
    01c13240: 00000000 00000000 00000000 00000000    ................
    01c13250: 00000000 00000000 00000000 00000000    ................
    01c13260: 00000000 00000000 00000000 00000000    ................
    01c13270: 00000000 00000000 00000000 00000000    ................
    01c13280: 00000000 00000000 00000000 00000000    ................
    01c13290: 00000000 00000000 00000000 00000000    ................
    01c132a0: 00000000 00000000 00000000 00000000    ................
    01c132b0: 00000000 00000000 00000000 00000000    ................
    01c132c0: 00000000 00000000 00000000 00000000    ................
    01c132d0: 00000000 00000000 00000000 00000000    ................
    01c132e0: 00000000 00000000 00000000 00000000    ................
    01c132f0: 00000000 00000000 00000000 00000000    ................
    01c13300: 00000000 00000000 00000000.00000000    ................
    01c13310: 00000000 00000000 00000000 00000000    ................
    01c13320: 00000000 00000000 00000000 00000000    ................
    01c13330: 00000000 00000000 00000000 00000000    ................
    01c13340: 00000000 00000000 00000000 00000000    ................
    01c13350: 00000000 00000000 00000000 00000000    ................
    01c13360: 00000000 00000000 00000000 00000000    ................
    01c13370: 00000000 00000000 00000000 00000000    ................
    01c13380: 00000000 00000000 00000000 00000000    ................
    01c13390: 00000000 00000000 00000000 00000000    ................
    01c133a0: 00000000 00000000 00000000 00000000    ................
    01c133b0: 00000000 00000000 00000000 00000000    ................
    01c133c0: 00000000 00000000 00000000 00000000    ................
    01c133d0: 00000000 00000000 00000000 00000000    ................
    01c133e0: 00000000 00000000 00000000 00000000    ................
    01c133f0: 00000000 00000000 00000000 00000000    ................
    
[/code]
### Common Registers
Register Name  | Offset  | MUSB offset  | Size  | Description  | Note   
---|---|---|---|---|---  
`PCTL / POWER` | `0x40` | `0x01` | `1 B` | USB Power Control  |   
`DEVCTL` | `0x41` | `0x60` | `1 B` | OTG Device Control  |   
`EPIND / INDEX` | `0x42` | `0x0E` | `1 B` |  |   
`VEND0` | `0x43` | `0x??` | `1 B` | Vendor specific register  | Controls whether to use DMA mode   
`INTTx / INTRTX` | `0x44` | `0x02` | `2 B` | Transmit interrupt status  |   
`INTRx / INTRRX` | `0x46` | `0x04` | `2 B` | Receive interrupt status  |   
`INTTxE / INTRTXE` | `0x48` | `0x06` | `2 B` | Transmit interrupt mask  |   
`INTRxE / INTRRXE` | `0x4A` | `0x08` | `2 B` | Receive interrupt mask  |   
`INTUSB / INTRUSB` | `0x4C` | `0x0A` | `1 B` | USB function interrupt status  |   
`INTUSBE / INTRUSBE` | `0x50` | `0x0B` | `1 B` | USB function interrupt mask  |   
`FRNUM / FRAME` | `0x54` | `0x0C` | `2 B` |  |   
`EPINFO` | `0x78` | `0x78` | `1 B` |  |   
`RAMINFO` | `0x79` | `0x79` | `1 B` |  |   
`LINKINFO` | `0x7A` | `0x7A` | `1 B` |  |   
`VPLEN` | `0x7B` | `0x7B` | `1 B` |  |   
`HSEOF / HS_EOF1` | `0x7C` | `0x7C` | `1 B` |  |   
`FSEOF / FS_EOF1` | `0x7D` | `0x7D` | `1 B` |  |   
`LSEOF / LS_EOF1` | `0x7E` | `0x7E` | `1 B` |  |   
#### PCTL / POWER
Default value: 0x20  
Offset: 0x40  
MUSB offset: 0x01 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`ISOUPDATE` | `7` | `?` | `0` | ` ` | (device only)   
`SOFTCONN` | `6` | `?` | `0` | ` ` | (device only)   
`HSENAB` | `5` | `?` | `1` | ` ` |   
`HSMODE` | `4` | `?` | `0` | ` ` |   
`RESET` | `3` | `?` | `0` | ` ` |   
`RESUME` | `2` | `?` | `0` | ` ` |   
`SUSPENDM` | `1` | `?` | `0` | ` ` |   
`ENSUSPEND` | `0` | `?` | `0` | ` ` |   
#### DEVCTL
Default value: 0x80  
Offset: 0x41  
MUSB offset: 0x60 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`B_DEVICE / BDEVICE` | `7` | `?` | `1` | ` ` |   
`FS_DEV / FSDEV` | `6` | `?` | `0` | ` ` |   
`LS_DEV / LSDEV` | `5` | `?` | `0` | ` ` |   
`VBUS` | `4:3` | `?` | `10` | ` ` |   
`HOST_MODE / HM` | `2` | `?` | `0` | ` ` |   
`HOST_REQ / HR` | `1` | `?` | `0` | ` ` |   
`SESSION` | `0` | `?` | `0` | ` ` |   
#### VEND0
Default value: 0x20  
Offset: 0x43  
MUSB offset: 0x?? 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`DRQ_SEL` | `1` | `Read/Write` | `0` | ` ` |   
`BUS_SEL` | `0` | `Read/Write` | `0` | ` ` |   
### Endpoint Registers
To access these under indexed mode, you must first write the endpoint number to the INDEX register. 
#### Endpoint 0
Register Name  | Offset  | MUSB offset  | Size  | Description  | Note   
---|---|---|---|---|---  
`CSR0` | `0x82` | `0x12` | `2 B` | MUSB main control / status register  |   
`COUNT0` | `0x88` | `0x18` | `2 B` |  |   
`EP0TYPE / TYPE0` | `0x8A` | `0x1A` | `1 B` |  |   
`NAKLIMIT0` | `0x8B` | `0x1B` | `1 B` |  |   
`CONFIGDATA` | `0xC0` | `0x1F` | `2 B` | MUSB core hardware feature flags  |   
#### Endpoint 1 ~ N
Register Name  | Offset  | MUSB offset  | Size  | Description  | Note   
---|---|---|---|---|---  
`TXMAXP` | `0x80` | `0x10` | `2 B` |  |   
`TXCSR` | `0x82` | `0x12` | `2 B` |  |   
`RXMAXP` | `0x84` | `0x14` | `2 B` |  |   
`RXCSR` | `0x86` | `0x16` | `2 B` |  |   
`RXCOUNT` | `0x88` | `0x18` | `2 B` |  |   
`TXTYPE` | `0x8C` | `0x1A` | `1 B` |  |   
`TXINTERVAL` | `0x8D` | `0x1B` | `1 B` |  |   
`RXTYPE` | `0x8E` | `0x1C` | `1 B` |  |   
`RXINTERVAL` | `0x8F` | `0x1D` | `1 B` |  |   
`TXFIFOSZ` | `0x90` | `0x62` | `1 B` | TX FIFO size  | size = 2 ^ (TXFIFOSZ + 3)   
`RXFIFOSZ` | `0x94` | `0x63` | `1 B` | RX FIFO size  | size = 2 ^ (RXFIFOSZ + 3)   
`TXFIFOADD` | `0x92` | `0x64` | `2 B` | TX FIFO offset  | TXFIFOADD = offset >> 3   
`RXFIFOADD` | `0x96` | `0x66` | `2 B` | RX FIFO offset  | RXFIFOADD = offset >> 3   
## USB Port Controller Registers
### Default Map
[code] 
    sun7i# md 0x01c13400 0x4
    01c13400: 40000000 00000000 00000000 00000000    ...@............
    
[/code]
### Register List
Register Name  | Offset  | Size  | Description  | Note   
---|---|---|---|---  
`ISCR` | `0x0` | `4 B` | Interrupt status / control register  |   
`PHY_CTRL` | `0x4` | `2 B` | PHY control  |   
`PHY_BIST` | `0x8` | `4 B` | unknown  |   
`PHY_TUNE` | `0xC` | `4 B` | PHY tuning  |   
### ISCR
Default value: 0x40000000  
Offset: 0x0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`no operation` | `31` | `` | `` | `` |   
`VBUS_VALID_FROM_DATA` | `30` | `Read/Write` | `0x0` | ` `
[code]
        0 = Invalid
        1 = Valid
      
    
[/code]
|  VBUS_VALID_FROM_DATA = ! (EXT_DM_STATUS | EXT_DP_STATUS)   
`VBUS_VALID_FROM_VBUS` | `29` | `Read/Write` | `0x0` | ` `
[code]
        0 = Invalid
        1 = Valid
      
    
[/code]
| Status of External VBUS pin (pin not available on A10/A20)   
`EXT_ID_STATUS` | `28` | `Read` | `0x0` | ` `
[code]
        0 = Low
        1 = High
      
    
[/code]
| Status of External ID pin (pin not available on A10/A20)   
`EXT_DM_STATUS` | `27` | `Read` | `0x0` | ` `
[code]
        0 = Low
        1 = High
      
    
[/code]
| Status of D- pin   
`EXT_DP_STATUS` | `26` | `Read` | `0x0` | ` `
[code]
        0 = Low
        1 = High
      
    
[/code]
| Status of D+ pin   
`MERGED_VBUS_STATUS` | `25` | `Read` | `0x0` | ` `
[code]
        0 = Low
        1 = High
      
    
[/code]
|  MERGED_VBUS_STATUS = FORCE_VBUS | (VBUS_VALID_FROM_DATA ? VBUS_VALID_FROM_VBUS)   
`MERGED_ID_STATUS` | `24` | `Read` | `0x0` | ` `
[code]
        0 = Low
        1 = High
      
    
[/code]
| FORCE_ID   
`no operation` | `23:18` | `` | `` | `` |   
`ID_PULLUP_EN` | `17` | `Read/Write` | `0x0` | ` `
[code]
        0 = Disable pull-up
        1 = Enable pull-up
      
    
[/code]
| Controls pull-up on ID pin   
`DPDM_PULLUP_EN` | `16` | `Read/Write` | `0x0` | ` `
[code]
        0 = Disable pull-up
        1 = Enable pull-up
      
    
[/code]
| Controls pull-up on USB D+/D- pins   
`FORCE_ID` | `15:14` | `Read/Write` | `0x0` | ` `
[code]
        00 = Disable
        01 = unknown
        10 = Force ID to low
        11 = Force ID to high
      
    
[/code]
| Force internal ID pin state   
`FORCE_VBUS_VALID` | `13:12` | `Read/Write` | `0x0` | ` `
[code]
        00 = Disable
        01 = unknown
        10 = Force VBUS valid to low
        11 = Force VBUS valid to high
      
    
[/code]
| Force internal VBUS pin state   
`VBUS_VALID_SRC` | `11:10` | `Read/Write` | `0x0` | ` `
[code]
        00 = 
        01 = 
        10 = 
        11 = 
      
    
[/code]
| unknown   
`no operation` | `9:8` | `` | `` | `` |   
`HOSC_EN` | `7` | `Read/Write` | `0x0` | ` `
[code]
        0 = 
        1 = 
      
    
[/code]
|   
`VBUS_CHANGE_DETECT` | `6` | `Read/Write` | `0x0` | ` `
[code]
        0 = No change
        1 = Changed
      
    
[/code]
| Was VBUS changed?   

[code] 
      Write 1 to clear
    
[/code]  
`ID_CHANGE_DETECT` | `5` | `Read/Write` | `0x0` | ` `
[code]
        0 = No change
        1 = Changed
      
    
[/code]
| Was ID changed?   

[code] 
      Write 1 to clear
    
[/code]  
`DPDM_CHANGE_DETECT` | `4` | `Read/Write` | `0x0` | ` `
[code]
        0 = No change
        1 = Changed
      
    
[/code]
| Was D+/D- changed?   

[code] 
      Write 1 to clear
    
[/code]  
`IRQ_ENABLE` | `3` | `Read/Write` | `0x0` | ` `
[code]
        0 = Disable
        1 = Enable
      
    
[/code]
| Interrupt on wake   
`VBUS_CHANGE_DETECT_EN` | `2` | `Read/Write` | `0x0` | ` `
[code]
        0 = Disable
        1 = Enable
      
    
[/code]
| Interrupt on VBUS change   
`ID_CHANGE_DETECT_EN` | `1` | `Read/Write` | `0x0` | ` `
[code]
        0 = Disable
        1 = Enable
      
    
[/code]
| Interrupt on ID change   
`DPDM_CHANGE_DETECT_EN` | `0` | `Read/Write` | `0x0` | ` `
[code]
        0 = Disable
        1 = Enable
      
    
[/code]
| Interrupt on D+/D- status change   
### PHY_CTRL
Default value: 0x0000  
Offset: 0x4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`no operation` | `31:19` | `` | `` | `` |   
`DATA` | `16 + i ( i = 0 ~ 2 )` | `Read/Write` | `` | `` | Data bit read back, one bit per PHY   
`ADDR` | `15:8` | `Write` | `` | `` | Bit address to write to   
`DATA` | `7` | `Read/Write` | `` | `` | Data bit to write   
`USBC_i` | `i (i = 0 ~ 2)` | `Read/Write` | `` | `` | Pulse the corresponding bit to signal writing to a PHY   
## USB PHY Control Register Addresses
Name  | Bit Address  | Size  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`SET_PLL_BW` | `0x03` | `2` | `0x2` | `0x0 ~ 0x3` | Common to all PHYs, set USB PLL bandwidth   
`RES45_CAL_EN` | `0x0c` | `1` | `0x0` | ` `
[code]
       0x0: Disable
       0x1: Enable
      
    
[/code]
| Common to all PHYs, control 45 Ohm resistor calibration (?)   
`SET_TX_AMPLITUDE_TUNE` | `0x20` | `2` | `0x0` | `0x0 ~ 0x3` | Set USB TX signal amplitude   
`SET_TX_SLEWRATE_TUNE` | `0x22` | `3` | `0x5` | `0x0 ~ 0x7` | Set USB TX signal slew rate   
`SET_VBUS_VALID_THRESHOLD` | `0x25` | `2` | `0x2` | `0x0 ~ 0x3` | Set USB VBUS valid threshold   
`OTG_FUNC_ENABLE` | `0x28` | `1` | `0x1` | ` `
[code]
       0x0: Disable
       0x1: Enable
      
    
[/code]
| Control USB OTG function   
`VBUS_DET_ENABLE` | `0x29` | `1` | `0x1` | ` `
[code]
       0x0: Disable
       0x1: Enable
      
    
[/code]
| Control USB VBUS detection   
`SET_DISCON_DET_THRESHOLD` | `0x2a` | `3` | `0x1` | `0x0 ~ 0x3 ` | Control USB disconnect detection threshold   
# Documentation
  * [File:Musbmhdrc.pdf][57385]
