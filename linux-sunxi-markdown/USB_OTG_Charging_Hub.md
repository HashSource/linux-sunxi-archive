# USB OTG Charging Hub
Some sunxi devices, primarily tablets, only have a single USB OTG connector (mini or micro) as the only way to connect USB peripheral devices. Moreover, these tablets often don't have a dedicated 5V DC power connector and also rely on USB OTG for charging. This is less than perfect if the tablet is supposed to be sometimes used in a "linux desktop" or a "linux server" role, which requires being able to operate indefinitely without any need for periodic cumbersome maintenance, such as battery recharging. At the same time, supporting USB keyboard/mouse is necessary for handling interaction with the user. And if the tablet does not have an ethernet connector, then a USB ethernet dongle is very useful for providing network connectivity. So, ideally, we want to have the following feature: **the USB OTG connector should be able to work as a USB host and also supply power to the tablet at the same time**. 
Fortunately, searching ebay or other online webshops for "otg charging hub" keywords allows to find relatively cheap ~5$ devices, which might be a reasonable solution for this particular problem. They may look like this: 
[![4 Port Micro Usb Power Charging Otg Hub.jpg][57325]][57326]
There is a mechanical switch, which changes between "OTG" and "Charge" modes. In the "OTG" mode, it acts as a powered USB hub, which allows to connect 3 USB devices to it. The power can be provided to it by a microusb charger cable by plugging it to a "female" microusb connector in the hub. The "male" microusb connector is connected to the OTG port of a sunxi device. If the switch is set to the "Charge" position, then the hub is also providing 5V on the VBUS pin to the sunxi device. 
## sunxi-3.4 kernel
Apply the following patch to the kernel: 
[code] 
    From 2033a7f5d19cfcc76daad382660eb31add9e33ee Mon Sep 17 00:00:00 2001
    From: Siarhei Siamashka <[[email protected]][57327]>
    Date: Fri, 14 Nov 2014 19:34:12 +0200
    Subject: [PATCH] HACK: Support USB OTH Charging Hub
    
    We assume that the hub is supplying power to the device on VBUS
    and also provides host ports for connecting USB peripherals.
    
    Hence configure OTG as 'host only' and remove the bits of code,
    which try to configure AXP to provide 5V on VBUS. AXP should
    always treat VBUS as the external source of power and charge
    the battery from it, regardless of the MUSB state.
    ---
     arch/arm/configs/sun4i_defconfig         |  1 +
     arch/arm/configs/sun5i_defconfig         |  1 +
     arch/arm/configs/sun7i_defconfig         |  1 +
     drivers/usb/sunxi_usb/hcd/hcd0/sw_hcd0.c | 17 +++++------------
     4 files changed, 8 insertions(+), 12 deletions(-)
    
    diff --git a/arch/arm/configs/sun4i_defconfig b/arch/arm/configs/sun4i_defconfig
    index 2bc999d..b313b60 100644
    --- a/arch/arm/configs/sun4i_defconfig
    +++ b/arch/arm/configs/sun4i_defconfig
    @@ -240,6 +240,7 @@ CONFIG_USB_FILE_STORAGE=m
     CONFIG_USB_FILE_STORAGE_TEST=y
     CONFIG_USB_SW_SUNXI_USB=y
     CONFIG_USB_SW_SUNXI_USB_MANAGER=y
    +CONFIG_USB_SW_SUNXI_USB0_HOST_ONLY=y
     CONFIG_USB_SW_SUNXI_USB_DEBUG=y
     CONFIG_MMC=y
     CONFIG_MMC_UNSAFE_RESUME=y
    diff --git a/arch/arm/configs/sun5i_defconfig b/arch/arm/configs/sun5i_defconfig
    index f837d69..ed0e1b52 100644
    --- a/arch/arm/configs/sun5i_defconfig
    +++ b/arch/arm/configs/sun5i_defconfig
    @@ -174,6 +174,7 @@ CONFIG_USB_FILE_STORAGE=m
     CONFIG_USB_FILE_STORAGE_TEST=y
     CONFIG_USB_SW_SUNXI_USB=y
     CONFIG_USB_SW_SUNXI_USB_MANAGER=y
    +CONFIG_USB_SW_SUNXI_USB0_HOST_ONLY=y
     CONFIG_USB_SW_SUNXI_USB_DEBUG=y
     CONFIG_MMC=y
     CONFIG_MMC_UNSAFE_RESUME=y
    diff --git a/arch/arm/configs/sun7i_defconfig b/arch/arm/configs/sun7i_defconfig
    index d414a27..e306d9d 100644
    --- a/arch/arm/configs/sun7i_defconfig
    +++ b/arch/arm/configs/sun7i_defconfig
    @@ -239,6 +239,7 @@ CONFIG_USB_FILE_STORAGE=m
     CONFIG_USB_FILE_STORAGE_TEST=y
     CONFIG_USB_SW_SUNXI_USB=y
     CONFIG_USB_SW_SUNXI_USB_MANAGER=y
    +CONFIG_USB_SW_SUNXI_USB0_HOST_ONLY=y
     CONFIG_USB_SW_SUNXI_USB_DEBUG=y
     CONFIG_MMC=y
     CONFIG_MMC_UNSAFE_RESUME=y
    diff --git a/drivers/usb/sunxi_usb/hcd/hcd0/sw_hcd0.c b/drivers/usb/sunxi_usb/hcd/hcd0/sw_hcd0.c
    index 2399ec6..8c80ae9 100644
    --- a/drivers/usb/sunxi_usb/hcd/hcd0/sw_hcd0.c
    +++ b/drivers/usb/sunxi_usb/hcd/hcd0/sw_hcd0.c
    @@ -550,23 +550,16 @@ static void sw_hcd_board_set_vbus(struct sw_hcd *sw_hcd, int is_on)
     
     	if (is_on && hcd0_set_vbus_cnt == 1) {
     		DMSG_INFO("[%s]: Set USB Power On\n", sw_hcd->driver_name);
    -		if (sw_hcd->sw_hcd_io->drv_vbus_gpio_set.port == 0xffff)
    -			axp_gpio_set_value(hcd_io->drv_vbus_gpio_set.port_num,
    -					on_off);
    -		else
    -			gpio_write_one_pin_value(hcd_io->Drv_vbus_Handle,
    -					on_off, NULL);
    +
    +		/* leave AXP alone and don't touch VBUS */
    +
     	/* set gpio data */
     		USBC_Host_StartSession(sw_hcd->sw_hcd_io->usb_bsp_hdle);
     		USBC_ForceVbusValid(sw_hcd->sw_hcd_io->usb_bsp_hdle, USBC_VBUS_TYPE_HIGH);
     	} else if (!is_on && hcd0_set_vbus_cnt == 0) {
     		DMSG_INFO("[%s]: Set USB Power Off\n", sw_hcd->driver_name);
    -		if (sw_hcd->sw_hcd_io->drv_vbus_gpio_set.port == 0xffff)
    -			axp_gpio_set_value(hcd_io->drv_vbus_gpio_set.port_num,
    -					on_off);
    -		else
    -			gpio_write_one_pin_value(hcd_io->Drv_vbus_Handle,
    -					on_off, NULL);
    +
    +		/* leave AXP alone and don't touch VBUS */
     
     		set_hcd0_connect_status(0);
     		USBC_Host_EndSession(sw_hcd->sw_hcd_io->usb_bsp_hdle);
    -- 
    2.0.4
    
[/code]
After this kernel tweak, if the mechanical switch is set to the "Charge" mode, then the hub can be used to provide power to boot the sunxi device perfectly fine and also drive 3 USB host ports. Tested on [Olimex_A10-OLinuXino-Lime][57328], [Olimex_A13-OLinuXino-Micro][57329] and [Cubietech_Cubietruck][57330] with the use of "female microusb <-> male miniusb" adapter. 
[![OTG Charging Hub In Action.jpg][57331]][57332]
The picture above is showcasing the use of this hub to provide power to [Olimex_A13-OLinuXino-Micro][57329] board and also connect a USB Ethernet dongle and a USB wireless keyboard/mouse receiver. In this setup, X11 linux desktop system works properly with all the interaction with the outside world done using just USB OTG connector alone. 
Tablets and battery charging - TODO 
## mainline kernel
TODO
