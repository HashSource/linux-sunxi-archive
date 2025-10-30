# Sunxi devices as NAS
The following article tries to give some hints how to build a sufficient file server or NAS ([Network-attached storage][52585]) with sunxi devices. The focus is 'classic' [LAN][52586] based file sharing using protocols like NFS, SMB or AFP and not internet or cloud optimised stuff (FTP, SFTP, SeaFile, ownCloud and the like). 
## Contents
  * [1 Requirements / which device to choose][52587]
  * [2 Limitations][52588]
    * [2.1 Architectural differences][52589]
    * [2.2 Per connection limits][52590]
    * [2.3 Network/storage not blocking each other][52591]
  * [3 Differentiation to other devices][52592]
    * [3.1 SATA and GBit capable ARM alternatives][52593]
    * [3.2 What's different on sunxi compared to common server platforms (eg. x86)][52594]
    * [3.3 When to choose another device?][52595]
  * [4 Things to consider when using USB connected storage][52596]
  * [5 Influence of the chosen OS image on NAS performance][52597]
  * [6 Performance tweaks][52598]
  * [7 Benchmarking / Identifying bottlenecks][52599]
    * [7.1 Use the right tools][52600]
    * [7.2 Identifying bottlenecks][52601]
  * [8 New opportunities with mainline kernel][52602]
  * [9 UPS mode][52603]
  * [10 Unresolved issues][52604]
  * [11 See also][52605]
  * [12 References][52606]

## Requirements / which device to choose
Three things are important for a performant NAS: 
  1. I/O bandwidth (how fast can the server access storage/disks?)
  2. Network bandwidth (how fast can clients access the server?)
  3. CPU horsepower (is the server able to deliver all accessing clients at maximum speed?)

For normal NAS use cases the first 2 requirements are more important. Some Allwinner SoCs feature a [SATA][52607] port in addition to their USB ports, some provide 10/100 Mbits/sec [EMAC][52608] Ethernet and some even Gbit Ethernet ([GMAC][52609]). Since the [A20][52610] and [R40][52611] are the only SoC capable of both SATA and GMAC (see the [comparison of different sunxi SoCs][52612]) they're the most interesting choices for a NAS. And while the [A80][52613] would also be a great choice due to one USB 3.0 port Linux support for this SoC is still very limited. 
Since not every A20 based sunxi device uses GMAC networking (or even Ethernet at all) the following devices are the best choices: [A20-OLinuXino-Lime2][52614], [Banana Pi][52615], [Banana Pro][52616] or [Banana Pi M1+][52617], [Banana Pi M2 Ultra][52618], [Cubietruck][52619], [Hummingbird A20][52620], [Lamobo R1][52621], [Orange Pi][52622], [Orange Pi Mini][52623] or [pcDuino3 Nano (Lite)][52624]. 
[![Exclamation.png][52625]][52626] **Beware** : Recently sunxi devices appear that are advertised as being "SATA capable", but simply use an USB-to-SATA bridge (BPi M3 even behind an internal USB hub), which has both massive performance and functionality implications. For example, [Banana Pi M3][52627], [Cubietech Cubietruck Plus][52628] and [Orange Pi Plus][52629] aren't listed here because their SoCs ([H3][52630]/[A83T][52631]/[H8][52632]) no longer support SATA directly, and the onboard USB-to-SATA bridge used on all three devices (GL830) is horribly slow. 
## Limitations
### Architectural differences
Unlike dedicated server platforms with plenty of CPU horsepower and server features (eg. network adapters with [TCP offload engine][52633]) CPU performance/behaviour on sunxi devices always directly affects network/NAS performance. A feature called [CPU frequency scaling][52634] is responsible for adjusting CPU clock speeds according to needs. In case you use the wrong cpufreq settings it's impossible to achieve decent NAS performance (compare with [SATA performance influences][52635]). 
### Per connection limits
  * Wi-Fi: Don't trust in marketing numbers like _300 Mbps_ since reality differs much and Wi-Fi uses a shared medium (the more devices use the same frequency bands the less bandwidth available)
  * Ethernet: different GMAC capable sunxi devices perform different for yet unknown reasons (see [comparison of devices][52636])
  * SD Card: limited to max. 22-23 MB/s sequential speed with mainline kernel, random I/O differs heavily and is only dependant on the SD card in use
  * SATA: max. 45/200 MB/s with some tweaking (see [SATA performance influences][52635])
  * USB: 3 independant USB ports each capable of max. 30-35 MB/s. When used concurrently total bandwidth is able to reach or even slightly exceed 100 MB/s

### Network/storage not blocking each other
On A10/A20/R40 devices Ethernet, SATA and the 3 USB ports are all connected directly to the SoC and do not have to share bandwidth between (but you will find some devices where this restriction applies to USB connected onboard Wi-Fi). This is a real advantage compared to many other ARM devices where 2 or more of these ports are behind a single USB connection. Compare with every model of Raspberry Pi for example: only one single connection exists between SoC and an internal USB hub with integrated Ethernet controller ([LAN9512][52637]/[LAN9514][52638]). All expansions ports share the bandwidth of this single USB 2.0 connection. 
## Differentiation to other devices
### SATA and GBit capable ARM alternatives
There are 3 other affordable ARM SoC families available that also feature SATA, GBit Ethernet and even PCIe. Since these focus on different market segments they're way more expensive than Allwinner SoCs: 
  * Marvell [Kirkwood][52639]/[Armada][52640] (used mainly in NAS boxes, recent models show excellent disk/network performance even when used concurrently, hardware accelerated crypto engine _CESA_)
  * [i.MX6][52641] (used mainly in industrial applications and also some SBC, SATA performance 90/100 MB/s write/read, [Gbit Ethernet throughput limited to approx. 400 Mbits/sec][52642], hardware accelerated crypto engine _CAAM_)
  * Annapurna Labs' [Alpine SoCs][52643] (used by several NAS vendors and internally at Amazon in their data centers)

In the meantime also 64-bit ARM SoCs are available that do not only have a single SATA port and GBit Ethernet but that are able to access a couple of disks, provide 10 GbE Ethernet, several PCIe 3.0 lanes and use ECC RAM (eg. [AMD's A1100][52644]). But they're in a different league regarding price, too. 
An in-depth comparison of A20, i.MX6 quad and Marvell ARMADA 38x storage performance can be found [in Armbian forum testing through 3 SSD and 2 HDD][52645]. 
### What's different on sunxi compared to common server platforms (eg. x86)
  * CPU clock speeds always directly influence I/O and network bandwidth
  * Due to the limited CPU power even light workloads might heavily decrease NAS performance
  * The RTL8211 mainly used with A20/R40 GMAC works in a different mode than normal: only used as [PHY][52646] for the SoC's internal [MAC][52647] implementation and not combining MAC/PHY in a PCIe attached network adapter but --> different drivers, different features (no [WoL][52648] for example)
  * No ECC RAM available --> high(er) risk of [Bit rotting][52649]

### When to choose another device?
  * Need for transparent filesystem encryption (Allwinner's crypto engine seems to be slow/buggy and the CPU cores aren't that fast)
  * Need for more than 1 SATA port ([port multipliers are unrealiable][52650])
  * Need for _data integrity_ (not possible without ECC RAM[[1]][52651])

To be fair: the last two issues apply to nearly all cheap NAS boxes also. 
## Things to consider when using USB connected storage
USB connected disks are slower than expected (480 Mbps) due to protocol overhead (compare with [8b/10b encoding][52652]) and the inefficient [BOT mode][52653]. If you're using mainline kernel, configured it accordingly and your USB device is [USB Attached SCSI][52654] capable (an optional feature introduced with USB 3.0 that not only improves sequential transfer speeds but especially random I/O) only the first limitation applies. Some USB storage controllers don't work well with multiple concurrent I/O requests, see e.g. [this blog][52655]. 
When using BOT mode you won't be able to exceed 30 MB/s when accessing a disk connected to a single USB port (maybe 35 MB/s after extensive tuning). Using UASP it is possible to get close to 40 MB/s. Multiple disks on the same USB bus will not only have to share the available bandwidth but tend to partially block each other so overall bandwidth will be a bit lower when concurrent disk accesses happen. 
When using USB attached disks it's important to use an enclosure/adapter that is capable of [SCSI / ATA Translation][52656] (otherwise you won't be able to monitor drive health since no [S.M.A.R.T.][52657] data can be accessed and no S.M.A.R.T. selftests can be triggered) 
## Influence of the chosen OS image on NAS performance
Most of the manufacturer supplied OS images for your sunxi device didn't have NAS but instead desktop/GUI useage in mind. This might have some severe implications on achievable fileserver performance. In the following we'll have a look at an extreme example: from all A20 devices tested so far the Banana Pi is able to achieve the highest network throughput: 940/750 Mbits/sec RX/TX measured with iperf, therefore combined SATA/network performance is able to reach 44/72 MB/s (in client -> server direction A20's slow SATA write performance is the bottleneck and responsible for just 44 MB/s and in server -> client direction the slower TX Ethernet throughput limits) 
When using a desktop oriented OS image from the manufacturer (featuring an old sunxi 3.4 kernel, ARMv6 libs/userland and some unfavourable settings) performance dropped drastically with distro defaults: just 650/400 Mbits/sec RX/TX with iperf and 27.5/44.5 MB/s combined SATA/network. That's a whopping ~38 percent less compared to the maximum achievable with mainline kernel and NAS optimised settings. For details refer to this ["Raspbian vs. Armbian" thread][52658]. 
This does not just apply to OS images for Banana Pi but to most GUI oriented OS images manufacturers provide. In case you experience bad server performance check [possible performance tweaks][52598] and if that does not help be prepared to build your own u-boot/kernel or switch to a headless distro that takes care of optimised server settings (eg. [Armbian][52659], a Debian based distro that supports all of the recommended A20 devices except of the Hummingbird). 
## Performance tweaks
  * Check [general performance optimisation advises][52660], especially if your rootfs (/tmp and /var/log) is on a slow SD card
  * Adjust [CPU frequency scaling settings][52661] accordingly (eg. use _ondemand_ always togehter with _io_is_busy_)
  * Run the device headless or set the framebuffer's resolution, depth and refresh rate to a minimum ([increases memory bandwidth][52662])
  * Avoid memory reservations for GPUs since on all sunxi devices CPU and GPU cores have to share memory.
  * Assign eth0 IRQs to cpu1 since irqbalancing neither works on sunxi/ARM nor increases performance when used with network interrupts
  * check out different I/O schedulers (can be set and read out using _/sys/block/sda/queue/scheduler_). On sunxi _deadline_ seems to be the most performant
  * Use Mainline kernel and mainline U-Boot
  * When using Mainline kernel consider using a modern filesystem like btrfs with transparent file compression[[2]][52663]
  * Choose a device with more available DRAM if you experience memory shortages (the [Cubietruck][52619] is available with 2GiB RAM)
  * Do some TCP/IP stack tuning to adjust parameters for GBit Ethernet (especially increasing buffer sizes and queue lenghts)
  * Adjust application settings accordingly (eg. using Samba search for tuning guides and edit the contents of smb.conf)

## Benchmarking / Identifying bottlenecks
Always test from bottom to top (local disk performance, network performance, combined network/disk performance). Always have an eye on CPU utilisation especially when you're using only a single/dual core SoC. Consider switching temporarely to the _performance_ cpufreq governor to avoid random test results and false conclusions. 
### Use the right tools
People experienced with SBCs normally use completely different – and mostly inappropriate – tools/methods to measure I/O and network performance compared to server professionals that do this for a living. Due to this you'll find many questionable benchmark results on the net regardings SBCs as servers. Always check the test methodology used. 
Tools/methods that definitely lead to wrong results/assumptions: 
  * _dd_ with small filesizes and without approriate flags (testing mainly buffers/caches and therefore RAM not disk)
  * _time cp $src $dst_ (same problem as with _dd_ above)
  * _hdparm -tT_ (tampering disk throughput with memory bandwidth)
  * wget/curl downloads from somewhere (many random unrelated influences on both sides of the network connection **and** in between)
  * scp/SFTP (random results based on SSH ciphers negotiated between client and server[[3]][52664])

Use [IOzone, bonnie++, IOmeter and the like][52665] with large filesizes (at least twice as much as RAM available) and also test random I/O and not just only sequential transfers. Use network tools that don't tamper network throughput with other stuff like disk performance on one or both sides of the network connection (use [iperf/netperf and the like][52666]). When you're done testing individually always do a combined test using both synthetic benchmarks and real-world tasks (eg. copying a couple of small and afterwards a really large file between client and sunxi NAS. Always test both directions and keep in mind that copying many small files over the network is always slower than one big file, that in turn might be slower than a few large files transferred in a batch[[4]][52667]) 
### Identifying bottlenecks
  * iostat 5
  * htop
  * dstat -clnv --fs --vm --top-bio --top-cpu --top-io

Don't let you fool by platitudes. More CPU horsepower isn't always the key to more performance. Always check _%user_ , _%nice_ and _%system_ individually when you experience performance problems. And keep in mind that _%iowait_ is one key to understand when you're running in I/O bottlenecks[[5]][52668]
## New opportunities with mainline kernel
If a sunxi SoC is already supported by mainline kernel then USB gets interesting to be used for NAS use cases as well. That's due to 
  * the ability to benefit from [USB Attached SCSI][52669] resulting in USB performance close to 40 MB/s (tested with A20, H2+ and H3)
  * the ability to use [btrfs][52670], a modern mixture between filesystem and volume manager

You don't want to use btrfs with outdated kernel versions since nearly all the code lives inside the kernel and tons of bugs have been fixed in the meantime. And while btrfs is also the filesystem of choice when using SATA a few features make it especially useful when combined with USB: 
  * "End-to-end data integrity" through checksumming. Even if you use USB-to-SATA bridges that do not support [SAT][52671] to be able to query the drive's health directly btrfs can detect data corruption (or correct it when using redundancy). When you do regular [_scrubbing_][52672] btrfs can act as an early warning system even if the disk can not be queried through S.M.A.R.T.
  * Transparent filesystem compression: Using appropriate algorithms like LZO/LZ4 the data written to disks needs less space and more importantly: throughput increases. If your data can be compressed by 15% and USB throughput is limited to 40 MB/s you end up with transfer rates of ~46 MB/s. The costs are a slight increase in CPU utilisation unless you choose the wrong compression algorithm: zlib with high compression settings will slow I/O down massively.
  * Flexible RAID modes: btrfs implements different levels of redundancy and can also stripe data across media to increase performance. You can even combine both modes (striping data while mirroring metadata to get a clue when data corruption occured) and some modes work differently than normal: btrfs' RAID-1 implementation when used with 3 or more disks for example doesn't store the same data on every disk but "2 copies of all the data on different devices" instead. This way you can use 3 disks of _different_ size, combine them to a RAID-1, get full redundancy and end up with a total capacity of all the disks divided by two ([not exactly][52673]).
  * Unlimited number of [snapshots][52674] and the ability to send snapshots incrementally to another disk/machine. Snapshots are available with LVM and other filesystems already but if you create too many a severe performance degradation occurs. With btrfs this limitation doesn't exist any more and you've the ability to send snapshots (that means: Only blocks that have been changed between the current and the last snapshot) incrementally to another disk or host with 'btrfs send/receive'.

You get a couple of other interesting features with btrfs also (copy on write, deduplication, quota support for subvolumes) but the few above are the most interesting ones for multi-core sunxi devices especially when equipped with a few independent storage buses (like the A20 for example: 1 x SATA + 3 x USB 2.0. Or H3/H5 with 4 x USB 2.0). 
If you've an A20 board or an H3/H5 board with all 4 USB ports directly exposed (no internal USB hub!) you might connect 4 disks of equal size, configure them as RAID-10 (a striped mirror of 2 disks) and end up with full redundancy and sequential transfer speeds of ~80 MB/s (to be confirmed whether the SoC's internal bandwidth can cope with that). In case you've 3 disks (1 TB, 2 TB and 3 TB) you can create a RAID-1 and end up with full redundancy and a useable capacity of 3 TB. 
The combination of btrfs' checksumming, snapshots and 'btrfs send/receive' is also perfect to create [backups][52675] without much efforts. Given you have 2 disks of equal size connected to an A20 or R40 device. Connect one to the SATA bus with no compression and share this to the outside and use the other on USB with maximum zlib compression for snapshots. You can then create hourly snapshots on the SATA disk, transfer them incrementally to the USB disk, delete them afterwards on the SATA disk but keep every hourly snapshot on the USB disk (given your data is compressible). In the evening a script would then send the last hourly snapshot incrementally to a second location (be it in a different fire area or somewhere else on the planet through VPN). The send/receive feature will always only transfer the differences without scanning the filesystems at source and destination again like rsync would've to do for example to achieve the same. 
While btrfs also has its downsides (calculation of real disk useage if you make use of compression, deduplication and snapshots for example) it's a great opportunity when being able to use mainline kernel. UAS is responsible for a speed boost when you carefully choose the USB-to-SATA bridge ([should not only support UAS][52676] but SAT too to be able to use S.M.A.R.T.) and combined with btrfs' compression feature it accelerates disk access even more. And being able to fight 'bit rotting' to some extent (impossible without ECC-RAM) based on btrfs' checksumming is always great. 
Now only devices are missing. The few A20 boards mentioned on the top of the page are great but lack a bit CPU power when you want to make heavy use of filesystem compression. R40 based boards perform here way better due to being quad-core. Or the few H3/H5 boards that feature GbE and expose all 4 USB ports directly: [Orange Pi Plus 2E][52677], [Orange_Pi_PC_2][52678] or the upcoming [NanoPi M1 Plus][52679]. 
## UPS mode
The [A20-OLinuXino-Lime2][52614] and the [Lamobo R1][52621] when used together with 2.5" SATA disks provide _Uninterruptible power supply_ capabilities since on these two boards the 5V SATA power connector is fed through the AXP209 PMU and a DC-DC step-up converter. In case these boards are running on battery a connected disk will still be powered (applies also to all other LIME/LIME2/MICRO boards from Olimex). Unfortunately that's not the case with most other A20 boards since there the SATA power connector is directly connected to DC-IN therefore in case of a power outage the disk simply shuts off. 
## Unresolved issues
  * Slow SATA write performance (if this problem could be solved A20 based devices would be able to easily outperform most cheap GBit capable NAS)
  * GMAC settings (where do the variations in RX direction origin from?)
  * slow Lamobo R1 performance (maybe due to b53 driver quirks?)

# See also
  * [Some storage benchmarks on SBCs @ Armbian forums][52680]
  * [Cubieboard/HDD ][52681]

# References
  1. [↑][52682] The [most comprehensive study on this subject so far][52683] sums it up: "For example, we observe DRAM error rates that are orders of magnitude higher than previously reported, with FIT rates (failures in time per billion device hours) of 25,000 to 70,000 per Mbit and more than 8% of DIMMs affected per year."
  2. [↑][52684] [Btrfs' Transparent file compression][52685] trades CPU cycles for more I/O bandwidth which increases througput with uncompressed files. Using a fast algorithm like lzo/LZ4 might even help on slow devices to overcome slow disk access (USB in general, SATA writes)
  3. [↑][52686] When a SSH/scp/SFTP connection is established client and server try to negotiate dynamically a SSH cipher both sides support. When a strong cipher has been chosen performance will decrease dramatically since on sunxi devices then the CPU becomes the bottleneck, eg. [AES128/256 will take twice as long as arcfour][52687]
  4. [↑][52688] File managers like Windows' Explorer use some tricks to gain extra throughput therefore synthetic benchmarks might tell a different story (see this [in-depth explanation][52689])
  5. [↑][52690] For a basic understanding of the _%user_ , _%nice_ , _%system_ , _%idle_ and _%iowait_ meanings you'll have to dig a bit into Linux performance monitoring (eg. using [this overview][52691])
