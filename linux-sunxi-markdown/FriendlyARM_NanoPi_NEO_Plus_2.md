# FriendlyARM NanoPi NEO Plus 2
FriendlyARM NanoPi NEO Plus 2  
---  
[![NanoPi NEO Plus2 top.jpg][21258]][21259]  
Manufacturer |  [FriendlyARM][21260]  
Dimensions |  52 _mm_ x 40 _mm_  
Release Date |  Month year  
Website |  [Device Product Page][21261]  
Specifications   
SoC |  [H5][21262] @ XGhz   
DRAM |  1GiB DDR3 @ xxxMHz   
NAND |  8 GB   
Power |  DC 5V @ 2A via microUSB or pin headers   
Features   
Audio |  Line IN and Line OUT via headers, I2S.   
Network |  WiFi 802.11 b/g/n ([Manufacturer device][21263]), 10/100/1000Mbps Ethernet ([Manufacturer device][21264])   
Storage |  eMMC, µSD.   
USB |  2x USB2.0 Type A also avaiable on pin header, 1x OTG µUSB   
This page needs to be properly filled according to the [New Device Howto][21265] and the [New Device Page guide][21266].
NanoPi NEO Plus 2 is a H5 based small form-factor development boards produced by FriendlyARM. It has pretty much the same form factor than the NanoPi NEO2 but much features, The NEO Plus 2 comes with integrated 1000 Mbps Ethernet, 2 x USB A 2.0, and a micro-SD card slot, 1 GiB DDR3 and 8 GiB of eMMC. 
## Contents
  * [1 Identification][21267]
  * [2 Sunxi support][21268]
    * [2.1 Current status][21269]
    * [2.2 BSP][21270]
    * [2.3 Manual build][21271]
      * [2.3.1 U-Boot][21272]
        * [2.3.1.1 Mainline U-Boot][21273]
      * [2.3.2 Linux Kernel][21274]
        * [2.3.2.1 Sunxi/Legacy Kernel][21275]
        * [2.3.2.2 Mainline kernel][21276]
  * [3 Tips, Tricks, Caveats][21277]
    * [3.1 FEL mode][21278]
  * [4 Locating the UART][21279]
  * [5 Pictures][21280]
  * [6 See also][21281]
    * [6.1 Manufacturer images][21282]

# Identification
The PCB has the following silkscreened on it: 
[code] 
    V2.0 1907
    NanoPi NEO Plus2
[/code]
# Sunxi support
## Current status
The H5 SoC support has matured since its introduction in kernel 4.12. Most of the board functionality for boards such as FriendlyARM NanoPi NEO Plus2, including 3D graphics, hardware accelerated video and crypto, and DVFS are available with current mainline kernels. Only a very few minor features are still being worked on. For a more comprehensive list of supported features, see the [status matrix for mainline kernels][21283]. 
See the [Manual build][21271] section for more details. 
  

## BSP
## Manual build
You can build things for yourself by following our [Manual build howto][21284] and by choosing from the configurations available below. 
### U-Boot
#### Mainline U-Boot
Use the **nanopi_neo_plus2_defconfig** (supported since v2018.01) build target. 
### Linux Kernel
#### Sunxi/Legacy Kernel
#### Mainline kernel
The H5 SoC has support in the [mainline kernels][21285]. 
The development process, links to patches and links to kernel fork repositories are listed on the [ Linux mainlining effort][21285] page. Patches can also be found from the arm-linux mailing list. 
Repositories with H5 patches: 
  * [Ondřej Jirman's branch for H5 based orange Pi (kernel 4.19)][21286] (work-in-progress DVFS) 
    * Thermal regulation (if CPU heats above certain temperature, it will try to cool itself down by reducing CPU frequency)
    * HDMI audio support (from Jernej Skrabec)
    * Configure on-board micro-switches to perform system power off function
    * Wireguard (<https://www.wireguard.com/>)

  
Use the **sun50i-h5-nanopi-neo-plus2.dtb** device-tree binary. 
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The something button triggers [ FEL mode][21287]. 
# Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][21288].
# Pictures
  * [![NanoPi NEO Plus2 front.jpg][21289]][21290]
  * [![NanoPi NEO Plus2 back.jpg][21291]][21292]
  * [![NanoPi NEO Plus2 top.jpg][21293]][21259]
  * [![NanoPi NEO Plus2 bottom.jpg][21294]][21295]

# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
See the manufacturer's device pages above since links change from time to time.
