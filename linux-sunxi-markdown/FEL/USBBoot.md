# FEL/USBBoot
< [FEL][18884]
 
On [supported Allwinner SoCs][18887] it is possible to boot over USB OTG. This requires only minimal changes compared to the build steps in [ the manual build howto][18888], and these changes are explained on this wiki page. 
By booting over USB OTG, it is possible to forgo the SD-Card entirely, and it is especially useful for devices where no [UART][18889] can be found, or where the UART is multiplexed with the SD-Card. You can then use [ a micro-SD breakout adapter][18890] to access the serial port. 
## Contents
  * [1 Install the tools][18891]
  * [2 Switch your device into FEL mode][18892]
  * [3 Boot the system over USB][18893]
    * [3.1 Mainline U-Boot (v2015.04 and newer versions)][18894]
      * [3.1.1 Getting the mainline U-Boot sources][18895]
      * [3.1.2 Booting U-Boot over USB][18896]
      * [3.1.3 Booting the whole system over USB (U-Boot + kernel + initramfs)][18897]
      * [3.1.4 Overriding environment variables with uEnv-style data][18898]
        * [3.1.4.1 Example][18899]
      * [3.1.5 Early kernel development for new SoCs][18900]
    * [3.2 Legacy mainline U-Boot (v2015.04 and older versions)][18901]
    * [3.3 Legacy u-boot-sunxi][18902]
      * [3.3.1 Preparing U-Boot][18903]
      * [3.3.2 Manual loading][18904]
      * [3.3.3 usb-boot script][18905]
    * [3.4 Using sunxi-fel on Windows][18906]
      * [3.4.1 Mandatory USB driver][18907]
      * [3.4.2 Zadig to the rescue][18908]
  * [4 Adding support for new SoC variants][18909]
    * [4.1 SoC support status][18910]
    * [4.2 General description of the "sunxi-fel uboot" command implementation][18911]
    * [4.3 The SoC-specific mandatory thing][18912]
    * [4.4 The SoC-specific bonus features][18913]
    * [4.5 Testing][18914]
  * [5 Potential future improvements][18915]
  * [6 Known issues][18916]
  * [7 See also][18917]

# Install the tools
There is a utility in [ the sunxi-tools repository][18918] called 'sunxi-fel'. This utility is used for booting the system over USB and it needs to be installed first. 
The command line syntax of the `sunxi-fel` utility: 
[code] 
    Usage: sunxi-fel [options] command arguments... [command...]
            -v, --verbose                   Verbose logging
            -p, --progress                  "write" transfers show a progress bar
            -l, --list                      Enumerate all (USB) FEL devices and exit
            -d, --dev bus:devnum            Use specific USB bus and device number
                --sid SID                   Select device by SID key (exact match)
    
            spl file                        Load and execute U-Boot SPL
                    If file additionally contains a main U-Boot binary
                    (u-boot-sunxi-with-spl.bin), this command also transfers that
                    to memory (default address from image), but won't execute it.
    
            uboot file-with-spl             like "spl", but actually starts U-Boot
                    U-Boot execution will take place when the fel utility exits.
                    This allows combining "uboot" with further "write" commands
                    (to transfer other files needed for the boot).
    
            hex[dump] address length        Dumps memory region in hex
            dump address length             Binary memory dump
            exe[cute] address               Call function address
            reset64 address                 RMR request for AArch64 warm boot
            memmove dest source size	Copy <size> bytes within device memory
            readl address                   Read 32-bit value from device memory
            writel address value            Write 32-bit value to device memory
            read address length file        Write memory contents into file
            write address file              Store file contents into memory
            write-with-progress addr file   "write" with progress bar
            write-with-gauge addr file      Output progress for "dialog --gauge"
            write-with-xgauge addr file     Extended gauge output (updates prompt)
            multi[write] # addr file ...    "write-with-progress" multiple files,
                                            sharing a common progress status
            multi[write]-with-gauge ...     like their "write-with-*" counterpart,
            multi[write]-with-xgauge ...      but following the 'multi' syntax:
                                              <#> addr file [addr file [...]]
            echo-gauge "some text"          Update prompt/caption for gauge output
            ver[sion]                       Show BROM version
            sid                             Retrieve and output 128-bit SID key
            clear address length            Clear memory
            fill address length value       Fill memory
    
    	spiflash-info			Retrieves basic information
    	spiflash-read addr length file	Write SPI flash contents into file
    	spiflash-write addr file	Store file contents into SPI flash
    
[/code]
[![Exclamation.png][18919]][18920] _Warning:_ some Linux distributions are already providing packaging for sunxi-tools. However they are also removing certain tools and renaming executables at their discretion. If you encounter troubles with the sunxi-tools package from your distro, then getting sunxi-tools directly from the [github repository][18921] is always an option. 
# Switch your device into FEL mode
Before the 'sunxi-fel' tool can actually talk to your device, the device needs to be connected to your PC using a "USB A to USB mini/micro B" cable. 
And then the device needs to be switched into FEL mode. Please refer to the [ FEL howto][18884] for information on how to boot to FEL mode. Device pages should mention the button which triggers FEL mode as well. 
If you run: 
[code] 
     sunxi-fel version 
[/code]
and it returns something like: 
[code] 
     AWUSBFEX soc=00162500(A13) 00000001 ver=0001 44 08 scratchpad=00007e00 00000000 00000000 
[/code]
Then you have successfully switched the device into FEL mode and it is ready to accept commands or load the system over USB. 
# Boot the system over USB
## Mainline U-Boot (v2015.04 and newer versions)
### Getting the mainline U-Boot sources
To obtain the U-Boot sources, clone the current U-Boot master branch: 
[code] 
    git clone git://git.denx.de/u-boot.git
    cd u-boot
    
[/code]
Or alternatively the 'next' branch from the sunxi custodian tree: 
[code] 
    git clone -b next git://git.denx.de/u-boot-sunxi.git
    cd u-boot-sunxi
    
[/code]
Both of these branches are bleeding edge and may contain bugs from time to time. If you encounter troubles, try a tarball with the latest formal U-Boot release before giving up. 
### Booting U-Boot over USB
Then just do a regular u-boot build: 
[code] 
    make CROSS_COMPILE=arm-linux-gnueabihf- Cubietruck_defconfig
    make CROSS_COMPILE=arm-linux-gnueabihf- -j$(nproc)
    
[/code]
For 64-bit SoCs: 
[code] 
    make CROSS_COMPILE=aarch64-linux-gnu- <your-board>_defconfig
    make CROSS_COMPILE=aarch64-linux-gnu- -j$(nproc) BL31=/path/to/trusted-firmware/build/sun50i-a64/debug/bl31.bin SCP=/dev/null
    
[/code]
Make sure to pick the right Trusted-Firmware (TF-A, aka ATF) target, for A64 and H5 it's sun50i-a64, for H6 it's sun50i-h6, for H616/H313 it's sun50i-h616. 
And boot it over USB (the 'sunxi-fel uboot' command requires an up to date version of sunxi-tools): 
[code] 
    sunxi-fel uboot u-boot-sunxi-with-spl.bin
    
[/code]
This boots U-Boot over USB. And after U-Boot takes control, it starts scanning various default locations for the boot.scr file in order to boot the rest of the system. 
### Booting the whole system over USB (U-Boot + kernel + initramfs)
This needs to be used with **U-Boot v2015.10** or newer (which can automatically find the 'boot.scr' blob in RAM after it had been uploaded there by 'sunxi-fel'). 
Assuming that you have a kernel image, a correct dtb blob for your hardware, a [boot script blob][18922] and an initrd image, booting all of this can be done with just a single 'sunxi-fel' invocation: 
[code] 
    sunxi-fel -v uboot u-boot-sunxi-with-spl.bin \
                 write 0x42000000 uImage \
                 write 0x43000000 sun7i-a20-cubietruck.dtb \
                 write 0x43100000 boot.scr \
                 write 0x43300000 rootfs.cpio.lzma.uboot
    
[/code]
For 64-bit SoCs: 
[code] 
    sunxi-fel -v uboot u-boot-sunxi-with-spl.bin \
                 write 0x40200000 Image \
                 write 0x4fa00000 sun50i-a64-pine64-lts.dtb \
                 write 0x4fc00000 boot.scr \
                 write 0x4ff00000 rootfs.cpio.lzma.uboot
    
[/code]
If you wonder about all the magic addresses used in the command line above, the right values can be found in the [U-Boot sources][18923] in `MEM_LAYOUT_ENV_SETTINGS` definition (see #ifdef CONFIG_ARM64 for the 64-bit values): 
[code] 
    bootm_size     = 0xf000000
    kernel_addr_r  = 0x42000000
    fdt_addr_r     = 0x43000000
    scriptaddr     = 0x43100000
    pxefile_addr_r = 0x43200000
    ramdisk_addr_r = 0x43300000
    
[/code]
Somewhere between U-Boot v2017.03 and v2017.07, U-Boot switched to a new SPL format, which is not compatible with sunxi-tools release <=1.4.2 provided by some distros. The tool will print error message such as 
[code] 
    sunxi SPL version mismatch: found 0x02 > maximum supported 0x01.
    You need a more recent version of this (sunxi-tools) fel utility.
    
[/code]
You will need a later sunxi-tools from git to avoid this problem. 
an example boot.cmd   
---  
32-bit boards  | 64-bit boards 
[code] 
    env set fdt_high ffffffff
    bootm 0x42000000 0x43300000 0x43000000
    
[/code]  
| 
[code] 
    booti 0x40200000 0x4ff00000 0x4fa00000
    
[/code]  
Following options may have to be enabled if you are using Buildroot (for 32-bit systems): 
[code] 
    BR2_LINUX_KERNEL_UIMAGE=y
    BR2_LINUX_KERNEL_UIMAGE_LOADADDR=0x42000000
    BR2_TARGET_ROOTFS_CPIO=y
    BR2_TARGET_ROOTFS_CPIO_LZMA=y
    BR2_TARGET_ROOTFS_CPIO_UIMAGE=y
    BR2_TARGET_ROOTFS_INITRAMFS=y
    
[/code]
### Overriding environment variables with uEnv-style data
With v1.4 and above, the `sunxi-fel` utility has gained the ability to pass environment data to U-Boot via FEL. 
_key= <value>_ pairs from a textual representation will get **merged with the default environment** ; similar to U-Boot's `import -t` command, or what older U-Boot did with the _uEnv.txt_ file on autoboot. 
    [![Sticky-note-pin.png][18924]][18925] _Note:_ This requires an up-to-date U-Boot (v2016.09 or later), plus you need to start your data with a special 'magic' signature:
    
[code]
    #=uEnv
[/code]
The signature will allow the sunxi-fel "write" command to detect uEnv-style data - and will cause it to flag this transfer accordingly, in turn requesting U-Boot v2016.09+ to import it afterwards. You may override arbitrary environment variables this way, including the `bootcmd`. 
#### Example
Use your text editor to save a _my.env_ file with 
[code] 
    #=uEnv
    myvar=world
    bootcmd=echo "Hello $myvar."
    
[/code]
and then test it with 
[code] 
    ./sunxi-fel uboot u-boot-sunxi-with-spl.bin write 0x43100000 my.env
[/code]
You should see U-Boot's autoboot print the corresponding message and drop you to the prompt, proving that you have successfully overwritten the default "bootcmd". 
### Early kernel development for new SoCs
Because FEL boot is supported by the BROM code, it is readily available out of the box. The 'sunxi-fel' tool only needs to be patched to add the SRAM layout information, but this is [usually very simple][18926] and also extensively documented on this wiki page. A relatively challenging task is the U-Boot support, because it needs the DRAM initialization code for the SPL. But assuming that the U-Boot bootloader is already available, FEL boot can be used for kernel development even when there is no Ethernet or MMC support in the kernel yet. For the sake of convenience, it is best to write [fel-sdboot.sunxi][18927] to the SD card (substitute /dev/sdX with the appropriate block device of your card reader): 
[code] 
    wget https://github.com/linux-sunxi/sunxi-tools/raw/master/bin/fel-sdboot.sunxi
    dd if=fel-sdboot.sunxi of=/dev/sdX bs=1024 seek=8
    
[/code]
Then just use the instructions from the previous section [about U-Boot + kernel + initramfs][18928]. And after the MMC support is implemented in the kernel, it becomes possible to move the rootfs to the SD card and get rid of the initrd image. But FEL USB boot is still useful until either Ethernet or USB becomes good enough for booting over network. 
## Legacy mainline U-Boot (v2015.04 and older versions)
**Is here for historical reference only (click on the 'Expand' link to see it):**
The U-Boot had to be configured using "*_**felconfig** " option before compiling (instead of "*_defconfig", as that builds a SPL only suitable for MMC boot). For example, in the case of a Cubietruck board, that would be: 
[code] 
    make CROSS_COMPILE=arm-linux-gnueabihf- Cubietruck_felconfig
    make CROSS_COMPILE=arm-linux-gnueabihf- -j$(nproc)
    
[/code]
Then just use the 'sunxi-fel' tool to upload various pieces to certain magic addresses (the magic CONFIG_SPL_TEXT_BASE=0x2000 and CONFIG_SYS_TEXT_BASE=0x4a000000 values can be found in the [U-Boot sources][18929]). And execute them in a certain order: 
[code] 
    echo == upload the SPL to SRAM and execute it ==
    sunxi-fel write 0x2000 spl/u-boot-spl.bin
    sunxi-fel exe   0x2000
    
    sleep 1 # wait for DRAM initialization to complete
    
    echo == upload the main u-boot binary to DRAM ==
    sunxi-fel write 0x4a000000 u-boot.bin
    
    echo == execute the main u-boot binary ==
    sunxi-fel exe   0x4a000000
    
[/code]
This boots U-Boot over USB. And after U-Boot takes control, it starts scanning various default locations for the boot.scr file in order to boot the rest of the system. 
## Legacy u-boot-sunxi
**Is here for historical reference only (click on the 'Expand' link to see it):**
### Preparing U-Boot
U-boot needs to be built specifically for booting over USB. This is called FEL mode, and enabling this disables the full SD card (for u-boot, script.bin and the kernel might re-enable it later on). 
Just follow the [ guide to compile u-boot][18930], but [ select a target][18931] whose name has **_FEL**. 
### Manual loading
While the script from the next section is perhaps better, you can now choose to load u-boot manually: 
[code] 
      sunxi-fel write 0x2000 ../u-boot/spl/u-boot-spl.bin
      sunxi-fel exe 0x2000
      sleep 1 # Wait for DRAM initialization to complete
      sunxi-fel write 0x4a000000 ../u-boot/u-boot.bin
      sunxi-fel exe 0x4a000000
    
[/code]
### usb-boot script
There was a script in the older releases of [Sunxi-tools][18918] called [ usb-boot][18932]. You can download this script from github using the tag for an old version 1.2: 
[code] 
    wget https://raw.githubusercontent.com/linux-sunxi/sunxi-tools/v1.2/usb-boot
    chmod +x usb-boot
    
[/code]
And then use it as follows: 
[code] 
    Usage: ./usb-boot u-boot-spl.bin u-boot.bin [boot.scr] [kernel script.bin [initramfs]]
[/code]
u-boot-spl.bin and u-boot.bin are the [u-boot binaries][18933] which are [ FEL enabled][18934]. 
[ boot.scr][18935] is the u-boot script. If you do not specify a file ending with .scr the default is used. 
uImage is your [ compiled kernel image][18936]. 
[ script.bin][18937] is your hw configuration converted to binary from .fex. 
initramfs is an optional initramfs/initrd image in u-boot mkimage format. 
## Using sunxi-fel on Windows
  * [https://github.com/linux-sunxi/sunxi-tools/tree/windows#using-sunxi-tools-under-windows][18938]
  * Pre-built mingw32-w64 [binaries][18939] \- built from revision 530adfa1420c1a1a73aa93df5b4d4c39f997f490 of [sunxi-tools][18921].

### Mandatory USB driver
Under Windows (unlike Linux) every USB device that an application program wishes to access **must have a suitable USB driver installed**. 
This means that _any device that shows up as "unknown" in your Device Manager will be inaccessible_ \- typical symptoms would be an `ERROR: Allwinner USB FEL device not found!` message, or even 
[code] 
    libusb_open() ERROR -12: Operation not supported or unimplemented on this platform
[/code]
when trying to enforce the specific device with the `--dev` option. 
### Zadig to the rescue
Fortunately, there's a very convenient utility to help with the USB driver setup. Grab your copy from <http://zadig.akeo.ie/>. 
Before launching it, make sure your Allwinner device is connected and in [FEL][18884] mode. 
[![Zadig-fel-winusb-instructions.png][18940]][18941]
  
Initially, the Zadig utility should only present you a single "Unknown Device #1". If it happens to actually list multiple devices, make sure you pick the correct one by verifying the **USB ID** , shown as "**1F3A:EFE8** " in above picture. 
  1. _(Optional, but recommended)_ Tick the "Edit" checkbox on the right hand side, and enter a more descriptive name for the USB ID in question. This helps a lot later, to distinguish your Allwinner device from other USB entries in the Device Manager.
  2. Select the desired USB driver. This depends on the Windows executables you intend to use; namely the specific version of _libusb_ that those binaries were compiled with. If your `sunxi-fel.exe` has special driver requirements, those should be stated in the accompanying documentation. When in doubt, select [**WinUSB**][18942] for a "generic" driver (available from Win XP SP3 onwards).
  3. Click "Install Driver". Voilà - from now on your device should no longer be "unknown" in Device Manager, and `sunxi-fel` is expected to work with it.

    [![Sunxi-fel win32.png][18943]][18944]
  
**Troubleshooting:**
  * If you have `listdevs.exe` available in your package, you may use it to check that Windows detects your device at all, and to determine the _libusb_ bus/device numbers.
  * In case you selected the wrong driver, you may simply re-run Zadig to install another. Use "_Options_ ", "_List All Devices_ " and pick the desired one (keeping an eye on the USB ID once more). Alternatively you can use the Windows Device Manager to remove/uninstall the driver (effectively rendering the device "unknown" again), and then start from scratch.

* * *
# Adding support for new SoC variants
If everything is already working fine for you, then you can stop reading here :-) But sometimes you may get messages like **"SPL: Unsupported SoC type"** or **"Warning: no 'soc_sram_info' data for your SoC"** when trying to use the instructions from the previous sections. In this case, doing some work to add support for your SoC may be required. It is also a good idea to first check the [SoC support status][18887] table below. 
## SoC support status
SoC name  | SoC support status in sunxi-tools [[1]][18945] | SoC support status in U-Boot  | "sunxi-fel write" speed [[2]][18946] | USB DFU speed  | MMU setup  | Stack pointers [[3]][18947] | Notes   
---|---|---|---|---|---|---|---  
Allwinner [A10][18948] | Supported | Supported | ~600 KB/s | ~3.2 MB/s | Enabled by BROM, ttbr0=0x20000 | sp_irq=0x02000, sp=0x05DF8 |   
Allwinner [A13][18949] | Supported | Supported | ~570 KB/s (win7 laptop), ~940kB/s (linux opipc) |  | Enabled by BROM, ttbr0=0x08000 | sp_irq=0x02000, sp=0x05DF8 |   
Allwinner [A20][18950] | Supported | Supported | ~960 KB/s | ~3.7 MB/s | Enabled by BROM, ttbr0=0x20000 | sp_irq=0x02000, sp=0x05E08 |   
Allwinner [A23][18951] | Supported | Supported |  |  | Enabled by BROM, ttbr0=0x08000 |  |   
Allwinner [A31s][18952] | Supported | Supported | ~510 KB/s |  | Enabled by BROM, ttbr0=0x20000 | sp_irq=0x02000, sp=0x05E08 |   
Allwinner [A33][18953] | Supported | Supported | ~191 KB/s |  | Not enabled by BROM |  |   
Allwinner [A64][18954] | Supported | Supported [[4]][18955] | ~510 KB/s |  | Not needed [[5]][18956] | sp_irq=0x12000, sp=0x15E08 | SPL needs to be loaded at 0x10000 (instead of 0x0)   
Allwinner [A80][18957] | Supported | Supported | ~930 KB/s (boot0) |  | Not enabled by BROM | sp_irq=0x12000, sp=0x15AD0 | SPL needs to be loaded at 0x10000 (instead of 0x0)   
Allwinner [A83T][18958] | Supported | Supported | ~510 KB/s (~191 KB/s if MMU not enabled) |  | Enabled by sunxi-fel, ttbr0=0x44000 | sp_irq=0x00002000, sp=0x00005E08 |   
Allwinner [H3][18959] | Supported | Supported | ~960 KB/s |  | Enabled by sunxi-fel, ttbr0=0x44000 | sp_irq=0x00002000, sp=0x00005E08 |   
Allwinner [H5][18960] | Supported | Supported [[4]][18955] | ? |  | ? | sp_irq=0x12000, sp=0x15E08 | SPL needs to be loaded at 0x10000   
Allwinner [H6][18961] | Supported | Supported [[4]][18955] | ~177 KB/s |  | Not enabled by BROM | sp_irq=0x22000, sp=0x25E08 | SPL needs to be loaded at 0x20000   
Allwinner [R8][18962] | Supported | Supported | ~500 KB/s |  | Enabled by BROM, ttbr0=0x08000 | sp_irq=0x02000, sp=0x05DF8 | basically like A13,  
handled by same _soc_id_  
Allwinner [R40][18963] | Supported | Supported | ? |  | Not enabled by BROM | sp_irq=0x02000, sp=0x05E08 |   
  1. [↑][18964] Basic FEL commands like "read", "write" and "exe" are already supported in a generic way on every SoC. This table column only shows support status for advanced commands like "spl" and "uboot".
  2. [↑][18965] The transfer speed can be measured by running the following commands: 
[code]# Execute only the SPL part of the U-Boot image in order to initialize DRAM
         sunxi-fel spl u-boot-sunxi-with-spl.bin
         
         # Upload a file to DRAM ('-p' enables a progress display, which includes transfer speed)
         sunxi-fel -p write 0x42000000 uImage
         
[/code]
You can use any file instead of "uImage". Larger file size means better speed measurement accuracy, so pick something that has size of at least several megabytes. Please note that the devices, which have MMU disabled, are currently expected to show slow transfer speeds (this can be probably improved later). 
  3. [↑][18966] There are two stacks in FEL mode: 
     * 'sp_irq' is the value of the IRQ stack pointer register. The IRQ stack is typically empty, which means that the 'sp_irq' is pointing to both top and bottom of this stack (unless the processor is currently handling an IRQ).
     * 'sp' is the value of the normal stack pointer register, also available to your code when it is executed via "sunxi-fel exe" command. This stack typically contains quite a bit of data between 'sp' and 0x7000 (which was written there by the FEL code from BROM).
When uploading data via "sunxi-fel write" command, be sure not to overwrite these stacks (don't touch the data in SRAM below 'sp_irq' and above 'sp').
  4. ↑ [4.0][18967] [4.1][18968] [4.2][18969] Requires a 32-bit SPL build. There is a not-mainline(able) [sunxi64-fel32][18970] branch for that, also pre-built [binaries][18971] for easy use with sunxi-fel.
  5. [↑][18972] The BROM in A64 is not [troublesome][18973] anymore and "sunxi-fel hexdump 0x1c14200 16" works fine for retrieving SID. This indicates somewhat better implementation and the MMU speed boosting workaround is not needed.

## General description of the "sunxi-fel uboot" command implementation
Allwinner is treating booting over USB in a special way, and this behaviour is unfortunately hardcoded in the [BROM][18974]. The main differences between booting from MMC/NAND and booting from USB are: 
  * For booting from the SD card or NAND, the BROM code is searching for a special eGON signature on a bootable media and loading up to 32K (in fact a bit less than that) of the initial code to the address 0x0 in SRAM (that's typically the SRAM section A1) and then executes it. This initial code (known as "SPL" in U-Boot or "boot0" in the Allwinner's bootloader) configures the DRAM to get access to more storage space, then loads the main part of the bootloader and the rest of the system there.
  * For booting via FEL, the Allwinner's idea is that we are supposed to upload only something like up to ~15K of code at the address 0x2000 in SRAM and execute it.

This is at least inconsistent and definitely not good for us. U-Boot used to require a special size-optimized variant of the SPL specifically for booting via FEL, which also had the base address changed from 0x0 to 0x2000 as an additional inconvenience. Having a special variant of the SPL means an extra configuration to maintain. And the code size limitation is also a nasty problem because a certain set of features has to be disabled. But the "spl" and "uboot" commands, which are implemented by the "sunxi-fel" tool, can work-around this limitation by smuggling just the ordinary MMC or NAND variant of the U-Boot SPL into SRAM. More technical details are provided below. 
The reason why we have ~15K code size limitation when booting via FEL is illustrated on the picture below. When we are booting the device in FEL mode, a special code is activated in the BROM and starts communicating over USB using FEL protocol. The USB driver code from the BROM allocates two stacks at rather inconvenient locations inside of the first 32K of SRAM. The IRQ handler stack is set at the address 0x2000 and grows down. And the ordinary application stack is set at the address 0x7000 and also grows down. These stacks make the SRAM space fragmented, and the largest usable contiguous ~15K area is sandwiched between these two stacks. Overwriting either of these stacks via the "sunxi-fel write" crashes the device and it just stops responding to further FEL commands. So uploading a normal U-Boot SPL (which typically has size slightly larger than 20K) to the address 0x0 via "sunxi-fel write" command with the intention to execute it via "sunxi-fel exe" command does not work as expected. 
[![FEL uboot memory map.jpg][18975]][18976]
So, how do we solve this problem? Allwinner devices typically have more than 32K of SRAM (the smallest total amount of SRAM among all devices is 48K in Allwinner A13). And we can use extra SRAM locations as a backup storage for the FEL stacks (shown as "backup area 1" and "backup area 2" on the picture above). We also upload a special [thunk code][18977], which is responsible for swapping the content of the FEL stacks with the content of these backup areas before jumping to the address 0x0. Now in order to execute a full-fledged SPL from U-Boot, we only need to split the SPL into chunks and upload it to SRAM, writing the parts which are supposed to overlap the FEL stacks to the backup areas. Executing the thunk code saves the FEL stacks to the backup areas, reassembles the SPL together and passes control to the SPL. 
Why do we need to backup the original FEL stacks? The reason is that just uploading and executing the SPL alone is not enough to boot the system. The SPL code is very small and its primary task is to setup clocks and initialize the DRAM. After the DRAM is initialized, all the storage space problems are resolved and we want to load the main U-Boot code to the device. And for this we still need the BROM FEL code alive and getting control back, so that it can still talk with the 'sunxi-fel' tool over USB and execute FEL commands. Hence the SPL returns control back to the thunk code. The thunk code swaps FEL stacks with backup areas again and finally passes control back to the FEL code in the BROM, which is able to happily resume its work because it has all the original data back in its stacks. 
## The SoC-specific mandatory thing
The previous section describes how the "sunxi-fel spl" and "sunxi-fel uboot" commands work. But not everything is perfect. One inconvenient thing is that the SRAM address space layout (and the location of the backup areas) may be different for different SoC variants. Hence we need to provide the [SRAM layout description information][18978] for each SoC in the source code of the 'sunxi-fel' program. The comments in the source code should provide reasonable explanations. And here is an example of such SRAM layout information for A31: 
[code] 
    /*
     * A31 is very similar to A10/A13/A20, except that it has no SRAM at 0x8000.
     * So we use the SRAM section at 0x44000 instead. This is the memory, which
     * is normally shared with the OpenRISC core (should we do an extra check to
     * ensure that this core is powered off and can't interfere?).
     */
    sram_swap_buffers a31_sram_swap_buffers[] = {
    	{ .buf1 = 0x01800, .buf2 = 0x44000, .size = 0x800 },
    	{ .buf1 = 0x05C00, .buf2 = 0x44800, .size = 0x8000 - 0x5C00 },
    	{ 0 }  /* End of the table */
    };
    
    soc_sram_info soc_sram_info_table[] = {
    	{
    		.soc_id       = 0x1633, /* Allwinner A31 */
    		.thunk_addr   = 0x46E00, .thunk_size = 0x200,
    		.swap_buffers = a31_sram_swap_buffers,
    	},
    	{ 0 } /* End of the table */
    };
    
[/code]
Basically, the first backup area for A31 is set at 0x44000 and covers the IRQ stack (0x1800-0x2000). The second backup area is set at 0x44800 and covers the normal FEL stack plus also some extra area above it (0x5C00-0x8000). The thunk code is placed at 0x46E00. 
## The SoC-specific bonus features
  * While this is not strictly required, we can [tweak the cacheability attributes of the memory sections by modifying the MMU translation table][18979]. This improves the performance of the "sunxi-fel write" command and helps to significantly reduce the time needed to upload large chunks of data to DRAM.

  * The Cortex-A8 based SoC variants need [a tweak for the AUXCR L2EN bit][18980]. Without this, the L2 cache ends up disabled in Linux after booting over FEL.

## Testing
After adding the support for a new SoC variant to the 'sunxi-fel' tool, it makes sense to actually test whether it works. In the case if U-Boot already has support for this particular SoC variant, the testing is simple and can be done by just running **"sunxi-fel uboot u-boot-sunxi-with-spl.bin"** command and confirming that U-Boot starts properly on the device. 
In the case if U-Boot still does not have full support for this particular SoC variant yet, testing still can be done using the Allwinner's boot0 bootloader. If you have some boot0-based bootable SD card image (let's call it 'sdcard-image.bin'), then you can: 
  * write this image to an SD card
  * extract the boot0 part from this image via running **"dd if=sdcard-image.bin of=boot0.bin bs=1024 skip=8 count=32"**
  * switch the device into FEL mode
  * insert the SD card
  * run **"sunxi-fel spl boot0.bin"**

If the system boots normally, in the same way as just doing a normal boot from the SD card, then the 'sunxi-fel' tool is working fine. Please note that you may get error messages from the 'sunxi-fel' tool while doing this. This is normal and expected (boot0 does not return control back to the FEL code in BROM but instead does its usual booting of the system from the SD card). 
  

# Potential future improvements
There is quite a lot of room for improvement: 
  * Allow the 'sunxi-fel spl' command to also use raw SD card images in addition to just recognizing 'u-boot-sunxi-with-spl.bin' format.
  * Store the magic addresses (CONFIG_SYS_TEXT_BASE, kernel_addr_r, fdt_addr_r, scriptaddr, ramdisk_addr_r) in the [EGON][18981] header extension in order to avoid the need of passing them to the 'sunxi-fel' tool as command line parameters.
  * Single U-Boot binary for both the regular UART serial console and the UART over the [MicroSD Breakout][18890] configurations. The configuration option can be provided to the 'sunxi-fel' tool in a command line argument and handed over to to U-Boot in the eGON header extension.

The exact eGON header extension format needs to be formalized. We should also check whether it can provide backwards/forward compatibility with the Allwinner's BOOT0 bootloader. 
# Known issues
Please report problems to <https://github.com/linux-sunxi/sunxi-tools/issues>
# See also
  * [FEL][18884]
  * [miniroot][18982]
