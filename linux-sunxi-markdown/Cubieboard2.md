# Cubietech Cubieboard2
(Redirected from [Cubieboard2][14725])
 
Cubietech Cubieboard2  
---  
[![Cubieboard2 Overview.jpg][14728]][14729]  
Manufacturer |  [CubieTech][14730], [Cubieboard][14731]  
Dimensions |  10 _cm_ x 6 _cm_  
Release Date |  June 2013   
Website |  [Cubieboard2 Product page][14732]  
Specifications   
SoC |  [A20][14733] @ 1Ghz   
DRAM |  1GiB DDR3 @ 480MHz ([GT8UB256M16BP-BG][14734], [H5TQ4G63AFR-PBC][14735])   
NAND |  4GB   
Power |  DC 5V @ 2A (4.0mm/1.7mm barrel plug - centre positive)   
Features   
Video |  HDMI   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, HDMI   
Network |  10/100 Ethernet ([Realtek RTL8201CP][14736])   
Storage |  µSD, SATA (+5v power)   
USB |  2 USB2.0 Host, 1 USB2.0 OTG   
Other |  IRDA (Vishay HS0038B)   
Headers |  2 48pin expansion ports which export (amongst others): I2C (TWI), SPI, RGB/LVDS, CSI/TS, FM-IN, ADC, CVBS, VGA, SPDIF-OUT, touch-panel   
Cubieboard2 is an update of the popular [Cubieboard][14737] and replaces the [A10 SoC][14738] with the pin-compatible [A20 SoC][14733]. 
## Contents
  * [1 Identification][14739]
  * [2 Sunxi support][14740]
    * [2.1 Current status][14741]
    * [2.2 Images][14742]
    * [2.3 HW-Pack][14743]
    * [2.4 BSP][14744]
    * [2.5 Manual build][14745]
      * [2.5.1 U-Boot][14746]
        * [2.5.1.1 Sunxi/Legacy U-Boot][14747]
        * [2.5.1.2 Upstream/Mainline U-Boot][14748]
      * [2.5.2 Linux Kernel][14749]
        * [2.5.2.1 Sunxi/Legacy Kernel][14750]
        * [2.5.2.2 Upstream/Mainline kernel][14751]
  * [3 Tips, Tricks, Caveats][14752]
    * [3.1 FEL mode][14753]
    * [3.2 Machine ID mismatch][14754]
  * [4 Adding a serial port][14755]
  * [5 Pictures][14756]
  * [6 Hardware documentation][14757]
  * [7 Also known as][14758]
  * [8 See also][14759]

# Identification
The board helpfully reads "Cubietech" "Cubieboard.org" and has an A20 chip on it. 
# Sunxi support
## Current status
The cubieboard is well represented within the main sunxi developer community and has excellent support both in u-boot as well as 3.4 and mainline kernels. 
## Images
  * [Android firmwares.][14760]
  * [Further android firmwares.][14761]
  * [Ubuntu images.][14762]
  * [Lubuntu images.][14763]
  * [ArchLinuxARM image and installation procedure][14764]

Cubietech also has a bunch of official firmwares available on their [download][14765] page. 
## HW-Pack
Generating a HW pack for the cubieboard2 is easily done with the sunxi-bsp and well supported. 
## BSP
Under the BSP the cubieboard2 is simply known as cubieboard2. Just run: 
[code] 
    ./configure cubieboard2
    make
[/code]
## Manual build
You can build things for yourself by following our [ Manual build howto][14766] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _Cubieboard2_ build target. 
#### Upstream/Mainline U-Boot
Use the _Cubieboard2_ build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
Use the [_cubieboard2.fex_][14767] file. 
#### Upstream/Mainline kernel
Use the _sun7i-a20-cubieboard2.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
The only difference between the first version of the [Cubieboard][14737] (with the [A10][14738], mistakenly known as the "original" Cubieboard, but both versions are "original") and the Cubieboard2 (second version with the [A20][14733]) is the SoC itself. The other hardware is _completely_ identical. Because of this many of the [Tips, Tricks, Caveats of the Cubieboard1][14768] regarding the hardware can be applied to the Cubieboard2 as well. 
## FEL mode
The FEL button triggers [ FEL mode][14769]. 
## Machine ID mismatch
There is a difference in the naming of the sun7i platform between the cubieboard2 stock u-boot and the sunxi u-boot. This might cause the kernel to refuse to load, with a message like this: 
[code] 
    Error: unrecognized/unsupported machine ID (r1 = 0x000010bb).
    
    Available machine support:
    
    ID (hex)        NAME
    00000f35        sun7i
    
    Please check your kernel config and/or bootloader.
[/code]
You need to add the following to your [ U-Boot boot.cmd][14770] for the cubieboard stock variant: 
[code] 
    setenv machid 0x00000f35
[/code]
or (for the sunxi variant) 
[code] 
    setenv machid 0x000010bb
[/code]
# Adding a serial port
[![][14771]][14772]
[][14773]
Cubieboard UART pads
There is a nice 2.54mm pin header near to the SoC. All you have to do is connect the correct wires, according to our [UART howto][14774] or the [ Cubieboard TTL howto][14775]. **[![Exclamation-red.png][14776]][14777]Do not connect Vcc as that might damage your board.**
# Pictures
  * [![Cubie UP.jpeg][14778]][14779]
  * [![Cubie DOWN.jpeg][14780]][14781]
  * [![Cubie FRONT.jpeg][14782]][14783]
  * [![Cubie REAR.jpeg][14784]][14785]

# Hardware documentation
  * <https://github.com/lipro-armbian/pddocs/tree/master/Cubietech/CubieBoard2>

# Also known as
Like the first [Cubieboard][14737], the Cubieboard2 was very popular on its own. Therefor, no rebadging has taken place, but who knows, there might be some bad chinese rip-offs out there, which carry the same name. 
# See also
  * [Cubietech Cubieboard][14737]
  * [Cubietech Cubietruck][14786]
