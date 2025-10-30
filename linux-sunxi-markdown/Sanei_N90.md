# Sanei N90
Sanei N90  
---  
[![M9701-front.jpg][48814]][48815]  
Manufacturer |  [Sanei][48816]  
Dimensions |  242 _mm_ x 190 _mm_ x 9.8 _mm_  
Release Date |  February 2012   
Website |  [Product page][48817]  
Specifications   
SoC |  [A10][48818] @ 1Ghz   
DRAM |  1GiB DDR3 @ 456MHz ([H5TQ2G83CFR-H9C][48819])   
NAND |  16GB (Micron 29F64C08CBAAA)   
Power |  DC 5V @ 3A, 7200mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (9.7" 4:3) IPS   
Touchscreen |  10-finger capacitive ([Focaltech FT5606NED][48820])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (Realtek RTL8192CUS)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  640x480 (VGA) front, 1920x1080 (HD) rear   
Other |  Accelerometer ([Bosch BMA250][48821]), Bluetooth   
This page needs to be properly filled according to the [New Device Howto][48822] and the [New Device Page guide][48823].
The "single core" version of the Sanei N90/Ampe A90 is a 9.7" A10-based tablet. 
## Contents
  * [1 Identification][48824]
  * [2 Sunxi support][48825]
    * [2.1 Current status][48826]
    * [2.2 Images][48827]
    * [2.3 HW-Pack][48828]
    * [2.4 BSP][48829]
    * [2.5 Manual build][48830]
      * [2.5.1 U-Boot][48831]
        * [2.5.1.1 Sunxi/Legacy U-Boot][48832]
        * [2.5.1.2 Upstream/Mainline U-Boot][48833]
      * [2.5.2 Linux Kernel][48834]
        * [2.5.2.1 Sunxi/Legacy Kernel][48835]
        * [2.5.2.2 Upstream/Mainline kernel][48836]
  * [3 Tips, Tricks, Caveats][48837]
    * [3.1 Camera][48838]
    * [3.2 FEL mode][48839]
  * [4 Adding a serial port (**voids warranty**)][48840]
    * [4.1 Device disassembly][48841]
    * [4.2 Locating the UART][48842]
  * [5 Pictures][48843]
  * [6 Variants][48844]
  * [7 Also known as][48845]
  * [8 See also][48846]

# Identification
In Android, under Settings->About Tablet, you will find: 
  * Model Number: M9701
  * Build Number: crane_anpei-eng 4.0.3 IML74K 20120622 test-keys

# Sunxi support
## Current status
Fully supported (except for the cameras) by the legacy U-Boot and kernel; _not_ yet supported by upstream U-Boot or kernel. 
## Images
## HW-Pack
## BSP
## Manual build
You can build things for yourself by following our [ Manual build howto][48847] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _Sanei_N90_ build target. 
#### Upstream/Mainline U-Boot
Not supported. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_sanei_n90.fex_][48848] file. 
#### Upstream/Mainline kernel
Not supported. 
# Tips, Tricks, Caveats
## Camera
Interesting work, but this needs a better solution, like some patches or so.
As shipped, the device has "gc0308" and "gc0308b" modules loaded for the two cameras. Source for the latter doesn't appear to be available, but disassembling the two binaries shows that they're identical except that references to "client->addr" (the camera's I2C address) in "gc0308" have been changed to "0x21" in "gc0308b", and the "CSI_SUBDEV_PWR_OFF" handler in "sensor_power" calls "csi_gpio_write" rather than "csi_gpio_set_status". The hardcoded I2C address doesn't match the one in the shipped .fex file. 
## FEL mode
The Vol+ button triggers [FEL mode][48849]. 
# Adding a serial port (**voids warranty**)
[![][48850]][48851]
[][48852]
DEVICE UART pads
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped.
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][48853].
# Pictures
  * [![M9701-front.jpg][48854]][48815]
  * [![M9701-back.jpg][48855]][48856]
  * [![M9701-side.jpg][48857]][48858]
  * [![Device board front.jpg][48859]][48860]
  * [![Device board back.jpg][48861]][48862]

# Variants
Ampe/Sanei have used the same model names for later tablets using the same form factor, which aren't Allwinner-based. The original "single core" version, using an Allwinner A10, was released in February 2012 ([press release][48863]). They've since built a "dual core" version using the Rockchip RK3066, and a "quad core" version ([Ampe A90][48864], [Sanei N90][48865]) using the Mediatek MTK8382. 
# Also known as
  * Ampe A90
  * [LinITX TP-971AE][48866] (unbranded)

# See also
  * [Sanei Android firmware updates for the N90][48867].
  * [N90 discussion thread on SlateDroid][48868]
  * [Photos showing the inside of an N90][48869]
  * [Photo of the N90 motherboard][48870]
  * [Video showing how to dismantle an N90][48871]
  * [Christian Troy's A10 CyanogenMod][48872] supported the N90, using the vendor kernel
  * [Manifest for CyanogenMod jellybean for the N90][48873], based on [allwinner-dev-team's A10 port][48874] and the linux-sunxi kernel
