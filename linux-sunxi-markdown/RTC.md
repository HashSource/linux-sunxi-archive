# RTC
Please note that this guide is written for AllWinner H3 although the concepts could be applied to others. There are many H3 boards and some of them have on-board RTC clock while others dont. 
## Contents
  * [1 On-Board RTC][46879]
  * [2 No on-board RTC][46880]
  * [3 Trouble Shooting Commands][46881]
  * [4 Troubleshooting][46882]
    * [4.1 The corresponding I2C address (e.g. 0x68) is not in use, and no /dev/rtc1 is created][46883]
  * [5 Tips and Tricks][46884]
    * [5.1 Enabling the external RTC module permanently in device tree][46885]
    * [5.2 Automatically set system time on startup from /dev/rtc1 instead of the default /dev/rtc0][46886]
    * [5.3 Setting /dev/rtc1 as the default RTC device used to sync NTP adjustment][46887]
  * [6 See Also][46888]

# On-Board RTC
For Boards that have on-board RTC, the kernel will enumerate I2C device to /dev/rtc1 because /dev/rtc0 is occupied by built-in Allwinner's RTC (sunxi-rtc). That means you have to modify a symlink "/dev/rtc" to point to /dev/rtc1 instead of /dev/rtc0 like this: sudo ln -f -s /dev/rtc1 /dev/rtc 
After that standard hwclock will work fine however its recommended to use an init-script to make sure time is automatically adjusted. Here is an example (/etc/init.d/rtc_ds1307) 
[code] 
    #! /bin/sh
    ### BEGIN INIT INFO
    # Provides:          rtc_ds1307
    # Required-Start:    $remote_fs $syslog
    # Required-Stop:     $remote_fs $syslog
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: DS1307 real-time clock usage script
    # Description:       This file should be used to construct scripts to be
    #                    placed in /etc/init.d.
    ### END INIT INFO
    # PATH should only include /usr/* if it runs after the mountnfs.sh script
    PATH=/sbin:/usr/sbin:/bin:/usr/bin
    DESC="ds1307_rtc maintenance service"
    do_start()
    {
           echo "Selecting correct  RTC instance "
           echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-0/new_device
           sudo ln -f -s /dev/rtc1 /dev/rtc
           echo "Syncing system time to RTC"
           sudo hwclock -s
    }
    do_stop()
    {
           echo "Syncing RTC to system time"
           sudo hwclock -w
    }
    case "$1" in
     start)
           do_start
           ;;
     stop)
           do_stop
           ;;
     status)
           echo "RTC time:"
           hwclock -r
           echo "System time:"
           date
           ;;
     restart|force-reload)
           do_stop
           ;;
     *)
           echo "Usage: rtc_ds1307 {start|stop|status|restart}" >&2
           exit 3
           ;;
    esac
    
[/code]
# No on-board RTC
Nanopi M1 is one board where it doesnt have on-board RTC clock. I have used DS1307 and DS3231 IC based RTC Clocks and both work. Make you include the I2C Kernel Modules in the kernel config namely under I2C RTC drivers CONFIG_RTC_DRV_DS1307=y and CONFIG_RTC_DRV_DS3232=y. Please understand DS1307 module supports both DS1307 and DS3231. Next after booting type the following line which will help add make the RTC module load at boot time as a new device. Second command help us to test the RTC module. 
[code] 
    echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-0/new_device
    hwclock -r
    
[/code]
Here is how its supposed to be connected = Nanopi m1 to RTC Clock 
  * **RTC Pin Spec**

    
     Board-Pin# | Name | RTC-Pin# | Name   
---|---|---|---  
1 | SYS_3.3V |  | VCC   
3 | I2C0_SDA |  | SDA   
5 | I2C0_SCL |  | SCL   
7 | GPIOG11 |  | DoNOTConnect   
9 | GND |  | GN   
**Please note in-case of on-board RTC, make you use I2C1_SDA, I2C1_SCL etc.**
To ensure that the device is created at boot and the time is set from the RTC, we edit /etc/rc.local : 
[code] 
     sudo vi /etc/rc.local
    
[/code]
and add the following lines before ‘exit 0’ (change /i2c-0/new_device to **i2c-1/new_device** if required): 
[code] 
     echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-0/new_device
     hwclock -s
    
[/code]
# Trouble Shooting Commands
[code] 
    ls -l /sys/bus/i2c/devices/i2c-*
    dmesg
    i2cdetect -y *
    
[/code]
some "other" notes: 
sun4i has an internal RTC sun5i does not have an internal RTC, rtc-sun5i.c is a chopped up rtc-pcf8563.c with some i2c stuff 
# Troubleshooting
## The corresponding I2C address (e.g. 0x68) is not in use, and no /dev/rtc1 is created
After echoing the RTC chip and its address to sysfs, it's expected that the address is occupied as shown by **i2cdetect** ("UU" symbol in the address), and a new rtc device is created in /dev, which can be read by **hwclock -f /dev/rtc1**. If not, the I2C bus (not I2C address) specified may not match the physically connected I2C bus of GPIO pins. 
[code] 
    # The expected output of "i2cdetect -y 1" when DS1307 is connected to /dev/i2c-1 and being in use
    
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:                         -- -- -- -- -- -- -- -- 
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- UU -- -- -- -- -- -- -- 
    70: -- -- -- -- -- -- -- -- 
    
[/code]
It's likely that the upstream device tree does not expose all of the available I2c buses. For example, **i2cdetect -l** may only show 2 I2C buses on Orange Pi PC with upsteam device tree (i2c-0 and i2c-1), which is already used by DesignWare HDMI and SY8106A respectively. But H3 supports 4 I2C buses (excluding HDMI), according to the section _TWI Controller Register List_ in H3 datasheet. 
Part of Allwinner H3 TWI (I2C) Controller Bus Base Address  Module Name | Base Address   
---|---  
R_TWI (for CPU voltage regulator) | 0x01F02400   
TWI0 (on GPIO) | 0x01C2AC00   
TWI1 (on GPIO) | 0x01C2B000   
TWI2 (usually populated on CSI) | 0x01C2B400   
As a result, the external I2C buses and addresses populated on GPIO may be mixed with internal buses in operating system, and you risk failing to announce new I2C device, encountering error messages like _probe with driver rtc-ds1307 failed with error -5_ shown by dmesg, or even corrupting internal firmware (e.g. EDID firmware) when reaching into the muddy water. So in this case, it's necessary to expose more (empty) I2C buses by modifying the device tree. 
Some distros like Ambian already provide device tree overlays for exposing more I2C buses. We can start by referring to the Armbian sunxi-DT-overlays (<https://github.com/armbian/sunxi-DT-overlays>). With reference to the files sun8i-h3-i2c0.dts, sun8i-h3-i2c1.dts, etc., we can add the following sections in the board-specific dts source files as follows (taking Orange Pi PC as an example): 
[code] 
    arch/arm/boot/dts/allwinner/sun8i-h3-orangepi-pc.dts:
    
    / {
    ...
     aliases {
      ...
      /* The base address of I2C (TWI) can found in SoC datasheet */
      i2c0 = "/soc/i2c@01c2ac00";
      i2c1 = "/soc/i2c@01c2b000";
      i2c2 = "/soc/i2c@01c2b400";
     };
    };
    ...
    &i2c0 {
     status = "okay";
    };
    &i2c1 {
     status = "okay";
    };
    &i2c2 {
     status = "okay";
    };
    
[/code]
Rebuild, replace and reboot. There will be i2c-0...i2c-4 in /dev instead of the default i2c-0 and i2c-1. The exact mapping of I2C bus number to the physical ID label of GPIO pins should be double-checked by running dmesg. In my case, /dev/i2c-1 corresponds to TWI0. More hints can be shown by enabling CONFIG_I2C_DEBUG_* when building kernel. 
An example of I2C bus mapping  /dev/i2c-* | Hardware bus name | Alias in DT | Description   
---|---|---|---  
i2c-0 | HSCL & HSDA (for HDMI) |  | DesignWare HDMI   
i2c-1 | TWI0-SCK & TWI0-SDA (on GPIO) | &i2c0 | mv64xxx_i2c adapter   
i2c-2 | TWI1-SCK & TWI1-SDA (on GPIO) | &i2c1 | mv64xxx_i2c adapter   
i2c-3 | CSI-SCK & CSI-SDA (on CSI) | &i2c2 | mv64xxx_i2c adapter   
i2c-4 | R_TWI (for SY8106A) |  | mv64xxx_i2c adapter   
If everything goes well, assumed the DS1307 RTC chip is connected to I2C bus 1, **i2cdetect -y 1** will print "68" on the address 0x68, which is the I2C address of DS1307. After running **echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device**, the label on address 0x68 will change to "UU", indicating the address is in use. A new RTC device will also be created accordingly. 
# Tips and Tricks
## Enabling the external RTC module permanently in device tree
Instead of adding the "echo xxx > new_device" line to start-up scripts, the RTC chip can also be enabled in device tree, automating the system time-setting process on boot. An example section in device tree file is shown as follows: 
[code] 
    arch/arm/boot/dts/allwinner/sun8i-h3-orangepi-pc.dts:
    
    ...
    &i2c0 {
     /* The "status" line must be parsed before the child nodes "rtc@68" */
     status = "okay";
     #address-cells = <1>;
     #size-cells = <0>;
     rtc@68 {
      compatible = "dallas,ds1307";
      reg = <0x68>;
     };
    };
    ...
    
[/code]
It's advised to check the kernel documentation for required device tree declaration of the chip in e.g. Documentation/devicetree/bindings/rtc/rtc-ds1307.yaml. The examples in Armbian device tree overlays repository may also be a good reference. 
By the way, building the corresponding RTC driver as a built-in driver instead of a kernel module may be necessary for early initialization. 
## Automatically set system time on startup from /dev/rtc1 instead of the default /dev/rtc0
As is discussed above, /dev/rtc0 is usually occupied by SoC's internal RTC which is not battery-backed. Instead of adding **hwclock -s -f /dev/rtc1** to start-up scripts (the -f parameter may be crucial as hwclock defaults to /dev/rtc0), the default rtc device used to set system time can also be specified by kernel, further automating the system time-setting process on boot. The corresponding kernel configs are shown as follows: 
[code] 
    CONFIG_RTC_HCTOSYS=y
    CONFIG_RTC_HCTOSYS_DEVICE="rtc1"
    
[/code]
## Setting /dev/rtc1 as the default RTC device used to sync NTP adjustment
Moreover, the default rtc device used to sync NTP adjustment can also be set by kernel. It seems that **systemd-timesyncd** honors the setting of CONFIG_RTC_SYSTOHC_DEVICE, even though the "RTC time" output of **timedatectl** still defaults to /dev/rtc which is a symbolic link as discussed above. 
[code] 
    CONFIG_RTC_SYSTOHC=y
    CONFIG_RTC_SYSTOHC_DEVICE="rtc1"
    
[/code]
# See Also
  * [I2C on the Orange Pi PC 2 with Armbian Bionic][46889]
  * [GitHub - armbian/sunxi-DT-overlays: Device Tree overlays for sunxi devices][46890]
