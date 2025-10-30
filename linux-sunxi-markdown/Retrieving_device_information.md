# Retrieving device information
This page describes how to obtain memory information and the script.bin from the stock operating system of a sunxi device. This is needed for adding support for a new device, as part of our [ New Device Bringup howto][47229]. 
Any of the methods below requires that [Sunxi-tools][47230] is installed and built on your computer. 
## Contents
  * [1 Using FEL][47231]
    * [1.1 Entering FEL mode][47232]
      * [1.1.1 By using physical buttons][47233]
      * [1.1.2 By using the serial console][47234]
    * [1.2 Retrieving data over USB in FEL mode][47235]
  * [2 Using the original OS][47236]
    * [2.1 Working with android][47237]
      * [2.1.1 Android Debug Bridge][47238]
      * [2.1.2 Terminal program][47239]
      * [2.1.3 SSH server][47240]
      * [2.1.4 USB storage][47241]
      * [2.1.5 SD-Cards under android][47242]
      * [2.1.6 Rooting android devices][47243]
    * [2.2 Reading memory information from registers][47244]
    * [2.3 copying script.bin from flash][47245]
    * [2.4 copying script.bin from RAM][47246]
  * [3 Using a livesuit image][47247]
    * [3.1 Extract the image][47248]
    * [3.2 Retrieve bootinfo][47249]
    * [3.3 Retrieve script.bin][47250]
    * [3.4 Retrieve firmware and other random files from Android system][47251]
  * [4 Alternate script.bin retrieval method][47252]
  * [5 Other information][47253]
    * [5.1 Wifi, Bluetooth][47254]
    * [5.2 Touchscreen][47255]
      * [5.2.1 Identify via kernel log][47256]
      * [5.2.2 Identify via ADB/Shell][47257]
      * [5.2.3 Identify using the chips from PCB][47258]
    * [5.3 cameras, accelerometers, gps, rtc and other miscellaneous devices][47259]

# Using FEL
Make sure that the original image is on the device, and that the original u-boot will be booted by the device ROM. Remove any SD-card that might have been inserted. 
## Entering FEL mode
The procedure for entering FEL mode is described [on this page][47260], but for clarity, it is reproduced here as well. 
### By using physical buttons
  1. Fully power off the device, if needs be through a power-button reset.
  2. Hold down the home button and do not release.
  3. Power on the device by pressing the power button.
  4. After a few seconds, press the power button at least three times (or just keep on triggering the power button for several seconds).
  5. After several seconds, release home button.

Note that, if you do not have a Home button, the vol+ / vol- button might work as well. If you have booted through a hard reset (if you have a reset button), or by holding the recovery button (if available), or through usbboot, FEL will not load the necessary information to memory, and the retrieved data will be bogus. 
### By using the serial console
  1. Fully power off the device, if needs be through a power-button reset.
  2. Connect the UART cable (but do not connect it before or the device will not power off properly).
  3. Start the console program.
  4. Send "2" over the serial link, by hold down "2" on your keyboard.
  5. Power on the device by pressing the power button.
  6. Wait until boot1 says it enters FEL mode, and then you can release "2".

## Retrieving data over USB in FEL mode
You should now attach a USB OTG cable. If you have been able to correctly trigger FEL mode, you should now be able to get the FEL version. Run the following from the sunxi-tools tree on your host: 
[code] 
    ./sunxi-fel version
    
[/code]
This should return something resembling: 
[code] 
    AWUSBFEX soc=00162300(A10) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000
    
[/code]
If not, you might not have entered FEL mode correctly. 
Now you should be able to retrieve the relevant information by running: 
[code] 
     ./sunxi-fel read 0x42400000 0x82d0 boot1.header 
     ./sunxi-fel read 0x43000000 0x20000 script.bin 
    
[/code]
Now the retrieved data can be converted to readable text which can then be used in the [ Device Bringup howto][47229]. 
[code] 
     ./sunxi-bootinfo boot1.header > bootinfo.txt
     ./bin2fex script.bin script.fex
    
[/code]
# Using the original OS
## Working with android
The information which was originally here spent most of its time dealing with android intricacies. These are often device specific and the necessary information tends to be multiplied endlessly all over the internet. 
To successfully retrieve the necessary information, you need access to the command line, you need a means of transferring the retrieved data, and you need to have root access to the device. 
### Android Debug Bridge
When working, ADB is by far the most convenient way of working with android. It can give you shell access, and can transfer files. 
More information on ADB can be found [here][47261]. 
### Terminal program
... 
### SSH server
... 
### USB storage
... 
### SD-Cards under android
... 
### Rooting android devices
Most sunxi based systems have no restrictions, and root access can be readily attained. If not, search the web for android forums which might describe how to root your device. 
## Reading memory information from registers
DRAM information can be read from the SoC registers directly using the [ meminfo tool][47262]. 
Once you've [ built this tool][47263], all you need to do is get this file somewhere on your android filesystem (for instance, /data/cache), make sure that it is executable (chmod 755), and then run it and retrieve its output (for instance, to the sdcard). 
## copying script.bin from flash
Script.bin is directly available from the first partition of the NAND flash (but apparently this is not the case with newer Allwinner devices). Under Android, this flash device should appear as /dev/block/nanda. Often nanda is already mounted, if not, you can just mount it with -t vfat. 
## copying script.bin from RAM
Script.bin can be also dumped directly from RAM using the [ script-extractor tool][47264]. 
# Using a livesuit image
While it is much much preferable to retrieve information from your device directly, this sometimes is not possible (either due to a bricked device, or the lack of a fel button or usb-otg). If you have been able to find a livesuit image, you might still get the information you need, at least until you can boot a full sunxi and examine the nand filesystem directly. 
## Extract the image
First, git clone the [ awutils repository][47265] and build it. 
Then, extract the image with awimage: 
[code] 
    awimage -u name.img
[/code]
This will create a directory called _name.img.dump_ , filled with loads of files and matching .hdr files. 
## Retrieve bootinfo
The files for this are often called _12345678_1234567890boot_0_ or _2345678_1234567890boot_1_. When in doubt, grep: 
[code] 
    grep "eGON.BT" *
[/code]
You can then run bootinfo from sunxi-tools on one of the files to retrieve the memory information. 
## Retrieve script.bin
You then need to find the filesystem which usually lives in nanda. This is usually known as _RFSFAT16_BOOTLOADER_00000_ , but when in doubt, grep: 
[code] 
    grep "SCRIPT  BIN" *
[/code]
This is a fat image that can be mounted directly: 
[code] 
    mount -o loop /home/user/dir/name.img.dump/RFSFAT16_BOOTLOADER_00000 /mnt/
[/code]
You can then just take the script.bin and run it through bin2fex. 
## Retrieve firmware and other random files from Android system
The largest file in your unpacked Livesuit image should be a sparse ext4 filesystem. 
[code] 
    file RFSFAT16_SYSTEM_000000000
     RFSFAT16_SYSTEM_000000000: Android sparse image, version: 1.0, Total of 131072 4096-byte output blocks in 1346 input chunks.
    simg2img RFSFAT16_SYSTEM_000000000 RFSFAT16_SYSTEM_000000000.img
    mount -o loop,ro RFSFAT16_SYSTEM_000000000.img /mnt
    cp -a /mnt/vendor/modules .
    
[/code]
You can find simg2img in Android SDK or a distro package such as android-tools-fsutils on Debian. 
# Alternate script.bin retrieval method
This method is limited in that it can only retrieve the script.bin and not the necessary memory information. It also requires access to the UART, which means that it is of limited use now that we have [the ability to talk to FEL mode directly][47266]. 
  1. Fully power off the device, if needs be through a power-button reset.
  2. Connect the UART cable (but do not connect it before or the device will not power off properly).
  3. Start the console program.
  4. Send "1" over the serial link, by hold down "1" on your keyboard.
  5. Power on the device by pressing the power button.
  6. Wait until boot1 says it enters FEL mode, and then you can release "1".

You should now be able to connect a USB OTG cable, and copy script.bin (and .fex if available) off usb storage. 
# Other information
## [Wifi][47267], Bluetooth
It is good idea what to try and find out what [Wifi][47267] and Bluetooth chips your device has. Bluetooth is often implemented in the same chip as wifi if present at all. 
You can try to read the text on a chip near antenna wire (often on a subboard) and compare it to list of [known WiFi chips common on tablets][47267] or try to look at kernel messages from the android system preinstalled on your device. 
It is possible that the chip you have is already supported and will work out of the box when you boot linux but you may have a new yet unknown chip. Even when driver for the [wifi][47267] chip is available somewhere you may need to copy a firmware file from the original android system to use [wifi][47267]. 
## [Touchscreen][47268]
[Touchscreen][47268] support is not very good so far. Although Allwinner SoCs have built-in support for single-touch resistive touchscreen, it is usually not used due to popularity of capacitive multitouch touchscreens. 
Many touchscreens require a firmware file that has to be extracted from android - either from a kernel module (`.ko` file) or from special directory (usually `/etc/firmware` or `/vendor/firmware`). 
### Identify via kernel log
One possible way to identify the touchscreen controller is to look at the kernel messages from the original android system: 
[code] 
    $ cat kernel.log |grep input
    <6>[    1.912941] input: sun4i-keyboard as /devices/virtual/input/input0
    <6>[    2.181851] input: axp20-supplyer as /devices/platform/sun4i-i2c.0/i2c-0/0-0034/axp20-supplyer.28/input  /input1
    <6>[    8.590497] input: Goodix-TS-board-3 as /devices/virtual/input/input2
    <6>[    8.936340] input: bma250 as /devices/virtual/input/input3
    
[/code]
From the log above, we can see that this device has 4 input devices. And using [ common knowledge][47268] we know that this device is using one of the Goodix chips. Further identification is left as a exercise to the reader. 
### Identify via ADB/Shell
If that does not work, try this over adb: Access the device shell 
[code] 
       $ adb shell
    
[/code]
Get a list of input devices (/dev/input/event0, /dev/input/event1 etc) and events. ^C to stop this process 
[code] 
       # getevent
    
[/code]
Try this for some and compare with the information on [Touchscreen][47268] to identify your touchscreen 
[code] 
       # getevent -i /dev/input/eventX
    
[/code]
### Identify using the chips from PCB
It is sometimes possible to identify the touchscreen driver by searching the web for some alphanumeric codes that are [printed on the chip][47269] near the touchscreen cable. 
## cameras, accelerometers, gps, rtc and other miscellaneous devices
Linux has suport for many of these devices. However, not many people care about them working or not so far.
