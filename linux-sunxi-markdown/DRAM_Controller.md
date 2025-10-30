# DRAM Controller
Several different families of DRAM controllers exist: 
## Contents
  * [1 sun4i (Allwinner A10), sun5i (Allwinner A13) and sun7i (Allwinner A20) hardware][16228]
  * [2 sun6i (Allwinner A31) hardware][16229]
  * [3 sun9i (Allwinner A80) and early sun8i (Allwinner A23) hardware][16230]
  * [4 sun8i (Allwinner A33, A83T, H3) and sun50i (Allwinner A64, H5) hardware][16231]
  * [5 sun50i (Allwinner H6) hardware][16232]
  * [6 sun50i (Allwinner A133, H616) hardware][16233]
  * [7 sun55i (Allwinner A523) hardware][16234]
  * [8 sun60i (Allwinner A733) hardware][16235]

## sun4i (Allwinner [A10][16236]), sun5i (Allwinner [A13][16237]) and sun7i (Allwinner [A20][16238]) hardware
No accurate documentation for this particular DRAM controller exists in public access. But it is suspected that Allwinner uses one of the revisions of Synopsys DesignWare [DDR2/3-Lite Memory Controller IP (MCTL)][16239] combined with [DDR2/3-Lite PHY IP][16240] in A10/A13/A20. Also this DRAM controller apparently has siblings in Rockchip RK29XX, RK30XX and TI KeyStone2 hardware, which have some documentation and some bits of kernel and bootloader sources available in the Internet. Not to mention the original Allwinner boot0 bootloader sources and the suspend support code from the linux-sunxi kernel. This provides enough hints for finding out how the DRAM controller actually works by checking various bits of information via the trial and error method. 
As a result, we have a reasonably usable reconstructed [A10 DRAM Controller Register Guide][16241]. 
[A10 DRAM Controller Performance][16242]
[A10 DRAM Controller Calibration][16243]
[DRAM Calibration Results][16244]
* * *
See also: [DRAM controller quirks][16245]
## sun6i (Allwinner [A31][16246]) hardware
The sun6i DRAM controller is very similar to the one found in public Rockchip RK30xx documentation. 
A31 boot0/boot1 source: [[1]][16247]
A31 u-boot support: [A31 dram.c][16248] [dram_sun6i.c][16249]
[A31 DRAM Controller Register Guide][16250]
## sun9i (Allwinner [A80][16251]) and early sun8i (Allwinner [A23][16252]) hardware
This DRAM controller generation is similar to the one found in Xilinx Zynq UltraScale+ SoCs, but with reduced features, maybe an older version. The PHY has more differences, some parts are still similar to RK30xx and TI KeyStone2. 
Some initial register dumps from [A23][16252] reveal that there are significant differences between the A31 and A23 dram controllers. There are dram controller register defines in the [a23 suspend code][16253] in [this code (dram_init)][16254] the SPL parameters are read and stored into structure defined [here][16255] without using the definition. 
## sun8i (Allwinner [A33][16256], [A83T][16257], [H3][16258]) and sun50i (Allwinner [A64][16259], [H5][16260]) hardware
This generation's DRAM controller is similar to the previous sun9i generation, but with completely different register layout and some features removed. Controller and PHY registers got combined into a single block, with no particular or meaningful order. 
There are some small differences between the various SoCs, especially in the PHYs, but overall it looks like they all use the same generation of DRAM controller. It seems like H5 doesn't have a BIST anymore, also some data training regsiters vanished. 
## sun50i (Allwinner [H6][16261]) hardware
This generation of DRAM controller has DDR4 memory support, and still being mysterious now. 
According to disassembly of auto_set_timing_para function of the libdram of H6, the PHY/controller seems to be similar to the one found in Xilinx Zynq UltraScale+ SoCs. 
## sun50i (Allwinner [A133][16262], [H616][16263]) hardware
These use the Synopsys DesignWare uMCTL2 DRAM controller (similar to the Zynq UltraScale+ SoCs), alongside with what appears to be an Innosilicon DDR PHY (based on similarities to the A523), aside from being an older version or having different stride settings. Their COMMON blocks are different as well. 
## sun55i (Allwinner [A523][16264]) hardware
Reverse engineering, but the controller and PHY appear to be the same as the A133/H616, with some critical differences; notably, certain registers in the PHY appear to now be in packed representations, like the address_remapping/CA pad swizzle. The PHY appears to match the Rockchip RK3568's DDR PHY (an Innosilicon DDR3/DDR4/LPDDR3/LPDDR4 IP) perfectly. 
## sun60i (Allwinner [A733][16265]) hardware
Based on symbols and read/write patterns in DFI initialization, these use the Synopsis DesignWare [LPDDR5/4/4X Controller][16266] and [PHY][16267].
