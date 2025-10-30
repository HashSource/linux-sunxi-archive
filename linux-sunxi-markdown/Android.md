# Android
Building [Android (operating system)][7633] for an embedded A10 device can be done in a variety of ways. One method is to use the repo tool from google and point to a git repository. 
Here is one example of building and flashing Android on the "cubieboard". This same method should apply to other A10 boards. 
## Contents
  * [1 Android repo setup instructions for Android on A10][7634]
  * [2 Detailed instructions for Ubuntu 12.04 (and variants)][7635]
    * [2.1 Introduction][7636]
    * [2.2 SET BASIC PATH AND ENVIRONMENT SETTINGS][7637]
    * [2.3 X - INSTALL JAVA DEVELOPMENT KIT FROM ORACLE][7638]
    * [2.4 X - PREPARE THE ANDROID NEEDED TOOLS AND LIBS (FOR 12.04)][7639]
    * [2.5 X - PREPARE THE ANDROID NEEDED TOOLS AND LIBS (FOR 12.10)][7640]
    * [2.6 X - IS TIME TO BUILD ANDROID FROM SOURCES][7641]
  * [3 Install LiveSuit on Linux (64bit)][7642]
  * [4 Flash nand flash on your board][7643]
  * [5 Tips and tricks][7644]
    * [5.1 Uploading files from Android to a tftp server][7645]
  * [6 See also][7646]

## Android repo setup instructions for Android on A10
1) Install Java 1.6 JDK (recently Oracle has made this more difficult, but you can do it following [these instructions:][7647]) 
Get the binary here: [Oracle Java 1.6][7648]
2) [setup repo tool][7649]
3) Get the sources and sync the android repository (this will download a large amount of files and take a while) 
[code] 
    mkdir cubie_android_ics && cd cubie_android_ics
    repo init -u https://github.com/matson-hall/manifest.git -b ics-cubieboard 
    cp .repo/manifests/local_manifest.xml .repo/
    
[/code]
4)Fix the bad manifest: (fixed now, so skip this step) 
[code] 
    sudo cd cubie_android_ics/.repo
    sudo leafpad local_manifest.xml
    
[/code]
Now change this line and save the modified manifest: 
[code] 
    <project path="kernel/allwinner/common" name="linux-allwinner" remote="matson-hall" revision="ics-cubieboard" />
    
[/code]
to: 
[code] 
    <project path="kernel/allwinner/common" name="linux-sunxi" remote="matson-hall" revision="ics-cubieboard" />
    
[/code]
5)sync the repository: 
[code] 
    repo sync 
    
[/code]
6) build android -- (Note: you will need around 40GB of free space to build android) 
[code] 
    source build/envsetup.sh 
    lunch 4   # option 4 is cubieboard-eng
    make -j4   # there maybe errors like to ask you "make update-api"
    
[/code]
7) Create the install image: 
[code] 
    chmod +x ./tools/pack-cm.sh
    ./tools/pack-cm.sh 
    
[/code]
You will see: 
[code] 
    ---------image is at-------------
    /home/username/cubie/allwinner-pack-tools/pack/sun4i_linux_cubieboard.img
    
[/code]
## Detailed instructions for Ubuntu 12.04 (and variants)
(courtesy of Silverio Diquigiovanni) 
### Introduction
In that document I will describe step by step all operations needed to build android ICS for AllWinner cubieboard using XUBUNTU 12.04-64Bit Precise Pangolin LTS. Same info are valid for all UBUNTU 12.04-64Bit distros like LUBUNTU, KUBUNTU and so on. I've also tried, with success, to use XUBUNTU 12.10-64bit so some parts are also 12.10 related. 
PS: That's a document for DUMMIES / NOOBS so don't care if I was so pedant in some step description. 
To keep simple my job I've installed XUBUNTU in a VMware Virtual Machine, actually in VMware Fusion with Mac OS X Lion as host computer. To work fine the virtual machine should have at least 4GB of ram and a disk of least 40GB. Also SWAP disk is important and mine was set to 2GB. More than one CPU are apprecied. 
PS: I've used a virtual machine because some things on XUBUNTU evironment need to be "forced" and I would not to use 
[code] 
       that for my daily jobs, but you can choose to use your working machine.
    
[/code]
So : \- Get xubuntu 12.04-64Bit from xubuntu repositories and install it in a virtual machine. Remember to update it. \- Install VMware Tools (if you need them - not necessary). 
  

### SET BASIC PATH AND ENVIRONMENT SETTINGS
[code] 
    cd ~/
    mkdir -p android
    mkdir -p android/bin
    
[/code]
ADD export paths for android develop environment 
[code] 
    nano ~/.bashrc
    # add this line at file tail
    export PATH=$PATH:/home/shine/android/bin
    
[/code]
CLOSE and REOPEN terminal console 
  

### X - INSTALL JAVA DEVELOPMENT KIT FROM ORACLE
DOWNLOAD and INSTALL repo 
[code] 
    sudo apt-get install curl
    curl <https://dl-ssl.google.com/dl/googlesource/git-repo/repo> > ~/android/bin/repo
    chmod a+x ~/android/bin/repo
    
[/code]
DOWNLOAD and INSTALL jdk-6u24-linux-x64.bin from oracle download page 
[code] 
    cd ~/Downloads/
    chmod +x jdk-6u24-linux-x64.bin
    ./jdk-6u24-linux-x64.bin 
    
[/code]
[code] 
    sudo mkdir /usr/lib/jvm
    sudo mv jdk1.6.0_24 /usr/lib/jvm
    sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.6.0_24/bin/java" 1
    sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.6.0_24/bin/javac" 1
    sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/jvm/jdk1.6.0_24/bin/javaws" 1
    sudo update-alternatives --config java
    sudo update-alternatives --config javac
    
[/code]
[code] 
    sudo nano /etc/environment
    # add this line at file tail
    JAVA_HOME="/usr/lib/jvm/jdk1.6.0_24"
    
[/code]
[code] 
    source /etc/environment
    
[/code]
  

### X - PREPARE THE ANDROID NEEDED TOOLS AND LIBS (FOR 12.04)
[code] 
    sudo apt-get install git gnupg flex bison gperf build-essential zip curl libc6-dev libncurses5-dev:i386 \
       x11proto-core-dev libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-glx:i386 \
         libgl1-mesa-dev g++-multilib mingw32 tofrodos python-markdown libxml2-utils xsltproc \
       zlib1g-dev:i386
    
[/code]
[code] 
    sudo ln -s /usr/lib/i386-linux-gnu/mesa/libGL.so.1 /usr/lib/i386-linux-gnu/libGL.so
    
[/code]
  

### X - PREPARE THE ANDROID NEEDED TOOLS AND LIBS (FOR 12.10)
[code] 
       sudo apt-get install git-core gnupg flex bison gperf build-essential zip curl zlib1g-dev zlib1g-dev:i386 \
       libc6-dev lib32ncurses5-dev ia32-libs x11proto-core-dev libx11-dev:i386 \ 
       libreadline6-dev:i386 lib32z-dev libgl1-mesa-glx:i386 libgl1-mesa-dev g++-multilib \
       mingw32 tofrodos python-markdown libxml2-utils xsltproc readline-common libreadline6-dev \
       libreadline6 lib32readline-gplv2-dev libncurses5-dev lib32readline5 lib32readline6 \
       libreadline-dev libreadline6-dev:i386 libreadline6:i386 bzip2 libbz2-dev libbz2-1.0 \
       libghc-bzlib-dev lib32bz2-dev libsdl1.2-dev libesd0-dev squashfs-tools pngcrush schedtool \
                                libwxgtk2.8-dev python
    
[/code]
[code] 
      	sudo ln -s /usr/lib/i386-linux-gnu/mesa/libGL.so.1 /usr/lib/i386-linux-gnu/libGL.so
    
[/code]
Unfortunately ICS don't compile with gcc (Ubuntu/Linaro 4.7.2-2ubuntu1) 4.7.2 already installed on (*)ubuntu so we need to manually install 4.4 version with following command: 
[code] 
       sudo apt-get install gcc-4.4 g++-4.4 g++-4.4-multilib gcc-4.4-multilib
    
[/code]
and manually change the softlink with : 
[code] 
          ...
    
[/code]
### X - IS TIME TO BUILD ANDROID FROM SOURCES
[code] 
    mkdir -p ~/android/build/Cubieboard
    cd ~/android/build/Cubieboard/
    wget <http://dl.cubieboard.org/software/a10-cubieboard/android/cubieboard_opentv.tar.gz>
    (also look at <http://github.com/cubieboard>)
    
[/code]
Now we will check that cubieboard_opentv.tar.gz match what used by that document: 
[code] 
    md5sum cubieboard_opentv.tar.gz 
    $ -> d36631c98f30ebc0f43eeafeba8201ec  cubieboard_opentv.tar.gz
    
[/code]
[code] 
    tar -zxf cubieboard_opentv.tar.gz
    cd cubieboard-tv-sdk/
    
[/code]
A this point is necessary to fix a but in cubieboard_opentv script and precisely to following file: 
[code] 
    nano frameworks/base/media/libstagefright/Android.mk
    search LOCAL_STATIC_LIBRARIES and add to list: libstagefright_rtsp \ so you get:
    
[/code]
[code] 
    LOCAL_STATIC_LIBRARIES := \
    libstagefright_color_conversion \
    libstagefright_aacenc \
    libstagefright_amrnbenc \
    libstagefright_amrwbenc \
    libstagefright_avcenc \
    libstagefright_m4vh263enc \
    libstagefright_matroska \
    libstagefright_timedtext \
    libvpx \
    libstagefright_mpeg2ts \
    libstagefright_id3 \
    libFLAC \
    libstagefright_rtsp \
           ...
    
[/code]
Time to build all from cubieboard_opentv root path :) 
[code] 
    . build/envsetup.sh 
    lunch        # (perhaps typo? Maybe 'launch'? --simos)
    make -j4
    
[/code]
and create the .img that is suitable for LiveSuit 
[code] 
    tools/pack-cm.sh
    
[/code]
## Install [LiveSuit][7650] on Linux (64bit)
[code] 
    sudo apt-get install dkms
    git clone https://github.com/matson-hall/allwinner-pack-tools.git -b cubieboard
    unzip allwinner-pack-tools/tools/Livesuit-linux.zip
    chmod +x LiveSuit_For_Linux64/LiveSuit.run
    ./LiveSuit_For_Linux64/LiveSuit.run #livesuit will be installed to ~/Bin
    
[/code]
## Flash nand flash on your board
[code] 
    sudo ~/Bin/LiveSuit/LiveSuit.sh #run livesuit
    
[/code]
1) Livesuit GUI will start 
2) Choose the image we built just now (sun4i_linux_cubieboard.img) 
3) Disconnect all power to board, connect USB cable to board side, but not computer, then hold down "usb boot" button on your board, and plug in USB to computer -- a new device should be detected. If using a virtual machine you may need to modify your .vmx file to include the "skip reset usb-quirk" option. Instead of this method, you can follow the instructions to get into [FEL][7651] mode. 
4) It should ask to format the partition first, say yes. 
5) You should see the progress bar increasing. 
6) flashing should complete in about 3-4 minutes 
## Tips and tricks
### Uploading files from Android to a tftp server
  * Android will expose a shell on serial line. You will not get a prompt, just type in some command and press Enter to see if the shell is really there.
  * Set up network, replace XXX with YYY

[code] 
       ip addr add 192.168.0.XXX/24 dev eth0
       ip link set eth0 up
       ip route add 0.0.0.0/0 via 192.168.0.YYY dev eth0
    
[/code]
  * Use tftp, replace ZZZ.

    **NOTE:** Your tftp root directory should be world writable and there should be a world writable file with the name _$TFTPROOT/path/to/file.txt_ on the server, otherwise it will not work.
[code] 
       busybox tftp -p -l /path/to/file.txt 192.168.0.ZZZ
    
[/code]
# See also
  * [ Building Jellybean for cubieboard.][7652]
