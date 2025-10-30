# DRAM Controller/Quirks
< [DRAM Controller][16191]
 
This is a list of some strange things and unresolved mysteries. 
#### Suspicious GPS manipulations
The current code in upstream u-boot: [http://git.denx.de/?p=u-boot.git;a=blob;f=arch/arm/cpu/armv7/sunxi/dram.c;h=b43c4b41d3c53dc339b3f4f4229daa9fca7f9764;hb=3fe1a8545b55d31a6db2d9e60d962c4f6e048913#l218][16194]
The [first commit][16195] introducing this code in the u-boot-sunxi says _"if we don't reset the gps module, it will access sdram but sdram is not ready, and the system will die..."_. 
The corresponding reference in the Allwinner boot0 bootloader is yet to be found. 
#### SDR_SCSR register ('csel' in the sunxi_dram_reg struct) on Allwinner A10
The current code in upstream u-boot: not available yet. 
The code in Allwinner boot1 bootloader: [https://github.com/hno/allwinner-boot/blob/6fd439377f0f0f0305d61fe6b87c9e77666facb3/boot1/core/standby/dram_standby.c#L326][16196]
Unless a magic value 0x16237495 is written to this register on Allwinner A10, the DRAM controller fails to operate properly. This register always reads back as 0. 
#### "super-standby"
The current code in upstream u-boot: [http://git.denx.de/?p=u-boot.git;a=blob;f=arch/arm/cpu/armv7/sunxi/dram.c;h=b43c4b41d3c53dc339b3f4f4229daa9fca7f9764;hb=3fe1a8545b55d31a6db2d9e60d962c4f6e048913#l535][16197]
The same code in boot0: [https://github.com/hno/allwinner-boot/blob/70576dd51b65722abadd5ea6169f6c20639cf211/boot0/drv/init_dram/dram_init.c#L409][16198]
We can see, that this particular code got mangled on the way to the upstream u-boot and does not make any sense there. For example: 
  * in the original boot0 code we had "mctl_write_w(SDR_DPCR, 0x16510000)" (write to the register) and in upstream u-boot it now looks like "setbits_le32(&dram->ppwrsctl, 0x16510000)" (set bits in the register)
  * in the original boot0 code it was issuing three commands "0x12, 0x17, 0x13" (Self-Refresh entry, Self-Refresh exit, Refresh), but in the upstream u-boot they have become "0x12, 0x12, 0x13" (Self-Refresh entry, Self-Refresh entry, Refresh)

It is very likely that the original code had something to do with wake up from super-standby (which keeps DDR3 in Self-Refresh mode?), where the previously stored ZQ calibration settings are retrieved from the battery backed Timer General Purpose Register 0 in the RTC power domain. 
Some messy commits in the Allwinner bootloader: 
  * <https://github.com/hno/allwinner-boot/commit/8bcc7de0e4cb166ad1e8db0debbadcfbfcdba079>
  * <https://github.com/hno/allwinner-boot/commit/a1baea05c83151b143bad629ac854cfa332c0635>
  * <https://github.com/hno/allwinner-boot/commit/386c71cd8fd57c7a860678a6c644f8d62ebf1db8>
