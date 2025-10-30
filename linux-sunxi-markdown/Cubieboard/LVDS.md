# Cubieboard/LVDS
< [Cubieboard][14272]
 
## Contents
  * [1 Introduction][14275]
    * [1.1 Powersupply][14276]
    * [1.2 Hardware Connections][14277]
    * [1.3 Software Configuration][14278]
      * [1.3.1 LCD Data Clock Frequency][14279]
      * [1.3.2 LCD Interface][14280]
      * [1.3.3 LCD Sync Settings][14281]

# Introduction
To use a LVDS TFT-LCD display with Cubieboard is very simple job. 
There are two main activities do to: 
  1. Connect the LVDS to Cubieboard.
  2. Configure script.bin for LVDS display.

For this example I will use a CHI-MEI G070Y2-L01 800x480 LED backlight TFT-LCD. For other displays there would be different power-supply requirements, LCD I/O pin layouts and script.fex values. 
## Powersupply
The LCD is a device which require a lot of power to work so we need two extra-power supplies: 
  1. One at 3.3V to supply LCD main board.
  2. One at 12V to supply LCD backlight system.

**NB:** Often you can't use 3.3V from Cubieboard because the display will typically have a Rush Current of > 1A at startup and Cubieboard can't supply that much power. 
Verify all these values with the datasheet of your display. There are displays which only use 5V for the LED power supply (e.g. AUO B089AW01 V1). Using 12V on these displays will destroy them (and potentially the board you connect them to). 
## Hardware Connections
**Generally** the following can be said of the hardware connection. 
  1. The pins VDD, VCC or similar must be connected to 3.3V external supply
  2. The pins VDD_LED, VDD_BL or similar must be connected to 5V/12V external backlight supply
  3. If there is a backlight PWM pin on the display connect it to PWM channel 0 on the board
  4. The pins GND must be connected to _both_ cubieboard and external supply GND

  1. Each LVDS lane RX0+/- to RX3+/- and the clock lane RXC+/- must be connected to corrosponding pins on cubieboard

Note for users of other boards: Mapping of LCD-Dx pin names to LVDS pin names is 
[code] 
    RX0+ = LCD0-D0
    RX0- = LCD0-D1
    RX1+ = LCD0-D3
    RX1- = LCD0-D4
    RX2+ = LCD0-D5
    RX2- = LCD0-D6
    RXC+ = LCD0-D7
    RXC- = LCD0-D8
    
[/code]
CubieBoard U14 | G070Y2-L01 LVDS I/O PIN | Notes   
---|---|---  
12 PD8 (LCDD8/LVDS0P3) | 01 (RX3+) |   
11 PD9 (LCDD9/LVDS0N3) | 02 (RX3-) |   
-N/A- | 03 (NC) | Leave unconnected.   
-N/A- | 04 (FRC) | Must be connected to extra 3.3V power supply VCC.   
02 Ground | 05 (GND) | Must be connected also with extra 3.3V power supply Ground.   
07 PD6 (LCDD6/LVDS0PC) | 06 (RXC+) |   
10 PD7 (LCDD7/LVDS0NC) | 07 (RXC-) |   
02 Ground | 08 (GND) | Must be connected also with extra 3.3V power supply Ground.   
05 PD4 (LCDD4/LNVS0P2) | 09 (RX2+) |   
08 PD5 (LCDD5/LVDS0N2) | 10 (RX2-) |   
02 Ground | 11 (GND) | Must be connected also with extra 3.3V power supply Ground.   
03 PD2 (LCDD2/LVDS0P1) | 12 (RX1+) |   
06 PD3 (LCDD3/LVDS0N1) | 13 (RX1-) |   
02 Ground | 14 (GND) | Must be connected also with extra 3.3V power supply Ground.   
01 PD0 (LCDD0/LVDSP0) | 15 (RX0) |   
04 PD1 (LCDD1/LVDS0N0) | 16 (RX0) |   
-N/A- | 17 (LR) | Leave unconnected. Together with UD describe only display scanning direction.   
-N/A- | 18 (UD) | Leave unconnected. Together with LR describe only display scanning direction.   
-N/A- | 19 (VCC_IN) | Must be connected to extra 3.3V power supply VCC.   
-N/A- | 29 (VCC_IN) | Must be connected to extra 3.3V power supply VCC.   
## Software Configuration
At this point is important to understand HOW TO set properly the A10 chip to run with the specific display settings. More simple job is recover and set display X/Y resolutions. With example's devices we should use: 
[code] 
     [lcd0_para]
     lcd_x = 800
     lcd_y = 480
    
[/code]
Now we will enter in the more complex range of settings regarding timings.  
At this point only display datasheet can help us with the TIMING CHARACTERISTICS: 
Vertical Display | Parameter | Symbol | Min. | Typ. | Max | Unit | Note   
---|---|---|---|---|---|---|---  
| Period | Tv | 490 | 500 | 550 | Th | Tv = Tvd + Tvb   
| Active | Tvd | - | 480 | - | Th |   
| Blanking | Tvb | 10 | 20 | 70 | Th |   
|  |  |  |  |  |  |   
Horizzontal Display | Parameter | Symbol | Min. | Typ. | Max | Unit | Note   
| Period | Th | 930 | 992 | 1090 | Tclock | Th = Thd + Thb   
| Active | Thd | - | 800 | - | Tclock |   
| Blanking | Thb | 130 | 192 | 290 | Tclock |   
|  |  |  |  |  |  |   
Clock Frequency |  | Symbol | Min. | Typ. | Max | Unit | Note   
|  | 1/Tclock | 27 | 29.5 | 33 | MHz |   
#### LCD Data Clock Frequency
Looking in the table, at field _Clock Frequency_ , a good value for _lcd_dclk_freq_ should be comprised between 29.5 to 33 MHz.  
The value of 30MHz should go fine so: 
[code] 
     ; lcd data clock frequency
     lcd_dclk_freq = 30
    
[/code]
#### LCD Interface
LCD interface define what type of interface to use for LCD. For LVDS the right value is 3: 
[code] 
     ; lcd interface
     lcd_if = 3
    
[/code]
Check whether 24 or 18 bit color is used, and set 
[code] 
     lcd_lvds_bitwidth = 1 (if 18bit (RGB666) is used)
    
[/code]
#### LCD Sync Settings
Now more interesting part of settings, the sync timings. A10 require four values: 
  1. LCD horizontal sync back porch
  2. LCD horizontal sync total cycle
  3. LCD vertical sync back porch
  4. LCD vertical sync total cycle * 2

In the upon table we can the needed values. 
  1. Horizontal sync total sycle (lcd_ht) is the same as _horizontal period_ in the datasheet which is = 1055 at 30Mhz
  2. Horizontal back porch (lcd_hpb) is the same as _horizontal blanking_ in the datasheet, which is the difference between _horizontal period_ and the _horizontal active_ time (1055-800) which is = 255, here 200 is used an approximate value
  3. Vertical sync total cycle (lcd_vt) is the same as 2*_vertical period_ in the datasheet which is = 1050 at 30Mhz
  4. Horizontal back porch (lcd_hpb) is the same as 2*_vertical blanking_ in the datasheet, which is the difference between 2*_vertical period_ and the 2*_vertical active_ time (1050-1000) which is = 50, 25 is used as an approximate value.

So the final values are: 
[code] 
     lcd_hbp = 200
     lcd_ht = 1055
     lcd_vbp = 25
     lcd_vt = 1050
    
[/code]
So the final config of the script.fex file: 
[code] 
     [disp_init]
     disp_init_enable = 1
     disp_mode = 0
     screen0_output_type = 1
     screen0_output_mode = 4
     screen1_output_type = 1
     screen1_output_mode = 4
     fb0_framebuffer_num = 2
     fb0_format = 10
     fb0_pixel_sequence = 0
     fb0_scaler_mode_enable = 1
     fb1_framebuffer_num = 2
     fb1_format = 10
     fb1_pixel_sequence = 0
     fb1_scaler_mode_enable = 1
     lcd0_bright = 197
     lcd1_bright = 197
     lcd0_screen_bright = 50
     lcd0_screen_contrast = 50
     lcd0_screen_saturation = 57
     lcd0_screen_hue = 50
     lcd1_screen_bright = 50
     lcd1_screen_contrast = 50
     lcd1_screen_saturation = 57
     lcd1_screen_hue = 50
     
     [lcd0_para]
     lcd_used = 1
     lcd_x = 800
     lcd_y = 480
     lcd_dclk_freq = 30
     lcd_pwm_not_used = 0
     lcd_pwm_ch = 0
     lcd_pwm_freq = 10000
     lcd_pwm_pol = 0
     lcd_if = 3
     lcd_hbp = 200
     lcd_ht = 1055
     lcd_vbp = 25
     lcd_vt = 1050
     lcd_hv_if = 0
     lcd_hv_smode = 0
     lcd_hv_s888_if = 0
     lcd_hv_syuv_if = 0
     lcd_hv_vspw = 0
     lcd_hv_hspw = 0
     lcd_lvds_ch = 0
     lcd_lvds_mode = 0
     lcd_lvds_bitwidth = 0
     lcd_lvds_io_cross = 0
     lcd_cpu_if = 0
     lcd_frm = 0
     lcd_io_cfg0 = 268435456
     lcd_gamma_correction_en = 0
     lcd_gamma_tbl_0 = 0x0
     lcd_gamma_tbl_1 = 0x10101
     lcd_gamma_tbl_255 = 0xffffff
     lcd_bl_en_used = 0
     lcd_bl_en = port:PH07<1><0><default><1>
     lcd_power_used = 1
     lcd_power = port:PH08<1><0><default><1>
     lcd_pwm_used = 1
     lcd_pwm = port:PB02<2><0><default><default>
     lcd_gpio_0 =
     lcd_gpio_1 =
     lcd_gpio_2 =
     lcd_gpio_3 =
     lcdd0 = port:PD00<2><0><default><default>
     lcdd1 = port:PD01<2><0><default><default>
     lcdd2 = port:PD02<2><0><default><default>
     lcdd3 = port:PD03<2><0><default><default>
     lcdd4 = port:PD04<2><0><default><default>
     lcdd5 = port:PD05<2><0><default><default>
     lcdd6 = port:PD06<2><0><default><default>
     lcdd7 = port:PD07<2><0><default><default>
     lcdd8 = port:PD08<2><0><default><default>
     lcdd9 = port:PD09<2><0><default><default>
     lcdd10 = port:PD10<2><0><default><default>
     lcdd11 = port:PD11<2><0><default><default>
     lcdd12 = port:PD12<2><0><default><default>
     lcdd13 = port:PD13<2><0><default><default>
     lcdd14 = port:PD14<2><0><default><default>
     lcdd15 = port:PD15<2><0><default><default>
     lcdd16 = port:PD16<2><0><default><default>
     lcdd17 = port:PD17<2><0><default><default>
     lcdd18 = port:PD18<2><0><default><default>
     lcdd19 = port:PD19<2><0><default><default>
     lcdd20 = port:PD20<2><0><default><default>
     lcdd21 = port:PD21<2><0><default><default>
     lcdd22 = port:PD22<2><0><default><default>
     lcdd23 = port:PD23<2><0><default><default>
     lcdclk = port:PH24<2><0><default><default>
     lcdde = port:PH25<2><0><default><default>
     lcdhsync = port:PH26<2><0><default><default>
     lcdvsync = port:PH27<2><0><default><default>
    
[/code]
