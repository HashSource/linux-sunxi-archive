# Azpen hybrx
Azpen hybrx  
---  
[![Hybrx open.jpg][8254]][8255]  
Manufacturer |  [Azpen Innovation][8256]  
Dimensions |  295 _mm_ x 198 _mm_ x 18 _mm_  
Release Date |  December 2016   
Website |  <https://www.azpeninnovation.com/collections/tablets/products/azpen-hybrx>  
Specifications   
SoC |  [A64][8257] @ XGhz   
DRAM |  1GiB/2GiB DDR3 @ xxxMHz   
NAND |  16/32/64GB   
Power |  DC 5V @ 3A 3.5mm socket compatible with SCP-2009A plug, 6000mAh 3.7V Li-Ion battery   
Features   
LCD |  1366x768 (11.6")   
Touchscreen |  none   
Video |  HDMI (Type B - mini)   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([RTL8723BS][8258])   
Storage |  µSD   
USB |  2 USB2.0 Host   
Camera |  0.480MP (800x600) front   
Other |  Accelerometer ([Manufacturer device][8259]), GPS   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][8260] and the [New Device Page guide][8261].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][8262]
  * [2 Sunxi support][8263]
    * [2.1 Current status][8264]
    * [2.2 Images][8265]
    * [2.3 HW-Pack][8266]
    * [2.4 BSP][8267]
    * [2.5 Manual build][8268]
      * [2.5.1 U-Boot][8269]
        * [2.5.1.1 Sunxi/Legacy U-Boot][8270]
        * [2.5.1.2 Mainline U-Boot][8271]
      * [2.5.2 Linux Kernel][8272]
        * [2.5.2.1 Sunxi/Legacy Kernel][8273]
        * [2.5.2.2 Mainline kernel][8274]
  * [3 Tips, Tricks, Caveats][8275]
    * [3.1 FEL mode][8276]
    * [3.2 Device specific topic][8277]
    * [3.3 ...][8278]
  * [4 Adding a serial port (**voids warranty**)][8279]
    * [4.1 Device disassembly][8280]
    * [4.2 Locating the UART][8281]
  * [5 Pictures][8282]
  * [6 Also known as][8283]
  * [7 See also][8284]
    * [7.1 Manufacturer images][8285]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Model: A1160
    www.azpenpc.com
[/code]
The PCB has the following silkscreened on it: 
[code] 
    INET-A311-REV02
    Zeng-gc-2016-07-28
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: A1160
  * Build Number: 5.1.1-B2016092602

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][8284]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][8286] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][8287] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
The Azpen Hybrix hardware is similar to the Pine64 board. With an external monitor connected to the Azpen Hybrix mini-HDMI connector a number of the SD card images on <http://wiki.pine64.org/index.php/Pine_A64_Software_Release> will boot. The [Ubuntu Mate][8288] provides a pretty usable environment on the machine. However, the device tree does not describe the LCD panel appropriately for this machine, so nothing comes up on the LCD panel. The battery information also seems to be missing. 
The Pine64 kernels from the "pine64-hacks-1.2" branch of <https://github.com/longsleep/linux-pine64.git> can be built locally on the Ubuntu Mate environment and the resulting Image file boots successfully on the Azpen Hybrix. 
Borrowing the devices tree information from the original ReMix OS or Phoenix OS DT to initialization the LCD panel with the Pinebook kernel doesn't work. It looks like a number of the parameters for LCD panel initialization are hard coded in [lcd_edp_anx9804.c][8289] and the values between the Azpen Hybrx and Pinebook differ. 
## FEL mode
A [Bootable SD card][8290] can be used to put the Azpen Hybrx into FEL mode. There doesn't appear to be button to trigger [ FEL mode][8291]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][8292]][8293]
[][8294]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][8295]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][8296].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][8295].
# Pictures
Take some pictures of your device, [ upload them][8297], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Hybrx mainboard2.JPG][8298]][8299]
  * [![Hybrx top.jpg][8300]][8301]
  * [![Hybrx bottom.jpg][8302]][8303]
  * [![Hybrx left.JPG][8304]][8305]
  * [![Hybrx right.jpg][8306]][8307]
  * [![Device board back.jpg][8308]][8309]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
