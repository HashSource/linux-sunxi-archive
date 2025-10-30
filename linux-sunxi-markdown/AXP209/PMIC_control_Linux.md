# AXP209/PMIC control Linux
< [AXP209][5531]
 
This page describes how to get information from PMIC [AXP209][5531]. 
TODO: how to change PMIC AXP209 behaviour. 
## Contents
  * [1 Get information][5534]
    * [1.1 From /sys/ directory][5535]
      * [1.1.1 Scripts][5536]
    * [1.2 From i2c][5537]
      * [1.2.1 Scripts][5538]
  * [2 See also][5539]

## Get information
### From /sys/ directory
Armbian examples for SBC Olimex A20-OLinuXino-LIME2 (Allwinner A20 + AXP209): 
It is possible to see information from current and voltage sensors (each multiplied by 1'000'000). Here, battery is charging: 
[code] 
     $ cat /sys/power/axp_pmu/ac/amperage
    1467500
     $ cat /sys/power/axp_pmu/ac/voltage
    4751500
     $ cat /sys/power/axp_pmu/battery/charge
    5718926
     $ cat /sys/power/axp_pmu/battery/charging
    1
    
[/code]
So you can calculate current AC power (A*V) by: 
[code] 
     $ echo "$(echo scale=3\; $(cat /sys/power/axp_pmu/ac/voltage) \* $(cat /sys/power/axp_pmu/ac/amperage)) / 10^12" | bc -l
    7.125
    
[/code]
Or, current power from battery: 
[code] 
     $ echo "$(echo scale=3\; $(cat /sys/power/axp_pmu/battery/voltage) \* $(cat /sys/power/axp_pmu/battery/amperage)) / 10^12" | bc -l
    2.641
    
[/code]
Mainline directory: 
[code] 
     $ ls -lAF /sys/power/axp_pmu/
    drwxr-xr-x 2 root root    0 Jun 27 15:34 ac/
    drwxr-xr-x 3 root root    0 Jun 27 15:34 axp20x-ac-power-supply/
    drwxr-xr-x 4 root root    0 Jun 27 15:34 axp20x-adc/
    drwxr-xr-x 4 root root    0 Jun 27 15:34 axp20x-battery-power-supply/
    drwxr-xr-x 5 root root    0 Jun 27 15:34 axp20x-gpio/
    drwxr-xr-x 5 root root    0 Jun 27 15:34 axp20x-pek/
    drwxr-xr-x 3 root root    0 Jun 27 15:34 axp20x-regulator/
    drwxr-xr-x 2 root root    0 Jun 27 15:34 battery/
    drwxr-xr-x 2 root root    0 Jun 27 15:34 charger/
    drwxr-xr-x 2 root root    0 Jun 27 15:34 control/
    lrwxrwxrwx 1 root root    0 Jun 27 15:34 driver -> ../../../../../../bus/i2c/drivers/axp20x-i2c/
    -r--r--r-- 1 root root 4096 Jun 27 15:34 modalias
    -r--r--r-- 1 root root 4096 Jun 27 15:34 name
    -rw-r--r-- 1 root root   16 Jun 27 16:22 ocv_curve
    lrwxrwxrwx 1 root root    0 Jun 27 16:22 of_node -> '../../../../../../firmware/devicetree/base/soc/i2c@1c2ac00/pmic@34'/
    drwxr-xr-x 2 root root    0 Jun 27 15:34 pmu/
    drwxr-xr-x 2 root root    0 Jun 27 15:34 power/
    drwxr-xr-x 9 root root    0 Jun 27 15:34 regulator/
    lrwxrwxrwx 1 root root    0 Jun 27 15:34 subsystem -> ../../../../../../bus/i2c/
    -rw-r--r-- 1 root root 4096 Jun 27 15:34 uevent
    drwxr-xr-x 2 root root    0 Jun 27 15:34 vbus/
    
     $ ls -lAF /sys/power/axp_pmu/battery/
    -r--r--r-- 1 root root 4096 Jun 27 16:22 amperage
    -r--r--r-- 1 root root 4096 Jun 27 15:35 capacity
    -r--r--r-- 1 root root 4096 Jun 27 16:22 charge
    -r--r--r-- 1 root root 4096 Jun 27 16:22 charging
    -r--r--r-- 1 root root 4096 Jun 27 15:35 connected
    -r--r--r-- 1 root root 4096 Jun 27 16:22 power
    -r--r--r-- 1 root root 4096 Jun 27 16:22 ts_voltage
    -r--r--r-- 1 root root 4096 Jun 27 16:22 voltage
    
     $ ls -lAF /sys/power/axp_pmu/ac/
    -r--r--r-- 1 root root 4096 Jun 27 16:26 amperage
    -r--r--r-- 1 root root 4096 Jun 27 15:35 connected
    -r--r--r-- 1 root root 4096 Jun 27 16:28 used
    -r--r--r-- 1 root root 4096 Jun 27 15:34 voltage
    
     $ ls -lAF /sys/power/axp_pmu/charger
    -r--r--r-- 1 root root 4096 Jun 27 16:34 amperage
    -r--r--r-- 1 root root 4096 Jun 27 16:34 cell_activation
    -r--r--r-- 1 root root 4096 Jun 27 15:35 charging
    -r--r--r-- 1 root root 4096 Jun 27 16:34 low_power
    
     $ ls -lAF /sys/power/axp_pmu/control
    -rw-r--r-- 1 root root 4096 Jun 27 16:34 battery_rdc
    -rw-r--r-- 1 root root 4096 Jun 27 16:34 charge_rtc_battery
    -rw-r--r-- 1 root root 4096 Jun 27 16:34 disable_fuel_gauge
    -rw-r--r-- 1 root root 4096 Jun 27 16:34 reset_charge_counter
    -rw-r--r-- 1 root root 4096 Jun 27 16:34 set_vbus_direct_mode
    
     $ ls -lAF /sys/power/axp_pmu/pmu
    -r--r--r-- 1 root root 4096 Jun 27 16:34 overheat
    -r--r--r-- 1 root root 4096 Jun 27 15:34 temp
    -r--r--r-- 1 root root 4096 Jun 27 16:34 voltage
    
[/code]
Legacy directory: 
[code] 
     $ ls -lAF /sys/class/power_supply/axp20x-battery/
    total 0
    -r--r--r-- 1 root root 4096 Jun 27 16:22 capacity
    -rw-r--r-- 1 root root 4096 Jun 27 16:22 constant_charge_current
    -rw-r--r-- 1 root root 4096 Jun 27 16:22 constant_charge_current_max
    -r--r--r-- 1 root root 4096 Jun 27 16:22 current_now
    lrwxrwxrwx 1 root root    0 Jun 27 16:22 device -> ../../../axp20x-battery-power-supply/
    -r--r--r-- 1 root root 4096 Jun 27 16:22 health
    drwxr-xr-x 3 root root    0 Jun 27 15:34 hwmon0/
    -r--r--r-- 1 root root 4096 Jun 27 16:22 online
    drwxr-xr-x 2 root root    0 Jun 27 15:34 power/
    -r--r--r-- 1 root root 4096 Jun 27 16:22 present
    -r--r--r-- 1 root root 4096 Jun 27 16:22 status
    lrwxrwxrwx 1 root root    0 Jun 27 15:34 subsystem -> ../../../../../../../../../class/power_supply/
    -r--r--r-- 1 root root 4096 Jun 27 16:22 type
    -rw-r--r-- 1 root root 4096 Jun 27 15:34 uevent
    -rw-r--r-- 1 root root 4096 Jun 27 16:22 voltage_max_design
    -rw-r--r-- 1 root root 4096 Jun 27 16:22 voltage_min_design
    -r--r--r-- 1 root root 4096 Jun 27 16:22 voltage_now
    -r--r--r-- 1 root root 4096 Jun 27 16:22 voltage_ocv
    drwxr-xr-x 2 root root    0 Jun 27 15:34 wakeup4/
    
[/code]
#### Scripts
Bash script `/etc/update-motd.d/30-armbian-sysinfo` ([source code][5540]) in Armbian gives such output: 
[code] 
    System load:   7%           	Up time:       44 min	Local users:   3
    Memory usage:  10% of 998M   	IP:	       192.168.1.188 172.20.1.1
    CPU temp:      47°C           	Usage of /:    5% of 29G
    Battery:       29% charging
    
[/code]
### From i2c
#### Scripts
[axp209.sh][5541] — with a links to another scripts 
## See also
  * [I2Cdev][5542] — general information about i2c
