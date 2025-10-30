# Yones Toptech BS1078
Yones Toptech BS1078  
---  
[![2015-01-03 11.50.32.jpg][63522]][63523]  
Manufacturer |  [Manufacturer][63524]  
Dimensions |  10.31 in x 6.5 in x 0.43 in (26.2 cm x 16.5 cm x 1.1 cm)   
Release Date |  Month year  
Website |  [Device Product Page][63525] [Software][63526]  
Specifications   
SoC |  [A31s][63527] @ 1Ghz (Quad-core Cortex-A7)   
DRAM |  1GB Elixir DDR3-1600 or (2x [Elpida J4216BFBG-GN-F][63528]) (In IROPRO: 2x [Elpida J4216BBBG-DJ-F][63529])   
NAND |  Micron MLC 16GB / 32GB or (2x SH hynix H27UCG8T2ETR) (In IROPRO: INTEL 29F16B08CCME2)   
Power |  DC 5V @ 2A, 6800mAh 3.7V Li-Ion polymer battery (In IROPRO: 6000mAh MODEL:25A0F0 SIZE:90x150x2.5mm)   
Features   
LCD |  LCD 16:9,resolution1024*600 (In IROPRO: boe10.1g40p-wjs)   
Touchscreen |  5-point capacitive touchscreen ([Silead GSL3635][63530]) (In IROPRO: YTG-P10025-F1 V1.0 Chipset: SILEAD GSL3675)   
Video |  Mini HDMI 1.4a 120Hz 720p (Type C)   
Audio |  3.5mm headphone plug, Stereo out through Mini HDMI (Type C), internal stereo speakers (8ohm 0.5w each), internal microphone   
Network |  WiFi 802.11 b/g/n Realtek RTL 8723AS 150mbit/s   
Storage |  External and internal MicroSD card slot expansion (2 expansion slots) SD v3.0   
Camera |  2.0MP (0.3MP 640x480 upscaled to 2MP 1600x1200) rear, 0.3MP (640x480) 1/6.5" CMOS VGA GC0307 front camera module   
Other |  MMA7660 Accelerometer, (In IROPRO: [**FT690M**][63531] 1W Mono Audio Power Amplifier,**KL4** SOT32 BAT54 SMD Schottky Barrier Diode,**ZC33** [AP7335][63532] LINEAR REGULATOR)   
This page needs to be properly filled according to the [New Device Howto][63533] and the [New Device Page guide][63534].
This is a cheap but very good tablet. It has features wich you cannot find in expensive tablets like HDMI, 3D over HDMI etc. Of course it has downsides like low volume speakers, 40nm CPU Die-shrink etc. 
## Contents
  * [1 Identification][63535]
  * [2 Sunxi support][63536]
    * [2.1 Current status][63537]
    * [2.2 Images][63538]
    * [2.3 HW-Pack][63539]
    * [2.4 BSP][63540]
    * [2.5 Manual build][63541]
    * [2.6 Mainline U-Boot][63542]
    * [2.7 Mainline kernel][63543]
  * [3 Tips, Tricks, Caveats][63544]
    * [3.1 FEL mode][63545]
    * [3.2 Device specific topic][63546]
    * [3.3 ...][63547]
  * [4 Adding a serial port (**voids warranty**)][63548]
    * [4.1 Device disassembly][63549]
    * [4.2 Locating the UART][63550]
  * [5 Pictures][63551]
  * [6 Also known as][63552]
  * [7 See also][63553]
    * [7.1 Manufacturer images][63554]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: BS1078

Information about the Android firmware: <http://www.androiddevice.info/submission/18763/show>
On the PCB (Poofek 10.1", also note that the main chip is epoxy-covered) the following is printed: V5-YONESTOPTECH-BS1078-20140901 
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either u-boot or kernel, mention this too, but add the extra sections below.
## Images
Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][63553]. If no sunxi based images are available, this section can be left blank.
## HW-Pack
Add MANUFACTURER DEVICE HW-pack specifics here. This section can be left blank.
## BSP
Add MANUFACTURER DEVICE BSP specifics here. This section can be left blank.
## Manual build
  * For building u-boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [yonestoptech_bs1078.fex][63555]

Everything else is the same as the [manual build howto][63556]. 
## Mainline U-Boot
If there is mainline u-boot support, add this section.
For [ building mainline u-boot][63557], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][63558]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][63559]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][63560]][63561]
[][63562]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][63563]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
  

## Device disassembly
Unscrew 2 screws on the side with the ports, then using small plastic tool open the cover. 
## Locating the UART
The RX and TX connections are labeled and on the front of the mainboard (just above the CPU). The large copper trace on the edge where the connectors are can be used as a ground. Refer to the [UART howto][63563] for more information. 
HYPER TERMINAL SETUP: 115200 8-N-1 Xon/Xoff 
# Pictures
  * [![2015-01-03 11.50.32.jpg][63564]][63523]
  * [![2015-01-03 11.51.07.jpg][63565]][63566]
  * [![2015-01-03 11.51.28.jpg][63567]][63568]
  * [![Poofek inside.jpg][63569]][63570]
  * [![BS1078 - UART position.png][63571]][63572]
  * [![IROPRO BACK.jpg][63573]][63574]
  * [![IROPRO BS1078 UART.jpg][63575]][63561]
  * [![V5-YONESTOPTECH BS1078-20140901 PCB1.jpg][63576]][63577]
  * [![V5-YONESTOPTECH BS1078-20140901 PCB2.jpg][63578]][63579]
  * [![V5-YONESTOPTECH BS1078-20140901 PCB3.jpg][63580]][63581]
  * [![V5-YONESTOPTECH BS1078-20140901 PCB4.jpg][63582]][63583]
  * [![V5-YONESTOPTECH BS1078-20140901 PCB5.jpg][63584]][63585]
  * [![V5-YONESTOPTECH BS1078-20140901 PCB6.jpg][63586]][63587]
  * [![V5-YONESTOPTECH BS1078-20140901 PCB7.jpg][63588]][63589]
  * [![V5-YONESTOPTECH BS1078-20140901 PCB8.jpg][63590]][63591]

# Also known as
Poofek 10.1" 
# See also
[Yones Toptech BD1078][63592]
## Manufacturer images
Optional. Add non-sunxi images in this section.
