# A10/PIO
< [A10][556]
 
## Programmable I/O Pins
Port Bank A  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PA00``][559]``` `` | D05  | I/O  | [ERXD3][560] | [SPI1_CS0][561] | [UART2_RTS][562] | _reserved_ | _reserved_ | _reserved_  
`[PA01``][563]``` `` | E05  | I/O  | [ERXD2][560] | [SPI1_CLK][561] | [UART2_CTS][562] | _reserved_ | _reserved_ | _reserved_  
`[PA02``][564]``` `` | D06  | I/O  | [ERXD1][560] | [SPI1_MOSI][561] | [UART2_TX][562] | _reserved_ | _reserved_ | _reserved_  
`[PA03``][565]``` `` | E06  | I/O  | [ERXD0][560] | [SPI1_MISO][561] | [UART2_RX][562] | _reserved_ | _reserved_ | _reserved_  
`[PA04``][566]``` `` | D07  | I/O  | [ETXD3][560] | [SPI1_CS1][561] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PA05``][567]``` `` | E07  | I/O  | [ETXD2][560] | [SPI3_CS0][561] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PA06``][568]``` `` | D08  | I/O  | [ETXD1][560] | [SPI3_CLK][561] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PA07``][569]``` `` | E08  | I/O  | [ETXD0][560] | [SPI3_MOSI][561] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PA08``][570]``` `` | D09  | I/O  | [ERXCK][560] | [SPI3_MISO][561] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PA09``][571]``` `` | E09  | I/O  | [ERXERR][560] | [SPI3_CS1][561] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PA10``][572]``` `` | D10  | I/O  | [ERXDV][560] | _reserved_ | [UART1_TX][562] | _reserved_ | _reserved_ | _reserved_  
`[PA11``][573]``` `` | E10  | I/O  | [EMDC][560] | _reserved_ | [UART1_RX][562] | _reserved_ | _reserved_ | _reserved_  
`[PA12``][574]``` `` | D11  | I/O  | [EMDIO][560] | [UART6_TX][562] | [UART1_RTS][562] | _reserved_ | _reserved_ | _reserved_  
`[PA13``][575]``` `` | E11  | I/O  | [ETXEN][560] | [UART6_RX][562] | [UART1_CTS][562] | _reserved_ | _reserved_ | _reserved_  
`[PA14``][576]``` `` | D12  | I/O  | [ETXCK][560] | [UART7_TX][562] | [UART1_DTR][562] | _reserved_ | _reserved_ | _reserved_  
`[PA15``][577]``` `` | E12  | I/O  | [ECRS][560] | [UART7_RX][562] | [UART1_DSR][562] | _reserved_ | _reserved_ | _reserved_  
`[PA16``][578]``` `` | D13  | I/O  | [ECOL][560] | [CAN_TX][579] | [UART1_DCD][562] | _reserved_ | _reserved_ | _reserved_  
`[PA17``][580]``` `` | C13  | I/O  | [ETXERR][560] | [CAN_RX][579] | [UART1_RING][562] | _reserved_ | _reserved_ | _reserved_  
Port Bank B  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7  | notes   
`[PB00``][581]``` `` | A15  | I/O  | [TWI0_SCK][582] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB01``][583]``` `` | B15  | I/O  | [TWI0_SDA][582] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB02``][584]``` `` | A14  | I/O  | PWM0  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB03``][585]``` `` | B14  | I/O  | IR0_TX  | _reserved_ | SPDIF_MCLK  | _reserved_ | STANBYWFI  | _reserved_ | verify SPDIF_MCLK   
`[PB04``][586]``` `` | A13  | I/O  | IR0_RX  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB05``][587]``` `` | B13  | I/O  | I2S_MCLK  | AC97_MCLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB06``][588]``` `` | A12  | I/O  | I2S_BCLK  | AC97_BCLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB07``][589]``` `` | B12  | I/O  | I2S_LRCK  | AC97_SYNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB08``][590]``` `` | A11  | I/O  | I2S_DO0  | AC97_DO  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | verify AC97_DO   
`[PB09``][591]``` `` | C12  | I/O  | I2S_DO1  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_ | verify AC97_DO   
`[PB10``][592]``` `` | C11  | I/O  | I2S_DO2  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB11``][593]``` `` | C10  | I/O  | I2S_DO3  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB12``][594]``` `` | C9  | I/O  | I2S_DI  | AC97_DI  | SPDIF_DI  | _reserved_ | _reserved_ | _reserved_ | verify SPDIF_DI   
`[PB13``][595]``` `` | B11  | I/O  | SPI2_CS1  | _reserved_ | SPDIF_DO  | _reserved_ | _reserved_ | _reserved_ | verify SPDIF_DO   
`[PB14``][596]``` `` | A10  | I/O  | SPI2_CS0  | JTAG_MS0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB15``][597]``` `` | B10  | I/O  | SPI2_CLK  | JTAG_CK0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB16``][598]``` `` | A9  | I/O  | SPI2_MOSI  | JTAG_DO0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB17``][599]``` `` | B9  | I/O  | SPI2_MISO  | JTAG_DI0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB18``][600]``` `` | A8  | I/O  | [TWI1_SCK][582] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB19``][601]``` `` | B8  | I/O  | [TWI1_SDA][582] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB20``][602]``` `` | C8  | I/O  | [TWI2_SCK][582] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB21``][603]``` `` | C7  | I/O  | [TWI2_SDA][582] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB22``][604]``` `` | A7  | I/O  | UART0_TX  | IR1_TX  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB23``][605]``` `` | B7  | I/O  | UART0_RX  | IR1_RX  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
Port Bank C  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PC00``][606]``` `` | M23  | I/O  | [NAND_WE#][607] | SPI0_MOSI  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC01``][608]``` `` | M22  | I/O  | [NALE][607] | SPI0_MISO  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC02``][609]``` `` | L32  | I/O  | [NCLE][607] | SPI0_CLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC03``][610]``` `` | L22  | I/O  | [NCE1][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC04``][611]``` `` | K23  | I/O  | [NCE0][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC05``][612]``` `` | K22  | I/O  | [NRE#][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC06``][613]``` `` | J23  | I/O  | [NRB0][607] | SDC2_CMD  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC07``][614]``` `` | J22  | I/O  | [NRB1][607] | SDC2_CLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC08``][615]``` `` | H23  | I/O  | [NDQ0][607] | SDC2_D0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC09``][616]``` `` | H22  | I/O  | [NDQ1][607] | SDC2_D1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC10``][617]``` `` | G23  | I/O  | [NDQ2][607] | SDC2_D2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC11``][618]``` `` | G22  | I/O  | [NDQ3][607] | SDC2_D3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC12``][619]``` `` | H21  | I/O  | [NDQ4][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC13``][620]``` `` | H20  | I/O  | [NDQ5][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC14``][621]``` `` | G21  | I/O  | [NDQ6][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC15``][622]``` `` | G20  | I/O  | [NDQ7][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC16``][623]``` `` | M21  | I/O  | [NWP][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC17``][624]``` `` | F23  | I/O  | [NCE2][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC18``][625]``` `` | F22  | I/O  | [NCE3][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC19``][626]``` `` | L21  | I/O  | [NCE4][607] | SPI2_CS0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC20``][627]``` `` | K21  | I/O  | [NCE5][607] | SPI2_CLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC21``][628]``` `` | J21  | I/O  | [NCE6][607] | SPI2_MOSI  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC22``][629]``` `` | J20  | I/O  | [NCE7][607] | SPI2_MISO  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC23``][630]``` `` | G19  | I/O  | _reserved_ | SPI0_CS0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC24``][631]``` `` | F21  | I/O  | [NDQS][607] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
Port Bank D  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PD00``][632]``` `` | AB15  | I/O  | LCD0_D0  | LVDS0_VP0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD01``][633]``` `` | AC15  | I/O  | LCD0_D1  | LVDS0_VN0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD02``][634]``` `` | AB14  | I/O  | LCD0_D2  | LVDS0_VP1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD03``][635]``` `` | AC14  | I/O  | LCD0_D3  | LVDS0_VN1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD04``][636]``` `` | AB13  | I/O  | LCD0_D4  | LVDS0_VP2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD05``][637]``` `` | AC13  | I/O  | LCD0_D5  | LVDS0_VN2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD06``][638]``` `` | AB12  | I/O  | LCD0_D6  | LVDS0_VPC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD07``][639]``` `` | AC12  | I/O  | LCD0_D7  | LVDS0_VNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD08``][640]``` `` | AB11  | I/O  | LCD0_D8  | LVDS0_VP3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD09``][641]``` `` | AC11  | I/O  | LCD0_D9  | LVDS0_VN3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD10``][642]``` `` | Y15  | I/O  | LCD0_D10  | LVDS1_VP0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD11``][643]``` `` | AA15  | I/O  | LCD0_D11  | LVDS1_VN0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD12``][644]``` `` | Y14  | I/O  | LCD0_D12  | LVDS1_VP1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD13``][645]``` `` | AA14  | I/O  | LCD0_D13  | LVDS1_VN1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD14``][646]``` `` | Y13  | I/O  | LCD0_D14  | LVDS1_VP2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD15``][647]``` `` | AA13  | I/O  | LCD0_D15  | LVDS1_VN2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD16``][648]``` `` | Y12  | I/O  | LCD0_D16  | LVDS1_VPC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD17``][649]``` `` | AA12  | I/O  | LCD0_D17  | LVDS1_VNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD18``][650]``` `` | Y11  | I/O  | LCD0_D18  | LVDS1_VP3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD19``][651]``` `` | AA11  | I/O  | LCD0_D19  | LVDS1_VN3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD20``][652]``` `` | Y10  | I/O  | LCD0_D20  | CSI1_MCLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD21``][653]``` `` | AA10  | I/O  | LCD0_D21  | SMC_VPPEN  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD22``][654]``` `` | AB10  | I/O  | LCD0_D22  | SMC_VPPPP  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD23``][655]``` `` | AC10  | I/O  | LCD0_D23  | SMC_DET  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD24``][656]``` `` | Y9  | I/O  | LCD0_CLK  | SMC_VCCEN  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD25``][657]``` `` | AA9  | I/O  | LCD0_DE  | SMC_RST  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD26``][658]``` `` | AB9  | I/O  | LCD0_HSYNC  | SMC_SCK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD27``][659]``` `` | AC9  | I/O  | LCD0_VSYNC  | SMC_SDA  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
Port Bank E  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PE00``][660]``` `` | E23  | I/O  | TS0_CLK  | CSI0_PCK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE01``][661]``` `` | E22  | I/O  | TS0_ERR  | CSI0_CK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE02``][662]``` `` | D23  | I/O  | TS0_SYNC  | CSI0_HSYNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE03``][663]``` `` | D22  | I/O  | TS0_DVLD  | CSI0_VSYNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE04``][664]``` `` | C23  | I/O  | TS0_D0  | CSI0_D0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE05``][665]``` `` | C22  | I/O  | TS0_D1  | CSI0_D1  | SMC_VPPEN  | _reserved_ | _reserved_ | _reserved_  
`[PE06``][666]``` `` | B23  | I/O  | TS0_D2  | CSI0_D2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE07``][667]``` `` | B22  | I/O  | TS0_D3  | CSI0_D3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE08``][668]``` `` | A23  | I/O  | TS0_D4  | CSI0_D4  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE09``][669]``` `` | A22  | I/O  | TS0_D5  | CSI0_D5  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE10``][670]``` `` | B21  | I/O  | TS0_D6  | CSI0_D6  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE11``][671]``` `` | A21  | I/O  | TS0_D7  | CSI0_D7  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
Port Bank F  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PF00``][672]``` `` | M20  | I/O  | SDC0_D1  | _reserved_ | JTAG_MS1  | _reserved_ | _reserved_ | _reserved_  
`[PF01``][673]``` `` | M19  | I/O  | SDC0_D0  | _reserved_ | JTAG_DI1  | _reserved_ | _reserved_ | _reserved_  
`[PF02``][674]``` `` | L20  | I/O  | SDC0_CLK  | _reserved_ | UART0_TX  | _reserved_ | _reserved_ | _reserved_  
`[PF03``][675]``` `` | L19  | I/O  | SDC0_CMD  | _reserved_ | JTAG_DO1  | _reserved_ | _reserved_ | _reserved_  
`[PF04``][676]``` `` | K20  | I/O  | SDC0_D3  | _reserved_ | UART0_RX  | _reserved_ | _reserved_ | _reserved_  
`[PF05``][677]``` `` | K19  | I/O  | SDC0_D2  | _reserved_ | JTAG_CK1  | _reserved_ | _reserved_ | _reserved_  
Port Bank G  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PG00``][678]``` `` | F20  | I/O  | TS1_CLK  | CSI1_PCK  | SDC1_CMD  | _reserved_ | _reserved_ | _reserved_  
`[PG01``][679]``` `` | E21  | I/O  | TS1_ERR  | CSI1_CK  | SDC1_CLK  | _reserved_ | _reserved_ | _reserved_  
`[PG02``][680]``` `` | E20  | I/O  | TS1_SYNC  | CSI1_HSYNC  | SDC1_D0  | _reserved_ | _reserved_ | _reserved_  
`[PG03``][681]``` `` | D21  | I/O  | TS1_DVLD  | CSI1_VSYNC  | SDC1_D1  | _reserved_ | _reserved_ | _reserved_  
`[PG04``][682]``` `` | D20  | I/O  | TS1_D0  | CSI1_D0  | SDC1_D2  | CSI0_D8  | _reserved_ | _reserved_  
`[PG05``][683]``` `` | C21  | I/O  | TS1_D1  | CSI1_D1  | SDC1_D3  | CSI0_D9  | _reserved_ | _reserved_  
`[PG06``][684]``` `` | E19  | I/O  | TS1_D2  | CSI1_D2  | UART3_TX  | CSI0_D10  | _reserved_ | _reserved_  
`[PG07``][685]``` `` | C20  | I/O  | TS1_D3  | CSI1_D3  | UART3_RX  | CSI0_D11  | _reserved_ | _reserved_  
`[PG08``][686]``` `` | D19  | I/O  | TS1_D4  | CSI1_D4  | UART3_RTS  | CSI0_D12  | _reserved_ | _reserved_  
`[PG09``][687]``` `` | C19  | I/O  | TS1_D5  | CSI1_D5  | UART3_CTS  | CSI0_D13  | _reserved_ | _reserved_  
`[PG10``][688]``` `` | D18  | I/O  | TS1_D6  | CSI1_D6  | UART4_TX  | CSI0_D14  | _reserved_ | _reserved_  
`[PG11``][689]``` `` | C18  | I/O  | TS1_D7  | CSI1_D7  | UART4_RX  | CSI0_D15  | _reserved_ | _reserved_  
Port Bank H  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PH00``][690]``` `` | A6  | I/O  | LCD1_D00  | ATAA00  | UART3_TX  | _reserved_ | EINT0  | CSI1_D0   
`[PH01``][691]``` `` | B6  | I/O  | LCD1_D01  | ATAA01  | UART3_RX  | _reserved_ | EINT1  | CSI1_D1   
`[PH02``][692]``` `` | C6  | I/O  | LCD1_D02  | ATAA02  | UART3_RTS  | _reserved_ | EINT2  | CSI1_D2   
`[PH03``][693]``` `` | A5  | I/O  | LCD1_D03  | ATAIRQ  | UART3_CTS  | _reserved_ | EINT3  | CSI1_D3   
`[PH04``][694]``` `` | B5  | I/O  | LCD1_D04  | ATAD00  | UART4_TX  | _reserved_ | EINT4  | CSI1_D4   
`[PH05``][695]``` `` | C5  | I/O  | LCD1_D05  | ATAD01  | UART4_RX  | _reserved_ | EINT5  | CSI1_D5   
`[PH06``][696]``` `` | A4  | I/O  | LCD1_D06  | ATAD02  | UART5_TX  | MS_BS  | EINT6  | CSI1_D6   
`[PH07``][697]``` `` | B4  | I/O  | LCD1_D07  | ATAD03  | UART5_RX  | MS_CLK  | EINT7  | CSI1_D7   
`[PH08``][698]``` `` | C4  | I/O  | LCD1_D08  | ATAD05  | KP_IN0  | MS_D1  | EINT8  | CSI1_D9   
`[PH09``][699]``` `` | D4  | I/O  | LCD1_D09  | ATAD04  | KP_IN1  | MS_D0  | EINT9  | CSI1_D8   
`[PH10``][700]``` `` | A3  | I/O  | LCD1_D10  | ATAD06  | KP_IN2  | MS_D2  | EINT10  | CSI1_D10   
`[PH11``][701]``` `` | B3  | I/O  | LCD1_D11  | ATAD07  | KP_IN3  | MS_D3  | EINT11  | CSI1_D11   
`[PH12``][702]``` `` | C3  | I/O  | LCD1_D12  | ATAD08  | PS2_SCK1  | _reserved_ | EINT12  | CSI1_D12   
`[PH13``][703]``` `` | A2  | I/O  | LCD1_D13  | ATAD09  | PS2_SDA1  | SMC_RST  | EINT13  | CSI1_D13   
`[PH14``][704]``` `` | B2  | I/O  | LCD1_D14  | ATAD10  | KP_IN4  | SMC_VPPEN  | EINT14  | CSI1_D14   
`[PH15``][705]``` `` | A1  | I/O  | LCD1_D15  | ATAD11  | KP_IN5  | SMC_VPPPP  | EINT15  | CSI1_D15   
`[PH16``][706]``` `` | B1  | I/O  | LCD1_D16  | ATAD12  | KP_IN6  | _reserved_ | EINT16  | CSI1_D16   
`[PH17``][707]``` `` | C1  | I/O  | LCD1_D17  | ATAD13  | KP_IN7  | SMC_VCCEN  | EINT17  | CSI1_D17   
`[PH18``][708]``` `` | C2  | I/O  | LCD1_D18  | ATAD14  | KP_OUT0  | SMC_SCK  | EINT18  | CSI1_D18   
`[PH19``][709]``` `` | D1  | I/O  | LCD1_D19  | ATAD15  | KP_OUT1  | SMC_SDA  | EINT19  | CSI1_D19   
`[PH20``][710]``` `` | D2  | I/O  | LCD1_D20  | ATAOE  | CAN_TX  | _reserved_ | EINT20  | CSI1_D20   
`[PH21``][711]``` `` | D3  | I/O  | LCD1_D21  | ATADREQ  | CAN_RX  | _reserved_ | EINT21  | CSI1_D21   
`[PH22``][712]``` `` | E1  | I/O  | LCD1_D22  | ATADACK  | KP_OUT2  | SDC1_CMD  | _reserved_ | CSI1_D22   
`[PH23``][713]``` `` | E2  | I/O  | LCD1_D23  | ATACS0  | KP_OUT3  | SDC1_CLK  | _reserved_ | CSI1_D23   
`[PH24``][714]``` `` | E3  | I/O  | LCD1_CLK  | ATAIORDY  | KP_OUT4  | SDC1_D1  | _reserved_ | CSI1_FIELD   
`[PH25``][715]``` `` | E4  | I/O  | LCD1_DE  | ATACS1  | KP_OUT5  | SDC1_D0  | _reserved_ | CSI1_PCLK   
`[PH26``][716]``` `` | F3  | I/O  | LCD1_HSYNC  | ATAIOR  | KP_OUT6  | SDC1_D2  | _reserved_ | CSI1_HSYNC   
`[PH27``][717]``` `` | F4  | I/O  | LCD1_VSYNC  | ATAIOW  | KP_OUT7  | SDC1_D3  | _reserved_ | CSI1_VSYNC   
Port Bank I  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PI00``][718]``` `` | A20  | I/O  | [GPS GPS_CLK][719] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI01``][720]``` `` | B20  | I/O  | [GPS GPS_SIGN][721] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI02``][722]``` `` | A19  | I/O  | [GPS GPS_MAG][723] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI03``][724]``` `` | B19  | I/O  | [PWM1][725] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI04``][726]``` `` | A18  | I/O  | [SDC3_CMD][727] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI05``][728]``` `` | B18  | I/O  | [SDC3_CLK][727] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI06``][729]``` `` | A17  | I/O  | [SDC3_D0][727] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI07``][730]``` `` | B17  | I/O  | [SDC3_D1][727] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI08``][731]``` `` | A16  | I/O  | [SDC3_D2][727] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI09``][732]``` `` | B16  | I/O  | [SDC3_D3][727] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI10``][733]``` `` | C17  | I/O  | [SPI0_CS0][734] | [UART5_TX][735] | _reserved_ | _reserved_ | EINT22  | _reserved_  
`[PI11``][736]``` `` | D17  | I/O  | [SPI0_CLK][734] | [UART5_RX][735] | _reserved_ | _reserved_ | EINT23  | _reserved_  
`[PI12``][737]``` `` | C16  | I/O  | [SPI0_MOSI][734] | [UART6_TX][735] | _reserved_ | _reserved_ | EINT24  | _reserved_  
`[PI13``][738]``` `` | D16  | I/O  | [SPI0_MISO][734] | [UART6_RX][735] | _reserved_ | _reserved_ | EINT25  | _reserved_  
`[PI14``][739]``` `` | C16  | I/O  | [SPI0_CS1][734] | [PS2_SCK1][740] | TCLKIN0  | _reserved_ | EINT26  | _reserved_  
`[PI15``][741]``` `` | D15  | I/O  | [SPI1_CS1][734] | [PS2_SDA1][740] | TCLKIN1  | _reserved_ | EINT27  | _reserved_  
`[PI16``][742]``` `` | E17  | I/O  | [SPI1_CS0][734] | [UART2_RTS][735] | _reserved_ | _reserved_ | EINT28  | _reserved_  
`[PI17``][743]``` `` | E16  | I/O  | [SPI1_CLK][734] | [UART2_CTS][735] | _reserved_ | _reserved_ | EINT29  | _reserved_  
`[PI18``][744]``` `` | E15  | I/O  | [SPI1_MOSI][734] | [UART2_TX][735] | _reserved_ | _reserved_ | EINT30  | _reserved_  
`[PI19``][745]``` `` | D14  | I/O  | [SPI1_MISO][734] | [UART2_RX][735] | _reserved_ | _reserved_ | EINT31  | _reserved_  
`[PI20``][746]``` `` | E14  | I/O  | [PS2_SCK0][740] | [UART7_TX][735] | _reserved_ | _reserved_ | HSCL  | _reserved_  
`[PI21``][747]``` `` | E13  | I/O  | [PS2_SDA0][740] | [UART7_RX][735] | _reserved_ | _reserved_ | HSDA  | _reserved_  
## Other Pins
Port | Ball | Function | Type | Comment   
---|---|---|---|---  
`XP_TP` | Y22 | Input | AI | Touchpad X+   
`XN_TP` | AA22 | Input | AI | Touchpad X-   
`YP_TP` | Y23 | Input | AI | Touchpad Y+   
`YN_TP` | AA23 | Input | AI | Touchpad Y-   
LRADC0 | AB23 | Input |  | Low Resolution ADC0   
LRADC1 | AB22 | Input |  | Low Resolution ADC1   
DM0 | N20 | I/O |  | USB0 D-   
DP0 | N21 | I/O |  | USB0 D+   
DM1 | P20 | I/O |  | USB1 D-   
DP1 | P21 | I/O |  | USB1 D+   
DM2 | R20 | I/O |  | USB2 D-   
DP2 | R21 | I/O |  | USB2 D+
