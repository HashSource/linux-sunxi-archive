# Ethernet
## Contents
  * [1 Configuration][18158]
    * [1.1 MAC address][18159]
      * [1.1.1 Mainline U-Boot based systems][18160]
      * [1.1.2 Legacy systems][18161]
        * [1.1.2.1 Through script.bin][18162]
        * [1.1.2.2 U-boot][18163]
        * [1.1.2.3 Through ifconfig][18164]
  * [2 Hardware][18165]
    * [2.1 EMAC][18166]
      * [2.1.1 Mainline Kernel driver][18167]
    * [2.2 GMAC][18168]
      * [2.2.1 Mainline Kernel driver][18169]
    * [2.3 sun8i EMAC][18170]
    * [2.4 Phyceivers][18171]
      * [2.4.1 Broadcom BCM53125][18172]
      * [2.4.2 ICplus IP101A][18173]
      * [2.4.3 ICplus IP101GA][18174]
      * [2.4.4 Microchip LAN8710A][18175]
      * [2.4.5 Micrel KSZ9031][18176]
      * [2.4.6 Realtek RTL8201CP][18177]
      * [2.4.7 Realtek RTL8211E][18178]
      * [2.4.8 Realtek RTL8211CL][18179]
  * [3 Devices][18180]

# Configuration
## MAC address
### Mainline U-Boot based systems
On mainline U-Boot based firmware, the MAC address will be generated at boot time, based on the unique serial number stored in the SID efuse device. It will be the same on every boot, and should be rather unique, within the limits of the [hashing algorithm][18181]. 
To trigger the routine, the DTB passed on to the kernel (which can also be U-Boot's own DT) must have an `ethernet0` alias in the `/aliases` DT node: 
[code] 
       aliases {
           ethernet0 = &emac;
           ethernet1 = &rtl8189etv;
       };
    
[/code]
Mainline DTs should already have this alias. Up to 4 MAC addresses will be assigned, if needed. The code will insert a `local-mac-address` and `mac-address` property into the DT node that the alias points to. This [standard DT property][18182] will then be picked up by any OS automatically. 
Despite the alias having the name _ethernet_ , this works and is needed for WiFi devices in the same way. 
Aside from making sure that the DT has the alias, there is no user intervention necessary, and a unique and stable MAC address should be assigned out of the box. 
### Legacy systems
By default both EMAC and GMAC use random MAC addresses that change with each reboot, but this can be fixed. 
The Bash script below will generate a unicast, locally administered, random MAC address. The first octet has bit 0 unset for unicast and bit 1 set for local administration so will be either `X2`, `X6`, `Xa` or `Xe`: 
[code] 
    printf "%02x" $((RANDOM%256 & 254 | 2));hexdump -n 5 -e '""5/1 ":%02x""\n"' /dev/urandom
    
[/code]
This MAC address can be loaded on each boot using one of the methods below to give a static MAC address. 
For alternative sources of MAC addresses the FAQ [14.2.14. Where Can I Get a Valid MAC Address from?][18183] at the U-Boot website may help. 
#### Through script.bin
the [Allwinner][18184] way, adding the value to your [script.bin][18185]
[code] 
    [dynamic]
    MAC = "XXXXXXXXXXXX"
    
[/code]
#### U-boot
the [bootloader][18186] to append `mac_addr=XX:XX:XX:XX:XX:XX`
#### Through ifconfig
[code] 
    ifconfig eth0 hw ether XX:XX:XX:XX:XX:XX
[/code]
# Hardware
In contrast to combined network chips used in the modern PC world, embedded SoCs split the network adapter functionality into two components: 
  * a [MAC][18187] device, fully integrated into the SoC, which deals with the actual packet handling and is driven by DMA and interrupts. It is also responsible for the timing. Its output is typically using one of multiple variants of the [MII][18188] interface, which connects it to:

  * a [PHY][18189] chip, commonly found as an extra chip on the board. This converts the logic levels of the *MII interface into the electrical domain of the Ethernet cable, and deals with the properties of the physical layer, like link and collision detection. Some Allwinner SoCs (like [H3][18190], [H5][18191], [H6][18192], [H616][18193]) contain a 100MBit/s Ethernet PHY on the same package, this is commonly used on cheap boards to save the cost of the extra PHY component.

## EMAC
[Allwinner][18184]'s [A10][18194], [A20][18195] and [F20][18196] [SoCs][18197] include a MAC unit called **EMAC** , but it's usable on very few [devices][18198], most notably the [Mele A1000, A2000 and A100][18199] HTPC and the [Cubieboard][18200]. Due to driver similarities it's believed to be based on **DM9000**. 
### Mainline Kernel driver
The EMAC driver can be found under "Ethernet driver support", "Allwinner devices", "Allwinner A10 EMAC support". It was [merged for kernel 3.11][18201]. 
## GMAC
[Allwinner][18184]'s [A20][18195], [A31/A31s][18202] and the [A80][18203] contain a MAC unit called **GMAC** ("Gigabit MAC"). The controller supports MII and RGMII modes. On the [A20][18195] it is pin compatible with the [ EMAC][18204] in MII mode. Also on A20 the manufacturer of the device in question can decide whether to use EMAC or GMAC. The controller is an early version of the Synopsys DWMAC (DesignWare MAC), with some hardware specific glue. 
The SoC's GMAC is always combined with an external [PHY][18205], in most cases a RTL8211E/CL (the [Lamobo R1][18206] uses the [Broadcom BCM53125][18207] switch IC instead). Important: In this special mode the RTL8211 chip is just used as PHY and only responsible for layer 1 operations, since everything else happens inside the SoC's GMAC (therefore no RealTek drivers are needed and some functionality differs, e.g. no [WoL][18208] possible). 
[![Information.png][18209]][18210] For reliable Gigabit networking (1000Mbit operation), several sunxi devices require an important tweak that adjusts the relative timing of the clock and data signals to the PHY, in order to compensate for differing trace lengths on the PCB ([details][18211]). Among others, this includes [Banana Pi][18212]/[Pro][18213], [Cubietruck][18214], [Lamobo R1][18206], [pcDuino3 Nano][18215] and [Orange Pi][18216]/[Mini][18217]. Recent [mainline U-Boot][18218] uses _CONFIG_GMAC_TX_DELAY_ to initialize these devices accordingly. If a necessary GMAC TX delay isn't set, then GBit Ethernet operation might be unreliable or won't work at all. 10/100 Mbit/sec negotiation is unaffected, so misconfigured devices could actually work (faster) when connected to a Fast Ethernet port instead of a GBit Ethernet port. 
### Mainline Kernel driver
DWMAC is supported by the _stmmac_ driver ("Ethernet driver support", "STMicroelectronics devices", "STMicroelectronics 10/100/1000 Ethernet driver", "STMMAC Platform bus support"). Platform glue for sunxi was merged in 3.14. Device tree patches for supported A20 devices were merged in 3.15. 
## sun8i EMAC
Ethernet in the [A83T][18219]/[H3][18190]/[A64][18220] and later SoCs is handled by the newer [Sun8i_emac][18221] MAC. It is another variant of the Designware MAC, with a changed register interface, and is handled in Linux by the _sun8i_emac_ driver, part of the _stmmac_ driver framework: 
[code] 
       -> Device Drivers
         -> Network device support
           -> Ethernet driver support
             -> STMicroelectronics devices
               -> STMicroelectronics Multi-Gigabit Ethernet driver
                 -> STMMAC Platform bus support (STMMAC_PLATFORM)
                   -> Allwinner sun8i GMAC support (DWMAC_SUN8I)
    
[/code]
## Phyceivers
### Broadcom BCM53125
The [Broadcom BCM53125][18222] is an integrated 7-port Gbit Ethernet switch IC that can be configured to act as a PHY on one port interconnecting the SoC with all wired Ethernet ports. It works with OpenWrt's b53-mdio driver, and the capability to route packets between different ports is based on VLANs and assigning them to virtual interfaces. At least the implementation on the [Lamobo R1][18206] suffers from less possible throughput compared to A20's GMAC working together with [RTL8211][18178] as PHY. 
### ICplus IP101A
The ICplus IP101A is a RMII 10/100 Ethernet PHY. 
### ICplus IP101GA
The ICplus IP101GA is a RMII 10/100 Ethernet PHY. 
### Microchip LAN8710A
### Micrel KSZ9031
The KSZ9031 is a gigabit ethernet PHY. 
It may require adjusting RX or TX delays, depending on PCB wiring of each board. According to [git commit notes for the linux driver][18223], TX delay can be 0 - 1.38ns and RX delay can be 0 - 2.58ns. 
The PHY is used on newer revisions of the [ Olimex Lime2][18224], where the board makers found [ a TX_DELAY=4 in u-boot][18225] suitable. 
### Realtek RTL8201CP
The Realtek RTL8201CP is a MII mode 10/100 Ethernet PHY. It is very very common and supported by just about any kernel out there, either with the generic phy driver or the realtek one. 
[Oliver][18226] broke his [PHY][18227] and ended up replacing it with another one. Here are some pictures. 
  * [![Tapeitup 01.JPG][18228]][18229]
  * [![Tapeitup 02.JPG][18230]][18231]
  * [![Addfoil 01.JPG][18232]][18233]
  * [![Addfoil 02.JPG][18234]][18235]
  * [![Suckit 01.JPG][18236]][18237]
  * [![Cleanit 01.JPG][18238]][18239]
  * [![Rtl replaced.JPG][18240]][18241]

### Realtek RTL8211E
The Realtek RTL8211E is a RGMII 10/100/1000 Ethernet PHY, which is gigabit capable. It is commonly paired with GMAC for gigabit speeds. Generic PHY support is enough to make it work. 
### Realtek RTL8211CL
The RTL8211 is known to have trouble connecting to certain types of devices. The problem is caused by an instable PLL when configured as master. A fix has been applied to u-boot. <http://lists.denx.de/pipermail/u-boot/2016-March/249734.html>
# Devices
The following devices all come with an ethernet port. 
[10moons LT390W][18242]
[Allwinner A83TDevBoard][18243]
[Allwinner Nezha][18244]
[Allwinner R329 EVB5 Development Board][18245]
[Anichips PhoenixA20][18246]
[Beelink GS1][18247]
[Beelink X2][18248]
[Biqu BTT Pi][18249]
[Biqu CB1][18250]
[CherryPi PC H6][18251]
[CherryPi PC V3S][18252]
[CherryPi PC V7][18253]
[CS918S][18254]
[Cubietech Cubieboard][18255]
[Cubietech Cubieboard2][18256]
[Cubietech Cubieboard4][18257]
[Cubietech Cubietruck][18214]
[Cubietech Cubietruck Plus][18258]
[Eachlink H6 Mini][18259]
[Eearl H1026A][18260]
[Foxconn Super Pi][18261]
[FriendlyARM NanoPi A64][18262]
[FriendlyARM NanoPi K1 Plus][18263]
[FriendlyARM NanoPi M1][18264]
[FriendlyARM NanoPi NEO & AIR][18265]
[FriendlyARM NanoPi NEO Plus 2][18266]
[FriendlyARM NanoPi NEO2][18267]
[FriendlyElec NanoPi R1][18268]
[HYH-TBH3][18269]
[In-Circuit ICnova A20][18270]
[Itead Iteaduino Plus][18271]
[Jesurun Q5][18272]
[Jide Remix Mini][18273]
[Kickpi K2B H618][18274]
[Lamobo R1][18206]
[Langcent h6s][18275]
[LeMaker Banana Pi][18276]
[LeMaker Banana Pro][18277]
[Libre Computer Board ALL-H3-CC][18278]
[LinkSprite pcDuino][18279]
[LinkSprite pcDuino Lite][18280]
[LinkSprite pcDuino2][18281]
[LinkSprite pcDuino3][18282]
[LinkSprite pcDuino3 Nano][18215]
[LinkSprite pcDuino8 Uno][18283]
[MarsBoard A10][18284]
[MarsBoard A20][18285]
[MarsBoard A20-SOM][18286]
[Mele A1000][18199]
[Mele A100Dual Core][18287]
[Mele I7][18288]
[Mele M3][18289]
[Mele M5][18290]
[Mele M6][18291]
[Merrii A80 Optimus Board][18292]
[Merrii Hummingbird A20][18293]
[Merrii Hummingbird A31][18294]
[Miniand Hackberry][18295]
[Mixtile LOFT-Q][18296]
[MXQ-4K][18297]
[NetCube Systems Kumquat][18298]
[NetCube Systems Nagami][18299]
[Olimex A10-OLinuXino-Lime][18300]
[Olimex A10s-OLinuXino-Micro][18301]
[Olimex A20-OLinuXino-Lime][18302]
[Olimex A20-OLinuXino-Lime2][18224]
[Olimex A20-OLinuXino-Micro][18303]
[Olimex A20-SOM][18304]
[Olimex A64-OLinuXino][18305]
[Pcduino8 A80 Board][18306]
[Pine64-LTS][18307]
[PineH64][18308]
[Radxa Cubie A5E][18309]
[Radxa Cubie A7A][18310]
[Rongpin RP-H6B][18311]
[Semitime Qt840a][18312]
[Sinlinx SinA31s][18313]
[Sinlinx SinA83T][18314]
[Sinovoip Banana Pi BPI-6204][18315]
[Sinovoip Banana Pi M2][18316]
[Sinovoip Banana Pi M2 Berry][18317]
[Sinovoip Banana Pi M2 Ultra][18318]
[Sinovoip Banana Pi M2+][18319]
[Sinovoip Banana Pi M3][18320]
[Sinovoip Banana Pi M4 Berry][18321]
[Sinovoip Banana Pi M64][18322]
[Sunchip CX-A99][18323]
[Sunchip SDK-758][18324]
[Sunvell R69][18325]
[T95][18326]
[T95H][18327]
[Tanix TX6][18328]
[Tanix TX6s][18329]
[TQC A01][18330]
[TXCZ A20][18331]
[VidOn Box][18332]
[Whatsminer CB4 v10][18333]
[X96 Mate][18334]
[X96QPro][18335]
[Xunlong Orange Pi][18216]
[Xunlong Orange Pi 2][18336]
[Xunlong Orange Pi 3][18337]
[Xunlong Orange Pi 3 LTS][18338]
[Xunlong Orange Pi 4A][18339]
[Xunlong Orange Pi Lite 2][18340]
[Xunlong Orange Pi Mini][18217]
[Xunlong Orange Pi Mini 2][18341]
[Xunlong Orange Pi One][18342]
[Xunlong Orange Pi One Plus][18343]
[Xunlong Orange Pi PC][18344]
[Xunlong Orange Pi PC 2][18345]
[Xunlong Orange Pi Plus][18346]
[Xunlong Orange Pi Plus 2][18347]
[Xunlong Orange Pi Plus 2E][18348]
[Xunlong Orange Pi Prime][18349]
[Xunlong Orange Pi Win][18350]
[Xunlong Orange Pi Zero][18351]
[Xunlong Orange Pi Zero Plus][18352]
[Xunlong Orange Pi Zero2][18353]
[Xunlong Orange Pi Zero3][18354]
[YBKJ A20][18355]
[YBKJ A20 JN][18356]
[YuzukiHD Avaota A1][18357]
