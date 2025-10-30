# Timers Controller Register guide
(Redirected from [A10/TIMER][949])
 
## Contents
  * [1 Timer Controller][952]
    * [1.1 Timer Registers][953]
      * [1.1.1 TMR_IRQ_EN][954]
      * [1.1.2 TMR_IRQ_STA][955]
      * [1.1.3 TMR_0_CTRL][956]
      * [1.1.4 TMR_0_INTR_VAL][957]
      * [1.1.5 TMR_0_CUR_VAL][958]
      * [1.1.6 TMR_1_CTRL][959]
      * [1.1.7 TMR_1_INTR_VAL][960]
      * [1.1.8 TMR_1_CUR_VAL][961]
      * [1.1.9 TMR_2_CTRL][962]
      * [1.1.10 TMR_2_INTR_VAL][963]
      * [1.1.11 TMR_2_CUR_VAL][964]
      * [1.1.12 TMR_3_CTRL][965]
      * [1.1.13 TMR_3_INTR_VAL][966]
      * [1.1.14 TMR_4_CTRL][967]
      * [1.1.15 TMR_4_INTR_VAL][968]
      * [1.1.16 TMR_4_CUR_VAL][969]
      * [1.1.17 TMR_5_CTRL][970]
      * [1.1.18 TMR_5_INTR_VAL][971]
      * [1.1.19 TMR_5_CUR_VAL][972]
      * [1.1.20 TMR_AVS_CTRL][973]
      * [1.1.21 TMR_AVS0_VAL][974]
      * [1.1.22 TMR_AVS1_VAL][975]
      * [1.1.23 TMR_AVS_DIV][976]
      * [1.1.24 TMR_WDT_CTRL][977]
      * [1.1.25 TMR_WDT_MODE][978]
      * [1.1.26 TMR_CNT64_CTRL][979]
      * [1.1.27 TMR_CNT64_LO][980]
      * [1.1.28 TMR_CNT64_HI][981]
      * [1.1.29 TMR_32KHZ_OSC_CTRL][982]
      * [1.1.30 TMR_RTC_DATE][983]
      * [1.1.31 TMR_RTC_TIME][984]
      * [1.1.32 TMR_ALARM_CNT][985]
      * [1.1.33 TMR_ALARM_WK][986]
      * [1.1.34 TMR_ALARM_EN][987]
      * [1.1.35 TMR_ALARM_IRQ][988]
      * [1.1.36 TMR_ALARM_IRQ_STATUS][989]
      * [1.1.37 TMR_GP0][990]
      * [1.1.38 TMR_GP1][991]
      * [1.1.39 TMR_GP2][992]
      * [1.1.40 TMR_GP3][993]
      * [1.1.41 CPU_CFG][994]
    * [1.2 Initial values][995]
      * [1.2.1 default map][996]
      * [1.2.2 all set to 1][997]
      * [1.2.3 all set to 0][998]

# Timer Controller
The A10 SoC has 6 timers, an RTC, alarm timer and an AVS-timer. 
Timer 0 and 1 can configure their input to come from various sources, the internal oscillator, the external 32K crystal or the external 24MHz crystal. Their main function is the provide an interrupt for the scheduler in the kernel. They both are programmable, 24bit wide and can safely overflow. Reload mode can be programmed to auto-reload or not. 
Timer 2 is usable by the kernel to generate periodic interrupts. 
Timers 3, 4 and 5 are general purpose timers. 
The watchdog timer resets the system in case of system errors. It can be re-purposed as a regular 16bit interval timer to request an interrupt. The generated signal is a the reset signal. 
The Real Time Clock (RTC) timer is normally a battery powered timer to be used as a timekeeping device. If software tells it that the current year is a leap year, it will automatically correct the dates for this year. On the SoC it has a dedicated power pin (RTCVDD) to supply either battery or live power. 
The Alarm timer can trigger an alarm even when battery powered (via the RTC). When running from battery only the power-management wakeup signal is activated. Otherwise the power-management wakeup signal and the alarm interrupt are triggered. 
An Audio Video Sync (AVS) timer with as purpose to synchronize audio and video data. One large 64bit counter, actually split up into two 32bit registers. 
Note for devs: according avs driver code AVS have some differences between A10 revisions 
## Timer Registers
Timer Base address: 0x01c20c00 
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`TMR_IRQ_EN` | `0x0000` | `4B` | All timer IRQ's Enable/Disable   
`TMR_IRQ_STA` | `0x0004` | `4B` | All timer status   
`TMR_0_CTRL` | `0x0010` | `4B` | Timer 0 control   
`TMR_0_INTR_VAL` | `0x0014` | `4B` | Timer 0 interval value   
`TMR_0_CUR_VAL` | `0x0018` | `4B` | Timer 0 Current Value   
`TMR_1_CTRL` | `0x0020` | `4B` | Timer 1 control   
`TMR_1_INTR_VAL` | `0x0024` | `4B` | Timer 1 interval value   
`TMR_1_CUR_VAL` | `0x0028` | `4B` | Timer 1 Current Value   
`TMR_2_CTRL` | `0x0030` | `4B` | Timer 2 control   
`TMR_2_INTR_VAL` | `0x0034` | `4B` | Timer 2 interval value   
`TMR_2_CUR_VAL` | `0x0038` | `4B` | Timer 2 Current Value   
`TMR_3_CTRL` | `0x0040` | `4B` | Timer 3 control   
`TMR_3_INTR_VAL` | `0x0044` | `4B` | Timer 3 interval value   
`TMR_3_CUR_VAL` | `0x0048` | `4B` | Timer 3 Current Value   
`TMR_4_CTRL` | `0x0050` | `4B` | Timer 4 control   
`TMR_4_INTR_VAL` | `0x0054` | `4B` | Timer 4 interval value   
`TMR_4_CUR_VAL` | `0x0058` | `4B` | Timer 4 Current Value   
`TMR_5_CTRL` | `0x0060` | `4B` | Timer 5 control   
`TMR_5_INTR_VAL` | `0x0064` | `4B` | Timer 5 interval value   
`TMR_5_CUR_VAL` | `0x0068` | `4B` | Timer 5 Current Value   
`TMR_AVS_CTRL` | `0x0080` | `4B` | AVS control   
`TMR_AVS0` | `0x0084` | `4B` | AVS Counter 0   
`TMR_AVS1` | `0x0088` | `4B` | AVS Counter 1   
`TMR_AVS_DIV` | `0x008c` | `4B` | AVS Divisor   
`TMR_WDT_CTRL` | `0x0090` | `4B` | Watchdog timer control   
`TMR_WDT_MODE` | `0x0094` | `4B` | Watchdog timer operating mode   
`TMR_CNT64_CTRL` | `0x00a0` | `4B` | 64bit counter control   
`TMR_CNT64_LO` | `0x00a4` | `4B` | 64bit counter lower-half   
`TMR_CNT64_HI` | `0x00a8` | `4B` | 64bit counter upper-half   
`TMR_32KHZ_OSC_CTRL` | `0x0100` | `4B` | Control the 32kHz timing crystal   
`TMR_RTC_DATE` | `0x0104` | `4B` | RTC date value   
`TMR_RTC_TIME` | `0x0108` | `4B` | RTC time value   
`TMR_ALARM_CNT` | `0x010a` | `4B` | Alarm counter counting days, hours, minutes and seconds   
`TMR_ALARM_WK` | `0x0110` | `4B` | Daily alarm   
`TMR_ALARM_EN` | `0x0114` | `4B` | Overal alarm enable   
`TMR_ALARM_IRQ_EN` | `0x0118` | `4B` | Alarm interrupt enable   
`TMR_ALARM_IRQ_STA` | `0x011c` | `4B` | Alarm interrupt status   
`TMR_GP0` | `0x0120` | `4B` | General purpose timer 0   
`TMR_GP1` | `0x0124` | `4B` | General purpose timer 1   
`TMR_GP2` | `0x0128` | `4B` | General purpose timer 2   
`TMR_GP3` | `0x012c` | `4B` | General purpose timer 3   
`CPU_CFG` | `0x013c` | `4B` | CPU configuration   
  

##### TMR_IRQ_EN
Default value: 0x00000000  
Offset: 0x0000 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_IRQ0_EN` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| Timer 0 interrupt   
`TMR_IRQ1_EN` | `1` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| Timer 1 interrupt   
`TMR_IRQ2_EN` | `2` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| Timer 2 interrupt   
`TMR_IRQ3_EN` | `3` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| Timer 3 interrupt   
`TMR_IRQ4_EN` | `4` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| Timer 4 interrupt   
`TMR_IRQ5_EN` | `5` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| Timer 5 interrupt   
`undefined` | `6:7` | `Read` | `0b00` |  |   
`TMR_IRQ_WDT_EN` | `8` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| Watchdog timer interrupt   
`no operation` | `9:12` |  |  |  |   
`unknown` | `13` | `Read` | `0b0` |  |   
`no operation` | `14:31` |  |  |  |   
##### TMR_IRQ_STA
Default value: 0x00000000  
Offset: 0x0004 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_IRQ0_PEN` | `0` | `Read/Write` | `0b0` | ` `
[code]
       0 = no operation
       Read:
         1 = Interrupt pending
       Write:
         1 = Clear interrupt
      
    
[/code]
| Timer 0 interrupt value reached   
`TMR_IRQ1_PEN` | `1` | `Read/Write` | `0b0` | ` `
[code]
       0 = no operation
       Read:
         1 = Interrupt pending
       Write:
         1 = Clear interrupt
      
    
[/code]
| Timer 1 interrupt value reached   
`TMR_IRQ2_PEN` | `2` | `Read/Write` | `0b0` | ` `
[code]
       0 = no operation
       Read:
         1 = Interrupt pending
       Write:
         1 = Clear interrupt
      
    
[/code]
| Timer 2 interrupt value reached   
`TMR_IRQ3_PEN` | `3` | `Read/Write` | `0b0` | ` `
[code]
       0 = no operation
       Read:
         1 = Interrupt pending
       Write:
         1 = Clear interrupt
      
    
[/code]
| Timer 3 interrupt value reached   
`TMR_IRQ4_PEN` | `4` | `Read/Write` | `0b0` | ` `
[code]
       0 = no operation
       Read:
         1 = Interrupt pending
       Write:
         1 = Clear interrupt
      
    
[/code]
| Timer 4 interrupt value reached   
`TMR_IRQ5_PEN` | `5` | `Read/Write` | `0b0` | ` `
[code]
       0 = no operation
       Read:
         1 = Interrupt pending
       Write:
         1 = Clear interrupt
      
    
[/code]
| Timer 5 interrupt value reached   
`no operation` | `6` |  |  |  | _Could be for AVS timer?_  
`no operation` | `7` |  |  |  |   
`TMR_IRQ_WDT_PEN` | `8` | `Read/Write` | `0b0` | ` `
[code]
       0 = no operation
       Read:
         1 = Interrupt pending
       Write:
         1 = Clear interrupt
      
    
[/code]
| Watchdog timer interrupt value reached   
`no operation` | `9:31` |  |  |  | padding   
##### TMR_0_CTRL
Default value: 0x00000005  
Offset: 0x0010 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_0_RUN` | `0` | `Read/Write` | `0b1` | ` `
[code]
        0 = stop/pause
        1 = start
      
    
[/code]
| Timer 0 start/stop  
On start, the countdown value is reloaded (T=0) and will start counting down to zero (T=1). Because of this atleast 2 T-Cycles[[1]][999] need to have passed in time between stop and start when reloading during active countdown.  
While counting down the timer TMR_0_RUN bit is set to 0, the countdown will pause. Again, wait at least 2 T-Cycles before starting the timer.  
While the timer is paused, the countdown value can be modified. For the timer to use this new value, TMR_0_RELOAD should be set to 1.  
  
`TMR_0_RELOAD` | `1` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = reload
      
    
[/code]
| Timer 0 reload   
`TMR_0_CLK_SRC` | `2:3` | `Read/Write` | `0b01` | ` `
[code]
        0x0 = 32kHz crystal 
        0x1 = 24MHz crystal
        0x2 = PLL6 divided by 6
        0x3 = no operation
      
    
[/code]
| Timer 0 clock source   
`TMR_0_CLK_PRESCALE` | `4:6` | `Read/Write` | `0b000` | ` `
[code]
        0x0 = div(1)
        0x1 = div(2)
        0x2 = div(4)
        0x3 = div(8)
        0x4 = div(16)
        0x5 = div(32)
        0x6 = div(64)
        0x7 = div(128)
      
    
[/code]
| Timer 0 clock pre-scale divisor.  
Uses TMR_0_CLK_PRESCALE to divide TMR_0_CLK_SRC with.   
`TMR_0_MODE` | `7` | `Read/Write` | `0b0` | ` `
[code]
        0 = continuous mode, restarts when timer has finished counting down
        1 = single, stop when done counting down
      
    
[/code]
| Timer 0 mode   
`no operation` | `8:31` |  |  |  |   
  1. [↑][1000] A Timer Cycle (T-Cycle) is defined as **Timer clock source/pre-scale**

##### TMR_0_INTR_VAL
Default value: undefined  
Offset: 0x0014 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_0_INTR_VAL` | `0:31` | `Read/Write` | `0xffffffff` | `0 - 232-1` | Timer 0 interval value   
##### TMR_0_CUR_VAL
Default value: undefined  
Offset: 0x0018 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_0_CUR_VAL` | `0:31` | `Read/Write` | `0x00` | `0 - 232-1` | Timer 0 current value  
This value can only be read back accurately if the PCLK is more than 2 T-Cycles.   
  

##### TMR_1_CTRL
Default value: 0x00000004  
Offset: 0x0020 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_1_RUN` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = stop/pause
        1 = start
      
    
[/code]
| Timer 1 start/stop  
See timer 0 description for additional information.   
`TMR_1_RELOAD` | `1` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = reload
      
    
[/code]
| Timer 1 reload   
`TMR_1_CLK_SRC` | `2:3` | `Read/Write` | `0b01` | ` `
[code]
        0x0 = 32kHz crystal 
        0x1 = 24MHz crystal
        0x2 = PLL6 divided by 6
        0x3 = no operation
      
    
[/code]
| Timer 1 clock source   
`TMR_0_CLK_PRESCALE` | `4:6` | `Read/Write` | `0x00` | ` `
[code]
        0x0 = div(1)
        0x1 = div(2)
        0x2 = div(4)
        0x3 = div(8)
        0x4 = div(16)
        0x5 = div(32)
        0x6 = div(64)
        0x7 = div(128)
      
    
[/code]
| Timer 1 clock pre-scale divisor.  
Uses TMR_1_CLK_PRESCALE to divide TMR_1_CLK_SRC with.   
`TMR_1_MODE` | `7` | `Read/Write` | `0b0` | ` `
[code]
        0 = continuous mode, restarts when timer has finished counting down
        1 = single, stop when done counting down
      
    
[/code]
| Timer 1 mode   
`no operation` | `8:31` |  |  |  | padding   
##### TMR_1_INTR_VAL
Default value: 0x00000000  
Offset: 0x0024 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_1_INTR_VAL` | `0:31` | `Read/Write` | `0x0000` | `0 - 232-1` | Timer 1 interval value   
##### TMR_1_CUR_VAL
Default value: undefined  
Offset: 0x0028 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_1_CUR_VAL` | `0:31` | `Read/Write` | `0x00` | `0 - 232-1` | Timer 1 current value  
See timer 0 description for additional information.   
  

##### TMR_2_CTRL
Default value: 0x00000004  
Offset: 0x0030 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_2_RUN` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = stop/pause
        1 = start
      
    
[/code]
| Timer 2 start/stop  
See timer 0 description for additional information.   
`TMR_2_RELOAD` | `1` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = reload
      
    
[/code]
| Timer 2 reload   
`TMR_2_CLK_SRC` | `2:3` | `Read/Write` | `0b1` | ` `
[code]
        0x0 = 32kHz crystal 
        0x1 = 24MHz crystal
        0x2 = PLL6 divided by 6
        0x3 = no operation
      
    
[/code]
| Timer 2 clock source   
`TMR_2_CLK_PRESCALE` | `4:6` | `Read/Write` | `0x00` | ` `
[code]
        0x0 = div(1)
        0x1 = div(2)
        0x2 = div(4)
        0x3 = div(8)
        0x4 = div(16)
        0x5 = div(32)
        0x6 = div(64)
        0x7 = div(128)
      
    
[/code]
| Timer 2 clock pre-scale divisor.  
Uses TMR_2_CLK_PRESCALE to divide TMR_2_CLK_SRC with.   
`TMR_2_MODE` | `7` | `Read/Write` | `0b0` | ` `
[code]
        0 = continuous mode, restarts when timer has finished counting down
        1 = single, stop when done counting down
      
    
[/code]
| Timer 2 mode   
`no operation` | `8:31` |  |  |  | padding   
##### TMR_2_INTR_VAL
Default value: 0x00000000  
Offset: 0x0034 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_2_INTR_VAL` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | Timer 2 interval value   
##### TMR_2_CUR_VAL
Default value: 0x00000000  
Offset: 0x0038 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_2_CUR_VAL` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | Timer 2 current value  
See timer 0 description for additional information.   
##### TMR_3_CTRL
Default value: 0x00000000  
Offset: 0x0040 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_3_RUN` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| Timer 3 enable/disable  
  
`no operation` | `1` |  |  |  |   
`TMR_3_CLK_PRESCALE` | `2:3` | `Read/Write` | `0b00` | ` `
[code]
        0x0 = div(16)
        0x1 = div(32)
        0x2 = div(64)
        0x3 = no operation
      
    
[/code]
| Timer 3 clock pre-scale divisor.  
Uses TMR_3_CLK_PRESCALE to divide the 32kHz clock with.   
`TMR_3_MODE` | `4` | `Read/Write` | `0b0` | ` `
[code]
        0 = continuous mode, restarts when timer has finished counting down
        1 = single, stop when done counting down
      
    
[/code]
| Timer 4 mode   
`no operation` | `5:31` |  |  |  |   
##### TMR_3_INTR_VAL
Default value: 0x00000000  
Offset: 0x0044 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_3_INTR_VAL` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | Timer 3 interval value   
##### TMR_4_CTRL
Default value: 0x00000004  
Offset: 0x0050 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_4_RUN` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = stop/pause
        1 = start
      
    
[/code]
| Timer 4 start/stop  
See timer 0 description for additional information.   
`TMR_4_RELOAD` | `1` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = reload
      
    
[/code]
| Timer 4 reload   
`TMR_4_CLK_SRC` | `2:3` | `Read/Write` | `0b1` | ` `
[code]
        0x0 = 32kHz crystal 
        0x1 = 24MHz crystal
        0x2 = External CLKIN0 pin
        0x3 = no operation
      
    
[/code]
| Timer 4 clock source  
If TMR_4_CLK_SRC is set to 0x2, the timer is no longer a down-counter, but an up-counter starting at 0.   
`TMR_4_CLK_PRESCALE` | `4:6` | `Read/Write` | `0b00` | ` `
[code]
        0x0 = div(1)
        0x1 = div(2)
        0x2 = div(4)
        0x3 = div(8)
        0x4 = div(16)
        0x5 = div(32)
        0x6 = div(64)
        0x7 = div(128)
      
    
[/code]
| Timer 4 clock pre-scale divisor.  
Uses TMR_4_CLK_PRESCALE to divide TMR_4_CLK_SRC with.   
`TMR_4_MODE` | `7` | `Read/Write` | `0b0` | ` `
[code]
        0 = continuous mode, restarts when timer has finished counting down
        1 = single, stop when done counting down
      
    
[/code]
| Timer 4 mode   
`no operation` | `8:31` |  |  |  |   
##### TMR_4_INTR_VAL
Default value: 0x00000000  
Offset: 0x0054 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_2_INTR_VAL` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | Timer 4 interval value  
Close attention to TMR_4_CLK_SRC should be payed!   
##### TMR_4_CUR_VAL
Default value: 0x00000000  
Offset: 0x0058 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_4_CUR_VAL` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | Timer 4 current value  
TMR_4_CUR_VAL is uninitialized and should be set to 0 before use. See timer 0 description for additional information.   
##### TMR_5_CTRL
Default value: 0x00000004  
Offset: 0x0060 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_5_RUN` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = stop/pause
        1 = start
      
    
[/code]
| Timer 5 start/stop  
See timer 0 description for additional information.   
`TMR_5_RELOAD` | `1` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = reload
      
    
[/code]
| Timer 5 reload   
`TMR_5_CLK_SRC` | `2:3` | `Read/Write` | `0b01` | ` `
[code]
        0x00 = 32kHz crystal 
        0x01 = 24MHz crystal
        0x02 = External CLKIN1 pin
        0x03 = no operation
      
    
[/code]
| Timer 5 clock source  
If TMR_5_CLK_SRC is set to 0x2, the timer is no longer a down-counter, but an up-counter starting at 0.   
`TMR_5_CLK_PRESCALE` | `4:6` | `Read/Write` | `0b00` | ` `
[code]
        0x00 = div(1)
        0x01 = div(2)
        0x02 = div(4)
        0x03 = div(8)
        0x04 = div(16)
        0x05 = div(32)
        0x06 = div(64)
        0x07 = div(128)
      
    
[/code]
| Timer 5 clock pre-scale divisor.  
Uses TMR_5_CLK_PRESCALE to divide TMR_5_CLK_SRC with.   
`TMR_5_MODE` | `7` | `Read/Write` | `0b0` | ` `
[code]
        0 = continuous mode, restarts when timer has finished counting down
        1 = single, stop when done counting down
      
    
[/code]
| Timer 5 mode   
`no operation` | `8:31` |  |  |  |   
##### TMR_5_INTR_VAL
Default value: 0x00000000  
Offset: 0x0064 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_5_INTR_VAL` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | Timer 5 interval value  
Close attention to TMR_5_CLK_SRC should be payed!   
##### TMR_5_CUR_VAL
Default value: 0x00000000  
Offset: 0x0068 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_5_CUR_VAL` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | Timer 5 current value  
TMR_5_CUR_VAL is uninitialized and should be set to 0 before use.  
See timer 0 description for additional information.   
##### TMR_AVS_CTRL
Default value: 0x00000000  
Offset: 0x0080 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_AVS0_EN` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| Audio/Video Sync counter 0.  
The AVS counter always uses the 24MHz clock.   
`TMR_AVS1_EN` | `1` | `Read/Write` | `0b0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| Audio/Video Sync counter 1.  
The AVS counter always uses the 24MHz clock.   
`no operation` | `2:7` |  |  |  |   
`TMR_AVS0_PAUSE` | `8` | `Read/Write` | `0b0` | ` `
[code]
        0 = run
        1 = pause
      
    
[/code]
| Pause AVS counter 0   
`TMR_AVS1_PAUSE` | `9` | `Read/Write` | `0b0` | ` `
[code]
        0 = run
        1 = pause
      
    
[/code]
| Pause AVS counter 1   
`no operation` | `10:31` |  |  |  |   
##### TMR_AVS0_VAL
Default value: 0x00000000  
Offset: 0x0084 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_AVS0_VAL` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | The 32 high bits of the internal 33-bits AVS counter. The value of the AVS counter can be written to at any time and the LSB bit should be internally initialized to 0.   
##### TMR_AVS1_VAL
Default value: 0x00000000  
Offset: 0x0088 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_AVS1_VAL` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | The 32 high bits of the internal 33-bits AVS counter. The value of the AVS counter can be written to at any time and the LSB bit should be internally initialized to 0.   
##### TMR_AVS_DIV
Default value: 0x05db05db  
Offset: 0x008c 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_AVS0_DIV` | `0:11` | `Read/Write` | `0x05db` | ` `
[code]
        0x0000 = div(1)
        0x0001 = div(2)
        ...
        n = div(n + 1)
        ...
        0x07ff = div(2048)
      
    
[/code]
| Uses TMR_AVS0_DIV as divisor on the 24MHz clock.  
The AVS counter internally uses an extra 12-bit counter. This counter is tied to the 24MHz clock. Whenever the internal 12-bit counter >= TMR_AVS0_DIV the actual 33-bit counter is increased.   
`no operation` | `12:15` |  |  |  |   
`TMR_AVS1_DIV` | `16:27` | `Read/Write` | `0x05db` | ` `
[code]
        0x0000 = div(1)
        0x0001 = div(2)
        ...
        n = div(n + 1)
        ...
        0x07ff = div(2048)
      
    
[/code]
| Uses TMR_AVS1_DIV as divisor on the 24MHz clock.  
The AVS counter internally uses an extra 12-bit counter. This counter is tied to the 24MHz clock. Whenever the internal 12-bit counter >= TMR_AVS1_DIV the actual 33-bit counter is increased.   
`no operation` | `28:31` |  |  |  |   
##### TMR_WDT_CTRL
Default value: 0x00000000  
Offset: 0x0090 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_WDT_CTRL` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = restart
      
    
[/code]
| Restarts the watchdog timer.   
`TMR_WDT_KEY` | `1:12` | `Write` | `0x00` | `0x0a57` | The watchdog timer needs a key to be re-armed/reset. 0x0a57 is this key and needs to be supplied[[1]][1001] on a restart; 
[code]
    TMR_WDT_CTRL | TMR_WDT_KEY << 1
[/code]  
`no operation` | `13:31` |  |  |  |   
  1. [↑][1002] The key is only required on a running watchdog.

##### TMR_WDT_MODE
Default value: 0x00000002  
Offset: 0x0094 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_WDT_EN` | `0` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| Enables the watchdog timer.   
`TMR_WDT_RST` | `1` | `Read/Write` | `0b1` | ` `
[code]
        0 = no operation
        1 = enable
      
    
[/code]
| Allow the watchdog timer to reset the system.   
`no operation` | `2` |  |  |  |   
`TMR_WDT_INTER_VALUE` | `3:6` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = 0.5
        0x01 = 1
        0x02 = 2
        0x03 = 3
        0x04 = 4
        0x05 = 5
        0x06 = 6
        0x07 = 8
        0x08 = 10
        0x09 = 12
        0x0a = 14
        0x0b = 16
        0x0c = no operation
        ...
      
    
[/code]
| The watchdog timer interval value in seconds, which depends on the 24MHz clock. Without it the watchdog cannot run.   
`no operation` | `7:31` |  |  |  |   
##### TMR_CNT64_CTRL
Default value: 0x00000000  
Offset: 0x00a0 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_CNT64_CLR` | `0` | `Read/Write` | `0x00` | ` `
[code]
         0 = clear success
         1 = clear
      
    
[/code]
| Clears the 64-bit counter, both Lo- and Hi- values. When clear has completed, TMR_CNT64_CLR reads 0.   
`TMR_CNT64_RL` | `1` | `Read/Write` | `0x00` | ` `
[code]
         0 = latched
         1 = latch
      
    
[/code]
| Latch the Lo- and Hi-counter registers together. TMR_CNT64_RL reads 0 on completion.   
`TMR_CNT64_CLK_SRC` | `2` | `Read/Write` | `0x00` | ` `
[code]
         0 = 24MHz clock
         1 = PLL6 divded by 6
      
    
[/code]
| Clock source for the 64-bit counter.   
`no operation` | `3:31` |  |  | padding  |   
  

##### TMR_CNT64_LO
Default value: 0x00000000  
Offset: 0x00a4 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_CNT64_LO` | `0:31` | `Read/Write` | `0x00` | `0 - 232-1` | The 32 LSB's ([0:31]) for the 64-bit counter.   
  

##### TMR_CNT64_HI
Default value: 0x00000000  
Offset: 0x00a8 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_CNT64_HI` | `0:31` | `Read/Write` | `0x00` | `0 - 232-1` | The 32 MSB's ([32:63]) for the 64-bit counter.   
  

##### TMR_32KHZ_OSC_CTRL
Default value: 0x00004000  
Offset: 0x0100 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_32KHZ_OSC_SRC` | `0` | `Read/Write` | `0x00` | ` `
[code]
         0 = internal 32kHz RC
         1 = external 32.768kHz crystal
      
    
[/code]
| Source for the 32kHz clock.   
`reserved` | `1` |  |  |  |   
`TMR_32KHZ_GSM` | `2:3` | `Read/Write` | `0x00` | ` `
[code]
         0x0 = low
         0x1 = undefined
         0x2 = undefined
         0x3 = high
      
    
[/code]
| External 32.768kHz crystal _GSM_.   
`reserved` | `4:6` |  |  |  |   
`TMR_32KHZ_RTC_DATE_XS` | `7` | `Read/Write` | `0x00` | ` `
[code]
         0 = write finished
         1 = writing
      
    
[/code]
| When TMR_RTC_DATE is being modified, this bit is set to 1. When all modifications on TMR_RTC_DATE are complete, this bit is set to 0. While TMR_RTC_DATE_XS, TMR_RTC_TIME_XS or TMR_ALARM_CNT_XS is set to 1 neither of TMR_RTC_DATE, TMR_RTC_TIME or TMR_ALARM_CNT should be written to.   
`TMR_32KHZ_RTC_TIME_XS` | `8` | `Read/Write` | `0x00` | ` `
[code]
         0 = write finished
         1 = writing
      
    
[/code]
| When TMR_RTC_TIME is being modified, this bit is set to 1. When all modifications on TMR_RTC_TIME are complete, this bit is set to 0. While TMR_RTC_DATE_XS, TMR_RTC_TIME_XS or TMR_ALARM_CNT_XS is set to 1 neither of TMR_RTC_DATE, TMR_RTC_TIME or TMR_ALARM_CNT should be written to.   
`TMR_32KHZ_ALARM_CNT_XS` | `9` | `Read/Write` | `0x00` | ` `
[code]
         0 = write finished
         1 = writing
      
    
[/code]
| When TMR_RTC_ALARM_CNT is being modified, this bit is set to 1. When all modifications on TMR_RTC_ALARM_CNT are complete, this bit is set to 0. While TMR_RTC_DATE_XS, TMR_RTC_TIME_XS or TMR_ALARM_CNT_XS is set to 1 neither of TMR_RTC_DATE, TMR_RTC_TIME or TMR_ALARM_CNT should be written to.  |   
`reserved` | `10:13` |  |  |  |   
`TMR_32KHZ_CLK_SWT_AUTO` | `14` | `Read/Write` | `0x01` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable/disable automatic switching.   
`TMR_32KHZ_CLK_SWT_PEN` | `15` | `Read/Write` | `0x00` | ` `
[code]
         0 = no operation
         1 = pending
      
    
[/code]
| Shows when a clock switch is pending.  |   
`reserved` | `16:31` |  |  |  | padding   
  

##### TMR_RTC_DATE
Default value: undefined  
Offset: 0x0104 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_RTC_DAY` | `0:4` | `Read/Write` | `undefined` | `01 - 31` | Day value of the RTC.   
`reserved` | `5:7` |  |  |  |   
`TMR_RTC_MONTH` | `8:11` | `Read/Write` | `undefined` | `01 - 12` | Month value of the RTC.   
`reserved` | `12:15` |  |  |  |   
`TMR_RTC_YEAR` | `16:21` | `Read/Write` | `undefined` | `00 - 63` | Year value of the RTC.   
`TMR_RTC_LEAP` | `22` | `Read/Write` | `0x00` | ` `
[code]
         0 = false
         1 = true
      
    
[/code]
| The current year is a leap year.  
This is not set by hardware. It needs to be set by software. Hardware will use this to calculate date/year values.   
`reserved` | `23:29` |  |  |  |   
`TMR_RTC_SIM` | `30` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enables/disables simulation of the RTC. _WARNING, it is unknown what 0 and 1 do nor what TMR_RTC_SIM does to begin with.**USE WITH CAUTION**_  
`TMR_RTC_TESTMODE` | `31` | `Read/Write` | `0x00` | `
[code] 
         0 = disable
         1 = enable
    
[/code]
` | Enables/disables RTC test mode. _WARNING, it is unknown what 0 and 1 do nor what TMR_RTC_TESTMODE does to begin with.**USE WITH CAUTION**_  
  

##### TMR_RTC_TIME
Default value: undefined  
Offset: 0x0108 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_RTC_SEC` | `0:5` | `Read/Write` | `undefined` | `00 - 59` | Seconds value of the RTC.   
`reserved` | `6:7` |  |  |  |   
`TMR_RTC_MIN` | `8:13` | `Read/Write` | `undefined` | `00 - 59` | Minutes value of the RTC.   
`reserved` | `14:15` |  |  |  |   
`TMR_RTC_HOUR` | `16:20` | `Read/Write` | `undefined` | `00 - 23` | Hours value of the RTC.   
`reserved` | `21:28` |  |  |  |   
`TMR_RTC_DAY` | `29:31` | `Read/Write` | `0x00` | ` `
[code]
         0x00 = Monday
         0x01 = Tuesday
         0x02 = Wednesday
         0x03 = Thursday
         0x04 = Friday
         0x05 = Satuday
         0x06 = Sunday
         0x07 = no operation
      
    
[/code]
| Day of the week value of the RTC.   
  

##### TMR_ALARM_CNT
Default value: undefined  
Offset: 0x010c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_ALARM_SEC` | `0:5` | `Read/Write` | `undefined` | `00 - 59` | Seconds value of the alarm counter.  
If set to 00, then it will be forced to 01.   
`reserved` | `6:7` |  |  |  |   
`TMR_ALARM_MIN` | `8:13` | `Read/Write` | `undefined` | `00 - 59` | Minutes value of the alarm counter.   
`reserved` | `14:15` |  |  |  |   
`TMR_ALARM_HOUR` | `16:20` | `Read/Write` | `undefined` | `00 - 23` | Hours value of the alarm counter.   
`reserved` | `21:23` |  |  |  |   
`TMR_ALARM_DAY` | `24:31` | `Read/Write` | `0x00` | `00 - 255` | Days value of the alarm counter.   
  

##### TMR_ALARM_WK
Default value: undefined  
Offset: 0x0110 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_ALARM_WK_SEC` | `0:5` | `Read/Write` | `undefined` | `00 - 59` | Seconds value of the alarm counter.   
`reserved` | `6:7` |  |  |  |   
`TMR_ALARM_WK_MIN` | `8:13` | `Read/Write` | `undefined` | `00 - 59` | Minutes value of the alarm counter.   
`reserved` | `14:15` |  |  |  |   
`TMR_ALARM_WK_HOUR` | `16:20` | `Read/Write` | `undefined` | `00 - 23` | Hours value of the alarm counter.   
`reserved` | `21:31` |  |  |  | padding   
  

##### TMR_ALARM_EN
Default value: undefined  
Offset: 0x0114 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_ALARM_WK0` | `0` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable the daily alarm to be only triggered based on TMR_ALARM_WK0 for day 0 (monday, see TMR_RTC_DAY). Also allows the TMR_ALARM_IRQ_STATUS to be set to 1 to indicate a pending alarm.   
`TMR_ALARM_WK1` | `1` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable the daily alarm to be only triggered based on TMR_ALARM_WK1 for day 1 (tuesday, see TMR_RTC_DAY). Also allows the TMR_ALARM_IRQ_STATUS to be set to 1 to indicate a pending alarm.   
`TMR_ALARM_WK2` | `2` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable the daily alarm to be only triggered based on TMR_ALARM_WK2 for day 2 (wednesday, see TMR_RTC_DAY). Also allows the TMR_ALARM_IRQ_STATUS to be set to 1 to indicate a pending alarm.   
`TMR_ALARM_WK3` | `3` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable the daily alarm to be only triggered based on TMR_ALARM_WK3 for day 3 (thursday, see TMR_RTC_DAY). Also allows the TMR_ALARM_IRQ_STATUS to be set to 1 to indicate a pending alarm.   
`TMR_ALARM_WK4` | `4` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable the daily alarm to be only triggered based on TMR_ALARM_WK4 for day 4 (friday, see TMR_RTC_DAY). Also allows the TMR_ALARM_IRQ_STATUS to be set to 1 to indicate a pending alarm.   
`TMR_ALARM_WK5` | `5` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable the daily alarm to be only triggered based on TMR_ALARM_WK5 for day 5 (saturday, see TMR_RTC_DAY). Also allows the TMR_ALARM_IRQ_STATUS to be set to 1 to indicate a pending alarm.   
`TMR_ALARM_WK0` | `6` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable the daily alarm to be only triggered based on TMR_ALARM_WK6 for day 6 (sunday, see TMR_RTC_DAY). Also allows the TMR_ALARM_IRQ_STATUS to be set to 1 to indicate a pending alarm.   
`reserved` | `7` |  |  |  |   
`TMR_ALARM_CNT_RUN` | `8` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| TMR_ALARM_CNT_RUN enables/disables the TMR_ALARM_CNT countdown. Also allows for the TMR_ALARM_IRQ_STATUS to be set.   
`reserved` | `9:31` |  |  |  | padding   
  

##### TMR_ALARM_IRQ
Default value: undefined  
Offset: 0x0118 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_ALARM_IRQ_WK` | `0` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable/disable the overal alarm interrupt.   
`TMR_ALARM_IRQ_CNT` | `1` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Enable/disable the overal alarm countdown interrupt.   
`reserved` | `2:31` |  |  |  | padding   
  

##### TMR_ALARM_IRQ_STATUS
Default value: undefined  
Offset: 0x011c 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_ALARM_IRQ_WK_PEND` | `0` | `Read/Write` | `0x00` | ` `
[code]
         0 = no operation
         1 = enable
      
    
[/code]
| Weekly alarm interrupt pending.  
Alarm has been reached and if TMR_ALARM_IRQ_WK is 1, the interrupt controller will trigger an interrupt.   
`TMR_ALARM_IRQ_CNT_PEND` | `1` | `Read/Write` | `0x00` | ` `
[code]
         0 = disable
         1 = enable
      
    
[/code]
| Alarm countdown interrupt pending.  
Alarmcountdown has reached 0. If TMR_ALARM_IRQ_CNT is 1, the interrupt controller will trigger an interrupt.   
`reserved` | `2:31` |  |  |  | padding   
  

##### TMR_GP0
Default value: 0x00000000  
Offset: 0x0120 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_GP0` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | General purpose data can be stored in this register. RTCVDD needs to be larger then 1.0 volt however.   
##### TMR_GP1
Default value: 0x00000000  
Offset: 0x0124 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_GP1` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | General purpose data can be stored in this register. RTCVDD needs to be larger then 1.0 volt however.   
##### TMR_GP2
Default value: 0x00000000  
Offset: 0x0128 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`TMR_GP2` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | General purpose data can be stored in this register. RTCVDD needs to be larger then 1.0 volt however.   
##### TMR_GP3
Default value: 0x00000000  
Offset: 0x012c 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`TMR_GP3` | `0:31` | `Read/Write` | `0x00000000` | `0 - 232-1` | General purpose data can be stored in this register. RTCVDD needs to be larger then 1.0 volt however.   
##### CPU_CFG
Default value: 0x00000080  
Offset: 0x013c 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`CPU_CFG_L2_CACHE_INV` | `0` | `Read/Write` | `0b0` | ` `
[code]
         0 = enable
         1 = disable
      
    
[/code]
| Enable L2 data cache invalidation on reset.  
L2 data cache invalidation can take up to 1024 CPU clock cycles. This bit can be set from software.   
`CPU_CFG_L1_CACHE_INV` | `1` | `Read/Write` | `0b0` | ` `
[code]
         0 = enable
         1 = disable
      
    
[/code]
| Enable L1 data cache invalidation on reset.  
L1 data cache invalidation can take up to 512 CPU clock cycles. This bit can be set from software.   
`reserved` | `2:5` |  |  |  |   
`CPU_CFG_CHIP_VER` | `6:7` | `Read` | `0b01` | ` `
[code]
         0x00 = A
         0x01 = C
         0x02 = C
         0x03 = B
      
    
[/code]
| Chip revision ID.   
`reserved` | `8:31` |  |  |  |   
## Initial values
Note, that the clocks/timers are running when this was obtained, so values are constantly changing and should be taken into account. 
### default map
md 0x01c20c00 0x54 
[code] 
    01c20c00: 00000000 00000000 00000000 00000000    ................
    01c20c10: 00000005 ffffffff d27fc842 00000000    ........B.......
    01c20c20: 00000004 00000000 00000000 00000000    ................
    01c20c30: 00000004 00000000 00000000 00000000    ................
    01c20c40: 00000000 00000000 00000000 00000000    ................
    01c20c50: 00000004 00000000 00000000 00000000    ................
    01c20c60: 00000004 00000000 00000000 00000000    ................
    01c20c70: 00000000 00000000 00000000 00000000    ................
    01c20c80: 00000000 00000000 00000000 05db05db    ................
    01c20c90: 00000000 00000000 00000000 00000000    ................
    01c20ca0: 00000000 00000000 00000000 00000000    ................
    01c20cb0: 00000000 00000000 00000000 00000000    ................
    01c20cc0: 00000000 00000000 00000000 00000000    ................
    01c20cd0: 00000000 00000000 00000000 00000000    ................
    01c20ce0: 00000000 00000000 00000000 00000000    ................
    01c20cf0: 00000000 00000000 00000000 00000000    ................
    01c20d00: 00006000 00000101 00000020 00000000    .`...... .......
    01c20d10: 00000000 00000000 00000000 00000000    ................
    01c20d20: 00000000 00000000 00000000 00000000    ................
    01c20d30: 00000000 00000000 00000000 00000080    ................
    01c20d40: 00006000 00000101 00000020 00000000    .`...... .......
    
[/code]
### all set to 1
mw 0x01c20c00 0xffffffff 0x54  
md 0x01c20c00 0x54 
[code] 
    01c20c00: 0000013f 00000000 00000000 00000000    ?...............
    01c20c10: 000000ff ffffffff ffffffff 00000000    ................
    01c20c20: 000000ff ffffffff ffffffff 00000000    ................
    01c20c30: 000000fd ffffffff fff97c33 00000000    ........3|......
    01c20c40: 0000001d ffffffff 00000000 00000000    ................
    01c20c50: 000000ff ffffffff ffffffff 00000000    ................
    01c20c60: 000000ff ffffffff ffffffff 00000000    ................
    01c20c70: 00000000 00000000 00000000 00000000    ................
    01c20c80: 00000303 ffffffff ffffffff ffffffff    ................
    01c20c90: 00000000 000000ff 00000000 00000000    ................
    01c20ca0: 00000007 00000000 00000000 00000000    ................
    01c20cb0: 00000000 00000000 00000000 00000000    ................
    01c20cc0: 00000000 00000000 00000000 00000000    ................
    01c20cd0: 00000000 00000000 00000000 00000000    ................
    01c20ce0: 00000000 00000000 00000000 00000000    ................
    01c20cf0: 00000000 00000000 00000000 00000000    ................
    01c20d00: 0000407e c0550515 601b1b1b ff1f3f3f    [[email protected]][1003]....`??..
    01c20d10: 001f3f3f 0000017f 00000003 00000001    ??..............
    01c20d20: ffffffff ffffffff ffffffff ffffffff    ................
    01c20d30: 00000000 00000000 00000000 000000bf    ................
    01c20d40: 0000407e c0550515 601b1b1b ff1f3f3f    [[email protected]][1003]....`??..
    
    
[/code]
### all set to 0
mw 0x01c20c00 0x00 0x54   
md 0x01c20c00 0x54 
[code] 
    01c20c00: 00000000 00000101 00000000 00000000    ................
    01c20c10: 00000000 00000000 00000000 00000000    ................
    01c20c20: 00000000 00000000 00000000 00000000    ................
    01c20c30: 00000000 00000000 00000000 00000000    ................
    01c20c40: 00000000 00000000 00000000 00000000    ................
    01c20c50: 00000000 00000000 00000000 00000000    ................
    01c20c60: 00000000 00000000 00000000 00000000    ................
    01c20c70: 00000000 00000000 00000000 00000000    ................
    01c20c80: 00000000 00000000 00000000 00000000    ................
    01c20c90: 00000000 00000000 00000000 00000000    ................
    01c20ca0: 00000000 00000000 00000000 00000000    ................
    01c20cb0: 00000000 00000000 00000000 00000000    ................
    01c20cc0: 00000000 00000000 00000000 00000000    ................
    01c20cd0: 00000000 00000000 00000000 00000000    ................
    01c20ce0: 00000000 00000000 00000000 00000000    ................
    01c20cf0: 00000000 00000000 00000000 00000000    ................
    01c20d00: 00002000 00000000 00000000 00000000    . ..............
    01c20d10: 00000000 00000000 00000000 00000000    ................
    01c20d20: 00000000 00000000 00000000 00000000    ................
    01c20d30: 00000000 00000000 00000000 00000080    ................
    01c20d40: 00002000 00000000 00000000 00000000    . ..............
    
[/code]
