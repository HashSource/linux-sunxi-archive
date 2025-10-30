# CedarX/JPEG-MJPEG Decoding
< [CedarX][11531]
 
## MJPEG/JPEG Decoding process
CedarX take care Decode JPEG and MJPEG(are set of JPEGs) 
Generaly JPEG decoding can be described: 
[code] 
    JPEG decoding process
    (Huffman(VLD) decode )
            |
    (Inverse Quantization(IQ))
            |
    (Inverse Discrete Cosine Transform(IDCT)) 
            |
    (YCrCb to RGB) (disp must do it)
    
[/code]
  
CedarX need to be configured in order: 
  * Do [CedarX/Kernel_Driver_guide#Kernel_driver_init_procedure][11534]

  * Do [CedarX/MPEG Engine Init procedure][11535]

  

  * Set JPEG Restart Interval

[code] 
    [MACC_MPEG_JPEG_RES_INT][11536] <- restart interval
    
[/code]
  * Set JPEG Input format

[code] 
    [MPEG_BASE+0x1b] <- 0x3 | (format << 3)
    
[/code]
format  | meaning   
---|---  
0x0  | 4:2:0 chroma subsampling   
0x1  | unknown   
0x2  | 4:2:2 horizontal chroma subsampling   
0x3  | 4:4:4 full chroma (but Cedar output is 4:2:2 hor.)   
0x4  | 4:2:2 vertical chroma subsampling (but Cedar output is 4:2:0)   
0x5...  | unknown   
  * Parse jpeg IQ table to [MACC_MPEG_IQ_MIN_INPUT][11537]

[code] 
    [MACC_MPEG_IQ_MIN_INPUT][11537] <- TABLE
    
[/code]
table are TWO 8x8 MATRIX first for chroma, second for luma. All 2 * 64 8bit values are written to this reg one after another (and copied to internal ve-sram ). 
bits  | Value  | Description   
---|---|---  
31:16  | 0x0000  | unknown   
15:8  | 0-63 for chroma, 64-127 for luma  | position in matrix in zigzag order (order is same as in JPEG)   
7:0  |  | IQ coefficient from DQT in JPEG   
  

  * Set Result buffer (Rotate-Scale buffer)

Must be physical address (in reseved space) and relative to DRAM start 
[code] 
    [MACC_MPEG_ROT_LUMA][11538] <- Chroma output buffer address
    [MACC_MPEG_ROT_CHROMA][11539] <- Luma output buffer address
    
[/code]
Data output is in 32x32 pixel blocks, DEFE should be able to reorder and convert this according to A13 manual. 
  * Set picture size in MCUs

[code] 
    [MACC_MPEG_JPEG_SIZE][11540] <- HEIGHT:WIDTH
    
[/code]
Height in upper bits (31:16), width in lower (15:0) beginning with 0 for up to one MCU 
  * Set scale mode

[code] 
    [MACC_MPEG_ROTSCALE_CTRL][11541] <- 0(1:1) (extra functions control register)
    
[/code]
  * Reset huffman table

[code] 
    [MACC_MPEG_JPEG_HUFFMAN_CTRL][11542] <- 0 (huffman control register)
    
[/code]
  * Parse from jpeg and load Huffman table

[code] 
    [MACC_MPEG_JPEG_HUFFMAN_LOAD][11543] <- TABLE
    
[/code]
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
  * Set VBV (limit address) maxumum reseved

[code] 
    this is for IRQ when we need more data than reserved in mem for new part
    [MACC_MPEG_VBV_END][11544] <- SRC_BUFF+ SRC_MAX_BUFF_SIZE-1
    
[/code]
  * Enable IRQ (may be also set work mode need check))

[code] 
    [MACC_MPEG_CTRL][11545] <- 0x0000007c
    
[/code]
  * Set SRC Buff parameters

  

[code] 
    [MACC_MPEG_VLD_OFFSET][11546] <- Offset in SRC buffer in bits (frame offset when may you have manyframes - mjpeg)
    [MACC_MPEG_VLD_LEN][11547] <- VLD LEN in bits
    [MACC_MPEG_VLD_ADDR][11548] <- (SRC address relative to DRAM start) | 0x70000000   How to access ram above 256MB?
    
[/code]
  

  * Start

[code] 
    [MACC_MPEG_TRIG][11549] <- 0xe  Trigger start
    
[/code]
  * Wait IRQ (using ioctr)

  * check [MACC_VE_STATUS][11550] register for finush
