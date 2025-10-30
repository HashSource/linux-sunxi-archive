# Xunlong Orange Pi PC 2
(Redirected from [Orange Pi PC 2][42906])
 
Xunlong Orange Pi PC 2  
---  
[![OPi PC 2 Top small.jpg][42909]][42910]  
Manufacturer |  [OrangePi][42911]  
Dimensions |  85 _mm_ x 55 _mm_  
Release Date |  November 2016   
Website |  [Orange Pi PC 2 Product Page][42912]  
Specifications   
SoC |  Allwinner [H5][42913] @ 1.3Ghz   
DRAM |  1GiB DDR3   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive)  
or via GPIO header pins   
Features   
Video |  HDMI 1.4 (HDCP, CEC), CVBS   
Audio |  3.5 mm Jack, HDMI, Microphone   
Network |  10/100/1000Mbps Ethernet ([Realtek RTL8211E][42914])   
Storage |  µSD, 16Mbit NOR Flash on board ([MX25L1606E][42915])   
USB |  3 USB 2.0 Host, 1 USB 2.0 OTG   
Other |  [CIR][42916]  
Headers |  3 pin UART, CSI, 40 pin GPIO   
The Orange Pi PC 2, manufactured by [Xunlong][42917], is an [H5][42913] [Allwinner SoC Family][42918] based 64-bit quad-core single-board computer. It was the first single-board computer from Xunlong to feature the [Allwinner][42919] [H5][42913]. It features Allwinner H5 quad core Cortex A53 processor, Mali-450MP4 GPU, 1GB DDR3 RAM, 3x USB 2.0 slots, 1x USB OTG port, Micro SD card slot, HDMI out, 3.5mm audio/video jack, Built-in microphone, Gigabit Ethernet, 40-pin GPIO header, IR receiver, Power button and Power and status LEDs. 
## Contents
  * [1 Identification][42920]
  * [2 Sunxi support][42921]
    * [2.1 Current status][42922]
    * [2.2 BSP][42923]
    * [2.3 Manual build][42924]
      * [2.3.1 U-Boot][42925]
        * [2.3.1.1 Mainline U-Boot][42926]
      * [2.3.2 Linux Kernel][42927]
        * [2.3.2.1 Sunxi/Legacy Kernel][42928]
        * [2.3.2.2 Mainline kernel][42929]
  * [3 Expansion Port][42930]
  * [4 Tips, Tricks, Caveats][42931]
    * [4.1 FEL mode activation][42932]
      * [4.1.1 UBOOT Switch][42933]
    * [4.2 PWR/KEYADC External Interrupt Switch][42934]
    * [4.3 LEDs][42935]
    * [4.4 Universal Serial Bus][42936]
    * [4.5 Audio/Video Output][42937]
    * [4.6 Camera Serial Interface][42938]
    * [4.7 Consumer Infrared Receiver][42939]
    * [4.8 Microphone][42940]
    * [4.9 CPU clock speed limit][42941]
  * [5 Adding a serial port][42942]
    * [5.1 Locating the UART][42943]
  * [6 Pictures][42944]
  * [7 Variants][42945]
  * [8 Also known as][42946]
  * [9 See also][42947]
    * [9.1 Manufacturer images][42948]
  * [10 References][42949]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    Orange Pi PC 2 V1.1
[/code]
# Sunxi support
## Current status
The H5 SoC support has matured since its introduction in kernel 4.12. Most of the board functionality for boards such as Orange Pi PC 2, including 3D graphics, hardware accelerated video and crypto, and DVFS are available with current mainline kernels. Only a very few minor features are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][42950]. 
See the [Manual build][42924] section for more details. 
  

## BSP
There are some somewhat abandoned 3.10 BSP code drops available in 'OrangePiLibra' and FriendlyELEC's github repos. Check the [orangepi-xunlong][42951] and [OrangePiLibra][42952] repositories in case of interest. 
It seems no device settings are contained and the BSP is broken anyway at least with regard to voltage regulation (that's also the reason vendor OS images seem to be limited to 1008 MHz since at this cpufreq those Orange Pi do not immediately crash with BSP kernel). 
## Manual build
You can build things for yourself by following our [Manual build howto][42953] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **orangepi_pc2_defconfig** (supported since v2017.05) build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
The H5 SoC has support in the [mainline kernels][42954]. 
The development process, links to patches and links to kernel fork repositories are listed on the [ Linux mainlining effort][42954] page. Patches can also be found from the arm-linux mailing list. 
Repositories with H5 patches: 
  * [Ondřej Jirman's branch for H5 based orange Pi (kernel 4.19)][42955] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)

  
Use the **sun50i-h5-orangepi-pc2.dtb** device-tree binary. 
# Expansion Port
The Orange Pi PC 2 has a 40-pin, 0.1" connector with several low-speed interfaces. To learn about accessing the GPIO pins through sysfs with mainline kernel read [GPIO][42956]  

2x20 Header   
---  
1 | _3.3V_ | 2 | _5V_  
3 | PA12 (TWI0_SDA/DI_RX/PA_EINT12) | 4 | _5V_  
5 | PA11 (TWI0_SCK/DI_TX/PA_EINT11) | 6 | _GND_  
7 | PA6 (SIM_PWREN/PWM1/PA_EINT6) | 8 | PC5 (NAND_RE/SDC2_CLK)  
9 | _GND_ | 10 | PC6 (NAND_RB0/SDC2_CMD)  
11 | PA1 (UART2_RX/JTAG_CK0/PA_EINT1) | 12 | PD14 (RGMII_NULL/MII_TXERR/RMII_NULL)  
13 | PA0 (UART2_TX/JTAG_MS0/PA_EINT0) | 14 | _GND_  
15 | PA3 (UART2_CTS/JTAG_DI0/PA_EINT3) | 16 | PC4 (NAND_CE0)  
17 | _3.3V_ | 18 | PC7 (NAND_RB1)  
19 | PA15 (SPI1_MOSI/UART3_RTS/PA_EINT15) | 20 | _GND_  
21 | PA16 (SPI1_MISO/UART3_CTS/PA_EINT16) | 22 | PA2 (UART2_RTS/JTAG_DO0/PA_EINT2)  
23 | PA14 (SPI1_CLK/UART3_RX/PA_EINT14) | 24 | PA13 (SPI1_CS/UART3_TX/PA_EINT13)  
25 | _GND_ | 26 | PA21 (PCM0_DIN/SIM_VPPPP/PA_EINT21)  
27 | PA19 (PCM0_CLK/TWI1_SDA/PA_EINT19) | 28 | PA18 (PCM0_SYNC/TWI1_SCK/PA_EINT18)  
29 | PA7 (SIM_CLK/PA_EINT7) | 30 | _GND_  
31 | PA8 (SIM_DATA/PA_EINT8) | 32 | PG8 (UART1_RTS/PG_EINT8)  
33 | PA9 (SIM_RST/PA_EINT9) | 34 | _GND_  
35 | PA10 (SIM_DET/PA_EINT10) | 36 | PG9 (UART1_CTS/PG_EINT9)  
37 | PD11 (RGMII_NULL/MII_CRS/RMII_NULL) | 38 | PG6 (UART1_TX/PG_EINT6)  
39 | _GND_ | 40 | PG7 (UART1_RX/PG_EINT7)  
# Tips, Tricks, Caveats
## FEL mode activation
FEL is a low-level subroutine contained in the BootROM on Allwinner devices. It is used for initial programming and recovery of devices using USB.  
There is no FEL button on this board. Booting without an SD card automagically enters FEL mode. 
[code] 
    ./sunxi-fel version
    AWUSBFEX soc=00001718(H5) 00000001 ver=0001 44 08 scratchpad=00017e00 00000000 00000000
[/code]
### UBOOT Switch
There is no accessible UBOOT switch or connector. However, UBOOT is pulled up by a 47Kohm resistor (R124) which is located between microUSB connector (CN1) and H5 SoC (U1) near the two status LEDs; you'll need to solder a switch from the GND test point near pin 5 of the GPIO connector (CON3) to the side of R124 not connected to the RTC test point (3.3V), which is next to the Vacc test point. So it's possible to solder in a switch to pull UBOOT low to reboot your board into FEL mode: 
  * 0: U_Boot
  * 1: Normal Boot

## PWR/KEYADC External Interrupt Switch
The board has a momentary action switch (SW4) located on the lower left corner near the 5V DC IN power jack (J1), which pulls low PL3 (R_PL_EINT external interrupt - #77, vectored to 0x0134) and KEYADC (interrupt #62 vectored to 0x00F8). 
## LEDs
The board has two LEDs mid-way between the Micro USB jack (CN1) and the H5 SoC (U1): 
  * A red PWR LED, D7, connected to the PL10 pin.
  * A green STATUS LED, D8, connected to the PA20 pin.

## Universal Serial Bus
  * Universal Serial Bus On The Go: USB0 port on H5 SoC is accessed via the microUSB connector (CN1) on the left hand edge of the board. The USB OTG is a Dual-Role Device controller, which supports both device and host functions which can also be configured as a Host-only or Device-only controller, fully compliant with the USB 2.0 Specification. It can support high-speed (HS, 480-Mbps), full-speed (FS, 12-Mbps), and low-speed (LS, 1.5-Mbps) transfers in Host mode. It can support high-speed (HS, 480-Mbps), and full-speed (FS, 12-Mbps) in Device mode.

  * USB Host Controller 1: USB1 and USB3 ports on H5 SoC is accessed via the dual USB A stacked connector (USB1) on the bottom right hand side of the PC2. It is fully compliant with the USB 2.0 specification, Enhanced Host Controller Interface (EHCI) Specification, Revision 1.0, and the Open Host Controller Interface (OHCI) Specification Release 1.0a. The controller supports high-speed, 480-Mbps transfers (40 times faster than USB 1.1 full-speed mode) using an EHCI Host Controller, as well as full and low speeds through one or more integrated OHCI Host Controllers.

  * USB Host Controller 2: USB2 port on H5 SoC is accessed via the vertical USB A connector (P1) on the right hand side of the PC2. It is fully compliant with the USB 2.0 specification, Enhanced Host Controller Interface (EHCI) Specification, Revision 1.0, and the Open Host Controller Interface (OHCI) Specification Release 1.0a. The controller supports high-speed, 480-Mbps transfers (40 times faster than USB 1.1 full-speed mode) using an EHCI Host Controller, as well as full and low speeds through one or more integrated OHCI Host Controllers.

USB Host Register base addresses are: USB_HCI1 at 0x01C1B000; USB_HCI2 at 0x01C1C000; and USB_HCI3 at 0x01C1D000 
## Audio/Video Output
The PC2 board has a 3.5mm Audio-Video (AV) jack (J4), located to the right of the HDMI connector and the two stacked USB ports. The AV jack outputs both Left and Right audio channels and a Color, Video, Blanking and Sync (CVBS) composite TV (up to 480p/576p NTSC/PAL signal from the H5 SoC TCON1 module. 
## Camera Serial Interface
The PC2 has a Camera Serial Interface (CSI) interface connector (CON1) located between the microUSB connector (CN1) and the Reset switch (SW4) on the laft hand side of the board. The CSI supports 8-bit yuv422 CMOS sensor interface and CCIR656 protocol for NTSC and PAL with maximum still capture resolution to 5M pixels and maximum video capture resolution to 1080 at 30fps. The CSI camera connector (CON1) is a 24-pin FPC connector which can connect directly with an external camera module. 
## Consumer Infrared Receiver
The PC2 board has a Consumer Infrared Receiver (CIR) module located to the right of GPIO connector (CON3) to receive data from a received infrared (IR) signal to port PL11 on H5 Soc. The CIR module is implemented in hardware and provides full physical layer implementation, supports IR for remote control, has 64x8 bits FIFO for data buffer and programmable FIFO thresholds. The CIR registers are at base address: 0x01F02000. 
## Microphone
The PC2 board has a built in microphone located just to the right of the HDMI connector with frequency range specification of ~20-16000Hz. It is connected to analog input port MICIn1 on H5 SoC and analog control registers: 0x05, Linein and Gain Control Register (Default Value: 0x30), 0x06 MIC1 Gain Control Register (Default Value: 0x33), and 0x0B MIC1 Boost and MICBIAS Control Register (Default Value: 0x04). MICIn2 input is not connected. 
## CPU clock speed limit
The Allwinner H5 manual does not provide the CPU clock speed information. The following comment is found in the SDK provided by Xunlong. 
[code] 
    ;----------------------------------------------------------------------------------
    ; dvfs voltage-frequency table configuration
    ;
    ; max_freq: cpu maximum frequency, based on Hz
    ; min_freq: cpu minimum frequency, based on Hz
    ;
    ; lv_count: count of lv_freq/lv_volt, must be < 16
    ;
    ; lv1: core vdd is 1.30v if cpu frequency is (1104Mhz, 1152Mhz]
    ; lv2: core vdd is 1.26v if cpu frequency is (1008Mhz, 1104Mhz]
    ; lv3: core vdd is 1.20v if cpu frequency is (816Mhz,  1008Mhz]
    ; lv4: core vdd is 1.10v if cpu frequency is (648Mhz,   816Mhz]
    ; lv5: core vdd is 1.04v if cpu frequency is (480Mhz,   648Mhz]
    ; lv6: core vdd is 1.04v if cpu frequency is (480Mhz,   648Mhz]
    ; lv7: core vdd is 1.04v if cpu frequency is (480Mhz,   648Mhz]
    ; lv8: core vdd is 1.04v if cpu frequency is (480Mhz,   648Mhz]
    ;
    ;----------------------------------------------------------------------------------
    [dvfs_table]
    ;extremity_freq = 1344000000
    max_freq = 1008000000
    min_freq = 480000000
    
[/code]
The Orange Pi PC 2 board uses the [SY8106A][42957] voltage regulator (U9) for providing the CPU core voltage (VDD_CPUX, nominally 1.2V at 6A). The default CPU voltage is 1.1V after power-on (selected by the resistors on the PCB) and can be changed at runtime by software via I2C interface (I2C address 0x65). According to the table above, this default voltage should be safe for using with the CPU clock frequencies up to 816MHz. The H5 user manual specifies 1.5V as the absolute maximum for the VDD_CPUX voltage and 1.4V as the recommended maximum. CPU core voltage (VDD_CPUX) can be measured at test point '1V1C', located just to the right of the camera interface connector (CON1). 
The stability of the Orange Pi PC2 was tested using HPL 2.1. Per frequency the voltage was lowered until HPL found data corruption during the tests. The results of this test show the Orange Pi PC 2 is able to run at 1368 MHz with a minimum core voltage of 1.38V. The tests fail while running at 1392 MHz with a core voltage of 1.4V. 
This test was only done on one single board. Accuracy of this data must be confirmed. The results of the test: <http://pastebin.com/0z3FhfkU>
# Adding a serial port
## Locating the UART
[![OPi PC 2 UART.jpg][42958]][42959]
[][42960]
Debug UART pins are located between the 5V power input jack (J1) and the HDMI connector (CON2). The three-pin single-in-line header pins are marked as _GND_ , _RX_ and _TX_ on the PCB. Just attach some leads according to our [UART Howto][42961]. 
# Pictures
  * [![OPi PC 2 Top.jpg][42962]][42963]
  * [![OPi PC 2 Bottom.jpg][42964]][42965]
  * [![OPi PC 2 1.jpg][42966]][42967]
  * [![OPi PC 2 2.jpg][42968]][42969]
  * [![OPi PC 2 3.jpg][42970]][42971]
  * [![OPi PC 2 4.jpg][42972]][42973]

# Variants
# Also known as
# See also
  * [Xunlong Orange Pi site][42974]
  * [Official Github Repository][42975]
  * [Unofficial Github Repository more worth a look][42976]
  * [H5 BSP by FriendlyELEC also containing documentation][42977]
  * [Official Orange Pi Forums][42978].
  * [Orange Pi PC 2 Schematics 1.2][42979]

## Manufacturer images
  * <http://www.orangepi.org/downloadresources/>
  * [https://mega.nz/#F!m40jgBYQ!-uNiWmKhGoQUAqnWQvlr-w][42980]

# References
