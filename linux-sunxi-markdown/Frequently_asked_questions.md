# Frequently asked questions
This page is more of collection of random issues one might run into, and hopefully their solutions, as opposed to an actual FAQ. 
## Contents
  * [1 General][19997]
    * [1.1 Where do i ask for help?][19998]
    * [1.2 My device is not listed, what can I do?][19999]
  * [2 Running linux-sunxi][20000]
    * [2.1 In uptime, load is always above 1][20001]
    * [2.2 I've connected a 3TB disk from another system via a USB dock, but I can't get it to mount][20002]
    * [2.3 I want to control my UPS over USB, but apcupsd won't start][20003]
  * [3 See Also][20004]

# General
## Where do i ask for help?
If you have any questions or problems with your device, please at first make sure, that the device is [ listed on the front page][20005]. 
Please **DO NOT** bother the community with issues caused by crappy vendor software, prebuilt images (vendor/ private), old kernel trees .... As this is a community which deals with open source software for Allwinner devices, linux-sunxi community is no replacement for missing vendor support. In case of such problems contact the vendor or use the appropriate forums. 
Otherwise feel free to use the [IRC][20006] or the [mailing list][20007]. **Don't feed the wiki with your questions!**
## My device is not listed, what can I do?
If your device is not [ listed on the front page][20005], then it is not supported yet. This usually means that no-one has worked through our [ new device howto][20008] yet. This howto is a full step by step guide which makes it as easy as possible to add support for your device to linux-sunxi. 
# Running linux-sunxi
## In uptime, load is always above 1
This is due to a bit of bad code in the sunxi-3.4 kernel usb driver for allwinner. You can fix this by editing your [ .fex file][20009], and setting. 
[code] 
    usb_detect_type = 1
[/code]
to 
[code] 
    usb_detect_type = 0
[/code]
The actual cause for this still needs to be investigated, but a busy wait loop is probably the culprit. 
## I've connected a 3TB disk from another system via a USB dock, but I can't get it to mount
Some kernels for the allwinner are built with kernel options CONFIG_PARTITION_ADVANCED and CONFIG_EFI_PARTITION turned off. This will cause the kernel to try and determine the device's partition table from the legacy fdisk partition data, which will probably cause the kernel to interpret the data differently (and incorrectly). Disks with more than 2TB capacity require the new partitioning standard, GPT/EFI. 
You can check with: 
[code] 
    gzip -d < /proc/config.gz | grep CONFIG_PARTITION_ADVANCED
[/code]
and 
[code] 
    gzip -d < /proc/config.gz | grep CONFIG_EFI_PARTITION
[/code]
Unless both have a value of "y", your GPT partition is not being used and thus your view of the disk is probably incorrect. 
## I want to control my UPS over USB, but apcupsd won't start
If you're trying to use the apcupsd package to talk to your UPS over USB, note that the daemon uses the hiddev interface from /dev. Many armhf kernels leave this out by default. To check, do: 
[code] 
    gzip -d < /proc/config.gz | grep HIDDEV
[/code]
and if the option does not have a value of "y", you'll need to get a kernel with CONFIG_USB_HIDDEV enabled. 
# See Also
[Cubieboard/FAQ][20010] contains loads of things which can be partly transplanted to here.
