# LIRC
Many media players and set-top boxes based on A1x SoCs feature a built-in standard CIR[[1]][30014] infrared receiver for 38 kHz based IR controllers that has LIRC software support, which in turn is compatible with most known media center remotes made for computers and media players. 
    [![Sticky-note-pin.png][30015]][30016] _Note:_ People tend to mix up CIR with IrDA[[2]][30017]. Most Allwinner SoCs can support the IrDA protocol via their UARTs, but would need additional hardware (an IrDA transceiver) to do so. Simple infrared receivers (which can be connected straight to _IR0_ / _IR1_) always relate to CIR instead, using a different protocol.
**LIRC** (Linux Infrared Remote Control) supports this integrated infrared receiver, and it acts as a middleware between the hardware and the software applications that supports LIRC, which most media player and media center applications does. 
## Contents
  * [1 What is LIRC?][30018]
  * [2 Using LIRC with Mele A2000][30019]
  * [3 Mele A1000/A2000 IR-receiver udev rule][30020]
  * [4 irrecord to record remote control key][30021]
  * [5 Using existing remote definitions][30022]
  * [6 InfraRed Remote Controls tested with standard CIR receivers for 38 kHz based IR controllers][30023]
  * [7 Using LIRC with Cubieboard2 (A20 SoC)][30024]
  * [8 Troubleshooting][30025]
    * [8.1 adding new remote (tl;dr version)][30026]
    * [8.2 adding new remote in mainline (tl;dr version)][30027]
  * [9 See Also][30028]
  * [10 External links][30029]
  * [11 References][30030]

## What is LIRC?
LIRC (Linux Infrared Remote Control) is an open source (GPL) package that allows users to receive and send infrared signals with a Linux-based computer system and applications. 
With LIRC and an IR receiver the user can control their computer with almost any infrared remote control (e.g. a TV remote control). The user may for instance control video or music playback software with their remote control. 
One GUI frontend is KDELirc, built on the KDE libraries. 
## Using LIRC with Mele A2000
To use Mele's IR-Receiver you have to make lirc listen at `/dev/input/event<X>`, because the IR-receiver emulates keyboard input. The following steps are necessary to get Mele's IR to work with the supplied remote: 
  * Install lirc
  * Be sure to have sun4i-ir.ko compiled and do a "modprobe sun4i_ir". This should result in something like:

[code] 
     input: sun4i-ir as /devices/virtual/input/input4
     IR Initial OK
    
[/code]
  * cat /proc/bus/input/devices may give you the right event<X>
  * Edit /etc/lirc/hardware.conf:

[code] 
     REMOTE_DRIVER="devinput"
     REMOTE_DEVICE="/dev/input/event4"
     START_LIRCD="true"
    
[/code]
  * Copy a suitable [lircd.conf][30031] to /etc/lirc/[lircd.conf][30031]
  * Start lirc, and test input with irw
  * Further steps to be done ...

## Mele A1000/A2000 IR-receiver udev rule
To use always the same name instead of looking for event<X> create udev rule (/etc/udev/rules.d/10-meleir.rules): 
[code] 
     SUBSYSTEM=="input", ACTION=="add", KERNEL=="event*", ATTRS{name}=="sun4i-ir", SYMLINK+="input/meleir"
    
[/code]
  * Edit /etc/lirc/hardware.conf:

[code] 
     REMOTE_DEVICE="/dev/input/meleir"
    
[/code]
  * reboot or

[code] 
     # rmmod sun4i_ir
     # /etc/init.d/udev restart
     # /etc/init.d/lirc restart
     # modprobe sun4i_ir
    
[/code]
  * ls -l /dev/input

[code] 
     drwxr-xr-x 2 root root     60 Jan 11 13:44 by-path
     crw-r----- 1 root root 13, 64 Jan 11 13:44 event0
     crw-r----- 1 root root 13, 65 Jan 11 15:19 event1
     lrwxrwxrwx 1 root root      6 Jan 11 15:19 meleir -> event1
     crw-r----- 1 root root 13, 63 Jan 11 13:44 mice
    
[/code]
## irrecord to record remote control key
irrecord should do the job by recording your remote keys: <http://linux.die.net/man/1/irrecord>
For example, to teach LIRC about a Syabas Popcorn Hour A-100 Remote Control. Note that **lircd** cannot be running; 
[code] 
    # /etc/init.d/lirc stop     # or pkill lircd
    # irrecord -d /dev/lirc0 a100.conf
    Don't stop pressing buttons until two lines of dots (2x80) have been
    generated.
    
    Press RETURN now to start recording.
    ................................................................................
    Found const length: 107344
    Please keep on pressing buttons like described above.
    ................................................................................
    Space/pulse encoded remote control found.
    Signal length is 67.
    Found possible header: 8977 4440
    Found trail pulse: 591
    Found repeat code: 8977 2201
    Signals are space encoded.
    Signal length is 32
    Now enter the names for the buttons.
    Please enter the name for the next button (press <ENTER> to finish recording)
    KEY_PLAY
    
    Now hold down button "KEY_PLAY".
    [continue for all buttons]
    
[/code]
## Using existing remote definitions
A large repository of known remote controls are available at <http://lirc.sourceforge.net/remotes/>
In this example case we will pick [Syabas A-100][30032] Remote Control (which is used with Syabas Popcorn Hour series of media player and other Networked Media Tank clones). 
[code] 
    # cd /etc/lirc/
    # wget <http://lirc.sourceforge.net/remotes/syabas/A-100>
    # cp A-100 lircd.conf
    # vi hardware.conf
    REMOTE="None"
    REMOTE_MODULES=""
    REMOTE_DRIVER=""
    REMOTE_DEVICE="**/dev/lirc0** "
    REMOTE_SOCKET="**/dev/lircd** "
    REMOTE_LIRCD_CONF=""
    REMOTE_LIRCD_ARGS=""
    
    START_LIRCD="**true** "
    
[/code]
[code] 
    # /etc/init.d/lirc start     # Or reboot
    * Starting remote control daemon(s) : LIRC 
      ...done.
    
[/code]
If you run something like; 
[code] 
     # tail -f /var/log/daemon.log &
    
[/code]
You can see the messages from **lircd**. Test that your remote now works with: 
[code] 
      # irw /dev/lircd
    Nov  1 02:48:26 a1x lircd-0.8.6[814]: accepted new client on /dev/lircd
    0000000020d30af5 00 KEY_PLAY Syabas_A-100
    0000000020d30af5 01 KEY_PLAY Syabas_A-100
    
[/code]
Now when you start **xbmc** the remote control should work. You can check that it works by viewing the xbmc.log log file: 
[code] 
    # tail -f /home/a1x/.xbmc/temp/xbmc.log
    Nov  1 02:44:26 a1x lircd-0.8.6[814]: accepted new client on /dev/lircd
    02:44:46 T:1100938672   DEBUG: LIRC: Update - NEW at 20549:0000000020d350af 00 KEY_DOWN Syabas_A-100 (KEY_DOWN)
    02:44:46 T:1100938672   DEBUG: SDLKeyboard: scancode: 74, sym: 0112, unicode: 0000, modifier: 0
    02:44:46 T:1100938672   DEBUG: OnKey: down (f081) pressed, action is Down
    
[/code]
We still need to tell xbmc to use the remote inputs, the best way to do that is to copy the default, and modify as needed: 
[code] 
    # cd /home/a1x/.xbmc/userdata
    # cp /usr/local/share/xbmc/system/Lircmap.xml .
    # vi Lircmap.xml
            <remote device="**Syabas_A-100** ">
    
[/code]
Change the remote name to that of what is in the lircd.conf you download/setup, (it is also printed in the xbmc.log output). Restart xbmc. 
## InfraRed Remote Controls tested with standard CIR receivers for 38 kHz based IR controllers
This only lists infrared remote controls that are compatible with standard CIR infrared receiver for 38 kHz based IR controllers. 
  1. [Syabas Popcorn Hour A-100 Remote Control][30032] works with [LIRC][30033] 0.9.0 and Linux Kernel 2.6.32 on Ubuntu 10.04 or later.
  2. Example #1 (works with [LIRC][30034] 0.9.0 and Linux Kernel 2.6.32 on Ubuntu 10.04)
  3. Example #2 (works with [LIRC][30034] 0.9.0 and Linux Kernel 3.0 on Ubuntu 11.10)
  4. Example #?

## Using LIRC with Cubieboard2 (A20 SoC)
Most of the information above is useful, as well as the Troubleshooting section below. Here are the modifications and configurations required for LIRC to work on a Cubieboard2 (A20 SoC). 
  * Using **Linux Cubian 3.4.79-sun7i**
  * LIRC kernel module here is **sunxi_ir** > add it to **/etc/modules**
  * Create the **/etc/udev/rules.d/10-cb2ir.rules** file and add the rule:

[code] 
    SUBSYSTEM=="input", ACTION=="add", KERNEL=="event*", ATTRS{name}=="sunxi-ir", SYMLINK+="input/cb2ir"
    
[/code]
  * **apt-get install lirc**
  * Create a new **/etc/lirc/hardware.conf** with just the following content:

[code] 
    # /etc/lirc/hardware.conf
    #
    START_LIRCMD=false
    START_IREXEC=false
    LOAD_MODULES=true
    DRIVER="devinput"
    DEVICE="/dev/input/cb2ir"
    START_LIRCD="true"
    
[/code]
  * Use <http://lirc.sourceforge.net/remotes/devinput/lircd.conf.devinput> as /etc/lirc/lircd.conf (change it afterwards to suit your specific remote controller unit buttons)
  * After rebooting, the following is expected to happen: preloaded kernel module, input device successfully generated and the lirc service up and running.

[code] 
    cubie@Cubian:~$ lsmod|grep ir
    sunxi_ir                4045  0
    
[/code]
[code] 
    cubie@Cubian:~$ ls -lh /dev/input/*ir
    lrwxrwxrwx 1 root root 6 Jul  8 10:56 /dev/input/cb2ir -> event4
    
[/code]
[code] 
    cubie@Cubian:~$ ps aux | grep [l]irc
    root      2340  0.0  0.0   3008   600 ?        Ss   10:56   0:00 /usr/sbin/lircd --driver=devinput --device=/dev/input/cb2ir
    
[/code]
  * Start irw and test with your remote. If it is a supported remote controller unit, it should start registering the events right away:

[code] 
    cubie@Cubian:~$ irw /dev/lircd 
    0000000080010012 00 KEY_E devinput
    000000008001000c 00 KEY_MINUS devinput
    0000000080010012 00 KEY_E devinput
    0000000080010017 00 KEY_I devinput
    0000000080010016 00 KEY_U devinput
    000000008001000c 00 KEY_MINUS devinput
    0000000080010001 00 KEY_ESC devinput
    000000008001001e 00 KEY_A devinput
    000000008001004f 00 KEY_KP1 devinput
    000000008001004b 00 KEY_KP4 devinput
    
[/code]
If you're stuck, make sure it works using the Troubleshooting section and running lircd manually - and then transporting your working parameters to the **/etc/lirc/hardware.conf** file, for the service to work. 
## Troubleshooting
Some of the remote configuration files on sourceforge are seriously out of date. If **lircd** seems to be starting up, but none of the tools is getting any events, try running **lircd** manually: 
[code] 
    # /etc/init.d/lirc stop
    # /usr/sbin/lircd -n --output=/dev/lircd --driver=devinput --device=/dev/input/event1 <suspect-config-file>
    lircd-0.9.0[17422]: lircd(devinput) ready, using /dev/lircd
    
[/code]
Now from another window, run **irw** : 
[code] 
    # irw /dev/lircd
    
[/code]
You should see something like this from **lircd** : 
[code] 
    lircd-0.9.0[17422]: accepted new client on /dev/lircd
    lircd-0.9.0[17422]: initializing '/dev/input/event1'
    
[/code]
And when you press a button on the remote: 
[code] 
    lircd-0.9.0[17422]: you are using an obsolete devinput config file: Success
    lircd-0.9.0[17422]: get the new version at <http://lirc.sourceforge.net/remotes/devinput/lircd.conf.devinput>: Success
    
[/code]
You'll have to get this new devinput file from sourceforge and use **irrecord** to create your own remote configuration file. Note that you can't just use an empty config file; **irrecord** appears to need some global values from the config file's header in order to capture the remote's signals. 
The configuration files generated by **irrecord** also seem to have extra garbage at the end of the key codes. For example, this was generated from a Sound-Fly Bluetooth remote: 
[code] 
             KEY_UP                   0x01001200000001 0x000000BED7A9ED
             KEY_DOWN                 0x01001100000001 0x000000BED7A9ED
    
[/code]
The third field confused lircd, causing it to ignore these keys; removing the 0x000000BED7A9ED from each line fixed it. Not sure if these values are necessary under special conditions (they had to be removed from the .conf files of 5 different remotes to get them to work), though, so you should first try lircd with them and then remove them if it doesn't seem to be working. 
### adding new remote (tl;dr version)
  * essential fields in /etc/lirc/hardware.conf (event1 is an example, check other entries if it doesn't work) 
    * DRIVER="devinput"
    * DEVICE="/dev/input/event1"
  * learn the keys of the remote (to list the available standard keys do: irrecord -l) 
    * cd /tmp
    * wget -O newremote.conf <http://lirc.sourceforge.net/remotes/devinput/lircd.conf.devinput>
    * irrecord -d /dev/input/event1 -H devinput newremote
  * if you were able to teach it new keys, just copy it onto default config: 
    * mv /etc/lircd.conf /etc/lircd.conf.old
    * mv newremote.conf /etc/lircd.conf
  * restart lircd and see if it can see your keys now: 
    * /etc/init.d/lirc restart
    * irw
  * if it doesn't work, check the troubleshooting above (remove third field from buttons in the config)

### adding new remote in mainline (tl;dr version)
  * essential fields in /etc/lirc/hardware.conf (event1 is an example, check other entries if it doesn't work: cat /proc/bus/input/devices|grep -A5 sunxi-ir|grep Handlers|grep -oE "event[0-9]+") 
    * # set protocol and keymap (lines like that in hardware.conf will get executed by shell)
    * /usr/bin/ir-keytable -c -p NEC -w /etc/rc_keymaps/my_remote
    * DRIVER="devinput"
    * DEVICE="/dev/input/event1"
    * MODULES="sunxi_cir"
  * create /etc/lircd.conf containing: 
    * include "/etc/lirc/lircd.conf.devinput"
  * get devinput table: 
    * wget -O /etc/lirc/lircd.conf.devinput <http://lirc.sourceforge.net/remotes/devinput/lircd.conf.devinput>
  * create keys of the remote. you will have to press the keys and associate scancodes with KEY_XXX mappings. 
    * set rc protocol to nec (or anything else, cat the file for alternatives): echo nec > /sys/class/rc/rc0/protocols
    * to get scancodes: ir-keytable -t
    * to get mapping names either: cat /etc/lirc/lircd.conf.devinput or irrecord -l
    * initialize your keytable: echo >/etc/rc_keymaps/my_remote "# table my_remote, type: NEC"
    * add mappings to above file in the format: 0xSCANCODE KEY_XXX, fe: 0x00 KEY_POWER
  * when finished, restart lircd: 
    * /etc/init.d/lirc restart
  * check if it works: 
    * irw

## See Also
  * [XBMC wiki articles with information about using remote controls in XBMC][30035]
    * [HOW-TO setup LIRC on Linux][30036] \- a guide on XBMC wiki that applies to all LIRC supporting applications
    * [Automatic LIRC resume script][30037] \- a guide on XBMC wiki that applies to all LIRC supporting applications
    * [Remote Control Reviews for XBMC usage][30038]

## External links
  * [LIRC - Linux Infrared Remote Control official homepage][30039]
    * [LIRC repository of lircd config files for known remote controls][30040]
  * [SourceForge.net - LIRC project and source code][30041]
  * [irrecord - IR record remote control key recorder][30042]
  * [KDELirc Homepage - KDELirc is a KDE frontend for the][30043]

## References
  1. [↑][30044] Consumer IR: <https://en.wikipedia.org/wiki/Consumer_IR>
  2. [↑][30045] Infrared Data Association standard: <https://en.wikipedia.org/wiki/IrDA>
