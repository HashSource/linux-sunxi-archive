# Linux mainlining effort
The purpose of this page is to try and define sub-goals and milestones for the mainlining effort, containing goals and sub-goals with milestones for adding Allwinner support in the upstream mainline Linux Kernel. 
## Contents
  * [1 Overview][32039]
  * [2 Status][32040]
    * [2.1 Status Matrix][32041]
    * [2.2 Work In Progress][32042]
      * [2.2.1 Core Stuff][32043]
      * [2.2.2 Major drivers][32044]
      * [2.2.3 Minor drivers][32045]
      * [2.2.4 Drivers that can still be improved/added][32046]
    * [2.3 Planned for next][32047]
    * [2.4 Merged into 6.17(-rc1)][32048]
    * [2.5 Merged into 6.16][32049]
    * [2.6 Merged into 6.15][32050]
    * [2.7 Merged into 6.14][32051]
    * [2.8 Merged into 6.13][32052]
    * [2.9 Merged into 6.12][32053]
    * [2.10 Merged into 6.11][32054]
    * [2.11 Merged into 6.10][32055]
    * [2.12 Merged into 6.9][32056]
    * [2.13 Merged into 6.8][32057]
    * [2.14 Merged into 6.7][32058]
    * [2.15 Merged into 6.6 (LTS)][32059]
    * [2.16 Merged into 6.5][32060]
    * [2.17 Merged into 6.4][32061]
    * [2.18 Merged into 6.3][32062]
    * [2.19 Merged into 6.2][32063]
    * [2.20 Merged into 6.1 (LTS)][32064]
    * [2.21 Merged into 6.0][32065]
    * [2.22 Merged into 5.19][32066]
    * [2.23 Merged into 5.18][32067]
    * [2.24 Merged into 5.17][32068]
    * [2.25 Merged into 5.16][32069]
    * [2.26 Merged into 5.15 (LTS)][32070]
    * [2.27 Merged into 5.14][32071]
    * [2.28 Merged into 5.13][32072]
    * [2.29 Merged into 5.12][32073]
    * [2.30 Merged into 5.11][32074]
    * [2.31 Merged into 5.10 (LTS)][32075]
    * [2.32 Merged into 5.9][32076]
    * [2.33 Merged into 5.8][32077]
    * [2.34 Merged into 5.7][32078]
    * [2.35 Merged into 5.6][32079]
    * [2.36 Merged into 5.5][32080]
    * [2.37 Merged into 5.4 (LTS)][32081]
    * [2.38 Merged into 5.3][32082]
    * [2.39 Merged into 5.2][32083]
    * [2.40 Merged into 5.1][32084]
    * [2.41 Merged into 5.0][32085]
    * [2.42 Merged into 4.20][32086]
    * [2.43 Merged into 4.19 (LTS)][32087]
    * [2.44 Changes merged up to 4.18][32088]
  * [3 References][32089]
  * [4 See also][32090]
  * [5 External Links][32091]
    * [5.1 How to upstream][32092]
  * [6 Notes][32093]

# Overview
The idea is to submit the code needed to run the Linux kernel on Allwinner SoCs upstream, ie. to the official Linux kernel. 
This can be achieved by following the concept outlined in the _Your new ARM SoC Linux support check-list!_ article published by Thomas Petazzoni from Bootlin.[[1]][32094][[2]][32095]
Where relevant, I have attempted to include who is currently working on an item, mostly separate from any particular mainlining goal. 
# Status
The [Mainline Kernel howto][32096] contains the currently used repositories for the mainlining process. The U-Boot repository and toolchain is described in the [Mainline U-Boot howto][32097]. 
The [ Mainline Kernel category ][32098] gives an overview of currently supported devices. 
## Status Matrix
The goal of this matrix is to give an easy view of work on each SoC worked on by linux-sunxi. 
Model  | [F1C-  
100s  
200s][32099] | [A10][32100] | [A10s][32101] | [A13][32102]  
[R8][32103] | [GR8][32104] | [A20][32105]  
[T2][32106] | [R40][32107]  
[V40][32108]  
[T3][32109]  
[A40i][32110] | [A80][32111] | [A31][32112] | [A23][32113] | [A33][32114]  
[R16][32115] | [A83T][32116] | [H3][32117]  
[H2+][32118] | [S3][32119]  
[S3L][32120]  
[V3][32121]  
[V3s][32122] | [A64][32123]  
[H64][32124] | [H5][32125] | [H6][32126] | [A50][32127] | [V831][32128]  
[V833][32129] | [H313][32130]  
[H616][32131]  
[H618][32132]  
[H700][32133]  
[T507][32134] | [A100][32135]  
[A133][32136] | [R329][32137] | [D1][32138]  
[D1s][32139]  
[T113][32140] | [A523][32141]  
[A527][32142]  
[MR527][32143]  
[T527][32144]  
[H728][32145]  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
ADC  | GPADC  | N/A  | 4.12  | 4.12  | 4.12  | 4.12  | 4.12  | [WIP][32146] | NO  | [WIP][32146] | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | 6.11  | ?  | [WIP][32146] | 6.6  | NO   
[LRADC][32147] | 6.2  | 4.0  | 4.0  | 4.0  | 4.9  | 4.0  | ?  | ?  | 4.0  | 4.0  | 4.2  | 5.2  | ?  | 4.13  | 5.3  | ?  | N/A  | ?  | ?  | 6.11  | ?  | 5.19  | 5.19  | NO   
Thermal  | NO  | 3.16  | 3.14  | 3.14  | 4.9  | 3.16  | 5.7  | [WIP][32146] | [WIP][32146] | ?  | 4.12  | 5.6  | 5.6  | N/A  | 5.6  | 5.6  | 5.6  | ?  | ?  | 6.9  | 5.10  | ?  | 6.8  | [WIP][32146]  
Touch  | NO  | 3.16  | 3.14  | 3.14  | 4.9  | 3.16  | [WIP][32146] | NO  | 4.0  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | N/A  | ?  | NO  | N/A   
Audio  | AC97  | N/A  | NO  | N/A  | N/A  | N/A  | NO  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | N/A  | ?  | N/A  | N/A   
[Analog Codec][32148] | 6.14  | 4.4  | 4.4  | 4.4  | 4.9  | 4.4  | NO  | N/A  | 4.10  | 4.10  | 4.11  | N/A  | 4.10  | 4.13  | 5.0  | 4.12  | NO  | ?  | ?  | [WIP][32146] | ?  | WIP  | [WIP][32146] | NO   
Audio Hub  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | N/A  | NO  | N/A  | N/A  | N/A  | N/A   
DMIC  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 6.1  | ?  | N/A  | ?  | ?  | ?  | ?  | NO   
I2S  | NO  | 4.8  | ?  | N/A  | 4.9  | 4.8  | NO  | NO  | 4.13  | ?  | 4.11  | 4.16  | 4.14  | [WIP][32146] | 4.17  | NO  | 5.11  | ?  | ?  | NO  | ?  | 5.18  | 5.18  | [WIP][32146]  
[SPDIF][32149] | NO  | 4.7  | N/A  | N/A  | 4.9  | 4.7  | ?  | ?  | 4.9  | N/A  | N/A  | 4.13  | 4.11  | N/A  | 4.17  | 4.12  | 5.4  | ?  | ?  | 6.9  | ?  | ?  | WIP  | [WIP][32146]  
[Camera][32150] | BT656  | NO  | 5.6  | ?  | ?  | ?  | 5.4  | 5.6  | ?  | 5.0  | ?  | ?  | 5.3  | 5.0  | 5.0  | 5.1  | 5.0  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO   
ISP  | N/A  | NO  | N/A  | N/A  | N/A  | NO  | N/A  | NO  | NO  | N/A  | N/A  | NO  | N/A  | [WIP][32151] | N/A  | N/A  | N/A  | ?  | ?  | N/A  | ?  | ?  | ?  | ?   
MIPI CSI-2  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | [WIP][32151] | N/A  | N/A  | [WIP][32151] | N/A  | 5.19  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | ?  | ?  | ?  | NO   
Parallel  | NO  | 5.6  | ?  | ?  | ?  | 5.4  | 5.6  | ?  | 5.0  | ?  | ?  | 5.3  | 5.0  | 5.0  | 5.1  | 5.0  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO   
CAN bus  | ?  | 4.4  | N/A  | N/A  | N/A  | 4.4  | 5.17  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | N/A  | ?  | 6.6  | NO   
Clocks  | 5.0  | 3.10  | 3.11  | 3.10  | 4.9  | 3.12  | 4.14  | 3.19  | 3.12  | 3.17  | 4.2  | 4.13  | 4.8  | 4.11  | 4.10  | 4.12  | 4.17  | ?  | [WIP][32152] | 5.12  | 5.10  | WIP  | 5.17  | 6.15   
CPUFreq (DVFS)  | NO  | 4.0  | 4.0  | 4.0  | NO  | 4.0  | 6.0  | NO  | 4.2  | NO  | 4.11  | 4.17  | 4.18  | NO  | 5.6  | 5.9  | 5.8  | ?  | ?  | 6.10  | 6.15  | ?  | [WIP][32146] | WIP   
CPUIdle  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | Crust  | NO  | Crust  | Crust  | Crust  | NO  | NO  | NO  | NO  | NO  | SBI  | NO   
[Crypto][32153] | N/A  | 4.3  | 4.13  | 4.13  | 4.13  | 4.3  | 5.5  | 5.5  | 4.3  | ?  | 4.3  | 5.5  | 5.5  | 5.10  | 5.5  | 5.5  | 5.5  | ?  | ?  | 6.11  | NO  | ?  | 6.3  | NO   
[Display (DRM)][32154] | CVBS  | NO  | ?  | 4.9 ?  | 4.7  | 4.9  | ?  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][32146] | N/A  | N/A  | [WIP][32146] | NO  | ?  | ?  | ?  | ?  | ?  | NO  | ?   
G2D  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO  | NO   
HDMI Audio  | N/A  | [WIP][32146] | NO  | N/A  | N/A  | [WIP][32146] | NO  | NO  | [WIP][32146] | N/A  | N/A  | NO  | [WIP][32151] | N/A  | [WIP][32151] | [WIP][32151] | [WIP][32151] | ?  | ?  | ?  | ?  | ?  | NO  | NO   
HDMI CEC  | N/A  | 4.15  | 4.14  | N/A  | N/A  | 4.15  | 4.19  | NO  | 4.15  | N/A  | N/A  | 4.17  | 4.17  | N/A  | 4.20  | 4.17  | 5.2  | ?  | ?  | ?  | ?  | ?  | NO  | NO   
HDMI Video  | N/A  | 4.15  | 4.13  | N/A  | N/A  | 4.15  | 4.19  | NO  | 4.15  | N/A  | N/A  | 4.17  | 4.17  | N/A  | 4.20  | 4.17  | 5.0  | ?  | ?  | ?  | ?  | ?  | WIP  | NO   
LVDS  | N/A  | ?  | N/A  | N/A  | N/A  | 5.7  | ?  | ?  | ?  | ?  | ?  | 4.16  | N/A  | N/A  | ?  | N/A  | N/A  | ?  | ?  | [WIP][32146] | ?  | ?  | [WIP][32146] | NO   
MIPI DSI  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][32151] | NO  | NO  | ?  | 4.18  | NO  | N/A  | N/A  | 5.6  | N/A  | N/A  | ?  | ?  | N/A  | 6.2  | ?  | 6.2  | NO   
RGB  | NO  | 4.15  | ?  | 4.7  | 4.9  | 4.15  | NO  | 4.17  | 4.10  | 5.1  | 4.9  | 4.16  | N/A  | 4.13  | 5.3  | N/A  | NO  | ?  | ?  | [WIP][32146] | ?  | ?  | 6.0  | NO   
VGA  | N/A  | NO  | N/A  | N/A  | N/A  | NO  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | N/A  | N/A  | ?  | N/A  | N/A   
Display (SimpleFB)  | NO  | 3.19  | 3.19  | 4.0  | 4.9  | 3.19  | NO  | NO  | 3.19  | 3.19  | 3.19  | NO  | 4.16  | 5.10  | 4.17  | 4.16  | NO  | ?  | ?  | ?  | ?  | ?  | NO  | NO   
DMA  | 6.14  | 4.3  | 4.3  | 4.3  | 4.9  | 4.3  | 5.10  | ?  | 3.17  | 3.18  | 4.2  | 4.9  | 4.2  | 4.13  | 4.15  | 4.12  | 5.3  | ?  | ?  | 6.9  | 6.1  | ?  | 5.19  | [WIP][32146]  
[Ethernet][32155] | [EMAC][32156] | N/A  | 3.11  | 3.11  | N/A  | N/A  | 3.11  | [WIP][32146] | 5.1  | N/A  | N/A  | N/A  | 4.16  | 4.15  | 4.13  | 4.15  | 4.15  | 5.0  | ?  | ?  | ?  | 6.17  | ?  | 5.15  | 6.16   
[GMAC][32157] | N/A  | N/A  | N/A  | N/A  | N/A  | 3.15  | 4.18  | 5.1  | 3.17  | N/A  | N/A  | 4.16  | 4.15  | 4.13  | 4.15  | 4.15  | 5.0  | ?  | N/A  | 6.0  | N/A  | ?  | N/A  | [WIP][32146]  
GPU (3D)  | [Mali][32158] | N/A  | 5.2  | ?  | ?  | ?  | 5.2  | 5.10  | N/A  | N/A  | ?  | ?  | N/A  | 5.2  | N/A  | 5.2  | 5.2  | 5.5  | ?  | ?  | 6.15  | N/A  | ?  | N/A  | 6.17   
[PowerVR][32159] | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | NO  | N/A  | N/A  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | N/A  | N/A   
HW Spinlocks  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | ?  | ?  | ?  | [WIP][32146] | [WIP][32146] | ?  | [WIP][32146] | NO  | NO  | ?  | ?  | N/A  | ?  | ?  | NO  | NO   
[I2C][32160] | 6.2  | 3.11  | 3.12  | 3.11  | 4.9  | 3.13  | 4.15  | 3.19  | 3.15  | 3.18  | 4.2  | 4.16  | 4.9  | 4.11  | 4.10  | 4.12  | 4.19  | ?  | ?  | 6.0  | 5.10  | ?  | 6.0  | 6.15   
IOMMU  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 5.8  | ?  | ?  | 6.11  | ?  | ?  | WIP  | NO   
[IR][32161] | [IR RX][32161] | 6.2  | 3.17  | 4.0  | 4.0  | 4.9  | 3.17  | 5.10  | 4.5  | 4.0  | N/A  | N/A  | 4.20  | 4.6  | N/A  | 5.4  | 4.12  | 5.4  | ?  | ?  | 6.0  | ?  | ?  | NO  | NO   
IR TX  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | N/A  | ?  | ?  | NO  | NO   
Keypad  | N/A  | WIP  | N/A  | N/A  | N/A  | WIP  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A   
LDOs  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | WIP  | WIP  | ?   
LEDC  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 6.8  | 6.8  | 6.8  | NO   
MBUS  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO  | NO  | ?  | ?  | ?  | NO  | 5.17  | 5.17  | NO  | NO  | NO  | NO  | NO  | NO  | NO  | ?   
MsgBox  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | ?  | ?  | ?  | 5.8  | 5.8  | N/A  | 5.8  | 5.8  | 5.8  | ?  | ?  | N/A  | ?  | ?  | WIP  | NO   
PCIe  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][32151] [[3]][32162] | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO   
Pinctrl  | 5.0  | 3.9  | 3.9  | 3.9  | 4.9  | 3.12  | 4.14  | 3.19  | 3.12  | 3.18  | 4.2  | 4.4  | 4.5  | 4.11  | 4.6  | 4.12  | 4.17  | ?  | [WIP][32152] | 5.12  | 5.10  | WIP  | 6.0  | 6.15   
[PMU][32163] (perf, DT only)  | N/A  | 5.1  | ?  | ?  | ?  | 3.16  | 5.6  | ?  | 3.16  | ?  | ?  | ?  | 5.6  | ?  | 5.5  | 5.6  | 5.6  | ?  | ?  | 6.0  | 6.13  | ?  | [WIP][32146] | 6.16   
[PWM][32164] | 6.2  | 4.0  | 4.4  | 4.4  | 4.9  | 4.0  | [WIP][32146] | NO  | NO  | 4.4  | 4.4  | 4.16  | 4.9  | 4.12  | 4.19  | 4.12  | 5.6  | ?  | ?  | WIP  | WIP  | [WIP][32146] | [WIP][32146] | NO   
Remoteproc  | AIPU  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | ?  | NO  | N/A  | NO   
DSP  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | ?  | WIP  | WIP  | NO   
[RSB][32165] | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 4.3  | N/A  | 4.4  | 4.4  | 4.14  | ?  | N/A  | 4.13  | ?  | 5.12  | ?  | ?  | 6.0  | ?  | ?  | N/A  | N/A   
[RTC][32166] | N/A  | 3.14  | N/A  | N/A  | N/A  | 3.14  | 5.0  | N/A  | 3.18  | 3.18  | 4.2  | N/A  | 4.5  | 4.11  | 4.10  | 4.12  | 5.4  | ?  | [WIP][32152] | 6.0  | WIP  | WIP  | 6.0  | 6.15   
SID (eFuse)  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | 6.7  | 5.10  | ?  | 5.18  | 6.17   
SMP  | N/A  | N/A  | N/A  | N/A  | N/A  | PSCI  | PSCI  | 4.17  | PSCI  | PSCI  | PSCI  | 4.18  | PSCI  | N/A  | PSCI  | PSCI  | PSCI  | ?  | ?  | PSCI  | PSCI  | PSCI  | N/A  | PSCI   
[SPI][32167] | 5.19  | 3.16  | 3.15  | 3.15  | 4.9  | 3.15  | 5.6  | ?  | 3.15  | ?  | ?  | ?  | 4.10  | 4.13  | 4.15  | 4.12  | 5.7  | ?  | [WIP][32152] | 6.0  | WIP  | [WIP][32146] | 6.5  | NO   
[SRAM][32168] | 5.0  | 4.2  | 4.2  | 4.2  | 4.2  | 4.2  | 5.10  | N/A  | NO  | 4.19  | 4.19  | N/A  | 4.19  | 5.10  | 4.19  | 5.0  | 5.1  | ?  | ?  | 6.0  | 6.14  | ?  | 6.1  | [WIP][32146]  
Storage  | EMCE  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][32151] | ?  | ?  | N/A  | N/A  | ?  | N/A  | N/A   
[NAND][32169] | N/A  | ?  | ?  | 4.12 [[4]][32170] | 4.9 [[4]][32170] | ?  | ?  | ?  | ?  | 4.9 [[4]][32170] | 4.9 [[4]][32170] | ?  | ?  | N/A  | ?  | ?  | [WIP][32146] | ?  | ?  | [WIP][32146] | NO  | ?  | NO  | NO   
[SATA][32171] | N/A  | 3.15  | N/A  | N/A  | N/A  | 3.15  | 4.20  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A   
[SD/MMC][32172] | 5.19  | 3.16  | 3.16  | 3.16  | 4.9  | 3.16  | 4.14  | 4.0  | 3.16  | 3.18  | 4.2  | 4.14  | 4.5  | 4.11  | 4.11  | 4.12  | 4.19  | ?  | [WIP][32152] | 6.0  | 5.12  | WIP  | 5.18  | 6.15   
Timer  | Arch Timer  | N/A  | N/A  | N/A  | N/A  | N/A  | 3.15  | 4.15  | 4.2  | 4.0  | 4.2  | 4.2  | 4.6  | 4.5  | 4.11  | WIP  | 4.12  | 4.17  | ?  | ?  | 6.0  | 5.10  | ?  | WIP  | 6.16   
HSTIMER  | ?  | ?  | 4.2  | 4.2  | 4.2  | 3.14  | ?  | ?  | 4.2  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | ?  | NO   
TIMER  | 5.0  | 3.15  | 4.2  | 4.2  | 4.2  | 3.15  | 5.14  | 3.19  | 3.15  | 5.4  | 5.4  | 5.4  | 5.4  | 5.4  | 5.14  | 5.4  | 5.14  | ?  | ?  | ?  | ?  | ?  | 6.0  | ?   
[USB][32173] | [USB][32173] | 6.3  | 3.15  | 3.15  | 3.15  | 4.9  | 3.15  | 4.15  | 4.2  | 3.16  | 4.3  | 4.3  | 4.14  | 4.8  | 4.11  | 4.11  | 4.12  | 5.0  | ?  | ?  | 6.1.3  | 6.13  | ?  | 5.18  | 6.15   
[USB OTG][32174] | 6.3  | 4.3  | 4.3  | 4.3  | 4.9  | 4.3  | [WIP][32146] | NO  | 4.3  | 4.8  | 4.8  | 5.2  | 4.12  | 4.11  | 4.11  | 4.12  | 5.0  | ?  | ?  | 6.1.3  | 6.13  | ?  | 5.18  | 6.15   
USB3.0  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | NO  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 5.5  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | [WIP][32146]  
[VE][32175] | NO  | 5.1  | ?  | 4.20  | ?  | 4.20  | 5.10  | NO  | ?  | ?  | 4.20  | NO  | 4.20  | [WIP][32151] | 5.0  | 5.0  | 5.2  | ?  | ?  | ?  | ?  | ?  | 5.17  | NO   
Watchdog  | 5.19  | 3.12  | 3.12  | 3.12  | 4.9  | 3.12  | 4.15  | 3.19  | 3.18  | 3.18  | 4.2  | 4.6  | 4.5  | 4.11  | 4.17  | 4.12  | 5.3  | ?  | [WIP][32152] | 6.0  | 6.13  | 5.16  | 5.16  | 6.15   
Model  | [F1C-  
100s  
200s][32099] | [A10][32100] | [A10s][32101] | [A13][32102]  
[R8][32103] | [GR8][32104] | [A20][32105]  
[T2][32106] | [R40][32107]  
[V40][32108]  
[T3][32109]  
[A40i][32110] | [A80][32111] | [A31][32112] | [A23][32113] | [A33][32114]  
[R16][32115] | [A83T][32116] | [H3][32117]  
[H2+][32118] | [S3][32119]  
[S3L][32120]  
[V3][32121]  
[V3s][32122] | [A64][32123]  
[H64][32124] | [H5][32125] | [H6][32126] | [A50][32127] | [V831][32128]  
[V833][32129] | [H313][32130]  
[H616][32131]  
[H618][32132]  
[H700][32133]  
[T507][32134] | [A100][32135]  
[A133][32136] | [R329][32137] | [D1][32138]  
[D1s][32139]  
[T113][32140] | [A523][32141]  
[A527][32142]  
[MR527][32143]  
[T527][32144]  
[H728][32145]  
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
  * [A733][32176] **Andre Przywara** [pinctrl: sunxi: Allwinner A733 support][32177]

  * [V853][32178] / [V851s][32179] / [V851s3][32180] Andras Szemzo [Support for Allwinner V853 SoC][32181]

  * [R329][32137] Clocks & Pinctrl / RTC / MMC - Icenowy Zheng [Initial support for Allwinner R329][32182]

  * [V831][32128] / [V833][32129] Clocks & Pinctrl / RTC / MMC / Watchdog / SPI - Icenowy Zheng [Support for Allwinner V831 SoC][32183]

  * [AR100][32184] firmware (WiP: Samuel Holland) [ARISC firmware for sunxi SoCs ][32185]

  * [A13][32102] PSCI Suspend / Resume / CPUIdle (WiP: Antoine Tenart) [patch-v1][32186]

### Major drivers
  * [V3s][32122] ISP (Image Signal Processor) Paul Kocialkowski [initial-allwinner-v3-isp-support-in-mainline-linux][32187]

  * [H6][32126] Hypervisor for PCIe [A try on utilizing H6 PCIe with "Virtualization"][32188]

  * [A64][32123] / [H3][32117] / [H5][32125] / [H6][32126] HDMI Audio - Clément Péron / Marcus Cooper / Jernej Škrabec [Add Allwinner H3/H5/A64 HDMI audio][32189]

  * [R40][32107] MIPI-DSI WIP Jagan Teki [drm/sun4i: Allwinner R40 MIPI-DSI support v3][32190]

  * [AC100][32191] Audio codec WiP Ondrej Jirman [digital part][32192] [analog part][32193]

  * [V3s][32122] SRAM & Video Decoding Engine (Cedrus) WiP Martin Cerveny [Enable video decoder][32194] ([testing with attached LCD][32195])
  * [H6][32126] VP9 decoder (Hantro G2) WiP jernej [branch][32196]

### Minor drivers
  * [A523][32141] / [H728][32145] / [A527][32142] / [T527][32144] Chen-Yu Tsai [allwinner: a523: Enable I2S and SPDIF TX][32197]
  * [H6][32126], [H313][32130],[H616][32131],[H618][32132],[H700][32133],[T507][32134] Richard Genoud [Introduce Allwinner H6/H616 NAND controller support][32198]
  * [A523][32141] / [H728][32145] / [A527][32142] / [T527][32144] Mikhail Kalashnikov [arm64: allwinner: a523: add USB3.0 support][32199]
  * [H313][32130],[H616][32131],[H618][32132],[H700][32133],[T507][32134] Ryan Walklin [allwinner: h616: add LCD timing controller and display engine support][32200]
  * [A523][32141] / [H728][32145] / [A527][32142] / [T527][32144] Mikhail Kalashnikov [Add support for A523 Thermal system][32201]
  * [D1s][32139] / [T113][32140] Kuba Szczodrzyński [drm/sun4i: Support LVDS on D1s/T113 combo D-PHY][32202]
  * [A64][32123] Ondrej Jirman [A64 audio jack detection][32203]
  * [D1][32138] Brandon Cheo Fusi [cpufreq support for the D1][32204]
  * [D1][32138] Inochi Amaoto [riscv: dts: allwinner: d1: Add PMU event node][32205]
  * [D1][32138] / [T113][32140] Maksim Kiselev [ASoC: sunxi: Add support for D1/T113s internal audio codec][32206]
  * [H6][32126] ethernet on opi3/opi1+ LABBE Corentin [arm64: add ethernet to orange pi 3][32207]
  * [D1][32138] / [R329][32137] Aleksandr Shubin [Add support for Allwinner PWM on D1/T113s/R329 SoCs][32208]
  * [D1][32138] IOMMU Samuel Holland [iommu/sun50i: Allwinner D1 support][32209]
  * [D1][32138] System LDOs Samuel Holland [regulator: Add support for Allwinner D1 system LDOs][32210]
  * [D1][32138] Video Engine Samuel Holland [Allwinner D1 video engine support][32211]
  * [R40][32107]/[T3][32109]/[A40i][32110] RTP/LRADC Evgeny Boger [[1]][32212]
  * [R40][32107]/[T3][32109]/[A40i][32110] EMAC Evgeny Boger [support for two Ethernet ports on Allwinner R40][32213]
  * [R40][32107]/[T3][32109]/[A40i][32110] USB OTG qianfan Zhao [ARM: sun8i-r40: Enable usb otg support][32214]
  * [V3][32121] I2S Tobias Schramm [Add missing peripherals to Allwinner V3s/V3 device trees][32215]
  * [H3][32117] / [H5][32125] CVBS WIP Jernej Skrabec [Add H3/H5 TVE support][32216]
  * [A64][32123] hwspinlock WIP Nikolay Borisov [Add support for hwspinlock on A64 SoC][32217]
  * [A83T][32116] / [A64][32123] / [H3][32117] hwspinlock WIP Corentin Labbe (montjoie) [RFC,1/3][32218][RFC,2/3][32219][RFC,3/3][32220]
  * [A10][32100] / [A20][32105] / [A31][32112] HDMI Audio WIP Stefan Mavrodiev [Add support for sun4i HDMI audio][32221]
  * [A80][32111] Thermal sensor WIP Philipp Rossak (embed-3d): <https://github.com/embed-3d/linux/branches/all>
  * [R40][32107] PWM (WIP Hao Zhang [patch-v2][32222])
  * [A20][32105] Keypad (WiP: Yassin Jaffer (ddc) [patch][32223])
  * sun8i-ce/sun8i-ss RSA/ECC WIP Corentin LABBE (no public patch yet)
  * EMCE WIP Corentin LABBE (no public patch yet) / Mripard <https://git.kernel.org/pub/scm/linux/kernel/git/mripard/linux.git/log/?h=sunxi/h6-emmc-inline-encryption> BUT proably not usable <https://lore.kernel.org/linux-mmc/20210317171554.a4vgihqfjq2xa5cb@gilmour/>

### Drivers that can still be improved/added
Nobody works on these features. If you're interested, you can pick one of these add your name to them and move them to one of the sections above, to indicate you're working on the driver/feature. 
  * [A31][32112]/[A31s][32224] PWM support ([patch-v4][32225] abandoned by Siarhei Volkau)
  * sunxi-musb driver lacks DMA support (with current driver, USB gadgets are limited to PIO, limiting speed to 10MiB/s and causing large CPU)
  * DE2 driver has buggy layer support, see [[2]][32226]
  * DE1/DE2/DE3 writeback support
  * H616 (and later) UHS-I SD card support (pinctrl device contains voltage switch for PortF)

## Planned for next
## Merged into 6.17(-rc1)
  * [A523][32141]
    * Mali GPU support
    * power domain controller support
    * SID support
  * [A100/A133][32136]
    * EMAC Ethernet support

New devices supported: 
  * [A523][32141]: [Xunlong Orange Pi 4A][32227]

## Merged into 6.16
  * [A523][32141]
    * Basic DT support
    * First Ethernet port support
  * [H616][32131]
    * Mali GPU support

New devices supported 
  * [A133][32136]: [Liontron H-A133L][32228]
  * [H616][32131]: YuzukiHD Chameleon
  * [A523][32141]: [Radxa Cubie A5E][32229]
  * [A523][32141]: [X96QPro+][32230]
  * [A523][32141]: [YuzukiHD Avaota A1][32231]

## Merged into 6.15
  * [A100/A133][32136]
    * enable DVFS support
  * [A523][32141]
    * main and PRCM clock support
    * pinctrl/GPIO support
    * watchdog support
    * NMI support

New devices supported 
  * [V3s][32122]: [NetCube Systems Kumquat][32232]

## Merged into 6.14
  * [A100/A133][32136]
    * syscon support
  * [F1C100s][32099]
    * DMA support
    * audio codec support

## Merged into 6.13
  * [A100/A133][32136]
    * PMU support (for perf tool)
    * watchdog support
    * USB support
    * MMC support
  * [H616][32131]
    * audio codec support

New devices supported 
  * [A33][32114]: RerVision A33-Vstar board

## Merged into 6.12
New devices supported 
  * [H616][32131]: Anbernic RG35XX-SP

## Merged into 6.11
  * [H616][32131]
    * LRADC support
    * IOMMU support
    * crypto engine

## Merged into 6.10
  * [D1][32138]/[T113-s3][32140]
    * LDO driver
  * [H616][32131]
    * enable DVFS support
  * sun4i-i2s: Support 32-bit audio formats

New devices supported 
  * [A13][32102]: PocketBook 614 Plus
  * [H616][32131]: [Tanix TX1][32233]
  * [H616][32131]: [Anbernic RG35XX Plus][32234]
  * [H616][32131]: [Anbernic RG35XX H][32235]
  * [H616][32131]: Anbernic RG35XX 2024

## Merged into 6.9
  * [H616][32131]
    * SPDIF
    * DMA
    * Thermal

New Devices supported 
  * [H616][32131]: Sipeed LonganPi 3H
  * [A64][32123]: [Remix Mini PC][32236]

## Merged into 6.8
  * [D1][32138]/[T113-s3][32140]
    * Thermal

New Devices supported 
  * [H616][32131]: [OrangePi Zero 2W][32237]
  * [H616][32131]: [Transpeed 8K618-T][32238]

## Merged into 6.7
  * [H616][32131]
    * SID

New Devices supported 
  * [H616][32131]: Bigtreetech CB1 Manta
  * [H616][32131]: Bigtreetech Pi
  * [V3s][32122]: Anbernic RG-Nano

## Merged into 6.6 (LTS)
  * [D1][32138]/[T113-s3][32140]
    * CAN
    * GPADC

New Devices supported 
  * [H616][32131]: [OrangePi Zero 3][32239]

## Merged into 6.5
  * [D1][32138]/[T113-s3][32140]
    * SPI

## Merged into 6.4
  * [F1C100s][32099]
    * Enable [LicheePi Nano][32240] USB support

New Devices supported 
  * [F1C100s][32099]
    * Popcorn Computer PopStick
    * [Lctech Pi F1C200s][32241]

  * [T113-s3][32140]
    * [MangoPi MQ-R-T113][32242]

## Merged into 6.3
  * [D1][32138]
    * Base DT and Kconfig
    * Crypto
    * Power Domain

  * [T113-s3][32140]
    * R528/T113 Clocks support

  * [F1C100s][32099]
    * USB PHY support
    * USB MUSB support

## Merged into 6.2
  * [A100][32135]
    * MIPI-DSI
  * [D1][32138]
    * MIPI-DSI

## Merged into 6.1 (LTS)
  * [A100][32135]
    * DMA
  * [D1][32138]
    * SRAM
  * [H6][32126]
    * DMIC
    * GPU Devfreq

## Merged into 6.0
  * [D1][32138]
    * RGB LCD
    * I2C
    * Pinctrl
    * RTC
  * [H616][32131] [Orange Pi Zero 2][32243]
  * [H616][32131] [X96 Mate][32244]
  * [R40][32107]/[T3][32109]/[A40i][32110]
    * CPUFreq (DVFS)

## Merged into 5.19
  * [D1][32138]
    * DMA
    * LRADC
  * [F1C100s][32099]
    * SD/MMC
    * SPI
    * Watchdog
  * [V3s][32122]
    * [MIPI-CSI2][32245]

## Merged into 5.18
  * [D1][32138]
    * I2S
    * MMC
    * SID
    * USB

## Merged into 5.17
  * [A64][32123]/[H5][32125]
    * DRAM frequency scaling (DEVFREQ)
  * [D1][32138]
    * Clocks
    * PLIC
  * [R40][32107]/[T3][32109]/[A40i][32110]
    * CAN ([series][32246])

## Merged into 5.16
  * [R329][32137]/[D1][32138]
    * Watchdog

## Merged into 5.15 (LTS)
## Merged into 5.14
  * [H616][32131]
    * PMIC - AXP305

New Devices Supported 
  * [H616][32131]
    * [Tanix TX6s][32247]
    * [X96 Mate][32244]
    * [Xunlong Orange Pi Zero2][32248]

## Merged into 5.13
New Devices Supported 
  * [A10][32100]
    * Topwise A721 Tablet

## Merged into 5.12
  * [H616][32131]
    * Clocks
    * Pinctrl
    * MMC
  * [H6][32126]
    * RSB
  * [A100][32135]
    * MMC

## Merged into 5.11
  * [H6][32126]
    * [I2S][32249]
  * multiple SoCs 
    * [Cedrus][32250] VP8 decoding

New Devices Supported 
  * [H3][32117]
    * [FriendlyArm NanoPi R1][32251]
    * [FriendlyArm ZeroPi][32252]
  * [S3][32119]
    * [Elimo Impetus][32253]
    * [Elimo Initium][32254]

## Merged into 5.10 (LTS)
  * [A100][32135]
    * Clocks
    * Pinctrl
    * [I2C][32160]
    * Thermal (THS)

  * [R40][32107]
    * DMA
    * GPU [Mali][32158]
    * [IR][32161]
    * [SRAM][32168]
    * [Video_Engine][32175] | [Sunxi-Cedrus][32255]

  * [V3s][32122]
    * Crypto
    * Ethernet
    * SimpleFB
    * [SRAM][32168]

  * sun8i-ce/sun8i-ss 
    * support for PRNG
    * support for hashs
    * support for TRNG ([H6][32126] only)

New Devices Supported 
  * [A100][32135]
    * [Perf1 board][32256]
  * [S3l][32257]
    * [PineCube][32258]

## Merged into 5.9
  * [H5][32125]
    * DVFS

New Devices Supported 
  * A64 
    * PinePhone v1.2

## Merged into 5.8
  * [H6][32126]
    * DVFS
    * IOMMU

  * [A64][32123] / [A83T][32116] / [H3][32117] / [H5][32125] / [H6][32126]
    * Message Box

New Devices Supported 
  * A20 
    * [OLinuXino Lime (A20)][32259] eMMC

## Merged into 5.7
  * [A20][32105]
    * LVDS

  * [A83T][32116] and [A64][32123]
    * Rotate driver

  * [H6][32126]
    * [SPI][32167]

  * [R40][32107]
    * Thermal

New Devices Supported 
  * [A13][32102]
    * [PocketBook Touch Lux 3][32260]
  * [A64][32123]
    * [PineTab][32261]
    * [PinePhone][32262] v1.0 & v1.1
  * [A20][32105]
    * Linutronix Testbox v2

## Merged into 5.6
  * [A10][32100]
    * CSI (BT656 and Parallel)

  * [A64][32123]
    * MIPI DSI
    * DVFS

  * [A64][32123] / [A83T][32116] / [H3][32117] / [H5][32125] / [H6][32126]
    * Thermal

  * [H6][32126]
    * PWM

  * [H3][32117] / [H5][32125] / [H6][32126] / [R40][32107]
    * PMU

  * [R40][32107]
    * CSI (BT656 and Parallel)
    * [SPI][32167]

New Devices Supported 
  * [H5][32125]
    * ALL-H3-IT H5 board
    * ALL-H5-CC H5 board
  * [H6][32126]
    * [PineH64][32263] Model B

## Merged into 5.5
  * [H3][32117]
    * Deinterlace driver

  * [H6][32126]
    * Crypto
    * GPU(3D) Mali
    * USB3 PHY (for boards not needing vbus switching)

  * [A64][32123] / [A80][32111] / [A83T][32116] / [H3][32117] / [H5][32125] / [R40][32107]
    * Crypto

  * multiple SoCs 
    * [Cedrus][32250] HEVC/H.265

  * [Broadcom-based (AMPAK modules) Bluetooth][32264] support on 
    * Emlid Neutis

New Devices Supported 
  * [H3][32117]
    * [FriendlyARM_NanoPi_Duo2][32265]

## Merged into 5.4 (LTS)
  * [A20][32105]
    * CSI (BT656 and Parallel)
  * [A64][32123]
    * IR
  * [H6][32126]
    * IR
    * RTC
    * SPDIF

New Devices Supported 
  * [A64][32123]
    * [Olimex A64-OLinuXino][32266] eMMC
  * [H6][32126]
    * [Tanix TX6][32267]
  * [S3][32119]
    * [Lichee Zero Plus][32268]

## Merged into 5.3
  * [A64][32123]
    * LRADC
    * RGB LCD
  * [A83T][32116]
    * CSI (BT656 and Parallel)
  * [H6][32126]
    * DMA
    * Watchdog
  * multiple SoCs 
    * [Cedrus][32250] h264

## Merged into 5.2
  * [A83T][32116]
    * LRADC
    * USB OTG

  * [H6][32126]
    * [Cedrus][32250]

  * multiple SoCs 
    * [Lima][32269]
    * [Panfrost][32269]

  * [Broadcom-based (AMPAK modules) Bluetooth][32264] support on 
    * Banana-Pi-M2-Zero

New Devices Supported 
  * [H6][32126]
    * [Beelink GS1][32270]
    * [Xunlong Orange Pi 3][32271]

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
    * [ARM Architectural Timer errata workaround][32272]
    * PMU
    * CSI (BT656 and Parallel)

  * A80 
    * GMAC support

  * CSI in general 
    * RGR565 support
    * JPEG pass-through support

  * [Broadcom-based (AMPAK modules) Bluetooth][32264] support on 
    * [Banana Pi M2+][32273]
    * [Banana Pi M2 Ultra][32274]

  * [LCD][32275] enabled on [A13][32102] [Q8][32276] tablets

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
    * initial T3 support[[5]][32277]

  * V3s 
    * CSI (BT656 and Parallel) Support

  * [Broadcom-based (AMPAK modules) Bluetooth][32264] support on 
    * [ Banana Pi M2 Magic][32278]
    * [Banana Pi M3][32279]
    * [Banana Pi M64][32280]
    * [Cubietruck][32281]
    * [Cubietruck Plus][32282]

New Devices Supported 
  * [Xunlong Orange Pi Lite 2][32283]
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
  * [Pine64][32284] LTS
  * [Xunlong Orange Pi One Plus][32285]
  * [Xunlong Orange Pi Zero Plus 2][32286] (H3 variant)
  * [Sinovoip Banana Pi M2+][32287] (H5 variant)

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
  * SPI flash node for [Orange Pi PC 2][32288] and [ Pine64 SoPINE][32289]
  * Use lid switch as wake-up source for A64 based laptops
  * LEDs added for [PineH64][32263]

New Devices 
  * [Pine Pinebook][32290]
  * Amarula A64-Relic

## Changes merged up to 4.18
Changes up to 4.18 can be found on [Linux mainlining history][32291] page. 
# References
  1. [↑][32292] <http://www.elinux.org/images/a/ad/Arm-soc-checklist.pdf>
  2. [↑][32293] [Your New ARM SoC Linux Support Check-List – ELCE 2012][32294]
  3. [↑][32295] Allwinner H6 has a quirky PCIe controller that doesn't map the PCIe address space properly to CPU, and accessing the PCIe config space, IO space or memory space needs to be wrapped. As Linux doesn't wrap PCIe memory space access, it's not possible to do a proper PCIe controller without using an hypervisor. The BSP kernel modifies the driver to wrap the access, so it's also not generic, and only devices with modified driver will work. <https://forum.armbian.com/topic/13529-a-try-on-utilizing-h6-pcie-with-virtualization/>
  4. ↑ [4.0][32296] [4.1][32297] [4.2][32298] [4.3][32299] While the NAND controller itself is supported, the NAND technology found on the vast majority of boards isn't. See [this page][32300]
  5. [↑][32301] <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=b7badd1d7aa61087010803affa19bb83fb5a0af1>

# See also
  * [Mainline Kernel Howto][32096]
  * [Possible setups for hacking on mainline][32302]
  * [Linux Kernel][32303]
    * [Toolchain][32304]

# External Links
  * [kernel.org][32305] \- Official website for the Linux Kernel 
    * <http://github.com/torvalds/linux> \- Linus Torvalds' GitHub account with the upstream Linux kernel
  * [Linux Kernel documentation index][32306]
  * [Linux Kernel man pages][32307]
  * [Kernel Newbies Site - Excellent source of information for people new to kernel][32308]
  * [Linus' kernel tree for 2.6][32309]
  * [Kernel bugzilla][32310] \- [Regressions for each of recent versions][32311]
  * [Linux-libre project - Maintains and distributes fully free kernel][32312]
  * [LinGrok, Linux kernel source code cross-reference][32313]
  * [Bootlin LXR (Linux Cross Reference)][32314]
  * [linux-arm-kernel - Mailing list archive][32315]

### How to upstream
  * [Your new ARM SoC Linux support check-list! by Thomas Petazzoni of Bootlin][32316]
  * [Linux Kernel Upstreaming How-To (CNXSoft - Embedded Software Development)][32317]
    * [Matt Porter's YouTube video talk on “Upstreaming 101" (LCA14-111)][32318]
      * [Matt Porter's presentation slides for “Upstreaming 101" (LCA14-111)][32319]
    * [Matt Porter's YouTube video talk on “Upstreaming 201" (LCA14-112)][32320]
      * [Matt Porter's presentation slides for “Upstreaming 201" (LCA14-112)][32321]
  * [How to Write and Submit a Linux Kernel Patch (CNXSoft - Embedded Software Development)][32322]
    * [YouTube Video- Write and Submit your first Linux kernel Patch][32323]
    * [Greg Kroah-­Hartman Kernel Tutorial Write and Submit your first Linux Kernel Patch][32324]
  * [Linaro resources page from LCA (Linaro Connect Asia) 2014][32325]

# Notes
