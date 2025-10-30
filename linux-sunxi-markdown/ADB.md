# ADB
ADB is Android Debug Bridge, a protocol over USB (OTG) to provide many necessary system access services. 
A full explanation on how to use ADB is provided [at the android developer website][5107]. 
## Contents
  * [1 Common pitfalls][5108]
    * [1.1 No devices found][5109]
    * [1.2 Only root has access][5110]
  * [2 root access][5111]

# Common pitfalls
## No devices found
If you run _adb devices_ , and it shows no devices: 
[code] 
    List of devices attached 
    
    
[/code]
Then verify that your device is present on the usb bus, by running _lsusb_ : 
[code] 
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 002 Device 032: ID abcd:1234
[/code]
You then need to make sure that adb knows about this new vendor id: 
[code] 
    mkdir ~/.android/
    echo "0xabcd" > ~/.android/adb_usb.ini
[/code]
You need to restart adb for this to take effect: 
[code] 
    adb kill-server
[/code]
## Only root has access
You need to alter the permissions of your usb device through udev. 
Add a file _51-android.rules_ in _/etc/udev/rules.d/_ with the following content (with the ID matching what _lsusb_ says). 
[code] 
    SUBSYSTEM=="usb", ATTR{idVendor}=="abcd", MODE="0666", GROUP="plugdev"
[/code]
When you now update udev, you should be able to access the device as a user: 
[code] 
    udevadm trigger
[/code]
# root access
While most Allwinner devices ship with root access enabled via ADB, some don't. There are different ways of gaining root access on the device, but many of them are not straightforward or involve using proprietary software. Android can be tricked to quickly provide root access on ADB shell, using the lax permissions set on /data/local/tmp files at boot. 
[code] 
    adb shell
    $ rm -rf /data/local/tmp
    $ ln -s /data /data/local/tmp
    
[/code]
Reboot the device. 
[code] 
    adb shell
    $ echo "ro.kernel.qemu=1" > /data/local/tmp/local.prop
    
[/code]
Reboot the device: ADB shell should now be running as root!
