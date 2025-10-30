# Clock Control Module
(Redirected from [A10/CCM][325])
 
## Contents
  * [1 Clock Control Module][328]
    * [1.1 Overview][329]
    * [1.2 Clock domain][330]
    * [1.3 Clock generation][331]
      * [1.3.1 PLL][332]
      * [1.3.2 Bus clock generation][333]
    * [1.4 Timer Registers][334]
      * [1.4.1 CCM_PLL1_CFG][335]
      * [1.4.2 CCM_PLL1_TUN][336]
      * [1.4.3 CCM_PLL1_TUN2][337]
      * [1.4.4 CCM_PLL2_CFG][338]
      * [1.4.5 CCM_PLL2_TUN][339]
      * [1.4.6 CCM_PLL3_CFG][340]
      * [1.4.7 CCM_PLL4_CFG][341]
      * [1.4.8 CCM_PLL5_CFG][342]
      * [1.4.9 CCM_PLL5_TUN][343]
      * [1.4.10 CCM_PLL5_TUN2][344]
      * [1.4.11 CCM_PLL6_CFG][345]
      * [1.4.12 CCM_PLL6_TUN][346]
      * [1.4.13 CCM_PLL7_CFG][347]
      * [1.4.14 CCM_OSC24M_CFG][348]
      * [1.4.15 CCM_CPU_AXI_AHB_APB0_CFG][349]
      * [1.4.16 CCM_APB1_CLK_DIV_CFG][350]
      * [1.4.17 CCM_AXI_CLK_GATE][351]
      * [1.4.18 CCM_AHB_GATING0][352]
      * [1.4.19 CCM_AHB_GATING1][353]
      * [1.4.20 CCM_APB0_GATING][354]
      * [1.4.21 CCM_APB1_GATING][355]
      * [1.4.22 CCM_NAND_CLK][356]
      * [1.4.23 CCM_MMC0_CLK][357]
      * [1.4.24 CCM_MMC1_CLK][358]
      * [1.4.25 CCM_MMC2_CLK][359]
      * [1.4.26 CCM_MMC3_CLK][360]
      * [1.4.27 CCM_SS_CLK][361]
      * [1.4.28 CCM_SPI0_CLK][362]
      * [1.4.29 CCM_SPI1_CLK][363]
      * [1.4.30 CCM_SPI2_CLK][364]
      * [1.4.31 CCM_SPI3_CLK][365]
      * [1.4.32 CCM_IR0_CLK][366]
      * [1.4.33 CCM_IR1_CLK][367]
      * [1.4.34 CCM_IIS_CLK][368]
      * [1.4.35 CCM_A97_CLK][369]
      * [1.4.36 CCM_SPDIF_CLK][370]
      * [1.4.37 CCM_KPAD_CLK][371]
      * [1.4.38 CCM_SATA_CLK][372]
      * [1.4.39 CCM_USB_CLK][373]
      * [1.4.40 CCM_GPS_CLK][374]
      * [1.4.41 CCM_DRAM_CLK][375]
      * [1.4.42 CCM_DE-BE0_CLK][376]
      * [1.4.43 CCM_DE-BE1_CLK][377]
      * [1.4.44 CCM_DE-FE0_CLK][378]
      * [1.4.45 CCM_DE-FE1_CLK][379]
      * [1.4.46 CCM_MP_CLK][380]
      * [1.4.47 CCM_LCD0_CH0_CLK][381]
      * [1.4.48 CCM_LCD0_CH1_CLK][382]
      * [1.4.49 CCM_LCD1_CH0_CLK][383]
      * [1.4.50 CCM_LCD1_CH1_CLK][384]
      * [1.4.51 CCM_CSI-ISP_CLK][385]
      * [1.4.52 CCM_TVD_CLK][386]
      * [1.4.53 CCM_CSI0_CLK][387]
      * [1.4.54 CCM_CSI1_CLK][388]
      * [1.4.55 CCM_VE_CLK][389]
      * [1.4.56 CCM_ADDA_CLK][390]
      * [1.4.57 CCM_AVS_CLK][391]
      * [1.4.58 CCM_ACE_CLK][392]
      * [1.4.59 CCM_LVDS_CLK][393]
      * [1.4.60 CCM_HDMI_CLK][394]
      * [1.4.61 CCM_MALI400_CLK][395]
      * [1.4.62 CCM_MBUS_CTRL][396]
      * [1.4.63 CCM_MBUS_CH2_CTRL][397]
    * [1.5 Initial values][398]
      * [1.5.1 default map][399]
      * [1.5.2 All to 1 (except main clock)][400]
      * [1.5.3 All to 0 (except main clock)][401]
    * [1.6 Code References][402]

# Clock Control Module
## Overview
Allwinner's A10 has 10 timing or clock sources. 7 [Phase Locking Loop's (PLL's)][403], a 24MHz main crystal oscillator, an RC based internal on chip based oscillator and a low-power 32kHz crystal oscillator. 
The 24MHz crystal oscillator is mandatory and is responsible for supplying a clock source for the PLL. The 32kHz crystal oscillator is connected only to the RTC to ensure proper time is kept. 
Many devices being driving by any of these clocks have often 2 clocks connected to them. One of the clocks drives the chip itself, the other clock matches the bus to whatever it is connected (usually the CPU). 
## Clock domain
Clock domain  | Used module  | Speed range  | Description   
---|---|---|---  
24MHZ_CLK  | Main clock  | `24.000 MHz` | Core clock source, feeds the PLL and some timers.   
RC_CLK  | Timers, key  | `32 kHz` | Internal 32 kHz source for timers and the RTC.  
As it is RC based, it is not highly accurate.   
32KHZ_CLK  | Timers, key  | `32.768 kHz` | External 32 kHz source for timers and the RTC.  
If an accurate 32.768 kHz crystal oscillator is used, this should provide the most accurate timing reference.   
CPU_CLK  | CPU  | `2 kHz - 1200 MHz` | The clock for the CPU clock domain is divided from either the CPU_CLK or the 24MHZ_CLK.   
AHB_CLK  | Advanced High-performance Bus clock domain  | `8 kHz - 276 MHz` | The clock for the AHB clock domain is divided from the CPU_CLK.   
APB_CLK  | Advanced Peripherals Bus clock domain  | `0.5 kHz - 138 MHz` | The clock for the peripherals clock domain is divided from the AHB_CLK.   
SDRAM_CLK  | SDRAM clock domain  | `0 - 400 MHz` | The clock for the SDRAM clock domain is provided by the PLL.   
USB_CLK  | USB  | `480 MHz` | The clock for the USB clock domain is provided by the PLL.   
AUDIO_CLK  | A/D and D/A devices  | `[24.576 MHz][404] or [22.5792 MHz][404]` | The clock for the Audio clock domain is provided by the PLL.   
## Clock generation
All PLL's are fed from the 24 MHz reference clock. 
### PLL
Name  | Input  | Speed range  | Output  | Defines   
---|---|---|---|---  
PLL1  | 24 MHz  | `240 MHz - 2 GHz` |  24 M H z × N × K M × P {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{M\times P}}} ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{M\\times P}}}][405] | ` ``N = {0, 1 ... 31}  
K = {1, 2, 3, 4}  
M = {1, 2, 3, 4}  
P = {1, 2, 4, 8}  
`  
PLL2  | 24 MHz  | `22.5792 MHz or 24.576 MHz` | 22.5792 MHz or 24.576 MHz  |   
PLL3  | 24 MHz  | `27 MHz - 381 MHz` | Integer mode:  3 M H z × M {\displaystyle 3\,\mathrm {MHz} \times M} ![{\\displaystyle 3\\,\\mathrm {MHz} \\times M}][406]  
  
Fractional mode:  270 M H z ∨ 297 M H z {\displaystyle 270\,\mathrm {MHz} \lor 297\,\mathrm {MHz} } ![{\\displaystyle 270\\,\\mathrm {MHz} \\lor 297\\,\\mathrm {MHz} }][407] | `M = {9, 10 ... 127}`  
PLL4  | 24 MHz  | `240 MHz - 2 GHz` |  24 M H z × N × K M × P {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{M\times P}}} ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{M\\times P}}}][405] | ` ``N = {0, 1 ... 31}  
K = {1, 2, 3, 4}  
M = {1, 2, 3, 4}  
P = {1, 2, 4, 8}  
`  
PLL5  | 24 MHz  | `240 MHz - 2 GHz` |  24 M H z × N × K M {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{M}}} ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{M}}}][408]  
  
24 M H z × N × K P {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{P}}} ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{P}}}][409] | ` ``N = {0, 1 ... 31}  
K = {1, 2, 3, 4}  
M = {1, 2, 3, 4}  
P = {1, 2, 4, 8}  
`  
PLL6  | 24 MHz  | SATA mode: `100 MHz`  
PLL6 mode: `240 MHz - 2 GHz` | SATA mode:  24 M H z × N × K M × 6 {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{M\times 6}}} ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{M\\times 6}}}][410]  
  
PLL6 mode:  24 M H z × N × K 2 {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{2}}} ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{2}}}][411]  
  
PLL6 * 2 mode:  24 M H z × N × K {\displaystyle 24\,\mathrm {MHz} \times N\times K} ![{\\displaystyle 24\\,\\mathrm {MHz} \\times N\\times K}][412] | ` ``N = {0, 1 ... 31}  
K = {1, 2, 3, 4}  
M = {1, 2, 3, 4}  
P = {1, 2, 4, 8}  
`  
PLL7  | 24 MHz  | `27 MHz - 381 MHz` | Integer mode:  3 M H z × M {\displaystyle 3\,\mathrm {MHz} \times M} ![{\\displaystyle 3\\,\\mathrm {MHz} \\times M}][406]  
  
Fractional mode:  270 M H z ∨ 297 M H z {\displaystyle 270\,\mathrm {MHz} \lor 297\,\mathrm {MHz} } ![{\\displaystyle 270\\,\\mathrm {MHz} \\lor 297\\,\\mathrm {MHz} }][407] | `M = {9, 10 ... 127}`  
### Bus clock generation
Name  | Input  | Output  | Defines   
---|---|---|---  
CPU_CLK  | {32KHZ_CLK, 24MHZ_CLK, PLL1,  P L L 6 6 {\displaystyle {\frac {\mathrm {PLL6} }{6}}} ![{\\displaystyle {\\frac {\\mathrm {PLL6} }{6}}}][413]}  |  |   
AXI_CLK  | CPU_CLK  |  I n p u t N {\displaystyle {\frac {\mathrm {Input} }{N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{N}}}][414] | `N = {1, 2, 3, 4}`  
AHB_CLK  | AXI_CLK  |  I n p u t N {\displaystyle {\frac {\mathrm {Input} }{N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{N}}}][414] | `N = {1, 2, 4, 8}`  
APB0_CLK  | AHB_CLK  |  I n p u t N {\displaystyle {\frac {\mathrm {Input} }{N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{N}}}][414] | `N = {2, 4, 8}`  
APB1_CLK  | {32KHZ_CLK, 24MHZ_CLK, PLL6}  |  I n p u t M × N {\displaystyle {\frac {\mathrm {Input} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times N}}}][415] | ` `
[code]
        M = {1, 2 ... 32}  
    
        N = {1, 2, 4, 8}
      
    
[/code]  
{TWI_CLK, UART_CLK, PS2_CLK, CAN_CLK, SCR_CLK}  | APB1_CLK  |  |   
{NAND_CLK, <unknown>_CLK, SD[0123]_CLK, TS_CLK, SS_CLK, SPI[0123]_CLK, IR[01]_CLK}  | {24MHZ_CLK, PLL5, PLL6}  |  I n p u t M × N {\displaystyle {\frac {\mathrm {Input} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times N}}}][415] | ` `
[code]
        M = {1, 2 ... 16}  
    
        N = {1, 2, 4, 8}
      
    
[/code]  
PATA_CLK  | {PLL5, PLL6}  |  I n p u t M × N {\displaystyle {\frac {\mathrm {Input} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times N}}}][415] | ` `
[code]
        M = {1, 2 ... 32}  
    
        N = {1, 2, 4, 8}
      
    
[/code]  
{IIS_CLK, <unknown>}  | 8 * PLL2  |  I n p u t N {\displaystyle {\frac {\mathrm {Input} }{N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{N}}}][414] | `N = {1, 2, 4, 8}`  
KEYPAD_CLK  | {32KHZ_CLK, 24MHZ_CLK}  |  I n p u t M × N {\displaystyle {\frac {\mathrm {Input} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times N}}}][415] | ` `
[code]
        M = {1, 2 ... 32}  
    
        N = {1, 2, 4, 8}
      
    
[/code]  
USB_CLK  | USB_CLK  |  |   
<unknown> | AHB_CLK  |  I n p u t M × N {\displaystyle {\frac {\mathrm {Input} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M\\times N}}}][415] | ` `
[code]
        M = {1, 2 ... 32}  
    
        N = {1, 2, 4, 8}
      
    
[/code]  
{DE-BE[01]_CLK, FE[01]_CLK, MP_CLK}  | {PLL3, PLL5, PLL7}  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][416] | `M = {1, 2 ... 16}`  
IEP_CLK  | BE_CLK  |  |   
VE_CLK  | PLL4  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][416] | `M = {1, 2 ... 8}`  
LCD_CH0_CLK  | {1 * PLL3, 2 * PLL3, 1 * PLL7, 2 * PLL7}  |  |   
LCD[01]_CH1_CLK2  | {1 * PLL3, 2 * PLL3, 1 * PLL7, 2 * PLL7}  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][416] | `M = {1, 2 ... 16}`  
LCD[01]_CH1_CLK1  | LCD[01]_CH1_CLK2  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][416] | `M = {1, 2}`  
CSI_ISP_CLK  | {PLL3, PLL4, PLL5, PLL6}  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][416] | `M = {1, 2 ... 16}`  
AUDIO_CODEC_CLK  | PLL2  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][416] |   
SATA_CLK  | PLL6  |  |   
AVS_CLK  | 24MHZ_CLK  |  |   
HDMI_CLK  | {1 * PLL3, 2 * PLL3, 1 * PLL7, 2 * PLL7}  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][416] | `M = {1, 2 ... 16}`  
ACE_CLK  | {PLL4, PLL5, 24MHZ_CLK}  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][416] | `M = {1, 2 ... 16}`  
CSI[01]_CLK  | {1 * PLL3, 2 * PLL3, 1 * PLL7, 2 * PLL7}  |  I n p u t M {\displaystyle {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {Input} }{M}}}][416] | `M = {1, 2 ... 32}`  
MALI400_CLK  | {PLL3, PLL4, PLL5, PLL7}  |  381 M H z ≥ I n p u t M {\displaystyle 381\,\mathrm {MHz} \geq {\frac {\mathrm {Input} }{M}}} ![{\\displaystyle 381\\,\\mathrm {MHz} \\geq {\\frac {\\mathrm {Input} }{M}}}][417] | `M = {1, 2 ... 16}`  
## Timer Registers
Timer Base address: 0x01c20000 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`CCM_PLL1_CFG` | `0x0000` | `4B` | `PLL1 Control (Core)`  
`CCM_PLL1_TUN` | `0x0004` | `4B` | `PLL1 Tuning`  
`CCM_PLL2_CFG` | `0x0008` | `4B` | `PLL2 Control (Audio))`  
`CCM_PLL2_TUN` | `0x000c` | `4B` | `PLL1 Tuning`  
`CCM_PLL3_CFG` | `0x0010` | `4B` | `PLL3 Control (Video0)`  
`CCM_PLL3_TUN (No Tuning 3 seems to exist)` | `0x0014 (Should be here if it exists)` | `4B` | `PLL3 Tuning (Unconfirmed)`  
`CCM_PLL4_CFG` | `0x0018` | `4B` | `PLL4 Control (VE)`  
`CCM_PLL4_TUN (No Tuning 4 seems to exist)` | `0x001c (Should be here if it exists)` | `4B` | `PLL4 Tuning (Unconfirmed)`  
`CCM_PLL5_CFG` | `0x0020` | `4B` | `PLL5 Control (DDR)`  
`CCM_PLL5_TUN` | `0x0024` | `4B` | `PLL5 Tuning`  
`CCM_PLL6_CFG` | `0x0028` | `4B` | `PLL6 Control (SATA)`  
`CCM_PLL6_TUN` | `0x002c` | `4B` | `PLL6 Tuning`  
`CCM_PLL7_CFG` | `0x0030` | `4B` | `PLL7 Control (Video1)`  
`CCM_PLL7_TUN (No Tuning 7 seems to exist)` | `0x0034 (Should be here if it exists)` | `4B` | `PLL7 Tuning (Unconfirmed)`  
`CCM_PLL1_TUN2` | `0x0038` | `4B` | `PLL1 Secondary Tuning`  
`CCM_PLL5_TUN2` | `0x003c` | `4B` | `PLL5 Secondary Tuning`  
`Reserved` | `0x0040` | `12B` |   
`CCM_PLL_LOCK_DBG` | `0x004c` | `4B` | `PLL Lock Debug`  
`CCM_OSC24M_CFG` | `0x0050` | `4B` | `OSC24M control`  
`CCM_CPU_AHB_APB0_CFG` | `0x0054` | `4B` | `CPU, AHB and APB0 division ratio`  
`CCM_APB1_CLK_DIV` | `0x0058` | `4B` | `APB1 clock division ratio`  
`CCM_AXI_GATING` | `0x005c` | `4B` | `AXI module clock gating`  
`CCM_AHB_GATING0` | `0x0060` | `4B` | `AHB module clock gating 0`  
`CCM_AHB_GATING1` | `0x0064` | `4B` | `AHB module clock gating 1`  
`CCM_APB0_GATING` | `0x0068` | `4B` | `APB0 module clock gating`  
`CCM_APB1_GATING` | `0x006c` | `4B` | `APB1 module clock gating`  
`Reserved` | `0x0070` | `16B` |   
`CCM_NAND_SCLK_CFG` | `0x0080` | `4B` | `Module clock type 0`  
`CCM_MS_SCLK_CFG` | `0x0084` | `4B` | `Module clock type 0`  
`CCM_MMC0_SCLK_CFG` | `0x0088` | `4B` | `Module clock type 0`  
`CCM_MMC1_SCLK_CFG` | `0x008c` | `4B` | `Module clock type 0`  
`CCM_MMC2_SCLK_CFG` | `0x0090` | `4B` | `Module clock type 0`  
`CCM_MMC3_SCLK_CFG` | `0x0094` | `4B` | `Module clock type 0`  
`CCM_TS_CLK` | `0x0098` | `4B` | `Module clock type 0`  
`CCM_SS_CLK` | `0x009c` | `4B` | `Module clock type 0`  
`CCM_SPI0_CLK` | `0x00a0` | `4B` | `Module clock type 0`  
`CCM_SPI1_CLK` | `0x00a4` | `4B` | `Module clock type 0`  
`CCM_SPI2_CLK` | `0x00a8` | `4B` | `Module clock type 0`  
`CCM_PATA_CLK` | `0x00ac` | `4B` | `Module clock type 0`  
`CCM_IR0_CLK` | `0x00b0` | `4B` | `Module clock type 0`  
`CCM_IR1_CLK` | `0x00b4` | `4B` | `Module clock type 0`  
`CCM_IIS_CLK` | `0x00b8` | `4B` | `Module clock type 1`  
`CCM_AC97_CLK` | `0x00bc` | `4B` | `Module clock type 1`  
`CCM_SPDIF_CLK` | `0x00c0` | `4B` | `Module clock type 1`  
`CCM_KEYPAD_CLK` | `0x00c4` | `4B` |   
`CCM_SATA_CLK` | `0x00c8` | `4B` |   
`CCM_USB_CLK` | `0x00cc` | `4B` |   
`CCM_GPS_CLK` | `0x00d0` | `4B` |   
`CCM_SPI3_CLK` | `0x00d4` | `4B` |   
`Reserved` | `0x00d8` | `40B` |   
`CCM_DRAM_CLK` | `0x0100` | `4B` |   
`CCM_BE0_SCLK` | `0x0104` | `4B` |   
`CCM_BE1_SCLK` | `0x0108` | `4B` |   
`CCM_FE0_CLK` | `0x010c` | `4B` |   
`CCM_FE1_CLK` | `0x0110` | `4B` |   
`CCM_MP_CLK` | `0x0114` | `4B` |   
`CCM_LCD0_CH0_CLK` | `0x0118` | `4B` |   
`CCM_LCD1_CH0_CLK` | `0x011c` | `4B` |   
`CCM_CSI_ISP_CLK` | `0x0120` | `4B` |   
`Reserved` | `0x0124` | `4B` |   
`CCM_TVD_CLK` | `0x0128` | `4B` |   
`CCM_LCD0_CH1_CLK` | `0x012c` | `4B` |   
`CCM_LCD1_CH1_CLK` | `0x0130` | `4B` |   
`CCM_CS0_CLK` | `0x0134` | `4B` |   
`CCM_CS1_CLK` | `0x0138` | `4B` |   
`CCM_VE_CLK` | `0x013c` | `4B` |   
`CCM_AUDIO_CODEC_CLK` | `0x0140` | `4B` |   
`CCM_AVS_CLK` | `0x0144` | `4B` |   
`CCM_ACE_CLK` | `0x0148` | `4B` |   
`CCM_LVDS_CLK` | `0x014c` | `4B` |   
`CCM_HDMI_CLK` | `0x0150` | `4B` |   
`CCM_MALI400_CLK` | `0x0154` | `4B` |   
`CCM_MBUS_CLK` | `0x015c` | `4B` |   
`CCM_GMAC_CLK` | `0x0164` | `4B` |   
`CCM_HDMI1_RST_CLK` | `0x0170` | `4B` |   
`CCM_HDMI1_CTRL_CLK` | `0x0174` | `4B` |   
`CCM_HDMI1_SLOW_CLK` | `0x0178` | `4B` |   
`CCM_HDMI1_REPEAT_CLK` | `0x017c` | `4B` |   
`CCM_OUTA_CLK` | `0x01F0` | `4B` |   
`CCM_OUTB_CLK` | `0x01F4` | `4B` |   
### CCM_PLL1_CFG
Default value: 0x21005000  
Offset: 0x0000 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL1_M` | `0:1` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 3
        0x03 = 4
      
    
[/code]
| PLL1 factor M   
`CCM_PLL1_SD` | `2` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| Sigma-delta pattern enable   
`CCM_PLL1_SD_IN` | `3` | `Read/Write` | `0x00` |  | Sigma-delta pattern input   
`CCM_PLL1_K` | `4:5` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 3
        0x03 = 4
      
    
[/code]
| PLL1 factor K   
`no operation` | `6:7` |  |   
`CCM_PLL1_N` | `8:12` | `Read/Write` | `0x10` | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0x1f = 31
      
    
[/code]
| PLL1 factor N   
`CCM_PLL1_LCK_CTRL` | `13:15` | `Read/Write` | <unknown> |  | PLL1 lock timer control   
`CCM_PLL1_P` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| External factor P   
`no operation` | `18:19` |  |  |   
`CCM_PLL1_BIAS` | `20:24` | `Read/Write` | <unknown> |  | PLL1 bias current   
`CCM_PLL1_PLL4_EX` | `25` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      {unverified}
    
[/code]
| Exchange with PLL4 enable   
`CCM_PLL1_VCO_BIAS` | `26:29` |  |  | <unknown> | PLL1 VCO bias control (e.g. pre-div)   
`CCM_PLL1_VCO_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = no operation
        1 = reset
      {unverified}
    
[/code]
| PLL1 VCO reset in   
`CCM_PLL1` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
|  24 M H z × N × K M × P {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{M\times P}}} ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{M\\times P}}}][405]  
The default value for the output is 384 MHz.  
If bypass is disabled, the result must be `240 MHz - 2 GHz`  
### CCM_PLL1_TUN
Default value: unknown  
Offset: 0x0004 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:15` |  |  |  | Reserved for verification   
`CCM_FREQ_INIT` | `16:25` | `Read/Write` |  |  | PLL1 initial frequency control   
`CCM_PLL1_VCO_GAIN` | `26` | `Read/Write` |  | ` `
[code]
        0 = no operation
        1 = enable
      {unverified}
    
[/code]
| PLL5 VCO gain control   
`CCM_PLL1_BW` | `27` | `Read/Write` |  | ` `
[code]
        0 = narrow
        1 = wide
      {unverified}
    
[/code]
| PLL1 bandwith control   
`CCM_PLL1_DAMP` | `28:31` | `Read/Write` |  |  | PLL1 dampening factor   
### CCM_PLL1_TUN2
Default value: unknown  
Offset: 0x0038 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL1_WAV_BOT` | `0:16` |  |  |   
`CCM_PLL1_FREQ` | `17:18` | `Read/Write` | `0x00` | ` `
[code]
       0x00 = 31.5 kHz
       0x01 = 32.0 kHz
       0x02 = 32.5 kHz
       0x03 = 33.0 kHz
     
    
[/code]
| PLL1 frequency   
`reserved` | `19` |  |  |  |   
`CCM_PLL1_WAV_STP` | `20:28` | `Read/Write` | `0x00` |  | PLL1 Wave step   
`CCM_PLL1_FREQ_MOD` | `29:30` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = DC=0
        0x01 = DC=1
        0x02 = triangular
        0x03 = awmode
      
    
[/code]
| PLL1 Spread spectrum frequency mode   
`CCM_PLL1_SD_PAT` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL1 Sigma delta pattern enable   
### CCM_PLL2_CFG
Default value: 0x81000010  
Offset: 0x0008 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL2_VCO_BIAS` | `0:4` | `Read/Write` | `0x10` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x1f = 32
      
    
[/code]
| PLL2 VCO bias control (e.g. pre-div)   
`reserved` | `5:7` |  |  |  |   
`CCM_PLL2_N` | `8:14` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 1
        0x02 = 2
        ...
        0x7f = 127
      
    
[/code]
| PLL2 factor N   
`reserved` | `15` |  |  |  |   
`CCM_PLL2_BIAS` | `16:20` | `Read/Write` | `0x02` | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0x0f = 15
      {unverified}
    
[/code]
| PLL2 bias current control (e.g. post-div)   
`reserved` | `21:27` |  |  |  |   
`CCM_PLL2_SD_OUT` | `28` | `Read/Write` |  |  | PLL2 sigma delta output   
`no operation` | `29:31` |  |   
`CCM_PLL2` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL2 is used for Audio. Output formula:  24 M H z × N C C M _ P L L _ V C O _ B I A S × C C M _ P L L _ B I A S {\displaystyle {\frac {24\,\mathrm {MHz} \times N}{\mathrm {CCM\\_PLL\\_VCO\\_BIAS} \times \mathrm {CCM\\_PLL\\_BIAS} }}} ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N}{\\mathrm {CCM\\_PLL\\_VCO\\_BIAS} \\times \\mathrm {CCM\\_PLL\\_BIAS} }}}][418]  
  

[code] 
      1x 
      
        
          
            
              
                
                  (
                  2
                  ×
                  24
                  
                  
                    M
                    H
                    z
                  
                  )
                  ×
                  N
                
                
                  
                    C
                    C
                    M
                    _
                    P
                    L
                    L
                    _
                    V
                    C
                    O
                    _
                    B
                    I
                    A
                    S
                  
                  ×
                  
                    C
                    C
                    M
                    _
                    P
                    L
                    L
                    _
                    B
                    I
                    A
                    S
                  
                  ×
                  2
                
              
            
          
        
        {\displaystyle {\frac {(2\times 24\,\mathrm {MHz} )\times N}{\mathrm {CCM\_PLL\_VCO\_BIAS} \times \mathrm {CCM\_PLL\_BIAS} \times 2}}}
      
    ![{\\displaystyle {\\frac {\(2\\times 24\\,\\mathrm {MHz} \)\\times N}{\\mathrm {CCM\\_PLL\\_VCO\\_BIAS} \\times \\mathrm {CCM\\_PLL\\_BIAS} \\times 2}}}][419](Not 50% duty cycle)  
    
    
[/code]
  

[code] 
      2x 
      
        
          
            
              
                
                  (
                  2
                  ×
                  24
                  
                  
                    M
                    H
                    z
                  
                  )
                  ×
                  N
                
                
                  
                    C
                    C
                    M
                    _
                    P
                    L
                    L
                    _
                    V
                    C
                    O
                    _
                    B
                    I
                    A
                    S
                  
                  ×
                  
                    C
                    C
                    M
                    _
                    P
                    L
                    L
                    _
                    B
                    I
                    A
                    S
                  
                  ×
                  4
                
              
            
          
        
        {\displaystyle {\frac {(2\times 24\,\mathrm {MHz} )\times N}{\mathrm {CCM\_PLL\_VCO\_BIAS} \times \mathrm {CCM\_PLL\_BIAS} \times 4}}}
      
    ![{\\displaystyle {\\frac {\(2\\times 24\\,\\mathrm {MHz} \)\\times N}{\\mathrm {CCM\\_PLL\\_VCO\\_BIAS} \\times \\mathrm {CCM\\_PLL\\_BIAS} \\times 4}}}][420](8 x /4 50% duty cycle)  
    
    
[/code]
  

[code] 
      4x 
      
        
          
            
              
                
                  (
                  2
                  ×
                  24
                  
                  
                    M
                    H
                    z
                  
                  )
                  ×
                  N
                
                
                  
                    C
                    C
                    M
                    _
                    P
                    L
                    L
                    _
                    V
                    C
                    O
                    _
                    B
                    I
                    A
                    S
                  
                  ×
                  
                    C
                    C
                    M
                    _
                    P
                    L
                    L
                    _
                    B
                    I
                    A
                    S
                  
                  ×
                  2
                
              
            
          
        
        {\displaystyle {\frac {(2\times 24\,\mathrm {MHz} )\times N}{\mathrm {CCM\_PLL\_VCO\_BIAS} \times \mathrm {CCM\_PLL\_BIAS} \times 2}}}
      
    ![{\\displaystyle {\\frac {\(2\\times 24\\,\\mathrm {MHz} \)\\times N}{\\mathrm {CCM\\_PLL\\_VCO\\_BIAS} \\times \\mathrm {CCM\\_PLL\\_BIAS} \\times 2}}}][419](8 x /2 50% duty cycle)  
    
    
[/code]
  

[code] 
      8x 
      
        
          
            
              
                
                  (
                  2
                  ×
                  24
                  
                  
                    M
                    H
                    z
                  
                  )
                  ×
                  N
                
                
                  
                    C
                    C
                    M
                    _
                    P
                    L
                    L
                    _
                    V
                    C
                    O
                    _
                    B
                    I
                    A
                    S
                  
                  ×
                  
                    C
                    C
                    M
                    _
                    P
                    L
                    L
                    _
                    B
                    I
                    A
                    S
                  
                
              
            
          
        
        {\displaystyle {\frac {(2\times 24\,\mathrm {MHz} )\times N}{\mathrm {CCM\_PLL\_VCO\_BIAS} \times \mathrm {CCM\_PLL\_BIAS} }}}
      
    ![{\\displaystyle {\\frac {\(2\\times 24\\,\\mathrm {MHz} \)\\times N}{\\mathrm {CCM\\_PLL\\_VCO\\_BIAS} \\times \\mathrm {CCM\\_PLL\\_BIAS} }}}][421](Not 50% duty cycle)
    
[/code]  
  

### CCM_PLL2_TUN
Default value: 0x00000000  
Offset: 0x000c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL2_WAV_BOTTOM` | `0:16` | `Read/Write` | `0x00` |  | Wave bottom   
`CCM_PLL2_FREQ` | `17:18` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 31.5 kHz
        0x01 = 32.0 kHz
        0x02 = 32.5 kHz
        0x03 = 33.0 kHz
      
    
[/code]
| PLL2 Frequency   
`reserved` | `19` |  |  |  |   
`CCM_PLL2_WAV_STEP` | `20:28` | `Read/Write` | `0x00` |  | PLL2 Wave step   
`CCM_PLL2_SPRD_FREQ` | `29:30` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = DC=0
        0x01 = DC=1
        0x02 = Triangle
        0x03 = awmode
      
    
[/code]
| PLL2 Spread spectrum frequency mode   
`CCM_PLL2_SD_PAT` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL2 Sigma delta pattern enable   
  

### CCM_PLL3_CFG
Default value: 0x0010d063  
Offset: 0x0010 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL3_M` | `0:6` | `Read/Write` | `0x63` | ` `
[code]
        0x00 = no operation
        ...
        0x09 = 9
        ...
        0x7f = 127
      
    
[/code]
| PLL3 factor M   
`reserved` | `7` |  |  |  |   
`CCM_PLL3_BIAS` | `8:12` | `Read/Write` | <unknown> | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0x0f = 15
      {unverified}
    
[/code]
| PLL3 bias current control (e.g. post-div)   
`reserved` | `13` |  |  |  |   
`CCM_PLL3_FRAC` | `14` | `Read/Write` | `0x01` | ` `
[code]
        0 = 270 MHz
        1 = 297 MHz 
      {unverified}
    
[/code]
| PLL3 fractional frequency setting   
`CCM_PLL3_MODE` | `15` | `Read/Write` | `0x01` | ` `
[code]
        0 = fractional
        1 = integer
      
    
[/code]
| PLL3 mode   
`CCM_PLL3_VCO_BIAS` | `16:20` | `Read/Write` | <unknown> | ` `
[code]
       0x00 = 1
       0x01 = 2
       ...
       0x1f = 32
      {unverified}
    
[/code]
| PLL3 bias current control (e.g. pre-div)   
`CCM_PLL3_DAMP` | `21:23` | <unknown> |  | PLL3 dampening factor   
`reserved` | `24:26` |  |  |   
`CCM_PLL3` | `` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL3 output range: `27 MHz - 381 MHz`  

[code] 
      Integer mode: 
      
        
          
            3
            
            
              M
              H
              z
            
            ×
            M
          
        
        {\displaystyle 3\,\mathrm {MHz} \times M}
      
    ![{\\displaystyle 3\\,\\mathrm {MHz} \\times M}][406]  
      
    
      Fractional mode: 
      
        
          
            270
            
            
              M
              H
              z
            
            ∨
            297
            
            
              M
              H
              z
            
          
        
        {\displaystyle 270\,\mathrm {MHz} \lor 297\,\mathrm {MHz} }
      
    ![{\\displaystyle 270\\,\\mathrm {MHz} \\lor 297\\,\\mathrm {MHz} }][407] (see bit 14)
    
[/code]  
### CCM_PLL4_CFG
Default value: 0x21081000  
Offset: 0x0018 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL4_M` | `0:1` | `Read/Write` | `0x00` | ` `
[code]
        0x01 = 1
        0x02 = 2
        0x03 = 3
        0x04 = 4
      
    
[/code]
| PLL4 factor M   
`reserved` | `2:3` |  |  |  |   
`CCM_PLL4_K` | `4:5` | `Read/Write` | `0x00` | ` `
[code]
        0x01 = 1
        0x02 = 2
        0x03 = 3
        0x04 = 4
      
    
[/code]
| PLL4 factor K   
`reserved` | `6:7` |  |  |  |   
`CCM_PLL4_N` | `8:12` | `Read/Write` | `0x10` | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0x1f = 31
      
    
[/code]
| PLL4 factor N   
`reserved` | `13:14` |  |  |  |   
`CCM_PLL4_SW` | `15` | `Read/Write` | `0x00` | ` `
[code]
       0 = disabled
       1 = enabled
      
    
[/code]
| When enabled, PLL4 is sourced by PLL6   
`CCM_PLL4_P` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
       0x00 = 1
       0x01 = 2
       0x02 = 4
       0x03 = 8
      
    
[/code]
| PLL4 external factor P   
`reserved` | `18` |  |  |  |   
`CCM_PLL4_VCO_GAIN` | `19` | `Read/Write` | <unknown> | ` `
[code]
        0 = disabled
        1 = enabled
      {unverified}
    
[/code]
| PLL4 VCO bias control   
`CCM_PLL4_BIAS` | `20:24` | `Read/Write` | <unknown> | ` `
[code]
       0x00 = 1
       0x01 = 2
       ...
       0x1f = 32
      {unverified}
    
[/code]
| PLL4 bias control   
`CCM_PLL4_VCO_GAIN` | `25:29` | `Read/Write` | <unknown> | ` `
[code]
       0x00 = 1
       0x01 = 2
       ...
       0x1f = 32
      {unverified}
    
[/code]
| PLL4 VCO gain control   
`CCM_PLL4_BYPASS` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL4 bypass, when enabled 24 MHz is being output   
`CCM_PLL4` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL4 output range: `24 MHz` or `240 MHz - 2 GHz`  

[code] 
      
      
        
          
            
              
                
                  24
                  
                  
                    M
                    H
                    z
                  
                  ×
                  N
                  ×
                  K
                
                
                  M
                  ×
                  P
                
              
            
          
        
        {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{M\times P}}}
      
    ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{M\\times P}}}][405]  
    
      Output when CCM_PLL4_BYPASS is disabled must be in the 240 MHz - 2 GHz range
    
[/code]  
### CCM_PLL5_CFG
Default value: 0x11049280  
Offset: 0x0020 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL5_M` | `0:1` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 3
        0x03 = 4
      
    
[/code]
| PLL5 factor M   
`CCM_PLL5_M1` | `2:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 3
        0x03 = 4
      {unconfirmed}
    
[/code]
| PLL5 factor M1   
`CCM_PLL5_K` | `4:5` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 3
        0x03 = 4
      
    
[/code]
| PLL5 factor K   
`reserved` | `6` |  |  |  |   
`CCM_PLL5_LDO` | `7` | `Read/Write` | `0x01` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| PLL5 LDO enable   
`CCM_PLL5_N` | `8:12` | `Read/Write` | `0x12` | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0x1f = 31
      
    
[/code]
| PLL5 factor N   
`CCM_PLL5_P` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 3
        0x03 = 4
      
    
[/code]
| PLL5 external factor P   
`CCM_PLL5_BW` | `18` | `Read/Write` | <unknown> | ` `
[code]
        0 = narrow
        1 = wide
      
    
[/code]
| PLL5 bandwith control   
`CCM_PLL5_VCO_GAIN` | `19` | `Read/Write` |  | ` `
[code]
        0 = no operation
        1 = enable
      {unverified}
    
[/code]
| PLL5 VCO gain control   
`CCM_PLL5_BIAS` | `20:24` | `Read/Write` | <unknown> | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x1f = 32
      {unverified}
    
[/code]
| PLL5 bias current control   
`CCM_PLL5_VCO_BIAS` | `25:28` | `Read/Write` | <unknown> | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x1f = 32
      {unverified}
    
[/code]
| PLL5 VCO bias control (e.g. pre-div)   
`CCM_PLL5_DDR_CLK` | `29` | `Read/Write` | `0x00` | ` `
[code]
        0 = no operation
        1 = enable
      {unverified}
    
[/code]
| PLL5 DDR clock output enable   
`CCM_PLL5_BYPASS` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL5 bypass, when enabled 24 MHz is being output   
`CCM_PLL5` | `` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL5 output range: `24 MHz` or `240 MHz - 2 GHz`  
  

[code] 
      DDR: 
      
        
          
            
              
                
                  24
                  
                  
                    M
                    H
                    z
                  
                  ×
                  N
                  ×
                  K
                
                M
              
            
          
        
        {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{M}}}
      
    ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{M}}}][408]  
      
    
      Others: 
      
        
          
            
              
                
                  24
                  
                  
                    M
                    H
                    z
                  
                  ×
                  N
                  ×
                  K
                
                P
              
            
          
        
        {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{P}}}
      
    ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{P}}}][409]  
      
    
      Output when CCM_PLL5_BYPASS is disabled must be in the 240 MHz - 2 GHz range
    
[/code]  
### CCM_PLL5_TUN
Default value: unknown  
Offset: 0x0024 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:15` |  |  |  |   
`CCM_PLL5_FREQ_INIT` | `16:22` | `Read/Write` |  |  | PLL5 initial frequency control   
`CCM_PLL5_VCO_RST` | `23` | `Read/Write` |  | ` `
[code]
       0 = no operation
       1 = reset
      {unverified}
    
[/code]
| PLL5 VCO reset in   
`CCM_PLL5_LCK_CTRL` | `24:26` | `Read/Write` | <unknown> |  | PLL5 lock timer control   
`reserved` | `27` |  |  |  |   
`CCM_PLL5_VREG1` | `28` | `Read/Write` | <unknown> |  | VReg1 output enable   
`CCM_PLL5_DAMP` | `29:31` | `Read/Write` | <unknown> |  | PLL5 dampening factor   
### CCM_PLL5_TUN2
Default value: 0x00000000  
Offset: 0x003c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL5_WAV_BOT` | `0:16` |  |  |   
`CCM_PLL5_FREQ` | `17:18` | `Read/Write` | `0x00` | ` `
[code]
       0x00 = 31.5 kHz
       0x01 = 32.0 kHz
       0x02 = 32.5 kHz
       0x03 = 33.0 kHz
     
    
[/code]
| PLL5 frequency   
`reserved` | `19` |  |  |  |   
`CCM_PLL5_WAV_STP` | `20:28` | `Read/Write` | `0x00` |  | PLL5 Wave step   
`CCM_PLL5_FREQ_MOD` | `29:30` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = DC=0
        0x01 = DC=1
        0x02 = triangular
        0x03 = awmode
      
    
[/code]
| PLL5 Spread spectrum frequency mode   
`CCM_PLL5_SD_PAT` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL5 Sigma delta pattern enable   
### CCM_PLL6_CFG
Default value: 0x21009911  
Offset: 0x0028 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL6_M` | `0:1` | `Read/Write` | `0x01` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 3
        0x03 = 4
      
    
[/code]
| PLL6 factor M   
`reserved` | `2:3` |  |  |  |   
`CCM_PLL6_K` | `4:5` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 3
        0x03 = 4
      
    
[/code]
| PLL6 factor K   
`CCM_PLL6_DAMP` | `6:7` | `Read/Write` |  | PLL6 dampening factor   
`CCM_PLL6_N` | `8:12` | `Read/Write` | `0x19` | ` `
[code]
        0x00 = 0
        0x01 = 1
        ...
        0x1f = 31
      
    
[/code]
| PLL6 factor N   
`reserved` | `13` |  |  |  |   
`CCM_PLL6_SATA_CLK` | `14` | `Read/Write` | <unknown> | ` `
[code]
        0 = no operation
        1 = enabled
      {unconfirmed}
    
[/code]
| PLL6 SATA clock output enable   
`CCM_PLL6_BW` | `15` | `Read/Write` | <unknown> | ` `
[code]
       0 = narrow
       1 = wide
      {unconfirmed}
    
[/code]
| PLL6 bandwidth control   
`reserved` | `16:19` |  |  |   
`CCM_PLL6_BIAS` | `20:24` | `Read/Write` | <unknown> |  | PLL6 bias current   
`CCM_PLL6_VCO_BIAS` | `25:29` |  |  | <unknown> | PLL6 VCO bias control (e.g. pre-div)   
`CCM_PLL6_BYPASS` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = disabled
        1 = enabled
      
    
[/code]
| PLL6 bypass, when enabled 24 MHz is being output   
`CCM_PLL6` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL6 output range: `24 MHz` or `240 MHz - 2 GHz`  
  

[code] 
      DDR: 
      
        
          
            
              
                
                  24
                  
                  
                    M
                    H
                    z
                  
                  ×
                  N
                  ×
                  K
                
                
                  M
                  ×
                  6
                
              
            
          
        
        {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{M\times 6}}}
      
    ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{M\\times 6}}}][410]  
      
    
      Others: 
      
        
          
            
              
                
                  24
                  
                  
                    M
                    H
                    z
                  
                  ×
                  N
                  ×
                  K
                
                2
              
            
          
        
        {\displaystyle {\frac {24\,\mathrm {MHz} \times N\times K}{2}}}
      
    ![{\\displaystyle {\\frac {24\\,\\mathrm {MHz} \\times N\\times K}{2}}}][411]  
      
    
      Output when CCM_PLL6_BYPASS is disabled must be in the 240 MHz - 2 GHz range
    
[/code]  
  

### CCM_PLL6_TUN
Default value: unknown  
Offset: 0x002c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:31` |  |  |  |   
### CCM_PLL7_CFG
Default value: 0x0010d063  
Offset: 0x0030 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_PLL7_M` | `0:6` | `Read/Write` | `0x63` | ` `
[code]
       0x00 = no operation
       ...
       0x09 = 9
       ...
       0x7f = 127
      
    
[/code]
| PLL7 factor M   
`reserved` | `7` |  |  |  |   
`CCM_PLL7_BIAS` | `8:12` | `Read/Write` | <unknown> |  | PLL6 bias current   
`reserved` | `13` |  |  |  |   
`CCM_PLL7_FRAC` | `14` | `Read/Write` | `0x01` | ` `
[code]
       0 = 270 MHz
       1 = 297 MHz 
      
    
[/code]
| PLL7 fractional frequency setting   
`CCM_PLL7_MODE` | `15` | `Read/Write` | `0x01` | ` `
[code]
       0 = fractional
       1 = integer
      
    
[/code]
| PLL7 mode   
`CCM_PLL7_VCO_BIAS` | `16:20` |  |  | <unknown> | PLL7 VCO bias control (e.g. pre-div)   
`reserved` | `21:23` |  |  |  |   
`CCM_PLL7_DAMP` | `24:26` | <unknown> |  | PLL7 dampening factor   
`reserved` | `27:30` |  |  |  |   
`CCM_PLL7` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| PLL7 output range: `27 MHz - 381 MHz`  

[code] 
      Integer mode: 
      
        
          
            3
            
            
              M
              H
              z
            
            ×
            M
          
        
        {\displaystyle 3\,\mathrm {MHz} \times M}
      
    ![{\\displaystyle 3\\,\\mathrm {MHz} \\times M}][406]  
      
    
      Fractional mode: 
      
        
          
            270
            
            
              M
              H
              z
            
            ∨
            297
            
            
              M
              H
              z
            
          
        
        {\displaystyle 270\,\mathrm {MHz} \lor 297\,\mathrm {MHz} }
      
    ![{\\displaystyle 270\\,\\mathrm {MHz} \\lor 297\\,\\mathrm {MHz} }][407] (see bit 14)
    
[/code]  
  

### CCM_OSC24M_CFG
Default value: 0x001380133  
Offset: 0x0050 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_OSC24M` | `0` | `Read/Write` | `0x01` | ` `
[code]
       0 = disable
       1 = enable
      
    
[/code]
| Enable or disable the external 24 MHz Oscillator   
`CCM_OSC24M_GSM` | `1` | `Read/Write` | `0x01` | ` `
[code]
       0 = disable
       1 = enable
      {Unconfirmed}
    
[/code]
|   
`reserved` | `2:14` |  |  |  |   
`CCM_OSC24M_PLL_BIAS` | `15` | `Read/Write` | `0x01` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| OSC24M PLL bias current   
`CCM_OSC24M_LDO` | `16` | `Read/Write` | `0x01` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| OSCM24M LDO   
`CCM_OSC24M_PWR` | `17` | `Read/Write` | `0x01` | ` `
[code]
       0 = 2.5 V
       1 = 3.3 V
      
    
[/code]
| OSC24M input power select   
`CCM_OSC24M_LDO_OUT` | `18:20` | `Read/Write` | `unknown` | ` `
[code]
       0x00 = ???
       ...
       0x04 = 1.25 V
       ...
      
    
[/code]
| OSC24M LDO output   
`CCM_OSC24M_KEYFIELD` | `21:31` | `Read/Write` | `0x538` `` |  | OSC24M keyfield for LDO. Bits 24 - 31 are valid. Writing "strb" will do nothing.   
### CCM_CPU_AXI_AHB_APB0_CFG
Default value: 0x00010010  
Offset: 0x0054 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_AXI_CLK_DIV` | `0:1` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 3
        0x03 = 4
      
    
[/code]
| Choose the clock divider for the AXI-bus when the AXI clock source is the CPU clock.   
`reserved` | `2:3` |  |  |   
`CCM_AHB_CLK_DIV` | `4:5` | `Read/Write` | `0x01` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| Choose the clock divider for the AHB when the AHB clock source is the AXI clock.   
`reserved` | `5:7` |  |  |   
`CCM_APB0_CLK_DIV` | `8:9` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 2
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| Choose the clock divider for the APB0 when the APB0 clock source is the AHB2 clock.   
`reserved` | `10:15` |  |  |   
`CCM_CPU_CLK_SRC` | `16:17` | `Read/Write` | `0x01` | ` `
[code]
        0x00 = 32 KHz internal RC clock
        0x01 = 24 MHz external Oscillator
        0x02 = PLL1
        0x03 = 200 MHz sourced from PPL6
      
    
[/code]
| Change the CPU Clock source. After changing the clock source, at least 8 clock cycles need to pass before changes are active.   
`reserved` | `18:31` |  |  |   
### CCM_APB1_CLK_DIV_CFG
Default value: 0x00000000  
Offset: 0x0058 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_APB1_M` | `0:4` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x1f = 32
      
    
[/code]
| APB1 factor M   
`reserved` | `5:15` |  |  |   
`CCM_APB1_N` | `16:17` | `Read/Write` | `0x01` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| APB1 factor N   
`reserved` | `18:23` |  |  |   
`CCM_APB1_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 24 MHz
        0x01 = 1.2 GHz (from PLL6)
        0x02 = 32 kHz
        0x03 = no operation
      
    
[/code]
| APB1 clock source   
`reserved` | `26:30` |  |  |  |   
`reserved` | `31` |  |  |  | Could possibly be APBI Enable/disable?  
Some special modules (twi, uart, ps2, can, scr) using the APB_CLK use this clock as they need a special clock rate, even if APB_CLK is changed.  C C M _ A P B 1 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_APB1\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_APB1\\_CLK\\_SRC} }{M\\times N}}}][422]  
  
  
### CCM_AXI_CLK_GATE
Default value: 0x00000000  
Offset: 0x005c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_AXI_GATE_MASK` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AXI dram clock gate pass- or masking   
`reserved` | `1:31` |  |  |   
### CCM_AHB_GATING0
Default value: 0x00000000  
Offset: 0x0060 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_AHB_GATE_USB0` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB USB 0 clock gate pass- or masking   
`CCM_AHB_GATE_EHCI0` | `1` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB USB EHCI 0 clock gate pass- or masking   
`CCM_AHB_GATE_OHCI0` | `2` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB USB OHCI 0 clock gate pass- or masking   
`CCM_AHB_GATE_EHCI1` | `3` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB USB EHCI 1 clock gate pass- or masking   
`CCM_AHB_GATE_OHCI1` | `4` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB USB OHCI 1 clock gate pass- or masking   
`CCM_AHB_GATE_SS` | `5` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SS clock gate pass- or masking   
`CCM_AHB_GATE_DMA` | `6` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB DMA clock gate pass- or masking   
`CCM_AHB_GATE_BIST` | `7` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB BIST clock gate pass- or masking   
`CCM_AHB_GATE_SDMMC0` | `8` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SD/MMC 0 clock gate pass- or masking   
`CCM_AHB_GATE_SDMMC1` | `9` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SD/MMC 1 clock gate pass- or masking   
`CCM_AHB_GATE_SDMMC2` | `10` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SD/MMC 2 clock gate pass- or masking   
`CCM_AHB_GATE_SDMMC3` | `11` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SD/MMC 3 clock gate pass- or masking   
`CCM_AHB_GATE_MS` | `12` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB MS clock gate pass- or masking   
`CCM_AHB_GATE_NAND` | `13` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB NAND clock gate pass- or masking   
`CCM_AHB_GATE_SDRAM` | `14` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SDRAM clock gate pass- or masking   
`CCM_AHB_GATE_DLL` | `15` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB DLL clock gate pass- or masking   
`CCM_AHB_GATE_ACE` | `16` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB ACE clock gate pass- or masking   
`CCM_AHB_GATE_EMAC` | `17` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB EMAC clock gate pass- or masking   
`CCM_AHB_GATE_TS` | `18` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB TS clock gate pass- or masking   
`reserved` | `19` |  |  |   
`CCM_AHB_GATE_SPI0` | `20` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SPI 0 clock gate pass- or masking   
`CCM_AHB_GATE_SPI1` | `21` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SPI 1 clock gate pass- or masking   
`CCM_AHB_GATE_SPI2` | `22` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SPI 2 clock gate pass- or masking   
`CCM_AHB_GATE_SPI3` | `23` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SPI 3 clock gate pass- or masking   
`CCM_AHB_GATE_PATA` | `24` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB PATA clock gate pass- or masking   
`CCM_AHB_GATE_SATA` | `25` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB SATA clock gate pass- or masking   
`CCM_AHB_GATE_GPS` | `26` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB GPS clock gate pass- or masking   
`reserved` | `27` |  |  |   
`reserved` | `28` |  |  |   
`reserved` | `29` |  |  |   
`reserved` | `30` |  |  |   
`reserved` | `31` |  |  |   
### CCM_AHB_GATING1
Default value: 0x00000000  
Offset: 0x0064 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_AHB_GATE_VE` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB VE clock gate pass- or masking   
`CCM_AHB_GATE_TVD` | `1` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB TVD clock gate pass- or masking   
`CCM_AHB_GATE_TVE0` | `2` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB TVE 0 clock gate pass- or masking   
`CCM_AHB_GATE_TVE1` | `3` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB TVE 1 clock gate pass- or masking   
`CCM_AHB_GATE_LCD0` | `4` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB LCD 0 clock gate pass- or masking   
`CCM_AHB_GATE_LCD1` | `5` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB LCD 1 clock gate pass- or masking   
`reserved` | `6` |  |  | Possibly for AVS? (LVDS)?   
`reserved` | `7` |  |  |  | Possibly for AVS? (LVDS)?   
`CCM_AHB_GATE_CS0` | `8` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB CS 0 clock gate pass- or masking   
`CCM_AHB_GATE_CS1` | `9` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB CS 1 clock gate pass- or masking   
`reserved` | `10` |  |  |  | Possibly LVDS? AVS?   
`CCM_AHB_GATE_HDMI` | `11` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB HDMI clock gate pass- or masking   
`CCM_AHB_GATE_DE-BE0` | `12` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB DE-BE 0 clock gate pass- or masking   
`CCM_AHB_GATE_DE-BE1` | `13` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB DE-BE 1 clock gate pass- or masking   
`CCM_AHB_GATE_DE-FE0` | `14` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB DE-FE 0 clock gate pass- or masking   
`CCM_AHB_GATE_DE-FE1` | `15` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB DE-FE 1 clock gate pass- or masking   
`reserved` | `16` |  |  |  | Possibly LVDS? AVS?   
`reserved` | `17` |  |  |  | Possibly LVDS? AVS?   
`CCM_AHB_GATE_MP` | `18` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB MP clock gate pass- or masking   
`reserved` | `19` |  |  |  | Possibly LVDS? AVS?   
`CCM_AHB_GATE_MALI400` | `20` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AHB Mali-400 clock gate pass- or masking   
`reserved` | `21:31` |  |  |   
  

### CCM_APB0_GATING
Default value: 0x00000000  
Offset: 0x0068 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_APB_AUDIOCODEC` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 0 audiocodec clock gate pass- or masking   
`CCM_APB_SPDIF` | `1` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 0 SPDIF clock gate pass- or masking   
`CCM_APB_GATE_AC97` | `2` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 0 AC97 clock gate pass- or masking   
`CCM_APB_GATE_IIS` | `3` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 0 IIS clock gate pass- or masking   
`reserved` | `4` |  |  |  |   
`CCM_APB_GATE_PIO` | `5` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 0 PIO clock gate pass- or masking   
`CCM_APB_GATE_IR0` | `6` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 0 IR 0 clock gate pass- or masking   
`CCM_APB_GATE_IR1` | `7` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 0 IR 1 clock gate pass- or masking   
`reserved` | `8` |  |  |  | Possibly LVDS? AVS?   
`reserved` | `9` |  |  |  | Possibly LVDS? AVS?   
`CCM_APB_GATE_KEYPAD` | `10` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 0 Keypad clock gate pass- or masking   
`reserved` | `11:31` |  |  |  |   
### CCM_APB1_GATING
Default value: 0x00000000  
Offset: 0x006c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_APB_GATE_TWI0` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 TWI 0 clock gate pass- or masking   
`CCM_APB_GATE_TWI1` | `1` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 TWI 1 clock gate pass- or masking   
`CCM_APB_GATE_TWI2` | `2` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 TWI 2 clock gate pass- or masking   
`CCM_APB_GATE_TWI3` | `3` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 TWI 3 clock gate pass- or masking   
`CCM_APB_GATE_CAN` | `4` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 CAN clock gate pass- or masking   
`CCM_APB_GATE_SCR` | `5` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 SCR clock gate pass- or masking   
`CCM_APB_GATE_PS20` | `6` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 PS/2 0 clock gate pass- or masking   
`CCM_APB_GATE_PS21` | `7` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 PS/2 1 clock gate pass- or masking   
`reserved` | `8:14` |  |  |  |   
`CCM_APB_GATE_TWI4` | `15` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 TWI 4 clock gate pass- or masking   
`CCM_APB_GATE_UART0` | `16` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 UART 0 clock gate pass- or masking   
`CCM_APB_GATE_UART1` | `17` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 UART 1 clock gate pass- or masking   
`CCM_APB_GATE_UART2` | `18` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 UART 2 clock gate pass- or masking   
`CCM_APB_GATE_UART3` | `19` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 UART 3 clock gate pass- or masking   
`CCM_APB_GATE_UART4` | `20` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 UART 4 clock gate pass- or masking   
`CCM_APB_GATE_UART5` | `21` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 UART 5 clock gate pass- or masking   
`CCM_APB_GATE_UART6` | `22` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 UART 6 clock gate pass- or masking   
`CCM_APB_GATE_UART70` | `23` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| APB 1 UART 7 clock gate pass- or masking   
`reserved` | `24:31` |  |  |  |   
### CCM_NAND_CLK
Default value: 0x00000000  
Offset: 0x0080 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_NAND_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| NAND factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_NAND_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| NAND factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_NAND_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for NAND controller   
`reserved` | `26:30` |  |  |  |   
`CCM_NAND_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| NAND special clock gating (Max clock = 200 MHz):  
C C M _ N A N D _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_NAND\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_NAND\\_CLK\\_SRC} }{M\\times N}}}][423]  
### CCM_MMC0_CLK
Default value: 0x00000000  
Offset: 0x0088 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_MMC0_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| SD/MMC 0 factor M   
`reserved` | `4:7` |  |  |  |   
`CCM_MMC_CTRL_OCLK_DLY` | `8:10` | `Read/Write` | `0x00` |  | Output clock phase control; The output clock phase delay is based on the number of source clock that is from 0 to 7.   
`reserved` | `11:15` |  |  |  |   
`CCM_MMC0_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| SD/MMC 0 factor N   
`reserved` | `18:19` |  |  |  |   
`CCM_MMC_CTRL_SCLK_DLY` | `20:22` | `Read/Write` | `0x00` |  | Sample clock phase control; The sample clock phase delay is based on the number of source clock that is from 0 to 7.   
`reserved` | `23` |  |  |  |   
`CCM_MMC0_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for SD/MMC 0 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_MMC0_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SD/MMC 0 special clock gating (Max clock = 200 MHz):  
C C M _ M M C 0 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_MMC0\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_MMC0\\_CLK\\_SRC} }{M\\times N}}}][424]  
### CCM_MMC1_CLK
Default value: 0x00000000  
Offset: 0x008c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_MMC1_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| SD/MMC 1 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_MMC1_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| SD/MMC 1 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_MMC1_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for SD/MMC 1 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_MMC1_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SD/MMC 1 special clock gating (Max clock = 200 MHz):  
C C M _ M M C 1 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_MMC1\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_MMC1\\_CLK\\_SRC} }{M\\times N}}}][425]  
### CCM_MMC2_CLK
Default value: 0x00000000  
Offset: 0x0090 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_MMC2_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| SD/MMC 2 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_MMC2_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| SD/MMC 2 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_MMC2_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for SD/MMC 2 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_MMC2_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SD/MMC 2 special clock gating (Max clock = 200 MHz):  
C C M _ M M C 2 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_MMC2\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_MMC2\\_CLK\\_SRC} }{M\\times N}}}][426]  
### CCM_MMC3_CLK
Default value: 0x00000000  
Offset: 0x0094 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_MMC3_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| SD/MMC 3 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_MMC3_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| SD/MMC 3 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_MMC3_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for SD/MMC 3 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_MMC3_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SD/MMC 3 special clock gating (Max clock = 200 MHz):  
C C M _ M M C 3 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_MMC3\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_MMC3\\_CLK\\_SRC} }{M\\times N}}}][427]  
### CCM_SS_CLK
Default value: 0x00000000  
Offset: 0x009c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_SS_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| SS factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_SS_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| SS factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_SS_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for SS controller   
`reserved` | `26:30` |  |  |  |   
`CCM_SS_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SS special clock gating (Max clock = 200 MHz):  
C C M _ S S _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_SS\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_SS\\_CLK\\_SRC} }{M\\times N}}}][428]  
  

### CCM_SPI0_CLK
Default value: 0x00000000  
Offset: 0x00a0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_SPI0_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| SPI 0 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_SPI0_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| SPI 0 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_SPI0_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for SPI 0 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_SPI0_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SPI 0 special clock gating (Max clock = 200 MHz):  
C C M _ S P I 0 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_SPI0\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_SPI0\\_CLK\\_SRC} }{M\\times N}}}][429]  
### CCM_SPI1_CLK
Default value: 0x00000000  
Offset: 0x00a4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_SPI1_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| SPI 1 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_SPI1_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| SPI 1 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_SPI1_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for SPI 1 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_SPI1_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SPI 1 special clock gating (Max clock = 200 MHz):  
C C M _ S P I 1 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_SPI1\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_SPI1\\_CLK\\_SRC} }{M\\times N}}}][430]  
### CCM_SPI2_CLK
Default value: 0x00000000  
Offset: 0x00a8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_SPI2_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| SPI 2 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_SPI2_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| SPI 2 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_SPI2_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for SPI 2 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_SPI2_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SPI 2 special clock gating (Max clock = 200 MHz):  
C C M _ S P I 2 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_SPI2\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_SPI2\\_CLK\\_SRC} }{M\\times N}}}][431]  
### CCM_SPI3_CLK
Default value: 0x00000000  
Offset: 0x00d4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_SPI3_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| SPI 3 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_SPI3_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| SPI 3 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_SPI3_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for SPI 3 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_SPI3_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SPI 3 special clock gating (Max clock = 200 MHz):  
C C M _ S P I 3 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_SPI3\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_SPI3\\_CLK\\_SRC} }{M\\times N}}}][432]  
### CCM_IR0_CLK
Default value: 0x00000000  
Offset: 0x00b0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_IR0_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| IR 0 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_IR0_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| IR 0 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_IR0_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for IR 0 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_IRI0_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| IR 0 special clock gating (Max clock = 200 MHz):  
C C M _ I R 0 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_IR0\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_IR0\\_CLK\\_SRC} }{M\\times N}}}][433]  
### CCM_IR1_CLK
Default value: 0x00000000  
Offset: 0x00b4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_IR1_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| IR 1 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_IR1_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| IR 1 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_IR1_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for IR 1 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_IR1_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| IR 1 special clock gating (Max clock = 200 MHz):  
C C M _ I R 1 _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_IR1\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_IR1\\_CLK\\_SRC} }{M\\times N}}}][434]  
### CCM_IIS_CLK
Default value: 0x00000000  
Offset: 0x00b8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:15` |  |  |  |   
`CCM_IIS_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x08 = 8
      
    
[/code]
| IIS factor N   
`reserved` | `18:30` |  |  |  |   
`CCM_IIS_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| IIS special clock gating (Max clock = 100 MHz):  
8 × P L L 2 M × N {\displaystyle {\frac {8\times \mathrm {PLL2} }{M\times N}}} ![{\\displaystyle {\\frac {8\\times \\mathrm {PLL2} }{M\\times N}}}][435]  
### CCM_A97_CLK
Default value: 0x00030000  
Offset: 0x00bc 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:15` |  |  |  |   
`CCM_AC97_N` | `16:17` | `Read/Write` | `0x03` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x08 = 8
      
    
[/code]
| AC97 factor N   
`reserved` | `18:30` |  |  |  |   
`CCM_AC97_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AC97 special clock gating (Max clock = 200 MHz):  
8 × P L L 2 N {\displaystyle {\frac {8\times \mathrm {PLL2} }{N}}} ![{\\displaystyle {\\frac {8\\times \\mathrm {PLL2} }{N}}}][436]  
  

### CCM_SPDIF_CLK
Default value: 0x00030000  
Offset: 0x00c0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:15` |  |  |  |   
`CCM_SPDIF_N` | `16:17` | `Read/Write` | `0x03` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x08 = 8
      
    
[/code]
| SPDIF factor N   
`reserved` | `18:30` |  |  |  |   
`CCM_SPDIF_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SPDIF special clock gating (Max clock = 200 MHz):  
8 × P L L 2 N {\displaystyle {\frac {8\times \mathrm {PLL2} }{N}}} ![{\\displaystyle {\\frac {8\\times \\mathrm {PLL2} }{N}}}][436]  
  

### CCM_KPAD_CLK
Default value: 0x0000001f  
Offset: 0x00c4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_KPAD_M` | `0:4` | `Read/Write` | `0x1f` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x1f = 32
      
    
[/code]
| Keypad factor M   
`reserved` | `5:15` |  |  |  |   
`CCM_KPAD_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        0x02 = 4
        0x03 = 8
      
    
[/code]
| Keypad factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_KPAD_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = no operation
        0x02 = RC_CLK
        0x03 = no operation
      
    
[/code]
| Clock source for keypad controller   
`reserved` | `26:30` |  |  |  |   
`CCM_KPAD_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Keypad special clock gating (Max clock = 100 MHz):  
C C M _ K P A D _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_KPAD\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_KPAD\\_CLK\\_SRC} }{M\\times N}}}][437]  
  

### CCM_SATA_CLK
Default value: 0x00000000  
Offset: 0x00c8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:23` |  |  |  |   
`CCM_SATA_CLK_SRC` | `24` | `Read/Write` | `0x00` | ` `
[code]
        0 = PLL6 (100 MHz)
        1 = External Clock
      
    
[/code]
| Clock source for SATA controller   
`reserved` | `25:30` |  |  |  |   
`CCM_SATA_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| SATA clock gate pass- or masking   
### CCM_USB_CLK
Default value: 0x00000000  
Offset: 0x00cc 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_USB0_RESET` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| USB PHY0 reset control   
`CCM_USB1_RESET` | `1` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| USB PHY1 reset control   
`CCM_USB2_RESET` | `2` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| USB PHY2 reset control   
`reserved` | `3` |  |  |  |   
`CCM_USB_CLK_SRC` | `4` | `Read/Write` | `0x00` | ` `
[code]
        0 = PLL6 / 25
        1 = 48 MHz
      
    
[/code]
| Clock source for USB controller:  
48 MHz is generated from a 24 MHz sample taken from PLL6   
`CCM_USB_CLK_SW` | `5` | `Read/Write` | `0x00` | ` `
[code]
        0 = ?
        1 = ?
      
    
[/code]
| USB Clock switch   
`CCM_USB_OHCI0_GATE` | `6` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Special USB clock gating for USB OHCI 0   
`CCM_USB_OHCI1_GATE` | `7` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Special USB clock gating for USB OHCI 1   
`CCM_USB_GATE` | `8` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Special USB clock gating for USB PHY[012]   
`reserved` | `9:31` |  |  |  |   
  

### CCM_GPS_CLK
Default value: 0x00000000  
Offset: 0x00d0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_GPS_RESET` | `0` | `Read/Write` | `unknown` | ` `
[code]
        0 = disable 
        1 = enable
      {unconfirmed}
    
[/code]
| Enable reset for the GPS module   
`CCM_GPS_GATE` | `1` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| GPS clock gate pass- or masking   
`reserved` | `2:31` |  |  |  |   
### CCM_DRAM_CLK
Default value: 0x00000000  
Offset: 0x0100 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_DRAM_VE_GATE` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM VE clock gate pass- or masking   
`CCM_DRAM_CSI0_GATE` | `1` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM CSI 0 clock gate pass- or masking   
`CCM_DRAM_CSI1_GATE` | `2` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM CSI 1 clock gate pass- or masking   
`CCM_DRAM_TS_GATE` | `3` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM TS clock gate pass- or masking   
`CCM_DRAM_TVD_GATE` | `4` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM TVD clock gate pass- or masking   
`CCM_DRAM_TVE0_GATE` | `5` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM TVE 0 clock gate pass- or masking   
`CCM_DRAM_TVE1_GATE` | `6` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM TVE 1 clock gate pass- or masking   
`reserved` | `7:14` |  |  |  |   
`CCM_DRAM_CLK_OUT` | `15` | `Read/Write` | `0x00` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| Enable or disable DRAM clock output   
`reserved` | `16:23` |  |  |  |   
`CCM_DRAM_FE1_GATE` | `24` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM FE 1 clock gate pass- or masking   
`CCM_DRAM_FE0_GATE` | `25` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM FE 0 clock gate pass- or masking   
`CCM_DRAM_BE0_GATE` | `26` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM BE 0 clock gate pass- or masking   
`CCM_DRAM_BE1_GATE` | `27` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM BE 1 clock gate pass- or masking   
`CCM_DRAM_MP_GATE` | `28` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM MP clock gate pass- or masking   
`CCM_DRAM_ACE_GATE` | `29` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DRAM ACE clock gate pass- or masking   
`reserved` | `30:31` |  |  |  |   
  

### CCM_DE-BE0_CLK
Default value: 0x00000000  
Offset: 0x0104 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_DE-BE0_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| DE-BE 0 factor M   
`reserved` | `4:23` |  |  |  |   
`CCM_DE-BE0_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3
        0x01 = PLL7
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for DE-BE 0   
`reserved` | `26:29` |  |  |  |   
`CCM_DE-BE0_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| DE-BE0 reset   
`CCM_DE-BE0_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DE-BE 0 special clock gating:  
C C M _ D E − B E 0 _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_DE-BE0\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_DE-BE0\\_CLK\\_SRC} }{M}}}][438]  
  

### CCM_DE-BE1_CLK
Default value: 0x00000000  
Offset: 0x0108 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_DE-BE1_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| DE-BE 1 factor M   
`reserved` | `4:23` |  |  |  |   
`CCM_DE-BE1_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3
        0x01 = PLL7
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for DE-BE1   
`reserved` | `26:29` |  |  |  |   
`CCM_DE-BE1_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| DE-BE1 reset   
`CCM_DE-BE1_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DE-BE 1 special clock gating:  
C C M _ D E − B E 1 _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_DE-BE1\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_DE-BE1\\_CLK\\_SRC} }{M}}}][439]  
### CCM_DE-FE0_CLK
Default value: 0x00000000  
Offset: 0x010c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_DE-FE0_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| DE-FE 0 factor M   
`reserved` | `4:23` |  |  |  |   
`CCM_DE-FE0_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3
        0x01 = PLL7
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for DE-FE 0   
`reserved` | `26:29` |  |  |  |   
`CCM_DE-FE0_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| DE-FE0 reset   
`CCM_DE-FE0_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DE-FE 0 special clock gating:  
C C M _ D E − F E 0 _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_DE-FE0\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_DE-FE0\\_CLK\\_SRC} }{M}}}][440]  
### CCM_DE-FE1_CLK
Default value: 0x00000000  
Offset: 0x0110 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_DE-FE1_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| DE-FE 1 factor M   
`reserved` | `4:23` |  |  |  |   
`CCM_DE-FE1_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3
        0x01 = PLL7
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for DE-FE 1   
`reserved` | `26:29` |  |  |  |   
`CCM_DE-FE1_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| DE-FE1 reset   
`CCM_DE-FE1_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| DE-FE 1 special clock gating:  
C C M _ D E − F E 1 _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_DE-FE1\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_DE-FE1\\_CLK\\_SRC} }{M}}}][441]  
### CCM_MP_CLK
Default value: 0x00000000  
Offset: 0x0114 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_MP_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| MP factor M   
`reserved` | `4:23` |  |  |  |   
`CCM_MP_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3
        0x01 = PLL7
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for MP   
`reserved` | `26:29` |  |  |  |   
`CCM_MP_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| MP reset   
`CCM_MP_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| MP special clock gating:  
C C M _ M P _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_MP\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_MP\\_CLK\\_SRC} }{M}}}][442]  
  

### CCM_LCD0_CH0_CLK
Default value: 0x00000000  
Offset: 0x0118 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:23` |  |  |  |   
`CCM_LCD0_CH0_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3 (x1)
        0x01 = PLL7 (x1)
        0x02 = PLL3 (x2)
        0x03 = PLL7 (x2)
      
    
[/code]
| Clock source for LCD 0 CH 0   
`reserved` | `26:29` |  |  |  |   
`CCM_LCD0_CH0_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| LCD 0 CH 0 reset   
`CCM_LCD0_CH0_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| LCD 0 channel 0 special clock gating:  
C C M _ L C D 0 _ C H 0 _ C L K _ S R C {\displaystyle \mathrm {CCM\\_LCD0\\_CH0\\_CLK\\_SRC} } ![{\\displaystyle \\mathrm {CCM\\_LCD0\\_CH0\\_CLK\\_SRC} }][443]  
### CCM_LCD0_CH1_CLK
Default value: 0x00000000  
Offset: 0x012c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_LCD0_CH1_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| LCD 0 CH 1 factor M   
`reserved` | `4:10` |  |  |  |   
`CCM_LCD0_CH1_CLK_SRC0` | `11` | `Read/Write` | `0x00` | ` `
[code]
        0 = CCM_LCD0_CH1_CLK_SRC1
        1 = CCM_LCD0_CH1_CLK_SRC1 / 2
      
    
[/code]
| Clock source 0 for LCD 0 CH 1   
`reserved` | `12:14` |  |  |  |   
`CCM_LCD0_CH1_GATE0` | `15` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| LCD 0 channel 1 special clock 0 gating   
`reserved` | `16:23` |  |  |  |   
`CCM_LCD0_CH1_CLK_SRC1` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3 (x1)
        0x01 = PLL7 (x1)
        0x02 = PLL3 (x2)
        0x03 = PLL7 (x2)
      
    
[/code]
| Clock source 1 for LCD 0 CH 1   
`reserved` | `26:30` |  |  |  |   
`CCM_LCD0_CH1_GATE1` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| LCD 0 channel 1 special clock 1 gating:  
C C M _ L C D 0 _ C H 1 _ C L K _ S R C 1 M {\displaystyle {\frac {\mathrm {CCM\\_LCD0\\_CH1\\_CLK\\_SRC1} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_LCD0\\_CH1\\_CLK\\_SRC1} }{M}}}][444]  
### CCM_LCD1_CH0_CLK
Default value: 0x00000000  
Offset: 0x011c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:23` |  |  |  |   
`CCM_LCD1_CH0_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3 (x1)
        0x01 = PLL7 (x1)
        0x02 = PLL3 (x2)
        0x03 = PLL7 (x2)
      
    
[/code]
| Clock source for LCD 1 CH 0   
`reserved` | `26:29` |  |  |  |   
`CCM_LCD1_CH0_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| LCD 1 CH 0 reset   
`CCM_LCD1_CH0_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| LCD 1 channel 0 special clock gating:  
C C M _ L C D 1 _ C H 0 _ C L K _ S R C {\displaystyle \mathrm {CCM\\_LCD1\\_CH0\\_CLK\\_SRC} } ![{\\displaystyle \\mathrm {CCM\\_LCD1\\_CH0\\_CLK\\_SRC} }][445]  
  

### CCM_LCD1_CH1_CLK
Default value: 0x00000000  
Offset: 0x0130 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_LCD1_CH1_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| LCD 1 CH 1 factor M   
`reserved` | `4:10` |  |  |  |   
`CCM_LCD1_CH1_CLK_SRC0` | `11` | `Read/Write` | `0x00` | ` `
[code]
        0 = CCM_LCD1_CH1_CLK_SRC1
        1 = CCM_LCD1_CH1_CLK_SRC1 / 2
      
    
[/code]
| Clock source 0 for LCD 1 CH 1   
`reserved` | `12:14` |  |  |  |   
`CCM_LCD1_CH1_GATE0` | `15` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| LCD 1 channel 1 special clock 0 gating   
`reserved` | `16:23` |  |  |  |   
`CCM_LCD1_CH1_CLK_SRC1` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3 (x1)
        0x01 = PLL7 (x1)
        0x02 = PLL3 (x2)
        0x03 = PLL7 (x2)
      
    
[/code]
| Clock source 1 for LCD1 CH 1   
`reserved` | `26:30` |  |  |  |   
`CCM_LCD1_CH1_GATE1` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| LCD 1 channel 1 special clock 1 gating:  
C C M _ L C D 1 _ C H 1 _ C L K _ S R C 1 M {\displaystyle {\frac {\mathrm {CCM\\_LCD1\\_CH1\\_CLK\\_SRC1} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_LCD1\\_CH1\\_CLK\\_SRC1} }{M}}}][446]  
  

### CCM_CSI-ISP_CLK
Default value: 0x00000000  
Offset: 0x0120 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_CSI-ISP_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| CSI-ISP factor M   
`reserved` | `4:23` |  |  |  |   
`CCM_CSI-ISP_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3
        0x01 = PLL4
        0x02 = PLL5
        0x03 = PLL6
      
    
[/code]
| Clock source for CSI-ISP   
`reserved` | `26:30` |  |  |  |   
`CCM_CSI-ISP_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| CSI-ISP clock gate pass- or masking:  
C C M _ C S I − I S P _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_CSI-ISP\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_CSI-ISP\\_CLK\\_SRC} }{M}}}][447]  
### CCM_TVD_CLK
Default value: 0x00000000  
Offset: 0x0128 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:23` |  |  |  |   
`CCM_TVD_CLK_SRC` | `24` | `Read/Write` | `0x00` | ` `
[code]
        0 = PLL3
        1 = PLL7
      
    
[/code]
| Clock source for TVD   
`reserved` | `25:30` |  |  |  |   
`CCM_TVD_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| TVD clock gate pass- or masking:  
C C M _ T V D _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_TVD\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_TVD\\_CLK\\_SRC} }{M}}}][448]  
### CCM_CSI0_CLK
Default value: 0x00000000  
Offset: 0x0134 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_CSI0_M` | `0:4` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x1f = 32
      
    
[/code]
| CSI 0 factor M   
`reserved` | `5:23` |  |  |  |   
`CCM_CSI0_CLK_SRC` | `24:26` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL3 (x1)
        0x02 = PLL7 (x1)
        0x03 = no operation
        0x04 = no operation
        0x05 = PLL3 (x2)
        0x06 = PLL7 (x2)
        0x07 = no operation
      
    
[/code]
| Clock source for CSI 0   
`reserved` | `27:29` |  |  |  |   
`CCM_CSI0_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| CSI 0 reset   
`CCM_CSI0_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| CSI special clock gating:  
C C M _ C S I 0 _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_CSI0\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_CSI0\\_CLK\\_SRC} }{M}}}][449]  
### CCM_CSI1_CLK
Default value: 0x00000000  
Offset: 0x0138 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_CSI1_M` | `0:4` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x1f = 32
      
    
[/code]
| CSI 1 factor M   
`reserved` | `5:23` |  |  |  |   
`CCM_CSI1_CLK_SRC` | `24:26` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL3 (x1)
        0x02 = PLL7 (x1)
        0x03 = no operation
        0x04 = no operation
        0x05 = PLL3 (x2)
        0x06 = PLL7 (x2)
        0x07 = no operation
      
    
[/code]
| Clock source for CSI 1   
`reserved` | `27:29` |  |  |  |   
`CCM_CSI1_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| CSI 1 reset   
`CCM_CSI1_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| CSI special clock gating:  
C C M _ C S I 1 _ C L K _ S R C 1 M {\displaystyle {\frac {\mathrm {CCM\\_CSI1\\_CLK\\_SRC1} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_CSI1\\_CLK\\_SRC1} }{M}}}][450]  
### CCM_VE_CLK
Default value: 0x00000000  
Offset: 0x013c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_VE_RESET` | `0` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| VE reset   
`reserved` | `1:15` |  |  |  |   
`CCM_VE_N` | `16:18` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x7 = 8
      
    
[/code]
| CSI 0 factor M   
`reserved` | `19:30` |  |  |  |   
`CCM_VE_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| CSI special clock gating:  
P L L 4 M {\displaystyle {\frac {\mathrm {PLL4} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {PLL4} }{M}}}][451]  
  

### CCM_ADDA_CLK
Default value: 0x00000000  
Offset: 0x0140 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:30` |  |  |  |   
`CCM_ADDA_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AD/DA (audiocodec) special clock gating:  
P L L 2 {\displaystyle \mathrm {PLL2} } ![{\\displaystyle \\mathrm {PLL2} }][452]  
### CCM_AVS_CLK
Default value: 0x00000000  
Offset: 0x0144 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:30` |  |  |  |   
`CCM_AVS_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| AVS special clock gating:  
O S C 24 M {\displaystyle \mathrm {OSC24M} } ![{\\displaystyle \\mathrm {OSC24M} }][453]  
  

### CCM_ACE_CLK
Default value: 0x00000000  
Offset: 0x0148 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_ACE_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| ACE factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_ACE_RESET` | `16` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| ACE 1 reset   
`reserved` | `17:23` |  |  |  |   
`CCM_ACE_CLK_SRC` | `24` | `Read/Write` | `0x00` | ` `
[code]
        0 = PLL4
        1 = PLL5
      
    
[/code]
| Clock source for CSI 1   
`reserved` | `25:30` |  |  |  |   
`CCM_ACE_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| CSI special clock gating (Max clock = 200 MHz):  
C C M _ A C E _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_ACE\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_ACE\\_CLK\\_SRC} }{M}}}][454]  
  

### CCM_LVDS_CLK
Default value: 0x00000000  
Offset: 0x014c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`reserved` | `0:30` |  |  |  |   
`CCM_LVDS_RESET` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| LVDS reset   
  

### CCM_HDMI_CLK
Default value: 0x00000000  
Offset: 0x0150 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_HDMI_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| HDMI factor M   
`reserved` | `4:23` |  |  |  |   
`CCM_HDMI_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3 (x1)
        0x01 = PLL7 (x1)
        0x02 = PLL3 (x2)
        0x03 = PLL7 (x2)
      
    
[/code]
| Clock source for HDMI   
`reserved` | `26:30` |  |  |  |   
`CCM_HDMI_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| HDMI special clock gating:  
C C M _ H D M I _ C L K _ S R C 1 M {\displaystyle {\frac {\mathrm {CCM\\_HDMI\\_CLK\\_SRC1} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_HDMI\\_CLK\\_SRC1} }{M}}}][455]  
  

### CCM_MALI400_CLK
Default value: 0x00000000  
Offset: 0x0154 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_MALI400_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| MALI 400 factor M   
`reserved` | `4:23` |  |  |  |   
`CCM_MALI400_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = PLL3
        0x01 = PLL4
        0x02 = PLL5
        0x03 = PLL7
      
    
[/code]
| Clock source for MALI400   
`reserved` | `26:29` |  |  |  |   
`CCM_MALI400_RESET` | `30` | `Read/Write` | `0x00` | ` `
[code]
        0 = reset
        1 = no reset
      
    
[/code]
| MALI 400 reset   
`CCM_MALI400_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| MALI 400 special clock gating (Max clock = 381 MHz):  
C C M _ M A L I 400 _ C L K _ S R C M {\displaystyle {\frac {\mathrm {CCM\\_MALI400\\_CLK\\_SRC} }{M}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_MALI400\\_CLK\\_SRC} }{M}}}][456]  
### CCM_MBUS_CTRL
Default value: 0x00000000  
Offset: 0x015c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_MBUS_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| MBUS factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_MBUS_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| MBUS factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_MBUS_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6 (*2 for A20)
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for MBUS controller   
`reserved` | `26:30` |  |  |  |   
`CCM_MBUS_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| MBUS special clock gating (Max clock = 300 MHz):  
C C M _ M B U S _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_MBUS\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_MBUS\\_CLK\\_SRC} }{M\\times N}}}][457]  
### CCM_MBUS_CH2_CTRL
Default value: 0x00000000  
Offset: 0x0160 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`CCM_MBUS_M` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| MBUS Channel 2 factor M   
`reserved` | `4:15` |  |  |  |   
`CCM_MBUS_N` | `16:17` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 1
        0x01 = 2
        ...
        0x0f = 16
      
    
[/code]
| MBUS Channel 2 factor N   
`reserved` | `18:23` |  |  |  |   
`CCM_MBUS_CLK_SRC` | `24:25` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = OSC24M
        0x01 = PLL6
        0x02 = PLL5
        0x03 = no operation
      
    
[/code]
| Clock source for MBUS Channel 2 controller   
`reserved` | `26:30` |  |  |  |   
`CCM_MBUS_GATE` | `31` | `Read/Write` | `0x00` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| MBUS Channel 2 special clock gating (Max clock = 300 MHz):  
C C M _ M B U S _ C L K _ S R C M × N {\displaystyle {\frac {\mathrm {CCM\\_MBUS\\_CLK\\_SRC} }{M\times N}}} ![{\\displaystyle {\\frac {\\mathrm {CCM\\_MBUS\\_CLK\\_SRC} }{M\\times N}}}][457]  
## Initial values
### default map
md 0x01c20000 0x56 
[code] 
    01c20000: a1005000 0a101010 08100010 00000000    .P..............
    01c20010: 0010d063 00000000 21081000 00000000    c..........!....
    01c20020: b1059491 14888020 21009911 00000000    .... ......!....
    01c20030: 0010d063 00000000 00000000 00000000    c...............
    01c20040: 00000000 00000000 00000000 00000000    ................
    01c20050: 00138013 00020010 00000000 00000000    ................
    01c20060: 00004140 00000000 00000020 00010001    @A...... .......
    01c20070: 00000000 00000000 00000000 00000000    ................
    01c20080: 00000000 00000000 82000004 00000000    ................
    01c20090: 00000000 00000000 00000000 00000000    ................
    01c200a0: 00000000 00000000 00000000 00000000    ................
    01c200b0: 00000000 00000000 00000000 00030000    ................
    01c200c0: 00010000 0000001f 00000000 00000000    ................
    01c200d0: 00000000 00000000 00000000 00000000    ................
    01c200e0: 00000000 00000000 00000000 00000000    ................
    01c200f0: 00000000 00000000 00000000 00000000    ................
    01c20100: 00008000 00000000 00000000 00000000    ................
    01c20110: 00000000 00000000 00000000 00000000    ................
    01c20120: 00000000 00000000 00000000 00000000    ................
    01c20130: 00000000 00000000 00000000 00000000    ................
    01c20140: 00000000 00000000 00000000 00000000    ................
    01c20150: 00000000 00000000    ........
    
[/code]
### All to 1 (except main clock)
[/code]
[code] 
### All to 0 (except main clock)
[/code]
[code] 
## Code References
<https://github.com/hno/uboot-allwinner/blob/lichee/lichee-dev-mmc/arch/arm/include/asm/arch-sunxi/clock.h> <https://github.com/amery/linux-allwinner/blob/allwinner-v3.0-android-v2/arch/arm/mach-sun4i/include/mach/ccmu_regs.h>
