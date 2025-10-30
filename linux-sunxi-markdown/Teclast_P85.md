# Teclast P85
Teclast P85  
---  
[![][54682]][54683] [][54684]Teclast P85 (R8A1) front image  
Manufacturer |  [Teclast][54685]  
Specifications   
SoC |  [A10][54686] @ 1Ghz   
DRAM |  1GiB DDR3 @360MHz ([DDR3#H5TQ2G83CFR-H9C][54687])   
NAND |  8GB   
Power |  USB, 3900mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x768 (8" 4:3)   
Touchscreen |  5-finger capacitive FT5306DE4 ([Touchscreen#FT5x06][54688])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, internal speaker, internal microphone   
Network |  WiFi 802.11 b/g/n (Realtek RTL8188CUS)   
Storage |  microSD   
USB |  1 USB2.0 OTG   
Camera |  front-facing   
Other |  Accelerometer   
Headers |  UART   
## Contents
  * [1 Identification][54689]
  * [2 Sunxi support][54690]
    * [2.1 Manual build][54691]
      * [2.1.1 Mainline U-Boot][54692]
      * [2.1.2 Mainline Linux kernel][54693]
  * [3 Tips, Tricks, Caveats][54694]
    * [3.1 FEL mode][54695]
    * [3.2 External power supply hacking][54696]
  * [4 Adding a serial port][54697]
  * [5 See also][54698]

# Identification
On the back of the device, the following is printed: 
[code] 
    Teclast TPad
    P85 id:R8A1
[/code]
The PCB has the following silkscreened on it: 
[code] 
    M858/M868-V1.2
    20120216
[/code]
Or the following: 
[code] 
    M858/M868-V1.1-20120115
    
[/code]
In android, under Settings->About Tablet, you will find: 
  * Model Number _P85(R8A1)_
  * Kernel Version _3.0.8_

# Sunxi support
## Manual build
### Mainline U-Boot
Use the **Linksprite_pcDuino_defconfig** build target as a workaround. The P85 R8A1 and some of [LinkSprite pcDuino2][54699] boards use the same DDR3 chips (H5TQ2G83CFR-H9C). CONFIG_SUN4I_EMAC can be disabled, as the tablet lacks Ethernet port. U-Boot HDMI output is supported, but USB keyboard connected via OTG doesn't work in U-Boot shell. 
### Mainline Linux kernel
Use the **sun4i-a10-pcduino.dtb** device-tree binary as a workaround, but some editing to the sun4i-a10-pcduino.dts is necessary: 
[code] 
    &usb_otg {
      dr_mode = "host"; /* dr_mode="otg" has problems recognizing USB devices*/
      status = "okay";
    };
    
    &reg_usb0_vbus {
      /* If powered by AXP209's ACIN pin instead of battery,
       * regulator-always-on must be omitted, otherwise the kernel fails to boot.
       */
      regulator-always-on;
      status = "okay";
    };
    
    /* usb1 is disabled in scirpt.fex */
    
    &reg_usb2_vbus {
      gpio = <&pio 7 12 GPIO_ACTIVE_HIGH>; /* PH12 */
      status = "okay";
    };
    
    &usbphy {
      usb0_id_det-gpios = <&pio 7 4 (GPIO_ACTIVE_HIGH | GPIO_PULL_UP)>; /* PH4 */
      usb0_vbus_det-gpios = <&pio 7 5 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>; /*PH5*/
      usb0_vbus-supply = <&reg_usb0_vbus>;
      usb2_vbus-supply = <&reg_usb2_vbus>;
      status = "okay";
    };
    
    &lradc {
      vref-supply = <&reg_vcc3v0>;
      status = "okay";
    
      button-400 {
        label = "Key Esc";
        linux,code = <KEY_ESC>;
        channel = <0>;
        voltage = <400000>;
      };
    
      button-800 {
        label = "Key Menu";
        linux,code = <KEY_MENU>;
        channel = <0>;
        voltage = <800000>;
      };
    };
    
    &ac_power_supply {
      status = "okay"
    };
    
    &usb_power_supply 
      status = "okay"
    };
    
    &battery_power_supply {
      status = "okay"
    };
    
[/code]
Note that **" &de { status = "okay"; };"** in device tree may result in HDMI output failing to work after sun4i-drm driver is loaded. Not sure if it's a hardware-related or software-related issue. GPU 3D acceleration doesn't work. 
The kernel compilation option **CONFIG_DRM_SIMPLEDRM=y** may cause HDMI output to fail altogether. Just have **CONFIG_FB_SIMPLE=y** enabled, and HDMI output works fine with simple-framebuffer driver. 
Internal audio codec may not work, neither is USB audio DAC connected via USB OTG, although the USB audio device is recognized. 
# Tips, Tricks, Caveats
## FEL mode
Holding the MENU button while connecting USB to another PC triggers [FEL mode][54700]. 
## External power supply hacking
[![][54701]][54702]
[][54703]
Teclast P85 (R8A1) AXP209 ACIN hack
The [AXP209][54704] PMU supports external 5V DC power supply (ACIN pin), alleviating the need for a battery or a [USB OTG Charging Hub][54705] while using a USB Hub. Battery charging with ACIN connected is supported with the above *_power_supply device tree editing. 
# Adding a serial port
[![][54706]][54707]
[][54708]
Teclast P85 (R8A1) UART TX pad
Three are 2 consecutive tiny solder pads besides the A10 chip. The one near the 4 consecutive pads is TX. 
# See also
[Lark FreeMe 70.2S, another A10 tablet supported by postmarketOS. Its &lradc and &*_power_supply fields in device tree work on Teclast P85 (R8A1)][54709]
