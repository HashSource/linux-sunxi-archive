# Allwinner SoC Family
## Contents
  * [1 SoC series][6649]
    * [1.1 "A"-Series][6650]
    * [1.2 "F"-Series][6651]
    * [1.3 "H"-Series][6652]
    * [1.4 "R"-Series][6653]
    * [1.5 "T"-series][6654]
    * [1.6 "V"-series][6655]
    * [1.7 "X" - (B/MR/S/VR/TV) - series][6656]
    * [1.8 "RISC-V"-Series][6657]
  * [2 2013 naming scheme change][6658]
  * [3 Features][6659]
    * [3.1 Comparison table][6660]
  * [4 References][6661]

# SoC series
**A** series processors are used for mobile applications, mainly referring to tablet application here; 
**B** for "Book", used for E-book tablet reader. 
**H** for “Homlet”, mainly used in home entertainment applications, including smart OTT boxes, HDMI mini PCs, gaming boxes, etc; 
**V** for video-related applications, including video surveillance, automotive DVR, etc; 
**T** series processors target the Automotive products like ADAS. 
**TV** series processors target to the video-related applications, projector, TV 
**F** series are processors based on Allwinner’s melis OS, mainly used in smart video radios, video MP5, etc; 
## "A"-Series
Based on ARMv7 Cortex-A cores (Cortex-A7, A8 and A15) targeted for high-end devices like digital media players, tablets, and netbooks: 
[Allwinner A10][6662] | (sun4i) | 1 x Cortex-A8 CPU-core   
---|---|---  
[Allwinner A13][6663] | (sun5i) | 1 x Cortex-A8 CPU-core   
[Allwinner A10s][6664] | (sun5i) | 1 x Cortex-A8 CPU-core   
[Allwinner A20][6665][[1]][6666] | (sun7i) | 2 x Cortex-A7 CPU-cores   
[Allwinner A23][6667] | (sun8i) | 2 x Cortex-A7 CPU-cores   
[Allwinner A31][6668] | (sun6i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A31s][6669] | (sun6i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A33][6670][[2]][6671] | (sun8i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A40i][6672][[3]][6673] | (sun8i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A50][6674][[4]][6675] | (sun8i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A80][6676] | (sun9i) | 4 x Cortex-A7 CPU-cores + 4 x Cortex-A15 CPU-cores   
(using ARM big.LITTLE heterogeneous CPU architecture)  
[Allwinner A83T][6677][[5]][6678] | (sun8i) | 8 x Cortex-A7 CPU-cores   
**64-bit**
Based on ARMv8 Cortex-A cores (Cortex-A53, A55) targeted for high-end devices like digital media players, tablets, and netbooks: 
[Allwinner A63][6679][[6]][6680] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner A64][6681][[7]][6682] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner A100][6683] | (sun50i) | 4 x Cortex-A53 CPU-cores   
[Allwinner A133][6684][[8]][6685] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner A523][6686] | (sun55i) | 8 x Cortex-A55 CPU-core   
[Allwinner A527][6687] | (sun55iw3) | 8 x Cortex-A55 CPU-core   
[Allwinner A733][6688] | (sun60i) | 2 x Cortex-A76 CPU-core + 6 x Cortex-A55 CPU-core   
[Allwinner A537][6689] | (sun65i) | 2 x Cortex-A73 CPU-core + 2 x Cortex-A53 CPU-core + 4 x Cortex-A53 CPU-core   
[Allwinner A333][6690] | (sun65i) | 1 x Cortex-A73 CPU-core + 4 x Cortex-A53 CPU-core   
## "F"-Series
    **[![Sticky-note-pin.png][6691]][6692]_Note:_ The F series is not supported by the linux-sunxi community due to lack of developers and hardware. _sun3i_ have only official linux support, _sunii_ have no linux support, only Allwinner's "Melis" RTOS.**
Based on ARMv5 ARM926-EJS core and currently targeted for low market devices such as cheap ebook readers, etc. 
F1C700 seems to be a remarked A13, and it's ARMv7. 
[Boxchip C100][6693] | (sun3i)  
---|---  
[Boxchip E200][6694] | (sun3i)  
[Boxchip F10][6695] aka SoChip SC9800 aka Teclast T8100 | (sunii)  
[Boxchip F13][6696] | (sunii)  
[Boxchip F15][6696] aka SoChip SC8600 aka Teclast T7200 | (sunii)  
[Boxchip F18][6697] | (sunii)  
[Boxchip F20][6698] | (sun3i)  
[Allwinner F23][6699][[9]][6700] aka F1C100A | (suniv)  
[Allwinner F25][6701][[10]][6702] | (suniv)  
[Allwinner F1C100A][6703][[11]][6704] | (suniv)  
[Allwinner F1C100s][6705][[12]][6706] | (suniv)  
[Allwinner F1C200s][6707][[13]][6708] | (suniv)  
[Allwinner F1C500][6709][[14]][6710] | (suniv)  
[Allwinner F1C500s][6711][[15]][6712] | (suniv)  
[Allwinner F1C600][6713][[16]][6714] | (suniv)  
[Allwinner F1C700][6715] | (sun5i)  
[Allwinner F1C800][6716][[17]][6717] | (suniv)  
[Allwinner F1D100][6718][[18]][6719] | (suniv)  
## "H"-Series
Based on ARMv7/ARMv8 Cortex-A cores (A7/A53) targeted for video OTT (over-the-top) boxes and high-end gaming consoles: 
[Allwinner H2+][6720][[19]][6721] | (sun8i) | 4 x Cortex-A7 CPU-core  
---|---|---  
[Allwinner H3][6722][[20]][6723] | (sun8i) | 4 x Cortex-A7 CPU-core  
[Allwinner H8][6724] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner H80][6725][[21]][6726] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner H133][6727] | (sun8i) | 2 x Cortex-A7 CPU-core   
**64-bit**
[Allwinner H5][6728][[22]][6729] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner H6][6730][[23]][6731] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H64][6732][[24]][6733] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H313][6734][[25]][6735] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H616][6736][[26]][6737] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H618][6738] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H700][6739] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H713][6740] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H716][6741] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H728][6742] | (sun55i) | 8 x Cortex-A55 CPU-core   
[Allwinner H135][6743] | (sun251i) | 1 x RISC-V T-Head XuanTie C906 CPU-core   
[Allwinner H136][6744] | (sun251i) | 1 x RISC-V T-Head XuanTie C906 CPU-core   
[Allwinner H137][6745] | (sun251i) | 1 x RISC-V T-Head XuanTie C906 CPU-core   
## "R"-Series
[Allwinner R6][6746][[27]][6747] | (sun3i) | 1 x ARM926EJ-S CPU-core   
---|---|---  
[Allwinner R7][6748][[28]][6749] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner R8][6750][[29]][6751] | (sun5i) | 1 x Cortex-A8 CPU-core   
[Allwinner R11][6752][[30]][6753] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner R16][6754][[31]][6755] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner R40][6756][[32]][6757] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner R58][6758][[33]][6759] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner R311][6760][[34]][6761] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner R328][6762][[35]][6763] | (sun8i) | 2 x Cortex-A7 CPU-core   
[Allwinner R853][6764] | (sun8i) | 1 x Cortex-A7 CPU-core + 1 x RISC-V MCU   
The Allwinner R8 is repackaged version of the A13. This SoC gets used in the minicomputer presented in Next Thing Co.'s [_C.H.I.P._][6765] kickstarter project ("The $9 computer")[[36]][6766]. 
By comparing the product pages the R16 seems to be a relabeled version of A33. This is somewhat confirmed by the (identical) SoC ID the BROM reports.[[37]][6767]
**64-bit**
[Allwinner R18][6768][[38]][6769] | sun50i | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner R329][6770][[39]][6771] | (sun50i) | 2 x Cortex-A53 CPU-core   
[Allwinner R818][6772][[40]][6773] | (sun50i) | 4 x Cortex-A53 CPU-core   
**64-bit Heterogeneous**
[Allwinner R128][6774] | sun20i | 1 x Cortex-m33, 1 x Xuantie C906, 1 x HiFi5 DSP   
---|---|---  
## "T"-series
[Allwinner T2][6775][[41]][6776] | (sun8i) | 2 x Cortex-A7 CPU-core   
---|---|---  
[Allwinner T3][6777][[42]][6778] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner T7][6779][[43]][6780] | (sun8i) | 6 x Cortex-A7 CPU-core   
[Allwinner T8][6781][[44]][6782] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner T113-S3][6783] | (sun8i) | 2 x Cortex-A7 CPU-core   
[Allwinner T113-I][6784] | (sun8i) | 2 x Cortex-A7 CPU-core + 1 x RISC-V [T-Head XuanTie C906][6785] CPU-core   
  
**64-bit**
[Allwinner T507(T5 Series)][6786][[45]][6787] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner T527][6788][[46]][6789] | (sun55i) | 8 x Cortex-A55 CPU-core   
[Allwinner T536][6790] | (sun55i) | 4 x Cortex-A55 CPU-core   
## "V"-series
[Allwinner V3][6791][[47]][6792] | (sun8i) | 1 x Cortex-A7 CPU-core   
---|---|---  
[Allwinner V3s][6793][[48]][6794] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner V5][6795][[49]][6796] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner V40][6797][[50]][6798] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner V66][6799][[51]][6800] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner V316][6801][[52]][6802] | (sun8i) | 2 x Cortex-A7 CPU-core   
[Allwinner V536][6803][[53]][6804] | (sun8i) | 2 x Cortex-A7 CPU-core   
[Allwinner V831][6805] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner V833][6806] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner V837s][6807] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V853s][6808] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V853][6809] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V851s][6810] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V851se][6811] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V821][6812] | (sun300i) | 1 x [Andes A27L2][6813] RISC-V RV32 CPU-core + 1x [T-Head XuanTie E907][6814] RISC-V RV32 MCU-Core   
## "X" - (B/MR/S/VR/TV) - series
[Allwinner B288][6815][[54]][6816] | (sun8i) | 2 x Cortex-A7 CPU-core   
---|---|---  
[Allwinner B300][6817][[55]][6818] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner MR100][6819][[56]][6820] | (sun8i) | 4 x Cortex-A7 CPU-core   
---|---|---  
[Allwinner MR133][6821][[57]][6822] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner S3][6823][[58]][6824] | (sun8i) | 1 x Cortex-A7 CPU-core   
---|---|---  
**64-bit**
[Allwinner VR9][6825][[59]][6826] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner MR813][6827] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner MR527][6828] | (sun55i) | 8 x Cortex-A55 CPU-core   
[Allwinner TV303][6829] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
## "RISC-V"-Series
[Allwinner D1][6830][[60]][6831] | (sun20i) | 1 x RISC-V [T-Head XuanTie C906][6785] CPU-core   
---|---|---  
[Allwinner D1s (or F133)][6832][[61]][6833] | (sun20i) | 1 x RISC-V [T-Head XuanTie C906][6785] CPU-core   
[Allwinner V821][6812] | (sun300i) | 1 x [Andes A27L2][6813] RISC-V RV32 CPU-core + 1x [T-Head XuanTie E907][6814] RISC-V RV32 MCU-Core   
# 2013 naming scheme change
Initially, Allwinner named their SoCs chronologically: 
  * sun4i = A10
  * sun5i = A13/A10s
  * sun6i = A31
  * sun7i = A20

but, somewhere in 2013, Allwinner decided to update their naming scheme to be based on the ARM core used instead: (taken from the A80 SDK kernel code). 
Note: SoCs with "?" have never appeared on Allwinner's website. [[62]][6834]
TODO: Add to the following table: [F1C800][6716], [F23][6699], [F25][6701], [R11][6752], [R328][6762], [T2][6775], [T5][6835], [T8][6781], [MR100][6819], [VR9][6825], [H716][6741], [V837s][6807], [F135][6836], [H727][6837], [T153][6838]
sunxi (arm cores) | sunxiwx (soc id) | p (rev id) | soc name | cores | notes   
---|---|---|---|---|---  
sun3i (arm926ejs) | sun3iw1 (0x1663) | sun3iw1p1 | [F1C100s][6705], [F1C100A][6703], [F1C200s][6707], [F1C500][6709], [F1C500s][6711], [F1C600][6713], [F1D100][6718], [R6][6746] | 1xARM926EJ-S   
sun4i (cortex-a8)  | sun4iw1 (0x1623) | sun4iw1p1 | [A10][6662] | 1xCortex-A8   
sun4iw2 (0x1625)  | sun4iw2p1 | [A13][6663] | 1xCortex-A8   
sun4iw2p2 | [A12][6839] | ?   
sun4iw2p3 | [A10s][6664] | 1xCortex-A8   
sun8i (cortex-a7 smp)  | sun8iw1 (0x1633)  | sun8iw1p1 | [A31][6668] | 4xCortex-A7   
sun8iw1p2 | [A31s][6669] | 4xCortex-A7   
sun8iw2 (0x1651)  | sun8iw2p1 | [A20][6665] | 2xCortex-A7   
sun8iw2p2 | ? | ?   
sun8iw3 (0x1650)  | sun8iw3p1 | [A23][6667] | 2xCortex-A7   
sun8iw3p2 | ? | ?   
sun8iw5 (0x1667) | sun8iw5p1 | [A33][6670], [R16][6754] | 4xCortex-A7   
sun8iw6 (0x1673) | sun8iw6p1 | [A83T][6677], [H8][6724], [H80][6725], [V66][6799], [R58][6758] | 8xCortex-A7   
sun8iw7 (0x1680) | sun8iw7p1 | [H3][6722], [H2+][6720] | 4xCortex-A7   
sun8iw8 (0x1681)  | sun8iw8p1 | [V3][6791], [S3][6823], [V3s][6793] | 1xCortex-A7 | called V30 in allwinner's kernel source   
sun8iw8p2 | ? | ? | called V33 in allwinner's kernel source   
sun8iw10 (0x1699) | sun8iw10p1 | [B288][6815], [B100][6840] | 2xCortex-A7   
sun8iw11 (0x1701)  | sun8iw11p1 | [R40][6756], [V40][6797], [T3][6777], [A40i][6672], [A20e][6841]? | 4xCortex-A7   
sun8iw11p2 | ?? | 4xCortex-A7   
sun8iw11p3 | ?? | 4xCortex-A7   
sun8iw11p4 | ?? | 4xCortex-A7   
sun8iw12 (0x1721) | sun8iw12p1 | [V5][6795], [V100][6842] | 4xCortex-A7   
sun8iw15 (0x1755) | sun8iw15p1 | [A50][6674], [MR133][6821], [R311][6760], [B300][6817] | 4xCortex-A7   
sun8iw16 (0x1816) | sun8iw16p1 | [V313][6843], [V316][6801], [V526][6844], [V536][6803], [V5V200][6845] | 2xCortex-A7   
sun8iw17 (0x1708) | sun8iw17p1 | [T7][6779] | 6xCortex-A7   
sun8iw19 (0x1817) | sun8iw19p1 | [V533][6846], [V833][6806], [V831][6805] | 1xCortex-A7   
sun8iw20 (0x1859) | sun8iw20p1 | [R528][6847], [T113][6848], [T133-I][6849], [T113-s3][6783], [H133][6727] | 2xCortex-A7   
sun8iw21 (0x1886) | sun8iw21p1 | [V853][6809], [V851s][6810], [V851se][6811] | 1xCortex-A7 1xE907 AMP   
sun9i (cortex-a15/cortex-a7 big.LITTLE)  | sun9iw1 (0x1639)  | sun9iw1p1 | [A80][6676] | 4xCortex-A7 + 4xCortex-A15   
sun9iw1p2 | [A80T][6850] | ?   
sun20i (RISC-V)  | sun20iw1 (0x1859) | sun20iw1p1 | [D1][6830], [F133][6851], [F133-A][6832], [F133-B][6832] | 1xXuantie C906   
sun20iw2 (0x1886) | sun20iw2p1 | [V853][6809], [V851s][6810], [V851se][6811] | 1xXuantie E907 | Remoteproc   
sun20iw3 (0x1883) | sun20iw3p1 | [R128][6774] | 1xXuantie C906 + 1xARM STAR MC1 + 1xHIFI5 DSP   
sun50i (cortex-a53 smp)  | sun50iw1 (0x1689) | sun50iw1p1 | [A64][6681], [H64][6732], [R18][6768] | 4xCortex-A53   
sun50iw2 (0x1718) | sun50iw2p1 | [H5][6728] | 4xCortex-A53   
sun50iw3 (0x1719) | sun50iw3p1 | [A63][6679] | 4xCortex-A53   
sun50iw5 (?) | sun50iw5p1 | [AW1750][6852] | ?   
sun50iw6 (0x1728) | sun50iw6p1 | [H6][6730] | 4xCortex-A53   
sun50iw9 (0x1823) | sun50iw9p1 | [H313][6734], [H503][6853], [H513][6854], [H616][6736], [H618][6738], [H700][6739], [T507][6786], [T517][6855] | 4xCortex-A53   
sun50iw10 (0x1855) | sun50iw10p1 | [A100][6683], [A133][6684], [A53][6856], [T509][6857], [R818][6772], [B810][6858], [MR813][6827] | 4xCortex-A53   
sun50iw11 (0x1851) | sun50iw11p1 | [R329][6770] | 2xCortex-A53   
sun50iw12 (0x1860) | sun50iw12p1 | [TV303][6829], [H713][6740] | 4xCortex-A53   
sun55i (cortex-a55 smp big.LITTLE)  | sun55iw3 (0x1890) | sun55iw3p1 | [A523][6686], [T527][6788], [MR527][6828], [A527][6687], [H728][6742] | 8xCortex-A55   
sun55iw6 (0x1909) | sun55iw6p1 | [T536][6790], [MR536][6859] | 4xCortex-A55   
sun60i (cortex-a76 smp big.LITTLE)  | sun60iw1 | sun60iw1p1 | [T736][6860] Abandoned | ?xCortex-A76 + ?xCortex-A55   
sun60iw2 (0x1903) | sun60iw2p1 | [A733][6688] [T736][6860] | 2xCortex-A76 + 6xCortex-A55   
sun65i (cortex-a73 smp big.LITTLE)  | sun65iw1 (0x19xx) | sun65iw1p1 | [A537][6689] | 2xCortex-A73 + 2xCortex-A53 + 4xCortex-A53   
sun65iw1 (0x19xx) | sun65iw1p1 | [A333][6690] | 1xCortex-A73 + 4xCortex-A53   
sun251i (RISC-V C906)  | sun251iw1 (0x19xx) | sun251iw1p1 | [H135][6743] [H136][6744] [H137][6745] | 1 x RISC-V T-Head XuanTie C906 CPU-core   
sun300i (RISC-V)  | sun300iw1 (0x1882) | sun300iw1p1 | [V821][6812] | 1xRISC-V CPU + 1xRISC-V MCU   
This new naming scheme is of absolutely no value with respect to the rest of the SoC. The actual ARM core(s) used are usually the least important piece of information for SoC support. This table completely ignores the fact that A20 is an updated A10 and is pin compatible. It also ignores the fact that A31 introduced a lot of changes which were carried on to the A23/A33 and possibly A80 parts. It therefore is quite likely that this naming scheme was purely a marketing decision, and that Allwinner marketing will change its mind again. 
# Features
  * CPU: ARMv7-A [Cortex-A7][6861], [Cortex-A15][6862] or [Cortex-A8][6863] Central Processor Unit with (co-)processor extensions: 
    * Advanced SIMD: [NEON][6864] (ARM's extended general-purpose advanced SIMD vector processing extension engine)
    * [Vector Floating Point Unit][6865] ([VFPU][6866]): ARM VFPv3 lite (Cortex-A8) / VFPv4 (Cortex-A7)
    * Security Extensions: 
      * [TrustZone][6867] secure world
      * [Security accelerator][6868] supporting AES, DES, 3DES, SHA-1, MD5 and pseudo-random number generation
    * [Thumb-2][6869] instruction set extension for optimized code to reduce memory footprint and improve performance
  * GPU: [Mali400][6870], Mali400-MP2, SGX544 or PowerVR G6230 Graphics Procesor Unit, supporting OpenGL ES2.
  * VPU: [Cedar Engine][6871] (Video Processor Unit for audio and video hardware decoding or encoding)
  * HDMI-transmitter with [HDMI CEC][6872] (Consumer Electronics Control), with exception of A13 which lacks HDMI-transmitter and SATA-controller[[63]][6873]
  * Hardware virtualization capabilities (Cortex-A7 only).
  * Up to 4GB memory (Cortex-A8), Up to 1TB memory with LPAE (Cortex-A7 only).

## Comparison table
| [A10][6662] | [A10s][6664] | [A13][6663] | [A20][6665] | [A23][6667] | [A31][6668] | [A31s][6669] | [A33][6670] | [A80][6676]  
---|---|---|---|---|---|---|---|---|---  
Generation  | sun4i | sun5i | sun5i | sun7i | sun8i | sun6i | sun6i | sun8i | sun9i   
CPU  | Cortex-A8 | Cortex-A8 | Cortex-A8 | Cortex-A7 | Cortex-A7 | Cortex-A7 | Cortex-A7 | Cortex-A7 | Cortex-A7 / A15   
CPU Maximum frequency  | 1 GHz | 1 GHz | 1 GHz | 960 MHz | 1.5 GHz | ? GHz | ? GHz | 1.5 GHz | 2 (??) GHz   
Cores  | 1 | 1 | 1 | 2 | 2 | 4 | 4 | 4 | 2 x 4   
Extensions  | NEON, VFPv3, Thumb-2 | NEON, VFPv3, Thumb-2 | NEON, VFPv3, Thumb-2 | NEON, VFPv3 / VFPv4, Thumb-2 | NEON, VFPv3 / VFPv4, Thumb-2 | NEON, VFPv3 / VFPv4, Thumb-2 | NEON, VFPv3 / VFPv4, Thumb-2 | NEON, VFPv3 / VFPv4, Thumb-2 | ? (A80)   
Memory  | DDR2, DDR3  
(max 2GB @ DDR800) | DDR2, DDR3  
(max 2GB @ DDR800) | DDR2, DDR3  
(max 512MB @ DDR800) | LPDDR3, DDR3,  
LPDDR2 | DDR3  
(max 1GB) | 2-channel DDR3, LPDDR2,   
2-channel DDR3L, DDR3U | DDR3, DDR3L, LPDDR2 | single-channel DDR3, DDR3L  
(max 1GB) | 2-channel DDR3, DDR3L, LPDDR3, LPDDR2  
up to 8GB   
GPU  | [Mali400][6870]  
320 MHz | [Mali400][6870]  
320 MHz | [Mali400][6870]  
320 MHz | [Mali400][6870]-MP2  
350 MHz | [Mali400][6870]-MP2 | SGX544  
200 MHz | SGX544  
200 MHz | [Mali400][6870]-MP2 | 64-core PowerVR G6230   
GPU API  | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1, OpenCL 1.1, and DirectX 9.3 | OpenGL ES 2.0, OpenVG 1.1, OpenCL 1.1, and DirectX 9.3 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL 3.x, OpenGL ES Next,3.0,2.0, Open CL 1.x, DirectX 11 level 9_3/10_0[[64]][6874]  
[Video decoder][6871] | 2160p | 1080p | 1080p | 2160p, 4K×2K, 1080p 3D | 1080p@60fps | 2160p, 4K×2K, 1080p 3D | 2160p, 1080p 3D | 1080p@60fps | ? (A80)   
[Video encoder][6871] | H.264 1080p@30fps, JPEG | H.264 1080p@30fps, JPEG | H.264 1080p@30fps, JPEG | H.264 1080p@30fps, JPEG | 1080p@60fps | H.264 1080p@60fps, JPEG | H264 1080p@30fps, 720p@60fps | H.264 1080p@60fps, JPEG | H.264 HP/VP8 4Kx2K@30fp   
Audio decoder  | AC3, DTS | ? | ? | AC3, DTS | - | ? (A31) | ? (A31S) | ? (A33) | ? (A80)   
Video interfaces  | HDMI 1.3, YPbPr, VGA, CPU/RGB/LVDS LCD | HDMI 1.3, RGB/LVDS LCD | RGB LCD, VGA | HDMI 1.4, CVBS, YPbPr, VGA, CPU/RGB/LVDS LCD | CPU/RGB/LVDS LCD, MIPI DSI | HDMI 1.4, MIPI DSI, 2-channel LVDS, 2-channel RGB LCD | HDMI 1.4, LVDS, RGB LCD | CPU/RGB/LVDS LCD, MIPI DSI | HDMI 4K, RGB LCD 2048x1536@60fps, dual-channel LVDS 1920x1080@60fps, 4-lane MIPI DSI 1920x1200@60fps, 4-lane eDP 2560x1600@60fps   
Audio interfaces  | I2S, SPDIF, AC97 | I2S, AC97 | I2S, AC97 | I2S, PCM, AC97 | I2S, PCM | 2 I2S, 2 PCM | I2S, 2 PCM | ? (A33) | ? (A80)   
USB OTG  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ? (A33) | 1   
USB Host  | 2 | 1 | 1 | 2 | 1 | 2 | 2 | ? (A33) | 2x USB Host, USB 3.0/2.0 Dual-Role (host/device)   
Ethernet  | EMAC | EMAC | - | EMAC/GMAC | - | GMAC | GMAC | - | GMAC   
Storage  | NAND (max 64GB), SATA II, SD Card 3.0 | NAND (max 64GB), SD Card 3.0 | NAND (max 64GB), SD Card 3.0 | NAND, MMC, [SATA][6875] | raw NAND, eMMC, SD card | 4 x SD Card, eMMC NAND, 2-channel raw NAND | 4 x SD Card, eMMC NAND, raw NAND | 3 x SD Card, eMMC NAND, raw NAND | 4 x SD/MMC   
Package  | BGA441  
19 mm × 19 mm  
0.80 mm Pitch | BGA336  
14 mm × 14 mm  
0.65 mm Pitch | eLQFP176  
20 mm × 20 mm | BGA441  
19 mm × 19 mm  
0.80 mm Pitch | FBGA280  
14 mm x 14 mm x 1.4 mm  
0.80 mm Pitch | BGA609  
18 mm × 8 mm  
0.65 mm Pitch | ? (A31S) | ? (Allwinner: pin compatible with A23) | ? (A80)   
Lithography  | 55 nm | 55 nm | 55 nm | 40 nm | 40 nm | 40 nm | 40 nm | 40 nm | 28 nm   
[[65]][6876]
# References
  1. [↑][6877] [http://www.allwinnertech.com/index.php?c=product&a=index&id=45][6878]
  2. [↑][6879] [http://www.allwinnertech.com/index.php?c=product&a=index&id=23][6880]
  3. [↑][6881] [http://www.allwinnertech.com/index.php?c=product&a=index&id=69][6882]
  4. [↑][6883] [http://www.allwinnertech.com/index.php?c=product&a=index&id=72][6884]
  5. [↑][6885] [http://www.allwinnertech.com/index.php?c=product&a=index&id=24][6886]
  6. [↑][6887] [http://www.allwinnertech.com/index.php?c=product&a=index&id=67][6888]
  7. [↑][6889] [http://www.allwinnertech.com/index.php?c=product&a=index&id=9][6890]
  8. [↑][6891] [http://www.allwinnertech.com/index.php?c=product&a=index&id=93][6892]
  9. [↑][6893] [http://www.allwinnertech.com/index.php?c=product&a=index&id=30][6894]
  10. [↑][6895] [http://www.allwinnertech.com/index.php?c=product&a=index&id=31][6896]
  11. [↑][6897] [http://www.allwinnertech.com/index.php?c=product&a=index&id=29][6898]
  12. [↑][6899] [http://www.allwinnertech.com/index.php?c=product&a=index&id=73][6900]
  13. [↑][6901] [http://www.allwinnertech.com/index.php?c=product&a=index&id=74][6902]
  14. [↑][6903] [http://www.allwinnertech.com/index.php?c=product&a=index&id=27][6904]
  15. [↑][6905] [http://www.allwinnertech.com/index.php?c=product&a=index&id=75][6906]
  16. [↑][6907] [http://www.allwinnertech.com/index.php?c=product&a=index&id=28][6908]
  17. [↑][6909] [http://www.allwinnertech.com/index.php?c=product&a=index&id=76][6910]
  18. [↑][6911] [http://www.allwinnertech.com/index.php?c=product&a=index&id=64][6912]
  19. [↑][6913] [http://www.allwinnertech.com/index.php?c=product&a=index&id=62][6914]
  20. [↑][6915] [http://www.allwinnertech.com/index.php?c=product&a=index&id=47][6916]
  21. [↑][6917] [http://www.allwinnertech.com/index.php?c=product&a=index&id=46][6918]
  22. [↑][6919] [https://web.archive.org/web/20180131124325/http://www.allwinnertech.com/index.php?c=product&a=index&id=57][6920]
  23. [↑][6921] [http://www.allwinnertech.com/index.php?c=product&a=index&id=66][6922]
  24. [↑][6923] <http://web.archive.org/web/20160425223052/http://www.allwinnertech.com/en/clq/H_series/6100.html>
  25. [↑][6924] [http://www.allwinnertech.com/index.php?c=product&a=index&id=90][6925]
  26. [↑][6926] [http://www.allwinnertech.com/index.php?c=product&a=index&id=89][6927]
  27. [↑][6928] [http://www.allwinnertech.com/index.php?c=product&a=index&id=79][6929]
  28. [↑][6930] [https://web.archive.org/web/20191218202340/http://www.allwinnertech.com/index.php?c=product&a=index&id=82][6931]
  29. [↑][6932] <http://web.archive.org/web/20160510053338/http://www.allwinnertech.com/en/clq/R_series/2015/0514/R8.html>
  30. [↑][6933] [http://www.allwinnertech.com/index.php?c=product&a=index&id=83][6934]
  31. [↑][6935] [http://www.allwinnertech.com/index.php?c=product&a=index&id=51][6936]
  32. [↑][6937] [https://web.archive.org/web/20191229233801/http://www.allwinnertech.com/index.php?c=product&a=index&id=56][6938]
  33. [↑][6939] [http://www.allwinnertech.com/index.php?c=product&a=index&id=49][6940]
  34. [↑][6941] [http://www.allwinnertech.com/index.php?c=product&a=index&id=84][6942]
  35. [↑][6943] [http://www.allwinnertech.com/index.php?c=product&a=index&id=85][6944]
  36. [↑][6945] <http://nextthing.co/>
  37. [↑][6946] <https://groups.google.com/d/msg/linux-sunxi/vx6oQMy-nis/vgVc8d1KBAAJ>
  38. [↑][6947] [http://www.allwinnertech.com/index.php?c=product&a=index&id=68][6948]
  39. [↑][6949] [http://www.allwinnertech.com/index.php?c=product&a=index&id=91][6950]
  40. [↑][6951] [http://www.allwinnertech.com/index.php?c=product&a=index&id=92][6952]
  41. [↑][6953] [http://www.allwinnertech.com/index.php?c=product&a=index&id=39][6954]
  42. [↑][6955] [http://www.allwinnertech.com/index.php?c=product&a=index&id=41][6956]
  43. [↑][6957] [http://www.allwinnertech.com/index.php?c=product&a=index&id=71][6958]
  44. [↑][6959] [http://www.allwinnertech.com/index.php?c=product&a=index&id=43][6960]
  45. [↑][6961] [http://www.allwinnertech.com/index.php?c=product&a=index&id=94][6962]
  46. [↑][6963] [http://www.allwinnertech.com/index.php?c=product&a=index&id=94][6962]
  47. [↑][6964] [http://www.allwinnertech.com/index.php?c=product&a=index&id=37][6965]
  48. [↑][6966] [http://www.allwinnertech.com/index.php?c=product&a=index&id=38][6967]
  49. [↑][6968] [http://www.allwinnertech.com/index.php?c=product&a=index&id=70][6969]
  50. [↑][6970] [http://www.allwinnertech.com/index.php?c=product&a=index&id=36][6971]
  51. [↑][6972] [http://www.allwinnertech.com/index.php?c=product&a=index&id=35][6973]
  52. [↑][6974] [http://www.allwinnertech.com/index.php?c=product&a=index&id=87][6975]
  53. [↑][6976] [http://www.allwinnertech.com/index.php?c=product&a=index&id=88][6977]
  54. [↑][6978] [http://www.allwinnertech.com/index.php?c=product&a=index&id=59][6979]
  55. [↑][6980] [http://www.allwinnertech.com/index.php?c=product&a=index&id=86][6981]
  56. [↑][6982] [http://www.allwinnertech.com/index.php?c=product&a=index&id=77][6983]
  57. [↑][6984] [http://www.allwinnertech.com/index.php?c=product&a=index&id=81][6985]
  58. [↑][6986] [https://www.allwinnertech.com/index.php?c=product&a=index&id=78][6987]
  59. [↑][6988] [https://www.allwinnertech.com/index.php?c=product&a=index&id=65][6989]
  60. [↑][6990] [https://www.allwinnertech.com/index.php?c=product&a=index&id=97][6991]
  61. [↑][6992] [https://www.allwinnertech.com/index.php?c=product&a=index&id=101][6993]
  62. [↑][6994] <https://github.com/tinalinux/brandy/blob/r40-v1.y/SUNXI_README>
  63. [↑][6995] ["Cortex A8 in TQFP? sure Allwinner A13"][6996] _Retrieved 23 September 2012_
  64. [↑][6997] <http://www.imgtec.com/news/detail.asp?ID=845>
  65. [↑][6998] <https://web.archive.org/web/20130301050520/http://blog.thinkteletronics.com/all-mobile-socsolutions/> All Mobile Soc/Solutions.
