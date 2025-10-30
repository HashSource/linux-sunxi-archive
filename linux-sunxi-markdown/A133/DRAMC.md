# A133/DRAMC
< [A133][2003]
 
**DRAMC** is the name given by Allwinner to the memory region containing the DDR controller and PHY blocks. These handle initializing the DRAM and mapping it into memory accessible by the processor. The DDR controller and PHY used on the A133 appear to be largely similar to that used by the H616; thus, knowledge is mostly transferable between the two. 
This is a high-level overview that assumes some prior knowledge regarding DDR memory. 
## Contents
  * [1 Blocks][2006]
    * [1.1 MCTL_CTL][2007]
    * [1.2 MCTL_COM][2008]
    * [1.3 MCTL_PHY][2009]
  * [2 DRAM initialization in boot0][2010]
    * [2.1 init_DRAM][2011]
    * [2.2 mctl_core_init][2012]

## Blocks
### MCTL_CTL
MCTL_CTL is the DDR controller, based on the Synopsys Enhanced Universal DDR Memory Controller (uMCTL2) IP core. This is used on a number of SoCs, including the Zynq UltraScale+ series of SoCs. This was also used on the H6 and H616. 
Unlike most implementations of this IP, there appear to be at least 3 additional sets of shadow registers; these are all `0x1000` bytes apart. Whether or not they are used is unknown. 
This communicates with the PHY via DFI, the "DDR PHY Interface", to configure mode registers, timings, address mapping, etc. There are a number of useful resources to understand the register layout: 
  * [Zynq UltraScale+ DDRC module documentation][2013]
  * [ChipSelect.org DDRC_REGS][2014] (this was stumbled across by accident)
  * [i.MX 8M Processor Reference Manual (requires an NXP account)][2015]

This region is initially unaccessible by the processor, causing a hang of some nature (likely a data abort) on access. It appears to be gated by MCTL_COM. 
Based on observed aliasing, the actual size of this register block is `0x8000` bytes; this seems to imply that there are potentially 7 shadow registers, with the upper 4 being completely unused. 
### MCTL_COM
This block is largely unknown, and is used infrequently in the A133's boot0. On the H6 and H616, this appears to control more functionality, but on the A133 only two offsets are accessed: 
  * `0x08` appears to potentially control power/gating to the PHY. This is assumed due to this being written to during a function, named "mctl_phy_cold_reset", where a bit is cleared, a delay occurs, and is set again.
  * `0x20` appears to gate access to other blocks. Some parts of MCTL_CTL are gated by BIT(8) (mostly DFI registers), while BIT(15) unlocks the majority of other registers.

Based on observed aliasing, the actual size of this register block is `0x2000` bytes. 
### MCTL_PHY
The PHY is what actually communicates with the DRAM. The specific IP core is unknown, and does not appear to match any known cores in register layout; naming of the PHY config initialization function in boot0 (`ddrphy_phyinit_C_initPhyConfig`) would suggest it is DWC IP, but the layout does not match either the LPDDR4 multiPHY V1 or V2. The controller supports (LP)DDR3/4 memory, and appears to support the following, based on boot0 function names: 
  * "Address remapping" (DQ pin swizzling?)
  * CA bit delay compensation (CA per-bit deskew?)
  * VREF selection
  * Write leveling
  * Read calibration (Read gate training?)
  * Read training (Read DQ deskew?)
  * Write training (Write DQ deskew?)
  * DX bit delay compensation (DX per-bit deskew?)
  * DFS (Dynamic Frequency Scaling?)
  * ZQ calibration (though this is unused)

The highest offset into the DDRPHY block that is accessed is conditional and depends on what appears to be a SID-related quirk: 
  * If the chipid is `0x800` or `0x2400`, the highest accessed address is `+0x2388`, during CA bit delay compensation when DDR3 is used.
  * Otherwise, the highest accessed address is `0x0b80`, used during write training on DX3

Based on observed aliasing, the actual size of the DDRPHY block is `0x1000` bytes. 
## DRAM initialization in boot0
Multiple steps occur during DRAM initialization. In vendor trees, this code is precompiled and stored in an object file renamed with a ".a" extension. Usually, the name of the file is `libsub50iw10p1.o`, and is stored in `lichee/brandy-2.0/spl/board/{sun50iw10p1,a133,r818}/libsun50iw10p1.a`. 
Initialization is done in `int init_DRAM(int _type /* unused */, struct dram_para* para)`. 
### init_DRAM
  1. Bit 8 is set at `SYS_CFG +0x160`, and `+0x168` has the bitmask `0x3f` cleared. Purpose of this is unknown
  2. DRAM voltage is set on using the PMIC.
  3. If `TPR13[0]` is not set, the DRAM configuration is auto-scanned.
  4. If `TPR13[12]` is set, software eye training is attempted using DMA.
  5. `mctl_core_init` is called (documented below)
  6. The DRAM size is calculated using the parameters that successfully initialized the PHY
  7. A simple memory test is run.

If any of these steps fail, an error is returned and the DRAM does not initialize. 
### mctl_core_init
Many functions are called from here, so this is extremely high level 
  1. MBUS, DRAM clock, DRAM gate, and PLL5 are reset, configured, and enabled
  2. MCTL access is enabled
  3. The DRAM scheduler is confgiured
  4. The master register, controlling DRAM type, burst length, geardown and 2T mode, are configured
  5. ODT mappings are configured
  6. HIF (Host Interface?) address mapping are configured based on SDRAM organization.
  7. DDR timings are set up.
  8. Automatic controller updates and automatic controller update requests are disabled.
  9. DBI (Data Bus Inversion) is conditionally enabled
  10. DDR auto refresh is disabled
  11. PHY is "cold reset" (powered off and on?)
  12. PHY configuration occurs; many pieces of this are unknown, what is known is: 
     1. PHY DQ swizzling is configured, based on the DRAM type and SOC "chipid" from the SID
     2. VREF is configured
     3. DX drive/ODT and CA drive are configured
     4. CA per-bit deskewing is conditionally performed
  13. Mode registers are configured via MCTL_CTL
  14. DDR auto refresh is re-enabled
  15. Depending on TPR10, the following calibrations may occur, in the following order: 
     1. Write leveling
     2. Read gate training
     3. Read DQ deskew
     4. Write DQ deskew
     5. DX per-bit deskew
  16. Depending on the value of TPR13, PHY DFS calibrations occur.
