# U-Boot/USB Mass Storage
< [U-Boot][56610]
 
## Contents
  * [1 USB Mass Storage (UMS) Gadget][56613]
    * [1.1 Prerequisites][56614]
    * [1.2 Using it][56615]
    * [1.3 Benchmarks][56616]
  * [2 See also][56617]

# USB Mass Storage (UMS) Gadget
For few years now, starting from v2014.07, U-Boot has contained UMS gadget that allows for easier access to onboard eMMC/SD storage by emulating a simple block device over OTG to the host. Similar to the Linux kernel [Mass Storage Gadget][56618]. 
U-Boot UMS Gadget also provides a simpler alternative to [Fastboot][56619] based device setup and recovery. 
## Prerequisites
  * `USB_MUSB_GADGET=y`
  * `CONFIG_CMD_USB_MASS_STORAGE=y`
  * Sunxi device connected to a host over USB OTG port.

On my [NanoPi NEO Core][56620] I also had to enable 
  * `USB_MUSB_PIO_ONLY=y`
  * `USB_ETHER=y`

## Using it
In U-Boot prompt you can use the `ums` command. 
[code] 
    => ums
    ums - Use the UMS [USB Mass Storage]
    
    Usage:
    ums <USB_controller> [<devtype>] <dev[:part]>  e.g. ums 0 mmc 0
        devtype defaults to mmc
    
[/code]
  
To export internal eMMC storage, just type 
[code] 
    => ums 0 mmc 1
    
[/code]
Press `Ctrl+C` to stop UMS gadget. 
## Benchmarks
On my NanoPi NEO Core internal eMMC I got around 13MB/s read and 9MB/s write. 
[![U-boot ums gadget benchmark.png][56621]][56622]
# See also
  * [Fastboot][56619]
  * <https://boundarydevices.com/u-boot-usb-mass-storage-gadget/>
