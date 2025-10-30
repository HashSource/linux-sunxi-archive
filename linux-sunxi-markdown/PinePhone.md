# PinePhone
PinePhone  
---  
[![Pinephone-front.jpg][44642]][44643]  
Manufacturer |  [Pine64][44644]  
Dimensions |  160.5 _mm_ x 76.6 _mm_ x 9.2 _mm_  
Release Date |  2019   
Website |  [Device Product Page][44645]  
Specifications   
SoC |  [A64][44646] @ 1.152 GHz   
DRAM |  2GiB LPDDR3 @ ????MHz or 3GiB LPDDR3 @ ????MHz   
NAND |  16GB or 32GB   
Power |  USB Type C (5V - 3A), 2750-3000mAh 3.7V Li-Ion battery   
Features   
LCD |  1440x720 (5.95" 18:9)   
Touchscreen |  5-finger capacitive ([Goodix device][44647])   
Video |  DisplayPort over USB-C   
Audio |  3.5mm headphone plug, HDMI, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8723CS][44648])   
Storage |  µSD   
USB |  1x USB2.0 OTG   
Camera |  2.0MP (????x????) front (GC2145), 5.0MP (????x????) rear (OV5640)   
Other |  Accelerometer ([Manufacturer device][44649]), GPS, Gyroscope, Proximity, Ambient Light, Magnetometer   
Headers |  UART   
This page needs to be properly filled according to the [New Device Howto][44650] and the [New Device Page guide][44651].
the pinephone is a cheap, generic, arm64 smartphone produced with the goal of supporting user-modifiable operating systems and hardware 
## Contents
  * [1 Identification][44652]
  * [2 Sunxi support][44653]
    * [2.1 Current status][44654]
    * [2.2 Images][44655]
    * [2.3 Manual build][44656]
      * [2.3.1 Mainline U-Boot][44657]
      * [2.3.2 Mainline Linux Kernel][44658]
  * [3 Tips, Tricks, Caveats][44659]
    * [3.1 FEL mode][44660]
  * [4 Adding a serial port][44661]
    * [4.1 Device disassembly][44662]
  * [5 Pictures][44663]
  * [6 See also][44664]
    * [6.1 Manufacturer images][44665]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
The PCB has the following silkscreened on it: 
[code] 
    AL_QZ01_MB_V10
[/code]
# Sunxi support
## Current status
Basic support in mainline trees, more features found in out-of-tree mainline Linux forks. 
## Images
[Prebuilt postmarketOS images][44666] [Ubuntu Touch (UBports) images][44667]
## Manual build
You can build things for yourself by following our [ Manual build howto][44668] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _pinephone_defconfig_ build target. 
### Mainline Linux Kernel
Use the _sun50i-a64-pinephone-1.1.dtb_ or _sun50i-a64-pinephone-1.2.dtb_ device-tree binary in the mainline kernel. Mainline U-Boot detects the model and selects the appropriate DTB automatically. 
A more sophisticated feature set is available in the [downstream forked kernel][44669]. 
# Tips, Tricks, Caveats
There are 6 dip switches if the back cover is removed, and they're labeled by a sticker: 
\- Modem \- Wifi/BT \- Microphone (internal microphone, not headphones) \- Rear Camera \- Front Camera \- Headphone (switches between headphones and UART) 
## FEL mode
Use the fel-sdboot.sunxi file in sunxi-tools to enter FEL mode. 
# Adding a serial port
There is no need to add one as the UART is multiplexed with audio jack, see [[1]][44670] for the pinout. 
You'll also need to turn off the headphone dip switch in order to turn on UART. 
## Device disassembly
1\. With the phone facing you, pull off the back cover by pulling the tab on the bottom right, holding the phone in your other hand. then pry off the rest of the case. 
  * [![Pinephone prybackcover1.png][44671]][44672]
  * [![Pinephone prybackcover2.png][44673]][44674]

From here you can access the pogo pins and replace the battery. 
2\. Then, with the phone facing the table, take the battery out using the indent below the battery. push the battery up against it's spring contacts, then out. 
  * [![Pinephone removebatt1.png][44675]][44676]
  * [![Pinephone removebatt2.png][44677]][44678]

From here you can change the SIM and MicroSD. 
3\. Remove the screws with a small philips screwdriver. Remember the screw in the top right corner, which is covered by a paper tamper seal. 
  * [![Pinephone unscrew1.png][44679]][44680]
  * [![Pinephone unscrew2.png][44681]][44682]

4\. Carefully remove the back assembly. there is ~1mm gap on the bottom, so you can just use your thumbnail or something to unsnap it, and then pry the rest of the back assembly. 
  * [![Pinephone prybackassembly1.png][44683]][44684]
  * [![Pinephone prybackassembly3.png][44685]][44686]

From here you can replace the individual components on the board. 
Note: When re-assembling, replace the screws and make sure the back cover and back assembly are fully snapped in place. 
# Pictures
Take some pictures of your device, [ upload them][44687], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Pinephone-front.jpg][44688]][44643]
  * [![New-Pinephone-back.jpg][44689]][44690]
  * [![Pinephone sidebuttons.jpg][44691]][44692]
  * [![Pinephone backcoveroff.jpg][44693]][44694]
  * [![Pinephone circutboard.png][44695]][44696]
  * [![Device board back.jpg][44697]][44698]

# See also
[Pine Pinebook][44699]
[PineTab][44700]
## Manufacturer images
Optional. Add non-sunxi images in this section.
