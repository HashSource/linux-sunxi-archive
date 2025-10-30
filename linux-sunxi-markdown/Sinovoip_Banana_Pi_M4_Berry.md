# Sinovoip Banana Pi M4 Berry
Sinovoip Banana Pi M4 Berry  
---  
[![Banana Pi M4 Berry Front.jpeg][50590]][50591]  
Manufacturer |  [Sinovoip][50592]  
Dimensions |  56 _mm_ x 85 _mm_ x 20 _mm_  
Release Date |  Nov 2023  
Website |  [BPI M4 Berry Product Page][50593]  
Specifications   
SoC |  [H618][50594] @ 1.512 Ghz   
DRAM |  2GiB LPDDR4 @ 792 MHz   
Power |  DC 5V @ 3A via USB-C connector   
Features   
Video |  HDMI 2.0a   
Audio |  3.5mm headphone plug  
HDMI   
Network |  WiFi 802.11 a/b/g/n/ac (Realtek RTL8821CU)  
10/100/1000Mbps Ethernet (Realtek RTL8211F)  
Bluetooth4.2 (Realtek RTL8821CU)   
Storage |  µSD, 8GB eMMC (Samsung)   
USB |  4 USB2.0 Host (via hub chip), 1 USB2.0 OTG   
Headers |  UART, GPIO, I2S, I2C, SPI   
Not to be confused with Banana Pi M4 (w/Realtek SOC). This is Raspberry Pi 3+ clone board using the H618 SOC. It has PoE pins for use with PoE Hat. 
## Contents
  * [1 Identification][50595]
  * [2 Sunxi support][50596]
    * [2.1 Current status][50597]
    * [2.2 Manual build][50598]
      * [2.2.1 U-Boot][50599]
        * [2.2.1.1 Vendor U-Boot][50600]
        * [2.2.1.2 Mainline U-Boot][50601]
      * [2.2.2 Linux Kernel][50602]
        * [2.2.2.1 Vendor Kernel][50603]
        * [2.2.2.2 Mainline kernel][50604]
  * [3 Tips, Tricks, Caveats][50605]
    * [3.1 FEL mode][50606]
    * [3.2 Locating the UART][50607]
  * [4 Pictures][50608]
  * [5 Schematic][50609]
  * [6 See also][50610]
    * [6.1 Manufacturer images][50611]

# Identification
The PCB has the following silkscreened on the front: 
[code] 
    (Banana Pi Logo) 
    BPI_M4B
    V00
[/code]
# Sunxi support
## Current status
Many features (eMMC, USB, Ethernet, GPIO, WiFi(?)) are supported by mainline Linux, but audio and video support are missing (see the H616 column of the [status matrix][50612] for more details). U-Boot support is usable. 
## Manual build
You can build things for yourself by following our [ Manual build howto][50613] and by choosing from the configurations available below. 
### U-Boot
#### Vendor U-Boot
<https://github.com/BPI-SINOVOIP/pi-u-boot/tree/v2021.07-sunxi>
#### Mainline U-Boot
LPDDR4 support and AXP313a PMIC support were merged into U-Boot v2024.01-rc3. 
### Linux Kernel
#### Vendor Kernel
<https://github.com/BPI-SINOVOIP/pi-linux/tree/pi-6.1-sunxi>
Use the _sun50i-h618-bananapi-m4berry.dtb_ device-tree binary. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary.
[Patches are available][50614], but untested, so not upstreamed. Please report back to [ Andre][50615] when you have tested these. 
# Tips, Tricks, Caveats
## FEL mode
The FEL/SW2 button triggers [ FEL mode][50616]. 
## Locating the UART
The UART pins are located near back of right USB ports, in a clearly distinct group of three pins. They are marked as _TX_ , _RX_ and _GND_ on the PCB. Just attach some leads according to our [UART Howto][50617]. 
# Pictures
  * [![Banana Pi M4 Berry Top.jpeg][50618]][50619]
  * [![Banana Pi M4 Berry Bottom.jpeg][50620]][50621]

# Schematic
[Banana Pi M4 Berry board v00 schematic][50622]
# See also
[Device page on Banana Pi Wiki][50623]  
[Official Forum][50624]  

## Manufacturer images
[Manufacturer images on Banana Pi Wiki page][50625]
