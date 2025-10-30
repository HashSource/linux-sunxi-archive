# Allwinner SoC Family
(Redirected from [Sunxi][52201])
 
## Contents
  * [1 SoC series][52204]
    * [1.1 "A"-Series][52205]
    * [1.2 "F"-Series][52206]
    * [1.3 "H"-Series][52207]
    * [1.4 "R"-Series][52208]
    * [1.5 "T"-series][52209]
    * [1.6 "V"-series][52210]
    * [1.7 "X" - (B/MR/S/VR/TV) - series][52211]
    * [1.8 "RISC-V"-Series][52212]
  * [2 2013 naming scheme change][52213]
  * [3 Features][52214]
    * [3.1 Comparison table][52215]
  * [4 References][52216]

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
[Allwinner A10][52217] | (sun4i) | 1 x Cortex-A8 CPU-core   
---|---|---  
[Allwinner A13][52218] | (sun5i) | 1 x Cortex-A8 CPU-core   
[Allwinner A10s][52219] | (sun5i) | 1 x Cortex-A8 CPU-core   
[Allwinner A20][52220][[1]][52221] | (sun7i) | 2 x Cortex-A7 CPU-cores   
[Allwinner A23][52222] | (sun8i) | 2 x Cortex-A7 CPU-cores   
[Allwinner A31][52223] | (sun6i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A31s][52224] | (sun6i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A33][52225][[2]][52226] | (sun8i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A40i][52227][[3]][52228] | (sun8i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A50][52229][[4]][52230] | (sun8i) | 4 x Cortex-A7 CPU-cores   
[Allwinner A80][52231] | (sun9i) | 4 x Cortex-A7 CPU-cores + 4 x Cortex-A15 CPU-cores   
(using ARM big.LITTLE heterogeneous CPU architecture)  
[Allwinner A83T][52232][[5]][52233] | (sun8i) | 8 x Cortex-A7 CPU-cores   
**64-bit**
Based on ARMv8 Cortex-A cores (Cortex-A53, A55) targeted for high-end devices like digital media players, tablets, and netbooks: 
[Allwinner A63][52234][[6]][52235] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner A64][52236][[7]][52237] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner A100][52238] | (sun50i) | 4 x Cortex-A53 CPU-cores   
[Allwinner A133][52239][[8]][52240] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner A523][52241] | (sun55i) | 8 x Cortex-A55 CPU-core   
[Allwinner A527][52242] | (sun55iw3) | 8 x Cortex-A55 CPU-core   
[Allwinner A733][52243] | (sun60i) | 2 x Cortex-A76 CPU-core + 6 x Cortex-A55 CPU-core   
[Allwinner A537][52244] | (sun65i) | 2 x Cortex-A73 CPU-core + 2 x Cortex-A53 CPU-core + 4 x Cortex-A53 CPU-core   
[Allwinner A333][52245] | (sun65i) | 1 x Cortex-A73 CPU-core + 4 x Cortex-A53 CPU-core   
## "F"-Series
    **[![Sticky-note-pin.png][52246]][52247]_Note:_ The F series is not supported by the linux-sunxi community due to lack of developers and hardware. _sun3i_ have only official linux support, _sunii_ have no linux support, only Allwinner's "Melis" RTOS.**
Based on ARMv5 ARM926-EJS core and currently targeted for low market devices such as cheap ebook readers, etc. 
F1C700 seems to be a remarked A13, and it's ARMv7. 
[Boxchip C100][52248] | (sun3i)  
---|---  
[Boxchip E200][52249] | (sun3i)  
[Boxchip F10][52250] aka SoChip SC9800 aka Teclast T8100 | (sunii)  
[Boxchip F13][52251] | (sunii)  
[Boxchip F15][52251] aka SoChip SC8600 aka Teclast T7200 | (sunii)  
[Boxchip F18][52252] | (sunii)  
[Boxchip F20][52253] | (sun3i)  
[Allwinner F23][52254][[9]][52255] aka F1C100A | (suniv)  
[Allwinner F25][52256][[10]][52257] | (suniv)  
[Allwinner F1C100A][52258][[11]][52259] | (suniv)  
[Allwinner F1C100s][52260][[12]][52261] | (suniv)  
[Allwinner F1C200s][52262][[13]][52263] | (suniv)  
[Allwinner F1C500][52264][[14]][52265] | (suniv)  
[Allwinner F1C500s][52266][[15]][52267] | (suniv)  
[Allwinner F1C600][52268][[16]][52269] | (suniv)  
[Allwinner F1C700][52270] | (sun5i)  
[Allwinner F1C800][52271][[17]][52272] | (suniv)  
[Allwinner F1D100][52273][[18]][52274] | (suniv)  
## "H"-Series
Based on ARMv7/ARMv8 Cortex-A cores (A7/A53) targeted for video OTT (over-the-top) boxes and high-end gaming consoles: 
[Allwinner H2+][52275][[19]][52276] | (sun8i) | 4 x Cortex-A7 CPU-core  
---|---|---  
[Allwinner H3][52277][[20]][52278] | (sun8i) | 4 x Cortex-A7 CPU-core  
[Allwinner H8][52279] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner H80][52280][[21]][52281] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner H133][52282] | (sun8i) | 2 x Cortex-A7 CPU-core   
**64-bit**
[Allwinner H5][52283][[22]][52284] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner H6][52285][[23]][52286] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H64][52287][[24]][52288] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H313][52289][[25]][52290] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H616][52291][[26]][52292] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H618][52293] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H700][52294] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H713][52295] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H716][52296] | (sun50i) | 4 x Cortex-A53 CPU-core   
[Allwinner H728][52297] | (sun55i) | 8 x Cortex-A55 CPU-core   
[Allwinner H135][52298] | (sun251i) | 1 x RISC-V T-Head XuanTie C906 CPU-core   
[Allwinner H136][52299] | (sun251i) | 1 x RISC-V T-Head XuanTie C906 CPU-core   
[Allwinner H137][52300] | (sun251i) | 1 x RISC-V T-Head XuanTie C906 CPU-core   
## "R"-Series
[Allwinner R6][52301][[27]][52302] | (sun3i) | 1 x ARM926EJ-S CPU-core   
---|---|---  
[Allwinner R7][52303][[28]][52304] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner R8][52305][[29]][52306] | (sun5i) | 1 x Cortex-A8 CPU-core   
[Allwinner R11][52307][[30]][52308] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner R16][52309][[31]][52310] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner R40][52311][[32]][52312] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner R58][52313][[33]][52314] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner R311][52315][[34]][52316] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner R328][52317][[35]][52318] | (sun8i) | 2 x Cortex-A7 CPU-core   
[Allwinner R853][52319] | (sun8i) | 1 x Cortex-A7 CPU-core + 1 x RISC-V MCU   
The Allwinner R8 is repackaged version of the A13. This SoC gets used in the minicomputer presented in Next Thing Co.'s [_C.H.I.P._][52320] kickstarter project ("The $9 computer")[[36]][52321]. 
By comparing the product pages the R16 seems to be a relabeled version of A33. This is somewhat confirmed by the (identical) SoC ID the BROM reports.[[37]][52322]
**64-bit**
[Allwinner R18][52323][[38]][52324] | sun50i | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner R329][52325][[39]][52326] | (sun50i) | 2 x Cortex-A53 CPU-core   
[Allwinner R818][52327][[40]][52328] | (sun50i) | 4 x Cortex-A53 CPU-core   
**64-bit Heterogeneous**
[Allwinner R128][52329] | sun20i | 1 x Cortex-m33, 1 x Xuantie C906, 1 x HiFi5 DSP   
---|---|---  
## "T"-series
[Allwinner T2][52330][[41]][52331] | (sun8i) | 2 x Cortex-A7 CPU-core   
---|---|---  
[Allwinner T3][52332][[42]][52333] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner T7][52334][[43]][52335] | (sun8i) | 6 x Cortex-A7 CPU-core   
[Allwinner T8][52336][[44]][52337] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner T113-S3][52338] | (sun8i) | 2 x Cortex-A7 CPU-core   
[Allwinner T113-I][52339] | (sun8i) | 2 x Cortex-A7 CPU-core + 1 x RISC-V [T-Head XuanTie C906][52340] CPU-core   
  
**64-bit**
[Allwinner T507(T5 Series)][52341][[45]][52342] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner T527][52343][[46]][52344] | (sun55i) | 8 x Cortex-A55 CPU-core   
[Allwinner T536][52345] | (sun55i) | 4 x Cortex-A55 CPU-core   
## "V"-series
[Allwinner V3][52346][[47]][52347] | (sun8i) | 1 x Cortex-A7 CPU-core   
---|---|---  
[Allwinner V3s][52348][[48]][52349] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner V5][52350][[49]][52351] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner V40][52352][[50]][52353] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner V66][52354][[51]][52355] | (sun8i) | 8 x Cortex-A7 CPU-core   
[Allwinner V316][52356][[52]][52357] | (sun8i) | 2 x Cortex-A7 CPU-core   
[Allwinner V536][52358][[53]][52359] | (sun8i) | 2 x Cortex-A7 CPU-core   
[Allwinner V831][52360] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner V833][52361] | (sun8i) | 1 x Cortex-A7 CPU-core   
[Allwinner V837s][52362] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V853s][52363] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V853][52364] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V851s][52365] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V851se][52366] | (sun8i) | 1 x Cortex-A7 CPU-core + 1x RISC-V MCU Core   
[Allwinner V821][52367] | (sun300i) | 1 x [Andes A27L2][52368] RISC-V RV32 CPU-core + 1x [T-Head XuanTie E907][52369] RISC-V RV32 MCU-Core   
## "X" - (B/MR/S/VR/TV) - series
[Allwinner B288][52370][[54]][52371] | (sun8i) | 2 x Cortex-A7 CPU-core   
---|---|---  
[Allwinner B300][52372][[55]][52373] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner MR100][52374][[56]][52375] | (sun8i) | 4 x Cortex-A7 CPU-core   
---|---|---  
[Allwinner MR133][52376][[57]][52377] | (sun8i) | 4 x Cortex-A7 CPU-core   
[Allwinner S3][52378][[58]][52379] | (sun8i) | 1 x Cortex-A7 CPU-core   
---|---|---  
**64-bit**
[Allwinner VR9][52380][[59]][52381] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner MR813][52382] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
[Allwinner MR527][52383] | (sun55i) | 8 x Cortex-A55 CPU-core   
[Allwinner TV303][52384] | (sun50i) | 4 x Cortex-A53 CPU-core   
---|---|---  
## "RISC-V"-Series
[Allwinner D1][52385][[60]][52386] | (sun20i) | 1 x RISC-V [T-Head XuanTie C906][52340] CPU-core   
---|---|---  
[Allwinner D1s (or F133)][52387][[61]][52388] | (sun20i) | 1 x RISC-V [T-Head XuanTie C906][52340] CPU-core   
[Allwinner V821][52367] | (sun300i) | 1 x [Andes A27L2][52368] RISC-V RV32 CPU-core + 1x [T-Head XuanTie E907][52369] RISC-V RV32 MCU-Core   
# 2013 naming scheme change
Initially, Allwinner named their SoCs chronologically: 
  * sun4i = A10
  * sun5i = A13/A10s
  * sun6i = A31
  * sun7i = A20

but, somewhere in 2013, Allwinner decided to update their naming scheme to be based on the ARM core used instead: (taken from the A80 SDK kernel code). 
Note: SoCs with "?" have never appeared on Allwinner's website. [[62]][52389]
TODO: Add to the following table: [F1C800][52271], [F23][52254], [F25][52256], [R11][52307], [R328][52317], [T2][52330], [T5][52390], [T8][52336], [MR100][52374], [VR9][52380], [H716][52296], [V837s][52362], [F135][52391], [H727][52392], [T153][52393]
sunxi (arm cores) | sunxiwx (soc id) | p (rev id) | soc name | cores | notes   
---|---|---|---|---|---  
sun3i (arm926ejs) | sun3iw1 (0x1663) | sun3iw1p1 | [F1C100s][52260], [F1C100A][52258], [F1C200s][52262], [F1C500][52264], [F1C500s][52266], [F1C600][52268], [F1D100][52273], [R6][52301] | 1xARM926EJ-S   
sun4i (cortex-a8)  | sun4iw1 (0x1623) | sun4iw1p1 | [A10][52217] | 1xCortex-A8   
sun4iw2 (0x1625)  | sun4iw2p1 | [A13][52218] | 1xCortex-A8   
sun4iw2p2 | [A12][52394] | ?   
sun4iw2p3 | [A10s][52219] | 1xCortex-A8   
sun8i (cortex-a7 smp)  | sun8iw1 (0x1633)  | sun8iw1p1 | [A31][52223] | 4xCortex-A7   
sun8iw1p2 | [A31s][52224] | 4xCortex-A7   
sun8iw2 (0x1651)  | sun8iw2p1 | [A20][52220] | 2xCortex-A7   
sun8iw2p2 | ? | ?   
sun8iw3 (0x1650)  | sun8iw3p1 | [A23][52222] | 2xCortex-A7   
sun8iw3p2 | ? | ?   
sun8iw5 (0x1667) | sun8iw5p1 | [A33][52225], [R16][52309] | 4xCortex-A7   
sun8iw6 (0x1673) | sun8iw6p1 | [A83T][52232], [H8][52279], [H80][52280], [V66][52354], [R58][52313] | 8xCortex-A7   
sun8iw7 (0x1680) | sun8iw7p1 | [H3][52277], [H2+][52275] | 4xCortex-A7   
sun8iw8 (0x1681)  | sun8iw8p1 | [V3][52346], [S3][52378], [V3s][52348] | 1xCortex-A7 | called V30 in allwinner's kernel source   
sun8iw8p2 | ? | ? | called V33 in allwinner's kernel source   
sun8iw10 (0x1699) | sun8iw10p1 | [B288][52370], [B100][52395] | 2xCortex-A7   
sun8iw11 (0x1701)  | sun8iw11p1 | [R40][52311], [V40][52352], [T3][52332], [A40i][52227], [A20e][52396]? | 4xCortex-A7   
sun8iw11p2 | ?? | 4xCortex-A7   
sun8iw11p3 | ?? | 4xCortex-A7   
sun8iw11p4 | ?? | 4xCortex-A7   
sun8iw12 (0x1721) | sun8iw12p1 | [V5][52350], [V100][52397] | 4xCortex-A7   
sun8iw15 (0x1755) | sun8iw15p1 | [A50][52229], [MR133][52376], [R311][52315], [B300][52372] | 4xCortex-A7   
sun8iw16 (0x1816) | sun8iw16p1 | [V313][52398], [V316][52356], [V526][52399], [V536][52358], [V5V200][52400] | 2xCortex-A7   
sun8iw17 (0x1708) | sun8iw17p1 | [T7][52334] | 6xCortex-A7   
sun8iw19 (0x1817) | sun8iw19p1 | [V533][52401], [V833][52361], [V831][52360] | 1xCortex-A7   
sun8iw20 (0x1859) | sun8iw20p1 | [R528][52402], [T113][52403], [T133-I][52404], [T113-s3][52338], [H133][52282] | 2xCortex-A7   
sun8iw21 (0x1886) | sun8iw21p1 | [V853][52364], [V851s][52365], [V851se][52366] | 1xCortex-A7 1xE907 AMP   
sun9i (cortex-a15/cortex-a7 big.LITTLE)  | sun9iw1 (0x1639)  | sun9iw1p1 | [A80][52231] | 4xCortex-A7 + 4xCortex-A15   
sun9iw1p2 | [A80T][52405] | ?   
sun20i (RISC-V)  | sun20iw1 (0x1859) | sun20iw1p1 | [D1][52385], [F133][52406], [F133-A][52387], [F133-B][52387] | 1xXuantie C906   
sun20iw2 (0x1886) | sun20iw2p1 | [V853][52364], [V851s][52365], [V851se][52366] | 1xXuantie E907 | Remoteproc   
sun20iw3 (0x1883) | sun20iw3p1 | [R128][52329] | 1xXuantie C906 + 1xARM STAR MC1 + 1xHIFI5 DSP   
sun50i (cortex-a53 smp)  | sun50iw1 (0x1689) | sun50iw1p1 | [A64][52236], [H64][52287], [R18][52323] | 4xCortex-A53   
sun50iw2 (0x1718) | sun50iw2p1 | [H5][52283] | 4xCortex-A53   
sun50iw3 (0x1719) | sun50iw3p1 | [A63][52234] | 4xCortex-A53   
sun50iw5 (?) | sun50iw5p1 | [AW1750][52407] | ?   
sun50iw6 (0x1728) | sun50iw6p1 | [H6][52285] | 4xCortex-A53   
sun50iw9 (0x1823) | sun50iw9p1 | [H313][52289], [H503][52408], [H513][52409], [H616][52291], [H618][52293], [H700][52294], [T507][52341], [T517][52410] | 4xCortex-A53   
sun50iw10 (0x1855) | sun50iw10p1 | [A100][52238], [A133][52239], [A53][52411], [T509][52412], [R818][52327], [B810][52413], [MR813][52382] | 4xCortex-A53   
sun50iw11 (0x1851) | sun50iw11p1 | [R329][52325] | 2xCortex-A53   
sun50iw12 (0x1860) | sun50iw12p1 | [TV303][52384], [H713][52295] | 4xCortex-A53   
sun55i (cortex-a55 smp big.LITTLE)  | sun55iw3 (0x1890) | sun55iw3p1 | [A523][52241], [T527][52343], [MR527][52383], [A527][52242], [H728][52297] | 8xCortex-A55   
sun55iw6 (0x1909) | sun55iw6p1 | [T536][52345], [MR536][52414] | 4xCortex-A55   
sun60i (cortex-a76 smp big.LITTLE)  | sun60iw1 | sun60iw1p1 | [T736][52415] Abandoned | ?xCortex-A76 + ?xCortex-A55   
sun60iw2 (0x1903) | sun60iw2p1 | [A733][52243] [T736][52415] | 2xCortex-A76 + 6xCortex-A55   
sun65i (cortex-a73 smp big.LITTLE)  | sun65iw1 (0x19xx) | sun65iw1p1 | [A537][52244] | 2xCortex-A73 + 2xCortex-A53 + 4xCortex-A53   
sun65iw1 (0x19xx) | sun65iw1p1 | [A333][52245] | 1xCortex-A73 + 4xCortex-A53   
sun251i (RISC-V C906)  | sun251iw1 (0x19xx) | sun251iw1p1 | [H135][52298] [H136][52299] [H137][52300] | 1 x RISC-V T-Head XuanTie C906 CPU-core   
sun300i (RISC-V)  | sun300iw1 (0x1882) | sun300iw1p1 | [V821][52367] | 1xRISC-V CPU + 1xRISC-V MCU   
This new naming scheme is of absolutely no value with respect to the rest of the SoC. The actual ARM core(s) used are usually the least important piece of information for SoC support. This table completely ignores the fact that A20 is an updated A10 and is pin compatible. It also ignores the fact that A31 introduced a lot of changes which were carried on to the A23/A33 and possibly A80 parts. It therefore is quite likely that this naming scheme was purely a marketing decision, and that Allwinner marketing will change its mind again. 
# Features
  * CPU: ARMv7-A [Cortex-A7][52416], [Cortex-A15][52417] or [Cortex-A8][52418] Central Processor Unit with (co-)processor extensions: 
    * Advanced SIMD: [NEON][52419] (ARM's extended general-purpose advanced SIMD vector processing extension engine)
    * [Vector Floating Point Unit][52420] ([VFPU][52421]): ARM VFPv3 lite (Cortex-A8) / VFPv4 (Cortex-A7)
    * Security Extensions: 
      * [TrustZone][52422] secure world
      * [Security accelerator][52423] supporting AES, DES, 3DES, SHA-1, MD5 and pseudo-random number generation
    * [Thumb-2][52424] instruction set extension for optimized code to reduce memory footprint and improve performance
  * GPU: [Mali400][52425], Mali400-MP2, SGX544 or PowerVR G6230 Graphics Procesor Unit, supporting OpenGL ES2.
  * VPU: [Cedar Engine][52426] (Video Processor Unit for audio and video hardware decoding or encoding)
  * HDMI-transmitter with [HDMI CEC][52427] (Consumer Electronics Control), with exception of A13 which lacks HDMI-transmitter and SATA-controller[[63]][52428]
  * Hardware virtualization capabilities (Cortex-A7 only).
  * Up to 4GB memory (Cortex-A8), Up to 1TB memory with LPAE (Cortex-A7 only).

## Comparison table
| [A10][52217] | [A10s][52219] | [A13][52218] | [A20][52220] | [A23][52222] | [A31][52223] | [A31s][52224] | [A33][52225] | [A80][52231]  
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
GPU  | [Mali400][52425]  
320 MHz | [Mali400][52425]  
320 MHz | [Mali400][52425]  
320 MHz | [Mali400][52425]-MP2  
350 MHz | [Mali400][52425]-MP2 | SGX544  
200 MHz | SGX544  
200 MHz | [Mali400][52425]-MP2 | 64-core PowerVR G6230   
GPU API  | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL ES 2.0, OpenVG 1.1, OpenCL 1.1, and DirectX 9.3 | OpenGL ES 2.0, OpenVG 1.1, OpenCL 1.1, and DirectX 9.3 | OpenGL ES 2.0, OpenVG 1.1 | OpenGL 3.x, OpenGL ES Next,3.0,2.0, Open CL 1.x, DirectX 11 level 9_3/10_0[[64]][52429]  
[Video decoder][52426] | 2160p | 1080p | 1080p | 2160p, 4K×2K, 1080p 3D | 1080p@60fps | 2160p, 4K×2K, 1080p 3D | 2160p, 1080p 3D | 1080p@60fps | ? (A80)   
[Video encoder][52426] | H.264 1080p@30fps, JPEG | H.264 1080p@30fps, JPEG | H.264 1080p@30fps, JPEG | H.264 1080p@30fps, JPEG | 1080p@60fps | H.264 1080p@60fps, JPEG | H264 1080p@30fps, 720p@60fps | H.264 1080p@60fps, JPEG | H.264 HP/VP8 4Kx2K@30fp   
Audio decoder  | AC3, DTS | ? | ? | AC3, DTS | - | ? (A31) | ? (A31S) | ? (A33) | ? (A80)   
Video interfaces  | HDMI 1.3, YPbPr, VGA, CPU/RGB/LVDS LCD | HDMI 1.3, RGB/LVDS LCD | RGB LCD, VGA | HDMI 1.4, CVBS, YPbPr, VGA, CPU/RGB/LVDS LCD | CPU/RGB/LVDS LCD, MIPI DSI | HDMI 1.4, MIPI DSI, 2-channel LVDS, 2-channel RGB LCD | HDMI 1.4, LVDS, RGB LCD | CPU/RGB/LVDS LCD, MIPI DSI | HDMI 4K, RGB LCD 2048x1536@60fps, dual-channel LVDS 1920x1080@60fps, 4-lane MIPI DSI 1920x1200@60fps, 4-lane eDP 2560x1600@60fps   
Audio interfaces  | I2S, SPDIF, AC97 | I2S, AC97 | I2S, AC97 | I2S, PCM, AC97 | I2S, PCM | 2 I2S, 2 PCM | I2S, 2 PCM | ? (A33) | ? (A80)   
USB OTG  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ? (A33) | 1   
USB Host  | 2 | 1 | 1 | 2 | 1 | 2 | 2 | ? (A33) | 2x USB Host, USB 3.0/2.0 Dual-Role (host/device)   
Ethernet  | EMAC | EMAC | - | EMAC/GMAC | - | GMAC | GMAC | - | GMAC   
Storage  | NAND (max 64GB), SATA II, SD Card 3.0 | NAND (max 64GB), SD Card 3.0 | NAND (max 64GB), SD Card 3.0 | NAND, MMC, [SATA][52430] | raw NAND, eMMC, SD card | 4 x SD Card, eMMC NAND, 2-channel raw NAND | 4 x SD Card, eMMC NAND, raw NAND | 3 x SD Card, eMMC NAND, raw NAND | 4 x SD/MMC   
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
[[65]][52431]
# References
  1. [↑][52432] [http://www.allwinnertech.com/index.php?c=product&a=index&id=45][52433]
  2. [↑][52434] [http://www.allwinnertech.com/index.php?c=product&a=index&id=23][52435]
  3. [↑][52436] [http://www.allwinnertech.com/index.php?c=product&a=index&id=69][52437]
  4. [↑][52438] [http://www.allwinnertech.com/index.php?c=product&a=index&id=72][52439]
  5. [↑][52440] [http://www.allwinnertech.com/index.php?c=product&a=index&id=24][52441]
  6. [↑][52442] [http://www.allwinnertech.com/index.php?c=product&a=index&id=67][52443]
  7. [↑][52444] [http://www.allwinnertech.com/index.php?c=product&a=index&id=9][52445]
  8. [↑][52446] [http://www.allwinnertech.com/index.php?c=product&a=index&id=93][52447]
  9. [↑][52448] [http://www.allwinnertech.com/index.php?c=product&a=index&id=30][52449]
  10. [↑][52450] [http://www.allwinnertech.com/index.php?c=product&a=index&id=31][52451]
  11. [↑][52452] [http://www.allwinnertech.com/index.php?c=product&a=index&id=29][52453]
  12. [↑][52454] [http://www.allwinnertech.com/index.php?c=product&a=index&id=73][52455]
  13. [↑][52456] [http://www.allwinnertech.com/index.php?c=product&a=index&id=74][52457]
  14. [↑][52458] [http://www.allwinnertech.com/index.php?c=product&a=index&id=27][52459]
  15. [↑][52460] [http://www.allwinnertech.com/index.php?c=product&a=index&id=75][52461]
  16. [↑][52462] [http://www.allwinnertech.com/index.php?c=product&a=index&id=28][52463]
  17. [↑][52464] [http://www.allwinnertech.com/index.php?c=product&a=index&id=76][52465]
  18. [↑][52466] [http://www.allwinnertech.com/index.php?c=product&a=index&id=64][52467]
  19. [↑][52468] [http://www.allwinnertech.com/index.php?c=product&a=index&id=62][52469]
  20. [↑][52470] [http://www.allwinnertech.com/index.php?c=product&a=index&id=47][52471]
  21. [↑][52472] [http://www.allwinnertech.com/index.php?c=product&a=index&id=46][52473]
  22. [↑][52474] [https://web.archive.org/web/20180131124325/http://www.allwinnertech.com/index.php?c=product&a=index&id=57][52475]
  23. [↑][52476] [http://www.allwinnertech.com/index.php?c=product&a=index&id=66][52477]
  24. [↑][52478] <http://web.archive.org/web/20160425223052/http://www.allwinnertech.com/en/clq/H_series/6100.html>
  25. [↑][52479] [http://www.allwinnertech.com/index.php?c=product&a=index&id=90][52480]
  26. [↑][52481] [http://www.allwinnertech.com/index.php?c=product&a=index&id=89][52482]
  27. [↑][52483] [http://www.allwinnertech.com/index.php?c=product&a=index&id=79][52484]
  28. [↑][52485] [https://web.archive.org/web/20191218202340/http://www.allwinnertech.com/index.php?c=product&a=index&id=82][52486]
  29. [↑][52487] <http://web.archive.org/web/20160510053338/http://www.allwinnertech.com/en/clq/R_series/2015/0514/R8.html>
  30. [↑][52488] [http://www.allwinnertech.com/index.php?c=product&a=index&id=83][52489]
  31. [↑][52490] [http://www.allwinnertech.com/index.php?c=product&a=index&id=51][52491]
  32. [↑][52492] [https://web.archive.org/web/20191229233801/http://www.allwinnertech.com/index.php?c=product&a=index&id=56][52493]
  33. [↑][52494] [http://www.allwinnertech.com/index.php?c=product&a=index&id=49][52495]
  34. [↑][52496] [http://www.allwinnertech.com/index.php?c=product&a=index&id=84][52497]
  35. [↑][52498] [http://www.allwinnertech.com/index.php?c=product&a=index&id=85][52499]
  36. [↑][52500] <http://nextthing.co/>
  37. [↑][52501] <https://groups.google.com/d/msg/linux-sunxi/vx6oQMy-nis/vgVc8d1KBAAJ>
  38. [↑][52502] [http://www.allwinnertech.com/index.php?c=product&a=index&id=68][52503]
  39. [↑][52504] [http://www.allwinnertech.com/index.php?c=product&a=index&id=91][52505]
  40. [↑][52506] [http://www.allwinnertech.com/index.php?c=product&a=index&id=92][52507]
  41. [↑][52508] [http://www.allwinnertech.com/index.php?c=product&a=index&id=39][52509]
  42. [↑][52510] [http://www.allwinnertech.com/index.php?c=product&a=index&id=41][52511]
  43. [↑][52512] [http://www.allwinnertech.com/index.php?c=product&a=index&id=71][52513]
  44. [↑][52514] [http://www.allwinnertech.com/index.php?c=product&a=index&id=43][52515]
  45. [↑][52516] [http://www.allwinnertech.com/index.php?c=product&a=index&id=94][52517]
  46. [↑][52518] [http://www.allwinnertech.com/index.php?c=product&a=index&id=94][52517]
  47. [↑][52519] [http://www.allwinnertech.com/index.php?c=product&a=index&id=37][52520]
  48. [↑][52521] [http://www.allwinnertech.com/index.php?c=product&a=index&id=38][52522]
  49. [↑][52523] [http://www.allwinnertech.com/index.php?c=product&a=index&id=70][52524]
  50. [↑][52525] [http://www.allwinnertech.com/index.php?c=product&a=index&id=36][52526]
  51. [↑][52527] [http://www.allwinnertech.com/index.php?c=product&a=index&id=35][52528]
  52. [↑][52529] [http://www.allwinnertech.com/index.php?c=product&a=index&id=87][52530]
  53. [↑][52531] [http://www.allwinnertech.com/index.php?c=product&a=index&id=88][52532]
  54. [↑][52533] [http://www.allwinnertech.com/index.php?c=product&a=index&id=59][52534]
  55. [↑][52535] [http://www.allwinnertech.com/index.php?c=product&a=index&id=86][52536]
  56. [↑][52537] [http://www.allwinnertech.com/index.php?c=product&a=index&id=77][52538]
  57. [↑][52539] [http://www.allwinnertech.com/index.php?c=product&a=index&id=81][52540]
  58. [↑][52541] [https://www.allwinnertech.com/index.php?c=product&a=index&id=78][52542]
  59. [↑][52543] [https://www.allwinnertech.com/index.php?c=product&a=index&id=65][52544]
  60. [↑][52545] [https://www.allwinnertech.com/index.php?c=product&a=index&id=97][52546]
  61. [↑][52547] [https://www.allwinnertech.com/index.php?c=product&a=index&id=101][52548]
  62. [↑][52549] <https://github.com/tinalinux/brandy/blob/r40-v1.y/SUNXI_README>
  63. [↑][52550] ["Cortex A8 in TQFP? sure Allwinner A13"][52551] _Retrieved 23 September 2012_
  64. [↑][52552] <http://www.imgtec.com/news/detail.asp?ID=845>
  65. [↑][52553] <https://web.archive.org/web/20130301050520/http://blog.thinkteletronics.com/all-mobile-socsolutions/> All Mobile Soc/Solutions.
