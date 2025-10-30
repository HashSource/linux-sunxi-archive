# Initial Ramdisk
To use an initial ramdisk (initramfs/initrd) on sunxi, for example if you have modular sata support and your root filesystem on sata, you need to use mkimage to convert your regular initial ramdisk to U-Boot's format and adjust your U-Boot configuration. 
To convert an initial ramdisk to U-Boot's format: 
[code] 
    mkimage -A arm -T ramdisk -C none -n uInitrd -d /path/to/initrd.img /path/to/uInitrd
    
[/code]
In the U-Boot configuration you will want to load the uInitrd file and add it's address to bootm. 
  * For a fex/script.bin kernel (e.g. sunxi's 3.0 or 3.4) you might use:

[code] 
    fatload mmc 0 0x43000000 script.bin
    fatload mmc 0 0x41000000 uImage
    fatload mmc 0 0x50000000 uInitrd
    bootm 0x41000000 0x50000000
    
[/code]
uInitrd must not fall inside the range 0x43000000-0x4FFFFFF due to memory allocation conflicts. More details [here][27760]. 
(is it still valid? i'm loading kernel-3.4.113 at 0x48000000 and initrd at 0x47200000 and cma happily got reserved, 300MB at 0x4d400000) 
  * For a mainline/devicetree using kernel (e.g. sunxi-current or mainline 3.8+) you might use:

[code] 
    fatload mmc 0 0x43000000 board.dtb
    fatload mmc 0 0x41000000 uImage
    fatload mmc 0 0x45000000 uInitrd
    bootm 0x41000000 0x45000000 0x43000000
    
[/code]
For at least the cubieboard with the mainline/devicetree kernel you will also want to set initrd_high before calling bootm, such as: 
[code] 
    setenv initrd_high 0xffffffff
    
[/code]
If you are doing this to use a rootfs on sata, then you will need to ensure the initial ramdisk loads the sata module. On Debian using initramfs-tools you would do this simply by adding sw_ahci_platform to /etc/initramfs-tools/modules on a line on it's own. 
After any edits to /etc/initramfs-tools/modules you will need to update any initial ramdisk's you want to use it with a command such as (this will update the initramfs for all available kernels known to initramfs-tools): 
[code] 
    update-initramfs -u -k all
    
[/code]
It would also be a good idea to have the initial ramdisk load the display modules early so you can see the output, and interact with the shell, in case of any issues. You can add the following modules to /etc/initramfs-tools/modules in this order to do this (and again update the initial ramdisk): 
[code] 
    lcd
    hdmi
    ump
    disp
    mali
    mali_drm
    
[/code]
In the unusual circumstances where you need the initial ramdisk to access files from a fat partition then you would also want to add the relevant charset modules, such as nls_ascii and nls_cp437, to the list of modules loaded early in the initial ramdisk.
