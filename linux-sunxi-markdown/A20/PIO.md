# A20/PIO
< [A20][2199]
 
## Contents
  * [1 Programmable I/O Pins][2202]
  * [2 Port bank A][2203]
  * [3 Port bank B][2204]
  * [4 Port bank C][2205]
  * [5 Port bank D][2206]
  * [6 Port bank E][2207]
  * [7 Port bank F][2208]
  * [8 Port bank G][2209]
  * [9 Port bank H][2210]
  * [10 Port bank I][2211]
  * [11 Other Pins][2212]
  * [12 See also][2213]

## Programmable I/O Pins
## Port bank A
Port Bank A (0)  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PA00 (0)``][2214]``` `` | D05  | I/O  | [ERXD3][2215] | [SPI1_CS0][2216] | [UART2_RTS][2217] | [GRXD3][2218] | _reserved_ | _reserved_  
`[PA01 (1)``][2219]``` `` | E05  | I/O  | [ERXD2][2215] | [SPI1_CLK][2216] | [UART2_CTS][2217] | [GRXD2][2218] | _reserved_ | _reserved_  
`[PA02 (2)``][2220]``` `` | D06  | I/O  | [ERXD1][2215] | [SPI1_MOSI][2216] | [UART2_TX][2217] | [GRXD1][2218] | _reserved_ | _reserved_  
`[PA03 (3)``][2221]``` `` | E06  | I/O  | [ERXD0][2215] | [SPI1_MISO][2216] | [UART2_RX][2217] | [GRXD0][2218] | _reserved_ | _reserved_  
`[PA04 (4)``][2222]``` `` | D07  | I/O  | [ETXD3][2215] | [SPI1_CS1][2216] | _reserved_ | [GTXD3][2218] | _reserved_ | _reserved_  
`[PA05 (5)``][2223]``` `` | E07  | I/O  | [ETXD2][2215] | [SPI3_CS0][2216] | _reserved_ | [GTXD2][2218] | _reserved_ | _reserved_  
`[PA06 (6)``][2224]``` `` | D08  | I/O  | [ETXD1][2215] | [SPI3_CLK][2216] | _reserved_ | [GTXD1][2218] | _reserved_ | _reserved_  
`[PA07 (7)``][2225]``` `` | E08  | I/O  | [ETXD0][2215] | [SPI3_MOSI][2216] | _reserved_ | [GTXD0][2218] | _reserved_ | _reserved_  
`[PA08 (8)``][2226]``` `` | D09  | I/O  | [ERXCK][2215] | [SPI3_MISO][2216] | _reserved_ | [GRXCK][2218] | _reserved_ | _reserved_  
`[PA09 (9)``][2227]``` `` | E09  | I/O  | [ERXERR][2215] | [SPI3_CS1][2216] | _reserved_ | [GNULL/ERXERR][2218] | [I²S1_MCLK][2228] | _reserved_  
`[PA10 (10)``][2229]``` `` | D10  | I/O  | [ERXDV][2215] | _reserved_ | [UART1_TX][2217] | [RXDV][2218] | _reserved_ | _reserved_  
`[PA11 (11)``][2230]``` `` | E10  | I/O  | [EMDC][2215] | _reserved_ | [UART1_RX][2217] | [GMDC][2218] | _reserved_ | _reserved_  
`[PA12 (12)``][2231]``` `` | D11  | I/O  | [EMDIO][2215] | [UART6_TX][2217] | [UART1_RTS][2217] | [GMDIO][2218] | _reserved_ | _reserved_  
`[PA13 (13)``][2232]``` `` | E11  | I/O  | [ETXEN][2215] | [UART6_RX][2217] | [UART1_CTS][2217] | [GTXCTL/ETXCK][2218] | _reserved_ | _reserved_  
`[PA14 (14)``][2233]``` `` | D12  | I/O  | [ETXCK][2215] | [UART7_TX][2217] | [UART1_DTR][2217] | [GNULL/ETXCK][2218] | [I²S1_BCLK][2228] | _reserved_  
`[PA15 (15)``][2234]``` `` | E12  | I/O  | [ECRS][2215] | [UART7_RX][2217] | [UART1_DSR][2217] | [GTXCK/ECRS][2218] | [I²S1_LRCK][2228] | _reserved_  
`[PA16 (16)``][2235]``` `` | D13  | I/O  | [ECOL][2215] | [CAN_TX][2236] | [UART1_DCD][2217] | [GCLKIN/ECOL][2218] | [I²S1_DO][2228] | _reserved_  
`[PA17 (17)``][2237]``` `` | C13  | I/O  | [ETXERR][2215] | [CAN_RX][2236] | [UART1_RING][2217] | [GNULL/ETXERR][2218] | [I²S1_DI][2228] | _reserved_  
## Port bank B
Port Bank B (1)  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7  | notes   
`[PB00 (32)``][2238]``` `` | A15  | I/O  | [TWI0_SCK][2239] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB01 (33)``][2240]``` `` | B15  | I/O  | [TWI0_SDA][2239] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB02 (34)``][2241]``` `` | A14  | I/O  | PWM0  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB03 (35)``][2242]``` `` | B14  | I/O  | IR0_TX  | _reserved_ | SPDIF_MCLK  | _reserved_ | _reserved_ | _reserved_ | verify SPDIF_MCLK   
`[PB04 (36)``][2243]``` `` | A13  | I/O  | IR0_RX  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB05 (37)``][2244]``` `` | B13  | I/O  | I²S0_MCLK  | AC97_MCLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB06 (38)``][2245]``` `` | A12  | I/O  | I²S0_BCLK  | AC97_BCLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB07 (39)``][2246]``` `` | B12  | I/O  | I²S0_LRCK  | AC97_SYNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB08 (40)``][2247]``` `` | A11  | I/O  | I²S0_DO0  | AC97_DO  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | verify AC97_DO   
`[PB09 (41)``][2248]``` `` | C12  | I/O  | I²S0_DO1  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_ | verify AC97_DO   
`[PB10 (42)``][2249]``` `` | C11  | I/O  | I²S0_DO2  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB11 (43)``][2250]``` `` | C10  | I/O  | I²S0_DO3  | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB12 (44)``][2251]``` `` | C9  | I/O  | I²S0_DI  | AC97_DI  | SPDIF_DI  | _reserved_ | _reserved_ | _reserved_ | verify SPDIF_DI   
`[PB13 (45)``][2252]``` `` | B11  | I/O  | SPI2_CS1  | _reserved_ | SPDIF_DO  | _reserved_ | _reserved_ | _reserved_ | verify SPDIF_DO   
`[PB14 (46)``][2253]``` `` | A10  | I/O  | SPI2_CS0  | JTAG_MS0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB15 (47)``][2254]``` `` | B10  | I/O  | SPI2_CLK  | JTAG_CK0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB16 (48)``][2255]``` `` | A9  | I/O  | SPI2_MOSI  | JTAG_DO0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB17 (49)``][2256]``` `` | B9  | I/O  | SPI2_MISO  | JTAG_DI0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB18 (50)``][2257]``` `` | A8  | I/O  | [TWI1_SCK][2239] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB19 (51)``][2258]``` `` | B8  | I/O  | [TWI1_SDA][2239] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB20 (52)``][2259]``` `` | C8  | I/O  | [TWI2_SCK][2239] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB21 (53)``][2260]``` `` | C7  | I/O  | [TWI2_SDA][2239] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB22 (54)``][2261]``` `` | A7  | I/O  | UART0_TX  | IR1_TX  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PB23 (55)``][2262]``` `` | B7  | I/O  | UART0_RX  | IR1_RX  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
## Port bank C
Port Bank C (2)  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PC00 (64)``][2263]``` `` | M23  | I/O  | [NAND_WE#][2264] | SPI0_MOSI  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC01 (65)``][2265]``` `` | M22  | I/O  | [NALE][2264] | SPI0_MISO  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC02 (66)``][2266]``` `` | L23  | I/O  | [NCLE][2264] | SPI0_CLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC03 (67)``][2267]``` `` | L22  | I/O  | [NCE1][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC04 (68)``][2268]``` `` | K23  | I/O  | [NCE0][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC05 (69)``][2269]``` `` | K22  | I/O  | [NRE#][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC06 (70)``][2270]``` `` | J23  | I/O  | [NRB0][2264] | SDC2_CMD  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC07 (71)``][2271]``` `` | J22  | I/O  | [NRB1][2264] | SDC2_CLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC08 (72)``][2272]``` `` | H23  | I/O  | [NDQ0][2264] | SDC2_D0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC09 (73)``][2273]``` `` | H22  | I/O  | [NDQ1][2264] | SDC2_D1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC10 (74)``][2274]``` `` | G23  | I/O  | [NDQ2][2264] | SDC2_D2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC11 (75)``][2275]``` `` | G22  | I/O  | [NDQ3][2264] | SDC2_D3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC12 (76)``][2276]``` `` | H21  | I/O  | [NDQ4][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC13 (77)``][2277]``` `` | H20  | I/O  | [NDQ5][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC14 (78)``][2278]``` `` | G21  | I/O  | [NDQ6][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC15 (79)``][2279]``` `` | G20  | I/O  | [NDQ7][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC16 (80)``][2280]``` `` | M21  | I/O  | [NWP][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC17 (81)``][2281]``` `` | F23  | I/O  | [NCE2][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC18 (82)``][2282]``` `` | F22  | I/O  | [NCE3][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC19 (83)``][2283]``` `` | L21  | I/O  | [NCE4][2264] | SPI2_CS0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC20 (84)``][2284]``` `` | K21  | I/O  | [NCE5][2264] | SPI2_CLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC21 (85)``][2285]``` `` | J21  | I/O  | [NCE6][2264] | SPI2_MOSI  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC22 (86)``][2286]``` `` | J20  | I/O  | [NCE7][2264] | SPI2_MISO  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC23 (87)``][2287]``` `` | G19  | I/O  | _reserved_ | SPI0_CS0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PC24 (88)``][2288]``` `` | F21  | I/O  | [NDQS][2264] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
## Port bank D
Port Bank D (3)  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PD00 (96)``][2289]``` `` | AB15  | I/O  | LCD0_D0  | LVDS0_VP0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD01 (97)``][2290]``` `` | AC15  | I/O  | LCD0_D1  | LVDS0_VN0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD02 (98)``][2291]``` `` | AB14  | I/O  | LCD0_D2  | LVDS0_VP1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD03 (99)``][2292]``` `` | AC14  | I/O  | LCD0_D3  | LVDS0_VN1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD04 (100)``][2293]``` `` | AB13  | I/O  | LCD0_D4  | LVDS0_VP2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD05 (101)``][2294]``` `` | AC13  | I/O  | LCD0_D5  | LVDS0_VN2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD06 (102)``][2295]``` `` | AB12  | I/O  | LCD0_D6  | LVDS0_VPC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD07 (103)``][2296]``` `` | AC12  | I/O  | LCD0_D7  | LVDS0_VNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD08 (104)``][2297]``` `` | AB11  | I/O  | LCD0_D8  | LVDS0_VP3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD09 (105)``][2298]``` `` | AC11  | I/O  | LCD0_D9  | LVDS0_VN3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD10 (106)``][2299]``` `` | Y15  | I/O  | LCD0_D10  | LVDS1_VP0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD11 (107)``][2300]``` `` | AA15  | I/O  | LCD0_D11  | LVDS1_VN0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD12 (108)``][2301]``` `` | Y14  | I/O  | LCD0_D12  | LVDS1_VP1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD13 (109)``][2302]``` `` | AA14  | I/O  | LCD0_D13  | LVDS1_VN1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD14 (110)``][2303]``` `` | Y13  | I/O  | LCD0_D14  | LVDS1_VP2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD15 (111)``][2304]``` `` | AA13  | I/O  | LCD0_D15  | LVDS1_VN2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD16 (112)``][2305]``` `` | Y12  | I/O  | LCD0_D16  | LVDS1_VPC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD17 (113)``][2306]``` `` | AA12  | I/O  | LCD0_D17  | LVDS1_VNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD18 (114)``][2307]``` `` | Y11  | I/O  | LCD0_D18  | LVDS1_VP3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD19 (115)``][2308]``` `` | AA11  | I/O  | LCD0_D19  | LVDS1_VN3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD20 (116)``][2309]``` `` | Y10  | I/O  | LCD0_D20  | CSI1_MCLK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD21 (117)``][2310]``` `` | AA10  | I/O  | LCD0_D21  | SMC_VPPEN  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD22 (118)``][2311]``` `` | AB10  | I/O  | LCD0_D22  | SMC_VPPPP  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD23 (119)``][2312]``` `` | AC10  | I/O  | LCD0_D23  | SMC_DET  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD24 (120)``][2313]``` `` | Y9  | I/O  | LCD0_CLK  | SMC_VCCEN  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD25 (121)``][2314]``` `` | AA9  | I/O  | LCD0_DE  | SMC_RST  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD26 (122)``][2315]``` `` | AB9  | I/O  | LCD0_HSYNC  | SMC_SCK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PD27 (123)``][2316]``` `` | AC9  | I/O  | LCD0_VSYNC  | SMC_SDA  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
## Port bank E
Port Bank E (4)  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PE00 (128)``][2317]``` `` | E23  | I/O  | TS0_CLK  | CSI0_PCK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE01 (129)``][2318]``` `` | E22  | I/O  | TS0_ERR  | CSI0_CK  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE02 (130)``][2319]``` `` | D23  | I/O  | TS0_SYNC  | CSI0_HSYNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE03 (131)``][2320]``` `` | D22  | I/O  | TS0_DVLD  | CSI0_VSYNC  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE04 (132)``][2321]``` `` | C23  | I/O  | TS0_D0  | CSI0_D0  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE05 (133)``][2322]``` `` | C22  | I/O  | TS0_D1  | CSI0_D1  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE06 (134)``][2323]``` `` | B23  | I/O  | TS0_D2  | CSI0_D2  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE07 (135)``][2324]``` `` | B22  | I/O  | TS0_D3  | CSI0_D3  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE08 (136)``][2325]``` `` | A23  | I/O  | TS0_D4  | CSI0_D4  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE09 (137)``][2326]``` `` | A22  | I/O  | TS0_D5  | CSI0_D5  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE10 (138)``][2327]``` `` | B21  | I/O  | TS0_D6  | CSI0_D6  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PE11 (139)``][2328]``` `` | A21  | I/O  | TS0_D7  | CSI0_D7  | _reserved_ | _reserved_ | _reserved_ | _reserved_  
## Port bank F
Port Bank F (5)  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PF00 (160)``][2329]``` `` | M20  | I/O  | SDC0_D1  | _reserved_ | JTAG_MS1  | _reserved_ | _reserved_ | _reserved_  
`[PF01 (161)``][2330]``` `` | M19  | I/O  | SDC0_D0  | _reserved_ | JTAG_DI1  | _reserved_ | _reserved_ | _reserved_  
`[PF02 (162)``][2331]``` `` | L20  | I/O  | SDC0_CLK  | _reserved_ | UART0_TX  | _reserved_ | _reserved_ | _reserved_  
`[PF03 (163)``][2332]``` `` | L19  | I/O  | SDC0_CMD  | _reserved_ | JTAG_DO1  | _reserved_ | _reserved_ | _reserved_  
`[PF04 (164)``][2333]``` `` | K20  | I/O  | SDC0_D3  | _reserved_ | UART0_RX  | _reserved_ | _reserved_ | _reserved_  
`[PF05 (165)``][2334]``` `` | K19  | I/O  | SDC0_D2  | _reserved_ | JTAG_CK1  | _reserved_ | _reserved_ | _reserved_  
## Port bank G
Port Bank G (6)  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PG00 (192)``][2335]``` `` | F20  | I/O  | TS1_CLK  | CSI1_PCK  | SDC1_CMD  | _reserved_ | _reserved_ | _reserved_  
`[PG01 (193)``][2336]``` `` | E21  | I/O  | TS1_ERR  | CSI1_CK  | SDC1_CLK  | _reserved_ | _reserved_ | _reserved_  
`[PG02 (194)``][2337]``` `` | E20  | I/O  | TS1_SYNC  | CSI1_HSYNC  | SDC1_D0  | _reserved_ | _reserved_ | _reserved_  
`[PG03 (195)``][2338]``` `` | D21  | I/O  | TS1_DVLD  | CSI1_VSYNC  | SDC1_D1  | _reserved_ | _reserved_ | _reserved_  
`[PG04 (196)``][2339]``` `` | D20  | I/O  | TS1_D0  | CSI1_D0  | SDC1_D2  | CSI0_D8  | _reserved_ | _reserved_  
`[PG05 (197)``][2340]``` `` | C21  | I/O  | TS1_D1  | CSI1_D1  | SDC1_D3  | CSI0_D9  | _reserved_ | _reserved_  
`[PG06 (198)``][2341]``` `` | E19  | I/O  | TS1_D2  | CSI1_D2  | UART3_TX  | CSI0_D10  | _reserved_ | _reserved_  
`[PG07 (199)``][2342]``` `` | C20  | I/O  | TS1_D3  | CSI1_D3  | UART3_RX  | CSI0_D11  | _reserved_ | _reserved_  
`[PG08 (200)``][2343]``` `` | D19  | I/O  | TS1_D4  | CSI1_D4  | UART3_RTS  | CSI0_D12  | _reserved_ | _reserved_  
`[PG09 (201)``][2344]``` `` | C19  | I/O  | TS1_D5  | CSI1_D5  | UART3_CTS  | CSI0_D13  | _reserved_ | _reserved_  
`[PG10 (202)``][2345]``` `` | D18  | I/O  | TS1_D6  | CSI1_D6  | UART4_TX  | CSI0_D14  | _reserved_ | _reserved_  
`[PG11 (203)``][2346]``` `` | C18  | I/O  | TS1_D7  | CSI1_D7  | UART4_RX  | CSI0_D15  | _reserved_ | _reserved_  
## Port bank H
Port Bank H (7)  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PH00 (224)``][2347]``` `` | A6  | I/O  | LCD1_D00  | _reserved_ | UART3_TX  | _reserved_ | EINT0  | CSI1_D0   
`[PH01 (225)``][2348]``` `` | B6  | I/O  | LCD1_D01  | _reserved_ | UART3_RX  | _reserved_ | EINT1  | CSI1_D1   
`[PH02 (226)``][2349]``` `` | C6  | I/O  | LCD1_D02  | _reserved_ | UART3_RTS  | _reserved_ | EINT2  | CSI1_D2   
`[PH03 (227)``][2350]``` `` | A5  | I/O  | LCD1_D03  | _reserved_ | UART3_CTS  | _reserved_ | EINT3  | CSI1_D3   
`[PH04 (228)``][2351]``` `` | B5  | I/O  | LCD1_D04  | _reserved_ | UART4_TX  | _reserved_ | EINT4  | CSI1_D4   
`[PH05 (229)``][2352]``` `` | C5  | I/O  | LCD1_D05  | _reserved_ | UART4_RX  | _reserved_ | EINT5  | CSI1_D5   
`[PH06 (230)``][2353]``` `` | A4  | I/O  | LCD1_D06  | _reserved_ | UART5_TX  | MS_BS  | EINT6  | CSI1_D6   
`[PH07 (231)``][2354]``` `` | B4  | I/O  | LCD1_D07  | _reserved_ | UART5_RX  | MS_CLK  | EINT7  | CSI1_D7   
`[PH08 (232)``][2355]``` `` | C4  | I/O  | LCD1_D08  | [ERXD3][2215] | KP_IN0  | MS_D1  | EINT8  | CSI1_D9   
`[PH09 (233)``][2356]``` `` | D4  | I/O  | LCD1_D09  | [ERXD2][2215] | KP_IN1  | MS_D0  | EINT9  | CSI1_D8   
`[PH10 (234)``][2357]``` `` | A3  | I/O  | LCD1_D10  | [ERXD1][2215] | KP_IN2  | MS_D2  | EINT10  | CSI1_D10   
`[PH11 (235)``][2358]``` `` | B3  | I/O  | LCD1_D11  | [ERXD0][2215] | KP_IN3  | MS_D3  | EINT11  | CSI1_D11   
`[PH12 (236)``][2359]``` `` | C3  | I/O  | LCD1_D12  | _reserved_ | PS2_SCK1  | _reserved_ | EINT12  | CSI1_D12   
`[PH13 (237)``][2360]``` `` | A2  | I/O  | LCD1_D13  | _reserved_ | PS2_SDA1  | SMC_RST  | EINT13  | CSI1_D13   
`[PH14 (238)``][2361]``` `` | B2  | I/O  | LCD1_D14  | [ETXD3][2215] | KP_IN4  | SMC_VPPEN  | EINT14  | CSI1_D14   
`[PH15 (239)``][2362]``` `` | A1  | I/O  | LCD1_D15  | [ETXD2][2215] | KP_IN5  | SMC_VPPPP  | EINT15  | CSI1_D15   
`[PH16 (240)``][2363]``` `` | B1  | I/O  | LCD1_D16  | [ETXD1][2215] | KP_IN6  | _reserved_ | EINT16  | CSI1_D16   
`[PH17 (241)``][2364]``` `` | C1  | I/O  | LCD1_D17  | [ETXD0][2215] | KP_IN7  | SMC_VCCEN  | EINT17  | CSI1_D17   
`[PH18 (242)``][2365]``` `` | C2  | I/O  | LCD1_D18  | [ERXCK][2215] | KP_OUT0  | SMC_SCK  | EINT18  | CSI1_D18   
`[PH19 (243)``][2366]``` `` | D1  | I/O  | LCD1_D19  | [ERXERR][2215] | KP_OUT1  | SMC_SDA  | EINT19  | CSI1_D19   
`[PH20 (244)``][2367]``` `` | D2  | I/O  | LCD1_D20  | [ERXDV][2215] | CAN_TX  | _reserved_ | EINT20  | CSI1_D20   
`[PH21 (245)``][2368]``` `` | D3  | I/O  | LCD1_D21  | [EMDC][2215] | CAN_RX  | _reserved_ | EINT21  | CSI1_D21   
`[PH22 (246)``][2369]``` `` | E1  | I/O  | LCD1_D22  | [EMDIO][2215] | KP_OUT2  | SDC1_CMD  | _reserved_ | CSI1_D22   
`[PH23 (247)``][2370]``` `` | E2  | I/O  | LCD1_D23  | [ETEN][2215] | KP_OUT3  | SDC1_CLK  | _reserved_ | CSI1_D23   
`[PH24 (248)``][2371]``` `` | E3  | I/O  | LCD1_CLK  | [ETXCK][2215] | KP_OUT4  | SDC1_D0  | _reserved_ | CSI1_FIELD   
`[PH25 (249)``][2372]``` `` | E4  | I/O  | LCD1_DE  | [ECRS][2215] | KP_OUT5  | SDC1_D1  | _reserved_ | CSI1_PCLK   
`[PH26 (250)``][2373]``` `` | F3  | I/O  | LCD1_HSYNC  | [ECOL][2215] | KP_OUT6  | SDC1_D2  | _reserved_ | CSI1_HSYNC   
`[PH27 (251)``][2374]``` `` | F4  | I/O  | LCD1_VSYNC  | [ETXERR][2215] | KP_OUT7  | SDC1_D3  | _reserved_ | CSI1_VSYNC   
## Port bank I
Port Bank I (8)  
---  
Port | Ball | Type | MUX 2 | MUX 3 | MUX 4 | MUX 5 | MUX 6 | MUX 7   
`[PI00 (256)``][2375]``` `` | A20  | I/O  | _reserved_ | [TWI TWI3_SCK][2376] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI01 (257)``][2377]``` `` | B20  | I/O  | _reserved_ | [TWI TWI3_SDA][2378] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI02 (258)``][2379]``` `` | A19  | I/O  | _reserved_ | [TWI TWI4_SCK][2380] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI03 (259)``][2381]``` `` | B19  | I/O  | [PWM1][2382] | [TWI TWI4_SDA][2383] | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI04 (260)``][2384]``` `` | A18  | I/O  | [SDC3_CMD][2385] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI05 (261)``][2386]``` `` | B18  | I/O  | [SDC3_CLK][2385] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI06 (262)``][2387]``` `` | A17  | I/O  | [SDC3_D0][2385] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI07 (263)``][2388]``` `` | B17  | I/O  | [SDC3_D1][2385] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI08 (264)``][2389]``` `` | A16  | I/O  | [SDC3_D2][2385] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI09 (265)``][2390]``` `` | B16  | I/O  | [SDC3_D3][2385] | _reserved_ | _reserved_ | _reserved_ | _reserved_ | _reserved_  
`[PI10 (266)``][2391]``` `` | C17  | I/O  | [SPI0_CS0][2392] | [UART5_TX][2393] | _reserved_ | _reserved_ | EINT22  | _reserved_  
`[PI11 (267)``][2394]``` `` | D17  | I/O  | [SPI0_CLK][2392] | [UART5_RX][2393] | _reserved_ | _reserved_ | EINT23  | _reserved_  
`[PI12 (268)``][2395]``` `` | C16  | I/O  | [SPI0_MOSI][2392] | [UART6_TX][2393] | CLK_OUT_A  | _reserved_ | EINT24  | _reserved_  
`[PI13 (269)``][2396]``` `` | D16  | I/O  | [SPI0_MISO][2392] | [UART6_RX][2393] | CLK_OUT_B  | _reserved_ | EINT25  | _reserved_  
`[PI14 (270)``][2397]``` `` | C15  | I/O  | [SPI0_CS1][2392] | [PS2_SCK1][2398] | TCLKIN0  | TCLKIN0  | EINT26  | _reserved_  
`[PI15 (271)``][2399]``` `` | D15  | I/O  | [SPI1_CS1][2392] | [PS2_SDA1][2398] | TCLKIN1  | TCLKIN1  | EINT27  | _reserved_  
`[PI16 (272)``][2400]``` `` | E17  | I/O  | [SPI1_CS0][2392] | [UART2_RTS][2393] | _reserved_ | _reserved_ | EINT28  | _reserved_  
`[PI17 (273)``][2401]``` `` | E16  | I/O  | [SPI1_CLK][2392] | [UART2_CTS][2393] | _reserved_ | _reserved_ | EINT29  | _reserved_  
`[PI18 (274)``][2402]``` `` | E15  | I/O  | [SPI1_MOSI][2392] | [UART2_TX][2393] | _reserved_ | _reserved_ | EINT30  | _reserved_  
`[PI19 (275)``][2403]``` `` | D14  | I/O  | [SPI1_MISO][2392] | [UART2_RX][2393] | _reserved_ | _reserved_ | EINT31  | _reserved_  
`[PI20 (276)``][2404]``` `` | E14  | I/O  | [PS2_SCK0][2398] | [UART7_TX][2393] | HSCL  | _reserved_ | _reserved_ | _reserved_  
`[PI21 (277)``][2405]``` `` | E13  | I/O  | [PS2_SDA0][2398] | [UART7_RX][2393] | HSDA  | _reserved_ | _reserved_ | _reserved_  
## Other Pins
Port | Ball | Function | Type   
---|---|---|---  
`XP_TP` | Y22 | Output | AI   
`XN_TP` | AA22 | Output | AI   
`YP_TP` | Y23 | Output | AI   
`YN_TP` | AA23 | Output | AI   
## See also
  * [A20][2199]
  * [A10/PIO][2406]
  * [A13/PIO][2407]
