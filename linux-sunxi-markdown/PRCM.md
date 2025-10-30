# PRCM
The A31 and A23 SoCs contain a seperate module called PRCM, or "Power, Reset & Clock Management". 
The neighboring address space also has new IP blocks, such as a GPIO controller for PL/PM pins,   
shared UART, TWI, and the new P2WI (A31) or RSB (A23) controllers. These are not documented in the   
user manuals, but the address spaces and registers can be found in the A23 SDK.   

## Contents
  * [1 Power, Reset & Clock Management][43743]
    * [1.1 Overview][43744]
    * [1.2 Features][43745]
    * [1.3 Clocks][43746]
      * [1.3.1 Bus clock generation][43747]
    * [1.4 Registers][43748]
      * [1.4.1 CPUS_CFG][43749]
      * [1.4.2 APB0_CLK_DIV_REG][43750]
        * [1.4.2.1 A31][43751]
        * [1.4.2.2 A23][43752]
      * [1.4.3 APB0_GATING_REG][43753]
      * [1.4.4 APB0_MODULE_RST_REG][43754]
  * [2 R_PIO][43755]
    * [2.1 Pins][43756]
      * [2.1.1 A31][43757]
      * [2.1.2 A23][43758]
    * [2.2 Registers][43759]

# Power, Reset & Clock Management
## Overview
This module controls APB0 clocks, resets, and power domains. 
## Features
  * Support clock configuration
  * Support module reset
  * Support GPU power clamp control
  * Support system core power clamp control
  * Support one clock output channel

## Clocks
This module controls the clocks for the AR100 OpenRISC core (named CPU0 in some Allwinner sources), AHB0, APB0, and some special clocks in this cluster of IP blocks. 
### Bus clock generation
Name  | Input  | Output  | Defines  | Notes   
---|---|---|---|---  
AR100_CLK   
(CPU0_CLK)  | {LOSC, HOSC, PLL6}  |  I n p u t M × N {\displaystyle {\frac {\mathrm {Input} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times N}}}][43760] | ` `
[code]
        M = {1, 2 ... 32}  
    
        N = {1, 2, 4, 8}
      
    
[/code]
| Missing on A23   
AHB0_CLK  | AR100_CLK  |  I n p u t {\displaystyle Input} ![{\\displaystyle Input}][43761] |   
APB0_CLK  | AHB0_CLK  |  I n p u t N {\displaystyle {\frac {\mathrm {Input} }{N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{N}}}][43762] | ` `
[code]
        N = {1, 2, 4, 8}
      
    
[/code]  
R_ONE_WIRE_CLK  | {LOSC, HOSC}  |  I n p u t M × N {\displaystyle {\frac {\mathrm {Input} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times N}}}][43760] | ` `
[code]
        M = {1, 2 ... 32}  
    
        N = {1, 2, 4, 8}
      
    
[/code]
| A31 only   
R_CIR_CLK  | {LOSC, HOSC}  |  I n p u t M × N {\displaystyle {\frac {\mathrm {Input} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times N}}}][43760] | ` `
[code]
        M = {1, 2 ... 16}  
    
        N = {1, 2, 4, 8}
      
    
[/code]
| A31 only   
RTC_OUT_CLK  | unknown  |  I n p u t M × N {\displaystyle {\frac {\mathrm {Input} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times N}}}][43760] | ` `
[code]
        M = {1, 2 ... 32} (unsure)  
    
        N = {1, 2, 4, 8}
      
    
[/code]
| A31 only   
## Registers
Base address: 0x01f01400 
The registers are documented using the A23 user manual, with A31 bits added from Allwinner code. 
Offset | Name | Description | Notes   
---|---|---|---  
0x0000 | CPUS_CFG_REG | CPU0 (AR100) clock configuration | Most likely not available on A23   
0x0004 | Reserved |  |   
0x000C | APB0_CLK_DIV_REG | APB0 clock divide ratio   
0x0010 | CPU1_EN_REG | CPU1 clock/NEON enable | A31 only   
0x0014 | CPU2_EN_REG | CPU2 clock/NEON enable | A31 only   
0x0018 | CPU3_EN_REG | CPU3 clock/NEON enable | A31 only   
0x001C | CPU4_EN_REG | CPU4 clock/NEON enable | A31 only   
0x0020 | Reserved |  |   
0x0024 | Reserved |  |   
0x0028 | APB0_GATING_REG | APB0 clock gating control   
0x0040 | PLL_CTRL_REG0 | PLL control 0   
0x0044 | PLL_CTRL_REG1 | PLL control 1   
0x0050 | R_ONE_WIRE_CLK_REG | One Wire module special clock | A31 only   
0x0054 | R_CIR_CLK_REG | CIR module special clock | A31 only   
0x0064 | CPU1_PWR_CLAMP_STATUS | CPU1 power clamp status | A31 only   
0x00A4 | CPU2_PWR_CLAMP_STATUS | CPU2 power clamp status | A31 only   
0x00B0 | APB0_MODULE_RST_REG | APB0 module software reset control   
0x00E4 | CPU3_PWR_CLAMP_STATUS | CPU3 power clamp status | A31 only   
0x00F0 | RTC_CLK_OUT_REG | RTC external clock output control | A31 only   
0x0100 | CPU_PWROFF_GATING | CPU power off gating control   
0x0110 | VDD_SYS_PWROFF_GATING | VDD_SYS power off gating control   
0x0118 | GPU_PWROFF_GATING | GPU power off gating control   
0x0120 | VDD_SYS_PWR_RST | VDD_SYS power domain reset control   
0x0124 | CPU4_PWR_CLAMP_STATUS | CPU4 power clamp status | A31 only   
0x0140 | CPU1_PWR_CLAMP | CPU1 power clamp | A31 only   
0x0144 | CPU2_PWR_CLAMP | CPU2 power clamp | A31 only   
0x0148 | CPU3_PWR_CLAMP | CPU3 power clamp | A31 only   
0x014C | CPU4_PWR_CLAMP | CPU4 power clamp | A31 only   
0x01c0 | AUDIO_CFG | Audio codec configuration | A23 only   
0x01c4 | HMIC_EN | Headphone Mic detect digital part enable | A23 only   
0x01c8 | HMIC_CTL | HMIC detect control | A23 only   
0x01cc | HMIC_DATA | HMIC pending & data | A23 only   
### CPUS_CFG
Default value: unknown  
Offset: 0x0000 
C P U 0 _ C L K = C P U 0 _ C L K _ S R C M × N {\displaystyle CPU0\\_CLK={\frac {\mathrm {CPU0\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle CPU0\\_CLK={\\frac {\\mathrm {CPU0\\_CLK\\_SRC} }{M\\times N}}}][43763]
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `31:18` |  |  |   
`CPU0_CLK_SRC` | `17:16` | `Read/Write` | `0x01` | ` `
[code]
        0x00 = 32 KHz internal RC clock
        0x01 = 24 MHz external Oscillator
        0x02 = PLL6 (ratio?)
        0x03 = reserved
      
    
[/code]
| Change the CPU0 (AR100) Clock source. (test: After changing the clock source, at least 8 clock cycles need to pass before changes are active.)   
`reserved` | `15:13` |  |  |   
`CPU0_CLK_DIV_M` | `12:8` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x1f = 32
      
    
[/code]
| CPU0 clock divide factor M   
`reserved` | `7:6` |  |  |   
`CPU0_CLK_DIV_N` | `5:4` | `Read/Write` | `0x01` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| CPU0 clock divide factor N   
`reserved` | `3:0` |  |  |   
### APB0_CLK_DIV_REG
Default value: 0x00000000  
Offset: 0x000C 
#### A31
Allwiner A31 u-boot sources states: 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `31:2` |  |  |   
`APB0_CLK_RATIO` | `1:0` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = /2
        0x01 = /2
        0x02 = /4
        0x03 = /8
      
    
[/code]
| APB0 Clock divide ratio   
#### A23
The A23 manual states: 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `31:2` |  |  |   
`APB0_CLK_RATIO` | `1:0` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = /1
        0x01 = /2
        0x02 = /4
        0x03 = /8
      
    
[/code]
| APB0 Clock divide ratio   
### APB0_GATING_REG
Default value: 0x00000000  
Offset: 0x0028 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `31:7` |  |  |  |   
`R_TWI_GATING` | `6` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Gating APB clock for R_TWI   
`R_ONE_WIRE_GATING` | `5` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Gating APB clock for R_ONE_WIRE (A31 only)   
`R_UART_GATING` | `4` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Gating APB clock for R_UART   
`R_P2WI_GATING` | `3` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Gating APB clock for R_P2WI (R_RSB on A23)   
`R_TIMER0_1_GATING` | `2` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Gating APB clock for R_TIMER0_1   
`R_CIR_GATING` | `1` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Gating APB clock for R_CIR (A31 only)   
`R_PIO_GATING` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Gating APB clock for R_PIO   
### APB0_MODULE_RST_REG
Default value: 0x00000000  
Offset: 0x00B0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `31:7` |  |  |  |   
`R_TWI_RST` | `6` | `Read/Write` | `0x00` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| R_TWI reset control   
`R_ONE_WIRE_RST` | `5` | `Read/Write` | `0x00` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| R_ONE_WIRE reset control (A31 only)   
`R_UART_RST` | `4` | `Read/Write` | `0x00` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| R_UART reset control   
`R_P2WI_RST` | `3` | `Read/Write` | `0x00` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| R_P2WI (R_RSB on A23) reset control   
`R_TIMER0_1_RST` | `2` | `Read/Write` | `0x00` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| R_TIMER0_1 reset control   
`R_CIR_RST` | `1` | `Read/Write` | `0x00` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| R_CIR reset control (A31 only)   
`R_PIO_RST` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| R_PIO reset control   
# R_PIO
The A31 SoC (and SoCs based on the A31, such as the A23) has a separate pinmux/GPIO controller   
for the PL and PM pins. Sources for sun9iw1 in the A23 SDK also mention PN pins, possibly   
controlled from the same IP block. The SDK sources list this new controller as "R_PIO".   

## Pins
### A31
Port Bank L  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PL00``][43764]``` `` | P27  | I/O  | [S_TWI0_SCK][43765] | S_P2WI_SCK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PL01``][43766]``` `` | R25  | I/O  | [S_TWI0_SDA][43765] | S_P2WI_SDA  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PL02``][43767]``` `` | R24  | I/O  | [S_UART0_TX][43768] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PL03``][43769]``` `` | R22  | I/O  | [S_UART0_RX][43768] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PL04``][43770]``` `` | R26  | I/O  | S_IR0_RX  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PL05``][43771]``` `` | T21  | I/O  | EINT0  | [S_JTAG0_MS][43772] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PL06``][43773]``` `` | U21  | I/O  | EINT1  | [S_JTAG0_CK][43772] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PL07``][43774]``` `` | U22  | I/O  | EINT2  | [S_JTAG0_DO][43772] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PL08``][43775]``` `` | T22  | I/O  | EINT3  | [S_JTAG0_DI][43772] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
Port Bank M  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PM00``][43776]``` `` | M26  | I/O  | EINT0  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PM01``][43777]``` `` | M27  | I/O  | EINT1  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PM02``][43778]``` `` | K21  | I/O  | EINT2  | [1Wire0][43779] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PM03``][43780]``` `` | M22  | I/O  | EINT3  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PM04``][43781]``` `` | N24  | I/O  | EINT4  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PM05``][43782]``` `` | N25  | I/O  | EINT5  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PM06``][43783]``` `` | N26  | I/O  | EINT6  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PM07``][43784]``` `` | N27  | I/O  | EINT7  | RTC0_CLK0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
### A23
Port Bank L  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PL00``][43764]``` `` | ???  | I/O  | S_RSB_SCK  | [S_TWI0_SCK][43765] | EINT0  | _reserved_ | _reserved_ | _reserved_  
`[PL01``][43766]``` `` | ???  | I/O  | S_RSB_SDA  | [S_TWI0_SDA][43765] | EINT1  | _reserved_ | _reserved_ | _reserved_  
`[PL02``][43767]``` `` | ???  | I/O  | [S_UART0_TX][43768] | _reserved_ | EINT2  | _reserved_ | _reserved_ | _reserved_  
`[PL03``][43769]``` `` | ???  | I/O  | [S_UART0_RX][43768] | _reserved_ | EINT3  | _reserved_ | _reserved_ | _reserved_  
`[PL04``][43770]``` `` | ???  | I/O  | [S_JTAG0_MS][43772] | _reserved_ | EINT4  | _reserved_ | _reserved_ | _reserved_  
`[PL05``][43771]``` `` | ???  | I/O  | [S_JTAG0_CK][43772] | _reserved_ | EINT5  | _reserved_ | _reserved_ | _reserved_  
`[PL06``][43773]``` `` | ???  | I/O  | [S_JTAG0_DO][43772] | _reserved_ | EINT6  | _reserved_ | _reserved_ | _reserved_  
`[PL07``][43774]``` `` | ???  | I/O  | [S_JTAG0_DI][43772] | _reserved_ | EINT7  | _reserved_ | _reserved_ | _reserved_  
`[PL08``][43775]``` `` | ???  | I/O  | [S_TWI0_SCK][43765] | _reserved_ | EINT8  | _reserved_ | _reserved_ | _reserved_  
`[PL09``][43785]``` `` | ???  | I/O  | [S_TWI0_SDA][43765] | _reserved_ | EINT9  | _reserved_ | _reserved_ | _reserved_  
`[PL10``][43786]``` `` | ???  | I/O  | S_PWM0  | _reserved_ | EINT10  | _reserved_ | _reserved_ | _reserved_  
`[PL11``][43787]``` `` | ???  | I/O  | _reserved_ | _reserved_ | EINT11  | _reserved_ | _reserved_ | _reserved_  
## Registers
Base address: 0x01f02c00 
The register format is the same as the PIO controller.
