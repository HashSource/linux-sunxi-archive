# Fastboot
## Contents
  * [1 Using fastboot on sunxi devices][19246]
    * [1.1 Prerequisites][19247]
    * [1.2 Getting your device into Fastboot mode][19248]
    * [1.3 Preparing the device for flashing][19249]
    * [1.4 Flashing the device][19250]
  * [2 See also][19251]

# Using fastboot on sunxi devices
Fastboot is a diagnostic protocol, primarily used to modify the filesystems on the flash device via USB or UDP. It requires that the device is started in a boot loader or Secondary Boot Loader mode. 
This document currently walks through an installation with a device with eMMC storage. 
## Prerequisites
  * fastboot binaries installed on client machine
  * sunxi-tools installed on client machine (optional)
  * u-boot tools (mkimage)
  * u-boot binaries for the target sunxi device
  * filesystem images: 
    * root file system containing operating system
    * EFI partition (VFAT) for u-boot scripts
  * Sunxi device connected to client via OTG port

## Getting your device into Fastboot mode
To enter into fastboot mode, execute the `fastboot` command in U-Boot: 
[code] 
     fastboot usb 0
    
[/code]
On the client machine, you can check whether the device is visible using the `fastboot devices` command. And for fun, you can also fetch the bootloader version using the fastboot protocol: 
[code] 
     $ fastboot devices 
     1234567890abcdef	Android Fastboot
     $ fastboot getvar version-bootloader
     version-bootloader: U-Boot 2023.01-00003-g84563525cd
     Finished. Total time: 0.000s
    
[/code]
## Preparing the device for flashing
[![MBOX icon important.png][19252]][19253] | On some older devices booting directly from eMMC might fail due to BROM not supporting newer eMMC variants. To overcome this, some manufacturers are also populating the board with [SPI EEPROM for storing the SPL and u-boot][19254], so you do not have to populate **loader1/loader2** partitions.   
---|---  
Now that the device is in the fastboot mode, we can continue with creating the partitions on the device. By default, u-boot for sunxi defines following partitions: 
  * loader1 - partition for SPL - secondary program loader (not needed for [SPI-based bootloader][19254])
  * loader2 - partition for u-boot (not needed for SPI-based bootloader)
  * esp - EFI system partition (VFAT), for u-boot scripts (boot.scr)
  * system - Root partition for system

These partitions have also assigned GUID's according to [Discoverable Partitions Specification][19255], to enable automatic discovery of partitions and their mountpoints. 
You can start by formatting the internal storage by executing the `fastboot oem format` command from client: 
[code] 
     fastboot oem format
    
[/code]
This equivalent to running the `gpt write mmc 1 $partitions` from u-boot. 
## Flashing the device
Now that we have the partitions created, all that is left for us is to flash the data. 
`loader1` is used for storing the Secondary Program Loader, in our case, it is the `spl/sunxi-spl.bin` in the u-boot directory: 
[code] 
     fastboot flash loader1 spl/sunxi-spl.bin
    
[/code]
`loader2` is for storing the u-boot binary. Depending on architecture, it's either `u-boot.img` (for arm32) and `u-boot-sunxi-with-spl.fit.itb (for arm64) : 
[code] 
     fastboot flash loader2 <file..>
    
[/code]
`esp` partition (EFI System Partition) can be kept empty, although if it is VFAT partition, u-boot automatically looks up the `boot.scr` file for device-specific configuration. (You can create empty vfat partition by `fallocate -l 32M esp.img && mkfs.vfat esp.img`) 
[code] 
     fastboot flash esp esp.img
    
[/code]
`system` partition is where the operating system resides. Creating that is left as an exercise to the reader. 
[code] 
     fastboot flash system system.img
    
[/code]
Now, if everything has been properly set up (aka proper kernel with machine-specific dtb installed on system.img, and boot.scr on esp partition), you can reboot the machine: 
[code] 
     fastboot reboot
    
[/code]
# See also
  * [U-Boot USB Mass Storage Gadget][19256] as an alternative to getting system image into onboard storage
