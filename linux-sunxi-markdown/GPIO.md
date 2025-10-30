# GPIO
**General Purpose Input/Output** (**GPIO**) is a generic pin on a integrated circuit chip whose behavior (including whether it is an input or output pin) can be controlled / programmed by the user at run time. 
## Contents
  * [1 Overview][21612]
  * [2 Accessing the GPIO pins through sysfs with mainline kernel][21613]
  * [3 Accessing the GPIO pins through character device with mainline kernel][21614]
  * [4 Accessing the GPIO pins through sysfs on sunxi-3.4][21615]
    * [4.1 Example: Controlling GPIO on Olimex's A13-OLinuXino (sunxi-3.4)][21616]
      * [4.1.1 What do you need:][21617]
      * [4.1.2 The Process][21618]
      * [4.1.3 C/C++ program][21619]
      * [4.1.4 Other stuff][21620]
  * [5 See also][21621]
  * [6 References][21622]
  * [7 External Links][21623]

# Overview
GPIO pins have no special purpose defined, and usually go unused by default. The idea is that sometimes the system integrator building a full system that uses the chip might find it useful to have a handful of additional digital control lines, and having these available from the chip can save the hassle of having to arrange additional circuitry to provide them. 
A GPIO port is a group of GPIO pins (typically 8 GPIO pins) arranged in a group, and treated as a single port. 
# Accessing the GPIO pins through sysfs with mainline kernel
The GPIO pins can be accessed from user space using sysfs. To enabled this you need the following kernel option enabled: CONFIG_GPIO_SYSFS 
[code] 
    Device Drivers  ---> GPIO Support  ---> /sys/class/gpio/... (sysfs interface)
    
[/code]
To access a GPIO pin you first need to _export_ it with 
[code] 
    echo XX > /sys/class/gpio/export
    
[/code]
with _XX_ being the number of the desired pin. To obtain the correct number you have to calculate it from the pin name (like PH18)[[1]][21624]: 
[code] 
    (position of letter in alphabet - 1) * 32 + pin number
    
[/code]
E.g for PH18 this would be ( 8 - 1) * 32 + 18 = 224 + 18 = 242 (since 'h' is the 8th letter). 
Alternatively, you can read the mapping from debugfs with 
[code] 
    cat /sys/kernel/debug/pinctrl/*/pinmux-pins
    
[/code]
After you have successfully exported the pin you can access it through **/sys/class/gpio/gpio*NUMBER*** (in case of PH18 it's _/sys/class/gpio/gpio242_). 
With /sys/class/gpio/gpio*NUMBER*/direction you must set the pin to **out** or **in** using 
[code] 
    echo "out" > /sys/class/gpio/gpio*NUMBER*/direction
    
[/code]
and only then you can read/write the value with **/sys/class/gpio/gpio*NUMBER*/value**. 
When you are done unexport the pin with 
[code] 
    echo XX > /sys/class/gpio/unexport
    
[/code]
# Accessing the GPIO pins through character device with mainline kernel
The sysfs GPIO interface is now deprecated in favor of character devices /dev/gpiochipX 
Verify that your system supports it with 
[code] 
    ls /dev/gpiochip*
    
[/code]
The easiest way to access the pins is with libgpiod and the set of tools it includes. <https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/>
You can read a pin with 
[code] 
    sudo gpioget gpiochip0 XX
    
[/code]
where XX is the pin number, calculated the same way as in the sysfs method (see section above). 
Set a pin value with 
[code] 
    sudo gpioset gpiochip0 XX=value
    
[/code]
where value is 0 or 1. Note the value will return to default after gpioset exits. Consult _gpioset --help_ for further options. 
Monitor the state of a pin with 
[code] 
    sudo gpiomon gpiochip0 XX
    
[/code]
You can use gpioinfo to see how the pins are configured, but 
[code] 
     cat /sys/kernel/debug/pinctrl/*/pinmux-pins 
    
[/code]
give you also the pin mapping (see section above). 
# Accessing the GPIO pins through sysfs on sunxi-3.4
This is subject to changing without notice :( Anyway I found this to hold true on 3.4.103: 
First you need to make sure that script.bin has some pins designated for gpio or when you load the appropriate module it will complain that no gpio pins are configured in script.bin. 
[code] 
     [gpio_para]
     gpio_used= 1
     gpio_num=12
     gpio_pin_1= port:PE00
     gpio_pin_2= port:PE01
     gpio_pin_3= port:PE02
     gpio_pin_4= port:PE03
     gpio_pin_5= port:PE04
     gpio_pin_6= port:PE05
     gpio_pin_7= port:PE06
     gpio_pin_8= port:PE07
     gpio_pin_9= port:PE08
     gpio_pin_10= port:PE09
     gpio_pin_11= port:PE10
     gpio_pin_12= port:PE11
    
[/code]
Reading the FEX tutorial in the section concerning the [Port Definitions][21625] would allow you to set pull up/down on the input ports. 
Next you need to load the appropriate module: 
[code] 
      modprobe gpio-sunxi
    
[/code]
Now export the pins 
[code] 
     for A in 1 2 3 4 5 6 7 8 9 10 11 12; do echo "$A" > /sys/class/gpio/export ; done
    
[/code]
This should make some links appear in sys/class/gpio/: 
[code] 
     root@headless2:/sys/class/gpio# ls -l
     total 0
     --w------- 1 root root 4096 Jan 10 00:12 export
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio10_pe9 -> ../../devices/platform/gpio-sunxi/gpio/gpio10_pe9/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio11_pe10 -> ../../devices/platform/gpio-sunxi/gpio/gpio11_pe10/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio12_pe11 -> ../../devices/platform/gpio-sunxi/gpio/gpio12_pe11/
     lrwxrwxrwx 1 root root    0 Jan 10 00:11 gpio1_pe0 -> ../../devices/platform/gpio-sunxi/gpio/gpio1_pe0/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio2_pe1 -> ../../devices/platform/gpio-sunxi/gpio/gpio2_pe1/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio3_pe2 -> ../../devices/platform/gpio-sunxi/gpio/gpio3_pe2/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio4_pe3 -> ../../devices/platform/gpio-sunxi/gpio/gpio4_pe3/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio5_pe4 -> ../../devices/platform/gpio-sunxi/gpio/gpio5_pe4/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio6_pe5 -> ../../devices/platform/gpio-sunxi/gpio/gpio6_pe5/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio7_pe6 -> ../../devices/platform/gpio-sunxi/gpio/gpio7_pe6/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio8_pe7 -> ../../devices/platform/gpio-sunxi/gpio/gpio8_pe7/
     lrwxrwxrwx 1 root root    0 Jan 10 00:12 gpio9_pe8 -> ../../devices/platform/gpio-sunxi/gpio/gpio9_pe8/
     lrwxrwxrwx 1 root root    0 Jan 10 00:10 gpiochip1 -> ../../devices/platform/gpio-sunxi/gpio/gpiochip1/
     --w------- 1 root root 4096 Jan 10 00:09 unexport
     root@headless2:/sys/class/gpio#
    
[/code]
Set the desired direction 
[code] 
     echo out > /sys/class/gpio/gpio12_pe11/direction
    
[/code]
You may now output something 
[code] 
     echo 1 > /sys/class/gpio/gpio12_pe11/value
    
[/code]
Reading the kernel documentation on sysfs gpio can be a good reading and will give you ideas on how to use the other features available. [Documentation/gpio/sysfs.txt][21626]
**You need root privileges to do this. If you don't want this, you may try the following:**
Add a group gpio and add the desired user to this group. Then add a file /etc/udev/rules.d/97-gpio.rules 
[code] 
    # /etc/udev/rules.d/97-gpio.rules
    SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c '\
        chown -R root:gpio /sys/class/gpio && chmod -R 0770 /sys/class/gpio &&\
        chown -R root:gpio /sys/devices/platform/soc && chmod -R 0770 /sys/devices/platform/soc'"
    
[/code]
or /etc/udev/rules.d/96-gpio.rules 
[code] 
    # /etc/udev/rules.d/96-gpio.rules
    SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c '\
        chown -R root:gpio /sys/class/gpio && chmod -R 0770 /sys/class/gpio &&\
        chown -R root:gpio /sys/devices/platform/sunxi-pinctrl/gpio && chmod -R 0770 /sys/devices/platform/sunxi-pinctrl/gpio'"
    
[/code]
Try which rule runs better. 
## Example: Controlling GPIO on Olimex's A13-OLinuXino (sunxi-3.4)
### What do you need:
  * [Kernel][21627] with `CONFIG_GPIO_SUNXI=y` If you set the option to m you should take care of loading the module. There was previously SUN4I_GPIO_UGLY option which is now deprecated.
  * `bin2fex` and `fex2bin` tools from [sunxi-tools][21628].

### The Process
  1. Open a console and connect to your A13.
  2. Make a directory in /media: mkdir /media/nanda
  3. Mount the nanda there: mount /dev/nanda /media/nanda
  4. Copy the file /media/nanda/script.bin to your PC. This file configures the A13.
  5. Now we need to make it a text file so we use the bin2fex. On a linux machine go into the directory where you compiled the sunxi-tools and from there type this: ./bin2fex /path/to/script.bin > script.fex This will create a text file named script.fex in your current directory.
  6. Now we need to edit it with a text editor and define the pins that are going to be used for GPIO. Look for a section named "[gpio_para]" if there is no such section (probably there will not be) go to the bottom of the file and add it like this:
[code] [gpio_para]
    gpio_used = 1
    gpio_num = 1
    gpio_pin_1 = port:PE11<1>
    
[/code]
gpio_used
    Do you want to use any GPIO at all? 1=yes 0=no
gpio_num
    The number of total gpio ports you want / pins you are using?
gpio_pin_$Num = PXN<Z>
    Where $Num is the GPIO pin number. starting from 1.
    PXN is the name of the pin you want to use
    Z is pin a output or a input? 0 for **in** put or 1 for **out** put.
In this example I used pin PE11 which is pin number 12 on the GPIO-2. The PXN names can be found here: [http://linux-sunxi.org/A13-OLinuXino#Expansion_ports][21629]. TO CHECK: when I used PE11 this pin is part of the [csi0_para] so I went to [csi0_para] and made csi_used = 0 Not sure if this is needed, but I think it is. 
  7. Now we need to make the modified fex file back to bin format so again from the directory where you compiled the sunxi-tools: ./fex2bin script.fex > script.bin
  8. Now put back the script.bin on the board and overwrite the old script.bin in /media/nanda
  9. Unmount the /media/nanda: umount /media/nanda
  10. Reboot the A13
  11. Log back in and now if you did everything correct in /sys/devices/virtual/misc/sun4i-gpio/pin you will see "pe11"
  12. If you solder a LED and a resistor to the right pin and ground (for example pin 2) <http://linux-sunxi.org/images/e/e7/A13-olinuxino-brd.png> and type: "echo 1 > /sys/devices/virtual/misc/sun4i-gpio/pin/pe11" the LED will light and "echo 0 > /sys/devices/virtual/misc/sun4i-gpio/pin/pe11" will turn it off.

### C/C++ program
Lib gpio_lib.h  
compiler eclipse c/c++  
steps:  
1)  

[code] 
           #define PNXX   SUNXI_GPN(XX)
    
[/code]
2)  

[code] 
           if(SETUP_OK!=sunxi_gpio_init()){
           printf("Failed to initialize GPIO\n");
           return -1;
       }
    
[/code]
3)  

[code] 
           if(SETUP_OK!=sunxi_gpio_set_cfgpin(PNXX,DIRECTION)){
           printf("Failed to config GPIO pin\n");
           return -1;
       }
    
[/code]
PNXX: ex.PD01  
DIRECTION: OUTPUT,INPUT  
4)  

[code] 
            if(sunxi_gpio_output(PNXX,LEVEL)){
            printf("Failed to set GPIO pin value\n");
            return -1;
           }
    
[/code]
LEVEL: HIGH,LOW  

5)  

[code] 
            sunxi_gpio_cleanup();
    
[/code]
### Other stuff
Olimex wrote another article on the subject at <http://olimex.wordpress.com/2012/10/23/a13-olinuxino-playing-with-gpios/>
# See also
  * [JTAG][21630]
  * [MicroSD Breakout][21631]
  * [A10/PIO][21632]
  * [A13/PIO][21633]
  * [A20/PIO][21634]
  * [H3/PIO][21635]

# References
  1. [↑][21636] [https://github.com/torvalds/linux/blob/master/drivers/pinctrl/sunxi/pinctrl-sunxi.h#L19][21637]

# External Links
  * [ALSA Development List][21638]
  * [Linux Kernel Doc on GPIO][21639]
  * [LinuxTV GPIO Pins Info][21640]
  * [GPIO Tutorial - بیر رباتیک][21641]
  * [Access GPIO from Linux user space][21642]
