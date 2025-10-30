# SPDIF
## Contents
  * [1 Info][48326]
    * [1.1 SUNXI-SPDIF Registers][48327]
      * [1.1.1 SUNXI_SPDIF_CTL][48328]
      * [1.1.2 SUNXI_SPDIF_TXCFG][48329]
      * [1.1.3 SUNXI_SPDIF_RXCFG][48330]
      * [1.1.4 SUNXI_SPDIF_TXFIFO][48331]
      * [1.1.5 SUNXI_SPDIF_RXFIFO][48332]
      * [1.1.6 SUNXI_SPDIF_FCTL][48333]
      * [1.1.7 SUNXI_SPDIF_FSTA][48334]
      * [1.1.8 SUNXI_SPDIF_INT][48335]
      * [1.1.9 SUNXI_SPDIF_ISTA][48336]
      * [1.1.10 SUNXI_SPDIF_TXCNT][48337]
      * [1.1.11 SUNXI_SPDIF_RXCNT][48338]
      * [1.1.12 SUNXI_SPDIF_TXCHSTA0][48339]
      * [1.1.13 SUNXI_SPDIF_TXCHSTA1][48340]
      * [1.1.14 SUNXI_SPDIF_RXCHSTA0][48341]
      * [1.1.15 SUNXI_SPDIF_RXCHSTA1][48342]
    * [1.2 SUNXI SPDIF DEFAULT VALUES][48343]
      * [1.2.1 default a20 registers][48344]
      * [1.2.2 default a10 registers][48345]

## Info
The SUNXI SPDIF Controller was not documented in the user manual until the release of the H3 specification. So some of the following values and descriptions are taken from the code. The base address of the block is 0x01C21000. 
#### SUNXI-SPDIF Registers
Register Name  | Offset  | Size  | Description  | Notes   
---|---|---|---|---  
`SUNXI_SPDIF_CTL` | `0x0000` | `4 B` | SUNXI SPDIF CONTROLLER Register   
`SUNXI_SPDIF_TXCFG` | `0x0004` | `4 B` | SUNXI SPDIF TX CONTROLLER Register   
`SUNXI_SPDIF_RXCFG` | `0x0008` | `4 B` | SUNXI SPDIF RX CONTROLLER Register   
`SUNXI_SPDIF_TXFIFO` | `0x000c` | `4 B` | SUNXI SPDIF TX FIFO Write Register   
`SUNXI_SPDIF_RXFIFO` | `0x0010` | `4 B` | SUNXI SPDIF RX FIFO Read Register   
`SUNXI_SPDIF_FCTL` | `0x0014` | `4 B` | SUNXI SPDIF FIFO CONTROLLER Register   
`SUNXI_SPDIF_FSTA` | `0x0018` | `4 B` | SUNXI SPDIF FIFO STATUS Register  | Not Used in linux-sunxi kernel   
`SUNXI_SPDIF_INT` | `0x001c` | `4 B` | SUNXI SPDIF INTERRUPT CONTROLLER Register   
`SUNXI_SPDIF_ISTA` | `0x0020` | `4 B` | SUNXI SPDIF INTERRUPT STATUS Register   
`SUNXI_SPDIF_TXCNT` | `0x0024` | `4 B` | SUNXI SPDIF TX FIFO COUNT Register   
`SUNXI_SPDIF_RXCNT` | `0x0028` | `4 B` | SUNXI SPDIF RX FIFO COUNT Register   
`SUNXI_SPDIF_TXCHSTA0` | `0x002c` | `4 B` | SUNXI SPDIF TX CHANNEL STATUS Register 0   
`SUNXI_SPDIF_TXCHSTA1` | `0x0030` | `4 B` | SUNXI SPDIF TX CHANNEL STATUS Register 1   
`SUNXI_SPDIF_RXCHSTA0` | `0x0034` | `4 B` | SUNXI SPDIF RX CHANNEL STATUS Register 0   
`SUNXI_SPDIF_RXCHSTA1` | `0x0038` | `4 B` | SUNXI SPDIF RX CHANNEL STATUS Register 1   
##### SUNXI_SPDIF_CTL
Default value: 0x00000000  
Offset: 0x00 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_CTL_RESET` | `0` | `Read/Write` | `0b0` | ` `
[code]
       0 = normal
       1 = reset
      
    
[/code]
| Reset the SPDIF block. Self clear to 0   
`SUNXI_SPDIF_CTL_GEN` | `1` | `Read/Write` | `0b0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| Enable or disable the SPDIF block   
`SUNXI_SPDIF_CTL_MCLKOUTEN` | `2` | `Read/Write` | `0b0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| Enable or disable the MCLK Output   
`no operation` | `3` | `0x00`  
`SUNXI_SPDIF_CTL_MCLKDIV` | `4:9` | `Read/Write` | `0b0` | ` `
[code]
        MCLK divide ratio.
       
    
[/code]
| Mclk divide Ratio. Note: only support 2n divide ratio(n=1~31). This is documented in the header but isn't seemed to be used in the code.   
`no operation` | `10:31` | `0x00`  
##### SUNXI_SPDIF_TXCFG
Default value(A20): 0x00001000  
Default value(A10): 0x00000f00  
Offset: 0x04 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_TXCFG_TXEN` | `0` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| Enable the Transmission FIFO.   
`SUNXI_SPDIF_TXCFG_CHSTMODE` | `1` | `Read/Write` | `0xb0` | ` `
[code]
        0 = Channel status A&B set to 0
        1 = Channel status A&B generated from TX_CHSTA
       
    
[/code]
| Channel stereo mode   
`SUNXI_SPDIF_TXCFG_FMTRVD` | `2:3` | `Read/Write` | `0xb0` | ` `
[code]
        0 = 16 bits audio resolution
        1 = 20 bits audio resolution
        2 = 24 bits audio resolution
        3 = reserved
       
    
[/code]
| Format of the audio data resolution.   
`SUNXI_SPDIF_TXCFG_TXRATIO` | `4:8` | `Read/Write` | `0x01(A10)/0x00(A20)` | `` | TX clock divide Ratio. Note: clock divide ratio = TX RATIO + 1. This seems to be related to the sample rate based on the division of 192KHz minus 1. If you are setting the bit rate to 48KHz then 192/48 = 4. Therefore you will need to set the TX ratio to 3. It seems that it is possible to drop the sample rate down to 6KHz but this would be unsupported by SPDIF receivers.   
`no operation` | `9:15` | `0xb0`  
`SUNXI_SPDIF_TXCFG_NONAUDIO` | `16` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| Enable the sending of compressed audio data over the connection. When disabled Linear PCM (Valid bit of both sub­frame set to 0 ), when enabled Non-audio(Valid bit of both sub­frame set to 1)   
`SUNXI_SPDIF_TXCFG_ASS` | `17` | `Read/Write` | `0xb0` | ` `
[code]
        0 = Sending Zeros
        1 = Sending last audio sample.
       
    
[/code]
| Audio Sample Select when TX FIFO under run. This bit is only valid in PCM mode.   
`no operation` | `18:30` | `0xb0`  
`SUNXI_SPDIF_TXCFG_SINGLEMOD` | `31` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| TX Single Channel mode.   
##### SUNXI_SPDIF_RXCFG
Default value: 0x00808000  
Offset: 0x08 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_RXCFG_RXEN` | `0` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| Enable the Receiver FIFO.   
`SUNXI_SPDIF_RXCFG_CHSTCP` | `1` | `Read/Write` | `0xb0` | ` `
[code]
        0 = Idle or capture end
        1 = Capture Channel status start
       
    
[/code]
| Channel status Capture. When set to ‘1’, the channel status information is capturing, the bit will clear to ‘0’ after captured.   
`no operation` | `2` | `0x00`  
`SUNXI_SPDIF_RXCFG_CHSTSRC` | `3` | `Read/Write` | `0xb0` | ` `
[code]
        0 = RX_CH_STA Register holds status from Channel A
        1 = RX_CH_STA Register holds status from Channel B
       
    
[/code]
| Not used in code.   
`SUNXI_SPDIF_RXCFG_LOCKFLAG` | `4` | `Read/Write` | `0xb0` | ` `
[code]
        0 = unlock
        1 = lock
       
    
[/code]
| Not used in code.   
`no operation` | `5:31` | `0x00`  
##### SUNXI_SPDIF_TXFIFO
Default value: 0x00000000  
Offset: 0x0c 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_TXFIFO` | `0:31` | `Write` | `0x00000000` | `0xXXXXXXXX` | Write register for the transmitted data   
##### SUNXI_SPDIF_RXFIFO
Default value: 0x05b00000  
Offset: 0x10 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_RXFIFO` | `0:31` | `Read` | `0x00000000` | `0xXXXXXXXX` | Read register for the received data. Host can get one sample by reading this register, the A channel data is first and then the B channel data.   
##### SUNXI_SPDIF_FCTL
Default value(A20): 0x10709555  
Default value(A10): 0x15f09555  
Offset: 0x14 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_FCTL_RXOM` | `0:1` | `Read/Write` | `0x00000000` | ` `
[code]
       00 - Expanding “0” at LSB of SPDIP_RXFIFO register
       01 - Expanding received sample sign bit at MSB of OWA_RXFIFO register
       10 - Truncating received samples at high half­word of OWA_RXFIFO register and low half­word of AC_FIFO register is filled by “0”
       11 - Truncating received samples at low half­word of OWA_RXFIFO register and high half­word of AC_FIFO register is expanded by its sign bit
     
    
[/code]
| Reciever Fifo Control Receiver Output Mode(Mode 0,1,2,3). Set to 3 in code. 
[code] 
       Mode0: RXFIFO[31:0] = {FIFO_O[23:0], 8’h0}
       Mode 1: RXFIFO[31:0] = {8’FIFO_O[23], FIFO_O[23:0]}
       Mode 2: RXFIFO[31:0] = {FIFO_O[23:8], 16’h0}
       Mode 3: RXFIFO[31:0] = {16’FIFO_O[23], FIFO_O[23:8]}
    
[/code]  
`SUNXI_SPDIF_FCTL_TXIM` | `2` | `Read/Write` | `0x00000000` | `` | Transmitter Fifo Control Input Mode(Mode 0,1). Set to 1 in code. 
[code] 
       0: Valid data at the MSB of OWA_TXFIFO register
       1: Valid data at the LSB of OWA_TXFIFO register
    
[/code]
Example for 20­bits transmitted audio sample: 
[code] 
       Mode 0: FIFO_I[23:0] = {TXFIFO[31:12], 4’h0}
       Mode 1: FIFO_I[23:0] = {TXFIFO[19:0], 4’h0}
    
[/code]  
`SUNXI_SPDIF_FCTL_RXTL` | `3:7` | `Read/Write` | `0x0000000F` | `` | Fifo Control Receive FIFO Trigger Level. Set to 15 in code. Interrupt and DMA request trigger level for RX FIFO normal condition. Trigger Level = RXTL + 1   
`SUNXI_SPDIF_FCTL_TXTL` | `8:12` | `Read/Write` | `0x00000010` | `` | Interrupt and DMA request trigger level for TX FIFO normal condition. Set to 16 in code.   
`no operation` | `13:15` | `0x00`  
`SUNXI_SPDIF_FCTL_FRX` | `16` | `Read/Write` | `0xb0` | `` | Fifo Control Flush Reciever FIFO. Write “1” to flush RX FIFO, self clear to “0”   
`SUNXI_SPDIF_FCTL_FTX` | `17` | `Read/Write` | `0xb0` | `` | Fifo Control Flush Transmittion FIFO. Write “1” to flush TX FIFO, self clear to “0”   
`no operation` | `18:30` | `0x00`  
`SUNXI_SPDIF_FCTL_FIFOSRC` | `31` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| Not sure what this does. Isn't really used by driver. In the H3 documentation it is described as a enabler for the Audio Hub.   
##### SUNXI_SPDIF_FSTA
Default value: 0x00000600  
Offset: 0x18 
This register doesn't seem to be used by the driver so it's difficult to judge what it does. 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_RXA_CNT` | `0:5` | `Read` | `0xb0` | `` | RX FIFO Available Sample Word Counter.   
`SUNXI_SPDIF_FSTA_RXA` | `6` | `Read` | `0xb0` | ` `
[code]
        0 = No available data in RX FIFO
        1 = More than one sample in RX FIFO ( >=1 word )
       
    
[/code]
| RX FIFO Available. Not used by driver.   
`no operation` | `7` | `0x00`  
`SUNXI_SPDIF_TXE_CNT` | `8:13` | `Read` | `0xb0` | `` | TX FIFO Empty Space Word Counter.   
`SUNXI_SPDIF_FSTA_TXA` | `14` | `Read` | `0xb0` | ` `
[code]
        0 = No room for new sample in TX FIFO
        1 = More than one room for new sample in TX FIFO ( >=1 word )
       
    
[/code]
| TX FIFO Empty (indicate FIFO is not full)   
`no operation` | `15:31` | `0x00`  
##### SUNXI_SPDIF_INT
Default value: 0x00000f00  
Offset: 0x1C 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_INT_RXAIEN` | `0` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| RX FIFO Data Available Interrupt Enable. Not used by driver.   
`SUNXI_SPDIF_INT_RXOIEN` | `1` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| RX FIFO Overrun Interrupt Enable. Not used by driver.   
`SUNXI_SPDIF_INT_RXDRQEN` | `2` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| RX FIFO Data Available DMA Request Interrupt Enable for reciever. When set to “1”, RX FIFO DMA Request is asserted if Data is available in RX FIFO.   
`no operation` | `3` | `0x00`  
`SUNXI_SPDIF_INT_TXEIEN` | `4` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| TX FIFO Empty Interrupt Enable. Not used by driver.   
`SUNXI_SPDIF_INT_TXOIEN` | `5` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| TX FIFO Overrun Interrupt Enable. Not used by driver.   
`SUNXI_SPDIF_INT_TXUIEN` | `6` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| TX FIFO Underrun Interrupt Enable. Not used by driver.   
`SUNXI_SPDIF_INT_TXDRQEN` | `7` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| DMA Request Interrupt Enable for transmitter.   
`no operation` | `8:15` | `0xb0`  
`SUNXI_SPDIF_INT_RXPARERREN` | `16` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| Receiver Parity Error Enabled Interrupt. Not used by driver.   
`SUNXI_SPDIF_INT_RXUNLOCKEN` | `17/tt> ` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
       
    
[/code]
| Receiver Unlocked Enabled Interrupt. Not used by driver.   
`SUNXI_SPDIF_INT_RXLOCKEN` | `18` | `Read/Write` | `0xb0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| Receiver Locked Enabled Interrupt. Not used by driver.   
`no operation` | `19:31` | `0x00`  
##### SUNXI_SPDIF_ISTA
Default value: 0x00000000  
Offset: 0x20 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_ISTA_RXASTA` | `0` | `Read/Write` | `0xb0` | ` `
[code]
        0 = No Pending IRQ
        1 = Data Available Pending IRQ
      
    
[/code]
| SPDIF Receiver FIFO Available Pending Interrupt. Write “1” to clear this interrupt or automatically clear if interrupt condition fails. Not used by driver.   
`SUNXI_SPDIF_ISTA_RXOSTA` | `1` | `Read/Write` | `0xb0` | ` `
[code]
        0 = No Pending IRQ
        1 = FIFO Overrun Pending IRQ
      
    
[/code]
| SPDIF Receiver FIFO Overflow Pending Interrupt. Write 1 to clear. Not used by driver.   
`no operation` | `2:3` | `0x00`  
`SUNXI_SPDIF_ISTA_TXESTA` | `4` | `Read/Write` | `0xb0` | ` `
[code]
        0 = No Pending IRQ
        1 = FIFO Empty Pending IRQ
      
    
[/code]
| SPDIF Transmission FIFO Empty Pending Interrupt. Write 1 to clear or automatically clear if interrupt condition fails. Not used by driver.   
`SUNXI_SPDIF_ISTA_TXOSTA` | `5` | `Read/Write` | `0xb0` | ` `
[code]
        0 = No Pending IRQ
        1 = FIFO Overrun Pending IRQ
      
    
[/code]
| SPDIF Transmission FIFO Overrun Pending Interrupt. Write 1 to clear. Not used by driver.   
`SUNXI_SPDIF_ISTA_TXUSTA` | `6` | `Read/Write` | `0xb0` | ` `
[code]
        0 = No Pending IRQ
        1 = FIFO Underrun Pending IRQ
      
    
[/code]
| SPDIF Transmission FIFO Underrun Pending Interrupt. Write 1 to clear. Not used by driver.   
`no operation` | `7:15` | `0x00`  
`SUNXI_SPDIF_ISTA_RXPARERRSTA` | `16` | `Read/Write` | `0xb0` | ` `
[code]
        0 = No Pending IRQ
        1 = RX Parity Error Underrun Pending IRQ
      
    
[/code]
| SPDIF Receiver Parity Error Pending Interrupt. Write 1 to clear. Not used by driver.   
`SUNXI_SPDIF_ISTA_RXUNLOCKSTA` | `17` | `Read/Write` | `0xb0` | ` `
[code]
        0 = No Pending IRQ
        1 = RX Unlocked Pending IRQ
      
    
[/code]
| SPDIF Receiver Unlocked Pending Interrupt(RX_LOCK_FLAG 1→0). Write 1 to clear. Not used by driver.   
`SUNXI_SPDIF_ISTA_RXLOCKSTA` | `18` | `Read/Write` | `0xb0` | ` `
[code]
        0 = No Pending IRQ
        1 = RX Locked Pending IRQ
      
    
[/code]
| SPDIF Receiver Locked Pending Interrupt(RX_LOCK_FLAG 0→1) Write 1 to clear. Not used by driver.   
`no operation` | `19:31` | `0x00`  
##### SUNXI_SPDIF_TXCNT
Default value(A20): 0x0034814c?  
Default value(A10): 0x0534816c?  
Offset: 0x24 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_TXCNT` | `0:31` | `Read` | `0x00000000` | `` | Count of the level for the Transmit FIFO The audio sample number of writing into TX FIFO. When one sample is written by DMA or by host IO, the TX sample counter register increases by one. The TX Counter register can be set to any initial value at any time. After been updated by the initial value, the counter register should count on base of this value.   
##### SUNXI_SPDIF_RXCNT
Default value: 0x00000000  
Offset: 0x28 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_TXCNT` | `0:31` | `Read` | `0x00000000` | `` | Count of the level for the Receive FIFO The audio sample number of writing into RX FIFO. When one sample is written by Codec, the RX sample counter register increases by one. The RX Counter register can be set to any initial value at any time. After been updated by the initial value, the counter register should count on base of this value.   
##### SUNXI_SPDIF_TXCHSTA0
Default value: 0x00000000  
Offset: 0x30 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_TXCHSTA0_PRO` | `0` | `Read/Write` | `0xb0` | ` `
[code]
        0 = Consumer Application
        1 = Professional Application
      
    
[/code]
| PRO. Application type.Note: This bit must be fixed to “0”. Not used by driver.   
`SUNXI_SPDIF_TXCHSTA0_AUDIO` | `1` | `Read/Write` | `0xb0` | ` `
[code]
        0 = Linear PCM Samples
        1 = For none­linear PCM audio such as AC3, DTS, MPEG audio
      
    
[/code]
| Audio Data Type. Not used by driver.   
`SUNXI_SPDIF_TXCHSTA0_CP` | `2` | `Read/Write` | `0xb0` | ` `
[code]
        0 = copyright is asserted
        1 = no copyright is asserted
      
    
[/code]
| Copyright. Not used by driver.   
`SUNXI_SPDIF_TXCHSTA0_EMPHASIS` | `3:5` | `Read/Write` | `0x00` | `` | Emphasis For bit 1 = “0”, Linear PCM audio mode: 
[code] 
     000: 2 audio channels without pre­emphasis
     001: 2 audio channels with 50 μs / 15 μs pre­emphasis
     010: Reserved (for 2 audio channels with pre­emphasis)
     011: Reserved (for 2 audio channels with pre­emphasis)
     100~111: Reserved
    
[/code]
For bit 1 = “1”, other than Linear PCM applications: 
[code] 
     000: Default state
     001~111: Reserved
    
[/code]  
`SUNXI_SPDIF_TXCHSTA0_MODE` | `6:7` | `Read/Write` | `0x00` | ` `
[code]
        0 = Default Mode
        01~11 = Reserved
      
    
[/code]
| Mode. Not used by driver.   
`SSUNXI_SPDIF_TXCHSTA0_CATACOD` | `8:15` | `Read/Write` | `0x00` | `` | Category code Indicates the kind of equipment that generates the digital audio interface signal.   
`SUNXI_SPDIF_TXCHSTA0_SRCNUM` | `16:19` | `Read/Write` | `0x00` | `` | Source Number. Not used by driver.   
`SUNXI_SPDIF_TXCHSTA0_CHNUM` | `20:23` | `Read/Write` | `0x00` | `` | Channel Number. Driver always uses channel number 2.   
`SUNXI_SPDIF_TXCHSTA0_SAMFREQ` | `24:27` | `Read/Write` | `0x00` | ` `
[code]
        0000: 44.1kHz
        0001: not indicated 
        0010: 48kHz 
        0011: 32kHz 
        0100: 22.05kHz
        0101: Reserved 
        0110: 24kHz 
        0111: Reserved
        1000: Reserved
        1001: 768kHz
        1010: 96kHz
        1011: Reserved
        1100:176.4kHz
        1101: Reserved
        1110: 192kHz
        1111: Reserved
      
    
[/code]
| Sampling frequency   
`SUNXI_SPDIF_TXCHSTA0_CLK` | `28:29` | `Read/Write` | `0x00` | `
[code] 
        00: Level 2
        01: Level 1
        10: Level 3
        11: not matched
    
[/code]
``` | Clock Accuracy. Not used by driver.   
`no operation` | `30:31` | `0x00`  
##### SUNXI_SPDIF_TXCHSTA1
Default value: 0x00000000  
Offset: 0x34 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_TXCHSTA1_MAXWORDLEN` | `0` | `Read/Write` | `0xb0` | ` `
[code]
        0 = Maximum audio sample word length is 20 bits
        1 = Maximum audio sample word length is 24 bits
      
    
[/code]
| Max Word length. Not used by driver.   
`SUNXI_SPDIF_TXCHSTA1_SAMWORDLEN` | `1:3` | `Read/Write` | `0xb0` | `` | Sample word length. Set to 1 in driver. For bit 0 = “0”: 
[code] 
     000: not indicated
     001: 16 bits
     010: 18 bits
     100: 19 bits
     101: 20 bits
     111: Reserved
    
[/code]
For bit 0 = “1”: 
[code] 
     000: not indicated
     001: 20 bits
     010: 22 bits
     100: 23 bits
     101: 24 bits
     110: 21 bits
     111: Reserved
    
[/code]  
`SUNXI_SPDIF_TXCHSTA1_ORISAMFREQ` | `4:7` | `Read/Write` | `0xb0` | `
[code] 
        0000: not indicated
        0001: 192kHz
        0010: 12kHz
        0011: 176.4kHz
        0100: Reserved
        0101: 96kHz
        0110: 8kHz
        0111: 88.2kHz
        1000: 16kHz
        1001: 24kHz
        1010: 11.025kHz
        1011: 22.05kHz
        1100: 32kHz
        1101: 48kHz
        1110: Reserved
        1111: 44.1kHz
    
[/code]
``` | Original Sampling frequency.   
`SUNXI_SPDIF_TXCHSTA1_CGMSA` | `8:11` | `Read/Write` | `0x00` | `
[code] 
        00: Copying is permitted without restriction
        01: One generation of copies may be made
        10: Condition not be used
        11: No copying is permitted
    
[/code]
``` | Copying Manager?. Not used by driver.   
`no operation` | `12:31` | `0x00`  
##### SUNXI_SPDIF_RXCHSTA0
Default value(A20): 0x0034814c  
Default value(A10): 0x0040c20a  
Offset: 0x38 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_RXCHSTA0_PRO` | `0` | `Read/Write` | `0xb0` | ` `
[code]
        0 = Consumer Application
        1 = Professional Application
      
    
[/code]
| PRO. Application type.   
`SUNXI_SPDIF_RXCHSTA0_AUDIO` | `1` | `Read/Write` | `0xb0` | ` `
[code]
        0 = Linear PCM Samples
        1 = For none­linear PCM audio such as AC3, DTS, MPEG audio
      
    
[/code]
| Audio Data Type. Not used by driver.   
`SUNXI_SPDIF_RXCHSTA0_CP` | `2` | `Read/Write` | `0xb0` | ` `
[code]
        0 = copyright is asserted
        1 = no copyright is asserted
      
    
[/code]
| Copyright. Not used by driver.   
`SUNXI_SPDIF_RXCHSTA0_EMPHASIS` | `3:5` | `Read/Write` | `0x00` | `` | Emphasis For bit 1 = “0”, Linear PCM audio mode: 
[code] 
     000: 2 audio channels without pre­emphasis
     001: 2 audio channels with 50 μs / 15 μs pre­emphasis
     010: Reserved (for 2 audio channels with pre­emphasis)
     011: Reserved (for 2 audio channels with pre­emphasis)
     100~111: Reserved
    
[/code]
For bit 1 = “1”, other than Linear PCM applications: 
[code] 
     000: Default state
     001~111: Reserved
    
[/code]  
`SUNXI_SPDIF_RXCHSTA0_MODE` | `6:7` | `Read/Write` | `0x00` | ` `
[code]
        0 = Default Mode
        01~11 = Reserved
      
    
[/code]
| Mode. Not used by driver.   
`SSUNXI_SPDIF_RXCHSTA0_CATACOD` | `8:15` | `Read/Write` | `0x00` | `` | Category code Indicates the kind of equipment that generates the digital audio interface signal.   
`SUNXI_SPDIF_RXCHSTA0_SRCNUM` | `16:19` | `Read/Write` | `0x00` | `` | Source Number. Not used by driver.   
`SUNXI_SPDIF_RXCHSTA0_CHNUM` | `20:23` | `Read/Write` | `0x00` | `` | Channel Number. Not used by driver.   
`SUNXI_SPDIF_RXCHSTA0_SAMFREQ` | `24:27` | `Read/Write` | `0x00` | ` `
[code]
        0000: 44.1kHz
        0001: not indicated 
        0010: 48kHz 
        0011: 32kHz 
        0100: 22.05kHz
        0101: Reserved 
        0110: 24kHz 
        0111: Reserved
        1000: Reserved
        1001: 768kHz
        1010: 96kHz
        1011: Reserved
        1100:176.4kHz
        1101: Reserved
        1110: 192kHz
        1111: Reserved
      
    
[/code]
| Sampling frequency   
`SUNXI_SPDIF_RXCHSTA0_CLK` | `28:29` | `Read/Write` | `0x00` | ` `
[code]
        00: Level 2
        01: Level 1
        10: Level 3
        11: not matched
       
    
[/code]
| Clock Accuracy. Not used by driver.   
`no operation` | `30:31` | `0x00` |  |   
##### SUNXI_SPDIF_RXCHSTA1
Default value(A20): 0x90000060  
Default value(A10): 0x00000000  
Offset: 0x3c 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`SUNXI_SPDIF_RXCHSTA1_MAXWORDLEN` | `0` | `Read/Write` | `0xb0` | ` `
[code]
        0 = Maximum audio sample word length is 20 bits
        1 = Maximum audio sample word length is 24 bits
      
    
[/code]
| Max Word length. Not used by driver.   
`SUNXI_SPDIF_RXCHSTA1_SAMWORDLEN` | `1:3` | `Read/Write` | `0xb0` | `` | Sample word length. Set to 1 in driver. For bit 0 = “0”: 
[code] 
     000: not indicated
     001: 16 bits
     010: 18 bits
     100: 19 bits
     101: 20 bits
     110: 17 bits
     111: Reserved
    
[/code]
For bit 0 = “1”: 
[code] 
     000: not indicated
     001: 20 bits
     010: 22 bits
     100: 23 bits
     101: 24 bits
     110: 21 bits
     111: Reserved
    
[/code]  
`SUNXI_SPDIF_RXCHSTA1_ORISAMFREQ` | `4:7` | `Read/Write` | `0xb0` | ` `
[code]
        0000: not indicated
        0001: 192kHz
        0010: 12kHz
        0011: 176.4kHz
        0100: Reserved
        0101: 96kHz
        0110: 8kHz
        0111: 88.2kHz
        1000: 16kHz
        1001: 24kHz
        1010: 11.025kHz
        1011: 22.05kHz
        1100: 32kHz
        1101: 48kHz
        1110: Reserved
        1111: 44.1kHz
      
    
[/code]
| Original Sampling frequency.   
`SUNXI_SPDIF_RXCHSTA1_CGMSA` | `8:11` | `Read/Write` | `0x00` | ` `
[code]
        00: Copying is permitted without restriction
        01: One generation of copies may be made
        10: Condition not be used
        11: No copying is permitted
      
    
[/code]
| Copying Manager?. Not used by driver.   
`no operation` | `12?:31` | `0x00` |  |   
#### SUNXI SPDIF DEFAULT VALUES
To be confirmed! 
##### default a20 registers
[code] 
    01c22c00: 00000000 00001000 00808000 00000000    ................
    01c22c10: 05b00000 10709555 00000600 00000f00    ....U.p.........
    01c22c20: 00000000 00000000 0034814c 00000000    ........L.4.....
    01c22c30: 00000000 00000000 0040c20a 90000060    ..........@.`...
    
[/code]
##### default a10 registers
[code] 
    01c22c00: 00000000 00000f00 00808000 00000000    ................
    01c22c10: 05b00000 15f09555 00000600 00000f00    ....U...........
    01c22c20: 00000000 00000000 0534816c 00000000    ........l.4.....
    01c22c30: 00000000 00000000 00409200 00000000    ..........@.....
    
[/code]
