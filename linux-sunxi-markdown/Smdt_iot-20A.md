# Smdt iot-20A
Smdt iot-20A  
---  
[![Device front.jpg][51111]][51112]  
Manufacturer |  <http://www.smartdevicetech.com/>  
Dimensions |  124 x 88 mm   
Release Date |  07 2017   
Website |  <http://www.smartdevicetech.com/IoT-mainboard/iot-20a.html>  
Specifications   
SoC |  [A20][51113] @ [Template:1][51114]Ghz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  8GB emmc interface   
Power |  DC 12V @ 3A   
Features   
LCD |  1920x1080 (21,5")   
Touchscreen |  no   
Video |  lvds dual output, HDMI (Type A - full)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Wifi#realtek rtl8188etv][51115]), 10/100 Ethernet ([Ethernet#realtek rtl8201cp][51116])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  no   
Other |  uboot button, touch screen interface   
Headers |  2 channels serial port UART, 1 IIC, 4 IO interface, rtc,ir, dbgu,   
  
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][51117]
  * [2 Sunxi support][51118]
    * [2.1 Current status][51119]
    * [2.2 BSP][51120]
    * [2.3 Manual build][51121]
      * [2.3.1 U-Boot][51122]
        * [2.3.1.1 Sunxi/Legacy U-Boot][51123]
        * [2.3.1.2 Mainline U-Boot][51124]
      * [2.3.2 Linux Kernel][51125]
        * [2.3.2.1 Sunxi/Legacy Kernel][51126]
        * [2.3.2.2 Mainline kernel][51127]
  * [3 Tips, Tricks, Caveats][51128]
    * [3.1 FEL mode][51129]
    * [3.2 ...][51130]
  * [4 Adding a serial port (**voids warranty**)][51131]
    * [4.1 Locating the UART][51132]
  * [5 Pictures][51133]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Manufacturer Marketing Name
    ModelNumber
[/code]
The PCB has the following silkscreened on it: 
[code] 
    SMDT IoT-20A
    rev:v1.3
    2017-07-21
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
need help to install linux, and finally kodi. no boot since i had press uboot button. 
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][51134] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][51135] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][51136]. 
}} 
## ...
# Adding a serial port (**voids warranty**)
[![][51137]][51138]
[][51139]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][51140]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][51140].
# Pictures
Take some pictures of your device, [ upload them][51141], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![IMG 20200301 190505.jpg][51142]][51143]
  * [![IMG 20200301 190925.jpg][51144]][51145]
  * [![Capture5.JPG][51146]][51147]
  * [![Capture2.JPG][51148]][51149]
  * [![Capture6.JPG][51150]][51151]

}
