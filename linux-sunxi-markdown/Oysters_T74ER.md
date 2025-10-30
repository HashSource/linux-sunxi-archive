# Oysters T74ER
Oysters T74ER  
---  
[![Oysters t74er u-boot202201.jpg][43638]][43639]  
Manufacturer |  [Manufacturer][43640]  
Dimensions |  190.7mm x 115.7mm x 11.7mm   
Release Date |  23/03/2015   
Website |  [Device Product Page][43641]  
Specifications   
SoC |  [A33][43642] @ 1.3Ghz   
DRAM |  512MiB DDR3 @ 400MHz   
NAND |  4GB   
Power |  DC 5V @ 1A, 2000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (7" 16:9)   
Touchscreen |  X-finger capacitive/resistive ([Manufacturer device][43643])   
Audio |  3.5mm headphone plug, 3.5mm microphone plug, internal mono speaker, internal microphone   
Network |  WiFi 802.11 b/g/n   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  ??.?MP (????x????) front, ??.?MP (????x????) rear   
Headers |  LCD   
A Q8 style cheap tablet, but with an A33 SoC. 
## Contents
  * [1 Identification][43644]
  * [2 Sunxi support][43645]
    * [2.1 Current status][43646]
      * [2.1.1 Mainline U-Boot][43647]
      * [2.1.2 Linux Kernel][43648]
        * [2.1.2.1 Mainline kernel][43649]
  * [3 Tips, Tricks, Caveats][43650]
    * [3.1 FEL mode][43651]
    * [3.2 Device specific topic][43652]
    * [3.3 ...][43653]
  * [4 Adding a serial port (**voids warranty**)][43654]
    * [4.1 Device disassembly][43655]
    * [4.2 Locating the UART][43656]
    * [4.3 Adding USB Host port][43657]
  * [5 Pictures][43658]
  * [6 Schematic][43659]
  * [7 Also known as][43660]
  * [8 See also][43661]
    * [8.1 Manufacturer images][43662]

# Identification
This section explains how to most easily identify your device. For a development board, explain the name(s) printed on the board. For an android device, find out the strings as reported under settings.
On the back of the device, the following is printed: 
[code] 
    Tablet PC I T74ER
[/code]
The PCB has the following silkscreened on it: 
[code] 
    AL-AX3-751S_V1.5
    2015.03.23
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number: _DEVICE_
  * Build Number: _Oysters_T74ER_SA002_08092015_

# Sunxi support
## Current status
Mainline U-boot OK from SD. 
Mainline kernel started but usb and drm don't work 
#### Mainline U-Boot
Use the **q8_a33_tablet_1024x600_defconfig** build target. 
In new versions of U-Boot, USB-OTG power supply does not work. Use a USB hub with active power supply, or an old U-Boot 
### Linux Kernel
#### Mainline kernel
Use the **sun8i-a33-q8-tablet.dtb** device-tree binary. 
To work with GPU acceleration, apply this old patch. Worked in 2022. 
**Patch file (click on the 'Expand' link to see it):**
[code] 
    diff --git a/arch/arm/boot/dts/sun8i-a23-a33.dtsi b/arch/arm/boot/dts/sun8i-a23-a33.dtsi
    index 4461d5098..81c694c55 100644
    --- a/arch/arm/boot/dts/sun8i-a23-a33.dtsi
    +++ b/arch/arm/boot/dts/sun8i-a23-a33.dtsi
    @@ -284,7 +284,7 @@ usb_otg: usb@1c19000 {
     			phys = <&usbphy 0>;
     			phy-names = "usb";
     			extcon = <&usbphy 0>;
    -			dr_mode = "otg";
    +			dr_mode = "host";
     			status = "disabled";
     		};
     
    diff --git a/arch/arm/boot/dts/sun8i-a33-q8-tablet.dts b/arch/arm/boot/dts/sun8i-a33-q8-tablet.dts
    index 9c5750c25..f37b8cdc2 100644
    --- a/arch/arm/boot/dts/sun8i-a33-q8-tablet.dts
    +++ b/arch/arm/boot/dts/sun8i-a33-q8-tablet.dts
    @@ -49,9 +49,21 @@ / {
     	compatible = "allwinner,q8-a33", "allwinner,sun8i-a33";
     };
     
    +&panel {
    +	compatible = "oysters,1024-600", "simple-panel";
    +};
    +
     &tcon0_out {
     	tcon0_out_lcd: endpoint@0 {
     		reg = <0>;
     		remote-endpoint = <&panel_input>;
     	};
     };
    +
    +&sound {
    +	status = "okay";
    +};
    +
    +&codec {
    +	status = "okay";
    +};
    diff --git a/arch/arm/boot/dts/sun8i-reference-design-tablet.dtsi b/arch/arm/boot/dts/sun8i-reference-design-tablet.dtsi
    index 872d56caa..5f9ca7abe 100644
    --- a/arch/arm/boot/dts/sun8i-reference-design-tablet.dtsi
    +++ b/arch/arm/boot/dts/sun8i-reference-design-tablet.dtsi
    @@ -208,7 +208,7 @@ &simplefb_lcd {
     };
     
     &usb_otg {
    -	dr_mode = "otg";
    +	dr_mode = "host";
     	status = "okay";
     };
     
    diff --git a/drivers/gpu/drm/panel/panel-simple.c b/drivers/gpu/drm/panel/panel-simple.c
    index 9e46db5e3..fcc60550e 100644
    --- a/drivers/gpu/drm/panel/panel-simple.c
    +++ b/drivers/gpu/drm/panel/panel-simple.c
    @@ -3651,6 +3651,28 @@ static const struct panel_desc arm_rtsm = {
     	.bus_format = MEDIA_BUS_FMT_RGB888_1X24,
     };
     
    +static const struct drm_display_mode oysters_1024_600_mode = {
    +	.clock = 51000,
    +	.hdisplay = 1024,
    +	.hsync_start = 1024 + 160,
    +	.hsync_end = 1024 + 160 + 1,
    +	.htotal = 1024 + 160 + 1 + 159,
    +	.vdisplay = 600,
    +	.vsync_start = 600 + 12,
    +	.vsync_end = 600 + 12 + 1,
    +	.vtotal = 600 + 12 + 1 + 22,
    +};
    +
    +static const struct panel_desc oysters_1024_600 = {
    +	.modes = &oysters_1024_600_mode,
    +	.num_modes = 1,
    +	.bpc = 6,
    +	.size = {
    +		.width = 154,
    +		.height = 86,
    +	},
    +};
    +
     static const struct of_device_id platform_of_match[] = {
     	{
     		.compatible = "ampire,am-1280800n3tzqw-t00h",
    @@ -3709,6 +3731,9 @@ static const struct of_device_id platform_of_match[] = {
     	}, {
     		.compatible = "bananapi,s070wv20-ct16",
     		.data = &bananapi_s070wv20_ct16,
    +	}, {
    +		.compatible = "oysters,1024-600",
    +		.data = &oysters_1024_600,
     	}, {
     		.compatible = "boe,hv070wsa-100",
     		.data = &boe_hv070wsa
    
    
[/code]
# Tips, Tricks, Caveats
Add MANUFACTURER DEVICE specific tips, tricks, Caveats and nice to have changes here.
## FEL mode
The Volume+ button triggers [ FEL mode][43663]. 
## Device specific topic
If there are no further device specific topics to add, remove these sections.
## ...
# Adding a serial port (**voids warranty**)
[![][43664]][43665]
[][43666]
DEVICE UART pads
This section explains how to attach a serial port to the device. Make sure it refers to our [UART howto][43667]. For a development board, you can just mention how to find the header with the pins and include a picture, and you can remove the warranty voiding warning.
## Device disassembly
If necessary, provide a short description of how to open the device. Perhaps explain how the pins can be most easily popped. If pins do need to be popped, mention the [Plastic tool howto][43668].
## Locating the UART
Describe how to find the RX,TX,GND signals here, and mention the [UART howto][43667].
## Adding USB Host port
This device has an empty USB Host pad near the Wi-Fi chip. Don't forget to enable **CONFIG_USB_EHCI_GENERIC** in u-boot 
# Pictures
Take some pictures of your device, [ upload them][43669], and add them here. DO NOT UPLOAD PICTURES WHICH YOU PLUCKED OFF THE INTERNET.
  * [![Oysters t74er PCB1.jpg][43670]][43671]
  * [![Oysters t74er back1.jpg][43672]][43673]

# Schematic
List schematics, board layout, cad files, etc here.
# Also known as
List rebadged devices here.
# See also
Add some nice to have links here. This includes related devices, and external links.
## Manufacturer images
Optional. Add non-sunxi images in this section.
