# Lamobo R1
Lamobo R1  
---  
[![BPi-R1-top 250px.jpg][30109]][30110]  
Manufacturer |  [Lamobo][30111]  
Dimensions |  148 _mm_ x 100 _mm_ x 18 _mm_  
Release Date |  November 2014   
Website |  [[1]][30112] [BPi-R1][30113]  
Specifications   
SoC |  [A20][30114] @ 1Ghz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  no nand available   
Power |  DC 5V @ 2A (micro-USB), JST XH 2.5mm header as Battery connector   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5mm headphone plug, HDMI, internal microphone   
Network |  10/100/1000Mbps Ethernet, [Broadcom BCM53125][30115] switch with 5 external GB-Ports; WiFi 802.11 b/g/n ([Realtek RTL8192CU][30116] connected internally via USB2.0, two Hirose U.FL connectors for WiFi antennas)   
Storage |  µSD, SATA   
USB |  1 USB2.0 Host, 1 µUSB2.0 OTG   
Other |  IrDA   
Headers |  UART, LCD/LVDS, CSI, 26 pin GPIO, all fully compatible with [Banana Pi][30117]  
The Lamobo R1 is a [A20][30114] based development board by Lamobo. It shares the majority of hardware with the original [Banana Pi][30117]. It makes not only a nice home automation hub or a NAS but with its on-board VLAN-capable switch, this should make a nice router board as well behind a firewall. 
The board differs from the Banana Pi by having a different layout, allowing directly attaching a 2.5" SATA disk (unlike other SATA capable Bananas here powered through the [AXP209 PMU][30118]), a VLAN-capable [Broadcom BCM53125][30115] switch (see [_security implications_][30119] below) interconnecting the SoC and the 5 GBit Ethernet ports and onboard 802.11 b/g/n Wi-Fi. Since the Lamobo R1 features exactly the same 26 pin GPIO connector as Banana Pi and the ported WiringPi library also works here all hardware Add-Ons utilising GPIO will also work. 
## Contents
  * [1 Identification][30120]
  * [2 Sunxi support][30121]
    * [2.1 Current status][30122]
    * [2.2 Images][30123]
    * [2.3 HW-Pack][30124]
    * [2.4 BSP][30125]
    * [2.5 Manual build][30126]
    * [2.6 Mainline U-Boot][30127]
    * [2.7 Mainline kernel][30128]
  * [3 Tips, Tricks, Caveats][30129]
    * [3.1 FEL mode][30130]
    * [3.2 Current drawbacks][30131]
      * [3.2.1 Powering the board][30132]
      * [3.2.2 SATA power fix][30133]
      * [3.2.3 Network performance][30134]
      * [3.2.4 Available enclosures and thermal issues][30135]
      * [3.2.5 Security Implications][30119]
    * [3.3 Configuring the BCM53125 Switch in Mainline Linux][30136]
    * [3.4 GPIO header][30137]
    * [3.5 Locating the UART][30138]
  * [4 Pictures][30139]
  * [5 Also known as][30140]
  * [6 Variants][30141]
  * [7 See also][30142]
    * [7.1 Manufacturer images][30143]

# Identification
The Device is also marketed as Banana Pi Router or BPi-R1. 
The PCB has the following silkscreened on it: 
[code] 
    Lamobo R1-SD_V3
[/code]
# Sunxi support
## Current status
No support in sunxi 3.4. 
OpenWrt support using kernel 3.18 is currently awaiting upstream. Gigabit Ethernet needs some tickling from U-Boot to properly setup the TX clock delay, the on-board switch works nicely with OpenWrt's b53-mdio driver but there seem to be performance issues when data is transferred between CPU and the outside (traffic bridged by the BCM53125 between switch ports is not affected). The rtl8192cu mac80211 WiFi driver seems to be buggy/not work well with hostapd, however, client and ad-hoc mode works just fine. 
Apart from the on-board switch, the board is very similar to the Banana Pi (M1) - thus any OS capable of running on the Banana Pi should work on the R1 as well. 
## Images
Every image the manufacturer provided so far is broken more or less. These three community projects provide 'ready to run' OS images for the R1 containing .dts/fex files and patches to get the switch working: 
  * [Armbian][30144] also supporting mainline kernel for the R1 over half a year and providing a customizable build system

  * [Bananian][30145] started to support mainline kernel also recently. Status unknown regarding R1

  * [David Bentham's OpenWRT Chaos Calmer fork][30146] claims to have resolved the GMAC speed issues partially

## HW-Pack
## BSP
## Manual build
  * Armbian's working [ .fex][30147] file for kernel 3.4 including [fixed SATA power definition][30148] is now officially included [[2]][30149]
  * For building u-boot it is recommended to rely on u-boot 2015.4 or above and use the _Lamobo_R1_defconfig_ target. As long as it's not included in mainline u-boot you find a patch here [[3]][30150]

To get older kernels booted by recent u-boot versions you have to apply this hack to u-boot sources: 
[code] 
    echo -e "CONFIG_ARMV7_BOOT_SEC_DEFAULT=y\nCONFIG_OLD_SUNXI_KERNEL_COMPAT=y" >> .config
    echo -e "CONFIG_ARMV7_BOOT_SEC_DEFAULT=y\nCONFIG_OLD_SUNXI_KERNEL_COMPAT=y" >> spl/.config
[/code]
Everything else is the same as the [manual build howto][30151]. 
## Mainline U-Boot
For [ building mainline u-boot][30152], use the _Lamobo_R1_defconfig_ target. As long as it's not included in mainline u-boot you find a working version including correct CONFIG_GMAC_TX_DELAY and SATA power config here [[4]][30150]
## Mainline kernel
Use the _sun7i-a20-lamobo-r1.dts_ device-tree file for the [mainline kernel][30153]. As long as it's not included in mainline you can find it here [[5]][30154]
To make the switch working, apply the patches from [[6]][30155]. For 4.0 or above better use these patches including a more recent version of the driver from here [[7]][30156] (some stuff has to be deleted before as outlined in [[8]][30157]
A working .config for kernel 3.19.5 can be found at [[9]][30158]. Since this config doesn't contain CONFIG_FHANDLE=y (necessary for systemd) and some other tweaks another alternative is [[10]][30159] (ready for 4.0 and above) 
# Tips, Tricks, Caveats
## FEL mode
There seems to be no button to enter [ FEL mode][30160]. If no SD card is present, the A20 will automatically fall back to FEL mode (as this device has no other means of booting, like e.g. onboard NAND flash). So if you want to enforce FEL mode, you may simply remove the SD card and connect to the Lamobo R1 via the OTG micro USB (the one next to the USB type A port). This also supplies power to the board at the same time that might not be sufficient to power a SATA disk. So you might have to disconnect a SATA drive to use FEL mode. 
## Current drawbacks
as of June 2015 
  * lousy SATA-write throughput - this is fixed in 2020
  * low Ethernet throughput
  * power supply, connector,
  * enclosures force thermal issues
  * housing proposal a la Lamobo FB posting, stand upright, Acrylglas.

Some details in the text below: 
### Powering the board
[![][30161]][30162]
[][30163]
connection
The Lamobo R1 powers the SATA disk through the AXP209 PMU unlike most other SATA capable Banana Pi variants (a reverse engineered power scheme is available: [File:BPi-R1-power-scheme.pdf][30164] and in early 2016 sinoVoip even managed to publish their [schematics][30142]). Therefore the whole board consumption in A can be read out using I2C/sysfs (1st example for use with 3.4 kernel, 2nd for [patched][30165] mainline kernel): 
[code] 
    awk '{printf ("%0.2f",$1/1000000); }' </sys/devices/platform/sunxi-i2c.0/i2c-0/0-0034/axp20-supplyer.28/power_supply/ac/current_now
    awk '{printf ("%0.2f",$1/1000000); }' </sys/power/axp_pmu/ac/amperage
[/code]
Since powering the board through the Micro-USB power-in connector is often somewhat unreliable (due to voltage drops between PSU and board and a faulty power design of the board) which can lead to all sorts of strange symptoms a different way to power the board is to use the LiPo Battery connector next to the J12/J13 expansion headers. The [AXP209's][30118] charger will disable itself when the voltage on this connector exceeds 4.2V so you can inject here up to 6.5V and exceed the 5V/1.8A limitation of the Micro-USB port. If you power the board this way consumption in A can be read out using (1st example for use with 3.4 kernel, 2nd for [patched][30165] mainline kernel): 
[code] 
    awk '{printf ("%0.2f",$1/1000000); }' </sys/devices/platform/sunxi-i2c.0/i2c-0/0-0034/axp20-supplyer.28/power_supply/battery/current_now
    awk '{printf ("%0.2f",$1/1000000); }' </sys/power/axp_pmu/battery/amperage
[/code]
Polarity of the JST XH header, 5V inwards, GND near the edge – in black.   
housing: JST, XHP-2, 2,5mm, 3A   
crimp: JST, BXH-001T-P0.6   

### SATA power fix
[![][30166]][30167]
[][30168]
Lamobo R1 SATA Power Fix
With the Lamobo R1 electrical design, the SATA drive is powered from the system supply of the AXP209: **IPSOUT**. A maximum of 2.5A can be sourced from this supply, which is barely enough to power a SATA drive and the rest of the system when the drive is busy. More specifically, spikes in the current consumption caused by the drive's activity can cause the system voltage and remaining available current to lower below the required minimum for proper operation of the DRAM, that will get corrupted. When DRAM corruption happens, the kernel soon fails to handle kernel paging requests, as the page table got corrupted. 
In order to fix this issue, the input of the SATA voltage regulator has to be diverted from **IPSOUT** to **ACIN** or **VBAT** directly. Resistor **R6** connects the SATA voltage regulator's input to **IPSOUT**. It can be moved to the unpopulated pads of **R51** to connect the input to **VBAT** or it can be removed to connect **ACIN** , sourced from **CT5/C16** to the input, as shown in the picture. 
### Network performance
Some of the available OS images for the Lamobo R1 suffer from missing CONFIG_GMAC_TX_DELAY adjustments in u-boot (4 seems to be the best value). This results in bad performance when network packets are transferred between A20 SoC and the outside. Even with correctly set GMAC TX delay settings the network throughput is bad compared to the combination GMAC+RTL8211E (with optimised TCP/IP stack tuning noone achieved more than 370/460 Mbits/sec TX/RX using iperf with 100% CPU utilisation -- maybe due to problems with the b53 driver used?). 
### Available enclosures and thermal issues
When Wi-Fi and a SATA disk is used the temperature of the [AXP209][30118] PMU will increase even more compared to other Banana Pi variants. The BCM53125 switch IC that is also on the bottom side of the PCB gets hot as well. Since a SATA disk on the top side of the PCB will be directly above the BCM53125 operating the board horizontally is no good idea. Especially when an enclosure is used that doesn't provide any airflow around AXP209/BCM53125. An example for an enclosure with good thermal design (vertical orientation and use of convection -- unfortunately only available in Taiwan) can be found in the gallery below. 
### Security Implications
On the Lamobo R1 the BCM53125 (a simple switch IC that features two RGMII GbE host ports and 5 GbE PHYs and can be configured through MDIO to separate traffic through VLANs) interconnects by default all 5 Ethernet ports and the A20 SoC. This means we can not speak about a true WAN port and LAN ports since all the ports are connected at network layer 2 by default. Since the A20 SoC features only one single RGMII interface no other mode of operation is possible ([illustration available][30169]). 
This might raise serious security risks since while the device boots or when it is in bricked state or booted without SD card or when VLAN configuration hasn't been setup correctly or a simple bug exists in the b53 driver then the BCM53125 always acts as a primitive layer 2 switch forwarding Ethernet frames between **all** external Ethernet ports (not differentiating between the so called _WAN port_ and the 4 _LAN ports_). **Since this device in _fail state_ always bridges the networks it should separate instead of building a barrier it simply can not be considered a router between the so called WAN port and the other Ethernet ports. It's just a switch!**
If one tries to use the R1 as a (NAT) router without a separate firewall between WAN and the R1 then it depends largely on the ISP's infrastructure whether this is not that good or an absolute no-go from a security point of view since all sorts of attacks against devices behind the so called _LAN ports_ can be triggered from behind the _WAN port_. In case you're not sure what that means you should simply treat the _WAN port_ as another _LAN port_ and use a separate USB to Ethernet adapter to be connected to WAN. Only in this mode the R1 might reliably work as a router. 
## Configuring the BCM53125 Switch in Mainline Linux
Kernel sources include documentation for configuring the BCM53125 (B53) and DSA in general: 
  * [DSA configuration][30170]
  * [B53 configuration][30171]

As of kernel version v5.6, the b53 driver supports Broadcom tags for DSA operation. For kernel versions v5.6 and later, see the [Configuration with Tagging Support][30172] section. For earlier kernels, see the [Configuration without Tagging Support][30173] section. 
Using a kernel that supports tagging makes the configuration much easier. 
See [this thread from Armbian build tools][30174] for older discussions on the topic. 
## GPIO header
The Lamobo R1 uses the very same 26 pin GPIO connector with identical pin mappings like the original Banana Pi. In case you plan to use Add-on boards be aware that due to the orientation of the connector Add-ons will project over the board in the opposite direction than intended. See the gallery below for an example. 
## Locating the UART
[![][30175]][30176]
[][30177]
Lamobo R1 UART pins
There is a 2.54mm pitch connector right next to battery connector. Connect your [UART][30178] adapter as shown in the picture. 
# Pictures
  * [![BPi-R1-top.jpg][30179]][30180]
  * [![BPi-R1-bottom.jpg][30181]][30182]
  * [![BPi-R1-connectors.jpg][30183]][30184]
  * [![Lamobo Vertical Acrylic Case.jpg][30185]][30186]
  * [![Addon Board on Lamobo R1 Fixed Orientation.JPG][30187]][30188]
  * [![Lamobo R1 powered through LiPo Connector cables corrected.jpg][30189]][30162]
  * [![Lamobo R1 SATA Power Fix.jpg][30190]][30167]

# Also known as
  * Banana Pi R1
  * BPi-R1
  * Banana Pi Router

# Variants
  * the upcoming ['Banana Pi Routerboard R2' or BPi-R2][30191] is **absolutely incompatible** to R1 since it relies on a Mediatek MT7623N SoC (no internal switch but HDMI and Mali450 GPU) combined with a MT7530B Gigabit Ethernet switch. Don't expect software to be compatible since it is not, don't expect support outside of banana-pi.org forums so good luck anyway.

# See also
  * [Forum at bananapi.com][30192]
  * [Bananian -- Debian Wheezy based OS image that also fully supports Lamobo R1][30193]
  * [Armbian -- Debian Wheezy/Jessie and Ubuntu Trusty based OS images for a variety of sunxi boards with full support for BPi-R1][30194]
  * Schematics released on 2016/02/16: [File:Banan pi BPI-R1 MP Schematic-SD V3-20140922.pdf][30195]

## Manufacturer images
  * [Android and openwrt images][30196]
  * ['Official' OpenWRT sources for R1][30197]
