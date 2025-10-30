# Anichips PhoenixA20/Headers
< [Anichips PhoenixA20][7683]
 
The Anichips PhoenixA20 board has four 2.00mm pitch headers. These are labelled [UART][7686], digital, analogue and LCD. The information here has been pulled from an inspection of the board, the [PhoenixA20 schematics][7687] and the [Allwinner A20 User Manual][7688]. 
  
A number of pins are controlled through the Allwinner A20 port controller. These pins are shown as (P _xn_) in the diagrams below, where _x_ is the port identifier (A through to S) and _n_ is the pin number. By [modifying a FEX file][7689] for a sunxi 3.4 Linux kernel or a DTS file for a mainline Linux kernel the use of the port can be modified. For example the LCD pins can be re-purposed as a LVDS video interface. If port controlled pins are unused they can be set up as [general purpose input/output (GPIO)][7690], with the LCD connector this gives a potential 28 GPIO pins. The Allwinner A20 User Manual provides mappings between pin and purpose. 
  

## Contents
  * [1 UART Header][7691]
  * [2 Digital Header][7692]
  * [3 Analogue Header][7693]
  * [4 LCD Header][7694]

# UART Header
This header provides access to UART0 and can be used for [debugging][7686]. 
[![Phoenixa20 pinout-uart0.png][7695]][7696]
# Digital Header
The digital header mainly provides three additional UART interfaces and two [I2C interfaces][7697]. 
  
On the board pins are also labelled for [Inter-IC Sound (I2S)][7698], but the schematics show these pins are used to carry Bluetooth PCM audio between the AP6210 and A20 audio system. One of the I2S labelled pins (PB9) is used as a USB power switch. This leaves two pins (PB10 and PB11) unused and these could be configured as GPIO for a [1-wire interface][7699]. For anyone interested in I2S this post, [CUBIEBOARD FOR AUDIO?][7700], that discusses the CubieTruck may be a starting point. 
  
The UART interfaces are numbered 3,4 and 5 and this corresponds to the numbers used on the A20 SOC. UART0 is exposed on a separate header shown above, UART1 is not available as the pins are used for the Ethernet MAC controller and UART2 is connected to the Bluetooth chip of the AP6210. The numbers exposed in the Linux user space will be different because UART1 is not available. 
[![Phoenixa20 pinout-digital.png][7701]][7702]
# Analogue Header
The analogue header mainly provides audio, human input and video interfaces. The header also has the power enable and reset pins for the power management unit. 
  
For audio there are pins for: 
  * Mono microphone
  * Stereo line level input
  * Stereo auxiliary input (marked as from an auxiliary FM tuner, there is no FM tuner on the A20 SOC)
  * Stereo headphones
  * SPDIF output

  
For human input there are pins for: 
  * Resistive touchpanel
  * Two low resolution ADCs (6bit, 0-2V) usually used for buttons
  * Infra-red receiver, confusingly the schematic shows the pin wired to IR-RX(PB4) but labels the pin on the connector as IR-OUT.

  
For video there are pins for: 
  * Composite video out
  * TV in, these are undocumented for Allwinner SOCs so are effectively useless

  
There are also two [Pulse Width Modulation pins (PWM)][7703] that could be used for controlling LED brightness or a stepper motor. 
Very few of the pins are part of the port controller so most cannot be re-purposed as GPIO pins. 
[![Phoenixa20 pinout-analogue.png][7704]][7705]
# LCD Header
The LCD header could be re-purposed as a 28 pin GPIO header. The A20 User Manual also shows the pins could be re-purposed for LVDS video connector. 
[![Phoenixa20 pinout-lcd.png][7706]][7707]
