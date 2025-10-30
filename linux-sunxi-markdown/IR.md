# IR
## Contents
  * [1 Infra Red][25084]
  * [2 sunxi-3.4 ("legacy" kernel)][25085]
    * [2.1 remapping][25086]
  * [3 mainline kernel (4.x) and sunxi-cir][25087]
  * [4 See also][25088]

# Infra Red
IR (Infra Red) light is used in many consumer applications to transmit small amounts of data such as key presses on remotes and keyboards. These devices are refered to as CIR ([Consumer Infra Red][25089]). Receivers for this signal are available on many common boards. 
  

# sunxi-3.4 ("legacy" kernel)
The sunxi-3.4 IR is exposed as a a keyboard on the Linux input device interface if built into kernel or after modprobe sunxi-cir (previously sunxi_ir_rx). For example, the following simple _keybinder_ application might be used to run arbitrary commands when receiving a specific keycode via IR. You can install it by 
[code] 
    $ git clone https://github.com/elopez/keybinder.git
    $ cd keybinder
    $ sudo make install
    
[/code]
Configuration is handled on _/etc/keybinder.conf_ , as a "keycode,command" pair per line. The application prints every keycode received, so you may as well use it to figure out the keycodes you want to use. 
To execute the application, run 
[code] 
    $ sudo keybinder /dev/input/event0
    
[/code]
## remapping
in 3.4 kernel i haven't found any easy way to remap ir scancodes coming from particular remote. it's possible by editing drivers/input/keyboard/ir-keymap.h though: 
  1. find out what scancodes you get for your remote by running evtest, pressing keys and making notes of key--code
  2. edit header file. start in the secpond half of the file. possible key aliases are in include/linux/input.h
  3. recompile the kernel (make modules will do if you selected suni-ir as module)
  4. reinsert the module or update kernel and reboot

# mainline kernel (4.x) and sunxi-cir
For devices that feature a standard (38 kHz) CIR receiver, the mainline kernel can be configured with `CONFIG_IR_SUNXI`. The kernel option is located under "Device drivers", "Multimedia support", "Remote Controller devices", "SUNXI IR remote control"; the driver is named **sunxi-cir**. 
[![Sticky-note-pin.png][25090]][25091] _Note:_ You do not need LIRC installed to follow the steps below. The input subsystem of recent Linux kernels can handle RC devices and associated keymaps just fine without it. 
If you compiled the driver as a module, the first step is to make sure that module gets loaded - either by adding it to the autoloaded modules (depends on your distribution), or manually: `modprobe sunxi-cir`. 
Once the driver is initialized, your kernel log (`dmesg`) should show something similar to 
[code] 
    [  110.032464] Registered IR keymap rc-empty
    [  110.033667] input: sunxi-ir as /devices/platform/soc@01c00000/1c21800.ir/rc/rc0/input1
    [  110.033729] rc0: sunxi-ir as /devices/platform/soc@01c00000/1c21800.ir/rc/rc0
    [  110.066201] IR NEC protocol handler initialized
    [  110.083973] IR RC5(x/sz) protocol handler initialized
    [  110.101950] IR Sony protocol handler initialized
    [  110.103835] IR JVC protocol handler initialized
    [  110.107900] IR RC6 protocol handler initialized
    [  110.114389] IR SANYO protocol handler initialized
    [  110.116697] IR MCE Keyboard/mouse protocol handler initialized
    [  110.119481] input: MCE IR Keyboard/Mouse (sunxi-ir) as /devices/virtual/input/input2
    [  110.119720] sunxi-ir 1c21800.ir: initialized sunXi IR driver
    [  110.120865] IR Sharp protocol handler initialized
    [  110.130851] IR XMP protocol handler initialized
    
[/code]
Check that the sunxi IR shows up in `cat /proc/bus/input/devices` : 
[code] 
    I: Bus=0019 Vendor=0001 Product=0001 Version=0100
    N: Name="sunxi-ir"
    P: Phys=sunxi-ir/input0
    S: Sysfs=/devices/platform/soc@01c00000/1c21800.ir/rc/rc0/input1
    U: Uniq=
    H: Handlers=kbd event1
    B: PROP=0
    B: EV=100013
    B: KEY=1000000 0 0 0 0
    B: MSC=10
    
    I: Bus=0000 Vendor=0000 Product=0000 Version=0000
    N: Name="MCE IR Keyboard/Mouse (sunxi-ir)"
    P: Phys=/input0
    S: Sysfs=/devices/virtual/input/input2
    U: Uniq=
    H: Handlers=kbd event2
    B: PROP=0
    B: EV=100017
    B: KEY=30000 0 7 ff87207a c14057ff febeffdf ffefffff ffffffff fffffffe
    B: REL=3
    B: MSC=10
    
[/code]
    [![Sticky-note-pin.png][25090]][25091] _Note:_ Make sure those "H: Handlers=" lines list the event nodes associated with the devices. In case they are missing, there's a chance your kernel may be misconfigured - check that **CONFIG_INPUT_EVDEV=y** is set! The following commands can be used to find the actual /dev/input/eventX device:
[code] 
    EVT=`awk '/^[N|H]/{if(f){for(i=2;i<=NF;i++){ if(match($i,/event/)){ print $i; exit 0;} }}; if(match($2, /sunxi-ir/)){ f=1 } }'</proc/bus/input/devices`
    ln -s /dev/input/$EVT /dev/shm/ir
    
[/code]
The device should also be available in _/sys/class/rc/_ , usually as _rc0_ : 
[code] 
    ~ # cat /sys/class/rc/rc0/protocols
    other [unknown] rc-5 nec rc-6 jvc sony rc-5-sz sanyo sharp mce_kbd [lirc] xmp
    
[/code]
The above command lists the available IR protocols. At this point it may be necessary to **select a specific protocol** that corresponds to the remote you intend to use. You do so by writing to the _sysfs_ node. For example, I have a universal remote control that works with the "nec" protocol - so to configure it, I use: `echo nec > /sys/class/rc/rc0/protocols`
When you're set, run the `evtest` program to check if everything works. Either start it without arguments to get prompted, or pass the input (event) node that corresponds to the _Name="sunxi-ir"_ device. In the above example, that would be `evtest /dev/input/event1`. 
If all goes well, _evtest_ will now report events for key presses that you do on your infrared remote. 
# See also
  * [LIRC][25092]
  * [IR Controller Register Guide][25093]
  * [CIR][25089]
