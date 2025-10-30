# Armbian
[Armbian][7986] is a lightweight Debian or Ubuntu based distribution specialized for ARM developing boards. It is compiled from scratch, has powerfull build and software development tools, and a vibrant community. 
Armbian supports a wide variety of Allwinner A10, A20, A31, H3, A64 boards. 
## Contents
  * [1 Legacy kernel is no more supported][7987]
    * [1.1 Compilation][7988]
      * [1.1.1 Add legacy kernel option][7989]
      * [1.1.2 Change compiler version][7990]

## Legacy kernel is no more supported
As of October 6, 2019 Armbian [dropped support][7991] of [kernels older than 4.0][7992], which obviously effects frequently used sunxi-3.4 and sunxi-3.10 kernels. It may be more convenient for some to use these kernels for the sole purpose of utilizing [VE][7993] and [GPU][7994] with a batteries included distribution like Armbian, until [Cedrus][7995] and [Mali Open Source Driver][7996] completely make it to the matured, ready to download distribution images. 
### Compilation
You can apply the following dirty hacks to compile an Armbian image with Ubuntu Xenial Xerus rootfs image containing legacy kernel. 
Clone v19.08 branch, the latest one with the legacy kernel components 
[code] 
    git clone -b v19.08 https://github.com/armbian/build.git
[/code]
#### Add legacy kernel option
Check if the board configuration file which you are planning to use has **default** option listed in its **KERNEL_TARGET** variable. Board configuration files can be found under **build/config/boards** directory. 
#### Change compiler version
Unfortunately it is not possible to use legacy 3.4 kernel with GCC version above 4.9 without patching the kernel. Make sure that your target board family source file, listed under **build/config/sources** has **KERNEL_USE_GCC=' > 4.0'** value for **default** branch. 
Now you can execute ./compile.sh and start compiling an Armbian image.
