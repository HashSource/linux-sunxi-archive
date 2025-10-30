# PocketBook Basic Lux 4 (PB618)
PocketBook Basic Lux 4 (PB618)  
---  
[![Device front.jpg][45187]][45188]  
Manufacturer |  [PocketBook][45189]  
Dimensions |  width _161.3_ x breadth _108_ x height _8_  
Release Date |  2023   
Website |  [Device Product Page][45190]  
Specifications   
SoC |  [B288][45191] @ 1Ghz   
DRAM |  512MiB DDR3L @ 1866MHz   
NAND |  8GB KLM8G1GETF-B041   
Power |  1300mAh battery   
Features   
LCD |  758x1024 (X" X:Y)   
Touchscreen |  2-finger self-capacitive ([FocalTech FT6336U][45192])   
Video |  proprietary eInk display / ED060XCH   
Audio |  none   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][45193])   
Storage |  nand/eMMC KLM8G1GETF-B041, µSD(external)   
USB |  X USB2.0 Host, 1 USB2.0 OTG   
Camera |  none   
Other |  eInk "backlight", AXP227   
Headers |  UART, TWI   
This page needs to be properly filled according to the [New Device Howto][45194] and the [New Device Page guide][45195].
If a device is special, then feel free to provide a terse description of what makes this device so special. But terse, no novels, no marketing blurb.
## Contents
  * [1 Identification][45196]
  * [2 Sunxi support][45197]
    * [2.1 Current status][45198]
    * [2.2 Images][45199]
    * [2.3 HW-Pack][45200]
    * [2.4 BSP][45201]
    * [2.5 Manual build][45202]
      * [2.5.1 U-Boot][45203]
        * [2.5.1.1 Sunxi/Legacy U-Boot][45204]
        * [2.5.1.2 Mainline U-Boot][45205]
      * [2.5.2 Linux Kernel][45206]
        * [2.5.2.1 Sunxi/Legacy Kernel][45207]
        * [2.5.2.2 Mainline kernel][45208]
  * [3 Tips, Tricks, Caveats][45209]
    * [3.1 Preinstalled U-Boot shell/monitor entry][45210]
    * [3.2 FEL mode][45211]
    * [3.3 AXP227][45212]
  * [4 Adding a serial port (**voids warranty**)][45213]
    * [4.1 Device disassembly][45214]
  * [5 Pictures][45215]
  * [6 Schematic][45216]
  * [7 Also known as][45217]
  * [8 See also][45218]
    * [8.1 Files to understand the device better:][45219]
    * [8.2 Manufacturer images][45220]

# Identification
On the back of the device, the following is printed: 
[code] 
    Model No.: PB618
[/code]
The PCB has the following silkscreened on it: 
[code] 
    XRZ_E159-PB618 main V1.0 20230115
[/code]
# Sunxi support
## Current status
Currently no support 
## Images
Optional. Add MANUFACTURER DEVICE specific sunxi ROM images here. E.g. a livesuit image or some other linux image which uses linux-sunxi code. Do not put non-sunxi images here, they should live under [See also][45218]. If no sunxi based images are available, this section can be removed.
## HW-Pack
Optional. Add MANUFACTURER DEVICE sunxi HW-pack specifics here. When empty, this section can be removed.
## BSP
Optional. Add MANUFACTURER DEVICE sunxi BSP specifics here. When empty, this section can be removed.
## Manual build
You can build things for yourself by following our [ Manual build howto][45221] and by choosing from the configurations available below. 
### U-Boot
#### Sunxi/Legacy U-Boot
Legacy B288 U-Boot uploaded by PocketBook: 
<https://github.com/pocketbook/uboot_b288>
My fork with fixed compilation and Boot0 modifications to init DRAM: 
<https://github.com/Soupborsh/uboot_b288>
#### Mainline U-Boot
There is almost zero support. I am absolute noob but I created a [U-Boot fork][45222] which can be booted through FEL. 
What works: 
  * UART
  * GPIO (seems to work, can toggle pins)
  * I2C (Currently bus 2 does not work)
  * USB maybe??

Booting from FEL: 
  1. Init DRAM (see [#FEL_mode][45223])
  2. `sunxi-fel write 0x4a000000 u-boot-dtb.bin`
  3. `sunxi-fel execute 0x4a000000`

### Linux Kernel
#### Sunxi/Legacy Kernel
Legacy B288 3.10.65 kernel uploaded by PocketBook: 
<https://github.com/pocketbook/kernel-b288>
My fork with fixed compilation: 
<https://github.com/Soupborsh/kernel-b288>
Touchscreen proprietary binary module does not work with it. I booted kernel using preinstalled U-Boot. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
### Preinstalled U-Boot shell/monitor entry
On the step where you need to press power button 3 times to enter FEL, press it less than 3 times and type into UART many times CTRL+C and many other characters. U-Boot should then enter it's shell/monitor and you should see it display interrupts. 
Emmc works, however, if you use `mmc` command it stops for some reason. IIRC You can use `fatls`, `ls` and similar, as well as, there was a command to enter USB Mass Storage Mode but it is for /boot partition only. 
## FEL mode
Way that doesn't rely on emmc contents(probably unsafe): 
  1. Remove protective metal shield on PCB
  2. Connect smd thing that probably goes to probably emmc clock from side of CPU to ground(it is PC4 gpio pin)
  3. Power on

Intended by the manufacturer way: 
  1. Connect device to pc by USB
  2. Power off device
  3. Press and hold central home button, do not release
  4. Press power on button once to power on, and then 3 more times to enter FEL mode
  5. You can release central home button now, your device should be now in FEL mode

Here is what UART outputs during this: 
[code] 
    [     0.270]HELLO ;) BOOT0 is starting!
    [     0.280]AXP22 Voff=3.3V
    [     0.283]fel flag  = 0x00000000
    [     0.292]DRAM: 512
    [     0.311]MMC3 v5.1 HSDDR52/DDR50 8 bit 7456 MB
    [     0.361]Entry_name        = u-boot
    [     0.369]Entry_name        = soc-cfg
    [     0.373]Entry_name        = dtb
    [     0.377]Jump to u-boot
    
    
    U-Boot 2014.07-hg78e7bb6939f0 (Aug 08 2023 - 15:56:03) Allwinner Technology , Build: 78e7bb6939f0
    
    normal mode
    i2c_init: by cpux
    [      0.397]pmbus:   ready
    [      0.412]PMU: AXP221
    [      0.412]PMU: AXP22X found
    [      0.413]PMU: dcdc2 1260
    [      0.415]IC Version: 1(0:A 1:B 2:other)
    [      0.418]PMU: pll1 1008 Mhz,PLL6=600 Mhz
    AXI=336 Mhz,AHB=100 Mhz, APB1=50 Mhz
    dcdc1_vol = 3000, onoff=1
    dcdc2_vol = 1260, onoff=1
    dcdc3_vol = 1800, onoff=0
    dcdc4_vol = 1100, onoff=1
    dcdc5_vol = 1350, onoff=1
    aldo1_vol = 3000, onoff=0
    aldo2_vol = 1800, onoff=1
    aldo3_vol = 3000, onoff=1
    dldo1_vol = 1800, onoff=1
    dldo2_vol = 3300, onoff=0
    dc1sw_vol = 3300, onoff=0
    dc5ldo_vol = 1100, onoff=0
    DRAM:  512 MiB
    fdt addr: 0x56ddc0f8
    gd->fdt_size: 0x11ec0
    Relocation Offset is: 15f3b000
    gic: normal mode
    [      0.534]MMC:        3
    [mmc]: mmc driver ver 2016-08-01 13:45:00
    [mmc]: get sdc_ex_dly_used 2, use auto tuning sdly
    [mmc]: card3 io is 1.8V.
    [mmc]: get sdc3 sdc_tm4_hs200_max_freq 100.
    [mmc]: get sdc3 sdc_tm4_hs400_max_freq 100.
    SUNXI SD/MMC: 3
    [mmc]: 50 MHz...
    [mmc]: sample: 52 - 192(ps)
    [mmc]: ds: 50 - 200(ps)
    [mmc]: 100 MHz...
    [mmc]: sample: 26 - 192(ps)
    [mmc]: ds: 25 - 200(ps)
    [mmc]: media type 0x8000000
    [mmc]: host caps: 0x1ef
    [mmc]: MMC3: v5.1 HSSDR52/SDR25 50MHz 8 bit 7456 MB
    [mmc]: already at HSSDR52_SDR25 mode
    [mmc]: EOL Info(Rev blks): Normal
    [mmc]: Wear out(type A): 0%-10% life time used
    [mmc]: Wear out(type B): 0%-10% life time used
    [      0.613]sunxi flash init ok
    Using default environment
    
    bootcmd set setargs_mmc
    vbus pc exist, limit to pc
    Bus:2 VBat:4232 Ratio:100
    Disable PF0-PF5
    SW fel:   1
    VBUS req: 0
    KEYCOUNTER:1
    KEYCOUNTER:2
    Entering FEL
    set next system status
    sunxi_board_close_source
    [mmc]: MMC Device 2 not found
    [mmc]: mmc 2 not find, so not exit
    [mmc]: mmc exit start
    [mmc]: 50 MHz...
    [mmc]: sample: 51 - 196(ps)
    [mmc]: ds: 51 - 196(ps)
    [mmc]: 100 MHz...
    [mmc]: sample: 26 - 192(ps)
    [mmc]: ds: 25 - 200(ps)
    [mmc]: mmc 3 exit ok
    reset cpu
    [     0.270]HELLO ;) BOOT0 is starting!
    [     0.280]AXP22 Voff=3.3V
    [     0.282]fel flag  = 0x5aa5a55a
    [     0.286]eraly jump fel
    
[/code]
DRAM is not initialized. 
DRAM initialization is WIP, we can execute modified Boot0 to init DRAM and return to FEL.: 
1.Build [My Boot0 fork][45224]: 
2.Set FEL flag: 
`sunxi-fel writel 0x1C20508 0x5AA5A55A`
3.Load and execute boot0.img(result of building Boot0) `sunxi-fel spl boot0.img`
4.Wait for about 20 seconds, and the attempt running some FEL commands(`sunxi-fel readl 0x1C20508` for example) until they do not fail. 
5\. Your device should be in FEL with initialized DRAM. If it did not work, you can try again(sometimes it does not work for me). 
## AXP227
AXP227 seems to be same as [AXP221][45225] but with address 34, even Boot0 says AXP221 to it. SCL and SDA pins seem to be in the same place. I watched them with my logic analyzer. I can manually write to registers(using U-Boot's i2c command) specifed in AXP221 wiki and it works here(at least dldo2 and "REG 12h: Regulator output control"). 
# Adding a serial port (**voids warranty**)
[![][45226]][45227]
[][45228]
PB618 UART pads
Follow [UART howto][45229], there are 3 pads shown in the photo, solder wires to them. UART is 3.3V and 115200 8N1(default for many programs, such as minicom.) 
## Device disassembly
See [Plastic tool howto][45230]. Back panel can be removed using plastic tool, it pops out. Power connector needs to be lifted up(be careful, I am not sure because I had to apply a lot of force), other connectors can be disconnecting by gently lifting the thing that fixes in place the ribbon cable, and then ribbon cable can be disconnected from motherboard easily since nothing holds them. Motherboard can be removed by unscrewing 4 screws holding it then sliding slightly in the direction to SD card hole(I refer to it as downwards) because there are some metal things that hold it on top, then carefully remove ribbon cables through holes to not tear them apart. Screen removing is untested. 
# Pictures
Take some pictures of your device, [ upload them][45231], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Device front.jpg][45232]][45188]
  * [![PB618 back.jpg][45233]][45234]
  * [![Device buttons 1.jpg][45235]][45236]
  * [![Device buttons 2.jpg][45237]][45238]
  * [![Device board front.jpg][45239]][45240]
  * [![Device board back.jpg][45241]][45242]

# Schematic
By toggling GPIO pins and looking at fex file, I identified some pins(hopefully correct), look at the image. 
[![PB618 board with labels.png][45243]][45244]
[][45245]
P.S: I will later upload my Krita file. 
# Also known as
List rebadged devices here.
# See also
[FT6336U datasheet][45246]
[KLM8G1GETF-B041 eMMC datasheet][45247]
### Files to understand the device better:
[decompiled fex file][45248]
[decompiled fdt][45249]
Kernel dts: [sun8iw10p1.dtsi][45250] [sun8iw10p1-pinctrl.dtsi][45251] [sun8iw10p1-clk.dtsi][45252]
[pinctrl-sun8iw10p1.c][45253]
and many others in sources. 
## Manufacturer images
Optional. Add non-sunxi images in this section.
