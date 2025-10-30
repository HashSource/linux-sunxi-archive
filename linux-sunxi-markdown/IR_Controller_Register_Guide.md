# IR Controller Register Guide
**From A10/A13/A20 User manuals** :  
Infrared Interface (IR) supports CIR, MIR, and FIR modes. The IR includes the following features: 
  * Compliant with IrDA 1.1 for MIR and FIR
  * Full physical layer implementation
  * Support 0.576 Mbit/sec and 1.152 Mbit/sec Medium Infrared (MIR) physical layer protocol
  * Support 4 Mbit/sec FIR physical layer protocol defined by IrDA version 1.4
  * Support CIR for remote control or wireless keyboard
  * Hardware CRC16 for MIR and CRC32 for FIR
  * Dual FIFOs for data transfer: 
    * 16x8-bits on A10/A13
    * 64x8-bits on A20
  * Programmable FIFO thresholds
  * Support Interrupt and DMA

**A23/sun8i** does not have IR controller. 
# IR Controller registers
  * IR0 base: `0x01c21800`
  * IR1 base: `0x01c21c00` **(not present on A13?)**
  * Source manuals: **A10, A20**

Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[IR_CTL][25349]` | `0x00` | `4B` | IR Control Register   
`[IR_TXCTL][25350]` | `0x04` | `4B` | IR Transmitter Configure Register **Disabled on A13?**  
`[IR_TXADR][25351]` | `0x08` | `4B` | IR Transmitter Address Register **Disabled on A13?**  
`[IR_TXCNT][25352]` | `0x0c` | `4B` | IR Transmitter Counter Register **Disabled on A13?**  
`[IR_RXCTL][25353]` | `0x10` | `4B` | IR Receiver Control Register   
`[IR_RXADR][25354]` | `0x14` | `4B` | IR Receiver Address Register **Disabled on A13?**  
`[IR_RXCNT][25355]` | `0x18` | `4B` | IR Receiver Counter Register **Disabled on A13?**  
`[IR_TXFIFO][25356]` | `0x1C` | `4B` | IR Transmitter FIFO Register **Disabled on A13?**  
`[IR_RXFIFO][25357]` | `0x20` | `4B` | IR Receiver FIFO Register   
`[IR_TXINT][25358]` | `0x24` | `4B` | IR Transmitter IRQ Control Register **Disabled on A13?**  
`[IR_TXSTA][25359]` | `0x28` | `4B` | IR Transmitter Status Register **Disabled on A13?**  
`[IR_RXINT][25360]` | `0x2C` | `4B` | IR Receiver IRQ Control Register   
`[IR_RXSTA][25361]` | `0x30` | `4B` | IR Receiver Status Register   
`[IR_CIR][25362]` | `0x34` | `4B` | CIR Configure Register   
## Memory Map
[code] 
    01c21800: 00000000 00000004 00000000 00000000    ................
    01c21810: 00000004 00000000 00000000 00000000    ................
    01c21820: 00000000 00000000 00001030 00000000    ........0.......
    01c21830: 00000000 00001828 00000000 00000000    ....(...........
[/code]
## IR_CTL
  * **Default value** : `00000000`
  * **Offset** : 0x00
  * Source manuals: **A10, A13, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`GEN` | `0` | `R/W` | `0` | `0/1` | Global Enable - enables/disables block and flushes all FIFOs 
  * `0`: disable
  * `1`: enable

  
`RXEN` | `1` | `R/W` | `0` | `0/1` | RX block enable 
  * `0`: disable
  * `1`: enable

  
`TXEN` | `2` | `R/W` | `0` | `0/1` | TX block enable 
  * `0`: disable
  * `1`: enable

**Not available on A13?**  
`LOOP` | `3` | `R/W` | `0` | `0/1` | Allows setting loopback mode which connects FRXD to FTXD 
  * `0`: normal mode
  * `1`: loopback mode

**Not mentioned in A20 manual** **Not available on A13?**  
`MD` | `4:5` | `R/W` | `00` | `0b00...0b11` | IrDA mode selection 
  * `00`: 0.576 Mbit/s MIR mode (**Unused on A13**)
  * `01`: 1.152 Mbit/s MIR mode (**Unused on A13**)
  * `10`: 4.0 Mbit/s FIR mode (**Unused on A13**)
  * `11`: CIR mode

  
`` | `6:7` | `` | `` | `` | \-   
`CGPO` | `8` | `R/W` | `0` | `0/1` | General Program Output (GPO) control in CIR mode 
  * `0`: low level
  * `1`: high level

  
`` | `9:31` | `` | `` | `` | \-   
## IR_TXCTL
  * **Default value** : `0x00000004`
  * **Offset** : 0x04
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `0:1` | `` | `` | `` | \-   
`TPPI` | `2` | `R/W` | `1` | `0/1` | Transmit Pulse Polarity Invert setting 
  * `0`: regular transmit pulse
  * `1`: Inverted transmit pulse

  
`SIP` | `3` | `R/W` | `0` | `0` | Transmit SIP Writing '1' produces 'Serial Infrared Interaction Pulse' transmission. Writing '0' to this bit is ignored and is always read as '0'. If this bit is set while in the middle of transfer, the packet will be ignored by IrDA controller. Don't set SIP bit in the middle of transfer. A SIP is defined as 1.6us optical pulse of the transmitter followed by a 7.1us off time of transmitter. It simulates a start pulse, causing the potentially interfering system to listen for at least 500ms.   
`` | `4` | `` | `` | `` | \-   
`PCF` | `5` | `R/W` | `0` | `0/1` | Packet Complete by FIFO This bit determines how a packet is completed if a TX FIFO underrun event occurs. The value of this bit selects between two recovery modes: 
  * 0: Send CRC and STO fields 
    * CRC16+STO for MIR
    * CRC32+STO for FIR
  * 1: Send packet abort symbol 
    * `0b111111` for MIR
    * `0b0000000` for FIR

  
`` | `6:31` | `` | `` | `` | \-   
## IR_TXADR
  * **Default value** : `0x00000000`
  * **Offset** : 0x08
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TPA` | `0:7` | `R/W` | `0` | `` | Transmit Packet Address This field contains the 8-bit Transmit Packet Address. If the HAG bit is cleared, the TPA bits have no effect   
`HAG` | `8` | `R/W` | `0` | `0/1` | Hardware Address Generator When this bit is set, the content of the TPA bits is transmitted as a packet address. When the bit is cleared, the packet address is read from TX FIFO. 
  * `0`: Read packet address from TX FIFO
  * `1`: Use TPA bits as packet address

  
`` | `9:31` | `` | `` | `` | \-   
## IR_TXCNT
  * **Default value** : `0x00000000`
  * **Offset** : 0x0C
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TPL` | `0:10` | `R/W` | `0` |  | Transmit Packet Length This field contains the length of the address, control and data. Length is N+1 bytes 
  * `0x000 / 0`: 1 byte
  * ...
  * `0x7ff / 2047`: 2048 bytes

  
`` | `11:31` | `` | `` | `` | \-   
## IR_RXCTL
  * **Default value** : `0x00000004`
  * **Offset** : 0x10
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `0:1` | `` | `` | `` | \-   
`RPPI` | `2` | `R/W` | `1` | `0/1` | Receiver Pulse Polarity Invert 
  * `0`: uninverted receiver signal
  * `1`: inverted receiver signal

  
`RPA` | `3` | `R/W` | `0` | `0/1` | Receiver Packet Abort bit. Determines behaviour of the RX FIFO upon detection of an illegal symbol. When an illegal symbol is detected, the DDE or CRCE bit in the receiver status register is set. If the RPA bit is set, the RX FIFO pointers are cleared and the receiver starts to search for the PA or STA field for FIR and MIR mode, respectively. If RPA is cleared, the receiver continues to write to the RX FIFO. 
  * `0`: Does not clear RX FIFO when illegal symbol received
  * `1`: Clear RX FIFO when illegal symbol received

  
`` | `4:31` | `` | `` | `` | \-   
## IR_RXADR
  * **Default value** : `0x00000000`
  * **Offset** : 0x14
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`RA` | `0:7` | `R/W` | `0` | `` | Receiver Address The value of this bit can be changed when RXEN bit is cleared.   
`RAM` | `8` | `R/W` | `0` | `0/1` | Receiver Address Match Determines whether to accept message into RX FIFO based on packet address. 
  * `0`: no address matching required. When a new packet is received, address, control and data fields are filled into RX FIFO.
  * `1`: packet address must match RA bits. If address matches, the control and data fields are filled into RX FIFO, excluding the address field.

The value of this bit can be changed when RXEN bit is cleared.   
`` | `9:31` | `` | `` | `` | \-   
## IR_RXCNT
  * **Default value** : `0x00000000`
  * **Offset** : 0x18
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`RPL` | `0:11` | `R` | `0` |  | Receiver Packet Length This field contains the length of the address, control and data. It is automatically cleared by IrDA controller when new packet is received. 
  * `0`: 0 bytes received
  * ...
  * `N`: N bytes received

  
`` | `12:31` | `` | `` | `` | \-   
## IR_TXFIFO
  * **Default value** : `0x00000000`
  * **Offset** : 0x1C
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TX_DATA` | `0:7` | `W` | `0` | `` | Transmitter Byte FIFO   
`` | `8:31` | `` | `` | `` | \-   
## IR_RXFIFO
  * **Default value** : `0x00000000`
  * **Offset** : 0x20
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`RX_DATA` | `0:7` | `R` | `0` | `` | Receiver Byte FIFO   
`` | `8:31` | `` | `` | `` | \-   
## IR_TXINT
  * **Default value** : `0x00000000`
  * **Offset** : 0x24
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TUI_EN` | `0` | `R/W` | `0` | `0/1` | Transmitter FIFO Underrun Interrupt Enable `0: disable, 1: enable`  
`TPEI_EN` | `1` | `R/W` | `0` | `0/1` | Transmitter Packet (address, control and data fields) End Interrupt Enable `0: disable, 1: enable`  
`SIPEI_EN` | `2` | `R/W` | `0` | `0/1` | Transmitter SIP End Interrupt Enable `0: disable, 1: enable`  
`TCI_EN` | `3` | `R/W` | `0` | `0/1` | Transmit (including CRC and STO fields) Complete Interrupt Enable `0: disable, 1: enable`  
`TEI_EN` | `4` | `R/W` | `0` | `0/1` | TX FIFO Empty Interrupt Enable When set to `1`, the TX FIFO interrupt is asserted if reaching TEL. The interrupt is de-asserted when condition fails or specified amount of data has been sent from host CPU. `0: disable, 1: enable`  
`DRQ_EN` | `5` | `R/W` | `0` | `0/1` | TX FIFO Empty DMA Enable When set to `1`, the TX FIFO DRQ is asserted if reaching TEL. The DRQ is de-asserted when condition fails or specified amount of data has been sent from host CPU. `0: disable, 1: enable`  
`` | `6:7` | `` | `` | `` | \-   
`TEL` | `8:11` | `R/W` | `0` | `` | TX FIFO Empty Level for interrupt and DMA request `TRIGGER_LEVEL = TEL + 1`  
`` | `12:31` | `` | `` | `` | \-   
## IR_TXSTA
  * **Default value** : `0x00001010`
  * **Offset** : 0x28
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TU` | `0` | `R/W` | `0` | `0/1` | Transmitter FIFO Underrun. `0: no underrun, 1: FIFO is underrun` This bit is cleared by writing a '1'.   
`TPE` | `1` | `R/W` | `0` | `0/1` | Transmitter Packet End `0: packet (address, control and data fields) transmission in progress, 1: packet transmission completed` This bit is cleared by writing a '1'.   
`SIPE` | `2` | `R/W` | `0` | `0/1` | Transmitter SIP End `0: transmission of SIP in progress, 1: transmission of SIP completed` This bit is cleared by writing a '1'.   
`TC` | `3` | `R/W` | `0` | `0/1` | Transmit (including CRC, STO fields) Complete `0: transmission in progress, 1: transmission completed` This bit is cleared by writing a '1'.   
`TE` | `4` | `R/W` | `0` | `0/1` | TX FIFO empty `0: TX FIFO not empty, 1: TX FIFO empty by its level` This bit is cleared by writing a '1'.   
`` | `5:7` | `` | `` | `` | \-   
`TA` | `8:12` | `R` | `0` | `0x00..0x16` | TX FIFO Available room counter 
  * `0`: TX FIFO Full
  * `1`: TX FIFO room for 1 byte of new data
  * ...
  * `16`: TX FIFO room for 16 bytes of new data (FIFO is empty)
  * others: reserved

  
`` | `13:31` | `` | `` | `` | \-   
## IR_RXINT
  * **Default value** : `0x00000000`
  * **Offset** : 0x2C
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`ROI_EN` | `0` | `R/W` | `0` | `0/1` | Receiver FIFO Overrun Interrupt Enable 
  * `0`: disable
  * `1`: enable

  
`RPEI_EN` | `1` | `R/W` | `0` | `0/1` | Receiver Packet End Interrupt Enable 
  * `0`: disable
  * `1`: enable

  
`RISI_EN` | `2` | `R/W` | `0` | `0/1` | Receiver Illegal Symbol Interrupt Enable 
  * `0`: disable
  * `1`: enable

  
`CRCI_EN` | `3` | `R/W` | `0` | `0/1` | Receiver CRC Error Interrupt Enable 
  * `0`: disable
  * `1`: enable

  
`RAI_EN` | `4` | `R/W` | `0` | `0/1` | RX FIFO Available Interrupt Enable When set to `1`, the RX FIFO IRQ is asserted if reaching RAL. The IRQ is de-asserted when condition fails. 
  * `0`: disable
  * `1`: enable

  
`DRQ_EN` | `5` | `R/W` | `0` | `0/1` | RX FIFO DMA Enable When set to `1`, the RX FIFO DRQ is asserted if reaching RAL. The DRQ is de-asserted when condition fails. 
  * `0`: disable
  * `1`: enable

  
`` | `6:7` | `` | `` | `` | \-   
`RAL` | `8:11` | `R/W` | `0` | `` | RX FIFO Available Received Byte Level for interrupt and DMA request `TRIGGER_LEVEL = RAL + 1`  
`` | `12:31` | `` | `` | `` | \-   
## IR_RXSTA
  * **Default value** : `0x00000000`
  * **Offset** : 0x30
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`ROI` | `0` | `R/W` | `0` | `0/1` | Receiver FIFO Overrun status 
  * `0`: no overrun
  * `1`: RX FIFO overrun

This bit is cleared by writing a '1'.   
`RPE` | `1` | `R/W` | `0` | `0/1` | Receiver Packet End Flag 
  * MIR/FIR mode: 
    * `0`: STO not detected
    * `1`: STO field or packet abort symbol detected (`0b0000000-MIR`, `0b00000000-FIR`)
  * CIR mode: 
    * `0`: symbol in progress or not detected
    * `1`: symbol received

This bit is cleared by writing a '1'.   
`RIS` | `2` | `R/W` | `0` | `0/1` | Receiver Illegal Symbol Flag 
  * `0`: no illegal symbols detected in packet
  * `1`: illegal symbol in address, control, data or CRC field

This bit is cleared by writing a '1'.   
`CRC` | `3` | `R/W` | `0` | `0/1` | Receiver CRC Error Flag 
  * `0`: no CRC failure
  * `1`: CRC failure

This bit is cleared by writing a '1'.   
`RA` | `4` | `R/W` | `0` | `0/1` | RX FIFO available 
  * `0`: RX FIFO not available according to its level
  * `1`: RX FIFO available according to its level

This bit is cleared by writing a '1'.   
`` | `5:7` | `` | `` | `` | \-   
`RAC` | `8:12` | `R` | `0` | `0..16` | RX FIFO Available Counter 
  * `0`: no available data in RX FIFO
  * `1`: 1 byte of data in RX FIFO
  * ...
  * `16`: 16 bytes of new data in RX FIFO

  
`` | `13:31` | `` | `` | `` | \-   
## IR_CIR
  * **Default value** : `0x00001828`
  * **Offset** : 0x34
  * Source manuals: **A10, A20**

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`SCS` | `0:1` | `R/W` | `0` | ` ` | Sample Clock Select for CIR  | SCS2 | SCS[1] | SCS[0] | Sample Clock   
---|---|---|---  
0 | 0 | 0 | `ir_clk/64`  
0 | 0 | 1 | `ir_clk/128`  
0 | 1 | 0 | `ir_clk/256`  
0 | 1 | 1 | `ir_clk/512`  
1 | 0 | 0 | `ir_clk`  
1 | 0 | 1 | reserved   
1 | 1 | 0 | reserved   
1 | 1 | 1 | reserved   
`NTHR` | `2:7` | `R/W` | `0xa` | `0..61` | Noise Threshold for CIR When the duration of signal pulse (H or L) is less than NTHR, the pulse is taken as noise and will be discarded by hardware. 
  * `0`: Noise threshold disabled, all samples are recorded into RX FIFO
  * `1`: If signal length is only one sample duration, it is discarded
  * `2`: If signal length is only <= 2 sample durations, it is discarded
  * ...
  * `61`: If signal length is only <= 61 sample durations, it is discarded

  
`ITHR` | `8:15` | `R/W` | `0x18` | `` | Idle Threshold for CIR The Receiver uses it to decide whether the CIR command has been received. If there is no CIR signal on the air, the receiver stays in the IDLE status. One active pulse will take the receiver from IDLE to Receiving status. After CIR is finished, the input signal will keep the specified level (H or L) for a long time. The receiver can use this idle signal duration to decide whether it has received the CIR command. The corresponding flag is asserted. If the corresponding interrupt is enabled, the interrupt line is asserted to CPU. When the duration of signal keeps one status for the specified duration:  
`((ITHR + 1)*128 * sample_clk)`, this means that the previous CIR command has been finished.   
`` | `16:23` | `` | `` | `` | \-   
`SCS2` | `24` | `R/W` | `0` | `0/1` | Bit2 of Sample Clock Select for CIR This bit is used together with SCS bits below. **Not present on A10?**  
`` | `25:31` | `` | `` | `` | \-
