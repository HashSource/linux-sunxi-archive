# 1-Wire
## Contents
  * [1 One Wire][3]
    * [1.1 1-Wire support for Mainline kernel][4]
      * [1.1.1 Device Tree][5]
    * [1.2 Linux kernel 3.4][6]
    * [1.3 Linux kernel 4.14][7]
    * [1.4 Read Data Sensor][8]
      * [1.4.1 BASH][9]
      * [1.4.2 Python][10]

## One Wire
**1-Wire** is a device communications bus system designed by Dallas Semiconductor that provides low-speed data, signaling, and power over a single signal. 1-Wire is similar in concept to [I²C][11], but with lower data rates and longer range. It is typically used to communicate with small inexpensive devices such as digital thermometers and weather instruments. A network of 1-Wire devices with an associated master device is called a _MicroLan_. 
### 1-Wire support for Mainline kernel
To communicate with 1-wire devices it is recommended to use **w1-gpio** driver as most of the Allwinner SoCs lack hardware controller (only present on A31 and A80). 
#### Device Tree
Create an overlay for your devicetree (assuming 1-wire device is connected to PE12 pin): 
[code] 
    /dts-v1/;
    /plugin/;
    
    &{/} {
            onewire {
            compatible = "w1-gpio";
            gpios = <&pio 4 12 16>;
            /* 4: "E" of PE12;
            12: "12" of PE12;
            16: GPIO_PULL_UP as defined in dt-bindings/gpio/gpio.h */
            status = "okay";
            };
    };
    
[/code]
Save this snippet with a name like sun50i-a64-w1-gpio-PE12.dts and compile it with: 
[code] 
    dtc -I dts -O dtb sun50i-a64-w1-gpio-PE12.dts -o sun50i-a64-w1-gpio-PE12.dtbo
    
[/code]
Specify the .dtbo file path in the fdtoverlays list inside the /boot/uEnv.txt file: 
[code] 
    cat /boot/uEnv.txt
    fdtoverlays=/root/sun50i-a64-w1-gpio-PE12.dtbo
    
[/code]
Reboot and check whether it's enabled: 
[code] 
    cat /sys/kernel/debug/pinctrl/1c20800.pinctrl/pinmux-pins |grep PE12
    
[/code]
The pin is properly configured if you have an output like: 
[code] 
    pin 140 (PE12): GPIO 1c20800.pinctrl:140
    
[/code]
### Linux kernel 3.4
Edit the script.fex file and set the gpio pin for 1-wire bus 
[code] 
    
    [gpio_para]
    gpio_used = 1
    gpio_num = 67
    gpio_pin_1 = port:PG03<1><default><default><1>
    ....
    gpio_pin_66 = port:PB10<1><default><default><1>
    
    [w1_para]
    gpio = 66
    
[/code]
Connect the data pin of devices to gpio pin PB10 and in sys folder you have 
[code] 
    /sys/bus/w1/devices/
    28-000004bfae30
    28-000004c022c5
    
[/code]
what are connect 2 DS18B20 devices 
[code] 
    cat /sys/bus/w1/devices/28-000004bfae30/w1_slave
    45 01 4b 46 7f ff 0b 10 84 : crc=84 YES
    45 01 4b 46 7f ff 0b 10 84 t=20312
    
[/code]
the temp is 20.312 °C 
### Linux kernel 4.14
You don't have to edit the fex-file, but the /boot/armbianEnv.txt and add the lines: 
[code] 
    overlays=w1-gpio
    param_w1_pin=PB10             # desired pin
    param_w1_pin_int_pullup=1     # internal pullup-resistor: 1=on, 0=off
    
[/code]
Connect the data pin of devices to gpio pin PB10 and proceed like Kernel 3.4 with 
[code] 
    /sys/bus/w1/devices/
    28-000004bfae30
    28-000004c022c5
    
[/code]
and 
[code] 
    cat /sys/bus/w1/devices/28-000004bfae30/w1_slave
    45 01 4b 46 7f ff 0b 10 84 : crc=84 YES
    45 01 4b 46 7f ff 0b 10 84 t=20312
    
[/code]
### Read Data Sensor
#### BASH
simple bash script for read 1-wire temp sensor 
[code] 
    
    #!/bin/bash
    
    file="/sys/bus/w1/devices/28-000004bfae30/w1_slave"
    function find(){
     [[ "$1" =~ "$2" ]] && true || false
    }
    
    while :
    do
    	DATE=$(date +"%d-%m-%Y-%H:%M:%S")
    	#read device
    	CRC=false
    	while read curline; do
    		#check crc
    		if( find "$curline" "crc" && find "$curline" "YES" ) then
    			CRC=true
    			DEVICE=`echo $curline|cut -d':' -f 1`	
    		fi
    		if($CRC && find "$curline" "t=") then
    		TEMP=`echo $curline|cut -d'=' -f 2`
    		echo $DEVICE ";" $DATE ";" `echo "scale=3;$TEMP/1000"|bc -l` 
    		fi
    	done <$file
    sleep 10
    done
    
[/code]
#### Python
[code] 
    def get_thermometer_filepath(thermometer_id: str):
        import os
        thermometer_filepath = os.path.join("/sys/bus/w1/devices/", thermometer_id, "w1_slave")
        try:
            with open(thermometer_filepath, "r"):
                pass
        except FileNotFoundError as e:
            print("Thermometer sysfs file not found: " + str(e))
            thermometer_filepath = None
        return thermometer_filepath
    
    def get_temperature(thermometer_filepath: str):
        if thermometer_filepath:
            err = None
            try:
                with open(thermometer_filepath, "r") as w1handle:
                    lines = w1handle.readlines()
                    try:
                        crc = lines[0].strip().endswith("YES")
                        if crc:
                            return int(lines[1][29:].strip())/1000
                        else:
                            err = "Thermometer read CRC failed: " + thermometer_filepath
                    except IndexError as e:
                        err = "Thermometer sysfs file "+thermometer_filepath+" is empty (communication unsuccessful): " + str(e)
            except FileNotFoundError as e:
                err = "Thermometer sysfs file "+thermometer_filepath+" not found: " + str(e)
            print(err)
            return -99.99
        else:
            return -99.99
    
[/code]
Usage: 
[code] 
    temperature = get_temperature(get_thermometer_filepath("28-000010400ca7"))
    
[/code]
