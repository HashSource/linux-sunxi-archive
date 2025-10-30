# Empire ElectroniX M712
Empire ElectroniX M712  
---  
[![Device front.png][18076]][18077]  
Manufacturer |  Empire ElectroniX [[1]][18078]  
Dimensions |  193mm x 120mm x 7mm   
Release Date |  September 2012   
Website |  unknown   
Specifications   
SoC |  [A13][18079] @ 1.2Ghz   
DRAM |  512MiB DDR3 @ 408MHz   
NAND |  4GB   
Power |  DC 5V @ 1.5A, 2500mAh 3.7V Li-Ion battery   
Features   
LCD |  7", 800 x 480, 16:9   
Touchscreen |  5-finger capacitive (KR070PE4T), Controler: GOODIX GT811   
Video |  None   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (REALTEK RTL8188EUS)   
Storage |  µSD (up to 32GB)   
USB |  1x mini USB2.0 (Host or OTG)   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer (±2g tri-axial digital accelerometer DMT ARD06)   
Headers |  UART, JTAG, LCD, VGA, ...   
  

## Contents
  * [1 Identification][18080]
  * [2 Sunxi support][18081]
    * [2.1 Current status][18082]
    * [2.2 Images][18083]
    * [2.3 HW-Pack][18084]
    * [2.4 BSP][18085]
    * [2.5 Manual build][18086]
      * [2.5.1 U-Boot][18087]
        * [2.5.1.1 Sunxi/Legacy U-Boot][18088]
        * [2.5.1.2 Mainline U-Boot][18089]
      * [2.5.2 Linux Kernel][18090]
        * [2.5.2.1 Sunxi/Legacy Kernel][18091]
        * [2.5.2.2 Mainline kernel][18092]
        * [2.5.2.3 Rootfs][18093]
  * [3 Tips, Tricks, Caveats][18094]
    * [3.1 FEL mode][18095]
    * [3.2 Device specific topic][18096]
    * [3.3 ...][18097]
  * [4 Adding a serial port (**voids warranty**)][18098]
    * [4.1 Device disassembly][18099]
    * [4.2 Locating the UART][18100]
  * [5 Pictures][18101]
  * [6 Also known as][18102]
  * [7 See also][18103]
    * [7.1 Manufacturer images][18104]

# Identification
On the back of the device, the following is printed: 
[code] 
    Empire ElectroniX
    S/N:EMPR20147124GB000087
[/code]
The PCB has the following silkscreened on it: 
[code] 
    XW712-V1.2
    2012-8-8
    QL20 12.43
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: Compatible-A13-eng- 4.2.2 JDQ39 by Toxicro
  * Build Number:

This is not useful information and may not be the original string of the tablet. The device was identified by searching the internet and finding the manual. 
  

# Sunxi support
## Current status
Supported: Boot from SD card, Touchscreen, Audio, WiFi, USB, Ethernet over USB-Adapter 
Both mainline and sunxi U-Boot work. There is no mainline kernel support but sunxi-3.4 kernel properly supports the device with Debian LXDE root file system. 
Not tested so far: accelerometer, camera 
## Images
## HW-Pack
## BSP
## Manual build
You can build things for yourself by following our [ Manual build howto][18105] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the "Empire_electronix_m712" build target. 
#### Mainline U-Boot
Use the "Empire_electronix_m712" build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Sunxi/Legacy Kernel provides more drivers than mainline. Use the [[2]][18106] file. 
#### Mainline kernel
Not used. 
#### Rootfs
tested succesfully: non-graphical [[[3]][18107]] graphical (minimal LXDE) [[4]][18108] graphical (LXDE, self built) [[[5]][18109]] 
  

# Tips, Tricks, Caveats
Don't forget to have the modules loaded upon boot (not all may be built into the kernel). 
## FEL mode
Turn device off. Press power button and hold down; after 2-3s push additionally Vol- 4-6 times quickly 
  

## Device specific topic
## ...
# Adding a serial port (**voids warranty**)
[![][18110]][18111]
[][18112]
DEVICE UART pads
[UART howto][18113]
## Device disassembly
Remove the screw under the SD-card slot cover. Looking at the screen carefully use your finger nails and/or a plastic tool to snap off the backcover. Start at the buttons and open the top and left side first. Then continue all the way around. Remove the backcover completely. There are screws that hold the board, but since there is nothing useful on the back of the board it is usually not necessary to remove them. 
[Plastic tool howto][18114]. 
## Locating the UART
UART1-Pads are next to the Pins 151 and 152 (below of the SoC). (red circle: RX left, TX right) 
# Pictures
  * [![Device front.png][18115]][18077]
  * [![Device back.png][18116]][18117]
  * [![Device open.png][18118]][18119]
  * [![Device inside.png][18120]][18121]
  * [![Device back of board.png][18122]][18123]
  * [![Boot screen.png][18124]][18125]

# Also known as
# See also
## Manufacturer images
