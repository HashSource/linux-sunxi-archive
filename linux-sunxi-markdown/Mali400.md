# Mali
(Redirected from [Mali400][34671])
 
The **Mali** series is a GPU (Graphics Processor Unit) from ARM Ltd. (ARM Holdings plc), designed for embedded systems.[[1]][34674][[2]][34675]
## Contents
  * [1 Overview][34676]
    * [1.1 Variants:][34677]
      * [1.1.1 Utgard][34678]
      * [1.1.2 Midgard][34679]
      * [1.1.3 Bifrost][34680]
  * [2 Driver][34681]
    * [2.1 Utgard (Mali-400 and Mali-450)][34682]
      * [2.1.1 Lima driver (Open Source)][34683]
      * [2.1.2 Binary driver][34684]
    * [2.2 Midgard (Mali T6xx, T7xx, T8xx) and Bifrost (G3x, G5x, G6x, G7x)][34685]
      * [2.2.1 Panfrost driver (Open Source)][34686]
  * [3 See also][34687]
  * [4 References][34688]
  * [5 External Links][34689]

# Overview
[![][34690]][34691]
[][34692]
es2gears running on Mali-400
[![][34693]][34694]
[][34695]
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
Mali-400 MP  | 1  | 1  | 256 KiB  | [A10][34696] (sun4i), [A10s][34697] (sun5i), and [A13][34698] (sun5i)   
Mali-400 MP2  | 1  | 2  | 256/512 KiB  | [A20][34699] (sun7i), [A23][34700] (sun8i), [A33][34701], [H3][34702], [R40][34703] (sun8i), [A64][34704] (sun50i)   
Mali-450 MP4  | 1  | 4  | 512 KiB  | [H5][34705] (sun50i)   
### Midgard
Name | unified shader cores | CPU Level 2 cache size | Allwinner implementations   
---|---|---|---  
Mali-T720 MP2  | 2  | 512 KiB  | [H6][34706] (sun50i)   
Mali-T760 MP2  | 2  | 512 KiB  | [A63][34707] (sun50i)   
### Bifrost
Name | unified shader cores | CPU Level 2 cache size | Allwinner implementations   
---|---|---|---  
Mali-G31 MP2  | 2  | ??? KiB  | [H616][34708], [H313][34709] (sun50i)   
More information can be found on the [ARM website][34710]. 
# Driver
## Utgard (Mali-400 and Mali-450)
### Lima driver (Open Source)
Lima is a project to develop a completely open source graphics driver which supports ARM's Mali-400 and Mali-450 GPUs. 
It consists of two main parts: 
  * [Kernel parts][34711] have been included in mainline kernel since v5.2
  * [Mesa][34712] (userspace) parts have been part of upstream project since April 2019.

Historical links: 
  * Pre-merge development of [Lima kernel driver][34713]
  * Pre-merge development of [mesa-lima userspace driver][34714]
  * based on re-engineering efforts from [Archive of http://limadriver.org/][34715]

### Binary driver
  * **Mainline Linux:** Maxime Ripard (Bootlin) worked on Mali OpenGL support with mainline Linux, please refer [these instructions][34716]
  * **Legacy Kernel (Outdated):** For information on the binary driver, please refer to the [ binary driver installation guide][34717].

## Midgard (Mali T6xx, T7xx, T8xx) and Bifrost (G3x, G5x, G6x, G7x)
### Panfrost driver (Open Source)
[Panfrost][34718] is a project to develop a completely open source graphics driver which supports ARM's Mali-T6xx, Mali-T7xx, Mali-T800 and Mali-G7x GPUs. This is a **work in progress and not yet ready** for general use.  
[Panfrost][34718] results from a merge of 2 driver reverse engineering projects: chai - for Midgard GPUs (by Alyssa Rosenzweig) and BiOpenly - for Bifrost GPUs (by Lyude Paul). The merge was done due to identical command streams of the ARM Midgard and Bifrost GPUs (but different shader cores). 
  * WIP: [Panfrost git repository][34718]
  * Alyssa Rosenzweig's Blog: [NIR shader compiler announce][34719]

  

The aim of this drivers and others such as freedreno is to finally bring all the advantages of open source software to ARM SoC graphics drivers. Currently, the sole availability of binary drivers is increasing development and maintenance overhead, while also reducing portability, compatibility and limiting choice. Anyone who has dealt with GPU support on ARM, be it for a linux with a GNU stack, or for an android, knows the pain of dealing with these binaries. 
  * [Graphics hardware and FOSS][34720]

# See also
  * [Display driver setup.][34721]
  * [ Mali binary driver installation][34717].

# References
  1. [↑][34722] <http://www.cnx-software.com/2013/01/19/gpus-comparison-arm-mali-vs-vivante-gcxxx-vs-powervr-sgx-vs-nvidia-geforce-ulp/> GPUs Comparison: ARM Mali vs Vivante GCxxx vs PowerVR SGX vs Nvidia Geforce ULP
  2. [↑][34723] <http://blog.thinkteletronics.com/all-mobile-socsolutions/> All Mobile Soc/Solutions.

# External Links
  * [Mali-400 MP website][34724]
  * [GPUs Comparison: ARM Mali vs Vivante GCxxx vs PowerVR SGX vs Nvidia Geforce ULP][34725]
  * [MALI graphics hardware series webpage at ARM Holdings][34726]
  * [Mali developer][34727] a developer site run by ARM
  * [Open Source Mali GPUs Linux EXA/DRI2 and X11 Display Drivers][34728]
  * [Lima driver (Web Archive)][34715]
