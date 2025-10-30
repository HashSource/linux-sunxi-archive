# Reduced Serial Bus
The RSBTM is a push-pull two wire bus developed by Allwinner Technology. Its primary (only?) use is to connect an (Allwinner) SoC to an AXP-series power management controller (PMIC) from X-Powers. 
## Contents
  * [1 Features][47090]
  * [2 Documentation][47091]
  * [3 Registers][47092]
    * [3.1 Register list][47093]
    * [3.2 CTRL][47094]
    * [3.3 CCR][47095]
    * [3.4 INTE][47096]
    * [3.5 STATUS][47097]
      * [3.5.1 Transfer error codes][47098]
    * [3.6 LCR][47099]
    * [3.7 PMCR][47100]
    * [3.8 CMD][47101]
    * [3.9 SADDR][47102]
  * [4 Hardware Addresses][47103]
  * [5 Example transactions][47104]

# Features
  * Related to the SMBus, which in turn is derived from I²C.
  * Connects to the SoC-internal AMBA Peripheral Bus (APB).
  * Supports speeds up to 20 MHz (in contrast to the 400 KHz of I²C).
  * Supports multiple devices, although most (all?) boards connect the pins to the only on-board PMIC.
  * Multiplexed with some I²C pins (allows driving slaves with I²C for compatibility).
  * Supports programmable output delay of CD signal.
  * Supports parity check for address and data transmission.
  * Included in [A23][47105], [A33][47106], [A80][47107], [A83T][47108], [H3][47109](?) and [A64][47110] SoCs.

# Documentation
The RSB is briefly mentioned (along with MMIO address and IRQ number) in the A23, A33 and A64 manuals, but explained in more detail (including a register description) in the A80 and A83 manuals. 
# Registers
This list was originally gained from Allwinner code, but was later extended with the help of the manuals. 
## Register list
Offset | Name | Description   
---|---|---  
0x00 | CTRL | Control   
0x04 | CCR | Clock control   
0x08 | INTE | Interrupt enable   
0x0C | STAT | Interrupt status (write 1 to clear)   
0x10 | DADDR0 | Register address within the slave   
0x14 | DADDR1 |   
0x18 | DLEN | (Not sure if this exists)   
0x1C | DATA0 | Up to four data bytes   
0x20 | DATA1 |   
0x24 | LCR | Line control register   
0x28 | PMCR | PMIC init register   
0x2C | CMD | Command for next transaction   
0x30 | SADDR | Slave address   
The DLEN register seems to be hardwired to 0 in most recent implementations and is redundant with the CMD register. According to documentation it holds the transfer length (1, 2 or 4 Bytes) in the lower two bits and the read(=1)/write(=0) indicator in bit 4. 
## CTRL
Bit | Name | Description | Value | R/W | Default   
---|---|---|---|---|---  
31-9 | Reserved   
8 | USE_RSB | Use RSB interface |  | RW | 0   
7 | START_TRANS | Start transfer | write 1 to start current transfer, resets to 0 when done | RW | 0   
6 | ABT_TRANS | Abort transfer | write 1 to abort current transfer, resets to 0 when done | RW | 0   
5-2 | Reserverd   
1 | GLB_INTEN | Enable interrupts | 1: enable | RW | 0   
0 | SOFT_RESET | Reset RSB controller, resets to 0 when done | write 1 to reset | RW | 0   
## CCR
This register controls the RSB bus clock (SCK) speed. 
Bit | Name | Description | Value | R/W | Default   
---|---|---|---|---|---  
31-9 | Reserved   
8 | CD_ODLY | ?? | cd_odly = !(div >> 1) | RW |   
7-0 | DIV | Clock divider | SCK = SRC / 2 / (DIV + 1) | RW |   
The reference clock is the 24 MHz oscillator, a common speed on most boards seems to be 3 MHz, so 0x103 is the value you most probably want to write into this register. 
## INTE
This register masks/unmasks interrupt events. 
Bit | Name | Description | R/W | Default   
---|---|---|---|---  
31-3 | Reserved   
2 | LBSY | Load busy (transfer in progress) | RW   
1 | TERR | Transfer error encountered | RW   
0 | TOVER | Transfer over (completed) | RW   
## STATUS
This register shows interrupt and transfer status. Write 1 to the corresponding bit to clear each interrupt. 
Bit | Name | Description | R/W | Default   
---|---|---|---|---  
31-24 | Reserved   
23-16 | TRANS_ERR_ID | Transfer error ID for transfer 0 | RW   
15-8 | TRANS_ERR_ID | Transfer error ID for transfer 0 | RW   
2 | LBSY | Load busy (transfer in progress) | RW   
1 | TERR | Transfer error encountered | RW   
0 | TOVER | Transfer over (completed) | RW   
### Transfer error codes
Bit | Description   
---|---  
15-9 | Reserved   
8 | No ACK when setting run-time slave address   
7-4 | Reserved   
3 | Error happened with the transmission of the 4th byte of data   
2 | Error happened with the transmission of the 3th byte of data   
1 | Error happened with the transmission of the 2th byte of data   
0 | Error happened with the transmission of the 1th byte of data   
## LCR
This register can seemingly be used to bit bang the bus. 
## PMCR
Educated guess: This register can be used to switch a PMIC from its reset-state configured I2C interface to RSB mode. This avoids configuring the pins to I2C and sending the switch sequence via standard I2C. 
## CMD
List of command codes 
Name | Value | Description   
---|---|---  
WR8 | 0x4E | Write byte   
WR16 | 0x59 | Write half word   
WR32 | 0x63 | Write word   
RD8 | 0x8B | Read byte   
RD16 | 0x9C | Read half word   
RD32 | 0xA6 | Read word   
SRTA | 0xE8 | Set run-time address   
## SADDR
This register is used with the SRTA command to connect a hardware address to a runtime address. 
Bit | Description   
---|---  
23-16 | Run-Time Slave Address   
15-0 | Hardware Slave Address   
# Hardware Addresses
RSB has hardware addresses and runtime addresses. Runtime addresses are configured at initialization time, and are used to talk to the slave devices. Hardware addresses are used to identify and configure runtime addresses. The configured runtime addresses are not queryable. 
Allwinner sources use a static mapping of hardware and runtime addresses. 
Hardware Address | (Static) Runtime Address | Known Devices   
---|---|---  
0x3a3 | 0x2d | AXP223, AXP809, AXP81X   
0x745 | 0x3a | AXP806   
0x3a3 | 0x2d | [AXP803][47111]  
0xe89 | 0x4e | AC100   
In contrast to the AXP 803 manual, the hardware address for it seems to be 0x3a3 instead of the documented 0x1d1. 
# Example transactions
For setting up the RSB controller in the first place, you have to: 
  * Configure the associated pins to connect to the RSB controller (Port Controller CPUs)
  * Configure the pins to be Pull-up level 2 drive strength (same Port Controller CPUs)
  * Un-gate the RSB clock (bit 3 in the APB0_CLK_GATING_REG (offset 0x28) in the R_PRCM block)
  * De-assert the RSB reset line (bit 3 in the APB0_SOFT_RST_REG (offset 0xB0) in the R_PRCM block)
  * Program the clock (CCR register) in the RSB block (1 cycle delay, 3 MHz)
  * Soft reset the RSB block (bit 0 in CTRL register)

After having setup the RSB block, a typical read transaction may look like: 
[code] 
    writel(rt_addr << 16, RSB_BASE + 0x30); /* set run-time address of slave */
    writel(0x8b, RSB_BASE + 0x2c);          /* "Read-one-byte" command into CMD register */
    writel(regnr, RSB_BASE + 0x10);         /* set register to be read */
    writel(0x80, RSB_BASE + 0x00);          /* start transaction */
    while (readl(RSB_BASE + 0x00) & 0x80)   /* poll for completion */
            ;
    ret = readl(RSB_BASE + 0x0c);           /* read status register */
    if (ret == 0x01)                        /* transaction completed without errors */
            return 0;
    return ret;
    
[/code]
