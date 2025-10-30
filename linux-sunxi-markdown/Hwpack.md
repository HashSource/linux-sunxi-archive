# Hwpack
"hwpack" means a "**hardware** -specific **pack** age". 
## Contents
  * [1 Download][24391]
  * [2 Installation][24392]
  * [3 Advanced][24393]
    * [3.1 Extracting][24394]
      * [3.1.1 Contents][24395]
      * [3.1.2 Updating an SD-card with u-boot from a hwpack][24396]

## Download
Latest hwpacks for various Allwinner devices are available from: 
  * **<http://dl.linux-sunxi.org/amery/sunxi-3.0/latest/>**

You can also create a new hwpack by using [sunxi-bsp][24397] tools. 
## Installation
Please refer to [BSP][24397] guide for hwpack automatic installation. 
## Advanced
### Extracting
You can extract the downloaded hwpack file by running: 
[code] 
    tar -xf *_hwpack.tar.xz
[/code]
#### Contents
After unpacking you will have three directories: 
  * **bootloader** : contains sunxi-spl and u-boot;
  * **kernel** : contains kernel uImage and [script.bin][24398];
  * **rootfs** : contains some configuration files and kernel modules.

#### Updating an SD-card with u-boot from a hwpack
u-boot consists of two files in the **bootloader** directory: 
  * **sunxi-spl.bin**
  * **u-boot.bin**

You need to write them into fixed areas of your SD-card: 
[code] 
    dd if=sunxi-spl.bin of=/dev/sdX bs=1024 seek=8
    dd if=u-boot.bin of=/dev/sdX bs=1024 seek=32
[/code]
...where /dev/sdX is your SD card (make sure you use the correct device name here). 
If you do this on an already existing SD-card image you may also want to clear the u-boot environment area, to remove any old settings that may have been saved there and return to the (very reasonable) u-boot defaults: 
[code] 
    dd if=/dev/zero of=/dev/sdX bs=1024 seek=544 count=128
[/code]
