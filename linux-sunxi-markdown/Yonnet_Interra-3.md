# Yonnet Interra-3
Yonnet Interra-3  
---  
[![Device front.jpg][63711]][63712]  
Manufacturer |  [YONNET][63713]  
Dimensions |  '155mm' x '1.6mm' x '80mm'   
Release Date |  May 2014   
Website |  [Device Product Page][63714]  
Specifications   
SoC |  [A20][63715] @ 1Ghz   
DRAM |  1GiB/2GiB DDR3 @ 456MHz   
eMMC |  8Gb SANDISK SDIN7DU2-8G   
NAND |  \-   
Power |  DC 12V @ 2A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  1280x800 (10.1" 16:10)   
Touchscreen |  5-finger capacitive/resistive ([Manufacturer device][63716] FIXME)   
Video |  HDMI,   
Audio |  PAM8620 HP to SPK amplifier   
Network |  100Mbps Ethernet   
Storage |  µSD, SATA   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Camera |  5MP (1280x720p) rear   
Other |  none   
Headers |  UART, LCD, ...   
This page needs to be properly filled according to the [New Device Howto][63717] and the [New Device Page guide][63718].
Interra-3 is an A20 based Smart Home automation board. It doesn't include any NAND, but instead has an eMMC. 
## Contents
  * [1 Identification][63719]
  * [2 Sunxi support][63720]
    * [2.1 Current status][63721]
    * [2.2 Images][63722]
    * [2.3 HW-Pack][63723]
    * [2.4 BSP][63724]
    * [2.5 Manual build][63725]
  * [3 Tips, Tricks, Caveats][63726]
    * [3.1 FEL mode][63727]
  * [4 Adding a serial port (**voids warranty**)][63728]
    * [4.1 Locating the UART][63729]
  * [5 Pictures][63730]
  * [6 Also known as][63731]
  * [7 See also][63732]

# Identification
Current PCB version is 3.0, under mass production.. 
# Sunxi support
## Current status
Board is running sunxi uboot and sunxi kernel 3.4.79, with debian wheezy rootfs. 
## Images
This is a proprietary product, therefore its images can not be published here :( 
## HW-Pack
Does not exist. The board runs Android 4.2.2 and sunxi kernel. A working linux system can be built easily similar to any other A20 based device. 
## BSP
Does not exists. 
## Manual build
  * For building u-boot, use the "Interra-3" target.
  * The .fex file can be found in sunxi-boards as [interra-3.fex][63733]

Everything else is the same as the [manual build howto][63734]. 
# Tips, Tricks, Caveats
The board has two buttons, one is RESET and the other is RECOVERY. 
## FEL mode
In order to enter Recovery mode, either press RECOVERY button, or use fel-sdboot binary 
# Adding a serial port (**voids warranty**)
Please see below. 
## Locating the UART
The board has 3.3V TTL UART DEBUG port on it directly visible ( and written ) on the PCB silkscreen. 
# Pictures
Product's images can not be published at the moment :( 
  * [![Device front.jpg][63735]][63712]
  * [![Device back.jpg][63736]][63737]
  * [![Device buttons 1.jpg][63738]][63739]
  * [![Device buttons 2.jpg][63740]][63741]
  * [![Device board front.jpg][63742]][63743]
  * [![Device board back.jpg][63744]][63745]

# Also known as
Interra-3 
# See also
None...
