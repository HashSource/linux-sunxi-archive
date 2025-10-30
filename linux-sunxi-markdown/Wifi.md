# Wifi
## Contents
  * [1 Driver specific information][59182]
    * [1.1 Allwinner][59183]
      * [1.1.1 XR819][59184]
      * [1.1.2 AW859A][59185]
    * [1.2 Ampak][59186]
      * [1.2.1 Ampak Devices][59187]
    * [1.3 Broadcom][59188]
      * [1.3.1 Broadcom Devices][59189]
    * [1.4 Espressif][59190]
      * [1.4.1 Espressif Devices][59191]
      * [1.4.2 ESP8089][59192]
    * [1.5 iNet][59193]
      * [1.5.1 iNet Devices][59194]
    * [1.6 RDA][59195]
    * [1.7 Realtek][59196]
      * [1.7.1 USB-based][59197]
      * [1.7.2 SDIO-based][59198]
        * [1.7.2.1 RTL8189ES / RTL8189ETV][59199]
        * [1.7.2.2 RTL8189FTV][59200]
      * [1.7.3 Legacy sunxi-3.4 kernel support][59201]
        * [1.7.3.1 Driver refusing to load (rt5370sta/8188eu/8189es/8192cu)][59202]
        * [1.7.3.2 8188eu driver on sunxi-3.4][59203]
  * [2 Software Configuration][59204]
    * [2.1 Debian/ubuntu with NetworkManager][59205]
    * [2.2 Debian/ubuntu without NetworkManager][59206]
      * [2.2.1 Setup with wpa_supplicant and without network manager][59207]
        * [2.2.1.1 Disabling networkmanager. Fully.][59208]
        * [2.2.1.2 Simple and dumb WPA setup][59209]
  * [3 Devices][59210]

# Driver specific information
## Allwinner
Device | Type | sdio id | sunxi-3.4 kernel | mainline kernel | 4.9.170-sun50iw9 kernel   
---|---|---|---|---|---  
XR819 | SDIO | [0020:2281][59211] | xradio_wlan |  |   
AW859A | SDIO | [8800:1][59211] |  |  | sunxi-wlan   
### XR819
For [XR819][59212] driver source was included in Allwinner H2 BSP. 
Firmware firmware blobs can be found from [Armbian firmware repository][59213]. 
Also some documentation is available now: 
  * [File:XR819 Datasheet V1.0-EN.pdf][59214]
  * [File:XR819 Datasheet V1.5-EN.pdf][59215]
  * [File:XR819 Application Guide V1.0-CH.pdf][59216]

May be related to ST cw1XX0 [[1]][59217]. 
Initial comparison between cw1200 (`drivers/net/wireless/st/cw1200`) and xradio driver shows that the source code for two drivers are really similar and the st1200 driver could be improved to support both devices. 
A working out-of-tree driver for mainline kernels is at [[2]][59218]. 
### AW859A
AW859A is a packaged Unisoc UWE5622 (sc2355) chip. 
For AW859A driver source was include in Allwinner H616 Orange Pi Zero2 BSP, you can get it from [orangepi-build repository][59219]. 
Firmware firmware blobs can be found from [orangepi firmware respository][59220]. 
This module [does not reliabily work with 802.11r / Band Steering enabled APs][59221]
## Ampak
Ampak combines broadcom wifi and [bluetooth][59222] chips in single modules. 
### Ampak Devices
Device | Type | usb/sdio id | module | sunxi-3.4 kernel | mainline kernel   
---|---|---|---|---|---  
AP6181 | SDIO/UART | 02d0:a962 | See right | bcmdhd | brcmfmac   
AP6210 | SDIO/UART | 02d0:a962 | See right | bcmdhd | brcmfmac   
AP6212 | SDIO/UART | 02d0:a9a6 | See right |  | brcmfmac   
AP6330 | SDIO/UART | 02d0:4330 | See right |  | brcmfmac   
AP6335 | SDIO/UART | 02d0:4335 | See right |  | brcmfmac   
## Broadcom
### Broadcom Devices
Device | Type | usb/sdio id | module | sunxi-3.4 kernel | mainline kernel   
---|---|---|---|---|---  
BCM4334 |  | 0x4334 | brcmfmac |  | brcmfmac since 3.6+   
|  |  |  |  |   
## Espressif
[Espressif][59223] is a fairly young Chinese company. 
### Espressif Devices
Device | Type | sdio id | module | sunxi-3.4 kernel | mainline kernel   
---|---|---|---|---|---  
ESP8089 | SDIO | 6666:1111 |  |  | out-of-tree driver exists   
### ESP8089
Firstly, you should use Hans de Goede's [sunxi-wip kernel branch][59224] containing various bits and pieces needed to make things work. 
Driver itself is currently in its own repository: 
[code] 
    git clone https://github.com/jwrdegoede/esp8089.git
    cd esp8089
    git checkout -B cleanup origin/cleanup
    cd ../linux
    make -j4 ARCH=arm CROSS_COMPILE=arm-linux-gnu- modules M=../esp8089 CONFIG_ESP8089=m
    
[/code]
Do not forget to copy `firmware/*.bin` to `/lib/firmware/` on the target system. 
## iNet
### iNet Devices
Device | Type | usb id | module | sunxi-3.4 kernel | mainline kernel   
---|---|---|---|---|---  
iNet i10 |  |  |  |  |   
## RDA
[RDA Microelectronics][59225] is a relatively unknown and new chinese chipmaker. 
Device | Type | usb id / sdio id | module | sunxi-3.4 kernel | mainline kernel   
---|---|---|---|---|---  
RDA5990P |  |  |  |  |   
RDA5991 | SDIO | 5449:0145 |  |  |   
The [RDA5990P][59226] is a single chip solution which includes Wifi, Bluetooth and an FM radio. Some code for this wifi chip is available in [a Rockchip RK3188 kernel tree][59227], but nobody has tested or ported this code yet. 
Datasheets: [RDA5990P][59228] [RDA5990][59229]
## Realtek
### USB-based
[![MBOX icon important.png][59230]][59231] | Best up-to-date information about Realtek driver in mainline Linux is available from [Linux Wireless Project's Realtek drivers page][59232].   
---|---  
Device | Type | USB id | mainline kernel | legacy (sunxi-3.4)   
---|---|---|---|---  
RTL8188CTV | USB | 0bda:8176 | `**rtl8xxxu**` | `8192cu`  
RTL8188CUS | USB | 0bda:8176 | `**rtl8xxxu**` | `8192cu`  
RTL8188ETV | USB | 0bda:0179 | `**rtl8xxxu**` | `8188eu` (see below)   
RTL8188EUS | USB | 0bda:8179 | `**rtl8xxxu**` | `8188eu` (see below)   
RTL8192CU | USB | 0bda:018a | `**rtl8xxxu**` (or `rtlwifi`) | `8192cu`  
RTL8723AU | USB | 0bda:0724 | `**rtl8xxxu**` | `8723au`  
### SDIO-based
[![MBOX icon important.png][59230]][59231] | Best up-to-date information about Realtek driver in mainline Linux is available from [Linux Wireless Project's Realtek drivers page][59232].   
---|---  
Device | Type | SDIO id | mainline kernel | legacy (sunxi-3.4)   
---|---|---|---|---  
RTL8189ES | SDIO | ?? | out-of-tree driver (see below) | ??   
RTL8189FTV | SDIO | `024c:f179` | out-of-tree driver (see below) | ??   
RTL8723BS  
RTL8703AS | SDIO |  ` 024c:0523  
024c:0623  
024c:0626  
024c:b723` | `rtl8723bs` (staging) | `8723bs`  
RTL8821CS | SDIO | 024c:c821 | rtw88 (since v6.4) | ??   
RTL8822BS | SDIO | 024c:b822 | rtw88 (since v6.4) [vendor driver][59233] | ??   
RTL8822CS | SDIO | 024c:c822 | rtw88 (since v6.4) [vendor driver][59234] | ??   
  

#### RTL8189ES / RTL8189ETV
Driver has its own repository: 
[code] 
    git clone https://github.com/jwrdegoede/rtl8189ES_linux.git
    cd rtl8189ES_linux
    make -j4 ARCH=arm CROSS_COMPILE=arm-linux-gnu- KSRC=../linux
    
[/code]
  

#### RTL8189FTV
Driver has its own repository: 
[code] 
    git clone https://github.com/jwrdegoede/rtl8189ES_linux.git
    cd rtl8189ES_linux
    git checkout -B rtl8189fs origin/rtl8189fs
    make -j4 ARCH=arm CROSS_COMPILE=arm-linux-gnu- KSRC=../linux
    
[/code]
### Legacy sunxi-3.4 kernel support
#### Driver refusing to load (rt5370sta/8188eu/8189es/8192cu)
Please note that sunxi-3.4 kernel is not supported and has been deprecated... 
When using the **rt5370sta** , **8188eu** , **8189es** or **8192cu** drivers, which are all for USB based realtek devices, it might occur that the driver refuses to load: 
[code] 
    ERR: script_parser_fetch usb_wifi_usbc_num failed
    modprobe: can't load module 8188eu (kernel/drivers/net/wireless/rtl8188eu/8188eu.ko): Cannot allocate memory 
    
[/code]
This is because the usb_wifi_para section is missing from your script.bin: 
[code] 
    [usb_wifi_para]
    usb_wifi_used = 1
    usb_wifi_usbc_num = 2
    
[/code]
Where usb_wifi_usbc_num is the usbc to which your realtek usb wireless chip is attached. 
Edit the .fex file and create the script .bin as explained in our [ Manual build howto][59235], and [ send a patch to sunxi-boards in to our mailinglist.][59236]
#### 8188eu driver on sunxi-3.4
Please note that sunxi-3.4 kernel is not supported and has been deprecated... 
The sunxi-3.4 branch currently has [v4.1.2_4787.20120803][59237] available. There are newer versions available at <https://github.com/lwfinger/rtl8188eu/> which are [v4.1.4_6773.20130222][59238] and [v4.1.8_9499.20131104][59239]. There's also a v4.1.8 file available at <https://github.com/LazyZhu/myblog/raw/gh-pages/file/RTL8188EUS_RTL8189ES_linux_v4.1.8_9499.20131104.zip> which is likely the original from Realtek. 
Here's how to compile the latest version from Realtek: 
Extract the driver/rtl8188EUS_rtl8189ES_linux_v4.1.8_9499.20131104.tar.gz from the RTL8188EUS_RTL8189ES_linux_v4.1.8_9499.20131104.zip file and extract it. These instructions assume your `linux-sunxi` directory is in the same directory as your `rtl8188EUS_rtl8189ES_linux_v4.1.8_9499.20131104` directory. It's also assumed that you've configured the kernel to include the 8188eu driver that's part of linux-sunxi. 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -C ../linux-sunxi/ M=`pwd` modules
    
[/code]
copy the `8188eu.ko` file over to the device and then install it into your kernel with the following commands (on the device as root): 
[code] 
    modprobe -r 8188eu
    rm -rf /lib/modules/`uname -r`/kernel/drivers/net/wireless/rtl8188eu
    install -p -m 644 8188eu.ko /lib/modules/`uname -r`/kernel/drivers/net/wireless/
    /sbin/depmod
    modprobe 8188eu
    
[/code]
There are two changes you may want to make in `include/autoconf.h`: 
1\. The default is to output a LOT of logging and you can disable that by commenting out the following line: 
[code] 
    #define CONFIG_DEBUG /* DBG_871X, etc... */
    
[/code]
2\. The default is to disable the activity LED on the wifi device which you may want to see to know that it's working. You can change that by un-commenting the following line: 
[code] 
    //#define CONFIG_LED
    
[/code]
# Software Configuration
## Debian/ubuntu with NetworkManager
NetworkManager uses its own wpa_supplicant configuration. That is the reason why manually editing /etc/network/interfaces to use wpa_supplicant does not work together with NetworkManager. 
You have to disable all interfaces in /etc/network/interfaces e.g. by commenting out each line by inserting "#" as a first character. 
You even have to **disable Ethernet section** to use wifi in network manager. Here is an example 
[code] 
       # interfaces(5) file used by ifup(8) and ifdown(8)
       auto lo
       iface lo inet loopback
       
       #allow-hotplug eth0
       #iface eth0 inet dhcp
       
       #auto eth0
       #iface eth0 inet static
       #address 192.168.101.50
       #netmask 255.255.255.0
       #gateway 192.168.101.1
       #broadcast 192.168.101.255
       
       #auto wlan0
       #iface wlan0 inet dhcp
       #    wpa-ssid YOUR-NETWORK-NAME
       #    wpa-key-mgmt WPA-PSK
       #    wpa-group TKIP CCMP
       #    wpa-psk YOUR-NETWORK-KEY
    
[/code]
  
At your desktop there should emerge a network icon from NetworkManager in the task bar. You can edit the network setting with the gui dialogs. 
## Debian/ubuntu without NetworkManager
### Setup with wpa_supplicant and without network manager
There are many tutorials out there on how to do this. Here is [a good one][59240]. 
#### Disabling networkmanager. Fully.
Even with the common trick of putting the following in /etc/NetworkManager/NetworkManager.conf 
[code] 
    [ifupdown]
    managed=true
    
[/code]
the despotic NetworkManager still will be messing up your careful setup from /etc/network/interfaces, and you might, once again, be left without wifi upon the next reboot. 
To stop NetworkManager from running altogether, you can run the following (as root): 
[code] 
    echo "manual" > /etc/init/network-manager.override
    
[/code]
Now, at least on ubuntu, your wifi driver, wpa_supplicant and ifupdown will not be smacked about anymore. 
#### Simple and dumb WPA setup
Install the following packages, if they are not installed already: 
[code] 
    apt-get install wireless-tools wpasupplicant
    
[/code]
Edit /etc/network/interfaces and add the following: 
[code] 
    auto wlan0
    iface wlan0 inet dhcp
        wpa-ssid YourSSID
        wpa-psk YourWPASharedKey
    
[/code]
This is the most basic, but static, setup possible for wifi. If you need anything more, you need to read up on wpa_supplicant, or run through one of the tutorials referenced above. 
# Devices
The following devices all come with an built-in wifi chip. 
[10moons LT390W][59241]
[A-Star KV49L][59242]
[A33 Q7 V1.0][59243]
[A70x][59244]
[A70x1][59245]
[Ainol AW1][59246]
[Allwinner A83TDevBoard][59247]
[Allwinner Nezha][59248]
[Along A13Q8][59249]
[Along rt713][59250]
[Ampe A76][59251]
[Anichips PhoenixA20][59252]
[Aoson M751s][59253]
[Auxtek T004][59254]
[Azpen A741][59255]
[Beelink GS1][59256]
[Beelink X2][59257]
[Biqu BTT Pi][59258]
[Biqu CB1][59259]
[CherryPi PC H6][59260]
[Coby MID7042][59261]
[Colorfly e708q1][59262]
[CS918S][59263]
[CUBE U11GT][59264]
[Cubietech Cubieboard4][59265]
[Cubietech Cubietruck][59266]
[Cubietech Cubietruck Plus][59267]
[Digix TAB-730][59268]
[Digma iDj7n][59269]
[Ditter v21][59270]
[DragonTouch Y88X][59271]
[Eearl H1026A][59272]
[Eken A70h][59273]
[ENET E714F][59274]
[ET Q8 V2.0][59275]
[ET-Q8 A33][59276]
[Finepower N1][59277]
[Forfun Q88DB][59278]
[FriendlyARM NanoPi A64][59279]
[FriendlyARM NanoPi Duo2][59280]
[FriendlyARM NanoPi K1 Plus][59281]
[FriendlyARM NanoPi NEO & AIR][59282]
[FriendlyARM NanoPi NEO Plus 2][59283]
[FriendlyElec NanoPi R1][59284]
[FSL S8][59285]
[Gemei G9][59286]
[Genesis GT-7220s][59287]
[GLD KF026][59288]
[Goclever Tab A971][59289]
[INET-3FTD][59290]
[IRULU X11][59291]
[IRULU X47][59292]
[Kickpi K2B H618][59293]
[KOHOTECH KP100 MB V3.0][59294]
[Lamobo R1][59295]
[LeMaker Banana Pro][59296]
[LinkSprite pcDuino Lite WiFi][59297]
[LinkSprite pcDuino2][59298]
[LinkSprite pcDuino3][59299]
[MangoPi MQ1][59300]
[MarsBoard A20-SOM][59301]
[Mele M3][59302]
[Milagrow MGPT09][59303]
[MSI Primo73L][59304]
[MXQ-4K][59305]
[Navon iQ7 2018][59306]
[Naxa NID-7015][59307]
[NextThingCo CHIP][59308]
[Nezha D1s][59309]
[Olimex A13-OLinuXino][59310]
[Olimex A13-SOM][59311]
[Olimex A64-OLinuXino][59312]
[Olimex Teres-A64][59313]
[Onda V972][59314]
[Pcduino8 A80 Board][59315]
[Pentagram P5355][59316]
[Pine Pinebook][59317]
[PineTab][59318]
[User:Putti/Unknown Device][59319]
[Q8H-HD][59320]
[Radxa Cubie A5E][59321]
[Radxa Cubie A7A][59322]
[Rubix A10][59323]
[Sinovoip Banana Pi BPI-6204][59324]
[Sinovoip Banana Pi M2][59325]
[Sinovoip Banana Pi M2 Berry][59326]
[Sinovoip Banana Pi M2 Ultra][59327]
[Sinovoip Banana Pi M2 Zero][59328]
[Sinovoip Banana Pi M2+][59329]
[Sinovoip Banana Pi M3][59330]
[Sinovoip Banana Pi M4 Berry][59331]
[Sinovoip Banana Pi M64][59332]
[Sunchip CX-A99][59333]
[Sunvell R69][59334]
[User:Svenska/QT-7][59335]
[T95][59336]
[T95H][59337]
[Tanix TX1][59338]
[Tanix TX6][59339]
[Tanix TX6s][59340]
[TBS A711][59341]
[Thomson TEO10][59342]
[TQC A01][59343]
[Tronsmart Draco H3][59344]
[Unisurf USFT60U7BLK][59345]
[X-View Proton Tab 2][59346]
[X96 Mate][59347]
[X96QPro][59348]
[Xassette Asterisk][59349]
[Xunlong Orange Pi][59350]
[Xunlong Orange Pi 2][59351]
[Xunlong Orange Pi 4A][59352]
[Xunlong Orange Pi Mini][59353]
[Xunlong Orange Pi One & Lite][59354]
[Xunlong Orange Pi Plus][59355]
[Xunlong Orange Pi Plus 2][59356]
[Xunlong Orange Pi Plus 2E][59357]
[Xunlong Orange Pi Prime][59358]
[Xunlong Orange Pi Win][59359]
[Xunlong Orange Pi Zero][59360]
[Xunlong Orange Pi Zero Plus][59361]
[Xunlong Orange Pi Zero Plus 2][59362]
[Xunlong Orange Pi Zero2][59363]
[Xunlong Orange Pi Zero2W][59364]
[Xunlong Orange Pi Zero3][59365]
[Yarvik tab462][59366]
[Yuntab PHT V101H A33 V1.0][59367]
[YuzukiHD Avaota A1][59368]
[YuzukiNezha D1s][59369]
