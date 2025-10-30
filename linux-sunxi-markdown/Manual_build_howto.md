# Manual build howto
This page describes the process to combine sunxi U-Boot, linux kernel and other bits together to create a useful SD-card from scratch, the basis for further hacking. 
This page is only suited for [A10][35228], [A13][35229]/[A10s][35230] and [A20][35231] based devices. [The manual build howtos for other SoCs are at the end of this page.][35232]
We of course do not build a whole distribution, we only build U-Boot, the kernel and a handful of tools, and then use an existing rootfs to get a useful system. Depending on the rootfs size, you might want to use a 2GB or larger SD Card. SD-card partitioning and formatting will be taken care of later. 
## Contents
  * [1 Get a cross toolchain][35233]
  * [2 Build U-Boot][35234]
    * [2.1 Sunxi/Legacy U-Boot][35235]
    * [2.2 Upstream/Mainline U-Boot][35236]
  * [3 Build the kernel][35237]
    * [3.1 Sunxi/Legacy kernel][35238]
      * [3.1.1 Build script.bin][35239]
      * [3.1.2 Build the actual kernel][35240]
    * [3.2 Upstream/Mainline kernel][35241]
  * [4 Set up SD-Card for booting][35242]
    * [4.1 Clean SD-Card][35243]
    * [4.2 Partition SD-Card][35244]
    * [4.3 Install Bootloader to the SD-Card][35245]
    * [4.4 Mount your boot or root partition][35246]
    * [4.5 Install bootloader configuration][35247]
    * [4.6 Install kernel binary][35248]
    * [4.7 Install board description][35249]
      * [4.7.1 script.bin (for sunxi kernel)][35250]
      * [4.7.2 device tree binary (for upstream kernel)][35251]
    * [4.8 Unmount your boot or root partition][35252]
  * [5 Setting up the rootfs][35253]
    * [5.1 Install kernel modules][35254]
  * [6 Boot!][35255]
  * [7 See also][35232]

# Get a cross toolchain
For this part, you need to refer to our [ toolchain page][35256]. 
To build the kernel you may need some additional packages: 
[code] 
    apt-get install flex bison
[/code]
# Build U-Boot
## Sunxi/Legacy U-Boot
Please refer to [Compile U-Boot][35257]. When the build has completed, there will be _spl/sunxi-spl.bin_ and _u-boot.img_ available in your U-Boot tree. 
The installation to SD card is covered in [Bootable_SD_card#Bootloader][35258]. 
## Upstream/Mainline U-Boot
If your device is [supported by upstream/mainline U-Boot][35259], you should probably use that instead. 
Follow [these instructions][35260] to create _u-boot-sunxi-with-spl.bin_. 
If you intend to boot older 3.4.x kernels with mainline U-Boot, make sure you also understand its [boot configuration][35261]. Some information presented on this page needs to be adjusted accordingly - especially **bootm_boot_mode** could be important in that case.
# Build the kernel
## Sunxi/Legacy kernel
### Build script.bin
The sunxi kernel depends on Allwinners own hardware description file, called [script.bin][35262], which needs to be loaded into memory by the bootloader so that the kernel can access it. 
To build _script.bin_ follow our [guide to building script.bin][35263]. 
### Build the actual kernel
Please refer to [ our Kernel compilation guide][35264]. 
## Upstream/Mainline kernel
Please refer to [ our upstream kernel howto][35265]. 
Remember to also build the device tree binaries. 
# Set up SD-Card for booting
## Clean SD-Card
Refer to [our SD-Card cleaning howto][35266]. 
## Partition SD-Card
Refer to [our SD-Card partitioning howto][35267]. 
## Install Bootloader to the SD-Card
Refer to [our SD-Card bootloader installation howto][35258]. 
## Mount your boot or root partition
Mount your boot or root partition again: 
[code] 
    mount /dev/${card}1 /mnt
    
[/code]
## Install bootloader configuration
Follow instructions to set up either mainline or legacy sunxi U-Boot: 
  * [mainline U-Boot][35261]
  * [legacy U-Boot][35268]

## Install kernel binary
Now you can install your built kernel into the boot partition: 
[code] 
    cp /home/user/dir/linux-sunxi/arch/arm/boot/uImage /mnt
[/code]
## Install board description
### script.bin (for sunxi kernel)
If you are using the sunxi kernel, you need to install [ _script.bin_][35269] to the boot partition: 
[code] 
    cp /home/user/dir/sunxi-boards/sys_config/aXX/script.bin /mnt
[/code]
### device tree binary (for upstream kernel)
If you are using the upstream/mainline kernel, you need to install the compiled [device tree][35270] into the boot partition as well. 
[code] 
    cp /home/user/dir/linux/arch/arm/boot/dtbs/<your_board>.dtb /mnt
[/code]
(assuming your kernel sources are in _/home/user/dir/linux_) 
You can find available compiled trees by listing kernel directory _arch/arm/boot/dts/_
[code] 
    ls /home/user/dir/linux/arch/arm/boot/dts/*.dtb
[/code]
What trees get compiled during kernel compilation depend on what you selected in "System Type" menuconfig during kernel configuration. However you can [compile any tree][35271] without recompiling kernel. 
By default U-Boot boots with a tree, specified with [U-Boot config option][35272] CONFIG_DEFAULT_DEVICE_TREE=<your_board>
## Unmount your boot or root partition
Unmount the partition again. 
[code] 
    umount /mnt
[/code]
# Setting up the rootfs
Please refer to [Bootable_SD_card#Rootfs][35273]
## Install kernel modules
As a last step you need to copy the kernel modules into the newly created rootfs. Change into the top level directory of the newly created rootfs and run: 
[code] 
    mount ${cardroot} /mnt
    mkdir -p /mnt/lib/modules
    rm -rf /mnt/lib/modules/
    cp -r <PATH_TO_KERNEL_TREE>/output/lib /mnt/
    umount /mnt
    
[/code]
(Replace <PATH_TO_KERNEL_TREE> with the directory you have built your kernel in as described [above][35274].) 
# Boot!
Now you should be able to unmount your SDCard filesystems, and you should be able to boot your brand new installation. 
# See also
We have Manual build howtos for all SoCs: 
[H3 Manual build howto][35275]
[Manual build howto][35276]
