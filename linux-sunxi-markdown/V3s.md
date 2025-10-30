# V3s
V3s  
---  
[![V3s.jpg][57758]][57759]  
Manufacturer|  Allwinner  
CPU|  ARM Cortex-A7 @ 1.2GHz  
Extensions|  NEON, VFPv4  
Memory|  DDR2 up to 400MHz, 64MB integrated  
Connectivity  
Video|  LCD  
Audio|  Mic, Headphone  
Network|  10/100M Ethernet PHY  
Storage|  NAND, NOR, SD/MMC  
USB|  1 OTG  
Other|  3 UARTs, SPI, 2 TWIs  
Website|  [Product Page][57760]  
[Allwinner][57761] **V3s** is SoC with build-in ARM Cortex A7 CPU and integrated 64MB DDR2 RAM 
## Contents
  * [1 Overview][57762]
    * [1.1 Main components of the V3s:][57763]
  * [2 V3s SoC Features][57764]
  * [3 Documentation][57765]
  * [4 Software][57766]
    * [4.1 Original SDK][57767]
  * [5 Devices][57768]
  * [6 Links][57769]

# Overview
The V3s targets the Car Digital Video Record (DVR) and IP Camera (IPC) Monitor System market. 
It comes in a hacker-friendly 128-pin eLQFP package. 
## Main components of the V3s:
  * CPU: [Cortex-A7 1.2GHz (ARM v7-A) Processor][57770] which have both [VFPv3][57771] and [NEON][57772] co-processors: 
    * FPU: [Vector Floating Point Unit][57771] (standard ARM VFPv4 FPU Floating Point Unit)
    * SIMD: [NEON][57772] (ARM's extended general-purpose SIMD vector processing extension engine)
  * Integrated 64MB DRAM

# V3s SoC Features
  * CPU 
    * ARM Cortex TM -A7 MP1 Processor
    * Thumb-2 Technology
    * Support NEON Advanced SIMD(Single Instruction Multiple Data)instruction for acceleration of media and signal processing functions
    * Support Large Physical Address Extensions(LPAE)
    * VFPv4 Floating Point Unit
    * 32KB L1 Instruction cache and 32KB L1 Data cache
    * 128KB L2 cache

  * Boot ROM 
    * Internal on-chip memory
    * Size:32KB
    * Support system boot from the following device: 
      * SPI Nor flash
      * SPI Nand flash
      * SD/TF card
      * eMMC
    * Support system code download through USB OTG

  * SDRAM 
    * Internal on-chip memory
    * Integrated a 512Mbit DDR2 in V3s processor
    * Support clock frequency up to 400MHz
    * Support Memory Dynamic Frequency Scale(MDFS)

  * SD/MMC Interface 
    * External off-chip memory and storage device
    * Up to three SD/MMC controllers
    * 1/4-bit SD,SDIO,MMC mode
    * Complies with eMMC standard specification V4.41, SD physical layer specification V2.0, SDIO card specification V2.0
    * Support hardware CRC generation and error detection
    * Support block size from 1 to 65535 bytes

# Documentation
  * [File:Allwinner V3s Datasheet V1.0.pdf][57773]

# Software
## Original SDK
  * Archives, lichee/camdroid: [[1]][57774], [[2]][57775]
  * Github repository: [[3]][57776]

# Devices
► [V3s Boards][57777]
# Links
  * [Product Page][57760] (Allwinner Tech)
