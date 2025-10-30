# LiveSuit images
## Contents
  * [1 Overview][32840]
  * [2 Software][32841]
    * [2.1 Allwinner pack tools (mix of Linux & Windows tools)][32842]
      * [2.1.1 bin][32843]
      * [2.1.2 Pack][32844]
      * [2.1.3 Tools][32845]
    * [2.2 How to pack a LiveSuit image (A20 example)][32846]
      * [2.2.1 sunxi-BSP][32847]
      * [2.2.2 Allwinner Android SDK][32848]
    * [2.3 Linux][32849]
      * [2.3.1 RedScorpio tools][32850]
      * [2.3.2 awutils][32851]
    * [2.4 Windows][32852]
      * [2.4.1 RedScorpio tools][32853]
      * [2.4.2 esxgx][32854]

# Overview
All sunxi devices use [LiveSuit][32855] as a default flasher and updater for retail customer and [PhoenixCard][32856] or PhoenixUSB for flashing when devices are manufactured. [LiveSuit][32855]/Phoenix protocol and data are closed-source standard used by many companies and devices. To decrypt/unpack firmware you need unpacker and 3 keys. These keys are same across all sunxi devices and can be different on other brands (SoChip, Rockchip and others). Keys are usually shipped with firmware as .key file. 
# Software
## Allwinner pack tools (mix of Linux & Windows tools)
    To pack a LiveSuit image under linux, you need to pack tool from <https://github.com/matson-hall/allwinner-pack-tools>
    Note: you need to check out the cubieboard branch (master branch does not have anything there), so do:
[code] 
    git clone <https://github.com/matson-hall/allwinner-pack-tools.git> -b cubieboard
    
[/code]
This pack tools, contain 3 folders, most are to be used on x86 Linux or Windows platform. 
### bin
  * build.sh (linux bash script): script for building root, uboot, linux kernel and _pack_ them.
  * mkbootimg (x86 linux binary): Generate a boot image after a kernel file, a ramdisk image, eventually à second bootloader image and some other informations.

### Pack
  * chips folder: contains some configs fex, eGon (boot0.bin & boot1.bin for NAND, sdcard and spinor), eFex (some fex and axf), wboot (some scripts and assets for bootfs)
  * pack (linux bash script): The pack tools for linux firmware
  * pctools folder: contains Windows and Linux tools. (eDragonEx, gen_check_code. mod_update, fsbuild200).

### Tools
The subfolder Documentations contain a simplified chinese manual of the tools. 
After the README.txt, tools subdir content : 
  * _Livesuit_ : Flashing tool
  * _LogGen_ : Android logo generation tool
  * _PhoenixCard_ : mass production tool (?)
  * _PlatformTools_ : adb tools.
  * _USBDriver_ : adb/mtp driver
  * _FastbootWin32_ : Fastboot tool
  * _AndroidModify_xx_ : firmware modification tool (for Android 4.0.x)
  * _OEMDataPacket_xx_ : Write files in user data area.
  * _HerculesV100_ : PC part of the Fastboot tool

## How to pack a LiveSuit image (A20 example)
    This section is WiP and not yet complete!
    There are several ways to build a functional LiveSuit image which are presented in the following sections.
### sunxi-BSP
    Even though it contains sys_config.fex files for several A20 boards, sunxi-BSP set of tools is not able to produce functional LiveSuit image for A20 since the proprietary Allwinner binary tools are too old. One example is that update_mbr tool is not able to produce partitions with the "new" softw411 magic, needed by A20's NAND driver.
### Allwinner Android SDK
    Tools found in Android SDK for A20 provided by Allwinner are generally able to produce valid LiveSuit images for A20. However, the pack scripts seem to be broken on several places and need some moderate modifications to properly work. It is also worth to note that there are several Android SDKs for A20, all featuring slightly different set of binary tools and build/pack scripts.
    In order to build a functional image, download the following Android SDK and unpack it:
    <http://dl.linux-sunxi.org/SDK/A20/A20_SDK_20130319.tar.gz>
    You will need only the _boot/_ and _tools/_ folders, since u-boot and linux 3.3 are long ago deprecated and buildroot scripts are too old to be of any real use. This is where the first obstacle is - there are duplicated pack scripts and tool sets - under tools/pack and under boot/pack. We will only use the ones from /boot/pack. The boot/pack contains the following:
  * chips: This is where all the configuration files for boards/chips/download are
  * pctools: Set of Allwinner binary tools for building a LiveSuit image
  * pack: Script used for packing the image (broken on several places)

## Linux
### RedScorpio tools
    Only closedsource binary version is available at the moment.
    **Note** : this unpacker/packer works with PhoenixSuit images too.
    Download: [http://forum.xda-developers.com/showpost.php?p=28329544&postcount=1][32857] (package includes both windows and linux versions)
### [awutils][32858]
    Open source toolset
    <https://github.com/Ithamar/awutils>
## Windows
### RedScorpio tools
    **Possiple virus warning! File: imgrepacker.exe**
    RedScorpio tools are two utilities: imagerepacker, which unpacks, decrypts and packs back firmwares and imgdecoder for SoChip images, that have slightly different layout.
    Download: [http://forum.xda-developers.com/showpost.php?p=28329544&postcount=1][32857] (package includes both windows and linux versions)
    **Note** : this unpacker/packer works with PhoenixSuit images too.
    usage is:
    unpack image and decrypt:
[code] 
    imgrepacker.exe image.img
    
[/code]
    repack image:
[code] 
    imgrepacker.exe image.img.dump
    
[/code]
    Here is standard output from imgrepacker.exe unpacking official [LY-F1][32859] firmware:
[code] 
    ==========================[ START ]==========================
           
            --- Firmware unpacking ---
           
            File "F1中性20120529.0.6.5-a721_v4.2.img"     was read
           
            BasePath.txt saved
           
            - image.cfg creating -
            image.cfg created
           
            - Files extracting -
            "out/sys_config.fex"            extracted
            "out/sys_config1.fex"           extracted
            "out/split_xxxx.fex"            extracted
            "out/bootloader.fex"            extracted
                    bootloader.fex.iso              created
            "out/env.fex"           extracted
                    env.fex.iso             created
            "out/boot.fex"          extracted
                    boot.fex.iso            created
            "out/system.fex"                extracted
                    system.fex.iso          created
            "out/recovery.fex"              extracted
                    recovery.fex.iso                created
            "out/oem.fex"           extracted
                    oem.fex.iso             created
            "out/diskfs.fex"                extracted
                    diskfs.fex.iso          created
            "out/vbootloader.fex"           extracted
            "out/venv.fex"          extracted
            "out/vboot.fex"         extracted
            "out/vsystem.fex"               extracted
            "out/vrecovery.fex"             extracted
            "out/voem.fex"          extracted
            "out/boot0.bin"         decrypted
            "out/boot1.bin"         decrypted
            "eFex//usb//tools.fex"          extracted
            "eFex//usb//fes_1-1.fex"                extracted
            "eFex//usb//fes_1-2.fex"                extracted
            "eFex//usb//fes_2.fex"          extracted
            "eFex//usb//fes.fex"            extracted
            "eFex//usb//HW_scan.axf"                decrypted
            "eFex//usb//update_boot0.axf"           decrypted
            "eFex//usb//update_boot1.axf"           decrypted
            "eFex//usb//fet_restore.axf"            decrypted
            "eFex//usb//magic_cr_start.fex"         extracted
            "eFex//usb//magic_cr_end.fex"           extracted
            "eFex//usb//magic_de_start.fex"         extracted
            "eFex//usb//magic_de_end.fex"           extracted
            "eFex//usb//fed_nand.axf"               decrypted
            "eFex//card//cardtool.fex"              extracted
            "eFex//card//cardscript.fex"            extracted
            "out/card_boot0.fex"            extracted
            "out/card_boot1.fex"            extracted
            "out/mbr.fex"           extracted
            "out/dlinfo.fex"                extracted
            "eFex//usb//card_update_boot0.axf"              decrypted
            "eFex//usb//card_update_boot1.axf"              decrypted
            "eFex//usb//fed_card.axf"               decrypted
            "eFex//usb//card_HW_scan.axf"           decrypted
           
            - Filelist.txt creating -
            Filelist.txt created
           
            ==========================[ STOP  ]==========================
    
[/code]
    How you can see, unpacker creates .fex files for partitions, sys_config and eFex, which is hardware flasher (you can see eFex ASCII logo if you connect UART to UART0 port).
    List of extracted data is in Filelist.txt, this file will be read if you want to repack image back to firmware after modifying.
### esxgx
    **Virus warning! (Gen:Trojan:RP.oqWbau67ogl) File: unimg.exe**
    Also known as unimg.exe. Unpacker/Packer from esxgx <http://forum.xda-developers.com/member.php?u=4494128>, shipped with AllWinner image package, SztupY A10 android kitchen <http://forum.xda-developers.com/showthread.php?t=1490886> and other kitchens. Default used by XDA sunxi guys.
    This is closed-source flasher without any documentation, this flasher creates weird file names like 12345678_1234567890script.fex and can crash on every wrong move, but you can use it if you just want to repack android for sunxi tablet.
    The following text describes the result from unpacking an Android ICS image.
    It is interpreted with the help from this thread:
    <http://www.slatedroid.com/topic/28942-50-to-the-first-person-to-figure-this-out/>
[code] 
    
    The Vxxxxxxxx files are for verification purposes. Note that filenames contain spaces the notation is like: "<Type>     <Name>"
    
    
    COMMON   	SYS_CONFIG000000						
    COMMON   	SYS_CONFIG100000
    
    Text file used as a command bunch for LiveSuit. It tells the app how to flash, what to flash and where, and it configures the device too (screen size, ram info, cpu info, etc).
    SYS_CONFIG1 is the old one.
    
    
    COMMON   	SPLIT_0000000000 
    
    Same content as magic.bin from the bootloader (nanda)
    
    
    RFSFAT16 	BOOTLOADER_00000.fex
    
    FAT16 image containing the u-boot binary. Use MagicISO (or any other ISO managing app) to open.
    In Linux do:
    sudo mount -o loop -t vfat RFSFAT16_BOOTLOADER_00000.fex bootloader
     
    
    RFSFAT16 	ENVIROMENT_00000
    
    u-boot's boot parameters, DO NOT MODIFY
    
    
    RFSFAT16 	BOOT_00000000000
    
    Standard Android boot image (boot.img) (2K header,gzipped kernel, initrd gzipped cpio archive, optional second stage loader is not present)
    More to read here:
    http://forum.xda-developers.com/showthread.php?t=443994
    
    
    RFSFAT16	SYSTEM_000000000.fex
    
    Standard Android sparse ext4 image with the /system file structure.(system.img)
    Use simg2img to make it into an ext4 image that can be loop mounted!
    
    
    RFSFAT16 	RECOVERY_0000000
    
    Sparse ext4 containing a standard Android recovery image.
    Use simg2img to make it into an ext4 image that can be loop mounted!
    
    
    RFSFAT16 	DISKFS_000000000
    
    ext4 image containing the the initram (init.rc, default.prop, initlogo, etc), it is empty in this example.
    
    
    
    BOOT     	BOOT0_0000000000 
    BOOT     	BOOT1_0000000000
    
    These are bootloaders to be put in nand. Boot0 is the SPL - Second Program Loader (sun4i-spl.bin when uboot is built from source)
    Boot1 is the U-boot!
    
    
    PXTOOLS  	xxxxxxxxxxxxxxxx
    This is a win32 DLL!!! - seems maybe a plugin for Livesuit
    
    FES      		FES_1-1000000000 
    FES      		FES_1-2000000000
    FES      		FES_200000000000 
    FES      		FES_000000000000
    Note: test that FES is actually FEL mode boot0/boot1/u-boot
    FET      		HW_SCAN_00000000 
    FET      		UPDATE_BOOT0_000 
    FET     		UPDATE_BOOT1_000 
    FET     		FET_RESTORE_0000 
    FET      		MAGIC_CRC_START_ 
    FET      		MAGIC_CRC_EN_000 
    FET      		MAGIC_DE_START_0
    FET      		MAGIC_DE_END_000 
    FED     		FED_NAND_0000000 
    FET      		CARD_UPDATE_BOT0 
    FET      		CARD_UPDATE_BOT1
    FED      		CARD_FED_0000000 
    FET      		CARD_HW_SCAN_000 
    
    
    These are tools are NAND flashing utilities, checksums, hardware scanner, and other tools used during flashing.
    
    
    12345678 	1234567890cardtl 
    12345678 	1234567890script 
    12345678 	1234567890boot_0 
    12345678 	1234567890boot_1
    2345678 	1234567890___mbr 
    12345678 	1234567890dlinfo 
    
    These are bootloaders, config files, and tools for SDMMC flashing, if there's a device with SDMMC internal instead of NAND, these are used!
    
    
[/code]
