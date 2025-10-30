# Kernel arguments
Kernel arguments can be specified in bootargs [U-boot][29476] environment variable or can be compiled into kernel. 
The [U-boot][29476] variables can be compiled in as default environment, saved in the environment on media or specified in boot.scr 
An example of kernel command line arguments: 
[code] 
     console=ttyS0,115200 hdmi.audio=EDID:0 disp.screen0_output_mode=EDID:1280x1024p60 root=/dev/mmcblk0p1 rootwait panic=10
    
[/code]
  * **console** =ttyS0,115200 is for taking over the serial port after u-boot. These are the default settings u-boot uses. You can specify console=ttyS0,115200 console=tty0 for both serial and framebuffer console

  * **earlyprintk** =serial,ttyS0,115200 enable earlyprintk on serial port. Pretty much useless on sunxi since some u-boot specific mechanism of printing to u-boot enabled serial port is used anyway and duplicates the earlyprintk functionality. Might come handy if you want to use another port, however.

  * **initcall_debug** kernel prints which init function it enters and exists. Useful to determine which driver crashed the kernel in case some driver crashed the kernel before it even printed anything.

  * **ddebug_query** ='"file 8250_sunxi.c +p"' enable debug prints (pr_info and pr_debug) in 8250_sunxi.c if you have CONFIG_DYNAMIC_DEBUG enabled. Note the double quoting - you will be probably setting this from u-boot which strips one set of quotes. The ddebug documentation says to use double quotes.

  * **consoleblank** =0 to disable screen saver of framebuffer.

  * **hdmi.audio** =EDID:0 this should presumably turn on HDMI audio only when screen EDID says it supports audio. Omit EDID to just turn on - 1 or off - 0. Currently HDMI audio is enabled even on screen that definitly does not support it - YMMW.

  * **disp**.screen0_output_mode=EDID:1280x1024p60 screen 0 is the first screen configured in script.bin. EDID instructs the kernel to try to read mode from the screen. Failing that you can pick a mode from a fixed mode list in the driver. Again, omit EDID to override mode manually. You can try to figure out supported modes from files like <https://github.com/linux-sunxi/linux-sunxi/blob/sunxi-3.0/drivers/video/sunxi/disp/disp_clk.c> cat /sys/class/graphics/fb0/modes might be of some help too.

  * **root** =/dev/mmcblk0p1 - root on first mmc device first partition. Use /dev/nandc for nand third partition (new partitioning scheme uses /dev/nand3) Some images use label or UUID to identify the root filesystem. /dev/sda1 identifies first SCSI device first partition but as both internal SATA and USB mass storage use SCSI emulation this device name is not assigned deterministically. Use labels or UUIDs for SCSI devices. If you have a seperate boot partition that holds the kernel, boot.scr and script.bin, the root file system would usually be /dev/mmcblk0p2 (use root=/dev/mmcblk0p2).

  * **rootwait** \- Wait (indefinitely) for root device to show up. Useful for devices that are detected asynchronously (e.g. USB and MMC devices).

  * **panic** =10 - the amount of time in seconds to wait before rebooting after kernel panic.

It is possible to significantly reduce the amount of reserved memory assigned to various video devices at boot time, resulting in more free system memory, which is especiallly helpful for 512MB devices: 
  * **sunxi_ve_mem_reserve** =0 -- This eliminates the reserved memory for the video acceleration engine, saving 80MB. You can use this if you don't run accelerated video with programs such as [VLC][29477], [Kodi][29478] or [libvdpau-sunxi][29479]. (This kernel parameter is ignored in recent 3.4 kernels, if CMA is enabled in kernel configuration. If CONFIG_CMA=y, ve_size is hardcoded to 80MB in sunxi_cedar kernel module.)

  * **cma** =96M the amount of memory to reserve for contimuous allocation. Default is 16M so you have to raise it for the Cedar ve_size to fit.

  * **sunxi_g2d_mem_reserve** =0 -- This eliminates the reserved memory for the 2D acceleration engine. You can use this if you don't have the G2D accelerated driver enabled in your xorg.conf. Even when G2D is enabled, it may not actually use any of this memory, so this setting may be safe (to be verified).

  * **sunxi_no_mali_mem_reserve** \-- This eliminates the reserved memory for the Mali400 3D GPU. If you do not have the Mali binary blob driver installed, it is safe to use this and save another 64MB. [Obsolete][29480].

  * **sunxi_fb_mem_reserve** =16 -- This sets the amount of total reserved memory for the framebuffer to 16MB. The default is 32MB. Because of double buffering Mali may require more than 16MB of framebuffer, so generally only enable this if you don't have Mali installed. 16MB should be sufficient for the largest supported resolution (normally 1920x1080x32bpp).

See also [Optimizing system performance][29481]. 
Feel free to add other relevant arguments. This list is not exhaustive.
