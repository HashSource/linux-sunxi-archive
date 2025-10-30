# Replace NAND with eMMC howto
The page describes the process to replace some board 's internal raw-NAND flash to eMMC. It will destroy your device warranty. So please think carefully before you do it. 
  

## Contents
  * [1 Why replace NAND with eMMC][47181]
  * [2 Why it can work?][47182]
  * [3 Equipment Required][47183]
  * [4 A example on modify Mele i7(A31)][47184]

# Why replace NAND with eMMC
The documents of the SUNXI-NFC is very hard to find. Although Allwinner has been release the open-source version of all-series Allwinner SoCs. But to write a usable MTD-driver is still a hardwork to do. 
Compare NAND with eMMC. The eMMC is more fast, more safe and more open in Allwinner platform. To avoid the bad support of Allwinner NFC, you can choose to replace NAND with eMMC. 
# Why it can work?
[![FORESEE TSDPinout.png][47185]][47186]
[![EMMCseeinBottom.jpg][47187]][47188]
As you can see in this picture from CubieTruck. The NANDD[0:7] is multiplexed with SDC2D[0:3](on A10/A20) or SDC2D[0:7](on A31 and later SoC). 
And SDCMD/SDCLK is multiplexed with N0RB0 & N0RB1. So we can simply connect this pins to the eMMC. And we're ready to go! 
# Equipment Required
Tools: An iron, a nipper. Maybe a piece of glass (To handle the eMMC chip，otherwise the chip maybe slip. And to prevent your desktop from iron) and a pair of glass if you donˊt have a good vision on small thing :). 
Materials: An eMMC, some thin wire, some tins and rosins. 
WARNING: Please make sure that you know what you're doing! And you must to make sure that you can solder chip with in TSSOP package! Otherwise the device maybe DAMAGED!
# A example on modify Mele i7(A31)
[![Mele I7 PCB.JPG][47189]][47190]
[][47191]
With the following step, you can replace the NAND with eMMC. 
First, unload the case of this device. And watch the PCB of it. Now you can see what place the NAND is. 
[![Melei7 UnloadNAND.jpg][47192]][47193]
Second, put tins and rosins on the NAND's pin, when the tin on the pin is full, you can stop it. You can do the anyside first. And you should drag the irons up and down, back and forward to make sure that the side of NAND's tin is fully melted. With in the tin is melted, please use your nipper to catch the side of this chip, and steadly handle it up, that the one side of the chip has been removed from the PCB. And you can do the same of the other side to remove the NAND flash from the PCB. 
Third, uses rosins to clean up spare tins on the board, make sure that there are no pins is linked by tins. 
Forth, wire the thin wire on the eMMC, and connect it to board. I haven't good advice for it. I just can tell that you have to be calm. Maybe you should wear your glass for doing this job. You can wire the eMMC part first, and wire another part to the empty-SDcard to test if you're right. If you make sure that you have do the right thing, then wire another part to the board. 
[![WireaeMMCtoSD.jpg][47194]][47195]
Finally you can got that, and you can drop some rosins to fix the eMMC right on the place. If your board is A31 based, you must to setup boot jumper.Enjoy your new board with eMMC! 
[![Melei7withSandisk4GBeMMC.jpg][47196]][47197]
