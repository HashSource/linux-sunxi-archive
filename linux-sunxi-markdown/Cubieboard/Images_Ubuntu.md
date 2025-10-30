# Cubieboard/Images Ubuntu
< [Cubieboard][14138]
 
## Prebuilt Images(For Nand Flash Only)
Version | Features | Tips   
---|---|---  
[Ubuntu 12.04 desktop v1.03 HDMI(click to download)][14141] |  1.Cpu frequency scaling   
2.stage-3.4@linux-sunxi kernel   
3.Support 8192cu, 8188eu and more wifi   
4.Could be written to Cubieboard's nandflash with livesuit   
5.Default HDMI output   
6.Suitable for Cubieboard(A10)   
|  1\. Try to run 'sudo dhclient eth0' command, if you could not access to external network with ethernet  
2\. Try to run following commands to tune filesystem partitions to its real size:  

[code] 
       sudo resize2fs /dev/nandc   
    
       sudo resize2fs /dev/nandd   
    
       sudo resize2fs /dev/nande   
    
       sudo resize2fs /dev/nandf   
    
    
[/code]
3\. the ethernet mac address is generated from chipid of a10   
[Ubuntu 12.04 desktop v1.03 VGA(click to download)][14142] |  1.Cpu frequency scaling   
2.stage-3.4@linux-sunxi kernel   
3.Support 8192cu, 8188eu and more wifi   
4.Could be written to Cubieboard's nandflash with livesuit   
5.Default VGA output   
6.Suitable for Cubieboard(A10)   
|  1\. You need a VGA baseboard   
  
[Ubuntu 13.03 server v1.03][14143] |  1.Cpu frequency scaling   
2.stage-3.4@linux-sunxi kernel   
3.Support 8192cu, 8188eu and more wifi   
4.Could be written to Cubieboard's nandflash with livesuit   
5.Default HDMI output   
6.Suitable for Cubieboard(A10)   
7.No X Window   
|  1\. [Kernel Tarball][14144]  
[Ubuntu 12.04 desktop v1.00 HDMI(A20)][14145] |  1\. Suitable for Cubieboard(A20)   
2\. Linux-3.3 kernel   
3\. For Cubieboard(A20) only   
4\. DRAM freq 432MHz   
5\. Dual-cores CPU   
6\. Dynamically CPU Frequency Scaling   
|  SDK: <https://github.com/cubieboard2/manifests>   
  
[Ubuntu 12.04 desktop v1.00 HDMI(A20)][14146] |  1\. Suitable for Cubieboard(A20)   
2\. Linux-3.3 kernel   
3\. For Cubieboard(A20) only   
4\. DRAM freq 480MHz   
5\. Dual-cores CPU   
6\. Dynamically CPU Frequency Scaling   
|  SDK: <https://github.com/cubieboard2/manifests>   
  
[Ubuntu 12.04 desktop v1.03 HDMI(A20)][14147] |  1\. Fixed livesuit(linux) hung issue   
|  SDK: <https://github.com/cubieboard2/manifests>   
  
[Ubuntu 12.04 desktop v1.03 VGA(A20)][14148] |  1\. Fixed livesuit(linux) hung issue   
2\. Default VGA output  
|  SDK: <https://github.com/cubieboard2/manifests>   
  
[Livesuit(Windows)][14149] |  Support Windows XP/7/8 32/64 bits   
|  Support Cubieboard(A10)   
  
[Livesuit(Mac)][14150] | Support MacOS | Support Cubieboard(A10)   
[Livesuit(x86)][14151] | Not stable | Support Cubieboard(A10)   
[Livesuit(x86_64)][14152] | Not stable | Support Cubieboard(A10)   
## Prebuilt Images(For TF/SD Card Only)
Version | Features | Tips   
---|---|---  
[lubuntu-linaro-quantal-alip-20130227-290 HDMI(click to download)][14153] |  1.Default HDMI output   
2.Suitable for Cubieboard(A10)   
|  for tf/sd card only   
  

## lubuntu SDK
Version | Features | Tips   
---|---|---  
[Cubieboard(A10) lubuntu desktop SDK(click to download)][14154] |  1.Suggest using ubuntu 12.04(x86_64) as host building enviroment   
2\. run 'make livesuit-cb ROOTFS=rootfs/linaro-quantal-alip-20130422-342.tar.gz' to build the final livesuit image  
|  You can replace the lubuntu rootfs as you can
