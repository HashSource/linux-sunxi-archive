# Cubieboard/ExpansionPorts
< [Cubieboard][13657]
 
## Expansion ports
These tables shows the available expansion ports, their pin assignments and available functions. We have tried to only list those functions which makes sense, omitting details on functions where not all needed signals are exposed in the pin headers. 
Note: Each Pxnn pin is also GPIO capable even if not explicitly mentioned in the tables. 
  

### rev 2012-08-08 and 2012-09-09
Two 2x24 2.0mm male headers. 
U14 (Next to SATA connector)  
---  
LCD   
1 | [PD0][13660] (LCDD0/LVDSP0) | 2 | _Ground_  
3 | [PD2][13661] (LCDD2/LVDS0P1) | 4 | [PD1][13662] (LCDD1/LVDS0N0)  
5 | [PD4][13663] (LCDD4/LNVS0P2) | 6 | [PD3][13664] (LCDD3/LVDS0N1)  
7 | [PD6][13665] (LCDD6/LVDS0PC) | 8 | [PD5][13666] (LCDD5/LVDS0N2)  
9 | _Ground_ | 10 | [PD7][13667] (LCDD7/LVDS0NC)  
11 | [PD9][13668] (LCDD9/LVDS0N3) | 12 | [PD8][13669] (LCDD8/LVDS0P3)  
13 | [PD11][13670] (LCDD11/LVDS1N0) | 14 | [PD10][13671] (LCDD10/LVDS1P0)  
15 | [PD13][13672] (LCDD13/LVDS1N1) | 16 | [PD12][13673] (LCDD12/LVDS1P1)  
17 | [PD15][13674] (LCDD15/LVDS1N2) | 18 | [PD14][13675] (LCDD14/LVDS1P2)  
19 | [PD16][13676] (LCDD16/LVDS1PC) | 20 | _Ground_  
21 | [PD18][13677] (LCDD18/LVDS1P3) | 22 | [PD17][13678] (LCDD17/LVDS1NC)  
23 | [PD20][13679] (LCDD20) | 24 | [PD19][13680] (LCDD19/LVDS1N3)  
25 | [PD22][13681] (LCDD22) | 26 | [PD21][13682] (LCDD21)  
27 | [PD27][13683] (LCDVSYNC)-VGA-VSYNC | 28 | [PD23][13684] (LCDD23)  
29 | [PD24][13685] (LCDCLK) | 30 | [PD26][13686] (LCDHSYNC)-VGA-HSYNC  
31 | [PB2][13687] (PWM0) | 32 | [PD25][13688] (LCDDE)  
33 | [YP_TP][13689] (TP-Y1) | 34 | [XP_TP][13690] (TP-X1)  
35 | [YN_TP][13691] (TP-Y2) | 36 | [XN_TP][13692] (TP-X2)  
37 | [PH7][13693] (LCD0-BL-EN/LCD-PIO0/UART5-RX/EINT7) | 38 | _Ground_  
39 | [PB11][13694] (LCD0-SDA/LCD-PIO2) | 40 | [PB10][13695] (LCD0-SCK/LCD-PIO1)  
41 | SPDIF  | 42 | _Ground_  
43 | VCC-5V  | 44 | 3.3V (_nc_ in 2012-08-08)  
SPI0   
45 | [PI10][13696] (SPI0-CS/UART5-TX/EINT22) | 46 | [PI12][13697] (SPI0-MOSI/UART6-TX/EINT24)  
47 | [PI11][13698] (SPI0-CLK/UART5-RX/EINT23) | 48 | [PI13][13699] (SPI0-MISO/UART6-RX/EINT25)  
U15 (Between Ethernet port and USB ports)  
---  
CSI1/TS   
1 | VCC-5V  | 2 | [PH15][13700] (CSI1-PWR/EINT15)  
3 | CSI1-IO-2V8  | 4 | [PH14][13701] (CSI1-RST#/EINT14)  
5 | [PG0][13702] (CSI1-PCLK/SDC1-CMD) | 6 | [PB18][13703] (TWI1-SCK)  
7 | [PB19][13704] (TWI1-SDA) | 8 | [PG3][13705] (CSI1-VSYNC/SDC1-D1)  
9 | [PG2][13706] (CSI1-HSYNC/SDC1-D0) | 10 | [PG1][13707] (CSI1-MCLK/SDC1-CLK)  
11 | [PG4][13708] (CSI1-D0/SDC1-D2) | 12 | [PG5][13709] (CSI1-D1/SDC1-D3)  
13 | [PG6][13710] (CSI1-D2/UART3-TX) | 14 | [PG7][13711] (CSI1-D3/UART3-RX)  
15 | [PG8][13712] (CSI1-D4/UART3-RTS) | 16 | [PG9][13713] (CSI1-D5/UART3-CTS)  
17 | [PG10][13714] (CSI1-D6/UART4-TX) | 18 | [PG11][13715] (CSI1-D7/UART4-RX)  
19 | _Ground_ | 20 | _Ground_  
Analog  | SDIO3   
21 | FMINL  | 22 | [PI4][13716] (SDC3-CMD)  
23 | FMINR  | 24 | [PI5][13717] (SDC3-CLK)  
25 | _Ground_ | 26 | [PI6][13718] (SDC3-D0)  
27 | VGA-R  | 28 | [PI7][13719] (SDC3-D1)  
29 | VGA-G  | 30 | [PI8][13720] (SDC3-D2)  
31 | VGA-B  | 32 | [PI9][13721] (SDC3-D3)  
| CSI0/TS   
33 | LCD1-VSYNC  | 34 | [PE4][13722] (CSI0-D0)  
35 | LCD1-HSYNC  | 36 | [PE5][13723] (CSI0-D1)  
37 | _Ground_ | 38 | [PE6][13724] (CSI0-D2)  
39 | AVCC  | 40 | [PE7][13725] (CSI0-D3)  
41 | LRADC0  | 42 | [PE8][13726] (CSI0-D4)  
43 | CVBS  | 44 | [PE9][13727] (CSI0-D5)  
45 | HPL  | 46 | [PE10][13728] (CSI0-D6)  
47 | HPR  | 48 | [PE11][13729] (CSI0-D7)
