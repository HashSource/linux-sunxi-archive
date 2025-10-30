# More-images
## Contents
  * [1 Annoying ZIPPYSHARE.com info][38529]
  * [2 Debian Images][38530]
  * [3 Cubian SD-card Images][38531]
  * [4 Linaro Precise Images][38532]
  * [5 Linaro Quantal images][38533]
  * [6 Ubuntu Desktop Images][38534]
  * [7 Updating Hardwarepacks and/or U-boot of any prebuild image][38535]

## Annoying ZIPPYSHARE.com info
To download from Zippyshare.com without any spam, adware or misleading links just click the download link on this page, solve the captcha on Zippyshare.com and then click the download link DIRECTLY below it. Your download will start immediately without any popups, spam or speed limitations. So don't let the big advertisement link in the middle fool you! 
All images here are tested and working as defined! The 512MB U-boot images can be used on any Cubieboard version but with limited memory size. Just replace U-boot if you have the 1GB Cubieboard version to get full memory available (see [[1]][38536]). 
## Debian Images
    [Debian Wheezy clean untouched ][38537] (incl. 512MB U-boot, kernel 3.0.52)
    [Debian Wheezy server ][38538] (512MB U-boot, XBMC, LAMP, kernel 3.0.62 + roman server 3.0.57-r1-rm9 part 1)
    [Debian Wheezy server ][38539] (512MB U-boot, XBMC, LAMP, kernel 3.0.62 + roman server 3.0.57-r1-rm9 part 2)
    [Debian Wheezy server 1GB][38540] (1GB U-boot, XBMC, LAMP, kernel 3.0.62 + roman server 3.0.57-r1-rm9 part 1)
    [Debian Wheezy server 1GB][38541] (1GB U-boot, XBMC, LAMP, kernel 3.0.62 + roman server 3.0.57-r1-rm9 part 2)
**Notes for the XBMC-Server Image:**
    
  * IP fixed to 192.168.1.155 (to be changed in /etc/network/interfaces)
  * download both files, unzip with 7zip and write to >=4GB Sdcard
  * added roman's headless server kernel uImage in /dev/mmcblkp01 [[2]][38542]
  * Both, standard linux-sunxi-kernel, and Roman's server-kernel are included (switch them by changing uImage files inside partition 1)
  * The XBMC image is set up as small Homeserver (including LAMP (Apache2, PHP, Mysql, PHPMyadmin), SAMBA and MPD)
  * Login/password for mysql and PHPMyadmin is root:mysqladmin .Other preset passwords can be found in /var/www/pass.
  * launch XMBC with ./allwinner/xbmc-pvr-binhf/lib/xbmc/xbmc.bin
  * AMPACHE(Music-Player-Webinterface [[3]][38543] ) Installed and running . Try 192.168.1.155/amp ...
  * full build environment for XBMC is still intact for easy rebuilding future XBMC versions.

**General Information for Debian Images:**
    
  * Default login: root | Password: password
  * you should also eventually install cpufrequtils to set up an acceptable CPU-behaviour

## Cubian SD-card Images
    [Cubian (Text mode) for A10 devices][38544] (1GB U-boot, kernel 3.4.75)
    [Cubian (Text mode) for A20 devices][38545] (1GB U-boot, kernel 3.4.75)
    [Cubian (Text mode) for Cubietruck][38546] (2GB U-boot, kernel 3.4.75)
    [Cubian desktop (LXDE) for A10 devices][38547] (1GB U-boot, kernel 3.4.75)
    [Cubian desktop (LXDE) for A20 devices][38548] (1GB U-boot, kernel 3.4.75)
    [Cubian desktop (LXDE) for Cubietruck][38549] (2GB U-boot, kernel 3.4.75)
## Linaro Precise Images
    [Linaro-Precise-Alip-20121124-519_1GB ][38550] (Confirmed working kernel 3.0.52)
    [Linaro-Precise-Alip-20121124-519_1GB_v2 ][38551] (Seems not to work kernel 3.0.52)
    [Linaro-Precise-Alip-20121124-519_1GB_v2 ][38552] (tested by [Mawi][38553] kernel 3.4)
    [Linaro-Precise-Alip-20121124-519_512MB ][38554] (Confirmed working kernel 3.0.52)
    [Linaro-Precise-Alip-20121124-519_512MB_v2][38555] (tested by [Mawi][38553] kernel 3.0.52)
    [Linaro Precise-Alip-20121124-519_512MB_v2][38556] (tested by [Mawi][38553] kernel 3.4)
## Linaro Quantal images
    [linaro-quantal-server-20130224-286_1GB ][38557] working, but wrong kernel 3.4.x -Replace before use ( link don't work )
    [linaro-quantal-alip-20130227-290_1GB ][38558] working , Kernel 3.0.62 (05.04.2013)
**General Information to Linaro Images:**
    
  * all linaro images are untouched with login linaro:linaro
  * to get rid of annoying root autologins rename "/etc/init/openvt.conf" to "/etc/init/openvt.conf.noboot" and edit "/etc/default/autogetty" to disable tty and serial autologin
  * you should also eventually install cpufrequtils to set up an acceptable CPU-behaviour

## Ubuntu Desktop Images
    [1GB Ubuntu Desktop Part 1][38559]
    [1GB Ubuntu Desktop Part 2][38560]
## Updating Hardwarepacks and/or U-boot of any prebuild image
To update the used Hardwarepack and the U-Boot of an image available here you can simply follow those easy steps (now we assume you run some sort of linux): 
  * first become sudo and get sunxi-bsp tools-set

[code] 
    git clone https://github.com/linux-sunxi/sunxi-bsp/
    cd sunxi-bsp
    
[/code]
  * then download latest hardwarepack fitting your hardware from here : [Amery's Hardwarepacks][38561]

[code] 
    wget YOURHWPACKLINK
    
[/code]
  * now just write everything to your SDcard . Make sure that the path to YOURSDCARD is always correct, or you might run into serious trouble!!

[code] 
    ./scripts/sunxi-media-create.sh /dev/YOURSDCARD YOURHARDWAREPACK norootfs
    eject /dev/YOURSDCARD
    
[/code]
  * thats all.

  * If you want to keep your current kernel/Hwpack and just want to Update U-boot Download An HWpack for your board, and extract it.

[code] 
    tar -xf YOURHARDWAREPACK
    
[/code]
  * Now you get 3 folders: 
    * BOOTLOADER — contains U-boot files;
    * KERNEL — contains uImage and script.bin;
    * ROOTFS — contains kernel modules and config files

To replace U-boot on your card cd now into /bootloader and do as Sudo: 
[code] 
    dd if=sunxi-spl.bin of=/dev/YOUSDCARD bs=1024 seek=8
    dd if=u-boot.bin of=/dev/YOURSDCARD bs=1024 seek=32
    
[/code]
Done. 
  * if you want to build your very own sdcard you can do this by using this commands:

[code] 
    git clone https://github.com/linux-sunxi/sunxi-bsp/
    cd sunxi-bsp
    wget YOURHWPACKLINK
    wget YOURROOTFSLINK
    ./scripts/sunxi-media-create.sh /dev/YOURSDCARD YOURHWPACK YOURROOTFS
    eject /dev/YOURSDCARD
    
[/code]
A good place to get an basic linaro alip rootfs is always here: 
[code] 
    [https://releases.linaro.org/latest/ubuntu/quantal-images] actual quantal rootfs
    
[/code]
