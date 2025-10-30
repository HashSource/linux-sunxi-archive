# Two Wire Interface Controller Register guide
(Redirected from [I²C][28665])
 
## Contents
  * [1 Two Wire Interface Controller][28668]
    * [1.1 Controller Overview][28669]
    * [1.2 Pins list][28670]
    * [1.3 TWI Controller Registry Guide][28671]
      * [1.3.1 Base Addresses][28672]
      * [1.3.2 Register List][28673]
      * [1.3.3 Status Codes][28674]
    * [1.4 See also][28675]
    * [1.5 External links][28676]

# Two Wire Interface Controller
**I²C** , also called **IIC** (Inter-Integrated Circuit) or **TWI** (Two-Wire-Interface) is a multi-master serial bus natively supported by **[sunxi SoCs][28677]**. Uses only two bidirectional lines, **SDA** (serial data) and **SCL** serial clock. 
## Controller Overview
This 2-Wire Controller is designed to be used as an interface between CPU host and the serial 2-Wire bus. It can support all the standard 2-Wire transfer, including Slave and Master. The communication to the 2-Wire bus is carried out on a byte-wise basis using interrupt or polled handshaking. This 2-Wire Controller can be operated in standard mode (100Kbps) or fast-mode, supporting data rate up to 400Kbps. Multiple Masters and 10-bit addressing Mode are supported for this specified application. General Call Addressing is also supported in Slave mode. 
The 2-Wire Controller includes the following features: 
  * Software-programmable for Slave or Master
  * Support Repeated START signal
  * Support Multi-master systems
  * Support 10-bit addressing with 2-Wire bus
  * Performs arbitration and clock synchronization
  * Own address and General Call address detection
  * Interrupt on address detection
  * Supports speeds up to 400Kbits/s ("fast mode")
  * Support operation from a wide range of input clock frequencies

## Pins list
| [A10][28678] | [A13][28679] | [A10s][28680] | [A20][28681]  
---|---|---|---|---  
Clock  | APB1-CLK  | APB1-CLK  | APB1-CLK  | APB1-CLK   
Bus  | Speed  | SCK | SDA  | SCK | SDA  | SCK | SDA  | SCK | SDA   
TWI0  | 400000  | `PB00<2>` | `PB01<2>` | `PB00<2>` | `PB01<2>` | `PB00<2>` | `PB01<2>` | `PB00<2>` | `PB01<2>`  
TWI1  | 200000  | `PB18<2>` | `PB19<2>` | `PB15<2>` | `PB16<2>` | `PB15<2>` | `PB16<2>` | `PB18<2>` | `PB19<2>`  
TWI2  | 200000  | `PB20<2>` | `PB21<2>` | `PB17<2>` | `PB18<2>` | `PB17<2>` | `PB18<2>` | `PB20<2>` | `PB21<2>`  
## TWI Controller Registry Guide
### Base Addresses
Bus | Base | Size   
---|---|---  
0 | `0x01C2ac00` | `1KiB`  
1 | `0x01C2b000` | `1KiB`  
2 | `0x01C2b400` | `1KiB`  
### Register List
Register | Offset | Description   
---|---|---  
`TWI_ADDR_REG` | `0x00` | 31:8bit reserved,7-1bit for slave addr,0 bit for GCE   
`TWI_XADDR_REG` | `0x04` | 31:8bit reserved,7-0bit for second addr in 10bit addr   
`TWI_DATA_REG` | `0x08` | 31:8bit reserved, 7-0bit send or receive data byte   
`TWI_CTL_REG` | `0x0C` | INT_EN,BUS_EN,M_STA,INT_FLAG,A_ACK   
`TWI_STAT_REG` | `0x10` | 28 interrupt types + 0xF8 normal type = 29   
`TWI_CLK_REG` | `0x14` | 31:7bit reserved,6-3bit,CLK_M,2-0bit CLK_N   
`TWI_SRST_REG` | `0x18` | 31:1bit reserved;0bit,write 1 to clear 0.   
`TWI_EFR_REG` | `0x1C` | 31:2bit reserved,1:0 bit data byte follow read comand   
`TWI_LCR_REG` | `0x20` | 31:6bits reserved 5:0bit for sda&scl control   
### Status Codes
Status | Code | Meaning   
---|---|---  
`TWI_STAT_BUS_ERR` | `0x00` | Bus error   
`TWI_STAT_TX_STA` | `0x08` | START condition transmitted   
`TWI_STAT_TX_RESTA` | `0x10` | Repeated START condition transmitted   
`TWI_STAT_TX_AW_ACK` | `0x18` | Address + Write bit transmitted, ACK received   
`TWI_STAT_TX_AW_NAK` | `0x20` | Address + Write bit transmitted, ACK not received   
`TWI_STAT_TXD_ACK` | `0x28` | Data byte transmitted in master mode, ACK received   
`TWI_STAT_TXD_NAK` | `0x30` | Data byte transmitted in master mode, ACK not received   
`TWI_STAT_ARBLOST` | `0x38` | Arbitration lost in address or data byte   
`TWI_STAT_TX_AR_ACK` | `0x40` | Address + Read bit transmitted, ACK received   
`TWI_STAT_TX_AR_NAK` | `0x48` | Address + Read bit transmitted, ACK not received   
`TWI_STAT_RXD_ACK` | `0x50` | Data byte received in master mode, ACK transmitted   
`TWI_STAT_RXD_NAK` | `0x58` | Data byte received in master mode, not ACK transmitted   
`TWI_STAT_RXWS_ACK` | `0x60` | Slave address + Write bit received, ACK transmitted   
`TWI_STAT_ARBLOST_RXWS_ACK` | `0x68` | Arbitration lost in address as master, slave address + Write bit received, ACK transmitted   
`TWI_STAT_RXGCAS_ACK` | `0x70` | General Call address received, ACK transmitted   
`TWI_STAT_ARBLOST_RXGCAS_ACK` | `0x78` | Arbitration lost in address as master, General Call address received, ACK transmitted   
`TWI_STAT_RXDS_ACK` | `0x80` | Data byte received after slave address received, ACK transmitted   
`TWI_STAT_RXDS_NAK` | `0x88` | Data byte received after slave address received, not ACK transmitted   
`TWI_STAT_RXDGCAS_ACK` | `0x90` | Data byte received after General Call received, ACK transmitted   
`TWI_STAT_RXDGCAS_NAK` | `0x98` | Data byte received after General Call received, not ACK transmitted   
`TWI_STAT_RXSTPS_RXRESTAS` | `0xA0` | STOP or repeated START condition received in slave mode   
`TWI_STAT_RXRS_ACK` | `0xA8` | Slave address + Read bit received, ACK transmitted   
`TWI_STAT_ARBLOST_SLAR_ACK` | `0xB0` | Arbitration lost in address as master, slave address + Read bit received, ACK transmitted   
_-_ | `0xB8` | Data byte transmitted in slave mode, ACK received   
_-_ | `0xC0` | Data byte transmitted in slave mode, ACK not received   
_-_ | `0xC8` | Last byte transmitted in slave mode, ACK received   
`TWI_STAT_TX_SAW_ACK` | `0xD0` | Second Address byte + Write bit transmitted, ACK received   
`TWI_STAT_TX_SAW_NAK` | `0xD8` | Second Address byte + Write bit transmitted, ACK not received   
`TWI_STAT_IDLE` | `0xF8` | No relevant status information or no interrupt   
## See also
## External links
  * [wikipedia article][28682]
