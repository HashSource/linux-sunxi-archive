# Tena b133
Tena b133  
---  
[![Device front.jpg][54860]][54861]  
Manufacturer |  [Shenzhen Tena][54862]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  September 2013   
Website |  [Product page][54863]  
Specifications   
SoC |  [A20][54864] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI, VGA   
Audio |  3.5mm AV connector, HDMI   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188ETV), 10/100Mbps Ethernet (IC Plus IP101A)   
Storage |  µSD   
USB |  2 USB2.0 Host   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][54865] and the [New Device Page guide][54866].
## Contents
  * [1 Identification][54867]
  * [2 Sunxi support][54868]
    * [2.1 Current status][54869]
    * [2.2 Images][54870]
    * [2.3 HW-Pack][54871]
    * [2.4 BSP][54872]
    * [2.5 Manual build][54873]
  * [3 Tips, Tricks, Caveats][54874]
    * [3.1 FEL mode][54875]
    * [3.2 USB power][54876]
    * [3.3 Power On/Off][54877]
  * [4 Adding a serial port (**voids warranty**)][54878]
    * [4.1 Device disassembly][54879]
    * [4.2 Locating the UART][54880]
  * [5 Pictures][54881]
  * [6 Also known as][54882]
  * [7 See also][54883]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: B133
  * Build Number: A20_B133-eng 4.4.4 JDQ39 20140221 test-keys

# Sunxi support
## Current status
Patches are on the mailing list, but there are some issues with the sunxi-3.4 stable kernel and the way the USBCs are configured in the .fex. The sunxi-3.3 kernel does seem to work. Following works with sunxi-3.3 : 
  * Wireless
  * NAND
  * USB Ports
  * SDCards
  * 10/100MBps Ethernet

What does not work: 
  * G2D engine seems to have problem with the sunxi-3.3 kernel

## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][54884]

Everything else is the same as the [manual build howto][54885]. 
# Tips, Tricks, Caveats
## FEL mode
There is a pinhole on the case to reach the recovery button which is near the RJ45 port. The USB port nearest to the SDcard is of OTG type even though it looks just like a normal USB port . If the device is put in recovery mode and then the port can be used to connect the device to a PC using a usb cable that is female type on both the ends. It was also possible to flash this device with LiveSuit on linux using the USB port. 
## USB power
When trying to power over USB, do not use a host port from another device, but instead use standalone powersupply still as otherwise the amperage delivered does not suffice. 
This is a case where you will run into trouble with your [UART adapter][54886] if you have connected Vcc.   
**Update:** It is possible to power up and run the device using the OTG USB port on the device. Refer Fel section for identification of the OTG port. However the current from usb hosts are limited to 500mA. 
## Power On/Off
There is no power switch, you have to power it down through software and restart it by reattaching the power cable. 
# Adding a serial port (**voids warranty**)
[![][54887]][54888]
[][54889]
DEVICE UART pads
Note if you are using CA-42 cable u need to attach the VCC. 
libv> i do not believe that, [this link][54890] shows the cable as a generic UART, without Vcc attach.
## Device disassembly
Disassembly is easy. Just unscrew the 4 screws concealed below the rubber footpads. Then lift up the TOP cover with a paper cutter. It should pop out with ease. The PCB can be taken out gently from the casing by lifting it up from the end which does NOT carries the connectors. Take care of the wireless antenna that is glued on the edge of the casing. Do NOT desolder the atenna lead unless you really need to. (PS: do not attempt to force out the PCB with sdcard plugged in unless you want to Guillotone your card ). 
## Locating the UART
There are four pin holes on the board on the left of the 2 memory chips. These holes first needs to be desoldered and then you can solder a 4 pin header block. the pin nearest to the memory banks is the GND to its left are the RX , TX and VCC. 
# Pictures
Take some pictures of your device, [ upload them][54891], and add them here.
  * [![Device front.jpg][54892]][54861]
  * [![Device back.jpg][54893]][54894]
  * [![Device buttons 1.jpg][54895]][54896]
  * [![Device buttons 2.jpg][54897]][54898]
  * [![2014-04-05-161.jpg][54899]][54900]
  * [![Device board front.jpg][54901]][54902]
  * [![Device board back.jpg][54903]][54904]

# Also known as
# See also
