# Anichips PhoenixA20
Anichips PhoenixA20  
---  
[![Anichips phoenixa20-topside.jpg][7737]][7738]  
Manufacturer |  [Anichips Technology][7739]  
Dimensions |  100 _mm_ x 72 _mm_ (Pico-ITX)   
Release Date |  November 2013   
Website |  [News/Product Page][7740]  
Specifications   
SoC |  [A20][7741] @ 1GHz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  4GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI, VGA   
Audio |  HDMI   
Network |  WiFi 802.11 b/g/n (Ampak AP6210), 10/100Mbps Ethernet (Realtek RTL8201CP)   
Storage |  µSD , SATA   
USB |  2 USB2.0 Host   
Other |  Bluetooth (Ampak AP6210), EEPROM   
Headers |  UART, LCD, Camera, 2 expansion connectors.   
This page needs to be properly filled according to the [New Device Howto][7742] and the [New Device Page guide][7743].
The phoenixA20 is a [Pico-ITX][7744] sized development board. 
## Contents
  * [1 Identification][7745]
  * [2 Sunxi support][7746]
    * [2.1 Current status][7747]
    * [2.2 Images][7748]
    * [2.3 HW-Pack][7749]
    * [2.4 BSP][7750]
    * [2.5 Manual build][7751]
  * [3 Tips, Tricks, Caveats][7752]
    * [3.1 FEL mode][7753]
    * [3.2 ADB][7754]
    * [3.3 Ethernet][7755]
    * [3.4 Headers][7756]
    * [3.5 Improved WIFI reception][7757]
    * [3.6 VGA][7758]
  * [4 Adding a serial port][7759]
  * [5 Pictures][7760]
  * [6 Also Known as][7761]
  * [7 See also][7762]
    * [7.1 Vendor Images][7763]

# Identification
Near the Wifi/Bluetooth module, opposite from the Ethernet connector, the PCB reads: 
[code] 
    Phoenix V2.0 2013-10-24
    Designed by EASITEK&ANICHIPS
[/code]
# Sunxi support
## Current status
No patches have been submitted for inclusion in the sunxi repositories.
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the "MANUFACTURER_DEVICE" target.
  * The .fex file can be found in sunxi-boards as [MANUFACTURER_DEVICE.fex][7764]

Everything else is the same as the [manual build howto][7765]. 
[![][7766]][7767]
[][7768]
U-boot button
# Tips, Tricks, Caveats
## FEL mode
The U-boot button triggers [ FEL mode][7769]. 
## ADB
To use ADB, you need to connect the board ONLY via the USB cable and don't connect the power-cable. 
## Ethernet
The Allwinner A20 provides two Ethernet MAC controllers: EMAC and GMAC. The PhoenixA20 board uses the [EMAC][7770] controller. 
## Headers
There are four 2.00mm pitch headers on the board. These are labelled UART, digital, analogue and LCD. The digital header mainly provides three additional UART interfaces, two I2C interfaces and two spare pins that could be used as GPIOs for two 1-wire interfaces. There is also a possibility of using it for [Inter-IC Sound (I2S)][7771]. The analogue header provides audio, human input, video and PWM interfaces and the power enable and reset pins. The LCD header could be re-purposed as a 28 pin GPIO header. For more details see the [PhoenixA20 Headers page][7772]. 
## Improved WIFI reception
[![][7773]][7774]
[][7775]
Solder a wire to the point closest UART pins to improve wifi signal
To improve Wifi reception you can solder a wire to the board of about 10cm long 
## VGA
Like with most devices based on Allwinners reference platform, no DDC is available, and the monitors capabilities cannot be detected. 
[![][7776]][7777]
[][7778]
UART pins
# Adding a serial port
There is a clearly marked 2.00mm pitch header for UART debugging on the board. A 2.00mm pitch connector to 2.54mm pitch header cable is also supplied with the board. Just connect the leads according to the [UART howto][7779]
# Pictures
  * [![Anichips phoenixa20-topside.jpg][7780]][7738]
  * [![Anichips phoenixa20-underside.jpg][7781]][7782]
  * [![Anichips phoenixa20-ports-side on.jpg][7783]][7784]
  * [![Anichips phoenixa20-uart analog-side on.jpg][7785]][7786]
  * [![Anichips phoenixa20-csi digital-side on.jpg][7787]][7788]
  * [![Anichips phoenixa20-lcd power sata-side on.jpg][7789]][7790]

# Also Known as
This type of device has no rebadgers. 
# See also
  * [Schematic][7791]
  * [phoenixA20 wiki][7792]
  * [phoenixA20 forums][7793]

## Vendor Images
  * [PHOENIXA20_android_4.2_hdmi.img][7794]
  * [PhoenixA20-debian-desktop-nand-v1.1.img][7795]
  * [PhoenixA20-debian-nand-basic.img][7796]
  * [PhoenixA20-ubuntu-server-nand-v2.0.img][7797]
  * Mirror: <http://filez.zoobab.com/allwinner/a20/phoenix/>
