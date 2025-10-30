# U-Boot/Legacy U-Boot
< [U-Boot][56470]
 
[![MBOX icon important.png][56473]][56474] | This page provides installation instructions for the legacy unmaintained u-boot-sunxi fork. It is only useful for the devices, which are still not supported by the [Mainline U-Boot][56475].   
---|---  
U-Boot is the bootloader commonly used on our allwinner SoCs. Amongst others, it provides the basic infrastructure to bring up a board to a point where it can load a linux kernel and start booting your operating system. 
This page covers the sunxi branch of U-Boot. Increasingly sunxi devices are available from upstream U-Boot, and we have a separate page for [Mainline U-Boot][56475]. 
## Contents
  * [1 Compile U-Boot][56476]
    * [1.1 Get a toolchain][56477]
    * [1.2 Clone the repository][56478]
    * [1.3 Determine build target][56479]
    * [1.4 Build][56480]
  * [2 Configure U-Boot][56481]
  * [3 Adding a new device to U-Boot][56482]
    * [3.1 System on Chip (SoC)][56483]
    * [3.2 DRAM Settings][56484]
      * [3.2.1 Generate a settings C file][56485]
      * [3.2.2 Verify the settings are unique][56486]
      * [3.2.3 Update the build system][56487]
      * [3.2.4 Stress test][56488]
      * [3.2.5 A note on optimization research][56489]
    * [3.3 Power Management Unit (PMU)][56490]
    * [3.4 Extra options][56491]
      * [3.4.1 UART][56492]
      * [3.4.2 Ethernet][56493]
      * [3.4.3 LEDs][56494]
    * [3.5 Build and run the new u-boot][56495]
    * [3.6 Commit your work to the git tree and send in the patch][56496]
  * [4 External links][56497]

# Compile U-Boot
[![MBOX icon important.png][56473]][56474] | This page provides installation instructions for the legacy unmaintained u-boot-sunxi fork. It is only useful for the devices, which are still not supported by the [Mainline U-Boot][56475].   
---|---  
## Get a toolchain
If you haven't done so before, get a suitable [toolchain][56498] installed and added to your PATH. 
## Clone the repository
You can clone our U-Boot repository by running: 
[code] 
    git clone -b sunxi https://github.com/linux-sunxi/u-boot-sunxi.git
[/code]
This should checkout the _sunxi_ branch, which allows booting from [ SD][56499], over [ USB][56500] and over [ ethernet][56501], but it still lacks support for booting off the [NAND][56502]. For more information about booting from NAND, check the [ NAND howto][56503]. 
[![Sticky-note-pin.png][56504]][56505] **Note:** the 'sunxi' branch in the _u-boot-sunxi_ repository is currently under active development and also frequently merges in the changes from the upstream U-Boot. Expect it to be occasionally broken. There is no stable branch or tag at the moment. If something does not work correctly, please consider trying older revisions from the 'sunxi' branch or look for any possible not-yet-applied fixes in the linux-sunxi and U-Boot mailing lists. 
## Determine build target
You can list the available U-Boot targets by running: 
[code] 
    sunxi/tools/genboardscfg.py
[/code]
[code] 
    grep sunxi boards.cfg | awk '{print $7}'
[/code]
You will notice that some board names are duplicates, but with __FEL_ attached. These are for use with [ USBBoot][56500], while the standard ones will boot from SD. 
## Build
When you have determined what target you want to build, configure: 
[code] 
    make CROSS_COMPILE=arm-linux-gnueabihf- {TARGET}_config 
[/code]
Then just build it: 
[code] 
    make CROSS_COMPILE=arm-linux-gnueabihf- 
[/code]
You might want to add '-j4' to make use of 4 processors (or any number that matches your system), to speed up the build. 
When the build has completed, there will be _spl/sunxi-spl.bin_ and _u-boot.img_ available in your u-boot tree. 
# Configure U-Boot
To be able to create the _boot.scr_ file from a _boot.cmd_ file, you need to have the _[mkimage][56506]_ tool. Various U-Boot scenarios are covered in the [configuration article][56507]. 
# Adding a new device to U-Boot
[![MBOX icon important.png][56473]][56474] | This page provides installation instructions for the legacy unmaintained u-boot-sunxi fork. It is only useful for the devices, which are still not supported by the [Mainline U-Boot][56475].   
---|---  
Please see [following email][56508] on how to add support for new devices to u-boot. 
Warning! Information below is a somewhat outdated as _u-boot-sunxi_ is not used anymore. The _boards.cfg_ file in the top level of your U-Boot tree holds all board configurations. 
Scroll down until you find the sunxi devices and create an entry for your device, in alphabetical order under device_name. The `device_name` field should follow the Manufacturer_Device format used for naming your device wiki page. The `device_name` field will be the target name used when building U-Boot. Note that this is case sensitive. 
[code] 
    Active  arm       armv7        sunxi     -             sunxi             device_name                sunXi:DEVICE_NAME,SPL                                                                                                             -
[/code]
If you wish to copy the above, then make sure that you make your browser wide enough so that even the _-_ at the end is shown. It is probably easier to copy another entry from _boards.cfg_ directly though. 
The next stage is to set the build options. In the example before these are `sunXi:DEVICE_NAME,SPL`, which sets the system on chip, DRAM settings and builds the secondary program loader. Each option after the colon should be capitalized and separated by a comma. The sections below give more details on the best options for your device. 
## System on Chip (SoC)
The first part of the build options, before the colon, identifies the sunxi generation your device's SoC belongs to. This with be either sun4i, sun5i, sun6i, sun7i or sun8i. See [Allwinner SoC Family][56509] to find the generation a chip belongs to. 
This option is used by the build system to identify a header file in `include/configs`. If you need to read the U-Boot source code for more details on build options then it is useful to know the SoC generation header files also include the `include/configs/sunxi-common.h` file. That file uses most of the build options given after the colon in boards.cfg and can be a useful source when investigating a build option. 
## DRAM Settings
Settings should aim to provide a stable system under heavy workloads, such as manipulating graphics, while giving maximum performance. 
There are three sources for DRAM settings: settings used by the device manufacturer; existing files from the sunxi U-Boot; and research of optimal settings. The recommended approach is to read the settings used by the device manufacturer and then check a similar file does not already exist in sunxi U-Boot. 
### Generate a settings C file
The device manufacturer is likely to have stored stable settings in the device and [sunxi tools][56510] can be used to [retrieve the device information][56511]. 
Execute [`meminfo -u`][56512] from within the original OS to read the memory registers and output a dram configuration C file for use with U-Boot. The output from [ bootinfo][56513] reads the settings from [boot1][56514] and could also be used to create a dram C file. 
Alternatively `[fexc][56515]` will translate values from a fex file into a C file ([![Sticky-note-pin.png][56504]][56505] _Note:_ using a fex file derived from a [script.bin][56516] will likely be missing important values). 
### Verify the settings are unique
The C file should be placed in the `board/sunxi` directory of your local copy of sunxi U-Boot. Run the bash script `./scripts/sunxi_dram_duplicates_find.sh` from the top level of your U-Boot directory and any files with the same settings should be shown. 
There are a lot of generic dram files available and if one of those matches your settings then refer to the generic file when adding your device to the build system and delete your created file. If an existing board config for another device matches yours, then please consider turning this into a generic dram file. 
If nothing matches, then `git add` your new file. 
### Update the build system
After you have a DRAM settings C file, edit board/sunxi/Makefile to add a line, in alphabetical order, for your device that links with the right dram_ object. 
[code] 
    obj-$(CONFIG_DEVICE_NAME)	+= dram_something.o
[/code]
Make sure that the _+=_ is preceded by just tabs, and not by spaces. 
The build option is DEVICE_NAME and can now be added to your devices's build options in boards.cfg. 
### Stress test
And as the final step, be sure to verify the reliability of the resulting dram settings using the [lima-memtester][56517] tool once you have built and run the new U-Boot. It has been discovered on more [than][56518] [one][56519] occasion that the dram settings from the vendors are not always perfectly reliable. So, let's say, in 90% of cases you are going to be fine by trusting the device manufacturers. But if you are out of luck, then you may get a system with mysterious application crashes or some very rare occasional deadlocks, preventing the system from having long uptime. These problems are very difficult to track, unless using dedicated stress testing tools. In other words, if you want to just save time by skipping a few minutes of downloading/compiling lima-memtester and a few hours of running it unattended, then you are essentially playing a [russian roulette][56520]. 
### A note on optimization research
You may have found reference to DRAM optimization on the Wiki, but this research should be done at a later stage as it can lead to unstable settings for different instances of the device. The [DRAM Controller page][56521] provides links to start researching this topic. Note that the 'zq' settings in 'dram_para' are not properly supported in the legacy _u-boot-sunxi_ , so these dram performance optimization experiments only make sense with the [Mainline U-Boot][56475]. 
## Power Management Unit (PMU)
There are three main PMUs used with Allwinner SoCs: [AXP152][56522], [AXP209][56523] and [AXP221][56524]
The default build option is for the AXP209. So if your device uses this PMU no build option should be given in _boards.cfg_. 
For AXP152 the build option is `AXP152_POWER` and for AXP221 it is `AXP221_POWER`. 
If there is no PMU then the build option is `NO_AXP`. 
## Extra options
### UART
Before building, you should check [ the U-Boot section in our UART howto][56525] and verify that you are using the standard UART IO pins. Failure to catch this will not give you any UART output, but might also prevent your device from booting (or worse). 
### Ethernet
TODO: Someone who has done this or is doing this, should describe how to add this.
### LEDs
U-Boot can be built to light up an LED when it runs. This will indicate that the boot process has passed beyond the secondary program loader (SPL) stage and started to run U-Boot. 
This build option is `STATUSLED=_n_`. 
`_n_` is the LED's GPIO pin identifier converted to an integer. For example PH25 would be 249. In schematics for Allwinner SoC based devices the pin identifier is written P _x_ _n_. Where _x_ is the port identifier (A through to S) and _n_ is the pin number. So in the example, H is the port identifier and 24 is the pin number. Each port can have up to 32 pins. So in the example, the numeric base value for port H is 224, because H is the 8th letter of the alphabet. That is (8-1)*32 = 224. Note that the base value for port A is 0. The numeric value for PH25 then is 224 plus pin number 25 = 249. 
## Build and run the new u-boot
That's it. You should now be able to [ compile][56526] and [ test U-Boot][56527]. It makes sense to also get a kernel and operating system running to more completely test the U-Boot dram settings before committing code. 
## Commit your work to the git tree and send in the patch
You can now commit your changes, and with: 
[code] 
    git format-patch -M -C HEAD^
[/code]
You will create a git mbox patch file which you can mail to [ our mailinglist][56528]. If you have [ set up git correctly][56529], you can just run: 
[code] 
    git send-email 0001-*.patch
[/code]
# External links
  * [git repository][56530]
  * [official wiki][56531]
