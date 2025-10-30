# Device Tree
The Device Tree is a data structure for describing hardware. [ Mainline Linux][16619] uses it to activate and configure the drivers available in the kernel's binary (similar to [script.bin][16620] for _linux-sunxi_). [Mainline U-Boot][16621] is also migrating towards the device tree model. 
## Contents
  * [1 Sources for information][16622]
    * [1.1 Introduction][16623]
    * [1.2 Particular Drivers][16624]
    * [1.3 Complete Examples][16625]
  * [2 Writing a Device Tree][16626]
    * [2.1 Coding Style][16627]
  * [3 Get the Device-tree Compiler][16628]
    * [3.1 For Gentoo][16629]
    * [3.2 For openSUSE][16630]
    * [3.3 For Debian/Ubuntu][16631]
    * [3.4 For Arch][16632]
    * [3.5 For Windows 64][16633]
  * [4 Compiling the Device Tree][16634]
  * [5 Using the Device Tree][16635]
  * [6 Adding a new device][16636]

# Sources for information
## Introduction
For a general introduction on device trees see: 
  * [elinux.org summary on Device Tree][16637]
  * [Device tree for Dummies][16638] (PDF)
  * [DeviceTree.org][16639]

In a nut shell, the kernel uses properties of the form 
[code] 
    compatible = "<manufacturer>,<model>"
[/code]
to identify a driver and initialize it with the configuration additionally provided by more attributes or sub-section. 
## Particular Drivers
Every driver has its particular parameters, documented in: 
  * [Documentation/devicetree/bindings][16640]

## Complete Examples
Writing a device tree for your board, you might want to look at: 
  * [arch/arm/boot/dts][16641]

# Writing a Device Tree
It is good to start with an example of a device which is close to the one you're working on. Trim down the original device's dts to what your device actually provides. If your device came with a fex file, check settings like the gpio for enabling the usb vbus in the fex file and adjust them in the dts file as necessary. Finally, work on activating drivers particular to your device. Again parameters might be taken over from a fex file. 
## Coding Style
Recently, coding style moved over from using a full node hierarchy to using label references in board dts files, see e.g. : 
[https://git.kernel.org/cgit/linux/kernel/git/mripard/linux.git/commit/?h=sunxi/dt-for-3.20&id=327f121fea91fd79d6b71f47a8e1bc62a7fd86e5][16642]
Note that the nodes should be sorted alphabetically. 
# Get the Device-tree Compiler
This program is usually called _dtc_. You can retrieve a [standalone version][16643], or install a distribution-provided package (see below for some examples). 
## For Gentoo
[code] 
    emerge dtc
[/code]
## For openSUSE
[code] 
    zypper install dtc
[/code]
## For Debian/Ubuntu
[code] 
    apt-get install device-tree-compiler
[/code]
## For Arch
[code] 
    pacman -S dtc
[/code]
## For Windows 64
[code] 
     Download dtc-1.4.7-mingw64.zip:
[/code]
[dtc-1.4.7-mingw64.zip][16644]
# Compiling the Device Tree
Device tree sources in the kernel deviate from the regular syntax, by using the _cpp_ preprocessor for includes and substitution. This proceeds as follows: 
[code] 
    IDE=<your-device-name>
    SRC=$IDE.dts
    TMP=$IDE.tmp.dts
    DST=$IDE.dtb
    
    cpp -nostdinc -I include -undef -x assembler-with-cpp $SRC > $TMP
    dtc -O dtb -b 0 -o $DST $TMP
    rm $TMP
    
[/code]
[![Sticky-note-pin.png][16645]][16646] _Note:_ A quick way to rebuild the device tree blobs for any enabled board(s) is to use the command `make dtbs` from an already configured kernel source directory. 
# Using the Device Tree
To actually make the kernel use the device tree, see [Mainline_Kernel_Howto#Boot][16647]. 
# Adding a new device
Add your _< device>.dts_ file to `/arch/arm/boot/dts/` and include it to `/arch/arm/boot/dts/Makefile` as done in this [patch][16648]. Help others by [publishing][16649] your device tree as a patch.
