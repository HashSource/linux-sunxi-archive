# Sunxi-tools
sunxi-tools are the command line utilities developed to work with devices based on the [Allwinner SoC Family][52124]. These tools are used in [Retrieving device information][52125] as part of the [New Device howto][52126]. 
## Contents
  * [1 Building from Source][52127]
    * [1.1 Prerequisites][52128]
      * [1.1.1 libusb-1.0 and zlib][52129]
        * [1.1.1.1 debian/ubuntu][52130]
        * [1.1.1.2 fedora][52131]
      * [1.1.2 pkg-config][52132]
        * [1.1.2.1 debian/ubuntu][52133]
    * [1.2 Repository][52134]
    * [1.3 Building][52135]
  * [2 Tools][52136]
    * [2.1 sunxi-fexc and wrappers][52137]
      * [2.1.1 sunxi-fexc][52138]
      * [2.1.2 bin2fex][52139]
      * [2.1.3 fex2bin][52140]
    * [2.2 sunxi-pio][52141]
    * [2.3 sunxi-fel and helpers][52142]
      * [2.3.1 sunxi-fel][52143]
      * [2.3.2 usb-boot][52144]
      * [2.3.3 fel-pio][52145]
      * [2.3.4 fel-gpio][52146]
    * [2.4 fel-sdboot][52147]
    * [2.5 jtag-loop][52148]
    * [2.6 sunxi-bootinfo][52149]
    * [2.7 meminfo][52150]
    * [2.8 script-extractor][52151]
    * [2.9 phoenix-info][52152]
    * [2.10 sunxi-nand-part][52153]
  * [3 See also][52154]

# Building from Source
[![Information.png][52155]][52156] See also [Instructions in the README][52157]
## Prerequisites
### libusb-1.0 and zlib
#### debian/ubuntu
[code] 
    apt-get install libusb-1.0-0-dev zlib1g-dev
[/code]
#### fedora
[code] 
    yum install libusbx-devel
[/code]
### pkg-config
#### debian/ubuntu
[code] 
    apt-get install pkg-config
[/code]
## Repository
The repository is located on [GitHub][52158]. 
Change to the directory that you would like to clone the repository into and use: 
[code] 
    apt-get install git
    git clone https://github.com/linux-sunxi/sunxi-tools
[/code]
## Building
Change to the sunxi-tools directory. Those programs that need to run on the host computer will be built when you run: 
[code] 
    make
[/code]
The programs meant to be run _on the sunxi device itself_ are not built by default. You either need to run `make target-tools` or make them individually, by explicitly naming them (e.g. `make sunxi-meminfo`). 
When you are using [a cross-compiling toolchain][52159] (make sure it is added to your PATH), you may need to specify the toolchain prefix to use so that the programs can be executed on the sunxi device's architecture, e.g. 
[code] 
    make target-tools CROSS_COMPILE=arm-linux-gnueabihf-
[/code]
Since all these tools are tiny, you can just as well build these 'natively' as well, i.e. on the target sunxi device itself. In that case, you don't need a cross compiler and it's possible to set CROSS_COMPILE to an empty string. In this scenario - to build everything in one go - you may use `make all CROSS_COMPILE=`
# Tools
## sunxi-fexc and wrappers
_sunxi-fexc_ is a small program to convert between [ FEX][52160] and its binary representation, back and forth. It comes with two shortcuts (symbolic links) for easier invocation. 
### sunxi-fexc
[code] 
    Usage: ./sunxi-fexc [-vq] [-I <infmt>] [-O <outfmt>] [<input> [<output>]]
    
    infmt:  fex, bin  (default:fex)
    outfmt: fex, bin, uboot  (default:bin)
    
[/code]
When no arguments are provided, it waits on stdin. Similar, when no _< output>_ is provided, it will dump to stdout. This is great for piping, but might mess up your terminal (type _reset_ to have your terminal reset and make sense again). 
### bin2fex
This is a copy of _sunxi-fexc_ which takes a _script.bin_ and dumps the _.fex_ text. 
### fex2bin
This is a copy of _sunxi-fexc_ which takes the _.fex_ text file and dumps the binary. 
## sunxi-pio
Manipulate PIO settings (GPIO / pinmux config). 
Can be used both on a file dump of the PIO registers for use by the fel-gpio script or natively on the device by direct mmap hardware acess. 
## sunxi-fel and helpers
FEL is a means of talking to the Allwinner SoCs [BROM][52161] over USB. You first need to [ activate FEL mode][52162] on your device to be able to access it. 
### sunxi-fel
Main program, which provides a script interface for talking to FEL. 
Unless you select a specific device using the `--dev` or `--sid` options, the tool will access the first Allwinner device (in FEL mode) that it finds. You can print a list of all FEL devices currently connected/detected with `sunxi-fel --list --verbose`. 
When called with no arguments, `sunxi-fel` will display usage information: 
[code] 
    Usage: ./sunxi-fel [options] command arguments... [command...]
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
    
[/code]
### usb-boot
Legacy script for booting via USB in [ FEL mode][52162], _no longer used_. Refer to [ our usb boot page for more information][52163]. 
### fel-pio
Small binary which runs on the target. It enables IO register access over [ FEL mode][52162]. This should not be used directly. 
### fel-gpio
A script which uses _sunxi-fel_ to upload fel-pio to the target, and which then can use the _sunxi-pio_ utility, and manipulate GPIO settings, over FEL/USB. 
## fel-sdboot
A small ARM native SD boot code which forces FEL mode, to boot straight into [FEL][52162] mode without having to press any buttons. 
## jtag-loop
A small ARM native SD boot code which sets PF (CARD0) to JTAG mode and then busy-waits for you to attach with JTAG. 
## sunxi-bootinfo
Dump information from Allwinner boot files (boot0/boot1) 
[code] 
    	--type=sd	include SD boot info
    	--type=nand	include NAND boot info (not implemented)
    
[/code]
## meminfo
This device side tool reads in register information and prints out all the information you need for [ adding new device support to U-Boot][52164]. This tool gets statically compiled so it can be used on Android (the target sunxi device) as well. 
## script-extractor
This device side tool reads the script.bin data from RAM at the magic address 0x43000000 and saves it to a file. This tool gets statically compiled so it can be used on Android as well. Please note that it is only usable with [FEX][52160] based kernels (as used in the stock Android firmware) and does not make any sense with the devicetree based mainline kernel. 
## phoenix-info
gives information about a phoenix SD image created by the phoenixcard utility and optionally extracts the embedded boot code & firmware file from their hidden partitions. Not usable for [LiveSuit images][52165]. 
## sunxi-nand-part
_sunxi-nand-part_ is a tool to repartition the internal [NAND][52166] on sunxi devices. It should be (cross-)compiled for the device's architecture, and it requires the device to have a special kernel patch (already included in our [kernel tree][52167]) to expose the full [NAND][52166] as a block device. 
# See also
  * [Fex Guide][52160]
  * [git repository][52168]
  * [ FEL mode][52162]
  * fexc for Windows: [[1]][52169] or [[2]][52170] or [[3]][52171]
