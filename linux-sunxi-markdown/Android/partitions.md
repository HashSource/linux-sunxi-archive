# Android/partitions
< [Android][7599]
 
Some quick initial notes on partitions. 
On my android tablet, the nand is devided into 9 partitions. Sizes are how they are on this devices, they should be used as an indication only. 
id  | dev/block/*  | Size  | Name  | Description   
---|---|---|---|---  
0  | nanda  | 32MiB  | bootloader  | Files to assist the bootloader. Think battery status images etc. also u-boot.bin lives here.   
1  | nandb  | 32MiB  | env  | Enviroment to assist u-boot.   
2  | nandc  | 64MiB  | boot  | Holds the kernel (and its ramdisk) in raw form   
3  | nandd  | 1GiB  | system  | Android's /system partition   
4  | nande  | 32MiB  | misc  | Partition used to pass data amongst various stages of the boot chain (e.g. boot into recovery mode, fastboot etc)   
5  | nandf  | 64MiB  | recovery  | Android's recovery partition, strangly this is on nandg!   
6  | nandg   
7  | nandh   
8  | nandi   
Allwinner changed the layout a little some time after changing to Android ICS 4.0. Previous versions of the Android firmware would use partition with field "user_type" of **0** or **2**. However, Allwinner appear to have added type **1**. 
The following is the partition layout from Mele-v1.3BETA Android firmware: 
id  | dev/block/*  | Size  | Name  | Type  | Description   
---|---|---|---|---|---  
0  | nanda  | 16MiB  | bootloader  | vfat  | Files to assist the bootloader. Think battery status images etc. also u-boot.bin, script.bin and .ini lives here   
1  | nandb  | 16MiB  | env  | raw  | Enviroment to assist u-boot.   
2  | nandc  | 32MiB  | boot  | raw  | Holds the kernel (and its ramdisk) in ANDROID mkbootimg form   
3  | nandd  | 512MiB  | system  | ext4  | Android's /system partition   
4  | nande  | 1.5GiB  | data  | ext4  | Android /data partition   
5  | nandf  | 16MiB  | misc  | raw  | Partition used to pass data amongst various stages of the boot chain (e.g. boot into recovery mode, fastboot etc)   
6  | nandg  | 32MiB  | recovery  | raw  | Android's recovery partition   
7  | nandh  | 128MiB  | cache  | ext4  | Mounted as /cache and appear to contain backup information   
8  | nandi  | 16MiB  | private  | vfat  | Mounted as /mnt/private   
9  | nandj  | 512MiB  | sysrecovery  | raw   
10  | nandk  | 944MiB  | UDISK  | vfat  | Mounted by vold as /mnt/sdcard and /mnt/secure/asec
