# Powering the boards and accessories
## Contents
  * [1 Intro][45671]
  * [2 Power supplies][45672]
  * [3 Troubleshooting][45673]
    * [3.1 SATA][45674]
  * [4 Power cables][45675]
  * [5 Power connectors][45676]
    * [5.1 Micro USB][45677]
    * [5.2 DC barrel plug (4.0mm/1.7mm, coaxial, centre positive)][45678]
    * [5.3 Special connectors and GPIO pins][45679]
    * [5.4 POE (power over ethernet)][45680]
  * [6 Power consumption][45681]
  * [7 Measuring power][45682]
    * [7.1 El cheapo power meters][45683]
    * [7.2 Tunable / lab power supplies][45684]
    * [7.3 Odroid power meter][45685]
    * [7.4 Instrument grade power sensors / oscilloscope][45686]
  * [8 See also][45687]

# Intro
This article attempts to cover a wide range of issues related to powering the devices, focusing on the development boards. In general, the [sunxi boards][45688] are all powered with an 5V DC external power source (some Olimex boards accept a wider range of voltages). For boards with a [RTC][45689] (real-time clock), a dedicated backup battery or battery pins might be provided. Most commonly used interfaces for feeding the main operating power for the board are (Micro) USB, a [coaxial DC plug][45690], [GPIO][45691] pins, li-ion batteries, and [POE][45692] (power over ethernet). The current draw depends on system load and accessories connected to the system. 
# Power supplies
Very cheap power supplies can be found online these days. The switched-mode supply electronics is actually cheap. Unfortunately, all that glitters is not gold. We do not recommend buying bad quality power supplies. The main issues with cheap supplies are: they can have a very low life expectancy (bad capacitors, overheating), they can fail and burn your house or even kill you. All this is due to marginal savings in core design and components of the supply. You can read more about these issues elsewhere. 
The more relevant issue for powering boards is, the cheap supplies might not be able to sustain acceptable voltage levels as the system load increases. Typical phone/tablet chargers take advantage of the USB specification and often provide a tiny amount of over-voltage (>5.0V) within the spec limits (5.0V +/- 5%). This can compensate the voltage drop across the power cable and the internal voltage drop (inside the supply) due to increased load. If you run into hardware problems, a systematic way is to estimate the consumption, measure the provided voltage and current, and to replace the power supply in case it does not deliver enough power. 
You can also power the boards using USB host ports (routers, PC) and powered USB hubs. Non-powered (USB 2) hubs cannot provide enough power for development boards. Using the PC or router is usually a cheap and reliable choice for casual experimenting with the boards and a dedicated power supply is only needed for e.g. long term use or for using the embedded system independently. 
# Troubleshooting
If you run into more or less random hardware problems and suspect issues with the power supply, consider buying a cheap USB power meter online. Possible hardware problems include booting issues, lockups and resets, garbled UART output, disconnects, some devices not initializing. A larger power supply from a reliable brand might also help. 
## SATA
Boards with a [SATA][45693] port can only power 5V portable (laptop) drives. Low power laptop drives can use up to 1-4W when spinning up and 0.5-2W when idle. SSD drives use a lot less power. 
The bigger 3.5" drives typically require 12V DC instead of 5V (12V is also provided via another power pin) and will not work. You can however use them with the boards when powered externally with a SATA-DC/SATA Y-shaped cable. 
When using a board with a SATA port that can be powered via Micro USB, consider powering the board via [GPIO][45691]/other pins or powering the SATA disk separately. The board designers have been lazy and the power draw can easily exceed Micro USB charging specs and lead to failing drives, lockups and even corrupt your data. Also keep in mind that bad quality power (ripple) from the supply can damage the drive. If the board supports SATA multipliers or multiple SATA ports, staggered spin-up might help with the spiky power drain at spin-up, but such systems might need DIY switches due to the lack of support in the SATA controllers. 
  

# Power cables
Boards with a Micro USB power input can be used with standard USB cables that come with any device these days. However, please note that the wires in the cable are usually thin and of low quality (e.g. AWG 28, not copper). Long cables can have [significant voltage drop][45694]. This cable type is mostly ok for smaller devices, but may have issues powering the bigger boards, SATA disks, and demanding USB devices (e.g. WiFi, DVB tuners). For best results, consider buying AWG20 (or thicker) charging cables. CNXSoft has written [an article about choosing the right power cable][45695]. The article has a table of voltage drop with difference cable lengths and thicknesses. 
[![][45696]][45697]
[][45698]
Voltage drop of around 100mV over a 1.5m cable. Note that the drop is proportional to the current. The cheap power meter shows 5.2V when directly connected, but the reported current seems always way off.
# Power connectors
## Micro USB
In short, powering a device via USB can be a mess. There are multiple [USB Battery Charging Specification][45699] versions with different max current ratings (v1.0 1.5A, v1.1 1.8A, v1.2 5.0A), multiple charging modes (dedicated charger, host, sleep-and-charge ports etc), and also few proprietary solutions for signaling the current draw. Connectors are rated for at least 10 000 connect/disconnect cycles, but cheap 3rd party cables might fail a lot faster. The connectors have very thin pins that may not be able to deliver the rated current. One extra advantage of Micro USB is that in some cases you can not only power the board with USB, but also provide the system images & networking via FEL boot, network file systems, and the Linux kernel USB gadget functionality. 
## DC barrel plug (4.0mm/1.7mm, coaxial, centre positive)
This plug is the most common power plug along the Micro USB powered boards. The board vendors might sell compatible cables in their stores, but this cable is actually dirt cheap (< $1) and easily available online. Search for a 'PSP charger cable'. There are at least two versions, one with a USB model A connector, the other with two exposed wires at the other end. You can also solder the connector yourself, but the quality might not be as good. Note that the connector only connects to the two power pins in a USB cable so nothing can be assumed about the max power rating for a certain cable + power supply combo. As this cable might not be USB compliant, it might work best with a dumb charger which does not regulate the current based on the signals from the data pins. 
## Special connectors and GPIO pins
Some boards (e.g. the) supports [power supply boards][45700] with custom connectors. 
## POE (power over ethernet)
Some boards (e.g. [Xunlong Orange Pi Zero][45701]) have ethernet pins routed to solder pads for POE functionality. The board can be used as a POE connector/injector by directly connecting the DC input lines to routed ethernet pins (make sure the voltage is compatible and take into account possible voltage drop especially with longer wire lengths) or via a DC/DC converter. POE enables the use of network connected boards without a separate power cable. The mode of POE functionality provided by the Orange Pi Zero is dumb/passive POE -- instead of injecting power on the data lines, the technique uses dedicated power lines, which limits the network speed to 100 Mbps. When building such systems, keep in mind that the ethernet cables are not designed for transfering large currents, the power lines might interfere with normal network traffic, and there are state regulations for building high voltage systems. The passive POE standard (802.3af mode b) can be used as guidelines for designing POE setups: max power per device 12.95W, injector voltage range 44-57V, max current 350 mA, max cable resistance 20 ohm, max voltage drop 7V. 
[![][45702]][45703]
[][45704]
POE solder pads on a Orange Pi Zero
# Power consumption
The total power consumption of the system is a sum of the power used by the [SoC][45705], [RAM][45706], the on-board electronics (regulators, LEDs, flash, [ethernet][45707], [WiFi][45708], and other controllers), and the plugged accessories. 
The SoC and RAM power consumption varies depending on the load. The voltage and clock frequency go hand in hand and can be lowered to save power. The SoC and the onboard electronics may usually draw up to 1-2A. On the other hand, a low-end device with a small board and underclocked SoC may only draw 100mA when mostly idle. 
The USB power standard ratings for low and high power devices are 100/500mA for USB2 (most sunxi boards). For a board with 4 onboard USB host ports, that already adds up to 2A. Each interface (e.g. ethernet) needs some power for signaling. You can also draw some power from the GPIO pins (usually << 20 mA per data pins and << 100 mA from 3.3/5VDC pins, refer to the datasheets for detailed info). As it is easy to stress the pins too much, the current draw is usually limited by the on-board regulator and the power rails. Drawing too much power may damage the board permanently. 
# Measuring power
To get reliable results, it's often best to measure the devices yourself. For instance, the web is full of [unbelievable results][45709] for SBC boards which are hard to reproduce. 
## El cheapo power meters
You can find simple USB power meters online. The typical meters have one USB model A input and 1-2 outputs. There are at least two versions, one with voltage/current displays and a more compex one that can also measure the energy consumption over time. These meters can usually show if there are serious problems with voltage drop and provide a rough estimate of the power consumption. However, these are not scientific instruments. They might not be calibrated, heat might have an effect on the results, and the sampling rate is quite low. 
[![][45710]][45711]
[][45712]
Cheap ebay power meter
## Tunable / lab power supplies
There are cheap tunable power supplies and DC-DC converters with LED/LCD displays. The problem with those devices is that they can damage the boards with overvoltage as they are not especially designed for 5V devices. To avoid such problems, only change the voltage when no boards are plugged in. The good thing about these power supplies is that they can usually easily provide more than enough power for SBC development, for instance a $12 device might support up to 50-100W (with the help of an 12VDC power brick). 
## Odroid power meter
~~[The Odroid power meter][45713] is a relatively cheap, can measure energy consumption over time, provides tunable output voltage (3.00 -- 5.25V out, 12V DC in), and connects to a PC via USB for statistics.~~ (now sold out). It is generally safe to use. Also compared to the cheap ebay power meters, the reported values seem more reliable. Update: A [SmartPower2][45714] device is now available since the original was sold out. 
[![][45715]][45716]
[][45717]
Odroid power meter
## Instrument grade power sensors / oscilloscope
The instrument grade sensors are more expensive, but can be used to analyze the devices further, e.g. by eavesdropping communications via a side channel. One relatively cheap alternative is available via [tindie][45718]. 
# See also
  * [Usb made simple @ Armbian forums][45719]
  * [SBC consumption/performance comparisons @ Armbian forums][45720]
  * [Using A20 board with Armbian as 'powermeter' @ Armbian forums][45721]
  * <https://www.loverpi.com/blogs/news/93532993-canakit-2-5a-vs-loverpi-2a-power-adapter-comparison>
