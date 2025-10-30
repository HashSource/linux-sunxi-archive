# Rikomagic mk802+
Rikomagic mk802+  
---  
[![MK802 1GB Top Case.jpg][47372]][47373]  
Manufacturer |  [Rikomagic][47374]  
Dimensions |  88.5 _mm_ x 35 _mm_ x 13.4 _mm_  
Release Date |  June 2012   
Website |  [German product page][47375]  
Specifications   
SoC |  [A10][47376] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI   
Audio |  HDMI, internal microphone.   
Network |  802.11 b/g/n ([Realtek RTL8188CTV][47377])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART   
This is the 1GB version of the popular [MK802][47378] and it comes with a redesigned motherboard. 
## Contents
  * [1 Identification][47379]
  * [2 Sunxi support][47380]
    * [2.1 Current status][47381]
    * [2.2 Images][47382]
    * [2.3 HW-Pack][47383]
    * [2.4 BSP][47384]
    * [2.5 Manual build][47385]
    * [2.6 Mainline U-Boot][47386]
    * [2.7 Mainline Kernel][47387]
  * [3 Tips, Tricks, Caveats][47388]
    * [3.1 FEL mode][47389]
    * [3.2 ADB][47390]
  * [4 Adding a serial port (**voids warranty**)][47391]
    * [4.1 Device disassembly][47392]
    * [4.2 Locating the UART][47393]
  * [5 Pictures][47394]
  * [6 Also known as][47395]
  * [7 See also][47396]

# Identification
Sometimes the case reads "MK802+", but this is also true for the [Semitime G2][47397]. Apart from a date code, there is no text printed on the board. 
In android, under Settings->About Device, you may find the following: 
  * Model Number: SoftwinnerEvb
  * Build Number: apollo_mele-eng 4.0.4 IMM76D 20120910 test-keys

There is one issue remaining with identification though. The board in the documented example is blue, has a microphone and has a [FEL][47398] button soldered on. The board commonly found on the internet is however green, but the layout seems to generally match, even though it sometimes lacks a FEL button. So there probably are a few different revisions available of this device. 
# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "mk802_1gb" target.
  * The .fex file can be found in sunxi-boards as [mk802-1gb.fex][47399]

Everything else is the same as the [manual build howto][47400]. 
## Mainline U-Boot
Use the _mk802_defconfig_ build target. 
## Mainline Kernel
Use the _sun4i-a10-mk802.dtb_ device-tree file for the [mainline kernel][47401]. 
# Tips, Tricks, Caveats
## FEL mode
The MK802+ has a [ FEL button][47398] under the bottom hole of the left side of the top cover (next to the hdmi connector). Some versions of the MK802+ have saved a few cents on attaching a button though, but perhaps some of these are different boards altogether. 
## ADB
The device is factory rooted but so far ADB over USB hasn't been possible. To use ADB install a SSH Server like SSHDroid and start up the service. With the information provided by the Android App you can remotely log into the device(the login prompt displays the password. Type "adb shell" to enter [ADB][47402] mode. 
# Adding a serial port (**voids warranty**)
[![][47403]][47404]
[][47405]
UART pads
## Device disassembly
The three piece case is clicked together. Do not try to get the semi-transparent bit around the USB Host connector off, as it is clipped into the top and you could damage the clip. Just gently push your [plastic tool][47406] between the bottom and the top, and push the top part of the shell outwards. You will soon hear the clips release. 
## Locating the UART
The TX and RX pins for UART 0 are to the right of the SoC. A good place to solder the GND connection is on the ground plane that runs along the side of the board. More information is available at [our UART howto][47407]. 
# Pictures
  * [![][47408]][47373]
Mk802+ photo top of casing 
  * [![][47409]][47410]
Mk802+ photo bottom of casing 
  * [![][47411]][47412]
Mk802+ photo side of casing showing SDcard 
  * [![][47413]][47414]
Mk802+ photo side of casing showing OTG 
  * [![][47415]][47416]
Mk802+ photo side of casing showing HDMI female socket 
  * [![][47417]][47418]
Mk802+ photo side of casing showing power connector and USB 
  * [![][47419]][47420]
Mk802+ photo showing the CPU, DRAM, Flash, Wireless chip and power circuitry. 
  * [![][47421]][47422]
Mk802+ photo showing the DRAM and external connectors. 
  * [![][47423]][47424]
Mk802+ photo top of packaging 
  * [![][47425]][47426]
Mk802+ photo bottom of packaging 
  * [![][47427]][47428]
Mk802+ photo side of packing showing variant 
  * [![][47429]][47430]
MK802+ with different printing on the case 

# Also known as
This is often sold as the plain [MK802][47378], but it has 1GiB of DDR3 RAM, and has a different motherboard. 
# See also
  * [Rikomagic MK802][47378]: The 512MiB original.
  * [Semitime G2][47397]: A 1GB A10s based device with the same case.
  * [Rikomagic MK802II][47431]: A completely redesigned A10 based HDMI stick.
