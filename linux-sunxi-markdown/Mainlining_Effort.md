# Linux mainlining effort
(Redirected from [Mainlining Effort][34266])
 
The purpose of this page is to try and define sub-goals and milestones for the mainlining effort, containing goals and sub-goals with milestones for adding Allwinner support in the upstream mainline Linux Kernel. 
## Contents
  * [1 Overview][34269]
  * [2 Status][34270]
    * [2.1 Status Matrix][34271]
    * [2.2 Work In Progress][34272]
      * [2.2.1 Core Stuff][34273]
      * [2.2.2 Major drivers][34274]
      * [2.2.3 Minor drivers][34275]
      * [2.2.4 Drivers that can still be improved/added][34276]
    * [2.3 Planned for next][34277]
    * [2.4 Merged into 6.17(-rc1)][34278]
    * [2.5 Merged into 6.16][34279]
    * [2.6 Merged into 6.15][34280]
    * [2.7 Merged into 6.14][34281]
    * [2.8 Merged into 6.13][34282]
    * [2.9 Merged into 6.12][34283]
    * [2.10 Merged into 6.11][34284]
    * [2.11 Merged into 6.10][34285]
    * [2.12 Merged into 6.9][34286]
    * [2.13 Merged into 6.8][34287]
    * [2.14 Merged into 6.7][34288]
    * [2.15 Merged into 6.6 (LTS)][34289]
    * [2.16 Merged into 6.5][34290]
    * [2.17 Merged into 6.4][34291]
    * [2.18 Merged into 6.3][34292]
    * [2.19 Merged into 6.2][34293]
    * [2.20 Merged into 6.1 (LTS)][34294]
    * [2.21 Merged into 6.0][34295]
    * [2.22 Merged into 5.19][34296]
    * [2.23 Merged into 5.18][34297]
    * [2.24 Merged into 5.17][34298]
    * [2.25 Merged into 5.16][34299]
    * [2.26 Merged into 5.15 (LTS)][34300]
    * [2.27 Merged into 5.14][34301]
    * [2.28 Merged into 5.13][34302]
    * [2.29 Merged into 5.12][34303]
    * [2.30 Merged into 5.11][34304]
    * [2.31 Merged into 5.10 (LTS)][34305]
    * [2.32 Merged into 5.9][34306]
    * [2.33 Merged into 5.8][34307]
    * [2.34 Merged into 5.7][34308]
    * [2.35 Merged into 5.6][34309]
    * [2.36 Merged into 5.5][34310]
    * [2.37 Merged into 5.4 (LTS)][34311]
    * [2.38 Merged into 5.3][34312]
    * [2.39 Merged into 5.2][34313]
    * [2.40 Merged into 5.1][34314]
    * [2.41 Merged into 5.0][34315]
    * [2.42 Merged into 4.20][34316]
    * [2.43 Merged into 4.19 (LTS)][34317]
    * [2.44 Changes merged up to 4.18][34318]
  * [3 References][34319]
  * [4 See also][34320]
  * [5 External Links][34321]
    * [5.1 How to upstream][34322]
  * [6 Notes][34323]

# Overview
The idea is to submit the code needed to run the Linux kernel on Allwinner SoCs upstream, ie. to the official Linux kernel. 
This can be achieved by following the concept outlined in the _Your new ARM SoC Linux support check-list!_ article published by Thomas Petazzoni from Bootlin.[[1]][34324][[2]][34325]
Where relevant, I have attempted to include who is currently working on an item, mostly separate from any particular mainlining goal. 
# Status
The [Mainline Kernel howto][34326] contains the currently used repositories for the mainlining process. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][34327]. 
The [ Mainline Kernel category ][34328] gives an overview of currently supported devices. 
## Status Matrix
The goal of this matrix is to give an easy view of work on each SoC worked on by linux-sunxi. 
Model  | [F1C-  
100s  
200s][34329] | [A10][34330] | [A10s][34331] | [A13][34332]  
[R8][34333] | [GR8][34334] | [A20][34335]  
[T2][34336] | [R40][34337]  
[V40][34338]  
[T3][34339]  
[A40i][34340] | [A80][34341] | [A31][34342] | [A23][34343] | [A33][34344]  
[R16][34345] | [A83T][34346] | [H3][34347]  
[H2+][34348] | [S3][34349]  
[S3L][34350]  
[V3][34351]  
[V3s][34352] | [A64][34353]  
[H64][34354] | [H5][34355] | [H6][34356] | [A50][34357] | [V831][34358]  
[V833][34359] | [H313][34360]  
[H616][34361]  
[H618][34362]  
[H700][34363]  
[T507][34364] | [A100][34365]  
[A133][34366] | [R329][34367] | [D1][34368]  
[D1s][34369]  
[T113][34370] | [A523][34371]  
[A527][34372]  
[MR527][34373]  
[T527][34374]  
[H728][34375]  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
ADC  | GPADC  | N/A  | 4.12  | 4.12  | 4.12  | 4.12  | 4.12  | [WIP][34376] | NO  | [WIP][34376] | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | 6.11  | ?  | [WIP][34376] | 6.6  | NO   
[LRADC][34377] | 6.2  | 4.0  | 4.0  | 4.0  | 4.9  | 4.0  | ?  | ?  | 4.0  | 4.0  | 4.2  | 5.2  | ?  | 4.13  | 5.3  | ?  | N/A  | ?  | ?  | 6.11  | ?  | 5.19  | 5.19  | NO   
Thermal  | NO  | 3.16  | 3.14  | 3.14  | 4.9  | 3.16  | 5.7  | [WIP][34376] | [WIP][34376] | ?  | 4.12  | 5.6  | 5.6  | N/A  | 5.6  | 5.6  | 5.6  | ?  | ?  | 6.9  | 5.10  | ?  | 6.8  | [WIP][34376]  
Touch  | NO  | 3.16  | 3.14  | 3.14  | 4.9  | 3.16  | [WIP][34376] | NO  | 4.0  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | N/A  | ?  | NO  | N/A   
Audio  | AC97  | N/A  | NO  | N/A  | N/A  | N/A  | NO  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | N/A  | ?  | N/A  | N/A   
[Analog Codec][34378] | 6.14  | 4.4  | 4.4  | 4.4  | 4.9  | 4.4  | NO  | N/A  | 4.10  | 4.10  | 4.11  | N/A  | 4.10  | 4.13  | 5.0  | 4.12  | NO  | ?  | ?  | [WIP][34376] | ?  | WIP  | [WIP][34376] | NO   
Audio Hub  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | N/A  | NO  | N/A  | N/A  | N/A  | N/A   
DMIC  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 6.1  | ?  | N/A  | ?  | ?  | ?  | ?  | NO   
I2S  | NO  | 4.8  | ?  | N/A  | 4.9  | 4.8  | NO  | NO  | 4.13  | ?  | 4.11  | 4.16  | 4.14  | [WIP][34376] | 4.17  | NO  | 5.11  | ?  | ?  | NO  | ?  | 5.18  | 5.18  | [WIP][34376]  
[SPDIF][34379] | NO  | 4.7  | N/A  | N/A  | 4.9  | 4.7  | ?  | ?  | 4.9  | N/A  | N/A  | 4.13  | 4.11  | N/A  | 4.17  | 4.12  | 5.4  | ?  | ?  | 6.9  | ?  | ?  | WIP  | [WIP][34376]  
[Camera][34380] | BT656  | NO  | 5.6  | ?  | ?  | ?  | 5.4  | 5.6  | ?  | 5.0  | ?  | ?  | 5.3  | 5.0  | 5.0  | 5.1  | 5.0  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO   
ISP  | N/A  | NO  | N/A  | N/A  | N/A  | NO  | N/A  | NO  | NO  | N/A  | N/A  | NO  | N/A  | [WIP][34381] | N/A  | N/A  | N/A  | ?  | ?  | N/A  | ?  | ?  | ?  | ?   
MIPI CSI-2  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | [WIP][34381] | N/A  | N/A  | [WIP][34381] | N/A  | 5.19  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | ?  | ?  | ?  | NO   
Parallel  | NO  | 5.6  | ?  | ?  | ?  | 5.4  | 5.6  | ?  | 5.0  | ?  | ?  | 5.3  | 5.0  | 5.0  | 5.1  | 5.0  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO   
CAN bus  | ?  | 4.4  | N/A  | N/A  | N/A  | 4.4  | 5.17  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | N/A  | ?  | 6.6  | NO   
Clocks  | 5.0  | 3.10  | 3.11  | 3.10  | 4.9  | 3.12  | 4.14  | 3.19  | 3.12  | 3.17  | 4.2  | 4.13  | 4.8  | 4.11  | 4.10  | 4.12  | 4.17  | ?  | [WIP][34382] | 5.12  | 5.10  | WIP  | 5.17  | 6.15   
CPUFreq (DVFS)  | NO  | 4.0  | 4.0  | 4.0  | NO  | 4.0  | 6.0  | NO  | 4.2  | NO  | 4.11  | 4.17  | 4.18  | NO  | 5.6  | 5.9  | 5.8  | ?  | ?  | 6.10  | 6.15  | ?  | [WIP][34376] | WIP   
CPUIdle  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | Crust  | NO  | Crust  | Crust  | Crust  | NO  | NO  | NO  | NO  | NO  | SBI  | NO   
[Crypto][34383] | N/A  | 4.3  | 4.13  | 4.13  | 4.13  | 4.3  | 5.5  | 5.5  | 4.3  | ?  | 4.3  | 5.5  | 5.5  | 5.10  | 5.5  | 5.5  | 5.5  | ?  | ?  | 6.11  | NO  | ?  | 6.3  | NO   
[Display (DRM)][34384] | CVBS  | NO  | ?  | 4.9 ?  | 4.7  | 4.9  | ?  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][34376] | N/A  | N/A  | [WIP][34376] | NO  | ?  | ?  | ?  | ?  | ?  | NO  | ?   
G2D  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO  | NO   
HDMI Audio  | N/A  | [WIP][34376] | NO  | N/A  | N/A  | [WIP][34376] | NO  | NO  | [WIP][34376] | N/A  | N/A  | NO  | [WIP][34381] | N/A  | [WIP][34381] | [WIP][34381] | [WIP][34381] | ?  | ?  | ?  | ?  | ?  | NO  | NO   
HDMI CEC  | N/A  | 4.15  | 4.14  | N/A  | N/A  | 4.15  | 4.19  | NO  | 4.15  | N/A  | N/A  | 4.17  | 4.17  | N/A  | 4.20  | 4.17  | 5.2  | ?  | ?  | ?  | ?  | ?  | NO  | NO   
HDMI Video  | N/A  | 4.15  | 4.13  | N/A  | N/A  | 4.15  | 4.19  | NO  | 4.15  | N/A  | N/A  | 4.17  | 4.17  | N/A  | 4.20  | 4.17  | 5.0  | ?  | ?  | ?  | ?  | ?  | WIP  | NO   
LVDS  | N/A  | ?  | N/A  | N/A  | N/A  | 5.7  | ?  | ?  | ?  | ?  | ?  | 4.16  | N/A  | N/A  | ?  | N/A  | N/A  | ?  | ?  | [WIP][34376] | ?  | ?  | [WIP][34376] | NO   
MIPI DSI  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][34381] | NO  | NO  | ?  | 4.18  | NO  | N/A  | N/A  | 5.6  | N/A  | N/A  | ?  | ?  | N/A  | 6.2  | ?  | 6.2  | NO   
RGB  | NO  | 4.15  | ?  | 4.7  | 4.9  | 4.15  | NO  | 4.17  | 4.10  | 5.1  | 4.9  | 4.16  | N/A  | 4.13  | 5.3  | N/A  | NO  | ?  | ?  | [WIP][34376] | ?  | ?  | 6.0  | NO   
VGA  | N/A  | NO  | N/A  | N/A  | N/A  | NO  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | N/A  | ?  | N/A  | N/A   
Display (SimpleFB)  | NO  | 3.19  | 3.19  | 4.0  | 4.9  | 3.19  | NO  | NO  | 3.19  | 3.19  | 3.19  | NO  | 4.16  | 5.10  | 4.17  | 4.16  | NO  | ?  | ?  | ?  | ?  | ?  | NO  | NO   
DMA  | 6.14  | 4.3  | 4.3  | 4.3  | 4.9  | 4.3  | 5.10  | ?  | 3.17  | 3.18  | 4.2  | 4.9  | 4.2  | 4.13  | 4.15  | 4.12  | 5.3  | ?  | ?  | 6.9  | 6.1  | ?  | 5.19  | [WIP][34376]  
[Ethernet][34385] | [EMAC][34386] | N/A  | 3.11  | 3.11  | N/A  | N/A  | 3.11  | [WIP][34376] | 5.1  | N/A  | N/A  | N/A  | 4.16  | 4.15  | 4.13  | 4.15  | 4.15  | 5.0  | ?  | ?  | ?  | 6.17  | ?  | 5.15  | 6.16   
[GMAC][34387] | N/A  | N/A  | N/A  | N/A  | N/A  | 3.15  | 4.18  | 5.1  | 3.17  | N/A  | N/A  | 4.16  | 4.15  | 4.13  | 4.15  | 4.15  | 5.0  | ?  | N/A  | 6.0  | N/A  | ?  | N/A  | [WIP][34376]  
GPU (3D)  | [Mali][34388] | N/A  | 5.2  | ?  | ?  | ?  | 5.2  | 5.10  | N/A  | N/A  | ?  | ?  | N/A  | 5.2  | N/A  | 5.2  | 5.2  | 5.5  | ?  | ?  | 6.15  | N/A  | ?  | N/A  | 6.17   
[PowerVR][34389] | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | NO  | N/A  | N/A  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | N/A  | N/A   
HW Spinlocks  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | ?  | ?  | ?  | [WIP][34376] | [WIP][34376] | ?  | [WIP][34376] | NO  | NO  | ?  | ?  | N/A  | ?  | ?  | NO  | NO   
[I2C][34390] | 6.2  | 3.11  | 3.12  | 3.11  | 4.9  | 3.13  | 4.15  | 3.19  | 3.15  | 3.18  | 4.2  | 4.16  | 4.9  | 4.11  | 4.10  | 4.12  | 4.19  | ?  | ?  | 6.0  | 5.10  | ?  | 6.0  | 6.15   
IOMMU  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 5.8  | ?  | ?  | 6.11  | ?  | ?  | WIP  | NO   
[IR][34391] | [IR RX][34391] | 6.2  | 3.17  | 4.0  | 4.0  | 4.9  | 3.17  | 5.10  | 4.5  | 4.0  | N/A  | N/A  | 4.20  | 4.6  | N/A  | 5.4  | 4.12  | 5.4  | ?  | ?  | 6.0  | ?  | ?  | NO  | NO   
IR TX  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | N/A  | ?  | ?  | NO  | NO   
Keypad  | N/A  | WIP  | N/A  | N/A  | N/A  | WIP  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A   
LDOs  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | WIP  | WIP  | ?   
LEDC  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 6.8  | 6.8  | 6.8  | NO   
MBUS  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO  | NO  | ?  | ?  | ?  | NO  | 5.17  | 5.17  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | ?   
MsgBox  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | ?  | ?  | 5.8  | 5.8  | N/A  | 5.8  | 5.8  | 5.8  | ?  | ?  | N/A  | ?  | ?  | WIP  | NO   
PCIe  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][34381] [[3]][34392] | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO   
Pinctrl  | 5.0  | 3.9  | 3.9  | 3.9  | 4.9  | 3.12  | 4.14  | 3.19  | 3.12  | 3.18  | 4.2  | 4.4  | 4.5  | 4.11  | 4.6  | 4.12  | 4.17  | ?  | [WIP][34382] | 5.12  | 5.10  | WIP  | 6.0  | 6.15   
[PMU][34393] (perf, DT only)  | N/A  | 5.1  | ?  | ?  | ?  | 3.16  | 5.6  | ?  | 3.16  | ?  | ?  | ?  | 5.6  | ?  | 5.5  | 5.6  | 5.6  | ?  | ?  | 6.0  | 6.13  | ?  | [WIP][34376] | 6.16   
[PWM][34394] | 6.2  | 4.0  | 4.4  | 4.4  | 4.9  | 4.0  | [WIP][34376] | NO  | NO  | 4.4  | 4.4  | 4.16  | 4.9  | 4.12  | 4.19  | 4.12  | 5.6  | ?  | ?  | WIP  | WIP  | [WIP][34376] | [WIP][34376] | NO   
Remoteproc  | AIPU  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | ?  | NO  | N/A  | NO   
DSP  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | WIP  | WIP  | NO   
[RSB][34395] | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 4.3  | N/A  | 4.4  | 4.4  | 4.14  | ?  | N/A  | 4.13  | ?  | 5.12  | ?  | ?  | 6.0  | ?  | ?  | N/A  | N/A   
[RTC][34396] | N/A  | 3.14  | N/A  | N/A  | N/A  | 3.14  | 5.0  | N/A  | 3.18  | 3.18  | 4.2  | N/A  | 4.5  | 4.11  | 4.10  | 4.12  | 5.4  | ?  | [WIP][34382] | 6.0  | WIP  | WIP  | 6.0  | 6.15   
SID (eFuse)  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | 6.7  | 5.10  | ?  | 5.18  | 6.17   
SMP  | N/A  | N/A  | N/A  | N/A  | N/A  | PSCI  | PSCI  | 4.17  | PSCI  | PSCI  | PSCI  | 4.18  | PSCI  | N/A  | PSCI  | PSCI  | PSCI  | ?  | ?  | PSCI  | PSCI  | PSCI  | N/A  | PSCI   
[SPI][34397] | 5.19  | 3.16  | 3.15  | 3.15  | 4.9  | 3.15  | 5.6  | ?  | 3.15  | ?  | ?  | ?  | 4.10  | 4.13  | 4.15  | 4.12  | 5.7  | ?  | [WIP][34382] | 6.0  | WIP  | [WIP][34376] | 6.5  | NO   
[SRAM][34398] | 5.0  | 4.2  | 4.2  | 4.2  | 4.2  | 4.2  | 5.10  | N/A  | NO  | 4.19  | 4.19  | N/A  | 4.19  | 5.10  | 4.19  | 5.0  | 5.1  | ?  | ?  | 6.0  | 6.14  | ?  | 6.1  | [WIP][34376]  
Storage  | EMCE  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][34381] | ?  | ?  | N/A  | N/A  | ?  | N/A  | N/A   
[NAND][34399] | N/A  | ?  | ?  | 4.12 [[4]][34400] | 4.9 [[4]][34400] | ?  | ?  | ?  | ?  | 4.9 [[4]][34400] | 4.9 [[4]][34400] | ?  | ?  | N/A  | ?  | ?  | [WIP][34376] | ?  | ?  | [WIP][34376] | NO  | ?  | NO  | NO   
[SATA][34401] | N/A  | 3.15  | N/A  | N/A  | N/A  | 3.15  | 4.20  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A   
[SD/MMC][34402] | 5.19  | 3.16  | 3.16  | 3.16  | 4.9  | 3.16  | 4.14  | 4.0  | 3.16  | 3.18  | 4.2  | 4.14  | 4.5  | 4.11  | 4.11  | 4.12  | 4.19  | ?  | [WIP][34382] | 6.0  | 5.12  | WIP  | 5.18  | 6.15   
Timer  | Arch Timer  | N/A  | N/A  | N/A  | N/A  | N/A  | 3.15  | 4.15  | 4.2  | 4.0  | 4.2  | 4.2  | 4.6  | 4.5  | 4.11  | WIP  | 4.12  | 4.17  | ?  | ?  | 6.0  | 5.10  | ?  | WIP  | 6.16   
HSTIMER  | ?  | ?  | 4.2  | 4.2  | 4.2  | 3.14  | ?  | ?  | 4.2  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO   
TIMER  | 5.0  | 3.15  | 4.2  | 4.2  | 4.2  | 3.15  | 5.14  | 3.19  | 3.15  | 5.4  | 5.4  | 5.4  | 5.4  | 5.4  | 5.14  | 5.4  | 5.14  | ?  | ?  | ?  | ?  | ?  | 6.0  | ?   
[USB][34403] | [USB][34403] | 6.3  | 3.15  | 3.15  | 3.15  | 4.9  | 3.15  | 4.15  | 4.2  | 3.16  | 4.3  | 4.3  | 4.14  | 4.8  | 4.11  | 4.11  | 4.12  | 5.0  | ?  | ?  | 6.1.3  | 6.13  | ?  | 5.18  | 6.15   
[USB OTG][34404] | 6.3  | 4.3  | 4.3  | 4.3  | 4.9  | 4.3  | [WIP][34376] | NO  | 4.3  | 4.8  | 4.8  | 5.2  | 4.12  | 4.11  | 4.11  | 4.12  | 5.0  | ?  | ?  | 6.1.3  | 6.13  | ?  | 5.18  | 6.15   
USB3.0  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 5.5  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][34376]  
[VE][34405] | NO  | 5.1  | ?  | 4.20  | ?  | 4.20  | 5.10  | NO  | ?  | ?  | 4.20  | NO  | 4.20  | [WIP][34381] | 5.0  | 5.0  | 5.2  | ?  | ?  | ?  | ?  | ?  | 5.17  | NO   
Watchdog  | 5.19  | 3.12  | 3.12  | 3.12  | 4.9  | 3.12  | 4.15  | 3.19  | 3.18  | 3.18  | 4.2  | 4.6  | 4.5  | 4.11  | 4.17  | 4.12  | 5.3  | ?  | [WIP][34382] | 6.0  | 6.13  | 5.16  | 5.16  | 6.15   
Model  | [F1C-  
100s  
200s][34329] | [A10][34330] | [A10s][34331] | [A13][34332]  
[R8][34333] | [GR8][34334] | [A20][34335]  
[T2][34336] | [R40][34337]  
[V40][34338]  
[T3][34339]  
[A40i][34340] | [A80][34341] | [A31][34342] | [A23][34343] | [A33][34344]  
[R16][34345] | [A83T][34346] | [H3][34347]  
[H2+][34348] | [S3][34349]  
[S3L][34350]  
[V3][34351]  
[V3s][34352] | [A64][34353]  
[H64][34354] | [H5][34355] | [H6][34356] | [A50][34357] | [V831][34358]  
[V833][34359] | [H313][34360]  
[H616][34361]  
[H618][34362]  
[H700][34363]  
[T507][34364] | [A100][34365]  
[A133][34366] | [R329][34367] | [D1][34368]  
[D1s][34369]  
[T113][34370] | [A523][34371]  
[A527][34372]  
[MR527][34373]  
[T527][34374]  
[H728][34375]  
Legend   
---  
In Linux mainline since version x   
Nobody works on it, but it should be compatible with already done drivers   
Somebody works on it   
No support, nobody works on it   
support impossible   
Status is unknown/to be completed   
## Work In Progress
### Core Stuff
  * [A733][34406] **Andre Przywara** [pinctrl: sunxi: Allwinner A733 support][34407]

  * [V853][34408] / [V851s][34409] / [V851s3][34410] Andras Szemzo [Support for Allwinner V853 SoC][34411]

  * [R329][34367] Clocks & Pinctrl / RTC / MMC - Icenowy Zheng [Initial support for Allwinner R329][34412]

  * [V831][34358] / [V833][34359] Clocks & Pinctrl / RTC / MMC / Watchdog / SPI - Icenowy Zheng [Support for Allwinner V831 SoC][34413]

  * [AR100][34414] firmware (WiP: Samuel Holland) [ARISC firmware for sunxi SoCs ][34415]

  * [A13][34332] PSCI Suspend / Resume / CPUIdle (WiP: Antoine Tenart) [patch-v1][34416]

### Major drivers
  * [V3s][34352] ISP (Image Signal Processor) Paul Kocialkowski [initial-allwinner-v3-isp-support-in-mainline-linux][34417]

  * [H6][34356] Hypervisor for PCIe [A try on utilizing H6 PCIe with "Virtualization"][34418]

  * [A64][34353] / [H3][34347] / [H5][34355] / [H6][34356] HDMI Audio - Clément Péron / Marcus Cooper / Jernej Škrabec [Add Allwinner H3/H5/A64 HDMI audio][34419]

  * [R40][34337] MIPI-DSI WIP Jagan Teki [drm/sun4i: Allwinner R40 MIPI-DSI support v3][34420]

  * [AC100][34421] Audio codec WiP Ondrej Jirman [digital part][34422] [analog part][34423]

  * [V3s][34352] SRAM & Video Decoding Engine (Cedrus) WiP Martin Cerveny [Enable video decoder][34424] ([testing with attached LCD][34425])
  * [H6][34356] VP9 decoder (Hantro G2) WiP jernej [branch][34426]

### Minor drivers
  * [A523][34371] / [H728][34375] / [A527][34372] / [T527][34374] Chen-Yu Tsai [allwinner: a523: Enable I2S and SPDIF TX][34427]
  * [H6][34356], [H313][34360],[H616][34361],[H618][34362],[H700][34363],[T507][34364] Richard Genoud [Introduce Allwinner H6/H616 NAND controller support][34428]
  * [A523][34371] / [H728][34375] / [A527][34372] / [T527][34374] Mikhail Kalashnikov [arm64: allwinner: a523: add USB3.0 support][34429]
  * [H313][34360],[H616][34361],[H618][34362],[H700][34363],[T507][34364] Ryan Walklin [allwinner: h616: add LCD timing controller and display engine support][34430]
  * [A523][34371] / [H728][34375] / [A527][34372] / [T527][34374] Mikhail Kalashnikov [Add support for A523 Thermal system][34431]
  * [D1s][34369] / [T113][34370] Kuba Szczodrzyński [drm/sun4i: Support LVDS on D1s/T113 combo D-PHY][34432]
  * [A64][34353] Ondrej Jirman [A64 audio jack detection][34433]
  * [D1][34368] Brandon Cheo Fusi [cpufreq support for the D1][34434]
  * [D1][34368] Inochi Amaoto [riscv: dts: allwinner: d1: Add PMU event node][34435]
  * [D1][34368] / [T113][34370] Maksim Kiselev [ASoC: sunxi: Add support for D1/T113s internal audio codec][34436]
  * [H6][34356] ethernet on opi3/opi1+ LABBE Corentin [arm64: add ethernet to orange pi 3][34437]
  * [D1][34368] / [R329][34367] Aleksandr Shubin [Add support for Allwinner PWM on D1/T113s/R329 SoCs][34438]
  * [D1][34368] IOMMU Samuel Holland [iommu/sun50i: Allwinner D1 support][34439]
  * [D1][34368] System LDOs Samuel Holland [regulator: Add support for Allwinner D1 system LDOs][34440]
  * [D1][34368] Video Engine Samuel Holland [Allwinner D1 video engine support][34441]
  * [R40][34337]/[T3][34339]/[A40i][34340] RTP/LRADC Evgeny Boger [[1]][34442]
  * [R40][34337]/[T3][34339]/[A40i][34340] EMAC Evgeny Boger [support for two Ethernet ports on Allwinner R40][34443]
  * [R40][34337]/[T3][34339]/[A40i][34340] USB OTG qianfan Zhao [ARM: sun8i-r40: Enable usb otg support][34444]
  * [V3][34351] I2S Tobias Schramm [Add missing peripherals to Allwinner V3s/V3 device trees][34445]
  * [H3][34347] / [H5][34355] CVBS WIP Jernej Skrabec [Add H3/H5 TVE support][34446]
  * [A64][34353] hwspinlock WIP Nikolay Borisov [Add support for hwspinlock on A64 SoC][34447]
  * [A83T][34346] / [A64][34353] / [H3][34347] hwspinlock WIP Corentin Labbe (montjoie) [RFC,1/3][34448][RFC,2/3][34449][RFC,3/3][34450]
  * [A10][34330] / [A20][34335] / [A31][34342] HDMI Audio WIP Stefan Mavrodiev [Add support for sun4i HDMI audio][34451]
  * [A80][34341] Thermal sensor WIP Philipp Rossak (embed-3d): <https://github.com/embed-3d/linux/branches/all>
  * [R40][34337] PWM (WIP Hao Zhang [patch-v2][34452])
  * [A20][34335] Keypad (WiP: Yassin Jaffer (ddc) [patch][34453])
  * sun8i-ce/sun8i-ss RSA/ECC WIP Corentin LABBE (no public patch yet)
  * EMCE WIP Corentin LABBE (no public patch yet) / Mripard <https://git.kernel.org/pub/scm/linux/kernel/git/mripard/linux.git/log/?h=sunxi/h6-emmc-inline-encryption> BUT proably not usable <https://lore.kernel.org/linux-mmc/20210317171554.a4vgihqfjq2xa5cb@gilmour/>

### Drivers that can still be improved/added
Nobody works on these features. If you're interested, you can pick one of these add your name to them and move them to one of the sections above, to indicate you're working on the driver/feature. 
  * [A31][34342]/[A31s][34454] PWM support ([patch-v4][34455] abandoned by Siarhei Volkau)
  * sunxi-musb driver lacks DMA support (with current driver, USB gadgets are limited to PIO, limiting speed to 10MiB/s and causing large CPU)
  * DE2 driver has buggy layer support, see [[2]][34456]
  * DE1/DE2/DE3 writeback support
  * H616 (and later) UHS-I SD card support (pinctrl device contains voltage switch for PortF)

## Planned for next
## Merged into 6.17(-rc1)
  * [A523][34371]
    * Mali GPU support
    * power domain controller support
    * SID support
  * [A100/A133][34366]
    * EMAC Ethernet support

New devices supported: 
  * [A523][34371]: [Xunlong Orange Pi 4A][34457]

## Merged into 6.16
  * [A523][34371]
    * Basic DT support
    * First Ethernet port support
  * [H616][34361]
    * Mali GPU support

New devices supported 
  * [A133][34366]: [Liontron H-A133L][34458]
  * [H616][34361]: YuzukiHD Chameleon
  * [A523][34371]: [Radxa Cubie A5E][34459]
  * [A523][34371]: [X96QPro+][34460]
  * [A523][34371]: [YuzukiHD Avaota A1][34461]

## Merged into 6.15
  * [A100/A133][34366]
    * enable DVFS support
  * [A523][34371]
    * main and PRCM clock support
    * pinctrl/GPIO support
    * watchdog support
    * NMI support

New devices supported 
  * [V3s][34352]: [NetCube Systems Kumquat][34462]

## Merged into 6.14
  * [A100/A133][34366]
    * syscon support
  * [F1C100s][34329]
    * DMA support
    * audio codec support

## Merged into 6.13
  * [A100/A133][34366]
    * PMU support (for perf tool)
    * watchdog support
    * USB support
    * MMC support
  * [H616][34361]
    * audio codec support

New devices supported 
  * [A33][34344]: RerVision A33-Vstar board

## Merged into 6.12
New devices supported 
  * [H616][34361]: Anbernic RG35XX-SP

## Merged into 6.11
  * [H616][34361]
    * LRADC support
    * IOMMU support
    * crypto engine

## Merged into 6.10
  * [D1][34368]/[T113-s3][34370]
    * LDO driver
  * [H616][34361]
    * enable DVFS support
  * sun4i-i2s: Support 32-bit audio formats

New devices supported 
  * [A13][34332]: PocketBook 614 Plus
  * [H616][34361]: [Tanix TX1][34463]
  * [H616][34361]: [Anbernic RG35XX Plus][34464]
  * [H616][34361]: [Anbernic RG35XX H][34465]
  * [H616][34361]: Anbernic RG35XX 2024

## Merged into 6.9
  * [H616][34361]
    * SPDIF
    * DMA
    * Thermal

New Devices supported 
  * [H616][34361]: Sipeed LonganPi 3H
  * [A64][34353]: [Remix Mini PC][34466]

## Merged into 6.8
  * [D1][34368]/[T113-s3][34370]
    * Thermal

New Devices supported 
  * [H616][34361]: [OrangePi Zero 2W][34467]
  * [H616][34361]: [Transpeed 8K618-T][34468]

## Merged into 6.7
  * [H616][34361]
    * SID

New Devices supported 
  * [H616][34361]: Bigtreetech CB1 Manta
  * [H616][34361]: Bigtreetech Pi
  * [V3s][34352]: Anbernic RG-Nano

## Merged into 6.6 (LTS)
  * [D1][34368]/[T113-s3][34370]
    * CAN
    * GPADC

New Devices supported 
  * [H616][34361]: [OrangePi Zero 3][34469]

## Merged into 6.5
  * [D1][34368]/[T113-s3][34370]
    * SPI

## Merged into 6.4
  * [F1C100s][34329]
    * Enable [LicheePi Nano][34470] USB support

New Devices supported 
  * [F1C100s][34329]
    * Popcorn Computer PopStick
    * [Lctech Pi F1C200s][34471]

  * [T113-s3][34370]
    * [MangoPi MQ-R-T113][34472]

## Merged into 6.3
  * [D1][34368]
    * Base DT and Kconfig
    * Crypto
    * Power Domain

  * [T113-s3][34370]
    * R528/T113 Clocks support

  * [F1C100s][34329]
    * USB PHY support
    * USB MUSB support

## Merged into 6.2
  * [A100][34365]
    * MIPI-DSI
  * [D1][34368]
    * MIPI-DSI

## Merged into 6.1 (LTS)
  * [A100][34365]
    * DMA
  * [D1][34368]
    * SRAM
  * [H6][34356]
    * DMIC
    * GPU Devfreq

## Merged into 6.0
  * [D1][34368]
    * RGB LCD
    * I2C
    * Pinctrl
    * RTC
  * [H616][34361] [Orange Pi Zero 2][34473]
  * [H616][34361] [X96 Mate][34474]
  * [R40][34337]/[T3][34339]/[A40i][34340]
    * CPUFreq (DVFS)

## Merged into 5.19
  * [D1][34368]
    * DMA
    * LRADC
  * [F1C100s][34329]
    * SD/MMC
    * SPI
    * Watchdog
  * [V3s][34352]
    * [MIPI-CSI2][34475]

## Merged into 5.18
  * [D1][34368]
    * I2S
    * MMC
    * SID
    * USB

## Merged into 5.17
  * [A64][34353]/[H5][34355]
    * DRAM frequency scaling (DEVFREQ)
  * [D1][34368]
    * Clocks
    * PLIC
  * [R40][34337]/[T3][34339]/[A40i][34340]
    * CAN ([series][34476])

## Merged into 5.16
  * [R329][34367]/[D1][34368]
    * Watchdog

## Merged into 5.15 (LTS)
## Merged into 5.14
  * [H616][34361]
    * PMIC - AXP305

New Devices Supported 
  * [H616][34361]
    * [Tanix TX6s][34477]
    * [X96 Mate][34474]
    * [Xunlong Orange Pi Zero2][34478]

## Merged into 5.13
New Devices Supported 
  * [A10][34330]
    * Topwise A721 Tablet

## Merged into 5.12
  * [H616][34361]
    * Clocks
    * Pinctrl
    * MMC
  * [H6][34356]
    * RSB
  * [A100][34365]
    * MMC

## Merged into 5.11
  * [H6][34356]
    * [I2S][34479]
  * multiple SoCs 
    * [Cedrus][34480] VP8 decoding

New Devices Supported 
  * [H3][34347]
    * [FriendlyArm NanoPi R1][34481]
    * [FriendlyArm ZeroPi][34482]
  * [S3][34349]
    * [Elimo Impetus][34483]
    * [Elimo Initium][34484]

## Merged into 5.10 (LTS)
  * [A100][34365]
    * Clocks
    * Pinctrl
    * [I2C][34390]
    * Thermal (THS)

  * [R40][34337]
    * DMA
    * GPU [Mali][34388]
    * [IR][34391]
    * [SRAM][34398]
    * [Video_Engine][34405] | [Sunxi-Cedrus][34485]

  * [V3s][34352]
    * Crypto
    * Ethernet
    * SimpleFB
    * [SRAM][34398]

  * sun8i-ce/sun8i-ss 
    * support for PRNG
    * support for hashs
    * support for TRNG ([H6][34356] only)

New Devices Supported 
  * [A100][34365]
    * [Perf1 board][34486]
  * [S3l][34487]
    * [PineCube][34488]

## Merged into 5.9
  * [H5][34355]
    * DVFS

New Devices Supported 
  * A64 
    * PinePhone v1.2

## Merged into 5.8
  * [H6][34356]
    * DVFS
    * IOMMU

  * [A64][34353] / [A83T][34346] / [H3][34347] / [H5][34355] / [H6][34356]
    * Message Box

New Devices Supported 
  * A20 
    * [OLinuXino Lime (A20)][34489] eMMC

## Merged into 5.7
  * [A20][34335]
    * LVDS

  * [A83T][34346] and [A64][34353]
    * Rotate driver

  * [H6][34356]
    * [SPI][34397]

  * [R40][34337]
    * Thermal

New Devices Supported 
  * [A13][34332]
    * [PocketBook Touch Lux 3][34490]
  * [A64][34353]
    * [PineTab][34491]
    * [PinePhone][34492] v1.0 & v1.1
  * [A20][34335]
    * Linutronix Testbox v2

## Merged into 5.6
  * [A10][34330]
    * CSI (BT656 and Parallel)

  * [A64][34353]
    * MIPI DSI
    * DVFS

  * [A64][34353] / [A83T][34346] / [H3][34347] / [H5][34355] / [H6][34356]
    * Thermal

  * [H6][34356]
    * PWM

  * [H3][34347] / [H5][34355] / [H6][34356] / [R40][34337]
    * PMU

  * [R40][34337]
    * CSI (BT656 and Parallel)
    * [SPI][34397]

New Devices Supported 
  * [H5][34355]
    * ALL-H3-IT H5 board
    * ALL-H5-CC H5 board
  * [H6][34356]
    * [PineH64][34493] Model B

## Merged into 5.5
  * [H3][34347]
    * Deinterlace driver

  * [H6][34356]
    * Crypto
    * GPU(3D) Mali
    * USB3 PHY (for boards not needing vbus switching)

  * [A64][34353] / [A80][34341] / [A83T][34346] / [H3][34347] / [H5][34355] / [R40][34337]
    * Crypto

  * multiple SoCs 
    * [Cedrus][34480] HEVC/H.265

  * [Broadcom-based (AMPAK modules) Bluetooth][34494] support on 
    * Emlid Neutis

New Devices Supported 
  * [H3][34347]
    * [FriendlyARM_NanoPi_Duo2][34495]

## Merged into 5.4 (LTS)
  * [A20][34335]
    * CSI (BT656 and Parallel)
  * [A64][34353]
    * IR
  * [H6][34356]
    * IR
    * RTC
    * SPDIF

New Devices Supported 
  * [A64][34353]
    * [Olimex A64-OLinuXino][34496] eMMC
  * [H6][34356]
    * [Tanix TX6][34497]
  * [S3][34349]
    * [Lichee Zero Plus][34498]

## Merged into 5.3
  * [A64][34353]
    * LRADC
    * RGB LCD
  * [A83T][34346]
    * CSI (BT656 and Parallel)
  * [H6][34356]
    * DMA
    * Watchdog
  * multiple SoCs 
    * [Cedrus][34480] h264

## Merged into 5.2
  * [A83T][34346]
    * LRADC
    * USB OTG

  * [H6][34356]
    * [Cedrus][34480]

  * multiple SoCs 
    * [Lima][34499]
    * [Panfrost][34499]

  * [Broadcom-based (AMPAK modules) Bluetooth][34494] support on 
    * Banana-Pi-M2-Zero

New Devices Supported 
  * [H6][34356]
    * [Beelink GS1][34500]
    * [Xunlong Orange Pi 3][34501]

## Merged into 5.1
  * A10 
    * Cedrus
    * PMU

  * A20 
    * Audio Codec improvements

  * A23 
    * Display pipeline
    * LCD enabled on Q8 A23 tablets

  * A64 
    * [ARM Architectural Timer errata workaround][34502]
    * PMU
    * CSI (BT656 and Parallel)

  * A80 
    * GMAC support

  * CSI in general 
    * RGR565 support
    * JPEG pass-through support

  * [Broadcom-based (AMPAK modules) Bluetooth][34494] support on 
    * [Banana Pi M2+][34503]
    * [Banana Pi M2 Ultra][34504]

  * [LCD][34505] enabled on [A13][34332] [Q8][34506] tablets

## Merged into 5.0
  * A64 
    * Cedrus
    * DTS changes for audio codec

  * F1C100s 
    * initial F1C100s support

  * H6 
    * Ethernet
    * DE3/HDMI support
    * USB 2.0

  * H3 / H5 
    * CSI (BT656 and Parallel) Support

  * H5 
    * Cedrus

  * R40 
    * RTC

  * T3 
    * initial T3 support[[5]][34507]

  * V3s 
    * CSI (BT656 and Parallel) Support

  * [Broadcom-based (AMPAK modules) Bluetooth][34494] support on 
    * [ Banana Pi M2 Magic][34508]
    * [Banana Pi M3][34509]
    * [Banana Pi M64][34510]
    * [Cubietruck][34511]
    * [Cubietruck Plus][34512]

New Devices Supported 
  * [Xunlong Orange Pi Lite 2][34513]
  * Mapleboard MP130
  * LicheePi Nano
  * Emlid Neutis N5

## Merged into 4.20
  * A13 / A20 / A33 / H3 
    * Cedrus driver

  * A83T 
    * IR receiver

  * A64 
    * Cleanup for device tree files
    * HDMI support
    * Audio codec support (DTS changes will be merged in 5.0)

  * H3 / H5 
    * SID

  * R40 
    * SATA

New Devices Supported 
  * [Pine64][34514] LTS
  * [Xunlong Orange Pi One Plus][34515]
  * [Xunlong Orange Pi Zero Plus 2][34516] (H3 variant)
  * [Sinovoip Banana Pi M2+][34517] (H5 variant)

## Merged into 4.19 (LTS)
  * A10 / A13 / A20 / A23 / A33 
    * SRAM controller / system control

  * A64 
    * SRAM controller / system control
    * Display clocks and bus
    * RTC clock output
    * PWM
    * R_I2C

  * H3 
    * SRAM controller / system control

  * H6 
    * MMC
    * PMIC

  * R40 
    * HDMI support

Board Changes 
  * SPI flash node for [Orange Pi PC 2][34518] and [ Pine64 SoPINE][34519]
  * Use lid switch as wake-up source for A64 based laptops
  * LEDs added for [PineH64][34493]

New Devices 
  * [Pine Pinebook][34520]
  * Amarula A64-Relic

## Changes merged up to 4.18
Changes up to 4.18 can be found on [Linux mainlining history][34521] page. 
# References
  1. [↑][34522] <http://www.elinux.org/images/a/ad/Arm-soc-checklist.pdf>
  2. [↑][34523] [Your New ARM SoC Linux Support Check-List – ELCE 2012][34524]
  3. [↑][34525] Allwinner H6 has a quirky PCIe controller that doesn't map the PCIe address space properly to CPU, and accessing the PCIe config space, IO space or memory space needs to be wrapped. As Linux doesn't wrap PCIe memory space access, it's not possible to do a proper PCIe controller without using an hypervisor. The BSP kernel modifies the driver to wrap the access, so it's also not generic, and only devices with modified driver will work. <https://forum.armbian.com/topic/13529-a-try-on-utilizing-h6-pcie-with-virtualization/>
  4. ↑ [4.0][34526] [4.1][34527] [4.2][34528] [4.3][34529] While the NAND controller itself is supported, the NAND technology found on the vast majority of boards isn't. See [this page][34530]
  5. [↑][34531] <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=b7badd1d7aa61087010803affa19bb83fb5a0af1>

# See also
  * [Mainline Kernel Howto][34326]
  * [Possible setups for hacking on mainline][34532]
  * [Linux Kernel][34533]
    * [Toolchain][34534]

# External Links
  * [kernel.org][34535] \- Official website for the Linux Kernel 
    * <http://github.com/torvalds/linux> \- Linus Torvalds' GitHub account with the upstream Linux kernel
  * [Linux Kernel documentation index][34536]
  * [Linux Kernel man pages][34537]
  * [Kernel Newbies Site - Excellent source of information for people new to kernel][34538]
  * [Linus' kernel tree for 2.6][34539]
  * [Kernel bugzilla][34540] \- [Regressions for each of recent versions][34541]
  * [Linux-libre project - Maintains and distributes fully free kernel][34542]
  * [LinGrok, Linux kernel source code cross-reference][34543]
  * [Bootlin LXR (Linux Cross Reference)][34544]
  * [linux-arm-kernel - Mailing list archive][34545]

### How to upstream
  * [Your new ARM SoC Linux support check-list! by Thomas Petazzoni of Bootlin][34546]
  * [Linux Kernel Upstreaming How-To (CNXSoft - Embedded Software Development)][34547]
    * [Matt Porter's YouTube video talk on “Upstreaming 101" (LCA14-111)][34548]
      * [Matt Porter's presentation slides for “Upstreaming 101" (LCA14-111)][34549]
    * [Matt Porter's YouTube video talk on “Upstreaming 201" (LCA14-112)][34550]
      * [Matt Porter's presentation slides for “Upstreaming 201" (LCA14-112)][34551]
  * [How to Write and Submit a Linux Kernel Patch (CNXSoft - Embedded Software Development)][34552]
    * [YouTube Video- Write and Submit your first Linux kernel Patch][34553]
    * [Greg Kroah-­Hartman Kernel Tutorial Write and Submit your first Linux Kernel Patch][34554]
  * [Linaro resources page from LCA (Linaro Connect Asia) 2014][34555]

# Notes
