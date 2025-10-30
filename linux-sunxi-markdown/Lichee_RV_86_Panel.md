# Lichee RV 86 Panel
This page describes the Sipeed RV86 touch screen LCD panel. This panel comes as 480x480 / 720x720 variants. 
## Contents
  * [1 Status][31023]
  * [2 Kernel Messages][31024]
  * [3 Kernel Configuration][31025]
  * [4 Frame Buffer][31026]
  * [5 Panels][31027]

# Status
This panel works with Vendor-provided kernel images. 
On the [mainline kernel][31028], the kernel uses the **sun4i-drm** driver. 
# Kernel Messages
The main line kernel will output this, during boot: 
[code] 
    sun4i-drm display-engine: Adding to iommu group 0
    sun4i-drm display-engine: bound 5100000.mixer (ops 0xffffffff80c5f628)
    sun4i-drm display-engine: bound 5200000.mixer (ops 0xffffffff80c5f628)
    sun4i-drm display-engine: bound 5460000.tcon-top (ops 0xffffffff80c63ca8)
    sun4i-drm display-engine: bound 5461000.lcd-controller (ops 0xffffffff80c5c6d8)
    sun4i-drm display-engine: bound 5470000.lcd-controller (ops 0xffffffff80c5c6d8)
    [drm] Initialized sun4i-drm 1.0.0 20150629 for display-engine on minor 0
    sun4i-drm display-engine: [drm] fb0: sun4i-drmdrmfb frame buffer device
    
[/code]
The vendor kernel does not have any sun4i-drm messages. In fact, it does not use DRM at all. Instead it merely reports on hdmi: 
[code] 
    HDMI 2.0 driver init start!
    boot_hdmi=false
    ERROR: pinctrl_get for HDMI2.0 DDC fail
    HDMI2.0 module init end
    hdmi_hpd_sys_config_release
    
[/code]
# Kernel Configuration
The vendor supplied kernel has these configuration options set: 
[code] 
    #
    # Video support for sunxi
    #
    CONFIG_DISP2_SUNXI=y
    CONFIG_SUNXI_DISP2_FB_DISABLE_ROTATE=y
    CONFIG_HDMI2_DISP2_SUNXI=y
    CONFIG_AW_PHY=y
    CONFIG_HDMI2_HDCP_SUNXI=y
    CONFIG_HDMI2_CEC_SUNXI=y
    CONFIG_DISP2_SUNXI_DEBUG=y
    CONFIG_DISP2_LCD_ESD_DETECT=y
    #
    # LCD panels select
    #
    CONFIG_LCD_SUPPORT_ST7701S_RGB=y
    CONFIG_LCD_SUPPORT_NV3052C_RGB=y
    CONFIG_LCD_SUPPORT_INET_DSI_PANEL=y
    CONFIG_LCD_SUPPORT_ST7789V_CPU=y
    CONFIG_LCD_SUPPORT_TFT08006=y
    #
    # Display engine feature select
    #
    CONFIG_DISP2_SUNXI_SUPPORT_SMBL=y
    CONFIG_DISP2_SUNXI_SUPPORT_ENAHNCE=y
    #
    # Backlight & LCD device support
    #
    # CONFIG_LCD_CLASS_DEVICE is not set
    CONFIG_BACKLIGHT_CLASS_DEVICE=y
    CONFIG_BACKLIGHT_GENERIC=y
    
[/code]
NOTE: These configuration options are not available in the mainline kernel. 
# Frame Buffer
The fbset tool will report this on the framebuffer device: 
[code] 
    $ sudo fbset -i
    
    mode "480x480"
        geometry 480 480 480 480 32
        timings 0 0 0 0 0 0 0
        accel true
        rgba 8/16,8/8,8/0,0/0
    endmode
    
    Frame buffer device information:
        Name        : sun4i-drmdrmfb
        Address     : 0
        Size        : 921600
        Type        : PACKED PIXELS
        Visual      : TRUECOLOR
        XPanStep    : 1
        YPanStep    : 1
        YWrapStep   : 0
        LineLength  : 1920
        Accelerator : No
    
[/code]
Compare this with the vendor-provided Linux sipeed 5.4.61, that has a working display: 
[code] 
    $ sudo fbset -i
    
    mode "480x480-60"
        # D: 19.000 MHz, H: 31.046 kHz, V: 59.704 Hz
        geometry 480 480 480 960 32
        timings 52631 48 72 14 22 12 4
        rgba 8/16,8/8,8/0,8/24
    endmode
    
    Frame buffer device information:
        Name        : 
        Address     : 0xffe00000
        Size        : 1843200
        Type        : PACKED PIXELS
        Visual      : TRUECOLOR
        XPanStep    : 1
        YPanStep    : 1
        YWrapStep   : 0
        LineLength  : 1920
        Accelerator : No
    
[/code]
Note that the fb device is unnamed in this case. 
# Panels
The device has been shipped with multiple panel types: 
  * A 480x272 panel, default_lcd driver
  * A 480x480 panel, st7701s_rgb driver
  * A 720x720 panel, nv3052c_rgb driver
  * A 720x720 panel, default_lcd driver

The last panel requires this device tree node on Allwinner kernels to use correct timings: 
[code] 
    &lcd0 {
    	lcd_used        = <1>;
    	lcd_driver_name = "default_lcd";
    
    	lcd_if          = <0>;
    	lcd_hv_if       = <0>;
    
    	lcd_width       = <70>;
    	lcd_height      = <72>;
    	lcd_x           = <720>;
    	lcd_y           = <720>;
    	lcd_dclk_freq   = <36>;
    	lcd_hbp         = <60>;
    	lcd_ht          = <800>;
    	lcd_hspw        = <12>;
    	lcd_vbp         = <25>;
    	lcd_vt          = <780>;
    	lcd_vspw        = <8>;
    
    	lcd_backlight   = <50>;
    	lcd_pwm_used    = <1>;
    	lcd_pwm_ch      = <7>;
    	lcd_pwm_freq    = <20000>;
    	lcd_pwm_pol     = <1>;
    	lcd_bright_curve_en = <0>;
    
    	lcd_frm         = <1>;
    	lcd_io_phase    = <0x0000>;
    	lcd_gamma_en    = <0>;
    	lcd_cmap_en     = <0>;
    	lcd_hv_clk_phase= <0>;
    	lcd_hv_sync_polarity= <0>;
    	lcd_rb_swap          = <0>;
    
    	lcd_power       = "vcc-lcd";
    	lcd_pin_power   = "vcc-pd";
    	lcd_gpio_0      = <&pio PG 13 GPIO_ACTIVE_HIGH>;
    	lcd_gpio_1      = <&pio PE 14 GPIO_ACTIVE_HIGH>;
    	lcd_gpio_2      = <&pio PE 12 GPIO_ACTIVE_HIGH>;
    	lcd_gpio_3      = <&pio PE 15 GPIO_ACTIVE_HIGH>;
    	pinctrl-0       = <&rgb18_pins_a>;
    	pinctrl-1       = <&rgb18_pins_b>;
    };
    
[/code]
The rest pin polarity is flipped between Allwinner Linux and U-Boot device trees.
