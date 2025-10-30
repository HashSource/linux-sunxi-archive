# USB/UAS
< [USB][57026]
 
The [USB Attached SCSI][57029] protocol (UASP) is the younger/faster sibling of USB's [Bulk-Only Transport][57030] (BOT) used to access HDDs/SSDs. It was introduced as an optional part of the USB 3.0 specs but can also be used with USB 2.0 host controllers when hardware/drivers are compatible. 
## Contents
  * [1 UAS capable Allwinner SoCs][57031]
  * [2 Benefits][57032]
    * [2.1 Testing 3 different external enclosures][57033]
    * [2.2 RAID 0 benchmark][57034]
  * [3 Requirements][57035]
  * [4 UASP capable chipsets in disk enclosures][57036]
    * [4.1 OK][57037]
    * [4.2 Blacklisted / UAS disabled][57038]
    * [4.3 Status unknown][57039]
  * [5 References][57040]

## UAS capable Allwinner SoCs
This section is work in progress, adding devices known to work is welcome
  * A20
  * A64 (tested on Pine64+ with kernel 4.9, ASM1153 and JMS567)
  * H2+ (tested on Orange Pi Zero with kernel 4.9, ASM1153 and JMS567)
  * H3 (tested on Orange Pi PC with kernel 4.4.0-rc4 and JMS567)
  * H5 (tested on Orange Pi Zero 2 Plus H5 with kernel 4.13 and JMS578)

## Benefits
UASP implements more efficient disk accesses over USB compared to the older BOT mode. Regarding sequential transfers you will stay below 35 MB/s with most enclosures in BOT mode while UAS enabled enclosures get close to 40 MB/s. When accessing disks concurrently UASP should easily outperform BOT mode. 
### Testing 3 different external enclosures
The following USB-to-SATA bridges were used: 
  * ASMedia ASM1051 (USB 3.0, UASP capable but due to problems blacklisted in mainline kernel)
  * Initio INIC-1608 (USB 2.0, BOT)
  * JMicron JMS567 (USB 3.0, UASP capable)

Tests done on a Banana Pi using an "APPLE HDD HTS727550A9E362" (Hitachi 2.5" 500 GB) with kernel 4.1.2, btrfs' defaults and disabled ASM1051 blacklisting (please keep that in mind since normally UAS will be automatically disabled for ASM1051/ASM1053 devices and a fallback to BOT will happen). The following iozone settings[[1]][57041] were used (4 GB test size to ensure that disks and not buffers/caches were tested. Only for the IOPS tests I used 2 GB since otherwise it would've took ages and the results didn't vary between 2 and 4 GB): 
[code] 
    iozone -a -g 4000m -s 4000m -i 0 -i 1 -r 4K
    iozone -a -g 4000m -s 4000m -i 0 -i 1 -r 1024K
    iozone -O -i 0 -i 1 -i 2 -e -+n -r 4K -s 2000m
[/code]
Cpufreq setting as follows: 
[code] 
    echo performance >/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
    echo 960000 >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
[/code]
(Sidenote: All three controllers support SAT so you can query S.M.A.R.T. values and trigger selftests: "smartctl -d sat") 
| ASM1051 BOT | JMS567 BOT | INIC-1608 BOT | ASM1051 UASP | JMS567 UASP   
---|---|---|---|---|---  
Seq. Write  | 33.1 MB/s | 34 MB/s | 33.5 MB/s | 37.1 MB/s | 38.1 MB/s   
Seq. Read  | 34.8 MB/s | 34.8 MB/s | 37.1 MB/s | 39.8 MB/s | 40.5 MB/s   
Seq. write IOPS  | 8225 | 8301 | 8220 | 9062 | 9284   
Seq. read IOPS  | 8844 | 8816 | 8684 | 9932 | 10227   
Random write IOPS  | 176 | 178 | 125 | 157 | 166   
Random read IOPS  | 3433 | 3479 | 4106 | 4818 | 4956   
**Update Nov 2016:** Quick test with kernel 4.9, the JMS567 enclosure, a Samsung EVO 750 and btrfs: 
  * A20 (same Banana Pi as above): 38.4 MB/s write, 40.8 MB/s read
  * A64 (Pine64+): 41.7 MB/s write, 42.1 MB/s read
  * H3 (Orange Pi Plus 2E): 38.9 MB/s write, 41.3 MB/s read

### RAID 0 benchmark
Just a quick test with a [pcDuino3 Nano][57042] with kernel 4.1.1 without UASP support and 4.1.2 with CONFIG_USB_UAS=m ([details][57043]). Two RAID-0 implementations were tested: btrfs' own implementation and mdraid+ext4. Obviously performance depends heavily on disk access patterns since btrfs' RAID-0 mode shows a whopping 17 MB/sec less without UAS while mdraid+ext4 are nearly unaffected: 
**With UASP enabled (write/read in MB/sec):** btrfs: 73/75 MB/s, mdraid+ext4: 69/72 MB/s 
**Without UASP (write/read in MB/sec):** btrfs: 56/58 MB/s, mdraid+ext4: 66/67 MB/s 
## Requirements
For reliable operation it's recommended to use UASP only with mainline kernel. You've to set _CONFIG_USB_UAS=m_ or _CONFIG_USB_UAS=y_ in your kernel config and you need an USB-to-SATA bridge in your disk enclosure that implements UAS correctly (and therefore isn't blacklisted -- in the latter case an automatic fallback to BOT should happen). 
How to check whether UAS is enabled? Always check dmesg output for 'uas' vs. 'USB Mass Storage device detected' since many USB-to-SATA bridges won't be accessed using UASP (even some that would work flawlessly since it's not possible to differentiate them from their broken siblings – that applies eg. to the [widely used ASM1053][57044]). You can also check the device with 'lsusb -t'. If it shows Class=Human Interface Device for the device, UAS is not enabled. 
**Important:** if you stumble accross USB errors with UAS and see 'Ring expansion failed' messages in dmesg output check/increase the kernel's [coherent-pool memory size][57045]. 
## UASP capable chipsets in disk enclosures
This section is work in progress, please add/correct
Even if the SoC in question is only USB 2.0 capable disk enclosures that are USB 3.0 ready are worth a try since UAS capable USB-to-SATA bridge chips appeared only after the release of the USB 3.0 specs therefore you will get UASP only together with USB 3.0. Please keep in mind that USB 3.0 allows USB peripherals to demand 900 mA instead of 500 mA as with USB 2.0. Therefore 2.5" disks in an USB 3.0 enclosure might not even spin-up when used with a sunxi device plugged into an USB 2.0 port when they're bus-powered only and do not feature a second power source. 
The following list tries to sum up the UAS support state in mainline kernel for different chipsets commonly used in HDD/SSD enclosures: 
### OK
  * ASMedia ASM1053-s [[2]][57046]
  * ASMedia ASM1153 [[2]][57046] [[3]][57047] (most Seagate USB3 disks based on ASM1153 with branded firmware need various quirks)
  * Genesys Logic GL3310 [[4]][57048]
  * JMicron JMS561 [[5]][57049]
  * JMicron JMS567 [[6]][57050]
  * JMicron JMS568 [[7]][57051]
  * JMicron JMS578 [[8]][57052]
  * VIA VL711 [[9]][57053]
  * VIA VL715 [[10]][57054] / VL716 [[11]][57055] (VL716 shares product ID with VL715 since the same just with USB-C capabilities added)

### Blacklisted / UAS disabled
  * ASMedia ASM1051/ASM1051E (no or broken UASP support[[2]][57046])
  * ASMedia ASM1053 (might work but it's impossible to differentiate between ASM1051 and ASM1053 when connected over USB2.0[[2]][57046])

### Status unknown
  * Fujitsu MB86C311
  * Renesas µPD720231
  * Texas Instruments TUSB9261 [[12]][57056]
  * NS1068X 0x2537:0x1068 ([should be blacklisted][57057])
  * Newer Seagate USB3 enclosures relying on ASM1153 with branded firmware (most probably they need quirks too as those already listed in **unusual_uas.h**)

# References
  1. [↑][57058] All test results in detail [here][57059]
  2. ↑ [2.0][57060] [2.1][57061] [2.2][57062] [2.3][57063] See this [patch description][57064] regarding different ASMedia chipsets
  3. [↑][57065] [http://www.asmedia.com.tw/eng/e_show_products.php?item=132&cate_index=97][57066]
  4. [↑][57067] <http://www.genesyslogic.com/en/product_view.php?show=4>
  5. [↑][57068] <http://www.jmicron.com/PDF/brief/jms561.pdf>
  6. [↑][57069] <http://www.jmicron.com/PDF/brief/jms567.pdf>
  7. [↑][57070] <http://www.jmicron.com/PDF/brief/jms568.pdf>
  8. [↑][57071] <http://www.jmicron.com/PDF/brief/jms578.pdf>
  9. [↑][57072] <http://www.via-labs.com/product_show.php?id=44>
  10. [↑][57073] <http://www.via-labs.com/product_show.php?id=49>
  11. [↑][57074] <http://www.via-labs.com/product_show.php?id=68>
  12. [↑][57075] <http://www.ti.com/product/tusb9261>
