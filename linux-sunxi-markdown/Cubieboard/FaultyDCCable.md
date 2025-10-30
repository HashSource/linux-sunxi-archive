# Cubieboard/FaultyDCCable
< [Cubieboard][13877]
 
## Contents
  * [1 Booting with faulty DC cable][13880]
    * [1.1 Case 1 - Red blink][13881]
    * [1.2 Case 2 - Runs for a bit][13882]
    * [1.3 Case 3 - Runs for several minutes][13883]
  * [2 Booting with USB cable][13884]

## Booting with faulty DC cable
Some of the Cubieboards that were sent through the Indiegogo campaign, were delivered with faulty USB-DC cables. In this page we describe how to diagnose if you have one of those cables. In any case, you can still power your Cubieboard by using any standard USB to miniUSB cable. 
If your Cubieboard is not from Indiegogo campaign but is unstable too, like non working continuously for 24-72h without crashes, firstly, check if the power cable is not doing this problem. Move gently the cable on the usb side and see if the power led is shutting down or if the cubieboard is crashing. 
Please note that the green LED is programmable; depending on which Android or Linux image you use, it may lit up or not. The pre-installed Android image from the Indiegogo orders does lit up the green LED. 
The following three cases were exhibited with the **same** USB-DC cable. 
### Case 1 - Red blink
When you power your Cubieboard, the red LED blinks for a split second, and no activity. The Cubieboard does not finish booting. 
See <http://www.youtube.com/watch?v=k4Eq5tBUsRg>
### Case 2 - Runs for a bit
When you power your Cubieboard, it runs for a few seconds and then it dies. The Cubieboard does not finish booting. 
See <http://www.youtube.com/watch?v=sv9dtr4KmZA>
### Case 3 - Runs for several minutes
It appears it works well. In this video, it strangely works. What we must do is try to power the Cubieboard a few times in order to verify that it boots reliably. 
See <http://www.youtube.com/watch?v=l-pdXCBmtq4>
## Booting with USB cable
Here the Cubieboard boots with a USB cable (USB to mini USB), powered from a computer (5V/500mA). At start up, first the red LED lights up, then the green (programmable) LED lights up. There is a slight delay between the two LEDs. Apparently, this is normal. 
See <http://www.youtube.com/watch?v=0-O0JPPbYeo>
