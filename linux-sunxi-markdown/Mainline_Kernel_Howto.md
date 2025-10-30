# Mainline Kernel Howto
This page describes how you can compile and use the Linux mainline kernel. 
Warning: Mainline NAND support is not compatible with Allwinner NAND support and will make your existing NAND unreadable. 
## Contents
  * [1 Current status][33870]
  * [2 Prerequisites][33871]
  * [3 Kernel source][33872]
    * [3.1 Linus' tree][33873]
    * [3.2 Patches merged in the next stable release][33874]
  * [4 Kernel Configuration][33875]
    * [4.1 defconfig][33876]
    * [4.2 oldconfig][33877]
    * [4.3 manual configuration][33878]
  * [5 Kernel Compilation][33879]
    * [5.1 zImage/ Image][33880]
    * [5.2 Devicetree][33881]
    * [5.3 modules][33882]
    * [5.4 headers][33883]
    * [5.5 Specific Debian kernel notes][33884]
  * [6 Boot][33885]
    * [6.1 SD-Card Boot partition][33886]
      * [6.1.1 boot.cmd][33887]
    * [6.2 eMMC boot partition][33888]
    * [6.3 Network boot setup][33889]
  * [7 Extra features][33890]
    * [7.1 IPv6][33891]
    * [7.2 SYSV IPC (debian users!)][33892]
    * [7.3 Early printk][33893]
    * [7.4 simplefb][33894]
  * [8 Adding a new device][33895]
  * [9 See also][33896]

# Current status
Please refer to the [Linux mainlining effort][33897] page for detailed status of the mainlining effort, and supported boards and driver coverage. 
Some SoCs and some subsystems might not be supported yet, you might need to revert to our [heavily hacked kernel version][33898] that's close to Allwinners code for A10/A13/A20, or use a BSP kernel. 
# Prerequisites
You should be running through this howto as part of our [Manual build howto][33899]. It guides you through toolchain, u-boot and rootfs steps as well. 
# Kernel source
## Linus' tree
The stable releases are released by Linus Torvalds. Since Linux 3.8, the Allwinner support is added gradually. 
For a full clone (if you wish to do future development) run: 
[code] 
    git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
[/code]
Often a shallow clone will suffice to just get mainline working: 
[code] 
    git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git --depth=1
[/code]
## Patches merged in the next stable release
There is also a _sunxi-next_ branch maintained with all the inclusions that have been accepted, merged and will be included in the next stable release. If you want to do some development, it's probably the best pick. 
[code] 
    git clone [http://github.com/linux-sunxi/linux-sunxi/tree/sunxi-next git://github.com/linux-sunxi/linux-sunxi.git] -b sunxi-next --depth=1
[/code]
# Kernel Configuration
## defconfig
To get a working kernel, just use the following for configuration: 
**armhf**
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- sunxi_defconfig
[/code]
**arm64**
[code] 
    ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- make defconfig
[/code]
## oldconfig
If you have an old relevant .config, e.g. if you installed a late debian, and now want to build the kernel, you can copy it in and run `make ARCH=arm oldconfig` or `make ARCH=arm64 oldconfig`. 
    [![Sticky-note-pin.png][33900]][33901] _Note:_ If you happen to run `make menuconfig` without specifying the architecture, architecture-specific options will be **lost** ; in that case you'll need to go back to an existing config and start again.
## manual configuration
If you wish to alter configuration, run: 
**armhf**
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig
[/code]
**arm64**
[code] 
    ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- make menuconfig
[/code]
# Kernel Compilation
## zImage/ Image
**armhf**
[code] 
    ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- make -j4 zImage
[/code]
**arm64**
[code] 
    ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- make -j4 Image
[/code]
After the compilation ended, you should have generated **zImage** in _arch/arm/boot_ (armhf) or **Image** in _arch/arm64/boot_ (arm64). 
## Devicetree
**armhf**
[code] 
    ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- make -j4 dtbs
[/code]
**arm64**
[code] 
    ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- make -j4 dtbs
[/code]
You should now have a device tree binary (_.dtb_) in _arch/arm/boot/dts_ (armhf) or _arch/arm64/boot/dts_ (arm64), which matches your device, it should be listed on the device page for your device. 
All the sunxi dtbs follow the pattern <family>-<soc>-<board>.dtb. 
## modules
**armhf**
[code] 
    ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- make -j4 modules
    ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=<any-path-you-like> make modules modules_install
[/code]
**arm64**
[code] 
    ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- make -j4 modules
    ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- INSTALL_MOD_PATH=<any-path-you-like> make modules modules_install
[/code]
After the build succeeds, you can find the modules in the supplied `INSTALL_MOD_PATH` directory. 
## headers
**armhf**
[code] 
    ARCH=arm INSTALL_HDR_PATH=<any-path-you-like> make headers_install
[/code]
**arm64**
[code] 
    ARCH=arm64 INSTALL_HDR_PATH=<any-path-you-like> make headers_install
[/code]
Change `INSTALL_HDR_PATH` to the path, you want the headers to be installed to, for example `/usr` or `<some_prefix>/usr` if you are doing a cross build. 
## Specific Debian kernel notes
Having installed a late debian using the arm installer, building the Debian kernel is an attractive proposition. (for Debian install, see [Rikomagic_mk802][33902] 'Images' section). 
Some notes on doing so (as it's not so obvious from Google): You can download the sources using apt-get linux-source. Today, Dec 2016, this will get you ~4.8.7. Given sufficient space, this can be built on device (~4 days compile time), but probably better to cross-compile. Extract the tar to a suitable location, and copy /boot/config-<your current version> to .config. You may want to edit the .config comment out CONFIG_MODULE_SIG_FORCE and CONFIG_MODULE_SIG. Prepare your cross machine, and then run 
`make ARCH=arm oldconfig`
(you may get some new options). 
Now, the important bit. IF 'uname -a' on your target shows 'armmp' anywhere, your kernel will need to be this 'flavor'; if it is not, then your newly created .deb kernel package will not install on the device..... So, to stamp it as flavor 'armmp': 
Create a file called 'localversion' in the linux-source directory, and put -armmp inside. This will then generate a kernel stamped with the version '4.8.7-armmp' rather than plain '4.8.7', and will make dpkg/flash-kernel happy on install. 
Then, to make the kernel, use; substituting your cross compiler;: 
`make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- deb-pkg`
Note: if you want to build, but not start from scratch, the target bindeb-pkg does not do a clean first, whereas deb-pkg does. 
You should end up with a file in one folder lower called something like `linux-image-4.8.7-armmp_4.8.7-armmp-3_armhf.deb`
To install this on the device, go to that folder, or copy it to the device, and use 
`dpkg -i linux-image-4.8.7-armmp_4.8.7-armmp-3_armhf.deb`
and if successful, reboot... 
  
Note from the author of this last bit: I'm no expert on this, but as it took me over a week to establish the above; I hope it helps somebody! Please feel free to enhance or correct any of the above. **If you do intend to reproduce this, then please make notes as you do it; a good (accurate) from scratch description would be a bonus here.**
# Boot
## SD-Card Boot partition
Like with our [ Manual build howto][33903], you have to set up the boot partition. Instead of _script.bin_ , you need to install your board-specific **.dtb** to the boot partition. (Above kernel compilation should generate this binary representation of the [device tree][33904] automatically.) 
### boot.cmd
Like in the [ Manual build howto][33905], create a boot.cmd with the following contents: 
[code] 
    fatload mmc 0 0x46000000 zImage
    fatload mmc 0 0x49000000 <board>.dtb
    
    setenv bootargs console=ttyS0,115200 earlyprintk root=/dev/mmcblk0p<partition> rootwait panic=10 ${extra}
    
    bootz 0x46000000 - 0x49000000
[/code]
    [![Sticky-note-pin.png][33900]][33901] _Note:_ In order to boot an **arm64** kernel, remember to use _Image_ instead of _zImage_. You also have to load it with _booti_ instead of _bootz_. So you have to adopt the corresponding lines in the above boot.cmd file.
Replace _fatload_ with _ext2load_ if needed. [earlyprintk][33893] is optional; if your kernel boots up just fine, you might as well remove it. 
If you are using an older U-Boot (you shouldn't - Which?), you might require the following line, to keep the extracted kernel from overwriting the device tree configuration: 
[code] 
    setenv fdt_high ffffffff
[/code]
If you wish to use an initramfs, then the _bootz_ command becomes: 
[code] 
    bootz 0x46000000 0x<initramfs-address> 0x49000000
[/code]
Now [generate boot.scr][33906]. Don't forget to copy over your _zImage_ and <board>.dtb files as well. 
## eMMC boot partition
[eMMC][33907] is very similar to the SD card case (see above). From a user's perspective, think of it as an "internal" memory card. Some devices are able to boot entirely from eMMC, forgoing the need for an external SD card. 
[![Information.png][33908]][33909] Keep a keen eye on the numbering of the _mmcblk_ devices when switching the boot process between SD card and eMMC, e.g. during installation. 
    The Linux kernel may change device numbers depending on which mmc devices are actually present.
    For example: If your SD card corresponds to _mmc0_ , and the eMMC is _mmc1_ , you'll probably end up with the eMMC as _mmcblk**1**_ when a SD card is also present (with the latter being _mmcblk**0**_). But it's likely that the eMMC becomes _mmcblk**0**_ as soon as no SD card (_mmc0_) is present. If in doubt, check the kernel messages and adjust your partition layout / boot options accordingly.
## Network boot setup
TODO. Fold in [Possible setups for hacking on mainline][33910]. 
# Extra features
## IPv6
In this day and age, you might want to use IPv6 as well. It is missing from the armhf defconfig. 
The config text file top level option is called **CONFIG_IPV6**
You can find this in _menuconfig_ under: 
[code] 
    [*] Networking support   --->
         Networking options  --->
         < >   The IPv6 protocol  --->
[/code]
## SYSV IPC (debian users!)
The current sunxi_defconfig has actually become rather complete, but SYSV IPC is disabled, and it is important for the fakeroot tool which is used for making debian packages. 
Go to: 
[code] 
        General setup  --->
[/code]
Then enable **CONFIG_SYSVIPC** : 
[code] 
    [*] System V IPC
[/code]
## Early printk
If and only if your kernel does nothing, it pays to enable early printk support. 
Go to: 
[code] 
        Kernel hacking  --->
[/code]
Then enable **CONFIG_DEBUG_KERNEL** : 
[code] 
    [*] Kernel debugging
[/code]
To actually get early printk, you need to also enable **CONFIG_DEBUG_LL** , select one of the **CONFIG_DEBUG_SUNXI_** options, and enable **CONFIG_EARLY_PRINTK** : Inside arm debugging: 
[code] 
    [*] Kernel low-level debugging functions (read help!)
          Kernel low-level debugging port (Kernel low-level debugging messages via sunXi UART0)  --->
    [*] Early printk
[/code]
The selection of the debugging port (**CONFIG_DEBUG_SUNXI_**) depends on the board you are using. The selection of these is this contrived as these are all symbolic names for the raw addresses for the debug port. 
  * For most SoCs, you should first select **DEBUG_SUNXI_UART0** :
[code](X) Kernel low-level debugging messages via sunXi UART0
[/code]
  * For A13, try **DEBUG_SUNXI_UART1** first:
[code](X) Kernel low-level debugging messages via sunXi UART1
[/code]
  * For A23, try **DEBUG_SUNXI_R_UART** first:
[code](X) Kernel low-level debugging messages via sunXi R_UART
[/code]
  * For A80, try **DEBUG_SUN9I_UART0** first:
[code](X) Kernel low-level debugging messages via sun9i UART0
[/code]

## simplefb
TODO: This is now part of defconfig anyway. Be sure to add the console command line option to the console/display support page.
Don't forget to change your console in your boot.cmd/boot.scr to console=tty1 to enable the simple framebuffer driver. 
# Adding a new device
Mainly, you have to write a [device description][33911]. Please [send a patch][33912] to help others finding good examples. 
# See also
  * [Manual build howto][33899]
  * [Linux mainlining effort][33897]
  * [Possible setups for hacking on mainline][33910]
