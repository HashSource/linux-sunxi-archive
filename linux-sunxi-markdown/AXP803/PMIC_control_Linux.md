# AXP803/PMIC control Linux
< [AXP803][5879]
 
This page describes how to get information from PMIC [AXP803][5879], which is very similar to [AXP209/PMIC control Linux][5882]. 
## Get information
### From /sys/ directory
Armbian examples for [PinePhone v1.2b][5883] (Allwinner A64 + AXP803): 
[code] 
     $ ls -lAF /sys/class/power_supply/axp20x-battery/
    total 0
    -r--r--r-- 1 root root 4096 Jul 19 19:59 capacity
    -rw-r--r-- 1 root root 4096 Jul 19 20:27 constant_charge_current
    -rw-r--r-- 1 root root 4096 Jul 19 20:27 constant_charge_current_max
    -r--r--r-- 1 root root 4096 Jul 19 19:59 current_now
    lrwxrwxrwx 1 root root    0 Jul 19 20:27 device -> ../../../axp20x-battery-power-supply/
    -r--r--r-- 1 root root 4096 Jul 19 20:27 health
    drwxr-xr-x 3 root root    0 Jul 19 19:59 hwmon4/
    -r--r--r-- 1 root root 4096 Jul 19 20:27 online
    drwxr-xr-x 2 root root    0 Jul 19 20:27 power/
    -r--r--r-- 1 root root 4096 Jul 19 19:59 present
    -r--r--r-- 1 root root 4096 Jul 19 19:59 status
    lrwxrwxrwx 1 root root    0 Jul 19 19:59 subsystem -> ../../../../../../../../class/power_supply/
    -r--r--r-- 1 root root 4096 Jul 19 19:59 type
    -rw-r--r-- 1 root root 4096 Jul 19 19:59 uevent
    -rw-r--r-- 1 root root 4096 Jul 19 19:59 voltage_max_design
    -rw-r--r-- 1 root root 4096 Jul 19 20:27 voltage_min_design
    -r--r--r-- 1 root root 4096 Jul 19 19:59 voltage_now
    drwxr-xr-x 2 root root    0 Jul 19 19:59 wakeup11/
     $ cat /sys/class/power_supply/axp20x-battery/current_now
    825000
     $ cat /sys/class/power_supply/axp20x-battery/status
    Charging
     $ cat /sys/class/power_supply/axp20x-battery/voltage_now
    4243000
    
[/code]
## See also
  * [I2Cdev][5884] — general information about i2c
