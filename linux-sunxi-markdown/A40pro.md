# R40
(Redirected from [A40pro][3724])
 
R40  
---  
[![R40.png][3727]][3728]  
Manufacturer|  Allwinner  
Process|  40 nm  
CPU|  Quad-Core ARM Cortex-A7 @ 1.2 GHz  
Extensions|  Thumb-2, Jazelle RCT, NEOS, VFPv4, LPAE  
Memory|  LPDDR2/LPDDR3/DDR2/DDR3/DDR3L  
GPU|  [Mali400][3729] MP2  
Connectivity  
Video|  CPU/RGB LCD, LVDS, MIPI DSI, HDMI V1.4  
Audio|  I2S, PCM  
Storage|  MMC, NAND, eMMC, Nor Flash, SATA  
USB|  OTG, 2x Host  
Website|  [http://www.allwinnertech.com/index.php?c=product&a=index&id=56][3730]  
Allwinner R40 (sun8i) SoC features a Quad-Core Cortex-A7 ARM CPU, and a [Mali400][3729] MP2 GPU from ARM. It is a not-pin-compatible quad core sucessor of the [A20][3731]. It's also known as the Allwinner [T3][3732] for In-Car Entertainment usage. [A40i][3733] and [A40pro][3734] are variants that differ in applicable temperatures range (industrial and military). [V40][3735] is a remarked R40. 
## Contents
  * [1 Overview][3736]
  * [2 R40 SoC Features][3737]
  * [3 Documentation][3738]
  * [4 Software][3739]
  * [5 Devices][3740]
  * [6 See also][3741]
  * [7 References][3742]
  * [8 External links][3743]

# Overview
The chip is decently supported in [mainline U-Boot][3744] and the [mainline kernel][3745], with features like HDMI video, Ethernet, USB, SATA and Mali 3D working. 
There is no support for the R40 in the (obsolete) linux-sunxi 3.4 kernel and in u-boot-sunxi. 
# R40 SoC Features
  * CPU 
    * ARM Cortex-A7 Quad-Core
    * 512 KB L2-Cache (shared between four cores)
    * 32 KB (Instruction) / 32 KiB (Data) L1-Cache per core
    * SIMD NEON, VFP4
    * Large Physical Address Extensions (LPAE) 1 TB
  * GPU 
    * ARM Mali400 MP2
    * Featuring 1 vertex shader (GP) and 2 fragment shaders (PP).
    * Complies with OpenGL ES 2.0
  * Memory 
    * DDR2/DDR3/DDR3L/LPDDR2/LPDDR3 controller up to 2GB address space
    * NAND Flash controller and 64-bit ECC
  * Storage 
    * SATA 1,5Gb/s + 3,0Gb/s, SATA spec 2.6, AHCI Revision 1.3
  * Video 
    * Full HD 1080p video decoding of MPEG-2, MPEG-4 SP/ASP GMC, H.263, H.264, WMV9/VC-1, and VP8
    * BD Directory, BD ISO and BD m2ts video decoding
    * H.264 High Profile 1080p @ 45 fps encoding
    * Complies with RTSP, HTTP,HLS,RTMP,MMS streaming media protocol
  * Display 
    * Supports output size up to 2048x2048
    * CPU/RGB/LVDS LCD interface 1920x1080@60fps
    * MIPI 4 lane DSI interface up to 1920x1080@60fps resolution
    * TV out: 4-ch CVBS, 1-ch YPbPr and 1-ch VGA
    * HDMI v1.4 with HDCP 1.2, up to 1920x1080@60fps
  * Camera 
    * 4-channel TVIN
    * Dual-sensor support
  * Audio 
    * Integrated HI-FI 100 dB Audio Codec
    * Dual MIC noise cancellation
  * PMIC 
    * AXP221s

# Documentation
  * [R40 User Manual v1.0][3746] (PDF, 784 pages, 2016-07-12)
  * [R40 Datasheet v1.0][3747] (PDF, 82 pages, 2016-07-12)
  * [File:Allwinner T3 User Manual V1.0 cleaned.pdf][3748]
  * [File:Allwinner T3 Datasheet V1.6 cleaned.pdf][3749]
  * [File:Allwinner A40i Datasheet V1.1 cleaned.pdf][3750]
  * [File:Allwinner A40i User Manual V1.1 cleaned.pdf][3751]

# Software
Source code and instructions are here 
  * [Linux 3.10 of TinaLinux][3752]
  * [T3 Linux SDK][3753][[1]][3754]

# Devices
► [R40 Boards][3755]
# See also
  * [A20][3731]
  * [T3][3732]

# References
  1. [↑][3756] [T3 Linux SDK Source][3757]

# External links
  * [Allwinner Product Page R40][3730]
  * [Allwinner Product Page T3][3758]
  * [Allwinner Product Page A40i][3759]
