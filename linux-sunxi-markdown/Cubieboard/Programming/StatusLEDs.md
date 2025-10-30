# Cubieboard/Programming/StatusLEDs
< [Cubieboard][14311]
 
## Accessing the status LEDs
The Cubieboard has two status LEDs, a green one and a blue one. These can be accessed and switched on and off with the following instructions. 
### Preparation
You need to have a bootable image with a recent kernel (3.x). 
Add the following lines to your script.bin 
[code] 
    [leds_para]
    leds_used = 1
    leds_num = 2
    leds_pin_1 = port:PH20<1><default><default><0>
    leds_name_1 = "green:ph20:led1"
    leds_pin_2 = port:PH21<1><default><default><0>
    leds_name_2 = "blue:ph21:led2"
    
[/code]
### Access
Enable an LED (blue, in this case): 
` `
`
[code]
    echo 255 > /sys/class/leds/blue\:ph21\:led2/brightness
    
[/code]
```
``
Switch off an LED (blue, in this case): 
` `
`
[code]
    echo 0 > /sys/class/leds/blue\:ph21\:led2/brightness
    
[/code]
```
``
Blinking an LED (blue, in this case): 
` `
`
[code]
    echo timer > /sys/class/leds/blue\:ph21\:led2/trigger
    
[/code]
```
``
  
Use an LED (blue, in this case) to show SD card activity 
` `
`
[code]
    echo mmc0 > /sys/class/leds/blue\:ph21\:led2/trigger
    
[/code]
```
``
For others available triggers, run the command 
` `
`
[code]
    cat /sys/class/leds/blue\:ph21\:led2/trigger
    
[/code]
```
``
