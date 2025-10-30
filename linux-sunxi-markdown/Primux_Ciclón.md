# Primux Ciclón
Primux Ciclón  
---  
Manufacturer |  [Primux][46015]  
Dimensions |  242 x 189 x 8   
Release Date |  01/01/2012   
Website |  [TABLET PRIMUX CICLÓN (9,7")][46016]  
Specifications   
SoC |  [A10][46017] @ 1 Ghz   
DRAM |  1GiB DDR3   
NAND |  4 GB   
Power |  DC 5V @ 2A, 8000mAh/3.7V Polymer Lithium   
Features   
LCD |  9,7" 1024:768   
Touchscreen |  IPS Capcitive touchscreen   
Video |  Mini HDMI,type C(1080p and 720p supported)   
Audio |  3.5mm headphone   
Network |  WiFi 802.11 b/g/n   
Storage |  µSD   
USB |  1 USB2.0 Host   
Camera |  2 MP front, 0.3 MP rear   
Other |  Accelerometer ([bosch][46018])   
  

## Contents
  * [1 Identification][46019]
  * [2 Sunxi support][46020]
    * [2.1 Current status][46021]
    * [2.2 Images][46022]
      * [2.2.1 U-Boot][46023]
        * [2.2.1.1 Sunxi/Legacy U-Boot][46024]
        * [2.2.1.2 Mainline U-Boot][46025]
      * [2.2.2 Linux Kernel][46026]
        * [2.2.2.1 Sunxi/Legacy Kernel][46027]
        * [2.2.2.2 Mainline kernel][46028]
  * [3 Tips, Tricks, Caveats][46029]
    * [3.1 FEL mode][46030]
  * [4 Adding a serial port (**voids warranty**)][46031]
    * [4.1 Device disassembly][46032]
    * [4.2 Locating the UART][46033]
  * [5 Pictures][46034]
  * [6 Also known as][46035]
  * [7 See also][46036]
    * [7.1 Manufacturer images][46037]

# Identification
On the back of the device, the following is printed: 
[code] 
    Primux Tech
    Ciclón
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: MID9106CM
  * Build Number: 03F2-P1-H2-M01-*.*
  * Fingerprint: iNet/crane_inet/cranet-inet:4.0.4/IMM76D/20120808:eng/test-keys

# Sunxi support
Supported 
## Current status
The device is not maintained by provider. 
## Images
[Ciclón Firmware Android 4.0.4][46038]
### U-Boot
#### Sunxi/Legacy U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
#### Mainline U-Boot
Use the _MANUFACTURER_DEVICE_ build target. 
### Linux Kernel
3.0.8 
#### Sunxi/Legacy Kernel
Use the [primux_ciclon.fex][46039] file. 
#### Mainline kernel
Use the _FAMILY-CHIP-DEVICE.dtb_ device-tree binary. 
# Tips, Tricks, Caveats
Image zip contains LiveSuit 1.07 to flash/upgrade the device. You can use PhoenixSuit 1.07 too. 
## FEL mode
To trigger [ FEL mode][46040] shutdown the device, press Vol +, connect to your computer and push 3 times power button . 
# Adding a serial port (**voids warranty**)
## Device disassembly
## Locating the UART
# Pictures
# Also known as
# See also
## Manufacturer images
