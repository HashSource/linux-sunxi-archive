# USB Gadget/Serial
< [USB Gadget][57288]
 
## Contents
  * [1 USB serial gadget][57291]
    * [1.1 Kernel support][57292]
    * [1.2 Preparing the gadget device][57293]
    * [1.3 See also][57294]

# USB serial gadget
This gadget allows your devices act as a serial port device. The gadget serial driver talks over USB to either a CDC ACM driver or a generic USB serial driver running on a host PC. This guide demonstrates a way to use the gadget driver as a poor man's serial port debugging tool. One downside of this approach is that the driver does not activate immediately when booting the kernel. The early boot messages (bootloader, kernel) will not be printed via this serial device, but the kernel messages can be accessed e.g. via 'dmesg' in case the system is able to boot to the command prompt. 
## Kernel support
Currently, the (arm 32-bit) `sunxi_defconfig` does not select the g_serial module or its configfs equivalent, however the arm64 defconfig and arm(32)'s multi_v7_defconfig activate the configfs functionality. 
Here we assume the user wants to compile the support in the kernel, not as a module: 
[code] 
    Device Drivers
    	USB support
    		<*>   Inventra Highspeed Dual Role Controller (TI, ADI, AW, ...)
    			MUSB Mode Selection (Dual Role mode)
    			*** Platform Glue Layer ***
    			<*>     Allwinner (sunxi)
    		<*>   USB Gadget Support
    			[*]   Serial gadget console support
                            <*>   USB Gadget functions configurable through configfs
                            [*]     Generic serial bulk in/out
                            [*]     Abstract Control Model (CDC ACM)
    			      USB Gadget precomposed configurations --->
                                    <*> (Serial Gadget (with CDC ACM and CDC OBEX support))
    
[/code]
Make sure you use the dual role mode for MUSB unless the device tree configuration has been updated accordingly. Otherwise the system might fail to set up the device, complaining about an invalid or missing 'dr_mode' property. 
You can now continue following [manual build howto][57295] to continue kernel compilation and installation. 
## Preparing the gadget device
The serial device shows up as /dev/ttyGS0 on the gadget device. You can redirect kernel messages to this device by changing the kernel command line: 
[code] 
    setenv bootargs "console=ttyS0,115200 console=ttyGS0,115200 init=/usr/lib/systemd/systemd"
    
[/code]
In case the host machine runs Linux, the serial device might show up as /dev/ttyACM0 or something similar. You can use minicom to communicate with the gadget device: 
[code] 
    minicom -D /dev/ttyACM0
    
[/code]
## See also
Some experiments with USB serial gadget here <https://forum.armbian.com/index.php/topic/1735-tutorial-use-armbian-to-set-up-rpi-zero-for-g-serial-connection/>
