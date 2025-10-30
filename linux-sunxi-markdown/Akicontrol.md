# akicontrol
Akicontrol is a GPLv2 X utility developed by [Daniel O'Neill][6209] to: 
  * Monitor battery status
  * Control LCD brightness
  * Switch CPU governors
  * Handle power button keypresses (to enable and disable the LCD/Backlight)

The application uses Qt and is developed in C++ for use on the Sun4i-based H6 Netbook, but may also be useful on other devices running Xorg. 
A udev rule must be in place to make the /dev/disp device writable by the application user to manage the display. 
To work with CPU governors the user must have the ability to: 
  * Read /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors
  * Read and Write /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

An example udev .rules file and systemd-compatible initscript for setting permissions can be found in the contrib/ directory in the source. These both assume the user is member to the groups _video_ and _sys_. 
## See also
  * [Cpufreq][6210]
  * [Display][6211]

## External links
  * [[1]][6212] \- git repository
  * [[2]][6213] \- Official project Wiki page
