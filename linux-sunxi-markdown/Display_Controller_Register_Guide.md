# Display Controller Register Guide
## Contents
  * [1 Display register guide][16983]
    * [1.1 Overview][16984]
    * [1.2 Sections][16985]
    * [1.3 FE Registers(Video FrontEnd)][16986]
    * [1.4 BE Registers(Video BackEnd)][16987]
    * [1.5 LCD Registers][16988]
    * [1.6 TVEC Registers][16989]
    * [1.7 HDMI Registers][16990]
      * [1.7.1 HDMI_INT_CTRL][16991]
      * [1.7.2 HDMI_CEC][16992]
    * [1.8 IEP Registers][16993]

# Display register guide
## Overview
Sunxi display registers are formed from 8-10 different register sets: BE0, BE1, FE0, FE1, LCD0, LCD1, TVEC0, TVEC1, HDMI and IEP. Display module also has dependencies to [CCMU], [SDRAM], [PIOC] and [PWM] registers 
## Sections
Section  | Subsection  | Address  | Size  | Description   
---|---|---|---|---  
**FE** | FE0  | `0x01e00000 - 0x01e0077f` | ?kiB  | Display Frontend0(Scaler layer)   
| FE1  | `0x01e20000 - 0x01e2077f` | ?kiB  | Display Frontend1   
**BE** | BE0  | `0x01e60000 - 0x01e657ff` | ?kiB  | Display Backend0(Color space converter layer)   
| BE1  | `0x01e40000 - 0x01e457ff` | ?kiB  | Display Backend1   
**LCD** | LCD0  | `0x01c0c000 - 0x01c0cfff` | ?kiB  |   
| LCD1  | `0x01c0d000 - 0x01c0dfff` | ?kiB  |   
**TVEC** | TVEC0  | `0x01c0a000 - 0x01c0afff` | ?kiB  |   
| TVEC1  | `0x01c1b000 - 0x01c1bfff` | ?kiB  |   
**HDMI** | HDMI  | `0x01c16000 - 0x01c165ff` | ?kiB  |   
**IEP** | IEP  | `0x01e70000 - 0x01e703ff` | ?kiB  | Only sun5i?   
## FE Registers(Video FrontEnd)
Base address: 0x01e00000 or 0x01e20000 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`modl_en` | `0x0000` | `4 B` | SCAL_EN_REG   
`frm_ctrl` | `0x0004` | `4 B` | SCAL_FRM_CTRL_REG   
`bypass` | `0x0008` | `4 B` | SCAL_BYPASS_REG   
`agth_sel` | `0x000C` | `4 B` | SCAL_AGTH_SEL_REG   
`lint_ctrl` | `0x0010` | `4 B` | SCAL_LINT_CTRL_REG   
`reserved` | `0x0014` | `12 B` |   
`buf_addr0` | `0x0020` | `4 B` | SCAL_BUF_ADDR0_REG   
`buf_addr1` | `0x0024` | `4 B` | SCAL_BUF_ADDR1_REG   
`buf_addr2` | `0x0028` | `4 B` | SCAL_BUF_ADDR2_REG   
`field_ctrl` | `0x002C` | `4 B` | SCAL_FIELD_CTRL_REG   
`mb_off0` | `0x0030` | `4 B` | SCAL_MB_OFF0_REG   
`mb_off1` | `0x0034` | `4 B` | SCAL_MB_OFF1_REG   
`mb_off2` | `0x0038` | `4 B` | SCAL_MB_OFF2_REG   
`reserved` | `0x003C` | `4 B` |   
`linestrd0` | `0x0040` | `4 B` | SCAL_LINESTRD0_REG   
`linestrd1` | `0x0044` | `4 B` | SCAL_LINESTRD1_REG   
`linestrd2` | `0x0048` | `4 B` | SCAL_LINESTRD2_REG   
`input_fmt` | `0x004C` | `4 B` | SCAL_INPUT_FMT_REG   
`wb_addr0` | `0x0050` | `4 B` | SCAL_WB_ADDR0_REG   
`wb_addr1` | `0x0054` | `4 B` | SCAL_WB_ADDR1_REG   
`wb_addr2` | `0x0058` | `4 B` | SCAL_WB_ADDR2_REG   
`output_fmt` | `0x005c` | `4 B` | SCAL_OUTPUT_FMT_REG   
`int_en` | `0x0060` | `4 B` | SCAL_INT_EN_REG   
`int_status` | `0x0064` | `4 B` | SCAL_INT_STATUS_REG   
`status` | `0x0068` | `4 B` | SCAL_STATUS_REG   
`reserved` | `0x006c` | `4 B` |   
`csc_coef` | `0x0070` | `48 B` | SCAL_CSC_COEF03_REG   
`di_ctrl` | `0x00a0` | `4 B` | SCAL_DI_CTRL_REG   
`di_diagintp` | `0x00a4` | `4 B` | SCAL_DI_DIAGINTP_REG   
`di_tempdiff` | `0x00a8` | `4 B` | SCAL_DI_TEMPDIFF_REG   
`di_sawtooth` | `0x00ac` | `4 B` | SCAL_DI_SAWTOOTH_REG   
`di_spatcomp` | `0x00b0` | `4 B` | SCAL_DI_SPATCOMP_REG   
`di_burstlen` | `0x00b4` | `4 B` | SCAL_DI_BURSTLEN_REG   
`di_preluma` | `0x00b8` | `4 B` | SCAL_DI_PRELUMA_REG   
`di_blkflag` | `0x00bc` | `4 B` | SCAL_DI_BLKFLAG_REG   
`di_flaglinestrd` | `0x00c0` | `4 B` | SCAL_DI_FLAGLINESTRD_REG   
`reserved` | `0x00c4` | `12 B` |   
`wb_linestrd_en` | `0x00d0` | `4 B` | SCAL_WB_LINESTRD_EN_REG   
`wb_linestrd0` | `0x00d4` | `4 B` | SCAL_WB_LINESTRD0_REG   
`wb_linestrd1` | `0x00d8` | `4 B` | SCAL_WB_LINESTRD1_REG   
`wb_linestrd2` | `0x00dc` | `4 B` | SCAL_WB_LINESTRD2_REG   
`trd_ctrl` | `0x00e0` | `4 B` | SCAL_3D_CTRL_REG   
`trd_buf_addr0` | `0x00e4` | `4 B` | SCAL_3D_BUF_ADDR0_REG   
`trd_buf_addr1` | `0x00e8` | `4 B` | SCAL_3D_BUF_ADDR1_REG   
`trd_buf_addr2` | `0x00ec` | `4 B` | SCAL_3D_BUF_ADDR2_REG   
`trd_mb_off0` | `0x00f0` | `4 B` | SCAL_3D_MB_OFF0_REG   
`trd_mb_off1` | `0x00f4` | `4 B` | SCAL_3D_MB_OFF1_REG   
`trd_mb_off2` | `0x00f8` | `4 B` | SCAL_3D_MB_OFF2_REG   
`reserved` | `0x00fc` | `4 B` |   
`ch0_insize` | `0x0100` | `4 B` | SCAL_CH0_INSIZE_REG   
`ch0_outsize` | `0x0104` | `4 B` | SCAL_CH0_OUTSIZE_REG   
`ch0_horzfact` | `0x0108` | `4 B` | SCAL_CH0_HORZFACT_REG   
`ch0_vertfact` | `0x010c` | `4 B` | SCAL_CH0_VERTFACT_REG   
`ch0_horzphase` | `0x0110` | `4 B` | SCAL_CH0_HORZPHASE_REG   
`ch0_vertphase0` | `0x0114` | `4 B` | SCAL_CH0_VERTPHASE0_REG   
`ch0_vertphase1` | `0x0118` | `4 B` | SCAL_CH0_VERTPHASE1_REG   
`reserved` | `0x011c` | `4 B` |   
`ch0_horztap0` | `0x0120` | `4 B` | SCAL_CH0_HORZTAP0_REG   
`ch0_horztap1` | `0x0124` | `4 B` | SCAL_CH0_HORZTAP1_REG   
`ch0_verttap` | `0x0128` | `4 B` | SCAL_CH0_VERTTAP_REG   
`reserved` | `0x012c` | `212 B` |   
`ch1_insize` | `0x0200` | `4 B` | SCAL_CH1_INSIZE_REG   
`ch1_outsize` | `0x0204` | `4 B` | SCAL_CH1_OUTSIZE_REG   
`ch1_horzfact` | `0x0208` | `4 B` | SCAL_CH1_HORZFACT_REG   
`ch1_vertfact` | `0x020c` | `4 B` | SCAL_CH1_VERTFACT_REG   
`ch1_horzphase` | `0x0210` | `4 B` | SCAL_CH1_HORZPHASE_REG   
`ch1_vertphase0` | `0x0214` | `4 B` | SCAL_CH1_VERTPHASE0_REG   
`ch1_vertphase1` | `0x0218` | `4 B` | SCAL_CH1_VERTPHASE1_REG   
`reserved` | `0x021c` | `4 B` |   
`ch1_horztap0` | `0x0220` | `4 B` | SCAL_CH1_HORZTAP0_REG   
`ch1_horztap1` | `0x0224` | `4 B` | SCAL_CH1_HORZTAP1_REG   
`ch1_verttap` | `0x0228` | `4 B` | SCAL_CH1_VERTTAP_REG   
`reserved` | `0x0228` | `468 B` |   
`ch0_horzcoef0` | `0x0400` | `128 B` | SCAL_CH0_HORZCOEF0_REGN   
`ch0_horzcoef1` | `0x0480` | `128 B` | SCAL_CH0_HORZCOEF1_REGN   
`ch0_vertcoef` | `0x0500` | `128 B` | SCAL_CH0_VERTCOEF_REGN   
`reserved` | `0x0580` | `128 B` |   
`ch1_horzcoef0` | `0x0600` | `128 B` | SCAL_CH1_HORZCOEF0_REGN   
`ch1_horzcoef1` | `0x0680` | `128 B` | SCAL_CH1_HORZCOEF1_REGN   
`ch1_vertcoef` | `0x0700` | `128 B` | SCAL_CH1_VERTCOEF_REGN   
`reserved??` | `0x0780` | `128 B` |   
`reserved` | `0x0800` | `512 B` |   
`vpp_en` | `0x0A00` | `4 B` | SCAL_VPP_EN_REG   
`vpp_dcti` | `0x0A04` | `4 B` | SCAL_VPP_DCTI_REG   
`vpp_lp1` | `0x0A08` | `4 B` | SCAL_VPP_LP1_REG   
`vpp_lp2` | `0x0A0c` | `4 B` | SCAL_VPP_LP2_REG   
`vpp_wle` | `0x0A10` | `4 B` | SCAL_VPP_WLE_REG   
`vpp_ble` | `0x0A14` | `4 B` | SCAL_VPP_BLE_REG   
## BE Registers(Video BackEnd)
Base address: 0x01e60000 or 0x01e40000 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`DE_BE_MODE_CTL` | `0x0800` | `4 B` | back-end mode control register   
`DE_BE_COLOR_CTL` | `0x0804` | `4 B` | back-end color control register   
`DE_BE_DISP_SIZE` | `0x0808` | `4 B` | back-end display size setting register   
`DE_BE_ERROR_CORRECTION` | `0x080C` | `4 B` |   
`DE_BE_LAYER_SIZE` | `0x0810` | `16? B` | back-end layer size register   
`DE_BE_LAYER_CRD_CTL` | `0x0820` | `32? B` | back-end layer coordinate control register   
`DE_BE_FRMBUF_WLINE` | `0x0840` | `16? B` | back-end frame buffer line width register   
`DE_BE_FRMBUF_LOW32ADDR` | `0x0850` | `16? B` | back-end frame buffer low 32bit address register   
`DE_BE_FRMBUF_HIGH4ADDR` | `0x0860` | `16? B` | back-end frame buffer high 4bit address register   
`DE_BE_FRMBUF_CTL` | `0x0870` | `16? B` | back-end frame buffer control register   
`DE_BE_CLRKEY_MAX` | `0x0880` | `8? B` | back-end color key max register   
`DE_BE_CLRKEY_CFG` | `0x0888` | `8? B` | back-end color key configuration register   
`DE_BE_LAYER_ATTRCTL_OFF0` | `0x0890` | `16? B` | back-end layer attribute control register0   
`DE_BE_LAYER_ATTRCTL_OFF1` | `0x08a0` | `16? B` | back-end layer attribute control register1   
`DE_BE_DLCDP_CTL` | `0x08b0` | `4 B` | direct lcd pipe control register   
`DE_BE_DLCDP_FRMBUF_ADDRCTL` | `0x08b4` | `4 B` | direct lcd pipe frame buffer address control register   
`DE_BE_DLCDP_CRD_CTL_OFF0` | `0x08b8` | `4 B` | direct lcd pipe coordinate control register0   
`DE_BE_DLCDP_CRD_CTL_OFF1` | `0x08bc` | `4 B` | direct lcd pipe coordinate control register1   
`DE_BE_INT_EN` | `0x08c0` | `4 B` |   
`DE_BE_INT_FLAG` | `0x08c4` | `? B` |   
`DE_BE_HWC_CRD_CTL` | `0x08d8` | `? B` | hardware cursor coordinate control register   
`DE_BE_HWC_FRMBUF` | `0x08e0` | `16? B` | hardware cursor framebuffer control   
`DE_BE_WB_CTRL` | `0x08f0` | `4 B` | back-end write back control   
`DE_BE_WB_ADDR` | `0x08f4` | `4 B` | back-end write back address   
`DE_BE_WB_LINE_WIDTH` | `0x08f8` | `4 B` | back-end write back buffer line width   
`DE_BE_SPRITE_EN` | `0x0900` | `8? B` | sprite enable   
`DE_BE_SPRITE_FORMAT_CTRL` | `0x0908` | `8? B` | sprite format control   
`DE_BE_SPRITE_ALPHA_CTRL` | `0x090c` | `? B` | sprite alpha control   
`DE_BE_SPRITE_POS_CTRL` | `0x0a00` | `? B` | sprite single block coordinate control   
`DE_BE_SPRITE_ATTR_CTRL` | `0x0b00` | `? B` | sprite single block attribute control   
`DE_BE_SPRITE_ADDR` | `0x0c00` | `? B` | sprite single block address setting SRAM array   
`DE_BE_SPRITE_LINE_WIDTH` | `0x0d00` | `? B` | sprite single block address setting SRAM array   
`DE_BE_YUV_CTRL` | `0x0920` | `? B` | back-end input YUV channel control   
`DE_BE_YUV_ADDR` | `0x0930` | `? B` | back-end YUV channel frame buffer address   
`DE_BE_YUV_LINE_WIDTH` | `0x0940` | `? B` | back-end YUV channel buffer line width   
`DE_BE_YG_COEFF` | `0x0950` | `? B` | back Y/G coefficient   
`DE_BE_YG_CONSTANT` | `0x095c` | `4 B` | back Y/G constant   
`DE_BE_UR_COEFF` | `0x0960` | `? B` | back U/R coefficient   
`DE_BE_UR_CONSTANT` | `0x096c` | `4 B` | back U/R constant   
`DE_BE_VB_COEFF` | `0x0970` | `? B` | back V/B coefficient   
`DE_BE_VB_CONSTANT` | `0x097c` | `? B` | back V/B constant   
`DE_BE_OUT_COLOR_CTRL` | `0x09c0` | `? B` |   
`DE_BE_OUT_COLOR_R_COEFF` | `0x09d0` | `? B` |   
`DE_BE_OUT_COLOR_R_CONSTANT` | `0x09dc` | `? B` |   
`DE_BE_OUT_COLOR_G_COEFF` | `0x09e0` | `? B` |   
`DE_BE_OUT_COLOR_G_CONSTANT` | `0x09ec` | `? B` |   
`DE_BE_OUT_COLOR_B_COEFF` | `0x09f0` | `? B` |   
`DE_BE_OUT_COLOR_B_CONSTANT` | `0x09fc` | `? B` |   
`DE_BE_SPRITE_PALETTE_TABLE_ADDR` | `0x4000` | `1024 B` |   
`DE_BE_GAMMA_TABLE_ADDR` | `0x4400` | `1024 B` | Used as internal framebuffer when layer attributes are set accordingly   
`DE_BE_HWC_MEMORY_ADDR` | `0x4800` | `1024 B` |   
`DE_BE_HWC_PALETTE_TABLE_ADDR` | `0x4c00` | `1024 B` |   
`DE_BE_INTER_PALETTE_TABLE_PIPE0_ADDR` | `0x5000` | `1024 B` |   
`DE_BE_INTER_PALETTE_TABLE_PIPE1_ADDR` | `0x5400` | `1024 B` |   
## LCD Registers
Base address: 0x01c0c000 or 0x01c0d000 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`LCDC_GCTL` | `0x0000` | `4 B` | global control registers   
`LCDC_GINT0` | `0x0004` | `4 B` | interrupt registers   
`LCDC_GINT1` | `0x0008` | `4? B` | interrupt registers   
`LCDC_FRM0` | `0x0010` | `4 B` | frm registers   
`LCDC_FRM1` | `0x0014` | `? B` | frm registers   
`LCDC_FRM2` | `0x002c` | `? B` | frm registers   
`LCDC_CTL` | `0x0040` | `4 B` | control registers   
`LCDC_DCLK` | `0x0044` | `4 B` | dot clock registers   
`LCDC_BASIC0` | `0x0048` | `4 B` | base0 registers   
`LCDC_BASIC1` | `0x004c` | `4 B` | base1 registers   
`LCDC_BASIC2` | `0x0050` | `4 B` | base2 registers   
`LCDC_BASIC3` | `0x0054` | `4 B` | base3 registers   
`LCDC_HVIF` | `0x0058` | `? B` | hv interface registers   
`LCDC_CPUIF` | `0x0060` | `4 B` | cpu interface registers   
`LCDC_CPUWR` | `0x0064` | `4 B` | cpu wr registers   
`LCDC_CPURD` | `0x0068` | `4 B` | cpu rd registers   
`LCDC_CPURDNX` | `0x006c` | `4 B` | cpu rdnx registers   
`LCDC_TTL0` | `0x0070` | `4 B` | TTL0 registers   
`LCDC_TTL1` | `0x0074` | `4 B` | TTL1 registers   
`LCDC_TTL2` | `0x0078` | `4 B` | TTL2 registers   
`LCDC_TTL3` | `0x007c` | `4 B` | TTL3 registers   
`LCDC_TTL4` | `0x0080` | `4 B` | TTL4 registers   
`LCDC_LVDS` | `0x0084` | `4 B` | LVDS registers   
`LCDC_IOCTL0` | `0x0088` | `4 B` | io control0 registers   
`LCDC_IOCTL1` | `0x008c` | `4 B` | io control1 registers   
`LCDC_HDTVIF` | `0x0090` | `4 B` | tv interface registers   
`LCDC_HDTV0` | `0x0094` | `4 B` | HDTV0 registers   
`LCDC_HDTV1` | `0x0098` | `4 B` | HDTV1 registers   
`LCDC_HDTV2` | `0x009c` | `4 B` | HDTV2 registers   
`LCDC_HDTV3` | `0x00a0` | `4 B` | HDTV3 registers   
`LCDC_HDTV4` | `0x00a4` | `4 B` | HDTV4 registers   
`LCDC_HDTV5` | `0x00a8` | `? B` | HDTV5 registers   
`LCDC_IOCTL2` | `0x00f0` | `4 B` | io control2 registers   
`LCDC_IOCTL3` | `0x00f4` | `? B` | io control3 registers   
`LCDC_DUBUG` | `0x00fc` | `? B` | debug register   
`LCDC_CEU` | `0x0100` | `? B` |   
`LCDC_MUX_CTRL` | `0x0200` | `? B` |   
`LCDC_LVDS_ANA0` | `0x0220` | `4 B` |   
`LCDC_LVDS_ANA1` | `0x0224` | `? B` |   
`LCDC_3DF_CTL` | `0x0300` | `4 B` |   
`LCDC_3DF_A1B` | `0x0304` | `4 B` |   
`LCDC_3DF_A1E` | `0x0308` | `4 B` |   
`LCDC_3DF_D1` | `0x030c` | `4 B` |   
`LCDC_3DF_A2B` | `0x0310` | `4 B` |   
`LCDC_3DF_A2E` | `0x0314` | `4 B` |   
`LCDC_3DF_D2` | `0x0318` | `4 B` |   
`LCDC_3DF_A3B` | `0x031c` | `4 B` |   
`LCDC_3DF_A3E` | `0x0320` | `4 B` |   
`LCDC_3DF_D3` | `0x0318??` | `? B` |   
`LCDC_GAMMA_TABLE` | `0x0400` | `? B` |   
## TVEC Registers
Base address: 0x01c0a000 or 0x01c1b000 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`TVE_000` | `0x0000` | `4 B` |   
`TVE_004` | `0x0004` | `4 B` |   
`TVE_008` | `0x0008` | `4 B` |   
`TVE_00C` | `0x000C` | `4 B` |   
`TVE_010` | `0x0010` | `4 B` |   
`TVE_014` | `0x0014` | `4 B` |   
`TVE_018` | `0x0018` | `4 B` |   
`TVE_01C` | `0x001c` | `4 B` |   
`TVE_020` | `0x0020` | `4 B` |   
`TVE_024` | `0x0024` | `4 B` |   
`TVE_030` | `0x0030` | `4 B` |   
`TVE_034` | `0x0034` | `4 B` |   
`TVE_038` | `0x0038` | `4 B` |   
`TVE_03C` | `0x003c` | `4 B` |   
`TVE_040` | `0x0040` | `4 B` |   
`TVE_044` | `0x0044` | `4 B` |   
`TVE_048` | `0x0048` | `4 B` |   
`TVE_04C` | `0x004c` | `4 B` |   
`TVE_100` | `0x0100` | `4 B` |   
`TVE_104` | `0x0104` | `4 B` |   
`TVE_10C` | `0x010c` | `4 B` |   
`TVE_110` | `0x0110` | `4 B` |   
`TVE_114` | `0x0114` | `4 B` |   
`TVE_118` | `0x0118` | `4 B` |   
`TVE_11C` | `0x011c` | `4 B` |   
`TVE_124` | `0x0124` | `4 B` |   
`TVE_128` | `0x0128` | `4 B` |   
`TVE_12C` | `0x012c` | `4 B` |   
`TVE_130` | `0x0130` | `4 B` |   
`TVE_138` | `0x0138` | `4 B` |   
`TVE_13C` | `0x013c` | `4 B` |   
## HDMI Registers
Base address: 0x01c16000 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`` | `0x000` | `4 B` | ???   
`HDMI_CTRL` | `0x004` | `4 B` | Ctrl   
`HDMI_INT_CTRL` | `0x008` | `4 B` |   
`HDMI_HPD` | `0x00c` | `4 B` |   
`HDMI_VIDEO_CTRL` | `0x010` | `4 B` | Video ctrl   
`HDMI_VIDEO_H` | `0x014` | `2 B` | Horizontal visible resolution   
`HDMI_VIDEO_V` | `0x016` | `2 B` |   
`HDMI_VIDEO_HBP` | `0x018` | `2 B` | length of horizontal sync + time from sync to picture   
`HDMI_VIDEO_VBP` | `0x01a` | `2 B` |   
`HDMI_VIDEO_HFP` | `0x01c` | `2 B` | time from picture to sync   
`HDMI_VIDEO_VFP` | `0x01e` | `2 B` |   
`HDMI_VIDEO_HSPW` | `0x020` | `2 B` | length of horizontal sync   
`HDMI_VIDEO_VPSW` | `0x022` | `2 B` |   
`HDMI_VIDEO_POLARITY` | `0x024` | `2 B` | Vsync/Hsync polarity   
`HDMI_TX_CLOCK` | `0x026` | `2 B?` | TX clock sequence   
`HDMI_AUDIO_CTRL` | `0x040` | `4 B` | Audio ctrl   
`` | `0x044` | `4 B` |   
`` | `0x048` | `4 B` |   
`` | `0x04c` | `4 B` |   
`` | `0x050` | `4 B` |   
`` | `0x054` | `4 B` |   
`` | `0x058` | `4 B` |   
`` | `0x05c` | `4 B` |   
`HDMI_AVI_INFOFRAME` | `0x080` | `16 B` |   
`HDMI_AUDIO_INFOFRAME` | `0x0a0` | `13? B` |   
`` | `0x0e0` | `8? B` | QCP packet   
`` | `0x200` | `4 B` | Tx driver   
`` | `0x204` | `4 B` | Tx driver   
`` | `0x208` | `4 B` | Tx driver   
`` | `0x20c` | `4 B` |   
`HDMI_CEC` | `0x214` | `4 B` |   
`HDMI_VENDOR_INFOFRAME` | `0x240` | `? B` |   
`` | `0x300` | `? B` |   
`HDMI_I2C_GENERAL` | `0x500` | `4 B` | I2C   
`HDMI_I2C_ADDR` | `0x504` | `4? B` | I2C   
`HDMI_I2C_STATUS` | `0x50c` | `4? B` | I2C   
`` | `0x510` | `4? B` | I2C   
`HDMI_I2C_DATA` | `0x518` | `4 B` | I2C   
`HDMI_I2C_DATA_LENGTH` | `0x51c` | `4 B` | I2C   
`HDMI_I2C_CMD` | `0x520` | `4 B` | I2C   
`` | `0x524` | `4 B` | I2C   
`HDMI_I2C_CLK` | `0x528` | `4? B` | I2C   
`HDMI_I2C_LINE_CTRL` | `0x540` | `4? B` | I2C   
`` | `0x5f0` | `? B` |   
  

##### HDMI_INT_CTRL
Default value: Unknown  
Offset: 0x04 
Bit  | Read/Write  | Default (Hex)  | Description   
---|---|---|---  
`0:3` | `Read/Write` | `Unknown` | ` `
[code]
       Interrupt flag?
      
    
[/code]  
`15:18` | `Write` | `Unknown` | ` `
[code]
       Interrupt enable?
      
    
[/code]  
  

##### HDMI_CEC
Default value: Unknown  
Offset: 0x214 
The register is called HPD_CEC in A20 manual 
Bit | Read/Write | Default | description   
---|---|---|---  
31:12 | / | / | reserved   
11 | Read/Write | 0 | REG_CEC_EN   
10 | Read/Write | 0 | REG_CECPS   
9 | Read/Write | 0 | W_CEC   
8 | Read | / | R_CEC   
7:4 | / | / | reserved   
3 | Read/Write | 0 | REG_HPD_EN   
2 | Read/Write | 0 | REG_HPDPD   
1 | Read/Write | 0 | W_HPD   
0 | Read | / | R_HPD   
## IEP Registers
Base address: 0x01e70000 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`gnectl` | `0x0000` | `4 B` | __imgehc_gnectl_reg_t   
`drcsize` | `0x0004` | `4 B` | __imgehc_drcsize_reg_t   
`reserved` | `0x0008` | `8 B` |   
`drcctl` | `0x0010` | `4 B` | __imgehc_drcctl_reg_t   
`drclgc_addr` | `0x0014` | `4 B` | __imgehc_drclgc_staadd_reg_t   
`drc_set` | `0x0018` | `4 B` | __imgehc_drc_set_reg_t   
`drc_wp0` | `0x001c` | `4 B` | __imgehc_drc_wp_reg0_t   
`drc_wp1` | `0x0020` | `4 B` | __imgehc_drc_wp_reg1_t   
`wbctl` | `0x0024` | `4 B` | __imgehc_wbctl_reg_t   
`wbaddr` | `0x0028` | `4 B` | __imgehc_wbaddr_reg_t   
`wbline` | `0x002c` | `4 B` | __imgehc_wbline_reg_t   
`lhctl` | `0x0030` | `4 B` | __imgehc_lhctl_reg_t   
`lhthr0` | `0x0034` | `4 B` | __imgehc_lhthr_reg0_t   
`lhthr1` | `0x0038` | `4 B` | __imgehc_lhthr_reg1_t   
`reserved` | `0x003c` | `4 B` |   
`lhslum` | `0x0040` | `32 B` | __imgehc_lhslum_reg_t   
`lhscnt` | `0x0060` | `32 B` | __imgehc_lhscnt_reg_t   
`dfctl` | `0x0080` | `4 B` | __imgehc_dfctl_reg_t   
`reserved` | `0x0084` | `60 B` |   
`cscygcoff` | `0x00c0` | `12 B` | __imgehc_cscygcoff_reg_t   
`cscygcon` | `0x00cc` | `4 B` | __imgehc_cscygcon_reg_t   
`cscurcoff` | `0x00d0` | `12 B` | __imgehc_cscurcoff_reg_t   
`cscurcon` | `0x00dc` | `4 B` | __imgehc_cscurcon_reg_t   
`cscvbcoff` | `0x00e0` | `12 B` | __imgehc_cscvbcoff_reg_t   
`cscvbcon` | `0x00ec` | `4 B` | __imgehc_cscvbcon_reg_t   
`drcspacoff` | `0x00f0` | `12 B` | __imgehc_drcspacoff_reg_t   
`reserved` | `0x00ff` | `4 B` |   
`drcintcoff` | `0x0100` | `256 B` | __imgehc_drcintcoff_reg_t   
`drclgcoff` | `0x0200` | `512 B` | __imgehc_drclgcoff_reg_t
