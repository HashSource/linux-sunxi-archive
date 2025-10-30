# Mele I7
Mele I7  
---  
[![Mele I7.JPG][36982]][36983]  
Manufacturer |  [Mele][36984]  
Dimensions |  158 _mm_ x 104 _mm_ x 38 _mm_  
Release Date |  July 2014   
Website |  [Mele I7 Product Page][36985]  
Specifications   
SoC |  [A31][36986] @ 1 GHz   
DRAM |  1GiB DDR3 @ 312 MHz (4x [H5TQ2G63DFR-PBC][36987])   
NAND |  8GB   
Power |  DC 5V @ 2A   
Features   
Video |  HDMI (Type A - full)   
Audio |  3.5 mm headphone plug, HDMI, SPDIF   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8188ETV][36988]), 10/100Mbps Ethernet ([Realtek RTL8201CP][36989])   
Storage |  Full-size SD   
USB |  3 x USB 2.0 Host, 1 x USB 2.0 OTG   
Other |  IRDA   
Headers |  UART   
The Mele I7 is an [A31][36986] based HTPC housed in the case of the [Mele A2000][36990]. 
## Contents
  * [1 Identification][36991]
  * [2 Sunxi support][36992]
    * [2.1 Current status][36993]
    * [2.2 Images][36994]
    * [2.3 HW-Pack][36995]
    * [2.4 BSP][36996]
    * [2.5 Manual build][36997]
    * [2.6 Mainline kernel][36998]
  * [3 Tips, Tricks, Caveats][36999]
    * [3.1 FEL mode][37000]
    * [3.2 Android ADB access][37001]
    * [3.3 Adding a eMMC/SD slot][37002]
  * [4 Adding a serial port][37003]
    * [4.1 Device disassembly][37004]
    * [4.2 Locating the UART][37005]
  * [5 Pictures][37006]
  * [6 Also known as][37007]
  * [7 See also][37008]
    * [7.1 Manufacturer images][37009]

# Identification
On the connector side of the device, the follow text can be read: 
  * _迈乐魔盒 (客厅电脑)_ (meaning "Mele magic box (living room computer)")
  * _型号: I7_ (型号 means "model")
  * _www.mele.cn_
  * _Designed by mele_

In android, under Settings->About Device, you will find: 
  * Model Number: MeLE I7
  * Build Number: CHOA-V1.0.3

# Sunxi support
## Current status
Like all [A31][36986] devices, the Mele I7 is not supported by our [sunxi u-boot][37010] and [sunxi kernel][37011], but it is supported by Mainline U-Boot and Mainline Kernel(partly), so we hope to provide [an A31 specific Manual build howto][37012] soon. 
## Images
## HW-Pack
## BSP
## Manual build
  * For building u-boot, use the Mele I7 target (make Mele_I7_defconfig). [the memory register dump can be found in our sunxi-boards repository][37013].
  * The .fex file can be found in sunxi-boards as [mele_i7.fex][37014]

Further instructions will be available soon in our [A31 Manual build howto][37012]. 
## Mainline kernel
Use the _sun6i-a31-i7.dts_ device-tree file for the [mainline kernel][37015]. 
[![][37016]][37017]
[][37018]
Mele i7 Fel button Hole.
[![][37019]][37020]
[][37021]
Mele i7 Fel button.
# Tips, Tricks, Caveats
## FEL mode
There is a FEL button available through a hole on the bottom of the device that can be used to trigger [ FEL mode][37022]. Connect via the OTG with no power to the board. 
## Android ADB access
Standard ADB does not work out of the box. You need to add the vendor id **0x18d1** to [the adb usb config file][37023]. Attach via the OTG connector. 
## Adding a eMMC/SD slot
[![FORESEE TSDPinout.png][37024]][37025]
As you can see in this pinout, the Mele I7 has a complex-NAND mounter. A typical NAND flash can be soldered on it. You can also solder a SD_SLOT or a eMMC/tSD flash on it. 
If you don't want to be trapped on the bad A31 MTD NAND flash driver, you can simply let the NAND out, and solder or wire a eMMC flash on it. 
This is a Mele i7 with a Sandisk 4GB eMMC on it. But it won't boot from the eMMC flash. 
The BootSelect Jumper is realized by two resistors on the bottom of the PCB which are marked 9R16 and 9R17. 
[![Melei7Bootjumper.jpg][37026]][37027]
[][37028]
By setting this jumper to one of the following values you can get difference devices to boot: 
9R16 | 9R17 | Action   
---|---|---  
NC | NC | Boot from NAND   
NC | 0R | Boot from 4-bit eMMC/SD   
0R | NC | Boot from 8-bit eMMC   
0R | 0R | Boot from SPI Flash which is on the north of the A31   
[![Melei7withSandisk4GBeMMC.jpg][37029]][37030]
[][37031]
# Adding a serial port
[![][37032]][37033]
[][37034]
Mele I7 UART connector
## Device disassembly
Unscrew the two screws on the rear of the device and the four screws on the base. The case then slides off. 
## Locating the UART
The Mele I7 has a 4 pin 2.0 pitch JST-PH connector available for its UART0 port. This is the same as some 90s analog audio cables which ran from a CDROM to the sound card. More information is available at [our UART howto][37035]. 
# Pictures
  * [![Mele I7 Front.JPG][37036]][37037]
  * [![Mele I7 Rear.JPG][37038]][37039]
  * [![Mele I7 Top.JPG][37040]][37041]
  * [![Mele I7 LeftSide.JPG][37042]][37043]
  * [![Mele I7 RightSide.JPG][37044]][37045]
  * [![Mele I7 PCB.JPG][37046]][37047]
  * [![Mele I7 PCB Rear.JPG][37048]][37049]

# Also known as
# See also
  * [Mele M9][37050]: A 2GiB RAM 16GiB ROM HTPC from the same company using the same SOC. Comes in a newer style case.
  * [Mele A1000G Quad][37051]: A 2GiB RAM 16GiB ROM HTPC from the same company using the same SOC.
  * [Mele A2000][36990]: The original Mele with this case design.

## Manufacturer images
  * [CH0A-V1.0.5][37052]
