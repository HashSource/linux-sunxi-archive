# U-Boot/Tools
< [U-Boot][56563]
 
## Contents
  * [1 Installing the U-Boot tools][56566]
    * [1.1 On openSUSE][56567]
    * [1.2 Installing on Arch Linux][56568]
    * [1.3 Installing on Gentoo Linux][56569]
    * [1.4 Installing on Fedora Linux][56570]
  * [2 Tool documentation][56571]
    * [2.1 dumpimage][56572]
    * [2.2 fw_printenv][56573]
    * [2.3 fw_setenv][56574]
    * [2.4 img2srec][56575]
    * [2.5 jtagconsole][56576]
    * [2.6 mkenvimage][56577]
    * [2.7 mkimage][56578]
    * [2.8 ncb][56579]
    * [2.9 netconsole][56580]

# Installing the U-Boot tools
## On openSUSE
[code] 
    zypper install u-boot-tools
[/code]
## Installing on Arch Linux
[code] 
    pacman -S uboot-tools
[/code]
## Installing on Gentoo Linux
[code] 
    emerge u-boot-tools
[/code]
## Installing on Fedora Linux
[code] 
    dnf install uboot-tools
[/code]
# Tool documentation
## dumpimage
## fw_printenv
## fw_setenv
## img2srec
## jtagconsole
## mkenvimage
The mkenvimage tool takes a key=value input file (same as would a `printenv' show) and generates the corresponding environment image, ready to be flashed. See this article for more details: <https://bootlin.com/blog/mkenvimage-uboot-binary-env-generator/>
## mkimage
The mkimage command is used to create images for use with the U-Boot boot loader. Thes eimages can contain the linux kernel, device tree blob, root file system image, firmware images etc., either separate or combined. 
The [U-Boot article][56581] describes how to create a _boot.scr_ from a _boot.cmd_ file. The [Initial Ramdisk][56582] article is used to convert an initramfs into a uInitrd. 
  

## ncb
## netconsole
