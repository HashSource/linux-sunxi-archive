# Miniand Hackberry
Miniand Hackberry  
---  
[![Miniand hackberry a10 top.jpg][38099]][38100]  
Manufacturer |  [Miniand][38101]  
Dimensions |  85.60 _mm_ x 54 _mm_ x height _mm_  
Release Date |  September 2012   
Website |  [Hackberry Product Page][38102]  
Specifications   
SoC |  [A10][38103] @ 1Ghz   
DRAM |  512MiB/1GiB DDR3 @ 408MHz   
NAND |  4GB (also limited edition 8GB model)   
Power |  DC 5V @ 1A   
Features   
Video |  HDMI (Type A - full), AV connector, YPbPr connector   
Audio |  3.5mm microphone plug, HDMI, AV connector   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188CUS][38104]), 10/100Mbps Ethernet ([Realtek RTL8201CP][38105])   
Storage |  SD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG (lower one)   
Other |  IRDA, Power Button, Reset Button, Recovery Button   
Headers |  UART   
The hackberry is an [A10][38103] "development" board which has no external headers. 
## Contents
  * [1 Identification][38106]
  * [2 Sunxi support][38107]
    * [2.1 Current status][38108]
    * [2.2 Images][38109]
    * [2.3 HW-Pack][38110]
    * [2.4 BSP][38111]
    * [2.5 Manual build][38112]
    * [2.6 Mainline kernel][38113]
  * [3 Tips, Tricks, Caveats][38114]
    * [3.1 FEL mode][38115]
  * [4 Adding a serial port][38116]
  * [5 Pictures][38117]
  * [6 Also known as][38118]
  * [7 See also][38119]

# Identification
Unfortunately there's no branding printed on this board to help identify it, but a visual inspection of the pictures should help you identify it. The PCB board is also red. 
In android, under Settings->About Tablet, you will find: 
  * Model Number: TV_T100
  * Build Number: 4.0.4 IMM76D 20120920 test-keys

# Sunxi support
## Current status
Supported. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Hackberry" target.
  * The .fex file can be found in sunxi-boards as [hackberry.fex][38120]

Everything else is the same as the [manual build howto][38121]. 
## Mainline kernel
Use the sun4i-a10-hackberry.dts device-tree file for the [mainline kernel][38122]. 
# Tips, Tricks, Caveats
## FEL mode
THIS IS UNTESTED
The Reset button (just under the DC jack) triggers [ FEL mode][38123] on the OTG USB port (the lower one). 
# Adding a serial port
[![][38124]][38125]
[][38126]
Hackberry UART port
Recently the Hackberry has been shipped with a 4 wire cable with male headers on each end that will fit into the UART port. You can refer to the picture for the pin-outs and read the [UART howto][38127] on how to use this. 
# Pictures
  * [![Miniand hackberry a10 top.jpg][38128]][38100]
  * [![Miniand hackberry a10 bottom.jpg][38129]][38130]
  * [![Miniand hackberry a10 ports.jpg][38131]][38132]

# Also known as
  * HackBerry A10

There are no rebadgers for this type of device. 
# See also
  * [Rhombus-Tech: Hackberry A10 Dev Board][38133] \- datasheets and schematics can be found here
  * [Miniand Hackberry A10 forums][38134]
