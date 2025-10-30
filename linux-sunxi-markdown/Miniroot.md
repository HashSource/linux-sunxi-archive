# Miniroot
miniroot is a small busybox based system, meant to be used as an initramfs. 
## Obtaining miniroot
[code] 
       git clone <https://github.com/hno/miniroot.git>
    
[/code]
## Building
First build your kernel and install kernel modules at a suitable place. 
[code] 
       cd linux-sunxi
       make ... LOADADDR=0x40008000 INSTALL_MOD_PATH=/some/suitable/path uImage modules modules_install
    
[/code]
Then build miniroot by 
[code] 
       cd miniroot
       make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- KERNEL_MODULES=/path/to/kernel/INSTALL_MOD_PATH
    
[/code]
This produces an initramfs u-boot image suitable for use in for example [USB booting][38170]
