# Camera
[![MBOX icon important.png][11464]][11465] | This page provides outdated set of instructions and needs to be updated to reflect current status. For current status, you might be more interested in [CSI][11466] page.   
---|---  
Camera functionality in sunxi is not well tested, and still in Proof-Of-Concept stage. However, in this document, I will try to write down my experiences with CSI cameras and one webcam. 
## WHAT YOU NEED:
1) Be able to compile & install linux-sunxi kernel ( see: <http://linux-sunxi.org/Linux_Kernel> ) 
2) Be able to modify your FEX file, and create script.bin ( See: <http://linux-sunxi.org/Fex_Guide> and <http://linux-sunxi.org/Script.bin> ) 
3) A PCBA with Allwinner based SoC ( such as A20), with CSI / USB interface. 
4) A Compatible USB Webcam ( Such as Logitech c510) or a CSI camera module ( See images below ) 
  * [![][11467]][11468]
OV5640 Camera Module connected to Interra3 board CSI connector 

## KERNEL PART:
For this part, I had to make a lot of trial/error ; because when you compile some CSI drivers, they compile fine, but cause segmentation faults or random kernel panics in runtime. That is one of the reasons, why I say the CSI support is in alpha stage in sunxi. 
Here is my current setting in my kernel menuconfig, to be able to easily switch between different CSI camera modules and USB Webcam: 
  * [![][11469]][11470]
3.4.79 kernel CSI setting in menuconfig 
  * [![][11471]][11472]
3.4.79 kernel UVC setting in menuconfig 

After compile & install your kernel with above settings, you may think to autoload your csi drivers during boot. I have managed to do this by adding 
[code] 
    sun4i_csi0
    
[/code]
to my /etc/modules file in my Debian wheezy 7 distro in my board. Otherwise, you may add it manually like this: 
[code] 
    insmod /lib/modules/3.4.79-sertac+/kernel/drivers/media/video/sun4i_csi/csi0/sun4i_csi0.ko
    
[/code]
This would probably insmod your ov5640.ko automatically as well. 
## CSI Camera and FEX Relationship:
First of all, in order to have CSI camera functionality in your A20 (or any other) based PCB, you must edit your FEX file accordingly. 
In the FEX file, CSI camera is setup in two places, [camera_list_para] and [csiX_para]: 
[code] 
    [camera_list_para]
    camera_list_para_used = 1
    ov7670 = 0
    gc0308 = 0
    gt2005 = 0
    hi704 = 0
    sp0838 = 0
    mt9m112 = 0
    mt9m113 = 0
    gc2035 = 0
    ov2655 = 0
    hi253 = 0
    gc0307 = 0
    mt9d112 = 0
    ov5640 = 1
    gc2015 = 0
    ov2643 = 0
    gc0329 = 0
    gc0309 = 0
    tvp5150 = 0
    s5k4ec = 0
    ov5650_mv9335 = 0
    siv121d = 0
    
    ;0x40--hi253 0x5a--s5k4ec 0x78--ov5640
    
    [csi0_para]
    csi_used            = 1
    csi_mode            = 0
    csi_dev_qty         = 1
    csi_stby_mode       = 0
    ;csi_mname           = "s5k4ec"
    ;csi_mname           = "hi253"
    csi_mname           = "ov5640" 
    csi_twi_id          = 1
    ;csi_twi_addr        = 0x5a
    ;csi_twi_addr        = 0x40
    csi_twi_addr        = 0x78 
    csi_if              = 0
    csi_vflip           = 1
    csi_hflip           = 0
    csi_iovdd           = "axp20_pll"
    csi_avdd            = "axp20_pll"
    csi_dvdd            = ""
    csi_vol_iovdd       = 2800
    csi_vol_dvdd        = 
    csi_vol_avdd        = 
    csi_flash_pol       = 0
    
    csi_mname_b         = ""
    
    csi_twi_id_b        = 0
    csi_twi_addr_b      = 0x42
    csi_if_b            = 0
    csi_vflip_b         = 0
    csi_hflip_b         = 0
    csi_iovdd_b         = "axp20_pll"
    csi_avdd_b          = ""
    csi_dvdd_b          = ""
    csi_vol_iovdd_b     = 2800
    csi_vol_avdd_b      = 
    csi_vol_dvdd_b      = 
    csi_flash_pol_b     = 0
    
    csi_pck             = port:PE00<3><default><default><default>
    csi_ck              = port:PE01<3><default><default><default>
    csi_hsync           = port:PE02<3><default><default><default>
    csi_vsync           = port:PE03<3><default><default><default>
    csi_d0              = port:PE04<3><default><default><default>
    csi_d1              = port:PE05<3><default><default><default>
    csi_d2              = port:PE06<3><default><default><default>
    csi_d3              = port:PE07<3><default><default><default>
    csi_d4              = port:PE08<3><default><default><default>
    csi_d5              = port:PE09<3><default><default><default>
    csi_d6              = port:PE10<3><default><default><default>
    csi_d7              = port:PE11<3><default><default><default>
    csi_reset           = port:PH13<1><default><default><0>
    csi_power_en        = port:PH16<1><default><default><1>
    csi_stby            = port:PH18<1><default><default><1>
    csi_flash           =
    csi_af_en           =
    csi_reset_b         = port:PH14<1><default><default><0>
    csi_power_en_b      = port:PH16<1><default><default><0>
    csi_stby_b          = port:PH19<1><default><default><0>
    csi_flash_b         =
    csi_af_en_b         =
    
    [csi1_para]
    csi_used = 0
    csi_dev_qty = 1
    csi_stby_mode = 0
    csi_mname = "gc0308"
    csi_if = 0
    csi_iovdd = "axp20_pll"
    csi_avdd = ""
    csi_dvdd = ""
    csi_vol_iovdd = 2800
    csi_vol_dvdd =
    csi_vol_avdd =
    csi_vflip = 0
    csi_hflip = 0
    csi_flash_pol = 0
    csi_facing = 1
    csi_twi_id = 1
    csi_twi_addr = 0x42
    csi_pck = port:PG00<3><default><default><default>
    csi_ck = port:PG01<3><default><default><default>
    csi_hsync = port:PG02<3><default><default><default>
    csi_vsync = port:PG03<3><default><default><default>
    csi_d0 = port:PG04<3><default><default><default>
    csi_d1 = port:PG05<3><default><default><default>
    csi_d2 = port:PG06<3><default><default><default>
    csi_d3 = port:PG07<3><default><default><default>
    csi_d4 = port:PG08<3><default><default><default>
    csi_d5 = port:PG09<3><default><default><default>
    csi_d6 = port:PG10<3><default><default><default>
    csi_d7 = port:PG11<3><default><default><default>
    csi_reset = port:PH13<1><default><default><0>
    csi_power_en = port:PH16<1><default><default><0>
    csi_stby = port:PH19<1><default><default><0>
    
    
[/code]
As you may see, in [camera_list_para], I have selected ov5640 as my camera. If your PCB support two CSI cameras ( FRONT and REAR/BACK ), then you may select two of them here. 
Also, as you see, in [csi1_para], I set csi_used = 0 , because in my PCB, I only have one CSI connector. 
Also, setting correct I2C address for the camera is also important. Please have a look: 
[code] 
    ;0x40--hi253 
    ;0x5a--s5k4ec
    ;0x78--ov5640
    
    csi_twi_addr        = 0x78 
    
[/code]
So, for this example, I choose my OV5640 camera module. Also, this "mname" thing is also very sensitive I think. Writing ="ov5640" instead of = "ov5640" causes strange troubles in runtime ( Please note the space between equal sign and the string... Such things may be handled better in DTB thing ? ) 
Anyway, I also had to inform you that 
[code] 
    csi_vflip           = 1
    csi_hflip           = 0
    
[/code]
works perfectly. So you can rotate camera view in both VERTICAL and HORIZONTAL directions ! I also tested this in Android, it also works well there too. 
Finally I have to show some of the camera module behaviours, when you connect to an A20 board with 3.4.79 kernel: 
**HI253 ( 2Mpix ) CSI Camera module:**
[code] 
    root@i3-3bc3 ~ # insmod /lib/modules/3.4.79-sertac+/kernel/drivers/media/video/sun4i_csi/csi0/sun4i_csi0.ko 
    <6>[CSI]Welcome to CSI driver
    <6>[CSI]csi_init
    <6>[CSI]registered sub device,input_num = 0
    <4>axp20_ldo3: Failed to create debugfs directory
    <4>axp20_ldo3: Failed to create debugfs directory
    <6>[CSI]V4L2 device registered as video0
    root@i3-3bc3 ~ # <6>[CSI]sensor initial success when csi open!
    
    root@i3-3bc3 ~ # ll /dev/video0 
    crw-rw---T 1 root video 81, 0 Jan  4 14:43 /dev/video0
    root@i3-3bc3 ~ # 
    root@i3-3bc3 ~ # v4l2-ctl -L
    <6>[CSI]sensor initial success when csi open!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
                         brightness <6>[CSI_ERR]v4l2 sub device queryctrl error!
    (int)    : min=-4 max=4 step=1 d<6>[CSI_ERR]v4l2 sub device queryctrl error!
    efault=1 value=0 flags=slider
     <6>[CSI_ERR]v4l2 sub device queryctrl error!
                          contrast (<6>[CSI_ERR]v4l2 sub device queryctrl error!
    int)    : min=-4 max=4 step=1 default=1 value=0 flags=slider
      <6>[CSI_ERR]v4l2 sub device queryctrl error!
                       saturation (i<6>[CSI_ERR]v4l2 sub device queryctrl error!
    nt)    : min=-4 max=4 step=1 def<6>[CSI_ERR]v4l2 sub device queryctrl error!
    ault=1 value=0 flags=slider
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
            white_balance_automatic <6>[CSI_ERR]v4l2 sub device queryctrl error!
    (bool)   : default=1 value=1
      <6>[CSI_ERR]v4l2 sub device queryctrl error!
                 do_white_balance (i<6>[CSI_ERR]v4l2 sub device queryctrl error!
    nt)    : min=0 max=5 step=1 defa<6>[CSI_ERR]v4l2 sub device queryctrl error!
    ult=0 value=0
                     <6>[CSI_ERR]v4l2 sub device queryctrl error!
          exposure (int)    : min=-4<6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    
                    horizontal_flip<6>[CSI_ERR]v4l2 sub device queryctrl error!
     (bool)   : default=0 value=0
     <6>[CSI_ERR]v4l2 sub device queryctrl error!
                     vertical_flip (<6>[CSI_ERR]v4l2 sub device queryctrl error!
    bool)   : default=0 value=0
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
                      color_effects <6>[CSI_ERR]v4l2 sub device queryctrl error!
    (menu)   : min=0 max=9 default=0<6>[CSI_ERR]v4l2 sub device queryctrl error!
     value=0
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
    <6>[CSI_ERR]v4l2 sub device queryctrl error!
                    flashlight_mode <6>[CSI_ERR]v4l2 sub device queryctrl error!
    (menu)   : min=0 max=4 default=0 value=0
    root@i3-3bc3 ~ #
    root@i3-3bc3 ~ # rmmod sun4i_csi0
    <6>[CSI]csi_exit
    <6>sun4i_csi sun4i_csi.0: unregistering video0
    <6>[CSI]csi_release ok!
    <6>[CSI]csi_remove ok!
     
    
[/code]
**Samsung S5K4EC ( 5Mpix ) CSI Camera module:**
This works well under android, but there is no driver under 3.4.79 
**OV5640 ( 5Mpix ) CSI Camera module:**
Will be added later.. 
[code] 
    
    
[/code]
**Logitech c510 USB Webcam:**
[code] 
    root@i3-3bc3 ~ # ehci_irq: port change detect
    ehci_irq: port change detect
    ehci_irq: port change detect
    <6>usb 2-1: new high-speed USB device number 2 using sw-ehci
    <6>uvcvideo: Found UVC 1.00 device <unnamed> (046d:081d)
    <6>input: UVC Camera (046d:081d) as /devices/platform/sw-ehci.1/usb2/2-1/2-1:1.2/input/input3
    
    root@i3-3bc3 ~ # 
    root@i3-3bc3 ~ # 
    root@i3-3bc3 ~ # 
    root@i3-3bc3 ~ # v4l2-ctl -L
                         brightness (int)    : min=0 max=255 step=1 default=128 value=128
                           contrast (int)    : min=0 max=255 step=1 default=32 value=32
                         saturation (int)    : min=0 max=255 step=1 default=34 value=34
     white_balance_temperature_auto (bool)   : default=1 value=1
                               gain (int)    : min=0 max=255 step=1 default=64 value=64
               power_line_frequency (menu)   : min=0 max=2 default=2 value=2
    				0: Disabled
    				1: 50 Hz
    				2: 60 Hz
          white_balance_temperature (int)    : min=2800 max=6500 step=1 default=4000 value=4000
                          sharpness (int)    : min=0 max=255 step=1 default=22 value=22
             backlight_compensation (int)    : min=0 max=1 step=1 default=0 value=0
                      exposure_auto (menu)   : min=0 max=3 default=3 value=3
    				1: Manual Mode
    				3: Aperture Priority Mode
                  exposure_absolute (int)    : min=3 max=2047 step=1 default=166 value=166
             exposure_auto_priority (bool)   : default=0 value=1
                       pan_absolute (int)    : min=-36000 max=36000 step=3600 default=0 value=0
                      tilt_absolute (int)    : min=-36000 max=36000 step=3600 default=0 value=0
                      zoom_absolute (int)    : min=1 max=5 step=1 default=1 value=1
    root@i3-3bc3 ~ # 
    
[/code]
