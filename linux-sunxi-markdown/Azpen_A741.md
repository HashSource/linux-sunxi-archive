# Azpen A741
Azpen A741  
---  
[![A741 front.jpg][8188]][8189]  
Manufacturer |  [Azpenpc][8190]  
Dimensions |  8.6 _mm_ x 190 _mm_ x 130 _mm_  
Release Date |  unknown   
Website |  Missing product page.   
Specifications   
SoC |  [A33][8191] @ XGhz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  DC 5V @ ?A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" 16:9) IPS   
Touchscreen |  5-finger capacitive ([Silead GSL1680][8192])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][8193])   
Storage |  µSD   
USB |  X USB2.0 Host, X USB2.0 OTG   
Camera |  ??.?MP (????x????) rear   
Other |  Accelerometer ([Manufacturer device][8194])   
This page needs to be properly filled according to the [New Device Howto][8195] and the [New Device Page guide][8196].
  

## Contents
  * [1 Identification][8197]
  * [2 Tips, Tricks, Caveats][8198]
    * [2.1 FEL mode][8199]
    * [2.2 Device disassembly][8200]
  * [3 Adding a serial port (**voids warranty**)][8201]
  * [4 Pictures][8202]
  * [5 Also known as][8203]
  * [6 See also][8204]
    * [6.1 Manufacturer images][8205]

# Identification
On the back of the device, the model number is clearly visible (Model: A741) 
The PCB has the following silkscreened on it: 
[code] 
    TEAN E120339 94V-OML1
[/code]
In adb shell, the device identifies itself as astar-m86 
# Tips, Tricks, Caveats
The kernel normally boots in 'silent' mode, without printing anything useful to the uart. The debug mode can be activated by powering on the tablet with the Vol+ button pressed, and, while holding the button, plugging and unplugging the power/usb cable several times. 
## FEL mode
The Vol+ button triggers [ FEL mode][8206]. Other boot sources still take priority (microSD), indicating that this is not a proper FEL button, only a function of the bootloader in NAND. 
## Device disassembly
The device has two screws on the connector side, and the cover is 'clicked' on the screen. After removing the screws, the cover can be easily removed using fingernails or a [Plastic tool howto][8207]. Inside the board is mounted using three screws. 
# Adding a serial port (**voids warranty**)
[![][8208]][8209]
[][8210]
a741 UART pads
Two uarts' pins are available on the back of the board, see the picture on the right for reference. 
UART0 is used by the ROM bootloader and android bootloader, it is however multiplexed with the [microSD socket][8211]. The preinstalled bootloader doesn't respond to keys received on the RX pin. 
R_UART is free to use, but needs to be specifically enabled in your own uboot & linux image. 
For more information, see [UART howto][8212]. 
# Pictures
  * [![A741 front.jpg][8213]][8189]
  * [![A741 back.jpg][8214]][8215]
  * [![A741 pcb front.jpg][8216]][8217]
  * [![A741 pcb back.jpg][8218]][8219]

# Also known as
# See also
## Manufacturer images
