# PhoenixCard
**Phoenixcard** is a _closed source_ win32 application developed by [Allwinner][44299]. It's used to convert an Official Image into a bootable self-installing SD card. 
There is an open source application that runs on the linux commandline called [OpenixCard][44300] that does the same thing. 
## Contents
  * [1 Installing Phoenixcard][44301]
  * [2 Using Phoenixcard][44302]
  * [3 Resulting Card][44303]
  * [4 PhoenixCard for A31][44304]
    * [4.1 Make bootable sd card][44305]
    * [4.2 Resulting Card][44306]
    * [4.3 make a bootable sd card without PhoenixCard(fail)][44307]
  * [5 See also][44308]
  * [6 References][44309]

## Installing Phoenixcard
[![][44310]][44311]
[][44312]
Phienix card 3.0.3
## Using Phoenixcard
## Resulting Card
The mbr of the resulting card refers to an empty fat partition, but there is a real but hidden vfat [boot partition][44313] at offset 0x1500000 (21MB) or 0x2400000 (36MB). 
The partitions to be installed are stored raw in the card in an special format been reverse engineered[[1]][44314]. 
## PhoenixCard for A31
i try the **PhoenixCard 3.09** for [Mele M9][44315] STB. there are some differences between above description. 
### Make bootable sd card
  * press **DiskCheck** button for scaning the removable disk.
  * select your sdcard in _disk_
  * select image from **Img File**
  * if you want to write a bootable, check _Startup_.
  * **Burn** Sd card

### Resulting Card
boot1 will found the fat partition at 73728. but this partition is broken. i delete all other partition and re-create the fat start from 73728, size 50M. 
### make a bootable sd card without PhoenixCard(fail)
according to [A31 boot progress][44316], i want to make a bootable sd card by myself. but i do not success, here is my tring: 
repack the image through image imgrepacker, i could get boot0_sdcard.fex, boot1_sdcard.fex, sunxi_mbr.fex and sys_config.fex. convert sys_config.fex to sys_config.bin through [fex2bin][44317]
  * boot0 locate at 8k

[code] 
       dd if=boot0_sdcard.fex of=/dev/sdd seek=8 bs=1024
    
[/code]
  * boot1 locate at 19096k

[code] 
       dd if=boot1_sdcard.fex of=/dev/sdd seek=19096 bs=1024
    
[/code]
after this, boot1 will boot successfull and found sd card. but boot into burning nand. 
[code] 
       [       0.210] boot1 version : 2.0.0
       [       0.215] script installed ok
       [       0.216] PMU: AXP221
       [       0.216] bat ratio = 100
       [       0.218] dcdc3 1260
       [       0.264] pll1 1008
       [       0.320] power finish
       [       0.325] dcdc1 3300
       [       0.325] dcdc2 1200
       [       0.325] dcdc4 1200
       [       0.326] dcdc5 1500
       [       0.329] flash init start
       [       0.585] [mmc]: init mmc pll6clk 600000000, clk 25000000, mclkbase 0x8151030b
       [       0.587] [mmc]: SD/MMC Card: 4bit, capacity: 968MB
       [       0.592] [mmc]: vendor: Man 0x00035344 Snr 0x00ba5beb
       [       0.598] [mmc]: product: SD01G
       [       0.601] [mmc]: revision: 8.0
       [       0.604] flash init finish
       [       0.641] fs init ok
       [       0.642] fattype FAT16
       [       0.642] fs mount ok
       [       0.649] dram_para_set start
       [       0.652] dram_para_set end
       [       0.652] type=1
       [       0.719] Sprite start
       [       0.719] 0
       [       0.719] card sprite begin
       [       0.723] display init
       [       0.885] lcd 0 timeout=50
       [       0.939] try gpio config
       [       0.939] gpio start
       [       0.939] mbr fetch
       [       0.989] lcd 1 timeout=200
       [       1.189] lcd 2 timeout=100
       [       1.289] lcd 3 timeout=0
       [       1.289] lcd 4 timeout=0
       [       1.300] erase flag=1
       [       1.301] storage type = 1
       [       1.305] burn nand
       [       1.305] dram ch=0
       [       1.305] nand ch=2
       [       1.307] nand init
    
[/code]
compare with the right log: 
[code] 
       [       0.215] boot1 version : 2.0.0
       [       0.220] script installed ok
       [       0.221] PMU: AXP221
       [       0.221] bat ratio = 100
       [       0.223] dcdc3 1260
       [       0.269] pll1 1008
       [       0.325] power finish
       [       0.330] dcdc1 3300
       [       0.330] dcdc2 1200
       [       0.330] dcdc4 1200
       [       0.331] dcdc5 1500
       [       0.334] flash init start
       [       0.590] [mmc]: init mmc pll6clk 600000000, clk 25000000, mclkbase 0x8151030b
       [       0.592] [mmc]: SD/MMC Card: 4bit, capacity: 1886MB
       [       0.597] [mmc]: vendor: Man 0x00035344 Snr 0x5049ccd1
       [       0.602] [mmc]: product: SD02G
       [       0.606] [mmc]: revision: 8.0
       [       0.609] flash init finish
       [       0.647] fs init ok
       [       0.648] fattype FAT16
       [       0.649] fs mount ok
       [       0.655] dram_para_set start
       [       0.658] dram_para_set end
       [       0.658] type=1
       [       0.689] 0
       [       0.855] boot_disp.output_type=3
       [       0.855] boot_disp.output_mode=5
       [       0.857] boot_disp.auto_hpd=1
       [       0.860] hdmi open
       [       0.862] DRV_hdmi_set_display_mode,mode:5
       [       0.867] DRV_hdmi_open
       [       0.990] ERR: Parse_Pic_BMP failed
       [       0.991] key 0
       [       0.991] cant find rcvy value
       [       0.994] cant find fstbt value
       [       0.999] try to boot
       [       1.000] load kernel start
       [       1.036] load kernel successed
       [       1.036] start address = 0x4a000000
    
[/code]
  * i also the try the following things accoring the hexdump the bootable sd card. but no more luck.

[code] 
       dd if=sunxi_mbr.fex of=/dev/sdd seek=20480 bs=1024
       dd if=sys_config.bin of=/dev/sdd seek=19848 bs=1024
    
[/code]
  * boot1 will load the boot.axt, and boot.axf will load u-boot according to linux/linux.ini

## See also
  * [LiveSuit][44318]

## References
  1. [↑][44319] [phoenix_info@sunxi-tools][44320]
