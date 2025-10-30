# HiVision PWS700YA
HiVision PWS700YA  
---  
[![Device front.jpg][23945]][23946]  
Manufacturer |  [HiVision][23947]  
Dimensions |  185 _mm_ x 123 _mm_ x height _mm_ (265g)   
Release Date |  August 2012   
Website |  [Defunct Product Page][23948]  
Specifications   
SoC |  [A13][23949] @ 1Ghz   
DRAM |  512MiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ 1.5A, 2800mAh 3.7V Li-Ion battery   
Features   
LCD |  640x480 (7" 16:9)   
Touchscreen |  X-finger capacitive/resistive (TODO: [Manufacturer device][23950])   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188CTV)   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front   
Other |  Accelerometer ([ Domintech DMARD06][23951])   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][23952] and the [New Device Page guide][23953].
## Contents
  * [1 Identification][23954]
  * [2 Sunxi support][23955]
    * [2.1 Current status][23956]
    * [2.2 Images][23957]
    * [2.3 HW-Pack][23958]
    * [2.4 BSP][23959]
    * [2.5 Manual build][23960]
  * [3 Tips, Tricks, Caveats][23961]
    * [3.1 FEL mode][23962]
    * [3.2 HDMI][23963]
  * [4 Adding a serial port (**voids warranty**)][23964]
    * [4.1 Device disassembly][23965]
    * [4.2 Locating the UART][23966]
  * [5 Pictures][23967]
  * [6 Also known as][23968]
  * [7 See also][23969]

# Identification
Find out the strings as reported under settings.
In android, under Settings->About Tablet, you will find: 
  * Model Number: DEVICE
  * Build Number: SOC_BOARD_DEVICE_*.*

The following was acquired differently: 
  * Name in build.prop: PWS700YA
  * Brand in build.prop: HWX
  * Product name: nuclear_708h9
  * Device name: nuclear-708h9
  * Board name: nuclear

# Sunxi support
## Current status
No patches have been submitted, so no support is available.
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][23970]

Everything else is the same as the [manual build howto][23971]. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][23972]. 
## HDMI
Even though a HDMI connector has been soldered onto the board, the [A13][23949] does not natively support HDMI, and the connector does not seem to be functional. Perhaps this connector was just added to suit this popular case format? 
# Adding a serial port (**voids warranty**)
[![][23973]][23974]
[][23975]
DEVICE UART pads
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped.
Remove the small screws on each edge of the connectors side, then unclip the backplate from the LCD housing by inserting something thin in the gap between them. 
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][23976].
There seems to be a few pads right next to the SoC. One pair of them is bound to be RX/TX. 
# Pictures
Take some pictures of your device, [ upload them][23977], and add them here.
  * [![Device front.jpg][23978]][23946]
  * [![Device back.jpg][23979]][23980]
  * [![Device buttons 1.jpg][23981]][23982]
  * [![Device buttons 2.jpg][23983]][23984]
  * [![Device board front.jpg][23985]][23986]
  * [![Device board back.jpg][23987]][23988]

  * [![PWS700YA-1.jpg][23989]][23990]
  * [![PWS700YA-2.jpg][23991]][23992]

# Also known as
  * [Gonomad][23993] PWS700YA

# See also
Add some nice to have links here. This includes related devices, and external links.
