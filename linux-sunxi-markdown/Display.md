# Display
[![MBOX icon important.png][16915]][16916] | This page provides outdated set of instructions and needs to be updated to reflect current status.   
---|---  
## Contents
  * [1 Current issues][16917]
    * [1.1 A20/sun4i Broken CLK handling][16918]
  * [2 Various tips and tricks][16919]
    * [2.1 Framebuffer console at boot][16920]
    * [2.2 Changing resolution][16921]
      * [2.2.1 legacy kernel][16922]
      * [2.2.2 mainline kernel][16923]
    * [2.3 Framebuffer tips][16924]
      * [2.3.1 Blanking timeout][16925]
      * [2.3.2 Unblank][16926]
      * [2.3.3 Hide cursor][16927]
      * [2.3.4 Rotation][16928]
    * [2.4 HDMI][16929]
      * [2.4.1 boot.scr][16930]
      * [2.4.2 script.bin/fex file][16931]
    * [2.5 LVDS][16932]
    * [2.6 VGA][16933]
    * [2.7 TV/CVBS][16934]
    * [2.8 Using two displays][16935]
    * [2.9 Using hardware scaler][16936]
    * [2.10 Driving LCDs][16937]
  * [3 See Also][16938]

# Current issues
## A20/sun4i Broken CLK handling
The current mainline setup seems to prefer to set _all_ display related devices to depend on PLL3 (aka pll-video0). For both pipelines, and including the gpu. 
If u-boot does not have HDMI enabled, the clock halving bit on the hdmi pads is not set, and then the logic goes awry. In case of a 1280x1024/108MHz secondary pipeline resolution, this results in pll3 being set to half the dotclock, with only the hdmi-tmds clock being set to the target resolution. Here is the output of debugfs/clk-summary for pll-video0 (pll-video1/PLL7 is unused): 
[code] 
                                      enable  prepare  protect                                duty
       clock                          count    count    count        rate   accuracy phase  cycle
    ---------------------------------------------------------------------------------------------
           pll-video0                     6        6        2    54000000          0     0  50000
              hdmi1                       0        0        0    54000000          0     0  50000
              gpu                         0        0        0    54000000          0     0  50000
              hdmi                        1        1        0    54000000          0     0  50000
              tcon1-ch1-sclk2             1        1        1    54000000          0     0  50000
                 tcon1-ch1-sclk1          1        1        1    54000000          0     0  50000
              tcon0-ch1-sclk2             0        0        0    54000000          0     0  50000
                 tcon0-ch1-sclk1          0        0        0    54000000          0     0  50000
              tvd-sclk2                   0        0        0    54000000          0     0  50000
                 tvd-sclk1                0        0        0    54000000          0     0  50000
              csi-sclk                    0        0        0    54000000          0     0  50000
              tcon1-ch0-sclk              1        1        0    54000000          0     0  50000
                 tcon1-pixel-clock        0        0        0    54000000          0     0  50000
              tcon0-ch0-sclk              2        2        1    54000000          0     0  50000
                 tcon0-pixel-clock        1        1        1     9000000          0     0  50000
              de-mp                       0        0        0    54000000          0     0  50000
              de-fe1                      0        0        0    54000000          0     0  50000
              de-fe0                      0        0        0    54000000          0     0  50000
              de-be1                      1        1        0    54000000          0     0  50000
              pll-video0-2x               1        1        0   108000000          0     0  50000
                 hdmi-tmds                2        2        0   108000000          0     0  50000
                    hdmi-ddc              1        1        0       96428          0     0  50000
[/code]
  

# Various tips and tricks
When you are using a ready made image for your device your display should be configured automatically. 
In script.bin it is defined what display output is used and what hardware lines are used for connecting the output. 
On [kernel arguments][16939] you can specify the video mode used on the output or override autodetection on outputs that support EDID. 
  

## Framebuffer console at boot
To see boot traces you need to put all display related modules into linux kernel (3.4 branch ATM) : 
[code] 
    CONFIG_FB_SUNXI=y
    CONFIG_FB_SUNXI_LCD=y
    CONFIG_FB_SUNXI_HDMI=y
    
    CONFIG_FRAMEBUFFER_CONSOLE=y
    CONFIG_FONT_8x8=y
    CONFIG_FONT_8x16=y
    
[/code]
Then change u-boot config console=xxx parameter to tty0. If you want to still use a serial console you can define multiple consoles. For example "console=ttyS0,115200 console=tty0". 
  

## Changing resolution
### legacy kernel
The initial display resolution at boot time is defined in script.bin (fex-file), and can be overridden by [kernel command line options][16939]. 
But you can change it afterward by using this tool from doozan forum: 
[code] 
    http://forum.doozan.com/read.php?6,9002
    https://github.com/doozan/a10-tools/blob/master/a10_display.c
    
[/code]
Tool changes display timings for wanted resolution. After that you'll need to set correct resolution with fbset -xres xxx -yres xxx 
There is also a utility called a10disp that requires that version 1.0 or later of the sunxi kernel display driver is available (linux-sunxi 3.4.43 or later). It can be used to show information about the current display mode, change the resolution and color depth of HDMI modes, and switch between LCD and HDMI output. It can be found at <http://www.github.com/hglm/a10disp.git>. 
### mainline kernel
it should be possible to change mode in uboot by setting variable, ie.: 
[code] 
    setenv video-mode sunxi:1024x768-24@50,monitor=dvi,hpd=0,edid=0
    
[/code]
(but somehow it doesnt work in boot.cmd, hardcoding it in drivers/video/videomodes.c::video_get_video_mode() works as expected). 
params are described in [README.video][16940]
## Framebuffer tips
### Blanking timeout
The framebuffer has a default blank screen saver. The timeout (in seconds) can be changed or disabled (0) with a kernel parameter: 
[code] 
    consoleblank=0
    
[/code]
### Unblank
To blank or unblank a framebuffer, you can set 0 or 1 in this sysfs entry: 
[code] 
    /sys/class/graphics/fb0/blank
    
[/code]
### Hide cursor
If you are running a console on your framebuffer, you can hide the cursor with a kernel parameter: 
[code] 
    vt.global_cursor_default=0
    
[/code]
It can be changed at runtime by setting 0 or 1 in this sysfs entry: 
[code] 
    /sys/class/graphics/fbcon/cursor_blink
    
[/code]
All these parameters can be changed with setterm command. 
### Rotation
You can rotate the framebuffer by supplying fbcon=rotate:<n> kernel parameter, where n can be one of the following. 
  * 0 - normal orientation (0 degree)
  * 1 - clockwise orientation (90 degrees)
  * 2 - upside down orientation (180 degrees)
  * 3 - counterclockwise orientation (270 degrees)

Alternatively you could echo <n> to 
[code] 
    /sys/class/graphics/fbcon/rotate
    
[/code]
after kernel has booted. For more see Documentation/fb/fbcon.txt in kernel tree. 
## HDMI
If you are using a device with HDMI and have proper script.bin for your device setting up display is as simple as adding _disp.screen0_output_mode=EDID_ to your kernel command line in boot.scr file. You can specify a fixed mode like _disp.screen0_output_mode=1280x1024p60_ or a fallback in case EDID did not work _disp.screen0_output_mode=EDID:1280x1024p60_. The supported fallback display modes are currently hardcoded in the disp driver. Looking at the clock table in <https://github.com/linux-sunxi/linux-sunxi/blob/sunxi-3.0/drivers/video/sunxi/disp/disp_clk.c> might be helpful. 
Warning: some monitors require _hdmi.audio=EDID:0_ option in the kernel command line to work correctly! Otherwise they are confused by the audio data embedded in the HDMI signal. The 1680x1050 monitors are known to be particularly bad in this respect. 
### boot.scr
[code] 
    # fixed mode
    setenv bootargs console=tty0 hdmi.audio=EDID:0 disp.screen0_output_mode=1280x720p60 root=/dev/mmcblk0p1 rootwait panic=10
    
    # try EDID first, if it did not work fallback to specific output mode
    setenv bootargs console=tty0 hdmi.audio=EDID:0 disp.screen0_output_mode=EDID:1280x720p60 root=/dev/mmcblk0p1 rootwait panic=10
    
[/code]
To generate a new boot.scr you need to edit boot.cmd file and then make a new boot.scr binary file. 
[code] 
    mkimage -C none -A arm -T script -d <boot.cmd-file> boot.scr
    
[/code]
  

### script.bin/fex file
The settings in the [disp_init] section of the script.bin/fex file define the display output enabled at boot. 
An example configuration for HDMI: 
[code] 
    [disp_init]
    disp_init_enable = 1
    disp_mode = 0
    screen0_output_type = 3
    screen0_output_mode = 4
    fb0_framebuffer_num = 2
    fb0_format = 10
    fb0_pixel_sequence = 0
    fb0_scaler_mode_enable = 0
    
[/code]
  * disp_mode selects single-screen output or different dual screen modes. Generally this is 0, which means use screen0 with fb0 (one screen).
  * screen0_output_type = 3 means HDMI output.
  * screen0_output_mode selects the video/monitor mode to use (resolution and refresh rate). See the table in the [Fex guide][16941].
  * fb0_framebuffer_num selects the number of buffers for fb0, generally you need 2 or more for video acceleration or Mali (3D), 3 is better.
  * fb0_format and fb0_pixel_sequence determine the pixel format in the framebuffer. The above example (values of 10 and 0) selects the most common variant of 32bpp truecolor (ARGB).
  * fb0_scaler_mode_enable selects whether the scaler should be enabled. Enabling it does not really scale pixels, it configures the scaler to scale pixels 1-to-1 which can fix screen refresh-related problems at 1080p resolution. See the section below.

Similar parameter are defined for screen1 (which is usually disabled in practice). 
See the [Fex guide][16942] for a more detailed description. 
## LVDS
sunxi socs (A10 A13 A20 A31s) use same LCDC that support output of lvds display signals throught port D of SOC. 
Pin  | Function  | Note   
---|---|---  
PD0  | LVDS0_VP0  |   
PD1  | LVDS0_VN0  |   
PD2  | LVDS0_VP1  |   
PD3  | LVDS0_VN1  |   
PD4  | LVDS0_VP2  |   
PD5  | LVDS0_VN2  |   
PD6  | LVDS0_VPC  |   
PD7  | LVDS0_VNC  |   
PD8  | LVDS0_VP3  |   
PD9  | LVDS0_VN3  |   
PD10  | LVDS1_VP0  | Used only in Dual Channel   
PD11  | LVDS1_VN0  | Used only in Dual Channel   
PD12  | LVDS1_VP1  | Used only in Dual Channel   
PD13  | LVDS1_VN1  | Used only in Dual Channel   
PD14  | LVDS1_VP2  | Used only in Dual Channel   
PD15  | LVDS1_VN2  | Used only in Dual Channel   
PD16  | LVDS1_VPC  | Used only in Dual Channel   
PD17  | LVDS1_VNC  | Used only in Dual Channel   
PD18  | LVDS1_VP3  | Used only in Dual Channel   
PD19  | LVDS1_VN3  | Used only in Dual Channel   
See: [Cubieboard/LVDS][16943]
## VGA
TBD 
  

## TV/CVBS
The composite output can be used by configuring a screen in TV mode (2).  
Then DAC #3 must be configured for composite (0).  
Be sure to choose the right mode for your TV (PAL = 11 / NTSC = 14). 
[Fex][16942] example: 
[code] 
     [disp_init]
     disp_init_enable = 1
     disp_mode = 0
     screen0_output_type = 2
     screen0_output_mode = 11
     [tv_out_dac_para]
     dac_used = 1
     dac3_src = 0
    
[/code]
## Using two displays
A10 has support for using two independent display outputs. Depending on board wiring and other hardware limitations not all output combinations may be possible. More information is available on our [Dual Monitor Support][16944] page. 
## Using hardware scaler
In some configurations turning the hardware scaler on or off in script.bin solves some issues. 
More specifcally. when driving a high bandwidth screen resolution (specifically 1920x1080 (1080p) with 32bpp at 60Hz) the Allwinner chip may sometimes be starved for memory bandwidth for refreshing the screen, especially if other components on the chip are utilizing a lot of memory bandwidth. The symptom is a "wavy screen" with most of the screen scanlines bouncing up and down quickly. This has been observed on an A10 in the Xorg environment (small bouncing), and on an A20 in X when running GLES accelerated Mali applications (heavy bouncing), especially with a large window size. Turning on "scaler mode" seems to solve the issue in both cases (sometimes it can be enough to lower the refresh rate, for example use 1080p at 50 Hz instead of 60 Hz). Scaler mode can be enabled by changing script.bin (fb0_scaler_mode_enable = 1) or using a runtime mode-setting utility such as [[[1]][16945]]. 
## Driving LCDs
Tablet LCDs can generally may be made to work provided that the LCD parameters in script.bin are correct (see [Fex guide LCD parameter section][16946]). Usually these will be need to be obtained from the script.bin in Android's bootloader partition (/dev/block/nanda). Normally you would use Android's script.bin (converted to .fex) as a base and adopt it for linux-sunxi. 
Tthe script.bin settings in the [disp_init] section (see [Fex guide][16941]) for Android tablets are usually configured to boot with screen0 on the LCD. A fex file configured to boot from LCD might like this: 
[code] 
    [disp_init]
    disp_init_enable = 1
    disp_mode = 0
    screen0_output_type = 1
    screen0_output_mode = 4
    screen1_output_type = 1
    screen1_output_mode = 4
    fb0_framebuffer_num = 2
    fb0_format = 10
    fb0_pixel_sequence = 0
    fb0_scaler_mode_enable = 0
    fb0_width = 0
    fb0_height = 0
    fb1_framebuffer_num = 2
    fb1_format = 10
    fb1_pixel_sequence = 0
    fb1_scaler_mode_enable = 0
    fb1_width = 0
    fb1_height = 0
    
[/code]
screen0_output_type = 1 means LCD. The screen0_output_mode probably does not matter when the output type is LCD, since the LCD resolution is defined in the LCD parameter section. 
Switching between LCD and HDMI at runtime works using a utility such as <http://www.github.com/hglm/a10disp.git>. Driving two screens (such as LCD and HDMI) at the same time (which the hardware supports) has not been extensively tested or verified. 
  

# See Also
  * [IOCTLs for Allwinners disp driver.][16947]
  * [Setting up Xorg][16948]
  * [Mali binary driver][16949]
  * [Hardware Media decoding][16950]
