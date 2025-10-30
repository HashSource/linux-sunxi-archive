# Buying guide
If you are looking to acquire an Allwinner based device, then chances are that you are looking for the device with the best community support. 
While some development boards are very common in our sunxi community, and they therefore are best supported, we have the ability to easily support just about any [A10][10995], [A13][10996], [A10s][10997] and [A20][10998] based device (support for newer SoCs, like [A31][10999], [A23][11000] and [A31s][11001], is still lagging behind). This means that we can [easily bring up previously unknown devices][11002], but it might still be a good idea to choose the best known hardware. 
## Contents
  * [1 Recommended Development boards][11003]
    * [1.1 Open Source Hardware][11004]
      * [1.1.1 Olimex][11005]
    * [1.2 Community Hardware][11006]
      * [1.2.1 Cubietech][11007]
      * [1.2.2 Rhombus Tech][11008]
  * [2 Recommended tablets][11009]
  * [3 Other devices][11010]
  * [4 Support status][11011]

# Recommended Development boards
## Open Source Hardware
At sunxi we fully support the [OSHW][11012] initiative, as this gives people the freedom to adapt hardware designs to their own needs. 
### Olimex
Currently, [Olimex][11013] is the only company creating Allwinner based [OSHW][11012], and [Olimex][11013] actively contributes to the sunxi project. We particularly recommend: 
  * [A10-OLinuXino-LIME][11014]: An ultra cheap board with 512MiB RAM, HDMI, ethernet and SATA.
  * [A13-OLinuXino][11015]: A more full featured board with 512MiB RAM, optional 4GB NAND and optional 4GB Wifi.
  * [A20-OLinuXino-LIME][11016]: Based on the _A10-OLinuXino-LIME_ , but with a more advanced A20 CPU.
  * [A20-OLinuXino-LIME2][11017]: Similar to _A20-OLinuXino-LIME_ , features 1GB RAM and Gigabit ethernet.
  * [A20-OLinuXino-Micro][11018]: Powerful and complete Olimex board, with 1GB RAM, 4GB NAND, ethernet (100MBit/s), SATA and HDMI.

Olimex devices offer a lot of expansion possibilities through GPIO connectors, or Olimex's own [expansion modules][11019]. 
## Community Hardware
Some companies actively participate with and contribute to the sunxi community. While they don't always produce [OSHW][11012] devices, schematics tend to be available. 
### Cubietech
[Cubietech][11020] has been working with the sunxi community from the start, and the devices they create come with full schematics. 
  * [Cubieboard][11021]: The original cubietech board. Comes with an [A10][10995] SoC, 1GB RAM, 4GB NAND, SATA, Ethernet and HDMI.
  * [Cubieboard2][11022]: An updated cubieboard with an [A20][10998] SoC.
  * [Cubietruck][11023]: A full featured [A20][10998] board with 2GB RAM, 4GB NAND, Gigabit ethernet, WiFi, SATA, Bluetooth, HDMI and VGA.

### Rhombus Tech
[Rhombus Tech][11024] has been working on creating libre software supported devices since the start: they started the initial community that formed around Allwinner SoCs and became linux-sunxi. They are working on a range of modular platforms, the first being [EOMA-68][11025], with plans for a huge range of [community designs][11026] including a modular tablet, modular desktop and modular netbook. Currently running is a crowd-funding campaign on [Crowd Supply][11027] which turns into a "shop" after the campaign ends. 
# Recommended tablets
This section is still under construction and no particular tablet recommendations are available yet. While we can hardly expect the tablets to be proper [OSHW][11012] hardware, some tablets are expected to be much less problematic than the others for free software enthusiasts. A preliminary checklist for the wanted features: 
  * The device should be preferably easy to identify and the advertised specs should be reasonably accurate (trying to buy an Allwinner tablet and getting a Rockchip, Mediatek, Amlogic or Active instead is not always a pleasant surprise). If you are buying a no-name tablet from Aliexpress, Amazon or Ebay, pay special attention to negative reviews even if the vast majority of reviews are positive. Even if the description clearly states "Allwinner", it may still have a different SoC under the hood. Most users are happy as long as their cheap tablet just boots some sort of Android and works with it. But a few people who actually care about the SoC choice, may leave a lone warning somewhere in the comments. 
    * Read reviews of the device. eg. WiFi reception, screen durability and brightness, touch response, build quality and many other features of the tablet cannot be determined from a vendor specification. If the device is not identifiable easily enough that you can find reviews of it or that you can be sure the review actually applies to the device you are ordering you will never know what you get.
  * Availability of the stock firmware for download from the vendor site (for unbricking)
  * Availability of the firmware sources (for GPL compliance)
  * Good support for the peripherals (touchscreen, WIFI, ...) in the mainline kernel and sunxi-3.4
  * Reasonable features (screen resolution, screen quality, HDMI/USB connectors, battery capacity, ...)
  * Reasonable price

Somewhat worldwide available brands that produce Allwinner based tablets include 
  * [Prestigio][11028]
  * [MSI][11029]
  * [KD Interactive(Kurio) ][11030]
  * [Sencor][11031]
  * [Hewlett-Packard][11032]

Please add any other producers of recognizable Allwinner based hardware that you find. 
# Other devices
If none of the above boards suit your goals, then there are plenty more devices to choose from: 
► [A10 Boards][11033]► [A10 HTPC][11034]► [A10 Netbooks][11035]► [A10 Tablets][11036] | ► [A10s Boards][11037]► [A10s HTPC][11038]► [A10s Other][11039] | ► [A13 Boards][11040]► [A13 Ereaders][11041]► [A13 Tablets][11042] | ► [A20 Boards][11043]► [A20 HTPC][11044]► [A20 Other][11045]► [A20 Tablets][11046] | ► [A23 Tablets][11047] | ► [A31 Boards][11048]► [A31 HTPC][11049]► [A31 Tablets][11050] | ► [A31s Boards][11051]► [A31s HTPC][11052]► [A31s Tablets][11053] | ► [A33 Boards][11054]► [A33 Tablets][11055] | ► [A64 Boards][11056]► [A64 Tablets][11057] [Pine Pinebook][11058] [PinePhone][11059] | ► [A80 Boards][11060]► [A80 HTPC][11061] | ► [A83T Boards][11062]► [A83T Tablets][11063] | ► [H2+ Boards][11064] | ► [H3 Boards][11065]► [H3 HTPC][11066] [8BCraft Retrostone][11067] | ► [H5 Boards][11068] | ► [H8 Boards][11069] | ► [H64 HTPC][11070]  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
As previously stated, we have the ability to [easily support previously unknown hardware][11002], so the above list should not limit your options. 
# Support status
The [ device][11071] support is being developed on several fronts: 
  * The U-Boot bootloader development is being tracked on the [Mainline U-Boot][11072] page. Each [device page][11073] also has a detailed description of the bootloader status and instructions for that particular device. U-Boot is the de facto way of booting the devices so it is crucial for operating with the device. If a board is not supported yet in the official U-Boot, sometimes a compatible device configuration might work. Some Linux distributions (such as [Armbian][11074]) also have pretty up to date support for devices with 3rd party patches.

  * Devices such as development boards (see the [Table of Allwinner based boards][11075] page for more info) might come with official kernels and distributions. The [device pages][11071] provide links to 3rd party sites offering this support.

  * While the official kernel support from the device makers is often lacking, depends on badly outdated kernels, and might contain closed source binary blobs or licensing issues, the mainline support for devices is improving with each new kernel release. The long term goal is to provide official support for the devices in the mainline kernel. The status of this work for the sunxi devices is summarized on the [Linux mainlining effort][11076] page. Again, each [device page][11077] also has a detailed description of the kernel support status. There are also numerous kernel and userspace subsystems dealing with device specific hardware support, which have their own status pages with more details. For instance, the wiki contains pages for [Cedrus][11078] and [Cryptographic Hardware Accelerators][11079].
