# Used IP cores
This page defines a list of used IP cores of the current generation of Allwinner devices. 
Component name | IP core vendor | Driver available/usable? | A10 | A13 | A31 | A20 | A23 | A33   
---|---|---|---|---|---|---|---|---  
[Cortex A8][57553] | ARM ltd. | Mainline | Y | Y | N | N | N | N   
[Cortex A7][57554] | ARM ltd. | Mainline | N | N | Y | Y | Y | Y   
[GIC-400][57555] | ARM ltd. | Mainline | N | N | Y | N | Y | Y   
[IRQ][57556] | Unknown | Mainline, Allwinner | Y | Y | N | N | N | N   
[NMI][57557] | Unknown, seems to be a stripped down version of A10/A13 IRQ controller | Mainline, Allwinner | N | N | Y | Y | Y | Y   
[CCM][57558] | Most likely Allwinner | Mainline, Allwinner | Y | Y | Y | Y | Y | Y   
[SRAM][57559] Controller | Most likely Allwinner | Allwinner | Y | Y | Y | Y | Y | Y   
[DDR][57560] | Synopsys DesignWare, Same as Rockchip rk2918 DMC | Mainline/Allwinner U-Boot | Y | Y | N | Y | N | N   
[DDR][57560] | Synopsys DesignWare?, Similar to Xilinx Zynq UltraScale+ (reduced feature) | Mainline/Allwinner U-Boot | N | N | Y | N | Y | N   
[DDR][57560] | Synopsys DesignWare?, seems to be re-arranged A80/A23 DRAM controller | Mainline/Allwinner U-Boot | N | N | N | N | N | Y   
[JTAG][57561] | ARM CoreSight? | Limited by JTAG on/off in Fex system   
[DMA][57562] | Unknown | Allwinner | Y | Y | Y | Y   
[PWM][57563] | Most likely Allwinner | Allwinner   
[GPS][57564] | Highvision[[1]][57565] | No driver available. Only GPL-violating .ko were available, but untested | Y | N | N | N | N | N   
[G2D][57566] | Unknown | Allwinner implementation used. Might have connection to Exynos G2D.   
[GPU][57567] | ARM Mali-400 MP1 | Lima/ARM ltd | Y | Y | N | N   
[GPU][57567] | ARM Mali-400 MP2 | Lima/ARM ltd | N | N | N | Y   
[GPU][57567] | Imagination Technologies PowerVR SGX544 | ? | N | N | Y | N   
[IPU][57568] | Allwinner "DISP/LCD/HDMI" stack | Allwinner | Y | Y | Y | Y   
[Video Engine][57569] | Most likely a custom design by Chipsbank[[2]][57570] | Allwiner kernel driver + Blob | Y | Y | Y | Y   
[I2C][57571] | Marvell MV64xxx | Mainline | Y | Y | Y | Y   
[SPI][57572] | Unknown | Allwinner   
[UART][57573] | Synopsys DesignWare 8250 | Mainline | Y | Y | Y | Y   
[USB][57574] | ~~MentorGraphics MUSB~~ Generic OHCI/EHCI with glue | Allwinner | Y | Y | Y | Y   
[USB-OTG][57575] | MentorGraphics MSUSB[[3]][57576] | Allwinner (mainline musb)   
[SATA][57577] | Synopsys DesignWare SATA but PHY part maybe AW | Allwinner glue + mainline libata | Y | N | ? | Y   
[SD/MMC][57578] | Unknown | Allwinner | Y | Y | Y | Y   
[NAND][57579] | Unknown | Allwinner. Most likely IP core is not done by Allwinner due to weird glue | Y | Y | Y | Y   
[Memory Stick][57580] | Unknown | No driver available   
[CE-ATA][57581], IDE, ATA | Unknown | No driver available   
[TouchScreen controller][57582] | Unknown | Allwinner   
[SS][57583] | Unknown | No driver available   
[IR][57584] | Unknown | Allwinner | Y | ? | Y | Y   
[IIS][57585] | Unknown | Allwinner   
[AC97][57586] | Unknown | Allwinner   
[Keypad][57587] | Unknown | Allwinner   
[LRADC][57588] | Unknown | Allwinner | Y | Y | Y | Y   
[CSI][57589] | Unknown | Allwinner. Might use something pre made by MIPI   
[TransportStream][57590] | Unknown | Allwinner (3.4 only)   
[ACE][57591] | Most likely a custom design by Chipsbank[[2]][57570] | Allwinner   
[TV Encoder][57592] | Unknown | No driver available   
[GMAC][57593] | Synopsys DesignWare Ethernet MAC 10/100/1000 Universal | Allwinner. Mainline (3.14, stmmac) | N | N | Y? | Y   
[CAN][57594] | Unknown |   
## References
  1. [↑][57595] <http://www.highvision.com.cn/>
  2. ↑ [2.0][57596] [2.1][57597] <http://www.chipsbank.com/>
  3. [↑][57598] <http://www.mentor.com/products/ip/usb/usb20otg/upload/usb-2-0-multipoint-hi-speed-otg-controller-1c66e6a0-a88d-d2f7-65ca-77caf24abed0>
