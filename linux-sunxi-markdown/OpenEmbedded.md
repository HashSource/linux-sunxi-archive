# OpenEmbedded
A "meta layer" is an OpenEmbedded repository (layer) of recipes, needed to build machine-specific stuff (u-boot, Linux kernel, script.bin), and to generate a dd'able SD-Card image. 
The official repository can be found on [linux-sunxi/meta-sunxi on Github][41901]
To start, you will need: 
  1. A new fresh directory.
  2. Angstrom scripts.
  3. Luck and patience.

The repository supports the following boards ("machines" in OE terminology): 
  * cubieboard
  * cubieboard2
  * cubietruck
  * olinuxino-a13
  * olinuxino-a10
  * olinuxino-a10s
  * olinuxino-a20
  * mele
  * meleg

More will be added as contributions occur. 
## Contents
  * [1 Setting up Angstrom scripts][41902]
  * [2 Configuring][41903]
  * [3 Building][41904]
  * [4 Installation][41905]

## Setting up Angstrom scripts
To set up Angstrom scripts do: 
[code] 
    git clone git://github.com/Angstrom-distribution/setup-scripts.git
    cd setup-scripts
    git checkout -b next origin/next
    
[/code]
then you will need to set up the machine you will be using; for example, for cubieboard, do 
[code] 
    MACHINE=cubieboard ./oebb.sh config cubieboard
    
[/code]
for any other board replace cubieboard with your machine name 
If an error occurs, you can comment out problematic repositories in sources/layers.txt as well as remove appropriate layers in conf/bblayers.conf, and run 
[code] 
    MACHINE=cubieboard ./oebb.sh update
    
[/code]
## Configuring
You will probably want to configure conf/bblayers.conf and remove layers you don't need from BSP layers. Also, you will probably want to delete meta-linaro as it often causes magic problems. Also, there is a lot of layers, such as meta-kde, which you might not need, so you can disable them too, especially if you see errors in them, such as .bbappend files referencing non-existing .bb files. 
## Building
once everything is ready, you can import the configured environment to start working: 
[code] 
    . environment-angstrom
    
[/code]
Then you can start the build: 
[code] 
    MACHINE=cubieboard bitbake console-image
    
[/code]
The build time will depend on your computer speed. 
If something goes wrong with some other BSP layer (not meta-sunxi), you can comment out or delete appropriate lines in conf/bblayers.conf 
## Installation
As build finishes, you can dd the resulting image to your SD card (for example, for a USB mass storage card reader, /dev/sdd may be your card) 
[code] 
    dd if=deploy/eglibc/images/cubieboard/console-image-cubieboard.a10-sdimg of=/dev/sdd
    sync
    eject /dev/sdd
    
[/code]
For a directly attached mmc controller (eg /dev/mmcblk0) you can do: 
[code] 
    dd if=deploy/eglibc/images/cubieboard/console-image-cubieboard.a10-sdimg of=/dev/mmcblk0
    
[/code]
**_IMPORTANT NOTE:_ If your card gets mounted during insertion, unmount it before doing any dd. And yes, as usual, check that your device name is correct BEFORE doing dd. You will not be able to undo this operation.**
So you now have bootable SD card image you can play with. Enjoy! 
Ps. You can login with root and without password!! Enjoy it!!
