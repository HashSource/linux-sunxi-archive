# USB Gadget/Ethernet
< [USB Gadget][57146]
 
## Contents
  * [1 USB Ethernet support][57149]
    * [1.1 Kernel support][57150]
      * [1.1.1 Mainline kernel (via configfs)][57151]
      * [1.1.2 Mainline kernel (via Precomposed Configurations)][57152]
      * [1.1.3 sunxi-3.4][57153]
    * [1.2 Loading the driver (on the device)][57154]
      * [1.2.1 configfs][57155]
      * [1.2.2 Precomposed Configurations][57156]
    * [1.3 Configuring the gadget under configfs][57157]
    * [1.4 Configuring the device's networking][57158]
      * [1.4.1 Ubuntu/Debian][57159]
        * [1.4.1.1 Without network manager][57160]
    * [1.5 Setting up the host][57161]
    * [1.6 See also][57162]

# USB Ethernet support
This allows ethernet emulation over USB, allowing for all sorts of nifty things like SSH and NFS in one go plus charging over the same wire, at higher speeds than most Wifi connections. 
## Kernel support
### Mainline kernel (via configfs)
The configfs approach allows you to configure the device dynamically from user-space.Thereby, additional configuration needs to be done to bring up the gadget compared with precomposed configurations. 
_(Instructions below were tested on A20 with kernel 5.9.0.)_
The RNDIS gadget with configfs requires a number of _menuconfig_ options being enabled: 
[code] 
        Device Drivers  --->
            [*] USB support  --->
            <M> Inventra Highspeed Dual Role Controller (TI, ADI, AW, ...)
                    MUSB Mode Selection (Dual Role mode)  --->
                    *** Platform Glue Layer ***
                <M> Allwinner (sunxi)
                    *** MUSB DMA mode ***
                [*] Disable DMA (always use PIO)
            USB Physical Layer drivers  --->
                <M> NOP USB Transceiver Driver
            <M>   USB Gadget Support  --->
                <M>   USB Gadget functions configurable through configfs
                [*]     RNDIS
    
[/code]
    [![Sticky-note-pin.png][57163]][57164] _Note:_ You need to select both "Inventra Highspeed Dual Role Controller" and "NOP USB Transceiver Driver" **before** the required "Allwinner (sunxi)" option (_CONFIG_USB_MUSB_SUNXI_) becomes available.
Now you can compile the kernel and modules. For details, you can refer to [our manual build howto][57165]. 
### Mainline kernel (via Precomposed Configurations)
See <http://thread.gmane.org/gmane.comp.hardware.netbook.arm.sunxi/19214/focus=19215>
_(Instructions below were tested on A20 with kernel 4.4.6.)_
For Allwinner SoCs based on the sun4i controller (CONFIG_PHY_SUN4I_USB=y), the "MUSB" (Multipoint Highspeed Dual-Role Controller) driver provides the OTG / gadget functionality. For successful operation, a number of _Kconfig_ options need to be enabled: 
[code] 
    CONFIG_USB_MUSB_HDRC=m
    CONFIG_USB_MUSB_DUAL_ROLE=y
    CONFIG_USB_MUSB_SUNXI=m
    CONFIG_MUSB_PIO_ONLY=y
    CONFIG_USB_PHY=y
    CONFIG_NOP_USB_XCEIV=m
    
[/code]
(Substitute "y" for "m" where desired, if you do not wish modules to be built and want the drivers compiled-in instead.) 
With _menuconfig_ this looks like 
[code] 
        Device Drivers  --->
            [*] USB support  --->
            <M> Inventra Highspeed Dual Role Controller (TI, ADI, AW, ...)
                    MUSB Mode Selection (Dual Role mode)  --->
                    *** Platform Glue Layer ***
                <M> Allwinner (sunxi)
                    *** MUSB DMA mode ***
                [*] Disable DMA (always use PIO)
            USB Physical Layer drivers  --->
                <M> NOP USB Transceiver Driver
    
[/code]
    [![Sticky-note-pin.png][57163]][57164] _Note:_ You need to select both "Inventra Highspeed Dual Role Controller" and "NOP USB Transceiver Driver" **before** the required "Allwinner (sunxi)" option (_CONFIG_USB_MUSB_SUNXI_) becomes available.
You'll probably also want to select 
[code] 
            <*> USB Gadget Support
[/code]
and any desired gadget drivers on top of that. 
Proceed with compiling and installing your kernel and its corresponding modules (for assistance check our [howto][57166]). 
[![MBOX icon information.png][57167]][57168] | If you compiled the MUSB driver as module(s), make sure to load those first - before you attempt to use any of the gadget drivers: 
[code]
    modprobe sunxi
[/code]  
---|---  
Upon successful initialization the kernel will report something similar to: 
[code] 
    [   33.950832] usb_phy_generic.0.auto supply vcc not found, using dummy regulator
    [   33.951799] musb-hdrc: ConfigData=0xde (UTMI-8, dyn FIFOs, bulk combine, bulk split, HB-ISO Rx, HB-ISO Tx, SoftConn)
    [   33.951833] musb-hdrc: MHDRC RTL version 0.0 
    [   33.951872] musb-hdrc: 11/11 max ep, 5184/8192 memory
    [   33.952312] musb-hdrc musb-hdrc.1.auto: MUSB HDRC host driver
    [   33.952355] musb-hdrc musb-hdrc.1.auto: new USB bus registered, assigned bus number 5
    [   33.956664] hub 5-0:1.0: USB hub found
    [   33.956828] hub 5-0:1.0: 1 port detected
    
[/code]
After that, you should be able to use the USB gadget drivers/modules (_g_ether_ , _g_mass_storage_ , ...) as described below. 
### sunxi-3.4
Currently, the g_ether module is not compiled as part of our kernel configuration. 
To enable this, follow the kernel building information of [our manual build howto][57165]. But then after making defconfig, either run: 
[code] 
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig
[/code]
Then trawl down the options and set the "Ethernet Gadget" to "m": 
[code] 
        Device Drivers  --->
            USB support  --->
                <*>    USB Gadget Support  --->
                    <m>    Ethernet Gadget (with CDC Ethernet support)
                <*>    NOP USB Transceiver Driver
                [*]    SUNXI USB2.0 Dual Role Controller support --->
                    [*]    Sunxi USB2.0 Manager
                           USB0 Controller support (otg support) --->
                               (*) otg support
    
[/code]
Or just run: 
[code] 
    ./scripts/config -m CONFIG_USB_ETH -e CONFIG_USB_ETH_RNDIS -e CONFIG_USB_OTG_UTILS -e CONFIG_NOP_USB_XCEIV 
     -e CONFIG_USB_SW_SUNXI_USB -e CONFIG_USB_SW_SUNXI_USB_MANAGER -e CONFIG_USB_SW_SUNXI_USB0_OTG
    
[/code]
You can now continue following [our manual build howto][57165] to continue kernel compilation and installation. 
Note that for sun4i devices (A10), you also need to enable SoftWinner SUNXI USB peripheral controller in order to enable high-speed operation for gadget- otherwise it will be limited to full-speed only. 
[code] 
        Device Drivers  --->
            USB support  --->
                <*>     USB Gadget Support --->
                    <m> SoftWinner SUNXI USB Peripheral Controller 
    
[/code]
## Loading the driver (on the device)
### configfs
The configfs approach requires a number of modules being loaded: 
[code] 
    modprobe sunxi
    modprobe configfs
    modprobe libcomposite
    modprobe u_ether
    modprobe usb_f_rndis
    
[/code]
If you see nothing is printed to the kernel ring buffer, it is just normal since the gadget is not enabled until configurations under configfs are done. 
### Precomposed Configurations
We should now be able to run: 
[code] 
    modprobe g_ether
[/code]
successfully. We can then make this module autoload by adding it to /etc/modules. 
Now, so that g_ether doesn't randomly generate a new id every reboot, stick the following in /etc/modprobe.d/g_ether.conf: 
[code] 
    options g_ether host_addr=00:11:22:33:44:55
[/code]
g_ether should've just generated a pair of addresses for you, so replace _00:11:22:33:44:55_ with the outcome of: 
[code] 
     dmesg | grep "HOST MAC"
[/code]
We can also use _dev_addr_ option to set device MAC address. 
## Configuring the gadget under configfs
[![MBOX icon information.png][57167]][57168] | This chapter is for configfs approach only. Users who adopt precomposed configurations should skip following steps.   
---|---  
Some configuration must be done to set up the gadget properly. 
[code] 
    cd /sys/kernel/config/usb_gadget
    mkdir g1
    cd g1
    echo "0x1d6b" > idVendor
    echo "0x0104" > idProduct
    mkdir functions/rndis.rn0
    mkdir configs/c1.1
    ln -s functions/rndis.rn0 configs/c1.1/
    
[/code]
Here "0x1d6b" for idVendor stands for Linux Foundation and "0x0104" for idProduct stands for Multifunction Composite Gadget. In case your host can not identify these ids to recognize your device properly, you may need manually install RNDIS driver on your host for your device. 
Finally, the gadget can be enabled with 
[code] 
    echo <udc name> > UDC
    
[/code]
where <udc name> is one of those found in /sys/class/udc/* which is musb-hdrc.1.auto on my device. 
Similarly, the gadget can be disabled with 
[code] 
    echo "" > UDC
    
[/code]
You can use this to disconnect or reconnect your device to the host logically. 
## Configuring the device's networking
### Ubuntu/Debian
#### Without network manager
Stop networkmanager: 
[code] 
     stop network-manager 
[/code]
To prevent network-manager from starting, run: 
[code] 
    echo "manual" > /etc/init/network-manager.override
[/code]
Now add the following to /etc/network/interfaces: 
[code] 
    auto usb0
    iface usb0 inet static
    	address 192.168.0.2
    	netmask 255.255.255.0
    
[/code]
To manually activate the interface and set an IP (**NOTE:** if configured with ip from iproute2 it will not work): 
[code] 
         ifconfig usb0 up
         ifconfig usb0 192.168.0.2
    
[/code]
## Setting up the host
You can convince networkmanager to connect automatically to a specific MAC address, and then you need to hardcode the address to 192.168.0.1 for this connection. 
If all goes well, you should now be able to just plug in the USB cable. 
## See also
Experiments with USB ethernet and H3 @ Armbian forums: 
  * <https://forum.armbian.com/index.php/topic/1417-testers-wanted-g-ether-driver-h3-device-as-ethernet-dongle/>
  * <https://forum.armbian.com/index.php/topic/2916-usb-otg-as-a-network/>
