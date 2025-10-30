# A20/GMAC
< [A20][2157]
 
## Contents
  * [1 Gigabit MAC][2160]
    * [1.1 GMAC Registers][2161]
      * [1.1.1 GMAC_CONTROL][2162]
      * [1.1.2 GMAC_FRAME_FILTER][2163]
      * [1.1.3 GMAC_GMII_ADDR][2164]
      * [1.1.4 GMAC_FLOW_CTRL][2165]
      * [1.1.5 GMAC_DMA_BUS_MODE][2166]
      * [1.1.6 GMAC_DMA_STATUS][2167]
      * [1.1.7 GMAC_DMA_OP_MODE][2168]
      * [1.1.8 GMAC_DMA_INTR_ENA][2169]

# Gigabit MAC
## GMAC Registers
GMAC Base address: 0x01c50000 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[GMAC_CONTROL][2162]` | `0x0000` | `4B` | `Configuration`  
`[GMAC_FRAME_FILTER][2163]` | `0x0004` | `4B` | `Frame Filter`  
`GMAC_HASH_HIGH` | `0x0008` | `4B` | `Multicast Hash Table High`  
`GMAC_HASH_LOW` | `0x000c` | `4B` | `Multicast Hash Table Low`  
`[GMAC_GMII_ADDR][2164]` | `0x0010` | `4B` | `MMI Address`  
`GMAC_GMMI_DATA` | `0x0014` | `4B` | `MMI Data`  
`[GMAC_FLOW_CTRL][2165]` | `0x0018` | `4B` | `Flow Control`  
`GMAC_INT_STATUS` | `0x0038` | `4B` | `Interrupt Status`  
`GMAC_INT_MASK` | `0x003c` | `4B` | `Interrupt Mask`  
`GMAC_ADDR_HI[0-7]` | `0x0040 + i * 8` | `4B` | `upper 16bits of MAC address`  
`GMAC_ADDR_LO[0-7]` | `0x0044 + i * 8` | `4B` | `lower 32bits of MAC address`  
`GMAC_RGMII_STATUS` | `0x00D8` | `4B` | `S/R-GMII status`  
`[GMAC_DMA_BUS_MODE][2166]` | `0x1000` | `4B` | `DMA Bus Mode`  
`GMAC_DMA_XMT_POLL` | `0x1004` | `4B` | `DMA Transmit Poll Demand`  
`GMAC_DMA_RCV_POLL` | `0x1008` | `4B` | `DMA Received Poll Demand`  
`GMAC_DMA_RCV_LIST` | `0x100c` | `4B` | `DMA Received List Base`  
`GMAC_DMA_XMT_LIST` | `0x1010` | `4B` | `DMA Transmit List Base`  
`[GMAC_DMA_STATUS][2167]` | `0x1014` | `4B` | `DMA Status`  
`[GMAC_DMA_OP_MODE][2168]` | `0x1018` | `4B` | `DMA Operational Mode`  
`[GMAC_DMA_INTR_ENA][2169]` | `0x101c` | `4B` | `DMA Interrupt Enable`  
`GMAC_DMA_MISSED_FRAME` | `0x1020` | `4B` | `DMA Missed Frame and Buffer Overflow Counter`  
`GMAC_DMA_CUR_TX_DESC` | `0x1048` | `4B` | `DMA Current Host Transmit Descriptor`  
`GMAC_DMA_CUR_RX_DESC` | `0x104c` | `4B` | `DMA Current Host Received Descriptor`  
`GMAC_DMA_CUR_TX_BUF` | `0x1050` | `4B` | `DMA Current Host Transmit Buffer Address`  
`GMAC_DMA_CUR_RX_BUF` | `0x1054` | `4B` | `DMA Current Host Received Buffer Address`  
### GMAC_CONTROL
Default value: _unknown_  
Offset: 0x0000 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:25` | `Read/Write` | `` | `` | _unknown_  
`GMAC_CTL_TC` | `24` | `Read/Write` | `` | `` | Transmit Configuration in RGMII   
`GMAC_CTL_WD` | `23` | `Read/Write` | `` | `` | Watchdog Disable   
`GMAC_CTL_JD` | `22` | `Read/Write` | `` | `` | Jabber Disable   
`GMAC_CTL_BE` | `21` | `Read/Write` | `` | `` | Frame Burst Enable (only Half)   
`GMAC_CTL_JE` | `20` | `Read/Write` | `` | `` | Jumbo Frame Enable   
`GMAC_CTL_IFG` | `19:17` | `Read/Write` | `` | `` | Inter-Frame Gap   
`GMAC_CTL_DCRS` | `16` | `Read/Write` | `` | `` | Disable Carrier Sense During Transmission (only Half)   
`GMAC_CTL_PS` | `15` | `Read/Write` | `` | ` `
[code]
    0x0 = GMII
    0x1 = MII
    
[/code]
| Port Select   
`GMAC_CTL_FES` | `14` | `Read/Write` | `` | `` | Indicates the speed in Fast Ethernet(MII) mode   
`GMAC_CTL_ROD` | `13` | `Read/Write` | `` | `` | Receive own disable (only half-duplex)   
`GMAC_CTL_LM` | `12` | `Read/Write` | `` | `` | Loopback mode   
`GMAC_CTL_DM` | `11` | `Read/Write` | `` | `` | Duplex mode   
`GMAC_CTL_IPC` | `10` | `Read/Write` | `` | `` | Checksum Offload   
`GMAC_CTL_DR` | `9` | `Read/Write` | `` | `` | Retry disable (only half-duplex)   
`GMAC_CTL_LUD` | `8` | `Read/Write` | `` | `` | Link Up/Down (only RGMII/SGMII)   
`GMAC_CTL_ACS` | `7` | `Read/Write` | `` | `` | Automatic Pad/CRC Stripping   
`GMAC_CTL_BL` | `6:5` | `Read/Write` | `` | `` | Back-off limit.(only half-duplex)   
`GMAC_CTL_DC` | `4` | `Read/Write` | `` | `` | Deferral Check.(only half-duplex)   
`GMAC_CTL_TE` | `3` | `Read/Write` | `` | `` | Transmit Enable   
`GMAC_CTL_RE` | `2` | `Read/Write` | `` | `` | Receiver Enalbe   
`` | `1:0` | `Read/Write` | `` | `` | _unknown_  
### GMAC_FRAME_FILTER
Default value: _unknown_  
Offset: 0x0004 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`GMAC_FRAME_FILTER_RA` | `31` | `Read/Write` | `` | `` | Receive all mode   
`` | `30:11` | `Read/Write` | `` | `` | _unknown_  
`GMAC_FRAME_FILTER_HPF` | `10` | `Read/Write` | `` | `` | Hash or perfect Filter   
`GMAC_FRAME_FILTER_SAF` | `9` | `Read/Write` | `` | `` | Source Address Filter   
`GMAC_FRAME_FILTER_SAIF` | `8` | `Read/Write` | `` | `` | Inverse Filtering   
`` | `7:6` | `Read/Write` | `` | `` | _unknown_  
`GMAC_FRAME_FILTER_DBF` | `5` | `Read/Write` | `` | `` | Disable Broadcast frames   
`GMAC_FRAME_FILTER_PM` | `4` | `Read/Write` | `` | `` | Pass all multicast   
`GMAC_FRAME_FILTER_DAIF` | `3` | `Read/Write` | `` | `` | DA Inverse Filtering   
`GMAC_FRAME_FILTER_HMC` | `2` | `Read/Write` | `` | `` | Hash Multicast   
`GMAC_FRAME_FILTER_HUC` | `1` | `Read/Write` | `` | `` | Hash Unicast   
`GMAC_FRAME_FILTER_PR` | `0` | `Read/Write` | `` | `` | Promiscuous Mode   
### GMAC_GMII_ADDR
Default value: _unknown_  
Offset: 0x0010 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:16` | `Read/Write` | `` | `` | _unknown_  
`GMAC_GMII_PHY` | `15:6` | `Read/Write` | `` | `` | PHY   
`` | `5` | `Read/Write` | `` | `` | _unknown_  
`GMAC_GMII_CR` | `4:2` | `Read/Write` | `` | `` | CR   
`GMAC_GMII_WRITE` | `1` | `Read/Write` | `` | `` | write   
`GMAC_GMII_BUSY` | `0` | `Read/Write` | `` | `` | busy   
### GMAC_FLOW_CTRL
Default value: _unknown_  
Offset: 0x0018 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`GMAC_FLOW_CTRL_PT` | `31:16` | `Read/Write` | `` | `` | Pause Time   
`` | `15:3` | `Read/Write` | `` | `` | _unknown_  
`GMAC_FLOW_CTRL_RFE` | `2` | `Read/Write` | `` | `` | Rx Flow Control Enable   
`GMAC_FLOW_CTRL_TFE` | `1` | `Read/Write` | `` | `` | Tx Flow Control Enable   
`GMAC_FLOW_CTRL_BPA` | `0` | `Read/Write` | `` | `` | Flow Control Busy   
### GMAC_DMA_BUS_MODE
Default value: _unknown_  
Offset: 0x1000 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:26` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_BUS_MODE_ADDR_ALIGN` | `25` | `Read/Write` | `` | `` | Address-Aligned Beats   
`GMAC_DMA_BUS_MODE_4PBL` | `24` | `Read/Write` | `` | `` | 4xPBL Mode   
`GMAC_DMA_BUS_MODE_USP` | `23` | `Read/Write` | `` | `` | USP   
`GMAC_DMA_BUS_MODE_RPBL` | `22:17` | `Read/Write` | `` | `` | RPBL   
`GMAC_DMA_BUS_MODE_FIXBUST` | `16` | `Read/Write` | `` | `` | fixbu(r?)st   
`` | `15:14` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_BUS_MODE_PBL` | `13:8` | `Read/Write` | `` | `` | PBL   
`` | `7` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_BUS_MODE_DSL` | `6:2` | `Read/Write` | `` | `` | Descriptor skip length   
`GMAC_DMA_BUS_MODE_DA` | `1` | `Read/Write` | `` | `` | DMA Arbitration   
`GMAC_DMA_BUS_MODE_SOFT_RESET` | `0` | `Read/Write` | `` | `` | Software reset gdma   
### GMAC_DMA_STATUS
Default value: _unknown_  
Offset: 0x1014 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:27` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_STAT_GLI` | `26` | `Read/Write` | `` | `` | GLI   
`` | `25:23` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_STAT_TS` | `22:20` | `Read/Write` | `` | ` `
[code]
    0x0 = STOP
    0x1 = FETCH_DESC
    0x2 = WAIT_STAT
    0x3 = READ_DATA
    0x4-0x5 = _unknown_
    0x6 = SUSP
    0x7 = CLOSE_DESC
    
[/code]
| TS (Transmit Status?)   
`GMAC_DMA_STAT_RS` | `19:17` | `Read/Write` | `` | ` `
[code]
    0x0 = STOP
    0x1 = FETCH_DESC
    0x2 = _unknown_
    0x3 = WAIT_STAT
    0x4 = SUSP
    0x5 = CLOSE_DESC
    0x6 = _unknown_
    0x7 = WRITE_HOST
    
[/code]
| RS (Receive Status?)   
`GMAC_DMA_STAT_NIS` | `16` | `Read/Write` | `` | `` | Normal Interrupt Summary   
`GMAC_DMA_STAT_AIS` | `15` | `Read/Write` | `` | `` | Abnormal Interrupt Summary   
`GMAC_DMA_STAT_ERI` | `14` | `Read/Write` | `` | `` | Early Receive Interrupt   
`GMAC_DMA_STAT_FBI` | `13` | `Read/Write` | `` | `` | Fatal Bus Error Interrupt   
`` | `12:11` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_STAT_ETI` | `10` | `Read/Write` | `` | `` | Early Transmit Interrupt   
`GMAC_DMA_STAT_RWT` | `9` | `Read/Write` | `` | `` | Receive Watchdog Timeout   
`GMAC_DMA_STAT_RPS` | `8` | `Read/Write` | `` | `` | Receive Process Stopped   
`GMAC_DMA_STAT_RU` | `7` | `Read/Write` | `` | `` | Receive Buffer Unavailable   
`GMAC_DMA_STAT_RI` | `6` | `Read/Write` | `` | `` | Receive Interrupt   
`GMAC_DMA_STAT_UNF` | `5` | `Read/Write` | `` | `` | Transmit Underflow   
`GMAC_DMA_STAT_OVF` | `4` | `Read/Write` | `` | `` | Receive Overflow   
`GMAC_DMA_STAT_TJT` | `3` | `Read/Write` | `` | `` | Transmit Jabber Timeout   
`GMAC_DMA_STAT_TU` | `2` | `Read/Write` | `` | `` | Transmit Buffer Unavailable   
`GMAC_DMA_STAT_TPS` | `1` | `Read/Write` | `` | `` | Transmit Process Stopped   
`GMAC_DMA_STAT_TI` | `0` | `Read/Write` | `` | `` | Transmit Interrupt   
### GMAC_DMA_OP_MODE
Default value: _unknown_  
Offset: 0x1018 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:26` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_OP_MODE_RSF` | `25` | `Read/Write` | `` | `` | Receive Store and Forward   
`GMAC_DMA_OP_MODE_DFF` | `24` | `Read/Write` | `` | `` | Disable Flushing of Received Frames   
`GMAC_DMA_OP_MODE_RFA2` | `23` | `Read/Write` | `` | `` | MSB of Threshold for Activating Flow Control   
`GMAC_DMA_OP_MODE_RFD2` | `22` | `Read/Write` | `` | `` | MSB of Threshold for Deactivating Flow Control   
`GMAC_DMA_OP_MODE_TSF` | `21` | `Read/Write` | `` | `` | Transmit Store and Forward   
`GMAC_DMA_OP_MODE_FTF` | `20` | `Read/Write` | `` | `` | Flush Transmit FIFO   
`` | `19:17` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_OP_MODE_TTC` | `16:14` | `Read/Write` | `` | ` `
[code]
    0x0 = 64
    0x1 = 128
    0x2 = 192
    0x3 = 256
    0x4 = 40
    0x5 = 32
    0x6 = 24
    0x7 = 16
    
[/code]
| Transmit Threshold Control   
`GMAC_DMA_OP_MODE_ST` | `13` | `Read/Write` | `` | `` | Start/Stop Transmission Command   
`GMAC_DMA_OP_MODE_RFD` | `12:11` | `Read/Write` | `` | `` | Threshold for deactivating flow control   
`GMAC_DMA_OP_MODE_RFA` | `10:9` | `Read/Write` | `` | `` | Threshold for activating flow control   
`GMAC_DMA_OP_MODE_EFC` | `8` | `Read/Write` | `` | `` | Enable HW flow control   
`GMAC_DMA_OP_MODE_FEF` | `7` | `Read/Write` | `` | `` | Forward Error Frames   
`GMAC_DMA_OP_MODE_FUF` | `6` | `Read/Write` | `` | `` | Forward Undersized Frames   
`` | `5` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_OP_MODE_RTC` | `4:3` | `Read/Write` | `` | ` `
[code]
    0x0 = 64
    0x1 = 32
    0x2 = 96
    0x3 = 128
    
[/code]
| Receive Threshold Control   
`GMAC_DMA_OP_MODE_OSF` | `2` | `Read/Write` | `` | `` | Operate on Second Frame   
`GMAC_DMA_OP_MODE_SR` | `1` | `Read/Write` | `` | `` | Start/Stop Receive   
`` | `0` | `Read/Write` | `` | `` | _unknown_  
### GMAC_DMA_INTR_ENA
Default value: _unknown_  
Offset: 0x101c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:17` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_INTR_ENA_NIE` | `16` | `Read/Write` | `` | `` | Normal Summary   
`GMAC_DMA_INTR_ENA_AIE` | `15` | `Read/Write` | `` | `` | Abnormal Summary   
`GMAC_DMA_INTR_ENA_ERE` | `14` | `Read/Write` | `` | `` | Early Receive   
`GMAC_DMA_INTR_ENA_FBE` | `13` | `Read/Write` | `` | `` | Fatal Bus Error   
`` | `12:11` | `Read/Write` | `` | `` | _unknown_  
`GMAC_DMA_INTR_ENA_ETE` | `10` | `Read/Write` | `` | `` | Early Transmit   
`GMAC_DMA_INTR_ENA_RWE` | `9` | `Read/Write` | `` | `` | Receive Watchdog   
`GMAC_DMA_INTR_ENA_RSE` | `8` | `Read/Write` | `` | `` | Receive Stopped   
`GMAC_DMA_INTR_ENA_RUE` | `7` | `Read/Write` | `` | `` | Receive Buffer Unavailable   
`GMAC_DMA_INTR_ENA_RIE` | `6` | `Read/Write` | `` | `` | Receive Interrupt   
`GMAC_DMA_INTR_ENA_UNE` | `5` | `Read/Write` | `` | `` | Tx Underflow   
`GMAC_DMA_INTR_ENA_OVE` | `4` | `Read/Write` | `` | `` | Receive Overflow   
`GMAC_DMA_INTR_ENA_TJE` | `3` | `Read/Write` | `` | `` | Transmit Jabber   
`GMAC_DMA_INTR_ENA_TUE` | `2` | `Read/Write` | `` | `` | Transmit Buffer Unavailable   
`GMAC_DMA_INTR_ENA_TSE` | `1` | `Read/Write` | `` | `` | Transmit Stopped Enable   
`GMAC_DMA_INTR_ENA_TIE` | `0` | `Read/Write` | `` | `` | Transmit Interrupt Enable
