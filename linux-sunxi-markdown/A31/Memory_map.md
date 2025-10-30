# A31/Memory map
< [A31][3060]
 
ARM Core can access to control registers and physical memories over global memory space described here: 
# Memory Map
## CPU Memory space
Start  | End  | Size  | Name  | Short description  | sun6i  | sun8i   
---|---|---|---|---|---|---  
`0x00000000` | `0x00003fff` | `16KiB` | [SRAM A1][3063] | Fast onchip Static Ram, Bank A1  | Y  | Y   
`0x00004000` | `0x0000ffff` | `48KiB` | [VE SRAM][3063] | Fast onchip Static Ram, For VE  | Y  | Y   
`0x00010000` | `0x00010fff` | `4KiB` | [SRAM D][3063] | Fast onchip Static Ram, Bank D  | Y  |   
`0x00020000` | `0x0002ffff` | `64KiB` | [SRAM B][3063] | Fast onchip Static Ram, Bank B (Secure)  | Y  |   
`0x00044000` | `0x00053fff` | `64KiB` | [SRAM A2][3063] | Fast onchip Static Ram, Bank A2, shared with OpenRISC core  | Y  | Y   
`0x01c00000` | `0x01c00fff` | `4KiB` | [SRAM Config registers][3063] | Fast onchip Static Ram Controller  | Y  | Y   
`0x01c02000` | `0x01c02fff` | `4KiB` | [DMA Config registers][3064] | DMA  | Y  | Y   
`0x01c03000` | `0x01c03fff` | `4KiB` | [NFC0 Config registers][3065] | Nand Flash Controller  | Y  | Y   
`0x01c04000` | `0x01c04fff` | `4KiB` | [TS Config registers][3066] | Transport Stream controller (DVB)  | Y  |   
`0x01c05000` | `0x01c05fff` | `4KiB` | [NFC1 Config registers][3065] | Nand Flash Controller  | Y  | Y   
`0x01c0c000` | `0x01c0cfff` | `4KiB` | [LCD0 Config registers][3067] | Liquid Crystal Display controller 0  | Y  | Y   
`0x01c0d000` | `0x01c0dfff` | `4KiB` | [LCD1 Config registers][3067] | Liquid Crystal Display controller 1  | Y  | N   
`0x01c0e000` | `0x01c0efff` | `4KiB` | [VE Config registers][3068] | Video Engine  | Y  | Y   
`0x01c0f000` | `0x01c0ffff` | `4KiB` | [MMC0 Config registers][3069] | MultiMedia Controller 0 (SD Card)  | Y  | Y   
`0x01c10000` | `0x01c10fff` | `4KiB` | [MMC1 Config registers][3069] | MultiMedia Controller 1 (SD Card)  | Y  | Y   
`0x01c11000` | `0x01c11fff` | `4KiB` | [MMC2 Config registers][3069] | MultiMedia Controller 2 (SD Card)  | Y  | Y   
`0x01c12000` | `0x01c12fff` | `4KiB` | [MMC3 Config registers][3069] | MultiMedia Controller 3 (SD Card)  | Y  |   
`0x01c15000` | `0x01c15fff` | `4KiB` | [SS Config registers][3070] | Security System  | Y  | Y   
`0x01c16000` | `0x01c16fff` | `4KiB` | [HDMI Config registers][3071] | High-Definition Multimedia Interface  | Y  |   
`0x01c17000` | `0x01c17fff` | `4KiB` | MSGBOX Config registers  | Message box interface to OpenRISC core  | Y  | Y   
`0x01c18000` | `0x01c18fff` | `4KiB` | [SPINLOCK Config registers][3072] | Hardware spinlock  | Y  | Y   
`0x01c19000` | `0x01c19fff` | `4KiB` | [USB0 Config registers][3073] | Universal Serial Bus 0 (OTG)  | Y  | Y   
`0x01c1a000` | `0x01c1afff` | `4KiB` | [USB1 Config registers][3073] | Universal Serial Bus 1 (HCI)  | Y  | Y   
`0x01c1b000` | `0x01c1bfff` | `4KiB` | [USB2 Config registers][3073] | Universal Serial Bus 2 (HCI)  | Y  |   
`0x01c1c000` | `0x01c1cfff` | `4KiB` | [USB2 Config registers][3073] | Universal Serial Bus 3 (OHCI only)  | Y  |   
`0x01c1e000` | `0x01c1efff` | `4KiB` | [TZASC Config registers][3074] | Trust Zone Access Space Controller  | Y  |   
`0x01c20000` | `0x01c203ff` | `1KiB` | [CCM Config registers][3075] | Clock Control Module  | Y  | Y   
`0x01c20800` | `0x01c20bff` | `1KiB` | [PIO Config registers][3076] | Programmable Input Output  | Y  | Y   
`0x01c20c00` | `0x01c20fff` | `1KiB` | [Timer Config registers][3077] | Timers  | Y  | Y   
`0x01c21000` | `0x01c213ff` | `1KiB` | [SPDIF Config registers][3078] | Sony Philips Digital InterFace  | Y  |   
`0x01c21400` | `0x01c217ff` | `1KiB` | [PWM Config registers][3079] | Pulse Width Modulation  | Y  | Y   
`0x01c22000` | `0x01c223ff` | `1KiB` | [IIS0 Config registers][3080] | Integrated Interchip Sound 0 (I2S)  | Y  | Y   
`0x01c24000` | `0x01c247ff` | `1KiB` | [IIS1 Config registers][3080] | Integrated Interchip Sound 1 (I2S)  | Y  | Y   
`0x01c22800` | `0x01c22bff` | `1KiB` | [LRADC Config registers][3081] | Low Resolution Analog Digital Converter 0 and 1  | Y  | Y   
`0x01c22c00` | `0x01c22fff` | `1KiB` | [AD/DA][3082] | Digital Analog and Digital Analog converters  | Y  | Y   
`0x01c23000` | `0x01c233ff` | `1KiB` | [Keypad Config registers][3083] | Keyboard controller  | Y  |   
`0x01c23400` | `0x01c237ff` | `1KiB` | [TZPC Config registers][3084] | TrustZone Protection Controller  | Y  |   
`0x01c23800` | `0x01c23bff` | `1KiB` | [SID Config registers][3085] | Secure ID  | Y  |   
`0x01c23c00` | `0x01c23fff` | `1KiB` | [SJTAG Config registers][3086] | Secure JTAG  | Y  |   
`0x01c25000` | `0x01c253ff` | `1KiB` | [TP Config registers][3087] | Resitive Touch Panel controller  | Y  |   
`0x01c25000` | `0x01c253ff` | `1KiB` | GPADC Config registers  | Temperature Sensor controller  |  | Y   
`0x01c25400` | `0x01c257ff` | `1KiB` | DMIC  | ?  | Y  |   
`0x01c28000` | `0x01c283ff` | `1KiB` | [UART0 Config registers][3088] | Universal Asynchronous Receiver/Transmitter 0  | Y  | Y   
`0x01c28400` | `0x01c287ff` | `1KiB` | [UART1 Config registers][3088] | Universal Asynchronous Receiver/Transmitter 1  | Y  | Y   
`0x01c28800` | `0x01c28bff` | `1KiB` | [UART2 Config registers][3088] | Universal Asynchronous Receiver/Transmitter 2  | Y  | Y   
`0x01c28c00` | `0x01c28fff` | `1KiB` | [UART3 Config registers][3088] | Universal Asynchronous Receiver/Transmitter 3  | Y  | Y   
`0x01c29000` | `0x01c293ff` | `1KiB` | [UART4 Config registers][3088] | Universal Asynchronous Receiver/Transmitter 4  | Y  | Y   
`0x01c29400` | `0x01c297ff` | `1KiB` | [UART5 Config registers][3088] | Universal Asynchronous Receiver/Transmitter 5  | Y  |   
`0x01c2ac00` | `0x01c2afff` | `1KiB` | [TWI0 Config registers][3089] | Two Wire Interface 0  | Y  | Y   
`0x01c2b000` | `0x01c2b3ff` | `1KiB` | [TWI1 Config registers][3089] | Two Wire Interface 1  | Y  | Y   
`0x01c2b400` | `0x01c2b7ff` | `1KiB` | [TWI2 Config registers][3089] | Two Wire Interface 2  | Y  | Y   
`0x01c2b800` | `0x01c2bbff` | `1KiB` | [TWI3 Config registers][3089] | Two Wire Interface 3  | Y  |   
`0x01c30000` | `0x01c3ffff` | `64KiB` | [GMAC][3090] | Gigabit Media Access Control  | Y  |   
`0x01c40000` | `0x01c4ffff` | `64KiB` | [Mali 400 Config registers][3091] | Arm Mali 400 GPU  | Y  | Y   
`0x01c60000` | `0x01c60fff` | `4KiB` | [HSTimer][3092] | High-Speed Timer  | Y  | Y   
`0x01c62000` | `0x01c62fff` | `4KiB` | DRAMCOM Config registers  | DRAM related  | Y  | Y   
`0x01c63000` | `0x01c63fff` | `4KiB` | DRAMCTL0 Config registers  | DRAM Controller 0  | Y  | Y   
`0x01c64000` | `0x01c64fff` | `4KiB` | DRAMCTL1 Config registers  | DRAM Controller 1  | Y  |   
`0x01c65000` | `0x01c65fff` | `4KiB` | DRAMPHY0 Config registers  | DRAM PHY 0  | Y  | Y   
`0x01c66000` | `0x01c66fff` | `4KiB` | DRAMCTL1 Config registers  | DRAM PHY 1  | Y  |   
`0x01c68000` | `0x01c68fff` | `4KiB` | [SPI0 Config registers][3093] | Serial Peripheral Interface Bus 0  | Y  | Y   
`0x01c69000` | `0x01c69fff` | `4KiB` | [SPI1 Config registers][3093] | Serial Peripheral Interface Bus 1  | Y  | Y   
`0x01c6a000` | `0x01c6afff` | `4KiB` | [SPI2 Config registers][3093] | Serial Peripheral Interface Bus 0  | Y  |   
`0x01c6b000` | `0x01c6bfff` | `4KiB` | [SPI3 Config registers][3093] | Serial Peripheral Interface Bus 1  | Y  |   
`0x01c80000` | `0x01c80fff` | `4KiB` | SCU Config registers  | ARM Snoop Control Unit?  | Y  | Y   
`0x01c81000` | `0x01c81fff` | `4KiB` | [GIC Distributor Interface registers][3094] | ARM Generic Interrupt Controller  | Y  | Y   
`0x01c82000` | `0x01c82fff` | `4KiB` | [GIC CPU Interface registers][3094] | ARM Generic Interrupt Controller  | Y  | Y   
`0x01ca0000` | `0x01ca0fff` | `4KiB` | MIPI DSI0 Config registers  | MIPI Display Serial Interface 0  | Y  | Y   
`0x01ca1000` | `0x01ca1fff` | `4KiB` | MIPI DSI0 PHY Config registers  | MIPI Display Serial Interface 0 PHY  | Y  | Y   
`0x01cb0000` | `0x01cb0fff` | `4KiB` | [CSI0 Config registers][3095] | Camera Serial Interface 0  | Y  | Y   
`0x01cb1000` | `0x01cb1fff` | `4KiB` | MIPI CSI0 Config registers  | MIPI Camera Serial Interface 0  | Y  |   
`0x01cb2000` | `0x01cb2fff` | `4KiB` | MIPI CSI0 PHY Config registers  | MIPI Camera Serial Interface 0 PHY  | Y  |   
`0x01cb3000` | `0x01cb3fff` | `4KiB` | [CSI1 Config registers][3095] | Camera Serial Interface 1  | Y  |   
`0x01cb8000` | `0x01cb????` | `??? KiB` | ISP Config registers  | HawkView ISP (Camera Image Signal Processor)  | Y  |   
`0x01cc0000` | `0x01cc????` | `??? KiB` | ISP Memory  | HawkView ISP (Camera Image Signal Processor)  | Y  |   
`0x01d00000` | `0x01dfffff` | `1MiB` | [SRAM C][3096] | Fast onchip Static Ram, Bank C  | Y  |   
`0x01e00000` | `0x01e1ffff` | `128KiB` | [DE_FE 0 Config registers][3097] | Display Engine FrontEnd 0  | Y  | Y   
`0x01e20000` | `0x01e3ffff` | `128KiB` | [DE_FE 1 Config registers][3097] | Display Engine FrontEnd 1  | Y  |   
`0x01e40000` | `0x01e4ffff` | `128KiB` | [DE_BE 0 Config registers][3098] | Display Engine BackEnd 1  | Y  |   
`0x01e50000` | `0x01e5ffff` | `64KiB` | [IEP1 Config registers][3099] | Image Enhancement Processor  | Y  |   
`0x01e60000` | `0x01e6ffff` | `64KiB` | [DE_BE 0 Config registers][3098] | Display Engine BackEnd 0  | Y  | Y   
`0x01e70000` | `0x01e7ffff` | `64KiB` | [IEP0 Config registers][3099] | Image Enhancement Processor  | Y  | Y   
`0x01e80000` | `0x01e9ffff` | `128KiB` | [MP Config registers][3100] | Mixer Processor  | Y  |   
`0x01ea0000` | `0x01eaffff` | `64KiB` | DEU1 Config registers  | ?  | Y  |   
`0x01eb0000` | `0x01ebffff` | `64KiB` | DEU0 Config registers  | ?  | Y  |   
`0x01ef0000` | `0x01efffff` | `64KiB` | PS  | ?  | Y  |   
`0x01f00000` | `0x01f003ff` | `1KiB` | RTC Config registers  | Real Time Clock  | Y  | Y   
`0x01f00800` | `0x01f00bff` | `1KiB` | R_Timer Config registers  | RTC block Timer  | Y  | Y   
`0x01f00c00` | `0x01f00fff` | `1KiB` | R_INTC Config registers  | RTC block Interrupt Controller (NMI)  | Y  | Y   
`0x01f01000` | `0x01f013ff` | `1KiB` | R_WDOG Config registers  | RTC block Watchdog  | Y  | Y   
`0x01f01400` | `0x01f017ff` | `1KiB` | [R_PRCM Config registers][3101] | RTC block Power, Reset & Clock Management  | Y  | Y   
`0x01f01c00` | `0x01f01fff` | `1KiB` | R_CPUCFG Config registers  | RTC block CPU Config registers  | Y  | Y   
`0x01f02000` | `0x01f023ff` | `1KiB` | R_CIR Config registers  | RTC block Consumer InfraRed Controller  | Y  |   
`0x01f02400` | `0x01f027ff` | `1KiB` | [R_TWI Config registers][3089] | RTC block Two Wire Interface Controller  | Y  | Y   
`0x01f02800` | `0x01f02bff` | `1KiB` | [R_UART Config registers][3088] | RTC block Universal Asynchronous Receiver/Transmitter  | Y  | Y   
`0x01f02c00` | `0x01f02fff` | `1KiB` | [R_PIO Config registers][3101] | RTC block PIO controller  | Y  | Y   
`0x01f03000` | `0x01f033ff` | `1KiB` | R_ONE_WIRE Config registers  | RTC block One Wire Interface Controller  | Y  |   
`0x01f03400` | `0x01f037ff` | `1KiB` | R_P2WI Config registers  | RTC block Push-Pull 2 Wire Interface Controller  | Y  |   
`0x01f03400` | `0x01f037ff` | `1KiB` | R_RSB Config registers  | RTC block Reduced Serial Bus Interface Controller  |  | Y   
`0x3f500000` | `0x3f50ffff` | `64kiB` | [CoreSight Config registers][3102] | CoreSight Debug Module  | Y  | Y   
`0x3f506000` | `0x3f506fff` | `4kiB` | TSGEN Readonly registers  |  | Y  | Y   
`0x3f507000` | `0x3f507fff` | `4kiB` | TSGEN Config registers  |  | Y  | Y   
`0x40000000` | `0xbfffffff` | `2GiB` | [DDR-II/DDR-III][3103] | General memory space  | Y  | Y   
`0xc0000000` | `0xfffdffff` | `64KiB` |   
`0xffff0000` | `0xffff7fff` | `32KiB` | [BROM][3104] | Boot Read Only Memory  | Y  | Y   
`0xffff8000` | `0xffffffff` | `32KiB` |   
## External references
