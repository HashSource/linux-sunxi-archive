# Sinovoip Banana Pi M2 Zero
This page needs to be properly filled according to the [New Device Howto][50370] and the [New Device Page guide][50371].
Banana Pi M2 Zero is a [H2+][50372] based development board produced by Sinovoip. 
Despite its name the M2 Zero is **totally incompatible to Banana Pi/M1/M1+/Pro/M2/M2U/M3/M64** due to a different SoC - requiring different boot loaders and drivers. It's another attempt to cash-in on the Banana Pi's popularity with a SBC sharing only Brand-name, form factor and GPIO header. 
  

Sinovoip Banana Pi M2 Zero  
---  
[![Banana Pi M2 Zero top.jpg][50373]][50374]  
Manufacturer |  [Sinovoip][50375]  
Dimensions |  65 _mm_ x 30 _mm_  
Release Date |  October 2017   
Website |  [BPI-M2 Zero Product Page][50376]  
Specifications   
SoC |  [H2+][50372]  
DRAM |  512 MiB SDRAM   
Power |  DC 5V DC-IN via µUSB or OTG   
Features   
Video |  mini HDMI   
Network |  WiFi 802.11 b/g/n ([AMPAK AP6212][50377]), Ethernet on CON4   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Other |  RPi incompatible CSI interface   
Headers |  UART, LCD, Camera, Raspberry Pi 2 compatible header   
## Contents
  * [1 Identification][50378]
  * [2 Sunxi support][50379]
    * [2.1 Current status][50380]
    * [2.2 Manual build][50381]
      * [2.2.1 Mainline U-Boot][50382]
      * [2.2.2 Mainline Linux Kernel][50383]
  * [3 Tips, Tricks, Caveats][50384]
    * [3.1 Ethernet][50385]
  * [4 Adding a serial port][50386]
  * [5 Pictures][50387]
  * [6 Also known as][50388]
  * [7 See also][50389]
    * [7.1 Schematic][50390]
    * [7.2 Bananapi gitbook][50391]
    * [7.3 OS images][50392]

# Identification
The PCB has the following silkscreened on it along with a BananaPi logo: 
[code] 
    BPi-M2-ZERO-V1.0
    
[/code]
# Sunxi support
## Current status
Supported in mainline U-Boot and Linux kernel since 2019. 
## Manual build
You can build things for yourself by following our [ Manual build howto][50393]. 
### Mainline U-Boot
Use the _bananapi_m2_zero_defconfig_ build target. Available since v2019.01-rc1. 
### Mainline Linux Kernel
Use the _sun8i-h2-plus-bananapi-m2-zero.dtb_ device-tree binary. This has been available since release _v4.17_ (2018-06). 
# Tips, Tricks, Caveats
## Ethernet
[![][50394]][50395]
[][50396]
Ethernet Jack Wiring
  

The ethernet connector should be wired as follows: 
  * Top Left - 3
  * Top Right - 2
  * Bottom Left - 6
  * Bottom Right - 1

Some images do not have ethernet functioning. The following claim ethernet functionality: 
  * [Banana Pi Forums Image][50397] Kernel 3.4.113, Ubuntu Mate Desktop
  * [Github page][50398] made by a user

# Adding a serial port
[![][50399]][50400]
[][50401]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][50402]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
# Pictures
  * [![Banana Pi M2 Zero top.jpg][50403]][50404]
  * [![Banana Pi M2 Zero bottom.jpg][50405]][50406]
  * [![Banana Pi M2 Zero 1.jpg][50407]][50408]
  * [![Banana Pi M2 Zero 2.jpg][50409]][50410]
  * [![Banana Pi M2 Zero 3.jpg][50411]][50412]
  * [![Banana Pi M2 Zero 4.jpg][50413]][50414]
  * [![M2 Zero CON4.jpg][50415]][50416]

# Also known as
  * The marketing material (e.g. the [product page][50417]) also refers to the board as 'Banana Pi BPI-M2Z'.
  * The product page ([[1]][50376]) also uses the name 'Banana Pi Zero'.

# See also
## Schematic
[ Banana Pi M2 Zero Schematic V1.0 (20170814)][50418]. 
## Bananapi gitbook
Please be aware that 'information' on BPi M2 Zero [Gitbook][50419] page is mostly copy&paste from other Banana Pi pages and as usual we can't trust in anything there (even product dimensions are still wrong, the PCB is not 60x30mm but 65x30mm in reality). 
## OS images
[Official OS Images][50420]
