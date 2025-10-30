# Cubieboard/FAQ
< [Cubieboard][13794]
 
Frequently Asked Questions 
## Contents
  * [1 Background][13797]
    * [1.1 Who created Cubieboard and behind it?][13798]
  * [2 Distribution][13799]
    * [2.1 Where can I get one?][13800]
    * [2.2 I want to place a large order][13801]
    * [2.3 I want to distribute Cubieboard in my area][13802]
  * [3 Features and Specifications][13803]
    * [3.1 How can I tell how much RAM I have?][13804]
    * [3.2 Is the processor Dual Core?][13805]
    * [3.3 Is it possible to connect a SSD drive on Cubieboard?][13806]
    * [3.4 Does the Cubieboard support SATA port multipliers and what is the max limit of a SATA hard disk drive?][13807]
    * [3.5 There is a SATA connector. What harddrives will work?][13808]
    * [3.6 I attached the SATA disk. It spins up but when I start using the disk it would spin down repeatedly and/or cause errors in the logs. What is going on?][13809]
    * [3.7 What are the power specs for Cubieboard?][13810]
    * [3.8 Is it possible to power the Cubieboard via USB?][13811]
    * [3.9 What power supply sould I use for cubieboard?][13812]
    * [3.10 Does Cubieboard support SDHC memory cards?][13813]
    * [3.11 Looks like there are two 3.5mm jacks. Are the HP out and Mic in?][13814]
    * [3.12 I notice there is an IR interface on Cubieboard. How do I use it?][13815]
    * [3.13 What is difference between Cubieboard and Cubieboard2?][13816]
    * [3.14 What are new features in CubieTruck?][13817]
  * [4 OS and Software][13818]
    * [4.1 OK, I have my Cubieboard now! Where is a good place to start?][13819]
    * [4.2 What software does Cubieboard come with?][13820]
    * [4.3 Is there a link to the original images that have come preinstalled in the Cubieboard NAND memory, in case I want to re-install?][13821]
    * [4.4 How can I take backup of NAND memory?][13822]
    * [4.5 How can I flash linux onto NAND?][13823]
    * [4.6 I really don't care about Android!! I want to start with a real Linux on my SD-card][13824]
    * [4.7 Can I install Cubieboard image on Cubieboard2?][13825]
    * [4.8 What is difference between LiveSuit and PhoenixSuit?][13826]
  * [5 Display and Sound][13827]
    * [5.1 How do I get the monitor to work on the Cubieboard?][13828]
    * [5.2 What displays does cubieboard support? Can I connect my VGA/DVI/HDMI/LVDS/DP/.. display to cubieboard?][13829]
    * [5.3 There is no sound coming from Android on Cubieboard][13830]
  * [6 Connectivity][13831]
    * [6.1 What are the serial port settings?][13832]
    * [6.2 What is the spacing between the contacts of the pin headers?][13833]

## Background
### Who created Cubieboard and behind it?
    Benn, Tom Cubie and some of his friends.
## Distribution
### Where can I get one?
    See [The cubieboard site][13834]
### I want to place a large order
    Send email to [[email protected]][13835]
### I want to distribute Cubieboard in my area
    Send email to [[email protected]][13835]
## Features and Specifications
### How can I tell how much RAM I have?
    Look at the ID on the chips themselves. Then, if there are two chips mounted on the board and the description says 256X16 then **256Mbit x 16 = 512MB** per chip. If your Cubieboard has two of those chips, then the total memory is 1GB. Cubietruck has 2GB ram.
### Is the processor Dual Core?
    It's a Cortex-A8, therefore it's a single core. Cubieboard2 and Cubietruck has dual-core Cortex-A7 processor.
### Is it possible to connect a SSD drive on Cubieboard?
    Yes
### Does the Cubieboard support SATA port multipliers and what is the max limit of a SATA hard disk drive?
    A10 does not support port multipliers. A20 does support it in the mainline kernel since v3.19, but it's mutually exclusive with single drive mode, requiring the flag [enable_pmp=1][13836] for the ahci-sunxi module. Storage limit is per SATA 2.0 specifications, 48 bit LBA addressing or 128 PiB.
    To connect more disks, you would need a SATA cabinet that does RAID by itself. So the multiplier needs to emulate a single drive. The host system Cubieboard then sees only a single SATA disk, with whatever capacity your chosen RAID level gives you.
### There is a SATA connector. What harddrives will work?
    The onboard 5V SATA power connector is only capable to power 2.5" hard disk drives.
    For [3.5" HDD usage][13837] (and some very rare 2.5" disks) you need a power supply that supplies 5V + 12V, and power the cubieboard from 5V and HDD from 5v + 12v.
    The option of powering both separately from the same power supply is always possible.
### I attached the SATA disk. It spins up but when I start using the disk it would spin down repeatedly and/or cause errors in the logs. What is going on?
    Cubieboard _should_ be able to power a SATA disk if you give it enough power. I used a few SSDs and even one spinning disk without problems. However, I use 5V 6A PSU and not a cheap PSP PSU to power the board. I also found a disk that reproduces the dreaded spindown issue - it's an old Fujitsu MHV2080B. It is rated 5V 0.6A but the moment you start writing to the disk extensively it spins down when powered from cubieboard. Powered directly from the PSU using another barrel plug it works fine.
    The resistance of the included power cable for the board which came with the Cubieboard (or the resistance of its connector) seems to be quite high. I measured a voltage drop of >.3V between the USB connector at the PSU and the +5V and ground pads on the board. Together with the voltage drop across the diodes in the power circuit the voltage may get too low for some drives. Soldering the black/red wires of a cut-off USB cable directly to the ground/+5V pads on the board improved the situation for me. Powering the board thru the USB OTG port using a good (and short!) cable with a mini-USB connector may be worth a try.
### What are the power specs for Cubieboard?
    The Cubieboard requires a regulated 5V DC, 2A power supply with a 4.0mm (external diameter) x 1.7mm (internal diameter) barrel plug. The outside of the plug is the ground.
    A 500mA supply is sufficient if you do not attach a SATA hard disk to the Cubieboard.
    Your Cubieboard package may have a USB to DC power cable, so you can connect to your computer's USB port and power the Cubieboard.
    Please note that if you then connect USB peripherals to your Cubieboard, then these may require more power than the standard 500mA that a PC USB port provides.
### Is it possible to power the Cubieboard via USB?
    Yes, you can connect the USB cable to the OTG miniUSB port on the Cubieboard.
    Generally, you can get the power from the USB port of your computer (at 500mA, according to the USB specifications), or use a USB power supply like those available for mobile phones.
### What power supply sould I use for cubieboard?
    Any 5V and at least 0.5A (or 1A for cubieboard2) power supply should work. You can use common USB chargers or powered USB hubs with the USB power cable included with the board. If you connect many USB devices or a SATA disk you may need full 5V 2A or even power some of the devices directly from the PSU rather than through cubieboard.
    While Sony PSP power supply is rated 5V 2A and provides the correct barrel plug to connect into cubieboard it is reported that many PSUs marketed as Sony PSP PSU are very low quality and provide way less than their rated current.
### Does Cubieboard support SDHC memory cards?
    Yes, SDHC memory cards are supported by all A10-based devices.
### Looks like there are two 3.5mm jacks. Are the HP out and Mic in?
    Board markings says HP (HeadPhone) on the top one and LineIn on the bottom one. Note that a Line In is different from a Mic In. You need additional hardware to convert a Line In into a Mic In.
### I notice there is an IR interface on Cubieboard. How do I use it?
    Please refer to the [A10 User Manual][13838] section 19 IR Interface, the driver is already in the kernel, an input device that can work with normal IR remote. IR test is one of the tests of the Cubieboard before shipping. You can test remote using command 'getevent'. You should get multiple similar lines of these '/dev/input/event4: 0001 000c 00000001'. You can redefine keys by editing file ' /system/usr/keylayout/sun4i-ir.kl'. Please refer this post [IR remote on keyboard][13839] for more details.
### What is difference between Cubieboard and Cubieboard2?
    Cubieboard2 has dual core Cortex-A7 cpu and dual core Mali-400MP2 gpu which bring performance enhancement. It contains A20 SoC which brings stable Jelly Beans support. A20 is pin-to-pin compatible with A10. So, everything else on cubieboard remains as it is.
### What are new features in CubieTruck?
    Cubietruck is Allwinner A20 dual core Cortex-A7 has more ram(2 GB) and more nand storage(8 GB). It has builtin VGA port and Wifi+Bluetooth. It has Gbps ethernet. It also has rtc to keep up with time when it has no power supply. It runs latest version of android.(JB 4.2.2)
## OS and Software
### OK, I have my Cubieboard now! Where is a good place to start?
    CNXSoft has written a great Quick Start Guide [here.][13840] There is a [First Steps][13841] page on this Wiki. You can join the [Group Page][13842] and the Google+ [Community][13843]
### What software does Cubieboard come with?
    There is a screen of an application that is run during production to verify the board.
    Cubieboard is meant to customize and replace the default OS with whatever you need for your use the board. It is an open platform for you to meld into your liking.
    All Linux distributions which support ARM can run on the cubieboard. It ships with an OS based on Buildroot to give you full control to tinker with every bit, but you also have the option to run some more mainstream OS like Fedora, Debian, Arch, Ubuntu or any other ARM Linux distribution. It also runs Android if you are interested in exploring that.
    The new shipped Cubieboards (Indiegogo and latter) have ready to use Android ICS installed in the NAND memory.
### Is there a link to the original images that have come preinstalled in the Cubieboard NAND memory, in case I want to re-install?
    See <http://dl.cubieboard.org/software/android/> for those images.
### How can I take backup of NAND memory?
    Create sdcard with any linux distribution like Debian or Fedora. Boot from sdcard and run this command
    # dd if=/dev/nand conv=sync,noerror bs=64K | gzip -c -9 > /nand.ddimg.gz
    You can restore it using command
    # cd / ; gunzip nand.ddimg.gz; dd if=/nand.ddimg conv=sync,noerror bs=64K of=/dev/nand
### How can I flash linux onto NAND?
    The fastest way is to use the PIMP_MY_MELE utility from guillaume. He has Ubuntu and Debian distributions with this utility [here][13844] and [here][13845] For more detailed, "roll-your-own" instructions, see [this thread][13846] in the miniand.com forums.
### I really don't care about Android!! I want to start with a real Linux on my SD-card
    If you are looking for different ready-to-run linux-based images build for your Cubieboard you can find them here: <http://linux-sunxi.org/Bootable_OS_images>
### Can I install Cubieboard image on Cubieboard2?
    No. Cubieboard2 has slightly upgraded hardware. So, it need different kernel(rootfs can be shared). You can download cubieboard2 images from <http://cubieboard.org/download>
### What is difference between LiveSuit and PhoenixSuit?
    PhoenixSuit is actually LiveSuit2.0. So, it is upgraded version of Livesuit.
## Display and Sound
### How do I get the monitor to work on the Cubieboard?
    You really need an HDMI monitor capable of either 1280x720 (720p) or 1920x1080 (1080p) for use with the pre-installed image.
    Newer kernels should support any monitor with valid EDID.
### What displays does cubieboard support? Can I connect my VGA/DVI/HDMI/LVDS/DP/.. display to cubieboard?
    While A10 comes with support for VGA/TV/LVDS/HDMI only HDMI connetor is actualy provided on cubieboard out of the box. HDMI is DVI compatible but you need recent kernel to use most DVI screens. The pre-installed android kernel is configured for 720p digital TV mode. VGA/LVDS/TV outputs are available on the 2mm headers. To make use of them you need to add the resistors/buffers and connector required by the interface you want to use. Cubieboard only supports two displays at the same time and some pins are shared between VGA/LVDS/TV. You have to provide the interface hardware *and* properly configure the pins to which it is attached.
### There is no sound coming from Android on Cubieboard
    Select correct mode in Settings -> Sound -> Audio output mode.
## Connectivity
### What are the serial port settings?
    See [Cubieboard/TTL#Configuration][13847]
### What is the spacing between the contacts of the pin headers?
    2.0mm
