# Radxa Cubie A7A
Radxa Cubie A7A  
---  
[![Radxa Cubie A7A top.jpg][47023]][47024] [][47025]  
Manufacturer |  [Radxa][47026]  
Dimensions |  _56mm_ x _85mm_  
Release Date |  July 2025   
Website |  [Radxa Cubie A7A][47027]  
Specifications   
SoC |  [A733][47028]  
DRAM |  2/4/6/8/16GiB LPDDR5 @ 4800 MT/s   
Power |  DC 5V @ 4A via USB-C connector   
Features   
Video |  Standard HDMI 2.0b, MIPI FPC connector   
Audio |  Line out on header, HDMI audio   
Network |  WiFi 802.11 a/b/g/n/ac/ax (Quectel FCU760K), 1x 10/100/1000Mbps Ethernet ([Maxio MAE0621A][47029]), supports PoE   
Storage |  µSD, 128Mbit [SPI flash][47030] (Winbond W25Q128JWPIQ), eMMC Module, UFS Module   
USB |  3 X USB2.0 Host, 1 X USB3.0 HOST, 1x USB 2.0 OTG Type C   
Other |  1x PCIe 3.0 FPC   
Radxa Cubie A7A is the 2nd Allwinner based SBC introduced by Radxa, in a credit card size form factor. 
## Contents
  * [1 Identification][47031]
  * [2 General Notes][47032]
    * [2.1 Radxa BSP][47033]
    * [2.2 Allwinner SDK][47034]
    * [2.3 Tools][47035]
    * [2.4 Manual build][47036]
      * [2.4.1 U-Boot][47037]
      * [2.4.2 Linux Kernel][47038]
  * [3 Expansion ports][47039]
  * [4 Sunxi support][47040]
    * [4.1 Current status][47041]
  * [5 Pictures][47042]
  * [6 Schematics][47043]
  * [7 See also][47044]

# Identification
The PCB has a version number silkscreened at the top: 
[code] 
    Radxa Logo
    Cubie A7A V1.10
    
[/code]
# General Notes
Firmware download port is the USB C power port. 
RadxaOS is our current primary and actively developed operating system, and we recommend using it—featuring updated hardware drivers, regular security patches, and performance optimizations for your Radxa device. 
You can download it from the github page: <https://github.com/radxa-build/radxa-cubie-a7a/tags>
## Radxa BSP
allwinner-target: <https://github.com/radxa/allwinner-target/tree/target-a733-v1.4.6>   
allwinner-device: <https://github.com/radxa/allwinner-device/tree/device-a733-v1.4.6>   
allwinner-bsp: <https://github.com/radxa/allwinner-bsp/tree/cubie-aiot-v1.4.6>   
kernel: <https://github.com/radxa/kernel/tree/allwinner-aiot-linux-5.15>   
u-boot: <https://github.com/radxa/u-boot/tree/cubie-aiot-v1.4.6>   

Repository path in TinaSDK:   

[code] 
    allwinner-target => target/a733/
    allwinner-device => device/config/chips/a733/
    allwinner-bsp    => bsp/
    kernel           => kernel/linux-5.15/
    u-boot           => brandy/brandy-2.0/u-boot-2018/
    
[/code]
## Allwinner SDK
Tina SDK 1.4.6(partially uploaded):: <https://gitlab.com/tina5.0_aiot>   
Tina SDK 1.4.6(complete repo package, use command 'repo sync -l' to restore directory structure):  
Mega: [https://mega.nz/file/kFtD0BYY#zm3FXLiLK9SfOFss3BGY1Kx714BFBqyyPeYeE5FvOw0][47045]   
BaiduPan: <https://pan.baidu.com/s/1zcVq4l-rij7RPmJ92nccZg> password: 547b   
NOTE:   
Modify the name of the spl-pub folder under the brandy directory, for example, change it   
to spl-pub-bak, so that it no longer participates in compilation. The files compiled   
in this directory will replace the binary files in the devcie/xxxx/configs/a733/bin   
directory. However, we now need to temporarily use the binary files provided by   
Allwinner to achieve a better experience.  

## Tools
For Allwinner Phoenix Image:  
Linux Image Flash tool(CLI): <https://dl.radxa.com/tools/linux/phoenixconsole-3.0.9_amd64.deb>   
Windows Image Flash tool(UI): <https://dl.radxa.com/tools/windows/PhoenixCard_V4.3.2_20250331_1604_Release.zip>   

  

## Manual build
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
    Choice [android]: 1
    All available linux_dev:
       0. bsp
       1. dragonboard
       2. buildroot
       3. debian
       4. yocto
    Choice [bsp]: 3
    All available kern_name:
       0. linux-5.10
       1. linux-5.15
    Choice [linux-5.10]: 1
    All available ic:
       0. a523
       1. a527
       2. a733
       3. t527
       4. t736
    Choice [a523]: 2
    All available board:
       0. QA
       1. cubie_a7a
       2. fpga
       3. perf1
       4. pro2
       5. pro3
    Choice [QA]: 1
    All available flash:
       0. default
       1. nor
    Choice [default]: 0
    All available rootfs files:
       0. linaro-bullseye-gnome-arm64.tar.gz
       1. linaro-bullseye-lite-arm64.tar.gz
       2. linaro-bullseye-lxde-arm64.tar.gz
       3. linaro-bullseye-xfce-arm64.tar.gz
       4. linaro-bullseye-xfce-ros2-humble-arm64.tar.gz
    Choice [linaro-bullseye-gnome-arm64.tar.gz]: 3
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
    ./build.sh -p sun60iw2p1 -b a733
    
    # This will using sun60iw2p1_defconfig under the u-boot-2018/configs directory.
    # And compile the components required for the bootloader, including boot0, fes1, sboot, and u-boot.
    
    output: 
    u-boot-sun60iw2p1.bin 
    boot0_sdcard_sun60iw2p1.bin
    fes1_sun60iw2p1.bin
    sboot_sdcard_sun60iw2p1.bin 
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
    
    # 2）This will use the defconfig file located at device/config/chips/a733/configs/cubie_a7a/debian/linux-5.15/bsp_defconfig and
    the device tree file at device/config/chips/a733/configs/cubie_a7a/linux-5.15/board.dts.
    
    
    # 3）You will find the kernel image in the out/a733/cubie_a733/debian/ directory.
    
    +-----+-----------+--------------------------------------------------------+
    | num | type      | use                                                    |
    +=====+===========+========================================================+
    | 1   | boot.img  | bootimg containing the kernel and device tree   |
    +-----+-----------+--------------------------------------------------------+
    | 2   | sunxi.dtb | The device-tree blob                                   |
    +-----+-----------+--------------------------------------------------------+
    
    
[/code]
# Expansion ports
The Cubie A7A has a 40-pin, 0.1" populated connector with several low-speed interfaces. 
FUNC9  | FUNC8  | FUNC7  | FUNC6  | FUNC5  | FUNC4  | FUNC3  | FUNC2  | FUNC1  | Pin#  | Pin#  | FUNC1  | FUNC2  | FUNC3  | FUNC4  | FUNC5  | FUNC6  | FUNC7  | FUNC8  | FUNC9  | FUNC10   
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
|  |  |  |  |  |  |  | +3.3V  | 1  | 2  | +5.0V  |  |  |  |  |  |  |  |  |   
PJ-EINT23  | LCD0-D9  | TWI11-SDA  | TWI3-SDA  | TWI7-SDA  | UART2-CTS  | UART3-RX  | PWM1-5  | PJ23  | 3  | 4  | +5.0V  |  |  |  |  |  |  |  |  |   
PJ-EINT22  | LCD0-D8  | TWI11-SCK  | TWI3-SCK  | TWI7-SCK  | UART2-RTS  | UART3-TX  | PWM1-4  | PJ22  | 5  | 6  | GND  |  |  |  |  |  |  |  |  |   
| PB-EINT0  | JTAG-MS  | LCD0-D0  | DSI-TRIG-LCD-TE1  | SPI2-CS0  | UART0-TX  | UART2-TX  | PB0  | 7  | 8  | PB9  | UART0-TX  | I2S0-DIN2  | I2S0-DOUT2  | PWM1-1  | WATCHDOG-SIG  | LCD0-D16  | TWI8-SCK  | TWI0-SCK  | PB-EINT9   
|  |  |  |  |  |  |  | GND  | 9  | 10  | PB10  | UART0-RX  | I2S0-DIN3  | I2S0-DOUT3  | PWM1-2  | PLL-LOCK-DBG  | LCD0-D17  | TWI8-SDA  | TWI0-SDA  | PB-EINT10   
|  | PB-EINT1  | JTAG-CK  | LCD0-D1  | SPI2-CLK  | UART0-RX  | UART2-RX  | PB1  | 11  | 12  | PK0  | MCSIA-D0N  | UART6-DCD  | I2S4-BCLK  | HDMI-CEC  | TWI1-SDA  | NCSI1-HSYNC  | SGPIO-SLOAD  | PK-EINT0  |   
|  | PL-EINT6  | S-PWM0-4  | S-IR-RX  | S-SPI0-MOSI  | S-UART0-TX  | S-JTAG-DO  | PL6  | 13  | 14  | GND  |  |  |  |  |  |  |  |  |   
|  |  | PL-EINT7  | S-PWM0-5  | S-SPI0-MISO  | S-UART0-RX  | S-JTAG-DI  | PL7  | 15  | 16  | PJ24  | PWM1-6  | UART4-TX  | TWI4-SCK  | SPI3-CLK  | PJ-EINT24  |  |  |  |   
|  |  |  |  |  |  |  | +3.3V  | 17  | 18  | PJ25  | PWM1-7  | UART4-RX  | TWI4-SDA  | SPI3-MOSI  | PJ-EINT25  |  |  |  |   
| PD-EINT12  | PWM1-2  | SPI1-MOSI  | EINK-D12  | DSI1-D1P  | LVDS1-D1P  | LCD0-D18  | PD12  | 19  | 20  | GND  |  |  |  |  |  |  |  |  |   
| PD-EINT13  | PWM1-3  | SPI1-MISO  | EINK-D13  | DSI1-D1N  | LVDS1-D1N  | LCD0-D19  | PD13  | 21  | 22  | PL10  | S-UART0-TX  | S-TWI2-SCK  | S-UART1-TX  | S-PWM0-8  | PL-EINT10  |  |  |  |   
| PD-EINT11  | PWM1-1  | SPI1-CLK  | EINK-D11  | DSI1-D0N  | LVDS1-D0N  | LCD0-D15  | PD11  | 23  | 24  | PD10  | LCD0-D14  | LVDS1-D0P  | DSI1-D0P  | EINK-D10  | SPI1-CS0  | PWM1-0  | PD-EINT10  |  |   
|  |  |  |  |  |  |  | GND  | 25  | 26  | PD14  | LCD0-D20  | LVDS1-D2P  | DSI1-CKP  | EINK-D14  | SPI1-HOLD  | UART3-RTS  | PD-EINT14  |  |   
| PD-EINT1  | UART3-RX  | TWI2-SDA  | EINK-LEH  | DSI1-D2N  | LVDS1-CKN  | LCD0-D23  | PD17  | 27  | 28  | PD16  | LCD0-D22  | LVDS1-CKP  | DSI1-D2P  | EINK-OEH  | TWI2-SCK  | UART3-TX  | PD-EINT16  |  |   
PK-EINT5  | JTAG-MAS-CK  | NCSI1-D14  | SPI3-CLK  | PWM1-9  | PWM1-8  | PCIE-CLKREQN  | MCSIA-CKP  | PK5  | 29  | 30  | GND  |  |  |  |  |  |  |  |  |   
PK-EINT6  | JTAG-MAS-DO  | NCSI1-D13  | SPI3-MOSI  | UART2-RTS  | UART4-TX  | TWI2-SCK  | MCSIA-D2N  | PK6  | 31  | 32  | PD20  | LCD0-HSYNC  | DSI-TRIG-LCD-TE1  | TWI0-SCK  | EINK-CKV  | PCIE-CLKREQN  | UART4-TX  | TWI3-SCK  | PWM0-2  |   
PK-EINT7  | JTAG-MAS-DI  | NCSI1-D12  | SPI3-MISO  | UART2-CTS  | UART4-RX  | TWI2-SDA  | MCSIA-D2P  | PK7  | 33  | 34  | GND  |  |  |  |  |  |  |  |  |   
PK-EINT2  | SGPIO-SDATAIN  | NCSI1-PCLK  | TWI5-SDA  | HDMI-SDA  | I2S4-LRCK  | UART6-DTR  | MCSIA-D1N  | PK2  | 35  | 36  | PK1  | MCSIA-D0P  | UART6-DSR  | I2S4-MCLK  | HDMI-SCL  | TWI1-SCK  | NCSI1-VSYNC  | SGPIO-SCLK  | PK-EINT1  |   
PK-EINT8  | JTAG-MAS-NTRST  | NCSI1-D11  | SPI3-CS1  | UART2-TX  | UART4-RTS  | MCSI0-MCLK  | MCSIA-D3N  | PK8  | 37  | 38  | PK3  | MCSIA-D1P  | UART6-RI  | I2S4-DIN0  | I2S4-DOUT1  | TWI5-SCK  | NCSI1-MCLK  | SGPIO-SDATAOUT  | PK-EINT3  |   
|  |  |  |  |  |  |  | GND  | 39  | 40  | PK4  | MCSIA-CKN  | PCIE-WAKEN  | I2S4-DOUT0  | I2S4-DIN1  | SPI3-CS0  | NCSI1-D15  | JTAG-MAS-MS  | PK-EINT4  |   
# Sunxi support
## Current status
**Not Supported**
# Pictures
  * [![Radxa Cubie A7A gpio.jpg][47046]][47047]
  * [![Radxa Cubie A7A connectors.jpg][47048]][47049]
  * [![Radxa Cubie A7A bottom.jpg][47050]][47051]

# Schematics
  * [Radxa Cubie A7A schematic v1.10 pdf][47052]
  * [Radxa Cubie A7A components placement map v1.10 pdf][47053]

# See also
