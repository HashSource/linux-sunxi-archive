# Bootable OS images
## Contents
  * [1 GNU/Linux][10532]
    * [1.1 Alpine Linux][10533]
    * [1.2 Arch][10534]
    * [1.3 Berryboot][10535]
    * [1.4 Debian][10536]
    * [1.5 Fedora][10537]
    * [1.6 Gentoo][10538]
    * [1.7 Kali][10539]
    * [1.8 Linaro][10540]
    * [1.9 Mer][10541]
    * [1.10 openSUSE][10542]
    * [1.11 OpenWrt][10543]
    * [1.12 Parabola GNU/Linux-libre][10544]
    * [1.13 Slackware][10545]
    * [1.14 Tiny Core][10546]
    * [1.15 Tizen][10547]
    * [1.16 Ubuntu][10548]
  * [2 Android][10549]
    * [2.1 Cubieboard][10550]
    * [2.2 Generic H2+/H3 based device][10551]
  * [3 BSD derivatives][10552]
    * [3.1 FreeBSD][10553]
    * [3.2 NetBSD][10554]
    * [3.3 OpenBSD][10555]

# GNU/Linux
When the image you download is made for a different type of device (eg. [Cubieboard][10556] vs MK802) but using the same CPU (eg. [A10][10557]) you should be able to use it after updating u-boot and script.bin from your particular [hwpack][10558]. 
Some images that use very little hardware like the headless server images might work without changes on many devices. 
## Alpine Linux
experimental "Generic ARM" image (armhf): <http://alpinelinux.org/downloads/>
## [Arch][10559]
  * [ArchLinuxARM Official][10560] \- link down
  * [ArchLinuxARM][10561]

## [Berryboot][10562]
  * [Berryboot][10563]

_[![Exclamation.png][10564]][10565]Keep in mind berryboot is not a recommended boot image for A10 devices._
## [Debian][10566]
  * [Debian][10567] Unmodified Debian installation Wiki. [Stable][10568] [Unstable][10569] [Testing][10570] Images. You need a firmware.*.img.gz and the partition.img.gz. zcat firmware.<x>.img.gz partition.img.gz >/dev/sdn (if sdn is your µSD Reader)
  * [Armbian][10571] (build system and OS images for +30 different sunxi SBC)
  * [Bananian][10572] for Banana Pi/Pro
  * [Cubian][10573] for Cubieboard
  * [Debian Wheezy with LXDE][10574] \- link down
  * [Cubieboard / Cubietruck Debian Wheezy SD card image][10575] by **Igor Pečovnik**
  * [Hackberry Debian Wheezy (Headless) image][10576] ([discussion][10577])
  * [Mele headless: Debian wheezy (aka testing) armhf with nand install][10578]
  * [Minimal Debian Wheezy "Server" images for the A10 and A20][10579] by **[rm][10580]**
  * [Unmodified Debian Wheezy and (headless) LAMP-Server-Wheezy with prebuild XBMC][10581] by **Martin Wild**
  * [Cubieez (Debian 7.5 ARMHF with Mali400 + G2D) for A10/A20/CT][10582] by **Manel Alonso**
  * [Debian Wheezy for A10 Tablets (with sun4i-ts support)][10583] by **Guaripolo**
  * [Olimex Lime/Lime2/Micro Debian Wheezy or Jessie SD card image][10584] by **Igor Pečovnik**
  * [Olimex Lime/Lime2/Micro/Teres-I Debian Buster SD card image][10585] by **Jonas Smedegaard**
  * [The standard Debian installer][10586] running on top of [SD card based installer][10587]
  * [special purpose debian image to build digital photo frames for family and friends using open-source hardware (A20-OLinuXino-{MICRO,LIME2}+LCD‑OLinuXino‑{7,10}TS)][10588]

Most of above Debian derivatives have been customized, and strive to support specific boards / device families. 
See also: [Mainline Debian HowTo][10589]
## [Fedora][10590]
See the [Fedora][10590] page for a list of available images. 
## [Gentoo][10591]
Allwinner SoC support is part of the [Gentoo ARM Project][10592]. Various native stage3 tarballs are available from [here][10593]; you might also check out the [experimental][10594] directories (_arm_ and _arm64_) for "bleeding edge" builds. 
## Kali
  * [Kali Linux on Cubieboard][10595]
  * [Prebuild images for Cubieboard2 and other devices ][10596]

## [Linaro][10597]
  * [Ubuntu and Linaro images][10581] by **Martin Wild**
  * [Linaro desktop with 3.4 kernel for A20 EOMA68][10598] by **jm**
  * [[1]][10599] by **Ahrovan**

**Some boot images by FurryFox and 4pda team**
  * [[2]][10600] Lubuntu 12.04 Desktop 720p

## [Mer][10601]
  * [mer-test images][10602]
  * [Mer images for Improv][10603]

## openSUSE
  * openSUSE supports a variety of ARMv6/ARMv7/AArch64 targets, including some _sunxi_ devices. See [openSUSE ARM Portal][10604] and [Supported ARM boards][10605].

## [OpenWrt][10606]
See the [OpenWrt][10606] page. 
## [Parabola GNU/Linux-libre][10607]
See the [Parabola GNU/Linux-libre][10607] page. 
## Slackware
  * [ARM on Slackware][10608] supports at least one A20 device

## [Tiny Core][10609]
  * [ARMv7 Allwinner A10 official port][10610]

## [Tizen][10611]
  * Tizen:Common with Wayland and Linux-sunxi kernel 3.4 for A20-OLinuXino-MICRO: <http://bit.ly/1D8rLKe>

  * [https://wiki.tizen.org/wiki/ARM#SUNXI_.28AllWinner.29][10612]
    * file:tizen-common-wayland-arm-sunxi-20140527rzr.raw.gz
    * video: [https://www.youtube.com/watch?v=6JDy9uUqH4Y&list=UUHVSal7ifvk6Juar-FaddTQ][10613]

Related: [Tizen][10611]-Sunxi 
## [Ubuntu][10614]
  * [Armbian][10571] (build system and OS images for +30 different sunxi SBC)
  * [Mele: Ubuntu 12.10 armhf base with nand install][10615]
  * [Minimal Ubuntu 12.04.2 LTS with 3.4.29 kernel image for A13-OLinuXino][10616]
  * [MK802 Ubuntu Images][10617] by **[Miniand][10618]**
  * [Ubuntu and Linaro images][10581] by **Martin Wild**
  * [Ubuntu 13.04 Desktop Linux with 3.4 kernel for A20 EOMA68 and Cubieboard2][10619] by **jm**
  * [Ubuntu 13.04 Desktop Linux with 3D acceleration with stage 3.4 kernel for A20 EOMA68 and Cubieboard2][10620] by **jm**
  * [Olimex Lime/Lime2/Micro Ubuntu Trusty SD card image][10584] by **Igor Pečovnik**
  * [Ubuntu MATE (based on 15.04) armhf-rootfs][10621]

**Some boot images by FurryFox and 4pda team**
  * [[3]][10600] Lubuntu 12.04 Desktop 720p

# Android
Android is typically installed to the internal nand flash using LiveSuit or PhoenixCard. 
It is not easily possible to update the script.bin in LiveSuit images so you need an image for your particular device. Old android images would let the bootloader present on the nand set up memory controller so there is better chance of compatibility. 
## Cubieboard
  * [Cubieboard download page][10622] [Android][10623] TV box and testing images for LiveSuit (bottom of page) - HDMI TV output

## Generic H2+/H3 based device
  * [H3Droid][10624] is universal android 4.4.2 based on xunlong's bsp dump and tuned to work with most H2+/H3 based devices. with added bugfixes and features and normal installer. slim, fast and no need for livesuit.

# BSD derivatives
## [FreeBSD][10625]
FreeBSD for Allwinner SoCs is work in progress (currently in its early stages). Check the [FreeBSD/arm wiki page][10626]. 
## [NetBSD][10627]
The [NetBsd/evbarm][10628] port supports evaluation and prototyping boards based on the ARM architecture, including various [Allwinner][10629] CPUs. 
## OpenBSD
[OpenBSD/armv7][10630] targets various ARMv7 based systems, including A1x/A20 SoCs. As of 04/2015, Cubieboard 1+2 and pcDuino are listed as supported hardware platforms. However, this release is in development and not officially supported by OpenBSD. Some users report not being able to boot OpenBSD 5.8 release in Cubieboard 2. <http://openbsd-archive.7691.n7.nabble.com/pcDuino3-Nano-mount-root-problems-on-boot-td279382.html>
