# A80/Memory map
< [A80][4531]
 
ARM Core can access to control registers and physical memories over global memory space described here: 
# Memory Map
## CPU Memory space
Start  | End  | Size  | Name  | Short description  | sun9i   
---|---|---|---|---|---  
`0x00000000` | `0x00007fff` | `32KiB` | [BROM][4534] | Boot Read Only Memory  | Y   
`0x00008000` | `0x0000ffff` | `32KiB` | [BROM][4534] | Boot Read Only Memory  | Y   
`0x00010000` | `0x00019fff` | `40KiB` | [SRAM A1][4535] | Fast onchip Static Ram, Bank A1  | Y   
`0x08100000` | `0x08127fff` | `160KiB` | [SRAM A2][4535] | Fast onchip Static Ram, Bank A2 (shared with embedded processor)  | Y   
`0x00020000` | `0x0005ffff` | `256KiB` | [SRAM B][4535] | Fast onchip Static Ram, Bank B (stated as 'secure' on the datasheet)  | Y   
`0x01d00000` | `0x01dfffff` | `1MiB` | [SRAM A4][4535] | Fast onchip Static Ram, Bank C  | Y   
`0x01400000` | `0x0141ffff` | `64kiB` | [CoreSight Config registers][4536] | CoreSight Debug Module  | Y   
AHB0 devices   
`0x01c02000` | `0x01c02fff` | `4 KiB` | [SS Config registers][4537] | Security System   
`0x01c03000` | `0x01c03fff` | `4KiB` | [NFC0 Config registers][4538] | Nand Flash Controller 0  | Y   
`0x01c04000` | `0x01c04fff` | `4KiB` | [NFC1 Config registers][4538] | Nand Flash Controller 1  | Y   
`0x01c06000` | `0x01c06fff` | `4KiB` | [TS Config registers][4539] | Transport Stream controller (DVB)  | Y   
`0x01c08000` | `0x01c08fff` | `4KiB` | GPU Control registers  | GPU Control  | Y   
`0x01c09000` | `0x01c09fff` | `4KiB` | GTBUS Config registers  | GTBUS  | Y   
`0x01c0a000` | `0x01c0afff` | `4KiB` | [SATA Config registers][4540] | Serial AT Attachment  | Y   
`0x01c0e000` | `0x01c0efff` | `4KiB` | [SID Config registers][4541] | Secure ID  | Y   
`0x01c0f000` | `0x01c0ffff` | `4KiB` | [MMC0 Config registers][4542] | MultiMedia Controller 0 (SD Card)  | Y   
`0x01c10000` | `0x01c10fff` | `4KiB` | [MMC1 Config registers][4542] | MultiMedia Controller 1 (SD Card)  | Y   
`0x01c11000` | `0x01c11fff` | `4KiB` | [MMC2 Config registers][4542] | MultiMedia Controller 2 (SD Card)  | Y   
`0x01c12000` | `0x01c12fff` | `4KiB` | [MMC3 Config registers][4542] | MultiMedia Controller 3 (SD Card)  | Y   
`0x01c1a000` | `0x01c1afff` | `4KiB` | [SPI0 Config registers][4543] | Serial Peripheral Interface Bus 0  | Y   
`0x01c1b000` | `0x01c1bfff` | `4KiB` | [SPI1 Config registers][4543] | Serial Peripheral Interface Bus 1  | Y   
`0x01c1c000` | `0x01c1cfff` | `4KiB` | [SPI2 Config registers][4543] | Serial Peripheral Interface Bus 2  | Y   
`0x01c1d000` | `0x01c1dfff` | `4KiB` | [SPI3 Config registers][4543] | Serial Peripheral Interface Bus 3  | Y   
`0x01c1f000` | `0x01c1ffff` | `4KiB` | MIPI HSI Config registers  | MIPI HSI  | Y   
`0x01c40000` | `0x01c47fff` | `32KiB` | [A20/GIC/GIC][4544] | ARM Generic Interrupt Controller  | Y   
`0x01c62000` | `0x01c62fff` | `4KiB` | DRAMCOM  | DRAMCOM  | Y   
`0x01c63000` | `0x01c63fff` | `4KiB` | DRAMCTRL0  | DRAMCTRL0  | Y   
`0x01c64000` | `0x01c64fff` | `4KiB` | DRAMCTRL1  | DRAMCTRL1  | Y   
`0x01c65000` | `0x01c65fff` | `4KiB` | DRAMPHY0  | DRAMPHY0  | Y   
`0x01c66000` | `0x01c66fff` | `4KiB` | DRAMPHY1  | DRAMPHY1  | Y   
`0x01c90000` | `0x01c90fff` | `4KiB` | CCI400  | CCI400  | Y   
AHB1 Devices   
`0x00800000` | `0x00800fff` | `4KiB` | [SRAM Config registers][4535] | Fast onchip Static Ram Controller  | Y   
`0x00801000` | `0x00801fff` | `4KiB` | [HSTimer][4545] | High-Speed Timer  | Y   
`0x00802000` | `0x00802fff` | `4KiB` | [DMA Config registers][4546] | DMA  | Y   
`0x00803000` | `0x00803fff` | `4KiB` | MSGBOX Config registers  | Message box interface to embedded core  | Y   
`0x00804000` | `0x00804fff` | `4KiB` | [SPINLOCK Config registers][4547] | Hardware spinlock shared with embedded core  | Y   
`0x00805000` | `0x00805fff` | `4KiB` | [TZASC Config registers][4548] | TrustZone Address Space Controller  | Y   
`0x00830000` | `0x00830fff` | `4KiB` | [GMAC][4549] | Gigabit Media Access Control  | Y   
`0x00900000` | `0x009fffff` | `?KiB` | USB 3.0 OTG  | USB 3.0 OTG controller (likely dwc3)  | Y   
`0x00a00000` | `0x00a00fff` | `4KiB` | USB0 Config registers  | Universal Serial Bus 0 (HCI)  | Y   
`0x00a01000` | `0x00a01fff` | `4KiB` | USB1 Config registers  | Universal Serial Bus 1 (HCI)  | Y   
`0x00a02000` | `0x00a02fff` | `4KiB` | USB2 Config registers  | Universal Serial Bus 2 (HCI)  | Y   
`0x00a08000` | `0x00a08fff` | `4KiB` | [USB Control registers][4550] | Universal Serial Bus SIE/PHY clocks, resets, and controls  | Y   
AHB2 Devices   
`0x03000000` | `0x03000fff` | `4KiB` | DE SYS  | Display Engine SYS  | Y   
`0x03000000` | `0x03000fff` | `4KiB` | DISP SYS  | Display SYS  | Y   
`0x03100000` | `0x0311ffff` | `128KiB` | [DE_FE 0 Config registers][4551] | Display Engine FrontEnd 0  | Y   
`0x03140000` | `0x0315ffff` | `128KiB` | [DE_FE 1 Config registers][4551] | Display Engine FrontEnd 1  | Y   
`0x03180000` | `0x0319ffff` | `128KiB` | [DE_FE 2 Config registers][4551] | Display Engine FrontEnd 2  | Y   
`0x03200000` | `0x0321ffff` | `128KiB` | [DE_BE 0 Config registers][4552] | Display Engine BackEnd 0  | Y   
`0x03240000` | `0x0325ffff` | `128KiB` | [DE_BE 1 Config registers][4552] | Display Engine BackEnd 1  | Y   
`0x03280000` | `0x0329ffff` | `128KiB` | [DE_BE 2 Config registers][4552] | Display Engine BackEnd 2  | Y   
`0x03300000` | `0x0331ffff` | `128KiB` | DEU 0 Config registers  | DEU 0  | Y   
`0x03340000` | `0x0335ffff` | `128KiB` | DEU 1 Config registers  | DEU 1  | Y   
`0x03400000` | `0x0341ffff` | `128KiB` | DRC 0 Config registers  | DRC 0  | Y   
`0x03440000` | `0x0345ffff` | `128KiB` | DRC 1 Config registers  | DRC 1  | Y   
`0x03800000` | `0x03800fff` | `4KiB` | [CSI0 Config registers][4553] | Camera Sensor Interface 0  | Y   
`0x03801000` | `0x03801fff` | `4KiB` | MIPI CSI0 Config registers  | MIPI Camera Sensor Interface 0  | Y   
`0x03802000` | `0x03802fff` | `4KiB` | MIPI CSI0 PHY Config registers  | MIPI Camera Sensor Interface 0 PHY  | Y   
`0x03803000` | `0x03803fff` | `4KiB` | CSI0 CCI registers  | CSI0 CCI  | Y   
`0x03808000` | `0x03808fff` | `4KiB` | ISP Config registers  | HawkView ISP (Camera Image Signal Processor)  | Y   
`0x03900000` | `0x03900fff` | `4KiB` | [CSI1 Config registers][4553] | Camera Sensor Interface 1  | Y   
`0x03903000` | `0x03903fff` | `4KiB` | CSI0 CCI registers  | CSI0 CCI  | Y   
`0x03a00000` | `0x03a00fff` | `4KiB` | FD IO registers  | FD  | Y   
`0x03a01000` | `0x03a01fff` | `4KiB` | FD memory  | FD  | Y   
`0x03a4e000` | `0x03a4efff` | `4KiB` | [VE Config registers][4554] | Video Engine  | Y   
`0x03c00000` | `0x03c00fff` | `4KiB` | [LCD0 Config registers][4555] | Liquid Crystal Display controller 0  | Y   
`0x03c10000` | `0x03c10fff` | `4KiB` | [LCD1 Config registers][4555] | Liquid Crystal Display controller 1  | Y   
`0x03c20000` | `0x03c20fff` | `4KiB` | [LCD1 Config registers][4555] | Liquid Crystal Display controller 2  | Y   
`0x03c40000` | `0x03c400ff` | `4KiB` | MIPI DSI0 Config registers  | MIPI Display Serial Interface 0  | Y   
`0x03c40100` | `0x03c401ff` | `4KiB` | MIPI DSI0 PHY Config registers  | MIPI Display Serial Interface 0 PHY  | Y   
`0x03d00000` | `0x03d00fff` | `4KiB` | [HDMI Config registers][4556] | High-Definition Multimedia Interface  | Y   
`0x03f00000` | `0x03f1ffff` | `128KiB` | [MP Config registers][4557] | Mixer Processor  | Y   
APB0 Devices   
`0x06000000` | `0x060007ff` | `2KiB` | [CCM Config registers][4558] | Clock Control Module  | Y   
`0x06000800` | `0x06000bff` | `1KiB` | [PIO Config registers][4559] | Programmable Input Output  | Y   
`0x06000c00` | `0x06000dff` | `512B` | Timer Config registers  | Timers  | Y   
`0x06001000` | `0x060013ff` | `1KiB` | [SPDIF Config registers][4560] | Sony Philips Digital InterFace  | Y   
`0x06001400` | `0x060015ff` | `512B` | [PWM Config registers][4561] | Pulse Width Modulation  | Y   
`0x06001800` | `0x06001bff` | `1KiB` | [LRADC Config registers][4562] | Low Resolution Analog Digital Converter 0 and 1  | Y   
`0x06001c00` | `0x06001fff` | `1KiB` | [AC97 Config registers][4563] | Audio Codec 1997  | Y   
`0x06002000` | `0x060023ff` | `1KiB` | [IIS0 Config registers][4564] | Integrated Interchip Sound 0 (I2S)  | Y   
`0x06002400` | `0x060027ff` | `1KiB` | [IIS1 Config registers][4564] | Integrated Interchip Sound 1 (I2S)  | Y   
`0x06003000` | `0x060033ff` | `1KiB` | Timer Watchdog Config registers  | Timer Watchdog  | Y   
`0x06003400` | `0x060037ff` | `1KiB` | [TZPC Config registers][4565] | TrustZone Protection Controller  | Y   
`0x06003c00` | `0x06003fff` | `1KiB` | [SJTAG Config registers][4566] | Secure JTAG  | Y   
`0x06004400` | `0x060047ff` | `1KiB` | Consumer InfraRed TX Config registers  | Consumer InfraRed TX  | Y   
`0x06004c00` | `0x06004fff` | `1KiB` | GPADC Config registers  | General Purpose ADC  | Y   
APB1 Devices   
`0x07000000` | `0x070003ff` | `1KiB` | [UART0 Config registers][4567] | Universal Asynchronous Receiver/Transmitter 0  | Y   
`0x07000400` | `0x070007ff` | `1KiB` | [UART1 Config registers][4567] | Universal Asynchronous Receiver/Transmitter 1  | Y   
`0x07000800` | `0x07000bff` | `1KiB` | [UART2 Config registers][4567] | Universal Asynchronous Receiver/Transmitter 2  | Y   
`0x07000c00` | `0x07000fff` | `1KiB` | [UART3 Config registers][4567] | Universal Asynchronous Receiver/Transmitter 3  | Y   
`0x07001000` | `0x070013ff` | `1KiB` | [UART4 Config registers][4567] | Universal Asynchronous Receiver/Transmitter 4  | Y   
`0x07001000` | `0x070017ff` | `1KiB` | [UART5 Config registers][4567] | Universal Asynchronous Receiver/Transmitter 5  | Y   
`0x07002800` | `0x07002bff` | `1KiB` | [TWI0 Config registers][4568] | Two Wire Interface 0  | Y   
`0x07002c00` | `0x07002fff` | `1KiB` | [TWI1 Config registers][4568] | Two Wire Interface 1  | Y   
`0x07003000` | `0x070033ff` | `1KiB` | [TWI2 Config registers][4568] | Two Wire Interface 2  | Y   
`0x07003400` | `0x070037ff` | `1KiB` | [TWI3 Config registers][4568] | Two Wire Interface 3  | Y   
`0x07003800` | `0x07003bff` | `1KiB` | [TWI4 Config registers][4568] | Two Wire Interface 4  | Y   
CPUS (R block) Devices   
`0x08000800` | `0x08000bff` | `1KiB` | R_Timer Config registers  | R block Timer  | Y   
`0x08000c00` | `0x08000fff` | `1KiB` | R_NVIC Config registers  | R_NVIC  | Y   
`0x08001000` | `0x080013ff` | `1KiB` | R_Watchdog Config registers  | R block Watchdog  | Y   
`0x08001400` | `0x080017ff` | `1KiB` | R_PRCM Config registers  | Power, Reset, Clock management  | Y   
`0x08001c00` | `0x08001fff` | `1KiB` | R_CNT Config registers  | R_CNT  | Y   
`0x08002000` | `0x080023ff` | `1KiB` | R_CIR_RX Config registers  | R block Consumer IR receiver  | Y   
`0x08002400` | `0x080027ff` | `1KiB` | [R_TWI0 Config registers][4568] | R block Two Wire Interface 0  | Y   
`0x08002800` | `0x08002bff` | `1KiB` | R_UART Config registers  | R_UART  | Y   
`0x08002c00` | `0x08002fff` | `1KiB` | [R_PIO Config registers][4569] | R block Pin Controller  | Y   
`0x08003000` | `0x080033ff` | `1KiB` | R_ONE_WIRE Config registers  | R block One Wire interface  | Y   
`0x08003400` | `0x080037ff` | `1KiB` | R_RSB Config registers  | R block Reduced Serial Bus  | Y   
`0x08003800` | `0x08003bff` | `1KiB` | [R_TWI1 Config registers][4568] | R block Two Wire Interface 1  | Y   
`0x08004000` | `0x080043ff` | `1KiB` | R_PS2_0 Config registers  | R block PS/2 interface 0  | Y   
`0x08004400` | `0x080047ff` | `1KiB` | R_PS2_1 Config registers  | R block PS/2 interface 1  | Y   
`0x08006000` | `0x08006fff` | `4KiB` | R_DAUDIO_0 Config registers  | R block Integrated Interchip Sound 2 (I2S) / PCM interface 0  | Y   
`0x08007000` | `0x08007fff` | `4KiB` | R_DAUDIO_1 Config registers  | R block Integrated Interchip Sound 2 (I2S) / PCM interface 1  | Y   
`0x08008000` | `0x08008fff` | `4KiB` | R_DMA Config registers  | R block DMA controller  | Y   
Memory   
`0x20000000` | `0x21fffffff` | `4GiB` | [DDR-II/DDR-III][4570] | General memory space  | Y
