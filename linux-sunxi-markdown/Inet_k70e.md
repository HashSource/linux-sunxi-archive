# Inet k70e
Inet k70e  
---  
[![Inet k70e front.jpg][27518]][27519]  
Manufacturer |  [Inet][27520]  
Dimensions |  191 _mm_ x 115 _mm_ x 13 _mm_  
Release Date |  August 2013   
Website |  [Device Product Page][27521]  
Specifications   
SoC |  [A20][27522] @ 1Ghz   
DRAM |  1GiB DDR3 @ ???MHz   
NAND |  4GB   
Power |  DC 5V @ ??A, ??00mAh ?.?V Li-Ion battery   
Features   
LCD |  800x600 (7" 16:9)   
Touchscreen |  X-finger capacitive/resistive ([Focaltech ???][27523] FIXME)   
Video |  HDMI (Type C, mini)   
Audio |  3.5mm headphone plug, HDMI, SPDIF, internal stereo speakers, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (TODO: [Manufacturer device][27524])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Other |  Accelerometer (TODO: [Manufacturer device][27525])   
Headers |  UART, JTAG   
This page needs to be properly filled according to the [New Device Howto][27526] and the [New Device Page guide][27527].
## Contents
  * [1 Identification][27528]
  * [2 Sunxi support][27529]
    * [2.1 Current status][27530]
    * [2.2 Images][27531]
    * [2.3 HW-Pack][27532]
    * [2.4 BSP][27533]
    * [2.5 Manual build][27534]
  * [3 Tips, Tricks, Caveats][27535]
    * [3.1 FEL mode][27536]
  * [4 Adding a serial port (**voids warranty**)][27537]
    * [4.1 Disassembling the device][27538]
    * [4.2 Locating the UART][27539]
  * [5 Pictures][27540]
  * [6 Also known as][27541]
  * [7 See also][27542]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: JDQ39  WTF, this is the id string for Android 4.2.2
  * Build Number: wing_ibt-eng 4.2.2 JDQ39

# Sunxi support
## Current status
No sunxi-boards or u-boot-sunxi patches have been made available yet, but this can be trivially done following the [New Device howto][27526]. Touchscreen doesn't work yet, but apparently ft5x_ts.c can be hacked to make it work. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][27543]

Everything else is the same as the [ Manual build howto][27544]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][27545]. 
[![][27546]][27547]
[][27548]
DEVICE UART pads
# Adding a serial port (**voids warranty**)
[![Exclamation-red.png][27549]][27550] **WARNING: Do not attach VCC like the person who made this picture. This might harm your device.**
## Disassembling the device
Provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped.
## Locating the UART
There are 2 pads labelled "RX" and "TX" between the SoC area and the GSM/GPRS module. You can get Ground from anywhere else on the board. All you have to do is follow the [ UART howto][27551] to solder on some wires. 
# Pictures
  * [![Device front.jpg][27552]][27553]
  * [![Device back.jpg][27554]][27555]
  * [![Device buttons 1.jpg][27556]][27557]
  * [![Device buttons 2.jpg][27558]][27559]
  * [![Device board front.jpg][27560]][27561]
  * [![Device board back.jpg][27562]][27563]

  * [![Inet k70e front.jpg][27564]][27519]
  * [![Inet k70e board.jpg][27565]][27566]

# Also known as
List rebadged devices here.
# See also
