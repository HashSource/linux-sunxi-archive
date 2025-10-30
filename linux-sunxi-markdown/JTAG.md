# JTAG
[![][28867]][28868]
[][28869]
[µSD breakout][28870] showing 14pin JTAG connector
Initial notes: 
  * JTAG over Microsd
  * Below is default setup (A10) at boot! Bootloader etc may change it
  * Only tested with a microsd breakout board designed for a10
  * microsd breakout seems to have specific pull-ups/pull-downs in the board
  * I will test with direct connection to microsd pins later.
  * This has been tested on an MK802 only, but should theoretically work for everything.
  * This has been confirmed working on an A13 Tablet as well.

Microsd | Pin | JTAG Connection | 14-pin ARM JTAG Header   
---|---|---|---  
Data2 | 1 | TCK | 9   
Cmd | 3 | TDO | 11   
Data0 | 7 | TDI | 5   
Data1 | 8 | TMS | 7   
VDD | 4 | VTG | 1,13   
GND | 6 | GND |  2,3,4,6,8,10,12,14   
It is important to make sure boot0/boot1/u-boot/kernel doesn't pinmux this away, so nothing else must be using the pins. The script.bin needs to contain a correct jtag_para section. On my device, the default script.bin seems to contain an invalid configuration for the ports in question. Below is the configuration matching the working JTAG! 
[code] 
    [jtag_para]
    jtag_enable = 1
    jtag_ms = port:PF00<4><default><default><default>
    jtag_ck = port:PF05<4><default><default><default>
    jtag_do = port:PF03<4><default><default><default>
    jtag_di = port:PF01<4><default><default><default>
    
[/code]
I used a Dangerous Prototypes Bus Blaster V2(.5) for my experiments (<http://dangerousprototypes.com/docs/Bus_Blaster>). I'm using the default buffer, which makes it jtagkey compatible. For now, i've only verified that both UrJTAG and OpenOCD can detect a device over the JTAG connection, but I haven't managed to read/write from memory yet or anything else fancy. 
Some output: UrJTAG detect: 
[code] 
    jtag> detect
    IR length: 4
    
    Chain length: 1
    
    Device Id: 01001011101000000000010001110111 (0x4BA00477)
    
      Unknown manufacturer! (01000111011) (/usr/local/share/urjtag/MANUFACTURERS)
    
[/code]
UrJTAG discovery: 
[code] 
    jtag> discovery
    Detecting IR length ... 4
    Detecting DR length for IR 1111 ... 1
    Detecting DR length for IR 0000 ... 1
    Detecting DR length for IR 0001 ... 1
    Detecting DR length for IR 0010 ... 1
    Detecting DR length for IR 0011 ... 1
    Detecting DR length for IR 0100 ... 1
    Detecting DR length for IR 0101 ... 1
    Detecting DR length for IR 0110 ... 1
    Detecting DR length for IR 0111 ... 1
    Detecting DR length for IR 1000 ... 35
    Detecting DR length for IR 1001 ... 1
    Detecting DR length for IR 1010 ... 35
    Detecting DR length for IR 1011 ... 35
    Detecting DR length for IR 1100 ... 1
    Detecting DR length for IR 1101 ... 1
    Detecting DR length for IR 1110 ... 32
    
[/code]
  
Extremely work in progress OpenOCD cfg: 
[sun4i.cfg][28871]
Tested OpenOCD features: 
  * dumping memory (sun4i.cpu mdw commands)
  * halt & resuming
  * gdb 
    * Loading files (tested with fel-pio)
    * Single-stepping lines/instructions through loaded programs
    * Breakpoints

## See also
  * [MicroSD Breakout][28870]
  * [A10/PIO][28872]
  * [A13/PIO][28873]
  * [MarsBoard/JTAG][28874] \- includes A20 Trace32 script
