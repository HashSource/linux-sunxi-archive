# Working around missing SD
This page documents the route that I, libv, had to take to get an A13 with serial on the SD pins, booting a linux off of the NAND. This is a temporary page, and the information contained in it will eventually get split into the right places on our wiki. 
The plan is to boot a kernel with nfs and g_ether compiled in, and then mounting nfsroot over usb. This nfsroot lives on a previously prepared SD card on the host laptop. 
## Contents
  * [1 FEL/USBBoot][59440]
  * [2 hacking script.bin][59441]
  * [3 Build kernel][59442]
  * [4 Goal][59443]
  * [5 Result][59444]

# [FEL/USBBoot][59445]
First step was of course to bang some shape into this page. Then a special u-boot target was created for the inet_v86vz, called INet_86VZ_FEL with the following settings: 
[code] 
    sun5i:INET_86VZ,SPL_FEL,UART0_PORT_F
[/code]
This stops u-boot from trying to initialize the SD card, and then enables FEL mode based USB booting and also enables the UART pins on the SD card. 
# hacking script.bin
The [ microSD breakout page][59446] provides the changes needed to a .fex file to be able to do this. 
# Build kernel
Against defconfig, in order to get any UART output at all on this device, i needed to change the following: 
[code] 
    @@ -315,7 +315,7 @@
     #
     # Allwinner's sunxi options
     #
    -CONFIG_SW_DEBUG_UART=1
    +CONFIG_SW_DEBUG_UART=0
     CONFIG_SUNXI_MULTIPLATFORM=y
     CONFIG_SUNXI_MALI_RESERVED_MEM=y
     CONFIG_SUNXI_SCALING_MIN=60
    
[/code]
It also helped to enable early printk: 
[code] 
    @@ -2087,7 +2087,7 @@
     CONFIG_DEBUG_LL_UART_NONE=y
     # CONFIG_DEBUG_ICEDCC is not set
     # CONFIG_DEBUG_SEMIHOSTING is not set
    -# CONFIG_EARLY_PRINTK is not set
    +CONFIG_EARLY_PRINTK=y
     # CONFIG_OC_ETM is not set
     
     #
    
[/code]
Now usbboot was happily starting and booting a kernel with full uart output. 
# Goal
The boot.cmd bits needed are probably the following: 
[code] 
    setenv bootargs console=ttyS0,115200 console=tty0 root=/dev/nfs nfsroot=192.168.4.1:/mnt ip=192.168.4.2:192.168.4.1:192.168.4.1:255.255.255.0:gadget:usb0:off nfsrootdebug rootwait panic=10 ${extra}
    bootm 0x44000000
    
[/code]
Not that, apart from the nfsroot stuff, the bootm is a different address from all the other booting we do, as the usbboot script loads the kernel at 0x44000000 instead of 0x48000000. 
# Result
None really. 
I had created a rescue sd for this device before, and along the way i figured out what was wrong with it. So i only got halfway and never got to fully run nfsroot. The rest is documented in the hope that someone will be able to make use of it some day, and then perhaps turn this into a properly clean howto.
