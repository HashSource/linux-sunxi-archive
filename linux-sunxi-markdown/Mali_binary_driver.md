# Mali binary driver
The sun4i and sun5i use a [Mali400][34805]MP1 and sun7i uses Mali400MP2 (dual-core GPU). We have support available for several versions of the mali binary driver stack, even though our kernel tends to come with the R3P0 version. We support fbdev and X11 as windowing systems. 
## Contents
  * [1 Mali and UMP kernel drivers][34806]
    * [1.1 Modules][34807]
    * [1.2 Device permission][34808]
  * [2 Installing the UMP (Unified Memory Provider) userspace library][34809]
    * [2.1 From a package][34810]
    * [2.2 From source][34811]
      * [2.2.1 Prequisites][34812]
      * [2.2.2 Clone the repo][34813]
      * [2.2.3 Build][34814]
  * [3 Installing the Mali userspace driver][34815]
    * [3.1 Prerequisites][34816]
      * [3.1.1 Building Tools][34817]
      * [3.1.2 X11 development files (optional)][34818]
    * [3.2 Clone the repo][34819]
    * [3.3 Configure][34820]
    * [3.4 Dependencies][34821]
      * [3.4.1 libdri2 (r3p0 X11 only)][34822]
    * [3.5 Install][34823]
  * [4 Setting up the windowing system][34824]
    * [4.1 Framebuffer][34825]
    * [4.2 Xserver][34826]
  * [5 Verifying the EGL/GLES driver stack][34827]
  * [6 Common pitfalls][34828]
    * [6.1 Mesa libraries are still in the way][34829]
  * [7 See also][34830]

# Mali and UMP kernel drivers
First [get a working display driver][34831]. 
## Modules
The default config for the kernel should have the Mali kernel drivers as modules. You should be able to load it by simply running 
[code] 
    modprobe mali
    
[/code]
A cleaner solution is to have the module autoloaded at boot, by adding the following to /etc/modules: 
[code] 
    mali
    
[/code]
If you use [ a properly set up Xserver][34832], then the necessary modules will be automatically loaded when X starts. 
## Device permission
The default permissions of /dev/ump and /dev/mali make these unusable for normal users. Add a file to /etc/udev/rules.d/, perhaps called 50-mali.rules, with the following content: 
[code] 
    KERNEL=="mali", MODE="0660", GROUP="video"
    KERNEL=="ump", MODE="0660", GROUP="video"
    
[/code]
This should give a user belonging to the group video the right permissions to use the mali successfully. 
# Installing the UMP (Unified Memory Provider) userspace library
## From a package
There are [some packages available][34833] which fully install libUMP for you. 
## From source
### Prequisites
libUMP only depends on libc and the **ump** kernel module. 
**Debian/Ubuntu**
[code] 
    apt-get install git build-essential autoconf libtool
    
[/code]
**Fedora**
[code] 
    yum install gcc autoconf libtool git
    
[/code]
### Clone the repo
[code] 
    git clone https://github.com/linux-sunxi/libump.git
    cd libump
    
[/code]
### Build
**Building on Debian/Ubuntu**
If you are on debian or ubuntu, you should build the package. 
[code] 
    apt-get install debhelper dh-autoreconf fakeroot pkg-config
    
[/code]
Then build the packages, after descending into the git tree: 
[code] 
    dpkg-buildpackage -b
    
[/code]
When that finishes, install the main package: 
[code] 
    dpkg -i ../libump_*.deb
    
[/code]
**Building on other distributions**
[code] 
    autoreconf -i
    ./configure --prefix=/usr
    make
    make install
    
[/code]
# Installing the Mali userspace driver
## Prerequisites
### Building Tools
You will need to have the basic building tools installed: 
**Debian/Ubuntu**
[code] 
    apt-get install git build-essential autoconf automake
    
[/code]
**Fedora**
[code] 
    yum install gcc autoconf libtool git
    
[/code]
### X11 development files (optional)
If you wish to install the X11 version of the mali binaries, then you also need to install this: 
**Debian/Ubuntu**
[code] 
    apt-get install xutils-dev
    
[/code]
**Fedora**
[code] 
    yum install xorg-x11-server-devel
    
[/code]
## Clone the repo
[code] 
    git clone --recursive https://github.com/linux-sunxi/sunxi-mali.git
    cd sunxi-mali
    
[/code]
## Configure
Before you follow the instructions in this section, make sure that you have loaded [the mali module][34807], so that the kernel driver version can be autodetected. 
Now you can descend into sunxi-mali, and you can let it detect your environment: 
[code] 
    make config
    
[/code]
It will state the detected environment, like so: 
[code] 
    rm -f config.mk
    make config.mk
    make[1]: Entering directory `/home/libv/sunxi/sunxi-mali'
    make -f Makefile.config
    ABI="armhf" (Detected)
    VERSION="r3p0" (Detected)
    EGL_TYPE="x11" (Detected)
    make[2]: Entering directory `/home/libv/sunxi/sunxi-mali'
    echo "MALI_VERSION ?= r3p0" > config.mk
    echo "MALI_LIBS_ABI ?= armhf" >> config.mk
    echo "MALI_EGL_TYPE ?= x11" >> config.mk
    make[2]: Leaving directory `/home/libv/sunxi/sunxi-mali'
    make[1]: Leaving directory `/home/libv/sunxi/sunxi-mali'
    
[/code]
In case it complains about missing libdri2.so.1, follow the instructions in the [libdri2 (r3p0 X11 only)][34822] section and try again. 
## Dependencies
The sunxi-mali build system checks whether the selected library has all of its dependencies resolved. You might need to resolve these dependencies through your package manager. 
### libdri2 (r3p0 X11 only)
Some distributions have **libdri2** compiled into the X11 binary, instead of having it as a separate library and package. If that is the case, you need to compile libdri2 manually. 
You may need to install the following dependencies on Debian. On Fedora, the package **xorg-x11-server-devel** should be enough. 
[code] 
    apt-get install libx11-dev libxext-dev libdrm-dev x11proto-dri2-dev libxfixes-dev
[/code]
To build the library: 
[code] 
    git clone https://github.com/robclark/libdri2
    cd libdri2
    ./autogen.sh
    ./configure --prefix=/usr
    make
    make install
    ldconfig
[/code]
## Install
By following will install the GLES/EGL binaries into /usr/lib/, and EGL/GLES headers to /usr/include/: 
[code] 
    make install
[/code]
# Setting up the windowing system
## Framebuffer
If you are using the framebuffer/fbdev version of the binaries, then your setup work is done. 
You might want to change the fbdev device used by setting the **FRAMEBUFFER** environment variable. 
## Xserver
If you want a GLES capable Xserver, then you will need to install the fbturbo driver according to our [Xorg page][34832]. 
# Verifying the EGL/GLES driver stack
From the mali-sunxi repository, you can run: 
[code] 
    make test
    
[/code]
In case it complains about "/usr/bin/ld: /tmp/ccD8ofcr.o: undefined reference to symbol 'XNextEvent'", you probably need to add the linker option "-lX11" to the test/Makefile and try again. 
After it successfully builds, run: 
[code] 
    test/test
    
[/code]
And you should be able to see a smoothed triangle, either written out to the top left corner of the framebuffer, or in an X window. The console will tell you which renderer is being used: 
[code] 
    ...
    GL Vendor: "ARM"
    GL Renderer: "Mali-400 MP"
    GL Version: "OpenGL ES 2.0"
    ...
    
[/code]
Double check with: 
[code] 
    es2_info
    
[/code]
Success! 
# Common pitfalls
## Mesa libraries are still in the way
If you are seeing one of this, it means Mesa is still used instead of Mali: 
[code] 
    libEGL warning: failed to create a pipe screen for Mali DRI2
    libEGL warning: DRI2: failed to open Mali DRI2 (search paths /usr/lib/arm-linux-gnueabihf/dri)
    
[/code]
[code] 
    libEGL warning: failed to create a pipe screen for lima
    libEGL warning: DRI2: failed to open lima (search paths /usr/lib/arm-linux-gnueabihf/dri:${ORIGIN}/dri:/usr/lib/dri)
    
[/code]
Then the current best advice is to move the mesa-egl aside: 
[code] 
    mv /usr/lib/arm-linux-gnueabihf/mesa-egl/ /usr/lib/arm-linux-gnueabihf/.mesa-egl/
    
[/code]
If not present, look for _libGLESv2.so_ , _libEGL.so_ and their symlink in _/usr/lib_ (and subdir); then, make them point to _libMali.so_. 
[code] 
    ln -s /usr/lib/libMali.so /usr/lib/libGLESv2.so
    ...
    
[/code]
Awkward, but at least gets you something workable. 
Or for some cases, this can be tried: 
[code] 
    mkdir /usr/lib/arm-linux-gnueabihf/mesa-egl-BACKUP
    mv /usr/lib/arm-linux-gnueabihf/libEGL* /usr/lib/arm-linux-gnueabihf/libGLES* /usr/lib/arm-linux-gnueabihf/mesa-egl-BACKUP
    ...
    
[/code]
# See also
  * [ Setting up a working display driver][34831]
  * [ Setting up an accelerated driver for the Xserver][34834]
  * [ Hardware media acceleration (video decoding)][34835].
