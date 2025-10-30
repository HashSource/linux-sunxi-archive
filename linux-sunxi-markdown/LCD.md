# LCD
Allwinner SoCs can output display signals to LCD panels. 
For devices with LCD displays, the resolution and timing values can be found in the [ FEX file][29771]. 
## Contents
  * [1 Software][29772]
    * [1.1 Mainline U-Boot][29773]
      * [1.1.1 FEX conversion rules][29774]
      * [1.1.2 Mainline Linux (panel-simple)][29775]
      * [1.1.3 Script for automated conversion][29776]
      * [1.1.4 Dithering test program][29777]
      * [1.1.5 Bulk automatic conversion of all FEX files from the sunxi-boards repository][29778]
  * [2 LCD panel][29779]
  * [3 Downloadable LCD panel datasheets][29780]

# Software
## Mainline U-Boot
Support for LCD displays is available in mainline U-boot, starting from release v2015.04. 
#### FEX conversion rules
The timing definitions and values are slightly different from the FEX files. The following is a translation table. 
Value | CONFIG_DM_VIDEO | CONFIG_VIDEO_LCD_MODE | FEX file values | Notes   
---|---|---|---|---  
Horizontal resolution (pixels) | hactive | x | lcd_x   
Vertical Resolution (pixels) | vactive | y | lcd_y   
Color depth / format | data-mapping | depth | lcd_frm:0 => depth:24 (to be verified)  
lcd_frm:1 => depth:18   
Pixel Clock (KHz) | clock-frequency (Hz) | pclk_khz | lcd_dclk_freq * 1000   
Horizontal Sync Length | hsync-len | hs | lcd_hv_hspw (with a minimum of 1) | [[1]][29781]  
Vertical Sync Length | vsync-len | vs | lcd_hv_vspw (with a minimum of 1) | [[1]][29781]  
Left Margin (Horizontal back porch) | hback-porch | le | lcd_hbp - hs | [[1]][29781]  
Right Margin (Horizontal front porch) | hfront-porch | ri | lcd_ht - lcd_x - lcd_hbp | [[1]][29781]  
Top Margin (Vertical back porch) | vback-porch | up | lcd_vbp - vs | [[1]][29781]  
Bottom Margin (Vertical front porch) | vfront-porch | lo | [[1]][29781]
[code] 
    sun[457i]: (lcd_vt / 2) - lcd_y - lcd_vbp
    sun8i: lcd_vt - lcd_y - lcd_vbp
    
[/code]  
u-boot SYNC flags | NA | sync:3 | NA   
u-boot VMODE flags | NA | vmode:0 | NA   
  1. ↑ [1.0][29782] [1.1][29783] [1.2][29784] [1.3][29785] [1.4][29786] [1.5][29787] [Definition of back porch / front porch / sync pulse based on Wikipedia][29788]

#### Mainline Linux (panel-simple)
In the mainline kernel, this file is in /drivers/gpu/drm/panel 
Conversion from LCD timing from u-boot configuration string to `struct drm_display_mode` in mainline kernel: 
[code] 
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:18,pclk_khz:100000,le:799,ri:260,up:15,lo:16,hs:1,vs:1,sync:3,vmode:0"
[/code]
[code] 
    static const struct drm_display_mode unknown_display = {
        .clock = 100000,                    // pclk_khz (FEX: lcd_dclk_freq * 1000)
        .hdisplay = 1024,                   // x (FEX: lcd_x)
        .hsync_start = 1024 + 260,          // x + ri
        .hsync_end = 1024 + 260 + 1,        // x + ri + hs
        .htotal = 1024 + 260 + 1 + 799,     // x + ri + hs + le (FEX: lcd_ht)
        .vdisplay = 768,                    // y (FEX: lcd_y)
        .vsync_start = 768 + 16,            // y + lo
        .vsync_end = 768 + 16 + 1,          // y + lo + vs
        .vtotal = 768 + 16 + 1 + 15,        // y + lo + vs + up (FEX: lcd_vt / 2)
        .vrefresh = 60,  // 
    };
    
[/code]
Example timing calculation from a INNOLUX EJ070NA-01J 7inch LVDS LCD datasheet (tested on DS167 board): 
[![7inch-LVDS-example.png][29789]][29790]
Corresponding u-boot configuration string: 
[code] 
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:18,pclk_khz:51000,le:22,ri:297,up:1,lo:33,hs:1,vs:1,sync:3,vmode:0"
[/code]
Note: Some values above such as pclk, le, ri,lo...etc have margins as seen from above datasheet. You may get perfectly fine picture if you set ri=296 instead of ri=297 here. You might experience visual artifacts if your settings are beyond defined limits in the datasheet. 
#### Script for automated conversion
The following ruby script takes fex file name as a command line parameter and produces the corresponding config line for u-boot according to the rules from the table above. 
**Here is the ruby script (click on the 'Expand' link to see it):**
[code] 
    #!/usr/bin/env ruby
    
    if !ARGV[0] || !File.exists?(ARGV[0]) then
      abort "Usage: ruby #{__FILE__} [fex_file_name]\n"
    end
    
    def parse_fex_section(filename, section)
      results = {}
      current_section = ""
      File.open(filename).each_line {|l|
        current_section = $1 if l =~ /^\[(.*?)\]/
        next if current_section != section
        results[$1] = $2.strip if l =~ /^(\S+)\s*\=\s*(.*)/
        results[$1] = $2.to_i if l =~ /^(\S+)\s*\=\s*(\d+)\s*$/
      }
      return results
    end
    
    def print_video_lcd_mode(lcd0_para, vt_div)
      x        = lcd0_para["lcd_x"]
      y        = lcd0_para["lcd_y"]
      depth    = { 0 => 24, 1 => 18 }[lcd0_para["lcd_frm"]]
      pclk_khz = lcd0_para["lcd_dclk_freq"] * 1000
      hs       = [1, (lcd0_para["lcd_hv_hspw"] || lcd0_para["lcd_hspw"])].max
      vs       = [1, (lcd0_para["lcd_hv_vspw"] || lcd0_para["lcd_vspw"])].max
      le       = lcd0_para["lcd_hbp"] - hs
      ri       = lcd0_para["lcd_ht"] - x - lcd0_para["lcd_hbp"]
      up       = lcd0_para["lcd_vbp"] - vs
      lo       = lcd0_para["lcd_vt"] / vt_div - y - lcd0_para["lcd_vbp"]
    
      abort "Unsupported 'lcd_frm' parameter" if !depth
    
      printf("CONFIG_VIDEO_LCD_MODE=\"" +
             "x:#{x},y:#{y},depth:#{depth},pclk_khz:#{pclk_khz}," +
             "le:#{le},ri:#{ri},up:#{up},lo:#{lo},hs:#{hs},vs:#{vs}," +
             "sync:3,vmode:0\"\n")
    end
    
    lcd0_para = parse_fex_section(ARGV[0], "lcd0_para")
    abort "Not a valid 'lcd0_para' section" if lcd0_para["lcd_used"] != 1
    
    printf("== for sun[457]i ==\n")
    print_video_lcd_mode(lcd0_para, 2)
    
    printf("\n== for sun[68]i ==\n")
    print_video_lcd_mode(lcd0_para, 1)
    
[/code]
#### Dithering test program
If in doubt regarding 18-bit vs. 24-bit depth, it is possible to compile and run on the device the following simple test program. It should show a smooth gradient picture. If the gradient looks blocky, then the depth most likely needs to be changed to 18. 
**Here is the C source code (click on the 'Expand' link to see it):**
[code] 
    /* gcc -O2 -o fbgradient fbgradient.c */
    
    #include <stdint.h>
    #include <stdio.h>
    #include <fcntl.h>
    #include <linux/fb.h>
    #include <sys/ioctl.h>
    #include <sys/mman.h>
    
    int main()
    {
        int fd, x, y;
        uint32_t *fb;
        struct fb_fix_screeninfo finfo;
        struct fb_var_screeninfo vinfo;
    
        if ((fd = open("/dev/fb0", O_RDWR)) == -1) {
            printf("Can't open /dev/fb0\n");
            return 1;
        }
    
        if (ioctl(fd, FBIOGET_FSCREENINFO, &finfo)) {
            printf("FBIOGET_FSCREENINFO failed\n");
            return 1;
        }
    
        if (ioctl(fd, FBIOGET_VSCREENINFO, &vinfo)) {
            printf("FBIOGET_VSCREENINFO failed\n");
            return 1;
        }
    
        if (vinfo.bits_per_pixel != 32) {
            printf("Only 32bpp framebuffer is supported\n");
            return 1;
        }
    
        fb = mmap(0, finfo.smem_len, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
        if (fb == (void *)-1) {
            printf("mmap failed\n");
            return 1;
        }
    
        for (y = 0; y < vinfo.yres; y++)
            for (x = 0; x < vinfo.xres; x++)
                fb[y * vinfo.xres + x] = (255 * x / vinfo.xres) * 0x000100 +
                                         (255 * y / vinfo.yres) * 0x010001;
    
        return 0;
    }
    
[/code]
#### Bulk automatic conversion of all FEX files from the [sunxi-boards][29791] repository
The results of automatic FEX files conversion are listed in the table below. The CONFIG_VIDEO_LCD_MODE line should be accurate and calculated exactly as described in the first section of this page. But the GPIO settings need careful human review. "Green" settings are likely to be usable as-is. "Yellow" most definitely need some tweaks. "Orange" are impossible to support with the current u-boot code. 
CONFIG_VIDEO_LCD_PANEL_LVDS conversion rules - <http://lists.denx.de/pipermail/u-boot/2015-January/200168.html>
CONFIG_VIDEO_LCD_DCLK_PHASE conversion rules - <http://lists.denx.de/pipermail/u-boot/2015-January/201751.html>
SoC  | Device info  | FEX file  | CONFIG_VIDEO_LCD_MODE u-boot settings   
---|---|---|---  
[A20][29792] |  | [Mele_M3.fex][29793] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Olimex_A10-OLinuXino-Lime][29795] | [a10-olinuxino-lime.fex][29796] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10s][29797] | [Olimex_A10s-OLinuXino-Micro][29798] | [a10s-olinuxino-m.fex][29799] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:16,ri:209,up:22,lo:24,hs:30,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PB9"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10s][29797] |  | [a10s-olinuxino-m-lcd10.fex][29800] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:18,pclk_khz:45000,le:150,ri:16,up:21,lo:2,hs:10,vs:2,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PB9"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10s][29797] |  | [a10s-olinuxino-m-lcd7.fex][29801] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:16,ri:209,up:22,lo:22,hs:30,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PB9"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [Olimex_A13-OLinuXino][29803] | [a13-olinuxino.fex][29804] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:600,depth:18,pclk_khz:40000,le:88,ri:40,up:19,lo:5,hs:128,vs:4,sync:3,vmode:0"
    
[/code]  
[A13][29802] |  | [a13-olinuxino-lcd10.fex][29805] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:18,pclk_khz:45000,le:150,ri:16,up:21,lo:2,hs:10,vs:2,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] |  | [a13-olinuxino-lcd7.fex][29806] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:16,ri:209,up:22,lo:22,hs:30,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [Olimex_A13-OLinuXino-Micro][29807] | [a13-olinuxinom.fex][29808] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:600,depth:18,pclk_khz:40000,le:88,ri:40,up:19,lo:5,hs:128,vs:4,sync:3,vmode:0"
    
[/code]  
[A13][29802] |  | [a13-olinuxinom-lcd10.fex][29809] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:18,pclk_khz:45000,le:150,ri:16,up:21,lo:2,hs:10,vs:2,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PB10"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] |  | [a13-olinuxinom-lcd7.fex][29810] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:16,ri:209,up:22,lo:22,hs:30,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PB10"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] |  | [a13_mid.fex][29811] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:39,ri:88,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Olimex_A20-OLinuXino-Lime][29812] | [a20-olinuxino_lime.fex][29813] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:16,ri:209,up:22,lo:22,hs:30,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Olimex_A20-OLinuXino-Lime2][29814] | [a20-olinuxino_lime2.fex][29815] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:16,ri:209,up:22,lo:22,hs:30,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Olimex_A20-OLinuXino-Micro][29816] | [a20-olinuxino_micro.fex][29817] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [a20-olinuxino_micro-lcd10.fex][29818] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:18,pclk_khz:45000,le:150,ri:16,up:21,lo:2,hs:10,vs:2,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [a20-olinuxino_micro-lcd7.fex][29819] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:16,ri:209,up:22,lo:22,hs:30,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [A70x][29820] | [a70x.fex][29821] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Ainol_AW1][29822] | [ainol_aw1.fex][29823] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:40000,le:87,ri:112,up:38,lo:141,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [Ampe_A76][29824] | [ampe_a76.fex][29825] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:45,ri:82,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [banana_pi_35lcd.fex][29826] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:320,y:240,depth:24,pclk_khz:7000,le:38,ri:20,up:15,lo:4,hs:30,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH12"
    CONFIG_VIDEO_LCD_BL_EN="PH8"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [banana_pi_5lcd.fex][29827] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:30000,le:40,ri:40,up:29,lo:13,hs:48,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH12"
    CONFIG_VIDEO_LCD_BL_EN="PH8"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [banana_pi_7lcd.fex][29828] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:24,pclk_khz:55000,le:100,ri:170,up:10,lo:15,hs:50,vs:10,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH12"
    CONFIG_VIDEO_LCD_BL_EN="PH8"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [banana_pro_35lcd.fex][29829] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:320,y:240,depth:24,pclk_khz:7000,le:38,ri:20,up:15,lo:4,hs:30,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH12"
    CONFIG_VIDEO_LCD_BL_EN="PH8"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [banana_pro_5lcd.fex][29830] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:30000,le:40,ri:40,up:29,lo:13,hs:48,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH12"
    CONFIG_VIDEO_LCD_BL_EN="PH8"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [banana_pro_7lcd.fex][29831] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:24,pclk_khz:55000,le:100,ri:170,up:10,lo:15,hs:50,vs:10,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH12"
    CONFIG_VIDEO_LCD_BL_EN="PH8"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [cherry728.fex][29832] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:24,pclk_khz:51000,le:45,ri:274,up:22,lo:12,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH2"
    CONFIG_VIDEO_LCD_BL_EN="PH9"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [chuwi-v7-cw0825.fex][29833] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:24,pclk_khz:51000,le:19,ri:300,up:6,lo:31,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    VIDEO_LCD_HITACHI_TX18D42VM=y
    VIDEO_LCD_SPI_CS="PA0"
    VIDEO_LCD_SPI_SCLK="PA1"
    VIDEO_LCD_SPI_MOSI="PA2"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Coby_MID7042][29834] | [coby_mid7042.fex][29835] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:214,ri:40,up:33,lo:11,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [coby_mid8042.fex][29836] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:600,depth:18,pclk_khz:45000,le:85,ri:170,up:38,lo:11,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [coby_mid9742.fex][29837] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:18,pclk_khz:100000,le:479,ri:544,up:5,lo:26,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Cubietech_Cubieboard][29838] | [cubieboard.fex][29839] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [cubieboard_512.fex][29840] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Cubietech_Cubietruck][29841] | [cubietruck.fex][29842] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [dns_m82.fex][29843] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:24,pclk_khz:64000,le:198,ri:120,up:21,lo:15,hs:2,vs:2,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [Forfun_Q88DB][29844] | [forfun_q88db.fex][29845] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:87,ri:40,up:31,lo:13,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Topwise_A721][29846] | [gooseberry_a721.fex][29847] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [h6.fex][29848] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:24,pclk_khz:45000,le:159,ri:16,up:22,lo:12,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Miniand_Hackberry][29849] | [hackberry.fex][29850] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [HDB_MID_S906][29851] | [hbd_mid_s906.fex][29852] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:42000,le:110,ri:386,up:22,lo:130,hs:48,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [HSG_H702][29853] | [hsg_h702.fex][29854] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:39000,le:5,ri:83,up:20,lo:22,hs:40,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Hyundai_A7][29855] | [hyundai_a7.fex][29856] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:40,ri:40,up:29,lo:13,hs:48,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Hyundai_A7HD][29857] | [hyundai_a7hd.fex][29858] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:24,pclk_khz:51000,le:45,ri:274,up:22,lo:12,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH2"
    CONFIG_VIDEO_LCD_BL_EN="PH9"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [inet-k970.fex][29859] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:18,pclk_khz:65000,le:120,ri:180,up:22,lo:13,hs:20,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Inet_97f][29860] | [inet97f-ii.fex][29861] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [Inet_86vs][29862] | [inet_86vs.fex][29863] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [Inet_86vz][29864] | [inet_86vz.fex][29865] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Inet_k70hc][29866] | [inet_k70hc.fex][29867] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:18,pclk_khz:51000,le:138,ri:162,up:22,lo:10,hs:20,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Yonnet_Interra-3][29868] | [interra-3.fex][29869] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1280,y:800,depth:18,pclk_khz:69000,le:19,ri:118,up:9,lo:6,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Inet_k100c][29870] | [k1001l1c.fex][29871] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:24,pclk_khz:52000,le:32,ri:287,up:22,lo:12,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Kurio_7S][29872] | [kurio_7s.fex][29873] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:24,pclk_khz:51000,le:157,ri:160,up:20,lo:12,hs:3,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] |  | [ltm7.fex][29874] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [MarsBoard_A10][29875] | [marsboard_a10.fex][29876] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Merrii_Hummingbird_A20][29877] | [merrii_hummingbird_a20.fex][29878] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH11"
    CONFIG_VIDEO_LCD_BL_EN="PH12"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Pineriver_H24][29879] | [mini-x.fex][29880] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [MSI_Primo73][29881] | [msi_primo73.fex][29882] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:18,pclk_khz:60000,le:60,ri:160,up:13,lo:12,hs:100,vs:10,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] |  | [myaudio-708m.fex][29883] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:45,ri:210,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Olimex_A20-SOM][29884] | [olimex_a20_som.fex][29885] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1366,y:768,depth:18,pclk_khz:70000,le:53,ri:20,up:22,lo:17,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [LinkSprite_pcDuino][29886] | [pcduino.fex][29887] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [pov_protab2_ips9.fex][29888] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:18,pclk_khz:100000,le:480,ri:260,up:6,lo:16,hs:320,vs:10,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [pov_protab2_ips_3g.fex][29889] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:18,pclk_khz:100000,le:480,ri:260,up:6,lo:16,hs:320,vs:10,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [Q8][29890] | [pov_tab_p703.fex][29891] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:45,ri:210,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [Prestigio_PMP3670B][29892] | [prestigio_pmp3670b.fex][29893] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:30000,le:45,ri:79,up:22,lo:13,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [Sanei_N90][29894] | [sanei_n90.fex][29895] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:18,pclk_khz:100000,le:480,ri:260,up:6,lo:16,hs:320,vs:10,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [XW711][29896] | [szenio_1207c4.fex][29897] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:45,ri:82,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] | [T702A][29898] | [t702a.fex][29899] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [TZX-Q8-713B6][29900] | [tzx-q8-713b6.fex][29901] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:87,ri:40,up:31,lo:13,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [TZX-Q8-713B7][29902] | [tzx-q8-713b7.fex][29903] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:87,ri:40,up:31,lo:13,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Wexler_TAB_7200][29904] | [wexler_tab_7200.fex][29905] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:210,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A13][29802] | [Along_rt713][29906] | [xzpad700.fex][29907] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:2,ri:78,up:29,lo:13,hs:48,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="AXP0-0"
    CONFIG_VIDEO_LCD_BL_EN="AXP0-1"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [yarvik_tab260.fex][29908] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:24,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A20][29792] | [Yones_Toptech_BD1078][29909] | [yonestoptech_bd1078.fex][29910] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:24,pclk_khz:63000,le:32,ri:287,up:22,lo:12,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A10][29794] |  | [eoma68_a10.fex][29911] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1366,y:768,depth:18,pclk_khz:75000,le:12,ri:171,up:12,lo:25,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    # warning: contradicting 'lcd_pwm_used' and 'lcd_pwm_not_used'
    
[/code]  
[A31][29912] | [Merrii_Hummingbird_A31][29913] | [hummingbird_a31.fex][29914] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:65000,le:45,ri:82,up:22,lo:547,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    # warning: could not decode 'lcd_power' (port:power2<1><0><default><1>)
    CONFIG_VIDEO_LCD_BL_EN="PM1"
    CONFIG_VIDEO_LCD_BL_PWM="PH13"
    
[/code]  
[A20][29792] | [ICOU_Fatty_I][29915] | [icou_fatty_i.fex][29916] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:768,y:1024,depth:18,pclk_khz:66000,le:56,ri:60,up:30,lo:36,hs:64,vs:50,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    # warning: 'lcd_gpio_0' = 'port:PA06<1><0><default><1>'
    # warning: 'lcd_gpio_1' = 'port:PA07<1><0><default><1>'
    # warning: 'lcd_gpio_2' = 'port:PH24<1><0><default><0>'
    # warning: 'lcd_gpio_3' = 'port:PA05<1><0><default><1>'
    # warning: 'lcd_gpio_4' = 'port:PH23<1><0><default><0>'
    # warning: 'lcd_gpio_5' = 'port:PH22<1><0><default><0>'
    
[/code]  
[A10][29794] | [Inet_3fbt][29917] | [inet_3fbt.fex][29918] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:24,pclk_khz:100000,le:799,ri:260,up:15,lo:16,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    # warning: unsupported 'lcd_lvds_mode' : 1
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A23][29919] |  | [ippo_q8h_v1.0.fex][29920] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    # warning: could not decode 'lcd_power' (port:power2<1><0><default><1>)
    CONFIG_VIDEO_LCD_BL_EN="PH6"
    CONFIG_VIDEO_LCD_BL_PWM="PH0"
    # warning: 'lcd_gpio_0' = 'port:PH07<1><0><default><1>'
    
[/code]  
[A23][29919] |  | [ippo_q8h_v1.2.fex][29921] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:87,ri:167,up:31,lo:13,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    # warning: could not decode 'lcd_power' (port:power2<1><0><default><1>)
    CONFIG_VIDEO_LCD_BL_EN="PH6"
    CONFIG_VIDEO_LCD_BL_PWM="PH0"
    # warning: 'lcd_gpio_0' = 'port:PH07<1><0><default><1>'
    
[/code]  
[A23][29919] |  | [ippo_q8h_v2.fex][29922] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:45,ri:209,up:22,lo:22,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    # warning: could not decode 'lcd_power' (port:power2<1><0><default><1>)
    CONFIG_VIDEO_LCD_BL_EN="PH6"
    CONFIG_VIDEO_LCD_BL_PWM="PH0"
    # warning: 'lcd_gpio_0' = 'port:PH07<1><0><default><1>'
    
[/code]  
[A23][29919] | [Ippo_q8h][29923] | [ippo_q8h_v5.fex][29924] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:480,depth:18,pclk_khz:33000,le:87,ri:168,up:31,lo:13,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    # warning: could not decode 'lcd_power' (port:power2<1><0><default><1>)
    CONFIG_VIDEO_LCD_BL_EN="PH6"
    CONFIG_VIDEO_LCD_BL_PWM="PH0"
    # warning: 'lcd_gpio_0' = 'port:PH07<1><0><default><1>'
    
[/code]  
[A20][29792] | [Itead_ibox][29925] | [iteaduino_plus_a20.fex][29926] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:18,pclk_khz:51000,le:138,ri:162,up:22,lo:10,hs:20,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    # warning: contradicting 'lcd_pwm_used' and 'lcd_pwm_not_used'
    
[/code]  
[A20][29792] |  | [merrii_m2.fex][29927] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1920,y:1080,depth:24,pclk_khz:148000,le:19,ri:260,up:19,lo:25,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    # warning: unsupported 'lcd_lvds_ch' : 1
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A31s][29928] | [MSI_Primo81][29929] | [msi_primo81.fex][29930] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:768,y:1024,depth:18,pclk_khz:66000,le:56,ri:60,up:30,lo:36,hs:64,vs:50,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    # warning: could not decode 'lcd_power' (port:power2<1><0><default><1>)
    CONFIG_VIDEO_LCD_BL_EN="PA25"
    CONFIG_VIDEO_LCD_BL_PWM="PH13"
    # warning: 'lcd_gpio_0' = 'port:PH10<1><0><2><1>'
    # warning: 'lcd_gpio_1' = 'port:PH11<1><0><2><1>'
    # warning: 'lcd_gpio_2' = 'port:PA26<1><0><2><1>'
    # warning: 'lcd_gpio_3' = 'port:PH09<1><0><2><1>'
    
[/code]  
[A31s][29928] |  | [sinlinx_a31s.fex][29931] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:18,pclk_khz:66000,le:90,ri:160,up:3,lo:127,hs:70,vs:20,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    # warning: could not decode 'lcd_power' (port:power2<1><0><default><1>)
    CONFIG_VIDEO_LCD_BL_EN="PA25"
    CONFIG_VIDEO_LCD_BL_PWM="PH13"
    
[/code]  
[A31s][29928] | [Yones_Toptech_BS1078][29932] | [yonestoptech_bs1078.fex][29933] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:600,depth:24,pclk_khz:70000,le:120,ri:180,up:17,lo:15,hs:20,vs:3,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=0
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    # warning: could not decode 'lcd_power' (port:power2<1><0><default><1>)
    CONFIG_VIDEO_LCD_BL_EN="PA25"
    CONFIG_VIDEO_LCD_BL_PWM="PH13"
    # warning: 'lcd_gpio_0' = 'port:PH10<1><0><2><1>'
    # warning: 'lcd_gpio_1' = 'port:PH11<1><0><2><1>'
    # warning: 'lcd_gpio_2' = 'port:PA23<1><0><2><0>'
    # warning: 'lcd_gpio_3' = 'port:PH09<1><0><2><1>'
    
[/code]  
[A10][29794] | [Gemei_G9][29934] | [zatab.fex][29935] | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:24,pclk_khz:100000,le:799,ri:260,up:15,lo:16,hs:1,vs:1,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_PANEL_LVDS=y
    # warning: unsupported 'lcd_lvds_mode' : 1
    CONFIG_VIDEO_LCD_POWER="PH8"
    CONFIG_VIDEO_LCD_BL_EN="PH7"
    CONFIG_VIDEO_LCD_BL_PWM="PB2"
    
[/code]  
[A31][29912] |  | [A31_EVB.fex][29936] | 
[code]
    # warning: unsupported 'lcd_if' : 5 (LCD_IF_EDP)
    
[/code]  
[A10][29794] | [Itead_Iteaduino_Plus][29937] | [iteaduino_plus_a10.fex][29938] | 
[code]
    # warning: unsupported 'lcd_frm' : 
    
[/code]  
# LCD panel
LCD LVDS panels can be found on old notebook or desktop monitor. 
Model  | Inch  | u-boot settings   
---|---|---  
QD17EL07  | 17"  | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1280,y:1024,depth:24,pclk_khz:108000,le:56,ri:60,up:29,lo:3,hs:10,vs:10,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=1
    
[/code]  
LTN150XB  | 15"  | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1024,y:768,depth:18,pclk_khz:65000,le:88,ri:24,up:29,lo:3,hs:136,vs:6,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=1
    
[/code]  
B150XG01  
LTD154EX0K  | 15" 16:9  | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:1280,y:800,depth:18,pclk_khz:71100,le:88,ri:48,up:15,lo:2,hs:32,vs:6,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=1
    
[/code]  
HSD121PS11  | 12.1"  | 
[code]
    CONFIG_VIDEO_LCD_MODE="x:800,y:600,depth:18,pclk_khz:40000,le:88,ri:40,up:23,lo:1,hs:128,vs:4,sync:3,vmode:0"
    CONFIG_VIDEO_LCD_DCLK_PHASE=1
    
[/code]  
  
Monitor with vertical size bigger 768 px and 24bit deep need u-boot patch to add lvds dual channel support. 
# Downloadable LCD panel datasheets
Some of the LCD panel web shops are kind enough to conveniently provide freely downloadable collections of datasheets: 
  * <http://yslcd.com.tw/Docs.aspx>
  * <http://www.beyondinfinite.com/library.html>
