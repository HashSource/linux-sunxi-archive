# DWC HDMI Controller
The [A83T][16299]/[H3][16300]/[A64][16301]/[A80][16302] SoCs use a Synopsys DesignWare HDMI controller. A80 and A83T use a PHY from Synopsys too, but H3 and A64 PHY is unknown. 
There is no sunxi specific documentation about this controller, so everything on this page is only guessed based on observations, trial and error and third party documentation of similar systems. Don't rely on it being 100% correct and feel free to discuss ambiguous parts. 
## Contents
  * [1 Overview][16303]
    * [1.1 Clocks][16304]
      * [1.1.1 H3][16305]
    * [1.2 Resets][16306]
  * [2 Register Guide][16307]
    * [2.1 HDMI_READ_EN][16308]
    * [2.2 HDMI_UNSCRAMBLE_ADDR][16309]
    * [2.3 DWC HDMI Controller][16310]
    * [2.4 DWC HDMI PHY][16311]
    * [2.5 H3/A64 HDMI PHY][16312]
      * [2.5.1 HDMI_H3_PHY_CTRL][16313]
      * [2.5.2 HDMI_H3_PHY_PLL][16314]
      * [2.5.3 HDMI_H3_PHY_CLK][16315]
      * [2.5.4 HDMI_H3_PHY_STATUS][16316]
      * [2.5.5 HDMI_H3_PHY_CEC][16317]
  * [3 Documents][16318]

# Overview
The HDMI controller consists of two blocks, the inner real HDMI controller from Synopsys, and some outer wrapper (above address 0x10000) scrambling the addresses and locking read access of the inner controller. On H3/A64 the outer block also provides configuration registers for the PHY. A80 might not have the outer part, this has to be checked. 
## Clocks
(A80/A83T/A64 not checked yet, might be different there) 
### H3
There are three clocks: BUS_CLK_HDMI_GATE, HDMI_SLOW_CLK, PLL3_CLK. HDMI_CLK seems to be unused, leaving it disabled or changing dividers has no effect. 
HDMI_SLOW_CLK is the actual module clock, used by the inner controller for configuration and low-speed interfaces. Everything except the high-speed data is clocked from this. 
PLL3_CLK is input to the PHY PLL, which provides a 1-16 pre-divider to match the pixel clock from TCON. This PLL generates the pixel/TMDS clocks and feeds them back to the inner controller as required. 
## Resets
There are two resets (A80 not checked yet), HDMI0_RST and HDMI1_RST. 
HDMI0_RST resets the inner controller. 
HDMI1_RST resets the outer wrapper (and at least on H3/A64 the PHY too). 
# Register Guide
Base address: 0x01ee0000 (sun8i/sun50i), 0x03d00000 (sun9i) 
### HDMI_READ_EN
Offset | `0x10010`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` HDMI_READ_EN ` | ` 31:0 ` | `W` | `` | 
[code]
    0x54524545 = enable read access
    0x57415452 = disable read access
    
[/code]
|   
### HDMI_UNSCRAMBLE_ADDR
Offset | `0x10014`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` HDMI_UNSCRAMBLE_ADDR ` | ` 31:0 ` | `W` | `` | 
[code]
    0x42494E47 = unscramble addresses
    0 = scramble addresses
    
[/code]
| Unsrambling restores same addresses as they are described in i.MX6 manual.  
NOTE: Be sure to make dummy read before scrambling addresses, otherwise, if the last operation is write to HDMI register, value will be lost.  
## DWC HDMI Controller
0x01ee0000 - 0x01eeffff (only byte-accessible) 
(A similar version of) the controller is publicly documented in the i.MX6 Reference Manual, chapter 33. There also is a mainline Linux driver for the controller in [drivers/gpu/drm/bridge/dw_hdmi.c][16319]. 
The design, revision, product and config IDs are 13 2a a0 c1 bf 02 fe 00 on H3/A64/A80/A83T and 21 2a a0 c1 9f 62 f3 00 on H6. 
Now the hard part, the register addresses are obfuscated in sunxi SoCs (except A80 and H6). To use existing drivers/documentation the address bits have to be rearranged in the following way: 
[code] 
    real <-> obfuscated address bits
    A1   <-> A15
    A3   <-> A14
    A5   <-> A13
    A7   <-> A12
    A9   <-> A11
    A11  <-> A10
    A13  <-> A9
    A15  <-> A8
    A14  <-> A7
    A12  <-> A6
    A10  <-> A5
    A8   <-> A4
    A6   <-> A3
    A4   <-> A2
    A2   <-> A1
    A0   <-> A0
[/code]
For example, to access register 0x100D (vsync width) one has to access 0x4043 on sunxi. 
[code] 
    # Python functions to translate DWC registers to sunxi register value:
    def bitrev32(x):
        x = ((x & 0x55555555) <<  1) | ((x & 0xAAAAAAAA) >>  1)
        x = ((x & 0x33333333) <<  2) | ((x & 0xCCCCCCCC) >>  2)
        x = ((x & 0x0F0F0F0F) <<  4) | ((x & 0xF0F0F0F0) >>  4)
        x = ((x & 0x00FF00FF) <<  8) | ((x & 0xFF00FF00) >>  8)
        x = ((x & 0x0000FFFF) << 16) | ((x & 0xFFFF0000) >> 16)
        return x
    
    def dwc2sunxi(x):
        x = bitrev32(x) | x                 # put bit-reversed version in upper 16bit
        x = x & 0x55555555                  # extract all even bits
        x = (x | (x >> 1)) & 0x33333333     # move all of them to lower 16 bits
        x = (x | (x >> 2)) & 0x0f0f0f0f     # in multiple steps
        x = (x | (x >> 4)) & 0x00ff00ff
        x = (x | (x >> 8)) & 0x0000ffff
        return x
    
[/code]
[code] 
    def sunxi2dwc(x):
        x = ((x & 0xff00) << 8) | (x & 0x00ff)
        x = ((x << 4) | x) & 0x0f0f0f0f
        x = ((x << 2) | x) & 0x33333333
        x = ((x << 1) | x) & 0x55555555
        x = (bitrev32(x) | x) & 0xffff
        return x
    
[/code]
Optimized version (bitrev32() as defined in linux bitrev.h): 
[code] 
    uint16_t dwc2sunxi(uint16_t addr)
    {
        uint32_t x = bitrev32((uint32_t)addr) | (uint32_t)addr; // put bit-reversed version in upper 16bit
        x = x & 0x55555555;                                     // then extract all even bits
        x = (x | (x >> 1)) & 0x33333333;                        // and move them all to the lower 16bit
        x = (x | (x >> 2)) & 0x0f0f0f0f;                        // in multiple steps
        x = (x | (x >> 4)) & 0x00ff00ff;                        // ...
        x = (x | (x >> 8)) & 0x0000ffff;
        return (uint16_t)x;
    }
    
[/code]
## DWC HDMI PHY
A80 and A83T use a Synopsys PHY, connected to controllers internal I2C bus. This PHY is documented in the i.MX6 Reference Manual, chapter 34, too. The existing Linux driver has support for this PHY, but SoC specific parameters are needed for configuration. 
## H3/A64 HDMI PHY
The H3/A64 PHY is unknown and undocumented. 
The HDMI block uses PLL3 as input clock, not HDMI_CLK. It looks like the input clock has to be higher than ~165MHz to get a stable HDMI signal. 
Some register guessing, only notes from experiments, no facts yet: 
### HDMI_H3_PHY_CTRL
Offset | `0x10020`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` HDMI_TMDS_CLK_OUTPUT_EN ` | ` 15 ` | `RW` | `` |  | enable TMDS clock output  
` HDMI_TMDS_2_OUTPUT_EN ` | ` 14 ` | `RW` | `` |  | enable TMDS data2 output  
` HDMI_TMDS_1_OUTPUT_EN ` | ` 13 ` | `RW` | `` |  | enable TMDS data1 output  
` HDMI_TMDS_0_OUTPUT_EN ` | ` 12 ` | `RW` | `` |  | enable TMDS data0 output  
### HDMI_H3_PHY_PLL
Offset | `0x1002c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` ` | ` 25 ` | `RW` | `` |  | enable pll?  
` ` | ` 5:0 ` | `RW` | `` |  | some pll parameter  
### HDMI_H3_PHY_CLK
Offset | `0x10030`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` ` | ` 19 ` | `RW` | `` |  | ?enable 18:16?  
` ` | ` 18:16 ` | `RW` | `` |  | some pll parameter (bandwidth?)  
` ` | ` 15:12 ` | `RW` | `` |  | some pll parameter  
` HDMI_CLK_DIV ` | ` 3:0 ` | `RW` | `` |  | clock divider  
### HDMI_H3_PHY_STATUS
Offset | `0x10038`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` HPD ` | ` 19 ` | `RW` | `` |  | HPD status  
` ` | ` 16:11 ` | `RW` | `` |  | some pll calibration? result  
### HDMI_H3_PHY_CEC
Note: Description field has notes found by trial and error. 
Offset | `0x1003c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` CTRL_SEL ` | ` 7 ` | `RW` | `0` | 
[code]
    0 - cec controller
    1 - reg control
    
[/code]
| if bit 2=0 send bit 0 on cec line  
` / ` | ` 6 ` | `RW` | `0` |  |   
` PAD_SELO2 ` | ` 5 ` | `RW` | `0` |  | ?  
` PAD_SELO1 ` | ` 4 ` | `RW` | `0` |  | ?  
` INPUT_EN ` | ` 3 ` | `RW` | `0` |  | 1 = disable input cec line(bit 1) If set to 1 hw tx will send but don't get ACKs  
` OUTPUT_EN ` | ` 2 ` | `RW` | `0` |  | 1 = pass cec line to hardware cec receiver  
0 = pass cec line to hardware cec transmitter. Transmitting works only when bits 2:7 = 0  
` INPUT_DATA ` | ` 1 ` | `RW` | `0` |  | status cec line when bit 3=0  
` OUPUT_DATA ` | ` 0 ` | `RW` | `0` |  | output on cec line when bit 2=0 and 7=1  
# Documents
  * [File:AW HDMI TX PHY S40 Spec V0.1.pdf][16320](PDF, 11 pages, 2018-01-03)
