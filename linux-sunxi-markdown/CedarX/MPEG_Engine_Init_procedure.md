# CedarX/MPEG Engine Init procedure
< [CedarX][11650]
 
## MPEG Engine reset/clock init procedure
Before use MPEG engine for MPEG/MJPEG/DIVX/MS-MPEG/VP6 files, MPEG engine should be clocked and reseted 
[code] 
    [MACC_VE_CTRL][11653] <= 0x7 /*place in reset*/
    [MACC_VE_CTRL][11653] <= 0x030007 /* Set DRAM type?? */
    [MACC_VE_CTRL][11653] <= 0x130007 /* DRAM Blank ?? */
    [MACC_VE_CTRL][11653] <= 0x130000 /* Select MPEG Engine */
    
[/code]
