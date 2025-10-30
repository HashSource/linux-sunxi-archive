# Pine Pinebook
Pine Pinebook  
---  
[![Pinebook 11 Inch Small Clip.png][44812]][44813]  
Manufacturer |  [Pine Microsystems Inc.][44814]  
Dimensions |  329 _mm_ x 220 _mm_ x 23?_mm_ (14" model), 300 _mm_ x 200 _mm_ x 23?_mm_ (11" model)   
Release Date |  tba   
Website |  [Pinebook product page][44815]  
Specifications   
SoC |  [A64][44816] @ 1152Mhz max.   
DRAM |  2GiB DDR3L (Prototype) @ xxxMHz, 2GiB LPDDR3 (Production) [Foresee NCLD3B2512M32][44817] @ 533 MHz   
Power |  DC 5V@3A 3.5mm/1.35mm barrel plug, 10Ah 3.7V 1S2P LiPo battery   
Features   
LCD |  14" (HB140WX1-501) - 1366x768 (TN panel), 11" (N116BGE) - 1366x768 (TN panel), 11" (LC116LF3L01) - 1920x1080 (IPS)   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headset plug (4pin), HDMI, internal stereo speakers, internal microphone(s)   
Network |  WiFi 802.11 b/g/n + BT4.0 ([RTL8723cs][44818])   
Storage |  16GB replaceable eMMC module (default) (HS-200), uSD slot (SDR25)   
USB |  1 USB2.0 Host (USB-A) via internal 4 port hub (camera, HID), 1 USB2.0 OTG/Host (USB-A)   
Camera |  0.3MP (640x480) front USB camera (ZC-RZ3762 / BYD BF3703)   
Other |  8051 based (SinoWealth SH68F83) USB HID keyboard/touchpad bridge; weight 1260 _g_ (14"), 1040 _g_ (11")   
This page needs to be properly filled according to the [New Device Howto][44819] and the [New Device Page guide][44820].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][44821]
    * [1.1 Different models][44822]
  * [2 Sunxi support][44823]
    * [2.1 Current status][44824]
    * [2.2 Images][44825]
    * [2.3 HW-Pack][44826]
    * [2.4 BSP][44827]
    * [2.5 Manual build][44828]
      * [2.5.1 U-Boot][44829]
        * [2.5.1.1 Sunxi/Legacy U-Boot][44830]
        * [2.5.1.2 Mainline U-Boot][44831]
      * [2.5.2 Linux Kernel][44832]
        * [2.5.2.1 Sunxi/Legacy Kernel][44833]
        * [2.5.2.2 Mainline kernel][44834]
  * [3 Tips, Tricks, Caveats][44835]
    * [3.1 FEL mode][44836]
    * [3.2 Power Management][44837]
    * [3.3 Audio Paths][44838]
    * [3.4 Video Paths][44839]
    * [3.5 Wifi/BT][44840]
    * [3.6 Extra internal headers, sensors][44841]
      * [3.6.1 Prototype][44842]
      * [3.6.2 Production][44843]
    * [3.7 ...][44844]
  * [4 Adding a serial port][44845]
    * [4.1 Production Pinebook][44846]
    * [4.2 Prototype Pinebook][44847]
    * [4.3 Opening the Pinebook][44848]
    * [4.4 Locating the UART][44849]
  * [5 Pictures][44850]
    * [5.1 Pinebook 11.6"][44851]
    * [5.2 Pinebook 11.6" 1080p][44852]
    * [5.3 Pinebook 14"][44853]
    * [5.4 Accessories and pre-production units][44854]
  * [6 See also][44855]
    * [6.1 Datasheets][44856]
    * [6.2 Manufacturer images][44857]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    * Prototypes
    ** Prototypes do not seem to have external markings besides Pine64 stickers...
[/code]
The PCB has the following silkscreened on it: 
[code] 
    * Prototypes
    ** Mainboard (bottom): A114-A64_V1.1 2016-08-23
    ** Daughterboard (top): A114-A64_USB_V1.1 2016-09-23
    
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

## Different models
So far there are two different models based on the same PCB 
  * 14inch LCD
  * 11inch LCD

# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here.
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][44855]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][44858] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][44859] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
  * Prototypes

The FEL mode can be entered either via pulling the FEL tespad to GND while turning on the system (see below for Testpad location) or via a specially crafted boot0 on a microSD card. 
  * Production Units

The FEL mode can be entered either by using the FEL button on the PCB while turning on the unit or via a specially crafted boot0 on a microSD card. 
## Power Management
The Pinebook is powered by a 3.5mm/1.35mm barrel plug, sleeve is GND, inner contact +5V. The maximum input current is 3A. The PCB contains an implementation of the standard AXP803 PMIC with a 10Ah LiPo battery attached. There is a secondary power path via the OTG-USB port... TODO: add more info, add current requirements for LCD/backlight and other components 
## Audio Paths
The Pinebook utilizes the internal codec of the A64 with some extra hardware in the audio paths: 
  * LINEOUT via amplifiers (1W/8R) (with GPIO controlled mute, PA-SHDN = PH7) to the internal speakers
  * HP-OUT is connected to the 4-pin 3.5mm headset jack
  * MIC1 & MIC2 are used in a multiplexed scheme for either headset jack or internal microphones (TODO/check new schematics) 
    * MIC1 is connected to one of the internal microphones
    * MIC2 is multiplexed between the second internal microphone (MIC2-EN=L) or the headphone jack (MIC2-EN=H)
    * GPIO to control MIC2 multiplexer: MIC2-EN = PL11

## Video Paths
  * HDMI ...
  * RGB-LCD --> ANX6345 eDP bridge --> LCD ... 
    * LCD/backlight is controlled via GPIOs (LCD-EN=PH6, LCD-BL-EN=PD23, LCD-RST=PD24, LCD-HPD=PL7 ) and a PWM output (LCD-PWM=PD22/PWM0)
    * LCD open/close status is detected via a hall effect sensor connected to GPIO PH10 (sensor located between the uSD card slot and headphone jack)

TODO: add more info 
## Wifi/BT
The RTL8723cs SDIO module is similar to the RTL8723bs used for the Pine64 Wifi/BT module... TODO: wifi mainline driver source and BT firmware loader description... 
  * GPIOs 
    * WL-PMU-EN = PL2
    * WL-WAKE-AP = PL3
    * BT-RST-N = PL4
    * BT-WAKE-AP = PL5
    * AP-WAKE-BT = PL6

## Extra internal headers, sensors
  * Keyboard controller is a [SH68F83][44860] low speed USB microcontroller with 8051 core
  * Touchpad is connected via i2c to keyboard controller

### Prototype
  * Capacitive touchpanel header (provides access to I2C/TWI0, GPIOs PH4&PH8)
  * Bosch BMA223 acceleration sensor (via I2C/TWI1, default address=0x18 and GPIO-IRQ PH5)
  * Free USB port on the internal hub? (seems routed to the sdcard daughterboard, production units may have testpads, TODO: confirm)

### Production
  * Free USB port on the internal hub is routed to daughterboard connector pins 7(DP) and 8(DM)

TODO: add more info 
## ...
# Adding a serial port
## Production Pinebook
Production Pinebooks have the serial port multiplexed with the audio jack output. See here for the pinout: 
  * [Pinebook Headphone Jack UART Connector Pinout][44861]

(Beware, for me it seems RX/TX are swapped, and the TIP is actually RX on my Pinebook!) 
For activating the serial/UART on the audio jack on the production pinebook there seem to be two variants: 
  1. Variant with a software controller GPIO, which can be activated using the "sudo pinebook_enable_uart.sh" command (and "sudo pinebook_enable_headphone.sh" to restore back to headphones output)
  2. Variant with a hardware switch that needs to be toggled, and requires opening the back cover of the pinebook. Once opened, flip the switch located here:

  * [![Pinebook 14 UART serial switch.jpg][44862]][44863]

Once the audio jack is configured for outputting serial/uart data, you'll be able to see boot0, uboot, linux kernel logs, ... up until you'll eventually get a login prompt. Serial settings: 
115200, 8N1, no flow control 
In case of a software controlled GPIO, you might have to disable the service restoring audio output, if you want the UART to remain active: $> sudo systemctl disable pinebook-headphones 
## Prototype Pinebook
The prototype Pinebook PCBs do not have a UART0 header, only testpads on the bottom side which requires removing the PCB and soldering some wires / breakout board to it. The production units are planned to have UART0 multiplexed on the headphone jack (TODO: describe trigger condition) 
## Opening the Pinebook
Opening the Pinebook is easy: 
  * Remove all the screws on the bottom. Make sure to note which screws go where since they have different lengths!
  * To pull off the cover, slide a plastic/metal lid/spudger in between the cover and the laptop body, to unclip it in several locations. Start at an easy spot and work your way around the whole cover.

## Locating the UART
The UART and FEL testpad locations for the prototype PCBs can bee seen in the picture, colors are as following: Green-TXD, Orange-RXD, Yellow-FEL, Black-GND. The A64 uses 3,3V CMOS signal levels, so make sure your UART adapter does not use 5V, see [UART howto][44864] for more information. 
  * [![Pinebook uart fel.jpg][44865]][44866]

# Pictures
Take some pictures of your device, [ upload them][44867], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
## Pinebook 11.6"
  * [![Pinebook 11 Inch.jpg][44868]][44869]
  * [![Pinebook 11 Inch Side View.jpg][44870]][44871]
  * [![Pinebook 11 Bottom.jpg][44872]][44873]

## Pinebook 11.6" 1080p
  * [![Pinebook 11 1080p front.jpg][44874]][44875]
  * [![Pinebook 11 1080p keyboard.jpg][44876]][44877]
  * [![Pinebook 11 1080p bottom.jpg][44878]][44879]
  * [![Pinebook 11 1080p inside overview.jpg][44880]][44881]
  * [![Pinebook 11 1080p battery.jpg][44882]][44883]
  * [![Pinebook 11 1080p mainboard.jpg][44884]][44885]

## Pinebook 14"
  * [![Pinebook 14 Inch with Ethernet Adapter.jpg][44886]][44887]
  * [![Pinebook 14 Inch Side View.jpg][44888]][44889]
  * [![Pinebook 14 Bottom.jpg][44890]][44891]
  * [![Pinebook 14 inside.jpg][44892]][44893]

## Accessories and pre-production units
  * [![16GB NCEMBSF9-16G eMMC.jpg][44894]][44895]
  * [![Pinebook 11inch.jpg][44896]][44897]
  * [![Pinebook 11inch left.jpg][44898]][44899]
  * [![Pinebook 11inch right.jpg][44900]][44901]
  * [![Pinebook prototype open.jpg][44902]][44903]

# See also
  * [Ayufan's GitHub with BSP based builds of Android and u-boot, Linux kernel for Pine64, Pinebook][44904]
  * [wiki.pine64.org Further info on the hardware and firmware][44905].
  * [forum.pine64.org Discussion on pine64][44906]

## Datasheets
  * [Pinebook Logicboard Schematic V1.0 (prototypes)][44907]
  * [Pinebook Logicboard Schematic V3.0 (Production)][44908]
  * [Pinebook Daughterboard Schematic V1.0][44909]
  * [Pinebook Headphone Jack UART Connector Pinout][44861]

## Manufacturer images
[Pine A64 Android release and Linux BSP][44910]
