# Sun8i emac
This page is about the _sun8i_emac_ /_dwmac-sun8i_ driver which handles the integrated Ethernet MAC of A83T/H3/A64. 
## Contents
  * [1 Specifications][51517]
  * [2 Status][51518]
    * [2.1 H3][51519]
    * [2.2 A83T][51520]
    * [2.3 A64][51521]
      * [2.3.1 Pine64+ (Gigabit PHY)][51522]
  * [3 Tips, troubleshoot][51523]
  * [4 Performance][51524]

## Specifications
The EMAC main features are 
  * 10/100/1000 Mbit/s speed
  * RX/TX CSO (CheckSum Offload)

## Status
Linux driver is dwmac-sun8i, a glue to the stmmac driver. You can find the latest version at <https://github.com/montjoie/linux/tree/dwmac-sun8i-current>
Another legacy driver, sun8i-emac, exist as well. You can find the latest sun8i-emac driver version on <https://github.com/montjoie/linux/tree/sun8i-emac-wip> This driver will never reach mainline and development is discontinued. 
### H3
The H3 SoC is well supported, and no tweaks are necessary for all MII types (Internal MII, RGMII). 
### A83T
  * BananaPI M3: For powering the PHY you need wens' a80-pmic uboot branch (<https://github.com/wens/u-boot-sunxi/tree/a80-pmic>).
  * H8 homlet: The PHY is AC200 for which there is no datasheet.

### A64
The stock boot0 or the BSP U-Boot do not program the PMIC to power the PHY. The latest ["upstream" firmware][51525] enables the PHY in the ARM Trusted Firmware (ATF) [code][51526], so the EMAC driver works there. 
#### Pine64+ (Gigabit PHY)
Section C5 on page 19 in the schematics shows the power requirements: 
  * DC1-SW needs to be enabled (bit 7 in register 0x12 of the AXP803 PMIC).
  * The schematics hints that the GPIO1 output on the PMIC needs to be configured as an LDO output at 2.5 volts (0x12 (=2.5V) into PMIC register 0x93, 0x3 (=enable LDO) to PMIC register 0x92). But the BSP kernel leaves this register disabled (0x92: 0x7), so apparently no driving is needed here. That means that the Pine64+ runs RGMII at 3.3 volts.
  * The PHYRSTB pin on the PHY is connected to the SoC's PD14 pin (confusingly labeled MAC-RST), but also pulled up. PD14 is part of the EMAC block (RGMII-NULL), but needs to be configured differently (not function 4): either as disabled (7) or as a high output pin.

## Tips, troubleshoot
  * EMAC reset timeout

This error is generally related to not having PHY powered. 
  * Link but no transfer with Gigabit EMAC

You perhaps need to tweak RX/TX delay. You could find the correct value in FEX files. 
For the moment the only way is to write the value via /dev/mem. 
You could use either busybox's `devmem` applet or compile the free-electrons.com/pub/mirror/devmem2.c utility for this. 
Example: for BPIM3 
devmem 0x1c00030 w 0x1806 
  * MAC address with 3 leading zeros

Try a more recent uboot 
  * No link when booting with cable attached

Try a more recent uboot 
## Performance
Performance is calculated with `iperf`. Thoses numbers are not definitive. 
| Transmission | Reception | Notes   
---|---|---|---  
OrangePiPC (100Mbit FullDuplex) | 94Mb/s | 94Mb/s   
Bananapi M3 (Gigabit FD) | 373Mb/s | 387Mb/s | no PSCI   
Pine64 | 511Mb/s | 428Mb/s |
