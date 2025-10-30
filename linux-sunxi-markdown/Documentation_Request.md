# Documentation Request
## Reason
<benn> allwinner ask me to give suggestion to them for datasheet writing <benn> If you have any suggestion about it , please let me know, so that the coming datasheet will more readable for us 
## Suggestions
<mnemoc> the most important thing is to document all the registers of all the IPs =) <mnemoc> benn____: we are working on getting an androidized sunxi-3.10 branch (DTS based) including everything going into mainline but also the other allwinner drivers which don't have the required quality or use the proper frameworks yet. we will also teach fexc (from sunxi-tools to generate a .dts out of the script.bin (sys_config). I would be awesome if AW, instead of hacking all their stuff directly on top of android-3.10 (for A60 and A80) would help us and work to <mnemoc> benn____: but proper documentation of ALL registers of ALL IPs of ALL SoCs is already awesome ;-) 
<steev> nand? 
<mripard> mnemoc: I'd be more interested in how to use these registers, than just having a list. 
<hramrach> also they might have much easier time writing if they could obtain permission to disclose the documentation they received from the IP provider and only described how they connected the IP 
<focus> benn: as an electronic engineer, I help you with datasheet and make any amount of contributions needed to make the documentation readable and successfull - if allwinner don't mind, i would also like to make html documentation - that way you don't have to flick pages, just clicko on diagrams and suggestions to get specific information about a pin or register. 
<focus> benn: i can't release any of it because i would infringe copyright of someone or other - so it would be good if the documentation they finally release allow is creative commons license so that diagrams can be cut and integrated into html documentation without infringing copyright - more information for their engineers and more sales for their chips
