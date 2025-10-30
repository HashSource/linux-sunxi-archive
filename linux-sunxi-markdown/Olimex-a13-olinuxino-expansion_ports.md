# Olimex-a13-olinuxino-expansion ports
This is the pin-outs for the expansion ports of the [A13-OLinuXino][40193]. 
If you want to match up the below tables with the actual pin numbers of the connectors, then just turn the device over. All pin numbers are printed on the back. 
## Contents
  * [1 LCD_CON][40194]
  * [2 UEXT][40195]
  * [3 UART][40196]
  * [4 GPIO-1][40197]
  * [5 GPIO-2][40198]

# LCD_CON
LCD_CON   
---  
`1` | +5V  | `2` | _Ground_  
`3` | +3.3V  | `4` | _Ground_  
`5` | [PD18][40199] (LCD_D18)  | `6` | _nc_  
`7` | [PD18][40199] (LCD_D18)  | `8` | [PD19][40199] (LCD_D19)   
`9` | [PD20][40199] (LCD_D20)  | `10` | [PD21][40199] (LCD_D21)   
`11` | [PD22][40199] (LCD_D22)  | `12` | [PD23][40199] (LCD_D23)   
`13` | [PD10][40199] (LCD_D10)  | `14` | _nc_  
`15` | [PD10][40199] (LCD_D10)  | `16` | [PD11][40199] (LCD_D11)   
`17` | [PD12][40199] (LCD_D12)  | `18` | [PD13][40199] (LCD_D13)   
`19` | [PD14][40199] (LCD_D14)  | `20` | [PD15][40199] (LCD_D15)   
`21` | [PD2][40199] (LCD_D2)  | `22` | _nc_  
`23` | [PD2][40199] (LCD_D2)  | `24` | [PD3][40199] (LCD_D3)   
`25` | [PD4][40199] (LCD_D4)  | `26` | [PD5][40199] (LCD_D5)   
`27` | [PD6][40199] (LCD_D6)  | `28` | [PD7][40199] (LCD_D7)   
`29` | [PD26][40199] (LCD_HSYNC)  | `30` | [PD27][40199] (LCD_VSYNC)   
`31` | [PD24][40199] (LCD_CLK)  | `32` | [PD25][40199] (LCD_DE)   
`33` | [PB3][40200] | `34` | [PB4][40200]  
`35` | [PB10][40200] | `36` | [PB2][40200] (PWM0)   
`37` | TPX1  | `38` | TPX2   
`39` | TPY1  | `40` | TPY2   
# UEXT
UEXT   
---  
`1` | +3.3V  | `2` | _Ground_  
`3` | [PG3][40201] (UART1_TX)  | `4` | [PG4][40201] (UART1_RX)   
`5` | [PB17][40200] (TWI2_SCK)  | `6` | [PB18][40200] (TWI2_SDA)   
`7` | [PE3][40202] (SPI2_MISO)  | `8` | [PE2][40202] (SPI2_MOSI)   
`9` | [PE1][40202] (SPI2_CLK)  | `10` | [PE0][40202] (SPI2_CS0)   
# UART
UART   
---  
`4` | _Ground_  
`3` | [PF2][40203] (**SDC0_SCK** /UART0-TX)   
`2` | [PF4][40203] (**SDC0_D3** /UART0-RX)   
`1` | +3.3V   
# GPIO-1
GPIO-1   
---  
`1` | +5V  | `2` | _Ground_  
`3` | +3.3V  | `4` | _Ground_  
`5` | RESET_N  | `6` | NMI_N   
`7` | [PMU/GPIO-0][40204] | `8` | [PMU/GPIO-3][40204]  
`9` | [PMU/GPIO-1][40204] | `10` | [PMU/GPIO-2][40204]  
# GPIO-2
GPIO-2   
---  
`1` | +5V  | `2` | _Ground_  
`3` | +3.3V  | `4` | _Ground_  
`5` | [PB0][40200] (TWI0-SCK)  | `6` | [PG11][40201] (USBH_EN)   
`7` | [PB1][40200] (TWI0-SDA)  | `8` | [PG10][40201] (VGA_DIS)   
`9` | [PB2][40200] (PWM0)  | `10` | [PG9][40201] (LED1)   
`11` | [PB3][40200] | `12` | [PE11][40202]  
`13` | [PB4][40200] | `14` | [PE10][40202]  
`15` | [PB10][40200] | `16` | [PE9][40202]  
`17` | [PB15][40200] (TWI1-SCK)  | `18` | [PE8][40202]  
`19` | [PB16][40200] (TWI1-SDA)  | `20` | [PE7][40202]  
`21` | [PC0][40205] (NWE/SPI0_MOSI)  | `22` | [PE6][40202]  
`23` | [PC1][40205] (NALE/SPI0_MISO)  | `24` | [PE5][40202]  
`25` | [PC2][40205] (NCLE/SPI0_CLK)  | `26` | [PE4][40202]  
`27` | [PC3][40205] (NCE1/SPI0_CS0)  | `28` | [PC19][40205] (NDQS)   
`29` | [PC4][40205] (NCE0)  | `30` | [PC15][40205] (NDQ7)   
`31` | [PC5][40205] (NRE)  | `32` | [PC14][40205] (NDQ6)   
`33` | [PC6][40205] (NRB0)  | `34` | [PC13][40205] (NDQ5)   
`35` | [PC7][40205] (NRB1)  | `36` | [PC12][40205] (NDQ4)   
`37` | [PC8][40205] (NDQ0)  | `38` | [PC11][40205] (NDQ3)   
`39` | [PC9][40205] (NDQ1)  | `40` | [PC10][40205] (NDQ2)
