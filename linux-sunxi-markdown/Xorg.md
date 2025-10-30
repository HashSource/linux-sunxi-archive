# Xorg
This page contains an explanation of how to set up the X server for our hardware. 
## Contents
  * [1 fbdev driver][60157]
  * [2 fbturbo driver][60158]
    * [2.1 Manual build][60159]
      * [2.1.1 Prerequisites][60160]
      * [2.1.2 Clone the repository][60161]
      * [2.1.3 Build][60162]
      * [2.1.4 Installation][60163]
      * [2.1.5 Configuration][60164]
    * [2.2 Packages][60165]
    * [2.3 Verification][60166]
    * [2.4 Common issues][60167]
      * [2.4.1 The log complains about being compiled without libUMP][60168]
      * [2.4.2 The screen goes off and will not restart until reset][60169]
  * [3 See also][60170]

# fbdev driver
X tends to come preinstalled with the standard fbdev driver. This gives you a working environment, but it might be lagging a bit, and you get no hardware supported 2d or 3d acceleration. 
No action needs to be taken for this driver to work though, you only need to have [a working display driver][60171]. 
# fbturbo driver
fbturbo driver works on both mainline and legacy (sunxi-3.x) kernels, utilizing a combination of various acceleration options to make your desktop experience much more fluid: 
  * NEON CPU instructions
  * sunxi G2D 2D acceleration (legacy only)
  * sunxi display engine for overlays and hardware cursor (legacy only)
  * Mali GPU acceleration for 3D/GL applications

  
For Mali support see [ our Mali binary driver installation howto][60172]). 
This driver is a further development from the ARM provided mali xorg driver, which is available from [our sunxi repositories][60173], but that driver only provides Mali support and no NEON or 2D acceleration, and doesn't use the sunxi display engine. 
## Manual build
### Prerequisites
For debian or ubuntu you need the following development packages for building X drivers: 
[code] 
    apt-get install git build-essential xorg-dev xutils-dev x11proto-dri2-dev libltdl-dev libtool automake 
    
[/code]
If you intend to use the Mali GPU, then you need to first [ install libUMP][60172] as well. 
### Clone the repository
Now get the fbturbo xf86 driver (from the 0.4.0 release tag): 
[code] 
    git clone -b 0.4.0 https://github.com/ssvb/xf86-video-fbturbo.git
    cd xf86-video-fbturbo
    
[/code]
### Build
[code] 
    autoreconf -vi
    ./configure --prefix=/usr
    make
    
[/code]
Note: in modern distro autoreconf fail and leave you with a broken configure. If running configure give you an error like: 
[code] 
    ./configure: line 17982: syntax error near unexpected token RANDR
    
[/code]
try to use the configure file in git. 
### Installation
[code] 
    make install
    
[/code]
### Configuration
Then copy over the default xorg.conf for the fbturbo driver (the preferred location for xorg.conf would be /etc/X11/ instead of /usr/share/X11/xorg.conf.d/): 
[code] 
    rm /usr/share/X11/xorg.conf.d/99-sunxifb.conf
    cp xorg.conf /etc/X11/xorg.conf
    
[/code]
## Packages
For some distributions, there are packages available. For more information, check our [ packages howto][60174]. 
## Verification
You should now be able to (re)start your xserver, have a quick look through /var/log/Xorg.0.log to verify that the correct driver has been loaded: 
[code] 
    ...
    (II) Module fbturbo: vendor="X.Org Foundation"
       compiled for 1.12.4, module version = 0.4.0
       Module class: X.Org Video Driver
       ABI class: X.Org Video Driver, version 12.1
    (II) FBTURBO: driver for framebuffer: fbturbo
    (--) using VT number 7
    ...
    
[/code]
## Common issues
### The log complains about being compiled without libUMP
If you have the following lines in your Xorg.0.log, then you need to install libUMP (or the libump-dev package), and then rebuild and install the fbturbo driver. 
[code] 
    (II) FBTURBO(0): no 3D acceleration because the driver has been compiled without libUMP
    (II) FBTURBO(0): if this is wrong and needs to be fixed, please check ./configure log
    
[/code]
### The screen goes off and will not restart until reset
This seems to be linked (to be verified) to fbturbo (former name sunxifb). DPMS has 3 options : standby, suspend and off. The standby and suspend options work. But DPMS off put off the screen with the following error on console and in dmesg : 
[code] 
     disp clks: lcd 146000000 pre_scale 1 hdmi 146000000 pll 219000000 2x 1
[/code]
A workaround is to add in /usr/share/X11/xorg.conf.d/99-sunxifb.conf, in `Section "Device"`: 
[code] 
     Option "OffTime" "0"
[/code]
However, it you still have problems, you can disable DPMS completely in the X server by properly editing xorg.conf (located either in /etc/X11 or /usr/share/X11/xorg.conf.d) add adding a Screen and Monitor section that disables DPMS. The following xorg.conf works with xf86-video-fbturbo (the new name of xf86-video-sunxifb): 
[code] 
     Section "Screen"
             Identifier      "My Screen"
             Device          "fbturbo device"
             Monitor         "My Monitor"
     EndSection
     
     Section "Device"
             Identifier      "fbturbo device"
             Driver          "fbturbo"
             Option          "fbdev" "/dev/fb0"
             Option          "SwapbuffersWait" "true"
     EndSection
     
     Section "Monitor"
             Identifier      "My Monitor"
             Option          "DPMS" "false"
     EndSection
    
[/code]
Another suggested option is to alter the other DPMS timers (OffTime is sometimes called BlankTime): 
[code] 
     Section "ServerLayout"
        Identifier "ServerLayout0"
        Option "StandbyTime" "0"
        Option "SuspendTime" "0"
     EndSection
    
    
[/code]
# See also
  * [Display driver setup][60171]
  * [ How to install the Mali binary 3D driver][60172]
  * [ Hardware Media acceleration][60175]
  * [GraphicsPerformanceX11][60176]
  * [Benchmarks][60177]
