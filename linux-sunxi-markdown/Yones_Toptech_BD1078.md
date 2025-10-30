# Yones Toptech BD1078
Yones Toptech BD1078  
---  
[![Yones Toptech BD1078 Front.png][63438]][63439]  
Manufacturer |  [Yones Toptech][63440]  
Dimensions |  263 _mm_ x 165 _mm_ x 12 _mm_  
Release Date |  April 2014   
Specifications   
SoC |  [A20][63441] @ 1Ghz   
DRAM |  1GiB DDR3 @ 408MHz   
NAND |  8/16/32GB   
Power |  DC 5V @ 2A, 6000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (10.1" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][63442])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8723AS][63443])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2.0MP (1600x1200) rear   
Other |  Accelerometer ([Memsic MXC622x][63444]), Bluetooth (Realtek RTL8723AS)   
Headers |  UART   
## Contents
  * [1 Identification][63445]
  * [2 Sunxi support][63446]
    * [2.1 Current status][63447]
    * [2.2 Mainline U-Boot][63448]
    * [2.3 Manual build][63449]
  * [3 Tips, Tricks, Caveats][63450]
    * [3.1 FEL mode][63451]
    * [3.2 USB storage mode][63452]
    * [3.3 Reset button][63453]
    * [3.4 Internal µSD card][63454]
  * [4 Adding a serial port (**voids warranty**)][63455]
    * [4.1 Device disassembly][63456]
    * [4.2 Locating the UART][63457]
  * [5 Pictures][63458]
  * [6 Also known as][63459]
  * [7 See also][63460]
    * [7.1 Manufacturer images][63461]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    YONESTOPTECH-BD1078-20131105
[/code]
In Android, under Settings->About Tablet, you will find: 
  * Model Number: _AX105_
  * Build Number: _wing_bd1078-eng 4.2.2 JDQ39 20140307 test-keys_

# Sunxi support
## Current status
The device is supported and maintained in [mainline U-Boot][63462]. There is no [mainstream kernel][63463] support at this point. 
Some features are missing on [Linux (sunxi-3.4 branch)][63464]: 
  * USB OTG doesn't work on the external connector (common to all sun7i devices) and it doesn't seem to work in either host or device mode
  * Wi-Fi and Bluetooth are untested

## Mainline U-Boot
For [ building mainline U-Boot][63465], use the _Yones_Toptech_BD1078_ target. 
## Manual build
  * For building u-boot, use the _Yones_Toptech_BD1078_ target.
  * The .fex file can be found in sunxi-boards as [yones_toptech_bd1078.fex][63466]

Everything else is the same as the [manual build howto][63467]. 
# Tips, Tricks, Caveats
## FEL mode
Any button (VOL-, VOL+, BACK) triggers [ FEL mode][63468] from boot1. 
Sending '2' over UART at boot triggers [ FEL mode][63468] from boot1. 
## USB storage mode
Sending '1' over UART at boot triggers an USB storage mode that exposes the nanda partition as well as the Android external storage. 
## Reset button
The reset button (on the side of the device) reboots the device. 
## Internal µSD card
The device has an internal µSD card port that shows as _mmcblk1_. This port doesn't have boot priority over NAND. 
# Adding a serial port (**voids warranty**)
[![][63469]][63470]
[][63471]
Yones Toptech BD1078 UART pads
## Device disassembly
In order to open the device, there are two Phillips screws to remove from the side with the connectors. The pins from the white part are easy to pop but it is advised to use a [a plastic tool][63472], starting from the side with the connectors. The front panel is very fragile and pressuring the screen to pop open the pins can easily end up in breaking the touch screen panel. 
## Locating the UART
The UART pads are located on the back of the PCB. There is a plastic film that protects the back of the board from shorting with the back of the LCD panel. The pads are clearly labeled on the PCB: GND, Rx, Tx. It is advised to put the plastic film back after soldering connectors according to the [UART howto][63473]. 
# Pictures
  * [![Yones Toptech BD1078 Front.png][63474]][63439]
  * [![Yones Toptech BD1078 Back.png][63475]][63476]
  * [![Yones Toptech BD1078 Buttons.jpg][63477]][63478]
  * [![Yones Toptech BD1078 Connectors.jpg][63479]][63480]
  * [![Yones Toptech BD1078 PCB.jpg][63481]][63482]
  * [![Yones Toptech BD1078 PCB back.jpg][63483]][63484]

# Also known as
  * V10Pro

# See also
  * [DealExtreme Product Page][63485]
  * [Inet k100c][63486]: Same case, different board.

## Manufacturer images
  * [BD1078 FW][63487]
