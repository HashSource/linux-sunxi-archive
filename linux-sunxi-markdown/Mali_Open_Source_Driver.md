# Mali Open Source Driver
The [Mali][34760] series is a GPU (Graphics Processor Unit) from ARM Ltd. (ARM Holdings plc), designed for embedded systems. 
## Contents
  * [1 Overview][34761]
  * [2 Kernel drivers][34762]
  * [3 Userspace drivers][34763]
    * [3.1 Dependencies][34764]
    * [3.2 Configuration and Build][34765]
    * [3.3 Cross Compiling][34766]
      * [3.3.1 Build dependencies for cross-compiling][34767]
      * [3.3.2 Meson cross compile settings for armv7hf][34768]
      * [3.3.3 Configuration][34769]
    * [3.4 Wayland support][34770]

# Overview
Two open source drivers based on reverse engineering efforts exist for the Mali GPUs. 
  * Lima covers the Utgard family (Mali-400/450) used on most Allwinner SoCs that have Mali GPUs.
  * Panfrost covers Midgard (Mali-T[678]xx) (Mali-T720 used on the H6), and Bifrost (Mali-G[357]x) (not implemented by Allwinner).

These include both kernel drivers and userspace drivers in Mesa. 
As of 2019/04/12, both drivers have had their userspace components merged into upstream Mesa. 
Lima's kernel driver has been merged, and will be in Linux kernel v5.2, while Panfrost's kernel driver has gone through multiple review cycles, and is likely to be merged soon. 
# Kernel drivers
The lima driver is enabled by the kernel config option **DRM_LIMA**. The panfrost driver is enabled by the kernel config option **DRM_PANFROST**. 
Enable the desired options and follow the mainline kernel build procedures. 
# Userspace drivers
The userspace drivers are part of the [Mesa 3D Graphics Library][34771]. 
Mesa's website has a guide on howto build and install the library: [[1]][34772]. Following it will build in support for mostly everything. 
The following are some steps using meson to build a reduced version just for Mali support. 
## Dependencies
Mesa has a lot of build time dependencies. For the reduced version we are building, install the following packages (on Debian): 
[code] 
    g++ meson python3-mako zlib1g-dev libexpat1-dev libdrm-dev flex bison libx11-dev libxext-dev libxdamage-dev \
    libxcb-glx0-dev libx11-xcb-dev libxcb-dri2-0-dev libxcb-dri3-dev libxcb-present-dev libxshmfence-dev \
    libxxf86vm-dev libxrandr-dev x11proto-gl-dev x11proto-dri2-dev gettext pkg-config
    
[/code]
## Configuration and Build
[code] 
    # Check out mesa
    git clone <https://gitlab.freedesktop.org/mesa/mesa.git>
    # Or Choose the last Stable tag, ex: 'mesa-19.3.2'
    git clone --branch mesa-19.3.2 <https://gitlab.freedesktop.org/mesa/mesa.git>
    cd mesa/
    
[/code]
[code] 
    # Configure the build
    #
    # Only the lima and panfrost drivers are enabled.
    # kmsro is the "kernel mode-setting render-only" support driver.
    # swrast is the fallback software renderer.
    # X11, DRM, and surfaceless targets are enabled
    # DRI and Vulkan drivers are not supported.
    # For aarch32
    meson build/ --optimization s --buildtype release --prefix=/usr/local --libdir=lib/arm-linux-gnueabihf \
    -Dgallium-drivers=lima,panfrost,kmsro,swrast -Dplatforms=x11,drm,surfaceless -Dvulkan-drivers= -Ddri-drivers= \
    -Dllvm=false
    # For aarch64
    meson build/ --optimization s --buildtype release --prefix=/usr/local --libdir=lib/aarch64-linux-gnu \
    -Dgallium-drivers=lima,panfrost,kmsro,swrast -Dplatforms=x11,drm,surfaceless -Dvulkan-drivers= -Ddri-drivers= \
    -Dllvm=false
    
[/code]
[code] 
    # Build the library
    ninja -C build/
    
[/code]
[code] 
    # Install the library (under /usr/local as previously specified with the --prefix parameter)
    sudo ninja -C build/ install
    
[/code]
## Cross Compiling
While the Mesa library isn't very large, compiling natively on ARM / ARM64 is quite slow. 
### Build dependencies for cross-compiling
Install the following packages (on Debian). 
[code] 
    g++-arm-linux-gnueabihf meson python3-mako flex bison
    zlib1g-dev:armhf libexpat1-dev:armhf libdrm-dev:armhf libx11-dev:armhf libxext-dev:armhf libxdamage-dev:armhf
    libxcb-glx0-dev:armhf libx11-xcb-dev:armhf libxcb-dri2-0-dev:armhf libxcb-dri3-dev:armhf libxcb-present-dev:armhf
    libxshmfence-dev:armhf libxxf86vm-dev:armhf libxrandr-dev:armhf
    
[/code]
### Meson cross compile settings for armv7hf
Put the following in some file. This will be used by meson. 
[code] 
    [binaries]
    c = 'arm-linux-gnueabihf-gcc'
    cpp = 'arm-linux-gnueabihf-g++'
    ar = 'arm-linux-gnueabihf-ar'
    strip = 'arm-linux-gnueabihf-strip'
    pkgconfig = 'arm-linux-gnueabihf-pkg-config'
    
    [host_machine]
    system = 'linux'
    cpu_family = 'arm'
    cpu = 'armv7hl'
    endian = 'little'
    
    
[/code]
### Configuration
Follow the same steps as the native build, but add the following to the **meson** command. 
[code] 
    --cross-file=<path to cross compile settings> --libdir=lib/arm-linux-gnueabihf
    
[/code]
## Wayland support
If you want to build wayland support as well, add **wayland** to the list of **platforms** in the configuration command. 
You will need to install the following dependency packages. 
[code] 
    libwayland-dev wayland-protocols libwayland-egl-backend-dev
    
[/code]
For cross-compiling, you will need to install both the native and target versions of **libwayland-dev**.
