# A80/SDRAM Controller
< [A80][4833]
 
## Contents
  * [1 SDRAM Control Module][4836]
    * [1.1 Overview][4837]
    * [1.2 Common registers][4838]
    * [1.3 CTL Registers][4839]
    * [1.4 PHY Registers][4840]
    * [1.5 Various other registers][4841]
    * [1.6 dram_para tpr fields][4842]
    * [1.7 registers][4843]

# SDRAM Control Module
## Overview
Allwinner's A80 has a dual channel SDRAM controller. Very likely a close sibling to the controller used in A31. 
## Common registers
Common registers shared by both channels 
[code] 
    MCTL_COM_BASE                   0x01c62000
    
[/code]
[code] 
    SDR_COM_CR                      0x00
    SDR_COM_CCR                     0x04
    SDR_COM_DBGCR                   0x08
    SDR_COM_DBGCR1                  0x0c
    SDR_COM_RMCR                    0x10
    SDR_COM_MMCR                    0x30
    SDR_COM_MBAGCR                  0x70
    SDR_COM_MBACR                   0x74
    SDR_COM_MAER                    0x88
    SDR_COM_MDFSCR                  0x100
    SDR_COM_MDFSMER                 0x104
    SDR_COM_MDFSMRMR                0x108
    SDR_COM_MDFSTR0                 0x10c
    SDR_COM_MDFSTR1                 0x110
    SDR_COM_MDFSTR2                 0x114
    SDR_COM_MDFSTR3                 0x118
    SDR_COM_MDFSGCR                 0x11c
    SDR_COM_MDFSIVR                 0x13c
    SDR_COM_MDFSTCR                 0x14c
    
[/code]
## CTL Registers
CTL registers, one set per channel 
[code] 
    MCTL_CTL0_BASE                  0x01c63000
    MCTL_CTL1_BASE                  0x01c64000
    
[/code]
[code] 
    SDR_SCTL                        0x04
    SDR_SSTAT                       0x08
    SDR_MCMD                        0x40
    SDR_CMDSTAT                     0x4c
    SDR_CMDSTATEN                   0x50
    SDR_MRRCFG0                     0x60
    SDR_MRRSTAT0                    0x64
    SDR_MRRSTAT1                    0x68
    SDR_MCFG1                       0x7c
    SDR_MCFG                        0x80
    SDR_PPCFG                       0x84
    SDR_MSTAT                       0x88
    SDR_LP2ZQCFG                    0x8c
    SDR_DTUSTAT                     0x94
    SDR_DTUNA                       0x98
    SDR_DTUNE                       0x9c
    SDR_DTUPRD0                     0xa0
    SDR_DTUPRD1                     0xa4
    SDR_DTUPRD2                     0xa8
    SDR_DTUPRD3                     0xac
    SDR_DTUAWDT                     0xb0
    SDR_TOGCNT1U                    0xc0
    SDR_TOGCNT100N                  0xcc
    SDR_TREFI                       0xd0
    SDR_TMRD                        0xd4
    SDR_TRFC                        0xd8
    SDR_TRP                         0xdc
    SDR_TRTW                        0xe0
    SDR_TAL                         0xe4
    SDR_TCL                         0xe8
    SDR_TCWL                        0xec
    SDR_TRAS                        0xf0
    SDR_TRC                         0xf4
    SDR_TRCD                        0xf8
    SDR_TRRD                        0xfc
    SDR_TRTP                        0x100
    SDR_TWR                         0x104
    SDR_TWTR                        0x108
    SDR_TEXSR                       0x10c
    SDR_TXP                         0x110
    SDR_TXPDLL                      0x114
    SDR_TZQCS                       0x118
    SDR_TZQCSI                      0x11c
    SDR_TDQS                        0x120
    SDR_TCKSRE                      0x124
    SDR_TCKSRX                      0x128
    SDR_TCKE                        0x12c
    SDR_TMOD                        0x130
    SDR_TRSTL                       0x134
    SDR_TZQCL                       0x138
    SDR_TMRR                        0x13c
    SDR_TCKESR                      0x140
    SDR_TDPD                        0x144
    SDR_DTUWACTL                    0x200
    SDR_DTURACTL                    0x204
    SDR_DTUCFG                      0x208
    SDR_DTUECTL                     0x20c
    SDR_DTUWD0                      0x210
    SDR_DTUWD1                      0x214
    SDR_DTUWD2                      0x218
    SDR_DTUWD3                      0x21c
    SDR_DTUWDM                      0x220
    SDR_DTURD0                      0x224
    SDR_DTURD1                      0x224
    SDR_DTURD2                      0x22c
    SDR_DTURD3                      0x230
    SDR_DTULFSRWD                   0x234
    SDR_DTULFSRRD                   0x238
    SDR_DTUEAF                      0x23c
    SDR_DFITCTLDLY                  0x240
    SDR_DFIODTCFG                   0x244
    SDR_DFIODTCFG1                  0x248
    SDR_DFIODTRMAP                  0x24c
    SDR_DFITPHYWRD                  0x250
    SDR_DFITPHYWRL                  0x254
    SDR_DFITRDDEN                   0x260
    SDR_DFITPHYRDL                  0x264
    SDR_DFITPHYUPDTYPE0             0x270
    SDR_DFITPHYUPDTYPE1             0x274
    SDR_DFITPHYUPDTYPE2             0x278
    SDR_DFITPHYUPDTYPE3             0x27c
    SDR_DFITCTRLUPDMIN              0x280
    SDR_DFITCTRLUPDMAX              0x284
    SDR_DFITCTRLUPDDLY              0x288
    SDR_DFIUPDCFG                   0x290
    SDR_DFITREFMSKI                 0x294
    SDR_DFITCRLUPDI                 0x298
    SDR_DFITRCFG0                   0x2ac
    SDR_DFITRSTAT0                  0x2b0
    SDR_DFITRWRLVLEN                0x2b4
    SDR_DFITRRDLVLEN                0x2b8
    SDR_DFITRRDLVLGATEEN            0x2bc
    SDR_DFISTCFG0                   0x2c4
    SDR_DFISTCFG1                   0x2c8
    SDR_DFITDRAMCLKEN               0x2d0
    SDR_DFITDRAMCLKDIS              0x2d4
    SDR_DFILPCFG0                   0x2f0
    
[/code]
## PHY Registers
PHY registers, one set per channel 
[code] 
    MCTL_PHY0_BASE                  0x01c65000
    MCTL_PHY1_BASE                  0x01c66000
    
[/code]
[code] 
    SDR_PIR                         0x04
    SDR_PGCR                        0x08
    SDR_PGSR                        0x0c
    SDR_DLLGCR                      0x10
    SDR_ACDLLCR                     0x14
    SDR_PTR0                        0x18
    SDR_PTR1                        0x1c
    SDR_PTR2                        0x20
    SDR_ACIOCR                      0x24
    SDR_DXCCR                       0x28
    SDR_DSGCR                       0x2c
    SDR_DCR                         0x30
    SDR_DTPR0                       0x34
    SDR_DTPR1                       0x38
    SDR_DTPR2                       0x3c
    SDR_MR0                         0x40
    SDR_MR1                         0x44
    SDR_MR2                         0x48
    SDR_MR3                         0x4c
    SDR_ODTCR                       0x50
    SDR_DTAR                        0x54
    SDR_DTDT0                       0x58
    SDR_DTDT1                       0x5c
    SDR_DCUAR                       0xc0
    SDR_DCUDR                       0xc4
    SDR_DCURR                       0xc8
    SDR_DCULR                       0xcc
    SDR_DCUGCR                      0xd0
    SDR_DCUTPR                      0xd4
    SDR_DCUSR0                      0xd8
    SDR_DCUSR1                      0xdc
    SDR_BISTRR                      0x100
    SDR_BISTMSKR0                   0x104
    SDR_BISTMSKR1                   0x108
    SDR_BISTWCR                     0x10c
    SDR_BISTLSR                     0x110
    SDR_BISTAR0                     0x114
    SDR_BISTAR1                     0x118
    SDR_BISTAR2                     0x11c
    SDR_BISTUDPR                    0x120
    SDR_BISTGSR                     0x124
    SDR_BISTWER                     0x128
    SDR_BISTBER0                    0x12c
    SDR_BISTBER1                    0x130
    SDR_BISTBER2                    0x134
    SDR_BISTWCSR                    0x138
    SDR_BISTFWR0                    0x13c
    SDR_BISTFWR1                    0x140
    SDR_ZQ0CR0                      0x180
    SDR_ZQ0CR1                      0x184
    SDR_ZQ0SR0                      0x188
    SDR_ZQ0SR1                      0x18c
    SDR_DX0GCR                      0x1c0
    SDR_DX0GSR0                     0x1c4
    SDR_DX0GSR1                     0x1c8
    SDR_DX0DLLCR                    0x1cc
    SDR_DX0DQTR                     0x1d0
    SDR_DX0DQSTR                    0x1d4
    SDR_DX1GCR                      0x200
    SDR_DX1GSR0                     0x204
    SDR_DX1GSR1                     0x208
    SDR_DX1DLLCR                    0x20c
    SDR_DX1DQTR                     0x210
    SDR_DX1DQSTR                    0x214
    SDR_DX2GCR                      0x240
    SDR_DX2GSR0                     0x244
    SDR_DX2GSR1                     0x248
    SDR_DX2DLLCR                    0x24c
    SDR_DX2DQTR                     0x250
    SDR_DX2DQSTR                    0x254
    SDR_DX3GCR                      0x280
    SDR_DX3GSR0                     0x284
    SDR_DX3GSR1                     0x288
    SDR_DX3DLLCR                    0x28c
    SDR_DX3DQTR                     0x290
    SDR_DX3DQSTR                    0x294
    
[/code]
## Various other registers
Driver touches various other registers 
[code] 
    CCM_BASE                        (0x01c20000)
    CCM_PLL5_DDR_CTRL               (CCM_BASE+0x020)
    CCM_MDFS_CLK_CTRL               (CCM_BASE+0x0f0)
    CCM_DRAMCLK_CFG_CTRL            (CCM_BASE+0x0f4)
    CCM_AHB1_RST_REG0               (CCM_BASE+0x02C0)
    CCM_AHB1_GATE0_CTRL             (CCM_BASE+0x060)
    R_PRCM_BASE                     (0x01f01400)
    R_VDD_SYS_PWROFF_GATE           (R_PRCM_BASE + 0x110)
    CCM_AXI_GATE_CTRL               (CCM_BASE+0x05c)
    CCM_DRAM_GATING                 (CCM_BASE+0x100)
    
[/code]
## dram_para tpr fields
[code] 
    trefi = ((para->dram_tpr2)>>15)&0xFF;
    tmrd  = ((para->dram_tpr3)>>0)&0x7;
    trfc  = ((para->dram_tpr2)>>23)&0x1FF;
    trp   = ((para->dram_tpr3)>>3)&0xF;
    tprea = ((para->dram_tpr1)>>0)&0x3;
    trtw  = ((para->dram_tpr4)>>8)&0xF;
    tal   = ((para->dram_tpr4)>>4)&0xF;
    tcl   = ((para->dram_tpr4)>>0)&0xF;
    tcwl  = ((para->dram_tpr5)>>28)&0xF;
    tras  = ((para->dram_tpr3)>>19)&0x3F;
    trc   = ((para->dram_tpr3)>>13)&0x3F;
    trcd  = ((para->dram_tpr5)>>24)&0xF;
    trrd  = ((para->dram_tpr5)>>20)&0xF;
    trtp  = ((para->dram_tpr5)>>16)&0xF;
    twr   = ((para->dram_tpr5)>>11)&0x1F;
    twtr  = ((para->dram_tpr5)>>7)&0xF;
    texsr = ((para->dram_tpr1)>>22)&0x3FF;
    txp   = ((para->dram_tpr5)>>0)&0x7;
    txpdll= ((para->dram_tpr3)>>7)&0x3F;
    tzqcs = ((para->dram_tpr2)>>0)&0x7F;
    tzqcsi= (para->dram_tpr0);
    tdqs  = ((para->dram_tpr6)>>29)&0x7;
    tcksre= ((para->dram_tpr4)>>27)&0x1F;
    tcksrx= ((para->dram_tpr4)>>22)&0x1F;
    tcke  = ((para->dram_tpr4)>>17)&0x1F;
    tmod  = ((para->dram_tpr4)>>12)&0x1F;
    trstl = ((para->dram_tpr3)>>25)&0x7F;
    tzqcl = ((para->dram_tpr1)>>2)&0x3FF;
    tmrr  = ((para->dram_tpr2)>>7)&0xFF;
    tckesr= ((para->dram_tpr5)>>3)&0xF;
    tdpd  = ((para->dram_tpr1)>>12)&0x3FF;
    tccd    = ((para->dram_tpr6)>>6)&0x1;
    taond   = ((para->dram_tpr6)>>2)&0x3;
    tfaw    = ((para->dram_tpr6)>>13)&0x3F;
    trtodt  = ((para->dram_tpr6)>>5)&0x1;
    tdqsck  = ((para->dram_tpr6)>>10)&0x7;
    tdqsckmax = ((para->dram_tpr6)>>7)&0x7;
    tdllk   = ((para->dram_tpr6)>>19)&0x3FF;
    titmsrst= ((para->dram_tpr7)>>18)&0xF;
    tdlllock = ((para->dram_tpr7)>>6)&0xFFF;
    tdllsrst= ((para->dram_tpr7)>>0)&0x3F;
    tdinit0 = ((para->dram_tpr8)>>0)&0x7FFFF;
    tdinit1 = ((para->dram_tpr8)>>19)&0xFF;
    tdinit2 = ((para->dram_tpr9)>>0)&0x1FFFF;
    tdinit3 = ((para->dram_tpr9)>>17)&0x3FF;
    
[/code]
## registers
[code] 
    SDR_MR0         dram_mr0
    SDR_MR1         dram_mr1
    SDR_MR2         dram_mr2
    SDR_MR3         dram_mr3
    SDR_PTR0        titmsrst<<18 tdlllock<<6 tdllsrst<<0
    SDR_PTR1        tdinit1<<19 tdinit0<<0
    SDR_PTR2        tdinit3<<17 tdinit2<<0
    SDR_DTPR0       tccd<<31 tRC<<25 tRRD<<21 tRAS<<16 tRCD<<12 tRP<<8 tWTR<<5 tRTP<<2 tMRD<<0
    SDR_DTPR1       tDQSCKMAX<<27 tdqsck<<24 trfc<<16 trtodt<<11 (tmod-12)<<9 0<<2 tfaw<<3 taond<<0
    SDR_DTPR2       tdllk<<19 tcke<<15 txpdll<<10 texsr<<0
    SDR_DCR         DDR2=a DDR3=b LPDDR=8 other=C   PHY DDR Mode
    
[/code]
