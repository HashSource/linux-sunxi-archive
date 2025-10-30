# Cubieboard/JTAG
< [Cubieboard][14235]
 
There is no dedicated JTAG on Cubieboard. For some reason those 4 pins on the A10 is not routed on the board. 
JTAG is available in the uSD connector, and can be accessed via a breakout board, but this requires a breakout board and also debugging u-boot via this method requires constant switching between uSD breakout and uSD JTAG boot card to hald the CPU immediately. 
I had previously added a JTAG header to OLinuxIno A13 exposing the relevant uSD pins as a 20-pin JTAG header + wired up system reset to it as well. Now time to repeat this on the cubieboard. 
At the back of the board, "below" the logo there is an array of resistors like this: 
[code] 
              +(     )-
    
    [ ]*2*[ ]  +[ ]  *[ ]
                    1
    [ ]*4*[ ]   [ ]*  [ ]
    
    [ ]   [ ]   [ ]*3*[ ]
    
[/code]
[code] 
    + VCC_3_3/Vref JTAG20 pin 1
    - GND          JTAG20 pin 4,6,8,10,12,14,16,18,20
    1 TDI          JTAG20 pin 5
    2 TMS          JTAG20 pin 7 
    3 TCK          JTAG20 pin 9
    4 TDO          JTAG20 pin 13
    [Reset][14238]          JTAG20 pin 11
    
[/code]
Final result: 
[![Cubieboard MMC2 JTAG final.jpg][14239]][14240]
[][14241]
