# How to boot the A10 or A20 over the network
## Contents
  * [1 Prerequisites][24261]
  * [2 Settin up network boot][24262]
  * [3 Network configuration][24263]
    * [3.1 Manual][24264]
    * [3.2 Automatic][24265]
  * [4 TFTP booting][24266]
  * [5 Booting from an NFS share][24267]
    * [5.1 Ubuntu 10.04][24268]
  * [6 Web resources][24269]

## Prerequisites
You'll need a Linux box, a microSD card, a card reader and a serial console adapter for this tutorial. 
  * [Build U-Boot][24270]
  * Prepare an SD Card

    For network booting it is enough to copy only the U-Boot to the SD card, so follow instructions in [Bootable_SD_card#Cleaning][24271] and [Bootable SD card#Bootloader][24272].
  * Linux Kernel, you can use either legacy but featurefull sunxi-3.4, or mainline kernel which has basic support only.
  * Root file system, or rootfs.

## Settin up network boot
SD Card is now ready to take for a spin. Put it into your board and connect your serial console and fire up a terminal on your host PC so you can interact with u-boot. Now power on the board. After booting you should see something like this: 
[code] 
       U-Boot SPL 2013.01-05621-gb7b6374 (Jan 18 2013 - 23:01:07)
       Board: Cubieboard
       DRAM: 1024MB
       SUNXI SD/MMC: 0
         
    
         
    
       U-Boot 2013.01-05621-gb7b6374 (Jan 18 2013 - 23:01:07) Allwinner Technology
         
    
       CPU:   SUNXI Family
       Board: Cubieboard 
       I2C:   ready
       DRAM:  1 GiB
       MMC:   SUNXI SD/MMC: 0
       In:    serial
       Out:   serial
       Err:   serial
       Net:   wemac
       Hit any key to stop autoboot:  0
       sun4i#
    
[/code]
The autoboot is stopped because we don't have any partitions on the SD card yet so it'll not succeed booting. 
## Network configuration
  * Let's bring up the ethernet interface.

    
  * We must set the ethaddr variable to the MAC address of the NIC on the board. For testing purposes you can use something dummy like this:

[code] 
       sun4i# setenv ethaddr 12:34:56:78:99:aa
    
[/code]
    but please don't do this in production environment. Next you can choose between manual or automatic setup.
### Manual
[code] 
    sun4i# setenv netmask <netmask>
    sun4i# setenv dnsip <dns>
    sun4i# setenv gatewayip <gateway>
    sun4i# setenv ipaddr <ip-address>
    
[/code]
### Automatic
    It is needed to also issue
[code] 
     sun4i# setenv autoload no
    
[/code]
    because by default once you execute the next 'dhcp' command and autoload is enabled it will automatically try to load an image from TFTP, named as the IP address in hex followed by .img, which is not what is wanted.
[code] 
    sun4i# dhcp
    
[/code]
Now you're ready to try out TFTP or NFS. In either case you first need to set the IP of the server 
[code] 
    sun4i# setenv serverip <server-ip>
    
[/code]
Also it is recommended to save your environment to the MMC card, so later or if something goes wrong with booting, you will not need to retype any of the previous commands. 
[code] 
    sun4i# saveenv
    
[/code]
## TFTP booting
Let's say you now have a TFTP server running on the IP address set above and serving files and have a kernel named 'uImage' and '<your-board>.dtb' (or 'script.bin') in the server file system. 
mainline kernel  | sunxi-3.4 kernel   
---|---
[code] 
     tftp 0x46000000 uImage
     tftp 0x49000000 <your-board>.dtb
     env set fdt_high ffffffff
     bootm 0x46000000 - 0x49000000
    
[/code]  
| 
[code] 
     setenv bootm_boot_mode sec
     tftp 0x42000000 uImage
     tftp 0x43000000 script.bin
     bootm 0x42000000
    
[/code]  
## Booting from an NFS share
    
  * You have to compile a custom kernel because you have to enable root NFS support to work with NFS mounted root filesystems. Follow the build instructions described here: [http://linux-sunxi.org/Linux#Building][24273] but before executing the second build command modify .config file in the kernel's source directory to contain the following lines:

[code] 
       CONFIG_IP_PNP=y
       CONFIG_ROOT_NFS=y
    
[/code]
    You might get some question from the next build command but you just have to say yes when it asks for the values above. You'll find the built kernel at arch/boot/uImage if you did everything right.
  * Prepare NFS share

### Ubuntu 10.04
    
  * You have to install the required package

[code] 
       apt-get install nfs-kernel-server 
    
[/code]
    
  * Create a share directory.

[code] 
       mkdir -p /var/nfsexport/arch/
    
[/code]
    
  * Edit /etc/exports to include this directory. Put the following line to the end:

[code] 
       /var/nfsexport *(rw,sync,no_root_squash,no_subtree_check)
    
[/code]
    
  * Finally restart the daemon

[code] 
       /etc/init.d/nfs-kernel-server restart
    
[/code]
  * Copy required files

    
  * Copy uImage from the first step to /var/nfsexport/arch/
  * We have to build a script.bin file for the kernel to work properly. Clone the <https://github.com/linux-sunxi/sunxi-boards> and <https://github.com/linux-sunxi/sunxi-tools> repository and compile sunxi tools (make). After that you have to convert your boards fex file with the fex2bin you've just built. In my case:

[code] 
       ./sunxi-tools/fex2bin sunxi-boards/sys_config/a10/cubieboard.fex > script.bin
    
[/code]
    
  * Copy script.bin next to the kernel
  * Download and extract Arch rootfs image. I'm using the MeleA100 image from the Arch ARM Linux site. Extract it to the NFS export folder:

[code] 
      wget <http://archlinuxarm.org/os/ArchLinuxARM-sun4i-latest.tar.gz>
      tar xzf ArchLinuxARM-sun4i-latest.tar.gz -C /var/nfsexport/arch/
    
[/code]
  * Configure U-Boot

    
  * Boot into U-Boot with the serial console attached and halt autoboot by pressing a key, then

[code] 
       sun4i# setenv nfsroot ${serverip}:/var/nfsexport/arch
       sun4i# setenv bootcmd "nfs 0x43000000 ${nfsroot}/script.bin; nfs 0x48000000 ${nfsroot}/uImage; bootm 0x48000000"
       sun4i# setenv bootargs "console=ttyS0,115200 root=/dev/nfs nfsroot=${nfsroot} ip=${ipaddr}:${serverip}:${gatewayip}:${netmask}:${hostname}:eth0"
       saveenv
    
[/code]
    
  * Reset the board

  * Known bugs if using Arch Linux rootfs:

    
  * Reboot is not working; network interface is stopped but Arch wants to write something to the NFS mount which can't be done after that.
  * No output on HDMI but you can interact with Arch through the serial console or by using an SSH client and connect to the IP you've specified in uboot.

## Web resources
  * This wiki page is quite useful for explaining the kernel booting with U-Boot: <http://processors.wiki.ti.com/index.php/Booting_Linux_kernel_using_U-Boot>  

  * You can read more about mkimage's usage here: <http://www.linuxfordevices.com/c/a/Linux-For-Devices-Articles/Introduction-to-Das-UBoot-the-universal-open-source-bootloader/>

  * You can follow this tutorial to get a TFTP server in Ubuntu: <http://www.davidsudjiman.info/2006/03/27/installing-and-setting-tftpd-in-ubuntu/> It can be installed to VM and set Virtualbox to bridge the internal NIC adapter directly to my local network where the Cubieboard is also connected. This way you can have a straight VM to Cubieboard development environment.
