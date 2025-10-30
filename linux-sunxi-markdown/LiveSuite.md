# LiveSuit
(Redirected from [LiveSuite][32889])
 
**LiveSuit** is developed by [Allwinner][32892] as an installation application for computer systems (Linux, Windows, Mac) to flash the [NAND][32893] for Allwinner chips. 
You could also look at the [Installing to NAND][32894] tutorial to flash and manage NAND using opensource tools. 
## Contents
  * [1 Linux][32895]
    * [1.1 Clone the repository][32896]
    * [1.2 Build and install the kernel module][32897]
      * [1.2.1 Debian/Ubuntu][32898]
      * [1.2.2 Fedora][32899]
    * [1.3 Running LiveSuit][32900]
    * [1.4 Flashing an image][32901]
    * [1.5 Common pitfalls][32902]
      * [1.5.1 Too many devices error][32903]
      * [1.5.2 "Failed to flash firmware: Get Device Stage Failed!"][32904]
  * [2 Windows][32905]
    * [2.1 Download][32906]
    * [2.2 Flash][32907]
  * [3 MacOS][32908]
    * [3.1 Download][32909]
    * [3.2 Installation and usage][32910]
  * [4 See Also][32911]
  * [5 Troubleshooting][32912]

# Linux
For linux, we have gathered everything you need [in one place][32913]. 
## Clone the repository
[code] 
    git clone https://github.com/linux-sunxi/sunxi-livesuite.git
[/code]
## Build and install the kernel module
### Debian/Ubuntu
Before you can build this module, you first need to install _dkms_
[code] 
    apt-get install dkms
[/code]
Now descend into the _awusb_ directory and run 
[code] 
    make
[/code]
If you are getting error that _/lib/modules/4.4.50+/build_ is missing try adding symlink to the _/usr/src/linux-headers-XXX_ , for example: 
[code] 
    sudo ln -s /usr/src/linux-headers-3.6-trunk-rpi/ /lib/modules/4.4.50+/build
[/code]
  
Now install the module in your module tree, and load it: 
[code] 
    cp awusb.ko /lib/modules/`uname -r`/kernel/
    depmod -a
    modprobe awusb
[/code]
Add the following _50-awusb.rules_ file to _/etc/udev/rules.d_ , to be able to access the device as a normal user: 
[code] 
    KERNEL=="aw_efex[0-9]*", MODE="0666"
[/code]
Now reload udev rules to make the change active 
[code] 
    udevadm control --reload-rules
[/code]
### Fedora
Before you can build this module, you first could need to install _dkms_ and _libusbx_ (maybe you need also _nas-libs_) 
[code] 
    yum install dkms libusbx nas-libs kernel-devel
[/code]
Now descend into the _awusb_ directory and run 
[code] 
    make
[/code]
Now, as root, install the module in your module tree, and load it: 
[code] 
    cp awusb.ko /lib/modules/`uname -r`/extra/
    depmod -a
    modprobe awusb.ko
[/code]
Add the following _50-awusb.rules_ file to _/etc/udev/rules.d_ , to be able to access the device as a normal user: 
[code] 
    SUBSYSTEM!="usb_device",ACTION!="add",GOTO="objdev_rules_end"
    #USBasp
    ATTRS{idVendor}=="1f3a",ATTRS{idProduct}=="efe8",GROUP="yuorgrupid",MODE="0666"
    LABEL="objdev_rules_end"
[/code]
where "yuorgrupid" have to be substituted by the group id of your user. 
Now reload udev rules to make the change active 
[code] 
    udevadm control --reload-rules
[/code]
## Running LiveSuit
Just run the shell script directly: 
[code] 
    ./LiveSuit.sh
[/code]
This will detect whether your system is x86 or x86-64 and will run the appropriate binaries. 
## Flashing an image
**Warning** : If you attach your FEL enabled device before you start LiveSuit, then LiveSuit will not detect it. You need to first start the LiveSuit application. 
First, properly power down the device by either pressing and holding the power button for about 10 seconds, or by cutting all power in case of development board. 
Start [LiveSuit][32900], if you haven't already done so, and select an image for flashing. 
Then, [put your device into FEL mode][32914], and attach the USB OTG cable. 
LiveSuit should now detect your device and start flashing. 
## Common pitfalls
### Too many devices error
If you try to flash a USB 2.0 Device (such as Cubietruck) from a recent Ubuntu on an USB 3.0 Port, Chances are your device is not flashed as it is recognized by both xhci_hcd and ehci_hcd kernel modules. Try deactivating xhci_hcd (it needs to be blacklisted if it is in the kernel, as on Ubuntu 14.04), or, easier if available, deactivate USB 3.0 in your BIOS. 
### "Failed to flash firmware: Get Device Stage Failed!"
If you get a dialog window reading: 
[code] 
    Failed to flash firmware: Get Device Stage Failed!
[/code]
While the log in the terminal states: 
[code] 
    Fex_Send error: Invalid argument
    Fex_transmit_receive Error: ./eFexCore.cpp, 318
    Fex_command Error ./eFexCore.cpp 409
    cmd_common_verify_dev 85
    GetCurrentStage Failed 142 ./DeviceMessage/ASuitDeviceMessage.cpp
[/code]
Then you are most likely using an older version of the kernel module with a newer LiveSuit binary. [Use the latest kernel driver][32897]. 
While if the log in the terminal states: 
[code] 
    open: Permission denied
    PANIC : dev_manager_open_raw_dev() : can not open raw dev
    cmd_common_verify_dev 85
    PANIC : GetCurrentStage() : run verify dev cmd ,fail
    PANIC : dev_manager_close_raw_dev() : can not close raw dev
    GetCurrentStage Failed 142 ./DeviceMessage/ASuitDeviceMessage.cpp
[/code]
likely you can overcome this issue unloading the _awusb_ module 
[code] 
    modprobe -r awusb.ko 
[/code]
and try again. 
# Windows
Please note that this version of livesuit only seems to work on Windows 7. 
It fails to run on windows XP, and shows the following error message in a dialog: 
[code] 
    Wait for PnpFesIn timeout!
[/code]
There are similar reports from Windows 8 users. 
## Download
  * Windows version [LiveSuit][32915]
  * Please note that PhoenixSuit is actually LiveSuit2.0

## Flash
To flash A10 devices with LiveSuit, first you need to let the device go to [FEL][32914] mode. 
Execute LiveSuit.exe and click SelectImg button to select the [LiveSuit images][32916] you have. Connect your devices to PC with a USB cable. If Windows ask you to install driver, select the driver in the LiveSuit program UsbDriver folder. 
# MacOS
## Download
[code] 
    <http://dl.cubieboard.org/software/tools/livesuit/LiveSuit_ForMac.zip>
    
[/code]
## Installation and usage
This zip archive contains a pdf explaining procedure (in English and Chinese) and another zip for the software itself. 
# See Also
  * [LiveSuit images][32916]

# Troubleshooting
\- Linux distribution Linux does not supported issue: 
LiveSuit is accessible two ways. One is above way by getting from sunxi repository. The other way is by downloading as a zip file. For the zip file, LiveSuit v3.0.6 or below, if you try to install under Linux Mint 17.1, when you run LiveSuit.run file, you get such error: 
[code] 
    "Linux distribution Linux does not supported!!!"
[/code]
This is because distribution name for Linux Mint starts with "Linux Mint....blablabla" in /etc/issue file. Simple edit that file ( sudo nano /etc/issue ), and add "Ubuntu" in the beginning of the line. 
After that, I highly recommend to install in root mode, i.e "sudo ./LiveSuit.run" Tested with LinuxMint 17.1 xfce 64bit, and LiveSuitV3.0.6 works perfectly to write img files to board via USB-OTG connection.
