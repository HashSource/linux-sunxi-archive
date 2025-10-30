# MarsBoard A20-SOM
MarsBoard A20-SOM  
---  
[![MarsBoard A20-SOM Baseboard.jpg][35577]][35578]  
Manufacturer |  [Haoyu Electronics][35579]  
Dimensions |  _115_ mm x _90_ mm x _18_ mm   
Release Date |  June 2014   
Website |  [Product website][35580]  
Specifications   
SoC |  [A20][35581] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz   
NAND |  8GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full), VGA, LCD-RGB, Composite   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188EU][35582]), 10/100Mbps Ethernet ([Microchip LAN8710A][35583])   
Storage |  µSD, SATA   
USB |  4 x USB2.0 Host, 1 x USB2.0 OTG   
Other |  Composite TV Input, CR1220 Cell for RTC   
Headers |  MicroUSB Debug UART (CP210x), LVDS, 2 x EXT   
This page needs to be properly filled according to the [New Device Howto][35584] and the [New Device Page guide][35585].
The MarsBoard A20-SOM was a short-lived, credit-card sized, extendable board with an Allwinner [A20][35581] SoC. The SOM variant (different from [Marsboard A20][35586]) has a completely different design though, with a SOM and a baseboard. 
## Contents
  * [1 Identification][35587]
  * [2 Sunxi support][35588]
    * [2.1 Current status][35589]
    * [2.2 Images][35590]
    * [2.3 HW-Pack][35591]
    * [2.4 BSP][35592]
    * [2.5 Manual build][35593]
    * [2.6 Mainline U-Boot][35594]
    * [2.7 Mainline kernel][35595]
  * [3 Tips, Tricks, Caveats][35596]
    * [3.1 FEL mode][35597]
  * [4 Pictures][35598]
  * [5 See also][35599]

# Identification
The Computer On Module PCB has the following silkscreened on it: 
[code] 
    CM-A10/A20
    Designed by Haoyu Electronics
    Marsboard Rev 2.0
    www.powermcu.com
    www.marsboard.com
[/code]
The Baseboard PCB has the following silkscreened on it: 
[code] 
    SOM-A10/A20
    Designed by Haoyu Electronics
    Open Source Hardware logo
    www.powermcu.com
    www.marsboard.com
[/code]
# Sunxi support
## Current status
Give a brief overview of the current status of support under sunxi here. If there is mainline support for either u-boot or kernel, mention this too, but add the extra sections below.
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the _MANUFACTURER_DEVICE_ target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][35600]

Everything else is the same as the [manual build howto][35601]. 
## Mainline U-Boot
Not currently supported. 
## Mainline kernel
Not currently supported. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The 'ESC' button triggers [ FEL mode][35602]. 
# Pictures
  * [![Marsboard A20-SOM Top.jpg][35603]][35604]
  * [![Marsboard A20-SOM Bottom.jpg][35605]][35606]
  * [![Marsboard SOM-Baseboard Top.jpg][35607]][35608]
  * [![Marsboard SOM-Baseboard Bottom.jpg][35609]][35610]
  * [![Marsboard A20-SOM Debug.jpg][35611]][35612]

# See also
Add some nice to have links here. This includes related devices, and external links.
