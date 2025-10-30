# Ippo q8h
Ippo q8h  
---  
[![Ippo q8h front.jpg][28149]][28150]  
Manufacturer |  [Ippo][28151]  
Dimensions |  181 _mm_ x 121 _mm_ x 10.5 _mm_  
Release Date |  November 2013   
Website |  [Missing Product Page ][28152]  
Specifications   
SoC |  [A23][28153] @ 1.5Ghz (verify me!)  
DRAM |  512MiB DDR3 @ 480MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, 1000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSL1680][28154])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][28155] / [Espressif ESP8089][28156] / [RDA RDA5990p][28157])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front-facing   
Other |  Accelerometer ([Domintech DMARD10][28158]), Bluetooth (when combined with RDA5990 module).   
Headers |  UART   
This cheap (40EUR) tablet is an [A23][28153] based update of the hugely popular [Q88][28159], which was based on the A13. It is currently often sold as an A13 device, even though the A23 is a serious step up from the measly A13. 
## Contents
  * [1 Identification][28160]
    * [1.1 Q8H-V2][28161]
    * [1.2 Q8H-V5][28162]
    * [1.3 Q8H-V1.0][28163]
    * [1.4 Q8H-V1.2][28164]
    * [1.5 Q8H-V1.5][28165]
      * [1.5.1 Working:][28166]
      * [1.5.2 Not working:][28167]
      * [1.5.3 Android modules][28168]
  * [2 Sunxi support][28169]
    * [2.1 Current status][28170]
    * [2.2 Images][28171]
    * [2.3 HW-Pack][28172]
    * [2.4 BSP][28173]
    * [2.5 Manual build specifics][28174]
    * [2.6 Mainline kernel][28175]
      * [2.6.1 Q8H-V1.2][28176]
      * [2.6.2 Q8H-V5][28177]
  * [3 Tips, Tricks, Caveats][28178]
    * [3.1 FEL mode][28179]
    * [3.2 Android ADB access][28180]
    * [3.3 Wifi][28181]
  * [4 Adding a serial port (**voids warranty**)][28182]
    * [4.1 Device disassembly][28183]
    * [4.2 Locating the UART][28184]
  * [5 Pictures][28185]
  * [6 Hardware documentation][28186]
  * [7 Also known as][28187]
  * [8 See also][28188]

# Identification
The Q8H has multiple revisions, with minor variations to passive component placement. 
## Q8H-V2
The markings on the board read: 
[code] 
    Q8H-V2
    2013-11-19
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: Q8H
  * Build Number: polaris a70H-eng 4.2.2 JDQ39 20131127 test-keys

These android ids matches the android image used on the [Eken A70h][28189], which has a different case design. 
This version comes with a [Realtek RTL8188ETV wifi][28155] usb module. 
## Q8H-V5
The markings on the board read: 
[code] 
    Q8H-V5
    2013-12-26
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: Q8H
  * Build Number: polaris-eng 4.2.2 8089 20140103-8089

This version comes with an [Espressif ESP8089 wifi][28156] usb module. 
## Q8H-V1.0
The markings on the board read: 
[code] 
    Q8H-V1.0
    2014 03 15
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: Q8H
  * Build Number: polaris-eng 4.2.2 JDQ39 20140326 test-keys

This version comes with an [RDA RDA5990P][28157] shared wifi/bluetooth/fm radio. 
## Q8H-V1.2
The markings on the board read: 
[code] 
    Q8H-V1.2
    2014 08 02
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: Q8H
  * Build Number: polaris_p1-eng 4.4.2 KVT 20140627 test-keys

This version comes with an [RDA RDA5990P][28157] shared wifi/bluetooth/fm radio. 
## Q8H-V1.5
The markings on the board read: 
[code] 
    Q8H-V1.5 
    2015 0129
[/code]
Q8H-V1.5 2015 0129 sports a:  
CPU: A33  
Ram: 512 mb  
Touchscren: GSL1680  
WIFI: RTL8703AS  
NAND: 4GB  
Screen 1024x768 (?)  
USB: 1 otg ( no additional pads found to support a second one )  
  

##### Working:
  
Display - you need to modify the lcd specifics in FEX (they can be extracted from uboot) - make sure you install the simple framebuffer driver  
Kernel - linux-sunxi next (4.6-rcX)  
DTB: tried some - sun8i-a33-q8-tablet.dtb works ok  
SDcard: OTG  
Brightness: 
    Make sure the GPIOS are exposed in the FEX file (should be by default) 
    echo 244 > /sys/class/gpio/export
    echo "out" > /sys/class/gpio244/direction
    Dim backlight: echo "1" > /sys/class/gpio244/value
    Full backlight: echo "0" > /sys/class/gpio244/value
Video on/off: 
    Make sure the GPIOS are exposed in the FEX file (should be by default) 
    echo 230 > /sys/class/gpio/export
    echo "out" > /sys/class/gpio230/direction
    Dim backlight: echo "1" > /sys/class/gpio230/value
    Full backlight: echo "0" > /sys/class/gpio230/value
[code] 
    import struct
    import os
    
    inputDevice = "/dev/input/event1"
    inputEventFormat = 'iihhi'
    inputEventSize = 16
    file = open(inputDevice, "rb")
    event = file.read(inputEventSize)
    lcdStatus = 1;
    
    os.system("echo 224 > /sys/class/gpio/export");
    os.system('echo "out" > /sys/class/gpio/gpio224/direction');
    os.system('echo 0 > /sys/class/gpio/gpio224/value');
    os.system("echo 230 > /sys/class/gpio/export");
    os.system('echo "out" > /sys/class/gpio/gpio230/direction');
    os.system('echo 1 > /sys/class/gpio/gpio230/value');
    
    
    while event:
      (time1, time2, type, code, value) = struct.unpack(inputEventFormat, event)
    
      print "code %d, value %d" %(code, value)
    
      if value == 1:
        if lcdStatus == 0:
         os.system('echo 1 > /sys/class/gpio/gpio230/value');
         lcdStatus = 1
        else:
         os.system('echo 0 > /sys/class/gpio/gpio230/value');
         lcdStatus = 0
    
      event = file.read(inputEventSize)
    file.close()
    
[/code]
Ubuntu - 15.10 Wily  
Instalation method - SDcard - debootstrap  
USB ethernet used AX88772b - OTG  
  

##### Not working:
  
wifi (chip is RTL8703AS but the driver is rtl8723bs, managed to modify the dtb now the device shows in /sys/bus/sdio but can't load the driver [mmc0:0001:1 failed with error -16]),   
bluetooth,   
audio,   
rotation,   
touchscreen,   
hardware keys (there is a screen saver [black screen] in place in the framebuffer, power on button can "wake" up the device) although power button shuts down the device after 5 seconds or so.  
  
  
Problems encountered:  

  1. kernel 4.6-rcX and Ubuntu 14 (trusty) does not boot
  2. USB has a weird behaviour 
     1. I had a 2.0 hub plugged in and in that the USB ethernet, and my keyboard G11 has an internal hub, I seems that the hubs can't work together in linux (tested in windows and all looks ok) I had no enthernet connection till I removed my keyboard (power was ok since I tested it charging my phone, a wifi adapter, a sdcard reader, and the AX88772b and network was just fine).
  3. Tried compiling the latest AX88772b driver I got a siocsifflags: No room left on device when up-ing the interface via ifconfig

  
  
In android, under Settings->About Tablet, you will find: 
  * Model Number: Q8H
  * Build Number: astar_y3-eng 4.4.2 KVT49L 20141120 test-keys

##### Android modules
[code] 
    Module name			Size		Status/used bu
    -------------------------------------------------------------------------------
    8723bs_vq0 			1836110		0 - Live 0x00000000
    gslX680 			305751		0 - Live 0x00000000 (F)
    mxc622x 			4341		0 - Live 0x00000000
    sunxi_schw 			12559		0 - Live 0x00000000 (O)
    cdc_ether 			5099		0 - Live 0x00000000
    rtl8150 			9023		0 - Live 0x00000000
    mcs7830 			6292		0 - Live 0x00000000
    qf9700 				7805		0 - Live 0x00000000
    asix 				17150		0 - Live 0x00000000
    usbnet 				17700 		4 cdc_ether,mcs7830,qf9700,asix, Live 0x00000000
    sunxi_keyboard 			3021 		0 - Live 0x00000000
    sw_device 			13668 		0 - Live 0x00000000
    vfe_v4l2 			446344 		0 - Live 0x00000000
    gc2035 				13729 		0 - Live 0x00000000
    gc0312 				9954 		1 - Live 0x00000000
    gc0328 				11571 		0 - Live 0x00000000
    gc0308 				10958 		0 - Live 0x00000000
    vfe_subdev 			4523 		5 vfe_v4l2,gc2035,gc0312,gc0328,gc0308, Live 0x00000000
    vfe_os 				4099 		2 vfe_v4l2,vfe_subdev, Live 0x00000000
    cci 				21594 		4 gc2035,gc0312,gc0328,gc0308, Live 0x00000000
    videobuf_dma_contig 		5535 		1 vfe_v4l2, Live 0x00000000
    videobuf_core 			16520 		2 vfe_v4l2,videobuf_dma_contig, Live 0x00000000
    leds_sunxi 			1351 		0 - Live 0x00000000
    mali 				209866 		15 - Live 0x00000000 (O)
    lcd 				49673 		0 - Live 0x00000000
    disp 				993096 		8 mali,lcd, Live 0x00000000
    nand 				287437 		10 - Live 0x00000000 (O)
    
[/code]
This version comes with an [Realtek RTL????][28155] wifi chip. Note that some Q8H-V1.5 boards also ship with an [A33][28190] soc. 
# Sunxi support
## Current status
Like all things A23, this hardware is not supported. It is however a prime target for development. For more information, check [ the Allwinner A23 SoC page][28153]. 
## Images
## HW-Pack
## BSP
## Manual build specifics
  * For building u-boot, use the "Ippo_q8h" target.
  * The .fex file can be found in sunxi-boards as [ippo_q8h_v5.fex][28191]

Everything else is the same as the [manual build howto][28192]. 
## Mainline kernel
### Q8H-V1.2
Use the _sun8i-a23-ippo-q8h-v1.2.dts_ device-tree file for the [mainline kernel][28193]. 
### Q8H-V5
Use the _sun8i-a23-ippo-q8h-v5.dts_ device-tree file for the [mainline kernel][28193]. 
# Tips, Tricks, Caveats
## FEL mode
The Volume + button triggers [ FEL mode][28194]. 
## Android ADB access
Standard ADB does not work out of the box. You need to add the vendor id **0x1F3A** to [the adb usb config file][28195]. 
## Wifi
While some use the well known [Realtek Wifi chips][28155], this tablet is also known to come with an [Espressif ESP8089][28156] or an [RDA RDA5990P][28157]. The latter two have no support in [our standard kernel][28196], but source code is available from other kernel tree releases. Please check our [Wifi page][28197] for more details. 
# Adding a serial port (**voids warranty**)
[![][28198]][28199]
[][28200]
UART pads
## Device disassembly
As is the case with the [Q8][28201], it is absolutely trivial to open this device. 
The edge of the back cover needs to be pushed to the outside to release the clips. So put the device on its back and insert your [plastic tool][28202] in the outer edge. Push the outer casing away from the display, and you should soon hear the clips release. 
## Locating the UART
An obvious serial port is available on the mainboard, to the right of the SoC, between the 2 oscillators. The 2 pads are separately enclosed in white circles. The pad nearer to the SoC is TX, the other is RX. 
These pads correspond to PL2/3, which is the R_UART in the SoC. This UART is not listed in the datasheets, however you can find information about it in the A23 SDK sources. 
The serial port is not enabled in the stock Android image. Edit the FEX file and set s_uart_used = 1 in the s_uart0 section. The port is then used by the OpenRISC core to dump debug messages. Whether this port can be used by the primary system with Allwinner's kernel is still unknown. From a hardware perspective, they can share the port, provided adequate locking is done. 
# Pictures
  * [![Ippo q8h front.jpg][28203]][28150]
  * [![Ippo q8h back.jpg][28204]][28205]
  * [![Ippo q8h buttons 1.jpg][28206]][28207]
  * [![Ippo q8h buttons 2.jpg][28208]][28209]
  * [![Ippo q8h innards.jpg][28210]][28211]
  * [![][28212]][28213]
[Q8H V2][28161] board front 
  * [![][28214]][28215]
[Q8H V5][28162] board front 
  * [![][28216]][28217]
[Q8H V5][28162] board back 
  * [![][28218]][28219]
[Q8H V1.0][28163] board front 
  * [![][28220]][28221]
[Q8H V1.2][28164] board front 

# Hardware documentation
  * [Schematic for Q8H V1.5 board.][28222]
  * [Top view for Q8H V1.5 board.][28223]
  * [Bottom view for Q8H V1.5 board.][28224]

# Also known as
This hardware is sold under many guises, very often as _Q88Pro_. If it is claimed to be an A13 tablet but with a 4.2.2 android, then chances are that it is an A23 one instead. 
# See also
  * [ Ippo Q88][28159]
  * [Eken A70h][28189]
  * [Inet 86dz d701c][28225], another cheap A23 tablet.
