# MSI Primo73L
MSI Primo73L  
---  
[250px][33257]  
Manufacturer |  [MSI][33258]  
Dimensions |  196 _mm_ x 121 _mm_ x 9.5 _mm_  
Release Date |  2013   
Website |  No longer available   
Specifications   
SoC |  [A23][33259] @ 1Ghz   
DRAM |  512MiB DDR3 @ 552MHz   
NAND |  8GB   
Power |  DC 5V @ 3A, 3000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" 16:9)   
Touchscreen |  X-finger capacitive ([Silead GSLx680][33260])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV - 0bda:0179][33261])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  GC0308 0.3MP (640x480) front, GC2035 2.0MP (1600x1200) rear   
Other |  Accelerometer ([Sensortek STK8312][33262])   
Headers |  Internal UART, JTAG; unidentified test points   
This page needs to be properly filled according to the [New Device Howto][33263] and the [New Device Page guide][33264].
This is a brand name tablet from a reputable hardware vendor, so no problems with identification are expected. The tablet has a sturdy metal back cover and the overall build quality is good. The design is almost the same as [MSI Primo73][33265], but missing the mini-HDMI port. 
## Contents
  * [1 Identification][33266]
  * [2 Sunxi support][33267]
    * [2.1 Current status][33268]
      * [2.1.1 U-Boot][33269]
        * [2.1.1.1 Mainline U-Boot][33270]
      * [2.1.2 Linux Kernel][33271]
        * [2.1.2.1 Mainline kernel][33272]
  * [3 Tips, Tricks, Caveats][33273]
    * [3.1 FEL mode][33274]
    * [3.2 Device specific topic][33275]
    * [3.3 ...][33276]
  * [4 Adding a serial port (**voids warranty**)][33277]
    * [4.1 Device disassembly][33278]
    * [4.2 Locating the UART][33279]
  * [5 Pictures][33280]
  * [6 See also][33281]

# Identification
On the back of the device, the msi logo is printed in the center of the cover. The following is printed on a label: 
[code] 
    PRIMO 73L-xxxxx
[/code]
with xxxxx likely being region specific. 
The PCB has the following silkscreened on it: 
[code] 
    N71L-A23-V1_1
    2014-05-07
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _Primo73L_
  * Build Number: _Primo73L-user 4.2.2 JDQ39 20140220 release-keys_

# Sunxi support
## Current status
There is currently no support for this device. 
### U-Boot
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][33282]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][33283]][33284]
[][33285]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][33286]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
Remove the two screws from the top of the device, on either side of the I/O ports. Then use a small plastic tool to pry the back cover off of the LCD screen. Insert the tool between the black bezel and grey aluminum back cover. Slowly repeat the process around the circumference of the device. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][33286].
# Pictures
Take some pictures of your device, [ upload them][33287], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][33288]][33289]
  * [![Device back.jpg][33290]][33291]
  * [![Device buttons 1.jpg][33292]][33293]
  * [![Device buttons 2.jpg][33294]][33295]
  * [![Device board front.jpg][33296]][33297]
  * [![Device board back.jpg][33298]][33299]

# See also
See [MSI Primo73][33265] for the similar looking device.
