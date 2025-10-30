# SGX544MP
## Contents
  * [1 Overview][48168]
  * [2 Known Informations][48169]
  * [3 A83T][48170]
  * [4 Published Imgtec documentation][48171]
  * [5 References][48172]
  * [6 External links][48173]

# Overview
PowerVR SGX544 is the second member of Imagination’s PowerVR Series5XT family. It can be implemented as a high-performance 4-pipeline single core or in various multiprocessor (MP) configurations of between 2 and 16 cores (8 to 64 pipelines).[[1]][48174]
[![][48175]][48176]
[][48177]
PowerVR SGX544 block diagram [[1]][48174]
Variant Table: 
MP  | GPU Cores  | Pipelines   
---|---|---  
1  | 1  | 4   
2  | 2  | 8   
...  | ...  | ...   
16  | 16  | 64   
Allwinner SoC with a PowerVR SGX544MP GPU: 
SOC  | PowerVR GPU  | Revision   
---|---|---  
[A31][48178] | SGX544MP1 or SGX544MP2  | 1.1.5   
[A83T][48179] | SGX544MP1  | 1.1.5   
Embedded API's: 
  * OpenGL ES 2.0 and OpenGL ES 1.1
  * OpenCL 1.1

# Known Informations
  * [SGX544MP/Registers][48180]
  * [SGX544MP/USP_OPCODE][48181]
  * [SGX544MP/USSE_ISA][48182]
  * [SGX544MP/ReverseEngineering][48183]
  * reverse engineered informations could be found [here][48184]

# A83T
[![][48185]][48186]
[][48187]
A83T: SGX544 Clocking
Clock Signal  | Full Name  | Frequency (4.3.x kernel)  | Usage   
---|---|---|---  
SYSCLK  | Interface clock  | 432 MHz  | clock for the slave interface   
MEMCLK  | Memory clock  | 432 MHz  | clock for the memories and master interface   
CORECLK  | Functional clock  | 432 MHz  | functional clock   
[[2]][48188]
# Published Imgtec documentation
Redistribution of this document is permitted with acknowledgement of the source. Since I didn't request this right now are her only the download links: 
  * [POD file format specification ][48189]
  * [PowerVR Hardware Architecture Overview for Developers][48190]
  * [PowerVR Instruction Set Reference][48191]

# References
  1. ↑ [1.0][48192] [1.1][48193] <https://www.imgtec.com/blog/the-powervr-sgx544mp-a-modern-gpu-for-todays-leading-platforms/> Imgtech Blog entry
  2. [↑][48194] <https://github.com/embed-3d/PVRSGX_hwdoc/blob/master/sources/pdfs/Spruh73c_chapter_SGX_Graphics_Accelerator.pdf> / SGX Ti Datasheet 

# External links
  * <https://libreplanet.org/wiki/Group:PowerVR_drivers>
  * <https://web.archive.org/web/20140805210128/http://powervr.gnu.org.ve/doku.php> Archieved powervr.gnu.org.ve site
