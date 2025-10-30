# A20
(Redirected from [Sun7i][51413])
 
A20  
---  
[![Allwinner A20.png][51416]][51417]  
Manufacturer|  Allwinner  
Process|  40nm  
CPU|  Dual-Core ARM Cortex-A7  
Memory|  LPDDR3/DDR3/LPDDR2  
GPU|  [Mali400][51418] MP2  
Connectivity  
Video|  HDMI 1.4, CVBS, YPbPr, VGA, CPU/RGB/LVDS LCD  
Audio|  I2S, PCM, AC97  
Storage|  MMC, NAND, SATA  
USB|  OTG, 2x Host  
Release Date|  December 2012  
Website|  [Product Page][51419]  
Allwinner A20 (sun7i) SoC features a Dual-Core Cortex-A7 ARM CPU, and a [Mali400][51418] MP2 GPU from ARM. 
Allwinner A20 is a low-end (budget) version of the [A31][51420]. It shares its Cortex-A7 ARM CPU architecture, but at the same time it is also pin-to-pin compatible with [A10][51421]. 
A20 is fully supported by the community from linux-sunxi 3.4 kernel and later. 
## Contents
  * [1 Overview][51422]
    * [1.1 Main components of the A20][51423]
    * [1.2 Cortex-A7][51424]
      * [1.2.1 Virtualization][51425]
    * [1.3 A20 SoC Features][51426]
  * [2 Documentation][51427]
  * [3 DVFS][51428]
  * [4 Software][51429]
    * [4.1 Original SDKs][51430]
    * [4.2 GPL Violations][51431]
  * [5 Devices][51432]
  * [6 See also][51433]
  * [7 References][51434]
  * [8 External links][51435]

# Overview
A20 CPU consists of dual ARM Cortex-A7 cores, and integrates the Mali400 MP2 GPU. Together with [Cedar Engine][51436] multimedia processing unit that is capable of up to 2160p (3840x1080@30fps 4k resolution or 1080p 3D decoding) video decoding, with integrated HDMI 1.4 output support, and H.264 HP (High Profile) in 1080p at 30fps video encoding. 
## Main components of the A20
  * CPU: Dual-Core ARM [Cortex-A7 1GHz Processor (r0p4, revidr=0x0)][51437] which have both VFP4 and NEON SIMD co-processors that share 32 floating point double-precision registers together[[1]][51438]: 
    * FPU: standard ARM VFPv4-D32 FPU Floating Point Unit
    * SIMD: NEON (ARM's extended general-purpose SIMD vector processing extension engine)
  * GPU: [Mali400 MP2][51418]
  * VPU: [Cedar Engine][51436] (Video Processor Unit for audio and video hardware decoding or encoding)
  * HDMI-transmitter: HDMI CEC (Consumer Electronics Control)

## Cortex-A7
Cortex-A7 is 100% ISA compatible with the Cortex-A15, this includes the new virtualization instructions, integer divide support and 40-bit memory addressing. Any code running on an A15 can run on a Cortex A7, just slower. This is a very important feature as it enables SoC vendors to build chips with both Cortex A7 and Cortex A15 cores, switching between them depending on workload requirements. ARM calls this a big.LITTLE configuration.[[2]][51439][[3]][51440][[4]][51441]
### Virtualization
Cortex A7 and A15 includes hardware virtualization support. 
  * It is managed by Xen ([Presentation of Cortex A7 and A15 capabilities for virtualisation][51442], [Xen ARM][51443] on xenproject.org, [PVH mode][51444] on blog.xen.org, [Xen ARMv7 with Virtualization Extensions][51445] on xenproject.org wiki)

  * [there is a guide about running xen on a20][51446]

  * [Some guides to deploy virtualization on Cortex-A15 and source for virtualization with KVM on Cortex-A15 on github][51447]

  * [Open Kernel Labs Delivers OKL4 Mobile Virtualization for ARM Cortex-A7 Processors][51448]

On the kvm branch of kernel.org, there is description of Cortex-A15 Virtualization extensions VGIC registers : 
  * [GIC of ARM on kvm branch of the kernel][51449]

After the ARM Cortex-A7 documentation: 
  * GIC memory MAP on Cortex-A7[[5]][51450]:

[code] 
    0x4000-0x4FFF	Virtual interface control, common base address
    0x5000-0x5FFF	Virtual interface control, processor-specific base address
    0x6000-0x7FFF	Virtual CPU interface
    
[/code]
  * Virtual Maintenance Interrupt (PPI6)[[6]][51451]
  * 2 virtual interrupt signals, nVIRQ and nVFIQ[[7]][51452]
  * With MMU-400, Intermediate Physical Address (IPA) ca be used by guest OS[[8]][51453]

## A20 SoC Features
[![][51454]][51455]
[][51456]
A20 SoC on a [Cubieboard2][51457]
  * CPU 
    * ARM Cortex-A7 Dual-Core ([revision r0p4][51458])
    * 256KiB L2-Cache (shared between two cores)
    * 32KiB (Instruction) / 32KiB (Data) L1-Cache per core
    * SIMD NEON, VFP4
    * Virtualization
    * Large Physical Address Extensions (LPAE) 1TB
  * GPU 
    * ARM Mali400 MP2
    * Featuring 1 vertex shader (GP) and 2 fragment shaders (PP).
    * Complies with OpenGL ES 2.0
  * Memory 
    * LPDDR2/DDR3/DDR3L controller
    * NAND Flash controller and 64-bit ECC
  * Video 
    * HD H.264 2160P video decoding
    * Full HD video decoding
    * BD Directory, BD ISO and BD m2ts video decoding
    * H.264 High Profile 1080P@30fps encoding
    * 3840×1080@30fps 3D decoding
    * Complies with RTSP, HTTP,HLS,RTMP,MMS streaming media protocol
  * Display 
    * Support multi-channel HD display
    * Integrated HDMI 1.4
    * CPU/RGB/LVDS LCD interface 1920×1080 resolution
    * CVBS/YPbPr/VGA support
    * Integrated TV decoder
    * 4 × up to 8096×8096 bitmaps layers
    * 32 × 32bits aRGB or 8bpp palette sprites blocks of up to 4096 (12 bits)×4096 size.
  * Camera 
    * Integrated parallel 8-bit I/F YUV sensor
    * Integrated 24-bit parallel YUV 444 I/F
    * 5M/8M CMOS sensor support
    * Dual-sensor support
  * Audio 
    * Integrated HI-FI 100dB Audio Codec
    * Dual MIC noise cancellation
  * package: BGA441 19 mm × 19 mm (0.80 mm Pitch)

# Documentation
  * [Allwinner A20 Manual v1.40][51459] (PDF, 857 pages, 2015-04-20)
  * [Allwinner A20 Datasheet v1.50][51460] (PDF, 36 pages, 2015-04-06)
  * [A20 Product Brief][51461] (Outdated)
  * [A20 User Manual][51462] (Outdated v1.0)

# DVFS
The A20 SoC supports dynamic voltage & frequency scaling. Below are the DVFS operating points, as documented in the A20 SDK (lichee-v2.0.tar.gz): 
[code] 
    ; dvfs voltage-frequency table configuration
    ;
    ; max_freq: cpu maximum frequency, based on Hz, can not be more than 1008MHz
    ; min_freq: cpu minimum frequency, based on Hz, can not be less than 60MHz
    ;
    ; LV_count: count of LV_freq/LV_volt, must be < 16
    ;
    ; LV1: core vdd is 1.45v if cpu frequency is (912Mhz, 1008Mhz]
    ; LV2: core vdd is 1.40v if cpu frequency is (864Mhz, 912Mhz]
    ; LV3: core vdd is 1.30v if cpu frequency is (792Mhz, 864Mhz]
    ; LV4: core vdd is 1.25v if cpu frequency is (720Mhz, 792Mhz]
    ; LV5: core vdd is 1.20v if cpu frequency is (624Mhz, 720Mhz]
    ; LV6: core vdd is 1.15v if cpu frequency is (528Mhz, 624Mhz]
    ; LV7: core vdd is 1.10v if cpu frequency is (312Mhz, 528Mhz]
    ; LV8: core vdd is 1.05v if cpu frequency is ( 60Mhz, 312Mhz]
    
[/code]
# Software
## Original SDKs
We have made some SDKs available on our server: 
  * A20-SDK-2.0 ([Full][51463])
  * A20_SDK_20130319 ([Reduced][51464], [Unpacked][51465])

## GPL Violations
See [CedarX violations.][51466]
# Devices
► [A20 Boards][51467]
► [A20 HTPC][51468]
► [A20 Other][51469]
► [A20 Tablets][51470]
# See also
  * [Mali400][51418]
  * [A10][51421]
  * [A10s][51471]
  * [A13][51472]
  * [A31][51420]

# References
  1. [↑][51473] [Cortex-A7 MPCore Technical Reference Manual — 1.3. Features][51474]
  2. [↑][51475] <http://www.anandtech.com/show/4991/arms-cortex-a7-bringing-cheaper-dualcore-more-power-efficient-highend-devices>
  3. [↑][51476] <http://en.wikipedia.org/wiki/ARM_Cortex-A7_MPCore>
  4. [↑][51477] <http://www.arm.com/products/processors/cortex-a/cortex-a7.php>
  5. [↑][51478] Cortex-A7 MPCore Technical Reference Manual - 8.2.1. GIC memory-map
  6. [↑][51479] Cortex-A7 MPCore Technical Reference Manual - 8.2.2. Interrupt sources
  7. [↑][51480] Cortex-A7 MPCore Technical Reference Manual - 8.2.4. GIC configuration
  8. [↑][51481] CoreLink MMU-400 System Memory Management Unit Technical Reference Manual - 1.1. About the MMU-400

# External links
  * [Product Page][51419]
  * [kernel source code for Allwinner A20][51482]
  * [Allwinner A20 EVB Schematics][51483]
  * [Allwinner A20 product brief][51484]
  * [Allwinner A20 article on wikipedia.org][51485]
