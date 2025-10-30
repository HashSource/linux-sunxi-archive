# MarsBoard/JTAG
## Contents
  * [1 Connection][35449]
  * [2 Notes:][35450]
  * [3 Lauterbach Trace32][35451]
  * [4 See Also][35452]

## Connection
The marsboard P2 connector includes the UART 0 and JTAG signals as 3.3V TTL!. 
You will need to make a JTAG adapter to suit your JTAG debugger. 
**ARM 20-pin JTAG** | **MarsBoard P2 Header**  
---|---  
pin 1 - Vref | pin 63 - VCC-3V3   
pin 5 - TDI | pin 70 - JTAG-DI   
pin 7 - TMS | pin 67 - JTAG-MS   
pin 9 - TCK | pin 68 - JTAG-CK   
pin 13 - TDO | pin 68 - JTAG-DO   
pins 2-20 (even) | pin 64 - GND   
Check your JTAG tool's cable details for alternate pinouts. 
  * MarsBoard P2-uart-jtag.png
MarsBoard P2 connector debug pins. 
  * [![][35453]][35454]
ARM 20-pin JTAG Header. 
  * [![][35455]][35456]
Combo serial / JTAG breakout. 

## Notes:
**On Allwinner A20** : 
  * Ensure Linux power-management is **disabled** and both CPUs are enabled to connect reliably, or setup your debugger to use a single-core only.

[code] 
     echo userspace > /sys/bus/cpu/devices/cpu0/cpufreq/scaling_governor
     echo 1 > /sys/bus/cpu/devices/cpu0/online
     echo 1 > /sys/bus/cpu/devices/cpu1/online
    
[/code]
## Lauterbach Trace32
The following are a single-core and dual-core version of the script. 
[code] 
       ; MarsBoard A20 uniprocessor Trace32 Script
       ; connect to CPU0 only
       ; 2013-08-12
    
       RESet
       SYStem.CPU CortexA7MPCore
       SYStem.CONFIG CoreNumber 1.
       CORE.ASSIGN 1.
    
       SYStem.JTAGCLOCK 20MHz
    
       SYStem.CONFIG MEMORYACCESSPORT 0.
       SYStem.CONFIG DEBUGACCESSPORT 1.
       SYStem.CONFIG COREBASE              0x80110000
       SYStem.CONFIG BMCBASE               0x80111000
    
       SYStem.Option EnReset OFF
    
       ; Allwinner A20 Details
       MAP.BONCHIP 0xffff0000--0xffff7fff
    
       Break.Implementation Program Onchip
    
       SYStem.Up
    
[/code]
The script below connects to the A20 configured in SMP mode with both CPUs powered on. If you are in the bootloader or trying to connect while only CPU0 is online, use the uni-processor script. 
[code] 
       ; MarsBoard A20 Dual-Core Trace32 Script
       ; This script requires BOTH cores to be powered on!
       ; 2013-08-12
    
       RESet
       SYStem.CPU CortexA7MPCore
       SYStem.CONFIG CoreNumber 2.
       CORE.ASSIGN 1. 2.
    
       SYStem.JTAGCLOCK 20MHz
    
       SYStem.CONFIG MEMORYACCESSPORT 0.
       SYStem.CONFIG DEBUGACCESSPORT 1.
       SYStem.CONFIG COREBASE              0x80110000 0x80112000
       SYStem.CONFIG BMCBASE               0x80111000 0x80113000
    
       SYStem.Option EnReset OFF
    
       ; Allwinner A20 Details
       MAP.BONCHIP 0xffff0000--0xffff7fff
    
       Break.Implementation Program Onchip
    
       SYStem.Up
    
[/code]
## See Also
[JTAG][35457]
