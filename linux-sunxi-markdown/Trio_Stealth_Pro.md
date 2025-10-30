# Trio Stealth Pro
Trio Stealth Pro  
---  
[![Trio Stealth Pro Front.jpg][55809]][55810]  
Manufacturer |  Trio   
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  Month year   
Website |  [Product page][55811]  
Specifications   
SoC |  [A10][55812] @ 1Ghz   
DRAM |  1GB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  DC 5V @ 1.5A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 9.7"   
Touchscreen |  X-Finger Capacitive ([FocalTech FT5x06][55813])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188???)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 0.3MP (640x480) rear   
Other |  Accelerometer ([Domintech DMARD06][55814])   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][55815] and the [New Device Page guide][55816].
## Contents
  * [1 Identification][55817]
  * [2 Sunxi support][55818]
    * [2.1 Current status][55819]
    * [2.2 Images][55820]
    * [2.3 HW-Pack][55821]
    * [2.4 BSP][55822]
    * [2.5 Manual build][55823]
  * [3 Tips, Tricks, Caveats][55824]
    * [3.1 FEL mode][55825]
  * [4 Adding a serial port (**voids warranty**)][55826]
    * [4.1 Device disassembly][55827]
    * [4.2 Locating the UART][55828]
  * [5 Pictures][55829]
  * [6 Also known as][55830]
  * [7 See also][55831]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: TRIO-97C
  * Build Number: crane_cube-eng 4.0.4 IMM76D 20130515

# Sunxi support
## Current status
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][55832]

Everything else is the same as the [ Manual build howto][55833]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][55834]. 
# Adding a serial port (**voids warranty**)
[![][55835]][55836]
[][55837]
DEVICE UART pads
## Device disassembly
The device is easily disassembled by sliding your [plastic tool][55838] between the metal back plate and the black plastic ring around the edge of the device. 
## Locating the UART
The UART0 RX/TX pins are identified in the picture to the right. The red arrow points to UART0_TX and the blue arrow points to UART0_RX. These pads are located on the back side of the PCB. 
# Pictures
  * [![Trio Stealth Pro Front.jpg][55839]][55810]
  * [![Trio Stealth Pro Back.jpg][55840]][55841]
  * [![Trio Stealth Pro Buttons1.jpg][55842]][55843]
  * [![Trio Stealth Pro Buttons2.jpg][55844]][55845]
  * [![Trio Stealth Pro PCB Front.jpg][55846]][55847]
  * [![Trio Stealth Pro PCB Back.jpg][55848]][55849]

# Also known as
# See also
  * [A10-meminfo][55850]
  * Original firmware [boot log][55851]
  * Original firmware [dmesg][55852]
  * Original firmware [script.bin][55853]
  * Original firmware [script.fex][55854]
