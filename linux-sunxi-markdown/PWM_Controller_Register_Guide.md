# PWM Controller Register Guide
## Contents
  * [1 PWM][43938]
    * [1.1 Observed behaviour on GR8 from NextThing][43939]
    * [1.2 Info][43940]
      * [1.2.1 PWM Registers][43941]
        * [1.2.1.1 PWM_CTRL][43942]
        * [1.2.1.2 PWM_CH0_PERIOD][43943]
        * [1.2.1.3 PWM_CH1_PERIOD][43944]
    * [1.3 Initial values][43945]
      * [1.3.1 default map][43946]
      * [1.3.2 all to 1][43947]
      * [1.3.3 all to 0][43948]

# PWM
There are two 16-bit up counters in the A10 SoC. Counters will reset when PWM_CH0_PERIOD/PWM_CH1_PERIOD has been reached. On initialization PWM_OUT is active high and starts counting from 0x0000. 
The PWM divisor devides the 24MHz clock by 1-4096 depending on the PWM_CTRL register. 
There are two output modes, cycle mode and pulse mode which are either, a square waveform or a postive/negative pulse, based on the frequency in the PWM_CH0_PERIOD/PWM_CH1_PERIOD register. 
## Observed behaviour on GR8 from NextThing
In this section, clock cycles refers to the 24 MHz divided by the current prescaler. With the default prescaler of 120, a clock cycle is 5 microseconds. 
GR8 has two PWM channels. 
In pulse mode, sending a pulse (time between starting and when the bit has been cleared) takes the time it should take + 1-2 clock cycles. 
Writing the period register (between starting and the ready bit has been cleared) takes 3-4 clock cycles. If the register is written while the clock gating is off, the ready bit will stay busy until the clock gating is turned on (and 3-4 clock cycles have passed). 
Time needed between disabling PWM and disabling the clock gate to make sure the PWM is actually turned off: 1-2 clock cycles. Otherwise the output signal may be stuck in the active state if it was turned off when the signal was active. 
A pulse (regardless of single pulse or cycle mode) always starts with the inactive part, followed by the active part, contrary to what the user manual says. 
The polarity register can always be written to, even when the clock gate is off, and will be applied immediately. 
In cycle mode, writing 0 to EN and then 1 to EN resets the pulse, i.e. it will immediately perform the inactive part and then the active part and repeat. Same applies if 1 is written to MODE followed by 0. Note that at least 1 clock cycle should be slept between the two writes. By only temporarily disabling the clock gating, that rather just pauses the PWM. 
In cycle mode, after a new value has been written to the period register, a pulse with the old parameters must first complete, regardless if the PWM is disabled and then enabled, prescaler is changed, or clock gate is toggled. The new values are applied as soon as the active part of a complete pulse ends. If the PWM is enabled when the period register is written, it may take up to one full pulse length before the new settings are applied. If the PWM was disabled when the period register got a new value, a full pulse with the old parameters will first take place after enabling, before the new parameters are applied. If the PWM is disabled while the pulse with the old parameters is in progress, then after enabling the PWM again a full pulse with the old parameters will still need to take place. Also note that if the prescaler is also changed in conjunction with the new period/duty values, for this complete pulse the old period/duty will be used with the new prescaler, which might lead to a very long period. The only way to clear the previous internal values without the need to wait one pulse with the previous settings seems to temporarily switch to pulse mode. After the period register has been written, sending a single pulse will use the new values immediately. After the single pulse has been sent and switching back to cycle mode, the new values are used (and not the old ones). So a simple workaround when changing the period register is to first write 0x00000000 to the period register (entire period is then one 1 clock cycle and active part is 0 clock cycles), switch to pulse mode and send a single pulse, write the desired value to the period register and then switch to cycle mode. 
Note that with the prescaler of 72k, one clock cycle is 3 ms, which depending on use case, might be a long time. If one wants to perform an operation quicker than the timings according to the clock cycle timings mentioned above, one could temporarily change the prescaler to the smallest available. If the prescaler of 1 is available (like it is on GR8), one clock cycle is around 42 nanoseconds. 
## Info
PWM Base address: 0x01c20e00 
#### PWM Registers
Register Name  | Offset  | Size  | Description  | Note   
---|---|---|---|---  
`PWM_CTRL` | `0x0000` | `4B` | PWM Control register  |   
`PWM_CH0_PERIOD` | `0x0004` | `4B` | PWM Channel 0 period register  |   
`PWM_CH1_PERIOD` | `0x0008` | `4B` | PWM Channel 1 period register  | Not available on sun5i   
##### PWM_CTRL
Default value: 0x00000000  
Offset: 0x00 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`PWM_CH0_PRESCALAR` | `0:3` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = div(120)
        0x01 = div(180)
        0x02 = div(240)
        0x03 = div(360)
        0x04 = div(480)
        0x05 = no operation
        ...
        0x08 = div(12000)
        0x09 = div(24000)
        0x0a = div(36000)
        0x0b = div(48000)
        0x0c = div(72000)
        0x0d = no operation
        ...
      
    
[/code]
| Setup the Channel 0 PWM prescalar  
Set these bits before enabling the clock-gate to this channel!   
`PWM_CH0_EN` | `4` | `Read/Write` | `0b0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| Enable or disable the Channel 0 PWM   
`PWM_CH0_ACT_STA` | `5` | `Read/Write` | `0b0` | ` `
[code]
        0 = low level
        1 = high level
      
    
[/code]
| Setup Channel 0 PWM Active State   
`PWM_CH0_CLK_GATING` | `6` | `Read/Write` | `0b0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Special clock gating for Channel 0 PWM   
`PWM_CH0_MODE` | `7` | `Read/Write` | `0b0` | ` `
[code]
        0 = cycle mode
        1 = pulse mode
      
    
[/code]
| Setup Channel 0 PWM Mode   
`PWM_CH0_PUL_START` | `8` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = output 1 pulse
      
    
[/code]
| Output one pulse according to PWM_CH0_PERIOD and PWM_CH0_ACT_STATE.  
The bit is cleared after the pulse.   
`no operation` | `9:14` |  |   
`PWM_CH1_PRESCALAR` | `15:18` | `Read/Write` | `0x00` | ` `
[code]
        0x00 = div(120)
        0x01 = div(180)
        0x02 = div(240)
        0x03 = div(360)
        0x04 = div(480)
        0x05 = no operation
        ...
        0x08 = div(12000)
        0x09 = div(24000)
        0x0a = div(36000)
        0x0b = div(48000)
        0x0c = div(72000)
        0x0d = no operation
        ...
      
    
[/code]
| Setup the PWM Channel 1 prescalar  
Set these bits before enabling the clock-gate to this channel!   
`PWM_CH1_EN` | `19` | `Read/Write` | `0b0` | ` `
[code]
        0 = disable
        1 = enable
      
    
[/code]
| Enable or disable the Channel 1 PWM   
`PWM_CH1_ACT_STATE` | `20` | `Read/Write` | `0b0` | ` `
[code]
        0 = low level
        1 = high level
      
    
[/code]
| Setup Channel 1 PWM Active State   
`PWM_CH1_CLK_GATING` | `21` | `Read/Write` | `0b0` | ` `
[code]
        0 = mask
        1 = pass
      
    
[/code]
| Special clock gating for Channel 1 PWM   
`PWM_CH1_MODE` | `22` | `Read/Write` | `0b0` | ` `
[code]
        0 = cycle mode
        1 = pulse mode
      
    
[/code]
| Setup Channel 1 PWM Mode   
`PWM_CH1_PUL_START` | `23` | `Read/Write` | `0b0` | ` `
[code]
        0 = no operation
        1 = output 1 pulse
      
    
[/code]
| Output one pulse according to PWM_CH1_PERIOD and PWM_CH1_ACT_STATE.  
The bit is cleared after the pulse.   
`no operation` | `24:31` |  |  |  |   
##### PWM_CH0_PERIOD
Default value: 0x00000000  
Offset: 0x04 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`PWM_CH0_ACT_CYC` | `0:15` | `Read/Write` | `0x00` | ` `
[code]
        0 = 0 cycles
        1 = 1 cycle
        ...
        n = n cycles
      
    
[/code]
| Number of active cycles in the channel 0 PWM clock   
`PWM_CH0_ENTIRE_CYC` | `16:31` | `Read/Write` | `0x00` | ` `
[code]
        0 = 1 cycle
        1 = 2 cycles
        ...
        n = n + 1 cycles
      
    
[/code]
| Numer of entire cycles in the channel 0 PWM clock  
If dynamic updates are required, the PCLK needs to be faster then the PWM_CLK (PWM_CLK = 24MHz/PWM_CH0_PRESCALAR)   
##### PWM_CH1_PERIOD
Default value: 0x00000000  
Offset: 0x08 
Name  | Bit  | Read/Write  | Default  | Values  | Description   
---|---|---|---|---|---  
`PWM_CH1_ACT_CYC` | `0:15` | `Read/Write` | `0x00` | ` `
[code]
        0 = 0 cycles
        1 = 1 cycle
        ...
        n = n cycles
      
    
[/code]
| Number of active cycles in the channel 1 PWM clock   
`PWM_CH1_ENTIRE_CYC` | `16:31` | `Read/Write` | `0x00` | ` `
[code]
        0 = 1 cycle
        1 = 2 cycles
        ...
        n = n + 1 cycles
      
    
[/code]
| Numer of entire cycles in the channel 1 PWM clock  
If dynamic updates are required, the PCLK needs to be faster then the PWM_CLK (PWM_CLK = 24MHz/PWM_CH1_PRESCALAR)   
## Initial values
### default map
md 0x01c20e00 3 
[code] 
    01c20e00: 00000000 00000000 00000000    ...........
    
[/code]
### all to 1
mw 0x01c20e00 0xffffffff 3  
md 0x01c20e00 3 
[code] 
    01c20e00: 007f80ff 00ff00ff 00ff00ff    ............
    
[/code]
### all to 0
mw 0x01c20e00 0x00 3  
md 0x01c20c00 3 
[code] 
    01c20c00: 00000000 00000000 00000000    ............
    
[/code]
