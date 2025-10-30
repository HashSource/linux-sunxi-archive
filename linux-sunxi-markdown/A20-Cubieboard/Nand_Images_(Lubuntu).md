# A20-Cubieboard/Nand Images (Lubuntu)
## Contents
  * [1 lubuntu-desktop-v1.02][2653]
    * [1.1 Download][2654]
    * [1.2 Features][2655]
    * [1.3 Issues][2656]
  * [2 lubuntu-desktop-v1.03][2657]
    * [2.1 Download][2658]
    * [2.2 Features][2659]
    * [2.3 Issues][2660]
  * [3 lubuntu-desktop-v1.04-beta1][2661]
    * [3.1 Download][2662]
    * [3.2 Features][2663]
    * [3.3 Issues][2664]
  * [4 lubuntu-desktop-v1.04][2665]
    * [4.1 Download][2666]
    * [4.2 Features][2667]
    * [4.3 Kernel][2668]
    * [4.4 Issues][2669]
  * [5 lubuntu-desktop-v1.05][2670]
    * [5.1 Download][2671]
    * [5.2 Features][2672]
    * [5.3 Kernel][2673]
    * [5.4 Issues][2674]
  * [6 lubuntu-desktop-v1.06 and lubuntu-server-v1.06][2675]
    * [6.1 Download][2676]
    * [6.2 Features][2677]
    * [6.3 Issues][2678]
  * [7 lubuntu server 20140125][2679]
    * [7.1 Download][2680]
  * [8 lubuntu v1.07][2681]
    * [8.1 Download][2682]
    * [8.2 Features][2683]
    * [8.3 Limitations][2684]
    * [8.4 Issues][2685]
  * [9 lubuntu-server-13.06-v1.00][2686]
    * [9.1 Download][2687]
    * [9.2 Features][2688]
  * [10 See also][2689]

## lubuntu-desktop-v1.02
### Download
  * **Note** : ubuntuone service is discontinued.

[code] 
    <http://ubuntuone.com/0tRcRMM8MsoHMJ2onL9YNI>
    
[/code]
### Features
  * Suport Livesuit(Windows:ok; Linux: not supported; Mac: not tested)
  * Default HDMI output
  * Linux-3.3 Kernel

### Issues
  * Do not support Linux Livesuit
  * X windows does not display correctly sometimes

## lubuntu-desktop-v1.03
### Download
  * **Note** : ubuntuone service is discontinued.

[code] 
    <http://ubuntuone.com/5SnwaG2DrsihQfpjQu9JPd> (HDMI)
    <http://ubuntuone.com/56srFr1jOaLMd7Jf1wn6tp> (VGA)
    
[/code]
### Features
  * Suport Livesuit(Windows:not supported; Linux: yes; Mac: not tested)
  * Support HDMI/VGA output

### Issues
  * Do not support Windows Livesuit
  * X windows does not display correctly sometimes

## lubuntu-desktop-v1.04-beta1
### Download
  * **Note** : ubuntuone service is discontinued.

[code] 
    <http://ubuntuone.com/3BhoQdUSDrPlFbqdisgCTq>
    
[/code]
### Features
  * Linux 3.4 kernel
  * Default HDMI output
  * Preinstall openssh-server/openssh-client
  * Preinstall fbset

[code] 
    #to tune screen display
    $fbset -left 10
    
[/code]
  * Preinstall GPIO python library
  * Preinstall Chinese font
  * RTL8188EU/RTL8192CU wifi have been tested
  * Enable DHCP eth0
  * DRAM 480MHz
  * Support Linux/Windows Livesuit(MAC Tested: Works)

### Issues
  * Take a long time to boot when no wired net cable

[code] 
    Wait DHCP timeout
    
[/code]
  * MALI GPU not support till now
  * VE not support till now
  * Cannot auto switch to VGA output
  * First time boot take about 2 minutes to setup
  * Early A20 chip have no CHIPID, the new will have chipid that can be used as MAC address

  

## lubuntu-desktop-v1.04
### Download
  * **Note** : ubuntuone service is discontinued.

[code] 
    <http://ubuntuone.com/69ifBXGgwj4rBQoDsmKB63>
    
[/code]
### Features
Most features is same as v1.04-beta1, the changes are: 
  * Add fex2bin/bin2fex tools
  * Add cb-display-tool

[code] 
    To switch VGA/HDMI display mode in command line. e.g.
    $cb-display-tool -o 8 -m 11
    Note: can switch to the same resolutions only currently.
    
[/code]
  * Add jdk-1.8 armhf
  * with many USB camera drivers builtin
  * Support PWM

[code] 
    To use pwm:
    $cd /lib/modules/`uname -r`/kernel/drivers/misc
    $sudo insmod pwm-sunxi.ko
    $sudo su - root
    #cd /sys/kernel/sunxi_pwm
    #echo '0 1200 2400' > start
    
[/code]
### Kernel
[code] 
    <http://dl.cubieboard.org/software/a20-cubieboard/lubuntu/linux-sunxi-kernel-cb2-lubuntu-v1.04.tgz>
    
[/code]
### Issues
  * Take a long time to boot when no wired net cable

[code] 
    Wait DHCP timeout
    
[/code]
  * MALI GPU not support till now
  * VE not support till now
  * Cannot auto switch to VGA output
  * First time boot take about 2 minutes to setup
  * Early A20 chip have no CHIPID, the new will have chipid that can be used as MAC address

  

## lubuntu-desktop-v1.05
### Download
[code] 
    <http://dl.cubieboard.org/software/a20-cubieboard/lubuntu/cb-a20-lubuntu-12.10-v1.05.img.gz>
    
[/code]
### Features
  * Enable MALI GPU
  * Enable many kernel modules that users want

### Kernel
[code] 
    <http://dl.cubieboard.org/software/a20-cubieboard/lubuntu/cb-a20-lubuntu-12.10-v1.05-kernelsource.tar.gz>
    
[/code]
### Issues
  * 2D, Video Encoding/Decoding, SPI doesn't work

## lubuntu-desktop-v1.06 and lubuntu-server-v1.06
Release date : 2013-10-26 
### Download
<http://dl.cubieboard.org/software/a20-cubieboard/lubuntu/cb-a20-lubuntu-12.10-v1.06/>
### Features
### Issues
## lubuntu server 20140125
  * kernel 3.4.75
  * Release date : 2014-01-25

### Download
<http://dl.cubieboard.org/software/a20-cubieboard/lubuntu/cb2-lubuntu-server-20140125/>
## lubuntu v1.07
  * kernel 3.4.79 (armv7l)
  * Based on Linaro 13.04
  * Release date: 2014-04-04
  * Login: linaro or root
  * pass: linaro

### Download
<http://dl.cubieboard.org/software/a20-cubieboard/lubuntu/cb-a20-lubuntu-v1.07/>
### Features
  * nginx 1.2.1
  * lignthdm 1.4.0
  * LXDE / lubuntu
  * gcc (ubuntu/linaro) 4.7.2, Python 2.7 & 3, OpenJDK 7
  * sunxi_cedar_mod, mali_drm & mali (both GPL).

### Limitations
  * Limited space on the image, that is a 2 GB partition : /dev/root 1.8G 1.4G 285M 84% /, another partition can be added on the NAND with [nand-part][2690] tool.

### Issues
## lubuntu-server-13.06-v1.00
### Download
[code] 
    <http://dl.cubieboard.org/software/a20-cubieboard/lubuntu/cb-a20-lubuntu-server-13.06-v1.00.img.gz>
    
[/code]
### Features
  * Enable MALI GPU
  * Enable many kernel modules that users want
  * Use linaro lubuntu 13.06 rootfs

## See also
  * [A20-Cubieboard/Nand Images (Android)][2691]
  * [A20-Cubieboard/Nand Images (Debian)][2692]
  * [A20-Cubieboard/Nand Images 2][2693]
