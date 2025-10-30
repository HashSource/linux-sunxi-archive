# SD card based installer
Many Allwinner devices can be booted using a single common SD card image, which can be potentially used to install the rest of the Linux system on a device without any assistance from the desktop PC. In a completely desktop PC free scenario, such an SD card can be, for example, received by snail mail from the device vendor. 
A prototype of such bootable SD card image is available for download from: <https://github.com/ssvb/sunxi-bootsetup/releases/tag/20141215-sunxi-bootsetup-prototype>
More information and the discussion in the u-boot mailing list archives: <http://lists.denx.de/pipermail/u-boot/2015-January/202306.html>
## The initial menu on HDMI monitor
If you have a HDMI monitor, then something like this should show up on it when booting from the SD card. The menu caption should display some information about the hardware. 
[![20141215-sunxi-bootsetup-prototype-hdmi-menu.jpg][48101]][48102]
## The initial menu on UART serial console
Even though this bootable SD card is designed to be primarily used with an HDMI monitor, the interactive menu is also duplicated on the serial console (primarily for debugging purposes): 
[code] 
      $ screen /dev/ttyUSB0 115200
    
[/code]
[![20141215-sunxi-bootsetup-prototype-uart-menu.png][48103]][48104]
