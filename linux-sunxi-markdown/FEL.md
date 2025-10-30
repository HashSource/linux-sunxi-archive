# FEL
FEL is a low-level subroutine contained in the [BootROM][19015] on Allwinner devices. It is used for initial programming and recovery of devices using USB. 
[![Sticky-note-pin.png][19016]][19017] Your device therefore needs to be attached to a host (your PC) by means of a **USB cable** , connected to a port where the sunxi device will present itself as a USB 'slave' (i.e. in device mode). Usually that means the "OTG" connector.[[1]][19018]
## Contents
  * [1 Tools for talking FEL mode][19019]
  * [2 Entering FEL mode][19020]
    * [2.1 Power off your device][19021]
    * [2.2 Triggering FEL mode][19022]
      * [2.2.1 Through a special FEL button][19023]
      * [2.2.2 By holding a standard button][19024]
      * [2.2.3 Through serial console][19025]
      * [2.2.4 Through a special SD card image][19026]
      * [2.2.5 By having no valid boot image][19027]
    * [2.3 Verifying FEL mode][19028]
      * [2.3.1 A new USB device appears][19029]
      * [2.3.2 Running the sunxi-fel tool][19030]
      * [2.3.3 Serial output][19031]
    * [2.4 Common Pitfalls][19032]
      * [2.4.1 It failed!][19033]
      * [2.4.2 Reading over USB fails][19034]
  * [3 FEL Protocol][19035]
  * [4 Tips and tricks][19036]
  * [5 See also][19037]
  * [6 References][19038]

# Tools for talking FEL mode
Our [tools][19039] repository has some tools for dealing with FEL mode. If you haven't done so already, [retrieve the repository and build it][19040]. 
# Entering FEL mode
While there are a few different ways to trigger FEL mode, they are not always equal. Some do low-level initialization (load Boot0 and Boot1), and some don't. 
If you are going to use FEL mode to retrieve device information, you need a to pick a method of entering FEL mode that initializes Boot1. 
## Power off your device
Before you try to enter FEL mode, make sure that your device is **truly powered off**. Do not leave any cables attached. 
[![Exclamation.png][19041]][19042] Due to a common design flaw, [(current leaking from) the UART][19043] will often keep the device in a slightly working state. So before you power up your device again: disconnect your UART, and re-attach it. 
## Triggering FEL mode
### Through a special FEL button
This is either called **recovery** or **uboot** or **fel**. If your device features such a button, you just need to hold it during power-up, and the device should have entered FEL mode just fine. 
### By holding a standard button
This is usually one of the standard tablet buttons, like the **VOL+** key or something. 
The following seems to work: 
  * Press and hold the suspected or reported FEL key.
  * Press and hold the power key for about 2 seconds.
  * Release the power key, and press it at least 3 times immediately.

Boot1 is initialized using this method. 
### Through serial console
If you have access to the [UART][19044] already, you can send the character '1' ('2' on some devices) to the device during power-up. 
Boot1 is initialized using this method. 
With later SoCs, Allwinner's U-boot supports the "efex" command. 
If "efex" is not available in your U-boot, you can use the simple uboot "go" command with arguments pointing to the return FEL address:  
[http://linux-sunxi.org/BROM#Other_booting_methods][19045]  
=> go 0xffff0020   
Starting application at 0xFFFF0020 ... 
  
Entering this command at the u-boot prompt will enter into FEL mode. 
[![Sticky-note-pin.png][19016]][19017] _Note:_ This is just an _alternative way of entering FEL mode_. FEL itself can/will _not_ talk over the serial connection! In other words: You still have to connect a USB cable to make actual use of FEL and associated tools. 
### Through a special SD card image
Included in our [sunxi-tools repository][19039], there is a small SDCARD boot image that does nothing more than jump to FEL. 
Just install it on an sdcard as you would with the u-boot SPL (**be sure to change`/dev/sdX` to where your sdcard is**): 
[code] 
    wget https://github.com/linux-sunxi/sunxi-tools/raw/master/bin/fel-sdboot.sunxi
    dd if=fel-sdboot.sunxi of=/dev/sdX bs=1024 seek=8
    
[/code]
### By having no valid boot image
If the [BROM][19015] doesn't find any valid boot image, it will automatically enter FEL mode. 
Thus for most devices that don't feature onboard NAND or eMMC, this should apply when you simply remove the SD/µSD card. 
## Verifying FEL mode
### A new USB device appears
When you run lsusb, you should see the following in it: 
[code] 
    Bus 001 Device 074: ID 1f3a:efe8
[/code]
### Running the sunxi-fel tool
[code] 
    > ./sunxi-fel version
    AWUSBFEX soc=00162500(A13) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
[/code]
### Serial output
If the method you chose initialized boot1, then you should see something like this over serial: 
[code] 
    HELLO! BOOT0 is starting!
    boot0 version : .3.0
    dram size =1024
    Succeed in opening nand flash.
    Succeed in reading Boot1 file head.
    The size of Boot1 is 0x00036000.
    The file stored in 0X00000000 of block 2 is perfect.
    Check is correct.
    Ready to disable icache.
    Succeed in loading Boot1.
    Jump to Boot1.
    [       0.145] boot1 version : 1.3.1a
    [       0.145] pmu type = 3
    [       0.145] bat vol = 4117
    [       0.176] axi:ahb:apb=3:2:2
    [       0.176] set dcdc2=1400, clock=1008 successed
    [       0.178] key
    [       2.486] you can unclench the key to update now
    [       2.486] key found, jump to fel
[/code]
## Common Pitfalls
### It failed!
Try again, make sure you fully power down the device and make sure you get the order of events right. You'll get there. 
### Reading over USB fails
If the following happens: 
[code] 
    > ./sunxi-fel read 0x43000000 0x20000 script.bin
    libusb usb_bulk_send error -7
[/code]
Then you probably are trying to read things that only get initialized when boot0 and boot1 have been loaded. Try another method of entering FEL mode, one that does initialize to boot1. 
# FEL Protocol
The FEL is actually a tiny usb stack implementing [a special USB protocol][19046]. 
Part of it is implemented in our [tools repository][19047] and can be used as reference code. 
# Tips and tricks
  * if you get usb_bulk_send error -7 after some command it means soc/fel stack left fel mode or crashed. you either booted something or hung the device
  * you can reset via fel by enabling watchdog: 
    * For A10 compatible ./sunxi-fel writel 0x01c20c94 3
    * For H3/H5 compatible ./sunxi-fel writel 0x01c20cb8 1
  * Or, if in u-boot, use: mw 0x01c20c94 3 ; ; ; ;

This will go back to FEL mode regardless if the device's FEL mode jumper/button is in place. Note that a couple of blank lines are needed after the mw for some reason. 
# See also
  * [ Booting using FEL][19048]

# References
  1. [↑][19049] There are exceptions to this rule, where boards might require you to connect to specific ports and/or use non-standard cables. Most notably is the [Pine64][19050].
