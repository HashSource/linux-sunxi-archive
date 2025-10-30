# Cubieboard/Webcam
< [Cubieboard][14555]
 
## Contents
  * [1 Cubieboard A10 - Surveillance Camera Setup][14558]
    * [1.1 Requirements][14559]
    * [1.2 Step 1 - Main objective][14560]
    * [1.3 Step 2 - Main Objective][14561]
      * [1.3.1 setup mjpg-streamer][14562]
      * [1.3.2 create the init script][14563]
      * [1.3.3 setup motion][14564]
      * [1.3.4 setup Wifi][14565]
      * [1.3.5 final step: reboot Cubieboard][14566]
      * [1.3.6 brightness, contrast...][14567]
    * [1.4 Acknowledgements][14568]

# Cubieboard A10 - Surveillance Camera Setup
## Requirements
  * cubieboard A10
  * USB webcam (MJPG support recommended)
  * USB wifi dongle (Realtek RTL8188CUS)
  * (optional) USB HUB

## Step 1 - Main objective
Add UVC video support to the SD card image running on the cubieboard. 
If you already have a booting linux system on the Cubieboard with the uvcvideo module loaded after boot, skip the following main step. 
A new kernel image and modules will be cross-compiled on a cross compile host and then copied to the SD card partitions. The cubieboard will boot and lsmod will confirm the loaded uvcvideo kernel module - that is what this step is all about. 
Ubuntu Linaro rootfs is being used for this tutorial. 
**The following steps are highly recommended:**
  * **<http://linux-sunxi.org/FirstSteps>**
    * go with the **easy option: sunxi-bsp** (**kernel 3.0.76** checked out)
    * move on to "Building the Kernel" and skip git checkout the kernel
    * run **make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- sun4i_defconfig**
    * run **make ARCH=arm menuconfig**
    * activate some specific kernel options

` Device Drivers `
`
[code]
    <*>Multimedia Support
     <*>Video For Linux
     [*]Video Capture Adapters
      [*]V4L USB Devices
       <M>USB Video Class (UVC)
       [*]UVC input events device support
    
[/code]
```
``
  *     * run **make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j5 uImage modules**
    * run **make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=output modules_install**
    * copy the **uImage** file (arch/arm/boot/uImage) to the SD card BOOT partition
    * copy the **modules** (output/lib/modules/*) to the SD card ROOT partition (under /lib/modules)

unmount the SD Card partitions, plug the card into the cubieboard and fire it up. 
If all went well, lsmod will show the uvcvideo module loaded. 
[code] 
    linaro@linaro-alip:~$ lsusb 
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 002: ID 05e3:0608 Genesys Logic, Inc. USB-2.0 4-Port HUB
    Bus 004 Device 003: ID 046d:0824 Logitech, Inc. 
    Bus 004 Device 004: ID 0bda:8176 Realtek Semiconductor Corp. RTL8188CUS 802.11n WLAN
    
[/code]
[code] 
    linaro@linaro-alip:~$ lsmod 
    Module                  Size  Used by
    disp_ump                 969  0 
    cpufreq_stats           2700  0 
    mali_drm                2560  1 
    8192cu                587686  0 
    drm                   176664  2 mali_drm
    uvcvideo               59051  1 
    mali                  107255  0 
    ump                    46575  4 disp_ump,mali
    sw_ahci_platform        3621  0 
    
[/code]
## Step 2 - Main Objective
Add mjpg-streamer, motion and Wifi support. Email a picture attachment on motion detection. 
  * install the following packages:

`sudo apt-get update` `sudo apt-get install subversion motion sendemail`
using a Gmail account for mailing purposes: 
`sudo apt-get install libio-socket-ssl-perl libnet-ssleay-perl perl`
### setup mjpg-streamer
[code] 
    svn co https://svn.code.sf.net/p/mjpg-streamer/code/mjpg-streamer mjpg-streamer
    cd mjpg-streamer/mjpg-streamer && make
    ./mjpg_streamer -i "./input_uvc.so -f 30" -o "./output_http.so -w ./www"
    
[/code]
At this point you should have http://<cubie_ip>:8080 with mjpg-streamer working 
stop mjpg_streamer 
`sudo make install`
### create the init script
[code] 
    #!/bin/bash
    # /etc/init.d/mjpg_streamer
    ### BEGIN INIT INFO
    # Provides:          mjpg_streamer
    # Required-Start:    $network
    # Required-Stop:     $network
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: mjpg_streamer for webcam
    # Description:       Streams /dev/video0 to http://IP/?action=stream
    ### END INIT INFO
    
    f_message(){
            echo "[+] $1"
            #echo "space here"
    }
    
    # Carry out specific functions when asked to by the system
    case "$1" in
            start)
                    f_message "Starting mjpg_streamer"
                    /usr/local/bin/mjpg_streamer -b -i "/usr/local/lib/input_uvc.so -d /dev/video0 -f 30" -o "/usr/local/lib/output_http.so -w /usr/local/www"
                    sleep 2
                    f_message "mjpg_streamer started"
                    ;;
            stop)
                    f_message "Stopping mjpg_streamer."
                    pid=`ps aux | grep [m]jpg_streamer|awk '{print $2}'`
                    if [[ $pid != "" ]]; then
                            kill -9 $pid
                    fi
                    f_message "mjpg_streamer stopped"
                    ;;
            restart)
                    f_message "Restarting mjpg_streamer"
                    pid=`ps aux | grep [m]jpg_streamer|awk '{print $2}'`
    		if [[ $pid != "" ]]; then
    			kill -9 $pid
    		fi
                    /usr/local/bin/mjpg_streamer -b -i "/usr/local/lib/input_uvc.so -d /dev/video0 -f 30" -o "/usr/local/lib/output_http.so -w /usr/local/www"
                    sleep 2
                    f_message "Restarted mjpg_streamer"
                    ;;
            status)
                    pid=`ps aux | grep [m]jpg_streamer|awk '{print $2}'`
                    if [ -n "$pid" ];
                    then
                            f_message "mjpg_streamer is running with pid ${pid}"
                            f_message "mjpg_streamer was started with the following command line"
                            cat /proc/${pid}/cmdline ; echo ""
                    else
                            f_message "Could not find mjpg_streamer running"
                    fi
                    ;;
            *)
                    f_message "Usage: $0 {start|stop|status|restart}"
                    exit 1
                    ;;
    esac
    exit 0
    
[/code]
add the init script to boot: 
`#update-rc.d mjpg-streamer defaults`
### setup motion
`sudo mkdir /motion && sudo chmod a+rwx /motion` `sudo apt-get install motion`
**/etc/motion/motion.conf**
[code] 
    input 8
    netcam_url http://localhost:8080/?action=stream
    target_dir /motion
    on_picture_save /usr/local/bin/cubieMotionMail %f
    
[/code]
**/usr/local/bin/cubieMotionMail**
[code] 
    #!/bin/bash
    
    curdate=`date +"%Y-%m-%d %H:%M:%S"`
    attachedPic=$1
    
    sendEmail -f <from_addr>@gmail.com -t <to_addr>@gmail.com -u "Cubie Motion" -m "Motion detected - "$curdate -a $attachedPic -s smtp.gmail.com -o tls=yes -xu <from_addr>@gmail.com -xp <password>
    
    #clean up the tmp snapshot dir
    rm -rf /motion/*
    
[/code]
**/etc/default/motion**
[code] 
    start_motion_daemon=yes
    
[/code]
`sudo service motion restart`
Test the setup by making some motion happen in from of the camera. An email with date and attached photo should be delivered to the configured email address. 
### setup Wifi
`wpa_passphrase <SSID> <password>`
[code] 
    linaro@linaro-alip:~$ wpa_passphrase wifiAP linaroWifi
    network={
    	ssid="wifiAP"
    	#psk="linaroWifi"
    	psk=0b42d2fe2335739a087ef051c07be1c724be49769ff2f724289299ce194949d0
    }
    linaro@linaro-alip:~$ 
    
[/code]
use the output to configure **/etc/network/interfaces**
[code] 
    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet dhcp
    wpa-ssid "wifiAP"
    wpa-psk 0b42d2fe2335739a087ef051c07be1c724be49769ff2f724289299ce194949d0
    
[/code]
### final step: reboot Cubieboard
  * Wifi, mjpg-streamer and motion expected to start at boot
  * emails expected to arrive, with attached photo, over email
  * test the setup by creating some motion in front of the camera - and you're done!

### brightness, contrast...
[code] 
    sudo apt-get install v4l-utils
    v4l2-ctl --list-ctrls
    
[/code]
And then as an example: 
[code] 
    v4l2-ctl --set-ctrl brightness=10
    
[/code]
... and on the web viewer, the settings should kick in realtime! 
## Acknowledgements
This working guide on the Cubieboard came as a result of combining several independent guides scattered over the web and for other platforms. Gathering all the information, adjusting and making it all work resulted in this guide. Some of the scripting has been rewritten/adjusted after testing on the Cubieboard, however original credit should be given to: 
  * <https://www.olimex.com/wiki/UVC_support>
  * <http://www.marcomc.com/2012/09/how-to-configure-wireless-lan-on-raspberrypi-with-raspbian-kernel-3-2-27-and-solwise-rtl8188cus-wifi-dongle/>
  * <http://www.debianadmin.com/how-to-sendemail-from-the-command-line-using-a-gmail-account-and-others.html>
  * [http://www.raspberrypi.org/phpBB3/viewtopic.php?t=31212&p=279214][14569]
