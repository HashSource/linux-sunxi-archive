# Tvheadend TV Tuner Server and PVR backend
**Tvheadend** is a TV tuner server (also known as a PVR backend) and video streaming software for Linux supporting television signal tuning of DVB-S, DVB-S2, DVB-C, DVB-T, ATSC, DTMB, ISDB, IPTV, and Analog video (V4L) as TV tuner input sources. 
Tvheadend TV server / PVR backend can be used as a PVR backend for [XBMC Media Center][56100] software, and while [CedarX/XBMC][56100] has already been ported to A10 based SoC, Tvheadend have not yet officially been ported but can still be used remotely over the network while testing XBMC. 
## Contents
  * [1 Overview][56101]
  * [2 Usage and Support once TVheadend is installed][56102]
    * [2.1 TVheadend Web GUI (Web User Interface)][56103]
  * [3 Using the TVheadend PVR Client in XBMC][56104]
    * [3.1 Manually adding TVheadend as a source in XBMC][56105]
  * [4 Compiling Tvheadend on Ubuntu for A10 based media players][56106]
  * [5 Compiling Tvheadend on Debian for A10 based media players][56107]
  * [6 Linux Media Infrastructure APIs supported][56108]
    * [6.1 Linux DVB API summary][56109]
    * [6.2 V4L2 API summary][56110]
    * [6.3 V4L1 API summary][56111]
  * [7 References][56112]
  * [8 See also][56113]
  * [9 External links][56114]

# Overview
Tvheadend (formerly HTS TVheadend) comes with a powerful and easy to use web interface both used for configuration and day-to-day operations, such as searching the EPG and scheduling recordings, and it even has integrated softcam support for those using card-sharing of their CAM on their local network at home. 
Even so, the most notable feature of Tvheadend is how easy it is to set up: Install it, navigate to the web user interface, drill into the TV adapters tab, select your current location and Tvheadend will start scanning channels and present them to you in just a few minutes. 
  * <http://www.lonelycoder.com/tvheadend/> \- Tvheadend official website

# Usage and Support once TVheadend is installed
  * [TVHeadend FAQ][56115]
  * [TVheadend Forum][56116]
  * Visit #hts channel at irc.freenode.net on IRC

## TVheadend Web GUI (Web User Interface)
You can access TVeadend's PVR backend/server WebGUI (Web User-Interface) by accessing <http://ipaddress:9981> and setup your DVB TV-adapter and probe channels. 
# Using the TVheadend PVR Client in XBMC
Once all is set on the the PVR backend/server-side, go to XBMC, and Add source "htsp://ipaddress:9982". If tvheadend's WebGUI found any channels, you should now be able to access those and enjoy Live TV function in XBMC. 
Note! You can use the WebGUI to schedule recordings, at the moment, however you can not yet record from within XBMC itself, but that feature will be coming to future versions of XBMC for sure. 
#### Manually adding TVheadend as a source in XBMC
This type of media source will contact to a HTS Tvheadend backend and allows you to watch Live TV. 
[code] 
     <xml>
     <name>HTS Tvheadend</name>
     <path>htsp://ipaddress:9982</path>
     </xml>
    
[/code]
If you have authentication enabled on your TVheadend backend (which is the default if, say, you've installed it using a .deb package) then you can specify the authentication credentials in the source as follows 
[code] 
     <xml>
     <name>HTS Tvheadend</name>
     <path>htsp://username:password@ipaddress:9982</path>
     </xml>
    
[/code]
# Compiling Tvheadend on Ubuntu for A10 based media players
This should work in theory: 
[code] 
    apt-get install git-core build-essential libssl-dev libssl0.9.8 pkg-config avahi-daemon
    git clone <https://github.com/tvheadend/tvheadend.git>
    cd tvheadend
    ./configure --disable-avahi
    make install
    
[/code]
To start it: 
[code] 
    tvheadend -C -f
    
[/code]
With this the grabbers weren't working 
# Compiling Tvheadend on Debian for A10 based media players
Insert the tvheadend repository in your sources.list an import the public key: 
[code] 
    echo "deb-src <http://www.lonelycoder.com/debian/> hts main" >> /etc/apt/sources.list
    wget -q --no-check-certificate <https://github.com/downloads/andoma/hts/public.key>  -O- | apt-key add -
    apt-get update
    
[/code]
Build the package: 
[code] 
    cd /usr/local/src
    apt-get source hts-tvheadend
    apt-get build-dep hts-tvheadend
    apt-get install dh-make fakeroot pkg-config libavahi-client3 libavahi-client-dev
    cd hts-tvheadend-*
    sed "s/CFLAGS  = -Wall -Werror -Wwrite-strings -Wno-deprecated-declarations/CFLAGS  = -Wall -Wwrite-strings -Wno-deprecated-declarations/g" -i Makefile
    dpkg-buildpackage -uc -us -rfakeroot
    cd ..
    
[/code]
Install the package: 
[code] 
    dpkg -i hts-tvheadend_*.deb
    
[/code]
Administrator Username and Password 
To restart you can do this: 
[code] 
    /etc/init.d/tvheadend restart
    
[/code]
# Linux Media Infrastructure APIs supported
The Linux Media Infrastructure API provides a common body of knowledge for kernel to userspace application programming interfaces used by media drivers. It converges two historically separate API, namely the Video for Linux (V4L) API, (available as a newer V4L2 API and older V4L1 API versions), and the latest Linux DVB API (Linux Digital Video Broadcasting API), plus adds the IR input event mapping API as well.[[1]][56117][[2]][56118][[3]][56119]
See more information about the [Linux Media Infrastructure API][56120] here! You can also download the [slides for the ELCE 2012 presentation][56121]. For further details about development, subscribe to linux-media mailing lists or chat on #v4l IRC channel on freenode. 
### Linux DVB API summary
The Linux DVB API (application programming interface) is essentially a kernel interface for [Digital Video Broadcasting][56122] device drivers. 
Digital Video Broadcasting is an evolving field that continuously sees new chipsets, STBs and software being developed and becoming available. As demands and requirements change, even the best-established APIs have to evolve too in order to keep pace with the technological advancements. Past development of the DVB API has proceeded in a very conservative way such that application developers see only a minimum impact on their already-written code. Today available as Linux DVB API version 5 with support for Linux kernel 3.3 and later Linux kernels. 
### V4L2 API summary
V4L2 API (Video for Linux (V4l) API). Upon release of the forthcoming 2.6.38 kernel, all but a very few vestiges of the antiquated V4L1 API will have been removed forever in favor of its successor, the V4L2 API (which, itself, now resides within the larger [Linux Media Infrastructure API][56120]). 
### V4L1 API summary
The LinuxTV project develops and maintains the media driver Linux Kernel Subsystems, which consists of devices for webcams, analog TV, digital TV and remote controllers. The video4linux subsystem was included on Kernel 2.2, and the dvb and remote controller subsystems was included in the 2.6 Kernel. The Linux kernel and the LinuxTV git tree include a fair number of drivers for commonly available PCI cards and USB devices, but the subsystems are also targeted towards Linux based set-top-boxes and embedded devices, like mobile phones. 
The original V4L and DVB API specs are still available as separate documents. 
# References
  1. [↑][56123] <http://linuxtv.org/wiki/index.php/Development:_Linux_Media_Infrastructure_API> Linux Media Infrastructure API
  2. [↑][56124] <http://www.cnx-software.com/2013/01/17/video4linux-current-status-and-future-work-elce-2012> Video4Linux: Current Status and Future Work – ELCE 2012
  3. [↑][56125] <http://www.elinux.org/images/4/4a/Video4Linux_Current_Status_and_Future_Work.pdf> slides for the ELCE 2012 presentation

# See also
  * [CedarX/XBMC][56100]

# External links
  * [Tvheadend official website][56126]
    * [Tvheadend detailed documentation][56127]
  * [LinuxTV.org - Television with Linux][56128]
    * [LinuxTV.org V4L-DVB Wiki][56129]
