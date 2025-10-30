# Wexler TAB 7200
Wexler TAB 7200  
---  
[![Wexler Tab 7200 front.jpg][58975]][58976]  
Manufacturer |  [Wexler][58977]  
Dimensions |  198 _mm_ x 123 _mm_ x 11 _mm_  
Release Date |  August 2013   
Website |  [Product Page][58978]  
Specifications   
SoC |  [A20][58979] @ 1Ghz   
DRAM |  1GiB DDR3 @ 384MHz   
NAND |  4GB   
Power |  USB, 4000mAh 3.7V Li-Ion battery   
Features   
LCD |  800x480 (7" 16:9)   
Touchscreen |  5-finger capacitive ([Goodix GT911][58980])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal microphone,   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8192CU][58981])   
Storage |  µSD   
USB |  1 USB2.0 HOST, 1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([Domintech ARD06][58982]), reset button   
Headers |  UART   
## Contents
  * [1 Identification][58983]
  * [2 Sunxi support][58984]
    * [2.1 Current status][58985]
    * [2.2 Images][58986]
    * [2.3 HW-Pack][58987]
    * [2.4 BSP][58988]
    * [2.5 Manual build][58989]
      * [2.5.1 U-Boot][58990]
        * [2.5.1.1 Sunxi/Legacy U-Boot][58991]
        * [2.5.1.2 Upstream/Mainline U-Boot][58992]
      * [2.5.2 Linux Kernel][58993]
        * [2.5.2.1 Sunxi/Legacy Kernel][58994]
        * [2.5.2.2 Upstream/Mainline kernel][58995]
  * [3 Tips, Tricks, Caveats][58996]
    * [3.1 FEL mode][58997]
    * [3.2 Touchscreen][58998]
    * [3.3 Accelerometer][58999]
  * [4 Adding a serial port][59000]
    * [4.1 Device disassembly][59001]
    * [4.2 Locating the UART][59002]
  * [5 Pictures][59003]
  * [6 See also][59004]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: TAB7200
  * Build Number: wing_mid-eng 4.2.2 *

# Sunxi support
## Current status
Everything working, except touchscreen and accelerometer. 
## Images
## HW-Pack
## BSP
## Manual build
You can build things for yourself by following our [ Manual build howto][59005] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _Wexler_TAB_7200_ build target. 
#### Upstream/Mainline U-Boot
Use the _Wexler_TAB7200_ target for building [mainline U-Boot][59006]. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_wexler_tab_7200.fex_][59007] file. 
#### Upstream/Mainline kernel
Use the _sun7i-a20-wexler-tab7200.dtb_ device-tree binary for the [mainline kernel][59008]. 
# Tips, Tricks, Caveats
## FEL mode
The Volume down button triggers [FEL mode][59009]. 
## Touchscreen
The touchscreen supported in mainline kernel via common **goodix** driver. 
## Accelerometer
No mainline support. 
No driver in sunxi-3.4, patch can be found [on our mailinglist][59010]. 
# Adding a serial port
[![][59011]][59012]
[][59013]
Wexler TAB 7200 UART pads.
## Device disassembly
Careful insert your [plastic tool][59014] in the space between the USB HOST port and the back cover. Then, gently move the tool towards the camera, and you should soon hear the clips popping. Move the plastic tool from edge to edge, until the back cover comes off. 
## Locating the UART
There are some small pads on the bottom of the board, near the SoC. Solder on some wires according to our [UART howto][59015]. 
# Pictures
  * [![Wexler Tab 7200 front.jpg][59016]][58976]
  * [![Wexler Tab 7200 back.jpg][59017]][59018]
  * [![Wexler Tab 7200 rear.jpg][59019]][59020]
  * [![Wexler Tab 7200 board front.jpg][59021]][59022]
  * [![Wexler Tab 7200 board back.jpg][59023]][59024]

# See also
