# Onda VX610W
Onda VX610W  
---  
[![Device front.jpg][41740]][41741]  
Manufacturer |  [Onda][41742]  
Dimensions |  186 _mm_ x 144 _mm_ x 14 _mm_  
Release Date |  Month year  
Website |  [Product Page][41743]  
Specifications   
SoC |  [A10][41744] @ 1Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  8GB   
Power |  DC 5.2V @ 1A, ??00mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([FocalTech FT5206][41745])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188CUS)   
Storage |  µSD   
USB |  X USB2.0 Host, X USB2.0 OTG   
Other |  Accelerometer ([Freescale MMA7660FC][41746])   
Headers |  UART, JTAG   
This page needs to be properly filled according to the [New Device Howto][41747] and the [New Device Page guide][41748].
## Contents
  * [1 Identification][41749]
  * [2 Sunxi support][41750]
    * [2.1 Current status][41751]
    * [2.2 Images][41752]
    * [2.3 HW-Pack][41753]
    * [2.4 BSP][41754]
    * [2.5 Manual build][41755]
  * [3 Tips, Tricks, Caveats][41756]
    * [3.1 FEL mode][41757]
  * [4 Adding a serial port (**voids warranty**)][41758]
    * [4.1 Device disassembly][41759]
    * [4.2 Locating the UART][41760]
  * [5 Pictures][41761]
  * [6 Also known as][41762]
  * [7 See also][41763]

# Identification
Find out the strings as reported under settings.
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

# Sunxi support
## Current status
Not supported. No patches have ever been submitted.
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][41764]

Everything else is the same as the [manual build howto][41765]. 
# Tips, Tricks, Caveats
## FEL mode
The something button triggers [ FEL mode][41766]. 
# Adding a serial port (**voids warranty**)
[![][41767]][41768]
[][41769]
UART pads
## Device disassembly
Provide a short description of how to open the device. Explain how the pins can be most easily popped.
## Locating the UART
There is a set of test pads above the SoC, all you have to do is solder on some wires according to our [UART howto][41770]. 
# Pictures
Take some pictures of your device, [ upload them][41771], and add them here.
  * [![Device front.jpg][41772]][41741]
  * [![Device back.jpg][41773]][41774]
  * [![Device buttons 1.jpg][41775]][41776]
  * [![Device buttons 2.jpg][41777]][41778]
  * [![Device board front.jpg][41779]][41780]
  * [![Device board back.jpg][41781]][41782]

  * [![Onda vx610w v1 pcb.jpg][41783]][41784]
  * [![Onda vx610w v1 battery antenna buttons.jpg][41785]][41786]
  * [![Onda vx610w v1 a.jpg][41787]][41788]

# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
