# CyanogenMod
This guide will get you started on adapting CyanogenMod to a new Allwinner device 
  

## Contents
  * [1 Prepare the Build Environment][15692]
    * [1.1 Install the ADB][15693]
    * [1.2 Install the Build Packages][15694]
    * [1.3 Create the Directories][15695]
    * [1.4 Install the Repository][15696]
      * [1.4.1 For the Ice Cream Sandwich (4.0.4) Repository][15697]
      * [1.4.2 For the JellyBean (4.1.2) Repository][15698]
      * [1.4.3 For the JellyBean (4.2.2) Repository][15699]
      * [1.4.4 For the JellyBean (4.3) Repository][15700]
  * [2 Creating a basic new device tree][15701]
  * [3 Copy proprietary files][15702]
  * [4 Building CyanogenMod][15703]
    * [4.1 Fetch Prebuilts][15704]
    * [4.2 Configure Build & Compile][15705]
  * [5 Install][15706]

## Prepare the Build Environment
    [![Sticky-note-pin.png][15707]][15708] _Note:_ You only need to do these steps the first time you build. If you previously prepared your build environment, skip to **[creating your device tree][15701]**.
### Install the [ADB][15709]
### Install the Build Packages
Install (using the package manager of your choice): 
For 32-bit & 64-bit systems: 
    `git-core gnupg flex bison gperf libsdl1.2-dev libesd0-dev libwxgtk2.6-dev squashfs-tools build-essential zip curl libncurses5-dev zlib1g-dev openjdk-6-jdk pngcrush schedtool`
For 64-bit only systems: 
    `g++-multilib lib32z1-dev lib32ncurses5-dev lib32readline5-dev gcc-4.3-multilib g++-4.3-multilib`
    [![Sticky-note-pin.png][15707]][15708] _Note:_ `gcc-4.3-multilib g++-4.3-multilib` is no longer available for Ubuntu 11.04 64-bit, but should still build without issue.
### Create the Directories
You will need to set up some directories in your build environment. 
To create them: 
[code] 
    mkdir -p ~/bin
    mkdir -p ~/android/system
    
[/code]
### Install the Repository
Enter the following to download the "repo" binary and make it executable: 
[code] 
    curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
    chmod a+x ~/bin/repo
    
[/code]
    [![Sticky-note-pin.png][15707]][15708] _Note:_ You may need to reboot for these changes to take effect.
It's time to choose your desired flavour, Ice Cream Sandwitch or Jelly Bean: 
#### For the Ice Cream Sandwich (4.0.4) Repository
Enter the following to initialize the repository: 
[code] 
    cd ~/android/system/
    repo init -u git://github.com/CyanogenMod/android.git -b ics
    wget http://turl.linux-sunxi.org/local_manifest.xml -O .repo/local_manifest.xml
    repo sync -j16
    
[/code]
#### For the JellyBean (4.1.2) Repository
Enter the following to initialize the repository: 
[code] 
    cd ~/android/system/
    repo init -u git://github.com/CyanogenMod/android.git -b jellybean
    wget http://turl.linux-sunxi.org/local_manifest_jb.xml -O .repo/local_manifest.xml
    repo sync -j16
    
[/code]
#### For the JellyBean (4.2.2) Repository
Enter the following to initialize the repository: 
[code] 
    cd ~/android/system/
    repo init -u git://github.com/CyanogenMod/android.git -b cm-10.1
    wget http://turl.linux-sunxi.org/local_manifest_jb.xml -O .repo/local_manifest.xml
    repo sync -j16
    
[/code]
#### For the JellyBean (4.3) Repository
Enter the following to initialize the repository: 
[code] 
    cd ~/android/system/
    repo init -u git://github.com/CyanogenMod/android.git -b cm-10.2
    wget http://turl.linux-sunxi.org/local_manifest_jb.xml -O .repo/local_manifest.xml
    repo sync -j16
    
[/code]
## Creating a basic new device tree
There is an example basic tree to support new Allwinner devices. It contains a convenience script to change most of the basic stuff: 
[code] 
    cd ~/android/system/device/allwinner/
    git clone https://github.com/allwinner-dev-team/android_device_allwinner_example.git «yourdevice»
    cd «yourdevice»
    ./initialize.sh «yourdevice» «yourdevicepretty» «yourvendorpretty»
    
[/code]
with _«yourdevice»_ being a single word, lowercase identifier (e.g. zatab), _«yourdevicepretty»_ being a mixed case, user-friendly name (e.g. ZaTab), and _«yourvendorpretty»_ being the user-friendly name of your vendor (e.g. ZaReason). 
Once the naming is all set up, you might want to: 
  * Adjust CWM recovery key mappings (see recovery_keys.c)
  * Make a kernel defconfig for your device (generally _«yourdevice»_ _defconfig, it can be adjusted on _BoardConfig.mk_)
  * Adjust kernel modules to be loaded on boot, see init.sun4i.modules.rc
  * Adjust WiFi configuration, see _BoardConfig.mk_ in `device/allwinner/common/` for the configuration variables, and adjust them on your own _BoardConfig.mk_
  * Adjust proprietary files list, see `proprietary-files.txt`

## Copy proprietary files
To copy the proprietary files, connect the device to the computer and ensure that ADB is working properly. 
[code] 
    cd ~/android/system/device/allwinner/«yourdevice»
    ./extract-files.sh
    
[/code]
The proprietary files listed in the template include the Mali GPU libraries (`libMali.so`, etc.). However, these need to match the API version of the `mali.ko` module in your kernel. Since you're going to be building your own up-to-date kernel from the linux-sunxi source, you'll need to obtain the right versions of the Mali libraries from the [sunxi-mali repository][15710]. 
(If your libraries don't match the kernel, then Android's graphics system won't start up; `adb logcat` will show something like `eglInitialize(0x1) failed (EGL_BAD_ALLOC)`.) 
## Building CyanogenMod
### Fetch Prebuilts
    [![Sticky-note-pin.png][15707]][15708] _Note:_ This only needs to be done when an update to the prebuilts is released. If you are-up-to date, you may skip to the next step.
Download the prebuilts which are needed by the build: 
[code] 
    ~/android/system/vendor/cm/get-prebuilts
[/code]
### Configure Build & Compile
To build using your new device tree, issue 
[code] 
    . build/envsetup.sh && brunch ''«yourdevice»''
[/code]
## Install
  1. Copy your .zip file from `~/android/system/out/target/product/_«yourdevice»_ /cm-_XXXXX_.zip` to the root of the SD card. 
    **optional:** Download [Google Apps][15711] for your android version and place it on the root of the SD card.
  2. Flash both of these .zip files from recovery.
