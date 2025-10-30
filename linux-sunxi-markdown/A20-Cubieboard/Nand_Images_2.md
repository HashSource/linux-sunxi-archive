# A20-Cubieboard/Nand Images 2
This page could not be up-to-date, please instead, look at the following page, each dedicated to a linux distribution : 
  * [A20-Cubieboard/Nand Images (Android)][2726]
  * [A20-Cubieboard/Nand Images (Debian)][2727]
  * [A20-Cubieboard/Nand Images (Lubuntu)][2728]

## Contents
  * [1 Android 4.2.2-v1.05(and before)][2729]
    * [1.1 Downloads][2730]
    * [1.2 Features][2731]
  * [2 lubuntu-desktop-v1.02][2732]
    * [2.1 Download][2733]
    * [2.2 Features][2734]
    * [2.3 Issues][2735]
  * [3 lubuntu-desktop-v1.03][2736]
    * [3.1 Download][2737]
    * [3.2 Features][2738]
    * [3.3 Issues][2739]
  * [4 lubuntu-desktop-v1.04-beta1][2740]
    * [4.1 Download][2741]
    * [4.2 Features][2742]
    * [4.3 Issues][2743]
  * [5 lubuntu-desktop-v1.04][2744]
    * [5.1 Download][2745]
    * [5.2 Features][2746]
    * [5.3 Kernel][2747]
    * [5.4 Issues][2748]
  * [6 See also][2749]

## Android 4.2.2-v1.05(and before)
### Downloads
The following images are suitable for Cubieboard2's Nand Flash installation 
cb_a20_android42_v1.01_ddr432_8188eu.img.gz  | <http://ubuntuone.com/65cb9IbMRw5FSwmwFsRzvk> |  1\. Support RTL8188EU wifi   
2\. Suport Livesuit(Windows:ok; Linux: not supported; Mac: not tested)   
3\. Default Language is English   
---|---|---  
cb_a20_android42_v1.01-ddr432.img.gz  | <http://ubuntuone.com/0XfWiwxnpW1P9oJDAeq3sI> |  1\. Support RTL8192CU wifi   
2\. Suport Livesuit(Windows:ok; Linux: not supported; Mac: not tested)   
cb_a20_android42_v1.03-ddr432-en_US-rtl8188eu.img.gz  | <http://ubuntuone.com/1LmPYFzQ213CmvzyOvOxb1> |  1\. Support RTL8188EU wifi   
2\. Suport Livesuit(Windows:not supported ; Linux: ok; Mac: not tested)   
cb_a20_android42_v1.03-ddr432-zh_CN-rtl8188eu.img.gz  | <http://ubuntuone.com/2eAFO6mFhJnPK7hA7qeEpo> |  1\. Support RTL8188EU wifi   
2\. Suport Livesuit(Windows:not supported ; Linux: ok; Mac: not tested)   
cb_a20_android42_v1.03_8188eu_livesuit-win.img.gz  | <http://ubuntuone.com/7dkV2RK8XeDrkXhqEed9cU> |  1\. Support RTL8188EU wifi   
2\. Suport Livesuit(Windows:yes ; Linux: not support; Mac: not tested)   
cb_a20_android42_v1.04_8188eu-ddr432-en_US.img   
| <http://ubuntuone.com/5IaFaSoVL5M9GzjN1FQd5R> |  1\. Support RTL8188EU wifi   
2\. Support Windows/Linux Livesuit   
3\. Fix SDCard issue   
4\. Change wallpaper and bootlogo   
  
cb_a20_android42_v1.05_8192cu-ddr432-en_US.img   
| <http://ubuntuone.com/0HdTKPlNHb5zsqOgNhpBPW> |  1\. Support RTL8192CU wifi   
2\. Support Windows/Linux Livesuit   
3\. Add USB camera audio  
4\. Add Email2  
  
### Features
  * Linux 3.3 Kernel

## lubuntu-desktop-v1.02
### Download
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

## See also
  * [A20-Cubieboard/Nand Images (Android)][2726]
  * [A20-Cubieboard/Nand Images (Debian)][2727]
  * [A20-Cubieboard/Nand Images (Lubuntu)][2728]
