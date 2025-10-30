# Radxa Cubie A5E
Radxa Cubie A5E  
---  
[![Radxa Cubie A5E top.jpg][46922]][46923] [][46924]  
Manufacturer |  [Radxa][46925]  
Dimensions |  _56mm_ x _69mm_  
Release Date |  Jan 2025   
Website |  [Radxa Cubie A5E][46926]  
Specifications   
SoC |  [A527][46927] or [T527][46928](industrial version) @ 1.8 Ghz   
DRAM |  1/2/4GiB LPDDR4 @ 2400 MT/s   
Power |  DC 5V @ 4A via USB-C connector   
Features   
Video |  Standard HDMI 2.0a, MIPI FPC connector   
Audio |  Line out on header, HDMI audio   
Network |  WiFi 802.11 a/b/g/n/ac/ax (BLink BL-M8800DS2), 2x 10/100/1000Mbps Ethernet ([Maxio MAE0621A][46929]), one supports PoE   
Storage |  µSD, 128Mbit [SPI flash][46930] (Winbond W25Q128JWPIQ), M.2 M Key for 2230 SSD   
USB |  1 X USB3.0 Host, 1 X USB2.0 OTG   
Radxa Cubie A5E is the first Allwinner based SBC introduced by Radxa. 
It features both an M-keyed M.2 socket for an NVMe SSD and a USB 3.0 receptacle, but only one of them can be used at any given time. A GPIO controlled mux connects either the M.2 or the USB socket to the SoC. 
## Contents
  * [1 Identification][46931]
  * [2 Sunxi support][46932]
    * [2.1 Current status][46933]
    * [2.2 Manual build][46934]
      * [2.2.1 Mainline U-Boot][46935]
      * [2.2.2 Mainline Linux Kernel][46936]
    * [2.3 Images][46937]
    * [2.4 Radxa BSP][46938]
    * [2.5 Allwinner SDK Download][46939]
    * [2.6 Manual build][46940]
      * [2.6.1 Image Build][46941]
      * [2.6.2 U-Boot][46942]
      * [2.6.3 Linux Kernel][46943]
  * [3 Expansion ports][46944]
  * [4 Tips, Tricks, Caveats][46945]
    * [4.1 FEL mode][46946]
    * [4.2 LEDs][46947]
    * [4.3 SPI booting][46948]
  * [5 Serial port][46949]
  * [6 Models and SKU][46950]
  * [7 Pictures][46951]
  * [8 Schematics][46952]
  * [9 See also][46953]

# Identification
The PCB has a version number silkscreened at the top: 
[code] 
    Cubie A5E V1.1
    Radxa Logo
[/code]
# Sunxi support
## Current status
Supported for basic headless use cases in mainline Linux and U-Boot, development closely follows the A523/T527 upstreaming progress. USB3.0 and support for the second Ethernet port are work in progress, with patches being on the list already. 
## Manual build
You can build things for yourself by following our [ Manual build howto][46954] and by choosing from the configurations available below. 
### Mainline U-Boot
Use the _radxa-cubie-a5e_defconfig_ build target. Supported since v2025.10-rc1. 
### Mainline Linux Kernel
Basic headless support is working since v6.15, with the DT being merged in v6.16. 
Use the _sun55i-a527-cubie-a5e.dtb_ device-tree binary. 
## Images
If the download file is in compressed format,you need decompression first.  

Unless otherwise specified, the images listed below require Allwinner's flashing tool to write the system image.  

Tools like dd cannot be used for these images  

Please use [PhoenixCard][46955] to flash the image to the SD card.  
Please use [PhoenixSuit][46956] to flash the image to the eMMC or SPI FLASH.  
Please use [LiveSuit][46957] to flash the image to the eMMC or SPI FLASH on linux OS.  
Alternatively script like [this][46958] can be used to convert BSP image to raw image, which can be flashed with dd, Etcher or similar tool. 
[code] 
    UserName: root/radxa
    Password: root/radxa
    
[/code]
NUM  | Download URL  | Description  | More Info   
---|---|---|---  
1  | [cubie_a5e_tina_debian_beta_20250211.fel.zip][46959] | ` cubie a5e debian11 xfce beta fel image ` | ` Fix the issue where Docker cannot be used. `  
2  | [cubie_a5e_tina_bsp_nor_beta_20250211.fel.zip][46960] | ` cubie a5e spinor flash beta fel image ` | ` A spi flash beta image, intended solely for verifying the functionality of SPI flash. `  
3  | [cubie_a5e_tina_debian_beta_20250303.gpt.img][46961] | ` cubie a5e debian11 xfce beta GPT image ` | ` This image is a GPT image, and it can be directly written to an SD card using the dd command or the Etcher tool. `  
4  | [cubie_a5e_tina_debian_beta_v1.gpt.img.gz][46962] | ` Update: Extlinux,FDT Overlay, NVME boot with SPI NOR.  
More Info: <https://github.com/cubie-image/sun55iw3p1/releases/tag/beta_v1>` | ` This image is a GPT image, and it can be directly written to an SD card using the dd command or the Etcher tool. `  
RadxaOS is our current primary and actively developed operating system, and we recommend using it—featuring updated hardware drivers, regular security patches, and performance optimizations for your Radxa device. 
You can download it from the github page: <https://github.com/radxa-build/radxa-cubie-a5e/tags>
## Radxa BSP
Here are the board support files for Radxa Cubie A5E, which should be downloaded and placed in the corresponding   
directories under the original SDK. The related information is as follows: 
  * Repository and SDK Directory Mapping *

num  | Repository Name  | SDK Directory Path  | Description   
---|---|---|---  
1  | [allwinner-target (branch: target-a527-v1.4.6)][46963] | `target/a527 ` | Target platform configurations and scripts   
2  | [allwinner-device (branch: device-a527-v1.4.6)][46964] | `device/config/chips/a527 ` | Device chip configuration files   
3  | [allwinner-bsp (branch: cubie-aiot-v1.4.6)][46965] | `bsp` | Board Support Package (BSP) related code   
4  | [kernel (branch: allwinner-aiot-linux-5.15)][46966] | `kernel/linux-5.15` | Linux kernel source code  
  
5  | [u-boot (branch: cubie-aiot-v1.4.6)][46967] | `brandy/brandy-2.0/u-boot-2018/` | U-Boot source code   
## Allwinner SDK Download
This is the Allwinner Official SDK Tina5.0 for T527/A527. 
Tina SDK 1.4.6(partially uploaded):: <https://gitlab.com/tina5.0_aiot>   
Tina SDK 1.4.6(complete repo package, use command 'repo sync -l' to restore directory structure):  
Mega: [https://mega.nz/file/kFtD0BYY#zm3FXLiLK9SfOFss3BGY1Kx714BFBqyyPeYeE5FvOw0][46968]   
BaiduPan: <https://pan.baidu.com/s/1zcVq4l-rij7RPmJ92nccZg> password: 547b   
NOTE:   
Modify the name of the spl-pub folder under the brandy directory, for example, change it   
to spl-pub-bak, so that it no longer participates in compilation. The files compiled   
in this directory will replace the binary files in the devcie/xxxx/configs/a733/bin   
directory. However, we now need to temporarily use the binary files provided by   
Allwinner to achieve a better experience.  

[T527_Tina5.0_AIOT V1.4.5][46969] & [MD5SUM][46970] &(Note: This is an old version and will be officially removed in the future. We recommend using the latest SDK instead.) 
The directory structure is as follows: 
[code] 
    ├── brandy
    ├── bsp
    ├── build
    ├── buildroot
    ├── build.sh -> build/top_build.sh
    ├── debian
    ├── device
    ├── docs
    ├── kernel
    ├── out
    ├── platform
    ├── prebuilt
    ├── rtos
    ├── target
    ├── tee_kit
    ├── test
    └── tools
    
[/code]
After that, you can refer to the "Radxa BSP" section mentioned above and integrate the BSP configuration files for the RADXA CUBIE A5E to build the image for the Cubie A5E. 
Now you can build things for yourself by following our [ Manual build howto][46954] and by choosing from the configurations available below. 
## Manual build
### Image Build
📢: Please add the following patch to the packaging script（path: TinaSDK/build/pack) to support extlinux booting: 
[code] 
    --- a/pack
    +++ b/pack
    @@ -235,6 +235,9 @@ ${LICHEE_CHIP_CONFIG_DIR}/configs/${PACK_BOARD}/wavefile/*:${LICHEE_PACK_OUT_DIR
     ${LICHEE_CHIP_CONFIG_DIR}/configs/${PACK_BOARD}/${PACK_TYPE}/*.bmp:${LICHEE_PACK_OUT_DIR}/boot-resource/
     ${LICHEE_CHIP_CONFIG_DIR}/boot-resource/boot-resource/bat/bempty.bmp:${LICHEE_PACK_OUT_DIR}/bempty.bmp
     ${LICHEE_CHIP_CONFIG_DIR}/boot-resource/boot-resource/bat/battery_charge.bmp:${LICHEE_PACK_OUT_DIR}/battery_charge.bmp
    +${LICHEE_CHIP_CONFIG_DIR}/boot-resource/extlinux:${LICHEE_PACK_OUT_DIR}/boot-resource/
    +${LICHEE_PLAT_OUT}/sunxi.dtb:${LICHEE_PACK_OUT_DIR}/boot-resource/extlinux/
    +${LICHEE_PLAT_OUT}/bImage:${LICHEE_PACK_OUT_DIR}/boot-resource/extlinux/Image
     )
    
[/code]
  * 📝 Configuration

[code] 
    source ./build/envsetup.sh
    ./build.sh config
    
[/code]
  * 📊 Configuration Example

[code] 
    Debian xfce image example:
    ========ACTION List: mk_config ;========
    options :
    All available platform:
       0. android
       1. linux
    Choice [linux]: 1
    All available linux_dev:
       0. bsp
       1. dragonboard
       2. buildroot
       3. debian
    Choice [debian]: 3
    All available kern_name:
       0. linux-5.10
       1. linux-5.15
    Choice [linux-5.15]: 1
    All available ic:
       0. a523
       1. a527
       2. t527
    Choice [a527]: 1
    All available board:
       0. cubie_a5e
       1. d10_linux_aiot
       2. demo_linux_aiot
       3. pro2_linux_aiot
    Choice [cubie_a5e]: 0
    All available flash:
       0. default
       1. nor
    Choice [default]: 0
    All available rootfs files:
       0. linaro-bullseye-gnome-arm64.tar.gz
       1. linaro-bullseye-lite-arm64.tar.gz
       2. linaro-bullseye-lxde-arm64.tar.gz
       3. linaro-bullseye-xfce-arm64.tar.gz
    Choice [linaro-bullseye-xfce-arm64.tar.gz]: 3
    Setup BSP files
    
[/code]
  * 🔨 Building Image

[code] 
    ./build.sh
    
[/code]
  * 📦 Packing Image

[code] 
    ./build.sh pack
    
[/code]
You will find the generated image in the ‘out’ directory. 
### U-Boot
* * *
[code] 
    ./build.sh bootloader
    
    # Running the command './build.sh bootloader' will execute the build.sh script located in the brandy/brandy-2.0/ directory.
    # Alternatively, you can manually execute the following command in this directory:
    
    cd brandy/brandy-2.0/
    ./build.sh -p sun55iw3p1 -b a527
    
    # This will using sun55iw3p1_defconfig under the u-boot-2018/configs directory.
    # And compile the components required for the bootloader, including boot0, fes1, sboot, and u-boot.
    
    output: 
    u-boot-sun55iw3p1.bin 
    boot0_sdcard_sun55iw3p1.bin
    fes1_sun55iw3p1.bin
    sboot_sdcard_sun55iw3p1.bin 
    etc.
    Viewing the compile log will reveal the folder where the compiled files are located.
    
    +-----+--------+--------------------------------------------------------------------------------------------------------------------+
    | num | type   | use                                                                                                                |
    +=====+========+====================================================================================================================+
    | 1   | boot0  | boot0 is the first stage bootloader (FSBL) in the Allwinner chip boot process.                                    |
    |     |        | It is responsible for initializing basic hardware (such as DRAM, clocks, etc.) and loading the next stage bootloader |
    |     |        | (such as U-Boot).                                                                                                  |
    +-----+--------+--------------------------------------------------------------------------------------------------------------------+
    | 2   | fes    | The program run during firmware burning.                                                                           |
    +-----+--------+--------------------------------------------------------------------------------------------------------------------+
    | 3   | sboot  | sboot is the bootloader for secure boot. It is responsible for verifying the signatures of subsequent bootloaders |
    |     |        | (such as U-Boot or the Linux kernel) to ensure the integrity and security of the boot chain.                        |
    +-----+--------+--------------------------------------------------------------------------------------------------------------------+
    | 4   | U-Boot | The universal boot loader.                                                                                         |
    +-----+--------+--------------------------------------------------------------------------------------------------------------------+
    
    
    
[/code]
### Linux Kernel
[code] 
    # 1) Ensure you have performed the parameter configuration with ‘./build.sh config’ before running this command.
    $./build.sh kernel
    
    # 2）This will use the defconfig file located at device/config/chips/a527/configs/cubie_a5e/debian/linux-5.15/bsp_defconfig and
    the device tree file at device/config/chips/a527/configs/cubie_a5e/linux-5.15/board.dts.
    
    
    # 3）You will find the kernel image in the out/a527/cubie_a5e/debian/ directory.
    
    +-----+-----------+--------------------------------------------------------+
    | num | type      | use                                                    |
    +=====+===========+========================================================+
    | 1   | boot.img  | bootimg containing the kernel and device tree   |
    +-----+-----------+--------------------------------------------------------+
    | 2   | sunxi.dtb | The device-tree blob                                   |
    +-----+-----------+--------------------------------------------------------+
    
    
[/code]
# Expansion ports
The Cubie A5E has a 40-pin, 0.1" populated connector with several low-speed interfaces. 
The primary function follows loosely the Raspberry Pi pin assignment, but pinmuxing gives access to more interfaces (not all at the same time). 
GPIO number  | Function7  | Function6  | Function5  | Function4  | Function3  | Function2  | Function1  | PIN#  |  | PIN#  | Function1  | Function2  | Function3  | Function4  | Function5  | Function6  | Function7  | GPIO number   
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
|  |  |  |  |  |  | +3.3V  | 1  |  | 2  | +5.0V  |  |  |  |  |  |  |   
37  | PB-EINT5  | HDMI-SDA  | PWM0-9  | TRACE-CLK  | I2S0-BCLK  | TWI1-SDA  | PB5  | 3  |  | 4  | +5.0V  |  |  |  |  |  |  |   
36  | PB-EINT4  | HDMI-SCL  | PWM0-8  | TRACE-DATA2  | I2S0-MCLK  | TWI1-SCK  | PB4  | 5  |  | 6  | GND  |  |  |  |  |  |  |   
263  |  | PI-EINT7  | SPI2-CLK  | PWM0-8  | UART4-CTS  | UART6-RX  | PI7  | 7  |  | 8  | PB9  | UARTO-TX  | TWIO-SCK  | TRACE-DATA1  | I2S0-DIN2  | I2S0-DOUT2  | PB-EINT9  | 41   
|  |  |  |  |  |  | GND  | 9  |  | 10  | PB10  | UARTO-RX  | TWIO-SDA  | PWM0-1  | I2S0-DIN3  | I2S0-DOUT3  | PB-EINT10  | 42   
265  |  |  | PI-EINT9  | PWM0-10  | DMIC-DATA2  | TWI5-SDA  | PI9  | 11  |  | 12  | PI2  | UART5-TX  | SPI1-CSO  | PWM0-3  | I2S2-BCLK  | I2S2-BCLK  | PI-EINT2  | 258   
266  |  | PI-EINT10  | I2S2-MCLK  | PWM0-11  | DMIC-DATA1  | OWA-OUT  | PI10  | 13  |  | 14  | GND  |  |  |  |  |  |  |   
12  | S-PL-EINT12  | S-SPI0-MOSI  | DMIC-DATA2  | S-UART0-TX  | MCU-PWM0-6  | S-TWI2-SCK  | PL12  
| 15  |  | 16  | PI11  | UART3-TX  | DMIC-DATA0  | PWM0-12  | PI-EINT11  |  |  | 267   
|  |  |  |  |  |  | +3.3V  | 17  |  | 18  | PI14  | UART6-RTS  | DMIC-CLK  | PWM0-15  | PI-EINT14  |  |  | 270   
45  |  |  | PI-EINT13  | PWM0-4  | UART7-TX  | TWI4-SCK  | PB13  | 19  |  | 20  | GND  |  |  |  |  |  |  |   
46  | PB-EINT14  | SPI1-MISO  | PWM0-5  | SPI1-MOSI  | UART7-RX  | TWI4-SDA  | PB14  | 21  |  | 22  | PL13  | S-TWI2-SDA  | MCU-PWM0-7  | S-UARTO-RX  | DMIC-DATA3  | S-SPI-MISO  | S-PL-EINT13  | 13   
44  |  | PB-EINT12  | PWM0-3  | SPI1-CLK  | UART7-CTS  | TWI5-SDA  | PB12  | 23  |  | 24  | PB11  | TWI5-SCK  | UART7-RTS  | PWM0-2  | SPI1-CSO  | PB-EINT11  |  | 43   
|  |  |  |  |  |  | GND  | 25  |  | 26  | PI0  | TWI4-SCK  | UART4-TX  | PWM0-1  | I2S2-DIN3  | I2S2-DOUT3  | PI-EINTO  | 256   
272  |  | (USB2 DP)*  | PI-EINT16  | PWM1-1  | TWI2-SDA  | UART3-CTS  | PI16  | 27  |  | 28  | PI15  | TWI2-SCK  | UART3-RTS  | PWM1-0  | PI-EINT15  | (USB2 DM)*  |  | 271   
264  |  | PI-EINT8  | SPI2-MOSI  | PWM0-9  | IR-RX  | TWI5-SCK  | PI8  | 29  |  | 30  | GND  |  |  |  |  |  |  |   
268  |  |  | PI-EINT12  | SPI2-MISO  | PWM0-13  | UART3-RX  | PI12  | 31  |  | 32  | PI1  | TWI4-SDA  | UART4-RX  | PWM0-2  | I2S2-DIN2  | I2S2-DOUT2  | PI-EINT1  | 257   
262  |  | PI-EINT6  | SPI2-CSO  | PWM0-7  | UART6-TX  | UART4-RTS  | PI6  | 33  |  | 34  | GND  |  |  |  |  |  |  |   
269  |  | PI-EINT13  | I2S2-MCLK  | PWM0-14  | DMIC-DATA3  | UART6-CTS  | PI13  | 35  |  | 36  | PI3  |  | UART5-RX  | PWM0-4  | I2S2-LRCK  | SPI1-CLK  | PI-EINT3  | 259   
|  |  |  |  |  |  | GPADC2  | 37  |  | 38  | PI5  | UART5-CTS  | SPI1-MISO  | PWM0-6  | I2S2-DINO  | I2S2-DOUT1  | PI-EINT5  | 261   
|  |  |  |  |  |  | GND  | 39  |  | 40  | PI4  | UART5-RTS  | SPI1-MOSI  | PWM0-5  | I2S2-DOUT0  | I2S2-DIN1  | PI-EINT4  | 260 
[code] 
       Note: 
       * The USB signal and GPIO(TWI/UART/PWM) signal on PIN 27 and PIN 28 cannot be active simultaneously and require different SKUs. Please refer to the Models and SKU section below.
    
[/code]  
# Tips, Tricks, Caveats
## FEL mode
A dedicated FEL button. [FEL mode][46971] will be entered without an SD card and with no valid eGON signature on the SPI flash. Alternatively the usual FEL trigger SD card image can be used. 
The USB-C connector used to power the board carries the USB-OTG signals for the FEL mode, so the board needs to be powered through a host computer or a powered USB hub for using FEL mode. 
Using [Sunxi-tools][46972] and issuing on the commercial-grade version of the board: 
[code] 
    sunxi-fel ver
[/code]
shows: 
[code] 
    AWUSBFEX soc=00001890(A523) 00000001 ver=0001 44 08 scratchpad=00001500 00000000 00000000
[/code]
## LEDs
There are two unlabelled LEDs on the board, a blue and a green one. According to the schematic they are Power (green) and Status (blue), but both are connected to GPIOs (PC12 and PC13), so need active software toggling to light up. 
## SPI booting
The board contains a 16MB SPI NOR flash chip, and the SoC can boot firmware from there. 
# Serial port
The UART pins are located at PIN 8 and PIN 10 at 40P GPIO of the board. You can use this serial port to log in or debug the system with a baud rate of **115200** , **8** data bits, **1** stop bit, **no** parity. Just attach some leads according to our [UART Howto][46973]. 
  * [![Radxa cubie a5e debug uart.jpg][46974]][46975]

# Models and SKU
**Example SKU Code** : RS500-D1E0G0J0R38S16 
  * RS500: Code for Cubie A5E
  * D1E0G0J0R38S16: Configurations, as explained in the table below:

Code  | Explanation  | Options  | Description   
---|---|---|---  
D  | DRAM Size  | D1  | 1GB RAM   
D2  | 2GB RAM   
D4  | 4GB RAM   
E  | eMMC Size  | E0  | eMMC chip not soldered   
E8  | 8GB eMMC   
E16  | 16GB eMMC   
E32  | 32GB eMMC   
G  | GPIO PIN#27/#28 Function  | G0  | PIN#27/#28 GPIO Function   
G1  | PIN#27/#28 USB Function   
J  | Industrial Grade  | J0  | Commercial Grade (0 °C ~ 60 °C)   
J1  | Industrial Grade (-40 °C ~ 85 °C)   
R  | SoC Model  | R38  | A527 SoC   
R41  | T527 SoC   
S  | SPI Flash Size  | S0  | SPI Flash Not Soldered   
S16  | 16MB SPI Flash   
# Pictures
  * [![Radxa Cubie A5E connectors.jpg][46976]][46977]
  * [![Radxa Cubie A5E chips.jpg][46978]][46979]
  * [![Radxa Cubie A5E gpio.jpg][46980]][46981]

# Schematics
  * [File:Radxa cubie a5e schematic v1.1 20250113.pdf][46982]
  * [File:Radxa cubie a5e schematic v1.2 20250113.pdf][46983]
  * [File:Radxa cubie a5e components placement map v1.2 20250113.pdf][46984]
  * [File:Radxa cubie a5e components placement map v1.1 20250113.pdf][46985]

# See also
