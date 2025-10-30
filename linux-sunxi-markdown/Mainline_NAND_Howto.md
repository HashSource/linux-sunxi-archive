# Mainline NAND Howto
[![MBOX icon important.png][33945]][33946] | MLC NANDs are not well supported right now. You can enable MLC NAND support, but remember that you risk data loss.   
---|---  
This page describes how to enable [NAND][33947] support in u-boot and [kernel][33948]. Just remember that this is incompatible with the legacy (Android) NAND layout. (see "== Known Issues ==" below) 
## Contents
  * [1 NAND support in u-boot][33949]
  * [2 NAND support in kernel][33950]
    * [2.1 Current status][33951]
    * [2.2 Prerequisites][33952]
    * [2.3 Kernel Configuration][33953]
    * [2.4 Known issues][33954]
      * [2.4.1 Many bad blocks][33955]
    * [2.5 Adding a new device][33956]
      * [2.5.1 Add NAND controller pin definitions][33957]
      * [2.5.2 Add NFC node to SoC's DTSI][33958]
      * [2.5.3 Enable NAND in board's DTS][33959]
      * [2.5.4 Define NAND partitions in DTS][33960]

# NAND support in u-boot
Follow the u-boot [README][33961]
# NAND support in kernel
## Current status
See [MTD Driver][33962]  

## Prerequisites
  * Mainline kernel >= 4.10.0-rc1
  * NAND detection/initialization patchset [patch-v5][33963]

## Kernel Configuration
To use MTD driver with Linux mainline kernel you should enable: 
[code] 
    Device Drivers  --->
      <*> Memory Technology Device (MTD) support  --->
        <*>   OpenFirmware partitioning information support
        <*>   NAND Device Support  --->
          <*>   Support for NAND on Allwinner SoCs
    
[/code]
## Known issues
### Many bad blocks
To fix many bad blocks issue you should: 
[code] 
    1. Disable nand-on-flash-bbt in your dts
    2. Remove this test: http://lxr.free-electrons.com/source/drivers/mtd/nand/nand_base.c?v=4.7#L2940
    3. Boot your new kernel and erase chip with flash_erase /dev/mtd[0-X]
    4. Re-introduce the bad block check removed in 2, re-enable nand-on-flash-bbt
       and boot the new kernel
    
[/code]
Patch to disable nand bad block check from here <https://lkml.org/lkml/2014/10/21/546>
[code] 
    diff --git a/arch/arm/boot/dts/sun7i-a20-cubieboard2.dts b/arch/arm/boot/dts/sun7i-a20-cubieboard2.dts
    index 1ef937b..65ac8af 100644
    --- a/arch/arm/boot/dts/sun7i-a20-cubieboard2.dts
    +++ b/arch/arm/boot/dts/sun7i-a20-cubieboard2.dts
    @@ -33,6 +33,7 @@
     
     				nand-ecc-mode = "hw";
     				nand-rnd-mode = "hw";
    +				/*
     				nand-on-flash-bbt;
     
     				boot0@0 {
    @@ -74,6 +75,7 @@
     						0x2d2e 0x1aea 0x2e17 0x173d 0x3a6e 0x71bf 0x25f9 0x0a5d
     						0x7c57 0x0fbe 0x46ce 0x4939 0x6b17 0x37bb 0x3e91 0x76db>;
     				};
    +				*/
     			};
     		};
     
    diff --git a/drivers/mtd/nand/nand_base.c b/drivers/mtd/nand/nand_base.c
    index 7311063..153b323 100644
    --- a/drivers/mtd/nand/nand_base.c
    +++ b/drivers/mtd/nand/nand_base.c
    @@ -3312,8 +3312,10 @@ int nand_erase_nand(struct mtd_info *mtd, struct erase_info *instr,
     					chip->page_shift, 0, allowbbt)) {
     			pr_warn("%s: attempt to erase a bad block at page 0x%08x\n",
     				    __func__, page);
    +			/*
     			instr->state = MTD_ERASE_FAILED;
     			goto erase_exit;
    +			*/
     		}
    
[/code]
## Adding a new device
### Add NAND controller pin definitions
Most of boards use the same pins for NAND controller, so you should add pin definitions in SoC's DTSI  
For example, Allwinner A10/A20 have the same pins used for NAND: 
[code] 
    			nand_pins_a: nand_base0@0 {
    				allwinner,pins = "PC0", "PC1", "PC2",
    						"PC5", "PC8", "PC9", "PC10",
    						"PC11", "PC12", "PC13", "PC14",
    						"PC15", "PC16";
    				allwinner,function = "nand0";
    				allwinner,drive = <SUN4I_PINCTRL_10_MA>;
    				allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
    			};
    
    			nand_cs0_pins_a: nand_cs@0 {
    				allwinner,pins = "PC4";
    				allwinner,function = "nand0";
    				allwinner,drive = <SUN4I_PINCTRL_10_MA>;
    				allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
    			};
    
    			nand_cs1_pins_a: nand_cs@1 {
    				allwinner,pins = "PC3";
    				allwinner,function = "nand0";
    				allwinner,drive = <SUN4I_PINCTRL_10_MA>;
    				allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
    			};
    
    			nand_cs2_pins_a: nand_cs@2 {
    				allwinner,pins = "PC17";
    				allwinner,function = "nand0";
    				allwinner,drive = <SUN4I_PINCTRL_10_MA>;
    				allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
    			};
    
    			nand_cs3_pins_a: nand_cs@3 {
    				allwinner,pins = "PC18";
    				allwinner,function = "nand0";
    				allwinner,drive = <SUN4I_PINCTRL_10_MA>;
    				allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
    			};
    
    			nand_rb0_pins_a: nand_rb@0 {
    				allwinner,pins = "PC6";
    				allwinner,function = "nand0";
    				allwinner,drive = <SUN4I_PINCTRL_10_MA>;
    				allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
    			};
    
    			nand_rb1_pins_a: nand_rb@1 {
    				allwinner,pins = "PC7";
    				allwinner,function = "nand0";
    				allwinner,drive = <SUN4I_PINCTRL_10_MA>;
    				allwinner,pull = <SUN4I_PINCTRL_NO_PULL>;
    			};
    
[/code]
[![Sticky-note-pin.png][33964]][33965] _Note:_ Enable only the pin groups that are actually used by boards. 
### Add NFC node to SoC's DTSI
Once you define pins, you should add NFC node.  
Example for Allwinner A10: 
[code] 
    		nfc: nand@01c03000 {
    			compatible = "allwinner,sun4i-a10-nand";
    			reg = <0x01c03000 0x1000>;
    			interrupts = <37>;
    			clocks = <&ahb_gates 13>, <&nand_clk>;
    			clock-names = "ahb", "mod";
    			dmas = <&dma SUN4I_DMA_DEDICATED 3>;
    			dma-names = "rxtx";
    			status = "disabled";
    			#address-cells = <1>;
    			#size-cells = <0>;
    		};
    
[/code]
Since Allwinner A20 SoCs have it's own interrupt controller, interrupts line should be changed.  
Example for A20: 
[code] 
    		nfc: nand@01c03000 {
    			compatible = "allwinner,sun4i-a10-nand";
    			reg = <0x01c03000 0x1000>;
    			interrupts = <GIC_SPI 37 IRQ_TYPE_LEVEL_HIGH>;;
    			clocks = <&ahb_gates 13>, <&nand_clk>;
    			clock-names = "ahb", "mod";
    			dmas = <&dma SUN4I_DMA_DEDICATED 3>;
    			dma-names = "rxtx";
    			status = "disabled";
    			#address-cells = <1>;
    			#size-cells = <0>;
    		};
    
[/code]
### Enable NAND in board's DTS
Once you have done with SoC's DTSI changes, you should enable NAND in your board DTS file.  
In a single-chip configuration, chip usually connected to base nand pins, cs0(Chip Select) and rb0(Ready/Busy) pins. 
[code] 
    &nfc {
    	pinctrl-names = "default";
    	pinctrl-0 = <&nand_pins_a>, <&nand_cs0_pins_a>, <&nand_rb0_pins_a>;
    	status = "okay";
    
    	nand@0 {
    		#address-cells = <2>;
    		#size-cells = <2>;
    		reg = <0>;
    		allwinner,rb = <0>;
    
    		nand-ecc-mode = "hw";
    		nand-on-flash-bbt;
    	};
    };
    
[/code]
### Define NAND partitions in DTS
If you want, you can define partitions on your NAND. See [mtd partitions documentation][33966]  
For example, if your board have 4G NAND chip, you can split it to 5 partitions:  
[![Sticky-note-pin.png][33964]][33965] _Note:_ This partition table is example and can be changed in feature. 
Partition | Partition name | Partition size | Uses   
---|---|---|---  
/dev/mtd0 | boot0 | 2M | SPL   
/dev/mtd1 | boot0-rescue | 2M | SPL Backup   
/dev/mtd2 | uboot | 2M | U-Boot   
/dev/mtd3 | uboot-rescue | 2M | U-Boot Backup   
/dev/mtd4 | main | 4G | User data   
This lines should be placed in NFC node of your board's DTS. 
[code] 
    		boot0@0 {
    			label = "boot0";
    			reg = /bits/ 64 <0x0 0x200000>;
    		};
    
    		boot0-rescue@200000 {
    			label = "boot0-rescue";
    			reg = /bits/ 64 <0x200000 0x200000>;
    		};
    
    		uboot@400000 {
    			label = "uboot";
    			reg = /bits/ 64 <0x400000 0x200000>;
    		};
    
    		uboot-rescue@600000 {
    			label = "uboot-rescue";
    			reg = /bits/ 64 <0x600000 0x200000>;
    		};
    
    		main@800000 {
    			label = "main";
    			reg = /bits/ 64 <0x800000 0xff800000>;
    		};
    
[/code]
Armbian has a full device tree definition in their dt-overlay git repo <https://github.com/armbian/sunxi-DT-overlays/blob/e4dfea8304d66cb3403e5e1b73d2f346349124ec/sun7i-a20/sun7i-a20-nand.dts>
