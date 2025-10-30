# Colorfly e708q1
Colorfly e708q1  
---  
[![IMG 1009.PNG][13142]][13143]  
Manufacturer |  [www.colorfly.eu][13144]  
Dimensions |  190 (H) x 113 (W) x 7.6 (D) mm   
Release Date |  September 2013   
Website |  [Official E708 Q1 Datasheet (Link is dead)][13145]  
Specifications   
SoC |  [A31s][13146] Allwinner A31s-up to 1 GHz Quad-Core Cortex-A7   
DRAM |  ELPIA J4216BBBG-GN-F (2x512mb ) DDR3 SDRAM 1GB   
NAND |  Intel I29F64G08AAMEI 8GB   
Power |  DC 5V⎓2A  
3.7V 2300Mha Li-Po battery   
Features   
LCD |  1200x800 (7" 16:9 edge-lit)   
Touchscreen |  Googix GT911 5-finger capacitive or Ilitek ILI2139 10-finger capacitive   
Video |  HDMI ver B   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([RTL8188EU@usb:0bda:8179][13147])  
_no bluetooth_  
Storage |  µSD   
USB |  1x USB2.0 OTG   
Camera |  0.3MP front camera ([GC0308][13148])  
_none on rear side_  
Other |  Accelerometer STK8313   
Headers |  none   
This page needs to be properly filled according to the [New Device Howto][13149] and the [New Device Page guide][13150].
## Contents
  * [1 Identification][13151]
  * [2 Tips, Tricks, Caveats][13152]
    * [2.1 Boot from SDCard mode][13153]
    * [2.2 ADB][13154]
    * [2.3 Recovery mode][13155]
  * [3 Device disassembly (voids warranty)][13156]
    * [3.1 Adding a serial port][13157]
  * [4 Pictures][13158]
  * [5 Also known as][13159]
  * [6 See also][13160]
    * [6.1 Manufacturer images][13161]

# Identification
On the back of the device, the following is printed: 
(Colorfly)
7" TABLET PC
E708 Q1   
5.0V ⎓ 2.0 A Wi-Fi   
Colorfly GmbH 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## Boot from SDCard mode
**How to prepare and Boot from MicroUSB:**
**1.Zero the beginning of the SD card:**
[code] 
      dd if=/dev/zero of=/dev/sdX bs=1M count=8
    
[/code]
**2.Start fdisk to partition the SD card:**
[code] 
         2.1-fdisk /dev/sdX
             At the fdisk prompt, delete old partitions and create a new one:
             Type o. This will clear out any partitions on the drive.
             Type p to list partitions. There should be no partitions left.
             Now type n, then p for primary, 1 for the first partition on the drive,
             2048 for the first sector, and then press ENTER to accept the default last sector.
             Write the partition table and exit by typing w.
         2.2-Create and mount the ext4 filesystem:
              mkfs.ext4 /dev/sdX1
              mkdir mnt
              mount /dev/sdX1 mnt
         2.3-Download and extract the root filesystem (for example, arch linux):
             wget <http://os.archlinuxarm.org/os/ArchLinuxARM-armv7-latest.tar.gz>
             bsdtar -xpf ArchLinuxARM-armv7-latest.tar.gz -C /mnt
             sync
             umount /mnt
    
[/code]
**3.Install the U-Boot bootloader:**
[code] 
         [Download git form denx.de:][13162]
              Edit sun6i-a31s-colorfly-e708-q1.dts to enable axp22x battery poweb:
                      At the end of file add:
                         _& axp22x { backup = <3000000 200>;   };_                     
             Next how to compile U-Boot:
             1-Configure u.boot for colorfly e708 
             make CROSS_COMPILE=arm-linux-gnueabihf- colorfly_e708_q1_defconfig
             2-If necessary configure sources:
             make CROSS_COMPILE=arm-linux-gnueabihf- menuconfig 
             3-Compile u-Boot
             make CROSS_COMPILE=arm-linux-gnueabihf- 
             4-Install U-BOOT on MicroSD boot sectors:
             dd if=u-boot-sunxi-with-spl.bin of=/dev/sdb bs=1024 seek=8
             5-Copy sun6i-a31s-colorfly-e708-q1.dtb (from ./arch/arm/dts/sun6i-a31s-colorfly-e708-q1.dtb) 
               to /mnt/boot (partition /dev/sdb1)
    
[/code]
**4.boot.scr** -boot.scr 
[code] 
                 1.mount /dev/sdb1  /mnt/
                 2.boot.cmd (source):
                 part uuid ${devtype} ${devnum}:${bootpart} uuid
                 setenv bootargs console=${console} root=PARTUUID=${uuid} rw rootwait
                 if load ${devtype} ${devnum}:${bootpart} ${kernel_addr_r} /boot/zImage; then
                   if load ${devtype} ${devnum}:${bootpart} ${fdt_addr_r} /boot/dtbs/${fdtfile}; then
                     if load ${devtype} ${devnum}:${bootpart} ${ramdisk_addr_r} /boot/initramfs-linux.img; then
                         bootz ${kernel_addr_r} ${ramdisk_addr_r}:${filesize} ${fdt_addr_r};
                 else
                 bootz ${kernel_addr_r} - ${fdt_addr_r};
                    fi;
                  fi;
                 fi                       
                3.compile boot.cmd:
                       mkimage -C none -A arm -T script -d boot.cmd boot.scr
                4. Copy boot.scr to /mnt/boot
                       cp boot.scr /mnt/boot
                5. Umount /mnt 
                   sync
                   umount /mnt
    
[/code]
**5\. How to compile linux kernel**
Compile zImage with this options : 
Download kernel: git clone <git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git>
[code] 
                1.Prepare compile kernel to suni allwinner:
                     make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- sunxi_defconfig
                2.Modify kernel propertiers(menu config):
                     make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig
                       2.1Kernel options (menu config) you can select this as modules(M):
                           Wifi:
                                1-Networking support -->Wireless -->Cfg80211
                                2-Device drivers -->Network Device Support-->wireles Lan
                                3-Device drivers -->Staging drivers--> RTL8188                             
                                 TouchScreen:
                                    -Device drivers -->Imput devices---> Goodix 911   
                                 OTG, filesystem (NTFS, DOS)..:
                                     1-Device drivers -->USB suport---> Otg, Mass storage, etc..
                                     2-File systems--> NTFS, VFAT...
               3.Compile Kernel:
                 ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- make zImage 
                  (copy to microsd partitrion, in my case sdb1 (vfat) de ./arch/arm/boot/zImage to /mnt/boot/zImage) 
                4.Install Modules:
                   mount second microsd partition to /mnt (mount /dev/sdb2 /mnt)
                   ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf-  INSTALL_MOD_PATH=/mnt  make modules modules_install
                   Now we have new modules in /mnt/lib/modules/4.6.0-rc2/...
                 5-Sync and umount /mnt:
                   sync
                   umount /mnt
            
    
[/code]
**NOTE** : In order to test battery status and charge (at now not soported at mailine kernel)download a modificied mainline kernel from <https://github.com/micile/linux-sunxi/tree/AXP_Battery> and compile zImage and modules witch sunxi_defconfig options. 
Insert the micro SD card into the colorfly e708 and apply 5V power. The default root password is root. 
**6\. In order to calibrate touch screen, X11:**
[code] 
          6.1. Edit 10-evdev.conf 
            vim /usr/share/X11/xorg.conf.d/10-evdev.conf 
          6.2. Add this lines:
              Section "InputClass"
                     Identifier      "calibration"
                     MatchProduct    "Goodix Capacitive TouchScreen"
                     Option  "Calibration"   "4 1200 800 -1"
                     Option  "SwapAxes"      "1"
              EndSection
    
[/code]
Devices on boad
    
[code] 
    
    # lsusb
    Bus 001 Device 002: ID 0bda:0179 Realtek Semiconductor Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    
    
[/code]
Info about CPU "cat /proc/cpuinfo"
[code] 
    processor       : 0
    model name      : ARMv7 Processor rev 3 (v7l)
    BogoMIPS        : 48.00
    Features        : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xc07
    CPU revision    : 3
    
    processor       : 1
    model name      : ARMv7 Processor rev 3 (v7l)
    BogoMIPS        : 48.00
    Features        : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xc07
    CPU revision    : 3
    
    processor       : 2
    model name      : ARMv7 Processor rev 3 (v7l)
    BogoMIPS        : 48.00
    Features        : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xc07
    CPU revision    : 3
    
    processor       : 3
    model name      : ARMv7 Processor rev 3 (v7l)
    BogoMIPS        : 48.00
    Features        : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xc07
    CPU revision    : 3
    
    Hardware        : Allwinner sun6i (A31) Family
    Revision        : 0000
    Serial          : 16524251080XXXXX
    
    
[/code]
## ADB
This device does not have root access enabled by default. If USB debugging is enabled in settings on the tablet, run 
[code] 
    echo -e '0x1f3a\n0x1002' >> .android/adb_usb.ini 
    sudo bash -c 'echo SUBSYSTEM==\"usb\", ATTR{idVendor}==\"1f3a\", ATTRS{idProduct}==\"1002\", MODE=\"0666\", \
      GROUP=\"plugdev\", SYMLINK+=\"android%n\" >> /etc/udev/rules.d/51-android.rules'
    udevadm control --reload-rules
    
[/code]
in order to make 
[code] 
    adb devices
    adb shell
    ..
    
[/code]
work. 
## Recovery mode
  1. Power off the device
  2. Hold down the vol+ button
  3. Power on the device
  4. Release the vol+ button when recovery starts

# Device disassembly (voids warranty)
The back cover uses snap-ins, but sits very tight on the front frame. Where the volume and power buttons sit, the plastic is so thin that it's very likely to break, when trying to remove the back cover. To start opening, be sure to pick a spot about one _mm_ below the display at a place where no buttons or connection holes are situated. Remember that you will loose warranty doing this with most vendors. 
## Adding a serial port
Howto needed: Does the [N7 Pro serial port guide][13163] to add a serial port work for this device too!? 
# Pictures
  * [![IMG 1008.PNG][13164]][13165]
  * [![20160312 234359702 iOS.jpg][13166]][13167]
  * [![20160311 155843735 iOS.jpg][13168]][13169]
  * [![E708 stress test.PNG][13170]][13171]

# Also known as
Unofficial
    
  * Since there are no firmware files publicly available to this date from Intenso, I've tried a couple of firmware images from different vendors listed on [chinagadgetsreviews.blogspot.de][13172] to repair a non-booting E708 that just showed (Intenso)-Logo on start. Most of the firmwares from other vendors show black screens, have wrong display resolutions or non-working sound and, unfortunately, non-working touchscreen input.

  * _Caution:_ If your QE708 is working fine, **do not** flash the below, but rather try to extract the stock rom firmware with sunxi-tools above and have someone with a broken one test your image.

.............................................................................. [Discussion, firmware, etc][13173]
  * [[1]][13174] has some firmwares. They're stored on Baidu NetDisk. (The webpage and the netdisk are both in Chinese)

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
