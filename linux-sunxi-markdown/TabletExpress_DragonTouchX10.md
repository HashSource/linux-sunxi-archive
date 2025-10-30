# TabletExpress DragonTouchX10
TabletExpress DragonTouchX10  
---  
[![Device front.jpg][54142]][54143]  
Manufacturer |  [TabletExpress][54144]  
Dimensions |  15.12 x 2.28 x 7.8 inches   
Release Date |  Month year  
Website |  [Device Product Page][54145]  
Specifications   
SoC |  [A83T][54146] @ 2.0Ghz   
DRAM |  1GiB DDR3   
NAND |  16GB   
Power |  DC 5V @ 2A, 7200mAh Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][54147])   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][54148]), 10/100/1000Mbps Ethernet ([Manufacturer device][54149])   
Storage |  µSD, SATA   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  5.0MP (2592x1936) front, 2.0MP (????x????) rear   
Other |  Accelerometer ([Bosch device][54150])   
This page needs to be properly filled according to the [New Device Howto][54151] and the [New Device Page guide][54152].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][54153]
  * [2 Sunxi support][54154]
    * [2.1 Current status][54155]
    * [2.2 Images][54156]
    * [2.3 Manual build][54157]
      * [2.3.1 U-Boot][54158]
        * [2.3.1.1 Sunxi/Legacy U-Boot][54159]
        * [2.3.1.2 Mainline U-Boot][54160]
      * [2.3.2 Linux Kernel][54161]
        * [2.3.2.1 Sunxi/Legacy Kernel][54162]
        * [2.3.2.2 Mainline kernel][54163]
  * [3 Tips, Tricks, Caveats][54164]
    * [3.1 FEL mode][54165]
    * [3.2 Device specific topic][54166]
    * [3.3 ...][54167]
  * [4 Adding a serial port (**voids warranty**)][54168]
    * [4.1 Device disassembly][54169]
    * [4.2 Locating the UART][54170]
      * [4.2.1 microSD breakout][54171]
  * [5 Pictures][54172]
  * [6 Also known as][54173]
  * [7 See also][54174]
    * [7.1 Manufacturer images][54175]

# Identification
On the back of the device, the following is printed: 
[code] 
    DragonTouch
    Model:x10
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INEI-N106-REV01
    2015-03-17
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _X10_
  * Build Number: _A83T_N106_N1061L2BC_1508208.20160115_

# Sunxi support
Unknown 
## Current status
Only stock manufacturer firmware tested and working. 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][54174]. If no sunxi based images are available, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][54176] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][54177] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
Power off the device either through the menu or by holding the power button for 10 seconds. 
Hold the volume down key while connecting the device via USB. 
Continue to hold the volume down key after USB is plugged in and press the power button 8 times. 
In linux you can verify it has gone into FEL mode using the lsusb command. It will be listed as 
[code] 
    Bus 002 Device 033: ID 1f3a:efe8 Onda (unverified) V972 tablet in flashing mode
    
[/code]
Firmware can then be successfully flash using LiveSuit(Linux) or PhoenixSuite(Windows) 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][54178]][54179]
[][54180]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][54181]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
Rear casing can be removed with plastic tool or credit card. Unscrew 6 screws to release chip from board. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][54181].
### microSD breakout
You will need to modify the original sys_config.fex This can be extracted from the manufacturer image. 
[code] 
     
    [uart_para]
    -uart_debug_port = 0
    -uart_debug_tx   = port:PB09<2><1><default><default>
    -uart_debug_rx   = port:PB10<2><1><default><default>
    +uart_debug_port = 0
    +uart_debug_tx   = port:PF02<2><1><default><default>
    +uart_debug_rx   = port:PF04<2><1><default><default>
    
    [force_uart_para]
    -force_uart_port  = 0
    -force_uart_tx    = port:PF02<3><1><default><default>
    -force_uart_rx    = port:PF04<3><1><default><default>
    +;force_uart_port  = 0
    +;force_uart_tx    = port:PF02<2><1><default><default>
    +;force_uart_rx    = port:PF04<2><1><default><default>
     
    [uart0]
    uart_used       = 1
    uart_port       = 0
    uart_type       = 2
    -uart_tx         = port:PB09<2><1><default><default>
    -uart_rx         = port:PB10<2><1><default><default>
    +uart_tx         = port:PF02<2><1><default><default>
    +uart_rx         = port:PF04<2><1><default><default>
    uart_regulator	= "vcc-io"
    
    [mmc0_para]
    -sdc_used          = 1
    +sdc_used          = 0
    
[/code]
Note: The sys_config.fex file that comes with the firmware left out parenthesis around vcc-vibrator on line 476. You will need to add these to successfully compile. 
This fex file can be used to compile new version of u-boot and boot0. 
Compile the new sys_config.fex file to a bin file using fex2bin: 
[code] 
    fex2bin sys_config.fex osys_config.bin
    
[/code]
Then compile a new u-boot, boot0_sdcard, and boot0_nand using this bin 
[code] 
    pctools/linux/mod_update/update_boot0 boot0_nand.fex sys_config.bin NAND
    pctools/linux/mod_update/update_boot0 boot0_sdcard.fex sys_config.bin SDMMC_CARD
    pctools/linux/mod_update/update_uboot u-boot.fex sys_config.bin
    
[/code]
Note: You will likely need to recompile update_uboot as shown [here][54182]. 
Once these are recompiled, you can repack a new firmware image and flash. 
# Pictures
  * [![DragonTouchX10 PCB Front.jpg][54183]][54184]
  * [![DragonTouchX10 PCB Back.jpg][54185]][54186]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
