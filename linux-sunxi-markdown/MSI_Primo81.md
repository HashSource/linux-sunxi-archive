# MSI Primo81
MSI Primo81  
---  
[![MSI Primo81 front.jpg][33335]][33336]  
Manufacturer |  [MSI][33337]  
Dimensions |  200 _mm_ x 135 _mm_ x 7.8 _mm_  
Release Date |  November 2013   
Website |  [Device Product Page][33338]  
Specifications   
SoC |  [A31s][33339] @ 1Ghz   
DRAM |  1GiB DDR3 @ 360MHz (2x [NT5CC256M16CP][33340]  
NAND |  16GB (2x H27UCG8T2MYR-BC)   
Power |  USB, 3500mAh 3.7V Li-Ion battery   
Features   
LCD |  768x1024 (7.85" 4:3), using [SSD2825][33341]  
Touchscreen |  5-finger capacitive ([Goodix GT911][33342])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([RTL8188ETV][33343])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2.0MP (1600x1200) rear   
Other |  Accelerometer ([Freescale MMA8452][33344])   
Headers |  Camera, capacitive touch panel, MIPI DSI LCD   
This page needs to be properly filled according to the [New Device Howto][33345] and the [New Device Page guide][33346].
This is a brand name tablet from a reputable hardware vendor, so no problems with identification are expected. The tablet has a nice slim, but sturdy aluminium frame and a high quality 1024x768 IPS screen. A Mini-HDMI connector is also available. 
This device is perfectly unbrickable because it effectively has a [hardware FEL button][33347]. Also the manufacturer helpfully provides [recovery images][33348] for the original Android system, so that the tablet can be always restored to the factory state after any crazy experiments. 
## Contents
  * [1 Identification][33349]
  * [2 Sunxi support][33350]
    * [2.1 Current status][33351]
    * [2.2 Images][33352]
    * [2.3 HW-Pack][33353]
    * [2.4 BSP][33354]
    * [2.5 Manual build][33355]
    * [2.6 Mainline U-Boot][33356]
    * [2.7 Mainline kernel][33357]
  * [3 Tips, Tricks, Caveats][33358]
    * [3.1 FEL mode][33359]
    * [3.2 LCD][33360]
    * [3.3 Touchpanel][33361]
    * [3.4 MicroSD breakout for debugging][33362]
    * [3.5 Use as a GNU/Linux desktop machine][33363]
  * [4 Adding a serial port (**voids warranty**)][33364]
    * [4.1 Device disassembly][33365]
    * [4.2 Locating the UART][33366]
  * [5 Pictures][33367]
  * [6 Also known as][33368]
  * [7 See also][33369]
    * [7.1 Manufacturer images][33370]

# Identification
There is a clearly visible **MSI Primo81-216** label on the back of the tablet. It simply can't be mistaken with anything else. 
Information about the Android firmware: <http://www.androiddevice.info/submission/18755/show>
# Sunxi support
## Current status
The [FEX][33371] file can be found in sunxi-boards as [msi_primo81.fex][33372]
Feature  | Mainline u-boot + mainline kernel  | Allwinner SDK  | sunxi-3.4 kernel   
---|---|---|---  
WLAN | Works (kernel 4.4rc1 or newer / u-boot v2015.04 or newer).  | The Android kernel from the Allwinner SDK may potentially work with GNU/Linux, but nobody has tested it on this device yet. Feel free to try [SDK build howto][33373] | No plans to support this kernel on [A31s][33339] hardware   
HDMI | Works with simplefb (kernel 4.4rc1 or newer / u-boot v2015.04 or newer).   
LCD | Works with simplefb (kernel 4.4rc1 or newer / u-boot v2015.04 or newer).   
USB OTG | Works in host-only mode (support was added in [kernel 4.3][33374]).   
Touchscreen | A goodix touchscreen driver exists in the mainline Linux kernel since v3.19, but devicetree support has only been [added][33375] in kernel v4.1. Basic functionality (cursor positioning and "left-button" click emulation) works.   
Accelerometer | A [driver exists][33376], but is currently untested.   
Camera | Unsupported   
Audio | Unsupported   
## Images
## HW-Pack
## BSP
## Manual build
No support in the community maintained sunxi-3.4 kernel is planned. Please skip to the next Mainline U-Boot/Mainline kernel sections. 
## Mainline U-Boot
Basic support in mainline u-boot (SPL and console output on the LCD) is available since u-boot v2015.04. Host mode support for the USB OTG port and console input with a USB keyboard is possible with the current [mainline u-boot git 'master' branch][33377] and will probably be enabled by default in [u-boot v2015.07][33378]. 
For [ building mainline u-boot][33379], use the _MSI_Primo81_ board name. 
## Mainline kernel
Use the _sun6i-a31s-primo81.dtb_ device-tree file for the [mainline kernel][33380]. 
# Tips, Tricks, Caveats
## FEL mode
The VOL+ button triggers [ FEL mode][33381]. The button is directly connected to the UBOOT_SEL pin and drives it low when pressed, as can be easily verified by reading the BOOT_SEL_PAD_STA bits from [ SRAM_VER_REG][33382]. This makes the device unbrickable even in the worst case scenario of NAND corruption. 
## LCD
[![][33383]][33384]
[][33385]
MSI Primo81 and [LCD][33386] support in u-boot
The tablet is using a high quality B079XAN01/LP079X01 7.85" 768x1024 IPS LCD display (the same as in the 1st generation iPad Mini). This LCD display is using MIPI DSI interface, but the [A31s][33339] SoC does not have native support for it. So a separate [SSD2825][33341] bridge chip converts parallel LCD interface into MIPI DSI for this display to work. Such setup is somewhat more complicated than a regular LCD display and needs a special code path in the u-boot display driver. 
Attempt to do software identification of the LCD panel with the help of issuing MIPI DCS commands via SSD2828: 
[code] 
    Trying standard MIPI DSI commands to identify LCD panel:
    DCS command 0x04 returned  1 bytes: 00
    DCS command 0xA1 returned  1 bytes: 00
    Trying nonstandard MIPI DSI commands to identify LCD panel:
    DCS command 0xB1 returned 15 bytes: A1 95 19 19 00 00 00 00 00 00 00 00 37 10 00
    DCS command 0xDA returned  1 bytes: 00
    DCS command 0xDB returned  1 bytes: 00
    DCS command 0xDC returned  1 bytes: 00
    
[/code]
Unfortunately neither of the standard MIPI_DCS_GET_DISPLAY_ID (0x04) and/or MIPI_DCS_READ_DDB_START (0xA1) commands is supported. The non-standard 0xB1 command returns some sequence of bytes, but we are yet to figure out whether this is actually anything meaningful. It does not look like AUO or LG codes from the [MIPI Alliance Manufacturer ID Page][33387] :-) 
The LCD's orientation is upside down, portrait mode, meaning the origin (0,0) point is in the bottom right corner if held upright, or the corner closed to the headphone jack. 
## Touchpanel
The touchpanel is a capacitive touchpanel, supported by a Goodix GT911 CTP IC. The touchpanel has a different orientation than the LCD. It has a landscape orientation, with the origin point in the same corner as the LCD, the corner closed to the headphone jack. 
## MicroSD breakout for debugging
[![][33388]][33389]
[][33390]
[ UART serial console][33391] with the help of [MicroSD Breakout][33392] and [TTL to USB serial cable][33393]
It is possible to temporarily abandon the [ SD card slot][33394] and instead gain [ UART serial console][33391] by using a [MicroSD Breakout][33392] accessory. This is useful for low level u-boot/kernel debugging without any need to dismantle the device. Even without the SD card, the system (u-boot + kernel + initramfs) still can be booted over a MicroUSB cable by using the [FEL/USBBoot][33395] mode provided by [BROM][33396]. 
## Use as a GNU/Linux desktop machine
A MiniHDMI cable can be used to connect a big desktop monitor. Something like a [USB OTG Charging Hub][33397] accessory allows using USB peripherals (keyboard, mouse, ethernet adapter, etc.) and supplying power to the tablet at the same time. 
# Adding a serial port (**voids warranty**)
[![][33398]][33399]
[][33400]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][33391]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
The tablet has a one-piece aluminum bezel/back. It is fastened to the LCD by 5 equally spaced plastic clips on both long sides. Since the aluminum is quite stiff, you should use a [Plastic_tool][33401] to pry it apart. Using a metal tool is likely to warp the aluminum back. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][33391].
# Pictures
  * [![MSI Primo81 front.jpg][33402]][33336]
  * [![MSI Primo81 back.jpg][33403]][33404]
  * [![MSI Primo81 connectors.jpg][33405]][33406]
  * [![MSI Primo81 buttons.jpg][33407]][33408]
  * [![MSI Primo81 Board Front.jpg][33409]][33410]

Display quality comparison with [MSI Primo73][33411]
  * [![Display quality - Primo73 \(TN\) vs. Primo81 \(IPS\) frontal.jpg][33412]][33413]
  * [![Display quality - Primo73 \(TN\) vs. Primo81 \(IPS\) left.jpg][33414]][33415]
  * [![Display quality - Primo73 \(TN\) vs. Primo81 \(IPS\) right.jpg][33416]][33417]

# Also known as
# See also
  * [MSI Primo73][33411] (has the same WLAN, touchscreen, accelerometer and camera, but different SoC and LCD screen)
  * [ICOU Fatty I][33418] (also uses SSD2828 for driving a MIPI LCD display)

## Manufacturer images
The manufacturer provides a PhoenixSuite recovery image at [http://www.msi.com/product/tablet/support/Primo-81.html#down-firmware][33419]
