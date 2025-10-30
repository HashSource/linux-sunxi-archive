# VE Register guide
# Video Engine Registers
Base address: 
  * `0x01c0e000` \- [A10][58143], [A13][58144], [A20][58145], [sun8iw1p1][58146], [sun8iw3p1][58147], [sun8iw5p1][58148], [sun8iw6p1][58149], [sun8iw7p1][58150], [sun8iw8p1][58151], [sun8iw9p1][58152]
  * `0x03a40000` \- [sun9iw1p1][58153]

  
[General Registers][58154]  
[MPEG Engine Registers][58155]  
[H264 Engine Registers][58156]  
[VC1 Engine Registers][58157]  
[RMVB Engine Registers][58158]  
[HEVC Engine Registers][58159]  
[ISP Engine Registers][58160]  
[AVC Encoder Engine Registers][58161]  

## General Registers
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[MACC_VE_CTRL][58162]` | `0x0000` | `4B` | `Sub-Engine Select and RAM type select`  
`[MACC_VE_RESET][58163]` | `0x0004` | `4B` | `Sub-Engines Reset`  
`[MACC_VE_CYCLES_COUNTER][58164]` | `0x0008` | `4B` | `Clock Cycles counter`  
`[MACC_VE_TIMEOUT][58165]` | `0x000c` | `4B` | `VE Timeout value`  
`[MACC_VE_MMCREQ_WNUM][58166]` | `0x0010` | `4B` | ``  
`[MACC_VE_CACHEREG_WNUM][58167]` | `0x0014` | `4B` | ``  
`[MACC_VE_STATUS][58168]` | `0x001c` | `4B` | `Busy status`  
`[MACC_VE_RDDATA_COUNTER][58169]` | `0x0020` | `4B` | `DRAM Read counter`  
`[MACC_VE_WRDATA_COUNTER][58170]` | `0x0024` | `4B` | `DRAM Write counter`  
`[MACC_VE_ANAGLYPH_CTRL][58171]` | `0x0028` | `4B` | `Anaglyph mode control`  
`[MACC_VE_MAF_CTRL][58172]` | `0x0030` | `4B` | `Motion adaptive filter config`  
`[MACC_VE_MAF_CLIP_TH][58173]` | `0x0034` | `4B` | ``  
`[MACC_VE_MAFREF1_LUMA_BUF][58174]` | `0x0038` | `4B` | `Reference luma buffer {unsure}`  
`[MACC_VE_MAFREF1_CHROMA_BUF][58175]` | `0x003c` | `4B` | `Reference chroma buffer {unsure}`  
`[MACC_VE_MAFCUR_ADDR][58176]` | `0x0040` | `4B` | `current maf output address {unsure}`  
`[MACC_VE_MAFREF1_ADDR][58177]` | `0x0044` | `4B` | `reference maf input address {unsure}`  
`[MACC_VE_MAFREF2_ADDR][58178]` | `0x0048` | `4B` | `second reference maf input address {unsure}`  
`[MACC_VE_MAFDIFF_GROUP_MAX][58179]` | `0x004c` | `4B` | ``  
`[MACC_VE_IPD_DBLK_BUF_CTRL][58180]` | `0x0050` | `4B` | `deblocking and intra prediction dram buffer config register (required for A13+ SoC for H264 decoding or on A10 for video with width >= 2048)`  
`[MACC_VE_IPD_BUF][58181]` | `0x0054` | `4B` | `Intra prediction buffer (needed on A13+ or (width >= 2048))`  
`[MACC_VE_DBLK_BUF][58182]` | `0x0058` | `4B` | `Deblocking buffer (needed on A13+ or (width >= 2048))`  
`[MACC_VE_ARGB_QUEUE_START][58183]` | `0x005c` | `4B` | `ARGB command queue`  
`[MACC_VE_ARGB_BLK_SRC1_ADDR][58184]` | `0x0060` | `4B` | `ARGB source 1 address`  
`[MACC_VE_ARGB_BLK_SRC2_ADDR][58185]` | `0x0064` | `4B` | `ARGB source 2 addres`  
`[MACC_VE_ARGB_BLK_DST_ADDR][58186]` | `0x0068` | `4B` | `ARGB destination address`  
`[MACC_VE_ARGB_SRC_STRIDE][58187]` | `0x006c` | `4B` | `ARGB source strides for src1 and src2`  
`[MACC_VE_ARGB_DST_STRIDE][58188]` | `0x0070` | `4B` | `ARGB destination stride`  
`[MACC_VE_ARGB_BLK_SIZE][58189]` | `0x0074` | `4B` | `ARGB size`  
`[MACC_VE_ARGB_BLK_FILL_VALUE][58190]` | `0x0078` | `4B` | `ARGB fill value`  
`[MACC_VE_ARGB_BLK_CTRL][58191]` | `0x007c` | `4B` | `ARGB control`  
`[MACC_VE_LUMA_HIST_THR[0-3]][58192]` | `0x0080 - 0x008c` | `4B` | `Luma histogram thresholds`  
`[MACC_VE_LUMA_HIST_VAL[0-15]][58193]` | `0x0090 - 0x00cc` | `4B` | `Luma histogram output values`  
`[MACC_VE_OUTPUT_CHROMA_OFFSET][58194]` | `0x00c4` | `4B` | `Offset of chroma second chroma plane _(since H3?)_`  
`[MACC_VE_OUTPUT_STRIDE][58195]` | `0x00c8` | `4B` | `Output line stride length _(since H3?)_`  
`[MACC_VE_EXTRA_OUT_STRIDE][58196]` | `0x00cc` | `4B` | `Extra output line stride length _(since H3?)_`  
`[MACC_VE_ANGL_R_BUF][58197]` | `0x00d0` | `4B` | `Anaglyph red output buffer`  
`[MACC_VE_ANGL_G_BUF][58198]` | `0x00d4` | `4B` | `Anaglyph green output buffer`  
`[MACC_VE_ANGL_B_BUF][58199]` | `0x00d8` | `4B` | `Anaglyph blue output buffer`  
`[MACC_VE_EXTRA_OUT_FMT_OFFSET][58200]` | `0x00e8` | `4B` | `Extra output format and chroma offset _(not available on A10/A13/A20)_`  
`[MACC_VE_OUTPUT_FORMAT][58201]` | `0x00ec` | `4B` | `Output formats _(since H3?)_`  
`[MACC_VE_VERSION][58202]` | `0x00f0` | `4B` | `IP Version register`  
`[MACC_VE_DBG_CTRL][58203]` | `0x00f8` | `4B` | `Debug control`  
`[MACC_VE_DBG_OUTPUT][58204]` | `0x00fc` | `4B` | `Debug output`  
## MPEG Engine Registers
Base address: 0x01c0e100  
Used by engine 0x0 (MPEG) 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[MACC_MPEG_PHDR][58205]` | `0x0100` | `4B` | `MPEG12 Picture Header register`  
`[MACC_MPEG_VOPHDR][58206]` | `0x0104` | `4B` | `MPEG Video Object Plane Header register (MPEG4 Header)`  
`[MACC_MPEG_SIZE][58207]` | `0x0108` | `4B` | `Frame size in MPEG macroblocks (16x16)`  
`[MACC_MPEG_FRAME_SIZE][58208]` | `0x010c` | `4B` | `Frame size in pixels `  
`[MACC_MPEG_MBA][58209]` | `0x0110` | `4B` | `MPEG Macro Block Address register`  
`[MACC_MPEG_CTRL][58210]` | `0x0114` | `4B` | `MPEG Control Register`  
`[MACC_MPEG_TRIG][58211]` | `0x0118` | `4B` | `MPEG Decoding Trigger`  
`[MACC_MPEG_STATUS][58212]` | `0x011c` | `4B` | `MACC MPEG Status register`  
`[MACC_MPEG_FRAME_DIST][58213]` | `0x0120` | `4B` | `MPEG P and B Frame distance`  
`[MACC_MPEG_TRBTRDFLD][58214]` | `0x0124` | `4B` | `Temporal References(TRB(B-VOP) and TRD)`  
`[MACC_MPEG_VLD_ADDR][58215]` | `0x0128` | `4B` | `MPEG Variable Length Decoding Address`  
`[MACC_MPEG_VLD_OFFSET][58216]` | `0x012c` | `4B` | `MPEG Variable Length Decoding Offset`  
`[MACC_MPEG_VLD_LEN][58217]` | `0x0130` | `4B` | `MPEG Variable Length Decoding Length`  
`[MACC_MPEG_VBV_END][58218]` | `0x0134` | `4B` | `MPEG VBV end - video source buffer end`  
`[MACC_MPEG_MBH_ADDR][58219]` | `0x0138` | `4B` | `MBH buffer address`  
`[MACC_MPEG_DCAC_ADDR][58220]` | `0x013c` | `4B` | `DCAC Buffer address`  
`[MACC_MPEG_BLK_OFFSET][58221]` | `0x0140` | `4B` | `MPEG Block address???`  
`[MACC_MPEG_NCF_ADDR][58222]` | `0x0144` | `4B` | `NFC buffer address`  
`[MACC_MPEG_REC_LUMA][58223]` | `0x0148` | `4B` | `MPEG Luma reconstruct buffer`  
`[MACC_MPEG_REC_CHROMA][58224]` | `0x014c` | `4B` | `MPEG Chroma reconstruct buffer`  
`[MACC_MPEG_FWD_LUMA][58225]` | `0x0150` | `4B` | `MPEG Luma forward buffer`  
`[MACC_MPEG_FWD_CHROMA][58226]` | `0x0154` | `4B` | `MPEG forward buffer`  
`[MACC_MPEG_BACK_LUMA][58227]` | `0x0158` | `4B` | `MPEG Luma Back buffer`  
`[MACC_MPEG_BACK_CHROMA][58228]` | `0x015c` | `4B` | `MPEG Chroma Back buffer`  
`[MACC_MPEG_SOCX][58229]` | `0x0160` | `4B` | `MS-MPEG related`  
`[MACC_MPEG_SOCY][58230]` | `0x0164` | `4B` | `MS-MPEG related`  
`[MACC_MPEG_SOL][58231]` | `0x0168` | `4B` | `MS-MPEG related`  
`[MACC_MPEG_SDLX][58232]` | `0x016c` | `4B` | `MS-MPEG related`  
`[MACC_MPEG_SDLY][58233]` | `0x0170` | `4B` | `MS-MPEG related`  
`[MACC_MPEG_SPRITESHFT][58234]` | `0x0174` | `4B` | `MS-MPEG related`  
`[MACC_MPEG_SDCX][58235]` | `0x0178` | `4B` | `MS-MPEG related`  
`[MACC_MPEG_SDCY][58236]` | `0x017c` | `4B` | `MS-MPEG related`  
`[MACC_MPEG_IQ_MIN_INPUT][58237]` | `0x0180` | `4B` | `MPEG Inverse Quantization minimum input level`  
`[MACC_MPEG_IQ_INPUT][58238]` | `0x0184` | `4B` | `MPEG Inverse Quantization input level`  
`[MACC_MPEG_MSMPEG4_HDR][58239]` | `0x0188` | `4B` | `MPEG MS-Mpeg-4 header`  
`[MACC_MPEG_VP6_HDR][58240]` | `0x018c` | `4B` | `MPEG VP6 Header`  
`[MACC_MPEG_IQ_IDCT_INPUT][58241]` | `0x0190` | `4B` | `MPEG Inverse Quantization and Inverse Discrete Cosine Transform input`  
`[MACC_MPEG_MB_HEIGHT][58242]` | `0x0194` | `4B` | `MPEG Macro Block Height`  
`[MACC_MPEG_MB_V1][58243]` | `0x0198` | `4B` | `MPEG Macro Block Vector 1`  
`[MACC_MPEG_MB_V2][58244]` | `0x019c` | `4B` | `MPEG Macro Block Vector 2`  
`[MACC_MPEG_MB_V3][58245]` | `0x01a0` | `4B` | `MPEG Macro Block Vector 3`  
`[MACC_MPEG_MB_V4][58246]` | `0x01a4` | `4B` | `MPEG Macro Block Vector 4`  
`[MACC_MPEG_MB_V5][58247]` | `0x01a8` | `4B` | `MPEG Macro Block Vector 5`  
`[MACC_MPEG_MB_V6][58248]` | `0x01ac` | `4B` | `MPEG Macro Block Vector 6`  
`[MACC_MPEG_MB_V7][58249]` | `0x01b0` | `4B` | `MPEG Macro Block Vector 7`  
`[MACC_MPEG_MB_V8][58250]` | `0x01b4` | `4B` | `MPEG Macro Block Vector 8`  
`[MACC_MPEG_JPEG_SIZE][58251]` | `0x01b8` | `4B` | `JPEG Size`  
`[MACC_MPEG_JPEG_MCU][58252]` | `0x01bc` | `4B` | `JPEG Minimum Coded Unit`  
`[MACC_MPEG_JPEG_RES_INT][58253]` | `0x01c0` | `4B` | `JPEG Restart Interval`  
`[MACC_MPEG_ERROR][58254]` | `0x01c4` | `4B` | `MPEG Error flags`  
`[MACC_MPEG_CTR_MB][58255]` | `0x01c8` | `4B` | `(Macroblock Control??)`  
`[MACC_MPEG_ROT_LUMA][58256]` | `0x01cc` | `4B` | `MPEG Rotate-Scale Luma buffer`  
`[MACC_MPEG_ROT_CHROMA][58257]` | `0x01d0` | `4B` | `MPEG Rotate-Scale Chroma buffer`  
`[MACC_MPEG_ROTSCALE_CTRL][58258]` | `0x01d4` | `4B` | `Control Rotate/Scale Buffer`  
`[MACC_MPEG_JPEG_MCU_START][58259]` | `0x01d8` | `4B` | `JPEG Macro Cell Unit Start`  
`[MACC_MPEG_JPEG_MCU_END][58260]` | `0x01dc` | `4B` | `JPEG Macro Cell Unit End`  
`[MACC_MPEG_SRAM_RW_OFFSET][58261]` | `0x01e0` | `4B` | `Auto incremental pointer for read/write VE SRAM`  
`[MACC_MPEG_SRAM_RW_DATA][58262]` | `0x01e4` | `4B` | `FIFO Like Data register for write/read VE SRAM`  
`[MACC_MPEG_START_CODE_BITOFFSET][58263]` | `0x01f0` | `4B` | `MPEG start code search result`  
## H264 Engine Registers
Base address: 0x01c0e200  
Used by engine 0x1 (H264) 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[MACC_H264_SEQ_HDR][58264]` | `0x0200` | `4B` | `H264 Sequence header`  
`[MACC_H264_PIC_HDR][58265]` | `0x0204` | `4B` | `H264 Picture header`  
`[MACC_H264_SLICE_HDR][58266]` | `0x0208` | `4B` | `H264 Slice header`  
`[MACC_H264_SLICE_HDR2][58267]` | `0x020c` | `4B` | `H264 Slice header`  
`[MACC_H264_PRED_WEIGHT][58268]` | `0x0210` | `4B` | `H264 weighted prediction parameters`  
`[MACC_H264_VP8_HDR][58269]` | `0x0214` | `4B` | `H264 VP8 Picture header`  
`[MACC_H264_QINDEX][58270]` | `0x0218` | `4B` | `H264 Quantizer settings (VP8)`  
`[MACC_H264_VP8_PART_OFFSET][58271] ``[MACC_H264_QP][58272]` | `0x021c` | `4B` | `H264 QP parameters (VP8 partition offset)`  
`[MACC_H264_CTRL][58273]` | `0x0220` | `4B` | `H264 Control Register`  
`[MACC_H264_TRIG][58274]` | `0x0224` | `4B` | `H264 Trigger Register`  
`[MACC_H264_STATUS][58275]` | `0x0228` | `4B` | `H264 Status Register`  
`[MACC_H264_CUR_MBNUM][58276]` | `0x022c` | `4B` | `H264 current Macroblock`  
`[MACC_H264_VLD_ADDR][58277]` | `0x0230` | `4B` | `H264 Variable Length Decoder Address`  
`[MACC_H264_VLD_OFFSET][58278]` | `0x0234` | `4B` | `H264 Variable Length Decoder Bit Offset`  
`[MACC_H264_VLD_LEN][58279]` | `0x0238` | `4B` | `H264 Variable Length Decoder Bit Length`  
`[MACC_H264_VLD_END][58280]` | `0x023c` | `4B` | `H264 Variable Length Decoder End Address`  
`[MACC_H264_SDROT_CTRL][58281]` | `0x0240` | `4B` | `H264 Scale Rotate buffer control`  
`[MACC_H264_SDROT_LUMA][58282]` | `0x0244` | `4B` | `H264 Scale Rotate buffer Luma color component`  
`[MACC_H264_SDROT_CHROMA][58283]` | `0x0248` | `4B` | `H264 Scale Rotate buffer Chroma color component`  
`[MACC_H264_OUTPUT_FRAME_INDEX][58284]` | `0x024c` | `4B` | `H264 output frame index in dpb`  
`[MACC_H264_FIELD_INTRA_INFO_BUF][58285] ``[MACC_H264_VP8_ENTROPY_PROBS][58286]` | `0x0250` | `4B` | `H264 field intra info buffer address (VP8 entropy brobabilities table address)`  
`[MACC_H264_NEIGHBOR_INFO_BUF][58287] ``[MACC_H264_VP8_FSTDATA_PARTLEN][58288]` | `0x0254` | `4B` | `H264 neighbor info buffer address (VP8 First partition length)`  
`[MACC_H264_PIC_MBSIZE][58289]` | `0x0258` | `4B` | `H264 Picture size in macroblocks`  
`[MACC_H264_PIC_BOUNDARYSIZE][58290]` | `0x025c` | `4B` | `H264 Picture size in pixels`  
`[MACC_H264_MB_ADDR][58291]` | `0x0260` | `4B` | `H264 Current macroblock position`  
`[MACC_H264_MB_NB1][58292]` | `0x0264` | `4B` | `H264 ??? MbNeightbour1`  
`[MACC_H264_MB_NB2][58293]` | `0x0268` | `4B` | `H264 MbNeightbour2`  
`[MACC_H264_MB_NB3][58294]` | `0x026c` | `4B` | `H264 ???`  
`[MACC_H264_MB_NB4][58295]` | `0x0270` | `4B` | `H264 ???`  
`[MACC_H264_MB_NB5][58296]` | `0x0274` | `4B` | `H264 ???`  
`[MACC_H264_MB_NB6][58297]` | `0x0278` | `4B` | `H264 ???`  
`[MACC_H264_MB_NB7][58298]` | `0x027c` | `4B` | `H264 ???`  
`[MACC_H264_MB_NB8][58299]` | `0x0280` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x0284` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x0288` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x028c` | `4B` | `H264 ???`  
`[MACC_H264_MB_QP][58300]` | `0x0290` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x0294` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x0298` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x029c` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x02a0` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x02a4` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x02a8` | `4B` | `H264 ???`  
`[MACC_H264_REC_LUMA][58301]` | `0x02ac` | `4B` | `H264 Luma reconstruct buffer`  
`[MACC_H264_FWD_LUMA][58302]` | `0x02b0` | `4B` | `H264 Luma forward buffer`  
`[MACC_H264_BACK_LUMA][58303]` | `0x02b4` | `4B` | `H264 Luma back buffer`  
`[MACC_H264_ERROR][58304]` | `0x02b8` | `4B` | `H264 Error`  
`MACC_H264_???` | `0x02bc` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x02c0` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x02c4` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x02c8` | `4B` | `H264 ???`  
`MACC_H264_???` | `0x02cc` | `4B` | `H264 ???`  
`[MACC_H264_REC_CHROMA][58305]` | `0x02d0` | `4B` | `H264 Chroma reconstruct buffer`  
`[MACC_H264_FWD_CHROMA][58306]` | `0x02d4` | `4B` | `H264 Chroma forward buffer`  
`[MACC_H264_BACK_CHROMA][58307]` | `0x02d8` | `4B` | `H264 Chroma back buffer`  
`[MACC_H264_BASIC_BITS_DATA][58308]` | `0x02dc` | `4B` | `H264 Basic bits data`  
`[MACC_H264_RAM_WRITE_PTR][58309]` | `0x02e0` | `4B` | `H264 ram write pointer`  
`[MACC_H264_RAM_WRITE_DATA][58310]` | `0x02e4` | `4B` | `H264 ram write data`  
`[MACC_H264_ALT_LUMA][58311]` | `0x02e8` | `4B` | `H264 Alternate Luma buffer`  
`[MACC_H264_ALT_CHROMA][58312]` | `0x02ec` | `4B` | `H264 Alternate Chroma buffer`  
`[MACC_H264_SEG_MB_LV0][58313]` | `0x02f0` | `4B` | `H264 ??? Segment Mb Level 0`  
`[MACC_H264_SEG_MB_LV1][58314]` | `0x02f4` | `4B` | `H264 ??? Segment Mb Level 1`  
`[MACC_H264_REF_LF_DELTA][58315]` | `0x02f8` | `4B` | `H264 ??? (VP8 ref lf deltas)`  
`[MACC_H264_MODE_LF_DELTA][58316]` | `0x02fc` | `4B` | `H264 ??? (VP8 mode lf deltas)`  
## VC1 Engine Registers
Base address: 0x01c0e300  
Used by engine 0x2 (VC1) 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`MACC_VC1_EPHS` | `0x0300` | `4B` | `VC1 ???`  
`MACC_VC1_PIC_CTRL` | `0x0304` | `4B` | `VC1 ???`  
`MACC_VC1_PIC_QP` | `0x0308` | `4B` | `VC1 ???`  
`MACC_VC1_PIC_MV` | `0x030c` | `4B` | `VC1 ???`  
`MACC_VC1_PIC_INTEN_COMP` | `0x0310` | `4B` | `VC1 ???`  
`MACC_VC1_PIC_INTERLANCE` | `0x0314` | `4B` | `VC1 ???`  
`MACC_VC1_HDR_LEN` | `0x0318` | `4B` | `VC1 ???`  
`MACC_VC1_FSIZE` | `0x031c` | `4B` | `VC1 ???`  
`MACC_VC1_PIC_SIZE` | `0x0320` | `4B` | `VC1 ???`  
`MACC_VC1_CTRL` | `0x0324` | `4B` | `VC1 Decoder Control`  
`MACC_VC1_START_TYPE` | `0x0328` | `4B` | `VC1 ???`  
`MACC_VC1_STATUS` | `0x032c` | `4B` | `VC1 Status`  
`MACC_VC1_VBV_BASE_ADDR` | `0x0330` | `4B` | `VC1 Source buffer address`  
`MACC_VC1_VLD_OFFSET` | `0x0334` | `4B` | `VC1 Variable Length Decoder Offset`  
`MACC_VC1_VBV_LEN` | `0x0338` | `4B` | `VC1 length of source video buffer`  
`MACC_VC1_VBV_END_ADDR` | `0x033c` | `4B` | `VC1 last address of source video buffer`  
`MACC_VC1_REC_FRAME_CHROMA` | `0x0340` | `4B` | `VC1 Chroma Reconstruct frame`  
`MACC_VC1_REC_FRAME_LUMA` | `0x0344` | `4B` | `VC1 Luma Reconstruct frame`  
`MACC_VC1_FWD_FRAME_CHROMA` | `0x0348` | `4B` | `VC1 Chroma Forward Frame`  
`MACC_VC1_FWD_FRAME_LUMA` | `0x034c` | `4B` | `VC1 Luma Forward Frame`  
`MACC_VC1_BACK_CHROMA` | `0x0350` | `4B` | `VC1 Chroma back buffer`  
`MACC_VC1_BACK_LUMA` | `0x0354` | `4B` | `VC1 Luma back buffer`  
`MACC_VC1_MBHADDR` | `0x0358` | `4B` | `VC1 ???`  
`MACC_VC1_DCAPRED_ADDR` | `0x035c` | `4B` | `VC1 ???`  
`MACC_VC1_BITPLANE_ADDR` | `0x0360` | `4B` | `VC1 ???`  
`MACC_VC1_MBINFO_ADDR` | `0x0364` | `4B` | `VC1 ???(or COLMVINFOADDR)`  
`MACC_VC1_???` | `0x0368` | `4B` | `VC1 ???`  
`MACC_VC1_???` | `0x036c` | `4B` | `VC1 ???`  
`MACC_VC1_MBA` | `0x0370` | `4B` | `VC1 ???`  
`MACC_VC1_MBHDR` | `0x0374` | `4B` | `VC1 ???`  
`MACC_VC1_LUMA_TRANSFORM` | `0x0378` | `4B` | `VC1 ???`  
`MACC_VC1_MBCBF` | `0x037c` | `4B` | `VC1 ???`  
`MACC_VC1_MBM_V1` | `0x0380` | `4B` | `VC1 ???`  
`MACC_VC1_MBM_V2` | `0x0384` | `4B` | `VC1 ???`  
`MACC_VC1_MBM_V3` | `0x0388` | `4B` | `VC1 ???`  
`MACC_VC1_MBM_V4` | `0x038c` | `4B` | `VC1 ???`  
`MACC_VC1_MBM_V5` | `0x0390` | `4B` | `VC1 ???`  
`MACC_VC1_MBM_V6` | `0x0394` | `4B` | `VC1 ???`  
`MACC_VC1_MBM_V7` | `0x0398` | `4B` | `VC1 ???`  
`MACC_VC1_MBM_V8` | `0x039c` | `4B` | `VC1 ???`  
`MACC_VC1_???` | `0x03a0` | `4B` | `VC1 ???`  
`MACC_VC1_???` | `0x03a4` | `4B` | `VC1 ???`  
`MACC_VC1_???` | `0x03a8` | `4B` | `VC1 ???`  
`MACC_VC1_???` | `0x03ac` | `4B` | `VC1 ???`  
`MACC_VC1_???` | `0x03b0` | `4B` | `VC1 ???`  
`MACC_VC1_???` | `0x03b4` | `4B` | `VC1 ???`  
`MACC_VC1_ERROR` | `0x03b8` | `4B` | `VC1 Error result code`  
`MACC_VC1_CRT_MB_NUM` | `0x03bc` | `4B` | `VC1 ???`  
`MACC_VC1_EXTRA_CTRL` | `0x03c0` | `4B` | `VC1 ???`  
`MACC_VC1_EXTRA_CBUF_ADDR` | `0x03c4` | `4B` | `VC1 EXTRA Chroma DRAM address`  
`MACC_VC1_EXTRA_YBUF_ADDR` | `0x03c8` | `4B` | `VC1 EXTRA Luma DRAM address`  
`MACC_VC1_OVERLAP_UP_ADDR` | `0x03d0` | `4B` | `VC1 ???`  
`MACC_VC1_DBLK_ABOVE_ADDR` | `0x03d4` | `4B` | `VC1 ???`  
`MACC_VC1_???` | `0x03d8` | `4B` | `VC1 ???`  
`MACC_VC1_BITS_RETDATA` | `0x03dc` | `4B` | `VC1 ???`  
`MACC_VC1_DEBUG_BUF_ADDR` | `0x03fc` | `4B` | `VC1 ???`  
## RMVB Engine Registers
Base address: 0x01c0e400  
Used by engine 0x3 (RMVB) 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`MACC_RMVB_SLC_HDR` | `0x0400` | `4B` | `Header`  
`MACC_RMVB_FRM_SIZE` | `0x0404` | `4B` | `Framesize (in macroblocks ?) `  
`MACC_RMVB_DIR_MODE_RATIO` | `0x0408` | `4B` | ``  
`MACC_RMVB_DIR_MB_ADDR` | `0x040c` | `4B` | ``  
`MACC_RMVB_QC_INPUT` | `0x0410` | `4B` | ``  
`MACC_RMVB_CTRL` | `0x0414` | `4B` | `RMVB IRQ Control `  
`MACC_RMVB_TRIG` | `0x0418` | `4B` | `Trigger register`  
`MACC_RMVB_STATUS` | `0x041c` | `4B` | `RMVB Status `  
`MACC_RMVB_VBV_BASE` | `0x0428` | `4B` | `Video source buffer base`  
`MACC_RMVB_VLD_OFFSET` | `0x042c` | `4B` | `Video source buffer DRAM address`  
`MACC_RMVB_VLD_LEN` | `0x0430` | `4B` | `Video source buffer length in bytes`  
`MACC_RMVB_VBV_END` | `0x0434` | `4B` | `Video source buffer last DRAM address`  
`MACC_RMVB_HUFF_TABLE_ADDR` | `0x043c` | `4B` | `Huffman table DRAM address`  
`MACC_RMVB_CUR_Y_ADDR` | `0x0440` | `4B` | `Luma Current buffer DRAM address`  
`MACC_RMVB_CUR_C_ADDR` | `0x0444` | `4B` | `Chroma Current buffer DRAM address`  
`MACC_RMVB_FOR_Y_ADDR` | `0x0448` | `4B` | `Luma Forward buffer DRAM address`  
`MACC_RMVB_FOR_C_ADDR` | `0x044c` | `4B` | `Chroma Forward buffer DRAM address`  
`MACC_RMVB_BAC_Y_ADDR` | `0x0450` | `4B` | `Luma Back buffer DRAM address`  
`MACC_RMVB_BAC_C_ADDR` | `0x0454` | `4B` | `Chroma Back buffer DRAM address`  
`MACC_RMVB_ROT_Y_ADDR` | `0x0458` | `4B` | `Luma Rot buffer DRAM address`  
`MACC_RMVB_ROT_C_ADDR` | `0x045c` | `4B` | `Chroma Rot Buffer DRAM address`  
`MACC_RMVB_MBH_ADDR` | `0x0460` | `4B` | ``  
`MACC_RMVB_MV_ADDR` | `0x0464` | `4B` | ``  
`MACC_RMVB_MBH_INFO` | `0x0470` | `4B` | ``  
`MACC_RMVB_MV0` | `0x0474` | `4B` | `Mountion vector 0`  
`MACC_RMVB_MV1` | `0x0478` | `4B` | `Mountion vector 1`  
`MACC_RMVB_MV2` | `0x047c` | `4B` | `Mountion vector 2`  
`MACC_RMVB_MV3` | `0x0480` | `4B` | `Mountion vector 3`  
`MACC_RMVB_DBLK_COEF` | `0x0490` | `4B` | ``  
`MACC_RMVB_ERROR` | `0x04b0` | `4B` | `Decode error result code`  
`MACC_RMVB_BITS_DATA` | `0x04b8` | `4B` | ``  
`MACC_RMVB_SLC_QUEUE_ADDR` | `0x04c0` | `4B` | ``  
`MACC_RMVB_SLC_QUEUE_LEN` | `0x04c4` | `4B` | ``  
`MACC_RMVB_SLC_QUEUE_TRIG` | `0x04c8` | `4B` | ``  
`MACC_RMVB_SLC_QUEUE_STATUS` | `0x04cc` | `4B` | ``  
`MACC_RMVB_SCALE_ROT_CTRL` | `0x04d0` | `4B` | ``  
`MACC_RMVB_SRAM_RW_OFFSET` | `0x04e0` | `4B` | `SRAM Fifo like index register`  
`MACC_RMVB_SRAM_RW_DATA` | `0x04e4` | `4B` | `SRAM Fifo like data register`  
## HEVC Engine Registers
Base address: 0x01c0e500  
Only on H3, used by engine 0x4 (HEVC) 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[MACC_HEVC_NAL_HDR][58317]` | `0x0500` | `4B` | `HEVC NAL header`  
`[MACC_HEVC_SPS][58318]` | `0x0504` | `4B` | `HEVC sequence parameter set`  
`[MACC_HEVC_PIC_SIZE][58319]` | `0x0508` | `4B` | `HEVC picture size`  
`[MACC_HEVC_PCM_HDR][58320]` | `0x050c` | `4B` | `HEVC PCM header`  
`[MACC_HEVC_PPS0][58321]` | `0x0510` | `4B` | `HEVC picture parameter set`  
`[MACC_HEVC_PPS1][58322]` | `0x0514` | `4B` | `HEVC picture parameter set`  
`[MACC_HEVC_SCALING_LIST_CTRL][58323]` | `0x0518` | `4B` | `HEVC scaling list control register`  
`` | `` | `` | ``  
`[MACC_HEVC_SLICE_HDR0][58324]` | `0x0520` | `4B` | `HEVC slice header`  
`[MACC_HEVC_SLICE_HDR1][58325]` | `0x0524` | `4B` | `HEVC slice header`  
`[MACC_HEVC_SLICE_HDR2][58326]` | `0x0528` | `4B` | `HEVC slice header`  
`[MACC_HEVC_CTB_ADDR][58327]` | `0x052c` | `4B` | `HEVC CTB address`  
`[MACC_HEVC_CTRL][58328]` | `0x0530` | `4B` | `HEVC control register`  
`[MACC_HEVC_TRIG][58329]` | `0x0534` | `4B` | `HEVC trigger register`  
`[MACC_HEVC_STATUS][58330]` | `0x0538` | `4B` | `HEVC status register`  
`[MACC_HEVC_CTU_NUM][58331]` | `0x053c` | `4B` | `HEVC current CTU number`  
`[MACC_HEVC_BITS_ADDR][58332]` | `0x0540` | `4B` | `HEVC bitstream address`  
`[MACC_HEVC_BITS_OFFSET][58333]` | `0x0544` | `4B` | `HEVC bitstream offset`  
`[MACC_HEVC_BITS_LEN][58334]` | `0x0548` | `4B` | `HEVC bitstream length`  
`[MACC_HEVC_BITS_END_ADDR][58335]` | `0x054c` | `4B` | `HEVC bitstream end address`  
`[MACC_HEVC_EXTRA_OUT_CTRL][58336]` | `0x0550` | `4B` | `HEVC extra output control register`  
`[MACC_HEVC_EXTRA_OUT_LUMA_ADDR][58337]` | `0x0554` | `4B` | `HEVC extra output luma address`  
`[MACC_HEVC_EXTRA_OUT_CHROMA_ADDR][58338]` | `0x0558` | `4B` | `HEVC extra output chroma address`  
`[MACC_HEVC_REC_BUF_IDX][58339]` | `0x055c` | `4B` | `HEVC reconstruct buffer index`  
`[MACC_HEVC_NEIGHBOR_INFO_ADDR][58340]` | `0x0560` | `4B` | `HEVC neighbor info buffer address`  
`[MACC_HEVC_TILE_LIST_ADDR][58341]` | `0x0564` | `4B` | `HEVC tile entry point list address`  
`[MACC_HEVC_TILE_START_CTB][58342]` | `0x0568` | `4B` | `HEVC tile start CTB`  
`[MACC_HEVC_TILE_END_CTB][58343]` | `0x056c` | `4B` | `HEVC tile end CTB`  
`` | `` | `` | ``  
`[MACC_HEVC_SCALING_LIST_DC_COEF0][58344]` | `0x0578` | `4B` | `HEVC scaling list DC coefficients`  
`[MACC_HEVC_SCALING_LIST_DC_COEF1][58345]` | `0x057c` | `4B` | `HEVC scaling list DC coefficients`  
`` | `` | `` | ``  
`[MACC_HEVC_BITS_DATA][58346]` | `0x05dc` | `4B` | `HEVC bitstream data`  
`[MACC_HEVC_SRAM_ADDR][58347]` | `0x05e0` | `4B` | `HEVC SRAM address`  
`[MACC_HEVC_SRAM_DATA][58348]` | `0x05e4` | `4B` | `HEVC SRAM data`  
`` | `` | `` | ``  
## ISP Engine Registers
Base address: 0x01c0ea00  
Used by engine 0x8 (MPEG enc), 0xa (ISP) and 0xb (AVC enc) 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[MACC_ISP_PIC_SIZE][58349]` | `0x0a00` | `4B` | `ISP source picture size in macroblocks (16x16)`  
`[MACC_ISP_PIC_STRIDE][58350]` | `0x0a04` | `4B` | `ISP source picture stride`  
`[MACC_ISP_CTRL][58351]` | `0x0a08` | `4B` | `ISP IRQ Control `  
`[MACC_ISP_TRIG][58352]` | `0x0a0c` | `4B` | `ISP Trigger `  
`[MACC_ISP_SCALER_SIZE][58353]` | `0x0a2c` | `4B` | `ISP scaler frame size/16`  
`[MACC_ISP_SCALER_OFFSET_Y][58354]` | `0x0a30` | `4B` | `ISP scaler picture offset for luma`  
`[MACC_ISP_SCALER_OFFSET_C][58355]` | `0x0a34` | `4B` | `ISP scaler picture offset for chroma`  
`[MACC_ISP_SCALER_FACTOR][58356]` | `0x0a38` | `4B` | `ISP scaler picture scale factor`  
`MACC_ISP_BUF???` | `0x0a44` | `4B` | `ISP PHY Buffer offset`  
`MACC_ISP_BUF???` | `0x0a48` | `4B` | `ISP PHY Buffer offset`  
`MACC_ISP_BUF???` | `0x0a4C` | `4B` | `ISP PHY Buffer offset`  
`MACC_ISP_??` | `0x0a74` | `4B` | `ISP ??`  
`[MACC_ISP_OUTPUT_LUMA][58357]` | `0x0a70` | `4B` | `ISP Output LUMA Address `  
`[MACC_ISP_OUTPUT_CHROMA][58358]` | `0x0a74` | `4B` | `ISP Output CHROMA Address `  
`[MACC_ISP_WB_THUMB_LUMA][58359]` | `0x0a78` | `4B` | `ISP THUMB WriteBack PHY LUMA Address `  
`[MACC_ISP_WB_THUMB_CHROMA][58360]` | `0x0a7c` | `4B` | `ISP THUMB WriteBack PHY CHROMA Adress`  
`[MACC_ISP_SRAM_INDEX][58361]` | `0x0ae0` | `4B` | `ISP VE SRAM Index`  
`[MACC_ISP_SRAM_DATA][58362]` | `0x0ae4` | `4B` | `ISP VE SRAM Data`  
## AVC Encoder Engine Registers
Base address: 0x01c0eb00  
Used by engine 0xb (AVC enc) 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`MACC_AVC_PICINFO` | `0x0b00` | `4B` | `unk(not used in blob) `  
`[MACC_AVC_JPEG_CTRL][58363] ``[MACC_AVC_H264_CTRL][58364]` | `0x0b04` | `4B` | `jpeg / h264 different settings`  
`[MACC_AVC_H264_QP][58365]` | `0x0b08` | `4B` | `H264 quantization parameters`  
`[MACC_AVC_H264_MOTION_EST][58366]` | `0x0b10` | `4B` | `Motion estimation parameters`  
`[MACC_AVC_CTRL][58367]` | `0x0b14` | `4B` | `AVC Encoder IRQ Control `  
`[MACC_AVC_TRIG][58368]` | `0x0b18` | `4B` | `AVC Encoder trigger `  
`[MACC_AVC_STATUS][58369]` | `0x0b1c` | `4B` | `AVC Encoder Busy Status `  
`[MACC_AVC_BITS_DATA][58370]` | `0x0b20` | `4B` | `AVC Encoder Bits Data `  
`[MACC_AVC_H264_MAD][58371]` | `0x0b50` | `4B` | `AVC H264 Encoder Mean Absolute Difference`  
`[MACC_AVC_H264_RESIDUAL_BITS][58372]` | `0x0b54` | `4B` | `AVC H264 Encoder Residual Bits`  
`[MACC_AVC_H264_HEADER_BITS][58373]` | `0x0b58` | `4B` | `AVC H264 Encoder Header Bits`  
`[MACC_AVC_H264_??][58374]` | `0x0b5c` | `4B` | `AVC H264 Encoder _unknown statistical data, maybe motion vectors_`  
`[MACC_AVC_H264_??][58374]` | `0x0b60` | `4B` | `AVC H264 Encoder _unknown buffer_`  
`[MACC_AVC_VLE_ADDR][58375]` | `0x0b80` | `4B` | `AVC Variable Length Encoder Start Address`  
`[MACC_AVC_VLE_END][58376]` | `0x0b84` | `4B` | `AVC Variable Length Encoder End Address`  
`[MACC_AVC_VLE_OFFSET][58377]` | `0x0b88` | `4B` | `AVC Variable Length Encoder Bit Offset`  
`[MACC_AVC_VLE_MAX][58378]` | `0x0b8c` | `4B` | `AVC Variable Length Encoder Maximum Bits`  
`[MACC_AVC_VLE_LENGTH][58379]` | `0x0b90` | `4B` | `AVC Variable Length Encoder Bit Length`  
`[MACC_AVC_REF_LUMA][58380]` | `0x0ba0` | `4B` | `Luma reference buffer`  
`[MACC_AVC_REF_CHROMA][58381]` | `0x0ba4` | `4B` | `Chroma reference buffer`  
`[MACC_AVC_REC_LUMA][58382]` | `0x0bb0` | `4B` | `Luma reconstruct buffer`  
`[MACC_AVC_REC_CHROMA][58383]` | `0x0bb4` | `4B` | `Chroma reconstruct buffer`  
`[MACC_AVC_REF_SLUMA][58384]` | `0x0bb8` | `4B` | `Smaller luma reference buffer ?`  
`[MACC_AVC_REC_SLUMA][58385]` | `0x0bbc` | `4B` | `Smaller luma reconstruct buffer ?`  
`[MACC_AVC_MB_INFO][58386]` | `0x0bc0` | `4B` | `Temporary buffer with macroblock information`  
`[MACC_AVC_SRAM_INDEX][58387]` | `0x0be0` | `4B` | `AVC VE SRAM Index`  
`[MACC_AVC_SRAM_DATA][58388]` | `0x0be4` | `4B` | `AVC VE SRAM Data`  
# VE General Registers
## MACC_VE_CTRL
Default value: 0x00000007  
Offset: 0x0000 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_VE_CTRL_ENGINE` | `0:3` | `Read/Write` | `0x7` | ` `
[code]
        0x0 = MPEG
        0x1 = H264
        0x2 = VC1
        0x3 = RMVB
        0x4 = HEVC (H3 only)
        0x5-0x6 = reserved
        0x7 = place in #reset
        0x8 = MPEG Encoder {may be present only in sun3i}
        0x9 = reserved
        0xa = ISP
        0xb = AVC (H264 Encoder)
        0xc-0xf = reserved
      
    
[/code]
| Select VE Engine: Each bit set represents Sub Engine that implemets personal codes sets, and enables required regiter set. H264 and MPEG Encoders using same register set, and seems 0x8 still here for historic reasons **Note:** selecting 0x7 mean 'place in reset state'   
`` | `4` | `Read only` | `0x0` |  | _reserved_  
`` | `5` | `Read/Write` | `0x0` |  | Enable JPEG decoder (sun8iw8p1 (H3?) only)   
`` | `6` | `Read/Write` | `0x0` | Enable ISP (1633 and newer only?)   
`` | `7` | `Read/Write` | `0x0` | Enable AVC encoder (1633 and newer only?)   
`MACC_VE_CTRL_???` | `8:9` | `Read/Write` | `0x0` |  | ?   
`` | `10:15` | `Read only` | `0x0` |  | _reserved_  
`MACC_VE_CTRL_MEM_TYPE` | `16:17` | `Read/Write` | `0x0` | ` `
[code]
        0x0 = DDR1 16-BITS
        0x1 = DDR1 32-BITS / DDR2 16-Bits
        0x2 = DDR2 32-BITS / DDR3 16-Bits
        0x3 = DDR3 32-BITS
      
    
[/code]
| Memory type (on current a10/a13 used only 0x3)   
`` | `18:19` | `Read only` | `0x0` |  | _reserved_  
`MACC_VE_CTRL_???` | `20` | `Read/Write` | `0x0` |  | more one mem type??   
`MACC_VE_CTRL_???` | `21` | `Read/Write` | `0x0` |  | needs to be set to decode pictures with more than 2048px width   
`` | `22:23` | `Read only` | `0x0` |  | _reserved_  
`MACC_VE_CTRL_???` | `24:25` | `Read/Write` | `0x0` |  | more one mem type??   
`` | `26:27` | `Read only` | `0x0` |  | _reserved_  
`MACC_VE_CTRL_???` | `28` | `Read/Write` | `0x0` |  | ?   
`` | `29:31` | `Read only` | `0x0` |  | _reserved_  
## MACC_VE_RESET
Default value: 0x00000000  
Offset: 0x0004 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `0` | `Read/Write` | `0` | `` | Reset sub-engines   
`` | `1:3` | `Read Only` | `0` | `` | unused?   
`` | `4` | `Read/Write` | `0` | `` | unknown?   
`` | `5:31` | `Read Only` | `0` | `` | unused?   
## MACC_VE_CYCLES_COUNTER
Default value: 0x00000000  
Offset: 0x0008 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_VE_CYCLES_COUNTER_EN` | `31` | `Read/Write` | `0` | ` `
[code]
    0 = disabled
    1 = enabled
    
[/code]
| Enable cycle counter   
`MACC_VE_CYCLES_COUNTER_VAL` | `30:0` | `Read Only` | `0` | `` | Clock cycles since start of counter   
## MACC_VE_TIMEOUT
Default value: 0x00000000  
Offset: 0x000C 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `0:7` | `Read Only` | `0` | `` | ?   
`` | `8:30` | `Read/Write` | `0` | `` | overtime value   
`` | `31` | `Read Only` | `0` | `` | ?   
## MACC_VE_STATUS
Default value: 0x00000000  
Offset: 0x001c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `0:8` | `Read Only` | `0` | `` | reserved   
`MACC_VE_STATUS` | `9:14` | `Read/Write` | `0x00` | ` `
[code]
        0x0 = Ready
        0x3 = Busy
      
    
[/code]
| CedarX status   
`` | `15:31` | `Read Only` | `0` | `` | reserved   
## MACC_VE_RDDATA_COUNTER
Default value: 0x00000000  
Offset: 0x0020 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_VE_RDDATA_COUNTER_EN` | `31` | `Read/Write` | `0` | ` `
[code]
    0 = disabled
    1 = enabled
    
[/code]
| Enable read counter   
`MACC_VE_RDDATA_COUNTER_VAL` | `30:0` | `Read Only` | `0` | `` | Data read from DRAM in 64 bit words   
## MACC_VE_WRDATA_COUNTER
Default value: 0x00000000  
Offset: 0x0024 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_VE_WRDATA_COUNTER_EN` | `31` | `Read/Write` | `0` | ` `
[code]
    0 = disabled
    1 = enabled
    
[/code]
| Enable write counter   
`MACC_VE_WRDATA_COUNTER_VAL` | `30:0` | `Read Only` | `0` | `` | Data written to DRAM in 64 bit words   
## MACC_VE_ANAGLYPH_CTRL
Default value: 0x00000000  
Offset: 0x0028 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_VE_ANAGLYPH_OUT_EN` | `31` | `Read/Write` | `0` | ` `
[code]
    0 = disabled
    1 = enabled
    
[/code]
| Enable anaglyph output   
`` | `30:10` | `Read/Write` | `0` | `` | _reserved_  
`MACC_VE_ANAGLYPH_COLORSPACE` | `9:8` | `Read/Write` | `0` | ` `
[code]
    0x0 = YCC
    0x1 = BT601
    0x2 = BT709
    0x3 = _reserved_
    
[/code]
| YUV to RGB conversion color space   
`` | `7` | `Read/Write` | `0` | `` | _reserved_  
`MACC_VE_ANAGLYPH_MODE` | `6:4` | `Read/Write` | `0` | ` `
[code]
    0x0 = red/blue
    0x1 = red/green
    0x2 = red/cyan
    0x3 = color
    0x4 = half color
    0x5 = optimized
    0x6 = yellow/blue
    0x7 = _reserved_
    
[/code]
| Anaglyph color channels   
`MACC_VE_ANAGLYPH_SIDE` | `3` | `Read/Write` | `0` | ` `
[code]
    0x0 = left
    0x1 = right
    
[/code]
| Current decoded picture for "seperate frames" source mode   
`` | `2` | `Read/Write` | `0` | `` | _reserved_  
`MACC_VE_ANAGLYPH_SRC_MODE` | `1:0` | `Read/Write` | `0` | ` `
[code]
    0x0 = side by side
    0x1 = top/down
    0x2 = line by line
    0x3 = separate frames
    
[/code]
| Source mode   
## MACC_VE_IPD_DBLK_BUF_CTRL
Default value: 0x00000000  
Offset: 0x0050 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:4` | `Read/Write` | `0` | `` | _reserved_  
`MACC_VE_IPD_BUF_CTRL` | `3:2` | `Read/Write` | `0` | ` `
[code]
    0x0 = only SRAM
    0x1 = left 1280 pixels SRAM, rest DRAM
    0x2 = only DRAM
    
[/code]
| Intraprediction buffer control   
`MACC_VE_DBLK_BUF_CTRL` | `1:0` | `Read/Write` | `0` | ` `
[code]
    0x0 = only SRAM
    0x1 = left 1280 pixels SRAM, rest DRAM
    0x2 = only DRAM
    
[/code]
| Deblocking buffer control   
## MACC_VE_LUMA_HIST_THRi
Default value: see table  
Offset: 0x0080 + (i * 4) 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_VE_LUMA_HIST_THR_i_3` | `31:24` | `Read/Write` | `(i * 0x40) + 0x40` | `` | Threshold for histogram channel (i * 4) + 3   
`MACC_VE_LUMA_HIST_THR_i_2` | `23:16` | `Read/Write` | `(i * 0x40) + 0x30` | `` | Threshold for histogram channel (i * 4) + 2   
`MACC_VE_LUMA_HIST_THR_i_1` | `15:8` | `Read/Write` | `(i * 0x40) + 0x20` | `` | Threshold for histogram channel (i * 4) + 1   
`MACC_VE_LUMA_HIST_THR_i_0` | `7:0` | `Read/Write` | `(i * 0x40) + 0x10` | `` | Threshold for histogram channel (i * 4) + 0   
## MACC_VE_LUMA_HIST_VALi
Default value: 0x00000000  
Offset: 0x0090 + (i * 4) 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:20` | `Read/Write` | `0x0` | `` | _reserved_  
`MACC_VE_LUMA_HIST_VAL` | `19:0` | `Read/Write` | `0x0` | `` | Output value for histogram channel i   
## MACC_VE_OUTPUT_CHROMA_OFFSET
Default value: 0x00000000  
Offset: 0x00c4  
at least since VE Version 1680 
Offset | `0x0c4`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:28` | `RW` | `` |  | _reserved_  
`MACC_VE_OUTPUT_CHROMA_OFFSET` | `27:0` | `RW` | `` |  | offset of second chroma plane  
  

## MACC_VE_OUTPUT_STRIDE
Default value: 0x00000000  
Offset: 0x00c8  
at least since VE Version 1680 
Offset | `0x0c8`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_VE_OUTPUT_CHROMA_STRIDE` | `31:16` | `RW` | `` |  | chroma line stride length  
`MACC_VE_OUTPUT_LUMA_STRIDE` | `15:0` | `RW` | `` |  | luma line stride length  
  

## MACC_VE_EXTRA_OUT_STRIDE
Default value: 0x00000000  
Offset: 0x00cc  
at least since VE Version 1680 
Offset | `0x0cc`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_VE_EXTRA_OUT_CHROMA_STRIDE` | `31:16` | `RW` | `` |  | chroma line stride length  
`MACC_VE_EXTRA_OUT_LUMA_STRIDE` | `15:0` | `RW` | `` |  | luma line stride length  
  

## MACC_VE_EXTRA_OUT_FMT_OFFSET
Default value: 0x00000000  
Offset: 0x00e8  
VE Version 1633 and newer 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_VE_EXTRA_OUT_FMT` | `30:31` | `Read/Write` | `0x0` | `
[code] 
    0x0 = 32x32 tile format
    0x1 = reserved / (at least since 1680: use special format from 0x0ec)
    0x2 = YUV planar
    0x3 = YVU planar
    
[/code]
``` | Extra output format   
`MACC_VE_EXTRA_OUT_ALIGN` | `29:28` | `Read/Write` | `0x0` | ` ``` | Extra output alignment _, yet to figure out the exact values_  
`MACC_VE_EXTRA_OUT_SEC_OFF` | `27:0` | `Read/Write` | `0x0` | `` | Offset for the second chroma plane   
## MACC_VE_OUTPUT_FORMAT
Default value: 0x00000000  
Offset: 0x00ec  
at least since VE Version 1680 
Offset | `0x0ec`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:7` | `RW` | `` |  | _reserved_  
`MACC_VE_OUTPUT_FORMAT` | `6:4` | `RW` | `` | 
[code]
    0x0 = 32x32 tiles
    0x1 = 128x32 tiles
    0x2 = I420
    0x3 = YV12
    0x4 = NV12
    0x5 = NV21
    0x6 = ?
    0x7 = ?
    
[/code]
|   
`` | `3` | `RW` | `` |  | _reserved_  
`MACC_VE_EXTRA_OUT_FORMAT` | `2:0` | `RW` | `` | 
[code]
    0x0 = 32x32 tiles
    0x1 = 128x32 tiles
    0x2 = I420
    0x3 = YV12
    0x4 = NV12
    0x5 = NV21
    0x6 = ?
    0x7 = ?
    
[/code]
| only valid if special format enabled in 0x0e8  
## MACC_VE_VERSION
Offset: 0x00f0 
Known values: 
  * 0x16230055 (A10/A20)
  * 0x16250055 (A13)
  * 0x16330040 (A31s)
  * 0x16390028 (A80)
  * 0x16670040 (A33)
  * 0x16800040 (H3)
  * 0x16890040 (A64)
  * 0x17180040 (H5)
  * 0x16810040 (S3)

Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_VE_VERSION_SOC` | `16:31` | `Read Only` | `0x1625(a13)` | ` `
[code]
        Video Core IP Version
        0x1625 - A13
        0x1623 - A10/A20
        ...
      
    
[/code]
| VE IP version **WARNING:** In case of A10 and A13 match SoC Version, but seems AW stuff was too lazy to fix blob code for A20 production, thats means, A10/A20 use absolutly same VE Engine(A20 Also workable with A10 blob except cortex a8/a7 cache behavior difference).   
`MACC_VE_VERSION_~~REV~~` | `15:0` | `Read Only` | `0x0055(A13)` | ` `
[code]
      
    
[/code]
| ~~IP revision(guess)~~  
# MPEG Engine Registers
## MACC_MPEG_PHDR
Mostly from Picture_Coding_Extension 
  
Default value: 0x00000000  
Offset: 0x0100 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_PHDR_TYPE` | `31:28` | `Read/Write` | `` | ` `
[code]
        MPEG picture_coding_type: [[1]][58389]
        0x0 = forbidden
        0x1 = I-Frame
        0x2 = P-Frame
        0x3 = B-Frame
        0x4 = D-Frame
        ... = reserved
    
      
    
[/code]
| Frame Type   
`MACC_MPEG_PHDR_FCODE_00` | `27:24` | `Read/Write` | `` | `
[code] 
       MPEG2 f_code[0][0] 
       MPEG1: forward_f_code
    
[/code]
``` | (4+ n)^2 - Mountion vector forward range   
`MACC_MPEG_PHDR_FCODE_01` | `23:20` | `Read/Write` | `` | ` `
[code]
      MPEG2: f_code[0][1] 
      MPEG1: forward_f_code
     
    
[/code]
| (4+ n)^2 - Mountion vector forward range   
`MACC_MPEG_PHDR_FCODE_10` | `19:16` | `Read/Write` | `` | ` `
[code]
      MPEG2: f_code[1][0] 
      MPEG1: backward_f_code
      
    
[/code]
| (4+ n)^2 - Mountion vector backward range   
`MACC_MPEG_PHDR_FCODE_11` | `15:12` | `Read/Write` | `` | ` `
[code]
      MPEG2: f_code[1][1] 
      MPEG1: backward_f_code
      
    
[/code]
| (4+ n)^2 - Mountion vector backward range   
`MACC_MPEG_PHDR_INTRA_DC_PREC` | `11:10` | `Read/Write` | `` | `
[code] 
      MPEG2: intra_dc_precision[[2]][58390]:
      00  - Precision (bits) 8
      01  - Precision (bits) 9
      10  - Precision (bits) 10
      11  - Precision (bits) 11
    
[/code]
`
[code]
      MPEG1: 0x0
     
    
[/code]
|   
`MACC_MPEG_PHDR_PIC_STRUCT` | `9:8` | `Read/Write` | `` | `
[code] 
      MPEG2: picture_structure [[3]][58391]:
       00 - reserved
       01 - top field
       10 - bottom field
       11 - frame picture
    
[/code]
`
[code]
      MPEG1: always 0x3 (Frame picture)
    
    
[/code]
|   
`MACC_MPEG_PHDR_TOP_FIRST` | `7` | `Read/Write` | `` | ` `
[code]
      MPEG2: top_field_first[[4]][58392] 
      MPEG1: always 0x1
     
    
[/code]
|   
`MACC_MPEG_PHDR_FRAME_PRED` | `6` | `Read/Write` | `` | ` `
[code]
      MPEG2: frame_pred_frame_dct[[5]][58393] 
       0 - not used 
       1 - used
      MPEG1: always 1
     
    
[/code]
| Is frame-DCT and frame prediction used   
`MACC_MPEG_PHDR_CON_MOTION` | `5` | `Read/Write` | `` | ` `
[code]
     MPEG2: concealment_motion_vectors[[6]][58394]
      0 - not coded
      1 - coded
     MPEG1: always 0
     
    
[/code]
| Is montion vectors are coded for intral MB   
`MACC_MPEG_PHDR_Q_SCALE` | `4` | `Read/Write` | `` | `
[code] 
     MPEG2: q_scale_type 
     MPEG1: always 0x0
    
[/code]
``` |   
`MACC_MPEG_PHDR_INTRA_VLC` | `3` | `Read/Write` | `` | ` `
[code]
       MPEG2: intra_vlc_format 
       MPEG1: always 0x0
    
[/code]
|   
`MACC_MPEG_PHDR_ALT_SCAN` | `2` | `Read/Write` | `` | ` `
[code]
      MPEG2: alternate_scan 
      MPEG1: always 0x0
    
[/code]
|   
`MACC_MPEG_PHDR_FULL_PEL_FWD` | `1` | `Read/Write` | `` | ` `
[code]
      MPEG1: full_pel_forward_vector 
      MPEG2: always 0x0 by specification
    
[/code]
|   
`MACC_MPEG_PHDR_FULL_PEL_BACK` | `0` | `Read/Write` | `` | ` `
[code]
      MPEG1: full_pel_backward_vector 
      MPEG2: always 0x0 by specification
    
[/code]
|   
## MACC_MPEG_VOPHDR
Default value: 0x00000000  
Offset: 0x0104 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | MPEG4 VOP Header   
## MACC_MPEG_SIZE
Default value: 0x00000000  
Offset: 0x0108 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:16` | `Read/Write` | `` | `` | unknown   
`MACC_MPEG_SIZE_WIDTH` | `15:8` | `Read/Write` | `` | `` | Picture width in macroblocks (rounded up to multiple of 16 and divided by 16)   
`MACC_MPEG_SIZE_HEIGHT` | `7:0` | `Read/Write` | `` | `` | Picture height in macroblocks (rounded up to multiple of 16 and divided by 16)   
## MACC_MPEG_FRAME_SIZE
Default value: 0x00000000  
Offset: 0x010c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_FRAME_SIZE_WIDTH` | `31:16` | `Read/Write` | `` | `` | Picture width rounded up to multiple of 16   
`MACC_MPEG_FRAME_SIZE_HEIGHT` | `15:0` | `Read/Write` | `` | `` | Picture height rounded up to multiple of 16   
## MACC_MPEG_MBA
Default value: 0x00000000  
Offset: 0x0110 
MPEG4: 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:16` | `Read/Write` | `` | `` | unused   
`` | `15:8` | `Read/Write` | `` | `` | MPEG4: Macroblock number in horizontal row (mb_x) of current picture slice   
`` | `31:0` | `Read/Write` | `` | `` | MPEG4: Macroblock number in vertical row (mb_y) of current picture slice   
MPEG2: 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Macroblock address location relative to previously coded MB in GOB, MBA = 1+(skipped MBs in GOB)   
## MACC_MPEG_CTRL
Default value: 0x00000000  
Offset: 0x0114 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:28` | `Read/Write` | `` | `` | Unknown   
`MACC_MPEG_CTRL_SW_VLD` | `27` | `Read/Write` | `` | `
[code] 
     0x00: VLD implemented in hardware
     0x01: VLD implemented in software
    
[/code]
` | Hardware/software Variable-Length Decoder (VLD) selection   
`` | `26:18` | `Read/Write` | `` | `` | Unknown   
`MACC_MPEG_CTRL_SW_IQIS` | `17` | `Read/Write` | `` | `
[code] 
     0x00: IQ/IS implemented in hardware
     0x01: IQ/IS implemented in software
    
[/code]
` | Hardware/software Inverse Quantization and Inverse Scan (IQIS) selection   
`MACC_MPEG_CTRL_HISTOGRAM_EN` | `16` | `Read/Write` | `` | ` `
[code]
    0 = disabled
    1 = enabled
    
[/code]
| Enable luma histogram output (see [MACC_VE_LUMA_HIST_VAL[0-15]][58193])   
`` | `15:9` | `Read/Write` | `` | `` | unknown   
`MACC_MPEG_CTRL_EXTRA_OUTPUT_ENABLE` | `8` | `Read/Write` | `` | ` `
[code]
     0x00: Disable extra output
     0x01: Enable extra output
     
    
[/code]
| enable writing extra output picture (rotate/scale/deblock)   
`MACC_MPEG_CTRL_WRITE_REC_DISABLE` | `7` | `Read/Write` | `` | ` `
[code]
     0x00: Write reconstructed picture
     0x01: Don't write reconstructed picture
     
    
[/code]
| disable writing of reconstructed picture   
`` | `6` | `Read/Write` | `` | `` | Unknown, maybe scale/rotation IRQ?   
`MACC_MPEG_CTRL_IRQ_VLD_REQUEST_EN` | `5` | `Read/Write` | `` | ` `
[code]
     0x00: VLD memory request IRQ Disable
     0x01: VLD memory request IRQ Enable
     
    
[/code]
| VLD memory request interrupt enable   
`MACC_MPEG_CTRL_IRQ_ERROR_EN` | `4` | `Read/Write` | `` | ` `
[code]
     0x00: Error IRQ Disable
     0x01: Error IRQ Enable
     
    
[/code]
| Error interrupt enable   
`MACC_MPEG_CTRL_IRQ_FINISH_EN` | `3` | `Read/Write` | `` | ` `
[code]
     0x00: Finish IRQ Disable
     0x01: Finish IRQ Enable
     
    
[/code]
| Finish interrupt enable   
## MACC_MPEG_TRIG
Default value: 0x00000000  
Offset: 0x0118 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_TRIG_ERROR_DISABLE` | `31` | `Read/Write` | `` | `
[code] 
    0x1 - disable 
    0x0 - enable 
    
[/code]
``` | MPEG bitstream error handling   
`` | `30` | `Read/Write` | `` | `` | unknow   
`MACC_MPEG_CTRL_COLOR_FMT` | `29:27` | `Read/Write` | `0x0` | ` `
[code]
        0x0 = YUV 4:2:0
        0x1 = YUV 4:1:1
        0x2 = YUV 4:2:2 horizontal
        0x3 = YUV 4:4:4
        0x4 = YUV 4:2:2 vertical
        0x5 = ???
        0x6 = ???
        0x7 = ???
      
    
[/code]
| Input color format   
`MACC_MPEG_CTRL_FORMAT` | `26:24` | `Read/Write` | `0x0` | ` `
[code]
        0x0 = reserved
        0x1 = MPEG1
        0x2 = MPEG2
        0x3 = JPEG
        0x4 = MPEG4
        0x5 = VP6
        0x6 = ???
        0x7 = ???
      
    
[/code]
| Input data format   
`MACC_MPEG_CTRL_MB_NUM` | `23:8` | `Read/Write` | `` | `` | Number of macroblock   
`` | `7:4` | `Read/Write` | `` | `` | unknown counter/offset(seen mpeg4)   
`` | `3:0` | `Read/Write` | `` | `
[code] 
    MPEGs: 0xe
    JPEG: 0xd
    MS-MPEG: 0x7 or 0x5
    VP6: 0xf
    Mpeg bit-offset search 0x8
    
[/code]
``` | Trigger bits, exact function unknown   
## MACC_MPEG_STATUS
Default value: 0x0000c000  
Offset: 0x011c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:16` | `Read/Write` | `` | `` | Reserved/Unknown   
`MACC_MPEG_STATUS_IQIS_IN_EMPTY` | `15` | `Read/Write` | `` | `` | Inverse quantization and inverse scan input empty   
`MACC_MPEG_STATUS_IDCT_IN_EMPTY` | `14` | `Read/Write` | `` | `` | Inverse discrete cosine transform input empty   
`MACC_MPEG_STATUS_ENGINE_BUSY` | `13` | `Read/Write` | `` | `` | MPEG engine busy status, 0 for free and 1 for busy   
`MACC_MPEG_STATUS_MC_BUSY` | `12` | `Read/Write` | `` | `` | Motion Compensator (MC) busy status, 0 for free and 1 for busy   
`MACC_MPEG_STATUS_IDCT_BUSY` | `11` | `Read/Write` | `` | `` | Inverse Discrete Cosine Transform (IDCT) busy status, 0 for free and 1 for busy   
`MACC_MPEG_STATUS_IQIS_BUSY` | `10` | `Read/Write` | `` | `` | Inverse Quantization and Inverse Scan (IQIS) busy status, 0 for free and 1 for busy   
`MACC_MPEG_STATUS_DCAC_BUSY` | `9` | `Read/Write` | `` | `` | DC/AC (separation?) busy status, 0 for free and 1 for busy   
`MACC_MPEG_STATUS_VLD_BUSY` | `8` | `Read/Write` | `` | `` | Variable-Length Decoder (VLD) busy status, 0 for free and 1 for busy   
`` | `7:3` | `Read/Write` | `` | `` | Reserved   
`MACC_MPEG_STATUS_VLD_REQUEST` | `2` | `Read/Write` | `` | `` | MPEG VLD memory request interrupt flag, set by hardware, write 1 to clear   
`MACC_MPEG_STATUS_ERROR` | `1` | `Read/Write` | `` | `` | MPEG error interrupt flag, set by hardware, write 1 to clear   
`MACC_MPEG_STATUS_FINISH` | `0` | `Read/Write` | `` | `` | MPEG finish interrupt flag, set by hardware, write 1 to clear   
## MACC_MPEG_FRAME_DIST
Default value: 0x00000000  
Offset: 0x0120 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `
[code] 
     MPEG1: always 0(initialy)
    
[/code]
``` | unknown   
## MACC_MPEG_TRBTRDFLD
Default value: 0x00000000  
Offset: 0x0124 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `
[code] 
     MPEG1: always 0x3(initialy)
    
[/code]
``` | unknown   
## MACC_MPEG_VLD_ADDR
Default value: 0x00000000  
Offset: 0x0128 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:28` | `Read/Write` | `` | `
[code] 
    MPEG - 0x5
    JPEG - 0x7
    
[/code]
``` | the 0x7 flag is used for both MPEG and JPEG decoding   
`` | `27:4` | `Read/Write` | `` | `
[code] 
    27:4 VLD Address bits
    
[/code]
``` | VLD Address LOW bits (for first bits dropped from address)   
`` | `3:0` | `Read/Write` | `` | `
[code] 
    31:28 VLD Address bits (for addesses beyond 256 MB)
    
[/code]
``` | VLD Address HI bits   
## MACC_MPEG_VLD_OFFSET
Default value: 0x00000000  
Offset: 0x012c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_VLD_OFFSET` | `31:0` | `Read/Write` | `` | `` | VLD Offset in bits - current frame offset from VLD start address   
## MACC_MPEG_VLD_LEN
Default value: 0x00000000  
Offset: 0x0130 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_VLD_LEN` | `31:0` | `Read/Write` | `` | `` | VLD Length in bits - source video size   
## MACC_MPEG_VBV_END
Default value: 0x00000000  
Offset: 0x0134 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Source video buffer last address   
## MACC_MPEG_MBH_ADDR
Default value: 0x00000000  
Offset: 0x0138 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | macro block hdr info   
## MACC_MPEG_DCAC_ADDR
Default value: 0x00000000  
Offset: 0x013c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_BLK_OFFSET
Default value: 0x00000000  
Offset: 0x0140 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_NCF_ADDR
Default value: 0x00000000  
Offset: 0x0144 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_REC_LUMA
Default value: 0x00000000  
Offset: 0x0148 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_REC_LUMA` | `31:0` | `Read/Write` | `` | `` | Luma Reconstruct Buffer Address (must be 1KB aligned)   
## MACC_MPEG_REC_CHROMA
Default value: 0x00000000  
Offset: 0x014c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_REC_CHROMA` | `31:0` | `Read/Write` | `` | `` | Chroma Reconstruct Buffer Address (must be 1KB aligned)   
## MACC_MPEG_FWD_LUMA
Default value: 0x00000000  
Offset: 0x0150 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_FWD_LUMA` | `31:0` | `Read/Write` | `` | `` | Luma Forward Prediction Buffer Address (must be 1KB aligned)   
## MACC_MPEG_FWD_CHROMA
Default value: 0x00000000  
Offset: 0x0154 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_FWD_CHROMA` | `31:0` | `Read/Write` | `` | `` | Chroma Forward Prediction Buffer Address (must be 1KB aligned)   
## MACC_MPEG_BACK_LUMA
Default value: 0x00000000  
Offset: 0x0158 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_BACK_LUMA` | `31:0` | `Read/Write` | `` | `` | Luma Backward Prediction Buffer Address (must be 1KB aligned)   
## MACC_MPEG_BACK_CHROMA
Default value: 0x00000000  
Offset: 0x015c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_BACK_CHROMA` | `31:0` | `Read/Write` | `` | `` | Chroma Backward Prediction Buffer Address (must be 1KB aligned)   
## MACC_MPEG_SOCX
Default value: 0x00000000  
Offset: 0x0160 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_SOCY
Default value: 0x00000000  
Offset: 0x0164 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_SOL
Default value: 0x00000000  
Offset: 0x0168 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_SDLX
Default value: 0x00000000  
Offset: 0x016c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_SDLY
Default value: 0x00000000  
Offset: 0x0170 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_SPRITESHFT
Default value: 0x00000000  
Offset: 0x0174 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_SDCX
Default value: 0x00000000  
Offset: 0x0178 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_SDCY
Default value: 0x00000000  
Offset: 0x017c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_IQ_MIN_INPUT
Default value: 0x00000000  
Offset: 0x0180 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Used for load IQ table for MPEG2/JPEG decoding, after write value automaticly moves to some v-sram   
## MACC_MPEG_IQ_INPUT
Default value: 0x00000000  
Offset: 0x0184 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MSMPEG4_HDR
Default value: 0x00000000  
Offset: 0x0188 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_VP6_HDR
Default value: 0x00000000  
Offset: 0x018c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_IQ_IDCT_INPUT
Default value: 0x00000000  
Offset: 0x0190 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MB_HEIGHT
Default value: 0x00000000  
Offset: 0x0194 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MB_V1
Default value: 0x00000000  
Offset: 0x0198 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MB_V2
Default value: 0x00000000  
Offset: 0x019c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MB_V3
Default value: 0x00000000  
Offset: 0x01a0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MB_V4
Default value: 0x00000000  
Offset: 0x01a4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MB_V5
Default value: 0x00000000  
Offset: 0x01a8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MB_V6
Default value: 0x00000000  
Offset: 0x01ac 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MB_V7
Default value: 0x00000000  
Offset: 0x01b0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_MB_V8
Default value: 0x00000000  
Offset: 0x01b4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_JPEG_SIZE
Default value: 0x00000000  
Offset: 0x01b8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_JPEG_SIZE_HEIGHT` | `31:16` | `Read/Write` | `0x0000` | ` `
[code]
        0 = 1 MCU
        1 = 2 MCU
         ...
      
    
[/code]
| Height in MCUs   
`MACC_MPEG_JPEG_SIZE_WIDTH` | `15:0` | `Read/Write` | `0x0000` | ` `
[code]
        0 = 1 MCU
        1 = 2 MCU
         ...
      
    
[/code]
| Width in MCUs   
## MACC_MPEG_JPEG_MCU
Default value: 0x00000000  
Offset: 0x01bc 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_JPEG_RES_INT
Default value: 0x00000000  
Offset: 0x01c0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_JPEG_RES_INT` | `31:0` | `Read/Write` | `0x0` | `
[code] 
    DRI marker
    
[/code]
``` | JPEG Restart Interval   
## MACC_MPEG_ERROR
Default value: 0x00000000  
Offset: 0x01c4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | (guess)Must return error code in some error cases   
## MACC_MPEG_CTR_MB
Default value: 0x00000000  
Offset: 0x01c8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_ROT_LUMA
Default value: 0x00000000  
Offset: 0x01cc 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_ROT_LUMA` | `31:0` | `Read/Write` | `` | `` | Luma Rotate/Scale Output Buffer Address (must be 1KB aligned)   
## MACC_MPEG_ROT_CHROMA
Default value: 0x00000000  
Offset: 0x01d0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_ROT_CHROMA` | `31:0` | `Read/Write` | `` | `` | Chroma Rotate/Scale Output Buffer Address (must be 1KB aligned)   
## MACC_MPEG_ROTSCALE_CTRL
Used for control Rotate/Scale buffer 
  
Default value: 0x00000000  
Offset: 0x01d4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:12` | `Read/Write` | `` | `` | unknown   
`MACC_MPEG_EXTRA_FUNC_SCALE_Y` | `11:10` | `Read/Write` | `` | ` `
[code]
        0x0 = /1 (full size)
        0x1 = /2
        0x2 = /4
        0x3 = /8
      
    
[/code]
| Downscale y   
`MACC_MPEG_EXTRA_FUNC_SCALE_X` | `9:8` | `Read/Write` | `` | ` `
[code]
        0x0 = /1 (full size)
        0x1 = /2
        0x2 = /4
        0x3 = /8
      
    
[/code]
| Downscale x   
`` | `7:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_JPEG_MCU_START
Default value: 0x00000000  
Offset: 0x01d8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_JPEG_MCU_END
Default value: 0x00000000  
Offset: 0x01dc 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_MPEG_SRAM_RW_OFFSET
Default value: 0x00000000  
Offset: 0x01e0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Used for reload huffman table(JPEG decoding)   
## MACC_MPEG_SRAM_RW_DATA
Default value: 0x00000000  
Offset: 0x01e4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Used for Huffman table load procedure in JPEG-decoding process   
Map for Jpeg decoding process: 
Cedar Huffman Tables are 2KiB of data written through this register. First half contains description of Huffman-tree, second half contains the data. 
[code] 
    +----------+----------+----------+----------+---- - - - ---------- - - - ---------- - - - -----+
    |  LumaDC  |  LumaAC  | ChromaDC | ChromaAC | Filled with zero (maybe more trees are possible) |
    | 64 bytes | 64 bytes | 64 bytes | 64 bytes |                    768 bytes                     |
    +----------+----------+----------+----------+---- - - - -----+---- - - - -----+---- - - - -----+
    |                Luma DC Data               |  Luma AC Data  | Chroma DC Data | Chroma AC Data |
    |                  256 bytes                |   256 bytes    |   256 bytes    |   256 bytes    |
    +-------------------------------------------+---- - - - -----+---- - - - -----+---- - - - -----+
    
[/code]
Each of the 64 byte tree-description has the following format: 
[code] 
    First 16 halfwords: first bitstream used for datacodes in corresponding depth (or 0xffff if no more data)
    Next 16 bytes: offset in data section for corresponding depth
    Rest (16 bytes): Filled with zero
    
[/code]
The 256 byte data sections contain the codes in same format as in JPEG. 
## MACC_MPEG_START_CODE_BITOFFSET
Default value: UNDEF   
Offset: 0x01f0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_MPEG_START_CODE_BITOFFSET ` | `31:0` | `Read/Write` | `` | `` | Used as result register for mpeg2 entry offset search procedure   
# H264 Engine Registers
## MACC_H264_SEQ_HDR
Default value: 0x00000000  
Offset: 0x0200 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:22` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_SEQ_HEADER_CHROMA_FORMAT` | `21:19` | `Read/Write` | `` | ` `
[code]
    chroma_format_idc
    
[/code]
|   
`MACC_H264_SEQ_HEADER_FRAME_MBS_ONLY` | `18` | `Read/Write` | `` | ` `
[code]
    frame_mbs_only_flag
    
[/code]
|   
`MACC_H264_SEQ_HEADER_MB_ADAPTIVE` | `17` | `Read/Write` | `` | ` `
[code]
    mb_adaptive_frame_field_flag
    
[/code]
|   
`MACC_H264_SEQ_HEADER_DIRECT_8X8` | `16` | `Read/Write` | `` | ` `
[code]
    direct_8x8_inference_flag
    
[/code]
|   
`MACC_H264_SEQ_HEADER_PIC_WIDTH` | `15:8` | `Read/Write` | `` | ` `
[code]
    pic_width_in_mbs_minus1
    
[/code]
| Width in macroblocks - 1   
`MACC_H264_SEQ_HEADER_PIC_HEIGHT` | `7:0` | `Read/Write` | `` | ` `
[code]
    pic_height_in_map_units_minus1
    
[/code]
| Height in map units - 1   
## MACC_H264_PIC_HDR
Default value: 0x00000000  
Offset: 0x0204 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:16` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_PIC_HDR_ENTROPY_CODING` | `15` | `Read/Write` | `` | ` `
[code]
    entropy_coding_mode_flag
    
[/code]
|   
`MACC_H264_PIC_HDR_NUM_REF_IDX_L0` | `14:10` | `Read/Write` | `` | ` `
[code]
    num_ref_idx_l0_default_active_minus1
    
[/code]
|   
`MACC_H264_PIC_HDR_NUM_REF_IDX_L1` | `9:5` | `Read/Write` | `` | ` `
[code]
    num_ref_idx_l1_default_active_minus1
    
[/code]
|   
`MACC_H264_PIC_HDR_WEIGHTED_PRED` | `4` | `Read/Write` | `` | ` `
[code]
    weighted_pred_flag
    
[/code]
|   
`MACC_H264_PIC_HDR_WEIGHTED_BIPRED` | `3:2` | `Read/Write` | `` | ` `
[code]
    weighted_bipred_idc
    
[/code]
|   
`MACC_H264_PIC_HDR_CONST_INTRA_PRED` | `1` | `Read/Write` | `` | ` `
[code]
    constrained_intra_pred_flag
    
[/code]
|   
`MACC_H264_PIC_HDR_TRANSFORM_8X8` | `0` | `Read/Write` | `` | ` `
[code]
    transform_8x8_mode_flag
    
[/code]
|   
## MACC_H264_SLICE_HDR
Default value: 0x00000000  
Offset: 0x0208 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_SLICE_HDR_FIRST_MB_X` | `31:24` | `Read/Write` | `` | ` `
[code]
    first_mb_in_slice % pic_width_in_mbs
    
[/code]
| First Macroblock in slice (x-coordinate)   
`MACC_H264_SLICE_HDR_FIRST_MB_Y` | `23:16` | `Read/Write` | `` | ` `
[code]
    first_mb_in_slice / pic_width_in_mbs
    ( * 2 if mbaff)
    
[/code]
| First Macroblock in slice (y-coordinate)   
`` | `15:13` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_SLICE_HDR_IS_REFERENCE` | `12` | `Read/Write` | `` | ` `
[code]
    0 = no reference
    1 = reference
    
[/code]
| This frame will be used as reference   
`MACC_H264_SLICE_HDR_TYPE` | `11:8` | `Read/Write` | `` | ` `
[code]
    0x0 = P
    0x1 = B
    0x2 = I
    
[/code]
| Slice type   
`` | `7:6` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_SLICE_HDR_FIRST_IN_PICTURE` | `5` | `Read/Write` | `` | ` `
[code]
    0 = further
    1 = first
    
[/code]
| First slice in Picture   
`MACC_H264_SLICE_HDR_FIELD_PIC` | `4` | `Read/Write` | `` | ` `
[code]
    field_pic_flag
    
[/code]
|   
`MACC_H264_SLICE_HDR_BOTTOM_FIELD` | `3` | `Read/Write` | `` | ` `
[code]
    bottom_field_flag
    
[/code]
|   
`MACC_H264_SLICE_HDR_DIRECT_SPAT_MV_PRED` | `2` | `Read/Write` | `` | ` `
[code]
    direct_spatial_mv_pred_flag
    
[/code]
|   
`MACC_H264_SLICE_HDR_CABAC_INIT` | `1:0` | `Read/Write` | `` | ` `
[code]
    cabac_init_idc
    
[/code]
|   
## MACC_H264_SLICE_HDR2
Default value: 0x00000000  
Offset: 0x020c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:29` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_SLICE_HDR_NUM_REF_IDX_L0` | `28:24` | `Read/Write` | `` | ` `
[code]
    num_ref_idx_l0_active_minus1
    
[/code]
| only used if override flag is set   
`` | `23:21` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_SLICE_HDR_NUM_REF_IDX_L1` | `20:16` | `Read/Write` | `` | ` `
[code]
    num_ref_idx_l1_active_minus1
    
[/code]
| only used if override flag is set   
`` | `15:13` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_SLICE_HDR_NUM_REF_IDX_OVERRIDE` | `12` | `Read/Write` | `` | ` `
[code]
    num_ref_idx_active_override_flag
    
[/code]
|   
`` | `11:10` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_SLICE_HDR_DEBLOCKING` | `9:8` | `Read/Write` | `` | ` `
[code]
    disable_deblocking_filter_idc
    
[/code]
|   
`MACC_H264_SLICE_HDR_ALPHA_OFFSET` | `7:4` | `Read/Write` | `` | ` `
[code]
    slice_alpha_c0_offset_div2
    
[/code]
|   
`MACC_H264_SLICE_HDR_BETA_OFFSET` | `3:0` | `Read/Write` | `` | ` `
[code]
    slice_beta_offset_div2
    
[/code]
|   
## MACC_H264_PRED_WEIGHT
Default value:   
Offset: 0x0210 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:7` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_PRED_WEIGHT_CHROMA_DENOM` | `6:4` | `Read/Write` | `` | ` `
[code]
    chroma_log2_weight_denom
    
[/code]
|   
`` | `3` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_PRED_WEIGHT_LUMA_DENOM` | `2:0` | `Read/Write` | `` | ` `
[code]
    luma_log2_weight_denom
    
[/code]
|   
## MACC_H264_VP8_HDR
Default value:   
Offset: 0x0214 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_FRAME_TYPE` | `31` | `Read/Write` | `` | ` `
[code]
       0 = KEY_FRAME
       1 = INTER_FRAME
      
    
[/code]
| current frame_type   
`MACC_H264_LAST_FRAME_SHARPNESS_LEVEL` | `30:28` | `Read/Write` | `` | `` | last frame sharpness_level   
`MACC_H264_LAST_FRAME_TYPE` | `27` | `Read/Write` | `` | ` `
[code]
       0 = KEY_FRAME
       1 = INTER_FRAME
      
    
[/code]
| last frame frame_type   
`MACC_H264_REF_FRAME_SIGN_BIAS_ALTREF_FRAME` | `26` | `Read/Write` | `` | `` | ref_frame_sign_bias for ALTREF_FRAME   
`MACC_H264_REF_FRAME_SIGN_BIAS_GOLDEN_FRAME` | `25` | `Read/Write` | `` | `` | ref_frame_sign_bias for GOLDEN_FRAME   
`` | `24` | `Read/Write` | `` | `` | reload_entropy_probs, allways set to 1   
`MACC_H264_REFRESH_ENTROPY_PROBS` | `23` | `Read/Write` | `` | `` | refresh_entropy_probs   
`MACC_H264_MB_NO_COEFF_SKIP` | `22` | `Read/Write` | `` | `` | mb_no_coeff_skip   
`MACC_H264_TOKEN_PARTITION_NUMBER` | `21:20` | `Read/Write` | `` | ` `
[code]
       0 = ONE_PARTITION
       1 = TWO_PARTITION
       2 = FOUR_PARTITION
       3 = EIGHT_PARTITION
      
    
[/code]
| number of token partitions   
`MACC_H264_MODE_REF_LF_DELTA_UPDATE` | `19` | `Read/Write` | `` | `` | mode_ref_lf_delta_update   
`MACC_H264_MODE_REF_LF_DELTA_ENABLED` | `18` | `Read/Write` | `` | `` | mode_ref_lf_delta_enabled   
`MACC_H264_FILTER_LEVEL` | `17:12` | `Read/Write` | `` | `` | current frame filter_level   
`MACC_H264_FILTER_TYPE` | `11` | `Read/Write` | `` | ` `
[code]
       0 = NORMAL_LOOPFILTER
       1 = SIMPLE_LOOPFILTER
      
    
[/code]
| current frame filter_type   
`MACC_H264_SHARPNESS_LEVEL` | `10:8` | `Read/Write` | `` | `` | sharpness_level   
`MACC_H264_LAST_FRAME_FILTER_TYPE` | `7` | `Read/Write` | `` | ` `
[code]
       0 = NORMAL_LOOPFILTER
       1 = SIMPLE_LOOPFILTER
      
    
[/code]
| last frame filter_type   
`MACC_H264_SEGMENTATION_ENABLED` | `6` | `Read/Write` | `` | `` | segmentation_enabled   
`MACC_H264_MB_SEGMENT_ABS_DELTA` | `5` | `Read/Write` | `` | `` | mb_segement_abs_delta   
`MACC_H264_UPDATE_MB_SEGMENTATION_MAP` | `4` | `Read/Write` | `` | `` | update_mb_segmentation_map   
`MACC_H264_FULL_PIXEL` | `3` | `Read/Write` | `` | `` | full_pixel (VP8 version)   
`MACC_H264_USE_BILLENAR_MC_FILTER` | `2` | `Read/Write` | `` | `` | use_billenar_mc_filter (VP8 version)   
`MACC_H264_FILTER_TYPE` | `1` | `Read/Write` | `` | ` `
[code]
       0 = NORMAL_LOOPFILTER
       1 = SIMPLE_LOOPFILTER
      
    
[/code]
| filter_type (VP8 version)   
`MACC_H264_NO_LPF` | `0` | `Read/Write` | `` | `` | no_lpf (VP8 version)   
## MACC_H264_QINDEX
Default value:   
Offset: 0x0218 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_UVAC_DELTA_Q` | `31:27` | `Read/Write` | `` | `` | uvac_delta_q   
`MACC_H264_UVDC_DELTA_Q` | `26:22` | `Read/Write` | `` | `` | uvdc_delta_q   
`MACC_H264_Y2AC_DELTA_Q` | `21:17` | `Read/Write` | `` | `` | y2ac_delta_q   
`MACC_H264_Y2DC_DELTA_Q` | `16:12` | `Read/Write` | `` | `` | y2dc_delta_q   
`MACC_H264_Y1DC_DELTA_Q` | `11:7` | `Read/Write` | `` | `` | y1dc_delta_q   
`MACC_H264_BASE_QINDEX` | `6:0` | `Read/Write` | `` | `` | base_qindex   
## MACC_H264_QP
Default value: 0x00000000  
Offset: 0x021c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:25` | `Read/Write` | `` | `` | unknown   
`MACC_H264_QP_DEFAULT_SCALING_MATRIX` | `24` | `Read/Write` | `` | ` `
[code]
    0 = custom
    1 = default
    
[/code]
| scaling matrix to use   
`` | `23:22` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_QP_SECOND_CHROMA_QP_OFFSET` | `21:16` | `Read/Write` | `` | ` `
[code]
    second_chroma_qp_index_offset
    
[/code]
|   
`` | `15:14` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_QP_CHROMA_QP_OFFSET` | `13:8` | `Read/Write` | `` | ` `
[code]
    chroma_qp_index_offset
    
[/code]
|   
`` | `7:6` | `Read/Write` | `` | `` | _reserved_  
`MACC_H264_QP_PARAM` | `5:0` | `Read/Write` | `` | ` `
[code]
    pic_init_qp + slice_qp_delta
    
[/code]
|   
## MACC_H264_CTRL
Default value:   
Offset: 0x0220 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:30` | `Read/Write` | `` | `` | reserved5   
`` | `29` | `Read/Write` | `` | `` | isVP8Dec   
`` | `28` | `Read/Write` | `` | `` | isAVS   
`` | `27` | `Read/Write` | `` | `` | reserved4   
`` | `26` | `Read/Write` | `` | `` | AVS_Demulate_Enable   
`MACC_H264_CTRL_STARTCODE_DETECT_EN` | `25` | `Read/Write` | `` | ` `
[code]
    0 = disabled
    1 = enabled
    
[/code]
| Enable start code detection   
`` | `24` | `Read/Write` | `` | `` | eptb_detection_bypass   
`` | `14:23` | `Read/Write` | `` | `` | reserved0   
`MACC_H264_CTRL_HISTOGRAM_EN` | `13` | `Read/Write` | `` | ` `
[code]
    0 = disabled
    1 = enabled
    
[/code]
| Enable luma histogram output (see [MACC_VE_LUMA_HIST_VAL[0-15]][58193])   
`` | `11:12` | `Read/Write` | `` | `` | reserved1   
`` | `10` | `Read/Write` | `` | `` | mcri_cache_enable   
`MACC_H264_CTRL_EXTRA_OUTPUT_ENABLE` | `9` | `Read/Write` | `` | `` | enable writing extra output picture   
`MACC_H264_CTRL_WRITE_REC_DISABLE` | `8` | `Read/Write` | `` | `` | disable writing of reconstructed picture   
`` | `3:7` | `Read/Write` | `` | `` | reserved0   
`` | `2` | `Read/Write` | `` | `` | vld_data_req_int_en IRQ   
`` | `1` | `Read/Write` | `` | `` | dec_error_int_en IRQ   
`` | `0` | `Read/Write` | `` | `` | slice_dec_finish_int_en IRQ   
## MACC_H264_TRIG
Default value:   
Offset: 0x0224 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:8` | `Read/Write` | `` | `` | Parameter , n_bits   
`` | `7:6` | `Read/Write` | `` | `` | reserved   
`` | `5:4` | `Read/Write` | `` | `` | stcd_type   
`MACC_H264_TRIG_FUNCTION` | `3:0` | `Read/Write` | `` | ` `
[code]
    0x0 = ?
    0x1 = ?
    0x2 = read basic bits
    0x3 = ?
    0x4 = read exp-golomb coded signed integer
    0x5 = read exp-golomb coded unsigned integer
    0x6 = ?
    0x7 = ? (maybe reset or init)
    0x8 = start decoding one H.264 slice
    0x9 = ?
    0xa = start decoding VP8 frame
    ... = ?
    0xe = start reading coef_probs to entropy 
          probabilities table using VP8 bool decoder
    0xf = read bits to MACC_H264_BASIC_BITS_DATA
          using VP8 bool decoder, where 
              31:24 - probability
              18:16 - (bits_count - 1)
    
[/code]
| Function   
## MACC_H264_STATUS
Default value:   
Offset: 0x0228 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31` | `Read/Write` | `` | `` | startcode detected   
`` | `30:28` | `Read/Write` | `` | `` | start code type   
`` | `27` | `Read/Write` | `` | `` | stcd_busy   
`` | `26` | `Read/Write` | `` | `` | _reserved_  
`` | `25` | `Read/Write` | `` | `` | avs_idct_busy   
`` | `24` | `Read/Write` | `` | `` | avs_busy   
`` | `23` | `Read/Write` | `` | `` | wb_busy   
`` | `22` | `Read/Write` | `` | `` | bs_dma_busy   
`` | `21` | `Read/Write` | `` | `` | it_busy   
`` | `20` | `Read/Write` | `` | `` | intram_busy   
`` | `19` | `Read/Write` | `` | `` | _reserved_  
`` | `18` | `Read/Write` | `` | `` | vp8_busy   
`` | `17` | `Read/Write` | `` | `` | vp8_upprob_busy   
`` | `16` | `Read/Write` | `` | `` | more_data_flag   
`` | `15` | `Read/Write` | `` | `` | dblk_busy   
`` | `14` | `Read/Write` | `` | `` | irec_busy   
`` | `13` | `Read/Write` | `` | `` | intra_pred_busy   
`` | `12` | `Read/Write` | `` | `` | mcri_busy   
`` | `11` | `Read/Write` | `` | `` | iq_it_bust   
`` | `10` | `Read/Write` | `` | `` | mvp_busy   
`` | `9` | `Read/Write` | `` | `` | is_busy   
`` | `8` | `Read/Write` | `` | `` | vld_busy   
`` | `7:4` | `Read/Write` | `` | `` | _reserved_  
`` | `3` | `Read/Write` | `` | `` | over_time_interrupt   
`` | `2` | `Read/Write` | `` | `` | vld_data_req_interrupt   
`` | `1` | `Read/Write` | `` | `` | decode_error_interrupt   
`` | `0` | `Read/Write` | `` | `` | slice_decode_finish_interrupt   
## MACC_H264_CUR_MBNUM
Default value:   
Offset: 0x022c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_CUR_MBNUM` | `31:0` | `Read/Write` | `` | `` | current decoded macroblock nr.   
## MACC_H264_VLD_ADDR
Default value:   
Offset: 0x0230 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31` | `Read/Write` | `` | `` | _reserved_  
`` | `30` | `Read/Write` | `` | ` `
[code]
    0x1 for h.264 and VP8
    
[/code]
| first_slice_data   
`` | `29` | `Read/Write` | `` | ` `
[code]
    0x1 for h.264 and VP8
    
[/code]
| last_slice_data   
`` | `28` | `Read/Write` | `` | ` `
[code]
    0x1 for h.264 and VP8
    
[/code]
| slice_data_valid   
`` | `27:4` | `Read/Write` | `` | ` `
[code]
    27:4 VLD Address bits
    
[/code]
| VLD Address LOW bits (four first bits dropped from address)   
`` | `3:0` | `Read/Write` | `` | ` `
[code]
    31:28 VLD Address bits (for addesses beyond 256 MB)
    
[/code]
| VLD Address HI bits   
## MACC_H264_VLD_OFFSET
Default value:   
Offset: 0x0234 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_VLD_OFFSET` | `31:0` | `Read/Write` | `` | `` | VLD Offset in bits   
## MACC_H264_VLD_LEN
Default value:   
Offset: 0x0238 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_VLD_LEN` | `31:0` | `Read/Write` | `` | `` | VLD Length in bits   
## MACC_H264_VLD_END
Default value:   
Offset: 0x023c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MAC_H264_VLD_END` | `31:0` | `Read/Write` | `` | `` | VLD End Address   
## MACC_H264_SDROT_CTRL
Default value:   
Offset: 0x0240 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `14:31` | `Read/Write` | `` | `` | r0   
`` | `13` | `Read/Write` | `` | `` | bottom_field_sel   
`` | `12` | `Read/Write` | `` | `` | field_scale_mode   
`` | `8:11` | `Read/Write` | `` | `` | scale_precision   
`` | `3:7` | `Read/Write` | `` | `` | r1   
`` | `0:2` | `Read/Write` | `` | `` | rot_angle   
## MACC_H264_OUTPUT_FRAME_INDEX
Default value:   
Offset: 0x024c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MAC_H264_OUTPUT_FRAME_INDEX` | `31:0` | `Read/Write` | `` | `` | Output frame index in dpb   
## MACC_H264_VP8_ENTROPY_PROBS
Default value:   
Offset: 0x024c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MAC_H264_ENTROPY_PROBS_TABLE_ADDRESS` | `31:0` | `Read/Write` | `` | `` | Entropy probabilities table address   
Size of entropy probabilities table is defined as 0x2400, but only first 0x11b0 bytes are used.  
The table contents buffer is null'ed after allocation and reused for every decoded frame.  
Memory layout of entropy probabilities table: 
[code] 
     0x000  - 0x7ff : coef_probs (BLOCK_TYPES are 512 bytes aligned,
                                  COEF_BANDS are 64 bytes aligned,
                                  PREV_COEF_CONTEXTS are 16 bytes aligned)
     0x800  - 0xfff : vp8_coef_update_probs (BLOCK_TYPES are 512 bytes aligned,
                                             COEF_BANDS are 64 bytes aligned,
                                             PREV_COEF_CONTEXTS are 16 bytes aligned)
     0x1000 - 0x1003: vp8_kf_ymode_prob
     0x1008 - 0x100b: ymode_prob
     0x1010 - 0x1012: uv_mode_prob or vp8_kf_uv_mode_prob depending on frame type
     0x1018 - 0x101a: mb_segment_tree_probs
     0x101c         : prob_skip_false
     0x101d         : prob_intra
     0x101e         : prob_last
     0x101f         : prob_gf
     0x1020 - 0x1032: mvc[0].prob
     0x1040 - 0x1052: mvc[1].prob
     0x1060 - 0x1062: vp8_mbsplit_probs
     0x1068 - 0x1070: vp8_bmode_prob
     0x1088 - 0x109b: vp8_sub_mv_ref_prob2 (4 bytes aligned)
     0x10a8 - 0x10bf: vp8_mode_contexts (4 bytes aligned)
     0x1100 - 0x1107: vp8_kf_ymode_tree
     0x1108 - 0x110f: vp8_ymode_tree
     0x1110 - 0x1115: vp8_uv_mode_tree
     0x1122 - 0x112f: vp8_small_mvtree
     0x1142 - 0x114f: vp8_small_mvtree (again)
     0x1160 - 0x1165: vp8_mbsplit_tree
     0x1168 - 0x1179: vp8_bmode_tree
     0x1188 - 0x118d: vp8_sub_mv_ref_tree
     0x11a8 - 0x11af: vp8_mv_ref_tree
    
[/code]
All trees should be in signed magnitude representation, e.g. 
[code] 
     table[0x1168] = (vp8_bmode_tree[0] <= 0)?(128-vp8_bmode_tree[0]):vp8_bmode_tree[0];
    
[/code]
## MACC_H264_VP8_FSTDATA_PARTLEN
Default value:   
Offset: 0x0254 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:28` | `Read/Write` | `` | `` | _reserved_  
`` | `27:0` | `Read/Write` | `` | `` | First partition length in bits   
## MACC_H264_PIC_MBSIZE
Default value:   
Offset: 0x0258 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:16` | `Read/Write` | `` | `` | unknown   
`MAC_H264_HORIZONTAL_MACROBLOCK_COUNT` | `15:8` | `Read/Write` | `` | `` | VP8: number of horizontal macroblocks (Y dimensions)   
`MAC_H264_VERTICAL_MACROBLOCK_COUNT` | `7:0` | `Read/Write` | `` | `` | VP8: number of vertical macroblocks (Y dimensions)   
For VP8: 
[code] 
     MAC_H264_HORIZONTAL_MACROBLOCK_COUNT = (frame_width + 15)/16
     MAC_H264_VERTICAL_MACROBLOCK_COUNT = (frame_height + 15)/16
    
[/code]
## MACC_H264_PIC_BOUNDARYSIZE
Default value:   
Offset: 0x025c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MAC_H264_PICTURE_WIDTH` | `31:16` | `Read/Write` | `` | `` | Picture width in pixels   
`MAC_H264_PICTURE_HEIGHT` | `15:0` | `Read/Write` | `` | `` | Picture height in pixels   
## MACC_H264_MB_ADDR
Default value:   
Offset: 0x0260 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:16` | `Read/Write` | `` | `` | unknown   
`MAC_H264_HORIZONTAL_MACROBLOCK_POSITION` | `15:8` | `Read/Write` | `` | `` | current decoded macroblock horizontal position   
`MAC_H264_VERTICAL_MACROBLOCK_POSITION` | `7:0` | `Read/Write` | `` | `` | current decoded macroblock vertical position   
## MACC_H264_REC_LUMA
Default value:   
Offset: 0x02ac 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Reconstruct Buffer luma color component   
## MACC_H264_FWD_LUMA
Default value:   
Offset: 0x02b0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Forward prediction buffer (last frame buffer for VP8) luma color component   
## MACC_H264_BACK_LUMA
Default value:   
Offset: 0x02b4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Back buffer (golden frame buffer for VP8) luma color component   
## MACC_H264_ERROR
Default value:   
Offset: 0x02b8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:4` | `Read/Write` | `` | `` | _reserved_  
`` | `3` | `Read/Write` | `` | `` | block_error   
`` | `2` | `Read/Write` | `` | `` | ref_idx_error   
`` | `1` | `Read/Write` | `` | `` | mbh_error   
`` | `0` | `Read/Write` | `` | `` | no_more_data_error   
## MACC_H264_REC_CHROMA
Default value:   
Offset: 0x02d0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Reconstruct buffer chroma color component   
## MACC_H264_FWD_CHROMA
Default value:   
Offset: 0x02d4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Forward prediction buffer (last frame buffer for VP8) chroma color component   
## MACC_H264_BACK_CHROMA
Default value:   
Offset: 0x02d8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Back buffer (golden frame buffer for VP8) chroma color component   
## MACC_H264_BASIC_BITS_DATA
Default value:   
Offset: 0x02dc 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | unknown   
## MACC_H264_RAM_WRITE_PTR
Default value:   
Offset: 0x02e0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_RAM_WRITE_PTR` | `31:0` | `Read/Write` | `` | `` | relative (to?) address to write to (auto incrementing)   
## MACC_H264_RAM_WRITE_DATA
Default value:   
Offset: 0x2e4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_RAM_WRITE_DATA` | `31:0` | `Read/Write` | `` | `` | Data to write to VE-SRAM at address pointed to by MACC_H264_RAM_WRITE_PTR   
Memory layout for h.264 decoding: 
[code] 
    0x000 - 0x2ff: Prediction weight table
    0x400 - 0x63f: Framebuffer list
    0x640 - ?    : Reference Picture list 0
    0x664 - ?    : Reference Picture list 1
    0x800 - 0x8df: Scaling lists
    
[/code]
Prediction weight table: 
[code] 
    uint32_t luma_l0[32];
    uint32_t chroma_l0[32][2];
    uint32_t luma_l1[32];
    uint32_t chroma_l1[32][2];
    
    each has bit 24:16 = signed offset
             bit 8:0 = signed weight
    
[/code]
Framebuffer list: 
[code] 
    struct {
       uint32_t top_pic_order_cnt;
       uint32_t bottom_pic_order_cnt;
       uint32_t flags; // bit 0-1: top ref type: 0x0 = short, 0x1 = long, 0x2 = no ref
                       // bit 4-5: bottom ref type:  0x0 = short, 0x1 = long, 0x2 = no ref
                       // bit 8-9: picture type: 0x0 = frame, 0x1 = field, 0x2 = mbaff
       uint32_t luma_addr;
       uint32_t chroma_addr;
       uint32_t extra_buffer_top_addr;    // prediction buffers?
       uint32_t extra_buffer_bottom_addr; // size = pic_width_in_mbs * pic_height_in_mbs * 32
       uint32_t unknown; // = 0x0
    } framebuffer_list[18];
    
[/code]
Reference Picture lists: 
[code] 
    uint8_t ref_picture[?]; // (index to framebuffer list) * 2 + (bottom_field ? 1 : 0)
    
[/code]
Scaling lists: 
[code] 
    uint8_t ScalingList8x8[2][64];
    uint8_t ScalingList4x4[6][16];
    
[/code]
## MACC_H264_ALT_LUMA
Default value:   
Offset: 0x02e8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Alternative buffer (altref frame buffer for VP8) luma color component   
## MACC_H264_ALT_CHROMA
Default value:   
Offset: 0x02ec 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:0` | `Read/Write` | `` | `` | Alternative buffer (altref frame buffer for VP8) chroma color component   
## MACC_H264_SEG_MB_LV0
Default value:   
Offset: 0x02f0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_SEGMENT_MB_LV0_4` | `31:24` | `Read/Write` | `` | `` | segment_feature_data[0][3]   
`MACC_H264_SEGMENT_MB_LV0_3` | `23:16` | `Read/Write` | `` | `` | segment_feature_data[0][2]   
`MACC_H264_SEGMENT_MB_LV0_2` | `15:8` | `Read/Write` | `` | `` | segment_feature_data[0][1]   
`MACC_H264_SEGMENT_MB_LV0_1` | `7:0` | `Read/Write` | `` | `` | segment_feature_data[0][0]   
## MACC_H264_SEG_MB_LV1
Default value:   
Offset: 0x02f4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_SEGMENT_MB_LV1_4` | `31:24` | `Read/Write` | `` | `` | segment_feature_data[1][3]   
`MACC_H264_SEGMENT_MB_LV1_3` | `23:16` | `Read/Write` | `` | `` | segment_feature_data[1][2]   
`MACC_H264_SEGMENT_MB_LV1_2` | `15:8` | `Read/Write` | `` | `` | segment_feature_data[1][1]   
`MACC_H264_SEGMENT_MB_LV1_1` | `7:0` | `Read/Write` | `` | `` | segment_feature_data[1][0]   
## MACC_H264_REF_LF_DELTA
Default value:   
Offset: 0x02f8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_REF_LF_DELTA_4` | `30:24` | `Read/Write` | `` | `` | ref_lf_deltas[3]   
`MACC_H264_REF_LF_DELTA_3` | `22:16` | `Read/Write` | `` | `` | ref_lf_deltas[2]   
`MACC_H264_REF_LF_DELTA_2` | `14:8` | `Read/Write` | `` | `` | ref_lf_deltas[1]   
`MACC_H264_REF_LF_DELTA_1` | `6:0` | `Read/Write` | `` | `` | ref_lf_deltas[0]   
## MACC_H264_MODE_LF_DELTA
Default value:   
Offset: 0x02fc 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`MACC_H264_MODE_LF_DELTA_4` | `30:24` | `Read/Write` | `` | `` | mode_lf_deltas[3]   
`MACC_H264_MODE_LF_DELTA_3` | `22:16` | `Read/Write` | `` | `` | mode_lf_deltas[2]   
`MACC_H264_MODE_LF_DELTA_2` | `14:8` | `Read/Write` | `` | `` | mode_lf_deltas[1]   
`MACC_H264_MODE_LF_DELTA_1` | `6:0` | `Read/Write` | `` | `` | mode_lf_deltas[0]   
# HEVC Engine Register
## MACC_HEVC_NAL_HDR
Offset | `0x500`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:9` | `RW` | `` |  | _reserved_  
`MACC_HEVC_NAL_HDR_TYPE` | `?:0` | `RW` | `` | 
[code]
    nal_unit_type
[/code]
|   
## MACC_HEVC_SPS
Offset | `0x504`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:27` | `RW` | `` |  | _reserved_  
`` | `26` | `RW` | `` | 
[code]
    strong_intra_smoothing_enabled_flag
[/code]
|   
`` | `25` | `RW` | `` | 
[code]
    sps_temporal_mvp_enabled_flag
[/code]
|   
`` | `24` | `RW` | `` | 
[code]
    sample_adaptive_offset_enabled_flag
[/code]
|   
`` | `23` | `RW` | `` | 
[code]
    amp_enabled_flag
[/code]
|   
`` | `22:20` | `RW` | `` | 
[code]
    max_transform_hierarchy_depth_intra
[/code]
|   
`` | `19:17` | `RW` | `` | 
[code]
    max_transform_hierarchy_depth_inter
[/code]
|   
`` | `16:15` | `RW` | `` | 
[code]
    log2_diff_max_min_transform_block_size
[/code]
|   
`` | `14:13` | `RW` | `` | 
[code]
    log2_min_transform_block_size_minus2
[/code]
|   
`` | `12:11` | `RW` | `` | 
[code]
    log2_diff_max_min_luma_coding_block_size
[/code]
|   
`` | `10:9` | `RW` | `` | 
[code]
    log2_min_luma_coding_block_size_minus3
[/code]
|   
`` | `8:2` | `RW` | `` |  | _unknown_  
`` | `1:0` | `RW` | `` | 
[code]
    chroma_format_idc
[/code]
|   
## MACC_HEVC_PIC_SIZE
Offset | `0x508`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:30` | `RW` | `` |  | _reserved_  
`MACC_HEVC_PIC_SIZE_HEIGHT` | `29:16` | `RW` | `` | 
[code]
    pic_height_in_luma_samples
[/code]
|   
`` | `15:14` | `RW` | `` |  | _reserved_  
`MACC_HEVC_PIC_SIZE_WIDTH` | `13:0` | `RW` | `` | 
[code]
    pic_width_in_luma_samples
[/code]
|   
## MACC_HEVC_PCM_HDR
Offset | `0x50c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:16` | `RW` | `` |  | _reserved_  
`` | `15` | `RW` | `` | 
[code]
    pcm_enabled_flag
[/code]
|   
`` | `14` | `RW` | `` |  | _unknown_  
`` | `13:12` | `RW` | `` |  | _reserved_  
`` | `11:10` | `RW` | `` | 
[code]
    log2_diff_max_min_pcm_luma_coding_block_size
[/code]
|   
`` | `9:8` | `RW` | `` | 
[code]
    log2_min_pcm_luma_coding_block_size_minus3
[/code]
|   
`` | `7:4` | `RW` | `` | 
[code]
    pcm_sample_bit_depth_chroma_minus1
[/code]
|   
`` | `3:0` | `RW` | `` | 
[code]
    pcm_sample_bit_depth_luma_minus1
[/code]
|   
## MACC_HEVC_PPS0
Offset | `0x510`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:29` | `RW` | `` |  | _reserved_  
`` | `28:24` | `RW` | `` | 
[code]
    pps_cr_qp_offset
[/code]
|   
`` | `23:21` | `RW` | `` |  | _reserved_  
`` | `20:16` | `RW` | `` | 
[code]
    pps_cb_qp_offset
[/code]
|   
`` | `15:14` | `RW` | `` |  | _reserved_  
`` | `13:8` | `RW` | `` | 
[code]
    init_qp_minus26
[/code]
|   
`` | `7:6` | `RW` | `` |  | _reserved_  
`` | `5:4` | `RW` | `` | 
[code]
    diff_cu_qp_delta_depth
[/code]
|   
`` | `3` | `RW` | `` | 
[code]
    cu_qp_delta_enabled_flag
[/code]
|   
`` | `2` | `RW` | `` | 
[code]
    transform_skip_enabled_flag
[/code]
|   
`` | `1` | `RW` | `` | 
[code]
    constrained_intra_pred_flag
[/code]
|   
`` | `0` | `RW` | `` | 
[code]
    sign_data_hiding_enabled_flag
[/code]
|   
## MACC_HEVC_PPS1
Offset | `0x514`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:11` | `RW` | `` |  | _reserved_  
`` | `10:8` | `RW` | `` | 
[code]
    log2_parallel_merge_level_minus2
[/code]
|   
`` | `7` | `RW` | `` |  | _reserved_  
`` | `6` | `RW` | `` | 
[code]
    pps_loop_filter_across_slices_enabled_flag
[/code]
|   
`` | `5` | `RW` | `` | 
[code]
    loop_filter_across_tiles_enabled_flag
[/code]
|   
`` | `4` | `RW` | `` | 
[code]
    entropy_coding_sync_enabled_flag
[/code]
|   
`` | `3` | `RW` | `` | 
[code]
    tiles_enabled_flag
[/code]
|   
`` | `2` | `RW` | `` | 
[code]
    transquant_bypass_enabled_flag
[/code]
|   
`` | `1` | `RW` | `` | 
[code]
    weighted_bipred_flag
[/code]
|   
`` | `0` | `RW` | `` | 
[code]
    weighted_pred_flag
[/code]
|   
## MACC_HEVC_SCALING_LIST_CTRL
Offset | `0x518`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_HEVC_SCALING_LIST_ENABLED` | `31` | `RW` | `` |  | Enable scaling lists  
`` | `30` | `RW` | `` |  | maybe use default scaling lists  
`` | `29:0` | `RW` | `` |  | _reserved_  
## MACC_HEVC_SLICE_HDR0
Offset | `0x520`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:30` | `RW` | `` |  | _reserved_  
`` | `29:28` | `RW` | `` |  | _unknown_  
`` | `27` | `RW` | `` |  | _reserved_  
`` | `26:24` | `RW` | `` | 
[code]
    five_minus_max_num_merge_cand
[/code]
|   
`MACC_HEVC_SLICE_HDR_NUM_REF_IDX_L1` | `23:20` | `RW` | `` | 
[code]
    num_ref_idx_l1_active_minus1
[/code]
|   
`MACC_HEVC_SLICE_HDR_NUM_REF_IDX_L0` | `19:16` | `RW` | `` | 
[code]
    num_ref_idx_l0_active_minus1
[/code]
|   
`` | `15:12` | `RW` | `` | 
[code]
    collocated_ref_idx
[/code]
|   
`` | `11` | `RW` | `` | 
[code]
    collocated_from_l0_flag
[/code]
|   
`MACC_HEVC_SLICE_HDR_CABAC_INIT` | `10` | `RW` | `` | 
[code]
    cabac_init_flag
[/code]
|   
`MACC_HEVC_SLICE_HDR_MVD_L1_ZERO` | `9` | `RW` | `` | 
[code]
    mvd_l1_zero_flag
[/code]
|   
`MACC_HEVC_SLICE_HDR_SAO_CHROMA` | `8` | `RW` | `` | 
[code]
    slice_sao_chroma_flag
[/code]
|   
`MACC_HEVC_SLICE_HDR_SAO_LUMA` | `7` | `RW` | `` | 
[code]
    slice_sao_luma_flag
[/code]
|   
`` | `6` | `RW` | `` | 
[code]
    slice_temporal_mvp_enabled_flag
[/code]
|   
`` | `5:4` | `RW` | `` |  | _unknown_  
`MACC_HEVC_SLICE_HDR_SLICE_TYPE` | `3:2` | `RW` | `` | 
[code]
    slice_type
[/code]
|   
`` | `1` | `RW` | `` | 
[code]
    dependent_slice_segment_flag
[/code]
|   
`` | `0` | `RW` | `` | 
[code]
    first_slice_segment_in_pic_flag
[/code]
|   
## MACC_HEVC_SLICE_HDR1
Offset | `0x524`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:28` | `RW` | `` | 
[code]
    slice_tc_offset_div2
[/code]
|   
`` | `27:24` | `RW` | `` | 
[code]
    slice_beta_offset_div2
[/code]
|   
`` | `23` | `RW` | `` | 
[code]
    slice_deblocking_filter_disabled_flag
[/code]
|   
`MACC_HEVC_SLICE_HDR_LOOP_FILTER_ACROSS_SLICES` | `22` | `RW` | `` | 
[code]
    slice_loop_filter_across_slices_enabled_flag
[/code]
|   
`` | `21` | `RW` | `` | 
[code]
    NumPocStCurrAfter == 0
[/code]
| _unsure_  
`` | `20:16` | `RW` | `` | 
[code]
    slice_cr_qp_offset
[/code]
|   
`` | `15:13` | `RW` | `` |  | _reserved_  
`` | `12:8` | `RW` | `` | 
[code]
    slice_cb_qp_offset
[/code]
|   
`` | `7:6` | `RW` | `` |  | _reserved_  
`MACC_HEVC_SLICE_HDR_QP_DELTA` | `5:0` | `RW` | `` | 
[code]
    slice_qp_delta
[/code]
|   
## MACC_HEVC_SLICE_HDR2
Offset | `0x528`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:22` | `RW` | `` |  | _reserved_  
`` | `21:8` | `RW` | `` | 
[code]
    num_entry_point_offsets
[/code]
|   
`` | `7` | `RW` | `` |  | _reserved_  
`` | `6:4` | `RW` | `` | 
[code]
    ChromaLog2WeightDenom
[/code]
|   
`` | `3` | `RW` | `` |  | _reserved_  
`` | `2:0` | `RW` | `` | 
[code]
    luma_log2_weight_denom
[/code]
|   
## MACC_HEVC_CTB_ADDR
Offset | `0x52c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:25` | `RW` | `` |  | _reserved_  
`MACC_HEVC_CTB_ADDR_Y` | `24:16` | `RW` | `` |  | start CTB y  
`` | `15:9` | `RW` | `` |  | _reserved_  
`MACC_HEVC_CTB_ADDR_X` | `8:0` | `RW` | `` |  | start CTB x  
## MACC_HEVC_CTRL
Offset | `0x530`  
---|---  
Name | Bits | R/W | Default | Values | Description  
## MACC_HEVC_TRIG
Offset | `0x534`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_HEVC_TRIG_PARA` | `?:8` | `RW` | `` |  | Parameter n  
`MACC_HEVC_TRIG_FUNCTION` | `?:0` | `RW` | `` | 
[code]
    0x0 = ?
    0x1 = ?
    0x2 = read n bits (n <= 32)
    0x3 = skip n bits (n <= 32)
    0x4 = read exp-golomb coded signed integer
    0x5 = read exp-golomb coded unsigned integer
    0x6 = ?
    0x7 = sync
    0x8 = decode H.265 slice
    
[/code]
| Function  
## MACC_HEVC_STATUS
Offset | `0x538`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_HEVC_STATUS_VLD_BUSY` | `8` | `RW` | `` |  | VLD busy  
`MACC_HEVC_STATUS_ERR` | `1` | `RW` | `` |  | decoding error  
`MACC_HEVC_STATUS_DONE` | `0` | `RW` | `` |  | decoding finished  
## MACC_HEVC_CTU_NUM
Offset | `0x53c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
## MACC_HEVC_BITS_ADDR
Offset | `0x540`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_HEVC_BITS_ADDR` | `23:0` | `RW` | `` | 
[code]
    bits 31:8 of address
[/code]
| Bitstream start address  
## MACC_HEVC_BITS_OFFSET
Offset | `0x544`  
---|---  
Name | Bits | R/W | Default | Values | Description  
## MACC_HEVC_BITS_LEN
Offset | `0x548`  
---|---  
Name | Bits | R/W | Default | Values | Description  
## MACC_HEVC_BITS_END_ADDR
Offset | `0x54c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_HEVC_BITS_END_ADDR` | `23:0` | `RW` | `` | 
[code]
    bits 31:8 of address
[/code]
| Bitstream end address  
## MACC_HEVC_EXTRA_OUT_CTRL
Offset | `0x550`  
---|---  
Name | Bits | R/W | Default | Values | Description  
## MACC_HEVC_EXTRA_OUT_LUMA_ADDR
Offset | `0x554`  
---|---  
Name | Bits | R/W | Default | Values | Description  
## MACC_HEVC_EXTRA_OUT_CHROMA_ADDR
Offset | `0x558`  
---|---  
Name | Bits | R/W | Default | Values | Description  
## MACC_HEVC_REC_BUF_IDX
Offset | `0x55c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:5` | `RW` | `` |  | _reserved_  
`MACC_HEVC_REC_BUF_IDX` | `4:0` | `RW` | `` |  | output buffer index in picture list  
## MACC_HEVC_NEIGHBOR_INFO_ADDR
Offset | `0x560`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_HEVC_NEIGHBOR_INFO_ADDR` | `23:0` | `RW` | `` | 
[code]
    bits 31:8 of address
[/code]
| Neighbor info buffer address  
## MACC_HEVC_TILE_LIST_ADDR
Offset | `0x564`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_HEVC_TILE_LIST_ADDR` | `23:0` | `RW` | `` | 
[code]
    bits 31:8 of address
[/code]
| Tile entry point list address  
Points to a list of entry point offsets and tile start/end CTBs 
[code] 
    struct {
       uint32_t entry_point_offset;
       uint32_t zero;
       uint16_t tile_start_ctb_x;
       uint16_t tile_start_ctb_y;
       uint16_t tile_end_ctb_x;
       uint16_t tile_end_ctb_y;
    } tile_list[num_entry_point_offsets];
    
[/code]
## MACC_HEVC_TILE_START_CTB
Offset | `0x568`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:25` | `RW` | `` |  | _reserved_  
`MACC_HEVC_TILE_START_CTB_Y` | `24:16` | `RW` | `` |  | start tile y  
`` | `15:9` | `RW` | `` |  | _reserved_  
`MACC_HEVC_TILE_START_CTB_X` | `8:0` | `RW` | `` |  | start tile x  
## MACC_HEVC_TILE_END_CTB
Offset | `0x56c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:25` | `RW` | `` |  | _reserved_  
`MACC_HEVC_TILE_END_CTB_Y` | `24:16` | `RW` | `` |  | end tile y  
`` | `15:9` | `RW` | `` |  | _reserved_  
`MACC_HEVC_TILE_END_CTB_X` | `8:0` | `RW` | `` |  | end tile x  
## MACC_HEVC_SCALING_LIST_DC_COEF0
Offset | `0x578`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:24` | `RW` | `` | 
[code]
    ScalingListDCCoeff32x32[1]
[/code]
|   
`` | `23:16` | `RW` | `` | 
[code]
    ScalingListDCCoeff32x32[0]
[/code]
|   
`` | `15:8` | `RW` | `` | 
[code]
    ScalingListDCCoeff16x16[1]
[/code]
|   
`` | `7:0` | `RW` | `` | 
[code]
    ScalingListDCCoeff16x16[0]
[/code]
|   
## MACC_HEVC_SCALING_LIST_DC_COEF1
Offset | `0x57c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:24` | `RW` | `` | 
[code]
    ScalingListDCCoeff16x16[5]
[/code]
|   
`` | `23:16` | `RW` | `` | 
[code]
    ScalingListDCCoeff16x16[4]
[/code]
|   
`` | `15:8` | `RW` | `` | 
[code]
    ScalingListDCCoeff16x16[3]
[/code]
|   
`` | `7:0` | `RW` | `` | 
[code]
    ScalingListDCCoeff16x16[2]
[/code]
|   
## MACC_HEVC_BITS_DATA
Offset | `0x5dc`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_HEVC_BITS_DATA` | `31:0` | `RW` | `` |  | Data read from bitstream  
## MACC_HEVC_SRAM_ADDR
Offset | `0x5e0`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:12` | `RW` | `` |  | _reserved_  
`` | `11:0` | `RW` | `` |  | SRAM address to write to (auto incrementing)  
## MACC_HEVC_SRAM_DATA
Offset | `0x5e4`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0` | `RW` | `` |  | Write data to SRAM  
Memory layout for H.265 decoding: 
[code] 
    0x000 - 0x01f  Prediction Weight Luma List 0
    0x020 - 0x05f  Prediction Weight Chroma List 0
    0x060 - 0x07f  Prediction Weight Luma List 1
    0x080 - 0x0bf  Prediction Weight Chroma List 1
    0x400 - 0x7ff  Picture List
    0x800 - 0xbdf  Scaling Lists
    0xc00 - 0xc0f  Reference Picture List 0
    0xc10 - 0xc1f  Reference Picture List 1
    
[/code]
Prediction Weight Luma Lists: 
[code] 
    struct {
       int8_t delta_luma_weight;
       int8_t luma_offset;
    } pred_weight_luma[16];
    
[/code]
Prediction Weight Chroma Lists: 
[code] 
    struct {
       int8_t delta_chroma_weight_cb;
       int8_t ChromaOffset_cb;
       int8_t delta_chroma_weight_cr;
       int8_t ChromaOffset_cr;
    } pred_weight_chroma[16];
    
[/code]
Picture List: 
[code] 
    struct {
       uint32_t pic_order_cnt;
       uint32_t pic_order_cnt;
       uint32_t extra_buffer_addr;
       uint32_t extra_buffer_addr;
       uint32_t luma_addr;
       uint32_t chroma_addr;
       uint32_t reserved;
       uint32_t reserved;
    } picture_list[32];
    
[/code]
Scaling Lists (in horizontal scan order): 
[code] 
    struct {
       uint8_t ScalingList8x8[6][64];
       uint8_t ScalingList32x32[2][64];
       uint8_t ScalingList16x16[6][64];
       uint8_t ScalingList4x4[6][16];
    } scaling_lists;
    
[/code]
Reference Picture Lists: 
[code] 
    uint8_t ref_picture[16]; // index to picture list (set bit7 for longterm reference)
    
[/code]
# ISP Engine Registers
## MACC_ISP_PIC_SIZE
Offset | `0xa00`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_ISP_PIC_SIZE_WIDTH ` | `26:16` | `RW` | `` |  | width of source picture in macroblocks  
`MACC_ISP_PIC_SIZE_HEIGHT` | `10:0 ` | `RW` | `` |  | height of source picture in macroblocks  
## MACC_ISP_PIC_STRIDE
Offset | `0xa04`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_ISP_PIC_STRIDE ` | `26:16` | `RW` | `` |  | stride of source picture in macroblocks  
`MACC_ISP_OUTPIC_STRIDE` | `10:0 ` | `RW` | `` |  | stride of output picture in macroblocks  
## MACC_ISP_CTRL
Offset | `0xa08`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_ISP_CTRL_COLOR_FORMAT` | `31:29` | `RW` | `` | 
[code]
    0x0 = nv12
    0x1 = nv16
    0x2 = tile32x32
    0x3 = nv16?
    0x4 = BGGR
    0x5 = RGGB
    0x6 = GBRG
    0x7 = GRBG
    
[/code]
| Source picture color format  
`MACC_ISP_CTRL_COLOR_SPACE ` | ` 28 ` | `RW` | `` | 
[code]
    ? = BT601
    ? = BT709
    
[/code]
| RGB to YCbCr color transformation mode  
`MACC_ISP_CTRL_? ` | `27:25` | `RW` | `` | 
[code]
    0x0 = /1    0x4 = /1
    0x1 = ?     0x5 = ? 
    0x2 = /2    0x6 = /2
    0x3 = /4    0x7 = /4
    
[/code]
| Output picture dimensions division factor  
`MACC_ISP_CTRL_? ` | ` 24 ` | `RW` | `` | 
[code]
    0 = nv12
    1 = nv16
    
[/code]
| Output picture color format  
`MACC_ISP_CTRL_OUTPUT_EN ` | ` 19 ` | `RW` | `` |  | Enable output  
`MACC_ISP_CTRL_SCALER_EN ` | ` 16 ` | `RW` | `` |  | Enable scaler/Clear IRQ status  
`MACC_ISP_CTRL_IRQ_EN ` | ` 0 ` | `RW` | `` |  | Enable IRQ from ISP  
## MACC_ISP_TRIG
Offset | `0xa0c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_ISP_TRIG_FUNCTION` | ` 3:0 ` | `RW` | `` | 
[code]
    1 = launch
[/code]
| Function  
## MACC_ISP_SCALER_SIZE
Offset | `0xa2c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_ISP_SCALER_SIZE_HEIGHT` | `15:8 ` | `RW` | `` |  | scale picture to height macroblocks  
`MACC_ISP_SCALER_SIZE_WIDTH ` | ` 7:0 ` | `RW` | `` |  | scale picture to width macroblocks  
## MACC_ISP_SCALER_OFFSET_Y
Offset | `0xa30`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_ISP_SCALER_Y_OFFSET` | `31:16` | `RW` | `` |  | picture luma y position  
`MACC_ISP_SCALER_X_OFFSET` | `15:0 ` | `RW` | `` | 
[code]
    0x0080 = 0.5 pixels
[/code]
| picture luma x position  
## MACC_ISP_SCALER_OFFSET_C
Offset | `0xa34`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_ISP_SCALER_Y_OFFSET` | `31:16` | `RW` | `` |  | picture chroma y position  
`MACC_ISP_SCALER_X_OFFSET` | `15:0 ` | `RW` | `` | 
[code]
    0x0080 = 0.5 pixels
[/code]
| picture chroma x position  
## MACC_ISP_SCALER_FACTOR
Offset | `0x038`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`MACC_ISP_SCALER_Y_FACTOR` | `23:12` | `RW` | `` |  | y scale factor  
`MACC_ISP_SCALER_X_FACTOR` | `11:0 ` | `RW` | `` | 
[code]
    0x080 = 2x
    0x100 = 1x
    0x200 = 0.5x
    
[/code]
| x scale factor  
  

## MACC_ISP_OUTPUT_LUMA
Offset | `0xa70`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0` | `RW` | `` |  | Output picture luma address.  
## MACC_ISP_OUTPUT_CHROMA
Offset | `0xa74`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0` | `RW` | `` |  | Output picture chroma address.  
## MACC_ISP_WB_THUMB_LUMA
Offset | `0xa78`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0` | `RW` | `` |  | WriteBack Thumb buffer offset, luma(Y) component  
## MACC_ISP_WB_THUMB_CHROMA
Offset | `0xa7c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0` | `RW` | `` |  | WriteBack Thumb buffer offset, chroma component  
## MACC_ISP_SRAM_INDEX
Offset | `0xae0`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0` | `RW` | `` |  | Auto incremental pointer for read/write VE SRAM  
## MACC_ISP_SRAM_DATA
Offset | `0xae4`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0` | `RW` | `` |  | Serial write/read buffer register for read/write VE SRAM  
When scaler is enabled (MACC_ISP_CTRL_SCALER_EN), and MACC_ISP_SRAM_INDEX set to 0x400 the next 64 values written into MACC_ISP_SRAM_DATA are treated as coefficients for a polyphase filter in the following mode. 
[code] 
    |0                             31|32                           64|           
    ---------------------------------|--------------------------------
    |            table A             |           table B             |
    ---------------------------------|--------------------------------
    All coefficients are signed 16 bit values.
     0x0100 =  1.0
     0x0080 =  0.5
     0x0000 =  0.0
     0xffff = -1/0x100
     0xff00 = -1.0 (?)
    
[/code]
[code] 
    Horizontal direction.
    Table A => 4-tap, 16-phase polyphase filter coefficients (h0, h1, h2, h3)
            | data written
     offset |31  16|15   0|
     ----------------------
     2*i+0  |  h1  |  h0  |
     2*i+1  |  h3  |  h2  |
     ----------------------
    
[/code]
[code] 
    Vertical direction.
    Table B => 2-tap, 32-phase polyphase filter coefficients (h0, h1)
            | data written
     offset |31  16|15   0|
     -----------------------
       i    |  h1  |  h0  |
    
[/code]
# AVC Engine Register
## MACC_AVC_JPEG_CTRL
Offset | `0xb04`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` MACC_AVC_JPEG_CTRL_FILL1 ` | ` 31 ` | `RW` | `` |  | fill the remaining bits as 1 for byte boundary alignment  
` MACC_AVC_JPEG_CTRL_STUFF ` | ` 30 ` | `RW` | `` |  | if last byte written is 0xff, stuff 0x00  
` MACC_AVC_JPEG_CTRL_BIAS_C ` | `26:16` | `RW` | `` | 
[code]
    0x400 / (chroma dc quantization value)
[/code]
| chroma dc component bias  
` MACC_AVC_JPEG_CTRL_BIAS_Y ` | `10:0 ` | `RW` | `` | 
[code]
    0x400 / (luma dc quantization value)
[/code]
| luma dc component bias  
  

## MACC_AVC_H264_CTRL
Offset | `0xb04`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` MACC_AVC_H264_CTRL_EPTB ` | ` 31 ` | `RW` | `` | 
[code]
    0x0 = enable
    0x1 = disable
    
[/code]
| automatically insert emulation_prevention_three_byte in bitstream  
`` | `30:9 ` | `RW` | `` |  | _unknown_  
` MACC_AVC_H264_CTRL_ENTROPY_CODING ` | ` 8 ` | `RW` | `` | 
[code]
    0x0 = CAVLC
    0x1 = CABAC
    
[/code]
| entropy_coding_mode_flag  
`` | ` 7:6 ` | `RW` | `` |  | _unknown_  
` MACC_AVC_H264_CTRL_SLICE_TYPE ` | ` 5:4 ` | `RW` | `` | 
[code]
    0x0 = I
    0x1 = P
    0x2 = unknown
    0x3 = looks like B, but unsure
    
[/code]
| Slice type  
`` | ` 3:0 ` | `RW` | `` |  | _unknown_  
## MACC_AVC_H264_QP
Offset | `0xb08`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:19` | `RW` | `` |  | _reserved_  
`` | `18:16` | `RW` | `` | 
[code]
    chroma_qp_index_offset
[/code]
| must have some range limit (spec says -12 to 12, but only 3 bits)  
`` | `15:14` | `RW` | `` |  | _reserved_  
`` | `13:8 ` | `RW` | `` | 
[code]
    pic_init_qp + slice_qp_delta
[/code]
|   
`` | ` 7:6 ` | `RW` | `` |  | _unknown_  
`` | ` 5:0 ` | `RW` | `` | 
[code]
    pic_init_qp + slice_qp_delta
    
    valid: 0x01 to 0x45
    
[/code]
| _why double?_  
## MACC_AVC_CTRL
Offset | `0xb14`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` MACC_AVC_CTRL_IRQ_EN ` | ` 7 ` | `RW` | `` |  | Enable IRQ form AVC  
  

## MACC_AVC_TRIG
Offset | `0xb18`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` MACC_AVC_TRIG_FORMAT ` | ` 16 ` | `RW` | `` | 
[code]
    0x0 = h264
    0x1 = jpeg
    
[/code]
|   
` MACC_AVC_TRIG_NBITS ` | `12:8 ` | `RW` | `` | 
[code]
    0 - 31
    
[/code]
| Number of put bits  
` MACC_AVC_TRIG_FUNCTION ` | ` 3:0 ` | `RW` | `` | 
[code]
    0x1 = Put bits
    0x8 = Launch encoding
    
[/code]
| Function  
## MACC_AVC_STATUS
Offset | `0xb1c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:16` | `RW` | `` |  | unknown, related to macroblocks number?  
`` | `12:4 ` | `RW` | `` | 
[code]
    0x26 = nominal
    0x06 = ?
    
[/code]
| unknown  
` MACC_AVC_STATUS_RESULT ` | ` 4:0 ` | `RW` | `` | 
[code]
    0x0 = nominal
    0x1 = success (at encoder finish)
    0x2 = error (at pic size zero)
                (at max bits written)
    
[/code]
[code] 
    write 1 to bit to clear bit
    0x1 clears bit 1
    0x3 clears bit 1 and bit 2
    
[/code]
| result, in IRQ should be cleared first 7:0 bits  
## MACC_AVC_BITS_DATA
Offset | `0xb20`  
---|---  
Name | Bits | R/W | Default | Values | Description  
` MACC_AVC_BITS_DATA ` | `31:0 ` | `RW` | `` |  | Data to be written by put bits.  
## MACC_AVC_VLE_ADDR
Offset | `0xb80`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0 ` | `RW` | `` |  | Address to output the encoded bitstream  
## MACC_AVC_VLE_END
Offset | `0xb84`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0 ` | `RW` | `` | 
[code]
    MACC_AVC_VLE_ADDR + (size of buffer) - 1
    
[/code]
| End position of the cyclic buffer, after reached starts from beginning.  
## MACC_AVC_VLE_OFFSET
Offset | `0xb88`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0 ` | `RW` | `` | 
[code]
    write only
    set MACC_AVC_VLE_LENGTH = bits[27:0]
    ???? reset position to (start address) + bits[4:0]
    
[/code]
| Offset in bits of the position to start writing  
## MACC_AVC_VLE_MAX
Offset | `0xb8c`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `27:0 ` | `RW` | `` | 
[code]
    0x0010000 = 8192 bytes
    0xfff0000 = 33546240 bytes
    
    bits[15:0] always zero
    
[/code]
| Maximum number of bits to write  
## MACC_AVC_VLE_LENGTH
Offset | `0xb90`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0 ` | `R` | `` | 
[code]
    MACC_AVC_VLE_OFFSET + (bits written)
[/code]
|   
## MACC_AVC_SRAM_INDEX
Offset | `0xbe0`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0 ` | `RW` | `` |  | Auto incremental pointer for read/write VE SRAM  
  

## MACC_AVC_SRAM_DATA
Offset | `0xbe4`  
---|---  
Name | Bits | R/W | Default | Values | Description  
`` | `31:0 ` | `RW` | `` |  |   
For mpeg/mjpeg, [MACC_AVC_SDRAM_INDEX][58395] is the start index to write the quantization matrix elements into MACC_AVC_SRAM_DATA. If index is 64, then the first 64 elements are for chroma component, and the next 64 wrap around to become luma. 
[code] 
    0                                  63|64                                 127
    ----------------------------------------------------------------------------
    |     luma quantization matrix       |      chroma quantization matrix     |  index by natural order
    ---------------------------------------------------------------------------- 
    MACC_AVC_SRAM_DATA[23:16] = (Q / 2) + 0.5
    MACC_AVC_SRAM_DATA[15:0]  = (0xffff / Q)
    When compared with libjpeg, there are still rounding errors in the coefficients value, around 1 unit of difference.
    
[/code]
[code] 
    (Quantized coefficients) = round(C / Q)
                             = floor((C + 0.5Q) / Q)
    
[/code]
# References
  1. [↑][58396] ISO/IEC 13818-2 Page 53 Table 6-12 
  2. [↑][58397] ISO/IEC 13818-2 Page 54 Table 6-13 
  3. [↑][58398] ISO/IEC 13818-2 Page 54 Table 6-14 
  4. [↑][58399] ISO/IEC 13818-2 Page 55
  5. [↑][58400] ISO/IEC 13818-2 Page 55
  6. [↑][58401] ISO/IEC 13818-2 Page 55
