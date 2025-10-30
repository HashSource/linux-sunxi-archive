# Qt5 For Mali Binaries
This page describes ways to build a Qt5 toolchain for Allwinner devices. 
## Contents
  * [1 Qt cross-compiler toolchain][46278]
    * [1.1 Get ARM C and C++ cross-compilers][46279]
    * [1.2 Build the system root][46280]
    * [1.3 Install video drivers][46281]
    * [1.4 Install development packages][46282]
    * [1.5 Download Qt][46283]
    * [1.6 Create Qt device config][46284]
    * [1.7 Configure Qt][46285]
    * [1.8 Make and install][46286]
    * [1.9 Test][46287]
    * [1.10 Debian Wheezy][46288]
  * [2 Native compilation][46289]

# Qt cross-compiler toolchain
A cross-compiler toolchain is the most practical option for building Qt binaries. Native compiler performance on most Allwinner devices is relatively good but you can get better performance on a laptop. The configuration and build process of a cross-compiler toolchain is not too difficult. You may have a working Qt cross-compiler in a matter of minutes, provided you have a system root for your device on the host machine. The below solution should work for all Cortex-A8 devices with Mali-400 and can also apply to devices with other ARM processor cores after minor modifications. The instructions work for Debian Jessie. Note that old stable Sunxi kernels before 3.4.105 may be incompatible with Jessie because of systemd. In that case Debian Wheezy is an option, see [Qt5_For_Mali_Binaries#Debian_Wheezy][46290] for appropriate adjustments. 
## Get ARM C and C++ cross-compilers
Install a C++ cross-compiler on your host, for example, from the [Emdebian][46291] repository: 
[code] 
     sudo apt-get update
     sudo apt-get install gcc-4.7-arm-linux-gnueabihf g++-4.7-arm-linux-gnueabihf
    
[/code]
provided that your `/etc/apt/sources.list` has the following lines: 
[code] 
     deb <http://www.emdebian.org/debian/> testing main
     deb <http://www.emdebian.org/debian/> unstable main
    
[/code]
Install appropriate alternatives by hand since these are not created automatically: 
[code] 
     sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcc \
       arm-linux-gnueabihf-gcc /usr/bin/arm-linux-gnueabihf-gcc-4.7 100
     sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-g++ \
       arm-linux-gnueabihf-g++ /usr/bin/arm-linux-gnueabihf-g++-4.7 100
    
[/code]
## Build the system root
Set up a Debian Testing system on your host. See [Mainline_Debian_HowTo][46292] for exact commands. SD-card setup can be skipped if installing on the local disk. I will assume `/var/sunxi-root` to be the system root: 
[code] 
     export SUNXI_SYSROOT=/var/sunxi-root
    
[/code]
## Install video drivers
Download `libump` sources and `libMali` binaries as described in [Mali_binary_driver][46293] to your disk. Copy the downloaded trees to `$SUNXI_SYSROOT` and install these libraries from within chroot. 
## Install development packages
Install XCB packages to `$SUNXI_SYSROOT` from chroot: 
[code] 
    apt-get install libxcb1 libxcb1-dev libx11-xcb1 libx11-xcb-dev \
      libxcb-keysyms1 libxcb-keysyms1-dev libxcb-image0 libxcb-image0-dev \
      libxcb-shm0 libxcb-shm0-dev libxcb-icccm4 libxcb-icccm4-dev \
      libxcb-sync0-dev libxcb-render-util0 libxcb-render-util0-dev \
      libxcb-xfixes0-dev libxrender-dev libxcb-shape0-dev libxcb-randr0-dev \
      libxcb-glx0-dev
    
[/code]
Also install zlib library and headers: 
[code] 
    apt-get install zlib1g-dev
    
[/code]
Do not exit from the chroot prompt because you are going to use it below. 
## Download Qt
Download Qt to your host (not to `$SUNXI_SYSROOT`): 
[code] 
     git clone <git://gitorious.org/qt/qt5.git> qt5
     cd qt5
     git checkout 5.4
     perl init-repository --no-webkit
    
[/code]
## Create Qt device config
[code] 
     mkdir qtbase/mkspecs/devices/linux-sunxi-g++
    
[/code]
[code] 
     cat <<EOF > qtbase/mkspecs/devices/linux-sunxi-g++/qplatformdefs.h
     #include "../../linux-g++/qplatformdefs.h"
     EOF
    
[/code]
[code] 
    cat <<EOF > qtbase/mkspecs/devices/linux-sunxi-g++/qmake.conf
    #
    # Qt system configuration for Sunxi Cortex-A8 devices
    #
    # Mali library and include files should be found in the standard locations in
    # /usr in sysroot.
    #
    
    include(../common/linux_device_pre.conf)
    
    QT_QPA_DEFAULT_PLATFORM = xcb
    
    DISTRO_OPTS += deb-multi-arch
    DISTRO_OPTS += hard-float
    
    SYSROOT_INC = $$[QT_SYSROOT]/usr/include
    SYSROOT_LIB = $$[QT_SYSROOT]/usr/lib
    
    COMPILER_FLAGS = -marm -march=armv7-a -mtune=cortex-a8
    
    QMAKE_CFLAGS   += -I $${SYSROOT_INC} \
                      -I $${SYSROOT_INC}/$${GCC_MACHINE_DUMP}
    
    QMAKE_CXXFLAGS += -I $${SYSROOT_INC} \
                      -I $${SYSROOT_INC}/$${GCC_MACHINE_DUMP}
    
    QMAKE_CXXFLAGS_RELEASE += -O3
    
    QMAKE_LFLAGS   += -Wl,-rpath-link,$$[QT_SYSROOT]/usr/lib \
                      -Wl,-rpath-link,$$[QT_SYSROOT]/lib
    
    QMAKE_LIBS += -lrt -lpthread -ldl
    
    # Mali EGL and GLES2 are in fact located in the same .so file.
    QMAKE_INCDIR_EGL        = $$[SYSROOT_INC]
    QMAKE_LIBDIR_EGL        = $$[SYSROOT_LIB]
    QMAKE_INCDIR_OPENGL_ES2 = $${QMAKE_INCDIR_EGL}
    QMAKE_LIBDIR_OPENGL_ES2 = $${QMAKE_LIBDIR_EGL}
    
    QMAKE_LIBS_EGL          = -lEGL
    QMAKE_LIBS_OPENGL_ES2   = -lGLESv2
    
    include(../common/linux_arm_device_post.conf)
    
    load(qt_config)
    EOF
    
[/code]
## Configure Qt
The below will configure Qt for installation into `/opt/qt/sunxi` on both the host and the target: 
[code] 
    ./configure -v -debug -opensource -confirm-license -no-use-gold-linker \
      -nomake examples -nomake tests -nomake tools -no-cups -no-pch -no-linuxfb \
      -skip qtquick1 -skip declarative -skip multimedia -opengl es2 -no-eglfs \
      -system-xcb -system-zlib -sysroot $SUNXI_SYSROOT -device linux-sunxi-g++ \
      -device-option CROSS_COMPILE=arm-linux-gnueabihf- -prefix /opt/qt/sunxi
    
[/code]
If configuration is successfull, you will see stats like these: 
[code] 
    Build options:
      Configuration .......... accessibility accessibility-atspi-bridge audio-backend c++11 clock-gettime clock-monotonic compile_examples concurrent cross_compile dbus debug egl evdev eventfd freetype full-config getaddrinfo getifaddrs harfbuzz iconv inotify ipv6ifname large-config largefile medium-config minimal-config mremap nis opengl opengles2 pcre png posix_fallocate qpa qpa reduce_exports rpath shared small-config system-zlib xcb xcb-glx xcb-plugin xcb-render xcb-xlib xkbcommon-qt 
      Build parts ............ libs
      Mode ................... debug
      Using C++11 ............ yes
      Using gold linker....... no
      Using PCH .............. no
      Target compiler supports:
        Neon ................. no
    
    Qt modules and options:
      Qt D-Bus ............... yes (loading dbus-1 at runtime)
      Qt Concurrent .......... yes
      Qt GUI ................. yes
      Qt Widgets ............. yes
      Large File ............. yes
      QML debugging .......... yes
      Use system proxies ..... no
    
    Support enabled for:
      Accessibility .......... yes
      ALSA ................... no
      CUPS ................... no
      Evdev .................. yes
      FontConfig ............. no
      FreeType ............... yes (bundled copy)
      Glib ................... no
      GTK theme .............. no
      HarfBuzz ............... yes (bundled copy)
      Iconv .................. yes
      ICU .................... no
      Image formats: 
        GIF .................. yes (plugin, using bundled copy)
        JPEG ................. yes (plugin, using bundled copy)
        PNG .................. yes (in QtGui, using bundled copy)
      journald ............... no
      mtdev .................. no
      Networking: 
        getaddrinfo .......... yes
        getifaddrs ........... yes
        IPv6 ifname .......... yes
        OpenSSL .............. no
      NIS .................... yes
      OpenGL / OpenVG: 
        EGL .................. yes
        OpenGL ............... yes (OpenGL ES 2.0+)
        OpenVG ............... no
      PCRE ................... yes (bundled copy)
      pkg-config ............. yes 
      PulseAudio ............. no
      QPA backends: 
        DirectFB ............. no
        EGLFS ................ no
        KMS .................. no
        LinuxFB .............. no
        XCB .................. yes (system library)
          EGL on X ........... no
          GLX ................ yes
          MIT-SHM ............ yes
          Xcb-Xlib ........... yes
          Xcursor ............ yes (loaded at runtime)
          Xfixes ............. yes (loaded at runtime)
          Xi ................. yes (loaded at runtime)
          Xi2 ................ no
          Xinerama ........... yes (loaded at runtime)
          Xrandr ............. yes (loaded at runtime)
          Xrender ............ no
          XKB ................ no
          XShape ............. yes
          XSync .............. yes
          XVideo ............. yes
      Session management ..... yes
      SQL drivers: 
        DB2 .................. no
        InterBase ............ no
        MySQL ................ no
        OCI .................. no
        ODBC ................. no
        PostgreSQL ........... no
        SQLite 2 ............. no
        SQLite ............... yes (plugin, using bundled copy)
        TDS .................. no
      udev ................... no
      xkbcommon .............. yes (bundled copy, XKB config root: /usr/share/X11/xkb)
      zlib ................... yes (system library)
    
    
    NOTE: Qt is using double for qreal on this system. This is binary incompatible against Qt 5.1.
    Configure with '-qreal float' to create a build that is binary compatible with 5.1.
    
    Qt is now configured for building. Just run 'make'.
    Once everything is built, you must run 'make install'.
    Qt will be installed into /opt/qt/sunxi
    
    Prior to reconfiguration, make sure you remove any leftovers from
    the previous build.
    
[/code]
## Make and install
This will make and install the cross-compiler as well as the Qt environment for the Sunxi device: 
[code] 
     make -j4
     sudo make install
    
[/code]
This installs the host cross-compiler into `/opt/qt/sunxi` and the target shared libraries and utilities to `$SUNXI_SYSROOT/opt/qt/sunxi`. You should then be able to copy the target Qt tree from `$SUNXI_SYSROOT` onto your Sunxi device root file system. 
You may also want to add Qt binaries such as `qmake` to the path on the host: 
[code] 
     export PATH=/opt/qt/sunxi/bin:$PATH
    
[/code]
## Test
[code] 
     cd qtbase/examples/qtestlib/tutorial1/
     qmake
     make
    
[/code]
The above should produce a working ARM binary `./tutorial1`. Run it from chroot with the option `-platform offscreen`. 
## Debian Wheezy
On Debian Wheezy system zlib doesn't seem to link correctly with Qt 5.4. Therefore don't install zlib1g-dev onto the target and configure Qt without the `-system-zlib` option. Also remove `-lrt` from the definition of `QMAKE_LIBS` in `qtbase/mkspecs/devices/linux-sunxi-g++/qmake.conf`. Debootstrap and chroot procedures are the same as for Jessie, only specify **wheezy** instead of **testing** during bootstrapping and apt initialisation. 
# Native compilation
Another way to get Qt on a Sunxi device is to compile Qt from source in-place. 
Here are instructions to be executed on the device, assuming X11, UMP and Mali drivers (see [Mali_binary_driver][46293]): 
[code] 
      wget <http://download.qt-project.org/official_releases/qt/5.1/5.1.0/single/qt-everywhere-opensource-src-5.1.0.tar.gz>
      tar -xzf qt-everywhere-opensource-src-5.1.0.tar.gz
      cd qt-everywhere-opensource-src-5.1.0
      ./configure -release -opensource -confirm-license -opengl es2 -no-eglfs -no-linuxfb -no-pch
      make
      make install
    
[/code]
This will take hours to compile on Allwinner A10 device! You may want to run it overnight. 
It may make sense to check the configure output before starting compilation. It may look like this (be sure that OpenGL ES 2.x is detected): 
[code] 
       Configure summary
    
    Build type:    linux-g++ (arm, CPU features: neon)
    Platform notes:
    
                - Also available for Linux: linux-kcc linux-icc linux-cxx
            
    Build options:
      Configuration .......... accessibility accessibility-atspi-bridge alsa audio-backend c++11 clock-gettime clock-monotonic concurrent cups dbus egl evdev eventfd fontconfig full-config getaddrinfo getifaddrs glib gstreamer gtk2 gtkstyle iconv icu inotify ipv6ifname large-config largefile libudev medium-config minimal-config mremap neon nis opengl opengles2 openssl pcre png pulseaudio qpa qpa reduce_exports reduce_relocations release rpath shared small-config system-freetype system-jpeg system-png system-zlib v8 v8snapshot xcb xcb-glx xcb-render xcb-xlib xinput2 xkbcommon-qt xlib xrender 
      Build parts ............ libs tools examples
      Mode ................... release
      Using C++11 ............ yes
      Using PCH .............. no
      Target compiler supports:
        iWMMXt/Neon .......... no/yes
    
    Qt modules and options:
      Qt D-Bus ............... yes (loading dbus-1 at runtime)
      Qt Concurrent .......... yes
      Qt GUI ................. yes
      Qt Widgets ............. yes
      JavaScriptCore JIT ..... yes (To be decided by JavaScriptCore)
      QML debugging .......... yes
      Use system proxies ..... no
    
    Support enabled for:
      Accessibility .......... yes
      ALSA ................... yes
      CUPS ................... yes
      FontConfig ............. yes
      Iconv .................. yes
      ICU .................... yes
      Image formats: 
        GIF .................. yes (plugin, using system library)
        JPEG ................. yes (plugin, using system library)
        PNG .................. yes (in QtGui, using system library)
      Glib ................... yes
      GStreamer .............. yes
      GTK theme .............. yes
      Large File ............. yes
      libudev ................ yes
      Networking: 
        getaddrinfo .......... yes
        getifaddrs ........... yes
        IPv6 ifname .......... yes
        OpenSSL .............. yes (loading libraries at run-time)
      NIS .................... yes
      OpenGL ................. yes (OpenGL ES 2.x)
      OpenVG ................. no
      PCRE ................... yes (bundled copy)
      pkg-config ............. yes 
      PulseAudio ............. yes
      QPA backends: 
        DirectFB ............. no
        EGLFS ................ no
        KMS .................. no
        LinuxFB .............. no
        XCB .................. yes (system library)
          MIT-SHM ............ yes
          Xcursor ............ yes (loaded at runtime)
          Xfixes ............. yes (loaded at runtime)
          Xi ................. no
          Xi2 ................ yes
          Xinerama ........... yes (loaded at runtime)
          Xrandr ............. yes (loaded at runtime)
          Xrender ............ yes
          XKB ................ no
          XShape ............. yes
          XSync .............. yes
          XVideo ............. yes
      Session management ..... yes
      SQL drivers: 
        DB2 .................. no
        InterBase ............ no
        MySQL ................ no
        OCI .................. no
        ODBC ................. yes (plugin)
        PostgreSQL ........... no
        SQLite 2 ............. no
        SQLite ............... yes (plugin, using bundled copy)
        TDS .................. no
      udev ................... yes
      xkbcommon .............. yes (bundled copy)
      zlib ................... yes (system library)
    
    NOTE: libxkbcommon 0.2.0 (or higher) not found on the system, will use 
    the bundled version from 3rd party directory.
    
    Qt is now configured for building. Just run 'gmake'.
    Once everything is built, you must run 'gmake install'.
    Qt will be installed into /usr/local/Qt-5.1.0
    
    Prior to reconfiguration, make sure you remove any leftovers from
    the previous build.
    
[/code]
Now in order to test it, we can download and compile the Qt5 Cinematic Experience demo: 
[code] 
       wget <http://quitcoding.com/download/Qt5_CinematicExperience_rpi_1.0.tgz>
       tar -xzf Qt5_CinematicExperience_rpi_1.0.tgz
       cd Qt5_CinematicExperience_rpi_1.0
       export PATH=/usr/local/Qt-5.1.0/bin:$PATH
       qmake
       make
       DISPLAY=:0 ./Qt5_CinematicExperience --fullscreen
    
[/code]
There are also many other Qt5 demos.
