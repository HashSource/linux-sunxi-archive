# USB
**[![Exclamation.png][57105]][57106]!!!Some of this information is outdated!!!**
## Contents
  * [1 USB Host Hardware (sun4i, sun7i)][57107]
  * [2 USB Host Status in Mainline Kernel / U-Boot][57108]
  * [3 Supported SoCs][57109]
  * [4 USB devices known to work][57110]
  * [5 USB to Ethernet Adapters known to work with U-Boot][57111]
  * [6 Known issues][57112]
  * [7 Reporting USB problem][57113]

## USB Host Hardware (sun4i, sun7i)
[code] 
                      USB Host 1 --------------------------------------------------> USB PORT
                    ---------------                                   VBUS_POWER1------^
          CLK2 ---> | EHCI | OHCI | <---- CLK1
                    ---------------
                    |     PHY1    | <--------------------|
                    ---------------                      |
                           ^-----RESET1                  |
                                                         |--------CLK5
                        USB Host 2-----------------------+-------------------------> USB PORT
                    ---------------                      |            VBUS_POWER2------^
          CLK4 ---> | EHCI | OHCI | <--- CLK3            |
                    ---------------                      |
                    |     PHY2    | <--------------------|
                    -------------------------
                           ^-----RESET2
    
[/code]
## USB Host Status in Mainline Kernel / U-Boot
EHCI/OHCI should work fine in the mainline kernel 
## Supported SoCs
  * A10
  * A20
  * A13
  * (A31 very preliminary work has been posted to the ML by bamvor)

## USB devices known to work
  * USB Keyboard
  * USB 2 Ethernet adapter
  * USB Stick/HDD (This allows you to have your rootfs on a USB stick/HDD. Add _root=/dev/sda1 rootwait_ to your cmdline.)
  * On-board WiFi module (idVendor=0bda, idProduct=8176) is identified and causes "detected XactErr len 0/0 retry" but still **works** , see [dmesg][57114].

## USB to Ethernet Adapters known to work with U-Boot
  * [Level One USB-0301][57115]

## Known issues
  * U-Boot outputs weird error messages if a USB sound card or USB midi device is plugged in on boot, both are full speed devices
  * On Hackberry A10 current stage/sunxi-3.4 (a7350cb6a9ec) has a regression which lefts USB ports without power supply. The issue can be workaround by using a powered USB hub.
  * On an Hackberry and A20-based tablet (with a single OTG USB port) the main sunxi-3.4 branch kernel (as of 22 Nov 2013) with default defconfig settings also seems to leave USB devices without power. This can be fixed by enabling the Inventra Highspeed Dual Role Controller in Device Drivers -> USB Support and selecting the Allwinner Platform Glue option.

## Reporting USB problem
If reporting USB Host related problems please turn on the following options in the menuconfig 
  * Device Drivers > USB support > USB verbose debug messages
  * Device Drivers > USB support > USB announce new devices
  * Change 0 to 1 at the line #37 of the drivers/usb/host/sw_hci_sunxi.h

Afterwards rebuild and boot a new kernel and submit the following information 
  * The exact tag or hash of the Linux kernel you are using
  * Your .config
  * Output of dmesg
  * Output of cat /proc/ccmu
  * Output of the following

    devmem2 0x01c14800
    devmem2 0x01c1c800
    devmem2 0x01c200cc
    devmem2 0x01c20060
Tip: You can use [sprunge.us][57116] paste service easily from the command line, for example 
[code] 
    cat .config | curl -F 'sprunge=<-' http://sprunge.us
[/code]
