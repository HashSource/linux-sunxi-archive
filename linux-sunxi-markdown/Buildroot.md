# Buildroot
Buildroot is a set of Makefiles and patches that makes it easy to generate a complete embedded Linux system. More information can be found at [buildroot.org][10946]. 
## Contents
  * [1 Build buildroot image for A10][10947]
  * [2 Flash the image][10948]
  * [3 Buildroot XBMC on the Mele A1000 and A2000 (Allwinner A10)][10949]
  * [4 Tips][10950]
  * [5 SkiffOS][10951]
  * [6 External links][10952]

## Build buildroot image for A10
Here are the instructions for building Livesuit image for Cubieboard using buildroot, they might also apply to other A10 devices. 
[code] 
    mkdir cubie && cd cubie
    git clone https://github.com/matson-hall/allwinner-buildroot.git -b cubieboard
    git clone https://github.com/matson-hall/allwinner-pack-tools.git -b cubieboard
    git clone https://github.com/matson-hall/linux-sunxi.git -b cubieboard linux-allwinner
    
    ./allwinner-pack-tools/bin/build.sh
    
[/code]
**[![Sticky-note-pin.png][10953]][10954]_Note:_ ** 64bit system needed to execute the pack tools script (files in this folder: `./allwinner-pack-tools/pack/pctools/linux/mod_update`) 
`script script.exe script_old script_old.exe u_boot_env_gen update_23 update_23.exe update_mbr update_mbr.exe`
**[![Information.png][10955]][10956]These binaries are meant to be executed on a 64bit system, so to use this script, it appears that you need a 64bit system.**
If the git commands failed, you want to wait for a few minutes before retrying. 
To log the build process: 
[code] 
    ./allwinner-pack-tools/bin/build.sh > buildlog.txt 2>&1
    
[/code]
There are some commands in the script that appear to require sudo to run (chown, ldconfig, mknod), so not clear if is expected to be run with sudo. 
This script will build buildroot and linux kernel with cubieboard default config, and pack the image into a [LiveSuit_images][10957]. 
The build should take about 10-15 minutes depending upon machine speed. If it goes much faster, your build environment may not be setup correctly. See the Instructions above for setting up build environment. 
At the end of the build, you will see 
[code] 
    ---------image is at-------------
    
    /home/«username»/cubie/allwinner-pack-tools/pack/sun4i_linux_cubieboard.img
    
[/code]
(File should be at `~/cubie/allwinner-pack-tools/pack/sun4i_linux_cubieboard.img`) ``
That's it, to flash the image to Nand flash, you need to install [LiveSuit][10958]. 
**[![Sticky-note-pin.png][10953]][10954]_Note:_ ** This image is minimalistic with only a few scripts to test hardware. You need to change rootfs if you want to build proper linux distribution. 
**[![Sticky-note-pin.png][10953]][10954]_Note:_ ** After flashing this image, if you are getting message "/bin/dwin: error while loading shared libraries: libdirectfb-1.4.so.5: cannot open shared object file: No such file or directory" in serial log, you need to 'make menuconfig' -> 'Package selection for the target' -> 'Graphics libraries and applications' and select appropriate directfb options. 
## Flash the image
[code] 
    unzip allwinner-pack-tools/tools/Livesuit-linux.zip
    chmod +x LiveSuit_For_Linux64/LiveSuit.run
    ./LiveSuit_For_Linux64/LiveSuit.run #livesuit will be installed to ~/Bin
    sudo ~/Bin/LiveSuit/LiveSuit.sh #run livesuit
    
[/code]
choose the image we built just now, let cubieboard go to [FEL][10959] mode, holding the button under the miniUSB port, then connecting the USB cable or power adapter, you should see the progress bar increasing. 
Note: LiveSuit.run installs a dynamic kernel module, you will need to install dkms in order to use this driver. It is an allwinner usb driver that talks to the board for flashing. 
[code] 
    sudo apt-get install dkms
    
[/code]
## Buildroot XBMC on the Mele A1000 and A2000 (Allwinner A10)
Team-XBMC developer Gimli (a.k.a. huceke) has updated his Buildroot development environment that he originally designed for developing XBMC on the Raspberry Pi to also be compatible with Mele A1000 and A2000 (Allwinner [A10][10960]) with [CedarX][10961] support: 
  * <http://github.com/huceke/buildroot-rbp>
  * <http://www.j1nx.nl/buildroot-xbmc-on-mele-a1000-allwinner-a10/>
  * <http://www.cnx-software.com/2012/11/12/xbmc-for-linux-on-allwinner-a10-devices-it-works-sort-of/>

_"Gimli recently decided to push his XBMC port to the public, so we now have a Buildroot XBMC on the mele A1000. Some of you are already knew about the port empatzero decided to release. This port is around for a while now and it does look like the same decoding gitches appear to happen. For some reason sometimes the decoding times show peaks in decoding time, up to the point it results in glitches._
_As both ports show similar bugs, Gimli decided to push it out in the open. Communication with Allwinner was still going on but progress was at a very slow rate. Having two different ports / approaches showing similar bugs kind of proof it is most likely something in the cedarX libraries. Hence the reason Gimli decided to release it._
_Up till this point I have been following the progress from the sideline. I saw the port of empatzero popping up, but never actually decided to give it a go. I did not really liked the full blown linux OS for only one program (XBMC)._
_I compiled the minimalistic buildroot envirnment (same as Gimli used for the RPi), compiled XBMC and merged them together with the necessary tweaks to get it running._
  * _3.0.42 kernel (just before the update to 3.0.52)._
  * _Buildroot environment._
  * _No window manager (X11). XBMC runs straight onto the framebuffer._
  * _Couple of tweaks here and there as this is not even an alpha release._
  * _All armhf compild with Linaro toolchain._

_Created a bootable SD card with a ext2 partition containing the rootfs and xbmc binaries and started it up. There appears to be a memory leak in samba armhf compiled, so disabled that for now (server, not the client). Further more there is nothing really included. No LIRC remote support or other side hardware for that matter._
_Inserted the SD card and turned on the Mele A1000. After a good couple of seconds the XBMC start splash appeared and the GUI showed up. GUI speed is fast enough and rendered at around ~40 FPS, similar as Empatzero his port._
_Exactly the same performance and issues as Empatzero his port. The only difference is the AVI playback, but it should be noted that the test results on linux-sunxi (at this moment) are done without empatzero his last commit and support for AVI and other missing codecs._
_There are still small issues here and there, but all with all not bad for a initial pre-alpha release. I will to some more testing, tweaking and adjustments. People that want to do it themselfs can already do so. Everything can be found on Gimli his github account<https://github.com/huceke>."_
## Tips
  * run /test/test.sh #you can test all the interface of cubieboard except the 96pin headers
  * run CedarXPlayerTest /root/test1.mp4 #you can play video from console
  * run /test/lightshow/lightshow #you can test openGL ES of mali400

## SkiffOS
[SkiffOS][10962] is an MIT-licensed configuration layering system for Buildroot which makes it easy to compartmentalize Buildroot configurations into layers and retarget them between different underlying device types. It also has optional support for Docker containers and running on standard Intel-based desktop PCs. 
## External links
  * [buildroot project's homepage][10946]
