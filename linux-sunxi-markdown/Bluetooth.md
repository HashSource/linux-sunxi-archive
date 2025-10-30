# Bluetooth
## Contents
  * [1 Overview of the Bluetooth Stack][10116]
  * [2 User Space][10117]
  * [3 Host Controller Interface (HCI)][10118]
  * [4 HCI Transport Layer][10119]
    * [4.1 UART][10120]
    * [4.2 USB][10121]
    * [4.3 Other][10122]
  * [5 Controller Specific Information][10123]
    * [5.1 AMPAK][10124]
      * [5.1.1 AP6210][10125]
      * [5.1.2 AP6330][10126]
    * [5.2 Broadcom][10127]
      * [5.2.1 BCM20710][10128]
    * [5.3 Realtek][10129]
      * [5.3.1 8723au][10130]
      * [5.3.2 8723bs][10131]

# Overview of the Bluetooth Stack
Bluetooth provides a large number of application [profiles][10132]. Examples are playing audio between devices (A2DP), wireless keyboards and mice (HID) and transferring data wirelessly between devices (FTP, OPP). 
These application profiles work on a stack of [protocols][10133], similar in concept to the networking and USB stacks. For example the Object Push Profile (OPP) uses the OBject EXchange (OBEX) protocol, which uses the Radio Frequency COMMunication (RFCOMM) protocol, which uses the Logical Link Control and Adaptation Protocol (L2CAP), which uses the Host Controller Interface (HCI) protocol, which uses the radio link protocols. 
This can rapidly become a complex area, but the user space tools make this all "just work" for users. It is beyond the scope of this page to configure Bluetooth profiles. 
The focus of this wiki page is on the interface between host and controller. 
# User Space
The collection of user space tools is maintained by the [Bluez][10134] project. Note that the tool chain requires D-Bus. For application development the [D-Bus API is documented in the Bluez source][10135]. 
A contemporary short instruction for CLI usage can be found in the [Archlinux Wiki][10136]. 
# Host Controller Interface (HCI)
The Host Controller Interface is a lower level protocol in the Bluetooth stack. A host is usually a PC, tablet, SBC, phone, etc. A controller is the chip with the Bluetooth radio. Although some simpler Bluetooth devices, such as a headset, may have the host and controller implemented on a single processor. 
The communication layer between host and controller can be over a number of interfaces, for example UART, USB and SPI. 
The purpose of a Bluetooth driver for a sunxi system on chip is to set up the Bluetooth controller ready for user space to provide Bluetooth applications. 
# HCI Transport Layer
This is the physical interface between host and controller. A number of [transport layer drivers][10137] are provided in the Linux kernel and the Kernel's [Kconfig file][10138] for the drivers gives a useful description. 
## UART
The Linux kernel driver is `hci_uart`
This is a serial interface and there are several protocols used, e.g. H4, H5, BCSP. The H4 protocol is probably the most common and uses serial control lines. The H5 protocol is a three-wire protocol so no serial control lines are used. There are also a number of proprietary protocols, BCSP (BlueCore Serial Protocol) being an example. 
The datasheet for the controller and the schematics for the device should be enough to determine which protocol is used. 
## USB
The Linux kernel driver is `btusb`
## Other
Examples are SPI and SDIO. These transport layers do not appear to be used in any devices with AllWinner SoCs. 
# Controller Specific Information
This section contains details on Bluetooth controller chips used alongside sunxi system on chips and how to drive them. A controller chip will need one or more of the following: 
  * Power management, usually wake and sleep
  * Configuration of the transport between host and controller, often over UART, but could also be SPI or USB
  * Copying of controller's firmware to controller on start up
  * Co-ordination on the host with other drivers, e.g. Bluetooth A2DP will also need the audio driver configured

## AMPAK
From Linux 5.2, there's nice clean upstream support for broadcom bluetooth. See <http://lists.infradead.org/pipermail/linux-arm-kernel/2018-November/610954.html> for the full details. If you're adding bluetooth nodes to existing hardware, the quick traps are: 
  * missing the [clocks/clock-names nodes][10139] on the wifi_pwrseq node.
  * thinking that the ["bt-reset-n" signal should be flagged as active low][10140].

Remember, you need kernel config option CONFIG_SERIAL_DEV_BUS to be able to select CONFIG_BT_HCIUART_BCM If you have these wrong, your kernel will keep reporting lines like ```Bluetooth: hci0: command 0x0c03 tx timeout``` 0x0c03 is the standard HCI request to reset the part, so this means your device is not (yet) responsive. Once this is all correct, your next trap will be finding suitable firmware, and getting it named correctly, though fortunately at this point, the kernel will simply tell you. linux-firmware repo has very few of the bluetooth files, your best bet is [armbian's][10141] [repo][10142], though they will all need renaming, because armbian patched all that too. 
### AP6210
The AMPAK AP**6210** combines Broadcom Wifi (BCM433**62**) and Bluetooth 4.0 (BCM207**10**) chips in a single [system in package][10143]. The package exposes only the Bluetooth chip's UART transport layer. Audio is carried over a PCM interface. 
Procedure for Sunxi Linux 3.4 kernel: 
  * [Cubietruck/Bluetooth][10144] \- notes on this Wiki about the Cubietruck that contains an AP6210
  * ["Got bluetooth working on Cubietruck - proof of concept"][10145] \- Arch Linux forum
  * [EddyBeaupre/ap6210][10146] \- GitHub, "Wifi and Bluetooth driver for CubieTruck"

Procedure for mainline Linux kernel: 
  * [phelum/CT_Bluetooth][10147] \- working procedure for Bluetooth with AP6210 using both Linux mainline and 3.4 kernels, still a work in progress and the author is seeking feedback on the [Mailing_list][10148]
  * ["ARM: dts: sun7i: add bluetooth module to CubieTruck DTS"][10149] \- patch as an example DTS file
  * [User_talk:Sehraf][10150] \- Sehraf has notes on an attempt to get the AP6210 working

### AP6330
The AMPAK AP**6330** combines Broadcom Wifi (BCM4330) and Bluetooth 4.0 (BCM40183) chips in a single [system in package][10143]. The package exposes only the Bluetooth chip's UART transport layer. 
## Broadcom
Broadcom provide a [tool][10151] for Linux to configure and test Broadcom Bluetooth chips. The tool source code is licensed under the Apache License 2.0. Binaries are also available for download. This tool can be used to upload firmware to the controller. For example a firmware upload over UART: 
[code] 
    brcm_patchram_plus -d --no2bytes --patchram firmware_file.hcd /dev/ttyS1
    
[/code]
### BCM20710
The BCM20710 provides both SPI and UART transport layers. See [BCM20710 datasheet][10152] for more details. 
The firmware needs to be uploaded to the controller. The firmware .hcd file is available [here][10153]. 
## Realtek
### 8723au
This device has no driver included in the kernel, but you can install it separately. It also supports [Wifi][10154] functionality. 
The Bluetooth functionality is included in the hardware that does the wifi, so you may need to have the wifi drivers described above working to also have this working. However, don't expect it to work particularly well as there appear to be numerous bugs (in either the driver or the hardware or both). There seems to also be an issue where using both wifi and bluetooth at the same time cause severe interference to the point where connections are dropped (this has been seen in the stock Android firmware as well). 
check out the code from <https://github.com/lwfinger/rtl8723au_bt.git> and compile with the following command: 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -C ../linux-sunxi/ M=`pwd` modules
    
[/code]
**NOTE:** This command assumes that you checked out the rtl8723au_bt repo into the same directory as the linux-sunxi repo (note the `../linux-sunxi/` points to where your local kernel repository is) 
copy the *.bin and *.ko files over to the device and run the following on the device (as root) where you have your files: 
[code] 
    mkdir -p /lib/firmware/rtk_bt
    cp rlt8723a_chip_b_cut_bt40_fw_asic_rom_patch-svn8511-0x0020342E-20121105-LINUX_USB.bin /lib/firmware/rtk_bt/rtk8723a.bin
    install -p -m 644 rtk_btusb.ko /lib/modules/`uname -r`/kernel/drivers/bluetooth/
    /sbin/depmod
    modprobe rtk_btusb
    
[/code]
Apparently, the RTL8723AU driver (r8728au) in mainline serves only wifi, though it has an option to coexist with BT. [rtl8723au_bt, branch new][10155] is the work repository for a current bluetooth driver. 
### 8723bs
Firmware and userspace loader can be found [here][10156].
