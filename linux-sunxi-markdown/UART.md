# UART
[![][56923]][56924]
[][56925]
A common CP2102 3.3V capable USB UART module
A UART (stands for universal asynchronous receiver-transmitter) or serial console is absolutely essential when doing bootloader or kernel development on any computer. Due to the lack of a standard PC BIOS and the VESA BIOS that goes with it, access to the serial console on ARM devices is even more important than on the PC. 
Even if you do not intend to do much U-Boot or kernel work, access to the serial console will be a life-saver when anything goes wrong. 
## Contents
  * [1 Before you start][56926]
  * [2 UART hardware][56927]
    * [2.1 PC Serial port][56928]
    * [2.2 UART-USB dongle][56929]
    * [2.3 Using an Arduino][56930]
    * [2.4 USB serial gadget][56931]
  * [3 Using the serial console][56932]
    * [3.1 Troubleshooting / device file permissions][56933]
    * [3.2 Software][56934]
      * [3.2.1 Linux / OSX][56935]
        * [3.2.1.1 _cu_][56936]
        * [3.2.1.2 _screen_][56937]
        * [3.2.1.3 _gtkterm_][56938]
        * [3.2.1.4 _tinyserial_][56939]
      * [3.2.2 Windows][56940]
  * [4 Attaching the UART][56941]
    * [4.1 With a UART connector available][56942]
    * [4.2 Without a UART connector][56943]
      * [4.2.1 Necessary tools and skills][56944]
      * [4.2.2 Disassembling the device][56945]
      * [4.2.3 Inspect the mainboard][56946]
      * [4.2.4 Attaching the UART module][56947]
      * [4.2.5 Make some noise][56948]
      * [4.2.6 Find TX][56949]
      * [4.2.7 Find RX][56950]
      * [4.2.8 Cable routing][56951]
      * [4.2.9 Soldering the jumper wires][56952]
      * [4.2.10 Reassemble your device][56953]
  * [5 No UART to be found][56954]
  * [6 When all else fails][56955]
  * [7 Common Pitfalls][56956]
    * [7.1 Serial output stops when kernel uart driver is loaded][56957]
    * [7.2 U-Boot stops after initial load][56958]
    * [7.3 UART transmits intermittent garbage when clocked with PLL_PERIPH0(1X)][56959]
    * [7.4 Board won't shut down completely][56960]
  * [8 See Also][56961]

# Before you start
Do **not** connect the RED WIRE unless you want to power the device via UART. Note that the UART power wire probably won't deliver enough power for powering a large SBC. Even a rather small ESP8266 might run out of power with some USB UART dongles. 
# UART hardware
## PC Serial port
Currently, all of the available sunxi hardware requires a **3.3V UART**. If you buy a voltage stepper module ("level shifter") you might get away with attaching it to the serial port of your IBM PC (RS232), but this is rather cumbersome. It is much much easier to just buy a 3.3V USB UART module. 
## UART-USB dongle
Currently, all of the available sunxi hardware requires a **3.3V UART**. Popular chips for such modules are the Silicon Labs CP2102 and the Prolific PL2303HX which are both cheap and relatively easy to find. Many cheap chinese dongles come with either of these or a CH340 based design. They all are supported by mainline Linux. 
If you don't know what to buy, consider one that explicitly has 3.3V and 5V printed on the board -- it will probably be compatible with both 3.3V TX/RX. Please note that the cheap dongles will probably leak more power to the SBC, which might cause issues if you want to reset or shut down the board properly. If you want to avoid this power leakage, google for (optically) isolated USB-UART designs. If you already have a cheap dongle, you could try adding some resistors or diodes between the dongle and the SBC or try a thin USB extension cable. These might lower the leakage just enough to enable resetting the board. 
[![Exclamation.png][56962]][56963] Unfortunately, many TTL adapters are very poorly documented. The actual available voltage level (1.8/3.3/5/…V) is either switchable, or a fixed arbitrary value depending on adapter design. Also adapters with the board embedded inside a case tend to have just wires sticking out at one end, with no documentation regarding which wire is which. **If in doubt use a multimeter.**
Sample measured values (against USB shell when connected to USB only): 
  * Original [Cubietech adapter (board SJ-019 V3.0)][56964] or [this (board SJ-019 V6.0)][56965] white (RX) floating, green (TX) 3.5V, black (gnd) 0V, red (5V) 4.9V. When connected to CB/CT and the board is powered off the power led on the board is dim (not off completely). (You can also check the "[Cubieboard/TTL][56966]" article to use it with a Cubieboard).

  * DX [this][56967] or [this][56968] board SJ-039 V1.0 3V3 3.5V, GND 0V, TXD 3.5V, RXD 1.8V, 5V 4.9V. When connected to CB/CT and the board is powered off the RX LED is lit. The power led on the board also lights up slightly.

  * Some PL2303HX 5V TTL USB adapter - board USB-STC-ISP GND 0V, RX 4.6V, TX 4.9V, 5V 5V, 3.3V 3.4V - this **won't work** \- the voltage is too high for cubieboard and would probably damage it. Untested due to lack of 5V uart.

## Using an Arduino
If you have an [Arduino USB][56969] lying around, you can use it as a UART-USB dongle/converter. Arduino USB and his successors (UNO, Duemilanove, Diecimila, NG, Extreme) have a detachable microcontroller and a USB-to-serial converter. You can use them by carefully taking out the microcontroller from its slot and connecting pins as described on [Attaching the UART module][56947]. Connect Ardunio's RX (pin 0) to the board's RX, TX (pin 1) to TX and GND to GND. Do not connect VCC. 
No driver is needed if you are using Linux. For Windows check [driver installation instructions on Arduino's website][56970]. 
Another alternative to disable the Arduino chip is to wire the RESET pin to the GND pin. Some new Arduino chips are soldered on the board, and cannot be removed easily. 
## USB serial gadget
There is also the option to use the [USB serial gadget][56971] driver. The driver activates only after the kernel has loaded so it won't be able to display U-Boot messages, but at least it can be used to analyze the kernel logs and for logging in. If you're going to use [USBBoot][56972] anyway, this might be a viable option. 
# Using the serial console
Once you hook up your usb module to the host, you should see something like the following appear in your syslog (among other messages): 
    `usb 1-1.3: cp210x converter now attached to ttyUSB0`
    or
    `usb 4-1: pl2303 converter now attached to ttyUSB0`
You see here to which tty your UART is connected to - and you can now use it through one of the programs listed next. 
## Troubleshooting / device file permissions
You might get the following error when trying to access the serial port 
[code] 
     $ sudo cu -s 115200 -l /dev/ttyUSB0
     cu: open (/dev/ttyUSB0): Permission denied
     cu: /dev/ttyUSB0: Line in use
    
[/code]
The reason why you cannot access the serial port even if you are root, is due to additional kernel-level security restrictions (such as AppArmor or SELinux). For the case of Ubuntu, which has AppArmor, your account needs to be member of the group _dialout_. To add your account to the _dialout_ group, run the command 
[code] 
     $ sudo usermod --append --groups dialout myusername
    
[/code]
Then, log out and log in again. 
Consider some other [solutions listed here][56973]. 
You could also try this, but it only works until reboot / device is disconnected: 
[code] 
    sudo chmod 666 /dev/ttyUSB0
[/code]
  

## Software
### Linux / OSX
'_If you are using OSX, you should replace**/dev/ttyUSB0** with **/dev/tty.PL2303-00001014'**_
#### _cu_
_cu_ is an utitlity that comes with popular system distributions like Fedora, Debian, Ubuntu, NetBSD, etc. It can be used to talk to a device connected to a serial port. On Linux with the serial cable as the only USB serial port 
[code] 
     stty -F /dev/ttyUSB0 -crtscts  # turn off hardware flow control - the cable has no wires for that
     _cu_ -s 115200 -l /dev/ttyUSB0
    
[/code]
#### _screen_
[code] 
    screen /dev/ttyUSB0 115200
[/code]
Be sure to set the baudrate to the maximum of 115200, otherwise your console might not function reliably. 
To exit screen is tricky: Ctrl + 'a' followed by '\' - Exit screen and terminate all programs. 
#### _gtkterm_
With gtkterm, a serial terminal tool with minimum graphic interface: 
[code] 
    gtkterm -p /dev/ttyUSB0 -s 115200
    
[/code]
#### _tinyserial_
On Archlinux, the command `com` from `[tinyserial][56974]` package can be used: 
[code] 
    com /dev/ttyUSB0 115200
    
[/code]
### Windows
On Windows you can use software like [TeraTerm][56975] or [Putty][56976] or similar which can connect over serial line. 
# Attaching the UART
## With a UART connector available
If you are using a development board, or a device like the Mele A1000, you should have a nice connector available for attaching your UART module to. If you are extremely lucky, the pin functions will even be printed on your board. Many will not be so lucky, especially with tablets. How to deal with those tougher cases is described below. 
  
**[![Exclamation-red.png][56977]][56978]Do not connect the VCC or 3.3V/5V pin, as that will damage your device!**   
Some modules have color-coded leads, in that case the red wire should correspond to VCC. 
Your USB UART module should have 3 pins:  
RX goes to TX  
TX goes to RX  
GND goes to GND on both 
If you have wired things up correctly, [(read serial console)][56979] and boot your device you should see boot messages flying by. If this does not work, try swapping RX/TX around. 
If it's not clear which pins are which on your target, use a multimeter to determine _GND_ and _VCC_. You can do this by measuring the voltage difference between, for instance, shielding of a USB connector and the UART pins, on a running device. 
## Without a UART connector
Finding the UART pins on a device not meant for development might get quite tricky. It involves disassembling your device with great care, some basic (logical) troubleshooting, some soldering, and then some creativity to be able to export your serial connection to the outside world. 
**[![Exclamation.png][56962]][56963]You will be seriously voiding your warranty here. The likelihood of being left with a damaged device is very high. You might even totally destroy your device. So you need to be extremely careful.**
**Like with everything on this wiki, you yourself are responsible for the actions you take. If you do damage or destroy your device, it's your own fault.**
If you do NOT want to risk damaging or destroying your device, then this howto is not for you. If you are not comfortable with disassembling your device, soldering wires to it, or are lacking some of the necessary equipment, get someone else to do it for you, or don't do it at all. 
### Necessary tools and skills
You need some very basic electronics equipment. A multimeter, your usual collection of banana plug cables, probes and hirschmann clamps, a fine soldering iron (temperature controlled preferred), good solder and flux. 
You will also need some jumper wires, which are easily scrounged off of an old PC case. Preferably black, green and white, in a triple housing. 
### Disassembling the device
Disassembling your device is outside of the scope of this document. By using google, you might be able to find someone who has already taken your device apart, and see the process documented on some android forum. Failing that, there are tons of tablet disassembly guides on the likes of youtube. But do use a [plastic tool][56980] instead of a screwdriver for prying your device open. 
You probably need to be able to access the backside of the motherboard as well, so make sure that the board is free. Do not cut any wires, you will need your device to work, even when all of it has been laid bare. 
### Inspect the mainboard
Often times, you can get lucky, and the UART can be spotted easily. The [Hyundai A7HD][56981] is a great example of that as it has a full serial port on big pre-tinned pads available. In case of the [ Hyundai A7][56982], due to the limited number of testpads, and the way they were grouped, it was also clear which were the UART pins. 
When you are not so lucky, you get presented with a motherboard with a big load of test-pads. This leaves you no option but to systematically try each one of them. 
Regardless of whether the connections are easy to find or not, you still pretty much need to run through the procedure as listed below. 
### Attaching the UART module
Boot your device, and get the original OS running. 
Attach your UART module to your host PC and run your console program on it. 
Connect GND of the UART module to a convenient ground location on your board, and attach a probe to RX of the UART module. 
If you now touch the probe to ground, you should see some broken characters appear on your console program. If not, check whether GND is wired up correctly, or swap RX/TX around on the module side. 
### Make some noise
Normally, your device will only sporadically send data out the serial bus, so the chances of seeing any text scroll past on the console, is pretty low. 
A small tool called [serial_noise][56983] is available, and it is statically compiled and verified to run on many android systems ([source code is available here][56984]). [Download it][56983] to your device, and run it. 
When serial_noise has successfully started, and has found serial consoles in /dev/, it says: 
[code] 
    Flooding serial consoles with text...
[/code]
It will then be sending the /dev/ device names out to all the detected serial consoles on the system. 
### Find TX
You can now go and carefully touch the testpads with your probe, for a few seconds each until you see a device name scroll past. From time to time, verify that your setup is still working by sending some garbage to your hosts console program by touching ground with your probe. 
### Find RX
If or when you have found TX, you should find RX nearby. 
Attach a second probe to the TX pin of the UART module. 
With the other probe on the TX pad on the device still, you can now go and probe for the RX pad. 
The easiest way to verify this is to touch a pad with the probe, and then typing things into the console program on your host computer. If you see your characters echoed back, then you have successfully located the RX pad. 
### Cable routing
Before you solder on the jumper wires, figure out how to get your serial connection available to the outside world. 
With space at a premium in any mobile device, it is not easy to find a good solution here. The punishment for bad routing is quite severe. Your device might not close anymore, and there might be pressure on your devices LCD, leading to uneven backlighting and colours. So do take care at this stage. 
A good example of bad routing and the damage that it causes can be seen on the [Hyundai A7HD page][56985]. 
Make a point of clearly marking which wire is GND by using a brown or black wire for it. If you use jumper wires from an old PC case, try use a triple connector to make life easier in future. 
[![][56986]][56987]
[][56988]
Great for development, but not very socially acceptable.
### Soldering the jumper wires
The usual recommendations for small electronics soldering apply. 
### Reassemble your device
And if all goes well, you should now have a tablet with something strange hanging out. You should be able to attach your UART module to it directly, fire up your console program and immediately get a console. 
Now you can do low level development on your tablet, even when on the move. Just don't bring it up in a conversation with normal people if you still want them to respect you afterwards. 
# No UART to be found
There is a (slight) possibility that the UART simply is not enabled in script.bin. In that case, first finish off the [Retrieving Device information howto][56989] from the [New Device howto][56990], so that you make sure that all the necessary data from the android installation has been retrieved. Then, still following the New Device Howto, try to set up a linux on an SD card and boot from that. You can then try editing [script.bin][56991], to enable the UART, and you can then [try to locate the UART][56947] on the board again. 
# When all else fails
In this case, you usually can still use the SD/micro-SD connector with a [MicroSD Breakout Adapter][56992]. Do note that this requires an altered [U-Boot target][56993] and an altered [script.bin][56991]. 
You lose the functionality of the SD-Card, but you can do [U-Boot][56993] or [Kernel][56994] development over [USBBoot][56972] instead. 
# Common Pitfalls
## Serial output stops when kernel uart driver is loaded
If you have working serial output with U-Boot, but the output stops just after loading the kernel uart driver, like so: 
[code] 
    <6>Serial: 8250/16550 driver, 8 ports, IRQ sharing disabled
    <6>[uart]: used uart info.: 0x01
    <6>[uart]: serial probe 0 irq 33 mapbase 0x01c28000
    <6>sunxi-uart.0: ttyS0 at MMIO 0x1c28000 (irq = 33) is a U6_16550A
    
[/code]
Then there might be something wrong with your kernel commandline. 
Please verify that you have "console=ttyS0,115200" in your commandline, for instance in your U-Boot boot.cmd: 
[code] 
    setenv bootargs console=ttyS0,115200 root=/dev/mmcblk0p2 rootwait panic=10 ${extra}
    
[/code]
Make sure that the baudrate is provided as well. 
## U-Boot stops after initial load
If U-Boot behaves erratically, and stops after initial load, with the last line printed of the boot log repeating the first lines, there might be something wrong with your UART pads, or the cabling to it. 
Here is an example of the boot log, note the repetition of the first line: 
[code] 
        U-Boot SPL 2014.04-10710-g509d96d (Sep 05 2014 - 18:47:53)
        Board: Iteaduino_Plus_A20
        DRAM: 1024 MiB
        Failed to set core voltage! Can't set CPU frequency
        spl: not an uImage at 1600
         
         
        U-Boot 2014.04-10710-g509d96d (Sep 05 2014 - 18:47:53) Allwinner Technology
         
        CPU:   Allwinner A20 (SUN7I)
        Board: Iteaduino_Plus_A20
        I2C:   ready
        DRAM:  1 GiB
        MMC:   SUNXI SD/MMC: 0
        *** Warning - bad CRC, using default environment
         
        In:    serial
        Out:   serial
        Err:   serial
        Net:   emac
        Hit any key to stop autoboot:  0
        sun7i#
        sun7i#
        sun7i#
        sun7i#
        sun7i#
        sun7i# U-Boot 2014.04-10710-g509d96d (Sep 05 2014 - 18:47:53) All2###### U-Boot 2014.04-10710-g509d96d (Sep 05 2014 - 18:47:53l
    
[/code]
When you probe the RX and TX lines with an oscilloscope you will see an erratic serial signal. 
The issue above was a short between RX and TX. Please verify that this is not the case if you have some of the above symptoms. 
## UART transmits intermittent garbage when clocked with PLL_PERIPH0(1X)
Problem was observed on an H5 (NanoPi Neo 2 2017). 
Switch UART clock source (APB2) to use PLL_PERIPH0(1X) running at nominal 600MHz. Confirmed baud rates were as expected. 
UART works but transmits intermittent garbage characters. Oscilloscope confirms that the wrong character is being transmitted and that it's not being mis-received. Observed on a 115000 baud link. 
Solution is to reduce the clock rate to the UART by setting a divide ratio in APB2_CFG_REG. I could achieve my baud rates by setting CLK_RAT_M=12 (divide by 13). 
Note the RM has the following to say when switching clock rates: "Make sure that the clock source output is valid before the clock source switch, and then set a proper divide ratio; after the division factor becomes valid, switch the clock source." 
I used writel(CLK_24M | NEW_DIV_RATIO,APB2_CFG_REG);writel(CLK_PERIPH0(1X) | NEW_DIV_RATIO,APB2_CFG_REG); and it worked fine. 
## Board won't shut down completely
The UART link may often leak some current, which prevents the board from completely shutting down. As a result, the board might not switch to FEL boot mode. Disconnecting and reattaching the UART cable should solve this issue. If one needs to constantly reboot, this can become an issue. There are (optically) isolated UART modules that don't leak power, but one could also experiment with a resistor in the host TX pin or using USB UART dongles with a long extension cable (will weaken the current just enough to prevent the board from staying on). 
# See Also
  * [JTAG][56995]
