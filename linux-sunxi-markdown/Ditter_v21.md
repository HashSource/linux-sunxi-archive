# Ditter v21
Ditter v21  
---  
[![Ditterv21-300x145.jpg][17028]][17029]  
Manufacturer |  Ditter (Shenzen Zuftai Tecnology Co. Ltd)   
Dimensions |  98 _mm_ x 42 _mm_ x 10 _mm_  
Release Date |  2013   
Specifications   
SoC |  A31s ([A31][17030]) @ 1Ghz   
DRAM |  1GiB DDR3 @ 750MHz   
NAND |  8GB   
Power |  DC 5V @ 2A (though dedicated USB plug)   
Features   
Video |  HDMI   
Network |  WiFi 802.11 b/g/n ([Ampak AP6210][17031])   
Storage |  µSD   
USB |  1 USB2.0 Host, 1 USB2.0 OTG   
## Contents
  * [1 Identification][17032]
  * [2 Sunxi support][17033]
    * [2.1 Images][17034]
    * [2.2 HW-Pack][17035]
    * [2.3 BSP][17036]
    * [2.4 Manual build][17037]
      * [2.4.1 U-Boot][17038]
        * [2.4.1.1 Sunxi/Legacy U-Boot][17039]
        * [2.4.1.2 Mainline U-Boot][17040]
      * [2.4.2 Linux Kernel][17041]
        * [2.4.2.1 Sunxi/Legacy Kernel][17042]
        * [2.4.2.2 Mainline kernel][17043]
  * [3 Tips, Tricks, Caveats][17044]
    * [3.1 FEL mode][17045]
    * [3.2 Device disassembly][17046]
    * [3.3 Locating the UART][17047]
  * [4 Pictures][17048]
  * [5 Also known as][17049]
    * [5.1 Manufacturer images][17050]

# Identification
The device is an HDMI "stick", defined also as an "Android mini-PC", marked with "Ditter (TM) V21" brand and model on the external case. 
The PCB back has the following silkscreened on it: 
[code] 
    I11 V1.3
    120130809
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: Softwinner
  * Build Number: mars_i11-eng 4.2.2 JDQ39 20131108 test-keys

# Sunxi support
Support on sunxi-linux is still not present. Collecting info. 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][17051]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
WIP
Apart from below caveats, [ Manual build howto][17052] procedures should be used as a guideline. 
Extracting "fex" file out of the file extracted with [Sunxi-tools#script-extractor][17053]: 
[code] 
    $ adb shell sunxi-script_extractor > script_extractor.out
[/code]
But "fexc" tool fails: 
[code] 
    $ ./sunxi-fexc -v -I bin -O fex script_extractor.out ditter_v21.fex
    ./sunxi-fexc: from bin:script_extractor.out to fex:ditter_v21.fex
    fexc-bin: script_extractor.out: version: 0.1.2
    fexc-bin: script_extractor.out: size: 131113 (73 sections)
    E: fexc-bin: script_extractor.out: product.~!: unknown type 0
[/code]
Error is because the "product" entry is none of the expected types: 
[code] 
    enum script_value_type {
    	SCRIPT_VALUE_TYPE_SINGLE_WORD = 1,
    	SCRIPT_VALUE_TYPE_STRING,
    	SCRIPT_VALUE_TYPE_MULTI_WORD,
    	SCRIPT_VALUE_TYPE_GPIO,
    	SCRIPT_VALUE_TYPE_NULL,
    };
[/code]
Infact, dumping head of the file, entries are all 0: 
[code] 
    $ hexdump -C script_extractor.out | head 
    00000000  49 00 00 00 00 00 00 00  01 00 00 00 02 00 00 00  |I...............|
    00000010  70 72 6f 64 75 63 74 00  00 00 00 00 00 00 00 00  |product.........|
    00000020  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    00000030  02 00 00 00 de 02 00 00  70 6c 61 74 66 6f 72 6d  |........platform|
    00000040  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    00000050  00 00 00 00 00 00 00 00  01 00 00 00 f2 02 00 00  |................|
    00000060  74 61 72 67 65 74 00 00  00 00 00 00 00 00 00 00  |target..........|
    00000070  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    00000080  02 00 00 00 fc 02 00 00  70 6f 77 65 72 5f 73 70  |........power_sp|
    00000090  6c 79 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |ly..............|
[/code]
It seems with A31 type devices that the fex file forms part of the uboot image and cannot be extracted with above tools. 
On the other hand, the [Sunxi-tools#meminfo][17054] tool extracts the memory info as expected. 
  

### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_MANUFACTURER_DEVICE.fex_][17055] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
Referring to the front PCB picture below, which shows two buttons near the lower border, device seems like getting to FEL mode trying to push the LEFT button while plugging in the power USB cable (the one marked with DC on case back). 
Plugging also an OTG USB cable to a Linux host (to the other mini-USB plug), I can read basic FEL info (using [Sunxi-tools][17056]): 
[code] 
    $ sudo ./sunxi-fel ver
    AWUSBFEX soc=00001633(A31) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
[/code]
but the _fel read_ command: 
[code] 
    $ sudo ./sunxi-fel read 0x42400000 0x82d0 boot1.header
[/code]
just hangs there... Later, _fel ver_ fails too (returns nothing). I also noticed chip getting very hot. 
## Device disassembly
Device case can be opened with a sharp knife, to speatare the two shells enclosing the PCB. No screw is used, just plastic pins for the joint. Pay attention to the flexible antenna cable. 
## Locating the UART
Apparently no UART pads are present on PCB (I couldn't find any evident on it). 
# Pictures
  * [![Ditterv21-300x145.jpg][17057]][17029]
  * [![20160114 164217.jpg][17058]][17059]
  * [![20160114 164200.jpg][17060]][17061]

# Also known as
The MK823 has the same PCB, but in version 1.2. It differs apparently just for the missing buttons, which this device has on the PCB front. 
## Manufacturer images
No manufacturer stock image is published (to present knowledge).
