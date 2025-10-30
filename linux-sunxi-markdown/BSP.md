# BSP
"BSP" means [**B** oard **S** upport **P** ackage][8550]. 
  

## Contents
  * [1 Requirements][8551]
  * [2 Usage][8552]
    * [2.1 hwpack][8553]
      * [2.1.1 Installation][8554]
        * [2.1.1.1 Build an SD-card from a hwpack and a root FS][8555]
        * [2.1.1.2 Update an SD-card from a hwpack][8556]
      * [2.1.2 Create your own hwpack][8557]
    * [2.2 Kernel][8558]
      * [2.2.1 Change kernel configuration][8559]
    * [2.3 rootfs images][8560]
    * [2.4 LiveSuit image][8561]

# Requirements
These three steps are only required if you are planning to create your own hwpack or configure kernel on an x86 PC running Linux and will install all packages required. (Tested and working on Linux Mint 13/14, Ubuntu 12.04/12.10/13.04) 
[![Sticky-note-pin.png][8562]][8563] _Note:_ On Debian (wheezy) / Ubuntu 13.10 (saucy) onwards, _uboot-mkimage_ package is removed, _mkimage_ command is included in _u-boot-tools_ package. 
[code] 
    apt-get update
    apt-get upgrade
    apt-get install build-essential u-boot-tools uboot-mkimage gcc-arm-linux-gnueabihf \
      libusb-1.0-0-dev git wget fakeroot \
      kernel-package zlib1g-dev libncurses5-dev pkg-config
    
[/code]
  
The git project is available at <https://github.com/linux-sunxi/sunxi-bsp>
To download it: 
[code] 
    git clone <git://github.com/linux-sunxi/sunxi-bsp.git>
    
[/code]
# Usage
## [hwpack][8564]
### Installation
#### Build an SD-card from a [hwpack][8564] and a root FS
[code] 
    ./scripts/sunxi-media-create.sh [device] [hwpack] [rootfs]
    
[/code]
#### Update an SD-card from a [hwpack][8564]
[code] 
    ./scripts/sunxi-media-create.sh [device] [hwpack] norootfs
    
[/code]
### Create your own [hwpack][8564]
[code] 
    ./configure # to list all currently supported boards
    ./configure <selected board>
    make
    
[/code]
## Kernel
### Change kernel configuration
[code] 
    # Following command calls 'make menuconfig' with correct O= parameter
    make linux-config
    
[/code]
## rootfs images
Rootfs images can be downloaded from **Linaro'** s site: 
  * <https://releases.linaro.org/>

In addition, Ubuntu Core is a rootfs image for Ubuntu, available at 
  * <http://cdimage.ubuntu.com/ubuntu-core/releases/>

Read more about the Ubuntu Core rootfs images for armhf at <https://wiki.ubuntu.com/Core>
For example the latest **Linaro nano** is: 
  * <https://releases.linaro.org/13.04/ubuntu/quantal-images/nano/linaro-quantal-nano-20130422-342.tar.gz>

## [LiveSuit][8565] image
_Requires 64bit linux._
sunxi-bsp supports generating Android and Linux LiveSuit images. You can generate Linux LiveSuit image by following next steps. 
[code] 
    ./configure # to list all currently supported boards
    ./configure <selected board>
    make linux # generate kernel and modules
    wget <rootfs.tar.gz>
    make livesuit ROOTFS=<rootfs.tar.gz>
    
[/code]
Flash and boot. Kernel modules can be found on nanda (FAT partition).
