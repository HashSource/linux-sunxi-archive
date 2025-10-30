# Nintendo Super NES Classic Edition
Nintendo Super NES Classic Edition  
---  
[![Device front.jpg][39990]][39991]  
Manufacturer |  [Manufacturer][39992]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year  
Website |  [Device Product Page][39993]  
Specifications   
SoC |  [AXX][39994] @ XGhz   
DRAM |  512MiB/1GiB/2GiB DDR3 @ xxxMHz   
NAND |  2/4/8/16GB   
Power |  DC 5V @ 3A, 3700mAh 3.7V Li-Ion battery   
Features   
LCD |  WidthxHeight (X" X:Y)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][39995])   
Video |  HDMI (Type A/B/C - full/mini/micro), VGA   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][39996]), 10/100/1000Mbps Ethernet ([Manufacturer device][39997])   
Storage |  µSD, SATA   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][39998]), GPS, IRDA   
Headers |  UART, JTAG, LCD, VGA, ...   
This page needs to be properly filled according to the [New Device Howto][39999] and the [New Device Page guide][40000].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][40001]
  * [2 Sunxi support][40002]
    * [2.1 Current status][40003]
    * [2.2 Images][40004]
    * [2.3 HW-Pack][40005]
    * [2.4 BSP][40006]
    * [2.5 Manual build][40007]
      * [2.5.1 U-Boot][40008]
        * [2.5.1.1 Sunxi/Legacy U-Boot][40009]
        * [2.5.1.2 Mainline U-Boot][40010]
      * [2.5.2 Linux Kernel][40011]
        * [2.5.2.1 Sunxi/Legacy Kernel][40012]
        * [2.5.2.2 Mainline kernel][40013]
  * [3 Tips, Tricks, Caveats][40014]
    * [3.1 FEL mode][40015]
    * [3.2 Device specific topic][40016]
    * [3.3 ...][40017]
  * [4 Adding a serial port (**voids warranty**)][40018]
    * [4.1 Device disassembly][40019]
    * [4.2 Locating the UART][40020]
  * [5 Pictures][40021]
  * [6 Also known as][40022]
  * [7 Nintendo GPL Violations][40023]
    * [7.1 U-Boot GPL Violations][40024]
    * [7.2 Kernel GPL Violations][40025]
  * [8 See also][40026]
    * [8.1 Manufacturer images][40027]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Manufacturer Marketing Name
    ModelNumber
[/code]
The PCB has the following silkscreened on it: 
[code] 
    LIA-BB-V6.66
    1970-01-01
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][40026]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][40028] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][40029] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][40030]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][40031]][40032]
[][40033]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][40034]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][40035].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][40034].
# Pictures
Take some pictures of your device, [ upload them][40036], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][40037]][39991]
  * [![Device back.jpg][40038]][40039]
  * [![Device buttons 1.jpg][40040]][40041]
  * [![Device buttons 2.jpg][40042]][40043]
  * [![Device board front.jpg][40044]][40045]
  * [![Device board back.jpg][40046]][40047]

# Also known as
List rebadged devices here.
# Nintendo GPL Violations
Nintendo uses the A33/R16 in its products. Nintendo provides [a source code zipfile on their website][40048], in an attempt to comply with open source licenses, but Nintendo ends up distributing the same binaries that Allwinner has been distributing with it's supposed source code releases before. 
## U-Boot GPL Violations
In the subdirectory called r16-uboot-371a64b6922f4b4a63be022768e251d0c1a6fa87, a patched u-boot 2011-09-rc1, the following binaries can be found:
[code]
    ./nand_sunxi/sun8iw3/libnand-sun8iw3
    ./nand_sunxi/sun8iw1/libnand-sun8iw1
    ./nand_sunxi/sun8iw8/libnand-sun8iw8
    ./nand_sunxi/sun9iw1/libnand-sun9iw1
    ./nand_sunxi/sun7i/libnand-sun7i
    ./nand_sunxi/sun8iw9/libnand-sun8iw9
    ./nand_sunxi/sun8iw7/libnand-sun8iw7
    ./nand_sunxi/sun5i/libnand-sun5i
    ./nand_sunxi/sun8iw6/libnand-sun8iw6
    ./board/sunxi/sun8iw7/box_standby/cpus_pm/cpus_pm_binary.code
    ./board/sunxi/sun8iw6/box_standby/cpus_pm/cpus_pm_binary.code
    ./arch/arm/cpu/armv7/sun8iw5/dram/libdram-riot
    ./arch/arm/cpu/armv7/sun8iw5/dram/libdram
    ./arch/arm/cpu/armv7/sun8iw8/dram/libdram
    ./arch/arm/cpu/armv7/sun9iw1/dram/libdram
    ./arch/arm/cpu/armv7/sun8iw9/dram/libdram
    ./arch/arm/cpu/armv7/sun8iw7/dram/libchipid
    ./arch/arm/cpu/armv7/sun8iw7/dram/libdram
    ./arch/arm/cpu/armv7/sun8iw6/dram/libdram-homlet
    ./arch/arm/cpu/armv7/sun8iw6/dram/libdram-pad
    ./drivers/video_sunxi/sunxi_v1/obj_video
    ./drivers/video_sunxi/sunxi_v2/de_bsp/hdmi/aw/libhdcp
    ./drivers/video_sunxi/sunxi_v2/de_bsp/de/lowlevel_sun9iw1/libdsi
    ./drivers/video_sunxi/sunxi_v2/de_bsp/de/lowlevel_sun9iw1/libedp
    ./drivers/video_sunxi/sunxi_v2/obj_video
    ./drivers/video_sunxi/sunxi_v3/obj_video
    
[/code]
In the subdirectory called r16-uboot-99c8444be7ac661b24c684d6615caf14dd9a1178, a patched u-boot 2011-09-rc1, the following binaries can be found:
[code]
    ./nand_sunxi/sun8iw3/libnand-sun8iw3
    ./nand_sunxi/sun8iw1/libnand-sun8iw1
    ./nand_sunxi/sun8iw8/libnand-sun8iw8
    ./nand_sunxi/sun9iw1/libnand-sun9iw1
    ./nand_sunxi/sun7i/libnand-sun7i
    ./nand_sunxi/sun8iw9/libnand-sun8iw9
    ./nand_sunxi/sun8iw7/libnand-sun8iw7
    ./nand_sunxi/sun5i/libnand-sun5i
    ./nand_sunxi/sun8iw6/libnand-sun8iw6
    ./board/sunxi/sun8iw7/box_standby/cpus_pm/cpus_pm_binary.code
    ./board/sunxi/sun8iw6/box_standby/cpus_pm/cpus_pm_binary.code
    ./arch/arm/cpu/armv7/sun8iw5/dram/libdram-riot
    ./arch/arm/cpu/armv7/sun8iw5/dram/libdram
    ./arch/arm/cpu/armv7/sun8iw8/dram/libdram
    ./arch/arm/cpu/armv7/sun9iw1/dram/libdram
    ./arch/arm/cpu/armv7/sun8iw9/dram/libdram
    ./arch/arm/cpu/armv7/sun8iw7/dram/libchipid
    ./arch/arm/cpu/armv7/sun8iw7/dram/libdram
    ./arch/arm/cpu/armv7/sun8iw6/dram/libdram-homlet
    ./arch/arm/cpu/armv7/sun8iw6/dram/libdram-pad
    ./drivers/video_sunxi/sunxi_v1/obj_video
    ./drivers/video_sunxi/sunxi_v2/de_bsp/hdmi/aw/libhdcp
    ./drivers/video_sunxi/sunxi_v2/de_bsp/de/lowlevel_sun9iw1/libdsi
    ./drivers/video_sunxi/sunxi_v2/de_bsp/de/lowlevel_sun9iw1/libedp
    ./drivers/video_sunxi/sunxi_v2/obj_video
    ./drivers/video_sunxi/sunxi_v3/obj_video
    
[/code]
## Kernel GPL Violations
In the subdirectory called linux-e1d8f93d058c1de94831eb1d69021633aa5fe9af, a patched linux-3.4.113, the following binaries can be found:
[code]
    ./arch/arm/mach-sunxi/pm/standby/sun9i_resume1_scatter.scat
    ./arch/arm/mach-sunxi/pm/standby/sun8i_resume1_scatter.scat
    ./arch/arm/mach-sunxi/pm/standby/standby.xn
    ./arch/arm/mach-sunxi/pm/standby/gen_check_code
    ./modules/aw_schw/libschw
    ./modules/nand/sun8iw1p1/libnand_sun8iw1p1
    ./modules/nand/sun8iw3p1/libnand_sun8iw3p1
    ./modules/nand/sun8iw5p1/libnand_sun8iw5p1
    ./modules/nand/sun9iw1p1/libnand_sun9iw1p1
    ./modules/nand/sun8iw6p1/libnand_sun8iw6p1
    ./drivers/video/sunxi/disp/de/lowlevel_sun9iw1/libdsi
    ./drivers/video/sunxi/disp/de/lowlevel_sun9iw1/libedp
    ./drivers/video/sunxi/hdmi/aw/libhdcp
    ./drivers/arisc/binary/arisc_sun8iw6p1.code
    ./drivers/arisc/binary/arisc_sun8iw3p1.code
    ./drivers/arisc/binary/arisc_sun8iw5p1.code
    ./drivers/arisc/binary/arisc_sun8iw1p1.code
    ./drivers/arisc/binary/arisc_sun9iw1p1.code
    ./drivers/input/touchscreen/aw5x06/libAW5306
    ./drivers/input/touchscreen/gslx680new/gsl_point_id_20131111
    ./drivers/input/touchscreen/ft5x/ft_app.i
    ./drivers/usb/sunxi_usb/usb3/libusb300
    ./drivers/devfreq/dramfreq/mdfs/mdfs_sun8iw6p1.code
    ./drivers/devfreq/dramfreq/mdfs/mdfs_sun8iw3p1.code
    ./drivers/media/video/sunxi-fd/lib/libfd
    ./drivers/media/video/sunxi-vfe/lib/libisp
    ./drivers/media/video/sunxi-vfe/lib/lib_mipicsi2_v1
    ./drivers/media/video/sunxi-vfe/lib/lib_mipicsi2_v2
[/code]
In the subdirectory called linux-e50bc29a890dc11e90db28f9e857bb8a08464c5f, a patched linux-3.4.113, the following binaries can be found:
[code]
    ./arch/arm/mach-sunxi/pm/standby/sun9i_resume1_scatter.scat
    ./arch/arm/mach-sunxi/pm/standby/sun8i_resume1_scatter.scat
    ./arch/arm/mach-sunxi/pm/standby/standby.xn
    ./arch/arm/mach-sunxi/pm/standby/gen_check_code
    ./modules/aw_schw/libschw
    ./modules/nand/sun8iw1p1/libnand_sun8iw1p1
    ./modules/nand/sun8iw3p1/libnand_sun8iw3p1
    ./modules/nand/sun8iw5p1/libnand_sun8iw5p1
    ./modules/nand/sun9iw1p1/libnand_sun9iw1p1
    ./modules/nand/sun8iw6p1/libnand_sun8iw6p1
    ./drivers/video/sunxi/disp/de/lowlevel_sun9iw1/libdsi
    ./drivers/video/sunxi/disp/de/lowlevel_sun9iw1/libedp
    ./drivers/video/sunxi/hdmi/aw/libhdcp
    ./drivers/arisc/binary/arisc_sun8iw6p1.code
    ./drivers/arisc/binary/arisc_sun8iw3p1.code
    ./drivers/arisc/binary/arisc_sun8iw5p1.code
    ./drivers/arisc/binary/arisc_sun8iw1p1.code
    ./drivers/arisc/binary/arisc_sun9iw1p1.code
    ./drivers/input/touchscreen/aw5x06/libAW5306
    ./drivers/input/touchscreen/gslx680new/gsl_point_id_20131111
    ./drivers/input/touchscreen/ft5x/ft_app.i
    ./drivers/usb/sunxi_usb/usb3/libusb300
    ./drivers/devfreq/dramfreq/mdfs/mdfs_sun8iw6p1.code
    ./drivers/devfreq/dramfreq/mdfs/mdfs_sun8iw3p1.code
    ./drivers/media/video/sunxi-fd/lib/libfd
    ./drivers/media/video/sunxi-vfe/lib/libisp
    ./drivers/media/video/sunxi-vfe/lib/lib_mipicsi2_v1
    ./drivers/media/video/sunxi-vfe/lib/lib_mipicsi2_v2
[/code]
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
