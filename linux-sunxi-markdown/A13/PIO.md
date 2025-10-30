# A13/PIO
< [A13][1710]
 
## Contents
  * [1 PB][1713]
  * [2 PC][1714]
  * [3 PD][1715]
  * [4 PE][1716]
  * [5 PF][1717]
  * [6 PG][1718]

## PB
Port  | Pin  | Type  | MUX 2  | MUX 4  | MUX 6   
---|---|---|---|---|---  
`PB0` | 101  | I/O  | [TWI0-SCK][1719]  
`PB1` | 102  | I/O  | [TWI0-SDA][1719]  
`PB2` | 103  | I/O  | PWM  | SPI2-MOSI  | EINT16   
`PB3` | 150  | I/O  | IR_TX  | SPI2_MISO  | EINT17   
`PB4` | 104  | I/O  | IR_RX  |  | EINT18   
`PB10` | 10  | I/O  | SPI2_CS1  |  | EINT24   
`PB15` | 105  | I/O  | [TWI1_SCK][1719]  
`PB16` | 106  | I/O  | [TWI1_SDA][1719]  
`PB17` | 161  | I/O  | [TWI2_SCK][1719]  
`PB18` | 160  | I/O  | [TWI2_SDA][1719]  
## PC
Port  | Pin  | Mux ?  | Mux ?   
---|---|---|---  
`PC0` | 8  | NWE  | SPI0_MOSI   
`PC1` | 7  | NALE  | SPI0_MISO   
`PC2` | 6  | NCLE  | SPI0_CLK   
`PC3` | 3  | NCE1  | SPI0_CS0   
`PC4` | 2  | NCE0   
`PC5` | 1  | NRE   
`PC6` | 176  | NRB0  | SDC2_CMD   
`PC7` | 175  | NRB1  | SDC2_CLK   
`PC8` | 174  | NDQ0  | SDC2_D0   
`PC9` | 172  | NDQ1  | SDC2_D1   
`PC10` | 171  | NDQ2  | SDC2_D2   
`PC11` | 170  | NDQ3  | SDC2_D3   
`PC12` | 168  | NDQ4  | SDC2_D4   
`PC13` | 167  | NDQ5  | SDC2_D5   
`PC14` | 166  | NDQ6  | SDC2_D6   
`PC15` | 165  | NDC7  | SDC2_D7   
`PC19` | 162  | NDQS   
## PD
Port  | Pin  | Mux ?  | Mux ?   
---|---|---|---  
`PD2` | 148  | LCD_D2   
`PD3` | 147  | LCD_D3   
`PD4` | 146  | LCD_D4   
`PD5` | 145  | LCD_D5   
`PD6` | 144  | LCD_D6   
`PD7` | 143  | LCD_D7   
`PD10` | 141  | LCD_D10   
`PD11` | 140  | LCD_D11   
`PD12` | 139  | LCD_D12   
`PD13` | 138  | LCD_D13   
`PD14` | 137  | LCD_D14   
`PD15` | 136  | LCD_D15   
`PD18` | 135  | LCD_D18   
`PD19` | 134  | LCD_D19   
`PD20` | 133  | LCD_D20   
`PD21` | 132  | LCD_D21   
`PD22` | 131  | LCD_D22   
`PD23` | 130  | LCD_D23   
`PD24` | 129  | LCD_CLK   
`PD25` | 128  | LCD_DE   
`PD26` | 127  | LCD_HSYNC   
`PD27` | 126  | LCD_VSYNC   
## PE
Port  | Pin  | Type  | MUX 3  | MUX 4  | MUX ?   
---|---|---|---|---|---  
PE0  | 114  | Input  | CSI_PCLK  | SPI2_CS0  | EINT14   
PE1  | 115  | Input  | CSI_MCLK  | SPI2_CLK  | EINT15   
PE2  | 116  | Input  | CSI_HSYNC  | SPI2_MOSI   
PE3  | 117  | I/O  | CSI_VSYNC  | SPI2_MISO   
PE4  | 118  | I/O  | CSI_D0  | SDC2_D0   
PE5  | 119  | I/O  | CSI_D1  | SDC2_D1   
PE6  | 120  | I/O  | CSI_D2  | SDC2_D2   
PE7  | 121  | I/O  | CSI_D3  | SDC2_D3   
PE8  | 122  | I/O  | CSI_D4  | SDC2_CMD   
PE9  | 123  | I/O  | CSI_D5  | SDC2_CLK   
PE10  | 124  | I/O  | CSI_D6  | UART1_TX   
PE11  | 125  | I/O  | CSI_D7  | UART1_RX   
## PF
Port Bank F  
---  
Port | Pin | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PF0``][1720]``` `` | 107  | I/O  | SDC0_DATA1  | _reserved_ | [JTAG_TMS][1721] | _reserved_ | _reserved_ | _reserved_  
`[PF1``][1722]``` `` | 108  | I/O  | SDC0_DATA0  | _reserved_ | [JTAG_TDI][1721] | _reserved_ | _reserved_ | _reserved_  
`[PF2``][1723]``` `` | 110  | I/O  | SDC0_CLK  | _reserved_ | UART0_TX  | _reserved_ | _reserved_ | _reserved_  
`[PF3``][1724]``` `` | 111  | I/O  | SDC0_CMD  | _reserved_ | [JTAG_TDO][1721] | _reserved_ | _reserved_ | _reserved_  
`[PF4``][1725]``` `` | 112  | I/O  | SDC0_DATA3  | _reserved_ | UART0_RX  | _reserved_ | _reserved_ | _reserved_  
`[PF5``][1726]``` `` | 113  | I/O  | SDC0_DATA2  | _reserved_ | [JTAG_TCK][1721] | _reserved_ | _reserved_ | _reserved_  
## PG
Port  | Pin  | Type  | MUX 2  | MUX 3  | MUX 6   
---|---|---|---|---|---  
`PG0` | 155  | Input  |  |  | EINT0   
`PG1` | 154  | Input  |  |  | EINT1   
`PG2` | 153  | Input  |  |  | EINT2   
`PG3` | 152  | I/O  | UART1_TX  |  | EINT3   
`PG4` | 151  | I/O  | UART1_RX  |  | EINT4   
`PG9` | 12  | I/O  | SPI1_CS0  | UART3_TX  | EINT9   
`PG10` | 13  | I/O  | SPI1_CLK  | UART3_RX  | EINT10   
`PG11` | 14  | I/O  | SPI1_MOSI  | UART3_CTS  | EINT11   
`PG12` | 15  | I/O  | SPI1_MISO  | UART3_RTS  | EINT12
