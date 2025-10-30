# A20-Cubieboard/Nand Images (Lubuntu)
(Redirected from [A20-Cubieboard/Nand Images(Lubuntu)][2438])
 
## Contents
  * [1 lubuntu-desktop-v1.02][2441]
    * [1.1 Download][2442]
    * [1.2 Features][2443]
    * [1.3 Issues][2444]
  * [2 lubuntu-desktop-v1.03][2445]
    * [2.1 Download][2446]
    * [2.2 Features][2447]
    * [2.3 Issues][2448]
  * [3 lubuntu-desktop-v1.04-beta1][2449]
    * [3.1 Download][2450]
    * [3.2 Features][2451]
    * [3.3 Issues][2452]
  * [4 lubuntu-desktop-v1.04][2453]
    * [4.1 Download][2454]
    * [4.2 Features][2455]
    * [4.3 Kernel][2456]
    * [4.4 Issues][2457]
  * [5 lubuntu-desktop-v1.05][2458]
    * [5.1 Download][2459]
    * [5.2 Features][2460]
    * [5.3 Kernel][2461]
    * [5.4 Issues][2462]
  * [6 lubuntu-desktop-v1.06 and lubuntu-server-v1.06][2463]
    * [6.1 Download][2464]
    * [6.2 Features][2465]
    * [6.3 Issues][2466]
  * [7 lubuntu server 20140125][2467]
    * [7.1 Download][2468]
  * [8 lubuntu v1.07][2469]
    * [8.1 Download][2470]
    * [8.2 Features][2471]
    * [8.3 Limitations][2472]
    * [8.4 Issues][2473]
  * [9 lubuntu-server-13.06-v1.00][2474]
    * [9.1 Download][2475]
    * [9.2 Features][2476]
  * [10 See also][2477]

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
  * Limited space on the image, that is a 2 GB partition : /dev/root 1.8G 1.4G 285M 84% /, another partition can be added on the NAND with [nand-part][2478] tool.

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
  * [A20-Cubieboard/Nand Images (Android)][2479]
  * [A20-Cubieboard/Nand Images (Debian)][2480]
  * [A20-Cubieboard/Nand Images 2][2481]
