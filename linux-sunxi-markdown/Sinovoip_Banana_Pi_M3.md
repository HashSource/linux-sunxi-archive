# Sinovoip Banana Pi M3
Banana Pi M3 is a [A83T][50459] based development board produced by Sinovoip. 
**Despite its name, the M3 is incompatible to previous Banana Pi boards ([Banana Pi][50460]/[M1][50461]/[M1+][50462]/[Pro][50463]/[M2][50464]/M2+), due to a different SoC - requiring different boot loaders and drivers.** It's another attempt to cash in on the Banana Pi's popularity with a SBC only sharing brand, name, ~~form factor~~ and GPIO header. 
  

[![MBOX icon information.png][50465]][50466] | Info to [Nora Lee][50467]: Please stop doing the marketing spam and join _#linux-sunxi_ on freenode ([IRC][50468]) to talk about why this edit was reversed the second time. If you keep changing info to untrue facts, your account will get blocked.   
---|---  
  

Sinovoip Banana Pi M3  
---  
[![BPi-M3-top-small.jpg][50469]][50470]  
Manufacturer |  [Sinovoip][50471]  
Dimensions |  92 _mm_ x 60 _mm_  
Release Date |  Nov 2015   
Website |  [M3 product page][50472]  
Specifications   
SoC |  [A83T][50459] @ 1.2-1.8Ghz   
DRAM |  2GiB LPDDR3 @ 672 MHz (SK hynix)   
NAND |  8GB eMMC 4.5 (Samsung KLM8G1GEAC-B001)   
Power |  DC 5V @ 2A DC-IN via µUSB or barrel jack, solder pads for LiPo battery   
Features   
Video |  HDMI (Type A - full), MIPI/DSI   
Audio |  3.5mm [TRRS/OMTP plug][50473] (stereo+mic), HDMI, on-board microphone   
Network |  BT4.0/WiFi 802.11 b/g/n ([Ampak AP6212][50474]), 10/100/1000Mbps Ethernet ([Realtek RTL8211E][50475])   
Storage |  µSD (max 64GB), eMMC, SATA 2.0 (via GL830 USB-to-SATA bridge, +5V power on JST XH 2.5mm connector)   
USB |  1 µUSB 2.0 OTG and an internal _Terminus Technology Inc. 4-Port HUB_ feeds 2x USB 2.0 Type-A ports and the SATA bridge   
Other |  IrDA   
Headers |  3 pin UART, LCD/ LVDS, CSI, 40 pin GPIO, WiFi external antenna connector (Hirose U.FL)   
## Contents
  * [1 Identification][50476]
  * [2 Sunxi support][50477]
    * [2.1 Current status][50478]
    * [2.2 Images][50479]
    * [2.3 Manual build][50480]
      * [2.3.1 U-Boot][50481]
        * [2.3.1.1 Sunxi/Legacy U-Boot][50482]
        * [2.3.1.2 Mainline U-Boot][50483]
      * [2.3.2 Linux Kernel][50484]
        * [2.3.2.1 Sunxi/Legacy Kernel][50485]
        * [2.3.2.2 Mainline kernel][50486]
  * [3 Tips, Tricks, Caveats][50487]
    * [3.1 LEDs][50488]
    * [3.2 SATA][50489]
    * [3.3 FEL mode][50490]
    * [3.4 Thermal behaviour][50491]
    * [3.5 USB 2.0 Hosts][50492]
    * [3.6 Powering the board / exchanged DC-IN connector][50493]
    * [3.7 Sudden shut offs / maximum consumption / cooling vs. consumption][50494]
    * [3.8 Booting from different device][50495]
    * [3.9 Display caveats][50496]
      * [3.9.1 HDMI to DVI converters][50497]
      * [3.9.2 LCD displays][50498]
    * [3.10 Wi-Fi][50499]
    * [3.11 ESD & over-current protections][50500]
  * [4 Adding a serial port][50501]
    * [4.1 Locating the UART][50502]
  * [5 Pictures][50503]
  * [6 See also][50504]

# Identification
It's an SBC with blue PCB silkscreened "BPI-M3" in white where you can easily recognise A83T/AXP813 on the PCB's top side. 
# Sunxi support
Supported. 
## Current status
All OS images the manufacturer provides are based on Allwinner's 3.4.39 kernel. [Mainlining efforts][50505] for the M3's A83T SoC just started so things won't improve that soon. 
## Images
  * [Official download page with M3 section containing various Linux images based on kernel 3.4.39][50506]
  * [Android 5.1.1 image provided by SinoVoip][50507]

All the OS images are based on u-boot 2011.09 and kernel 3.4.39 using an initrd and do not provide script.bin/uEnv.txt support. 
3 Months after releasing the first OS images the situation still hasn't improved. SinoVoip fixed some stuff in their Github repo but still doesn't provide a way to apply these updates to existing OS images. As the result of a quick try to let Armbian support the M3 (nope) here is an archive [BPI-M3-3.4.42_uEnv_Script_bin.zip][50508] (md5sum 360a32fe9d470296abebc4af0825acc9) containing boot-resource.fex, boot.img, env.fex, u-boot.fex and 3.4.42-BPI-M3-Kernel.tar. It can be used to _cure_ all available OS images for Banana Pi M3 (and for other A83T/H8 devices also I would suspect). It contains all BSP fixes for the M3 up to Feb 2016 and also a higher kernel version. To use it unpack the archive, choose an OS image $image as target and then do 
[code] 
    dd if=u-boot.fex of=$image bs=1k seek=19096
    dd if=boot-resource.fex of=$image bs=1k seek=36864
    dd if=env.fex of=$image bs=1k seek=69632
    dd if=boot.img of=$image bs=1k seek=86016
[/code]
Mount afterwards the 2nd partition of the image and unpack 3.4.42-BPI-M3-Kernel.tar below /lib/modules. You should then be able to create uEnv.txt and script.bin on the 1st partition (a [weird howto available in the official Banana Pi forum][50509]) 
## Manual build
No support in the community maintained sunxi-3.4 kernel is planned. Allwinner's kernel sources for the A83T can be found now [here][50510]. 
### U-Boot
#### Sunxi/Legacy U-Boot
The manufacturer uses an [u-boot.2011-something version][50511] without support for script.bin 
#### Mainline U-Boot
Use the **Sinovoip_BPI_M3_defconfig** (supported since v2016.03) build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Since the M3's bsp uses an aging u-boot from 2011 no script.bin support exists therefore you've to adjust display settings in the fex file. Some can be found in [SinoVoip's M3 repo][50512]. 
#### Mainline kernel
Use the _sun8i-a83t-bananapi-m3.dtb_ device-tree file for the [mainline kernel][50513]. 
# Tips, Tricks, Caveats
## LEDs
The BPi-M3 features 3 LEDs located between IR receiver and microphone: A _red_ one indicating power that can't be turned off and a _green_ and _blue_ one accessible through sysfs after latest fixes are applied to [kernel sources][50514] and [hardware initialisation][50515]. 
Both _green_ and _blue_ LED can then be controlled through sysfs and appear below _/sys/class/leds/_. To show the available triggers do a `cat /sys/class/leds/green_led/trigger` and set this to _none_ if the default _heartbeat_ blinking annoys you. Since the _timer_ trigger also exists [BananaLEDd][50516] should be useable to show disk activity and average load (to be confirmed) since BananaLEDd supports LEDs accessible through sysfs starting with version 1.2 
## SATA
Be aware that the A83T SoC used on the M3 isn't SATA capable and therefore the SATA port is provided by a cheap USB-to-SATA-bridge. This means you can neither expect [SATA performance][50517] nor full SATA functionality and the used chip is also [known to be buggy and reporting the disk size wrong][50518]. While the used GL830 bridge supports [S.M.A.R.T.][50519] attributes it does not support S.M.A.R.T. status notification (overall health indicator of the disk – instead of _PASSED_ or _FAILED_ you will only get _SMART Status not supported: Incomplete response, ATA output registers missing_). Fortunately the GL830 seems to have no 2TB limitation. 
Expected _SATA_ performance is even worse compared to [Orange Pi Plus][50520] that relies on the same old GL830 chip since on the M3 all externally available USB host ports and the SATA bridge are connected through the internal hub to one single USB port and therefore have to share bandwidth. First tests don't look that promising: tests done with a fast SSD/ext4 at two different clockspeeds: 13/23 MB/s @ 480 MHz vs 15/30 MB/s @1800 MHz write/read. Using an external Micron JMS567 that is known to [get close to 40 MB/s][50521] sequential transfer speeds @ 1800 MHz exceeded 35/34 MB/s write/read with same SSD/ext4. It seems the GL830 wasn't the best choice to provide a SATA port on the M3. 
## FEL mode
The u-boot button triggers [ FEL mode][50522]. 
## Thermal behaviour
Allwinner's kernel for H3 and A83T seem to implement identical thermal throttling strategies depending on [fex settings][50523] that can be read out through sysfs: _/sys/devices/virtual/thermal/thermal_zone0/trip_point*_. If these values are set in incremented order first throttling will occur and only if this still doesn't help CPU cores will dropped. By _tuning_ these settings you might get the opposite of what's intended: a slower system due to less available CPU cores. 
With Allwinner's kernel there's also something like fan control implemented. Below _/sys/devices/virtual/thermal/cooling_device0/_ you can read out _cur_state_ that will be adjusted depending on [fex settings][50524] between 0 and _max_state_. 
Without a heatsink you won't exceed 1.2GHz when running CPU intensive tasks, when choosing a good one and enough airflow you might get up to 1.6 GHz and everything above needs an annoying fan. The good news: This is still no overvolting/overclocking since it's just about better heat dissipation to avoid throttling. The bad news: You need to solder a sane way to provide more than 5V/2A to the board -- [see below][50494]. 
## USB 2.0 Hosts
In opposite to CubieBoard5, the M3s hardware design does not make use of all USB connections offered by the SoC (A83T).  
The HSIC port is connected to the Terminus Technology Inc. 4-Port USB hub. On this hub is attached the USB-to-SATA bridge and the 2x available USB Type-A ports. Therefore these 3 connectors have to share the bandwidth of a single USB2.0 connection.  
1x OTG MicroUSB  
It seems that the hub's fourth port is routed to solder pads located between onboard microphone and GPIO header. 
## Powering the board / exchanged DC-IN connector
The pre-production samples of this board had the usual 4.0/1.7mm barrel jack for DC-IN BPi M2/M2+ also use. This has been replaced by a Micro USB jack on the first production batch in Dec 2015 leading to the usual sorts of problems banana-pi.org forums are full of (see also next paragraph for some reasons). Starting in May 2016 Micro USB has been replaced by the 4.0/1.7mm barrel jack again so powering is possible more reliable now. The Micro USB receptacle on the longer board side is USB OTG, also connected to the board's PMIC and while looking like an alternative way to power the board that's not recommended unless you love underpowering situations, reboot loops and the like. 
In case you're unlucky enough to own an M3 from the first production batch have a look at the gallery below where to measure / fix undervoltage/undercurrent problems you'll run into sooner or later. 
## Sudden shut offs / maximum consumption / cooling vs. consumption
In case you experience shut offs when connecting peripherals or operating the device under high load have a look at the gallery below where to measure and where to solder a fix. This is especially recommended when you want to make use of the promised performance (octacore @ 2.0GHz according to the manufacturer). If you use the device without heatsink consumption through CPU cores will seldom being able to exceed 4W-5W since thermal throttling will decrease clockspeeds automagically and dynamic voltage frequency scaling (dvfs) will then also reduce Vcore. 
With an applied small heatsink and outside of an enclosure under constant full load the A83T will jump between 1008 MHz and 1200 MHz due to thermal throttling. At the latter cpufreq Vcore will be already set to 920mV while being set to 840mV at 1008 MHz: 
[![BPi-M3 full load small heatsink.png][50525]][50526]
Under these conditions CPU activity is responsible for the board consuming between 5.5W-6W. If you improve heat dissipation by using a large heatsink or even a fan you will let thermal throttling jump in later with drastical consequences. 
Due to the [dvfs settings Vcore will be increased to 1000mV or even 1080mV when reaching 1800 MHz][50527]. And then CPU activity alone is responsible for a whopping 8W consumption. And while this might work in a test environment with just a serial console attached it can't work in a normal environment with a connected display, a few USB peripherals and a connected disk needing another 4-5W exceeding 12W easily. Micro USB is rated 5V/1.8A max: 9W or maybe 10W under best conditions (most likely due to crappy USB cables the board's PMU will diagnose undervoltage way earlier and shuts down). 
In case you improve heat dissipation be prepared for shut-offs unless you solder a sane DC-IN solution and use 5V/3A at least (won't help with micro USB due to the tiny contacts) 
## Booting from different device
Using the BSP and the OS images SinoVoip provides it's only possible to boot from _/dev/mmcblk0p2_ (compare with /proc/cmdline). To change that you've to grab the BSP and adjust _sunxi-pack/chips/sun8iw6p1/configs/*/env.cfg_ to be able to boot using NFS or USB (please remember: the M3 has no SATA any more, just an ultra-slow onboard USB-to-SATA bridge). If you try to adjust _root=_ to point to any USB location always keep in mind that device nodes might not be persistent across reboots therefore always use the partition UUID instead. In case you want to boot from a partition that's currently mounted as /dev/sda1 do a _gdisk -l /dev/sda1_ and use the UUID it prints, eg.: _root=PARTUUID=1A40C346-C1F0-4613-B3AB-1FA3C6B6F343_. Don't use the output of _blkid_ , these aren't the partition UUIDs! 
Please always keep in mind that booting from a connected _SATA disk_ behind the GL830 is the worst idea ever since every BPi M3 ships with 8GB onboard eMMC which is more than twice as fast as any disk behind the slow GL830 bridge. 
## Display caveats
### HDMI to DVI converters
When trying to use HDMI to DVI converters with Allwinner's 3.4.39 kernel a small fix has to be applied. The contents of sysconfig.fex have to be adjusted (and the whole [BSP][50528] has to be rebuilt since there's no support for script.bin) so that the following has been added to the _[hdmi_para]_ section: 
[code] 
    hdcp_enable = 0
    hdmi_cts_compatibility = 1
[/code]
### LCD displays
Since the A83T/R58/H8 has only support for MIPI/DSI to drive LCD displays none of the available LVDS/RGB LCDs sold for older incompatible Banana Pi variants can be used. SinoVoip sold a 7" TS LCD panel since summer 2015 with just 800x480 pixels that's also incompatible to the Banana Pi M3 since it's also using LVDS/RGB as interface. In the meantime SinoVoip provides a new variant of this 7" LCD with a controller board featuring both MIPI/DSI for the M3 and LVDS/RGB for M1/M1+/M2. Of course they re-used the same article in their aliexpress shop so be prepared that reviews/ratings found there are for the older variant and not the current one. 
## Wi-Fi
In case WiFi isn't working (reliably) with an external antenna that's an intentional _feature_ of this board. Don't try to fix it in software unless you desoldered a small resistor on the PCB (that's not a bad joke but an [official suggestion][50529] obviously not taking into account that different PCB revisions exist) 
## ESD & over-current protections
Based on the schematic Rev 1.1 (October 16, 2015) the board incorporates the following protections: 
  

Protections x - no protection, ESD - Electrostatic Discharge, OC - Over-current  | Comments   
---|---  
1 | DCIN & Micro USB (power) | x | x | A ferrite bead with a power supply bypass capacitor   
2 | Micro SD | ESD | OC | Over-Current protection provided by U5?   
3 | eMMC | x | x |   
4 | Camera | x | x |   
5 | USB1 | ESD | OC | Over-Current protection provided by U6?   
6 | Dual USB2 | ESD | OC | USB Hub current limited by U7?   
7 | Additional 2-pin USB | ESD | N/A | This is just a 2-pin connector on PCB   
8 | SATA (link) | x | x |   
9 | SATA (power) | x | x | Power is routed directly from power DCIN/Micro USB connector   
10 | HDMI | ESD | x |   
11 | MIPI-DSI | x | x |   
12 | Ethernet | x | N/A | Over-current protection is not applicable   
13 | GPIO | x | x |   
14 | Debug UART | x | ?   
15 | Audio jack | ESD | N/A | Output current is internally limited by SoC   
# Adding a serial port
## Locating the UART
[![][50530]][50531]
[][50532]
UART pins
The UART header is between u-boot button and the Ethernet port. Just attach some leads according to our [UART howto][50533]. 
# Pictures
  * [![BPi-M3-front.jpg][50534]][50535]
  * [![BPi-M3-back.jpg][50536]][50537]
  * [![BPi-M3-left.jpg][50538]][50539]
  * [![BPi-M3-right.jpg][50540]][50541]
  * [![BPi-M3-top.jpg][50542]][50543]
  * [![BPi-M3-bottom.jpg][50544]][50545]
  * [![BPi-M3 Fix crappy DC-IN.jpg][50546]][50547]
  * [![BPi-M3 fixed DC-IN.jpg][50548]][50549]

# See also
  * [a so called 'User Manual' and some hardware docs][50550]
  * [BPI-M3 V1_2 schematic diagram 20151014(RELEASE)][50551]
