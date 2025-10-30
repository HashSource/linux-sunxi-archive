# H3/PIO
< [H3][22544]
 
## Programmable I/O Pins (WIP)
Port Bank A  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PA00``][22547]``` `` | D11  | I/O  | [UART2_TX][22548] | JTAG_MS  | _reserved_ | _reserved_ | [PA_EINT0][22549] | _reserved_  
`[PA01``][22550]``` `` | D5  | I/O  | [UART2_RX][22548] | JTAG_CK  | _reserved_ | _reserved_ | [PA_EINT1][22549] | _reserved_  
`[PA02``][22551]``` `` | D6  | I/O  | [UART2_RTS][22548] | JTAG_DO  | _reserved_ | _reserved_ | [PA_EINT2][22549] | _reserved_  
`[PA03``][22552]``` `` | E13  | I/O  | [UART2_CTS][22548] | JTAG_DI  | _reserved_ | _reserved_ | [PA_EINT3][22549] | _reserved_  
`[PA04``][22553]``` `` | F5  | I/O  | [UART0_TX][22548] | _reserved_ | _reserved_ | _reserved_ | [PA_EINT4][22549] | _reserved_  
`[PA05``][22554]``` `` | H6  | I/O  | [UART0_RX][22548] | PWM0  | _reserved_ | _reserved_ | [PA_EINT5][22549] | _reserved_  
`[PA06``][22555]``` `` | E14  | I/O  | SIM_PWREN  | PWM1  | _reserved_ | _reserved_ | [PA_EINT6][22549] | _reserved_  
`[PA07``][22556]``` `` | D8  | I/O  | SIM_CLK  | _reserved_ | _reserved_ | _reserved_ | [PA_EINT7][22549] | _reserved_  
`[PA08``][22557]``` `` | F13  | I/O  | SIM_DATA  | _reserved_ | _reserved_ | _reserved_ | [PA_EINT8][22549] | _reserved_  
`[PA09``][22558]``` `` | D13  | I/O  | SIM_RST  | _reserved_ | _reserved_ | _reserved_ | [PA_EINT9][22549] | _reserved_  
`[PA10``][22559]``` `` | E11  | I/O  | SIM_DET  | _reserved_ | _reserved_ | _reserved_ | [PA_EINT10][22549] | _reserved_  
`[PA11``][22560]``` `` | F11  | I/O  | [TWI TWI0_SCK][22561] | DI_TX  | _reserved_ | _reserved_ | [PA_EINT11][22549] | _reserved_  
`[PA12``][22562]``` `` | C13  | I/O  | [TWI TWI0_SDA][22563] | DI_RX  | _reserved_ | _reserved_ | [PA_EINT12][22549] | _reserved_  
`[PA13``][22564]``` `` | E15  | I/O  | [SPI1_CS][22565] | [UART3_TX][22548] | _reserved_ | _reserved_ | [PA_EINT13][22549] | _reserved_  
`[PA14``][22566]``` `` | G12  | I/O  | [SPI1_CLK][22565] | [UART3_RX][22548] | _reserved_ | _reserved_ | [PA_EINT14][22549] | _reserved_  
`[PA15``][22567]``` `` | F14  | I/O  | [SPI1_MOSI][22565] | [UART3_RTS][22548] | _reserved_ | _reserved_ | [PA_EINT15][22549] | _reserved_  
`[PA16``][22568]``` `` | D15  | I/O  | [SPI1_MISO][22565] | [UART3_CTS][22548] | _reserved_ | _reserved_ | [PA_EINT16][22549] | _reserved_  
`[PA17``][22569]``` `` | C14  | I/O  | [OWA_OUT][22570] | _reserved_ | _reserved_ | _reserved_ | [PA_EINT17][22549] | _reserved_  
`[PA18``][22571]``` `` | B13  | I/O  | PCM0_SYNC  | [TWI TWI1_SCK][22572] | _reserved_ | _reserved_ | [PA_EINT18][22549] | _reserved_  
`[PA19``][22573]``` `` | B14  | I/O  | PCM0_CLK  | [TWI TWI1_SDA][22574] | _reserved_ | _reserved_ | [PA_EINT19][22549] | _reserved_  
`[PA20``][22575]``` `` | A13  | I/O  | PCM0_DOUT  | SIM_VPPEN  | _reserved_ | _reserved_ | [PA_EINT20][22549] | _reserved_  
`[PA21``][22576]``` `` | A14  | I/O  | PCM0_DIN  | SIM_VPPPP  | _reserved_ | _reserved_ | [PA_EINT21][22549] | _reserved_  
Port Bank C  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PC00``][22577]``` `` | C15  | I/O  | [NAND_WE#][22578] | SPI0_MOSI  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC01``][22579]``` `` | C16  | I/O  | [NALE][22578] | [SPI0_MISO][22565] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC02``][22580]``` `` | B16  | I/O  | [NCLE][22578] | [SPI0_CLK][22565] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC03``][22581]``` `` | B15  | I/O  | [NCE1][22578] | [SPI0_CS][22565] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC04``][22582]``` `` | F16  | I/O  | [NCE0][22578] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC05``][22583]``` `` | A17  | I/O  | [NRE#][22578] | SDC2_CLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC06``][22584]``` `` | E16  | I/O  | [NRB0][22578] | SDC2_CMD  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC07``][22585]``` `` | A16  | I/O  | [NRB1][22578] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC08``][22586]``` `` | B18  | I/O  | [NDQ0][22578] | SDC2_D0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC09``][22587]``` `` | C17  | I/O  | [NDQ1][22578] | SDC2_D1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC10``][22588]``` `` | D17  | I/O  | [NDQ2][22578] | SDC2_D2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC11``][22589]``` `` | C18  | I/O  | [NDQ3][22578] | SDC2_D3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC12``][22590]``` `` | B17  | I/O  | [NDQ4][22578] | SDC2_D4  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC13``][22591]``` `` | B19  | I/O  | [NDQ5][22578] | SDC2_D5  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC14``][22592]``` `` | F17  | I/O  | [NDQ6][22578] | SDC2_D6  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC15``][22593]``` `` | C19  | I/O  | [NDQ7][22578] | SDC2_D7  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC16``][22594]``` `` | H16  | I/O  | [NDQS][22578] | SDC2_RST  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
Port Bank D  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PD00``][22595]``` `` | C21  | I/O  | RGMII_RXD3/MII_RXD3/RMII_NULL  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD01``][22596]``` `` | H17  | I/O  | RGMII_RXD2/MII_RXD2/RMII_NULL  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD02``][22597]``` `` | B20  | I/O  | RGMII_RXD1/MII_RXD1/RMII_RXD1  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD03``][22598]``` `` | H18  | I/O  | RGMII_RXD0/MII_RXD0/RMII_RXD0  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD04``][22599]``` `` | A20  | I/O  | RGMII_RXCK/MII_RXCK/RMII_NULL  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD05``][22600]``` `` | F19  | I/O  | RGMII_RXCTL/MII_RXDV/RMII_CRS_DV  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD06``][22601]``` `` | B21  | I/O  | RGMII_NULL/MII_RXERR/RMII_RXER  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD07``][22602]``` `` | E18  | I/O  | RGMII_TXD3/MII_TXD3/RMII_NULL  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD08``][22603]``` `` | E20  | I/O  | RGMII_TXD2/MII_TXD2/RMII_NULL  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD09``][22604]``` `` | F21  | I/O  | RGMII_TXD1/MII_TXD1/RMII_TXD1  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD10``][22605]``` `` | H19  | I/O  | RGMII_TXD0/MII_TXD0/RMII_TXD0  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD11``][22606]``` `` | F20  | I/O  | RGMII_NULL/MII_CRS/RMII_NULL  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD12``][22607]``` `` | E19  | I/O  | RGMII_TXCK/MII_TXCK/RMII_TXCK  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD13``][22608]``` `` | K17  | I/O  | RGMII_TXCTL/MII_TXEN/RMII_TXEN  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD14``][22609]``` `` | L17  | I/O  | RGMII_NULL/MII_TXERR/RMII_NULL  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD15``][22610]``` `` | K18  | I/O  | RGMII_CLKIN/MII_COL/RMII_NULL  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD16``][22611]``` `` | L18  | I/O  | MDC  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD17``][22612]``` `` | L19  | I/O  | MDIO  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
Port Bank E  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PE00``][22613]``` `` | B10  | I/O  | CSI_PCLK  | TS_CLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE01``][22614]``` `` | A10  | I/O  | CSI_MCLK  | TS_ERR  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE02``][22615]``` `` | B11  | I/O  | CSI_HSYNC  | TS_SYNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE03``][22616]``` `` | C10  | I/O  | CSI_VSYNC  | TS_DVLD  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE04``][22617]``` `` | C9  | I/O  | CSI_D0  | TS_D0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE05``][22618]``` `` | E10  | I/O  | CSI_D1  | TS_D1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE06``][22619]``` `` | D10  | I/O  | CSI_D2  | TS_D2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE07``][22620]``` `` | C8  | I/O  | CSI_D3  | TS_D3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE08``][22621]``` `` | C11  | I/O  | CSI_D4  | TS_D4  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE09``][22622]``` `` | C12  | I/O  | CSI_D5  | TS_D5  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE10``][22623]``` `` | E8  | I/O  | CSI_D6  | TS_D6  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE11``][22624]``` `` | A11  | I/O  | CSI_D7  | TS_D7  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE12``][22625]``` `` | B12  | I/O  | CSI_SCK  | TWI2_SCK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE13``][22626]``` `` | C7  | I/O  | CSI_SDA  | TWI2_SDA  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE14``][22627]``` `` | C6  | I/O  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE15``][22628]``` `` | C5  | I/O  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
Port Bank F  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PF00``][22629]``` `` | D19  | I/O  | SDC0_D1  | JTAG_MS  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PF01``][22630]``` `` | A19  | I/O  | SDC0_D0  | JTAG_DI  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PF02``][22631]``` `` | D20  | I/O  | SDC0_CLK  | UART0_TX  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PF03``][22632]``` `` | F18  | I/O  | SDC0_CMD  | JTAG_DO  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PF04``][22633]``` `` | E21  | I/O  | SDC0_D3  | UART0_RX  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PF05``][22634]``` `` | C20  | I/O  | SDC0_D2  | JTAG_CK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PF06``][22635]``` `` | G18  | I/O  | SDC0_DET  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
Port Bank G  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PG00``][22636]``` `` | J3  | I/O  | SDC1_CLK  | _reserved_ | _reserved_ | _reserved_ | PG_EINT0  | _reserved_  
`[PG01``][22637]``` `` | L2  | I/O  | SDC1_CMD  | _reserved_ | _reserved_ | _reserved_ | PG_EINT1  | _reserved_  
`[PG02``][22638]``` `` | H4  | I/O  | SDC1_D0  | _reserved_ | _reserved_ | _reserved_ | PG_EINT2  | _reserved_  
`[PG03``][22639]``` `` | F3  | I/O  | SDC1_D1  | _reserved_ | _reserved_ | _reserved_ | PG_EINT3  | _reserved_  
`[PG04``][22640]``` `` | C2  | I/O  | SDC1_D2  | _reserved_ | _reserved_ | _reserved_ | PG_EINT4  | _reserved_  
`[PG05``][22641]``` `` | C1  | I/O  | SDC1_D3  | _reserved_ | _reserved_ | _reserved_ | PG_EINT5  | _reserved_  
`[PG06``][22642]``` `` | G4  | I/O  | UART1_TX  | _reserved_ | _reserved_ | _reserved_ | PG_EINT6  | _reserved_  
`[PG07``][22643]``` `` | D3  | I/O  | UART1_RX  | _reserved_ | _reserved_ | _reserved_ | PG_EINT7  | _reserved_  
`[PG08``][22644]``` `` | C3  | I/O  | UART1_RTS  | _reserved_ | _reserved_ | _reserved_ | PG_EINT8  | _reserved_  
`[PG09``][22645]``` `` | E3  | I/O  | UART1_CTS  | _reserved_ | _reserved_ | _reserved_ | PG_EINT9  | _reserved_  
`[PG10``][22646]``` `` | M3  | I/O  | PCM1_SYNC  | _reserved_ | _reserved_ | _reserved_ | PG_EINT10  | _reserved_  
`[PG11``][22647]``` `` | D2  | I/O  | PCM1_CLK  | _reserved_ | _reserved_ | _reserved_ | PG_EINT11  | _reserved_  
`[PG12``][22648]``` `` | D1  | I/O  | PCM1_DOUT  | _reserved_ | _reserved_ | _reserved_ | PG_EINT12  | _reserved_  
`[PG13``][22649]``` `` | B1  | I/O  | PCM1_DIN  | _reserved_ | _reserved_ | _reserved_ | PG_EINT13  | _reserved_  
Port Bank L  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PL00``][22650]``` `` | N1  | I/O  | S_TWI_SCK  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT0  | _reserved_  
`[PL01``][22651]``` `` | M1  | I/O  | S_TWI_SDA  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT1  | _reserved_  
`[PL02``][22652]``` `` | P2  | I/O  | S_UART_TX  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT2  | _reserved_  
`[PL03``][22653]``` `` | R1  | I/O  | S_UART_RX  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT3  | _reserved_  
`[PL04``][22654]``` `` | N2  | I/O  | S_JTAG_MS  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT4  | _reserved_  
`[PL05``][22655]``` `` | R2  | I/O  | S_JTAG_CK  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT5  | _reserved_  
`[PL06``][22656]``` `` | T4  | I/O  | S_JTAG_DO  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT6  | _reserved_  
`[PL07``][22657]``` `` | T3  | I/O  | S_JTAG_DI  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT7  | _reserved_  
`[PL08``][22658]``` `` | T2  | I/O  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT8  | _reserved_  
`[PL09``][22659]``` `` | M6  | I/O  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT9  | _reserved_  
`[PL10``][22660]``` `` | V2  | I/O  | S_PWM  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT10  | _reserved_  
`[PL11``][22661]``` `` | U2  | I/O  | S_CIR_RX  | _reserved_ | _reserved_ | _reserved_ | S_PL_EINT12  | _reserved_  
## See also
  * [H3][22544]
