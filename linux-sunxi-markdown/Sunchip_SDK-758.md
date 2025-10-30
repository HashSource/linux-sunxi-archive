# Sunchip SDK-758
Sunchip SDK-758  
---  
[![SDK-758 front.jpg][51686]][51687]  
Manufacturer |  [Sunchip][51688]  
Dimensions |  101.6 _mm_ x 101.6 _mm_ x 23.6 _mm_  
Release Date |  April 2014   
Website |  [Device Product Page][51689]  
Specifications   
SoC |  [A20][51690] @ 1Ghz   
DRAM |  512MiB DDR3 @ 384MHz   
NAND |  4 GB   
Power |  DC 5.6V @ 2A   
Features   
Video |  HDMI, Composite Video through 3.5mm jack   
Audio |  3.5mm combined Composite AV plug, HDMI   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][51691]), 10/100Mbps Ethernet ([ICplus IP101GA][51692])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][51693] and the [New Device Page guide][51694].
## Contents
  * [1 Identification][51695]
  * [2 Sunxi support][51696]
    * [2.1 Current status][51697]
    * [2.2 Images][51698]
    * [2.3 HW-Pack][51699]
    * [2.4 BSP][51700]
    * [2.5 Manual build][51701]
    * [2.6 Mainline U-Boot][51702]
    * [2.7 Mainline kernel][51703]
  * [3 Tips, Tricks, Caveats][51704]
    * [3.1 AV plug][51705]
    * [3.2 FEL mode][51706]
  * [4 Adding a serial port (**voids warranty**)][51707]
    * [4.1 Device disassembly][51708]
    * [4.2 Locating the UART][51709]
  * [5 Pictures][51710]
  * [6 Also known as][51711]
  * [7 See also][51712]

# Identification
The case of this device has a very distinct and clean look. Other than that it reads the following printed information on the bottom: 
[code] 
    [Android Logo]
    ANDROID TELEVISION BOX
    INPUT : 5V = 2A
    [FCC] [CE] [Do not dispose]
    MADE IN CHINA
    
[/code]
On the bottom of the PCB it says: `SDK-758-V1.0 2013-12-03`
In android, under Settings->About Tablet, you will find: 
  * Model Number: CX_718
  * Build Number: sugar_ref001-eng 4.2.2 JDQ39 20140507 test-keys

# Sunxi support
## Current status
Kernel and u-boot are currently WIP. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][51713]

Everything else is the same as the [manual build howto][51714]. 
## Mainline U-Boot
## Mainline kernel
# Tips, Tricks, Caveats
## AV plug
The 3.5mm RCA AV jack has the following pinout: 
[code] 
    Tip:    Composite
    Ring 1: Audio Left
    Ring 2: Audio Right
    Base:   Ground
    
[/code]
## FEL mode
The "UBOOT" button triggers [ FEL mode][51715]. It is located between UART and the microSD slot. FEL mode is currently not too useful due to the lack of a standard OTG port, but perhaps a special USB Type-A (male-male) cable could work. 
# Adding a serial port (**voids warranty**)
[![][51716]][51717]
[][51718]
UART pads
## Device disassembly
The top lid (shiny part) is held only by plastic notches. Insert your [Plastic tool][51719] between top and bottom case vertically, and carefully work your way round. 
## Locating the UART
RX, TX and GND are clearly marked on the board right next to the microSD slot. Just solder on some wires according to our [UART howto][51720], or you can solder in some 2.54mm pitch connectors like in the picture. 
# Pictures
  * [![SDK-758 front.jpg][51721]][51687]
  * [![SDK-758 side1.jpg][51722]][51723]
  * [![SDK-758 side2.jpg][51724]][51725]
  * [![SDK-758 remote.jpg][51726]][51727]
  * [![SDK-758 board top.jpg][51728]][51729]
  * [![SDK-758 board bottom.jpg][51730]][51731]
  * [![SDK-758 dram.jpg][51732]][51733]
  * [![SDK-758 phy.jpg][51734]][51735]
  * [![SDK-758 pmu flash.jpg][51736]][51737]
  * [![SDK-758 wifi.jpg][51738]][51739]
  * [![SDK-758 case.jpg][51740]][51741]
  * [![SDK-758 lid edge.jpg][51742]][51743]
  * [![SDK-758 base edge.jpg][51744]][51745]

# Also known as
# See also
