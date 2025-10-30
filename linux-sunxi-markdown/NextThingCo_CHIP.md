# NextThingCo CHIP
NextThingCo CHIP  
---  
[![C-H-I-P SBC.JPG][39704]][39705]  
Manufacturer |  [Next Thing Co.][39706]  
Dimensions |  62 _mm_ x 41 _mm_ x 11/15 _mm_  
Release Date |  December 2015   
Website |  [Chip Product Page][39707]  
Specifications   
SoC |  [R8][39708] @ 1Ghz   
DRAM |  512MiB DDR3-800E @ 360MHz, timings: 6-6-6-14 (uboot timings) (K4B4G1646Q-HYK0)   
NAND |  4GB   
Power |  DC 5V @ ~1A, 3.7V Li-Ion battery (Not included)   
Features   
Video |  Composite with 3.5mm to RCA A/V adapter   
Audio |  3.5mm to RCA A/V adapter   
Network |  WiFi 802.11 b/g/n d/e/h/i Bluetooth v4 (rtl8723bs)   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Other |  ...  
Headers |  ...  
This page needs to be properly filled according to the [New Device Howto][39709] and the [New Device Page guide][39710].
CHIP (C.H.I.P.) was a single-board computer crowdfunded by now-defunct Next Thing Co. (NTC), released as open-source hardware running open-source software. CHIP and related products are discontinued. 
## Contents
  * [1 Identification][39711]
  * [2 Sunxi support][39712]
    * [2.1 Current status][39713]
    * [2.2 Manual build][39714]
      * [2.2.1 U-Boot][39715]
        * [2.2.1.1 Sunxi/Legacy U-Boot][39716]
        * [2.2.1.2 Mainline U-Boot][39717]
        * [2.2.1.3 NextThingCo U-Boot][39718]
      * [2.2.2 Linux Kernel][39719]
        * [2.2.2.1 Sunxi/Legacy Kernel][39720]
        * [2.2.2.2 Mainline kernel][39721]
        * [2.2.2.3 NextThingCo kernel][39722]
    * [2.3 Locating the UART][39723]
    * [2.4 FEL mode][39724]
    * [2.5 Pinout][39725]
  * [3 Tips, Tricks, Caveats][39726]
    * [3.1 Device specific topic][39727]
    * [3.2 Flashing CHIP OS with CHIP-tools (host computer on Debian/Ubuntu)][39728]
    * [3.3 Flashing CHIP OS (host computer on MacOS)][39729]
  * [4 Dips][39730]
  * [5 Pictures][39731]
  * [6 Variants][39732]
  * [7 Also known as][39733]
  * [8 See also][39734]
    * [8.1 Manufacturer images][39735]

# Identification
On the back of the device, the following is printed: 
[code] 
    CHIP v1.0
[/code]
# Sunxi support
## Current status
CHIP has some support in mainline U-Boot and kernel (defconfig and device tree). Mainline U-boot can boot an OS via USB. CHIP's builtin SLC NAND is not supported by Mainline U-Boot. NextThings version of U-boot supports the builtin NAND. 
## Manual build
You can build things for yourself by following our [ Manual build howto][39736] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Chip is not supported by Sunxi/Legacy U-Boot 
#### Mainline U-Boot
Use the **CHIP_defconfig** build target. Follow these [instructions][39737] to build Mainline U-Boot. You can now use _u-boot-sunxi-with-spl.bin_ via [sunxi-fel][39738] or write Mainline U-Boot to the builtin NAND with the help of NextThingCo's custom U-Boot version. 
#### NextThingCo U-Boot
Chip was shipped with a custom version of U-Boot supporting the SLC NAND. An archived version of the git-repo can be found [here][39739]
### Linux Kernel
#### Sunxi/Legacy Kernel
Not supported. 
#### Mainline kernel
Use the **sun5i-r8-chip.dtb** device-tree binary. Mainline kernel can not interact with the builtin NAND. 
#### NextThingCo kernel
Archived version of NextThingCo's git-repo [here][39740]. NextThingCo's patched linux kernel supports the builtin NAND. 
## Locating the UART
The UART located is on the header named U14. On this header Pin 1 is Ground (GND), Pin 3 is TX (Transmit) and Pin 5 is RX (Recieve). To establish a connection the TX of the Chip must be connected to the RX of USB-UART Converter and the RX of the Adapter to the TX of the Chip, Ground is connected to Ground. Do **NOT** Connect 5V or 3V to the Chip. Please note that the UART of the Chip uses **3.3V** ( RX of the Chip is 5V tolerant ). 
  

[code] 
       GND -> GND on the CHIP
       TX -> UART1-RX on the CHIP
       RX -> UART1-TX on the CHIP
    
[/code]
  

## FEL mode
Shorting out the FEL and GND pins before connecting power will cause the device to boot in [ FEL mode][39741]. 
## Pinout
Header U13L | Header U13R | Header U14L | Header U14R   
---|---|---|---  
Ground | Charge (5V) | Ground | VCC 5V   
VCC 5V | Ground | UART1 TX | Audio out left   
VCC 3V | Temperature sensor input | UART1 RX | Audio out ground   
VCC 1.8V | LIPO battery | FEL | Audio out right   
two wire SDA | power on | VCC 3V | mic mute   
two wire SCK | Ground | ADC | audio in   
X1 touch input | X2 touch input | XIO-P0 GPIO | XIO-P1 GPIO   
Y1 touch input | Y2 touch input | XIO-P2 GPIO | XIO-P3 GPIO   
LCD-D2 | PWM0 | XIO-P4 GPIO | XIO-P5 GPIO   
LCD-D4 | LCD-D3 | XIO-P6 GPIO | XIO-P7 GPIO   
LCD-D6 | LCD-D5 | Ground | Ground   
LCD-D10 | LCD-D7 | AP-EINT1 | AP-EINT3   
LCD-D12 | LCD-D11 | TWI2-SDA | TWI2-SCK   
LCD-D14 | LCD-D13 | CSIPCK:CMOS | CSICK:CMOS   
LCD-D18 | LCD-D15 | CSIHSYNC:CMOS | CSIVSYNC : CMOS   
LCD-D20 | LCD-19 | CSID0:CMOS | CSID1:CMOS   
LCD-D22 | LCD-21 | CSID2:CMOS | CSID3:CMOS   
LCD-CLK | LCD-D23 | CSID4:CMOS | CSID5:CMOS   
LCD-VSYNC | LCD-HSYNC | CSID6:CMOS | CSID7:CMOS   
Ground | LCD-DE | Ground | Ground   
  

# Tips, Tricks, Caveats
The Chip requires 2A to run without issues if less Power is provided a brownout may occure. 
If USB Devices attached to the Chip require more then 500mA the **No Limit** version needs to be Flashed. 
A single Cell Lithium battery can be attached to the Chip. 
If a external Antenna is required a[UFL][39742] connector can be soldered on the back. 
  

## Device specific topic
Other than most Single Board Computers, the Chip needs to be flashed with an Operating System (OS). 
The Vendor provided a custom OS called [CHIP OS][39743] based on [Debian][39744] Jessie. CHIP OS uses the Debian package repositories. Images of CHIP OS come in different Flavours (Desktop, Server, Pocketchip). 
Those Images were provided in proprietary and undocumented format with the Filetype .chp. 
These files were designed to be used with a (now offline) Website and Chrome addon. 
**Fortunately several Open Source alternatives exist.**
NexThingCo provided a collection of bash scripts called CHIP-tools to update and flash images via sunxi-fel and fastboot. Archived/forked versions can be found [here][39745] and [here][39746]. For the image files an [archived version][39747] of the original images is used. 
## Flashing CHIP OS with CHIP-tools (host computer on Debian/Ubuntu)
Clone the Repo from Github. 
[code] 
    git clone <https://github.com/Thore-Krug/Flash-CHIP.git>
    
[/code]
Change into the Directory. 
[code] 
    cd Flash-CHIP
    
[/code]
Make the Script executable 
[code] 
    sudo chmod +x Flash.sh
    
[/code]
Execute the script 
[code] 
    sudo ./Flash.sh
    
[/code]
Select the version you want to install. Wait until the installation finishes. 
**Troubleshooting**
Use USB 2 
Refresh Apt Repos 
[code] 
    sudo apt update
    
[/code]
## Flashing CHIP OS (host computer on MacOS)
Clone the Repo 
[code] 
    git clone <https://github.com/Thore-Krug/Install-Flash-Chip-Mac>
    
[/code]
Change into the Directory 
[code] 
    cd Install-Flash-Chip-Mac
    
[/code]
Make the Script executable 
[code] 
     sudo chmod +x Flasher.sh
    
[/code]
Install all necessary Dependencies. 
[code] 
    ./Flash.sh install-all
    
[/code]
Flash your Chip 
[code] 
    ./Flash.sh flash
    
[/code]
Select the version you want to install. Wait until the installation finishes. 
  

Or read the Help 
[code] 
    ./Flash.sh help
    
[/code]
  

**Troubleshooting**
  
Kill the Script with ctrl + C 
Read the output if something is not installed or Permissions are missing 
Just restart the Script (fixes most of the Problem with FEL and Fastboot ) 
If this does not help reboot, retry 
Open an Issue on the Git Repo. 
Use USB 2 
# Dips
Like on other Single Board Computers, Hardware Addons which add more functionality to the Board can be used. These Addon Boards are called **Dips** , the Vendor NTC (Next Thing Company) provided HDMI and VGA Dips. But other User created other Dips too, like a USB Hub or a SD Card addon. 
  * [![C-H-I-P-HDMI.JPG][39748]][39749]
  * [![C-H-I-P-VGA.JPG][39750]][39751]

# Pictures
  * [![C-H-I-P SBC.JPG][39752]][39705]
  * [![C-H-I-P-BACK.JPG][39753]][39754]
  * [![C-H-I-P-BACK-Cover.JPG][39755]][39756]

# Variants
  * Alpha CHIP
  * CHIP Pro

# Also known as
  * C.H.I.P.

# See also
  * ~~[NextThingCo Chip Pro][39757]~~
  * ~~[PocketChip][39758]~~
  * [C.H.I.P. Single-Board Computer Wiki][39759]
  * [C.H.I.P. (Wikipedia)][39760]
  * [Kickstarter project page][39761]

## Manufacturer images
Optional. Add non-sunxi images in this section.
