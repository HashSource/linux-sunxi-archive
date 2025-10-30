# Nextbook Ares 10a
Nextbook Ares 10a  
---  
[![Ares10a-Board.jpg][39798]][39799]  
Manufacturer |  [Nextbook]   
Release Date |  2017  
Website |  [Nextbook Website seemingly Dead]   
Specifications   
SoC |  [A64][39800] @ 1.3Ghz   
DRAM |  1GiB DDR3(L) @ ??MHz   
NAND |  32GB (28.906 Gb actual)   
Power |  DC 5V @ 2A, 4000mAh 3.8V Li-Ion battery   
Features   
LCD |  1280 x 800; DPI: 160   
Touchscreen |  5-finger capacitive   
Video |  Mali-400 MP; ARM; OpenGL ES-CM 1.1; OpenGL ES 2.0   
Audio |  3.5mm headphone plug, internal stereo speakers   
Network |  WiFi RTL8723CS, Ethernet Realtek 8150 based adapters   
Storage |  32Gb Flash, 128Gb SD Slot   
USB |  1 USB2.0 Host/OTG   
Camera |  1.9MP (1600x1200) front, 1.9MP (1600x1200) rear   
Other |  Bosch 3-axis Accelerometer, GPS, Bluetooth   
Headers |  UART(?), LCD   
This page needs to be properly filled according to the [New Device Howto][39801] and the [New Device Page guide][39802].
## Contents
  * [1 So Far][39803]
  * [2 Identification][39804]
  * [3 Sunxi support][39805]
  * [4 FEL Mode][39806]

# So Far
I've struggled to get this tablet going with lacking information around the innernet, however while writing this page, I'm finding more and more that this device is very close to the Pine64. Still searching! Specs found here: <http://specdevice.com/showspec.php?id=4b25-967f-0033-c5870033c587>
# Identification
At the bottom of the board is printed **AW02_V1.2** **2017/08/16**
Model Number: **NX16A10132SPS** Build Number: **tulip_p3-user 7.1.1 N9F27C 20171123 test-keys**
# Sunxi support
Responds well to all Suxni-tool as far as I can tell. 
# FEL Mode
1.) Hold VolUp+PWR - few sec. 2.) Release PWR - couple sec. 3.) Press PWR - Repeatedly - couple sec. 4.) Hold PWR - few sec. 5.) Release PWR. 6.) Release VolUp. (Note - VolUp is held until last step but the rest does not have to be exact.)
