# Rikomagic mk802
Rikomagic mk802  
---  
[![Nasty rikomagic mk802 front.jpg][47466]][47467]  
Manufacturer |  [Rikomagic][47468]  
Dimensions |  88.5 _mm_ x 35 _mm_ x 13.4 _mm_  
Release Date |  May 2012   
Website |  [German product page][47469]  
Specifications   
SoC |  [A10][47470] @ 1Ghz   
DRAM |  512MiB DDR3 @ 480MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI   
Audio |  HDMI   
Network |  802.11 b/g/n (Realtek RTL8188CTV)   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Headers |  UART   
This is the most popular HDMI stick out there. While the original idea came from the [FXI Cotton Candy][47471], the MK802 really opened up the world of HDMI sticks. 
Many devices are currently named MK802 as a result. Some use the same case, but have different innards ([MK802+][47472] and [Semitime G2][47473]). The [MK802II][47474] is a complete redesign, but uses an [A10][47470] as well. The MK802III and MK802IV are not allwinner based, and use a rockchip SoC instead. 
Rumour has it that many clones were made, so who knows, if we get enough [devices documented in our wiki][47475], we might see some severe motherboard differences. 
## Contents
  * [1 Identification][47476]
  * [2 Sunxi support][47477]
    * [2.1 Current status][47478]
    * [2.2 Images][47479]
    * [2.3 HW-Pack][47480]
    * [2.4 BSP][47481]
    * [2.5 Manual build][47482]
    * [2.6 Mainline kernel][47483]
  * [3 Tips, Tricks, Caveats][47484]
    * [3.1 FEL mode][47485]
    * [3.2 ADB][47486]
  * [4 Adding a serial port (**voids warranty**)][47487]
    * [4.1 Device disassembly][47488]
    * [4.2 Locating the UART][47489]
  * [5 Pictures][47490]
  * [6 Also known as][47491]
  * [7 See also][47492]

# Identification
When disassembled, the back of the board (connector side) will read _94V-0_ and _E232205_. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: AK-MINI-PC-001
  * Build Number: crane_risctek-eng 4.0.3 IML74K 20120608 test-keys

Or: 
  * Model Number: SoftwinnerEvb
  * Build Number: apollo_tvdevb-eng 4.0.4 IMM76D 20120710 test-keys

# Sunxi support
## Current status
Supported. 
## Images
Success with Debian arm installer by selecting pcduino in the installer menu. Possibly no wireless, used a usb ethernet for LAN and iso image on usb stick for Debian installer data. Process of making an installer SD card is described here: [Debian Installer SD Card Instructions][47493]
used: 
`firmware.pcDuino.img.gz`
and 
`?partition.img.gz`
from here: [Debian FTP Site][47494]
plus on a usb stick: `debian-stretch-DI-alpha8-armhf-netinst.iso` from [Debian Installer][47495] (I hope these links stand the test of time). 
Connect HDMI and usb keyboard - the installer may show on the monitor, or maybe on serial. Serial is essential if you want to install a non-gui debian. 
Please report here if anyone tries to modify this to use the correct mk802 device tree. (note: I did try this now, and it failed to run the kernel. This could mean I don't have a true Rikomagic MK802, or it could mean that the default sun4i-a10-mk802.dtb in Debian is wrong. My 'mk802' is marked 'DDR3/1GB' on the back.... If you try, then leave a copy of the pcduino dtb next to the new dtb, then you can swap in uboot by 'setenv fdtfile'). 
note [Mainline][47496] has been enhanced with Debian kernel build notes. 
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "mk802" target.
  * The .fex file can be found in sunxi-boards as [mk802.fex][47497]

Everything else is the same as the [manual build howto][47498]. 
## Mainline kernel
Use the _sun4i-a10-mk802.dts_ device-tree file for the [mainline kernel][47496]. 
# Tips, Tricks, Caveats
## FEL mode
The FEL button can be found by placing a pin into the hole in the bottom left corner on the top cover of the device. Pressing when powering up triggers [ FEL mode][47499]. 
## ADB
The device is factory rooted but so far ADB over USB hasn't been possible. To use ADB install a SSH Server like SSHDroid and start up the service. With the information provided by the Android App you can remotely log into the device(the login prompt displays the password. Type "adb shell" to enter [ADB][47500] mode. 
# Adding a serial port (**voids warranty**)
[![][47501]][47502]
[][47503]
DEVICE UART pads
## Device disassembly
The three piece case is clicked together. Do not try to get the semi-transparent bit around the USB Host connector off, as it is clipped into the top and you could damage the clip. Just gently push your [plastic tool][47504] between the bottom and the top, and push the top part of the shell outwards. You will soon hear the clips release. 
To remove the mainboard, be really careful, as all the connectors are wedged in. First release the two accessible clips of the transparent bit around the host connector, you will need this extra mm of space (don't push it further, or you might break the third clip). Then, try to wiggle the female hdmi connector free from its hole in the case. Then, start working the micro-usb-connector, use 2 [plastic tools][47504] to push the whole of the motherboard away from the case, from each side of the usb connector. After some careful wriggling you should be able to get the motherboard out. 
## Locating the UART
The TX and RX pins for UART 0 are next to the SoC. A good place to solder the GND connection is on the ground plane that runs along the side of the board. More information is available at [our UART howto][47505]. 
# Pictures
Below are some pictures of a very heavily maimed mk802. It had led a hard life at its previous owner, who had crudely opened the device (broken clips and lifted USB OTG ground pads) and who badly drilled holes into the case for ventilation. Then there were the tar deposits (heavy smoker) on the usb host and micro-sd connector shields, and the fact that the usb host connector was badly worn... 
  * [![][47506]][47467]
Only the two holes on the left hand side are original. 
  * [![][47507]][47508]
What a messy job this was. 
  * [![Nasty rikomagic mk802 connectors 1.jpg][47509]][47510]
  * [![Nasty rikomagic mk802 connectors 2.jpg][47511]][47512]
  * [![Nasty rikomagic mk802 connectors 3.jpg][47513]][47514]
  * [![Nasty rikomagic mk802 connectors 4.jpg][47515]][47516]
  * [![Nasty rikomagic mk802 board front.jpg][47517]][47518]
  * [![Nasty rikomagic mk802 board back.jpg][47519]][47520]

If anyone has a cleaner device, feel free to [ upload better pictures here][47521]. 
There should also be a green PCB version available. This has a much later timestamp (at least 1234), but still mentions _94V-0_ and _E233305_. The layout looks the same, but the FEL button seems to be missing. 
# Also known as
# See also
  * [Rikomagic MK802+][47472]: A 1GiB version of the original MK802 with a redesigned motherboard, but the same case.
  * [Semitime G2][47473]: A 1GiB A10s based device with the same case.
  * [Rikomagic MK802II][47474]: A completely redesigned A10 based HDMI stick.
