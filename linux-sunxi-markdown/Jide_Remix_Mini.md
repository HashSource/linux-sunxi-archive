# Jide Remix Mini
Jide Remix Mini  
---  
[![Jide Remix Mini.jpg][29161]][29162]  
Manufacturer |  [Jide][29163]  
Dimensions |  124 _mm_ x 88 _mm_ x 26 _mm_  
Release Date |  October 2015   
Website |  [Device Product Page][29164]  
Specifications   
SoC |  [H64][29165] @ 1152MHz   
DRAM |  1GiB/2GiB DDR3L @ 672 MHz (H5TC4G83AFR-PBA * 2)   
Power |  DC 5V @ 3A   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm combo headphone/microphone plug, HDMI   
Network |  WiFi 802.11 b/g/n + bluetooth 4.0 ([Realtek RTL8273BS][29166]), 100Mbps Ethernet ([X-Powers AC200][29167])   
Storage |  8/16GB eMMC, µSD   
USB |  2 USB2.0 Host   
Other |  IRDA   
Headers |  UART   
## Contents
  * [1 Identification][29168]
  * [2 Sunxi support][29169]
    * [2.1 Current status][29170]
    * [2.2 Manual build][29171]
      * [2.2.1 Mainline U-Boot][29172]
      * [2.2.2 Mainline Linux kernel][29173]
  * [3 Tips, Tricks, Caveats][29174]
    * [3.1 FEL mode][29175]
    * [3.2 eMMC][29176]
    * [3.3 Device specific topic][29177]
    * [3.4 ...][29178]
  * [4 Adding a serial port (**voids warranty**)][29179]
    * [4.1 Device disassembly][29180]
    * [4.2 Locating the UART][29181]
  * [5 Pictures][29182]
  * [6 See also][29183]
    * [6.1 Manufacturer images][29184]

# Identification
On the back of the device, the following is printed: 
[code] 
    Remix Mini
    Jide Technology Model:RM1G
[/code]
The PCB has the following silkscreened on it: 
[code] 
    JD-YZJ_8x4_V1_0
[/code]
# Sunxi support
## Current status
Supported in mainline Linux. The devicetree was merged rather late, in v6.9 (May 2024), but driver wise the support reaches back for many years. So presenting an older kernel with the new devicetree will probably just work. 
## Manual build
You can build things for yourself by following our [ Manual build howto][29185] and by choosing from the configurations available below. 
### Mainline U-Boot
[Defconfig][29186] posted and accepted, but not merged due to CI issues related to the TOC0 image generation. You can apply that patch on mainline U-Boot and then use the _remix-mini-pc_defconfig_ build target. 
### Mainline Linux kernel
Use the _sun50i-h64-remix-mini-pc.dtb_ devicetree binary. 
# Tips, Tricks, Caveats
The SoC has the "secure boot" fuse burned, so it will not accept any standard eGON boot media (on an SD card or on the eMMC). Instead it expects [TOC0][29187] wrapped boot code. Fortunately there does not seem to be any actual ROTPK HASH key burned into the fuses, so it will not try to match against a certain key, but will load boot code (SPL) signed with *any* key. 
## FEL mode
Normally Remix Mini boots from the internal 8/16 GiB eMMC. If an SD card with a valid TOC0 header is present, this will take precedence and the BROM will load code from there. FEL mode is another way to access the device: to trigger [ FEL mode][29188], there is a button accessible via the pin-hole, located between the SD card slot and the audio jack. A somewhat special USB cable (A male to A male) is needed to connect the upper USB host receptacle to your desktop PC, which is running the [sunxi-fel][29189] tool. 
[![FEL button pin-hole][29190]][29191] [![FEL button][29192]][29193]
Instead of pressing the button it is possible to have a [TOC0][29187] based bootable SD card image, which switches the device into FEL mode: 
[code] 
       wget <https://github.com/ssvb/sunxi-tools/raw/toc0/bin/fel-sdboot.toc0>
       dd if=fel-sdboot.toc0 of=/dev/sdX bs=1024 seek=8
    
[/code]
As the SoC starts up in "secure boot" mode, FEL will be entered in non-secure SVC mode. However any random smc call will immediately return, now in secure SVC mode, so with full access to the system. The sunxi-fel tool does that for you automatically, on the first access to the device. 
## eMMC
Remix Mini has eMMC connected to SMHC2 (0x1C11000) and apparently [clocked at 100MHz][29194] according to the [dmesg log from Remix OS][29195]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][29196]][29197]
[][29198]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][29199]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][29200].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][29199].
# Pictures
  * [![Jide Remix Mini.jpg][29201]][29162]
  * [![Jide Remix Mini PCB top.jpg][29202]][29203]
  * [![Jide Remix Mini PCB bottom.jpg][29204]][29205]
  * [![Jide Remix Mini UART wires.jpg][29206]][29207]

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
