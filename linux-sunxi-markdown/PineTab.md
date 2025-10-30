# PineTab
PineTab  
---  
[![Device front.jpg][44734]][44735]  
Manufacturer |  [Manufacturer][44736]  
Dimensions |  TODO  
Release Date |  2019   
Website |  [Device Product Page][44737]  
Specifications   
SoC |  [A64][44738] @ 1.152Ghz   
DRAM |  2GiB LPDDR3 @ 554MHz   
NAND |  16GiB eMMC, upgradable   
Power |  DC 5V @ 3A (barrel jack with unknown size), 5000mAh 3.7V Li-Ion battery, microUSB   
Features   
LCD |  1280x800 (10" 8:5)   
Touchscreen |  10-finger capacitive ([Goodix GT9271][44739])   
Video |  HDMI (Type C - micro)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8723CS][44740])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
Camera |  2MP (????x????) front, 5MP (????x????) rear   
Other |  Accelerometer ([Bosch BMA223][44741])   
This page needs to be properly filled according to the [New Device Howto][44742] and the [New Device Page guide][44743].
## Contents
  * [1 Identification][44744]
  * [2 Sunxi support][44745]
    * [2.1 Current status][44746]
    * [2.2 Images][44747]
    * [2.3 Manual build][44748]
      * [2.3.1 U-Boot][44749]
        * [2.3.1.1 Mainline U-Boot][44750]
      * [2.3.2 Linux Kernel][44751]
        * [2.3.2.1 Mainline kernel][44752]
    * [2.4 FEL mode][44753]
  * [3 Adding a serial port][44754]
  * [4 Device disassembly][44755]
  * [5 Pictures][44756]
  * [6 See also][44757]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
The PCB has the following silkscreened on it: 
[code] 
    PINE_TAB-V1_1-20190617
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _SOC_BOARD_DEVICE_*.*_

# Sunxi support
## Current status
Currently supported by out-of-tree mainline Linux forks. 
## Images
[Prebuilt postmarketOS images][44758]
## Manual build
You can build things for yourself by following our [ Manual build howto][44759] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
As we currently do not have any specific U-Boot config for this device, Use the _pine64-lts_defconfig_ build target temporarily as a hack. 
### Linux Kernel
#### Mainline kernel
Currently not supported in mainline. 
Use the _sun50i-a64-pinetab.dtb_ device-tree binary in the downstream forked kernel at [[1]][44760]. 
## FEL mode
Use the fel-sdboot.sunxi file in sunxi-tools to enter FEL mode. 
# Adding a serial port
PineTabs have the serial port multiplexed with the audio jack, see [[2]][44761] for the pinout. 
There's a switch to switch audio jack between headphone and UART, located near the microSD slot. 
# Device disassembly
Use [Plastic tool][44762] to loose the plastic clips between the main body and the back cover. Finish this operation at the side that the keyboard pogo pins are located. 
# Pictures
Take some pictures of your device, [ upload them][44763], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][44764]][44735]
  * [![Device back.jpg][44765]][44766]
  * [![Device buttons 1.jpg][44767]][44768]
  * [![Device buttons 2.jpg][44769]][44770]
  * [![Device board front.jpg][44771]][44772]
  * [![Device board back.jpg][44773]][44774]

# See also
[Pine Pinebook][44775] ~
