# Miyoo PocketGo-S30
Miyoo PocketGo-S30  
---  
[![Miyoo PocketGo-S30 Front.jpg][38279]][38280]  
Manufacturer |  [Miyoo][38281]  
Dimensions |  160 _mm_ x 70 _mm_ x 22 _mm_  
Release Date |  December 2020   
Website |  [Device Product Page][38282]  
Specifications   
SoC |  [A33][38283] [R16][38284] @ 1.2Ghz   
DRAM |  512MB DDR3 @ 552MHz   
NAND |  16MB (zb25q64)   
Power |  DC 5V @ 2A, 2600mAh 3.7V Li-Ion battery   
Features   
LCD |  480x320 (3.5" 3:2) TFT LCD (ili9488)   
Video |  Mali400 MP2 GPU   
Audio |  3.5mm headphone plug, internal mono speaker   
Storage |  µSD   
USB |  1 USB-C Host, 1 USB-C OTG   
Other |  17 GPIO Buttons, 1 Charging LED (Red), 1 Power LED (Blue), PMIC [AXP223][38285]  
Headers |  UART, LCD, Battery, Speaker, Nintendo Joycon Joystick   
## Contents
  * [1 Identification][38286]
  * [2 Sunxi support][38287]
    * [2.1 Current status][38288]
    * [2.2 Images][38289]
      * [2.2.1 mtd0][38290]
      * [2.2.2 mtd1][38291]
      * [2.2.3 mtd2][38292]
      * [2.2.4 mtd3][38293]
      * [2.2.5 mtd4][38294]
      * [2.2.6 mtd5][38295]
    * [2.3 HW-Pack][38296]
    * [2.4 BSP][38297]
    * [2.5 Manual build][38298]
      * [2.5.1 U-Boot][38299]
        * [2.5.1.1 Sunxi/Legacy U-Boot][38300]
        * [2.5.1.2 Mainline U-Boot][38301]
      * [2.5.2 Linux Kernel][38302]
        * [2.5.2.1 Sunxi/Legacy Kernel][38303]
        * [2.5.2.2 Mainline kernel][38304]
    * [2.6 FEL mode][38305]
    * [2.7 ADB][38306]
  * [3 Adding a serial port (**voids warranty**)][38307]
    * [3.1 Device disassembly][38308]
    * [3.2 Locating the UART][38309]
  * [4 Pictures][38310]
  * [5 Schematic][38311]
  * [6 Also known as][38312]
  * [7 See also][38313]
    * [7.1 Manufacturer images][38314]

# Identification
On the back of the device, the following is printed: 
[code] 
    Pocket-Go
    S30 Game Console
    MODEL: PocketGo-S30
    INPUT: 2600MmAh           Made In China
[/code]
The PCB has the following silkscreened on it: 
[code] 
    Miyoo353-B
    2020.11.20
[/code]
Using ADB Shell 
[code] 
    cat /sys/class/sunxi_info/sys_info
    sunxi_platform    : Sun8iw5p1
    sunxi_secure      : normal
    sunxi_chipid      : 000000002af798c78a5460400461872a
    sunxi_chiptype    : Not Supported!
    sunxi_batchno     : 0
[/code]
[code] 
    cat /proc/kmsg
    Linux version 3.4.39 (jf@jf) (gcc version 6.4.1 (OpenWrt/Linaro GCC 6.4-2017.11 2017-11))
[/code]
# Sunxi support
## Current status
Building and running your own build of u-boot and Linux is currently unsupported. The device seems to be running a custom build of u-boot version 1.1.0 and Linux version 3.4.39. 
## Images
[The NAND partition dumps can be found here.][38315]
### mtd0
  * Data offsets
    0x000000: SPL
    0x006000: U-BOOT
    0x056000: script.bin
    0x05F000: MTD name data?

For some reason if you extract the U-BOOT and script.bin from mtd0 it will result in seemingly corrupt or weirdly formatted data, making it unusable. Script.bin however can be successful extracted from memory using the sunxi-script-extractor tool. 
[code] 
    sunxi-script_extractor > script.bin
[/code]
### mtd1
Contains boot.cmd 
### mtd2
Contains image of rootfs 
### mtd3
SquashFS partition containing only a small directory tree. 
[code] 
    /dev/console
    /sbin
[/code]
### mtd4
Contains a single JPG image of the device boot logo. 
### mtd5
The U-DISK 
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][38316] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [PocketGoS30.fex][38317] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
## FEL mode
A specially formatted µSD card can activate [ FEL mode][38318]. It's possible there is a button that can activate FEL mode, but it is currently undiscovered. UART access has not been acquired yet, but it's possible this may also be a potential, undiscovered, option. 
## ADB
The PocketGo-S30 is running ADB, allowing us to access the shell using `adb shell` in a terminal. You can dump the nand partitions onto the µSD card and access other information about the device here. This shell access is how most of the information here has been gathered. 
# Adding a serial port (**voids warranty**)
[![][38319]][38320]
[][38321]
UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][38322]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
Remove two screws on the back of the case. The back case will now pop free and reveal the battery. The battery is double-sided taped down onto the button assembly that holds the L1, R1, L2, and R2 buttons. You can peel it free with relative ease and disconnect it from the header on the left-hand side of the board. Remove the 4 more screws on the button assembly bar will allow it to be easily removed, giving you full access to the motherboard. Be gentle and pop open the little plastic tabs on the the LCD and joystick headers to open and slip out the ribbon cables. Also be sure to remove the speaker connector on the opposite side. You can now unscrew the last 2 remaining screws and remove the motherboard from the front shell housing. The LCD seems to be glued or taped inside the front housing, making removing it destructive. 
## Locating the UART
UART pins can be found right underneath the battery and button assembly. They are the 3 unpopulated pins with a white rectangle around them. The port is enabled and functional, however, the kernel is not configured to use it. For some reason, there is also no output when u-boot is booting. [UART howto][38322]
# Pictures
  * [![Miyoo PocketGo-S30 Front.jpg][38323]][38280]
  * [![Miyoo PocketGo-S30 Back.jpg][38324]][38325]
  * [![Miyoo PocketGo-S30 Board Front.jpg][38326]][38327]
  * [![Miyoo PocketGo-S30 Board Back.jpg][38328]][38329]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
This device seems to have many different names associated with it, and it's hard to determine the original name. The motherboard has _Miyoo353_ on the silkscreen, but the Linux kernel and script.fex seems to call it _zkswe_a33_ internally. The most commonly used name and easily recognizable name is the _PocketGo S30_ or _S30_ for short. 
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
