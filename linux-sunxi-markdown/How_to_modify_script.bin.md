# How to modify script.bin
# General
This article describes how to modify the system configuration (i.e. script.bin) on a live system without re-flash the whole system. Similar topic has been discussed before (e.g. [here][24352]). The basic process is repeated below for the sake of completeness. 
When building, sunxi SDK will pack script.bin, along with u-boot image and some other stuff into a FAT parition. For a nand based system, it is at /dev/block/nanda. So just mount the parition and pull the file using adb 
[code] 
    $ adb shell
    $ mkdir /mnt/tmp
    $ mount -t vfat /dev/block/nanda /mnt/tmp
    $ exit
    $ adb pull /mnt/tmp/script.bin 
    
[/code]
Then use bin2fex and fex2bin from [sunxi-tools][24353] to decompile, modify, and then recompile the script.bin. After that, just push back the file and the new configuration is supposed to take effect on next boot. 
[code] 
    $ git clone git://github.com/linux-sunxi/sunxi-tools.git
    $ cd sunxi-tools
    $ make
    $ ./bin2fex script.bin > ./script.fex
    $
    $ # now edit the script.fex
    $
    $ ./fex2bin script.fex > ./script.bin
    $ adb push script.bin /mnt/tmp
    $ adb shell
    $ umount /mnt/tmp
    $ reboot
    
[/code]
# When the Above does not Work
The above process does not work on my ([User:Realthunder][24354]) [PhoenixA20][24355] board. I haven't tried other boards, so can't be sure, but I am guessing this is common to stock SDK based boards. It also did not work on a [Olimex_A20-OLinuXino-Lime2][24356] board. However, commenting out SCRIPT_INSTALL_EARLY and building boot0 allowed the method above to work on the Olimex_A20-OLinuXino-Lime2. 
According to the sunxi [Boot Process][24357], the stage one bootloader, boot0, is responsible for loading the stage two bootloader, which could either be boot1 from the stock SDK, or u-boot in the FAT parition. In my case, boot1 is used. And according to [SDK build howto#Manual Build of Separate Components][24358], the bootloader is packed with the binary system configuration during the build process. It is the bootloader's responsibility to load the system configuration to a specific memory position for kernel. It is usually at 0x43000000, but check your kernel header for sure. 
It turns out that boot1 in the stock A20 SDK is configured to load the packed system configuration instead of the script.bin in the FAT parition. To solve this, you can either, 
  * Each time you modify the system configuration, re-pack, and then flash boot1 only, if you know where it is located (hint: [SDK build howto#SD card][24359]), or
  * Add a u-boot script to load the script.bin as described [here][24360], if your board uses u-boot and it supports boot script, or
  * Modify boot1 by comment out the following line in lichee/boot/boot1/include/egon2.h file. After you make this change make sure that you are rebuilding boot1 (cd lichee/boot; make). Some build environments are setup to use precompiled versions of boot0 and boot1, therefore the code change below won't have any effect.

[code] 
     #define   SCRIPT_INSTALL_EARLY
    
[/code]
If your SDK does not come with source code of boot1, you can try your luck with [this repository][24361].
