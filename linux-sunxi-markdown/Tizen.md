# Tizen
Tizen is an open source Linux-based software platform for multiple device categories such as smartphones, tablets, personal computers, in-vehicle infotainment devices and smart TVs. Tizen is registered trademark of the Linux Foundation and it is governed by a Technical Steering Group composed by Samsung, Intel and other industry-leading companies. 
## Contents
  * [1 Tizen-sunxi][55140]
    * [1.1 Downloads][55141]
    * [1.2 TIZEN:COMMMON][55142]
    * [1.3 News / Resources][55143]
    * [1.4 Allwinner Processors][55144]
    * [1.5 Devices][55145]

## Tizen-sunxi
Tizen-sunxi is an open-source project for porting Tizen to devices with Allwinner A-Series processors. Sunxi represents the family of ARM SoC (System on Chip) designed for embedded systems, and made by Allwinner Tech. in Zhuhai (Guangdong, China). 
Since it's not (yet) supported by Tizen project let's use this page as entry point 
  

### Downloads
Tizen-sunxi images and instructions are available at [GitHub][55146] and Google Drive. 
  

### TIZEN:COMMMON
This profile is a good candidate to dig into tizen since it can be easly adapted to any hardware... 
You can rebuild stable kernel for source and then rebase or patch over it : 
  * <https://github.com/rzr/linux/tree/sandbox/pcoval/devel-sunxi>

Then use [armv7l][55147] images from project and install [Kernel][55148] on boot part and bootloaders 
See this How To for more : 
  * <https://dockr.eurogiciel.fr/blogs/embedded/tizen-arm-images-to-renesas/>

Or use preinstalled image for A20-OLinuxIno-Micro : 
  * <https://dockr.eurogiciel.fr/blogs/embedded/tizen-for-arm-qemu-device/>

  

### News / Resources
  * 2014-05-22 : Tizen:Common armv7l port announced <https://lists.tizen.org/pipermail/dev/2014-May/002921.html>
  * <https://wiki.tizen.org/wiki/ARM>

  

### Allwinner Processors
The port targets the following SoC: 
  * [A10][55149] (sun4i) Cortex-A8
  * [A13][55150] (sun5i) Cortex-A8
  * [A10s][55151] (sun5i) Cortex-A8
  * [A31][55152] (sun6i) quad Cortex-A7
  * [A31s][55153] (sun6i) quad Cortex-A7
  * [A20][55154] ([sun7i][55155]) dual Cortex-A7

### Devices
Tizen-sunxi has been tested with the following devices: 
  * [A20-OLinuXino-MICRO (Olimex)][55156]
  * [A10-OLinuXino-LIME (Olimex)][55157]
  * [A10s-OLinuXino-MICRO (Olimex)][55158]

Tizen-sunxi should also work on the following devices: 
  * [A13-OLinuXino (Olimex)][55159]
  * [A13-OLinuXino-MICRO (Olimex)][55160]
  * [A20-OLinuXino-LIME (Olimex)][55161]
  * Banana Pi
  * Auxtek T003 hdmi tv stick
  * Auxtek T004 hdmi tv stick
  * BA10 TV Box
  * [Cubieboard development board 1024 MB RAM][55162]
  * [Cubieboard2 (A20) development board][55163]
  * [Cubietruck development board][55164]
  * Gooseberry development board
  * [Mele A1000G][55165]/[A2000G][55166] 1024 MB RAM
  * Mini-X 1024 MB RAM
  * mk802 (with female mini hdmi) 512 MB RAM
  * mk802 with A10s (s with a circle around it on the barcode label)
  * mk802ii (with male normal hdmi) 1024 MB RAM
  * r7 hdmi tv stick
  * UHost U1A hdmi tv stick
  * Wobo i5 TV Box
  * A10 tablet sold under various names (whitelabel)
  * A13 tablet sold under various names (whitelabel)
  * [Coby MID7042 tablet][55167]
  * Coby MID8042 tablet
  * Coby MID9742 tablet
  * [Cubieboard development board 512 MB RAM][55162]
  * DNS AirTab M82 tablet
  * EOMA68 A10 CPU card
  * H6 netbook
  * [Hackberry development board][55168]
  * [Hyundai a7hd tablet][55169]
  * iNet-97F Rev.2 (and clones) tablet
  * [Marsboard A10][55170]
  * [Megafeis A08][55171]
  * [Mele A1000][55172]/[A2000][55173] 512 MB RAM
  * [Mele A3700][55174]
  * [Mini-X 512 MB RAM][55175]
  * [Mini-X with A10s soc][55175]
  * [mk802 (with female mini hdmi) 1024 MB RAM][55176]
  * [pcDuino development board][55177]
  * Point of View ProTab 2 IPS 9" tablet
  * Point of View ProTab 2 IPS tablet with 3g
  * [Sanei N90][55178]
  * XZPAD700 7" tablet
