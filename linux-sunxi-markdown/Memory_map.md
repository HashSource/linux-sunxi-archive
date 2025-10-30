# Memory map
ARM Core can access control registers and physical memories over global memory space described here: 
# Memory Map
## CPU Memory space
Start  | End  | Size  | Name  | Short description  | sun4i  | sun5i  | sun7i   
---|---|---|---|---|---|---|---  
`0x00000000` | `0x00003fff` | `16KiB` | [SRAM A1][37478] | Fast onchip Static Ram, Blank A1  | Y  | Y  | Y   
`0x00004000` | `0x00007fff` | `16KiB` | [SRAM A2][37478] | Fast onchip Static Ram, Blank A2  | Y  | Y  | Y   
`0x00008000` | `0x0000b3ff` | `13KiB` | [SRAM A3][37478] | Fast onchip Static Ram, Blank A3  | Y  | Y  | Y   
`0x0000b400` | `0x0000bfff` | `3KiB` | [SRAM A4][37478] | Fast onchip Static Ram, Blank A4  | Y  | Y  | Y   
`0x00010000` | `0x00010fff` | `4KiB` | [SRAM D][37478] | Fast onchip Static Ram, Bank D  | Y  | Y  | Y   
`0x00020000` | `0x0002ffff` | `64KiB` | [SRAM B][37478] | Fast onchip Static Ram, Bank B  | Y  | Y  | Y   
`0x01c00000` | `0x01c00fff` | `4KiB` | [SRAM Config registers][37478] | Fast onchip Static Ram Controller  | Y  | Y  | Y   
`0x01c01000` | `0x01c01fff` | `4KiB` | [DRAM Config registers][37479] | DRAM memory controller  | Y  | Y  | Y   
`0x01c02000` | `0x01c02fff` | `4KiB` | [DMA Config registers][37480] | DMA  | Y  | Y  | Y   
`0x01c03000` | `0x01c03fff` | `4KiB` | [NFC Config registers][37481] | Nand Flash Controller  | Y  | Y  | Y   
`0x01c04000` | `0x01c04fff` | `4KiB` | [TS Config registers][37482] | Transport Stream controller (DVB)  | Y  |  | Y   
`0x01c05000` | `0x01c05fff` | `4KiB` | [SPI0 Config registers][37483] | Serial Peripheral Interface Bus 0  | Y  | Y  | Y   
`0x01c06000` | `0x01c06fff` | `4KiB` | [SPI1 Config registers][37483] | Serial Peripheral Interface Bus 1  | Y  | Y  | Y   
`0x01c07000` | `0x01c07fff` | `4KiB` | [MS Config registers][37484] | Memory Stick  | Y  |  | Y   
`0x01c08000` | `0x01c08fff` | `4KiB` | [TVD Config registers][37485] | TV Decoder  | Y  |  | Y   
`0x01c09000` | `0x01c09fff` | `4KiB` | [CSI0 Config registers][37486] | Camera Serial Interface 0  | Y  |  | Y   
`0x01c0a000` | `0x01c0afff` | `4KiB` | [TVE0 Config registers][37487] | TV Encoder 0  | Y  |  | Y   
`0x01c0b000` | `0x01c0bfff` | `4KiB` | [EMAC Config registers][37488] | Ethernet Media Access Control  | Y  |  | Y   
`0x01c0c000` | `0x01c0cfff` | `4KiB` | [LCD0 Config registers][37489] | Liquid Crystal Display controller 0  | Y  |  | Y   
`0x01c0d000` | `0x01c0dfff` | `4KiB` | [LCD1 Config registers][37489] | Liquid Crystal Display controller 1  | Y  |  | Y   
`0x01c0e000` | `0x01c0efff` | `4KiB` | [VE Config registers][37490] | Video Engine  | Y  | Y  | Y   
`0x01c0f000` | `0x01c0ffff` | `4KiB` | [MMC0 Config registers][37491] | MultiMedia Controller 0 (SD Card)  | Y  |  | Y   
`0x01c10000` | `0x01c10fff` | `4KiB` | [MMC1 Config registers][37491] | MultiMedia Controller 1 (SD Card)  | Y  |  | Y   
`0x01c11000` | `0x01c11fff` | `4KiB` | [MMC2 Config registers][37491] | MultiMedia Controller 2 (SD Card)  | Y  |  | Y   
`0x01c12000` | `0x01c12fff` | `4KiB` | [MMC3 Config registers][37491] | MultiMedia Controller 3 (SD Card)  | Y  |  | Y   
`0x01c13000` | `0x01c13fff` | `4KiB` | [USB0 Config registers][37492] | Universal Serial Bus 0 (OTG)  | Y  |  | Y   
`0x01c14000` | `0x01c14fff` | `4KiB` | [USB1 Config registers][37492] | Universal Serial Bus 1 (HCI)  | Y  |  | Y   
`0x01c15000` | `0x01c15fff` | `4KiB` | [SS Config registers][37493] | Security System  | Y  |  | Y   
`0x01c16000` | `0x01c16fff` | `4KiB` | [HDMI Config registers][37494] | High-Definition Multimedia Interface  | Y  |  | Y   
`0x01c17000` | `0x01c17fff` | `4KiB` | [SPI2 Config registers][37483] | Serial Peripheral Interface Bus 2  | Y  |  | Y   
`0x01c18000` | `0x01c18fff` | `4KiB` | [SATA Config registers][37495] | Serial AT Attachment  | Y  |  | Y   
`0x01c19000` | `0x01c19fff` | `4KiB` | [PATA Config registers][37496] | Parallel AT Attachment  | Y  |  | Y   
`0x01c1a000` | `0x01c1afff` | `4KiB` | [ACE Config registers][37497] | Audio Codec Engine  | Y  |  | Y   
`0x01c1b000` | `0x01c1bfff` | `4KiB` | [TVE1 Config registers][37487] | TV Encoder 1  | Y  |  | Y   
`0x01c1c000` | `0x01c1cfff` | `4KiB` | [USB2 Config registers][37492] | Universal Serial Bus 2 (HCI)  | Y  |  | Y   
`0x01c1d000` | `0x01c1dfff` | `4KiB` | [CSI1 Config registers][37486] | Camera Serial Interface 1  | Y  |  | Y   
`0x01c1e000` | `0x01c1efff` | `4KiB` | [TZASC Config registers][37498] | Trust Zone Access Space Controller  | Y  |  | Y   
`0x01c1f000` | `0x01c1ffff` | `4KiB` | [SPI3 Config registers][37483] | Serial Peripheral Interface Bus 3  | Y  |  | Y   
`0x01c20000` | `0x01c203ff` | `1KiB` | [CCM Config registers][37499] | Clock Control Module  | Y  |  | Y   
`0x01c20400` | `0x01c207ff` | `1KiB` | [IRQ Config registers][37500] | Interrupt Controller  | Y  | Y  | N   
`0x01c20800` | `0x01c20bff` | `1KiB` | [PIO Config registers][37501] | Programmable Input Output  | Y  |  | Y   
`0x01c20c00` | `0x01c20dff` | `512B` | [Timer Config registers][37502] CPUCFG is also here  | Timers  | Y  |  | Y   
`0x01c20e00` | `0x01c20fff` | `512B` | [PWM Config registers][37503] | Pulse Width Modulation  | Y  |  | Y   
`0x01c21000` | `0x01c213ff` | `1KiB` | [SPDIF Config registers][37504] | Sony Philips Digital InterFace  | Y  |  | Y   
`0x01c21400` | `0x01c217ff` | `1KiB` | [AC97 Config registers][37505] | Audio Codec 1997  | Y  |  | Y   
`0x01c21800` | `0x01c21bff` | `1KiB` | [IR0 Config registers][37506] | InfraRed 0  | Y  |  | Y   
`0x01c21c00` | `0x01c21fff` | `1KiB` | [IR1 Config registers][37506] | InfraRed 1  | Y  |  | Y   
`0x01c22000` | `0x01c223ff` | `1KiB` | [IIS1 Config registers][37507] | Integrated Interchip Sound 1 (I2S)  | Y  |  | Y   
`0x01c24000` | `0x01c247ff` | `1KiB` | [IIS0 Config registers][37507] | Integrated Interchip Sound 0 (I2S)  | Y  |  | Y   
`0x01c22800` | `0x01c22bff` | `1KiB` | [LRADC Config registers][37508] | Low Resolution Analog Digital Converter 0 and 1  | Y  |  | Y   
`0x01c22c00` | `0x01c22fff` | `1KiB` | [AD/DA][37509] | Digital Analog and Digital Analog converters  | Y  |  | Y   
`0x01c23000` | `0x01c233ff` | `1KiB` | [Keypad Config registers][37510] | Keyboard controller  | Y  |  | Y   
`0x01c23400` | `0x01c237ff` | `1KiB` | [TZPC Config registers][37511] | TrustZone Protection Controller  | Y  |  | Y   
`0x01c23800` | `0x01c23bff` | `1KiB` | [SID Config registers][37512] | Secure ID  | Y  | Y  | Y   
`0x01c23c00` | `0x01c23fff` | `1KiB` | [SJTAG Config registers][37513] | Secure JTAG  | Y  |  | Y   
`0x01c24000` | `0x01c243ff` | `1KiB` | Reserved   
`0x01c24400` | `0x01c247ff` | `1KiB` | [IIS2 Config registers][37507] | Integrated Interchip Sound 2 (I2S)  |  |  | Y   
`0x01c24800` | `0x01c24bff` | `1KiB` | ?  |   
`0x01c24c00` | `0x01c24fff` | `1KiB` | ?  |   
`0x01c25000` | `0x01c253ff` | `1KiB` | [TP Config registers][37514] | Resitive Touch Panel controller  | Y  |  | Y   
`0x01c25400` | `0x01c257ff` | `1KiB` | [PMU Config registers][37515] | Power Management Unit  | Y  |  | Y   
`0x01c25800` | `0x01c25bff` | `1KiB` | ?  |   
`0x01c25c00` | `0x01c25fff` | `1KiB` | [CPU Config registers][37516] | CPU Configuration (SMP)  | N  | N  | Y   
`0x01c25600` | `0x01c27fff` | `10KiB` |   
`0x01c28000` | `0x01c283ff` | `1KiB` | [UART0 Config registers][37517] | Universal Asynchronous Receiver/Transmitter 0  | Y  | Y  | Y   
`0x01c28400` | `0x01c287ff` | `1KiB` | [UART1 Config registers][37517] | Universal Asynchronous Receiver/Transmitter 1  | Y  |  | Y   
`0x01c28800` | `0x01c28bff` | `1KiB` | [UART2 Config registers][37517] | Universal Asynchronous Receiver/Transmitter 2  | Y  |  | Y   
`0x01c28c00` | `0x01c28fff` | `1KiB` | [UART3 Config registers][37517] | Universal Asynchronous Receiver/Transmitter 3  | Y  |  | Y   
`0x01c29000` | `0x01c293ff` | `1KiB` | [UART4 Config registers][37517] | Universal Asynchronous Receiver/Transmitter 4  | Y  |  | Y   
`0x01c29000` | `0x01c297ff` | `1KiB` | [UART5 Config registers][37517] | Universal Asynchronous Receiver/Transmitter 5  | Y  |  | Y   
`0x01c29800` | `0x01c29bff` | `1KiB` | [UART6 Config registers][37517] | Universal Asynchronous Receiver/Transmitter 6  | Y  |  | Y   
`0x01c29c00` | `0x01c29fff` | `1KiB` | [UART7 Config registers][37517] | Universal Asynchronous Receiver/Transmitter 7  | Y  |  | Y   
`0x01c2a000` | `0x01c2a3ff` | `1KiB` | [PS/2 0 Config registers][37518] | Personal System/2 0  | Y  |  | Y   
`0x01c2a400` | `0x01c2a7ff` | `1KiB` | [PS/2 1 Config registers][37518] | Personal System/2 1  | Y  |  | Y   
`0x01c2a800` | `0x01c2abff` | `1KiB` |   
`0x01c2ac00` | `0x01c2afff` | `1KiB` | [TWI0 Config registers][37519] | Two Wire Interface 0  | Y  |  | Y   
`0x01c2b000` | `0x01c2b3ff` | `1KiB` | [TWI1 Config registers][37519] | Two Wire Interface 1  | Y  |  | Y   
`0x01c2b400` | `0x01c2b7ff` | `1KiB` | [TWI2 Config registers][37519] | Two Wire Interface 2  | Y  |  | Y   
`0x01c2b800` | `0x01c2bbff` | `1KiB` | [TWI3 Config registers][37519] | Two Wire Interface 3  | N?  |  | Y   
`0x01c2bc00` | `0x01c2bfff` | `1KiB` | [CAN0 Config registers][37520] | Controller Area Network 0  | Y  |  | Y   
`0x01c2c000` | `0x01c2c3ff` | `1KiB` | [CAN1 Config registers][37520] | Controller Area Network 1  | Y  |  | N   
`0x01c2c000` | `0x01c2c3ff` | `1KiB` | [TWI4 Config registers][37519] | Two Wire Interface 4  | N  |  | Y   
`0x01c2c400` | `0x01c2c7ff` | `1KiB` | [SCR Config registers][37521] | SmartCard Reader  | Y  |  | Y   
`0x01c2c800` | `0x01c2ffff` | `14KiB` | Reserved   
`0x01c30000` | `0x01c3ffff` | `64KiB` | [GPS Config registers][37522] | Global Positioning System  | Y  |  | Y   
`0x01c40000` | `0x01c4ffff` | `64KiB` | [Mali 400 Config registers][37523] | Arm Mali 400 GPU  | Y  | Y  | Y   
`0x01c50000` | `0x01c5ffff` | `64KiB` | [GMAC][37524] | Gigabit Media Access Control  | N  | N  | Y   
`0x01c60000` | `0x01c60fff` | `4KiB` | [HSTimer][37525] | High-Speed Timer  | N  | Y  | Y   
`0x01c61000` | `0x01c8ffff` | `128KiB` | reserved   
`0x01c80000` | `0x01c87fff` | `32KiB` | [A20/GIC/GIC][37526] | ARM Generic Interrupt Controller  | N  | N  | Y   
`0x01ce0000` | `0x01cfffff` | `128KiB` | [A20/HDMI/HDMI][37527] | High-Definition Multimedia Interface (likly CEC, Net etc)  |  |  | Y   
`0x01d00000` | `0x01dfffff` | `1MiB` | [SRAM C][37528] | Fast onchip Static Ram, Blank C  | Y  | Y  | Y   
`0x01e00000` | `0x01e1ffff` | `128KiB` | [DE_FE 0 Config registers][37529] | Display Engine FrontEnd 0  | Y  | Y  | Y   
`0x01e20000` | `0x01e3ffff` | `128KiB` | [DE_FE 1 Config registers][37529] | Display Engine FrontEnd 1  | Y  | n  | Y   
`0x01e40000` | `0x01e5ffff` | `128KiB` | [DE_BE 1 Config registers][37530] | Display Engine BackEnd 1  | Y  | N  | Y   
`0x01e60000` | `0x01e7ffff` | `128KiB` | [DE_BE 0 Config registers][37530] | Display Engine BackEnd 0  | Y  | Y  | Y   
`0x01e70000` | `0x01e8ffff` | `64KiB` | [IEP Config registers][37531] | Image Enhancement Processor  | N  | Y  | N   
`0x01e80000` | `0x01e9ffff` | `128KiB` | [MP Config registers][37532] | Mixer Processor  | Y  | Y  | Y   
`0x01ea0000` | `0x01ebffff` | `128KiB` | [AVG Config registers][37533] | Automatic Voltage Gain?  | Y  | N  | Y   
`0x01ec0000` | `0x3f4fffff` | `1005824KiB` | Reserved   
`0x3f500000` | `0x3f50ffff` | `64kiB` | [CoreSight Config registers][37534] | CoreSight Debug Module  | Y  | Y  | Y   
`0x3f501000` | `0x3f501fff` | `4kiB` | [CPUBIST Config registers][37535] | CPU Build In Test  | Y  | Y  | Y   
`0x3f510000` | `0x3fffffff` | `11468800KiB` | Reserved   
`0x40000000` | `0xbfffffff` | `2GiB` | [DDR-II/DDR-III][37536] | General memory space  | Y  | Y  | Y   
`0xc0000000` | `0xfffdffff` | `64KiB` |   
`0xffff0000` | `0xffff7fff` | `32KiB` | [BROM][37537] | Boot Read Only Memory  | Y  | Y  | Y   
`0xffff8000` | `0xffffffff` | `32KiB` |   
## External references
  * [A10 register guide][37538] ([RhombusTech's Wiki][37539])
  * [u-boot-sunxi][37540]
  * [linux-sunxi][37541]
