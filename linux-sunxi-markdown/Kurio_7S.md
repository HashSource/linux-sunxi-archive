# Kurio 7S
Kurio 7S  
---  
[![IMG 20140824 164641.jpg][29684]][29685]  
Manufacturer |  [Kurio][29686]  
Dimensions |  width _mm_ x breadth _mm_ x height _mm_  
Release Date |  October 2013   
Website |  [Product page][29687]  
Specifications   
SoC |  [A20][29688] @ 912Mhz   
DRAM |  1GiB DDR3 @ 432MHz   
NAND |  8GB   
Power |  USB, 4000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" 10:6)   
Touchscreen |  5-finger capacitive ([FocalTech ft5x_ts][29689] WORK)   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal stereo speakers, internal microphone   
Network |  WiFi 802.11 b/g/n ([rtl8188eu ???][29690])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  1.2MP (1280x1024) front, 2MP (1920x1080) rear   
Other |  Accelerometer (TODO: [Manufacturer device][29691])   
This page needs to be properly filled according to the [New Device Howto][29692] and the [New Device Page guide][29693].
  * WARNING* : IMAGES ARE UNRELIABLE. lima-memtester goes to red in less than 5 minutes (even with powersave governor)

YOU MAY LOSE YOUR DATA or trash your SD card partition table (as it happened to me) :( A fixedSPL is at <https://docs.google.com/file/d/0Bzj6Jo7OvWk-eU9INEllb3JqQ0E/preview>
## Contents
  * [1 Identification][29694]
  * [2 Sunxi support][29695]
    * [2.1 Current status][29696]
    * [2.2 Images][29697]
    * [2.3 HW-Pack][29698]
    * [2.4 BSP][29699]
    * [2.5 Manual build][29700]
  * [3 Tips, Tricks, Caveats][29701]
    * [3.1 Touchscreen:][29702]
    * [3.2 Right mouse click evdev][29703]
    * [3.3 Battery:][29704]
    * [3.4 Code lcd off and touchscreen][29705]
    * [3.5 FEL mode][29706]
  * [4 Adding a serial port (**voids warranty**)][29707]
    * [4.1 Device disassembly][29708]
    * [4.2 Locating the UART][29709]
  * [5 Pictures][29710]
  * [6 Also known as][29711]
  * [7 See also][29712]
    * [7.1 Manufacturer images][29713]

# Identification
In android, under Settings->About Tablet, you will find: 
  * Model Number: Kurio7S
  * Build Number: C13000A120a.20131218.160640

# Sunxi support
## Current status
I'm working to Debian Xfce and Kali linux(images cubieboard 2):  
Kernel 3.4.102/3.4.103   
Work now:  
-Lcd  
-Touchscreen  
-Hdmi  
-USB (OTG, charging working)  
-Audio  
-Debug (UART)  
-Wifi  
-Power button  

Not work (yet) :  
-Camera (Front,Rear)  
-NAND (Debian wheezy)  
-Volume +/-  

The touchscreen is *not* working with the base driver, at least in my Kurio 7S(but works fine on Android4.2.2 and in the Cubian tutorial after /etc/modules) 
## Images
[Tutorial of pepcio03][29714]  
[Kernel][29715]
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "Kurio_7S" target.
  * The .fex file can be found in sunxi-boards as [kurio_7s.fex][29716]

Everything else is the same as the [manual build howto][29717]. 
# Tips, Tricks, Caveats
##### Touchscreen:
Edit linux-sunxi-sunxi-3.4/drivers/input/touchscreen/ft5x_ts.c 
Removed the "IRQF_TRIGGER_FALLING |" line (1765) compiled kernel and now works 
##### Right mouse click evdev
[code] 
           $sudo mkdir /etc/X11/xorg.conf.d
           $sudo touch /etc/X11/xorg.conf.d/evdev.conf
           $sudo vim /etc/X11/xorg.conf.d/evdev.conf
    
[/code]
[code] 
           Section "InputClass"
                   Identifier "Touchscreen"
                   MatchProduct "ft5x_ts"
                   Driver "evdev"
                   Option "EmulateThirdButton" "1"
                   Option "EmulateThirdButtonTimeout" "1000"
                   Option "EmulateThirdButtonMoveThreshold" "30"
           EndSection
    
[/code]
##### Battery:
Folder battery info cappacity,status, etc. 
[code] 
           /sys/class/power_supply/battery/ 
    
[/code]
  

##### Code lcd off and touchscreen
NUM_DEVICE check 
[code] 
           $xinput | grep ft5x_ts 
    
[/code]
Create power file and add keyboard shortcut to power button 
[code] 
            $sudo vim /usr/bin/power
    
            #!/bin/bash
            NUM_DEVICE=7
            ENABLED=`xinput --list-props $NUM_DEVICE | grep "Device Enabled" | awk '{print $4}'`
            if [ $ENABLED = 0 ]; then
                    xinput enable $NUM_DEVICE
                    xset dpms force on
            else
                    xinput disable $NUM_DEVICE
                    xset dpms force off
            fi
            exit 0 
    
[/code]
## FEL mode
The Vol- [ FEL mode][29718].  
The Vol+ triggers [ Recovery mode][29719]  

# Adding a serial port (**voids warranty**)
[![][29720]][29721]
[][29722]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][29723]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][29724].
## Locating the UART
Under the processor are Tx, Rx.  

Describe how to find the RX,TX,GND signals here, and mention the [UART howto][29723].
# Pictures
  * [![IMG 20140824 164641.jpg][29725]][29685]
  * [![Back kurio 7s.jpg][29726]][29727]
  * [![IMG 20140824 184805.jpg][29728]][29729]
  * [![Device buttons 2.jpg][29730]][29731]
  * [![Device board front.jpg][29732]][29733]
  * [![IMG 20141030 145317.jpg][29734]][29735]

# Also known as
  * La Tablette Tactile 7 pouces by Gulli.

# See also
[Group Google][29736]   
[Touch screen work][29737]  
[Tutorial of pepcio03][29714]  

## Manufacturer images
