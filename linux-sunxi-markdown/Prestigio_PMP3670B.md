# Prestigio PMP3670B
Prestigio PMP3670B  
---  
[![Pmp3670b front.jpg][45929]][45930]  
Manufacturer |  [Manufacturer web page][45931]  
Dimensions |  192 _mm_ x 116 _mm_ x 10.7 _mm_  
Release Date |  May 2013   
Website |  [Product page][45932]  
Specifications   
SoC |  [A13][45933] @ 1Ghz   
DRAM |  512MiB @ 408MHz   
NAND |  4GB   
Power |  DC 5V microUSB, 3200mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Silead GSLX680][45934])   
Audio |  3.5mm headphone plug, internal speaker   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][45935])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front (gt2005)   
Other |  Accelerometer ([Domintech DMARD10][45936]), RTC (pcf8563)   
This page needs to be properly filled according to the [New Device Howto][45937] and the [New Device Page guide][45938].
## Contents
  * [1 Identification][45939]
  * [2 Sunxi support][45940]
    * [2.1 Current status][45941]
    * [2.2 Images][45942]
    * [2.3 HW-Pack][45943]
    * [2.4 BSP][45944]
    * [2.5 Manual build][45945]
  * [3 Tips, Tricks, Caveats][45946]
    * [3.1 FEL mode][45947]
    * [3.2 Enabling ADB][45948]
    * [3.3 Rooting][45949]
  * [4 Adding a serial port (**voids warranty**)][45950]
    * [4.1 Device disassembly][45951]
  * [5 Pictures][45952]
  * [6 Also known as][45953]
  * [7 See also][45954]
    * [7.1 Manufacturer images][45955]

# Identification
The back of the tablet reads: 
[code] 
    Prestigio Multipad 7.0 Ultra+
    Tablet PC|PMP3670B
[/code]
The board has the following printed on it: 
[code] 
    A86 MB V4.0
    2013/01/31
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: PMP3670B
  * Build Number: PMP3670B.2013.10.14.4.01.02

Note that there two different versions of this tablet. The ones with the black screen frame and different color back covers is what is currently documented here. There is also a version with a white screen frame and a white cover, which supposedly is somewhat incompatible with this device, as it at least has a different touchscreen controller. 
# Sunxi support
## Current status
Supported. 
Tested: 
  * boot from SD card - mmc0
  * PMU
  * original nand flash content access
  * LCD
  * USB OTG (ethernet gadget)
  * USB HOST (wifi)
  * tablet keys

Untested (should work): 
  * mali
  * cedar

Detected by kernel but needs testing: 
  * rtc
  * USB WiFi
  * audio

Unknown: 
  * accelerometer
  * camera
  * touchscreen

## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the **prestigio_pmp3670b** target.
  * The .fex file can be found in sunxi-boards as [prestigio_pmp3670b.fex][45956]

Everything else is the same as the [manual build howto][45957]. 
# Tips, Tricks, Caveats
## FEL mode
Powering on an A13 tablet requires somewhat longish press of the power button. If during that time Vol+ or Vol- is pressed repeatedly (~5 times) [ FEL mode][45958] is activated instead of powering on normally. 
## Enabling ADB
To enable **ADB** go to tablet info and tap the build number multiple (~7) times. Then in tablet settings debugging options appear. At the very top of debugging options a switch in OFF posistion is shown. Change to ON and find USB debugging in the list of options below. Tick the checkbox. 
## Rooting
[rootdashi (Chinese)][45959] appears to **root** the tablet. 
As advised [here][45960] you should use **su** in adb shell to get root access. 
# Adding a serial port (**voids warranty**)
The device has no useful [UART][45961] pads, as pins that would be usable for UART are in use by other devices. You can either use a [ µSD breakout board][45962] or disable the camera and locate the usable UART pins on the camera connector . 
## Device disassembly
Remove two screws on the connectors side. Then carefully use your [Plastic tool][45963] to pop the clips on the back cover by pushing the back cover out, **only** on the sides without the connectors. The connector side will come free when the other 3 sides are released. When re-assembling, replace the connector side first. 
# Pictures
  * [![Pmp3670b front.jpg][45964]][45930]
  * [![Pmp3670b back.jpg][45965]][45966]
  * [![Pmp3670b buttons.jpg][45967]][45968]
  * [![A86 board front.jpg][45969]][45970]
  * [![A86 board back.jpg][45971]][45972]
  * [![A86 board text.jpg][45973]][45974]
  * [![PER3670B display.jpg][45975]][45976]

# Also known as
  * Eli Lilly 4G Tablet

# See also
Manufacturer pictures of the case: 
  * [PMP3670B front picture][45977]
  * [PMP3670B back picture][45978]
  * [PMP3670B buttons][45979]

## Manufacturer images
  * [List of firmwares at Prestigio.][45980]

  * download link for current firmware <http://de05.dl.prestigio.com/Service_Files/TabletPC/PMP3670B/PMP3670B.20131014.4.01.02.zip>

Current firmware is not available from this site. Black firmware should work with non-white colour variants - eg. black display frame with different colour back covers. [Reportedly][45981] flashing black firmware on white tablet causes touchscreen to stop working.
