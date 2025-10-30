# Cubieboard/SDC2
< [Cubieboard][14380]
 
## Contents
  * [1 Adding a second SD slot to Cubieboard][14383]
    * [1.1 Pin locations][14384]
    * [1.2 Implementation][14385]
    * [1.3 Issues][14386]

# Adding a second SD slot to Cubieboard
This adds a second SD card slot in parallell to the NAND chip. The board is prepared for both modes of operation, and in debugging U-Boot I need both JTAG and SD. 
Note: There is also an SDC3 slot available on expansion pins. But I wanted to use SDC2 to be able to test booting from that slot. 
## Pin locations
The SDC2 signals are all located just above the NAND chip. The row of 6 unmounted resistors just above the NAND is the 6 SDC2 signals. The upper pads are the CPU pads and the lower pads go to the SD slot mounting pads below the NAND. We will use the CPU pads here. 
This is an very easy spot to solder. We can solder on all three pads closest to the NAND chip providing a good grip for the cables, just don't short to the uppermost row (that's 3.3v) 
The signals is in the same order as on SD cards. 
From right (card edge) to left (towards center of the board) the pads are: 
Pad | GPIO | SIGNAL | SD | uSD   
---|---|---|---|---  
1 | PC10 | D2 | 9\ | 1   
2 | PC11 | D3 | 1 | 2   
3 | PC6 | CMD | 2 | 3   
- | - | VSS/GND | 3 | \-   
- | - | VDD_3V3 | 4 | 4   
4 | PC7 | CLK | 5 | 5   
- | - | VSS/GND | 6 | 6   
5 | PC8 | D0 | 7 | 7   
6 | PC9 | D1 | 8 | 8   
SD cards have a odd numbering and 9\ is the indented pin. The \ is meant to illustrate the indented corner of the card. 
VDD_3V3 and VSS/GND can be found at many places. I took them from one of the larger capacitors nearby. 
## Implementation
[![Cubieboard MMC2 JTAG final.jpg][14387]][14388]
[][14389]
I used a uSD to SD card adapter that I got "for free" with the last uSD card I bought. The adapter bridges pins #3 & #6 so I did not need to connect #6. If unsure connect both #3 and #6 to VSS/GND. 
To fit the casing nicely a litle hole was cut out from the uSD adapter. 
I did not add any pullup resistors. Seems to work fine without them. 
The picture shows final result after also adding an [JTAG header][14390]
## Issues
To boot direclty from SDC2 the NAND chip need to be blocked. Unfortunately I forgot to add wires for this, and have to use a small screwdriver or the like to short appropriate pins of the NAND to make it fail. Works but not the best solution. Will look into fixing that later ading a switch that blocks the NAND. Unfortunately I realized this only after glueing the uSD adapter ontop of the nand chip. 
uSD card adapters have no card present detect as they are themselves a SD card. Might be possible to add a pulldown resistor on D3 and use that as card detect. Something to investigate later. Right now I don't need card present detect function in this slot.
