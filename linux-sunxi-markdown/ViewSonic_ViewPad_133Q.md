# ViewSonic ViewPad 133Q
ViewSonic ViewPad 133Q  
---  
[![Device front.jpg][58726]][58727]  
Manufacturer |  [ViewSonic][58728]  
Specifications   
SoC |  [A31s][58729] @ 1.2Ghz   
DRAM |  1GiB DDR3   
NAND |  16GB   
Power |  DC 5V @ 2.5A, 10000mAh 3.7V Li-Ion battery   
Features   
LCD |  1280x800 (13.3" 16:10)   
Touchscreen |  10-finger capacitive ([Goodix GT9110][58730])   
Video |  HDMI (mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8723AU][58731])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Other |  Accelerometer ([Freescale MMA86xx][58732])   
Headers |  LCD   
This page needs to be properly filled according to the [New Device Howto][58733] and the [New Device Page guide][58734].
  

## Contents
  * [1 Identification][58735]
  * [2 Sunxi support][58736]
    * [2.1 Current status][58737]
    * [2.2 Manual build][58738]
      * [2.2.1 U-Boot][58739]
        * [2.2.1.1 Sunxi/Legacy U-Boot][58740]
        * [2.2.1.2 Mainline U-Boot][58741]
      * [2.2.2 Linux Kernel][58742]
        * [2.2.2.1 Sunxi/Legacy Kernel][58743]
        * [2.2.2.2 Mainline kernel][58744]
    * [2.3 FEL mode][58745]
  * [3 Adding a serial port (**voids warranty**)][58746]
    * [3.1 Device disassembly][58747]
    * [3.2 Locating the UART][58748]
  * [4 Pictures][58749]
  * [5 Also known as][58750]
  * [6 See also][58751]
    * [6.1 Manufacturer images][58752]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    平板电脑/Tablet PC
    型号/Model: ViewPad 133Q
    输入/Input: 5V 2.5A
    中国制造/Made in China
    制造商：优派环宇通信技术（北京）有限公司
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _ViewPad 133Q_
  * Build Number: _A31S_Q130_Q1301L1B_1404109.20140507_

# Sunxi support
## Current status
Not supported yet. 
## Manual build
You can build things for yourself by following our [ Manual build howto][58753] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Not supported yet. 
#### Mainline U-Boot
Not supported yet. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Not supported yet. 
#### Mainline kernel
Not supported yet. 
## FEL mode
The Vol+ button triggers [ FEL mode][58754]. 
# Adding a serial port (**voids warranty**)
[![][58755]][58756]
[][58757]
DEVICE UART pads
## Device disassembly
[Plastic tool howto][58758] can disassembly it easily. 
## Locating the UART
The UART pins are well-noted near the power key. Please refer to [UART howto][58759] for more infomation. 
# Pictures
Take some pictures of your device, [ upload them][58760], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][58761]][58727]
  * [![Device back.jpg][58762]][58763]
  * [![Device buttons 1.jpg][58764]][58765]
  * [![Device buttons 2.jpg][58766]][58767]
  * [![Device board front.jpg][58768]][58769]
  * [![Device board back.jpg][58770]][58771]

# Also known as
# See also
## Manufacturer images
[| PheonixSuit Image download][58772]
