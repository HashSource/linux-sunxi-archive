# USB Gadget/Mass storage
< [USB Gadget][57236]
 
## Contents
  * [1 USB storage support][57239]
    * [1.1 Kernel support][57240]
    * [1.2 Preparing shared storage device][57241]
      * [1.2.1 Creating a sparse file][57242]
      * [1.2.2 Partitioning and formatting sparse file][57243]
        * [1.2.2.1 Create a single partition][57244]
        * [1.2.2.2 Find partition offset][57245]
        * [1.2.2.3 Set up loop device][57246]
        * [1.2.2.4 Format device][57247]
        * [1.2.2.5 Test device][57248]
        * [1.2.2.6 Release device][57249]
    * [1.3 Exporting mass storage / Loading the driver (on the device)][57250]
    * [1.4 Emulating a USB CD-ROM][57251]

# USB storage support
This allows your devices act as a USB mass storage like external hard drive or thumb drive. 
## Kernel support
Currently, the g_mass_storage module is not compiled as part of default kernel configuration. 
To enable this, follow same kernel building information as previous section [USB Ethernet support][57252] but instead of compiling "Ethernet Gadget", select the following to "m": 
[code] 
    Device Drivers  --->
    	USB support  --->
    		USB Gadget Support  --->
    			<M>     Mass Storage Gadget
    
[/code]
Please set **dr_mode = "otg"** in .dts file and check USB mode in kernel. 
[code] 
    Device Drivers  --->
    	USB support  --->
    		Inventra Highspeed Dual Role Controller  --->
    			MUSB Mode Selection  --->
    				<X>	Dual Role Mode
    
[/code]
You can now continue following [manual build howto][57253] to continue kernel compilation and installation. 
## Preparing shared storage device
See "[Backing Storage for the Mass Storage Gadget][57254]" for full instructions and recommendations. 
Be aware that shared storage cannot be used in "read write" mode if both systems (device and host) are using it at same time except if you accept to corrupt your data... 
An existing physical partition or a logical volume can be used as shared storage device; another option is to use a flat file as shared storage. 
[Here][57255] you can find useful some information. 
### Creating a sparse file
Use "dd" command's "count" and "seek" options to create a 1GB file that will not use storage until it is used: 
[code] 
    # dd if=/dev/zero of=/mass_storage bs=1M seek=1024 count=0
    # ls -l /mass_storage 
    -rw-r--r-- 1 root root 1073741824 Feb 15 16:40 /mass_storage
    # du -hs /mass_storage 
    0       /mass_storage
    
[/code]
### Partitioning and formatting sparse file
To be recognized by most Operating Systems, create a single FAT type partition and format it as DOS filesystem using Linux loop device driver. 
#### Create a single partition
[code] 
    # cat <<EOT | sfdisk -L -uS /mass_storage 
    ,,c
    EOT
    
[/code]
#### Find partition offset
[code] 
    # fdisk -lu /mass_storage 
    
    Disk /mass_storage: 1073 MB, 1073741824 bytes
    139 heads, 8 sectors/track, 1885 cylinders, total 2097152 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00000000
    
    	Device Boot      Start         End      Blocks   Id  System
    /mass_storage1               1     2097151     1048575+   c  W95 FAT32 (LBA)
    
[/code]
First partition starts at first sector: offset = 1 * 512 = 512 bytes 
#### Set up loop device
[code] 
    # losetup -o512 /dev/loop0 /mass_storage
    # losetup -a
    /dev/loop0: [b302]:14867 (/mass_storage), offset 512
    
[/code]
#### Format device
[code] 
    # apt-get install dosfstools
    # mkdosfs /dev/loop0
    
[/code]
  

#### Test device
[code] 
    # mount -t vfat /dev/loop0 /mnt/
    # df -h /mnt
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/loop0     1022M  4.0K 1022M   1% /mnt
    # mount | grep mnt
    /dev/loop0 on /mnt type vfat (rw,relatime,fmask=0022,dmask=0022,codepage=cp437,iocharset=ascii,shortname=mixed,errors=remount-ro)
    
[/code]
#### Release device
[code] 
    # umount  /mnt/
    # losetup -d /dev/loop0 
    # losetup -a
    
[/code]
As we can see below, 1GB sparse file is only using 2.1MB storage (size of filesystem metadata): 
[code] 
    # du -sh /mass_storage 
    2.1M    /mass_storage
    # ls -lh /mass_storage 
    -rw-r--r-- 1 root root 1.0G Feb 15 16:54 /mass_storage
    
[/code]
## Exporting mass storage / Loading the driver (on the device)
It looks like g_mass_storage conflicts with g_ether, remove g_ether first (if previously loaded): 
[code] 
    # modprobe -r g_ether
    
[/code]
Load g_mass_storage specifying storage to share (can also be a physical partition or a logical volume): 
[code] 
    # modprobe g_mass_storage file=/mass_storage
    
[/code]
We can now plug device to another host and use it as USB connected storage. 
Notes: Surprisingly it works well my Mac OS hosts (device automatically appears in Finder, I can copy and read files) but not with my Linux hosts (device appears and disappears constantly and cannot be mounted). Not tested with Windows hosts. 
## Emulating a USB CD-ROM
The _g_mass_storage_ module can also present an optical drive to the USB host. For this, your backing storage should be a suitable filesystem image - usually an .ISO file. Pass a "cdrom" module option like this: 
[code] 
    # modprobe g_mass_storage file=/path/to/your-image-file.iso cdrom=y
    
[/code]
(This can be useful with old PCs where the BIOS may have trouble starting from USB sticks, but supports booting via USB-CDROM.) 
[![Sticky-note-pin.png][57256]][57257] _Note:_ As of Linux v4.7-rc2, the _g_mass_storage_ driver can only emulate CD-ROM drives, not DVD-ROMs. 
    That means some restrictions, especially a hardcoded limit on the size of a backing (.iso) file. In case the file size exceeds 1152000 2KiB blocks (approx. 2.36GB / 2.2GiB), the driver will complain "_file too big_ " and limit the usable range (sector count). If the filesystem driver on the USB host requests any sector beyond that, it will encounter I/O errors ("_attempt to access beyond end of device_ ").
    In order to use larger images and properly emulate DVD media, the _g_mass_storage_ would have to be extended. Some ideas and patches for that have been around for a while, e.g. <https://lkml.org/lkml/2015/3/7/388> and <http://linuxehacking.blogspot.de/2013/07/how-to-emulatore-dvd-rom-hardware-usb.html>.
