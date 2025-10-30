# D1s
D1s  
---  
[![D1s.jpg][15882]][15883]  
Manufacturer|  Allwinner  
Process|  22nm[[1]][15884]  
CPU|  [XuanTie C906 RISC-V][15885]  
[[1]][15884]  
Extensions|  RV64IMAFDCVU  
Memory|  DDR2   
64 MB  
[[2]][15886]  
VPU|  **Decoding** : 1080p @ 60 FPS  
H265 / H264 / MPEG / JPEG / VC1 / MJPEG  
**Encoding** : 1080p @ 60 FPS  
JPEG / MJPEG  
[[2]][15886]  
Connectivity  
Video|  Out: MIPI / LVDS / LCD / CVBS  
In: CSI / CVBS  
[[2]][15886][[1]][15884]  
Audio|  DAC / ADC / CODEC / I2S-PCM / DMIC   
[[2]][15886]  
Network|  10/100/1000M EMAC[[2]][15886]  
Storage|  SDIO 3.0, eMMC 5.0, SPI NOR/NAND Flash[[1]][15884]  
USB|  USB2.0: 1x OTG + 1x Host[[2]][15886]  
Other|  G2D[[2]][15886]   
Display Engine[[2]][15886]  
SDIO, 2x SPI, 6x UART, 4x I2C, PWM, IR, LRADC, GPADC, TPADC  
LFBGA, 337 pins[[1]][15884]  
This page is still under construction.
Allwinner D1s (also known as **F133**) is based on a RISC-V core, and is a cheaper version of the [D1][15887] with the following differences: 
  * 64 MB of DDR2 memory included in the same package, instead of requiring external memory.
  * No [Tensilica HiFi4 DSP][15888].
  * No HDMI output.
  * One less I2S port.

The D1s features a single RV64GCV[[3]][15889] core [XuanTie C906][15885] from [T-Head Semiconductor][15890] (subsidiary of [Alibaba][15891]). 
## Contents
  * [1 Overview][15892]
  * [2 Documentation][15893]
  * [3 Devices][15894]
  * [4 References][15895]

# Overview
The [T113-s3][15896] is a pin-compatible variant with dual Cortex-A7 cores, all peripherals being identical. 
# Documentation
  * [D1s brief v1.0][15897]
  * [D1s Datasheet v1.0][15898]
  * [DIs User Manual v1.0][15899] (github) [DIs User Manual v1.0][15900] (backup)
  * [Xuantie C906 R1S0 RISC-V core User Manual (玄铁C906_R1S0用户手册) (chinese)][15901]
    * [OpenC906 User Manual (English)][15902]
  * [Specification of the DE2.0 Display Engine used in the D1s][15903]
  * [Xuantie C906 core RTL][15904]
    * [CLINT implementation][15905]
    * [PLIC gateway implementation][15906]

# Devices
► [D1s Boards][15907]
# References
  1. ↑ [1.0][15908] [1.1][15909] [1.2][15910] [1.3][15911] [1.4][15912] [Allwinner D1s/F133 RISC-V processor integrates 64MB DDR2 - CNX Software][15913]
  2. ↑ [2.0][15914] [2.1][15915] [2.2][15916] [2.3][15917] [2.4][15918] [2.5][15919] [2.6][15920] [2.7][15921] [F133 - Allwinner Technology][15922]
  3. [↑][15923] [RISC-V ISA base and extensions][15924]
