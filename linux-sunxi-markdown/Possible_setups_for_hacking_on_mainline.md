# Possible setups for hacking on mainline
# Booting kernels quickly
If hacking on the kernel we are interested in booting it as fast as possible. Also it's desirable to be able to boot legacy kernel (sunxi-3.4) and mainline with the same U-Boot. Writing kernels to an SD card is not an option, since SD card and/or slot can easily wear out. Instead you can setup network boot. First please read [How to boot the A10 over the network][45538], then armed with general knowledge adapt the following recipe. It is assumed the network is already configured in U-Boot. 
  * Mainline kernel

[code] 
    tftp 0x46000000 ml/uImage
    tftp 0x49000000 ml/sun4i-a10-a1000.dtb
    env set fdt_high ffffffff
    bootm 0x46000000 - 0x49000000
    
[/code]
  * Legacy kernel

[code] 
    tftp 0x43000000 aw/script.bin
    tftp 0x48000000 aw/uImage
    bootm 0x48000000
    
[/code]
Note, you can set up a shortcut for all of the commands above, for example a shortcut for mainline 
[code] 
    setenv ml "tftp 0x46000000 ml/uImage && tftp 0x49000000 ml/sun4i-a10-a1000.dtb && env set fdt_high ffffffff && bootm 0x46000000 - 0x49000000"
    
[/code]
and then just run 
[code] 
    run ml
    
[/code]
You can set another useful environment variables: 
[code] 
    setenv autoload no
    setenv bootdelay -1
    
[/code]
Last but not least, save your environment with 
[code] 
    saveenv
    
[/code]
# uEnv.txt example
[code] 
    autoload=no
    ethaddr=12:34:56:78:99:aa
    fdt_high=ffffffff
    serverip=192.168.1.130
    bootargs=earlyprintk console=ttyS0,115200
    boot_tftp=dhcp; tftp 0x46000000 arch/arm/boot/uImage; tftp 0x49000000 arch/arm/boot/dts/sun7i-a20-cubieboard2.dtb; bootm 0x46000000 - 0x49000000 
    uenvcmd=run boot_tftp
    
[/code]
