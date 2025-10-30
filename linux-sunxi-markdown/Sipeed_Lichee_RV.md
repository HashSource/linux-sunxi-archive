# Sipeed Lichee RV
Sipeed Lichee RV  
---  
[![Lichee-rv.jpeg][50745]][50746]  
Manufacturer |  [Sipeed][50747]  
Dimensions |  46.2 _mm_ x 25.0 _mm_  
Release Date |  November 2021   
Website |  [official documantation][50748] [Product Page][50749]  
Specifications   
SoC |  [D1][50750] @ 1.0Ghz   
DRAM |  512MiB DDR3 @ 792MHz, 1×[H5TQ4G63EFR][50751]  
Power |  DC 5V @ 2A (via OTG Type-C connector)   
Features   
Video |  SPI LCD (optional); via expansion board: HDMI (Type A - full), LVDS   
Audio |  via expansion board: audio, HDMI, I2S   
Network |  via expansion board: Realtek RTL8723DS   
Storage |  µSD   
USB |  1 USB Type-C OTG   
Other |  Power LED, system LED, OK & FEL buttons   
Headers |  4-pin UART DEBUG   
This page needs to be properly filled according to the [New Device Howto][50752] and the [New Device Page guide][50753].
The test pin near the power LED is RST (reset). 
## Contents
  * [1 Software Support][50754]
  * [2 FEL mode][50755]
  * [3 UART][50756]
  * [4 Pins][50757]
    * [4.1 User LED][50758]
  * [5 Optional screen][50759]
  * [6 Carrier Boards][50760]
    * [6.1 Lichee RV Dock][50761]
    * [6.2 Lichee RV Dock Pro][50762]
    * [6.3 Lichee RV 86 Panel][50763]
    * [6.4 jeadock][50764]
    * [6.5 Boot and system support][50765]
      * [6.5.1 Pre-made images][50766]
      * [6.5.2 Images builder][50767]
      * [6.5.3 Building mainline kernel][50768]
  * [7 Sipeed Mirrors][50769]
  * [8 Other Resources][50770]
  * [9 Pictures][50771]

## Software Support
Linux and U-Boot upstreaming are in progress. See [Allwinner_Nezha#Manual_build][50772] for build instructions. For U-Boot, use the `lichee_rv_dock_defconfig` configuration. 
The board mainline support is added in Linux-next in february, 2023 (ready for Linux-6.3). It can be installed using last linux-6.2-rc + linux-next patch. 
## FEL mode
The `FEL` button triggers [ FEL mode][50773]. 
The [xfel][50774] tool has support for the D1 chip. Currently `sunxi-fel` (from [Sunxi-tools][50775]) lists the SoC as `unknown`. 
## UART
[![][50776]][50777]
[][50778]
UART connectors holes at the left of the USB-C connector
The board has 4 pins holes at left of USB-C port for UART and is sold with the 4 pins to be soldered (not needed if you have the Dock). The pins name are wrote at the back of the board. from Top to bottom: 
  * **5V**
  * **G** round
  * **R** x
  * **T** x

This board can be powered by UART, by plugin a 5V pin. See the [UART Howto][50779] for general usage of UART. 
The pins should be soldered with pins at top top still be accessible when using the LicheeRV Dock. 
Board can be powered by UART alone or by USB-C port. 
## Pins
Pinout of the M.2 B-Key 67×2 pins connectors of the SoM is described [in schematic file][50780]
### User LED
The user LED on the board can be controlled via GPIO65. The SoC include an RGB LED controller (led-controller@2008000). 
## Optional screen
There is an optional 1.14" 135×240 SPI LCD screen coming with the board. It uses Sitronix ST7789V controller ([Datasheets][50781]). There is the [panel_Sitronix_ST7789V driver][50782] included in mainline. 
Pinout of the LED socket, after [schematic file][50780] are : 
  * SCK = PC2/LCD_SCK
  * MOSI = PC4
  * RS = PC5
  * CS = PC3
  * RESET = PC6
  * LEDA (screen backlight) = PD18

Another driver is included in Linux mainline in [FBTFT][50783] for using RGB port with framebuffer. But this staging driver [depend on FBTFT external source][50784] that has not been updated since August, 2021, and isn't compatible with kernel >=6.x. Looks like DRM replace progressively fb, a drmfb compatibility layer can be used if needed. 
There is also a [TinyDRM][50785] version of the driver, it was included in FBTFT, and is now include by default (at least on Linux 6.x) 
For information, the connector and driver are compatibles between Sipeed LicheeRV and Sipeed Longan Nano, just need to adapt the resolution. It can be helpful for tests in case of problem with screen. 
After [official documentation about screen][50786], the board support the following screens: 
  * SPI screen 1.14 inch(TODO)
  * RGB screen 4.3 inch 480x272；5.0 inch 800x480；
  * RGB+SPI screen 4.0 inch 480x480(st7701s); 4.0 inch 720x720(nv3052c)
  * MIPI screen 8.0 inch 1280x720(ILI9881C)

[code] 
    cat /sys/class/disp/disp/attr/sys
    
    screen 0:
    de_rate 300000000 hz, ref_fps:60
    mgr0: 480x480 fmt[rgb] cs[0x204] range[full] eotf[0x4] bits[8bits] err[0] force_sync[0] unblank direct_show[false] iommu[1]
    dmabuf: cache[0] cache max[0] umap skip[0] overflow[0]
        lcd output	backlight( 50)	fps:59.5	esd level(0)	freq(60)	pos(0)	reset(0)	 480x 480
        err:0	skip:184	irq:230715	vsync:0	vsync_skip:0
       BUF    enable ch[1] lyr[0] z[16] prem[N] a[globl 255] fmt[  0] fb[ 480, 480; 480, 480; 480, 480] crop[   0,   0, 480, 480] frame[   0,   0, 480, 480] addr[ffe00000,       0,       0] flags[0x       0] trd[0,0]
[/code]
## Carrier Boards
### Lichee RV Dock
[![][50787]][50788]
[][50789]
oreboot + RustSBI + LinuxBoot
This small board has a built-in mic, speaker port, reset button, one extra button, HDMI and USB ports, an FPC connector for a mic array, a 40 pin HAT style GPIO header, and an option for a Wi-Fi add-on SoM plus the corresponding antenna port. 
[![][50790]][50791]
[][50792]
The two pins at left are 5V. the most left pin of the lower row is 3.3V
The Dock has [UART pins connected to the CPU][50793] ([mirror][50794]) allowing to debug without soldering. For the upper row: 5V, 5V, GND, TX, RX, TP_RST, GND 
There are solder pads for an optional SPI flash (NAND or NOR) below the module. 
### Lichee RV Dock Pro
The Pro variant of the Dock is a bit larger in height, with a 16MB SPI NOR flash included, display connectors instead of the mic array connector, and an extra USB-C port for debugging via UART and/or JTAG. 
Behind the debug USB port sits a [Bouffalo Lab BL702][50795], listed as `42bf:b210 Bouffalo C-Sky CKLink-Lite`. It offers a `ttyACM` device on Linux to connect to via Minicom etc. 
References: [stock firmware boot log][50796]
### Lichee RV 86 Panel
The [Lichee RV 86 Panel][50797] is a box with a 480×480 or 720x720 LCD touchscreen panel, ethernet with power supply, optional Wi-Fi, a speaker, and GPIOs exposed at the back for adding a header. 
[![][50798]][50799]
[][50800]
Lichee RV 86 Panel
### jeadock
This is a custom board, not officially for sale, but open hardware. For the board design and schematic, see [repository][50801], and read the [blog post on the design process][50802]. 
### Boot and system support
#### Pre-made images
  * [**Sipeed Lichee RV** Archlinux 6.1.0-rc3 with LED and 1.14 Display support][50803]

    Login/pass: `root` / `archriscv`;
[code] 
     git clone https://github.com/miloserdev/sunxi_licheerv.git
     cd ./sunxi_licheerv
     ./create_sd.sh /dev/mmcblk0
    
[/code]
  * A [port of oreboot][50804] (Rust version of coreboot, so without C).
  * [U-Boot][50805] (See also [Allwinner Nezha][50806])
  * XBoot <https://github.com/xboot/xboot> bare-metal multimedia system that manage most of peripherals.
  * RTOS based Tina, and Linux based Debian and Ubuntu images are available from Sipeed mirrors ([Some Tutorials, in Chinese][50807]):
  * The [vendor-provided Debian image][50808] can use HDMI, (requires [OpenixCard][50809], a clone of [Windows only "PhoenixCard" tool][50810] to be written onto an SD card) volunteers have created such SD card and then saved its full contents into [a raw-format image file][50811], suitable for writing with **dd**.

    Login/pass: `sipeed` / `licheepi`; WiFi can be set up by Connman (there are [reports][50812] of transient lock-ups on associating to encrypted WiFi)
    16GB Image, **if you use a larger microSD don't repair the GPT or you will not boot anymore!!!**
    The partition number 8 can be deleted with fdisk or parted, and then partition 7 grown with parted to the whole microSD card, and filesystem itself with resize2fs. System still boot and work after this modification.
    sha256sum of the xz: `cf73baf3ed67d480e7606c666ccb81fce21295ba8fbba10e0ad86939065be6ffw`
    Asciinema [record of the boot sequence][50813] ([on Asciinema][50814]) with LicheeRV Dock
  * Ubuntu image displays the TTY on the Lichee RV LCD screen, keyboard can be used on Dock USB port. Archive include a readme about how to make the microSD card. In some cases, **80MB (163840) should be used instead of 40MB (81920, as wrote on the README)** as start of the primary partition.

    Login/Pass: `root` / `2183abc`
    sha256sum of the tgz: 4a414a36ba5ae8000bd2f8ee088ea399b502527e1868662427bc00676d65ca79
    [asciinema][50815] [record of the boot sequence][50816] ([on Asciinema][50817])
  * There is a working Debian image "RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip" that can be dd on a 32GB microSD card and boot on LicheeRV with several drivers working including the optional LCD screen (wait 2 or 3 minutes if you don't have serial), detect HDMI, WiFi, UVC Video of the Dock and wait for ethernet (to be investigated). It is mirrored [here][50818] from [here][50819] [original source][50820] The 6.1 version need the PhoenixCard tool.

    id/pass: `root` / `rvboards`
    SHA256sum: `bf3da52b179f03fd46c16d44d4f7ae71b53745ce4f260e13e03e48e1c626c461`
    kernel: Linux RVBoards 5.4.61 #12 PREEMPT Thu Jun 3 08:39:01 UTC 2021 riscv64 GNU/Linux [config.gz][50821]
    Asciinema [record of the boot sequence][50822] ([on Asciinema][50823]) with LicheeRV Dock
  * Minimal console-only (no hdmi due to closed-source kernel module) Debian ddimage with updated kernel/u-boot, wifi support, and a sane partition layout. Available [here][50824]

    Users: `root` / `sunxi` or `user` / `sunxi`
    SHA256sum: e5254b7815516c10b59d54e5a9247241502e676014c506eb2cbf01b9f9b508cd
    4GB image, compressed to 340MB, resizable with resize2fs
    kernel 5.14.0-rc4-nezha from <https://github.com/Cezarus27/linux/tree/riscv/d1-wip> with the following patch and .config available in /lib/modules [patch][50825]
  * Clean (i.e. no Android partition nonsense) Debian image with functioning HDMI (LXDE desktop) and 5.18 smaeul kernel (cc63db754b21) [here][50826]; **Warning:** if you upgrade this image to the latest Debian Sid as of 2024-05, some programs will start failing with an "Illegal instruction" error, e.g. shared-mime-info 2.4, and importantly the apt-get HTTP backend, so it becomes problematic to upgrade/downgrade after that.

    kernel config [here][50827]
    id/pass: `root` / `sunxi`
    SHA256sum: 503d91fbc73ae067b9685a327797d92f85369f6a408f71b8cc00eae49ca62f9c
    8GB image, compressed to 1.7GB, flash with `zstdcat licheerv-debian-clean-hdmi.zst > /dev/mmcblk0`
    image contains gparted for resizing to the full size of your card
    
#### Images builder
  * Arch linux: [Sehraf Arch Image Builder][50828] \- Last mainline kernel with Sameul patch (5.18.0-rc4-gf4bce410a6b4 has HDMI output, not more recent ones, probably due to some missing parameters in config file)
  * Debian: [Debian D1 build][50829] \- Last mainline kernel with Sameul patch
  * NixOS: [NixOS Image Builder][50830]
  * [LicheeRVBSPRebuild][50831] builds just the bootloader and kernel with patches from the Sipeed SDK. This can be combined with a Linux rootfs like Arch to create a full Linux system
  * SkiffOS: [SkiffOS Image Builder][50832] builds a fully-featured system including the bootloader, kernel, userspace, and with optional Docker support.

#### Building mainline kernel
The first script of [Archlinux Image Builder][50828] create automatically the last patched Sameul kernel, with working WiFi, HDMI, usb ethernet dongles, and fully open source boot parts. 
  * [Bottier][50833] build mainline kernel next, and allow to tune it by pass, and to install it on a card already built with Archlinux Image Builder (currently most things work but HDMI)

## Sipeed Mirrors
  * [pan.Baidu][50834] (提取码/password)：wbef
  * [Mega.nz][50835]
  * [Other mirror for the OS images][50836]

## Other Resources
  * [Sipeed Lichee RV Archlinux with LED and 1.14 Display support][50803]
  * [AllWinner D1 on Fedora Wiki][50837]
  * [how to build neural network ncnn framwork on D1][50838]
  * [Documentation Nezha D1 on RVBoards.org][50839] the author of the working Debian 11 image.

## Pictures
  * [![][50840]][50841]
LicheeRV backside. The LCD screen connector at upper-right is in open position to insert the flat ribbon. 
  * [![][50842]][50843]
LicheeRV with its optional screen, plugged in LicheeRV Dock (WiFi version) 
  * [![][50844]][50845]
LicheeRV Dock, Front (WiFi version), the Wifi chip can be seen on the right, and at it's bottom right, the antenna connector. 
  * [![][50846]][50847]
LicheeRV Dock, back (WiFi version) with some marks for UART+5V+3.3V+GND pins. 
  * [![][50848]][50849]
Lichee RV Dock Pro bare board, incl. 128Mbit NOR flash and Wi-Fi 
  * [![][50850]][50851]
Lichee RV Dock Pro with Lichee RV module
