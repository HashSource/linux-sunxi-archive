# Optimizing system performance
When the root filesystem used on the device is a flash memory card or flash memory as will often be the case, the performance bottleneck will often be write access to the root file system. It is therefore beneficial for overall system performance to reduce unnecessary writing by using methods such as ramdisk file systems, tmpfs, and reducing system logging activity. 
It is also possible to tweak the kernel and hardware devices to improve performance. 
## Contents
  * [1 Reducing system logging activity][42015]
  * [2 Optimizing cache directories][42016]
  * [3 Using tmpfs][42017]
  * [4 Increasing available system memory at boot time][42018]
  * [5 Increasing the memory clock speed][42019]
  * [6 Recompiling the kernel][42020]
  * [7 Optimizing boot speed][42021]
  * [8 Using a lower resolution graphics mode][42022]
  * [9 Reducing refresh rate for 1920x1080 video mode][42023]
  * [10 Notes for A20-based devices][42024]
  * [11 Changing the CPU frequency governor settings][42025]
  * [12 Using an optimized Xorg driver][42026]
  * [13 Advanced topic: Using more recent Mali drivers][42027]

## Reducing system logging activity
In a default distro install, system logging is often configured fully, suitable for a server or multi-user system. However, on a single-user system the constant writing of many system log files will result in reduced interactive system performance, and reducing logging activity will be beneficial for performance as well as the lifetime of the flash memory. 
In a Debian Wheezy installation, the default system logger is rsyslog, and it configuration file is /etc/rsyslog.conf. In the rules section, the following logs are often enabled by default: 
[code] 
    auth,authpriv.*                        /var/log/auth.log
    *.*;auth,authpriv.none         -/var/log/syslog
    cron.*                         /var/log/cron.log
    daemon.*                       -/var/log/daemon.log
    kern.*                         -/var/log/kern.log
    lpr.*                          -/var/log/lpr.log
    mail.*                         -/var/log/mail.log
    user.*                         -/var/log/user.log
    
[/code]
There may also be rules for -/var/log/debug and -/var/log/messages, and |/dev/xconsole. 
Note that kernel messages are logged in both kern.log and syslog, in addition to being available from the dmesg command from kernel memory. In a single user system, it is possible to disable most or all of these logs by placing a '#' character at the start of the corresponding lines. Logs can be re-enabled if it is necessary to debug a system problem. 
## Optimizing cache directories
Applications like browsers and window managers that use a disk cache may conform to the XDG Base Directory Specification standard. In that case, the environment variable XDG_CACHE_HOME defines the directory where cache files are stored. By setting this variable to a ramdisk location, it is possible to greatly speed-up the performance of certain browsers that otherwise stall with heavy writing to the disk-cache in flash memory. For example, in a Debian Wheezy installation with LXDE, there may be a configuration file called /etc/alternatives/x-session-manager. By adding the line 
[code] 
    export XDG_CACHE_HOME="/dev/shm/.cache"
    
[/code]
to the start of this file, programs running in X conforming to the standard will be using the ramdisk in /dev/shm to store cache files. One browser popular on light-weight configurations that benefits from this is Midori. The default disk cache size in Midori is 100MB, you can lower this if you don't have much system memory available, but you can configure Midori to clean the cache on exit and thus give back the memory to the system in Tools->Clear Private Data. 
In more recent Debian-based root file systems, the tmpfs device is called /run/shm (which must be present in /etc/fstab), and x-session-manager is a binary file, but you can add the same line to a new file in /etc/profile.d/, for example /etc/profile.d/xdg_cache_home.sh, that will be executed at the start of every login. The file should look like this: 
[code] 
     #!/bin/bash
    export XDG_CACHE_HOME="/run/shm/.cache
    
[/code]
## Using tmpfs
To mount /tmp and /var/tmp (the directories for temporary files used by programs) on a ramdisk, you may be able to add the following lines to /etc/fstab: 
[code] 
    tmpfs    /tmp        tmpfs    defaults    0 0
    tmpfs    /var/tmp    tmpfs    defaults    0 0
    
[/code]
There should also be line enabling /run/shm as tmpfs: 
[code] 
    tmpfs    /run/shm    tmpfs    defaults    0 0
    
[/code]
Refer to more general documentation sources for your distro for more details. 
## Increasing available system memory at boot time
It is possible to increase available system memory at boot time by reducing reserved memory allocated to video subsystems. See [Kernel arguments][42028] for more details. 
## Increasing the memory clock speed
Overclocking the memory in your device may result in stability problems. However, the default memory clock on your device may be set up for reduced power consumption with battery usage (on a tablet), and when battery lifetime is not of great concern (you leave power connected) you may be able to significantly increase the memory clock speed and as a result system performance. 
On some devices, the standard memory clock defined in Android's script.bin may even be too high and result in an unstable system. Reducing the memory clock may fix this. 
There is a utility to read out the current DRAM settings, called [meminfo][42029]. The dram_clk parameter shows the current DRAM clock speed. The speed must be a multiple of 24 Mhz. The default speed for A10 tablets is generally 360 MHz, boards may have a higher default speed. Although speeds as high as 480 MHz may appear stable at first, on heavy workloads especially using the Mali GPU errors may occur at higher memory clock settings. Most people find that 384 or 408 MHz run stable. 
Because the memory clock has to be configured at the beginning of the boot process, it is not straightforward to change the memory clock speed. It involves recompiling u-boot-sunxi and re-flashing the bootloader on your SD-card. If something goes wrong it has the potential to corrupt the SD-card installation or make it unbootable. So only continue if you are sure what you are doing. 
If you don't already have u-boot-sunxi installed, clone it using 
[code] 
    git clone <https:///github.com/linux-sunxi/u-boot-sunxi.git>
    
[/code]
Then go to the board/allwinner directory and select the configuration that most closely matches your device. For example. for a generic A10 1GB tablet you would pick a10_mid_1gb. Edit the file dram.c in the directory for your device and change the .clock parameter to the desired memory clock frequency. It must be a multiple of 24, usually in the range 360-480 MHz. Higher speeds may not be stable. Then run from the u-boot-sunxi base directory (replace a10_mid_1gb in the command below with the configuration that you selected): 
[code] 
    make a10_mid_1gb
    
[/code]
Now it's time to re-flash the bootloader on the SD-card. With a recent version of u-boot-sunxi, run: 
[code] 
    sudo dd if=spl/sunxi-spl.bin of=/dev/mmcblkN bs=1024 seek=8
    sudo dd if=u-boot.img of=/dev/mmcblkN bs=1024 seek=40
    
[/code]
With an old version of u-boot-sunx (< 2013.7) the procedure is slightly different: 
[code] 
    sudo dd if=spl/sunxi-spl.bin of=/dev/mmcblkN bs=1024 seek=8
    sudo dd if=u-boot.bin of=/dev/mmcblkN bs=1024 seek=32
    
[/code]
/dev/mmcblkN is the device name of your SD-card (for example /dev/mmcblk0). After rebooting the new memory clock speed should have taken effect. Verify it by running a10-meminfo (see above). 
The above procedure also works for A20-based devices. These may have a faster memory clock in their default configuration, although at least some devices (certain Android tablets) seem to be shipped with a memory clock may be too high resulting in stability problems. 
## Recompiling the kernel
By default the kernel may be configured with a large set of drivers to support a large number of configurations. It is possible to disable drivers that you don't need to reduce kernel size. The kernel may also be set up with a wide range of debugging options. Reducing debugging options will reduce the kernel size and improve performance a bit, although it may make debugging hardware or software problems harder. An advanced option for expert users that may be enabled is the 2G/2G memory split with high memory disabled, which theoretically could result in a measurable performance improvement. Note: highmem is needed for systems with more tham 512MB of ram - the maximum usable ram without highmem is something like 700~800MB. 
## Optimizing boot speed
All the steps above can contribute to reducing boot time. Smaller kernel loads faster from flash and decompresses faster. Reduced logging and optimized caching causes fewer stalls in the boot process. Setting default cpufreq governor to performance with as high cpu and memory speed as possible shortens time required for CPU intensive tasks during boot. However, picking your init system is also important and has very large impact with all else staying the same. 
**sysvinit** is ancient and **slow**. If your distribution uses it by default change it to **upstart** or **systemd**. If you want your board to run one self-contained application that does not need any system services running you can try passing **init=/path/to/your/application** to the kernel. Not many applications are made to run like that. Especially without udev running you might have hard time accessing devices but you might have good luck with eg. xbmc. Note the system crashes when the application exits so remember to pass something like **panic=1** as well so that it reboots again. 
## Using a lower resolution graphics mode
The Allwinner chip's graphics framebuffer is stored in the same memory chips as system memory. As a result, the memory access required for screen refresh detracts from the overall system memory bandwidth and latency. By setting a lower resolution graphics mode, or a graphics mode with a lower pixel (color) depth, it is possible to measurably increase system performance. 
When using the console, using a color depth of 16bpp may not be visibly different from 32bpp while improving performance. In X, performance will be improved but you will see banding on color gradients and acceleration options such as VE and Mali may not available in X and in console mode. G2D acceleration does support 16bpp. 
You can change the graphics mode with [Kernel arguments][42028], changing script.bin, or after boot with utilities such as a10_display and a10disp (see [Display][42030]). 
The following tables show memory performance using the benchmark program tinymembench (<https://github.com/ssvb/tinymembench‎>) at different resolutions, pixel depths and memory clock settings on the same monitor. 
NEON read bandwidth (MB/s): 
[code] 
    	Memclock (MHz):	 360	 384	 408
    Display output disabled	1114	1159	1198
    1280x720x16bpp		1075	1128	1195
    1280x720x32bpp		1053	1078	1126
    1920x1080x16bpp		1045	1089
    1920x1080x32bpp		 902	 972	 991
    
[/code]
NEON fill bandwidth (MB/s): 
[code] 
    	Memclock (MHz):	 360	 384	 408
    Display output disabled 1176	1256	1330
    1280x720x16bpp		1088	1171	1328
    1280x720x32bpp		 972	1078	1090
    1920x1080x16bpp		 934	1005
    1920x1080x32bpp		 545	 548	 552
    
[/code]
NEON copy bandwidth (MB/s) (unrolled copy prefetched (64 bytes step)): 
[code] 
    	Memclock (MHz):	 360	 384     408
    Display output disabled	 650	 714	 723
    1280x720x16bpp		 610	 650	 723
    1280x720x32bpp		 554	 594	 636
    1920x1080x16bpp		 538	 575
    1920x1080x32bpp		 453	 517	 523
    
[/code]
Memory latency in ns (block size 1MB, single random read): 
[code] 
    	Memclock (MHz):	 360	 384	 408
    Display output disabled	 171	 165	 159
    1280x720x16bpp		 173	 166	 159
    1280x720x32bpp		 174	 168	 159
    1920x1080x16bpp 	 175	 168
    1920x1080x32bpp		 176	 169	 163
    
[/code]
Memory latency in ns (block size 64MB, single random read): 
[code] 
    	Memclock (MHz):	 360	 384	 408
    Display output disabled	 264	 254	 240
    1280x720x16bpp		 265	 256	 240
    1280x720x32bpp		 268	 256	 241
    1920x1080x16bpp		 267	 257
    1920x1080x32bpp		 270	 259	 247
    
    
[/code]
As you can see, running at 1920x1080x32bpp really detracts from memory performance, especially write (fill) speed, which is also reflected in copy speed. Lowering the resolution and pixel depth, and increasing the memory clock improves system performance. Running headless (no display output) is fastest. 
## Reducing refresh rate for 1920x1080 video mode
Most LCD monitors are using 60Hz refresh rate, and this is never a problem for more capable desktop hardware. However for Allwinner A10, using 1920x1080x32bpp at 60Hz is causing a major performance drop for memory write performance (from a bit less than ~1000MB/s down to a bit more than ~500MB/s). Instead of reducing the resolution or color depth, it is possible to reduce the refresh rate. The crossover point for this major memory write speed performance drop is around: 
[code] 
     | 1920x1080-32 @60Hz | always slow with any memory frequency up to 480MHz
     | 1920x1080-32 @56Hz | slow with 456MHz memory | fast with 480MHz memory
     | 1920x1080-32 @50Hz | slow with 408MHz memory | fast with 432MHz memory
    
[/code]
Using 24bpp desktop color depth is also possible (via "fbset -depth 24 -rgba 8,8,8,0"), but it is poorly supported by software. However it avoids memory write performance drop until memory clock speed is reduced below 408MHz. 
[code] 
     | 1920x1080-24 @60Hz | 432MHz memory = ~970 MB/s write speed
     | 1920x1080-24 @60Hz | 408MHz memory = ~840 MB/s write speed
     | 1920x1080-24 @60Hz | 384MHz memory = ~430 MB/s write speed
    
[/code]
It might be potentially possible to make use of 24bpp framebuffer in Xorg via some ShadowFB tweaks. The shadow framebuffer may just use 32bpp format (and do 32bpp->24bpp conversion when copying data to the real framebuffer). All the applications will think that the desktop color depths is 32bpp. But ShadowFB also has some other drawbacks, for example making the use of G2D acceleration problematic. 
## Notes for A20-based devices
Even though the A20 uses a memory configuration similar to the A10 (with similar theoretical peak bandwidth), the memory interface on the A20 seems to be much more efficient. Higher memory bandwidth, especially for fills (writes), is seen and there are no dramatic drops in bandwidth when running 1080p at 32bpp. However, reducing the resolution, color depth or refresh rate of the display out still has a measurable influence on performance, as shown in the following table. 
Benchmarks on an A20 device with 408 MHz memory clock. 
[code] 
    HDMI output             copy speed      fill speed      Mali benchmark
                            (NEON)          (NEON)          X11-EGL (1024x576 window)
    1920x1080x32bpp 60 Hz   580 MB/s        1390 MB/s       157.6 fps
    1920x1080x32bpp 50 Hz   600 MB/s        1510 MB/s       168.2 fps
    1920x1080x16bpp 60 Hz   640 MB/s        1690 MB/s       not supported
    1280x720x32bpp 60 Hz    660 MB/s        1750 MB/s       183.8 fps
    1280x720x32bpp 50 Hz    660 MB/s        1770 MB/s       190.4 fps
    
[/code]
## Changing the CPU frequency governor settings
The CPU frequency governor may not be setup for maximum performance. See [Cpufreq][42031]. 
## Using an optimized Xorg driver
Your distro might be set up to only use the standard framebuffer driver for X. You can enable the fbturbo driver (new name for sunxifb) for X following the instructions in the section [ FBTurbo driver of the Xorg page][42032]. You can enable G2D for 2D acceleration using the G2D engine. 
## Advanced topic: Using more recent Mali drivers
The Mali-400MP2 used in the A20 chip has two pixel processor cores, as opposed only one in the A10's Mali-400. The standard Mali driver (r3p0) does not utilize the second pixel processor, while a more recent one (3p2) does. The r3p2 version of the Mali driver also seems to have other performance benefits. To use the r3p2 mali driver, a few steps have to be taken: 
  * A kernel with the r3p2 Mali kernel driver must be used. An example is ssvb's 20130913-mali-r3p2-01rel2 branch of linux-sunxi (<https://github.com/ssvb/linux-sunxi.git>). Note that this kernel does not include G2D (bitblt) acceleration, but that is generally not a critical performance issue with the A20.
  * The userspace mali drivers must be updated to r3p2. This is automatically handled by the mali drivers at <https://github.com/linux-sunxi/sunxi-mali.git> after updating the submodules.
  * The mali-r3p2-support branch of the xf86-video-fbturbo xorg driver must be installed.

The [Benchmarks][42033] section has a comparison of glmark2 results between the different Mali driver versions. 
The A10 should also work with the newer Mali driver, and performance may be a little better/more stable (needs verification).
