# Vivax TPC-9150
Vivax TPC-9150  
---  
Manufacturer |  [[1]][58806]  
Dimensions |  238 _mm_ x 147 _mm_ x 9 _mm_  
Release Date |  ?   
Specifications   
SoC |  [A20][58807]  
DRAM |  1GiB DDR3   
NAND |  8GB   
Power |  USB 5V @ 1A, 4000mAh 3.7V Li-Ion battery   
Features   
LCD |  1024x600 (9" 16:9)   
Touchscreen |  5-finger capacitive ([Focaltech FT5x06][58808])   
Video |  HDMI (Type C - mini)   
Audio |  3.5mm headphone plug, HDMI, internal mono speaker, internal microphone   
Network |  WiFi 802.11 b/g/n ([Realtek RTL8723A][58809])   
Storage |  µSD   
USB |  1 USB2.0 OTG   
Camera |  0.3MP (640x480) front, 2.0MP (1600x1200) rear   
Other |  Bluetooth (Realtek RTL8723AU)   
Headers |  UART   
  

## Contents
  * [1 Identification][58810]
  * [2 Sunxi support][58811]
    * [2.1 Legacy kernel support][58812]
    * [2.2 Mainline kernel support][58813]
      * [2.2.1 Support status][58814]
    * [2.3 Mainline U-Boot][58815]
    * [2.4 Manual build][58816]
  * [3 Tips, Tricks, Caveats][58817]
    * [3.1 FEL mode][58818]
    * [3.2 Reset button][58819]
    * [3.3 Internal µSD card][58820]
    * [3.4 Bad Wi-Fi range][58821]
    * [3.5 Suspend mode][58822]
    * [3.6 Touchscreen does not work!!!! Help!][58823]
    * [3.7 The accelerometer situation][58824]
    * [3.8 The screen's a bit shifted, what's going on?][58825]
  * [4 Adding a serial port (**voids warranty**)][58826]
    * [4.1 Device disassembly][58827]
    * [4.2 Locating the UART][58828]

# Identification
When booted into Android, open the "Settings" app and choose "About tablet". You will find the following information: 
Model number: TPC-9150 Firmware version: v2.0 Kernel version: 3.4.39 Build number: wing_um723-eng 4.33 JDQ39 20140322 test-keys 
[![][58829]][58830]
[][58831]
Android 4.2.2 running on TPC-9150
[![][58832]][58833]
[][58834]
Back side of TPC-9150
[![][58835]][58836]
[][58837]
Android identification on TPC-9150
[![][58838]][58839]
[][58840]
GDM running on TPC-9150
# Sunxi support
## Legacy kernel support
Use the [default sunxi kernel][58841] with the following [FEX file][58842]
## Mainline kernel support
Not yet merged. 
Clone the Linux kernel from <https://github.com/torvalds/linux>
[Apply the following patch][58843] (i.e. `patch -p1 < file.patch`) 
After applying that run the following: 
` make ARCH=arm sunxi_defconfig `
`make ARCH=arm dtbs `
Then afterwards use the desired `sun7i-a20-tpc9150.dtb` file with the latest mainline kernel. 
### Support status
Things that work: 
  * Accelerometer (hack required)
  * Audio input (only via internal microphone)
  * Audio output (only via headphone jack)
  * SD card
  * USB charging
  * Battery indicator
  * Battery charging
  * Power management (via AXP209)
  * Touchscreen and touchscreen wakeup
  * Included LCD display
  * Ability to control LCD brightness
  * Wi-Fi
  * Bluetooth
  * UART
  * HDMI
  * HDMI audio
  * Mali GPU (via lima driver)
  * Power button
  * USB slave (g_cdc and g_ether) work
  * Suspend
  * Charger hotplugging

Things that DO NOT work: 
  * The built-in speaker
  * NAND (the driver lacks MLC support and thus fails to initialize the NAND chip, although it properly recognizes it)
  * "ESC" key
  * HDMI hotplugging (but firmware already probes manually)
  * Both cameras

Things that are not tested (and probably don't work): 
  * USB OTG

## Mainline U-Boot
Not yet merged. 
Apply [this patch][58844] with a freshly cloned U-Boot repository. 
For [ building mainline U-Boot][58845], use the _Vivax_TPC9150_ target. 
UART, LCD, SD card work, nothing else does. 
## Manual build
Use the information in "Mainline kernel" and "Mainline U-Boot" along with the [manual build howto][58846], in order to build a functioning Linux system. 
# Tips, Tricks, Caveats
## FEL mode
Following the [FEL guide][58847] treat the "ESC" key as the FEL button. 
Otherwise build an FEL SD card, using the same [FEL guide][58847] and with a needle press the reset button, located on the back of the tablet. 
## Reset button
The reset button (on the back side of the device) reboots the device. 
## Internal µSD card
The device has an internal µSD card port that shows as _mmcblk0_. This port has boot priority over NAND. 
## Bad Wi-Fi range
The included Wi-Fi driver in most distros rtl8xxxu has really bad range on this device. It works, but Wi-Fi tends to cut off often. 
In order to improve range use this driver instead: <https://github.com/lwfinger/rtl8723au>
Follow it's instructions, then blacklist the included rtl8xxxu driver. 
Then to prevent the Wi-Fi connection from cutting off randomly, put the following into the `/etc/modprobe.d/8723au.conf`
` options 8723au rtw_power_mgnt=0 rtw_enusbss=0 rtw_low_power=0 rtw_smart_ps=0 `
## Suspend mode
The wake-up issue was fixed. However, the device can only be woken up by the touchscreen, as I was unable to find any interface from AXP209 to wake up the tablet. 
How I fixed the issue: Anyway I've found [this trick.][58848]
The original issue was that once the device was in suspend mode, the `i2c2` bus would get stuck and the device will be unable to be controlled with. In order to fix this you'll need to add `bias-pull-up;` to your DTS like so: 
[code] 
    &i2c2 {
    	status = "okay";
    
    	ft5x: touchscreen@38 {
    		compatible = "edt,edt-ft5406";
    		reg = <0x38>;
    		interrupt-parent = <&pio>;
    		interrupts = <7 21 IRQ_TYPE_EDGE_FALLING>; /* PH21 */
    
    		touchscreen-size-x = <800>;
    		touchscreen-size-y = <480>;
    
    		wake-gpios = <&pio 1 13 GPIO_ACTIVE_HIGH>; /* PB13 */
    
    		wakeup-source;
    		bias-pull-up;
    	};
    };
    
[/code]
## Touchscreen does not work!!!! Help!
Please check that there aren't any udev rule files in `/etc/udev/rules.d/` arbitrarily setting a libinput calibration matrix. 
## The accelerometer situation
For some reason the driver won't probe (or load) itself at boot, so you'll need to do it manually. This is a relatively simple process, just follow these steps: 
  1. Make sure that the `stk8312` module is available in your kernel
  2. Manually probe it with: `modprobe stk8312 probe=1,0x3d`
  3. It should appear under `/sys/module/stk8312/drivers/i2c:stk8312/1-003d`
  4. To make changes persist across reboots, you'll need to create two files 
     1. Create `/etc/modprobe.d/stk8312.conf` with the content `options stk8312 probe=1,0x3d`
     2. Create `/etc/modules-load.d/stk8312.conf` with the content `stk8312`
  5. Reboot and see whether it worked, if it didn't then just run modprobe on each boot

## The screen's a bit shifted, what's going on?
Basically there isn't a correct panel driver included into the current Linux source tree. Luckily, I have been successful in obtaining the correct LCD panel settings, but the problem is that I do not know the make or model of the LCD which would probably invalidate my kernel patch. Not only that, but manually patching this would require a kernel to be rebuild, which is too much effort in my opinion. 
So the panel parameters that are available in the current patch are "good enough" in most use cases. 
# Adding a serial port (**voids warranty**)
## Device disassembly
In order to open the device, there are two Phillips screws to remove from the side with the connectors. The pins from the white part are easy to pop but it is advised to use a [a plastic tool][58849], starting from opposite of the side with the connectors. The front panel is very fragile and pressuring the screen to pop open the pins can easily end up in breaking the touch screen panel. 
## Locating the UART
The UART pads are located on the front side of the PCB. The UART pads are labeled and large enough so that soldering wires to those UART pins becomes easy. 
[![][58850]][58851]
[][58852]
Open motherboard
[![][58853]][58854]
[][58855]
UART pin location
