# Cubieboard/TTL
< [Cubieboard][14455]
 
[![Exclamation-red.png][14458]][14459] WARNING: DO NOT CONNECT THE RED LINE TO VCC.
## Contents
  * [1 Connection][14460]
    * [1.1 Pictures][14461]
  * [2 Availability][14462]
  * [3 Driver][14463]
    * [3.1 Linux Driver][14464]
    * [3.2 OS X Driver][14465]
    * [3.3 Windows Driver][14466]
  * [4 Software][14467]
  * [5 Configuration][14468]
  * [6 Sample output][14469]

## Connection
**If you get a USB-Serial adapter from somewhere else, please check the cable colors of it at the vendor**. The RX pin on the adapter should be connected to the TX pin on the Cubieboard and the adapter TX pin vice versa, so that the serial wires are crossed. 
The CubieBoard (Rich package) is currently supplied with a Prolific PL2303 USB cable. This cable provides VCC power on the red cable. The Cubieboard does NOT require power (red cable), and it **may damage** your board if connected. The CubieBoard provides a pin header with 4 pins for [TTL UART][14470] connection. 
[![Exclamation-red.png][14458]][14459] Warning! Some PL2303 wires, like the PL2303HX 5V, could damage your Cubieboard. See [UART-USB Dongle][14471] for more details. 
If you are using the supplied PL2303 cable, then the connection should be as follows: 
[![][14472]][14473]
[][14474]
How to connect to a Cubieboard 1 or 2
**Cable** | **Pin on Cubieboard**  
---|---  
GROUND (BLACK) | GND   
_MUST NOT BE CONNECTED_ | VCC   
PIN2 (GREEN) | RX   
PIN1 (WHITE) | TX   
[![Exclamation-red.png][14458]][14459] WARNING: DO NOT CONNECT THE RED LINE TO VCC.
### Pictures
  * [![][14475]][14476]
Cubieboard TTL cable connection. Note that the red cable is NOT connected. 
  * [![][14477]][14478]
Another Cubieboard TTL cable connection. 
  * [![][14479]][14480]
Close-up that shows the pin connection. 

## Availability
  * <http://www.aliexpress.com/store/product/TTF-to-USB-Serial-line/511685_665830339.html>
  * <https://www.adafruit.com/products/954>

## Driver
### Linux Driver
Driver for the PL2303 is inside the kernel. It will work with default settings. 
### OS X Driver
The opensource driver on [github][14481] works and the binary version is on the link below. 
  * <https://github.com/downloads/berg/osx-pl2303/osx-pl2303-0.4.1-failberg.pkg> (could someone confirm that this works?)

It is at least confirmed to work on Mac OS X 10.6.8 32 bit version. 
There is also a vendor-made driver; 
  * Go to <http://www.prolific.com.tw/US/index.aspx>
  * Click support
  * Login with GUEST / GUEST
  * Click on "click here for PL2303 USB to Serial drivers"
  * half way down, download the file md_PL2303_MacOSX10.6_dmg_v1.4.0.zip

### Windows Driver
Windows Driver for Prolific PL2303 is installed automatically. If your "Device Manager" mark the PL2303 device (Prolific USB-to-Serial Comm Port) with yellow exclamation mark and the status of the device shows "code 10", then you probably got counterfeit (fake) cable or you are using the cable with Windows 8. In both cases you just have to install older version of Prolific drivers (1.6.0, 1.7.0, 1.8.0 or later won't work). 
  * For PL2303 HXA, XA (to check your version use the utility provided in latest [Prolific drivers][14482].)
  * Installer version & Build date: 1.5.0 (2011-10-21)
  * Windows XP (32 & 64-bit) WDM WHQL Driver: v2.1.27.185
  * Windows Vista/7/8 (32 & 64-bit) WDF WHQL Driver: v3.4.25.218
  * Files: 
    * PL2303_Prolific_DriverInstaller_v1.5.0.zip (SHA-1 [8b1e1a8b0ee5939ff2fb185690ec038f191dbcde][14483]) 
      * PL2303_Prolific_DriverInstaller_v1.5.0.exe (SHA-1 [43fe44b600586e9b41088ba1be5b4eee96c7dc23][14484])
  * [Download][14485] (Mirror [#1][14486], [#2][14487])

## Software
See the [ general instructions on using serial software][14488]. 
## Configuration
It seems the default setting for uBoot and terminal serial is **115200 8N1** : 
Serial line | /dev/ttyUSB0 or COM1   
---|---  
Speed (baud) | 115200   
Data bits | 8   
Stop bits | 1   
Parity | None   
Flow control | None   
_Windows users can determine proper COM port from Device Manager._
## Sample output
See <http://pastebin.com/p77V8xdC> for sample output. It shows the boot process of the Cubieboard.
