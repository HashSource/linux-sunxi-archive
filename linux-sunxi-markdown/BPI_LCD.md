# BPI LCD
The banana Pi was delivered with several different RGB LCD modules. 
# 3.5" (Bpi LCD 1003)
This is a 3.5" RGB TFT display with 320x240 resolution. 
This happens to be the displays used in the FOSDEM video boxes, and [ PaulK][8428] has kindly made this work. 
## Mainline U-boot
While these are destined for upstream, [ PaulK][8428] is currently tracking the relevant patches on [his own personal repo in the bananapi-lcd-3.5 branch][8429]. 
Build u-boot with the _Bananapi_LCD_BL035_defconfig_
## Mainline Kernel
While these are destined for upstream, [ PaulK][8428] is currently tracking the relevant patches on [his own personal repo in the bananapi-lcd-3.5 branch][8430]. 
Build the kernel, with _sunxi_defconfig_ and use the _sun7i-a20-bananapi.dtb_
