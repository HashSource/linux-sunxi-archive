# A80/Clock Control Module
< [A80][4479]
 
## Contents
  * [1 Clock Control Module][4482]
    * [1.1 Overview][4483]
    * [1.2 Clock generation][4484]
      * [1.2.1 PLL][4485]
      * [1.2.2 Bus clock generation][4486]
    * [1.3 Clock Control Module Registers][4487]
      * [1.3.1 CCM_PLL1_CFG][4488]
      * [1.3.2 CCM_PLL2_CFG][4489]
      * [1.3.3 CCM_PLL4_CFG][4490]
      * [1.3.4 CCM_PLL12_CFG][4491]
      * [1.3.5 CCM_APB0_GATE][4492]
      * [1.3.6 CCM_APB1_GATE][4493]
      * [1.3.7 CCM_APB0_RST][4494]
      * [1.3.8 CCM_APB1_RST][4495]

# Clock Control Module
## Overview
Allwinner's A80 has 12 [Phase Locking Loop's (PLL's)][4496], and a 24MHz main crystal oscillator. A low power 32.768 KHz clock is supplied externally, by the AC100 chip. 
The 24MHz crystal oscillator is mandatory and is responsible for supplying a clock source for the PLL. The 32kHz clock is only used by a few devices. 
Many devices being driving by any of these clocks have often 2 clocks connected to them. One of the clocks drives the module itself, the other clock matches the bus to whatever it is connected (usually the CPU). 
## Clock generation
All PLL's are fed from the 24 MHz reference clock. 
### PLL
Name  | Input  | Speed range  | Output  | Defines   
---|---|---|---|---  
PLL1  | 24 MHz  | `?? MHz - ?? GHz` |  24 M H z × N P {\displaystyle 24\,\mathrm {MHz} \times {\frac {N}{P}}} ![{\\displaystyle 24\\,\\mathrm {MHz} \\times {\\frac {N}{P}}}][4497] | ` ``N = {0, 1 ... 255}  
P = {1, 4}  
`  
PLL2  | 24 MHz  | `?? MHz - ?? GHz` |  24 M H z × N P {\displaystyle 24\,\mathrm {MHz} \times {\frac {N}{P}}} ![{\\displaystyle 24\\,\\mathrm {MHz} \\times {\\frac {N}{P}}}][4497] | ` ``N = {0, 1 ... 255}  
P = {1, 4}  
`  
PLL4  | 24 MHz  | `?? MHz - ?? GHz` |  24 M H z × N D 1 × D 2 {\displaystyle 24\,\mathrm {MHz} \times {\frac {N}{D_{1}\times D_{2}}}} ![{\\displaystyle 24\\,\\mathrm {MHz} \\times {\\frac {N}{D_{1}\\times D_{2}}}}][4498]  
  
| ` ``N = {0, 1 ... 255}  
D1 = {1, 2}  
D2 = {1, 2}  
`  
PLL12  | 24 MHz  | `?? MHz - ?? GHz` |  24 M H z × N D 1 × D 2 {\displaystyle 24\,\mathrm {MHz} \times {\frac {N}{D_{1}\times D_{2}}}} ![{\\displaystyle 24\\,\\mathrm {MHz} \\times {\\frac {N}{D_{1}\\times D_{2}}}}][4498]  
  
| ` ``N = {0, 1 ... 255}  
D1 = {1, 2}  
D2 = {1, 2}  
`  
### Bus clock generation
Name  | Input  | Output  | Defines   
---|---|---|---  
CLUSTER0  | {24MHZ, PLL1}  |  |   
CLUSTER1  | {24MHZ, PLL2}  |  |   
AXI0  | CLUSTER0  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][4499] | `M = {1, 2, 3, 4}`  
AXI1  | CLUSTER1  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][4499] | `M = {1, 2, 3, 4}`  
GT  | {24MHZ, PLL4, PLL12, PLL12}  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][4499] | `M = {1, 2, 3, 4}`  
AHB0  | {GT, PLL4, PLL12, PLL12}  |  I n p u t P {\displaystyle {\frac {\mathrm {Input} }{P}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{P}}}][4500] | `P = {1, 2, 4, 8}`  
AHB1  | {GT, PLL4, PLL12, PLL12}  |  I n p u t P {\displaystyle {\frac {\mathrm {Input} }{P}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{P}}}][4500] | `P = {1, 2, 4, 8}`  
AHB2  | {GT, PLL4, PLL12, PLL12}  |  I n p u t P {\displaystyle {\frac {\mathrm {Input} }{P}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{P}}}][4500] | `P = {1, 2, 4, 8}`  
APB0  | {24MHZ, PLL4}  |  I n p u t P {\displaystyle {\frac {\mathrm {Input} }{P}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{P}}}][4500] | `P = {1, 2, 4, 8}`  
APB1  | {24MHZ, PLL4}  |  I n p u t M × P {\displaystyle {\frac {\mathrm {Input} }{M\times P}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times P}}}][4501] | ` ``M = {1, 2 ... 32}  
P = {1, 2, 4, 8} `  
CCI400  | {24MHZ, PLL4, PLL12, PLL12}  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][4499] | `M = {1, 2, 3, 4}`  
## Clock Control Module Registers
Clock Control Module Base address: 0x06000000 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`CCM_PLL1_CFG` | `0x0000` | `4B` | `PLL1 Control (Cluster 0 CPU)`  
`CCM_PLL2_CFG` | `0x0004` | `4B` | `PLL2 Control (Cluster 1 CPU)`  
`CCM_PLL3_CFG` | `0x0008` | `4B` | `PLL3 Control (Audio)`  
`CCM_PLL4_CFG` | `0x000c` | `4B` | `PLL4 Control (Peripheral 0)`  
`CCM_PLL5_CFG` | `0x0010` | `4B` | `PLL5 Control (Video Engine)`  
`CCM_PLL6_CFG` | `0x0014` | `4B` | `PLL6 Control (DDR)`  
`CCM_PLL7_CFG` | `0x0018` | `4B` | `PLL7 Control (Video 0)`  
`CCM_PLL8_CFG` | `0x001c` | `4B` | `PLL8 Control (Video 1)`  
`CCM_PLL9_CFG` | `0x0020` | `4B` | `PLL9 Control (GPU)`  
`CCM_PLL10_CFG` | `0x0024` | `4B` | `PLL10 Control (Display Engine)`  
`CCM_PLL11_CFG` | `0x0028` | `4B` | `PLL11 Control (Image Signal Processor)`  
`CCM_PLL12_CFG` | `0x002c` | `4B` | `PLL12 Control (Peripheral 1)`  
`CCM_CPU_CFG` | `0x0050` | `4B` | `CPU Cluster clock mux`  
`CCM_AXI0_CFG` | `0x0054` | `4B` | `AXI0 bus clock division ratio`  
`CCM_AXI1_CFG` | `0x0058` | `4B` | `AXI1 bus clock division ratio`  
`CCM_GT_CFG` | `0x005c` | `4B` | `GT bus clock mux and division ratio`  
`CCM_AHB0_CFG` | `0x0060` | `4B` | `AHB0 bus clock mux and division ratio`  
`CCM_AHB1_CFG` | `0x0064` | `4B` | `AHB1 bus clock mux and division ratio`  
`CCM_AHB2_CFG` | `0x0068` | `4B` | `AHB2 bus clock mux and division ratio`  
`CCM_APB0_CFG` | `0x0070` | `4B` | `APB0 bus clock mux and division ratio`  
`CCM_APB1_CFG` | `0x0074` | `4B` | `APB1 bus clock mux and division ratio`  
`CCM_CCI_CFG` | `0x0078` | `4B` | `CCI clock mux and division ratio`  
`CCM_AHB0_GATE` | `0x0580` | `4B` | `AHB0 module clock gating`  
`CCM_AHB1_GATE` | `0x0584` | `4B` | `AHB1 module clock gating`  
`CCM_AHB2_GATE` | `0x0588` | `4B` | `AHB2 module clock gating`  
`CCM_APB0_GATE` | `0x0590` | `4B` | `APB0 module clock gating`  
`CCM_APB1_GATE` | `0x0594` | `4B` | `APB1 module clock gating`  
`CCM_AHB0_RST` | `0x05a0` | `4B` | `AHB0 module reset control`  
`CCM_AHB1_RST` | `0x05a4` | `4B` | `AHB1 module reset control`  
`CCM_AHB2_RST` | `0x05a8` | `4B` | `AHB2 module reset control`  
`CCM_APB0_RST` | `0x05b0` | `4B` | `APB0 module reset control`  
`CCM_APB1_RST` | `0x05b4` | `4B` | `APB1 module reset control`  
### CCM_PLL1_CFG
Default value: ??  
Offset: 0x0000 
Reserved   
---  
`CCM_PLL1_N` | `8:15` | `Read/Write` | `??` | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0xff = 255
      
    
[/code]
| PLL1 factor N   
`CCM_PLL1_P` | `16` | `Read/Write` | `0` | ` `
[code]
        0 = 1
        1 = 4
      
    
[/code]
| External factor P   
Reserved   
`??` | `25` | `Read/Write` | `0` |  | Set but Unknown   
Reserved   
`CCM_PLL1_EN` | `31` | `Read/Write` | `0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
|  24 M H z × N P {\displaystyle 24\,\mathrm {MHz} \times {\frac {N}{P}}} ![{\\displaystyle 24\\,\\mathrm {MHz} \\times {\\frac {N}{P}}}][4497]  
The default value for the output is ?? MHz.  
If bypass is disabled, the result must be `?? MHz - ?? GHz`  
### CCM_PLL2_CFG
Default value: ??  
Offset: 0x0004 
Reserved   
---  
`CCM_PLL2_N` | `8:15` | `Read/Write` | `??` | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0xff = 255
      
    
[/code]
| PLL2 factor N   
`CCM_PLL2_P` | `16` | `Read/Write` | `0` | ` `
[code]
        0 = 1
        1 = 4
      
    
[/code]
| External factor P   
Reserved   
`??` | `25` | `Read/Write` | `0` |  | Set but Unknown   
Reserved   
`CCM_PLL2_EN` | `31` | `Read/Write` | `0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
|  24 M H z × N P {\displaystyle 24\,\mathrm {MHz} \times {\frac {N}{P}}} ![{\\displaystyle 24\\,\\mathrm {MHz} \\times {\\frac {N}{P}}}][4497]  
The default value for the output is ?? MHz.  
If bypass is disabled, the result must be `?? MHz - ?? GHz`  
### CCM_PLL4_CFG
Default value: ??  
Offset: 0x000c 
Reserved   
---  
`CCM_PLL4_N` | `8:15` | `Read/Write` | `??` | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0xff = 255
      
    
[/code]
| PLL4 factor N   
`CCM_PLL4_D_1` | `16` | `Read/Write` | `0` | ` `
[code]
        0 = 1
        1 = 2
      
    
[/code]
| PLL4 Divider 1   
Reserved   
`CCM_PLL4_D_2` | `18` | `Read/Write` | `0` | ` `
[code]
        0 = 1
        1 = 2
      
    
[/code]
| PLL4 Divider 2   
Reserved   
`CCM_PLL4_EN` | `31` | `Read/Write` | `0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
|  24 M H z × N D 1 × D 2 {\displaystyle 24\,\mathrm {MHz} \times {\frac {N}{D_{1}\times D_{2}}}} ![{\\displaystyle 24\\,\\mathrm {MHz} \\times {\\frac {N}{D_{1}\\times D_{2}}}}][4498]  
The default value for the output is ?? MHz.  
If bypass is disabled, the result must be `?? MHz - ?? GHz`  
### CCM_PLL12_CFG
Default value: ??  
Offset: 0x002c 
Reserved   
---  
`CCM_PLL12_N` | `8:15` | `Read/Write` | `??` | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0xff = 255
      
    
[/code]
| PLL12 factor N   
`CCM_PLL12_D_1` | `16` | `Read/Write` | `0` | ` `
[code]
        0 = 1
        1 = 2
      
    
[/code]
| PLL12 Divider 1   
Reserved   
`CCM_PLL12_D_2` | `18` | `Read/Write` | `0` | ` `
[code]
        0 = 1
        1 = 2
      
    
[/code]
| PLL12 Divider 2   
Reserved   
`CCM_PLL12_EN` | `31` | `Read/Write` | `0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
|  24 M H z × N D 1 × D 2 {\displaystyle 24\,\mathrm {MHz} \times {\frac {N}{D_{1}\times D_{2}}}} ![{\\displaystyle 24\\,\\mathrm {MHz} \\times {\\frac {N}{D_{1}\\times D_{2}}}}][4498]  
The default value for the output is ?? MHz.  
If bypass is disabled, the result must be `?? MHz - ?? GHz`  
### CCM_APB0_GATE
Default value: 0x00000000  
Offset: 0x0590 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
Reserved   
`CCM_APB0_SPDIF` | `1` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB0 SPDIF clock gate   
Reserved   
`CCM_APB0_GATE_PIO` | `5` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB0 PIO clock gate   
Reserved   
`CCM_APB0_GATE_AC97` | `11` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB0 AC97 clock gate   
`CCM_APB0_GATE_I2S0` | `12` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB0 I2S0 clock gate   
`CCM_APB0_GATE_I2S1` | `13` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB0 I2S1 clock gate   
Reserved   
`CCM_APB0_GATE_LRADC` | `15` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB0 LRADC clock gate   
Reserved   
`CCM_APB0_GATE_GPADC` | `17` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB0 GPADC clock gate   
`CCM_APB0_GATE_TWD` | `18` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB0 TWD clock gate   
`CCM_APB_GATE_CIR_TX` | `19` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB0 CIR_TX clock gate   
Reserved   
### CCM_APB1_GATE
Default value: 0x00000000  
Offset: 0x0594 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_APB1_GATE_TWI0` | `0` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 TWI0 clock gate pass- or masking   
`CCM_APB1_GATE_TWI1` | `1` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 TWI1 clock gate pass- or masking   
`CCM_APB_GATE_TWI2` | `2` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 TWI2 clock gate pass- or masking   
`CCM_APB_GATE_TWI3` | `3` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 TWI3 clock gate pass- or masking   
`CCM_APB_GATE_TWI4` | `4` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 TWI4 clock gate pass- or masking   
Reserved   
`CCM_APB1_GATE_UART0` | `16` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 UART0 clock gate pass- or masking   
`CCM_APB1_GATE_UART1` | `17` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 UART1 clock gate pass- or masking   
`CCM_APB1_GATE_UART2` | `18` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 UART2 clock gate pass- or masking   
`CCM_APB1_GATE_UART3` | `19` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 UART3 clock gate pass- or masking   
`CCM_APB1_GATE_UART4` | `20` | `Read/Write` | `0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 UART4 clock gate pass- or masking   
`CCM_APB_GATE_UART5` | `21` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB1 UART5 clock gate pass- or masking   
Reserved   
### CCM_APB0_RST
Default value: 0x00000000  
Offset: 0x0590 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
Reserved   
`CCM_APB0_SPDIF` | `1` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB0 SPDIF reset control   
Reserved   
`CCM_APB0_RST_AC97` | `11` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB0 AC97 reset control   
`CCM_APB0_RST_I2S0` | `12` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB0 I2S0 reset control   
`CCM_APB0_RST_I2S1` | `13` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB0 I2S1 reset control   
Reserved   
`CCM_APB0_RST_LRADC` | `15` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB0 LRADC reset control   
Reserved   
`CCM_APB0_RST_GPADC` | `17` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB0 GPADC reset control   
Reserved   
`CCM_APB_RST_CIR_TX` | `19` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB0 CIR_TX reset control   
Reserved   
### CCM_APB1_RST
Default value: 0x00000000  
Offset: 0x05b4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_APB1_RST_TWI0` | `0` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 TWI0 reset control   
`CCM_APB1_RST_TWI1` | `1` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 TWI1 reset control   
`CCM_APB_RST_TWI2` | `2` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 TWI2 reset control   
`CCM_APB_RST_TWI3` | `3` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 TWI3 reset control   
`CCM_APB_RST_TWI4` | `4` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 TWI4 reset control   
Reserved   
`CCM_APB1_RST_UART0` | `16` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 UART0 reset control   
`CCM_APB1_RST_UART1` | `17` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 UART1 reset control   
`CCM_APB1_RST_UART2` | `18` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 UART2 reset control   
`CCM_APB1_RST_UART3` | `19` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 UART3 reset control   
`CCM_APB1_RST_UART4` | `20` | `Read/Write` | `0` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 UART4 reset control   
`CCM_APB_RST_UART5` | `21` | `Read/Write` | `0x00` | ` `
[code]
        0 = assert
        1 = de-assert
      
    
[/code]
| APB1 UART5 reset control   
Reserved
