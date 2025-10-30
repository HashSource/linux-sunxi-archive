# Biqu CB1
Biqu CB1  
---  
[![Biqu CB1 front.jpg][9996]][9997] [][9998]  
Manufacturer |  [[1]][9999]  
Dimensions |  40 _mm_ x 55 _mm_  
Release Date |  2022   
Website |  [[2]][10000]  
Specifications   
SoC |  [H616][10001] @ 1.512 Ghz   
DRAM |  1GiB DDR3 @ 720 MHz (2x Kingston D2516ECMDXGJD)   
Features   
Video |  2x HDMI (Micro)   
Audio |  HDMI   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][10002]), 10/100Mbps Ethernet ([Manufacturer device][10003])   
Storage |  µSD   
USB |  2/3/4 USB2.0 Host   
Headers |  UART, JTAG, LCD, VGA, ...   
Biqu CB1 is a H616 based board in Raspi Compute Module form factor, requires an extension board to drive(power, GPIO, ports .etc). 
This page needs to be properly filled according to the [New Device Howto][10004] and the [New Device Page guide][10005].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][10006]
  * [2 Sunxi support][10007]
    * [2.1 Current status][10008]
    * [2.2 Images][10009]
    * [2.3 Manual build][10010]
      * [2.3.1 U-Boot][10011]
        * [2.3.1.1 Mainline U-Boot][10012]
      * [2.3.2 Linux Kernel][10013]
        * [2.3.2.1 Mainline kernel][10014]
  * [3 Tips, Tricks, Caveats][10015]
    * [3.1 UART][10016]
  * [4 Adding a serial port (**voids warranty**)][10017]

# Identification
The board has silkscreened: BigTreeTech_CB1_VX.X 
# Sunxi support
## Current status
Board boots and works with downstream 5.16 kernel provided by Biqu. 
## Images
<https://github.com/bigtreetech/CB1/releases>
## Manual build
You can build things for yourself by following our [ Manual build howto][10018] and by choosing from the configurations available below. 
### U-Boot
Use the _h616_defconfig_ build target. 
#### Mainline U-Boot
WIP 
### Linux Kernel
#### Mainline kernel
WIP 
# Tips, Tricks, Caveats
Could not yet figure out how to boot the board in FEL mode 
## UART
# Adding a serial port (**voids warranty**)
Adding UART is very simple. All pins are already on the board. Just need to be soldered to. They are located on top of the board near the H616 SoC
