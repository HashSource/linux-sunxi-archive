# Cubieboard/Cubieboard Linux-3.4
< [Cubieboard][13592]
 
## Get source code
[code] 
    mkdir ~/mylinux
    cd ~/mylinux
    git clone <git://github.com/cubieboard/sunxi-tools.git> tools
    git clone <git://github.com/cubieboard/u-boot-sunxi.git> u-boot
    git clone <git://github.com/cubieboard/buildroot-sunxi.git> buildroot
    git clone <git://github.com/cubieboard/linux-sunxi.git> linux-3.4
    (cd tools; git checkout -b sunxi-3.4-cb origin/sunxi-3.4-cb)
    (cd u-boot; git checkout -b sunxi-3.4-cb origin/sunxi-3.4-cb)
    (cd buildroot; git checkout -b sunxi-3.4-cb origin/sunxi-3.4-cb)
    (cd linux-3.4; git checkout -b sunxi-3.4-cb origin/sunxi-3.4-cb)
    
[/code]
## Build from souce code
[code] 
    tools/build.sh
    
[/code]
The build.sh script will finally generate an image suitable for livesuit 
## See also
  * [Boot Process ][13595]
