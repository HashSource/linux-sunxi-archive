# Boot.axf
## Contents
  * [1 General][10339]
  * [2 Boot partition structure][10340]
  * [3 Configuration][10341]
  * [4 Source code][10342]

# General
boot.axf is the final allwinner bootloader. It can either load a u-boot image, or a stripped linux kernel directly, called bImage by the build scripts. Manually building is possible using _arm-linux-gnueabi-objcopy -R .note.gnu.build-id -S -O binary vmlinux output/bImage_ for example. 
# Boot partition structure
The default structure of the boot-partition, which boot.axf uses to load various data from. An example layout can be found on [github][10343]. 
# Configuration
The booting configuration is defined by the ini-file linux/linux.ini: 
[code] 
    [segment]
    img_name = c:\linux\bImage
    img_size = 0x2000000
    img_base = 0x40008000
    
    [segment]
    img_name = c:\linux\params
    img_size = 0x100
    img_base = 0x40000100
    
    [script_info]
    script_base = 0x43000000
    script_size = 0x10000
    
    [logo_info]
    logo_name = c:\linux\android.bmp
    logo_address = 0x48000000
    logo_show = 1
    
[/code]
Note: yes, they actually use DOS paths and partition names, and most likely internally translate those. 
boot.axf can also "chainload" u-boot, replacing the bImage portion by: 
[code] 
    [segment]
    img_name = c:\linux\u-boot.bin
    img_size = 0x80000
    img_base = 0x4a000000
    
[/code]
This is what is done on ICS firmwares on tablets, where what is booted is an Android boot.img by u-boot. 
# Source code
There is a source tree for building boot.axf available at [this repository][10344]. Use at your own risk, as it's very obscure and not well known.
