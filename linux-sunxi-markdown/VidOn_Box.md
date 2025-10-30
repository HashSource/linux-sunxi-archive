# VidOn Box
VidOn Box  
---  
[![VidOnBox.JPG][58589]][58590]  
Manufacturer |  [VidOn][58591]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Sept 2014   
Website |  [VidOn Box][58592]  
Specifications   
SoC |  [A31S][58593] @ XGhz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  8GB eMMC (Foresee NCTSTS76-08G)   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI 1.4 (Type A)   
Audio |  HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EUS][58594]]]), 10/100Mbps Ethernet ([IC+ IP101A][58595])   
USB |  2 USB2.0 Host   
Other |  IRDA   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][58596] and the [New Device Page guide][58597].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][58598]
  * [2 Sunxi support][58599]
    * [2.1 Current status][58600]
    * [2.2 Images][58601]
    * [2.3 HW-Pack][58602]
    * [2.4 BSP][58603]
    * [2.5 Manual build][58604]
    * [2.6 Mainline U-Boot][58605]
    * [2.7 Mainline kernel][58606]
  * [3 Tips, Tricks, Caveats][58607]
    * [3.1 FEL mode][58608]
    * [3.2 Device specific topic][58609]
    * [3.3 ...][58610]
  * [4 Adding a serial port (**voids warranty**)][58611]
    * [4.1 Device disassembly][58612]
    * [4.2 Locating the UART][58613]
  * [5 Pictures][58614]
  * [6 See also][58615]
    * [6.1 Manufacturer images][58616]

# Identification
On the bottom of the device, the following is printed: 
[code] 
    VidOn Box Input: 5V 2A Designed by: VidOn.me Made In China
[/code]
The PCB has the following silkscreened on it: 
[code] 
    VidOn.me on the top of the PCB
[/code]
[code] 
    VidOn Box VBOX1-1.30 on the bottom of the PCB
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _Softwinner_
  * Build Number: _vidonme a31s v1.0.0_
  * Linux Version: _3.3.0 (vbox@vbox-A11-Series)_

# Sunxi support
## Current status
Like all [A31][58617] devices, the VidOn Box is not supported by our [sunxi u-boot][58618] and [sunxi kernel][58619], but we hope to provide [an A31 specific Manual build howto][58620] soon. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][58621]

WIP: I've been unable to extract the fex file using the traditional method. It seems with A31 type devices that the fex file forms part of the uboot image. At the moment I've not be able to locate this on the flash device however the download zip file from a system upgrade does contain a file called uboot_sdcard.fex. By using the command 
[code]
    dd if=uboot_sdcard.fex bs=1 skip=688128 count=49134 of=script.bin 
[/code]
I'm able to produce a file that can be converted by bin2fex. This is linked below for now and will be uploaded to the usual place after I've done so more investigating. 
Everything else is the same as the [manual build howto][58622]. 
## Mainline U-Boot
If there is mainline u-boot support, add this section.
For [ building mainline u-boot][58623], use the _MANUFACTURER_DEVICE_ target. 
Don't forget to add 
[code]
    [[Category:Mainline_U-Boot]]
[/code]
at the bottom of the page.
## Mainline kernel
If there is mainline kernel support, add this section.
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree file for the [mainline kernel][58624]. 
Don't forget to add 
[code]
    [[Category:Mainline_Kernel]]
[/code]
at the bottom of the page.
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][58625]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][58626]][58627]
[][58628]
VidOn Box UART pads
## Device disassembly
There are two small phillips head screws at the rear of the device. Once loosened the gold casing can easily slide off. The PCB is attached to the rear panel and the wireless anteena via a thin cable which can be removed but it isn't necessary. 
## Locating the UART
The VidOn Box has a 4 pin 2.0 pitch JST-PH connector available for its UART0 port(to confirm) which is labelled on the PCB. This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. More information is available at our [our UART howto][58629]. 
# Pictures
  * [![VidOnBox Front.JPG][58630]][58631]
  * [![VidOnBox Rear.JPG][58632]][58633]
  * [![VidOnBox Top.JPG][58634]][58635]
  * [![VidOnBox Bottom.JPG][58636]][58637]
  * [![VidOnBox PCB Top.JPG][58638]][58639]
  * [![VidOnBox PCB Bottom.JPG][58640]][58641]
  * [![VidOnBox Case.JPG][58642]][58643]
  * [![VidOnBox Details.JPG][58644]][58645]

# See also
  * [Official Forum][58646]
  * [Kodi Forum][58647]: Nice thread which is thoroughly testing Kodi behaviour
  * [vidon_box.fex][58648]: Extracted fex file from OTA system update

## Manufacturer images
Optional. Add non-sunxi images in this section.
