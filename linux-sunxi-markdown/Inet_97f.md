# Inet 97f
Inet 97f  
---  
[![Device front.jpg][26705]][26706]  
Manufacturer |  [Inet-Tek][26707]  
Dimensions |  192 _mm_ x 124 _mm_ x 12.8 _mm_  
Release Date |  January 2012   
Website |  [Device Product Page][26708]  
Specifications   
SoC |  [A10][26709] @ 1Ghz   
DRAM |  512MiB DDR3 @ 408MHz   
NAND |  4GB   
Power |  DC 5V @ 2A, different 3.7V Li-Ion batteries.   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive/resistive ([Goodix GT80x][26710] or [Solomon Systemtech Ltd. SSD2533][26711])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (Unknown Realtek device(s))   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Manufacturer device][26712] FIXME)   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][26713] and the [New Device Page guide][26714].
The Inet 97F was one of the earliest Allwinner based tablets and, due to its low price, got sold under many many guises, and with many different options. These changes are different battery sizes, wifi modules, touchscreen controllers, camera modules, and of course slightly differing cases. 
## Contents
  * [1 Identification][26715]
  * [2 Sunxi support][26716]
    * [2.1 Current status][26717]
    * [2.2 Images][26718]
    * [2.3 HW-Pack][26719]
    * [2.4 BSP][26720]
    * [2.5 Manual build][26721]
      * [2.5.1 Yarvik Tab 260/264][26722]
    * [2.6 Mainline kernel][26723]
  * [3 Tips, Tricks, Caveats][26724]
    * [3.1 FEL mode][26725]
  * [4 Adding a serial port (**voids warranty**)][26726]
    * [4.1 Device disassembly][26727]
    * [4.2 Locating the UART][26728]
  * [5 Pictures][26729]
    * [5.1 Yarvik 26x internals][26730]
  * [6 Cherry M667 internals][26731]
  * [7 Visual Land VL879][26732]
  * [8 Also known as][26733]
  * [9 See also][26734]

# Identification
In android, under Settings->About Tablet, you can look at the Build Number, and it should start with **97F2** , like for the Yarvik Tab260: 
  * Model Number: TAB260
  * Build Number: 97F2-R1-H1-H01-1366.20111219

Most rebadgers did succeed in changing the Model Number. 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
Clarify why these are 2 different fex files, one for the [inet97f-ii.fex][26735] and the one below.
### Yarvik Tab 260/264
  * For building u-boot, use the "INet97F-II" target.
  * The .fex file can be found in sunxi-boards as [yarvik_tab260.fex][26736]

Everything else is the same as the [manual build howto][26737]. 
## Mainline kernel
Use the sun4i-a10-inet97fv2.dts device-tree file for the [mainline kernel][26738]. 
# Tips, Tricks, Caveats
## FEL mode
The volume up button triggers [ FEL mode][26739]. 
# Adding a serial port (**voids warranty**)
[![][26740]][26741]
[][26742]
TTL connections
## Device disassembly
The precise disassembly procedure varies per brand since each put a different case around the board. The Cherry M667 has a screwless plastic case that consists of a white back and a black front. After inserting a thin flat screwdriver the white back can easily be pushed off of the rest of the device. 
It helps that for most tablets the plastic case will have a lot of empty space, since the iNet-97F board is less than half the size of the display. Put the tablet with its screen facing down, then use your hands to knock on the back cover to find any hollow areas. Those would be good places to start with the screwdriver. 
Inside the device you should find a few tiny screws to hold the PCB in place (about 5), but most things are held together by tape. In the Cherry M667 the battery pack was tightly taped to the back of the display assembly. It could only be removed by guessing where the tape was (3 strips: 1 on top, 1 in the middle, 1 below) and sticking a screwdriver underneath to cut the tape. 
Be very careful when removing the display assembly: its metal casing is not sealed shut very well and bends easily. In the Cherry M667 the touchscreen module is glued to the black plastic frontpanel, so when you pull out the LCD module you separate touchscreen and display. Be careful not to damage the touchscreen. 
## Locating the UART
The [UART][26743] seems to be the 3 big pads in the bottom left corner of the board. From left to right they are: GND, RX (connect to the TX on your TTL adapter), and TX (connect to the RX on your TTL adapter). If you connect a voltmeter between GND and RX (or GND and TX) you should measure around 3 V. 
The connection has been tested with a CP2102 USB to UART adapter, but others should work fine too. Do not connect the +3.3V or +5V VCC from your adapter to the PCB, this is not necessary. 
The pads are quite close to eachother. To make your life a little easier the GND runs around the edge of the board, so you have a lot of freedom to choose where to connect that wire. 
Serial speed is 115200. 
# Pictures
Take some pictures of your device, [ upload them][26744], and add them here.
  * [![Device front.jpg][26745]][26706]
  * [![Device back.jpg][26746]][26747]
  * [![Device buttons 1.jpg][26748]][26749]
  * [![Device buttons 2.jpg][26750]][26751]
  * [![Device board front.jpg][26752]][26753]
  * [![Device board back.jpg][26754]][26755]

## Yarvik 26x internals
  * [![Yarvik Tab26x full.jpg][26756]][26757]
  * [![Yarvik Tab26x PCB01.jpg][26758]][26759]
  * [![Yarvik Tab26x PCB02.jpg][26760]][26761]
  * [![Yarvik Tab26x PCB03.jpg][26762]][26763]
  * [![Yarvik Tab26x PCB04.jpg][26764]][26765]
  * [![Yarvik Tab26x PCB05.jpg][26766]][26767]
  * [![Yarvik Tab26x PCB06.jpg][26768]][26769]
  * [![Yarvik Tab26x PCB07.jpg][26770]][26771]
  * [![Yarvik Tab26x PCB08.jpg][26772]][26773]
  * [![Inet 97f Flash clopseup 01.JPG][26774]][26775]
  * [![Inet 97f Flash clopseup 01 annotated.JPG][26776]][26777]

# Cherry M667 internals
  * [![Inet97f.jpg][26778]][26779]

# Visual Land VL879
  * [![VL879 Front.jpg][26780]][26781]
  * [![VL-879 back.jpg][26782]][26783]
  * [![VL-879 Edge.jpg][26784]][26785]
  * [![VL-879 Internals.jpg][26786]][26787]
  * [![VL-879 Serial.jpg][26788]][26789]

# Also known as
  * [Yarvik Tab224 GoTab Velocity 7"][26790] This claims to have a 4000mAh battery.
  * [Yarvik Tab260 GoTab Velocity 7"][26791] This claims to have a 4200mAh battery.
  * [Yarvik Tab264 GoTab Velocity 7"][26792] Same as Tab260.
  * Primux Tech M705F Bora 7"
  * [mpmap MID74C][26793] This has a 3500mAh battery, and different buttons.
  * Zero Tablet 7 inc, this tablet mount mb rev. 03

Other possible names include (according to [this forum post][26794], unverified) 
  * A71C
  * Benss B7
  * CherryPad Edwin C807 / M-677
  * Cougar Boxchip A10C
  * Intertoys Qware Pro 3
  * iView 760TPC
  * Eroda M701C
  * [mobiitab 7][26795]
  * Micromax funbook P300
  * Odys Xelio
  * Ployer Momo9
  * Picopad 7
  * Scroll Excel 3D
  * Skypad Alpha 2
  * Sumvision Cyclone Astro
  * Tracer OVO
  * VeeDee D10
  * vitalASC Center-ST0716
  * Visual Land VL-879
  * Wanxin TA-7B
  * [Woxter PC-65 CXi][26796]
  * X10 AirPad 7p

# See also
