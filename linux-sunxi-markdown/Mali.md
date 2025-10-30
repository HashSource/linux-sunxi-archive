# Mali
The **Mali** series is a GPU (Graphics Processor Unit) from ARM Ltd. (ARM Holdings plc), designed for embedded systems.[[1]][34587][[2]][34588]
## Contents
  * [1 Overview][34589]
    * [1.1 Variants:][34590]
      * [1.1.1 Utgard][34591]
      * [1.1.2 Midgard][34592]
      * [1.1.3 Bifrost][34593]
  * [2 Driver][34594]
    * [2.1 Utgard (Mali-400 and Mali-450)][34595]
      * [2.1.1 Lima driver (Open Source)][34596]
      * [2.1.2 Binary driver][34597]
    * [2.2 Midgard (Mali T6xx, T7xx, T8xx) and Bifrost (G3x, G5x, G6x, G7x)][34598]
      * [2.2.1 Panfrost driver (Open Source)][34599]
  * [3 See also][34600]
  * [4 References][34601]
  * [5 External Links][34602]

# Overview
[![][34603]][34604]
[][34605]
es2gears running on Mali-400
[![][34606]][34607]
[][34608]
XBMC running on Mali-400
The **Mali** series of Graphics Processing Units (GPUs) are semiconductor intellectual property cores produced by ARM Holdings for licensing in various ASIC (Application-specific integrated circuit) designs by ARM partners. The core is mainly developed by ARM Norway, at the former _Falanx_ company site. 
Like other embedded IP cores for 3D support, the Mali GPU does not feature display controllers driving monitors (such as the combination often found in common video cards). Instead it is a pure 3D engine that renders graphics into memory and hands the rendered image over to another core that handles the display. 
ARM supplies tools to help in authoring OpenGL ES shaders named _Mali GPU Shader Development Studio_ and _Mali GPU User Interface Engine_. 
All Mali4XX GPU Variants conform to OpenGL ES 1.1 & 2.0 as well as OpenVG 1.1.  
All Mali-TXXX GPU Variants conform to OpenGL ES up to 3.1 as well as OpenVG 1.1.  
All Mali-GXX GPU Variants conform to OpenGL ES up to 3.2 as well as OpenVG 1.1 and Vulkan 1.2 (panvk Vulkan driver not yet fully conformant). 
## Variants:
There are several generations of which two are currently used by Allwinner. 
### Utgard
Name | GP (Geometry Processor)   
/ vertex shader | PP (Pixel Processor)   
/ fragment shader | CPU Level 2 cache size | Allwinner implementations   
---|---|---|---|---  
Mali-400 MP  | 1  | 1  | 256 KiB  | [A10][34609] (sun4i), [A10s][34610] (sun5i), and [A13][34611] (sun5i)   
Mali-400 MP2  | 1  | 2  | 256/512 KiB  | [A20][34612] (sun7i), [A23][34613] (sun8i), [A33][34614], [H3][34615], [R40][34616] (sun8i), [A64][34617] (sun50i)   
Mali-450 MP4  | 1  | 4  | 512 KiB  | [H5][34618] (sun50i)   
### Midgard
Name | unified shader cores | CPU Level 2 cache size | Allwinner implementations   
---|---|---|---  
Mali-T720 MP2  | 2  | 512 KiB  | [H6][34619] (sun50i)   
Mali-T760 MP2  | 2  | 512 KiB  | [A63][34620] (sun50i)   
### Bifrost
Name | unified shader cores | CPU Level 2 cache size | Allwinner implementations   
---|---|---|---  
Mali-G31 MP2  | 2  | ??? KiB  | [H616][34621], [H313][34622] (sun50i)   
More information can be found on the [ARM website][34623]. 
# Driver
## Utgard (Mali-400 and Mali-450)
### Lima driver (Open Source)
Lima is a project to develop a completely open source graphics driver which supports ARM's Mali-400 and Mali-450 GPUs. 
It consists of two main parts: 
  * [Kernel parts][34624] have been included in mainline kernel since v5.2
  * [Mesa][34625] (userspace) parts have been part of upstream project since April 2019.

Historical links: 
  * Pre-merge development of [Lima kernel driver][34626]
  * Pre-merge development of [mesa-lima userspace driver][34627]
  * based on re-engineering efforts from [Archive of http://limadriver.org/][34628]

### Binary driver
  * **Mainline Linux:** Maxime Ripard (Bootlin) worked on Mali OpenGL support with mainline Linux, please refer [these instructions][34629]
  * **Legacy Kernel (Outdated):** For information on the binary driver, please refer to the [ binary driver installation guide][34630].

## Midgard (Mali T6xx, T7xx, T8xx) and Bifrost (G3x, G5x, G6x, G7x)
### Panfrost driver (Open Source)
[Panfrost][34631] is a project to develop a completely open source graphics driver which supports ARM's Mali-T6xx, Mali-T7xx, Mali-T800 and Mali-G7x GPUs. This is a **work in progress and not yet ready** for general use.  
[Panfrost][34631] results from a merge of 2 driver reverse engineering projects: chai - for Midgard GPUs (by Alyssa Rosenzweig) and BiOpenly - for Bifrost GPUs (by Lyude Paul). The merge was done due to identical command streams of the ARM Midgard and Bifrost GPUs (but different shader cores). 
  * WIP: [Panfrost git repository][34631]
  * Alyssa Rosenzweig's Blog: [NIR shader compiler announce][34632]

  

The aim of this drivers and others such as freedreno is to finally bring all the advantages of open source software to ARM SoC graphics drivers. Currently, the sole availability of binary drivers is increasing development and maintenance overhead, while also reducing portability, compatibility and limiting choice. Anyone who has dealt with GPU support on ARM, be it for a linux with a GNU stack, or for an android, knows the pain of dealing with these binaries. 
  * [Graphics hardware and FOSS][34633]

# See also
  * [Display driver setup.][34634]
  * [ Mali binary driver installation][34630].

# References
  1. [↑][34635] <http://www.cnx-software.com/2013/01/19/gpus-comparison-arm-mali-vs-vivante-gcxxx-vs-powervr-sgx-vs-nvidia-geforce-ulp/> GPUs Comparison: ARM Mali vs Vivante GCxxx vs PowerVR SGX vs Nvidia Geforce ULP
  2. [↑][34636] <http://blog.thinkteletronics.com/all-mobile-socsolutions/> All Mobile Soc/Solutions.

# External Links
  * [Mali-400 MP website][34637]
  * [GPUs Comparison: ARM Mali vs Vivante GCxxx vs PowerVR SGX vs Nvidia Geforce ULP][34638]
  * [MALI graphics hardware series webpage at ARM Holdings][34639]
  * [Mali developer][34640] a developer site run by ARM
  * [Open Source Mali GPUs Linux EXA/DRI2 and X11 Display Drivers][34641]
  * [Lima driver (Web Archive)][34628]
