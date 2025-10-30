# Honeywell VDP7
Honeywell VDP7  
---  
[![VDP7 front.jpg][24115]][24116]  
Manufacturer |  [Honeywell][24117]  
Dimensions |  217 _mm_ x 144 _mm_ x 17 _mm_  
Release Date |  2018   
Website |  not available]   
Specifications   
SoC |  [A64][24118] @ 1.2Ghz   
DRAM |  1GiB DDR3 @ 672MHz   
NAND |  None   
Power |  DC 12V @ 2A   
Features   
LCD |  154mm x 86mm (7" 1024:600Pixel)   
Touchscreen |  5-finger capacitive Touchscreen ([GT911][24119])   
Video |  None   
Audio |  internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8189ES][24120]), 10/100Mbps Ethernet ([ASIX AX88772C][24121])   
Storage |  µSD, eMMC   
USB |  USB2.0 Host (Connected to AX88772C), USB2.0 OTG (Pin-Header J4)   
Camera |  None   
Other |  None   
Headers |  UART, USB-OTG, LVDS-LCD, MIPI-LCD, Touch, Camera, ...   
## Contents
  * [1 Identification][24122]
  * [2 Sunxi support][24123]
    * [2.1 Current status][24124]
    * [2.2 Manual build][24125]
      * [2.2.1 U-Boot][24126]
        * [2.2.1.1 Sunxi/Legacy U-Boot][24127]
        * [2.2.1.2 Mainline U-Boot][24128]
      * [2.2.2 Linux Kernel][24129]
        * [2.2.2.1 Sunxi/Legacy Kernel][24130]
        * [2.2.2.2 Mainline kernel][24131]
  * [3 Tips, Tricks, Caveats][24132]
    * [3.1 FEL mode][24133]
    * [3.2 LVDS-Display][24134]
    * [3.3 Device disassembly][24135]
    * [3.4 Power Supply (J3)][24136]
    * [3.5 Locating the UART0 (J6)][24137]
    * [3.6 Locating the UART3/4 (CON2)][24138]
    * [3.7 Locating the USB-OTG (J4)][24139]
  * [4 Pictures][24140]
  * [5 Also known as][24141]
  * [6 See also][24142]

# Identification
On the back of the device, the following is printed: 
[code] 
    Honeywell
    Model: VDP7-KA-W
    7" IPVDP monitor, KA channel.White
[/code]
The PCB has the following silkscreened on it: 
[code] 
    TC-HONEYWELL-A64-JK-V15
    2017-12-08
    TC3287
[/code]
In GUI, under Settings->About, you will find: 
  * Device Name: _Tuna_

# Sunxi support
## Current status
The device is currently not supported by default by uboot or the Linux kernel 
## Manual build
You can build things for yourself by following our [ Manual build howto][24143] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
Use the following config with minimal own created A64 dts-files: 
[code] 
    CONFIG_ARM=y
    CONFIG_ARCH_SUNXI=y
    CONFIG_SPL=y
    CONFIG_MACH_SUN50I=y
    CONFIG_RESERVE_ALLWINNER_BOOT0_HEADER=y
    CONFIG_DRAM_ODT_EN=y
    CONFIG_MMC0_CD_PIN=""
    CONFIG_MMC_SUNXI_SLOT_EXTRA=2
    CONFIG_SPL_SPI_SUNXI=y
    CONFIG_DEFAULT_DEVICE_TREE="sun50i-a64-vdp7" # Currently missing
    CONFIG_DM_REGULATOR=y
    CONFIG_DM_REGULATOR_FIXED=y
    CONFIG_DM_PWM=y
    CONFIG_PWM_SUNXI=y
    # CONFIG_SYS_MALLOC_CLEAR_ON_INIT is not set
    # CONFIG_CMD_FLASH is not set
    # CONFIG_SPL_DOS_PARTITION is not set
    # CONFIG_SPL_EFI_PARTITION is not set
    CONFIG_USB_EHCI_HCD=y
    CONFIG_SYS_USB_EVENT_POLL_VIA_INT_QUEUE=y
[/code]
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][24144] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The Emergency button on the right side triggers the [ FEL mode][24145]. The corresponding USB OTG is available on the extension board connector J4 and has the following pin out: 
  1. VBUS
  2. DM
  3. DP
  4. USB-ID
  5. GND

## LVDS-Display
Is connected over LVDS pins PD12-PD21 on LCD2 connector. 
## Device disassembly
Remove the back 4 screws. There is a hole on the bottom back housing were a screw driver could be placed to open it. 
## Power Supply (J3)
The assembled connector J3 in the near of the network jack is for the 12V power supply and has the following pin out: 
  1. +12V
  2. GND

## Locating the UART0 (J6)
There is a not assembled connector J6 marked on the right extension board which is connected to UART0 and has the following pin out: 
  1. GND
  2. TX
  3. VCC
  4. RX

## Locating the UART3/4 (CON2)
The connector CON2 has 2 RS485 UARTs connected. 
  1. DBEL
  2. GND
  3. UART3-A
  4. UART3-B
  5. UART4-A
  6. UART4-B

## Locating the USB-OTG (J4)
There is a not assembled connector J4 marked on the right extension board which is connected to USB0 and has the following pin out: 
  1. VBUS
  2. DM
  3. DP
  4. ID
  5. GND

# Pictures
  * [![VDP7 front.jpg][24146]][24116]
  * [![VDP7 back.jpg][24147]][24148]
  * [![VDP7 PCBA.jpg][24149]][24150]

# Also known as
  * VDP7-KA-W
  * VDP7-KA-B
  * VDP7-PRO-W
  * VDP7-PRO-B

# See also
[Honeywell Price Reckoner 2019 - Page 47][24151]
