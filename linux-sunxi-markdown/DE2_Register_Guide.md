# DE2 Register Guide
## Contents
  * [1 DE2 register guide][16041]
    * [1.1 Overview][16042]
    * [1.2 Notes][16043]
    * [1.3 Documentation][16044]
    * [1.4 Sections][16045]
    * [1.5 CCU][16046]
      * [1.5.1 DE2_CCU_GATE][16047]
      * [1.5.2 DE2_CCU_BUS_GATE][16048]
      * [1.5.3 DE2_CCU_RST][16049]
      * [1.5.4 DE2_CCU_DIV][16050]
      * [1.5.5 DE2_CCU_SEL][16051]
    * [1.6 Mixer][16052]
      * [1.6.1 Global Configuration][16053]
        * [1.6.1.1 GLB_CTL_REG][16054]
        * [1.6.1.2 GLB_STATUS_REG][16055]
        * [1.6.1.3 GLB_DBUFF_REG][16056]
        * [1.6.1.4 GLB_SIZE_REG][16057]
      * [1.6.2 Blender][16058]
        * [1.6.2.1 BLD_PIPE_CTL][16059]

# DE2 register guide
## Overview
Although DE2 is listed as a single block in the datasheet, it in fact contains several sub-blocks. 
## Notes
On A64 the BIT(24) at 0x01c00004 should be cleared to make DE2 to work. 
## Documentation
[File:Allwinner DE2.0 Spec V1.0.pdf][16060] \- 147 pages, 2.9MB, 18-01-2018 
## Sections
Most SoCs position DE2 at 0x01000000 (A64/H3/H5), but it may also be on a different address. 
Section  | Subsection  | Offset  | Description   
---|---|---|---  
**CCU** | CCU  | `0x00000000` | DE2 Clock Controller   
**WB** | WB  | `0x00010000` | Write Back Controller   
**Transform** | Transform  | `0x00020000` | Rotate arbitrary framebuffers   
**Mixer** | Mixer0  | `0x00100000` | Display Mixer 0   
| Mixer1  | `0x00200000` | Display Mixer 1   
## CCU
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`DE2_CCU_GATE` | `0x00` | `4 B` | Module clock gate register   
`DE2_CCU_BUS_GATE` | `0x04` | `4 B` | Bus clock gate register   
`DE2_CCU_RST` | `0x08` | `4 B` | Bus reset register   
`DE2_CCU_DIV` | `0x0c` | `4 B` | Module clock division register   
`DE2_CCU_SEL` | `0x10` | `4 B` | Mixer/TCON relation register   
#### DE2_CCU_GATE
Bit | Read/Write | Default | description   
---|---|---|---  
31:4 | / | / | Reserved   
3 | Read/Write | 0 | Module clock gate for Transform   
2 | Read/Write | 0 | Module clock gate for WB   
1 | Read/Write | 0 | Module clock gate for Mixer 1   
0 | Read/Write | 0 | Module clock gate for Mixer 0   
#### DE2_CCU_BUS_GATE
Bit | Read/Write | Default | description   
---|---|---|---  
31:4 | / | / | Reserved   
3 | Read/Write | 0 | Bus gate for Transform   
2 | Read/Write | 0 | Bus gate for WB   
1 | Read/Write | 0 | Bus gate for Mixer 1   
0 | Read/Write | 0 | Bus gate for Mixer 0   
#### DE2_CCU_RST
Bit | Read/Write | Default | description   
---|---|---|---  
31:4 | / | / | Reserved   
3 | Read/Write | 0 | Bus reset for Transform   
2 | Read/Write | 0 | Bus reset for WB (and on A83T, H3, R40 and unknown sun8iw{9,10} SoCs, it's also the bus reset for Mixer 1)   
1 | Read/Write | 0 | Bus reset for Mixer 1 (on SoCs not mentioned above)   
0 | Read/Write | 0 | Bus reset for Mixer 0   
#### DE2_CCU_DIV
The real division value is the value in the register part + 1. 
Bit | Read/Write | Default | description   
---|---|---|---  
31:16 | / | / | Reserved   
12:15 | Read/Write | 0 | Module clock division for Transform   
8:11 | Read/Write | 0 | Module clock division for WB   
4:7 | Read/Write | 0 | Module clock division for Mixer 1   
0:3 | Read/Write | 0 | Module clock division for Mixer 0   
#### DE2_CCU_SEL
Bit | Read/Write | Default | description   
---|---|---|---  
31:1 | / | / | Reserved   
0 | Read/Write | 0 | Switch Mixer and TCON relation (0 -> Mixer0 - TCON0, Mixer1 - TCON1; 1 -> Mixer0 - TCON1, Mixer1 - TCON0)   
## Mixer
Main mixer property is the number of supported video and UI channels. If the SoC has multiple mixers, they usually support different number of channels and first supports more channels than the second. Video channels support YUV planes and UI channels support RGB planes. Another important mixer property is maximum plane size. The exact number of supported channels of either kind and max. plane size can be found in BSP code in de_feat.[c|h] files.  
  
vi - number of video channels  
ui - number of UI channels 
Subunit  | Offset  | Size  | Count   
---|---|---|---  
Global Configuration  | 0x00000  | 0x01000  | 1   
Blender  | 0x01000  | 0x01000  | 1   
Video Channels  | 0x02000  | 0x01000  | vi   
UI Channels  | (vi + 2) * 0x01000  | 0x01000  | ui   
Video Scaler  | 0x20000  | 0x20000  | vi   
UI Scaler  | (vi + 1) * 0x20000  | 0x10000  | ui   
CSC  | 0xb0000  | 0x10000 (?)  | 1   
### Global Configuration
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`GLB_CTL_REG` | `0x00` | `4 B` | Global control register   
`GLB_STATUS_REG` | `0x04` | `4 B` | Global status register   
`GLB_DBUFF_REG` | `0x08` | `4 B` | Global double buffer register   
`GLB_SIZE_REG` | `0x0c` | `4 B` | Global size register   
#### GLB_CTL_REG
Note: Only mixer enable and writeback port bits are used in BSP code. 
Bit | Read/Write | Default | description   
---|---|---|---  
31:14 | / | / | Reserved   
12:13 | Read/Write | 0 | Writeback port (?)   
10:11 | / | / | Reserved   
9 | Read/Write | 0 | flied_rev (?)   
8 | Read/Write | 0 | sync_rev (?)   
6:7 | / | / | Reserved   
5 | Read/Write | 0 | Enable error IRQ   
4 | Read/Write | 0 | Enable finish IRQ   
1:3 | / | / | Reserved   
0 | Read/Write | 0 | Enable mixer   
#### GLB_STATUS_REG
Note: This register is not used in BSP code. 
Bit | Read/Write | Default | description   
---|---|---|---  
31:9 | / | / | Reserved   
8 | Read (?) | 0 | Even/odd flag (?)   
6:7 | / | / | Reserved   
5 | Read (?) | 0 | Error status   
4 | Read (?) | 0 | Busy status   
2:3 | / | / | Reserved   
1 | Read/Write(?) | 0 | Error IRQ   
0 | Read/Write(?) | 0 | Finish IRQ   
#### GLB_DBUFF_REG
Bit | Read/Write | Default | description   
---|---|---|---  
31:1 | / | / | Reserved   
0 | Write (?) | 0 | 1 -> Apply mixer settings (transfer them to DE2)   
#### GLB_SIZE_REG
Sets mixer output size, should match width and height set in TCON and HDMI (if used). 
Bit | Read/Write | Default | description   
---|---|---|---  
31:29 | / | / | Reserved   
28:16 | Read/Write | 0 | Height - 1   
15:13 | / | / | Reserved   
0:12 | Read/Write | 0 | Width - 1   
### Blender
First enabled channel correlates to first enabled pipe and so on. To simplify things, it can be always tought as 1:1 mapping, even if channels are not used in order. Most notably, video channel is often unused, so it is ok to enable first UI channel and second pipe (when SoC have only one video channel, which is very common). 
Register Name  | Offset  | Size  | Count  | Description   
---|---|---|---|---  
`BLD_PIPE_CTL` | `0x00` | `4 B` | `1` | Enable "pipes" and their fill colors   
`BLD_PIPE_ATTR` | `0x04` | `16 B` | `5` | Pipe attributes   
`BLD_ROUTE_CTL` | `0x80` | `4 B` | `1` | Z order of pipes   
`BLD_PREMULTIPLY_CTL` | `0x84` | `4 B` | `1` | ?   
`BLD_BKCOLOR` | `0x88` | `4 B` | `1` | Background color   
`BLD_OUTPUT_SIZE` | `0x8c` | `4 B` | `1` | Output size   
`BLD_MODE` | `0x90` | `4 B` | `4` | Blending mode for each channel   
`BLD_CK_CTL` | `0xb0` | `4 B` | `1` | Color key control register   
`BLD_CK_CFG` | `0xb4` | `4 B` | `1` | Color key configuration   
`BLD_CK_MAX` | `0xc0` | `4 B` | `4` | Max. color for color keying   
`BLD_CK_MIN` | `0xe0` | `4 B` | `4` | Min. color for color keying   
`BLD_OUT_CTL` | `0xfc` | `4 B` | `4` | Output control register   
#### BLD_PIPE_CTL
Note: Enabling pipe's fill color does nothing if pipe is not enabled. 
Bit | Read/Write | Default | description   
---|---|---|---  
31:13 | / | / | Reserved   
12 | Read/Write | 0 | Enable pipe 4   
11 | Read/Write | 0 | Enable pipe 3   
10 | Read/Write | 0 | Enable pipe 2   
9 | Read/Write | 0 | Enable pipe 1   
8 | Read/Write | 0 | Enable pipe 0   
7:5 | / | / | Reserved   
4 | Read/Write | 0 | Enable fill color on pipe 4   
3 | Read/Write | 0 | Enable fill color on pipe 3   
2 | Read/Write | 0 | Enable fill color on pipe 2   
1 | Read/Write | 0 | Enable fill color on pipe 1   
0 | Read/Write | 0 | Enable fill color on pipe 0
