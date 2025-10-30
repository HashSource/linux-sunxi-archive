# Remote Reboot Jig
Developing Linux on a remote board can be challenging, because sometimes you'll need to reboot a crashed board. This can be simplified using a remote reboot jig consisting of a [USB relay board][47143]. 
[![Development jig.JPG][47144]][47145]
[][47146]
Here is a ASCII art diagram of the schematic: 
[code] 
     ------                        -------
    |     +| ----[ USB relay ]----|+      |
    | 5V   |                      | board |
    |     -| ---------------------|-      |
     ------                        -------
    
[/code]
Basically, you put the relay between the power source and the board on the Vbus line. You could do this by splicing a USB extension cord, by buying the appropriate power connector, or very fancy using a [USB breakout board][47147]. 
You can find a cheap USB relay on eBay, by searching for "USB relay smart home". Single channel suffices for 1 board, but you could go large, of course. Controlling the board (given you bought the HID "driverless" version) is done through [this software][47148]: 
[code] 
    jorik@neon:~$ cat bin/cycle.sh 
    #!/bin/sh
    hidusb-relay-cmd on 2
    hidusb-relay-cmd off 2
    
[/code]
Of course, on/off may need to be swapped, since the relay is [SPDT][47149].
