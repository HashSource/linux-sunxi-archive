# MYD-YT113X
MYD-YT113X  
---  
[![MYD-YT113X front.jpg][33609]][33610]  
Manufacturer |  [MYiR][33611]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  April 2023   
Website |  [Device Product Page][33612]  
Specifications   
SoC |  T133 @ 1GHz   
DRAM |  128Mb   
NAND |  4Gb EMMC or 256Mb NAND, 32Kb EEPROM   
Power |  DC 12V @ 2A   
Features   
Audio |  1x 4-pin audio-out header   
Network |  1Gbit ethernet, FNLink 6131E-U (RTL8731BU)   
Storage |  µSD   
USB |  FE1.1 USB hub, 2 USB2.0 Host, 1x USB_OTG, 1x USB debug   
Other |  4G slot (USB in mPCIe connector), 2x SIM slots, hardware power switch, ADC, LCD   
Headers |  UART, LCD   
This page needs to be properly filled according to the [New Device Howto][33613] and the [New Device Page guide][33614].
The board consists of the baseboard (MYD-YT113X) and a CPU SoM (MYTC-YT113S3). The CPU SoM is sold separately as well. 
## Contents
  * [1 Identification][33615]
  * [2 Sunxi support][33616]
    * [2.1 Current status][33617]
    * [2.2 BSP][33618]
    * [2.3 Manual build][33619]
      * [2.3.1 U-Boot][33620]
      * [2.3.2 Linux Kernel][33621]
  * [3 Tips, Tricks, Caveats][33622]
    * [3.1 Locating the UART][33623]
  * [4 Pictures][33624]
  * [5 External links][33625]

# Identification
CPU module / SoM: 
[code] 
    MYC-YT113S3-256N1 (SPINAND)
[/code]
[code] 
    MYC-YT113S3-4E128 (eMMC)
[/code]
The baseboard has the following silkscreened on it: 
[code] 
    MYB-YT113X-V10
    1970-01-01
[/code]
# Sunxi support
## Current status
U-boot and mainline kernel support is being worked on. 
## BSP
BSP is available at <http://d.myirtech.com/MYD-YT113X/>
## Manual build
### U-Boot
Mainline u-boot is Being worked on, based on Andre's T113 patchset. 
### Linux Kernel
Being worked on. 
# Tips, Tricks, Caveats
The DEBUG (J4) can be jumpered at JP2 and JP3 to use ttyS0 or ttyS5. Default is ttyS5. If ttyS0 is jumpered, booting from MMC will not work. 
The ethernet PHY is a Motorcomm YT8531SH, which is mainly used on the StarFive VisionFive 2 board. There is no support in mainline u-boot for this PHY yet. 
## Locating the UART
Located at J4 DEBUG connector. 
# Pictures
  * [![MYD-YT113X front.jpg][33626]][33610]
  * [![MYD-YT113X back.jpg][33627]][33628]
  * [![MYD-YT113X connectors.jpg][33629]][33630]
  * [![MYD-YT113X uart.jpg][33631]][33632]
  * [![MYD-YT113X wifi.jpg][33633]][33634]

# External links
[code] 
    [Hardware manual / schematics][33635]
    
[/code]
