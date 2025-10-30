# DDR3
This page is an attempt to collect all the information about the various DDR3 chips in use on Sunxi hardware. 
## Contents
  * [1 DDR3 configuration in u-boot][15957]
    * [1.1 JEDEC speed bin][15958]
  * [2 Manufacturers][15959]
    * [2.1 Elixir][15960]
      * [2.1.1 N2CB2G80GN-CG][15961]
    * [2.2 Elpida][15962]
      * [2.2.1 J2108BCSE-DJ-F][15963]
      * [2.2.2 J4216BFBG-GN-F][15964]
      * [2.2.3 J4216BBBG-DJ-F][15965]
    * [2.3 Foresee][15966]
      * [2.3.1 NCLD3B2512M32][15967]
    * [2.4 GT][15968]
      * [2.4.1 GT8UB256M16BP-BG][15969]
      * [2.4.2 GT8UB256M16BP-BH][15970]
      * [2.4.3 GT8UB512M8EN-BG][15971]
    * [2.5 MEMPHIS][15972]
      * [2.5.1 MEM4G08D3EABG-125][15973]
      * [2.5.2 MEM4G16D3EABG-125][15974]
    * [2.6 Micron][15975]
      * [2.6.1 MT41J256M16HA-125][15976]
    * [2.7 MIRA][15977]
      * [2.7.1 P3P4GF4BLF-GDJ][15978]
    * [2.8 Nanya][15979]
      * [2.8.1 NT5CB256M16BP-DI][15980]
      * [2.8.2 NT5CB256M8BN-CG][15981]
      * [2.8.3 NT5CB256M8DN-CG][15982]
      * [2.8.4 NT5CC256M16CP-DI][15983]
    * [2.9 Samsung][15984]
      * [2.9.1 K4B4G1646Q-HYK0][15985]
      * [2.9.2 K4B2G1646Q-HYK0][15986]
      * [2.9.3 K4B4G0846E][15987]
      * [2.9.4 K4B4G1646D-BCK0][15988]
    * [2.10 SK Hynix][15989]
      * [2.10.1 H5TC4G83AFR-PBA][15990]
      * [2.10.2 H5TQ1G63EFR-H9C][15991]
      * [2.10.3 H5TQ1G83TFR-H9C][15992]
      * [2.10.4 H5TQ1G83BFR-H9C][15993]
      * [2.10.5 H5TQ2G63BFR-H9C][15994]
      * [2.10.6 H5TQ2G63DFR-PBC][15995]
      * [2.10.7 H5TQ2G63GFR-RDC][15996]
      * [2.10.8 H5TQ2G83CFR-H9C][15997]
      * [2.10.9 H5TQ2G83EFR-PBC][15998]
      * [2.10.10 H5TQ4G63AFR-PBC][15999]
      * [2.10.11 H5TQ4G63CFR-RDC][16000]
      * [2.10.12 H5TQ4G83AFR-PBC][16001]
    * [2.11 SPECTEK][16002]
      * [2.11.1 PE918-15E][16003]
      * [2.11.2 PEB15-15E][16004]
    * [2.12 Unidentified][16005]
      * [2.12.1 256X8DDR3 HL 1320][16006]
  * [3 Useful information][16007]

# DDR3 configuration in u-boot
## JEDEC speed bin
Sunxi devices typically use DRAM clock speeds not exceeding 533MHz, which means that the JEDEC DDR3-1066F speed bin is the most common set of timings that they are expected to be targeting for. The DDR3-1333 and DDR3-1600 chips, which are rated for higher clock speeds, may or may not support down binning to DDR3-1066F (this information has to be checked in the datasheets). That's because the DDR3-1066F compatible chips need to support 13.125 ns timings for tRP/tRCD, while the DDR3-1333H chips are only required to support 13.5 ns. So the DDR3-1066F speed bin has a bit tighter timings than DDR3-1333H. This difference between 13.125 ns and 13.5 ns is relatively important, because when the delays are converted from nanoseconds to cycles and rounded up, it is a matter of having 7 cycles delay instead of 8! 
It is quite common to have DDR3-1333H or DDR3-1600K chips, which support DDR3-1066F timings too. This may look like an explicit note _"backward compatible to 1066 CL-7"_ in the datasheets of such chips. Or the tRP/tRCD timing information may be sometimes specified as _"13.5 (13.125) ns"_ in the table. 
The u-boot *_defconfig file for an Allwinner A10/A13/A20 device may use the following configuration option to indicate that the DRAM chip is in fact compatible with DDR3-1066F timings (and with DDR3-1333H for the DRAM clock speeds >533MHz): 
[code] 
      +S:CONFIG_DRAM_TIMINGS_DDR3_1066F_1333H=y
    
[/code]
In the unlikely case if the DDR3-1066F speed bin is not supported by the DRAM chip, a slower DDR3-1066G speed bin has to be assumed. 
# Manufacturers
## Elixir
#### N2CB2G80GN-CG
DDR3-1333H (supports down binning to DDR3-1066F), x8, density: 2G, page size: 1K 
Datasheet: <http://www.elixir-memory.com/products/file/elixir-ddr3-2gb-g-die-r10.pdf>
## Elpida
Elpida Memory. Inc was a Japanese company which filed for bankruptcy in the beginning of 2012 and was eventually acquired by [Micron Technology][15975]. 
#### J2108BCSE-DJ-F
DDR3-1333H (supports down binning to DDR3-1066F), x8, density: 2G, page size: 1K, tRFC: 160ns 
Datasheet: <http://www.datasheets360.com/part/detail/edj2108bcse-dj-f/2732776748928774995/>
#### J4216BFBG-GN-F
#### J4216BBBG-DJ-F
Unknown
## Foresee
#### NCLD3B2512M32
LPDRR3-1066, x32, density: 16G, page size: ?, tRFC: ? (marked as TBD in datasheet for 16Gb version) 
Datasheet: [File:FORESEE 178ball 12x11.5 LPDDR3 16G Spec V1.0-1228.pdf][16008]
## GT
#### GT8UB256M16BP-BG
DDR3-1333H, x16, density: 4G, page size: 2K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <https://github.com/SoM-Boards/SoM-allwinnerA10/blob/master/docs/GT-DDR3-4Gbit-B-DIE-x8%20x16.pdf>
#### GT8UB256M16BP-BH
DDR3-1600K (supports down binning to DDR3-1066F), x16, density: 4G, page size: 2K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <https://github.com/SoM-Boards/SoM-allwinnerA10/blob/master/docs/GT-DDR3-4Gbit-B-DIE-x8%20x16.pdf>
#### GT8UB512M8EN-BG
DDR3-1333H, x8, density: 4G, page size: 1K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <https://github.com/SoM-Boards/SoM-allwinnerA10/blob/master/docs/GT-DDR3-4Gbit-B-DIE-x8%20x16.pdf>
## MEMPHIS
#### MEM4G08D3EABG-125
DDR3-1600K (supports down binning to DDR3-1066F), x8, density: 4G, page size: 1K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <http://www.memphis.ag/fileadmin/datasheets/MEM4G0804D3EABG_10.pdf>
#### MEM4G16D3EABG-125
DDR3-1600K (supports down binning to DDR3-1066F), x16, density: 4G, page size: 2K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <http://www.memphis.ag/fileadmin/datasheets/MEM4G16D3EABG_10.pdf>
## Micron
#### MT41J256M16HA-125
DDR3-1600K (supports down binning to DDR3-1066F), x16, density: 4G, page size: 2K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <http://www.micron.com/~/media/documents/products/data-sheet/dram/ddr3/4gb_ddr3_sdram.pdf>
## MIRA
#### P3P4GF4BLF-GDJ
DDR3-1333H (supports down binning to DDR3-1066F), x16, density: 4G, page size: 2K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <http://www.deutron.com.tw/pdf/D3_256x16.pdf>
## Nanya
#### NT5CB256M16BP-DI
DDR3-1600K (supports down binning to DDR3-1066F), x16, density: 4G, page size: 2K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <http://www.nanya.com/NanyaAdmin/GetFiles.ashx?ID=1110>
#### NT5CB256M8BN-CG
DDR3-1333H (supports down binning to DDR3-1066F), x8, density: 2G, page size: 1K 
Datasheet: <http://www.nanya.com/NanyaAdmin/GetFiles.ashx?ID=961>
#### NT5CB256M8DN-CG
DDR3-1333H (supports down binning to DDR3-1066F), x8, density: 2G, page size: 1K 
Datasheet: <http://www.nanya.com/NanyaAdmin/GetFiles.ashx?ID=923>
#### NT5CC256M16CP-DI
DDR3-1600K (supports down binning to DDR3-1066F), x16, density: 4G, page size: 2K, tRFC: 260ns (lower than JEDEC default 300ns), 1.35V 
Datasheet: <http://www.nanya.com/NanyaAdmin/GetFiles.ashx?ID=1147>
## Samsung
[Samsung DDR3 product guide][16009] for decoding chip numbers 
#### K4B4G1646Q-HYK0
DDR3-1600K (supports down binning to DDR3-1333H and DDR3-1066F), x16, density: 4G, page size: 2K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <http://www.samsung.com/global/business/semiconductor/file/product/ds_k4b4g1646b_rev10-1.pdf>
#### K4B2G1646Q-HYK0
Datasheet: <http://www.samsung.com/global/business/semiconductor/file/product/DS_K4B2G1646Q-BY_Rev101.pdf>
#### K4B4G0846E
Datasheet: <http://www.samsung.com/semiconductor/global/file/product/DS_4G_E_DDR3_Rev1.2.pdf>
#### K4B4G1646D-BCK0
Datasheet: <http://www.samsung.com/semiconductor/search/?q=K4B4g1646D-BC>
## SK Hynix
#### H5TC4G83AFR-PBA
DDR3-1600? (???), x8, density: 4G, page size: 1K 
Datasheet: <https://www.skhynix.com/product/filedata/fileDownload.do?seq=2475>
#### H5TQ1G63EFR-H9C
DDR3-1333H (supports down binning to DDR3-1066F), x16, density: 1G, page size: 2K 
Datasheet: <https://www.skhynix.com/product/filedata/fileDownload.do?seq=2658>
#### H5TQ1G83TFR-H9C
DDR3-1333H (supports down binning to DDR3-1066F), x8, density: 1G, page size: 1K 
Datasheet: <http://www.skhynix.com/inc/pdfDownload.jsp?path=/datasheet/pdf/dram/DDR3_H5TQ1G(4_8)3TFR(Rev1.1).pdf>
#### H5TQ1G83BFR-H9C
DDR3-1333H (supports down binning to DDR3-1066F), x8, density: 1G, page size: 1K 
Datasheet: <http://www.hynix.com/product/filedata/fileDownload.do?seq=2274>
#### H5TQ2G63BFR-H9C
DDR3-1333H (supports down binning to DDR3-1066F), x16, density: 2G, page size: 2K 
Datasheet: <http://hands.com/~lkcl/H5TQ2G63BFR.pdf>
#### H5TQ2G63DFR-PBC
DDR3-1600K (supports down binning to DDR3-1066F and DDR3-1333H), x16, density: 2G, page size: 2K 
Datasheet: <https://www.skhynix.com/inc/pdfDownload.jsp?path=/datasheet/pdf/dram/Consumer_DDR3_H5TQ2G8(6)3DFR(Rev1.3)_131101.pdf>
#### H5TQ2G63GFR-RDC
Datasheet: <https://www.skhynix.com/product/filedata/fileDownload.do?seq=6119>
#### H5TQ2G83CFR-H9C
DDR3-1333H (supports down binning to DDR3-1066F), x8, density: 2G, page size: 1K 
Datasheet: <https://www.skhynix.com/inc/pdfDownload.jsp?path=/datasheet/pdf/dram/Computing_DDR3_H5TQ2G4(8)3CFR(Rev1.0).pdf>
#### H5TQ2G83EFR-PBC
DDR3-1333H ? (???), x8, density: 2G, page size: 1K 
Datasheet: <https://www.skhynix.com/product/filedata/fileDownload.do?seq=2630>
#### H5TQ4G63AFR-PBC
DDR3-1600K (supports down binning to DDR3-1066F), x16, density: 4G, page size: 2K, tRFC: 260ns (lower than JEDEC default 300ns) 
Datasheet: <https://www.skhynix.com/inc/pdfDownload.jsp?path=/datasheet/pdf/dram/Consumer_DDR3_H5TQ4G8(6)3AFR(Rev1.1)_130130.pdf>
#### H5TQ4G63CFR-RDC
Datasheet: <https://www.skhynix.com/product/filedata/fileDownload.do?seq=2688>
#### H5TQ4G83AFR-PBC
DDR3-1600K (supports down binning to DDR3-800E, DDR3-1066F, DDR3-1333H), x8, density: 4G, page size: 1K, tRFC: ??ns 
Datasheet: <https://www.skhynix.com/product/filedata/fileDownload.do?seq=2419>
## SPECTEK
#### PE918-15E
DDR3-1333H, x8, density: 2G, page size: 1K 
Datasheet: <http://www.spectek.com/pdfs/PRN256M8V79DG8GQF-15E.PDF>
#### PEB15-15E
DDR3-1333H, x16, density: 4G, page size: 1K 
Datasheet: <http://www.spectek.com/pdfs/SPECTEK_4GB_DDR3_SDRAM.PDF>
## Unidentified
#### 256X8DDR3 HL 1320
# Useful information
  1. The ["DDR3 Device Operation"][16010] document from SK Hynix contains a lot of copy/paste information from the DDR3 spec.
  2. ["A DRAM Refresh Tutorial"][16011] blog post jointly authored by Rajeev Balasubramonian (University of Utah), Manju Shevgoor (University of Utah), and Jung-Sik Kim (Samsung).
